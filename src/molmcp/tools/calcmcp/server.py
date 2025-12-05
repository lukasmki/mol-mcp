from fastmcp import FastMCP
from .tools import register_tools

calc_mcp = FastMCP(
    "CALC",
    instructions="Tools for running singlepoint and molecular dynamics calculations using xTB",
)
register_tools(calc_mcp)


def main():
    calc_mcp.run()
