from tempfile import gettempdir

from fastmcp import FastMCP

from molmcp.tools.filesystem.roots import RootsManager


mgr = RootsManager(gettempdir())
mcp = FastMCP(
    "Filesystem",
    instructions="Provides tools for interacting with the filesystem in allowed directories",
)
