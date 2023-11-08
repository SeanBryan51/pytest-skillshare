from demo_package.foo import Foo


class Bar:
    def __init__(self, foo: Foo) -> None:
        self.foo = foo

    def a(self):
        return True

    def b(self):
        return True
