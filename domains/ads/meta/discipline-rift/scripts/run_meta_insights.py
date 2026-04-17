"""
run_meta_insights.py — Phase 1 read-only Meta Ads insights extractor for Discipline Rift.
Pulls insights from Meta Marketing API and exports to CSV.
NEVER mutates campaigns, ad sets, ads, budgets, or creatives.
Uses only ads_read permission. No ads_management.
"""

import argparse
import csv
import hashlib
import hmac
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

REQUIRED_ENV_VARS = [
    "META_APP_ID",
    "META_APP_SECRET",
    "META_SYSTEM_USER_TOKEN",
    "META_AD_ACCOUNT_ID",
    "META_GRAPH_VERSION",
]

DEFAULT_FIELDS = {
    "campaign": [
        "campaign_name",
        "spend",
        "impressions",
        "reach",
        "clicks",
        "ctr",
        "cpc",
        "cpm",
    ],
    "adset": [
        "campaign_name",
        "adset_name",
        "spend",
        "impressions",
        "reach",
        "clicks",
        "ctr",
        "cpc",
        "cpm",
    ],
    "ad": [
        "campaign_name",
        "adset_name",
        "ad_name",
        "spend",
        "impressions",
        "reach",
        "clicks",
        "ctr",
        "cpc",
        "cpm",
    ],
}

DEFAULT_DATE_PRESET = "last_30d"


def load_env(env_path: Path) -> dict:
    """Load key=value pairs from a .env file into a dict."""
    env_vars = {}
    if not env_path.exists():
        print(f"ERROR: .env not found at {env_path}", file=sys.stderr)
        sys.exit(1)

    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, _, value = line.partition("=")
        env_vars[key.strip()] = value.strip()

    return env_vars


def validate_env(env_vars: dict):
    """Check that all required env vars are present and non-empty."""
    missing = [v for v in REQUIRED_ENV_VARS if not env_vars.get(v)]
    if missing:
        print("ERROR: Missing or empty environment variables:", file=sys.stderr)
        for var_name in missing:
            print(f"  - {var_name}", file=sys.stderr)
        sys.exit(1)

    token_length = len(env_vars["META_SYSTEM_USER_TOKEN"])
    account_id = env_vars["META_AD_ACCOUNT_ID"]
    print(f"META_AD_ACCOUNT_ID : {account_id}")
    print(f"META_SYSTEM_USER_TOKEN : SET ({token_length} chars)")
    print(f"META_GRAPH_VERSION : {env_vars['META_GRAPH_VERSION']}")


def build_appsecret_proof(app_secret: str, access_token: str) -> str:
    """Generate HMAC-SHA256 appsecret_proof for Meta API."""
    return hmac.new(
        app_secret.encode("utf-8"),
        access_token.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()


def fetch_insights(
    env_vars: dict,
    level: str,
    fields: list[str],
    date_preset: str,
    breakdowns: list[str] | None = None,
) -> list[dict]:
    """Call Meta Marketing API Insights endpoint. Returns list of row dicts."""
    account_id = env_vars["META_AD_ACCOUNT_ID"]
    access_token = env_vars["META_SYSTEM_USER_TOKEN"]
    app_secret = env_vars["META_APP_SECRET"]
    graph_version = env_vars["META_GRAPH_VERSION"]

    appsecret_proof = build_appsecret_proof(app_secret, access_token)

    base_url = f"https://graph.facebook.com/{graph_version}/act_{account_id}/insights"

    all_rows = []
    params = {
        "access_token": access_token,
        "appsecret_proof": appsecret_proof,
        "level": level,
        "fields": ",".join(fields),
        "date_preset": date_preset,
        "limit": "500",
    }
    if breakdowns:
        params["breakdowns"] = ",".join(breakdowns)

    url = f"{base_url}?{urllib.parse.urlencode(params)}"

    while url:
        try:
            request = urllib.request.Request(url, method="GET")
            with urllib.request.urlopen(request, timeout=60) as response:
                body = json.loads(response.read().decode("utf-8"))
        except urllib.error.HTTPError as http_err:
            error_body = http_err.read().decode("utf-8", errors="replace")
            print(f"ERROR: Meta API returned HTTP {http_err.code}", file=sys.stderr)
            try:
                error_json = json.loads(error_body)
                error_msg = error_json.get("error", {}).get("message", error_body)
                error_type = error_json.get("error", {}).get("type", "unknown")
                print(f"  Type: {error_type}", file=sys.stderr)
                print(f"  Message: {error_msg}", file=sys.stderr)
            except json.JSONDecodeError:
                print(f"  Body: {error_body[:500]}", file=sys.stderr)
            sys.exit(1)
        except urllib.error.URLError as url_err:
            print(f"ERROR: Network request failed: {url_err.reason}", file=sys.stderr)
            sys.exit(1)

        data = body.get("data", [])
        for row in data:
            flat = {}
            for field_name in fields:
                flat[field_name] = row.get(field_name, "")
            if breakdowns:
                for bd in breakdowns:
                    flat[bd] = row.get(bd, "")
            flat["date_start"] = row.get("date_start", "")
            flat["date_stop"] = row.get("date_stop", "")
            all_rows.append(flat)

        next_url = body.get("paging", {}).get("next")
        url = next_url if next_url else None

    return all_rows


def export_csv(rows: list[dict], out_path: Path):
    """Write list of dicts to CSV. Creates parent dirs if needed."""
    out_path.parent.mkdir(parents=True, exist_ok=True)

    if not rows:
        print("WARNING: Query returned 0 rows. Writing empty CSV.")
        out_path.write_text("")
        return

    fieldnames = list(rows[0].keys())

    with out_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(
        description="Pull Meta Ads insights and export to CSV (read-only)."
    )
    parser.add_argument(
        "--level",
        required=True,
        choices=["campaign", "adset", "ad"],
        help="Insights breakdown level.",
    )
    parser.add_argument(
        "--date-preset",
        default=DEFAULT_DATE_PRESET,
        help=f"Meta date preset (default: {DEFAULT_DATE_PRESET}).",
    )
    parser.add_argument(
        "--out",
        required=True,
        help="Output CSV path.",
    )
    parser.add_argument(
        "--fields",
        default=None,
        help="Comma-separated field list. Uses level-specific defaults if omitted.",
    )
    parser.add_argument(
        "--env-file",
        default=None,
        help="Path to .env file. Defaults to .env in script's parent directory.",
    )
    parser.add_argument(
        "--breakdowns",
        default=None,
        help="Comma-separated breakdown dimensions (e.g. publisher_platform,platform_position).",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    domain_root = script_dir.parent
    project_root = domain_root.parents[3]  # discipline-rift -> meta -> ads -> domains -> root

    if args.env_file:
        env_path = Path(args.env_file)
    elif (domain_root / ".env").exists():
        env_path = domain_root / ".env"
        print(f"Env source   : domain ({env_path})")
    elif (project_root / ".env").exists():
        env_path = project_root / ".env"
        print(f"Env source   : root fallback ({env_path})")
    else:
        print(
            f"ERROR: No .env found. Tried:\n"
            f"  {domain_root / '.env'}\n"
            f"  {project_root / '.env'}",
            file=sys.stderr,
        )
        sys.exit(1)

    env_vars = load_env(env_path)
    validate_env(env_vars)

    fields = args.fields.split(",") if args.fields else DEFAULT_FIELDS[args.level]
    breakdowns = args.breakdowns.split(",") if args.breakdowns else None

    print(f"Level        : {args.level}")
    print(f"Date preset  : {args.date_preset}")
    print(f"Fields       : {', '.join(fields)}")
    if breakdowns:
        print(f"Breakdowns   : {', '.join(breakdowns)}")

    rows = fetch_insights(env_vars, args.level, fields, args.date_preset, breakdowns)
    out_path = Path(args.out)
    export_csv(rows, out_path)

    print(f"Exported {len(rows)} rows → {out_path}")


if __name__ == "__main__":
    main()
