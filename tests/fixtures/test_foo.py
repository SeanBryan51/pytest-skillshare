import pytest

from demo_package.foo import Foo


@pytest.fixture()
def foo():
    return Foo()


def test_method_a(foo):
    assert foo.a()


def test_method_b(foo):
    assert foo.b()
