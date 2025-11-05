import os
import asyncio
from pathlib import Path

from fast_agent import FastAgent

# Create scratch directory in run dir
scratch = Path("scratch").resolve()
if not scratch.is_dir():
    scratch.mkdir()

# Create the agent
fast = FastAgent(
    "MolMCP Tool Agent",
    config_path=Path(__file__).parent.resolve() / "config.yaml",
    parse_cli_args=False,
)

default_instruction = """
You are a tool calling agent.
Before providing any file paths, check the allowed filesystem root directories.
"""


# Define the agent
@fast.agent(instruction=default_instruction, servers=["filesystem", "tblite", "smiley"])
async def main():
    async with fast.run() as agent:
        await agent.interactive()


if __name__ == "__main__":
    asyncio.run(main())
