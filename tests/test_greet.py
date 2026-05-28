from greet import greet


def test_greet_world() -> None:
    assert greet("world") == "Hello, world!"


def test_greet_alice() -> None:
    assert greet("Alice") == "Hello, Alice!"
