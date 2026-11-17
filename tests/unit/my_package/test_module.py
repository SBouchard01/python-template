from my_package.module import hello_world

# ruff: noqa: INP001 D100 D103 S101


def test_hello_world() -> None:
    assert hello_world() == "Hello, World!"
