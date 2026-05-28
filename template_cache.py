from collections.abc import Callable

_CACHE: dict[str, str] = {}


def render_template(name: str, version: int, loader: Callable[[str, int], str]) -> str:
    if name in _CACHE:
        return _CACHE[name]
    rendered = loader(name, version)
    _CACHE[name] = rendered
    return rendered
