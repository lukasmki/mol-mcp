# Mol-MCP: Computational Chemistry Interfaces for LLMs

> [!WARNING]
> This project is a work in progress! 

MolMCP is a modular set of interfaces for chemistry workflows. It provides a flexible architecture for building, configuring, and running agents and tools for chemical operatations.

## Features

- Modular agent and tool system
- Extensible via configuration and plugins
- Designed for quantum chemistry and molecular computation

## Project Structure

```sh
src/
  molmcp/           # Main package
    agents/         # Agent servers
    tools/          # Tool servers
tests/              # Test suite
pyproject.toml      # Project metadata and dependencies
README.md           # Project documentation
```

## Usage

### Tools

```sh
uvx --from git+https://github.com/lukasmki/mol-mcp mol-mcp serve --help
```

### Chat TUI

To use the built-in interactive agent with `mol-mcp` tools,

```sh
uv run mol-mcp go
```

Currently, the interactive agent is setup to use the Anthropic API. If you want to use another, take a look at the `src/molmcp/agents/interactive.py` script for an example of using fast-agent.

## Installation

Install `uv`

```sh
# macOS
brew install uv

# Linux/WSL2  
curl -LsSf https://astral.sh/uv/install.sh | sh
```

The `calc` and `geometry` servers depend on `tblite` and require a Fortran compiler to complete installation.

```sh
# macOS
brew install gfortran

# Linux/WSL2
sudo apt install gfortran
```

In your project directory, install with `uv`

```sh
uv add git+https://github.com/lukasmki/mol-mcp
```

or

```sh
uv pip install git+https://github.com/lukasmki/mol-mcp
```

You can also run it as a `uv` tool outside of a project!

```sh
uvx --from git+https://github.com/lukasmki/mol-mcp mol-mcp serve --help
```

or install it to use it anywhere

```sh
uv tool install --from git+https://github.com/lukasmki/mol-mcp
mol-mcp serve --help
```

### Easy Install with `uvx`: MCP-JSON Supporting Clients

Add the server into your MCP config:

```json
{
    "mcpServers": {
        "MolMCP": {
            "command": "uvx",
            "args": [
                "-from",
                "git+https://github.com/lukasmki/mol-mcp",
                "mol-mcp",
                "serve",
                "smiles",
                "geometry",
            ]
        }
    }
}
```

On Windows with WSL2,

```json
{
    "mcpServers": {
        "MolMCP": {
            "command": "wsl",
            "args": [
                "--shell_type",
                "login",
                "uvx",
                "-from",
                "git+https://github.com/lukasmki/mol-mcp",
                "mol-mcp",
                "serve",
                "smiles",
                "geometry",
            ]
        }
    }
}
```

### Development Install

Clone the repository.

```json
{
    "mcpServers": {
        "MolMCP": {
            "command": "uv",
            "args": [
                "run",
                "--project",
                "/path/to/mol-mcp",
                "mol-mcp",
                "serve",
                "smiles",
                "geometry",
            ]
        }
    }
}
```

On Windows with WSL2,

```json
{
    "mcpServers": {
        "MolMCP": {
            "command": "wsl",
            "args": [
                "--shell_type",
                "login",
                "uv",
                "run",
                "--project",
                "/path/to/mol-mcp",
                "mol-mcp"
                "serve",
                "smiles",
                "geometry",
            ]
        }
    }
}
```

## Contributing

Contributions are welcome! Please open issues or submit pull requests for bug fixes, new features, or improvements.

## License

This project is licensed under the MIT License.
