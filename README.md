# Shellix AI

Shellix is an open-source terminal AI assistant designed to enhance your command-line experience with intelligent suggestions and automation. It leverages advanced AI models to provide context-aware assistance, making it easier to execute complex commands and automate repetitive tasks.

## Features

- **Easy to Use:** Simple command-line interface with powerful capabilities.
- **Long Research and Development Web Search:** Capable of performing extensive web searches for research and development purposes.
- **Direct Access to Project Files and System:** Offers direct access to project files and system commands for seamless integration and operation.

## Installation

To install the dependencies, run:

```bash
poetry install
```

## Usage Examples

Here are some examples of how to use Shellix:

1. **Basic Command Execution**
   ```bash
   poetry run sx "List all files in the current directory"
   ```
   This command will intelligently list all files in your current working directory.

2. **Automating Tasks**
   ```bash
   poetry run sx "Create a new Python virtual environment and install requests"
   ```
   This will automate the creation of a virtual environment and install the `requests` package.

3. **Web Search for Development**
   ```bash
   poetry run sx "Search for the latest Python 3.9 features"
   ```
   This will perform a web search and provide you with the latest features of Python 3.9.

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
