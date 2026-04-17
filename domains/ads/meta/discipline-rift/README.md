# Meta Ads — Discipline Rift (DR)

## Purpose
Meta Ads pipeline for the Discipline Rift brand. Phase 1 extracts read-only insights from Meta Marketing API at campaign, adset, and ad level.

## Status: Phase 1 ready (read-only extraction)

Credentials template and extraction scripts are in place. Phase 2 (diagnostic) and Phase 3 (SOP) do not exist yet.

This phase uses only `ads_read` permission. `ads_management` is NOT used.

## Directory Structure

```
discipline-rift/
├── CLAUDE.md                  # Domain context (DR brand, Meta Ads specifics)
├── README.md                  # This file
├── .env.example               # Credentials template
├── .env                       # Local credentials (never commit)
├── scripts/
│   ├── run_meta_insights.py   # Python insights extractor
│   └── run_meta_phase1_extract.sh  # Phase 1 runner (all 3 levels)
├── data/raw/                  # CSV exports from Meta API
├── output/                    # Diagnostics and SOPs (future)
└── prompts/                   # Prompt templates (future)
```

## Prerequisites
- Meta app created in Meta Developers console
- System user token with `ads_read` permission (from Meta Business Settings → System Users)
- Ad account ID for the DR account (digits only, no `act_` prefix)

## Local env setup

```bash
cd domains/ads/meta/discipline-rift/
cp .env.example .env
# Fill in real values manually — never commit .env
```

### `.env` resolution order

Scripts resolve credentials in this order:

1. `domains/ads/meta/discipline-rift/.env` — domain-local override (use for DR-specific credentials)
2. `.env` in the workspace root — fallback if no domain-local file exists

If neither file exists, the script exits with a clear error listing both paths tried.
This allows DR credentials to be isolated from other brand pipelines when needed, without requiring a separate file when a root `.env` already covers it.

| Variable | Source |
|---|---|
| `META_APP_ID` | Meta Developers → App Dashboard |
| `META_APP_SECRET` | Meta Developers → App Dashboard |
| `META_SYSTEM_USER_TOKEN` | Business Settings → System Users → Generate Token (select `ads_read`) |
| `META_AD_ACCOUNT_ID` | Business Settings → Ad Accounts → digits only, no `act_` prefix |
| `META_GRAPH_VERSION` | Default `v25.0` |

## Phase 1 — Extraction

### Run manually

```bash
bash domains/ads/meta/discipline-rift/scripts/run_meta_phase1_extract.sh
```

### Run via skill (in Claude Code)

```
/ads-meta-dr-phase1-extract
```

### What it extracts

| Level | Output file | Default fields |
|---|---|---|
| campaign | `meta_campaign_insights_YYYYMMDD_HHMMSS.csv` | campaign_name, spend, impressions, reach, clicks, ctr, cpc, cpm |
| adset | `meta_adset_insights_YYYYMMDD_HHMMSS.csv` | campaign_name, adset_name, spend, impressions, reach, clicks, ctr, cpc, cpm |
| ad | `meta_ad_insights_YYYYMMDD_HHMMSS.csv` | campaign_name, adset_name, ad_name, spend, impressions, reach, clicks, ctr, cpc, cpm |

All CSVs include `date_start` and `date_stop` columns. Default date range: last 30 days.

### Run individual level

```bash
python3 domains/ads/meta/discipline-rift/scripts/run_meta_insights.py \
  --level campaign \
  --out domains/ads/meta/discipline-rift/data/raw/test.csv
```

## Planned Phases
1. **Phase 1 — Extraction** ← current
2. **Phase 2 — Diagnostic**: audience, creative, placement, spend analysis
3. **Phase 3 — Campaign Optimization**: manual SOP for improving active campaigns
