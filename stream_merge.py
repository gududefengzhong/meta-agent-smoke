from collections.abc import Sequence


def merge_chunks(chunks: Sequence[dict[str, object]]) -> dict[str, object]:
    content_parts: list[str] = []
    finish_reason = None
    for chunk in chunks:
        delta = chunk.get("content")
        if isinstance(delta, str):
            content_parts.append(delta)
        finish_reason = chunk.get("finish_reason")
    return {
        "content": "".join(content_parts),
        "finish_reason": finish_reason,
    }
