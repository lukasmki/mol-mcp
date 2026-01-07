import json
from typing import Any
from urllib import parse, request
from urllib.error import HTTPError

from fastmcp import FastMCP

from molmcp.core.types import ChemicalIdentifier, SmartsStr, SmilesStr

from .smileslib import SMILES


def register_tools(mcp: FastMCP[Any]):
    @mcp.tool
    def retrieve(chemical_identifier: ChemicalIdentifier) -> SmilesStr:
        """Retrieves a SMILES string from any non-SMILES chemical identifier"""
        try:  # catch valid smiles
            return str(SMILES(chemical_identifier))
        except Exception:
            try:
                url = f"http://cactus.nci.nih.gov/chemical/structure/{parse.quote(chemical_identifier)}/smiles"
                return request.urlopen(url).read().decode("utf8")
            except HTTPError:
                raise LookupError(
                    f"SMILES query failed for chemical_identifier=`{chemical_identifier}` with url=`{url}`"
                )

    @mcp.tool
    def info(smiles: SmilesStr) -> str:
        "Return JSON formatted descriptors for a SMILES"
        return json.dumps(SMILES(smiles).description, indent=2)

    @mcp.tool
    def has_substructure(mol: SmilesStr, target_smarts: SmartsStr) -> bool:
        "Check if SMILES contains SMARTS pattern substructure"
        return SMILES(mol).has_substructure(target_smarts)

    @mcp.tool
    def max_common_substructure(mols: list[SmilesStr]) -> dict:
        "Find maximum common substructure between SMILES"
        return SMILES(mols).max_common_substructure

    @mcp.tool
    def remove(mol: SmilesStr, target_smarts: SmartsStr) -> SmilesStr:
        "Remove SMARTS pattern from a SMILES"
        return str(SMILES(mol).remove(target_smarts))

    @mcp.tool
    def replace(
        mol: SmilesStr, target_smarts: SmartsStr, replacement_smarts: SmartsStr
    ) -> SmilesStr:
        "Replace SMARTS pattern in a SMILES"
        return str(SMILES(mol).replace(target_smarts, replacement_smarts))

    @mcp.tool
    def react(mol: SmilesStr, reaction_smarts: SmartsStr) -> SmilesStr:
        "Apply a reaction SMARTS to a SMILES"
        return str(SMILES(mol).react(reaction_smarts))
