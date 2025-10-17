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

## Installation

Install `uv`

```sh
# macOS
brew install uv

# Linux/WSL2  
curl -LsSf https://astral.sh/uv/install.sh | sh
```

The `qc` mcp server depends on `tblite` and requires a Fortran compiler to complete installation.

```sh
# macOS
brew install gfortran

# Linux/WSL2
sudo apt install gfortran
```

### Easy Install with `uvx`: MCP-JSON Supporting Clients (Claude Desktop)

Add the server into your `claude_desktop_config.json`.

```json
{
    "mcpServers": {
        "MolMCP": {
            "command": "uvx",
            "args": [
                "-from",
                "git+https://github.com/lukasmki/mol-mcp",
                "mol-mcp"
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
                "mol-mcp"
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
                "mol-mcp"
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
            ]
        }
    }
}
```

For running agents as MCP servers,

```json
{
    "mcpServers": {
        "MolMCP": {
            "command": "uv",
            "args": [
                "run",
                "--project",
                "/path/to/mol-mcp",
                "python",
                "-m",
                "molmcp",
                "<name-of-agent>"
            ]
        }
    }
}
```

## Usage

### Tools

```sh
uvx --from git+https://github.com/lukasmki/mol-mcp mol-mcp
```

### Agents



## Contributing

Contributions are welcome! Please open issues or submit pull requests for bug fixes, new features, or improvements.

## License

This project is licensed under the MIT License.
