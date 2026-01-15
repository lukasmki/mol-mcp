from typing import Any
from fastmcp import FastMCP
from molmcp.tools import calcmcp, qcmcp, smileymcp
from dotenv import load_dotenv

load_dotenv()

TOOLS: dict[str, FastMCP[Any]] = {
    "smiles": smileymcp.mcp,
    "geometry": qcmcp.mcp,
    "calc": calcmcp.mcp,
}
