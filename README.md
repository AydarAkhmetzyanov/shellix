# Shellix AI

Shellix is an open-source terminal AI assistant designed to enhance your command-line experience with intelligent suggestions and automation. It leverages advanced AI models to provide context-aware assistance, making it easier to execute complex commands and automate repetitive tasks.

## Features

- **Intelligent Command Suggestions:** Provides context-aware command suggestions to streamline your workflow.
- **Automation Capabilities:** Automate repetitive tasks with ease using AI-driven scripts.
- **Integration with Popular Libraries:** Utilizes libraries like `langgraph`, `langchain-openai`, and `tavily-python` for enhanced AI functionalities.
- **Easy to Use:** Simple command-line interface with powerful capabilities.
- **Customizable:** Easily extendable to fit your specific needs.
- **Long Research and Development Web Search:** Capable of performing extensive web searches for research and development purposes.
- **Direct Access to Project Files and System:** Offers direct access to project files and system commands for seamless integration and operation.

## Installation

To install the dependencies, run:

```bash
poetry install
```

## Usage

To run Shellix, use:

```bash
poetry run sx ...
```

## Updating Dependencies

To update the project dependencies, execute:

```bash
poetry update
```

## Building the Project

To build the project, use:

```bash
poetry build
```

## Publishing a New Version

To publish a new version of Shellix, follow these steps:

1. Ensure all changes are committed and the version number is updated in `pyproject.toml`.
2. Build the project:

    ```bash
    poetry build
    ```

3. Publish the package to PyPI:

    ```bash
    poetry publish
    ```

For more details, please see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Shellix is licensed under the GNU General Public License v3. See the [LICENSE](LICENSE) file for more details.
