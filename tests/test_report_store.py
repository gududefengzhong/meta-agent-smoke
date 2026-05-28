from report_store import write_report


def test_write_report_creates_parent_directories(tmp_path) -> None:
    target = tmp_path / "nested" / "daily" / "report.txt"

    write_report(str(target), "hello report\n")

    assert target.read_text(encoding="utf-8") == "hello report\n"
