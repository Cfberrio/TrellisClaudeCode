"""
dates.py — Month parsing utilities for the Meta monthly pipeline.

All date strings are ISO 8601 (YYYY-MM-DD).
"""

import re
from calendar import monthrange
from datetime import date


def parse_month(month_str: str) -> tuple[str, str]:
    """
    Parse a YYYY-MM string and return (start_date, end_date) as YYYY-MM-DD strings.

    Raises ValueError if the format is invalid or the month value is out of range.

    Examples:
        parse_month("2026-04") → ("2026-04-01", "2026-04-30")
        parse_month("2024-02") → ("2024-02-01", "2024-02-29")
    """
    if not re.fullmatch(r"\d{4}-\d{2}", month_str):
        raise ValueError(
            f"Invalid month format: '{month_str}'. Expected YYYY-MM (e.g. 2026-04)."
        )
    year = int(month_str[:4])
    month = int(month_str[5:])
    if not (1 <= month <= 12):
        raise ValueError(
            f"Invalid month value: {month}. Must be between 01 and 12."
        )
    _, last_day = monthrange(year, month)
    start = date(year, month, 1).isoformat()
    end = date(year, month, last_day).isoformat()
    return start, end
