import asyncio
from pathlib import Path

from fast_agent import FastAgent

# Create scratch directory in run dir
scratch = Path("scratch").resolve()
if not scratch.is_dir():
    scratch.mkdir()

# Create the agent
fast = FastAgent(
    "Smiley",
    config_path=str(Path(__file__).parent.resolve() / "config.yaml"),
    parse_cli_args=False,
)

default_instruction = """
You are Smiley, an expert in SMILES string generation, retrieval, and manipulation.
"""


# Define the agent
@fast.agent(instruction=default_instruction, servers=["smiley"])
async def main():
    async with fast.run() as agent:
        await agent.interactive()

    # await fast.start_server(
    #     server_name="SmileyAgent",
    #     server_description="An agent with access to SMILES string retrieval and manipulation tools",
    #     transport="stdio",
    # )


if __name__ == "__main__":
    asyncio.run(main())
