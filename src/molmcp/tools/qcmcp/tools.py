from io import StringIO
from ase import io
from typing import Any, Annotated
from fastmcp import FastMCP

from .geomopt import optimize


def register_tools(mcp: FastMCP[Any]):

    @mcp.tool
    def geometry_optimize(input: str):
        """Optimize the input geometry using xTB"""
        atoms = io.read(StringIO(input), index=0)

        log = StringIO()
        success, atoms = optimize(atoms, logfile=log)

        output = StringIO()
        io.write(output, atoms)

        return {
            "success": success,
            "output": output.getvalue(),
            "log": log.getvalue(),
        }
