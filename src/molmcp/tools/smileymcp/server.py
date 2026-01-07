from typing import Any
from fastmcp import FastMCP
from .tools import register_tools

smiley_mcp: FastMCP[Any] = FastMCP(
    name="SMILES",
    instructions="Tools for manipulating SMILES strings and applying SMARTS patterns",
)
register_tools(mcp=smiley_mcp)


def main():
    smiley_mcp.run()
