import pytest

from demo_package.add_int import add_int


def test_add_int_success_case():
    assert add_int(2, 2) == 4


def test_add_int_failure_case():
    with pytest.raises(TypeError, match="Received non-integer arguments."):
        add_int("foo", "bar")
