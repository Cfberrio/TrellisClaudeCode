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
