import asyncio
from pathlib import Path
from tempfile import gettempdir
from fast_agent import FastAgent


def get_config(servers: list[str]) -> str:
    # typically this would be somewhere permanent
    # but since im making this dynamically i store in /tmp
    config_path: Path = Path(gettempdir()) / "fastagent.config.yaml"
    serversstr = ", ".join([f'"{s}"' for s in servers])
    with open(config_path, "w") as fp:
        fp.write(f"""
# FastAgent Configuration File
default_model: claude-haiku-4-5
logger:
  progress_display: true
  show_chat: true
  show_tools: true
  truncate_tools: true
mcp:
  servers:
    tool:
      command: "uv"
      args: ["run", "mol-mcp", "serve", {serversstr}]
""")
    return str(config_path)


def setup_fastagent(servers: list[str]):
    # Get config path
    config_path = get_config(servers)

    # Create the agent
    fast = FastAgent(
        name="MolMCP Tool Agent",
        config_path=config_path,
        parse_cli_args=True,
    )
    default_instruction = "You are a tool calling agent. Always check the filesystem allowed directories before providing any file paths."

    # Define the agent
    @fast.agent(instruction=default_instruction, servers=["tool"])
    async def main():
        async with fast.run() as agent:
            await agent.interactive()

    return main


if __name__ == "__main__":
    asyncio.run(setup_fastagent(["smiles"])())
