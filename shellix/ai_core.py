from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_community.tools import TavilySearchResults
from shellix.shell_tool import ShellTool
from shellix.write_tool import write_file, modify_file, read_file
from shellix.memory import memory, save_memory
from datetime import datetime
import json
import os

from shellix.credentials_loader import load_credentials

credentials = load_credentials()

def load_tools(credentials):
    search_tool = TavilySearchResults(
        max_results=5,
        search_depth="advanced",
        include_answer=True,
        include_raw_content=False,
        include_images=False,
        tavily_api_key=credentials['TAVILY_KEY'],
    )
    shell_tool = ShellTool()
    tools = [shell_tool, search_tool, write_file, modify_file, read_file]
    return tools


def get_directory_contents(current_directory):
    try:
        entries = os.listdir(current_directory)
        files_list = [f for f in entries if os.path.isfile(os.path.join(current_directory, f))]
        folders_list = [d for d in entries if os.path.isdir(os.path.join(current_directory, d))]
        return files_list, folders_list
    except Exception as e:
        print(f"Error accessing directory: {e}")
        return [], []

def process_input(input_str):
    memory.append({"role": "human", "content": input_str})
    current_date = datetime.now().strftime("%Y-%m-%d")
    current_directory = os.getcwd()
    folder_path = os.path.abspath(current_directory)
    files_list, folders_list = get_directory_contents(current_directory)

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", f"""
            You are a helpful console assistant called Shellix.

            Current Date: {current_date}
            Current Directory: {folder_path}
            Files in Directory: {', '.join(files_list)}
            Folders in Directory: {', '.join(folders_list)}

            Your output and tool calls to user terminal. Minimize comments in code and provide clear responses overall. 
            Think about how can you use shell or search tool to accomplish the task if you don't have information directly provided.
            When asked to do something, likely the user wants you to apply a command or modify project files. 
            Use write_file and modify_file to directly modify files instead of outputting content to user.
            Feel free to traverse the current folder with 'ls' to accomplish your tasks. Don't ask for confirmations to modify project files.
            """),
            ("placeholder", "{messages}"),
        ]
    )

    tools = load_tools(credentials)

    model = ChatOpenAI(model=credentials['OPENAI_MODEL'], temperature=0, api_key=credentials['OPENAI_KEY'],
                       streaming=True)
    langgraph_agent_executor = create_react_agent(model, tools, prompt=prompt)

    converted_memory = memory
    tool_call_count = 0
    for i in range(len(converted_memory) - 1, -1, -1):
        if converted_memory[i]['content'].startswith('Tool call'):
            tool_call_count += 1
            if tool_call_count > 5:
                del converted_memory[i]
    converted_memory = [(msg["role"], msg["content"]) for msg in memory][-20:]

    messages = langgraph_agent_executor.invoke({"messages": converted_memory + [("human", input_str)]})

    memory.append({"role": "assistant", "content": messages["messages"][-1].content})
    save_memory()
    print(messages["messages"][-1].content)
