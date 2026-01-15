from pathlib import Path


class RootsManager:
    def __init__(self, *allowed_directories: str):
        self.allowed_directories = self.normalize_dirs(*allowed_directories)

    def normalize_dirs(self, *dirs: str) -> set[Path]:
        """
        Resolve list of path strings to Path objects

        :param dirs: List of path strings
        :type dirs: list[str]
        :return: List of Paths
        :rtype: list[Path]
        """
        resolved: set[Path] = set()
        for d in dirs:
            resolved.add(self.normalize_path(d))
        return resolved

    def validate(self, path: str) -> Path | None:
        """
        Checks if given path is within any of the allowed directories

        :param path: Filesystem path string
        :type path: str
        :return: normalized path
        :rtype: Path
        """
        normalized = self.normalize_path(path)
        valid = any(d in normalized.parents for d in self.allowed_directories)
        return normalized if valid else None

    def normalize_path(self, path: str) -> Path:
        expanded = Path.expanduser(Path(path))
        resolved = expanded.resolve()
        return resolved
