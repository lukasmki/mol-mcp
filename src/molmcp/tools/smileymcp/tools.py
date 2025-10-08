import json

from . import smiley_mcp
from .smileslib import SMILES


@smiley_mcp.tool
def info(smiles: str) -> str:
    "Return descriptors for a SMILES"
    return json.dumps(SMILES(smiles).description, indent=2)


@smiley_mcp.tool
def has_substructure(mol: str, target_smarts: str) -> bool:
    "Check if SMILES contains SMARTS pattern substructure"
    return str(SMILES(mol).has_substructure(target_smarts))


@smiley_mcp.tool
def max_common_substructure(mols: list[str]) -> dict[str, str]:
    "Find maximum common substructure between SMILES"
    return SMILES(mols).max_common_substructure


@smiley_mcp.tool
def add(mol_a: str, mol_b: str) -> str:
    "Add SMILES together (dot-separated SMILES)"
    return str(SMILES(mol_a).add(mol_b))


@smiley_mcp.tool
def remove(mol: str, target_smarts: str) -> str:
    "Remove SMARTS pattern from a SMILES"
    return str(SMILES(mol).remove(target_smarts))


@smiley_mcp.tool
def replace(mol: str, target_smarts: str, replacement_smarts: str) -> str:
    "Replace SMARTS pattern in a SMILES"
    return str(SMILES(mol).replace(target_smarts, replacement_smarts))


@smiley_mcp.tool
def react(mol: str, reaction_smarts: str) -> str:
    "Apply a reaction SMARTS to a SMILES"
    return str(SMILES(mol).react(reaction_smarts))
