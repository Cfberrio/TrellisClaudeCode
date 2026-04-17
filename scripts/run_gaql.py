"""
run_gaql.py — Phase 1 read-only Google Ads query runner for OEV.
Executes a GAQL query file and exports results to CSV.
NEVER mutates campaigns, conversions, assets, or configurations.
"""

import argparse
import csv
import sys
from pathlib import Path

from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException


def flatten_row(row) -> dict:
    """Flatten a GoogleAds API row object into a simple key-value dict."""
    result = {}
    row_dict = type(row).to_dict(row, including_default_value_fields=False)

    def _flatten(obj, prefix=""):
        if isinstance(obj, dict):
            for k, v in obj.items():
                _flatten(v, f"{prefix}{k}." if prefix else f"{k}.")
        elif isinstance(obj, list):
            for i, v in enumerate(obj):
                _flatten(v, f"{prefix}{i}.")
        else:
            key = prefix.rstrip(".")
            result[key] = obj

    _flatten(row_dict)
    return result


def run_query(client, customer_id: str, query: str) -> list[dict]:
    """Execute a GAQL query and return list of flattened row dicts."""
    service = client.get_service("GoogleAdsService")
    rows = []

    try:
        stream = service.search_stream(customer_id=customer_id, query=query)
        for batch in stream:
            for row in batch.results:
                rows.append(flatten_row(row))
    except GoogleAdsException as ex:
        print(f"ERROR: Google Ads API request failed.", file=sys.stderr)
        for error in ex.failure.errors:
            print(f"  - {error.message}", file=sys.stderr)
        sys.exit(1)

    return rows


def export_csv(rows: list[dict], out_path: Path):
    """Write list of dicts to CSV. Creates parent dirs if needed."""
    if not rows:
        print("WARNING: Query returned 0 rows. Writing empty CSV.")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text("")
        return

    out_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = list(rows[0].keys())

    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(
        description="Run a GAQL query file and export results to CSV (read-only)."
    )
    parser.add_argument(
        "--query-file",
        required=True,
        help="Path to .sql file containing the GAQL query.",
    )
    parser.add_argument(
        "--out",
        required=True,
        help="Output CSV path (e.g. data/raw/campaigns.csv).",
    )
    parser.add_argument(
        "--customer-id",
        default=None,
        help="Google Ads customer ID (digits only, no dashes). Falls back to env GOOGLE_ADS_LOGIN_CUSTOMER_ID.",
    )
    args = parser.parse_args()

    query_path = Path(args.query_file)
    if not query_path.exists():
        print(f"ERROR: Query file not found: {query_path}", file=sys.stderr)
        sys.exit(1)

    query = query_path.read_text(encoding="utf-8").strip()
    if not query:
        print(f"ERROR: Query file is empty: {query_path}", file=sys.stderr)
        sys.exit(1)

    try:
        client = GoogleAdsClient.load_from_env()
    except Exception as e:
        print(f"ERROR: Failed to load Google Ads client from env: {e}", file=sys.stderr)
        sys.exit(1)

    customer_id = args.customer_id or client.login_customer_id
    if not customer_id:
        print(
            "ERROR: No customer ID provided. Use --customer-id or set GOOGLE_ADS_LOGIN_CUSTOMER_ID.",
            file=sys.stderr,
        )
        sys.exit(1)

    customer_id = str(customer_id).replace("-", "")

    print(f"Running query: {query_path.name}")
    print(f"Customer ID:   {customer_id}")

    rows = run_query(client, customer_id, query)
    out_path = Path(args.out)
    export_csv(rows, out_path)

    print(f"Exported {len(rows)} rows → {out_path}")


if __name__ == "__main__":
    main()
