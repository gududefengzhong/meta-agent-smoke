from csv_reader import parse_csv_row


def test_parse_csv_row_keeps_commas_inside_quoted_fields() -> None:
    row = 'alpha,"beta,gamma",delta'

    assert parse_csv_row(row) == ["alpha", "beta,gamma", "delta"]
