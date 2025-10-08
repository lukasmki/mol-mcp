from typing import Self, Union, List

from rdkit.Chem import (
    DeleteSubstructs,
    Mol,
    MolFromSmarts,
    MolFromSmiles,
    MolToSmiles,
    ReplaceSubstructs,
)
from rdkit.Chem.Descriptors import CalcMolDescriptors
from rdkit.Chem.rdChemReactions import ChemicalReaction, ReactionFromSmarts
from rdkit.Chem.rdFMCS import FindMCS


class SMILES:
    def __init__(self, smiles: Union[str, Mol, List[Union[str, Mol]]]):
        if not isinstance(smiles, list):
            smiles = smiles.split(".")
        self.mol: list[Mol] = [self._convert_to_mol(s) for s in smiles]

    def _convert_to_mol(self, smiles: Union[str, Mol]):
        if isinstance(smiles, Mol):
            return smiles
        elif isinstance(smiles, str):
            m = MolFromSmiles(smiles, sanitize=True, replacements={})
            if not m:
                raise Exception(f"Parsing of smiles='{smiles}' failed.")
            return m
        else:
            raise ValueError(f"Input type '{type(smiles).__name__}' not Mol or str.")

    def __repr__(self):
        return ".".join([MolToSmiles(m) for m in self.mol])

    def __str__(self):
        return ".".join([MolToSmiles(m) for m in self.mol])

    def __add__(self, other):
        if isinstance(other, SMILES):
            self.mol.extend(other.mol)
            return self
        elif isinstance(other, (str, list)):
            return self + SMILES(other)
        raise TypeError(
            f"Unsupported operand type(s) for +: 'SMILES' and {type(other).__name__}"
        )

    @property
    def description(self) -> dict[str, float]:
        return CalcMolDescriptors(MolFromSmiles(str(self)))

    @property
    def max_common_substructure(self) -> dict:
        result = FindMCS(self.mol)
        return {
            "success": str(not result.canceled),
            "smarts": result.smartsString,
        }

    def has_substructure(self, target_smarts: str) -> bool:
        target = MolFromSmarts(target_smarts)
        if not target:
            raise Exception(f"Parsing of target_smarts='{target_smarts}' failed.")
        return any(mol.HasSubstructMatch(target) for mol in self.mol)

    def remove(self, target_smarts: str) -> Self:
        target = MolFromSmarts(target_smarts)
        if not target:
            raise Exception(f"Parsing of target_smarts='{target_smarts}' failed.")

        self.mol = [DeleteSubstructs(mol, target, onlyFrags=False) for mol in self.mol]
        self.mol = [mol for mol in self.mol if mol.GetNumAtoms() > 0]
        return self

    def replace(self, target_smarts: str, fragment_smarts: str) -> Self:
        target = MolFromSmarts(target_smarts)
        if not target:
            raise Exception(f"Parsing of target_smarts='{target_smarts}' failed.")
        fragment = MolFromSmarts(fragment_smarts)
        if not fragment:
            raise Exception(f"Parsing of fragment_smarts='{fragment_smarts}' failed.")
        self.mol = [
            ReplaceSubstructs(mol, target, fragment, replaceAll=True)[0]
            for mol in self.mol
        ]
        return self

    def add(self, smiles: str | Mol | list[str | Mol]) -> Self:
        if not isinstance(smiles, list):
            smiles = smiles.split(".")
        self.mol += [self._convert_to_mol(s) for s in smiles]
        return self

    def react(self, reaction_smarts: str) -> Self:
        reaction: ChemicalReaction = ReactionFromSmarts(reaction_smarts)
        if not reaction:
            raise Exception(f"Pasing of reaction_smarts='{reaction_smarts}' failed.")
        products = reaction.RunReactants(self.mol)
        if not products:
            return self
        self.mol = list({MolToSmiles(m) for p in products for m in p})
        self.mol = [self._convert_to_mol(m) for m in self.mol]
        return self


if __name__ == "__main__":
    m = MolFromSmiles("c1ccccc1.CO", sanitize=True, replacements={})
    print(CalcMolDescriptors(m))

    print(SMILES("CC(=O)(O)").has_substructure("[OX1]"))  # True
    print(SMILES("CC(=O)(O)").remove("[OX1]"))  # CCO
    print(SMILES("CC(=O)(O)").replace("[OX1]", "[O]"))  # CC(=O)O
    print(SMILES("CC(=O)(O)").add("CNC"))  # CC(=O)O.CNC
    print(
        SMILES("CC(=O)O").add("CNC").react("[C:1](=[O:2])O.[N:3]>>[C:1](=[O:2])[N:3]")
    )  # CC(=O)N(C)C

    print(
        SMILES(["Oc1ccc(N(=O)=O)cc1", "Oc1ccc(N)cc1"]).max_common_substructure
    )  # {'success': True, 'smarts': '[#8]-[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#7]'}
    print(
        SMILES(["Oc1ccc(N(=O)=O)cc1", "Oc1ccc(N)cc1"]).remove(
            "[#8]-[#6]1:[#6]:[#6]:[#6](:[#6]:[#6]:1)-[#7]"
        )
    )  # O=[N+]([O-])c1ccc(O)cc1

    print(
        SMILES("C(=O)OC(=O)O")
        .add("CNC")
        .react("[C:1](=[O:2])O.[N:3]>>[C:1](=[O:2])[N:3]")
    )  # CN(C)C=O.CN(C)C(=O)O.CN(C)C(=O)OC=O

    a = SMILES("C(=O)(O)C(=O)(O)")
    print(a)  # O=C(O)C(=O)O
    a.add("CNC")
    print(a)  # O=C(O)C(=O)O.CNC
    a.react("[C:1](=[O:2])O.[N:3]>>[C:1](=[O:2])[N:3]")
    print(a)  # CN(C)C(=O)C(=O)O

    # print(SMILES("CC(=O)(O)").description)
