import threading

from ranges import compress_ranges


def _run_with_timeout(values: list[int], timeout: float = 0.2) -> list[tuple[int, int]]:
    result: dict[str, list[tuple[int, int]]] = {}
    error: dict[str, BaseException] = {}

    def target() -> None:
        try:
            result["value"] = compress_ranges(values)
        except BaseException as exc:  # pragma: no cover - helper
            error["value"] = exc

    thread = threading.Thread(target=target, daemon=True)
    thread.start()
    thread.join(timeout)

    assert not thread.is_alive(), "compress_ranges hung on duplicated input"
    if "value" in error:
        raise error["value"]
    return result["value"]


def test_compress_ranges_handles_duplicates_without_hanging() -> None:
    assert _run_with_timeout([1, 2, 2, 3, 7, 8]) == [(1, 3), (7, 8)]
