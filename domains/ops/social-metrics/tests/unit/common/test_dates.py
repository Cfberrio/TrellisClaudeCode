import pytest
from src.common.dates import parse_month


def test_parse_april():
    start, end = parse_month("2026-04")
    assert start == "2026-04-01"
    assert end == "2026-04-30"


def test_parse_january():
    start, end = parse_month("2026-01")
    assert start == "2026-01-01"
    assert end == "2026-01-31"


def test_parse_february_leap_year():
    start, end = parse_month("2024-02")
    assert end == "2024-02-29"


def test_parse_february_non_leap_year():
    start, end = parse_month("2025-02")
    assert end == "2025-02-28"


def test_parse_december():
    start, end = parse_month("2026-12")
    assert start == "2026-12-01"
    assert end == "2026-12-31"


def test_invalid_format_missing_leading_zero():
    with pytest.raises(ValueError, match="YYYY-MM"):
        parse_month("2026-4")


def test_invalid_format_wrong_separator():
    with pytest.raises(ValueError, match="YYYY-MM"):
        parse_month("2026/04")


def test_invalid_format_plain_string():
    with pytest.raises(ValueError, match="YYYY-MM"):
        parse_month("april")


def test_invalid_month_value_13():
    with pytest.raises(ValueError):
        parse_month("2026-13")


def test_invalid_month_value_00():
    with pytest.raises(ValueError):
        parse_month("2026-00")
