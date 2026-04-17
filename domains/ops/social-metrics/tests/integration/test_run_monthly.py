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
    """Runner exits 1 if required env vars are missing.

    We pass all SOCIAL_METRICS_* vars as empty strings. Because load_dotenv()
    defaults to override=False, it will not overwrite vars already set in the
    env — so validate_all() sees empty values and raises EnvironmentError.
    """
    empty_env = {
        "PATH": __import__("os").environ.get("PATH", ""),
        # All required vars set to empty strings (not missing, but invalid)
        "SOCIAL_METRICS_META_APP_ID": "",
        "SOCIAL_METRICS_META_APP_SECRET": "",
        "SOCIAL_METRICS_META_CONFIGURATION_ID": "",
        "SOCIAL_METRICS_META_USER_ACCESS_TOKEN": "",
        "SOCIAL_METRICS_CHEESE_TO_SHARE_PAGE_ID": "",
        "SOCIAL_METRICS_CHEESE_TO_SHARE_PAGE_ACCESS_TOKEN": "",
        "SOCIAL_METRICS_CHEESE_TO_SHARE_IG_ID": "",
        "SOCIAL_METRICS_DISCIPLINE_RIFT_PAGE_ID": "",
        "SOCIAL_METRICS_DISCIPLINE_RIFT_PAGE_ACCESS_TOKEN": "",
        "SOCIAL_METRICS_DISCIPLINE_RIFT_IG_ID": "",
        "SOCIAL_METRICS_DR_VOLLEYBALL_CLUB_PAGE_ID": "",
        "SOCIAL_METRICS_DR_VOLLEYBALL_CLUB_PAGE_ACCESS_TOKEN": "",
        "SOCIAL_METRICS_DR_VOLLEYBALL_CLUB_IG_ID": "",
    }
    result = subprocess.run(
        [sys.executable, str(RUNNER), "--month", "2026-04"],
        capture_output=True, text=True,
        cwd=str(DOMAIN_ROOT),
        env=empty_env,
    )
    assert result.returncode == 1
    assert "SOCIAL_METRICS_" in result.stderr
