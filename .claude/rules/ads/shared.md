---
paths:
  - "scripts/**"
  - "queries/**"
  - "data/**"
  - "output/**"
  - "domains/ads/**"
---

# Ads — Shared Rules

## Default Posture
All ads pipelines default to **read-only**. Never mutate campaigns, conversions, assets, or configurations unless an explicit skill or instruction authorizes it.

## Signal Quality Over Vanity Metrics
- Do not assume that more conversions = better conversions.
- Do not optimize toward cheap leads without validating signal quality.
- Prioritize signal quality, search intent alignment, structure quality, and post-click fit.

## Data Handling
- CSV exports go into domain-specific `data/raw/` directories.
- Diagnostics go into domain-specific `output/` directories.
- If a query or extraction fails, reduce complexity before retrying.
- If a CSV is empty, state it clearly and do not invent conclusions.

## Analysis Standards
- Ground every recommendation in actual data. No intuition-only proposals.
- If data is missing, say so and continue with what is available.
- Reports must end with actions, not summaries.

## Cross-Platform
These rules apply to Google Ads, Meta Ads, and any future ads platform added to this workspace.
