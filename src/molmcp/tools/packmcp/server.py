from fastmcp import FastMCP
from .tools import register_tools

pack_mcp = FastMCP(
    "PACK",
    instructions="Tools for generating initial configurations for molecular dynamics simulations with Packmol",
)
register_tools(pack_mcp)


def main():
    pack_mcp.run()
