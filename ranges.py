def compress_ranges(values: list[int]) -> list[tuple[int, int]]:
    if not values:
        return []

    ordered = sorted(values)
    result: list[tuple[int, int]] = []
    i = 0

    while i < len(ordered):
        start = ordered[i]
        end = start

        while i + 1 < len(ordered):
            nxt = ordered[i + 1]
            if nxt == end + 1:
                end = nxt
                i += 1
                continue
            if nxt == end:
                continue
            break

        result.append((start, end))
        i += 1

    return result
