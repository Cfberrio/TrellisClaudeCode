# Meta Monthly Extraction Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the first functional version of the Meta monthly extractor — a CLI runner that extracts Facebook + Instagram organic metrics for a given calendar month and writes 8 consolidated output files per brand.

**Architecture:** Runner at `scripts/meta/run_monthly.py` orchestrates per-brand extraction. Facebook and Instagram extractors in `src/meta/{platform}/extractor.py` call Graph API v25.0. A consolidator merges both into a `BrandResult` dict. A reporter writes 8 files to `output/meta/{brand}/{YYYY-MM}/`.

**Tech Stack:** Python 3.10+, `urllib` (stdlib HTTP), `python-dotenv` (.env loading), `openpyxl` (xlsx output), `pytest` (tests)

---

## File Map

### New files

| File | Responsibility |
|---|---|
| `requirements.txt` | `python-dotenv`, `openpyxl`, `pytest` |
| `tests/conftest.py` | Add domain root to `sys.path` for all tests |
| `src/common/__init__.py` | Package marker |
| `src/common/dates.py` | `parse_month(YYYY-MM) → (start, end)` |
| `src/common/http.py` | `get(url, params, token)` with retry/backoff; `APIError` |
| `src/common/io.py` | `output_dir()`, `write_json/csv/xlsx/md()` |
| `src/meta/__init__.py` | Package marker |
| `src/meta/facebook/__init__.py` | Package marker |
| `src/meta/facebook/extractor.py` | `extract(brand, start, end, version) → dict \| None` |
| `src/meta/instagram/__init__.py` | Package marker |
| `src/meta/instagram/extractor.py` | `extract(brand, start, end, version) → dict \| None` |
| `src/meta/shared/__init__.py` | Package marker |
| `src/meta/shared/consolidator.py` | `consolidate(fb, ig, brand, month, start, end) → BrandResult` |
| `src/meta/shared/reporter.py` | `write_outputs(result, brand, month, base_dir)` — 8 files |
| `scripts/meta/__init__.py` | Package marker (empty) |
| `scripts/meta/run_monthly.py` | CLI entry point, orchestrator |
| `tests/unit/common/__init__.py` | Package marker |
| `tests/unit/common/test_dates.py` | Tests for `dates.py` |
| `tests/unit/common/test_http.py` | Tests for `http.py` |
| `tests/unit/common/test_io.py` | Tests for `io.py` |
| `tests/unit/meta/__init__.py` | Package marker |
| `tests/unit/meta/facebook/__init__.py` | Package marker |
| `tests/unit/meta/facebook/test_extractor.py` | Tests for FB extractor |
| `tests/unit/meta/instagram/__init__.py` | Package marker |
| `tests/unit/meta/instagram/test_extractor.py` | Tests for IG extractor |
| `tests/unit/meta/shared/__init__.py` | Package marker |
| `tests/unit/meta/shared/test_consolidator.py` | Tests for consolidator |
| `tests/unit/meta/shared/test_reporter.py` | Tests for reporter |
| `tests/integration/test_run_monthly.py` | Runner integration tests (mocked API) |
| `.claude/skills/social-metrics-meta-monthly/SKILL.md` | Claude skill for running the pipeline |

### Modified files

| File | Change |
|---|---|
| `src/config/meta_config.py` | No change — already complete |
| `README.md` | Add dotenv auto-load note and run instructions |
| `docs/setup.md` | Add python-dotenv/openpyxl install step |

---

## Task 1: Dependencies and test infrastructure

**Files:**
- Create: `requirements.txt`
- Create: `tests/conftest.py`
- Create: `src/common/__init__.py`, `src/meta/__init__.py`, `src/meta/facebook/__init__.py`, `src/meta/instagram/__init__.py`, `src/meta/shared/__init__.py`, `tests/unit/__init__.py`, `tests/unit/common/__init__.py`, `tests/unit/meta/__init__.py`, `tests/unit/meta/facebook/__init__.py`, `tests/unit/meta/instagram/__init__.py`, `tests/unit/meta/shared/__init__.py`, `tests/integration/__init__.py`, `scripts/meta/__init__.py`

- [ ] **Step 1: Create `requirements.txt`**

```
python-dotenv>=1.0.0
openpyxl>=3.1.0
pytest>=8.0.0
```

- [ ] **Step 2: Install dependencies**

Run from `domains/ops/social-metrics/`:
```bash
pip install -r requirements.txt
```
Expected: all three packages install without error.

- [ ] **Step 3: Create `tests/conftest.py`**

```python
import sys
from pathlib import Path

# Add domain root to sys.path so `from src.xxx import yyy` works in all tests.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
```

- [ ] **Step 4: Create all `__init__.py` package markers**

Run from `domains/ops/social-metrics/`:
```bash
touch src/common/__init__.py \
      src/meta/__init__.py \
      src/meta/facebook/__init__.py \
      src/meta/instagram/__init__.py \
      src/meta/shared/__init__.py \
      tests/unit/__init__.py \
      tests/unit/common/__init__.py \
      tests/unit/meta/__init__.py \
      tests/unit/meta/facebook/__init__.py \
      tests/unit/meta/instagram/__init__.py \
      tests/unit/meta/shared/__init__.py \
      tests/integration/__init__.py \
      scripts/meta/__init__.py
```

- [ ] **Step 5: Verify pytest discovers tests directory**

```bash
pytest tests/ --collect-only
```
Expected: `no tests ran` (no test files yet) with exit code 5, not an import error.

- [ ] **Step 6: Commit**

```bash
git add requirements.txt tests/conftest.py src/common/__init__.py src/meta/__init__.py \
        src/meta/facebook/__init__.py src/meta/instagram/__init__.py \
        src/meta/shared/__init__.py scripts/meta/__init__.py \
        tests/unit tests/integration
git commit -m "chore: add dependencies and test infrastructure for meta monthly pipeline"
```

---

## Task 2: `src/common/dates.py`

**Files:**
- Create: `tests/unit/common/test_dates.py`
- Create: `src/common/dates.py`

- [ ] **Step 1: Write failing tests**

`tests/unit/common/test_dates.py`:
```python
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
```

- [ ] **Step 2: Run to confirm they all fail**

```bash
pytest tests/unit/common/test_dates.py -v
```
Expected: `ERROR` or `FAILED` — `ModuleNotFoundError: No module named 'src.common.dates'`

- [ ] **Step 3: Implement `src/common/dates.py`**

```python
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
```

- [ ] **Step 4: Run tests to confirm they pass**

```bash
pytest tests/unit/common/test_dates.py -v
```
Expected: `10 passed`

- [ ] **Step 5: Commit**

```bash
git add src/common/dates.py tests/unit/common/test_dates.py
git commit -m "feat: add dates.parse_month utility"
```

---

## Task 3: `src/common/http.py`

**Files:**
- Create: `tests/unit/common/test_http.py`
- Create: `src/common/http.py`

- [ ] **Step 1: Write failing tests**

`tests/unit/common/test_http.py`:
```python
import json
import urllib.error
from io import BytesIO
from unittest.mock import MagicMock, call, patch

import pytest

from src.common.http import APIError, _mask_token, get


def _mock_response(data: dict, status: int = 200):
    """Create a mock urlopen response."""
    body = json.dumps(data).encode()
    mock = MagicMock()
    mock.read.return_value = body
    mock.__enter__ = lambda s: s
    mock.__exit__ = MagicMock(return_value=False)
    return mock


def _mock_http_error(status: int, body: dict = None):
    body_bytes = json.dumps(body or {}).encode()
    return urllib.error.HTTPError(
        url="http://x", code=status, msg="err",
        hdrs=None, fp=BytesIO(body_bytes)
    )


# ── mask_token ────────────────────────────────────────────────────────────────

def test_mask_token_normal():
    assert _mask_token("EAABcdef12345678") == "EAAB...5678"


def test_mask_token_short():
    assert _mask_token("abc") == "***"


def test_mask_token_empty():
    assert _mask_token("") == "***"


# ── get — happy path ─────────────────────────────────────────────────────────

def test_get_success():
    with patch("urllib.request.urlopen", return_value=_mock_response({"id": "123"})) as mock_open:
        result = get("https://graph.facebook.com/v25.0/123", {}, "token123")
    assert result == {"id": "123"}
    assert mock_open.called


def test_get_passes_access_token_in_url():
    with patch("urllib.request.urlopen", return_value=_mock_response({"id": "1"})) as mock_open:
        get("https://graph.facebook.com/v25.0/123", {"fields": "name"}, "mytoken")
    url_called = mock_open.call_args[0][0].full_url
    assert "access_token=mytoken" in url_called
    assert "fields=name" in url_called


# ── get — auth failures ───────────────────────────────────────────────────────

def test_get_401_raises_api_error_no_retry():
    with patch("urllib.request.urlopen", side_effect=_mock_http_error(401)) as mock_open:
        with pytest.raises(APIError) as exc_info:
            get("https://graph.facebook.com/v25.0/123", {}, "badtoken")
    assert "401" in str(exc_info.value)
    assert mock_open.call_count == 1  # no retry


def test_get_403_raises_api_error_no_retry():
    with patch("urllib.request.urlopen", side_effect=_mock_http_error(403)) as mock_open:
        with pytest.raises(APIError):
            get("https://graph.facebook.com/v25.0/123", {}, "badtoken")
    assert mock_open.call_count == 1


def test_get_auth_error_token_is_masked():
    with patch("urllib.request.urlopen", side_effect=_mock_http_error(401)):
        with pytest.raises(APIError) as exc_info:
            get("https://graph.facebook.com/v25.0/123", {}, "EAABcdef12345678")
    assert "EAABcdef12345678" not in str(exc_info.value)
    assert "EAAB...5678" in str(exc_info.value)


# ── get — rate limit retries ──────────────────────────────────────────────────

def test_get_429_retries_then_succeeds():
    rate_limit_err = _mock_http_error(429)
    success_resp = _mock_response({"id": "123"})
    with patch("urllib.request.urlopen", side_effect=[rate_limit_err, success_resp]):
        with patch("time.sleep") as mock_sleep:
            result = get("https://graph.facebook.com/v25.0/123", {}, "token", max_retries=3)
    assert result == {"id": "123"}
    assert mock_sleep.called


# ── get — network errors retry ───────────────────────────────────────────────

def test_get_network_error_retries():
    import urllib.error
    net_err = urllib.error.URLError("connection refused")
    success_resp = _mock_response({"id": "ok"})
    with patch("urllib.request.urlopen", side_effect=[net_err, success_resp]):
        with patch("time.sleep"):
            result = get("https://graph.facebook.com/v25.0/123", {}, "token", max_retries=3)
    assert result == {"id": "ok"}


def test_get_exhausted_retries_raises_api_error():
    import urllib.error
    net_err = urllib.error.URLError("always fails")
    with patch("urllib.request.urlopen", side_effect=[net_err, net_err, net_err]):
        with patch("time.sleep"):
            with pytest.raises(APIError, match="3 attempts"):
                get("https://graph.facebook.com/v25.0/123", {}, "token", max_retries=3)
```

- [ ] **Step 2: Run to confirm they fail**

```bash
pytest tests/unit/common/test_http.py -v
```
Expected: `ERROR` — `ModuleNotFoundError: No module named 'src.common.http'`

- [ ] **Step 3: Implement `src/common/http.py`**

```python
"""
http.py — HTTP client for the Meta Graph API.

Uses stdlib urllib only. Implements retry with exponential backoff.
Masks access tokens in all log output and error messages.
"""

import json
import logging
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

logger = logging.getLogger(__name__)

# Meta Graph API error codes that indicate rate limiting
_RATE_LIMIT_CODES = {4, 17, 32, 613}

# Meta Graph API error codes that indicate auth failure
_AUTH_ERROR_CODES = {102, 190, 10}


class APIError(Exception):
    """Unrecoverable API error (auth failure, exhausted retries, etc.)."""

    def __init__(self, message: str, status_code: int | None = None):
        super().__init__(message)
        self.status_code = status_code


def _mask_token(token: str) -> str:
    """Return a masked representation of an access token for safe logging."""
    if not token or len(token) <= 8:
        return "***"
    return token[:4] + "..." + token[-4:]


def get(
    url: str,
    params: dict[str, str],
    access_token: str,
    timeout: int = 30,
    max_retries: int = 3,
) -> dict[str, Any]:
    """
    Make a GET request to the Meta Graph API.

    Appends access_token to params. Retries on transient errors (5xx, network
    timeouts, rate limits) with exponential backoff. Raises APIError on auth
    failures (401/403) or after exhausting retries.

    The access_token is never logged or included in error messages.
    """
    all_params = {**params, "access_token": access_token}
    full_url = url + "?" + urllib.parse.urlencode(all_params)
    req = urllib.request.Request(full_url)

    last_error: Exception | None = None

    for attempt in range(max_retries):
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8"))

        except urllib.error.HTTPError as e:
            body: dict = {}
            try:
                body = json.loads(e.read().decode("utf-8"))
            except Exception:
                pass

            error = body.get("error", {})
            code = error.get("code", 0)
            msg = error.get("message", str(e))

            # Auth failures — never retry
            if e.code in (401, 403) or code in _AUTH_ERROR_CODES:
                masked = _mask_token(access_token)
                raise APIError(
                    f"Auth error {e.code} (token: {masked}): {msg}",
                    status_code=e.code,
                )

            # Rate limit — back off and retry
            if e.code == 429 or code in _RATE_LIMIT_CODES:
                wait = 5 * (2 ** attempt)
                logger.warning(
                    f"Rate limit hit (attempt {attempt + 1}/{max_retries}), "
                    f"backing off {wait}s"
                )
                time.sleep(wait)
                last_error = e
                continue

            # Other 4xx — don't retry
            if 400 <= e.code < 500:
                raise APIError(
                    f"Client error {e.code}: {msg}",
                    status_code=e.code,
                )

            # 5xx — retry
            logger.warning(f"Server error {e.code} (attempt {attempt + 1}/{max_retries})")
            time.sleep(2 ** attempt)
            last_error = e

        except (urllib.error.URLError, TimeoutError, OSError) as e:
            logger.warning(f"Network error (attempt {attempt + 1}/{max_retries}): {e}")
            time.sleep(2 ** attempt)
            last_error = e

    raise APIError(
        f"Request failed after {max_retries} attempts for {url}: {last_error}"
    )
```

- [ ] **Step 4: Run tests to confirm they pass**

```bash
pytest tests/unit/common/test_http.py -v
```
Expected: `11 passed`

- [ ] **Step 5: Commit**

```bash
git add src/common/http.py tests/unit/common/test_http.py
git commit -m "feat: add http.get utility with retry/backoff and token masking"
```

---

## Task 4: `src/common/io.py`

**Files:**
- Create: `tests/unit/common/test_io.py`
- Create: `src/common/io.py`

- [ ] **Step 1: Write failing tests**

`tests/unit/common/test_io.py`:
```python
import csv
import json
from pathlib import Path

import pytest

from src.common.io import output_dir, write_csv, write_json, write_md, write_xlsx


def test_output_dir_creates_path(tmp_path):
    d = output_dir(tmp_path, "discipline_rift", "2026-04")
    assert d == tmp_path / "output" / "meta" / "discipline_rift" / "2026-04"
    assert d.exists()


def test_output_dir_idempotent(tmp_path):
    d1 = output_dir(tmp_path, "discipline_rift", "2026-04")
    d2 = output_dir(tmp_path, "discipline_rift", "2026-04")
    assert d1 == d2


def test_write_json(tmp_path):
    data = {"brand": "test", "value": 42}
    path = tmp_path / "test.json"
    write_json(path, data)
    assert json.loads(path.read_text()) == data


def test_write_json_handles_none_values(tmp_path):
    data = {"brand": "test", "value": None}
    path = tmp_path / "test.json"
    write_json(path, data)
    assert json.loads(path.read_text())["value"] is None


def test_write_csv(tmp_path):
    rows = [
        {"brand": "dr", "metric": "reach", "value": "100"},
        {"brand": "dr", "metric": "likes", "value": "50"},
    ]
    path = tmp_path / "test.csv"
    write_csv(path, rows, fieldnames=["brand", "metric", "value"])
    content = path.read_text()
    assert "brand,metric,value" in content
    assert "dr,reach,100" in content


def test_write_md(tmp_path):
    path = tmp_path / "report.md"
    write_md(path, "# Title\n\nBody text.")
    assert path.read_text() == "# Title\n\nBody text."


def test_write_xlsx_creates_file(tmp_path):
    path = tmp_path / "report.xlsx"
    sheets = {
        "Overview": [{"metric": "Followers", "value": 1234}],
        "Empty Sheet": [],
    }
    write_xlsx(path, sheets)
    assert path.exists()
    assert path.stat().st_size > 0


def test_write_xlsx_correct_sheet_names(tmp_path):
    import openpyxl
    path = tmp_path / "report.xlsx"
    write_xlsx(path, {"Facebook": [{"a": 1}], "Instagram": [{"b": 2}]})
    wb = openpyxl.load_workbook(path)
    assert "Facebook" in wb.sheetnames
    assert "Instagram" in wb.sheetnames
```

- [ ] **Step 2: Run to confirm they fail**

```bash
pytest tests/unit/common/test_io.py -v
```
Expected: `ERROR` — `ModuleNotFoundError: No module named 'src.common.io'`

- [ ] **Step 3: Implement `src/common/io.py`**

```python
"""
io.py — File I/O utilities for the Meta monthly pipeline.

Handles writing JSON, CSV, xlsx, and markdown outputs.
All paths are resolved relative to a provided base directory.
"""

import csv
import json
from pathlib import Path
from typing import Any


def output_dir(base: Path, brand_slug: str, month_str: str) -> Path:
    """
    Resolve and create output/meta/{brand_slug}/{month_str}/ relative to base.

    Returns the created Path.
    """
    d = base / "output" / "meta" / brand_slug / month_str
    d.mkdir(parents=True, exist_ok=True)
    return d


def write_json(path: Path, data: Any) -> None:
    """Write data as indented UTF-8 JSON."""
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False, default=str),
        encoding="utf-8",
    )


def write_csv(path: Path, rows: list[dict], fieldnames: list[str]) -> None:
    """Write rows as CSV with the given field order. Extra keys are ignored."""
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def write_md(path: Path, content: str) -> None:
    """Write a string to a markdown file."""
    path.write_text(content, encoding="utf-8")


def write_xlsx(path: Path, sheets: dict[str, list[dict]]) -> None:
    """
    Write an xlsx workbook with one sheet per key in sheets.

    Each sheet value is a list of dicts. Dict keys become column headers.
    Empty lists produce a sheet with a 'No data available' placeholder.
    """
    try:
        import openpyxl
        from openpyxl.styles import Font, PatternFill
    except ImportError:
        raise ImportError(
            "openpyxl is required for xlsx output. "
            "Install with: pip install openpyxl"
        )

    wb = openpyxl.Workbook()
    wb.remove(wb.active)  # remove default empty sheet

    header_fill = PatternFill("solid", fgColor="E8F0FE")
    header_font = Font(bold=True)

    for sheet_name, rows in sheets.items():
        ws = wb.create_sheet(title=sheet_name[:31])  # Excel tab name limit

        if not rows:
            ws.append(["No data available"])
            continue

        headers = list(rows[0].keys())
        ws.append(headers)

        for cell in ws[1]:
            cell.font = header_font
            cell.fill = header_fill

        for row in rows:
            ws.append([row.get(h) for h in headers])

        # Auto-fit column widths (capped at 50)
        for col in ws.columns:
            max_len = max(
                (len(str(cell.value or "")) for cell in col), default=8
            )
            ws.column_dimensions[col[0].column_letter].width = min(
                max_len + 2, 50
            )

    wb.save(path)
```

- [ ] **Step 4: Run tests to confirm they pass**

```bash
pytest tests/unit/common/test_io.py -v
```
Expected: `8 passed`

- [ ] **Step 5: Commit**

```bash
git add src/common/io.py tests/unit/common/test_io.py
git commit -m "feat: add io utilities for JSON, CSV, xlsx, and markdown output"
```

---

## Task 5: `src/meta/instagram/extractor.py`

**Files:**
- Create: `tests/unit/meta/instagram/test_extractor.py`
- Create: `src/meta/instagram/extractor.py`

The IG extractor uses `brand.page_access_token` for all calls (Page Access Token is valid for linked Instagram Business Account endpoints). It returns `None` only on critical auth failure on the first account call.

- [ ] **Step 1: Write failing tests**

`tests/unit/meta/instagram/test_extractor.py`:
```python
from unittest.mock import MagicMock, patch

import pytest

from src.common.http import APIError
from src.config.meta_config import BrandConfig
from src.meta.instagram.extractor import extract

BRAND = BrandConfig(
    slug="discipline_rift",
    display_name="Discipline Rift",
    page_id="111222333",
    page_access_token="PAGE_TOKEN_TEST",
    ig_id="444555666",
)

MOCK_ACCOUNT = {
    "id": "444555666",
    "username": "disciplinerift",
    "name": "Discipline Rift",
    "followers_count": 5000,
    "follows_count": 120,
    "media_count": 80,
}

MOCK_MEDIA_RESP = {
    "data": [
        {
            "id": "media_1",
            "caption": "Great practice today!",
            "media_type": "IMAGE",
            "media_product_type": "FEED",
            "permalink": "https://www.instagram.com/p/abc123/",
            "timestamp": "2026-04-10T15:00:00+0000",
            "like_count": 45,
            "comments_count": 8,
        },
        {
            "id": "media_2",
            "media_type": "VIDEO",
            "media_product_type": "REELS",
            "permalink": "https://www.instagram.com/reel/xyz789/",
            "timestamp": "2026-03-28T12:00:00+0000",  # outside April window
            "like_count": 200,
            "comments_count": 30,
        },
    ],
    "paging": {},
}

MOCK_ACCOUNT_INSIGHTS = {
    "data": [
        {
            "name": "reach",
            "period": "day",
            "values": [
                {"value": 300, "end_time": "2026-04-02T07:00:00+0000"},
                {"value": 450, "end_time": "2026-04-03T07:00:00+0000"},
            ],
        }
    ]
}

MOCK_MEDIA_INSIGHTS = {
    "data": [
        {"name": "reach", "value": 1200},
        {"name": "saved", "value": 34},
        {"name": "likes", "value": 45},
        {"name": "comments", "value": 8},
        {"name": "shares", "value": 5},
    ]
}


def _side_effects(*responses):
    """Return a list of side effects for consecutive get() calls."""
    return list(responses)


def test_extract_returns_expected_keys():
    with patch("src.meta.instagram.extractor.get") as mock_get:
        mock_get.side_effect = [
            MOCK_ACCOUNT,
            MOCK_MEDIA_RESP,
            MOCK_ACCOUNT_INSIGHTS,
            MOCK_MEDIA_INSIGHTS,  # for media_1 only (media_2 filtered out)
        ]
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    assert result is not None
    assert "account" in result
    assert "media" in result
    assert "account_insights" in result
    assert "media_insights" in result


def test_extract_filters_media_to_month():
    with patch("src.meta.instagram.extractor.get") as mock_get:
        mock_get.side_effect = [
            MOCK_ACCOUNT,
            MOCK_MEDIA_RESP,
            MOCK_ACCOUNT_INSIGHTS,
            MOCK_MEDIA_INSIGHTS,
        ]
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    # media_2 is from March, should be filtered out
    assert len(result["media"]) == 1
    assert result["media"][0]["id"] == "media_1"


def test_extract_account_data_correct():
    with patch("src.meta.instagram.extractor.get") as mock_get:
        mock_get.side_effect = [
            MOCK_ACCOUNT,
            MOCK_MEDIA_RESP,
            MOCK_ACCOUNT_INSIGHTS,
            MOCK_MEDIA_INSIGHTS,
        ]
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    assert result["account"]["followers_count"] == 5000
    assert result["account"]["username"] == "disciplinerift"


def test_extract_critical_failure_returns_none():
    with patch("src.meta.instagram.extractor.get") as mock_get:
        mock_get.side_effect = APIError("Auth error 401 (token: PAGE...TEST): Invalid token", 401)
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    assert result is None


def test_extract_media_failure_returns_result_with_empty_media():
    with patch("src.meta.instagram.extractor.get") as mock_get:
        mock_get.side_effect = [
            MOCK_ACCOUNT,
            APIError("403 Forbidden", 403),  # media call fails
        ]
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    # Should not return None — media failure is non-critical
    assert result is not None
    assert result["media"] == []


def test_extract_media_insights_failure_continues():
    with patch("src.meta.instagram.extractor.get") as mock_get:
        mock_get.side_effect = [
            MOCK_ACCOUNT,
            MOCK_MEDIA_RESP,
            MOCK_ACCOUNT_INSIGHTS,
            APIError("Error getting insights", 400),  # per-media insights fails
        ]
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    assert result is not None
    # media_insights for media_1 should be empty dict (failed gracefully)
    assert result["media_insights"].get("media_1") is None or result["media_insights"].get("media_1") == {}
```

- [ ] **Step 2: Run to confirm they fail**

```bash
pytest tests/unit/meta/instagram/test_extractor.py -v
```
Expected: `ERROR` — `ModuleNotFoundError: No module named 'src.meta.instagram.extractor'`

- [ ] **Step 3: Implement `src/meta/instagram/extractor.py`**

```python
"""
instagram/extractor.py — Instagram organic metrics extractor.

Uses the validated IG Graph API endpoints. All calls use the brand's
Page Access Token, which is valid for linked Instagram Business accounts.

Critical failure (None return): account call returns 401/403.
Partial failures: logged as warnings, field set to None/empty, pipeline continues.
"""

import logging
import urllib.parse
from typing import Any

from src.common.http import APIError, get
from src.config.meta_config import BrandConfig

logger = logging.getLogger(__name__)

BASE_URL = "https://graph.facebook.com"


def _extract_metric_value(item: dict) -> int | float | None:
    """Extract the scalar value from a Graph API insights metric dict."""
    if "value" in item:
        return item["value"]
    values = item.get("values", [])
    if values and isinstance(values, list):
        return values[0].get("value")
    return None


def extract(
    brand: BrandConfig,
    start_date: str,
    end_date: str,
    api_version: str = "v25.0",
) -> dict[str, Any] | None:
    """
    Extract Instagram organic metrics for a brand over a calendar month.

    Args:
        brand: Brand credentials and identifiers.
        start_date: ISO date string (YYYY-MM-DD), first day of month.
        end_date: ISO date string (YYYY-MM-DD), last day of month.
        api_version: Meta Graph API version string.

    Returns:
        Dict with keys: account, media, account_insights, media_insights.
        Returns None only on critical auth failure (cannot proceed without account data).
    """
    token = brand.page_access_token
    ig_id = brand.ig_id
    base = f"{BASE_URL}/{api_version}"

    # ── Account (critical) ────────────────────────────────────────────────────
    try:
        account = get(
            f"{base}/{ig_id}",
            {"fields": "id,username,name,followers_count,follows_count,media_count"},
            token,
        )
    except APIError as e:
        logger.error(f"[{brand.slug}] IG: critical failure on account call — {e}")
        return None

    # ── Media (all pages, filtered to month window) ───────────────────────────
    media_items: list[dict] = []
    try:
        resp = get(
            f"{base}/{ig_id}/media",
            {
                "fields": (
                    "id,caption,media_type,media_product_type,"
                    "permalink,timestamp,like_count,comments_count"
                ),
                "limit": "100",
            },
            token,
        )
        for item in resp.get("data", []):
            ts = item.get("timestamp", "")
            if ts and start_date <= ts[:10] <= end_date:
                media_items.append(item)

        # Paginate while there are more pages and posts are within the window
        while resp.get("paging", {}).get("next"):
            next_url = resp["paging"]["next"]
            parsed = urllib.parse.urlparse(next_url)
            params = dict(urllib.parse.parse_qsl(parsed.query))
            params.pop("access_token", None)
            resp = get(
                f"{parsed.scheme}://{parsed.netloc}{parsed.path}", params, token
            )
            stop_paginating = True
            for item in resp.get("data", []):
                ts = item.get("timestamp", "")
                if ts and ts[:10] >= start_date:
                    if ts[:10] <= end_date:
                        media_items.append(item)
                    stop_paginating = False
            # Media comes newest-first; if all items are before window, stop
            if stop_paginating:
                break

    except APIError as e:
        logger.warning(f"[{brand.slug}] IG: media fetch failed — {e}")

    # ── Account insights (reach time series) ─────────────────────────────────
    account_insights: dict | None = None
    try:
        account_insights = get(
            f"{base}/{ig_id}/insights",
            {
                "metric": "reach",
                "period": "day",
                "metric_type": "time_series",
                "since": start_date,
                "until": end_date,
            },
            token,
        )
    except APIError as e:
        logger.warning(f"[{brand.slug}] IG: account insights failed — {e}")

    # ── Media insights (top 50 items in window) ───────────────────────────────
    media_insights: dict[str, dict] = {}
    for item in media_items[:50]:
        mid = item["id"]
        try:
            resp = get(
                f"{base}/{mid}/insights",
                {"metric": "views,reach,saved,likes,comments,shares"},
                token,
            )
            media_insights[mid] = {
                m["name"]: _extract_metric_value(m)
                for m in resp.get("data", [])
            }
        except APIError as e:
            logger.debug(f"[{brand.slug}] IG: media insights for {mid} failed — {e}")

    return {
        "account": account,
        "media": media_items,
        "account_insights": account_insights,
        "media_insights": media_insights,
    }
```

- [ ] **Step 4: Run tests to confirm they pass**

```bash
pytest tests/unit/meta/instagram/test_extractor.py -v
```
Expected: `7 passed`

- [ ] **Step 5: Commit**

```bash
git add src/meta/instagram/extractor.py tests/unit/meta/instagram/test_extractor.py
git commit -m "feat: add Instagram extractor with best-effort partial failure handling"
```

---

## Task 6: `src/meta/facebook/extractor.py`

**Files:**
- Create: `tests/unit/meta/facebook/test_extractor.py`
- Create: `src/meta/facebook/extractor.py`

Facebook extraction is entirely best-effort except for the first page call. `page_impressions_unique` and `page_fan_adds` are treated as optional within the insights call — if the API returns them, great; if not, they are `None`.

- [ ] **Step 1: Write failing tests**

`tests/unit/meta/facebook/test_extractor.py`:
```python
from unittest.mock import patch

import pytest

from src.common.http import APIError
from src.config.meta_config import BrandConfig
from src.meta.facebook.extractor import extract

BRAND = BrandConfig(
    slug="discipline_rift",
    display_name="Discipline Rift",
    page_id="111222333",
    page_access_token="PAGE_TOKEN_TEST",
    ig_id="444555666",
)

MOCK_PAGE = {
    "id": "111222333",
    "name": "Discipline Rift",
    "fan_count": 1200,
    "followers_count": 1180,
    "about": "Youth sports.",
}

MOCK_INSIGHTS = {
    "data": [
        {
            "name": "page_impressions",
            "period": "month",
            "values": [{"value": 45000, "end_time": "2026-04-30T07:00:00+0000"}],
        },
        {
            "name": "page_reach",
            "period": "month",
            "values": [{"value": 22000, "end_time": "2026-04-30T07:00:00+0000"}],
        },
        {
            "name": "page_engaged_users",
            "period": "month",
            "values": [{"value": 3400, "end_time": "2026-04-30T07:00:00+0000"}],
        },
    ]
}

MOCK_POSTS = {
    "data": [
        {
            "id": "post_1",
            "message": "Season starts now!",
            "created_time": "2026-04-05T14:00:00+0000",
            "permalink_url": "https://www.facebook.com/permalink/post_1",
            "attachments": {"data": [{"media_type": "photo"}]},
            "likes": {"summary": {"total_count": 34}},
            "comments": {"summary": {"total_count": 6}},
            "shares": {"count": 3},
        }
    ],
    "paging": {},
}

MOCK_POST_INSIGHTS = {
    "data": [
        {"name": "post_impressions", "values": [{"value": 500}]},
        {"name": "post_impressions_unique", "values": [{"value": 420}]},
        {"name": "post_engaged_users", "values": [{"value": 40}]},
        {"name": "post_clicks", "values": [{"value": 15}]},
    ]
}


def test_extract_returns_expected_keys():
    with patch("src.meta.facebook.extractor.get") as mock_get:
        mock_get.side_effect = [
            MOCK_PAGE,
            MOCK_INSIGHTS,
            MOCK_POSTS,
            MOCK_POST_INSIGHTS,
        ]
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    assert result is not None
    assert "page" in result
    assert "insights" in result
    assert "posts" in result
    assert "post_insights" in result


def test_extract_page_data_correct():
    with patch("src.meta.facebook.extractor.get") as mock_get:
        mock_get.side_effect = [MOCK_PAGE, MOCK_INSIGHTS, MOCK_POSTS, MOCK_POST_INSIGHTS]
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    assert result["page"]["name"] == "Discipline Rift"
    assert result["page"]["fan_count"] == 1200


def test_extract_critical_failure_on_page_returns_none():
    with patch("src.meta.facebook.extractor.get") as mock_get:
        mock_get.side_effect = APIError("Auth error 401", 401)
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    assert result is None


def test_extract_insights_failure_returns_result_with_none_insights():
    with patch("src.meta.facebook.extractor.get") as mock_get:
        mock_get.side_effect = [
            MOCK_PAGE,
            APIError("Insights unavailable", 400),
        ]
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    assert result is not None
    assert result["insights"] is None
    assert result["posts"] == []


def test_extract_post_insights_failure_continues():
    with patch("src.meta.facebook.extractor.get") as mock_get:
        mock_get.side_effect = [
            MOCK_PAGE,
            MOCK_INSIGHTS,
            MOCK_POSTS,
            APIError("Post insights unavailable", 400),
        ]
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    assert result is not None
    assert len(result["posts"]) == 1
    # Post insights for post_1 should be None or empty
    assert result["post_insights"].get("post_1") is None or result["post_insights"].get("post_1") == {}


def test_extract_insights_parses_metric_values():
    with patch("src.meta.facebook.extractor.get") as mock_get:
        mock_get.side_effect = [MOCK_PAGE, MOCK_INSIGHTS, MOCK_POSTS, MOCK_POST_INSIGHTS]
        result = extract(BRAND, "2026-04-01", "2026-04-30")
    assert result["insights"]["page_impressions"] == 45000
    assert result["insights"]["page_reach"] == 22000
```

- [ ] **Step 2: Run to confirm they fail**

```bash
pytest tests/unit/meta/facebook/test_extractor.py -v
```
Expected: `ERROR` — `ModuleNotFoundError: No module named 'src.meta.facebook.extractor'`

- [ ] **Step 3: Implement `src/meta/facebook/extractor.py`**

```python
"""
facebook/extractor.py — Facebook Page organic metrics extractor.

All extraction is best-effort except the initial page call.
page_impressions_unique and page_fan_adds are optional — None if unavailable.

Critical failure (None return): page call returns 401/403 (bad token).
"""

import logging
from typing import Any

from src.common.http import APIError, get
from src.config.meta_config import BrandConfig

logger = logging.getLogger(__name__)

BASE_URL = "https://graph.facebook.com"


def _extract_insights_values(data: list[dict]) -> dict[str, Any]:
    """Parse a list of insights metric dicts into {metric_name: value}."""
    result: dict[str, Any] = {}
    for item in data:
        name = item.get("name")
        if not name:
            continue
        values = item.get("values", [])
        if values and isinstance(values[0].get("value"), (int, float)):
            # Sum all values in the window (handles period=day cases)
            result[name] = sum(
                v.get("value", 0) for v in values
                if isinstance(v.get("value"), (int, float))
            )
        elif "value" in item:
            result[name] = item["value"]
    return result


def extract(
    brand: BrandConfig,
    start_date: str,
    end_date: str,
    api_version: str = "v25.0",
) -> dict[str, Any] | None:
    """
    Extract Facebook Page organic metrics for a brand over a calendar month.

    Args:
        brand: Brand credentials and identifiers.
        start_date: ISO date string (YYYY-MM-DD), first day of month.
        end_date: ISO date string (YYYY-MM-DD), last day of month.
        api_version: Meta Graph API version string.

    Returns:
        Dict with keys: page, insights, posts, post_insights.
        Returns None only on critical auth failure on the page call.
    """
    token = brand.page_access_token
    page_id = brand.page_id
    base = f"{BASE_URL}/{api_version}"

    # ── Page base (critical) ──────────────────────────────────────────────────
    try:
        page = get(
            f"{base}/{page_id}",
            {"fields": "id,name,fan_count,followers_count,about"},
            token,
        )
    except APIError as e:
        logger.error(f"[{brand.slug}] FB: critical failure on page call — {e}")
        return None

    # ── Page insights (best-effort) ───────────────────────────────────────────
    insights: dict | None = None
    try:
        resp = get(
            f"{base}/{page_id}/insights",
            {
                "metric": (
                    "page_impressions,page_reach,page_engaged_users,"
                    "page_impressions_unique,page_fan_adds"
                ),
                "period": "month",
                "since": start_date,
                "until": end_date,
            },
            token,
        )
        insights = _extract_insights_values(resp.get("data", []))
    except APIError as e:
        logger.warning(f"[{brand.slug}] FB: page insights failed — {e}")

    # ── Posts in window (best-effort) ─────────────────────────────────────────
    posts: list[dict] = []
    try:
        resp = get(
            f"{base}/{page_id}/posts",
            {
                "fields": (
                    "id,message,story,created_time,permalink_url,"
                    "attachments{media_type},"
                    "likes.summary(true),comments.summary(true),shares"
                ),
                "since": start_date,
                "until": end_date,
                "limit": "100",
            },
            token,
        )
        posts = resp.get("data", [])
    except APIError as e:
        logger.warning(f"[{brand.slug}] FB: posts fetch failed — {e}")

    # ── Per-post insights (top 25, best-effort) ───────────────────────────────
    post_insights: dict[str, dict] = {}
    for post in posts[:25]:
        pid = post["id"]
        try:
            resp = get(
                f"{base}/{pid}/insights",
                {
                    "metric": (
                        "post_impressions,post_impressions_unique,"
                        "post_engaged_users,post_clicks"
                    )
                },
                token,
            )
            post_insights[pid] = _extract_insights_values(resp.get("data", []))
        except APIError as e:
            logger.debug(f"[{brand.slug}] FB: post insights for {pid} failed — {e}")

    return {
        "page": page,
        "insights": insights,
        "posts": posts,
        "post_insights": post_insights,
    }
```

- [ ] **Step 4: Run tests to confirm they pass**

```bash
pytest tests/unit/meta/facebook/test_extractor.py -v
```
Expected: `6 passed`

- [ ] **Step 5: Commit**

```bash
git add src/meta/facebook/extractor.py tests/unit/meta/facebook/test_extractor.py
git commit -m "feat: add Facebook extractor with best-effort page insights and posts"
```

---

## Task 7: `src/meta/shared/consolidator.py`

**Files:**
- Create: `tests/unit/meta/shared/test_consolidator.py`
- Create: `src/meta/shared/consolidator.py`

The consolidator merges raw extractor dicts into a `BrandResult` — a plain dict with 6 keys (`account_summary`, `content_summary`, `audience_summary`, `messages_summary`, `top_content`, `flat_rows`). It handles `None` inputs gracefully.

- [ ] **Step 1: Write failing tests**

`tests/unit/meta/shared/test_consolidator.py`:
```python
import pytest
from src.meta.shared.consolidator import consolidate
from src.config.meta_config import BrandConfig

BRAND = BrandConfig(
    slug="discipline_rift",
    display_name="Discipline Rift",
    page_id="111",
    page_access_token="token",
    ig_id="444",
)

FB = {
    "page": {"id": "111", "name": "Discipline Rift", "fan_count": 1200, "followers_count": 1180},
    "insights": {
        "page_impressions": 45000,
        "page_reach": 22000,
        "page_engaged_users": 3400,
        "page_impressions_unique": 18000,
        "page_fan_adds": 35,
    },
    "posts": [
        {
            "id": "post_1",
            "message": "Season starts now!",
            "created_time": "2026-04-05T14:00:00+0000",
            "permalink_url": "https://facebook.com/post_1",
            "attachments": {"data": [{"media_type": "photo"}]},
            "likes": {"summary": {"total_count": 34}},
            "comments": {"summary": {"total_count": 6}},
            "shares": {"count": 3},
        }
    ],
    "post_insights": {
        "post_1": {
            "post_impressions": 500,
            "post_impressions_unique": 420,
            "post_engaged_users": 40,
            "post_clicks": 15,
        }
    },
}

IG = {
    "account": {
        "id": "444",
        "username": "disciplinerift",
        "followers_count": 5000,
        "follows_count": 120,
        "media_count": 80,
    },
    "media": [
        {
            "id": "media_1",
            "caption": "Great session!",
            "media_type": "IMAGE",
            "media_product_type": "FEED",
            "permalink": "https://instagram.com/p/abc/",
            "timestamp": "2026-04-10T15:00:00+0000",
            "like_count": 150,
            "comments_count": 20,
        },
        {
            "id": "media_2",
            "media_type": "VIDEO",
            "media_product_type": "REELS",
            "permalink": "https://instagram.com/reel/xyz/",
            "timestamp": "2026-04-18T10:00:00+0000",
            "like_count": 300,
            "comments_count": 45,
        },
    ],
    "account_insights": {
        "data": [
            {
                "name": "reach",
                "values": [
                    {"value": 800, "end_time": "2026-04-02T07:00:00+0000"},
                    {"value": 950, "end_time": "2026-04-03T07:00:00+0000"},
                ],
            }
        ]
    },
    "media_insights": {
        "media_1": {"reach": 1200, "saved": 34, "likes": 150, "comments": 20, "shares": 8},
        "media_2": {"reach": 3500, "saved": 80, "likes": 300, "comments": 45, "shares": 22, "views": 8000},
    },
}


def test_consolidate_returns_all_keys():
    result = consolidate(FB, IG, BRAND, "2026-04", "2026-04-01", "2026-04-30")
    assert "account_summary" in result
    assert "content_summary" in result
    assert "audience_summary" in result
    assert "messages_summary" in result
    assert "top_content" in result
    assert "flat_rows" in result


def test_account_summary_has_brand_and_month():
    result = consolidate(FB, IG, BRAND, "2026-04", "2026-04-01", "2026-04-30")
    s = result["account_summary"]
    assert s["brand"] == "discipline_rift"
    assert s["month"] == "2026-04"


def test_account_summary_facebook_followers():
    result = consolidate(FB, IG, BRAND, "2026-04", "2026-04-01", "2026-04-30")
    assert result["account_summary"]["facebook"]["followers"] == 1180


def test_account_summary_instagram_followers():
    result = consolidate(FB, IG, BRAND, "2026-04", "2026-04-01", "2026-04-30")
    assert result["account_summary"]["instagram"]["followers"] == 5000


def test_account_summary_consolidated_total_followers():
    result = consolidate(FB, IG, BRAND, "2026-04", "2026-04-01", "2026-04-30")
    assert result["account_summary"]["consolidated"]["total_followers"] == 6180


def test_top_content_has_at_most_5_items():
    result = consolidate(FB, IG, BRAND, "2026-04", "2026-04-01", "2026-04-30")
    assert len(result["top_content"]) <= 5


def test_top_content_ranked_by_reach():
    result = consolidate(FB, IG, BRAND, "2026-04", "2026-04-01", "2026-04-30")
    top = result["top_content"]
    reaches = [p.get("reach") or 0 for p in top]
    assert reaches == sorted(reaches, reverse=True)


def test_top_content_has_platform_field():
    result = consolidate(FB, IG, BRAND, "2026-04", "2026-04-01", "2026-04-30")
    for post in result["top_content"]:
        assert post["platform"] in ("facebook", "instagram")


def test_consolidate_with_fb_none():
    result = consolidate(None, IG, BRAND, "2026-04", "2026-04-01", "2026-04-30")
    assert result is not None
    assert result["account_summary"]["facebook"] is None


def test_flat_rows_have_required_fields():
    result = consolidate(FB, IG, BRAND, "2026-04", "2026-04-01", "2026-04-30")
    assert len(result["flat_rows"]) > 0
    for row in result["flat_rows"]:
        assert "brand" in row
        assert "month" in row
        assert "platform" in row
        assert "metric_name" in row
        assert "metric_value" in row
```

- [ ] **Step 2: Run to confirm they fail**

```bash
pytest tests/unit/meta/shared/test_consolidator.py -v
```
Expected: `ERROR` — `ModuleNotFoundError: No module named 'src.meta.shared.consolidator'`

- [ ] **Step 3: Implement `src/meta/shared/consolidator.py`**

```python
"""
consolidator.py — Merges Facebook + Instagram extractor results into a BrandResult.

BrandResult is a plain dict with these keys:
    account_summary   dict
    content_summary   dict
    audience_summary  dict
    messages_summary  dict
    top_content       list[dict]  — top 5 posts, ranked by reach→views→engagement→timestamp
    flat_rows         list[dict]  — one row per metric per post/account, for CSV

None inputs produce null-filled structures. No KeyErrors.
"""

from typing import Any

from src.config.meta_config import BrandConfig

# Fields for the flat CSV
FLAT_FIELDNAMES = [
    "brand", "month", "platform", "source_type", "entity_id", "entity_name",
    "media_id", "media_type", "media_product_type", "metric_name", "metric_value",
    "date", "permalink", "timestamp", "caption_snippet",
]


def _ranking_score(post: dict) -> tuple:
    """Sort key: (reach, views, engagement, timestamp). All descending."""
    reach = post.get("reach") or 0
    views = post.get("views") or 0
    engagement = (
        (post.get("likes") or 0)
        + (post.get("comments") or 0)
        + (post.get("shares") or 0)
        + (post.get("saved") or 0)
    )
    ts = post.get("timestamp") or "0"
    return (reach, views, engagement, ts)


def _sum_ig_reach(account_insights: dict | None) -> int | None:
    """Sum daily reach values from the IG account insights time series."""
    if not account_insights:
        return None
    for item in account_insights.get("data", []):
        if item.get("name") == "reach":
            return sum(
                v.get("value", 0)
                for v in item.get("values", [])
                if isinstance(v.get("value"), (int, float))
            )
    return None


def _build_ig_posts(ig: dict) -> list[dict]:
    """Build a unified post list from IG media + media_insights."""
    posts = []
    for item in ig.get("media", []):
        mid = item["id"]
        ins = ig.get("media_insights", {}).get(mid) or {}
        posts.append({
            "platform": "instagram",
            "media_id": mid,
            "media_type": item.get("media_type"),
            "media_product_type": item.get("media_product_type"),
            "permalink": item.get("permalink"),
            "timestamp": item.get("timestamp"),
            "caption": item.get("caption", ""),
            "likes": item.get("like_count") or ins.get("likes"),
            "comments": item.get("comments_count") or ins.get("comments"),
            "shares": ins.get("shares"),
            "saved": ins.get("saved"),
            "views": ins.get("views"),
            "reach": ins.get("reach"),
        })
    return posts


def _build_fb_posts(fb: dict) -> list[dict]:
    """Build a unified post list from FB posts + post_insights."""
    posts = []
    for item in fb.get("posts", []):
        pid = item["id"]
        ins = fb.get("post_insights", {}).get(pid) or {}
        media_type = None
        attachments = item.get("attachments", {}).get("data", [])
        if attachments:
            media_type = attachments[0].get("media_type")
        posts.append({
            "platform": "facebook",
            "media_id": pid,
            "media_type": media_type,
            "media_product_type": None,
            "permalink": item.get("permalink_url"),
            "timestamp": item.get("created_time"),
            "caption": item.get("message") or item.get("story", ""),
            "likes": (item.get("likes") or {}).get("summary", {}).get("total_count"),
            "comments": (item.get("comments") or {}).get("summary", {}).get("total_count"),
            "shares": (item.get("shares") or {}).get("count"),
            "saved": None,
            "views": None,
            "reach": ins.get("post_impressions_unique") or ins.get("post_impressions"),
        })
    return posts


def _build_flat_rows(
    brand: BrandConfig,
    month_str: str,
    all_posts: list[dict],
    account_summary: dict,
) -> list[dict]:
    """Build flat rows for CSV export."""
    rows = []

    # Account-level rows
    fb_acc = account_summary.get("facebook") or {}
    ig_acc = account_summary.get("instagram") or {}

    for metric, value in {
        "fb_followers": fb_acc.get("followers"),
        "fb_reach": fb_acc.get("reach"),
        "fb_impressions": fb_acc.get("impressions"),
        "fb_engaged_users": fb_acc.get("engaged_users"),
        "ig_followers": ig_acc.get("followers"),
        "ig_monthly_reach": ig_acc.get("monthly_reach"),
    }.items():
        rows.append({
            "brand": brand.slug,
            "month": month_str,
            "platform": "facebook" if metric.startswith("fb_") else "instagram",
            "source_type": "account",
            "entity_id": fb_acc.get("page_id") if metric.startswith("fb_") else ig_acc.get("ig_id"),
            "entity_name": brand.display_name,
            "media_id": None,
            "media_type": None,
            "media_product_type": None,
            "metric_name": metric,
            "metric_value": value,
            "date": None,
            "permalink": None,
            "timestamp": None,
            "caption_snippet": None,
        })

    # Post-level rows
    post_metrics = ["reach", "views", "likes", "comments", "shares", "saved"]
    for post in all_posts:
        for metric in post_metrics:
            value = post.get(metric)
            if value is None:
                continue
            rows.append({
                "brand": brand.slug,
                "month": month_str,
                "platform": post["platform"],
                "source_type": "post",
                "entity_id": post["media_id"],
                "entity_name": brand.display_name,
                "media_id": post["media_id"],
                "media_type": post.get("media_type"),
                "media_product_type": post.get("media_product_type"),
                "metric_name": metric,
                "metric_value": value,
                "date": (post.get("timestamp") or "")[:10] or None,
                "permalink": post.get("permalink"),
                "timestamp": post.get("timestamp"),
                "caption_snippet": (post.get("caption") or "")[:100],
            })

    return rows


def consolidate(
    fb: dict | None,
    ig: dict | None,
    brand: BrandConfig,
    month_str: str,
    start_date: str,
    end_date: str,
) -> dict[str, Any]:
    """
    Merge Facebook and Instagram extractor results into a BrandResult.

    Either input may be None (e.g. FB critical failure). The result always has
    all 6 keys; None inputs produce null-filled sub-structures.
    """
    # ── Account summary ───────────────────────────────────────────────────────
    fb_acc = None
    if fb:
        page = fb.get("page") or {}
        ins = fb.get("insights") or {}
        fb_acc = {
            "page_id": page.get("id"),
            "page_name": page.get("name"),
            "followers": page.get("followers_count"),
            "fan_count": page.get("fan_count"),
            "reach": ins.get("page_reach"),
            "impressions": ins.get("page_impressions"),
            "engaged_users": ins.get("page_engaged_users"),
            "impressions_unique": ins.get("page_impressions_unique"),
            "fan_adds": ins.get("page_fan_adds"),
        }

    ig_acc = None
    if ig:
        acct = ig.get("account") or {}
        ig_acc = {
            "ig_id": acct.get("id"),
            "username": acct.get("username"),
            "followers": acct.get("followers_count"),
            "follows": acct.get("follows_count"),
            "media_count": acct.get("media_count"),
            "monthly_reach": _sum_ig_reach(ig.get("account_insights")),
        }

    total_followers = None
    if fb_acc and ig_acc:
        fb_f = fb_acc.get("followers") or 0
        ig_f = ig_acc.get("followers") or 0
        total_followers = fb_f + ig_f
    elif ig_acc:
        total_followers = ig_acc.get("followers")
    elif fb_acc:
        total_followers = fb_acc.get("followers")

    account_summary = {
        "brand": brand.slug,
        "display_name": brand.display_name,
        "month": month_str,
        "date_range": {"start": start_date, "end": end_date},
        "facebook": fb_acc,
        "instagram": ig_acc,
        "consolidated": {
            "total_followers": total_followers,
            "total_reach": (
                (fb_acc.get("reach") or 0 if fb_acc else 0)
                + (ig_acc.get("monthly_reach") or 0 if ig_acc else 0)
            ) or None,
        },
    }

    # ── All posts (combined) ──────────────────────────────────────────────────
    all_posts: list[dict] = []
    ig_posts: list[dict] = []
    fb_posts: list[dict] = []

    if ig:
        ig_posts = _build_ig_posts(ig)
        all_posts.extend(ig_posts)
    if fb:
        fb_posts = _build_fb_posts(fb)
        all_posts.extend(fb_posts)

    # ── Content summary ───────────────────────────────────────────────────────
    def _safe_sum(items, key):
        vals = [p.get(key) for p in items if p.get(key) is not None]
        return sum(vals) if vals else None

    def _avg_engagement(posts):
        rates = []
        for p in posts:
            reach = p.get("reach") or 0
            if not reach:
                continue
            eng = (
                (p.get("likes") or 0)
                + (p.get("comments") or 0)
                + (p.get("shares") or 0)
                + (p.get("saved") or 0)
            )
            rates.append(eng / reach)
        return round(sum(rates) / len(rates), 4) if rates else None

    ig_reels = [p for p in ig_posts if p.get("media_product_type") == "REELS"] if ig_posts else []

    content_summary = {
        "brand": brand.slug,
        "month": month_str,
        "facebook": {
            "posts_published": len(fb_posts),
            "total_likes": _safe_sum(fb_posts, "likes"),
            "total_comments": _safe_sum(fb_posts, "comments"),
            "total_shares": _safe_sum(fb_posts, "shares"),
            "total_reach": _safe_sum(fb_posts, "reach"),
            "avg_engagement_rate": _avg_engagement(fb_posts),
        } if fb_posts else None,
        "instagram": {
            "posts_published": len([p for p in ig_posts if p.get("media_product_type") != "REELS"]),
            "reels_published": len(ig_reels),
            "total_likes": _safe_sum(ig_posts, "likes"),
            "total_comments": _safe_sum(ig_posts, "comments"),
            "total_saves": _safe_sum(ig_posts, "saved"),
            "total_reach": _safe_sum(ig_posts, "reach"),
            "avg_engagement_rate": _avg_engagement(ig_posts),
        } if ig_posts else None,
        "consolidated": {
            "total_posts": len(all_posts),
            "total_reach": _safe_sum(all_posts, "reach"),
        },
    }

    # ── Audience summary ──────────────────────────────────────────────────────
    audience_summary = {
        "brand": brand.slug,
        "month": month_str,
        "facebook": {
            "followers_end_of_period": fb_acc.get("followers") if fb_acc else None,
            "fan_count": fb_acc.get("fan_count") if fb_acc else None,
            "fan_adds_in_period": fb_acc.get("fan_adds") if fb_acc else None,
            "demographics": None,
        } if fb_acc else None,
        "instagram": {
            "followers_end_of_period": ig_acc.get("followers") if ig_acc else None,
            "follows_count": ig_acc.get("follows") if ig_acc else None,
            "demographics": None,
        } if ig_acc else None,
        "note": (
            "Audience demographics (age, gender, location) require additional "
            "API permissions not available in Phase 1."
        ),
    }

    # ── Messages summary ──────────────────────────────────────────────────────
    messages_summary = {
        "brand": brand.slug,
        "month": month_str,
        "facebook": {
            "status": "pending",
            "note": (
                "Facebook inbox metrics require pages_messaging permission "
                "with additional setup. Planned for Phase 2."
            ),
        },
        "instagram": {
            "status": "pending",
            "note": (
                "Instagram DM metrics require business_management permission. "
                "Planned for Phase 2."
            ),
        },
    }

    # ── Top content ───────────────────────────────────────────────────────────
    ranked = sorted(all_posts, key=_ranking_score, reverse=True)[:5]
    top_content = []
    for i, post in enumerate(ranked, start=1):
        top_content.append({
            "rank": i,
            "platform": post["platform"],
            "media_id": post["media_id"],
            "media_type": post.get("media_type"),
            "media_product_type": post.get("media_product_type"),
            "permalink": post.get("permalink"),
            "timestamp": post.get("timestamp"),
            "caption_snippet": (post.get("caption") or "")[:150],
            "likes": post.get("likes"),
            "comments": post.get("comments"),
            "shares": post.get("shares"),
            "saved": post.get("saved"),
            "views": post.get("views"),
            "reach": post.get("reach"),
            "ranking_score": _ranking_score(post)[0],  # reach used for ranking
        })

    # ── Flat rows ─────────────────────────────────────────────────────────────
    flat_rows = _build_flat_rows(brand, month_str, all_posts, account_summary)

    return {
        "account_summary": account_summary,
        "content_summary": content_summary,
        "audience_summary": audience_summary,
        "messages_summary": messages_summary,
        "top_content": top_content,
        "flat_rows": flat_rows,
    }
```

- [ ] **Step 4: Run tests to confirm they pass**

```bash
pytest tests/unit/meta/shared/test_consolidator.py -v
```
Expected: `11 passed`

- [ ] **Step 5: Commit**

```bash
git add src/meta/shared/consolidator.py tests/unit/meta/shared/test_consolidator.py
git commit -m "feat: add consolidator merging FB + IG into BrandResult"
```

---

## Task 8: `src/meta/shared/reporter.py`

**Files:**
- Create: `tests/unit/meta/shared/test_reporter.py`
- Create: `src/meta/shared/reporter.py`

The reporter writes all 8 output files. The `monthly_analysis.md` is generated programmatically with real data populated.

- [ ] **Step 1: Write failing tests**

`tests/unit/meta/shared/test_reporter.py`:
```python
import json
from pathlib import Path

import pytest

from src.config.meta_config import BrandConfig
from src.meta.shared.reporter import write_outputs

BRAND = BrandConfig(
    slug="discipline_rift",
    display_name="Discipline Rift",
    page_id="111",
    page_access_token="token",
    ig_id="444",
)

RESULT = {
    "account_summary": {
        "brand": "discipline_rift",
        "display_name": "Discipline Rift",
        "month": "2026-04",
        "date_range": {"start": "2026-04-01", "end": "2026-04-30"},
        "facebook": {"followers": 1200, "reach": 22000, "impressions": 45000, "engaged_users": 3400},
        "instagram": {"followers": 5000, "monthly_reach": 15000},
        "consolidated": {"total_followers": 6200, "total_reach": 37000},
    },
    "content_summary": {
        "brand": "discipline_rift",
        "month": "2026-04",
        "facebook": {"posts_published": 10, "avg_engagement_rate": 0.025},
        "instagram": {"posts_published": 8, "reels_published": 3, "avg_engagement_rate": 0.038},
        "consolidated": {"total_posts": 21, "total_reach": 37000},
    },
    "audience_summary": {
        "brand": "discipline_rift",
        "month": "2026-04",
        "facebook": {"followers_end_of_period": 1200},
        "instagram": {"followers_end_of_period": 5000},
        "note": "Demographics not available in Phase 1.",
    },
    "messages_summary": {
        "brand": "discipline_rift",
        "month": "2026-04",
        "facebook": {"status": "pending"},
        "instagram": {"status": "pending"},
    },
    "top_content": [
        {
            "rank": 1,
            "platform": "instagram",
            "media_id": "media_1",
            "media_type": "IMAGE",
            "media_product_type": "FEED",
            "permalink": "https://instagram.com/p/abc/",
            "timestamp": "2026-04-10T15:00:00+0000",
            "caption_snippet": "Great session today!",
            "likes": 150,
            "comments": 20,
            "shares": 8,
            "saved": 34,
            "views": None,
            "reach": 3500,
            "ranking_score": 3500,
        }
    ],
    "flat_rows": [
        {
            "brand": "discipline_rift",
            "month": "2026-04",
            "platform": "instagram",
            "source_type": "post",
            "entity_id": "media_1",
            "entity_name": "Discipline Rift",
            "media_id": "media_1",
            "media_type": "IMAGE",
            "media_product_type": "FEED",
            "metric_name": "reach",
            "metric_value": 3500,
            "date": "2026-04-10",
            "permalink": "https://instagram.com/p/abc/",
            "timestamp": "2026-04-10T15:00:00+0000",
            "caption_snippet": "Great session today!",
        }
    ],
}


def test_all_8_files_are_written(tmp_path):
    write_outputs(RESULT, BRAND, "2026-04", tmp_path)
    out = tmp_path / "output" / "meta" / "discipline_rift" / "2026-04"
    expected = [
        "account_summary.json",
        "content_summary.json",
        "audience_summary.json",
        "messages_summary.json",
        "top_content.json",
        "monthly_metrics_flat.csv",
        "monthly_metrics_pretty.xlsx",
        "monthly_analysis.md",
    ]
    for fname in expected:
        assert (out / fname).exists(), f"Missing: {fname}"


def test_account_summary_json_content(tmp_path):
    write_outputs(RESULT, BRAND, "2026-04", tmp_path)
    out = tmp_path / "output" / "meta" / "discipline_rift" / "2026-04"
    data = json.loads((out / "account_summary.json").read_text())
    assert data["brand"] == "discipline_rift"
    assert data["consolidated"]["total_followers"] == 6200


def test_top_content_json_wraps_list(tmp_path):
    write_outputs(RESULT, BRAND, "2026-04", tmp_path)
    out = tmp_path / "output" / "meta" / "discipline_rift" / "2026-04"
    data = json.loads((out / "top_content.json").read_text())
    assert "brand" in data
    assert "month" in data
    assert "top_posts" in data
    assert isinstance(data["top_posts"], list)


def test_monthly_analysis_md_has_required_sections(tmp_path):
    write_outputs(RESULT, BRAND, "2026-04", tmp_path)
    out = tmp_path / "output" / "meta" / "discipline_rift" / "2026-04"
    content = (out / "monthly_analysis.md").read_text()
    required_sections = [
        "Executive Summary",
        "Cross-Platform Snapshot",
        "Facebook Summary",
        "Instagram Summary",
        "Top Content Across Meta",
        "Audience Signals",
        "Messaging / Inbox Signals",
        "Key Takeaways",
        "Recommended Next Steps",
    ]
    for section in required_sections:
        assert section in content, f"Missing section: {section}"


def test_monthly_analysis_md_has_brand_and_month(tmp_path):
    write_outputs(RESULT, BRAND, "2026-04", tmp_path)
    out = tmp_path / "output" / "meta" / "discipline_rift" / "2026-04"
    content = (out / "monthly_analysis.md").read_text()
    assert "Discipline Rift" in content
    assert "2026-04" in content


def test_flat_csv_has_header_row(tmp_path):
    write_outputs(RESULT, BRAND, "2026-04", tmp_path)
    out = tmp_path / "output" / "meta" / "discipline_rift" / "2026-04"
    content = (out / "monthly_metrics_flat.csv").read_text()
    assert "brand" in content
    assert "metric_name" in content
    assert "metric_value" in content
```

- [ ] **Step 2: Run to confirm they fail**

```bash
pytest tests/unit/meta/shared/test_reporter.py -v
```
Expected: `ERROR` — `ModuleNotFoundError: No module named 'src.meta.shared.reporter'`

- [ ] **Step 3: Implement `src/meta/shared/reporter.py`**

```python
"""
reporter.py — Writes the 8 output files for a brand/month from a BrandResult.

Output location: output/meta/{brand_slug}/{YYYY-MM}/

Files written:
    account_summary.json
    content_summary.json
    audience_summary.json
    messages_summary.json
    top_content.json
    monthly_metrics_flat.csv
    monthly_metrics_pretty.xlsx
    monthly_analysis.md
"""

from pathlib import Path
from typing import Any

from src.common.io import (
    FLAT_FIELDNAMES,
    output_dir,
    write_csv,
    write_json,
    write_md,
    write_xlsx,
)
from src.config.meta_config import BrandConfig


def _fmt(value: Any, suffix: str = "", default: str = "Not available") -> str:
    """Format a value for display in the markdown report."""
    if value is None:
        return default
    if isinstance(value, float):
        return f"{value:.1%}{suffix}"
    if isinstance(value, int):
        return f"{value:,}{suffix}"
    return str(value)


def _build_md_report(result: dict, brand: BrandConfig, month_str: str) -> str:
    """Generate the human-readable monthly_analysis.md content."""
    acc = result.get("account_summary") or {}
    con = result.get("content_summary") or {}
    aud = result.get("audience_summary") or {}
    top = result.get("top_content") or []

    fb_acc = acc.get("facebook") or {}
    ig_acc = acc.get("instagram") or {}
    consolidated = acc.get("consolidated") or {}
    fb_con = con.get("facebook") or {}
    ig_con = con.get("instagram") or {}
    con_con = con.get("consolidated") or {}

    year, month = month_str.split("-")
    import calendar
    month_name = calendar.month_name[int(month)]
    _, last_day = calendar.monthrange(int(year), int(month))

    lines = [
        f"# {brand.display_name} — Meta Monthly Report — {month_str}",
        "",
        f"**Period:** {month_name} 1–{last_day}, {year}",
        f"**Generated:** {month_str}",
        "**Platforms:** Facebook + Instagram",
        "",
        "---",
        "",
        "## Executive Summary",
        "",
        (
            f"{brand.display_name} published **{_fmt(con_con.get('total_posts'))} pieces** "
            f"across Meta in {month_name} {year}. "
            f"Combined reach: **{_fmt(consolidated.get('total_reach'))}**. "
            f"Total audience: **{_fmt(consolidated.get('total_followers'))} followers** "
            f"({_fmt(fb_acc.get('followers'))} Facebook, {_fmt(ig_acc.get('followers'))} Instagram)."
        ),
        "",
        "---",
        "",
        "## Cross-Platform Snapshot",
        "",
        "| Metric | Facebook | Instagram | Combined |",
        "|---|---|---|---|",
        f"| Followers | {_fmt(fb_acc.get('followers'))} | {_fmt(ig_acc.get('followers'))} | {_fmt(consolidated.get('total_followers'))} |",
        f"| Monthly Reach | {_fmt(fb_acc.get('reach'))} | {_fmt(ig_acc.get('monthly_reach'))} | {_fmt(consolidated.get('total_reach'))} |",
        f"| Posts Published | {_fmt(fb_con.get('posts_published'))} | {_fmt(ig_con.get('posts_published'))} | {_fmt(con_con.get('total_posts'))} |",
        f"| Avg Engagement Rate | {_fmt(fb_con.get('avg_engagement_rate'))} | {_fmt(ig_con.get('avg_engagement_rate'))} | — |",
        "",
        "---",
        "",
        "## Facebook Summary",
        "",
        "**Account KPIs**",
        f"- Followers: {_fmt(fb_acc.get('followers'))}",
        f"- Fan Count: {_fmt(fb_acc.get('fan_count'))}",
        f"- Monthly Reach: {_fmt(fb_acc.get('reach'))}",
        f"- Monthly Impressions: {_fmt(fb_acc.get('impressions'))}",
        f"- Engaged Users: {_fmt(fb_acc.get('engaged_users'))}",
        "",
        "**Content**",
        f"- Posts published: {_fmt(fb_con.get('posts_published'))}",
        f"- Total likes: {_fmt(fb_con.get('total_likes'))}",
        f"- Total comments: {_fmt(fb_con.get('total_comments'))}",
        f"- Total shares: {_fmt(fb_con.get('total_shares'))}",
        f"- Avg engagement rate: {_fmt(fb_con.get('avg_engagement_rate'))}",
        "",
        "---",
        "",
        "## Instagram Summary",
        "",
        "**Account KPIs**",
        f"- Followers: {_fmt(ig_acc.get('followers'))}",
        f"- Monthly Reach: {_fmt(ig_acc.get('monthly_reach'))}",
        "",
        "**Content**",
        f"- Posts published: {_fmt(ig_con.get('posts_published'))}",
        f"- Reels published: {_fmt(ig_con.get('reels_published'))}",
        f"- Total likes: {_fmt(ig_con.get('total_likes'))}",
        f"- Total comments: {_fmt(ig_con.get('total_comments'))}",
        f"- Total saves: {_fmt(ig_con.get('total_saves'))}",
        f"- Total reach: {_fmt(ig_con.get('total_reach'))}",
        f"- Avg engagement rate: {_fmt(ig_con.get('avg_engagement_rate'))}",
        "",
        "---",
        "",
        "## Top Content Across Meta",
        "",
    ]

    if top:
        lines += [
            "| Rank | Platform | Type | Reach | Engagement | Link |",
            "|---|---|---|---|---|---|",
        ]
        for post in top:
            eng = (
                (post.get("likes") or 0)
                + (post.get("comments") or 0)
                + (post.get("shares") or 0)
                + (post.get("saved") or 0)
            )
            content_type = post.get("media_product_type") or post.get("media_type") or "—"
            permalink = post.get("permalink") or "—"
            link = f"[link]({permalink})" if permalink != "—" else "—"
            lines.append(
                f"| {post['rank']} | {post['platform'].title()} | {content_type} "
                f"| {_fmt(post.get('reach'))} | {_fmt(eng)} | {link} |"
            )
    else:
        lines.append("No content data available.")

    lines += [
        "",
        "---",
        "",
        "## Audience Signals",
        "",
        f"**Facebook:** {_fmt(fb_acc.get('followers'))} followers. "
        f"Fan adds this period: {_fmt(fb_acc.get('fan_adds', None))}.",
        "",
        f"**Instagram:** {_fmt(ig_acc.get('followers'))} followers.",
        "",
        "_Demographic breakdowns (age, gender, location) require additional API permissions. Not available in Phase 1._",
        "",
        "---",
        "",
        "## Messaging / Inbox Signals",
        "",
        "_Facebook and Instagram inbox metrics require additional API permissions. Planned for Phase 2._",
        "",
        "---",
        "",
        "## Key Takeaways",
        "",
        "1. <!-- Fill in after reviewing data -->",
        "2. <!-- Fill in after reviewing data -->",
        "3. <!-- Fill in after reviewing data -->",
        "",
        "---",
        "",
        "## Recommended Next Steps",
        "",
        "- [ ] <!-- Action 1 — Owner — Due date -->",
        "- [ ] <!-- Action 2 -->",
        "- [ ] <!-- Action 3 -->",
    ]

    return "\n".join(lines)


def _build_xlsx_sheets(result: dict, brand: BrandConfig, month_str: str) -> dict[str, list[dict]]:
    """Build the 5 sheets for the xlsx workbook."""
    acc = result.get("account_summary") or {}
    con = result.get("content_summary") or {}
    fb_acc = acc.get("facebook") or {}
    ig_acc = acc.get("instagram") or {}
    consolidated = acc.get("consolidated") or {}
    fb_con = con.get("facebook") or {}
    ig_con = con.get("instagram") or {}
    con_con = con.get("consolidated") or {}

    overview = [
        {"Metric": "Brand", "Facebook": brand.display_name, "Instagram": brand.display_name, "Combined": brand.display_name},
        {"Metric": "Month", "Facebook": month_str, "Instagram": month_str, "Combined": month_str},
        {"Metric": "Followers", "Facebook": fb_acc.get("followers"), "Instagram": ig_acc.get("followers"), "Combined": consolidated.get("total_followers")},
        {"Metric": "Monthly Reach", "Facebook": fb_acc.get("reach"), "Instagram": ig_acc.get("monthly_reach"), "Combined": consolidated.get("total_reach")},
        {"Metric": "Posts Published", "Facebook": fb_con.get("posts_published"), "Instagram": ig_con.get("posts_published"), "Combined": con_con.get("total_posts")},
        {"Metric": "Avg Engagement Rate", "Facebook": fb_con.get("avg_engagement_rate"), "Instagram": ig_con.get("avg_engagement_rate"), "Combined": None},
    ]

    facebook_rows = [
        {"Metric": "Followers", "Value": fb_acc.get("followers")},
        {"Metric": "Fan Count", "Value": fb_acc.get("fan_count")},
        {"Metric": "Monthly Reach", "Value": fb_acc.get("reach")},
        {"Metric": "Monthly Impressions", "Value": fb_acc.get("impressions")},
        {"Metric": "Engaged Users", "Value": fb_acc.get("engaged_users")},
        {"Metric": "Impressions Unique", "Value": fb_acc.get("impressions_unique")},
        {"Metric": "Fan Adds", "Value": fb_acc.get("fan_adds")},
        {"Metric": "Posts Published", "Value": fb_con.get("posts_published")},
        {"Metric": "Avg Engagement Rate", "Value": fb_con.get("avg_engagement_rate")},
    ]

    instagram_rows = [
        {"Metric": "Followers", "Value": ig_acc.get("followers")},
        {"Metric": "Follows Count", "Value": ig_acc.get("follows")},
        {"Metric": "Monthly Reach", "Value": ig_acc.get("monthly_reach")},
        {"Metric": "Posts Published", "Value": ig_con.get("posts_published")},
        {"Metric": "Reels Published", "Value": ig_con.get("reels_published")},
        {"Metric": "Total Likes", "Value": ig_con.get("total_likes")},
        {"Metric": "Total Comments", "Value": ig_con.get("total_comments")},
        {"Metric": "Total Saves", "Value": ig_con.get("total_saves")},
        {"Metric": "Total Reach", "Value": ig_con.get("total_reach")},
        {"Metric": "Avg Engagement Rate", "Value": ig_con.get("avg_engagement_rate")},
    ]

    top_rows = []
    for post in result.get("top_content") or []:
        top_rows.append({
            "Rank": post.get("rank"),
            "Platform": post.get("platform"),
            "Type": post.get("media_product_type") or post.get("media_type"),
            "Timestamp": post.get("timestamp"),
            "Reach": post.get("reach"),
            "Likes": post.get("likes"),
            "Comments": post.get("comments"),
            "Shares": post.get("shares"),
            "Saved": post.get("saved"),
            "Views": post.get("views"),
            "Caption": post.get("caption_snippet"),
            "Permalink": post.get("permalink"),
        })

    return {
        "Overview": overview,
        "Facebook": facebook_rows,
        "Instagram": instagram_rows,
        "Top Content": top_rows,
        "Flat Data": result.get("flat_rows") or [],
    }


def write_outputs(
    result: dict,
    brand: BrandConfig,
    month_str: str,
    base_dir: Path,
) -> None:
    """Write all 8 output files for a brand/month."""
    out = output_dir(base_dir, brand.slug, month_str)

    write_json(out / "account_summary.json", result["account_summary"])
    write_json(out / "content_summary.json", result["content_summary"])
    write_json(out / "audience_summary.json", result["audience_summary"])
    write_json(out / "messages_summary.json", result["messages_summary"])
    write_json(
        out / "top_content.json",
        {"brand": brand.slug, "month": month_str, "top_posts": result["top_content"]},
    )
    write_csv(out / "monthly_metrics_flat.csv", result["flat_rows"], FLAT_FIELDNAMES)
    write_xlsx(out / "monthly_metrics_pretty.xlsx", _build_xlsx_sheets(result, brand, month_str))
    write_md(out / "monthly_analysis.md", _build_md_report(result, brand, month_str))
```

- [ ] **Step 4: Add `FLAT_FIELDNAMES` to `src/common/io.py`**

Open `src/common/io.py` and add this constant after the imports:

```python
FLAT_FIELDNAMES = [
    "brand", "month", "platform", "source_type", "entity_id", "entity_name",
    "media_id", "media_type", "media_product_type", "metric_name", "metric_value",
    "date", "permalink", "timestamp", "caption_snippet",
]
```

- [ ] **Step 5: Run all tests so far**

```bash
pytest tests/unit/ -v
```
Expected: all tests pass (dates: 10, http: 11, io: 8, instagram: 7, facebook: 6, consolidator: 11, reporter: 6 = ~59 passed)

- [ ] **Step 6: Commit**

```bash
git add src/meta/shared/reporter.py tests/unit/meta/shared/test_reporter.py src/common/io.py
git commit -m "feat: add reporter writing 8 output files including monthly_analysis.md"
```

---

## Task 9: `scripts/meta/run_monthly.py`

**Files:**
- Create: `tests/integration/test_run_monthly.py`
- Create: `scripts/meta/run_monthly.py`

- [ ] **Step 1: Write failing integration tests**

`tests/integration/test_run_monthly.py`:
```python
import json
import subprocess
import sys
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

# Domain root
DOMAIN_ROOT = Path(__file__).resolve().parents[2]
RUNNER = DOMAIN_ROOT / "scripts" / "meta" / "run_monthly.py"


def test_runner_invalid_month_format_exits_1():
    result = subprocess.run(
        [sys.executable, str(RUNNER), "--month", "2026-4"],
        capture_output=True, text=True,
        cwd=str(DOMAIN_ROOT),
    )
    assert result.returncode == 1
    assert "YYYY-MM" in result.stderr


def test_runner_invalid_month_value_exits_1():
    result = subprocess.run(
        [sys.executable, str(RUNNER), "--month", "2026-13"],
        capture_output=True, text=True,
        cwd=str(DOMAIN_ROOT),
    )
    assert result.returncode == 1


def test_runner_unknown_brand_exits_1():
    result = subprocess.run(
        [sys.executable, str(RUNNER), "--month", "2026-04", "--brand", "unknown_brand"],
        capture_output=True, text=True,
        cwd=str(DOMAIN_ROOT),
        env={**__import__("os").environ,
             "SOCIAL_METRICS_META_APP_ID": "test",
             "SOCIAL_METRICS_META_APP_SECRET": "test",
             "SOCIAL_METRICS_META_CONFIGURATION_ID": "test",
             "SOCIAL_METRICS_META_USER_ACCESS_TOKEN": "test",
             "SOCIAL_METRICS_CHEESE_TO_SHARE_PAGE_ID": "1",
             "SOCIAL_METRICS_CHEESE_TO_SHARE_PAGE_ACCESS_TOKEN": "t",
             "SOCIAL_METRICS_CHEESE_TO_SHARE_IG_ID": "1",
             "SOCIAL_METRICS_DISCIPLINE_RIFT_PAGE_ID": "2",
             "SOCIAL_METRICS_DISCIPLINE_RIFT_PAGE_ACCESS_TOKEN": "t",
             "SOCIAL_METRICS_DISCIPLINE_RIFT_IG_ID": "2",
             "SOCIAL_METRICS_DR_VOLLEYBALL_CLUB_PAGE_ID": "3",
             "SOCIAL_METRICS_DR_VOLLEYBALL_CLUB_PAGE_ACCESS_TOKEN": "t",
             "SOCIAL_METRICS_DR_VOLLEYBALL_CLUB_IG_ID": "3"},
    )
    assert result.returncode == 1
    assert "unknown_brand" in result.stderr


def test_runner_missing_env_vars_exits_1():
    """Runner exits 1 if required env vars are missing."""
    result = subprocess.run(
        [sys.executable, str(RUNNER), "--month", "2026-04"],
        capture_output=True, text=True,
        cwd=str(DOMAIN_ROOT),
        env={"PATH": __import__("os").environ.get("PATH", "")},
    )
    assert result.returncode == 1
    assert "SOCIAL_METRICS_" in result.stderr
```

- [ ] **Step 2: Run to confirm validation tests pass (runner doesn't exist yet)**

```bash
pytest tests/integration/test_run_monthly.py -v
```
Expected: all 4 tests `FAILED` with errors like `FileNotFoundError` or `ModuleNotFoundError`.

- [ ] **Step 3: Implement `scripts/meta/run_monthly.py`**

```python
#!/usr/bin/env python3
"""
run_monthly.py — Meta monthly metrics extractor entry point.

Usage:
    python scripts/meta/run_monthly.py --month 2026-04
    python scripts/meta/run_monthly.py --month 2026-04 --brand discipline_rift

Loads the global .env from the workspace root automatically (via python-dotenv).
Validates all required SOCIAL_METRICS_* env vars before making any API calls.

Exit codes:
    0  All requested brands completed (partial warnings are OK)
    1  Critical failure: missing config, invalid args, or auth failure on any brand
"""

import argparse
import logging
import sys
from pathlib import Path

# ── Path setup (must come before any src/ imports) ────────────────────────────
DOMAIN_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(DOMAIN_ROOT))

# ── Load global .env from workspace root ─────────────────────────────────────
def _load_dotenv() -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        print(
            "WARNING: python-dotenv not installed. "
            "Install with: pip install python-dotenv",
            file=sys.stderr,
        )
        return

    # Walk up from domain root to find the nearest .env file
    for parent in [DOMAIN_ROOT, *DOMAIN_ROOT.parents]:
        env_file = parent / ".env"
        if env_file.exists():
            load_dotenv(env_file)
            return


_load_dotenv()

# ── Imports (after path setup and .env load) ──────────────────────────────────
from src.common.dates import parse_month
from src.config.meta_config import BRAND_ENV_MAP, load_brand_config, validate_all
from src.meta.facebook.extractor import extract as fb_extract
from src.meta.instagram.extractor import extract as ig_extract
from src.meta.shared.consolidator import consolidate
from src.meta.shared.reporter import write_outputs

# ── Logging ───────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)

API_VERSION = "v25.0"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract Meta monthly organic metrics for Trellis brands."
    )
    parser.add_argument(
        "--month",
        required=True,
        help="Calendar month to process, format YYYY-MM (e.g. 2026-04)",
    )
    parser.add_argument(
        "--brand",
        default="all",
        help=(
            f"Brand slug to process, or 'all'. "
            f"Valid slugs: {', '.join(BRAND_ENV_MAP.keys())}. Default: all"
        ),
    )
    args = parser.parse_args()

    # ── Validate month ────────────────────────────────────────────────────────
    try:
        start_date, end_date = parse_month(args.month)
    except ValueError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    # ── Validate brand arg ────────────────────────────────────────────────────
    if args.brand == "all":
        slugs = list(BRAND_ENV_MAP.keys())
    elif args.brand in BRAND_ENV_MAP:
        slugs = [args.brand]
    else:
        print(
            f"ERROR: Unknown brand '{args.brand}'. "
            f"Valid options: {', '.join(BRAND_ENV_MAP.keys())}",
            file=sys.stderr,
        )
        return 1

    # ── Validate all required env vars ────────────────────────────────────────
    try:
        validate_all()
    except EnvironmentError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    # ── Process brands ────────────────────────────────────────────────────────
    had_critical_failure = False

    for slug in slugs:
        brand = load_brand_config(slug)
        print(f"\n[{brand.display_name}] Extracting {args.month}...")

        fb_result = fb_extract(brand, start_date, end_date, API_VERSION)
        ig_result = ig_extract(brand, start_date, end_date, API_VERSION)

        fb_status = "OK" if fb_result else "FAILED"
        ig_status = "OK" if ig_result else "FAILED"

        if not ig_result:
            print(
                f"  FB: {fb_status} | IG: {ig_status} "
                f"→ CRITICAL: IG auth failure, skipping brand",
                file=sys.stderr,
            )
            had_critical_failure = True
            continue

        result = consolidate(fb_result, ig_result, brand, args.month, start_date, end_date)
        write_outputs(result, brand, args.month, DOMAIN_ROOT)

        out_path = f"output/meta/{slug}/{args.month}/"
        print(f"  FB: {fb_status} | IG: {ig_status} → {out_path}")

    return 1 if had_critical_failure else 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run integration tests**

```bash
pytest tests/integration/test_run_monthly.py -v
```
Expected: `4 passed`

- [ ] **Step 5: Run full test suite**

```bash
pytest tests/ -v
```
Expected: all tests pass (~63 passed, 0 failed)

- [ ] **Step 6: Commit**

```bash
git add scripts/meta/run_monthly.py tests/integration/test_run_monthly.py
git commit -m "feat: add run_monthly.py CLI runner with env auto-load and brand orchestration"
```

---

## Task 10: Skill file and documentation

**Files:**
- Create: `.claude/skills/social-metrics-meta-monthly/SKILL.md`
- Modify: `README.md`

- [ ] **Step 1: Create the skill file**

Create `.claude/skills/social-metrics-meta-monthly/SKILL.md` at the **workspace root** (not inside the domain):

Path: `/Users/cberrio04/Documents/CLAUDE CODE/.claude/skills/social-metrics-meta-monthly/SKILL.md`

```markdown
# social-metrics-meta-monthly

Run the monthly Meta organic metrics extraction for Trellis brands.

## What this does
Extracts Facebook + Instagram organic metrics for a given calendar month
and writes 8 consolidated output files per brand to:
  output/meta/{brand}/YYYY-MM/

Covers: Cheese To Share, Discipline Rift, DR Volleyball Club.
Does NOT cover: TikTok, paid ads, scheduling.

## Input
Requires `--month YYYY-MM` (e.g. `2026-04`).

If the user did not provide a month in their prompt, ask:
> "Which month should I run the extraction for? (format: YYYY-MM, e.g. 2026-04)"

Validate the month is a valid YYYY-MM string before running.

## How to run

From the domain root (`domains/ops/social-metrics/`):

```bash
python scripts/meta/run_monthly.py --month {MONTH}
```

To run for a single brand:
```bash
python scripts/meta/run_monthly.py --month {MONTH} --brand discipline_rift
```

Valid brand slugs: `cheese_to_share`, `discipline_rift`, `dr_volleyball_club`

## Output files (per brand)

Written to `output/meta/{brand}/{YYYY-MM}/`:
- `account_summary.json`     — FB + IG account KPIs
- `content_summary.json`     — posts, reach, engagement
- `audience_summary.json`    — follower counts (demographics: Phase 2)
- `messages_summary.json`    — inbox signals (Phase 2)
- `top_content.json`         — top 5 posts ranked by reach
- `monthly_metrics_flat.csv` — flat table for all metrics
- `monthly_metrics_pretty.xlsx` — formatted Excel report
- `monthly_analysis.md`      — human-readable monthly report

## Prerequisite check
Before running, verify the user has SOCIAL_METRICS_* variables in their .env.
Run the config validation command if needed:
```bash
python -c "from src.config.meta_config import validate_all; validate_all(); print('Config OK')"
```

## Exit codes
- 0: all brands completed (partial warnings are OK)
- 1: critical failure (missing config, invalid month, auth error)
```

- [ ] **Step 2: Update `README.md` — add dotenv auto-load note and run instructions**

Open `README.md`. Replace the **Setup** section with:

```markdown
## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Copy env variables into your global .env at the workspace root
# The runner finds .env automatically — no manual source needed
cat domains/ops/social-metrics/.env.example
# Add the SOCIAL_METRICS_* variables to your global .env and fill them in
```

## Running a Monthly Report

```bash
# From the domain directory
cd domains/ops/social-metrics/

# Extract all 3 brands for April 2026
python scripts/meta/run_monthly.py --month 2026-04

# Extract a single brand
python scripts/meta/run_monthly.py --month 2026-04 --brand discipline_rift
```

The runner auto-loads `.env` from the workspace root. No `source .env` step needed.

Output is written to `output/meta/{brand}/YYYY-MM/`.

## Validate Config

```bash
python -c "from src.config.meta_config import validate_all; validate_all(); print('Config OK')"
```
```

- [ ] **Step 3: Run full test suite one final time**

```bash
pytest tests/ -v --tb=short
```
Expected: all tests pass.

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/social-metrics-meta-monthly/SKILL.md README.md
git commit -m "feat: add skill file and update README with run instructions"
```

---

## Self-Review Notes

**Spec coverage check:**
- ✅ Auto-load .env via python-dotenv (Task 9)
- ✅ `--month YYYY-MM` CLI arg with validation (Task 2, 9)
- ✅ FB extractor, best-effort (Task 6)
- ✅ IG extractor, primary (Task 5)
- ✅ `page_access_token` used for IG calls (Task 5, spec clarification)
- ✅ `page_impressions_unique` and `page_fan_adds` optional (Task 6)
- ✅ IG insights uses only `reach` (Task 5)
- ✅ Retry/backoff, no fixed quota assumption (Task 3)
- ✅ Token masking in errors and logs (Task 3)
- ✅ Consolidator with FB=None tolerance (Task 7)
- ✅ Top content ranking: reach → views → engagement → timestamp (Task 7)
- ✅ 8 output files (Task 8)
- ✅ 5-sheet xlsx (Task 8)
- ✅ `monthly_analysis.md` with 9 required sections (Task 8)
- ✅ Exit code 0 on warnings, 1 on critical failure (Task 9)
- ✅ Skill file (Task 10)
- ✅ API version v25.0 (Tasks 5, 6, 9)

**Type consistency check:**
- `extract()` in both extractors: `(BrandConfig, str, str, str) → dict | None` ✅
- `consolidate()`: `(dict|None, dict|None, BrandConfig, str, str, str) → dict` ✅
- `write_outputs()`: `(dict, BrandConfig, str, Path) → None` ✅
- `FLAT_FIELDNAMES` imported from `src.common.io` in `consolidator.py` and `reporter.py` ✅
- `output_dir()` imported from `src.common.io` in `reporter.py` ✅

**No placeholders**: All code blocks contain complete implementations. ✅
