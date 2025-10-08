from io import StringIO
from ase import io
from .geomopt import optimize

from . import qc_mcp


@qc_mcp.tool
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
