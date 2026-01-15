import sys
import asyncio
from molmcp.agents.interactive import setup_fastagent
from typing import Annotated, Any

import typer
from fastmcp import FastMCP
from rich import print

from molmcp import TOOLS

app = typer.Typer()


# mol-mcp list
@app.command(name="list", help="List MCP toolkits")
def list_tools():
    print(f"{'name':20} server")
    print(f"{'----':20} ------")
    for name, server in TOOLS.items():
        print(f"{name:20} {server.instructions}")


# mol-mcp serve <name1> <name2> ... | --list
@app.command(help="Run an MCP server")
def serve(
    tools: Annotated[list[str], typer.Argument()] = ["smiles"],
    show_list: Annotated[bool, typer.Option("--list")] = False,
):
    if show_list:
        list_tools()
        return

    async def setup_server(mcp: FastMCP[Any], tools: list[str]):
        for tool in tools:
            if tool not in TOOLS:
                raise ValueError(
                    f"Toolkit `{tool}` not found. Run `mol-mcp list` to show toolkits."
                )
            await mcp.import_server(TOOLS[tool], prefix=tool)

    async def show_tools():
        tools = await mcp.get_tools()
        print(f"\n Available tools ({len(tools)}):", file=sys.stderr)
        for name in tools.keys():
            print(f"  - {name}", file=sys.stderr)

    mcp: FastMCP[Any] = FastMCP()
    asyncio.run(setup_server(mcp, tools))
    asyncio.run(show_tools())
    mcp.run()


# mol-mcp go <name1> <name2> ... | --list
@app.command(
    help="Run an FastAgent chat",
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
)
def go(
    tools: Annotated[list[str], typer.Argument()] = ["smiles"],
    show_list: Annotated[bool, typer.Option("--list")] = False,
):
    if show_list:
        list_tools()
        return
    asyncio.run(setup_fastagent(tools)())


def main():
    app()


if __name__ == "__main__":
    app()
