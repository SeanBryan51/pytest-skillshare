# pytest-skillshare

## What is pytest?

- The best unit testing framework for python.

## Setup

```shell
python3 -m venv pytest-env
source pytest-env/bin/activate
pip install -r requirements.txt
```

See [here](https://docs.python.org/3/library/venv.html) for help on python virtual environments.

## Basic assertions

To test the intended behaviour of a function (a success case), we can use the [`assert`](https://docs.pytest.org/en/7.1.x/how-to/assert.html#asserting-with-the-assert-statement) statement:

```python
def test_add_int_success_case():
    assert add_int(2, 2) == 4
```

To test unintended behaviour which causes an exception to be raised (a failure case), we can use [`pytest.raises`](https://docs.pytest.org/en/7.1.x/how-to/assert.html#assertions-about-expected-exceptions):

```python
def test_add_int_failure_case():
    with pytest.raises(TypeError, match="Received non-integer arguments."):
        add_int("foo", "bar")
```

## Fixtures

Tests often require some sort of setup before you call the function being tested.

For example, if each test tests a method of a class, we can put the instantiation of that class inside a fixture:

```python
@pytest.fixture()
def foo():
    return Foo()

def test_method_a(foo):
    assert foo.a()

def test_method_b(foo):
    assert foo.b()
```

Fixtures make tests easier to read and maintain, especially when tests become complex.

### Reusing fixtures

Fixtures can also be reused by other fixtures, for example if the class `Bar` is composed of class `Foo`, we can reuse the fixture `foo` to define a fixture `bar` :

```python
@pytest.fixture()
def foo():
    return Foo()

@pytest.fixture()
def bar(foo):
    return Bar(foo)
```

### Setup/teardown

Fixtures can be used to run code before and after each test that requests the fixture via the `yield` statement. This is useful for doing setup/teardown.

For example, if we want a fixture to create a file, returns its path and then delete the file once the test has completed, we can do the following:

```python
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
```

For more information, see [Teardown/Cleanup (AKA Fixture finalization)](https://docs.pytest.org/en/6.2.x/fixture.html#teardown-cleanup-aka-fixture-finalization).

### Autouse fixtures

[Autouse fixtures](https://docs.pytest.org/en/7.1.x/how-to/fixtures.html#autouse-fixtures-fixtures-you-don-t-have-to-request) are fixtures which get requested automatically for all tests. Fixtures can be made into an autouse fixture by passing `autouse=True` to the fixture’s decorator. For example,

```python
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
```

### Fixture factories

Instead of returning an object, fixtures can also return functions. One benefit of this is that fixture function can be called from within the test, allowing you to generate different return values per test.

See [Factories as fixtures](https://docs.pytest.org/en/6.2.x/fixture.html#factories-as-fixtures) for more details.

For more information on fixtures, see [How to use fixtures](https://docs.pytest.org/en/7.1.x/how-to/fixtures.html).

## Parametrization

### Parametrizing tests

Parametrization can be useful when we want to test a function with various inputs. For example,

```python
@pytest.mark.parametrize(("a", "b", "sum"), [(0, 0, 0), (-1, 1, 0), (1, 2, 3)])
def test_add_int(a, b, sum):
    assert add_int(a, b) == sum
```

### Parametrizing fixtures

Fixtures can also be parametrized over multiple parameters. For each parameter, the parametrized fixture will be called and will execute the tests that depend on the fixture.

See [parametrizing fixtures](https://pytest.org/en/7.4.x/how-to/fixtures.html#parametrizing-fixtures).

## Generating a code coverage report

Coverage reports can be generated with the [pytest-cov](https://github.com/pytest-dev/pytest-cov) plugin.

```
pytest --cov=./ --cov-report=html
```

The above command should generate a html document at `htmlcov/index.html`

## Best practices

- Unit tests should run quickly (< 1 minute)
- A unit test should not test more than one function.
- Tests should not depend on the environment in which the test is run.