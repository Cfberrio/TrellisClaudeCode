# Trellis — Multi-Domain Workspace

Workspace operativo para pipelines de ads, ops, content y automatización de Trellis.

---

## Active Pipeline: Google Ads OEV

El pipeline canónico activo es Google Ads para OEV. Vive en **root** y no debe moverse.

| Path | Role |
|---|---|
| `scripts/run_gaql.py` | GAQL query runner (Python) |
| `scripts/run_phase1_extract.sh` | Phase 1 extraction orchestrator |
| `queries/*.sql` | 8 GAQL query files |
| `data/raw/` | CSV exports from Google Ads API |
| `output/fase-2/` | Phase 2 diagnostic outputs |
| `output/fase-3/` | Phase 3 campaign rehab SOP outputs |
| `prompts/` | Prompt documentation |
| `start.sh` | Workspace launcher (venv + .env + claude) |
| `.env` / `.env.example` | Google Ads API credentials |
| `requirements.txt` | Python dependencies (`google-ads`) |

### Skills (active — do not modify)

| Skill | What it does |
|---|---|
| `/google-ads-phase1-extract` | Extracts Google Ads data → `data/raw/` |
| `/google-ads-phase2-diagnostic` | Reads `data/raw/` → writes `output/fase-2/` |
| `/google-ads-phase3-campaign-rehab` | Reads fase-2 + fase-3 outputs → writes `output/fase-3/` |

### Workflow

```
Phase 1: /google-ads-phase1-extract     → data/raw/*.csv
Phase 2: /google-ads-phase2-diagnostic  → output/fase-2/YYYY-MM-DD_phase2_diagnostic.md
Phase 3: /google-ads-phase3-campaign-rehab → output/fase-3/YYYY-MM-DD_phase3_campaign_rehab.md
```

---

## Workspace Architecture

### What lives where

| Location | Purpose |
|---|---|
| **Root** | Active Google Ads OEV pipeline (scripts, queries, data, output) |
| `CLAUDE.md` | Global workspace context (identity, brands, workflows, standards) |
| `.claude/skills/` | Active skills powering the Google Ads OEV pipeline |
| `.claude/rules/` | Modular context rules loaded by Claude Code runtime |
| `.claude/agents/` | Subagent definitions for specialized tasks |
| `domains/` | Scaffold for future pipelines and domains |

### Rules (`.claude/rules/`)

| File | Scope | Loads |
|---|---|---|
| `00-global.md` | Trellis identity, writing rules, output standards | Always |
| `10-repo-map.md` | Workspace architecture map | Always |
| `ads/shared.md` | Shared ads pipeline rules | When working in ads paths |
| `ads/google.md` | Google Ads platform specifics | When working in ads/google paths |
| `ads/meta.md` | Meta Ads placeholder | When working in ads/meta paths |
| `ops/social-automation.md` | Social automation rules (webhooks, DM safety, Meta policy) | When working in social-automation paths |
| `ops/notion.md` | Notion placeholder | When working in ops/notion paths |
| `ops/clickup.md` | ClickUp rules | When working in ops/clickup paths |
| `ops/ghl.md` | GHL / CRM rules | When working in ops/ghl paths |
| `content/editing.md` | Content & editing rules | When working in content paths |

### Agents (`.claude/agents/`)

| Agent | Purpose |
|---|---|
| `ads-researcher` | Research terms, competition, benchmarks before diagnostics |
| `ads-diagnostic` | Lightweight health checks on ads CSVs |
| `workflow-organizer` | Convert notes/meetings into ClickUp-ready tasks, briefs, SOPs |

These agents are auxiliary. They do not replace the active skills.

### Domains scaffold (`domains/`)

| Domain | Status |
|---|---|
| `domains/ads/google/oev/` | Context docs for active OEV pipeline (data still in root) |
| `domains/ads/meta/discipline-rift/` | Active Meta Ads pipeline for DR brand |
| `domains/ops/social-automation/discipline-rift/` | Social automation for DR (Supabase + Meta webhooks) |
| `domains/ops/notion/` | Future Notion integration |
| `domains/ops/clickup/` | Future ClickUp workflows |
| `domains/ops/ghl/` | Future GHL / CRM operations |
| `domains/content/editing/` | Future content editing workflows |

Each domain directory has its own `CLAUDE.md` and `README.md` with domain-specific context.

---

## How to Grow Without Breaking Things

1. **New domains**: create scaffold in `domains/` first. Each domain gets its own `CLAUDE.md`, `README.md`, isolated `data/`, `output/`, `scripts/`.
2. **New skills**: create new skills in `.claude/skills/` with descriptive names. Never rename or modify existing active skills.
3. **New rules**: add to `.claude/rules/` with appropriate `paths:` frontmatter. Rules without `paths:` load always.
4. **New agents**: add to `.claude/agents/`. Agents are supplementary, not replacements for skills.
5. **Migrations**: moving active pipeline code (e.g., from root to `domains/`) is a future Phase 3 decision. Do not attempt without explicit planning.

---

## What Was Intentionally NOT Changed

- Skills `google-ads-phase1-extract`, `google-ads-phase2-diagnostic`, `google-ads-phase3-campaign-rehab` remain exactly as created
- `scripts/`, `queries/`, `data/raw/`, `output/` paths stay in root
- `start.sh` launcher unchanged
- `.env` / `.env.example` / `requirements.txt` unchanged
- `.claude/settings.local.json` permissions unchanged
- Slash commands (`/google-ads-phase1-extract`, etc.) work exactly as before
- No active pipeline code was moved into `domains/`
- No skills were renamed to a namespaced convention

---

## Future Phase 3 Migration Options

These are potential future changes that were intentionally deferred:

- **Move Google Ads OEV pipeline** from root to `domains/ads/google/oev/` (requires updating all 3 skills, scripts, and path references)
- **Unify skill naming** to `{domain}-{platform}-{brand}-{phase}-{action}` convention (requires creating new skills and deprecating old ones, not renaming)
- **Add `@imports`** in `CLAUDE.md` to reference rules directly (reduces duplication further but adds a dependency on import support)
- **Activate Meta Ads DR pipeline** in `domains/ads/meta/discipline-rift/` with real scripts and skills
- **Connect ClickUp / GHL / Notion domains** with API integrations and dedicated skills
- **Trim `CLAUDE.md` further** once `.claude/rules/` loading is confirmed reliable across all runtimes (Cursor + Claude Code CLI)

---

## Dependencies

| Tool | Use | Setup |
|---|---|---|
| Python 3 + venv | Google Ads extraction scripts | `python3 -m venv .venv && pip install -r requirements.txt` |
| Google Ads API credentials | Data extraction | See `google_ads_oauth_refresh_token.py` and `.env.example` |
