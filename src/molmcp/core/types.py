from typing import Annotated, Literal
from pydantic import BaseModel, ValidationError
from pydantic import field_validator

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
