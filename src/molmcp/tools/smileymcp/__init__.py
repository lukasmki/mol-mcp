from fastmcp import FastMCP

smiley_mcp = FastMCP(
    "SMILEY",
    instructions="Tools for manipulating SMILES strings and applying SMARTS patterns",
)


def main():
    smiley_mcp.run(transport="stdio")
