# Shellix AI

Shellix is an open-source terminal AI assistant designed to revolutionize your development workflow by providing intelligent, context-aware assistance. With direct access to your project files and system, Shellix can automate complex tasks, modify code, and streamline your development process.

## Features

- **Development Assistance:** AI-driven insights and automation for coding, debugging, and project management.
- **Web Search and Deep Research:** Perform comprehensive web searches and gather detailed insights directly from the terminal.
- **Conversation History Support:** Maintain context with conversation history, allowing for seamless interactions and follow-ups.
- **Project Status and Files Awareness:** Access and modify project files with AI assistance, ensuring up-to-date project status awareness.
- **Simple Terminal Usage:** Execute complex commands and automate tasks with simple terminal inputs.

## Installation

To install the dependencies, run:

```bash
poetry install
```

## Usage Examples

1. **Automated Project Setup**
   ```bash
   poetry run sx "Initialize a new Git repository, create a Python virtual environment, and install Flask"
   ```
   Streamline your project initialization with automated setup commands.

2. **End-to-End Web App Development**
   ```bash
   poetry run sx "Create a full-stack React application with a Node.js backend"
   ```
   This command will automate the creation of a React frontend, a Node.js backend, providing a seamless development experience.

3. **AI-Powered Code Modification**
   ```bash
   poetry run sx "Refactor the existing codebase to improve performance and readability"
   ```
   Leverage AI to analyze and refactor your code, enhancing performance and maintainability.

4. **Advanced Web Research**
   ```bash
   poetry run sx "Conduct a detailed search on the latest advancements in AI and summarize the top three articles. Create CSV file with the list of summaries."
   ```
   Save time on research with AI-driven web searches and summaries.

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
