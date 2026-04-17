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
