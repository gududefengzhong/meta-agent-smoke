from stream_merge import merge_chunks


def test_merge_chunks_keeps_first_non_null_finish_reason() -> None:
    merged = merge_chunks(
        [
            {"content": "Hel", "finish_reason": None},
            {"content": "lo", "finish_reason": "stop"},
            {"content": "", "finish_reason": None},
        ]
    )

    assert merged == {
        "content": "Hello",
        "finish_reason": "stop",
    }
