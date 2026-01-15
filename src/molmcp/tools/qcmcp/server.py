from typing import Any
from fastmcp import FastMCP
from .tools import register_tools

mcp: FastMCP[Any] = FastMCP(
    name="GEOMETRY",
    instructions="Tools for creating and manipulating molecular geometries",
)
register_tools(mcp)


def main():
    mcp.run()
