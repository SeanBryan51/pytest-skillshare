from pathlib import Path


def dump_files():
    Path("foo").touch()
    Path("bar").touch()
