from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent
from langchain_community.tools import TavilySearchResults
from shellix.shell_tool import ShellTool
from shellix.write_tool import write_file, modify_file, read_file
from datetime import datetime
import os


def load_tools(credentials):
    search_tool = TavilySearchResults(
        max_results=10,
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


def process_input(input_str, credentials, current_directory):
    current_date = datetime.now().strftime("%Y-%m-%d")
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

            Your output and tool call results will be outputted to user terminal.
            Minimize comments in output code and provide clear responses overall. 
            You can creatively use the terminal commands and tools provided to you to accomplish your tasks.
            Think about how can you use shell or search tool to accomplish the task if you don't have information directly provided.
            When you asks to do something, likely user wants you to apply some command or modify project files.
            Feel free to traverse the current folder with 'ls' to accomplish your tasks.
            """),
            ("placeholder", "{messages}"),
        ]
    )

    tools = load_tools(credentials)

    model = ChatOpenAI(model=credentials['OPENAI_MODEL'], temperature=0, api_key=credentials['OPENAI_KEY'],
                       streaming=True)
    langgraph_agent_executor = create_react_agent(model, tools, prompt=prompt)
    messages = langgraph_agent_executor.invoke({"messages": [("human", input_str)]})
    print(messages["messages"][-1].content)
