from template_cache import render_template


def test_render_template_invalidates_cache_when_version_changes() -> None:
    calls: list[int] = []

    def loader(name: str, version: int) -> str:
        calls.append(version)
        return f"{name}@{version}"

    assert render_template("invoice", 1, loader) == "invoice@1"
    assert render_template("invoice", 2, loader) == "invoice@2"
    assert calls == [1, 2]
