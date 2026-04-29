# Team Usage Notes — Trellis Workspace

Quick orientation for a new teammate after `git clone` + `TEAM-SETUP-MCP.md` is done.

---

## Repo shape (one-line reference)

```
/                   active Google Ads OEV pipeline (root = canonical, do not move)
.claude/skills/     skill files — auto-trigger on intent
.claude/docs/       shared routing + setup docs
.claude/rules/      modular context rules
.mcp.json           project-scoped MCP servers (currently Apify only)
domains/            future and active non-OEV pipelines (Meta DR, school outreach, etc.)
remotion/           video workspace (heavy — most of it is gitignored)
hormozi-books/      copyrighted source PDFs (gitignored — never commit)
```

Architecture detail: see root `CLAUDE.md`, `.claude/rules/10-repo-map.md`.

---

## Slash commands you'll actually use

Hormozi first-wave skills (auto-trigger or call explicitly):
- `/offers` — single-offer construction/audit
- `/pricing` — pricing router (picks subskill)
- `/pricing-posture`, `/pricing-model`, `/pricing-plays`, `/price-test`, `/price-raise`
- `/branding` — brand strategy (tightly scoped)

Routing logic and "do not use when" rules: `.claude/docs/HORMOZI-SKILL-ROUTING-MANIFEST.md`.

When a skill misfires: log it using `.claude/skill-evals/hormozi-wave1/live-failure-log-template.md`.

---

## What is NOT in this repo (and why)

| Thing | Why excluded | Where it lives |
|---|---|---|
| Trellis-Brain Obsidian vault | Per-machine path, separate repo | Each teammate's local disk |
| Hormozi book PDFs | Copyright | `hormozi-books/` (gitignored) |
| `.env` files | Secrets | Each teammate's local; `.env.example` shows required keys |
| Raw Google Ads / Meta CSVs | Client metrics, regenerated each pipeline run | `data/raw/` and `domains/**/data/raw/` (gitignored) |
| School outreach PII | School lists, contact emails | `domains/ops/school-outreach/**/data/raw/` (gitignored) |
| Personal Claude settings | Per-user permissions | `~/.claude/settings.json`; `settings.local.json` is gitignored |
| `node_modules/`, `.venv/`, `whisper.cpp/`, `remotion/public/` | Generated / large | All gitignored |

---

## What IS tracked (and committed work depends on it)

- All `SKILL.md` files (skills are the product).
- All `.claude/docs/*.md` (routing manifest, build notes, this file).
- Root `CLAUDE.md` and `.claude/rules/*` (project behavior).
- `requirements.txt`, `start.sh`, query files, scripts.
- `.env.example` files (one per pipeline) — show required keys without leaking values.
- Markdown reports in `output/` (interpretation, not raw data).

---

## First-day checklist

1. Clone repo.
2. Follow `.claude/docs/TEAM-SETUP-MCP.md` end-to-end (`.env`, Obsidian MCP).
3. Open Claude Code in the repo root. Confirm root `CLAUDE.md` loaded automatically.
4. Try a benign Hormozi prompt: *"audit this offer against the Grand Slam definition"* — confirm `/offers` fires and Obsidian notes load.
5. If it errors on note load → MCP setup incomplete. Back to step 2.

---

## Operating norms

- **Never commit `.env`** or any file with credentials. `.gitignore` covers most cases but always `git status` before commit.
- **Never commit raw client data** (CSVs from `data/raw/`). They're gitignored — keep it that way.
- **Skills are versioned**. Improvements come from real failures (`live-failure-log-template.md`), not speculative rewrites. Threshold: 2-of-3 failure pattern (see `LIVE-USE-QA-PLAN.md`).
- **Routing manifest is source of truth**. Skills implement it. If you need to change routing, change the manifest first, then propagate.
- **Active pipeline paths at repo root are canonical.** Do not move/rename `scripts/`, `queries/`, `data/`, `output/`, `prompts/` for the Google Ads OEV pipeline. New pipelines go under `domains/`.
