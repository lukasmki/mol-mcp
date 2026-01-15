from .roots import RootsManager
from typing import Any, Annotated, Optional
from fastmcp import FastMCP
from molmcp.core.types import Status, File, Directory


def register_tools(mcp: FastMCP[Any], mgr: RootsManager):
    @mcp.tool
    def read_file(
        path: str, head: Optional[int] = None, tail: Optional[int] = None
    ) -> str:
        valid_path = mgr.validate(path)
        if not valid_path:
            raise ValueError(f"The given path `{path}` is not allowed")

        if head is not None:
            result = ""
            with open(valid_path) as fp:
                for _ in range(head):
                    line = fp.readline()
                    if not line:
                        break
                    result += line
            return result

        if tail is not None:
            pass

    def read_multiple_files(paths: list[str]):
        pass

    def write_file(path: str, content: str):
        pass

    def edit_file(
        path: str,
        edits: dict[
            Annotated[str, "Text to search for - must match exactly"],
            Annotated[str, "Text to replace with"],
        ],
    ):
        pass

    def move_file(source: str, destination: str):
        pass

    def create_directory(path: str):
        pass

    def list_directory(path: str):
        pass

    def tree_directory(path: str):
        pass

    def list_allowed_directories():
        pass
