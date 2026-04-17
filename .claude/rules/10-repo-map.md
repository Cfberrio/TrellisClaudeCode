# Repo Map — Workspace Architecture

## Root = Active Pipeline (Google Ads OEV)
The root of this workspace contains the **canonical, active** Google Ads pipeline for OEV. These paths are in production use and must not be moved, renamed, or restructured without explicit instruction:

| Path | Role |
|---|---|
| `scripts/` | Python runner (`run_gaql.py`) and bash orchestrator (`run_phase1_extract.sh`) |
| `queries/` | 8 GAQL query files for Phase 1 extraction |
| `data/raw/` | CSV exports from Google Ads API |
| `output/fase-2/` | Phase 2 diagnostic markdown outputs |
| `output/fase-3/` | Phase 3 campaign rehab SOP outputs |
| `prompts/` | Prompt documentation for Phase 1 |
| `start.sh` | Workspace launcher (activates venv, loads .env, opens claude) |
| `.env` / `.env.example` | Google Ads API credentials |
| `requirements.txt` | Python dependencies (google-ads) |

## Skills (Active — Do Not Modify)
Three skills power the Google Ads OEV pipeline. They reference root-level paths and must remain exactly as they are:

- `.claude/skills/google-ads-phase1-extract/SKILL.md` → extracts data to `data/raw/`
- `.claude/skills/google-ads-phase2-diagnostic/SKILL.md` → reads `data/raw/`, writes `output/fase-2/`
- `.claude/skills/google-ads-phase3-campaign-rehab/SKILL.md` → reads fase-2 + fase-3 outputs, writes `output/fase-3/`

## `domains/` = Future Scaffold
New pipelines and domains live under `domains/`. Each domain has its own `CLAUDE.md`, `README.md`, and isolated data/output paths.

```
domains/
  ads/google/oev/                          — context docs for the active OEV pipeline (data still in root)
  ads/meta/discipline-rift/                — active Meta Ads pipeline for DR brand
  ops/social-automation/discipline-rift/   — social automation for DR (Supabase + Meta webhooks)
  ops/notion/                              — future Notion integration
  ops/clickup/                             — future ClickUp workflows
  ops/ghl/                                 — future GHL / CRM operations
  content/editing/                         — future content editing workflows
```

## `.claude/rules/` = Modular Context
Rules provide contextual guidance without bloating every session:

- `00-global.md` → always loaded — Trellis identity, writing rules, output standards
- `10-repo-map.md` → always loaded — this file
- `ads/*` → loaded when working in ads-related paths
- `ops/*` → loaded when working in ops-related paths (includes social-automation)
- `content/*` → loaded when working in content-related paths

## `.claude/agents/` = Subagent Definitions
Auxiliary agents for specialized tasks. They do not replace skills:

- `ads-researcher.md` → research terms, competition, benchmarks
- `ads-diagnostic.md` → lightweight diagnostic checks on CSVs
- `workflow-organizer.md` → convert notes/meetings into structured tasks

## Key Principle
When in doubt about which path to use, check which domain is active. Root paths belong to Google Ads OEV. Everything else belongs under `domains/`.
