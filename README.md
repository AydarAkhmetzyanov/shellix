# Shellix AI

Shellix is an open-source terminal AI assistant designed to enhance your command-line experience with intelligent suggestions and automation.

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
