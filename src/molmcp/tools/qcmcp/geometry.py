from ase import Atoms
from tblite.ase import TBLite
from ase.optimize import FIRE2

from rdkit import Chem
from rdkit.Chem import AllChem


def geometry_optimize(atoms: Atoms, logfile: str = None) -> tuple[bool, Atoms]:
    atoms.calc = TBLite(atoms, method="GFN2-xTB", verbosity=0)
    opt = FIRE2(atoms, logfile=logfile)
    converged = opt.run()
    return converged, atoms


def geometry_from_smiles(smiles: str) -> Chem.Mol:
    mol: Chem.Mol = Chem.MolFromSmiles(smiles)
    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol)
    AllChem.UFFOptimizeMolecule(mol)
    return mol
