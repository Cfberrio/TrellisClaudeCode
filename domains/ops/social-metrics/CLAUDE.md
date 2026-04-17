# CLAUDE.md — Social Metrics Domain

## Purpose
This domain handles monthly social metrics extraction and reporting for Trellis brands.

Current active scope:
- Meta only
  - Facebook
  - Instagram

Future scope:
- TikTok
- Not active yet
- Do not mix TikTok into the Meta pipeline until a separate extraction path is explicitly implemented

## Brands
Active brands:
- Cheese To Share
- Discipline Rift
- DR Volleyball Club

Use the brand slugs exactly as:
- `cheese_to_share`
- `discipline_rift`
- `dr_volleyball_club`

## Core objective
For each active brand, extract monthly Facebook + Instagram metrics and generate one consolidated Meta output per brand.

The output is human-first and should be intuitive.

Primary rep- `monthly_analysis.md`

Supporting files:
- `account_summary.json`
- `content_summary.json`
- `audience_summary.json`
- `messages_summary.json`
- `top_content.json`
- `monthly_metrics_flat.csv`
- `monthly_metrics_pretty.xlsx`

## Reporting rule
Always work by **calendar month**.

Never default to:
- last 7 days
- last 28 days
- rolling windows
- arbitrary lookback ranges

The runner must accept:
- `--month YYYY-MM`

From that value, derive internally:
- start date = first day of month
- end date = last day of month

Example:
- `2026-04` → `2026-04-01` through `2026-04-30`

## Output rule
Output must always be consolidated by brand.

Do not create separate final output folders for:
- Facebook
- Instagram

Correct pattern:
- `output/meta/{brand}/YYYY-MM/`

Inside each month folder, Facebook + Instagram must be combined into one final brand-level Meta report.

Use `platform` as an internal field in data structures when needed, but not as separate final output folders.

## Data flow
Expected pipeline shape:
. `raw`
   - platform-specific source pulls
   - Facebook and Instagram may remain separate here

2. `staging`
   - normalize source payloads into a shared schema

3. `processed`
   - merge Facebook + Instagram into a brand-level Meta dataset

4. `output`
   - final human-readable and machine-readable deliverables

## Security rules
This domain uses a shared global `.env` strategy across the wider workspace.

Therefore:
- never use generic `META_*` variables in this domain
- always use `SOCIAL_METRICS_*` namespaced environment variables
- never print secrets in logs
- never write secrets into tracked files
- never hardcode live tokens into source, config, docs, tests, fixtures, markdown, or examples

Allowed:
- variable names
- placeholders
- masked values in errors

Forbidden:
- full token output
- full app secret output
- inline access tokens in scripts or docs

## Required environment strategy
This domain expects namespaced env vars only.

Examples:
- `SOCIAL_METRICS_META_APP_ID`
- `SOCIAL_METRICS_META_APP_SECRET`
- `SOCIAL_METRICS_META_CONFIGURATION_ID`
- `SOCIAL_METRICS_META_USER_ACCESS_TOKEN`

Brand-specific examples:
- `SOCIAL_METRICS_CHEESE_TO_SHARE_PAGE_ID`
- `SOCIAL_METRICS_CHEESE_TO_SHARE_PAGE_ACCESS_TOKEN`
- `SOCIAL_METRICS_CHEESE_TO_SHARE_IG_ID`

- `SOCIAL_METRICS_DISCIPLINE_RIFT_PAGE_ID`
- `SOCIAL_METRICS_DISCIPLINE_RIFT_PAGE_ACCESS_TOKEN`
- `SOCIAL_METRICS_DISCIPLINE_RIFT_IG_ID`

- `SOCIAL_METRICS_DR_VOLLEYBALL_CLUB_PAGE_ID`
- `SOCIAL_METRICS_DR_VOLLEYBALL_CLUB_PAGE_ACCESS_TOKEN`
- `SOCIAL_METRICS_DR_VOLLEYBALL_CLUB_IG_ID`

## Implementation rules
When building or updating this domain:

- keep things simple
- do not overengineer
- do not introduce extra infrastructure unless necessary
- prefer small, auditable scripts
- fail clearly when required config is missing
- validate brand config before running extraction
- validate month format before executing
- treat missing API fields as normal and handle gracefully
- separate extraction from reporting logic
- keep source-of-truth mappings in config, not scattered constants

## Meta extraction rules
Use the validated Page IDs, Page access tokens, and Instagram business account IDs from environment/config.

For Meta:
- Facebook metrics extraction should use page-level access where required
- Instagram metrics extraction should use the validated Instagram business account IDs
- only rely on endpoints already proven valid in this project unless explicitly expanding scope

## Reporting rules
`monthly_analysis.md` is the main deliverable.

It should always combine Facebook + Instagram in one report for the brand.

Minimum report structure:

# {Brand} — Meta Monthly Report — {YYYY-MM}

## Executive Summary

## Cross-Platform Snapshot

## Facebook Summary

## Instagram Summary

## Top Content Across Meta

## Audience Signals

## Messaging / Inbox Signals

## Key Takeaways

## Recommended Next Steps

## Quality bar
Outputs must be:
- readable
- concise
- executive-friendly
- operationally useful
- easy to compare month-to-month

Avoid:
- noisy dumps
- giaaw JSON in markdown
- duplicated platform summaries
- unclear field naming
- hidden assumptions about dates

## Change management
Do not touch unrelated domains.

Do not modify:
- ads pipelines
- social automation pipelines
- TikTok implementation paths
- root-level legacy systems

Scope all changes strictly to:
- `domains/ops/social-metrics/`

## Current status
Current active implementation target:
- Meta monthly extraction for 3 brands

Current non-goals:
- TikTok extraction
- automation scheduling
- dashboarding
- BI tooling
- ad metrics
- cross-domain refactors

## Default working posture
When asked to build inside this domain:
1. inspect current structure first
2. preserve the existing architecture
3. keep output consolidated by brand
4. keep secrets safe
5. prefer month-driven execution
6. stop before expanding into TikTok unless explicitly requested
