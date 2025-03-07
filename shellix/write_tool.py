from langchain_core.tools import tool
from shellix.memory import memory

@tool
def write_file(file_name: str, file_content: str) -> bool:
    """Writes full content to a file, please note that the full file content has to be provided."""
    print(f"Writing {file_name}...")
    with open(file_name, "w") as f:
        f.write(file_content)
    memory.append(
        {"role": "assistant", "content": f"Tool call, write_file: {file_name}"})
    return f"{file_name} written successfully"


@tool
def modify_file(file_name: str, substring_search: str, replacement: str) -> str:
    """Use to modify a part of file. Finds a specific substring in a file and replaces it with another string."""
    print(f"Modifying {file_name} Searching for '{substring_search}'...")
    try:
        with open(file_name, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return f"File {file_name} not found."

    occurrences = content.count(substring_search)
    if occurrences == 0:
        print(f"Substring '{substring_search}' not found in {file_name}.")
        return "No occurrences found to replace."
    elif occurrences > 1:
        print(f"More than one occurrence of '{substring_search}' found in {file_name}. Clarify search.")
        return "Error: More than one occurrence found. Clarify search."

    modified_content = content.replace(substring_search, replacement)
    with open(file_name, "w") as f:
        f.write(modified_content)
    memory.append(
        {"role": "assistant",
         "content": f"Tool call, modify_file: {file_name} Substring: {substring_search} Replacement: {replacement[0:255]}.."})
    print(f"Replaced '{substring_search}' with '{replacement}' in {file_name}.")
    return f"Replaced '{substring_search}' with '{replacement}' in {file_name}."

def read_file(file_name: str) -> str:
    """Reads the full content of a file."""
    print(f"Reading {file_name}...")
    with open(file_name, "r") as f:
        content = f.read()
    return content
