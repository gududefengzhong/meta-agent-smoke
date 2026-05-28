from pagination import slice_page


def test_slice_page_does_not_advertise_more_after_final_full_page() -> None:
    result = slice_page(["a", "b", "c", "d"], cursor=2, page_size=2)

    assert result == {
        "items": ["c", "d"],
        "next_cursor": None,
        "has_more": False,
    }


def test_slice_page_keeps_next_cursor_for_middle_pages() -> None:
    result = slice_page(["a", "b", "c", "d", "e"], cursor=0, page_size=2)

    assert result == {
        "items": ["a", "b"],
        "next_cursor": 2,
        "has_more": True,
    }
