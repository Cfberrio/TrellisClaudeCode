"""
run_meta_objects.py — Phase 1 read-only Meta Ads objects snapshot for Discipline Rift.
Pulls campaign and adset object data (not insights) from Meta Marketing API.
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

OBJECT_FIELDS = {
    "campaigns": [
        "id",
        "name",
        "status",
        "objective",
        "buying_type",
        "special_ad_categories",
    ],
    "adsets": [
        "id",
        "name",
        "status",
        "optimization_goal",
        "billing_event",
        "daily_budget",
        "lifetime_budget",
        "targeting",
        "campaign_id",
    ],
}


def load_env(env_path: Path) -> dict:
    env_vars = {}
    if not env_path.exists():
        print(f"ERROR: .env not found at {env_path}", file=sys.stderr)
        sys.exit(1)
    for line in env_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        env_vars[key.strip()] = value.strip()
    return env_vars


def validate_env(env_vars: dict):
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
    return hmac.new(
        app_secret.encode("utf-8"),
        access_token.encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()


def fetch_objects(env_vars: dict, object_type: str, fields: list[str]) -> list[dict]:
    """Call Meta Marketing API objects endpoint (campaigns or adsets). Returns list of row dicts."""
    account_id = env_vars["META_AD_ACCOUNT_ID"]
    access_token = env_vars["META_SYSTEM_USER_TOKEN"]
    app_secret = env_vars["META_APP_SECRET"]
    graph_version = env_vars["META_GRAPH_VERSION"]

    appsecret_proof = build_appsecret_proof(app_secret, access_token)

    base_url = f"https://graph.facebook.com/{graph_version}/act_{account_id}/{object_type}"

    all_rows = []
    params = {
        "access_token": access_token,
        "appsecret_proof": appsecret_proof,
        "fields": ",".join(fields),
        "limit": "500",
    }

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
        for obj in data:
            flat = {}
            for field_name in fields:
                val = obj.get(field_name, "")
                # Serialize nested structures (e.g. targeting, special_ad_categories) to JSON string
                if isinstance(val, (dict, list)):
                    val = json.dumps(val, ensure_ascii=False)
                flat[field_name] = val
            all_rows.append(flat)

        next_url = body.get("paging", {}).get("next")
        url = next_url if next_url else None

    return all_rows


def export_csv(rows: list[dict], out_path: Path):
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
        description="Pull Meta Ads object snapshots and export to CSV (read-only)."
    )
    parser.add_argument(
        "--type",
        required=True,
        choices=["campaigns", "adsets"],
        help="Object type to snapshot.",
    )
    parser.add_argument(
        "--out",
        required=True,
        help="Output CSV path.",
    )
    parser.add_argument(
        "--fields",
        default=None,
        help="Comma-separated field list. Uses type-specific defaults if omitted.",
    )
    parser.add_argument(
        "--env-file",
        default=None,
        help="Path to .env file.",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    domain_root = script_dir.parent
    project_root = domain_root.parents[3]

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

    fields = args.fields.split(",") if args.fields else OBJECT_FIELDS[args.type]

    print(f"Object type  : {args.type}")
    print(f"Fields       : {', '.join(fields)}")

    rows = fetch_objects(env_vars, args.type, fields)
    out_path = Path(args.out)
    export_csv(rows, out_path)

    print(f"Exported {len(rows)} rows → {out_path}")


if __name__ == "__main__":
    main()
