import os

from typing import Any
from fastmcp import FastMCP

try:
    PACKMOL_EXE = os.environ["PACKMOL_EXE"]
except KeyError:
    PACKMOL_EXE = "packmol"


def register_tools(mcp: FastMCP[Any]) -> None:
    @mcp.tool
    def run():
        pass
