from pathlib import Path


def write_report(path: str, content: str) -> None:
    report_path = Path(path)
    report_path.write_text(content, encoding="utf-8")
