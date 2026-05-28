from slugify import slugify


def test_slugify_lowercases() -> None:
    assert slugify("Hello") == "hello"


def test_slugify_trims_outer_whitespace() -> None:
    assert slugify("  Hello World  ") == "hello-world"


def test_slugify_collapses_repeated_spaces() -> None:
    assert slugify("Hello   World") == "hello-world"
