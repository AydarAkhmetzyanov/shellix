from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from shellix.shell_tool import ShellTool

shell_tool = ShellTool()

# @tool
# def magic_function(input: int) -> int:
#     """Applies a magic function to an input."""
#     return input + 2


tools = [shell_tool]

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful console assistant called Shellix. "
                   "Your output and tool call results will be outputted to user terminal."
                   "You can creatively use the terminal commands and tools provided to you to accomplish your tasks. For example ShellTool with 'cat' to read files. "
                   "Feel free to traverse the current folder with 'ls' to accomplish your tasks."),
        ("placeholder", "{messages}"),
    ]
)


def process_input(input_str, credentials, current_directory):
    model = ChatOpenAI(model=credentials['OPENAI_MODEL'], temperature=0, api_key=credentials['OPENAI_KEY'])
    langgraph_agent_executor = create_react_agent(model, tools, prompt=prompt)

    messages = langgraph_agent_executor.invoke({"messages": [("human", input_str)]})

    return messages["messages"][-1].content
