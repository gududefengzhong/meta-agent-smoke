from accumulator import append_item


def test_append_item_with_explicit_bucket() -> None:
    assert append_item("a", []) == ["a"]


def test_append_item_does_not_leak_state_across_calls() -> None:
    assert append_item("a") == ["a"]
    assert append_item("b") == ["b"]
