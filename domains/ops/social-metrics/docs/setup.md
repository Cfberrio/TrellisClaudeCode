# Setup & Monthly Operations

## Prerequisites

- Python 3.10+
- Access to a Meta Developer App with the following permissions:
  - `pages_read_engagement`
  - `pages_show_list`
  - `read_insights`
  - `instagram_manage_insights`
  - `pages_messaging` (for inbox signals)

---

## Environment Variables — Namespace

This project uses a **single global `.env`** shared across the workspace. To avoid collisions with other Meta projects (e.g. Meta Ads, which uses its own `META_*` variables), all variables in this project are prefixed with:

```
SOCIAL_METRICS_
```

Do not use bare `META_*` names here — those belong to the Ads pipeline.

---

## First-Time Setup

```bash
# 1. Open the global .env at the workspace root
#    (do NOT create a separate .env inside this domain)

# 2. Copy the block from .env.example into your global .env
cat domains/ops/social-metrics/.env.example

# 3. Fill in the real values for each SOCIAL_METRICS_* variable
```

---

## Required Environment Variables

### App-Level (shared across all brands)

| Variable | Where to find it |
|---|---|
| `SOCIAL_METRICS_META_APP_ID` | Meta for Developers → App → Settings → Basic → App ID |
| `SOCIAL_METRICS_META_APP_SECRET` | Meta for Developers → App → Settings → Basic → App Secret |
| `SOCIAL_METRICS_META_CONFIGURATION_ID` | Meta for Developers → App → Webhooks or Business Login config ID |
| `SOCIAL_METRICS_META_USER_ACCESS_TOKEN` | Generated via Graph API Explorer or Business token exchange |

### Per Brand

| Variable | Where to find it |
|---|---|
| `SOCIAL_METRICS_{BRAND}_PAGE_ID` | Facebook Page → About → Page transparency → Page ID |
| `SOCIAL_METRICS_{BRAND}_PAGE_ACCESS_TOKEN` | Graph API Explorer → generate token for the page |
| `SOCIAL_METRICS_{BRAND}_IG_ID` | Instagram Business Account ID linked to the FB Page |

Replace `{BRAND}` with:
- `CHEESE_TO_SHARE`
- `DISCIPLINE_RIFT`
- `DR_VOLLEYBALL_CLUB`

---

## Running the Monthly Report

> The report period is passed as a CLI argument — not stored in `.env`.

```bash
# Run for a specific month (once extraction is implemented)
python scripts/meta/run_monthly.py --month 2026-04

# Run for a specific brand only
python scripts/meta/run_monthly.py --month 2026-04 --brand discipline_rift

# Run for all brands
python scripts/meta/run_monthly.py --month 2026-04 --brand all
```

Output is written to:
```
output/meta/{brand}/2026-04/
├── account_summary.json
├── content_summary.json
├── audience_summary.json
├── messages_summary.json
├── top_content.json
├── monthly_metrics_flat.csv
├── monthly_metrics_pretty.xlsx
└── monthly_analysis.md
```

Each month creates its own folder. Previous months are never overwritten.

---

## Validating Your Config

Before running an extraction, validate that all required env vars are set:

```bash
python -c "from src.config.meta_config import validate_all; validate_all(); print('Config OK')"
```

If anything is missing, the error message lists exactly which `SOCIAL_METRICS_*` variables to add — without exposing any secret values.

---

## Token Notes

- **Page Access Tokens** expire unless they are Long-Lived Tokens (60-day TTL) or System User Tokens (no expiry). Use System User Tokens in production.
- **Instagram Stories** metrics expire 7 days after posting — run extraction within that window.
- **Facebook Post Insights** are available for 90 days. Monthly extraction is sufficient.

---

## Security Rules

- `.env` is in `.gitignore` — it will never be committed.
- Never paste token values into docs, Slack, ClickUp tasks, or comments.
- If a token is accidentally exposed, revoke it immediately in the Meta Developer dashboard and generate a new one.
