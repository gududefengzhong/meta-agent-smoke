from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def slice_page(items: Sequence[T], cursor: int, page_size: int) -> dict[str, object]:
    page = list(items[cursor : cursor + page_size])
    next_cursor = cursor + page_size if len(page) == page_size else None
    return {
        "items": page,
        "next_cursor": next_cursor,
        "has_more": next_cursor is not None,
    }
