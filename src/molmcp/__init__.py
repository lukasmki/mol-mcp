import asyncio
from fastmcp import FastMCP
from .tools.smileymcp import smiley_mcp

mcp = FastMCP(
    name="MolMCP",
    instructions="Toolkit for computational chemistry operations",
)


async def setup():
    await mcp.import_server(smiley_mcp, prefix="SMILES")


def main():
    asyncio.run(setup())
    mcp.run(transport="stdio")
