from typing import Any
from fastmcp import FastMCP
from .tools import register_tools

calc_mcp: FastMCP[Any] = FastMCP(
    name="CALC",
    instructions="Tools for running singlepoint and molecular dynamics calculations using xTB",
)
register_tools(mcp=calc_mcp)


def main():
    calc_mcp.run()
