import asyncio
from fastmcp import FastMCP
from molmcp.tools.smileymcp import smiley_mcp
from molmcp.tools.qcmcp import qc_mcp


mcp = FastMCP(
    name="MolMCP",
    instructions="Toolkit for computational chemistry operations",
)


async def setup():
    await mcp.import_server(smiley_mcp, prefix="SMILES")
    # await mcp.import_server(qc_mcp, prefix="QC")


try:
    loop = asyncio.get_running_loop()
    asyncio.ensure_future(setup(), loop=loop)
except RuntimeError:
    asyncio.run(setup())


async def show_tools():
    tools = await mcp.get_tools()
    print(f"\n📋 Available tools ({len(tools)}):")
    for name in sorted(tools.keys()):
        print(f"  - {name}")


asyncio.run(show_tools())


def main():
    mcp.run()
