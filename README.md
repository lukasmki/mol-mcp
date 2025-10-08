# Mol-MCP: Computational Chemistry Interfaces for LLMs

MolMCP is a modular set of interfaces for chemistry workflows. It provides a flexible architecture for building, configuring, and running agents and tools for chemical operatations.

## Features

- Modular agent and tool system
- Extensible via configuration and plugins
- Designed for quantum chemistry and molecular computation

## Project Structure

```sh
src/
  molmcp/           # Main package
    agents/        # Example agents and configs
    tools/         # Tool implementations (qc-mcp, smiley-mcp, etc.)
tests/              # Test suite
pyproject.toml      # Project metadata and dependencies
README.md           # Project documentation
```

## Installation

The `qc` mcp server depends on `tblite` and requires a Fortran compiler to complete installation.

```sh
$ brew install gfortran
```

## Usage

### Tools

```sh
$ uv run <mcp-server>
$ uv run mol-mcp
$ uv run smiley
$ uv run qc
```

```sh
$ uvx --from /this/repo/ mol-mcp
$ uvx --from /this/repo/ smiley
$ uvx --from /this/repo/ qc
```

```sh
$ uvx --from git+https://github.com/lukasmki/mol-mcp mol-mcp
$ uvx --from git+https://github.com/lukasmki/mol-mcp smiley
$ uvx --from git+https://github.com/lukasmki/mol-mcp qc
```

### Agents



## Contributing

Contributions are welcome! Please open issues or submit pull requests for bug fixes, new features, or improvements.

## License

This project is licensed under the MIT License.
