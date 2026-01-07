from typing import Annotated, Optional, Self
from pydantic import BaseModel

# type aliases
type SmilesStr = Annotated[str, "SMILES"]
type SmartsStr = Annotated[str, "SMARTS"]
type ChemicalIdentifier = Annotated[
    str,
    "Name",
    "IUPAC Name",
    "Chemical Formula",
    "Standard InChI",
    "Standard InChIKey",
    "CAS Registry Number",
]


class Status(BaseModel):
    success: bool
    message: Optional[str]


class File(BaseModel):
    path: str
    content: Optional[str]


class Directory(BaseModel):
    path: str
    children: Optional[list[Self | File]]
