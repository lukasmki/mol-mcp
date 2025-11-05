from fastmcp import FastMCP
from .tools import register_tools

qc_mcp = FastMCP(
    "GEOMETRY",
    instructions="Tools for creating and manipulating geometries",
)
register_tools(qc_mcp)


def main():
    qc_mcp.run()
