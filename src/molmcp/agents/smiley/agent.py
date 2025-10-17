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
    "fast-agent example",
    config_path=Path(__file__).parent.resolve() / "config.yaml",
    parse_cli_args=False,
)

default_instruction = """The current date is {{currentDate}}."""


# Define the agent
@fast.agent(instruction=default_instruction, servers=["smiley"])
async def main():
    # async with fast.run() as agent:
    #     await agent.interactive()
    await fast.start_server(
        server_name="ExampleAgent",
        server_description="This is an example.",
        transport="stdio",
    )


if __name__ == "__main__":
    asyncio.run(main())
