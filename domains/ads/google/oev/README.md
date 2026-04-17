# Google Ads OEV — Domain

## Status: Active (pipeline in root)

The Google Ads OEV pipeline is the first and currently active pipeline in this workspace.

**The pipeline code, data, and outputs live in root** — not in this directory. This directory contains domain-specific context only.

## Where Things Live

| What | Path |
|---|---|
| Phase 1 extraction | `scripts/run_phase1_extract.sh`, `scripts/run_gaql.py` |
| GAQL queries | `queries/*.sql` |
| Raw CSV data | `data/raw/` |
| Phase 2 diagnostic | `output/fase-2/` |
| Phase 3 rehab SOP | `output/fase-3/` |
| Skills | `.claude/skills/google-ads-phase1-extract/` |
| | `.claude/skills/google-ads-phase2-diagnostic/` |
| | `.claude/skills/google-ads-phase3-campaign-rehab/` |

## Why This Directory Exists
As the workspace scales to multiple domains (Meta Ads, ClickUp, GHL, etc.), each domain needs isolated context. This `CLAUDE.md` provides OEV-specific business context that supplements the root-level global context.

## Future
If the workspace migrates to a fully domain-isolated structure, the pipeline code and data would move here. That migration is not planned for the current phase.
