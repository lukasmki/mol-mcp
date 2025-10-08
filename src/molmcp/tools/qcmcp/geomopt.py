from ase import Atoms
from tblite.ase import TBLite
from ase.optimize import FIRE2


def optimize(atoms: Atoms, logfile: str = None) -> tuple[bool, Atoms]:
    atoms.calc = TBLite(atoms, method="GFN2-xTB", verbosity=0)
    opt = FIRE2(atoms, logfile=logfile)
    converged = opt.run()
    return converged, atoms
