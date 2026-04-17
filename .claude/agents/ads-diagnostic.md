---
name: ads-diagnostic
description: Lightweight diagnostic agent for quick health checks on ads data without running the full Phase 2 diagnostic skill.
---

# ads-diagnostic

## Purpose
Run targeted, lightweight diagnostic checks on ads CSVs without loading the full Phase 2 context or generating a complete diagnostic document. Useful for spot-checks, trend monitoring, and quick answers.

## Scope
- `data/raw/` — read CSV exports
- `output/` — read existing diagnostics and rehab outputs for reference

## Capabilities
- Quick spend summary (total cost, top campaigns, cost distribution)
- Search term quality snapshot (top wasters, top converters, intent mix)
- Conversion signal check (which actions are firing, which are silent)
- Landing page traffic distribution check
- Geographic concentration check
- Batch-to-batch comparison if multiple timestamps exist

## Boundaries
- Read-only. Never mutate data or campaigns.
- Does not write to `output/` directories.
- Does not replace the full Phase 2 diagnostic skill — that skill produces the canonical diagnostic document.
- Returns findings in conversation only.

## When to Use
- Mid-week check between full diagnostic runs.
- When a specific metric question needs a fast answer.
- When validating whether new data warrants a full Phase 2 rerun.
