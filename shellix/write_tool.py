from langchain_core.tools import tool


@tool
def write_file(file_name: str, file_content: str) -> bool:
    """Writes content to a file, please note that the full file content has to be provided."""
    print(f"Writing {file_name}...")
    with open(file_name, "w") as f:
        f.write(file_content)
    return f"{file_name} written successfully"

@tool
def modify_file(file_name: str, substring_search: str, lines_to_remove: int, replacement_snippet: str) -> str:
    """Finds a specific substring in a file, removes that line, removes the specified number of lines after it, and replaces it with new content. Please note that you should add spaces/tabs to match content."""
    print(f"Modifying {file_name} searching for {substring_search}...")
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            lines = f.readlines()

        updated_lines = []
        i = 0
        while i < len(lines):
            if substring_search in lines[i]:
                i += 1 + lines_to_remove
                updated_lines.append(replacement_snippet + "\n")
            else:
                updated_lines.append(lines[i])
                i += 1

        with open(file_name, "w", encoding="utf-8") as f:
            f.writelines(updated_lines)

        return f"{file_name} modified successfully"
    except Exception as e:
        return f"Error modifying file: {e}"
