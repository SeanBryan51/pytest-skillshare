from pathlib import Path


def write_message(file: Path, message: str):
    with file.open("w") as f:
        f.write(message)
