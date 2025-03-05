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

1. **Automated Project Setup**
   ```bash
   poetry run sx "Initialize a new Git repository, create a Python virtual environment, and install Flask"
   ```
   This command will set up a new Git repository, create a virtual environment, and install the Flask web framework, streamlining your project initialization process.

2. **Advanced Web Research**
   ```bash
   poetry run sx "Conduct a detailed search on the latest advancements in AI and summarize the top three articles. Create CSV file with the list of summaries."
   ```
   This command will perform an extensive web search on AI advancements and provide a concise summary of the top three articles, saving you time on research.

3. **Custom Development Environment Setup**
   ```bash
   poetry run sx "Set up a development environment with Node.js, MongoDB, and VSCode extensions for JavaScript"
   ```
   This command will install Node.js, MongoDB, and configure VSCode with essential JavaScript extensions, providing a ready-to-use development environment.


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
