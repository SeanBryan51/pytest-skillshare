import os
import shutil
from pathlib import Path

import pytest

from demo_package.dump_files import dump_files


@pytest.fixture()
def test_cwd():
    _test_cwd = Path("test_cwd")
    _test_cwd.mkdir()

    yield _test_cwd

    shutil.rmtree(_test_cwd)


@pytest.fixture(autouse=True)
def _run_around_tests(test_cwd):
    test_cwd = Path("test_cwd")
    prevdir = Path.cwd()
    os.chdir(test_cwd)

    yield

    os.chdir(prevdir)


def test_dump_files():
    dump_files()
    assert Path("foo").exists()
    assert Path("bar").exists()
