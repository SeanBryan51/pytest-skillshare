import pytest

from demo_package.add_int import add_int


@pytest.mark.parametrize(("a", "b", "sum"), [(0, 0, 0), (-1, 1, 0), (1, 2, 3)])
def test_add_int(a, b, sum):
    assert add_int(a, b) == sum
