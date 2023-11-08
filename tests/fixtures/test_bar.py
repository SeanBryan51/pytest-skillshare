import pytest

from demo_package.foo import Foo
from demo_package.bar import Bar


@pytest.fixture()
def foo():
    return Foo()


@pytest.fixture()
def bar(foo):
    return Bar(foo)


def test_method_a(bar):
    assert bar.a()


def test_method_b(bar):
    assert bar.b()
