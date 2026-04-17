# Design Spec: Meta Monthly Extraction Pipeline
**Date:** 2026-04-15
**Domain:** `domains/ops/social-metrics/`
**Status:** Approved — ready for implementation

---

## Overview

Build the first functional version of the Meta monthly extractor for 3 Trellis brands. Extracts Facebook + Instagram organic metrics for a given calendar month and produces 8 consolidated output files per brand.

**Brands:** Cheese To Share, Discipline Rift, DR Volleyball Club
**Platforms:** Facebook (best-effort) + Instagram (primary)
**Not in scope:** TikTok, scheduling, dashboards, email, webhooks, Google Sheets

---

## Architecture

```
run_monthly.py  (CLI entry point, orchestrator)
  │
  ├── src/config/meta_config.py        (exists — load/validate SOCIAL_METRICS_* env vars)
  ├── src/common/dates.py              (parse YYYY-MM, derive start/end dates)
  ├── src/common/http.py               (urllib client, retry/backoff, token masking)
  ├── src/common/io.py                 (write JSON, CSV, xlsx, md; manage output paths)
  │
  ├── src/meta/facebook/extractor.py   (FB page data, insights, posts — best-effort)
  ├── src/meta/instagram/extractor.py  (IG account, media, insights — primary)
  │
  ├── src/meta/shared/consolidator.py  (merge FB + IG → BrandResult dict)
  └── src/meta/shared/reporter.py      (write 8 output files from BrandResult)
```

Each extractor returns a `dict | None`. `None` only on critical auth failure (401/403 on first call). Partial failures return `None` per field, logged as warnings.

---

## Module Responsibilities

### `src/common/dates.py`
- `parse_month(month_str: str) -> tuple[str, str]`
  - Validates strict `YYYY-MM` format, raises `ValueError` with clear message otherwise
  - Returns `(start_date, end_date)` as `YYYY-MM-DD` strings
  - Example: `"2026-04"` → `("2026-04-01", "2026-04-30")`

### `src/common/http.py`
- `get(url, params, access_token, timeout=30) -> dict`
- Retry with exponential backoff on transient errors (5xx, network timeout)
- On rate-limit response (HTTP 429 or error code 32/17/4): back off and retry, do not assume a fixed quota
- Masks token in any log output: `token[:4] + "..." + token[-4:]`
- Raises `APIError` on unrecoverable errors (401, 403, invalid token)

### `src/common/io.py`
- `output_dir(brand_slug, month_str) -> Path` — resolves `output/meta/{slug}/{YYYY-MM}/`
- `write_json(path, data)`
- `write_csv(path, rows, fieldnames)`
- `write_xlsx(path, sheets: dict[str, list[dict]])` — uses `openpyxl`
- `write_md(path, content: str)`

### `src/meta/facebook/extractor.py`
- Input: `BrandConfig`, `start_date`, `end_date`, `api_version`
- Returns: `FacebookResult` dict with keys: `page`, `insights`, `posts`
- `page` is critical — `None` here = mark brand FB as failed, log error
- `insights` and `posts` are best-effort — `None` on failure, continue

**Endpoints:**

| Call | Endpoint | Critical? |
|---|---|---|
| Page base | `/{page_id}?fields=id,name,fan_count,followers_count,about` | Yes |
| Page insights | `/{page_id}/insights?metric=page_impressions,page_reach,page_engaged_users,page_impressions_unique,page_fan_adds&period=month&since={start}&until={end}` | No — `page_impressions_unique` and `page_fan_adds` treated as optional fields within this call |
| Posts | `/{page_id}/posts?fields=id,message,story,created_time,permalink_url,attachments{media_type},likes.summary(true),comments.summary(true),shares&since={start}&until={end}&limit=100` | No |
| Post insights | `/{post_id}/insights?metric=post_impressions,post_impressions_unique,post_engaged_users,post_clicks` (top 25 posts only) | No — per-post, skip on failure |

### `src/meta/instagram/extractor.py`
- Input: `BrandConfig`, `start_date`, `end_date`, `api_version`
- Uses `brand_config.page_access_token` for all IG API calls — the Page Access Token is valid for linked Instagram Business account endpoints (`instagram_manage_insights` permission)
- Returns: `InstagramResult` dict with keys: `account`, `media`, `account_insights`
- `account` call is critical

**Endpoints (all validated):**

| Call | Endpoint | Critical? |
|---|---|---|
| Account | `/{ig_id}?fields=id,username,name,followers_count,follows_count,media_count` | Yes |
| Media | `/{ig_id}/media?fields=id,caption,media_type,media_product_type,permalink,timestamp,like_count,comments_count&limit=100` | No |
| Account insights | `/{ig_id}/insights?metric=reach&period=day&metric_type=time_series&since={start}&until={end}` | No |
| Media insights | `/{media_id}/insights?metric=views,reach,saved,likes,comments,shares` (top 50 media items) | No — per-item, skip on failure |

**Note:** IG media is filtered client-side to posts within the `[start_date, end_date]` window using the `timestamp` field.

### `src/meta/shared/consolidator.py`
- Input: `FacebookResult | None`, `InstagramResult | None`, `BrandConfig`, `month_str`
- Output: `BrandResult` — a single dict ready for reporter, containing:
  - `account_summary` dict
  - `content_summary` dict
  - `audience_summary` dict
  - `messages_summary` dict
  - `top_content` list (top 5 by reach → fallback views → fallback likes+comments+shares+saves)
  - `flat_rows` list of dicts (one row per metric per post/account)
- `None` inputs produce `null`-filled structures, never KeyErrors

### `src/meta/shared/reporter.py`
- Input: `BrandResult`, `output_dir: Path`
- Writes all 8 files:
  1. `account_summary.json`
  2. `content_summary.json`
  3. `audience_summary.json`
  4. `messages_summary.json`
  5. `top_content.json`
  6. `monthly_metrics_flat.csv`
  7. `monthly_metrics_pretty.xlsx` — 5 sheets: Overview, Facebook, Instagram, Top Content, Flat Data
  8. `monthly_analysis.md` — data populated, human-readable, follows required section structure

### `scripts/meta/run_monthly.py`
- CLI args: `--month YYYY-MM` (required), `--brand <slug>|all` (default: `all`)
- Loads `.env` via `python-dotenv`, searching upward from script location to workspace root
- Calls `validate_all()` from `meta_config.py` before any API calls
- Iterates active brands from `BRAND_ENV_MAP`
- Calls FB extractor → IG extractor → consolidator → reporter per brand
- Exit code 0 if all brands complete (even with partial warnings)
- Exit code 1 if any brand has a critical auth failure
- Prints progress: `[brand] FB: OK | IG: OK → output written`

---

## Skill

**Location:** `.claude/skills/social-metrics-meta-monthly/SKILL.md`

The skill instructs Claude to:
- Ask for `--month YYYY-MM` if not provided in the prompt
- Validate the format
- Run `python scripts/meta/run_monthly.py --month {month}` from the domain root
- Report what was generated

---

## Output Files (per brand per month)

Path: `output/meta/{brand_slug}/YYYY-MM/`

| File | Content |
|---|---|
| `account_summary.json` | FB + IG account KPIs, consolidated totals, null where unavailable |
| `content_summary.json` | Post counts, platform breakdown, aggregate performance |
| `audience_summary.json` | Follower counts, growth, demographic signals (null if API doesn't return) |
| `messages_summary.json` | FB inbox signals; `status: "pending"` for IG DMs (Phase 1) |
| `top_content.json` | Top 5 posts ranked: reach → views → likes+comments+shares+saves → timestamp (most recent as tiebreaker) |
| `monthly_metrics_flat.csv` | One row per post per metric: brand, month, platform, media_id, metric_name, metric_value, etc. |
| `monthly_metrics_pretty.xlsx` | 5 sheets: Overview, Facebook, Instagram, Top Content, Flat Data |
| `monthly_analysis.md` | Human report with all 9 required sections, data populated, null fields labeled "Not available" |

---

## Error Handling

| Scenario | Behavior |
|---|---|
| Missing required env var | `validate_all()` raises `EnvironmentError` listing all missing vars, exit code 1 before any API call |
| Invalid `--month` format | `ValueError` with example, exit code 1 |
| FB page token 401/403 | Log error with masked token, skip FB for that brand, continue with IG |
| IG account 401/403 | Log error, skip brand entirely, continue with next brand |
| Any API endpoint returns error on best-effort field | Log warning, set field to `null`, continue |
| Rate limit response (429 / error codes 32/17/4) | Exponential backoff, retry up to 3 times |
| Network timeout | Retry up to 3 times with backoff |

---

## Security

- All secrets read from `SOCIAL_METRICS_*` env vars only
- `.env` loaded via `python-dotenv`, searched from script location upward — workspace root `.env` is found automatically
- Token masking in all logs: `value[:4] + "..." + value[-4:]`
- No tokens in output files, markdown, CSV headers, or xlsx sheets
- No tokens printed to stdout under any circumstances

---

## Dependencies

Add to `requirements.txt`:
- `python-dotenv` — env loading
- `openpyxl` — xlsx generation

Everything else uses Python 3.10+ stdlib (`urllib`, `json`, `csv`, `pathlib`, `dataclasses`, `argparse`).

---

## API Version

`v25.0` — matches `META_GRAPH_VERSION` in the global `.env`.

---

## What is explicitly out of scope (Phase 1)

- TikTok
- Page Access Token derivation from System User Token
- Raw → staging → processed staged pipeline
- Scheduling / cron
- IG DM inbox extraction
- Facebook audience demographics (API requires advanced permissions — left as `null` with note)
- Automated token refresh

