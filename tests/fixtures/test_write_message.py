from pathlib import Path

import pytest

from demo_package.write_message import write_message


@pytest.fixture()
def file():
    _file = Path("foo")
    _file.touch()

    yield _file

    _file.unlink()


def test_write_message(file):
    write_message(file, "hello there")
    with file.open("r") as f:
        assert f.read() == "hello there"
