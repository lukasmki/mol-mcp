from io import StringIO
from ase import Atoms, io
from rdkit import Chem

from typing import Any, Annotated, Literal
from fastmcp import FastMCP

from .geometry import geometry_optimize, geometry_from_smiles


def register_tools(mcp: FastMCP[Any]):
    @mcp.tool
    def optimize(
        input_file: Annotated[str, "URI to coordinates input file"],
        output_file: Annotated[str, "URI to coordinate output file"],
    ) -> dict:
        """Optimize the input geometry using xTB"""
        atoms = io.read(input_file, index=0)

        log = StringIO()
        success, atoms = geometry_optimize(atoms, logfile=log)

        io.write(output_file, atoms)

        return {
            "success": str(success),
            "log": log.getvalue(),
        }

    @mcp.tool
    def build(
        smiles: Annotated[str, "SMILES"],
        output_file: Annotated[
            str, "URI to coordinate output file (must be within root path)"
        ],
        format: Annotated[Literal["pdb", "xyz"], "Output file format (default: pdb)"],
    ) -> dict:
        """Generates a geometry for the input SMILES"""
        mol = geometry_from_smiles(smiles)

        if format == "pdb":
            Chem.MolToPDBFile(mol, output_file)
            # ase output
        else:
            pos = mol.GetConformer().GetPositions()
            num = [a.GetAtomicNum() for a in mol.GetAtoms()]
            atoms = Atoms(numbers=num, positions=pos)
            io.write(output_file, atoms, format=format)

        return {"success": "True"}
