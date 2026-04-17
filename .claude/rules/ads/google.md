---
paths:
  - "scripts/**"
  - "queries/**"
  - "data/**"
  - "output/**"
  - "domains/ads/google/**"
---

# Google Ads — Platform Rules

## Active Pipeline
The Google Ads OEV pipeline lives in root. Its canonical paths are:
- `scripts/run_gaql.py` — GAQL query runner
- `scripts/run_phase1_extract.sh` — Phase 1 orchestrator
- `queries/*.sql` — 8 GAQL query files
- `data/raw/` — extracted CSVs
- `output/fase-2/` and `output/fase-3/` — diagnostic and rehab outputs

## API Constraints (v23+)
- `metrics.cost_micros` is incompatible with `segments.conversion_action` — omit cost_micros when segmenting by conversion action.
- `campaign_search_term_view.status` does not exist in API v23 — omit from queries.
- `call_view` does not support `segments.date` — full history returned without date filter.
- If a field breaks GAQL compatibility, remove it and continue.

## Account Structure
- `GOOGLE_ADS_LOGIN_CUSTOMER_ID` = MCC / manager account (auth layer).
- `GOOGLE_ADS_CUSTOMER_ID` = client account where metrics live (query target).
- Metrics cannot be pulled at MCC level — always query against the client account.

## Authentication
- Use `GoogleAdsClient.load_from_env()` — credentials come from `.env`.
- `GOOGLE_ADS_USE_PROTO_PLUS=true` is required for proto-plus message types.

## Query Design
- Keep queries simple and phase-1 compatible.
- Use appropriate resources per dataset (campaign, asset_group, conversion_action, campaign_search_term_view, expanded_landing_page_view, geographic_view, call_view).
- Include base metrics when applicable: impressions, clicks, ctr, average_cpc, cost_micros, conversions, conversions_value, segments.date.
