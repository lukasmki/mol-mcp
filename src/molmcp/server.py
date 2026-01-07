"""mol-mcp all the tools"""

import asyncio
from typing import Any
from fastmcp import FastMCP
from fastmcp.tools import Tool
from molmcp.tools.smileymcp import smiley_mcp
from molmcp.tools.qcmcp import qc_mcp


mcp: FastMCP[Any] = FastMCP(
    name="MolMCP",
    instructions="Toolkit for computational chemistry operations",
)


async def setup():
    await mcp.import_server(smiley_mcp, prefix="SMILES")
    await mcp.import_server(qc_mcp, prefix="GEOMETRY")


try:
    loop = asyncio.get_running_loop()
    asyncio.ensure_future(setup(), loop=loop)
except RuntimeError:
    asyncio.run(setup())


async def show_tools():
    tools: dict[str, Tool] = await mcp.get_tools()
    print(f"\n Available tools ({len(tools)}):")
    for name in tools.keys():
        print(f"  - {name}")


asyncio.run(show_tools())


def main():
    mcp.run()
