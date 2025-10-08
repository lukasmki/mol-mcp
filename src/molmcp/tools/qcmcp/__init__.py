"""MCP server for running xtb calculations"""

from fastmcp import FastMCP

qc_mcp = FastMCP(
    "QC",
    instructions="Tools for running extended tight-binding (xTB) calculations",
)


def main():
    qc_mcp.run(transport="stdio")
