# OEV — Phase 1 Google Ads Extraction

## What this does
Extracts 8 read-only Google Ads datasets for OEV and saves them as CSVs in `data/raw/`.
No mutations. No reporting yet. Output is raw data only.

## How to rerun

```bash
cd "/Users/cberrio04/Documents/CLAUDE CODE"
./scripts/run_phase1_extract.sh
```

Override customer ID if needed:
```bash
./scripts/run_phase1_extract.sh 3123559470
```

## Prerequisites
- `.env` present with all 5 Google Ads credentials + `GOOGLE_ADS_CUSTOMER_ID`
- `.venv` active with `google-ads` installed (`pip install -r requirements.txt`)

## Account structure
- `GOOGLE_ADS_LOGIN_CUSTOMER_ID` = MCC/manager account (auth layer)
- `GOOGLE_ADS_CUSTOMER_ID` = client account where metrics live (query target)
- Metrics cannot be pulled at MCC level — always query against the client account

## Datasets extracted

| Query file | What it captures |
|---|---|
| `campaigns_last_30_days` | Daily campaign performance |
| `pmax_asset_groups_last_30_days` | PMax asset group performance |
| `conversion_actions` | Conversion action catalog (no date filter) |
| `campaign_conversions_by_action_last_30_days` | Conversions by action per campaign |
| `campaign_search_terms_last_30_days` | Search terms with performance metrics |
| `landing_pages_last_30_days` | Landing page URL performance |
| `geographic_performance_last_30_days` | Geographic performance by campaign |
| `call_conversions_last_30_days` | Call tracking log (no date filter) |

## Known GAQL constraints
- `metrics.cost_micros` is incompatible with `segments.conversion_action` — omitted in conversions query
- `campaign_search_term_view.status` does not exist in API v23 — omitted
- `call_view` does not support `segments.date` — full history returned, no date filter

## Output
CSVs land in `data/raw/` with a shared timestamp per run: `{query_name}_{YYYYMMDD_HHMMSS}.csv`
