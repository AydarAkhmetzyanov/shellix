from langchain_core.tools import tool


@tool
def write_file(file_name: str, file_content: str) -> bool:
    """Writes content to a file, please note that the full file content has to be provided."""
    print(f"Writing {file_name}...")
    with open(file_name, "w") as f:
        f.write(file_content)
    return f"{file_name} written successfully"


@tool
def modify_file(file_name: str, substring_search: str, replacement: str) -> str:
    """Finds a specific substring in a file and replaces it."""
    print(f"Modifying {file_name} Searching for '{substring_search}'...")
    try:
        with open(file_name, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"File {file_name} not found.")
        return f"File {file_name} not found."

    if substring_search not in content:
        print(f"Substring '{substring_search}' not found in {file_name}.")
        return "No occurrences found to replace."

    modified_content = content.replace(substring_search, replacement)
    with open(file_name, "w") as f:
        f.write(modified_content)
    print(f"Replaced '{substring_search}' with '{replacement}' in {file_name}.")
    return f"Replaced '{substring_search}' with '{replacement}' in {file_name}."
