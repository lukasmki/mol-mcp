from fastmcp import FastMCP
from .tools import register_tools

smiley_mcp = FastMCP(
    "SMILES",
    instructions="Tools for manipulating SMILES strings and applying SMARTS patterns",
)
register_tools(smiley_mcp)


def main():
    smiley_mcp.run()
