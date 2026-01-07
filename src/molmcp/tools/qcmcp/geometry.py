from typing import IO

from ase import Atoms
from ase.optimize import FIRE2
from rdkit import Chem
from rdkit.Chem import Mol
from rdkit.Chem.rdDistGeom import EmbedMolecule
from rdkit.Chem.rdForceFieldHelpers import UFFOptimizeMolecule
from tblite.ase import TBLite


def geometry_optimize(atoms: Atoms, logfile: IO | str) -> tuple[bool, Atoms]:
    atoms.calc = TBLite(atoms, method="GFN2-xTB", verbosity=0)
    opt = FIRE2(atoms, logfile=logfile)
    converged = opt.run()
    return converged, atoms


def geometry_from_smiles(smiles: str) -> Chem.Mol:
    mol: Chem.Mol = Chem.MolFromSmiles(smiles)
    mol: Mol = Chem.AddHs(mol)
    EmbedMolecule(mol)
    UFFOptimizeMolecule(mol)
    return mol
