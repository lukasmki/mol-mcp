import runpy
import sys
from argparse import ArgumentParser

# Map short names to agent module paths (package-style)
AGENTS = {
    "example": "molmcp.agents.example.agent",
    "smiley": "molmcp.agents.smiley.agent",
}


def main():
    parser = ArgumentParser()
    parser.add_argument("agent", nargs="?", default="example", help="Agent to run")
    parser.add_argument(
        "-l", "--list", action="store_true", help="List available agents"
    )
    # Any args after `--` will be forwarded to the agent script via sys.argv
    args, extra = parser.parse_known_args()

    if args.list or args.agent == "list":
        print("Available agents:")
        for name in sorted(AGENTS):
            print(f" - {name}")
        sys.exit(0)

    agent_name = args.agent
    if agent_name not in AGENTS:
        print(
            f"Unknown agent: {agent_name}\nAvailable: {', '.join(sorted(AGENTS.keys()))}"
        )
        raise SystemExit(2)

    module_name = AGENTS[agent_name]

    # Prepare sys.argv for the agent module: keep program name and forward extras
    # If user passed a '--' separator, allow extra args to be forwarded.
    sys.argv = [f"{agent_name}"] + extra

    # Execute the agent module as a script (honors if __name__ == '__main__')
    runpy.run_module(module_name, run_name="__main__", alter_sys=True)


if __name__ == "__main__":
    main()
