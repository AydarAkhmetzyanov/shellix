from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from langgraph.prebuilt import create_react_agent
from langgraph.prebuilt.chat_agent_executor import AgentState
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_community.tools import ShellTool

shell_tool = ShellTool()

#
# @tool
# def magic_function(input: int) -> int:
#     """Applies a magic function to an input."""
#     return input + 2


tools = [shell_tool]

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant."),
        ("placeholder", "{messages}"),
    ]
)



def process_input(input_str, credentials, current_directory):

    model = ChatOpenAI(model=credentials['OPENAI_MODEL'], temperature=0, api_key=credentials['OPENAI_KEY'])
    langgraph_agent_executor = create_react_agent(model, tools, prompt=prompt)

    messages = langgraph_agent_executor.invoke({"messages": [("human", input_str)]})

    return messages["messages"][-1].content
