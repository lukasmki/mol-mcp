from typing import Any
from fastmcp import FastMCP
from .tools import register_tools

qc_mcp: FastMCP[Any] = FastMCP(
    name="GEOMETRY",
    instructions="Tools for creating and manipulating molecular geometries",
)
register_tools(mcp=qc_mcp)


def main():
    qc_mcp.run()
