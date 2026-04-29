# Push-Readiness Report — Trellis Workspace

Single-pass audit + safe-fix log for team push and team usage. Ran 2026-04-29.

---

## TL;DR

Both this Claude Code repo and the supporting Obsidian vault integration are **push-ready** with one manual step before push: review the staged untrackings (59 files, 22k lines removed from git index — all client data / PII / personal settings) and confirm with `git status` before any commit/push.

---

## What was fixed (auto-applied, safe)

### Push safety
- Untracked `.claude/settings.local.json` (Anthropic convention: never version-controlled).
- Untracked all raw client CSVs: 14 Google Ads + 12 Meta DR.
- Untracked all school-outreach PII: Apify dumps, school lists, `ocps_emails.txt`, `PrivateSchoolList.xls`, `SchoolList.xls`.
- Untracked legacy school-outreach archive + first-pass discovery CSVs containing email/phone fields.
- Untracked official-rebuild safety-snapshot CSVs (school-outreach validated lists).
- Files preserved on local disk — only removed from git index.

### `.gitignore` expansion
Replaced 8-line `.gitignore` with comprehensive coverage:
- `.claude/settings.local.json`
- `.env`, `.env.local`, `**/.env` (with `!**/.env.example` exemption)
- `hormozi-books/` (copyrighted PDFs)
- `remotion/whisper.cpp/`, `remotion/public/`, `remotion/TESTDRVIDEO/`, `remotion/out/`
- `data/raw/*.{csv,json,xls,xlsx,txt}` and `domains/**/data/raw/**/*.{csv,json,xls,xlsx,txt}`
- `domains/ops/school-outreach/**/data/processed/`, `output/fase-1/*.csv`, `output/fase-2/*.csv`, `archive/`
- `node_modules/`, `**/node_modules/`, root `/package-lock.json` stub
- All `.gitkeep` and `.env.example` whitelisted back

### Team portability
- All 8 Hormozi SKILL.md files: replaced absolute `/Users/cberrio04/...` vault root with portable reference pointing teammates to `TEAM-SETUP-MCP.md`.
- `HORMOZI-DOMAIN-OVERVIEW.md` (2 path lines) and `HORMOZI-SKILL-ROUTING-MANIFEST.md` (1 path line): same treatment.
- Result: `grep -r /Users/cberrio04 .claude/ CLAUDE.md README.md` returns 0 hits.

### Team docs
- Created `TEAM-SETUP-MCP.md` — clone-day setup for `.env`, Obsidian MCP server, vault wiring.
- Created `TEAM-USAGE-NOTES.md` — repo shape, slash commands, what's tracked vs. ignored, first-day checklist, operating norms.
- Created this report.

### Skill quality
- No body-level changes needed. Descriptions verified under 1024-char limit (range 753–988).
- Routing manifest still source of truth; skill bodies still aligned.

---

## What was intentionally NOT touched

| Why | What |
|---|---|
| Active OEV pipeline canonical paths | `scripts/`, `queries/`, `data/raw/.gitkeep`, `output/`, `prompts/`, `start.sh` — preserved exactly. |
| Aesthetic cleanup | No skill body rewrites, no manifest reformatting. |
| Vault integrity | All 29 cited Hormozi note paths resolved during prior audit. No vault edits made (per user constraint). |
| Other-domain SKILL.md files | `google-ads-phase*`, `ads-meta-dr-phase*`, `social-metrics-meta-monthly` left as-is — already use repo-relative paths. |
| `.mcp.json` | Apify-only config kept. Obsidian MCP intentionally user-scoped (not project-scoped) because vault path varies per teammate. Documented in `TEAM-SETUP-MCP.md`. |
| Generated reports in `output/` | `.md` reports stay tracked (interpretation, not raw data). |
| Already-tracked `output/` markdown reports inside school-outreach | Not gitignored — they may contain client interpretation but not raw PII. Flagged below as manual review item. |
| Git history rewrite | Not done. Untrackings only affect future commits. **The CSVs and PII still exist in past commits.** See blockers. |

---

## Remaining blockers (manual action required)

### 🔴 HIGH — Git history still contains the secrets/PII

`git rm --cached` only removes from the **index**. The 26 client-data CSVs and PII files (school lists, emails) are still in past commits. If this repo is pushed to a public remote, anyone can recover them with `git log -p`.

**Decision required:** is the planned remote private (team-only org) or public?
- Private team remote → acceptable risk, can push as-is.
- Public remote → must `git filter-repo` or BFG before push to scrub history. **Do not push to public until done.**

### 🟡 MEDIUM — School-outreach `output/` markdown reports

Files like `domains/ops/school-outreach/discipline-rift/output/fase-3/summaries/phase3_full_summary*.md` are tracked. They likely contain interpretations of the raw PII. Spot-check before push:

```bash
grep -liE "(@gmail|@yahoo|@aol|phone|address)" domains/ops/school-outreach/**/output/**/*.md 2>/dev/null
```

If hits → either untrack or redact.

### 🟡 MEDIUM — `.env` already exists locally and was previously gitignored

Confirmed `.env` is gitignored and not in `git ls-files`. No leak risk on push. But: rotate the Google Ads tokens in your `.env` before adding any teammate, since they're tied to your personal OAuth grant.

### 🟢 LOW — `domains/ads/meta/discipline-rift/data/raw/.gitkeep` had unstaged tweak

Likely whitespace-only modification picked up by some editor. Stage it or revert it; either way harmless.

### 🟢 LOW — Remaining untracked dirs not covered by `.gitignore` patterns

Examples: `domains/cts/` (new untracked dir), `remotion/scripts/`, `remotion/src/components/`, `remotion/src/lib/`. These look like legitimate code that should probably be tracked. Decide per-folder before commit.

---

## Final verdict

| Item | Status |
|---|---|
| Claude Code repo push-ready (private remote) | **YES** — pending review of staged untrackings |
| Claude Code repo push-ready (public remote) | **NO** — git history still contains client data; needs scrub |
| Obsidian vault push-ready | **N/A** — vault is a separate repo; not touched in this pass |
| Team-usable after clone (Mac, Obsidian installed) | **YES** — once teammate follows `TEAM-SETUP-MCP.md` |

---

## Recommended next manual action before push

1. `git status` — confirm the 59 staged deletions are exactly the ones listed in `git diff --cached --stat`. None of them should be code or skill files.
2. Decide remote visibility (private team org vs. public). If public → run history scrub before push.
3. Spot-check school-outreach `output/*.md` for embedded PII (one grep, see above).
4. Stage the `.gitignore` rewrite + 11 patched skills/docs + 3 new docs + the modifications already in `git status`. Build one commit (or split: "chore: untrack secrets/raw data + portable paths" + "docs: team setup + push-readiness").
5. Push to a **private** remote first. Pull from a clean directory on a second machine to verify clone-and-go works end-to-end with `TEAM-SETUP-MCP.md`.
