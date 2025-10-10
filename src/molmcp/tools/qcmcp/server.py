from fastmcp import FastMCP
from .tools import register_tools

qc_mcp = FastMCP(
    "QC",
    instructions="Tools for running extended tight-binding (xTB) calculations",
)
register_tools(qc_mcp)
