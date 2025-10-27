import json

from urllib import request, parse
from urllib.error import HTTPError

from typing import Any, Annotated
from fastmcp import FastMCP
from .smileslib import SMILES

type SMILESstr = Annotated[str, "SMILES"]
type SMARTSstr = Annotated[str, "SMARTS"]


def register_tools(mcp: FastMCP[Any]):
    @mcp.tool
    def retrieve(structure_identifier: str) -> SMILESstr:
        """Retrieves a SMILES string from any chemical identifier"""
        try:
            url = f"http://cactus.nci.nih.gov/chemical/structure/{parse.quote(structure_identifier)}/smiles"
            return request.urlopen(url).read().decode("utf8")
        except HTTPError:
            raise LookupError(
                f"SMILES query failed for structure_identifier=`{structure_identifier}` with url=`{url}`"
            )

    @mcp.tool
    def info(smiles: SMILESstr) -> str:
        "Return JSON formatted descriptors for a SMILES"
        return json.dumps(SMILES(smiles).description, indent=2)

    @mcp.tool
    def has_substructure(mol: SMILESstr, target_smarts: SMARTSstr) -> bool:
        "Check if SMILES contains SMARTS pattern substructure"
        return SMILES(mol).has_substructure(target_smarts)

    @mcp.tool
    def max_common_substructure(mols: list[SMILESstr]) -> dict[str, str]:
        "Find maximum common substructure between SMILES"
        return SMILES(mols).max_common_substructure

    @mcp.tool
    def add(mol_a: SMILESstr, mol_b: SMILESstr) -> SMILESstr:
        "Add SMILES together (dot-separated SMILES)"
        return str(SMILES(mol_a).add(mol_b))

    @mcp.tool
    def remove(mol: SMILESstr, target_smarts: SMARTSstr) -> SMILESstr:
        "Remove SMARTS pattern from a SMILES"
        return str(SMILES(mol).remove(target_smarts))

    @mcp.tool
    def replace(
        mol: SMILESstr, target_smarts: SMARTSstr, replacement_smarts: SMARTSstr
    ) -> SMILESstr:
        "Replace SMARTS pattern in a SMILES"
        return str(SMILES(mol).replace(target_smarts, replacement_smarts))

    @mcp.tool
    def react(mol: SMILESstr, reaction_smarts: SMARTSstr) -> SMILESstr:
        "Apply a reaction SMARTS to a SMILES"
        return str(SMILES(mol).react(reaction_smarts))
