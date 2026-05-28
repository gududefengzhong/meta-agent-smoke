def parse_csv_row(line: str) -> list[str]:
    return [part.strip() for part in line.split(",")]
