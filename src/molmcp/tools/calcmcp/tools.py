from io import StringIO
from pydantic import BaseModel

from typing import Any, Annotated, Literal, Optional
from fastmcp import FastMCP

from ase import io, Atoms
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from tblite.ase import TBLite

from molmcp.core.types import Status


class SinglepointSchema(BaseModel):
    input_path: Annotated[str, "Path to geometry file"]
    input_index: Annotated[int, "Index of the geometry in input file"] = -1
    method: Literal["GFN2-xTB", "GFN1-xTB", "IPEA1-xTB"] = "GFN2-xTB"


class MolecularDynamicsSchema(SinglepointSchema):
    output_path: Optional[Annotated[str, "Path to output geometry file"]]
    num_steps: Annotated[int, "Number of molecular dynamics steps"]
    timestep: Annotated[int, "Timestep of simulation in femtoseconds"]
    output_freq: Annotated[
        int, "Interval to output frames from MD (ignored if output_path is not given)"
    ]
    log_freq: Annotated[int, "Interval to output logging information from MD run"]
    initialize_vel: Annotated[
        bool, "Initialize atom velocities from Maxwell-Boltzmann distribution"
    ]
    temperature_vel: Optional[
        Annotated[
            float,
            "Temperature to initialize atom velocities in Kelvin (ignored if initialize_vel is false)",
        ]
    ]


class NVTSchema(MolecularDynamicsSchema):
    temperature: Annotated[float, "Temperature in Kelvin"]
    friction: Annotated[float, "Langevin friction in inverse femtoseconds"]


def register_tools(mcp: FastMCP[Any]) -> None:
    @mcp.tool
    def run_singlepoint(config: SinglepointSchema) -> dict[str, Any]:
        """Runs a singlepoint xTB calculation"""
        atoms: Atoms | list[Atoms] = io.read(
            config.input_path, index=config.input_index
        )
        assert isinstance(atoms, Atoms)
        atoms.calc = TBLite(atoms, method=config.method, verbosity=0)
        atoms.calc.calculate(atoms)
        results: dict[str, Any] = atoms.calc.results
        return results

    @mcp.tool
    def run_NVE(config: MolecularDynamicsSchema) -> Status:
        """Runs an NVE molecular dynamics simulation"""

        from ase.md.verlet import VelocityVerlet

        atoms: Atoms | list[Atoms] = io.read(
            config.input_path, index=config.input_index
        )
        assert isinstance(atoms, Atoms)

        atoms.calc = TBLite(atoms, method=config.method, verbosity=0)

        if config.initialize_vel:
            MaxwellBoltzmannDistribution(atoms, temperature_K=config.temperature_vel)

        log = StringIO()
        dyn = VelocityVerlet(
            atoms, config.timestep, logfile=log, loginterval=config.log_freq
        )
        dyn.attach(io.write, config.output_freq, config.output_path, atoms)
        success = dyn.run(config.num_steps)

        return Status(success=success, message=log.getvalue())

    @mcp.tool
    def run_NVT(config: NVTSchema) -> Status:
        """Runs an NVT molecular dynamics simulation"""

        from ase.md.langevin import Langevin

        atoms: Atoms | list[Atoms] = io.read(
            config.input_path, index=config.input_index
        )
        assert isinstance(atoms, Atoms)

        atoms.calc = TBLite(atoms, method=config.method, verbosity=0)

        if config.initialize_vel:
            MaxwellBoltzmannDistribution(atoms, temperature_K=config.temperature_vel)

        log = StringIO()
        dyn = Langevin(
            atoms,
            config.timestep,
            temperature_K=config.temperature,
            friction=config.friction,
            logfile=log,
            loginterval=config.log_freq,
        )
        success: bool = dyn.run(config.num_steps)

        return Status(success=success, message=log.getvalue())
