from __future__ import annotations

from pathlib import Path


class InvalidPathError(ValueError):
    pass


def ensure_directory(path: Path) -> Path:
    if path.exists() and not path.is_dir():
        raise InvalidPathError(f"{path} is not a directory")

    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)

    return path


def validate_input_folder(path: Path) -> Path:
    if not path.exists():
        raise InvalidPathError(f"{path} does not exist")
    if not path.is_dir():
        raise InvalidPathError(f"{path} is not a directory")
    return path

