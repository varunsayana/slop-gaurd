import os
from pathlib import Path


def is_ignored(path: str, exclude_patterns: list[str]) -> bool:
    from fnmatch import fnmatch

    for pattern in exclude_patterns:
        if fnmatch(path, pattern) or fnmatch(path, f"*/{pattern}"):
            return True
    return False


def get_absolute_path(base_dir: str, rel_path: str) -> str:
    return os.path.abspath(os.path.join(base_dir, rel_path))
