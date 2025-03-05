from langchain_core.tools import tool


@tool
def write_file(file_name: str, file_content: str) -> bool:
    """Writes content to a file, please note that the full file content has to be provided."""
    print(f"Writing {file_name}...")
    with open(file_name, "w") as f:
        f.write(file_content)
    return f"{file_name} written successfully"
