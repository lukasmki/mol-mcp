from typing import Any
from fastmcp import FastMCP
from .tools import register_tools

mcp: FastMCP[Any] = FastMCP(
    name="SMILES",
    instructions="Tools for manipulating SMILES strings and applying SMARTS patterns",
)
register_tools(mcp)


def main():
    mcp.run()
