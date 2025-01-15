from __future__ import annotations

from os import chdir
from contextlib import contextmanager
from pathlib import Path

import yaml


def is_valid_yaml(path: str | Path):
    path = Path(path)

    if not path.is_file():
        print(f"File does not exist: {path}")
        return False

    try:
        with path.open("r") as file:
            yaml.safe_load(file)
    except yaml.YAMLError as e:
        print(f"Invalid YAML file: {path} - Error: {e}")
        return False
    except OSError as e:
        print(f"Error reading file: {path} - Error: {e}")
        return False

    return True


@contextmanager
def run_within_dir(path: str | Path):
    oldpwd = Path.cwd()
    chdir(Path(path))
    try:
        yield
    finally:
        chdir(oldpwd)


def file_contains_text(file: str | Path, text: str) -> bool:
    return text in Path(file).read_text()
