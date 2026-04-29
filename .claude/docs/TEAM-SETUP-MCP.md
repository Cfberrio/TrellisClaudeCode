# Team Setup — MCP & Vault Configuration

What every teammate needs after cloning this repo so the Hormozi skills and vault routing work end-to-end.

---

## 1. Prerequisites

- **Claude Code** installed (`claude` CLI on PATH).
- **Python 3.10+** for the Google Ads / Meta extraction pipelines (see `requirements.txt`).
- **Node 20+** for the `remotion/` workspace (only if doing video work).
- A local copy of the **Trellis-Brain Obsidian vault**. Path is up to you — pick a stable location.
- Obsidian app installed if you want to view notes interactively (not required for skills).

---

## 2. Required environment variables

Copy `.env.example` → `.env` and fill in real values.

```
cp .env.example .env
# then edit .env
```

The repo-root `.env` covers Google Ads OEV pipeline credentials. Domain-specific pipelines have their own `.env.example` files inside their folders (Meta DR, school outreach). Same `cp` pattern applies.

`.env` is **always gitignored** in this repo. Never commit it. Never paste tokens into Claude transcripts.

---

## 3. Obsidian MCP server (required for Hormozi skills)

The Hormozi first-wave skills (`/offers`, `/pricing*`, `/price-*`, `/branding`) read notes from the Trellis-Brain Obsidian vault via the **Obsidian MCP server** (`mcp__obsidian__*` tools).

This MCP server is **user-scoped, not project-scoped** — it lives in your personal Claude Code settings, not in `.mcp.json`. Add it once per machine:

### Option A — Claude Code CLI (recommended)

```bash
claude mcp add obsidian \
  --scope user \
  -- npx -y @modelcontextprotocol/server-obsidian "/absolute/path/to/Trellis-Brain"
```

Replace `/absolute/path/to/Trellis-Brain` with your local vault root (the directory that contains `00-Trellis-Core/`).

### Option B — Edit `~/.claude/settings.json` directly

```json
{
  "mcpServers": {
    "obsidian": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-obsidian", "/absolute/path/to/Trellis-Brain"]
    }
  }
}
```

Restart Claude Code after either option. Verify:

```bash
claude mcp list
# obsidian should appear with status "connected"
```

### Why user scope, not project scope

Vault location varies per teammate. Hardcoding it into the project `.mcp.json` would break for everyone whose vault sits elsewhere. User-scoped config keeps each machine's path local while skills stay portable.

---

## 4. How skills reference the vault

Hormozi skills do **not** contain absolute paths. They reference notes relative to the `00-Trellis-Core/Strategy-Models/` folder inside whichever vault you configured. Examples:

- `01-100M-Offers/Hormozi-Value-Equation.md`
- `13-Pricing/Hormozi-Pricing-Rules.md`
- `11-Price-Raise/Hormozi-RAISE-Letter.md`

When a skill fires, Claude calls `mcp__obsidian__obsidian_get_file_contents` with the relative path. The Obsidian MCP server resolves it against the vault root you set in step 3.

---

## 5. The vault itself

The Trellis-Brain vault is a **separate Obsidian repo / Drive folder**, not part of this Claude Code repo. Coordinate with the team on:

- Where the vault lives (Drive sync, Git, iCloud, local-only).
- How updates to Hormozi notes are propagated.
- Who owns canonical-home decisions (see `HORMOZI-SKILL-ROUTING-MANIFEST.md`).

If the vault is missing or the MCP server isn't configured, Hormozi skills will fire but fail when they try to load notes. The skill body will say "use Obsidian MCP" and the tool call will error. That's the signal to come back here.

---

## 6. Other MCPs in this repo

`.mcp.json` (project-scoped, shared across team) currently only declares the **Apify** HTTP server, used by Meta Ads and school-outreach pipelines. Apify auth is handled via `mcp__apify__authenticate` on first use — no env var required.

Other personal MCPs (Playwright, Canva, Google Drive, Obsidian) are **user-scoped** in `~/.claude/settings.json`. They are intentionally not in `.mcp.json` because their configs are personal.

---

## 7. Quick verification after setup

Run from repo root:

```bash
# Confirm .env loaded
python3 -c "import os; print('GOOGLE_ADS_DEVELOPER_TOKEN:', 'SET' if os.getenv('GOOGLE_ADS_DEVELOPER_TOKEN') else 'MISSING')"

# Confirm Obsidian MCP connected
claude mcp list | grep obsidian

# Confirm Hormozi vault folder is reachable from your MCP config
# (replace path with whatever you configured)
ls "/your/vault/path/00-Trellis-Core/Strategy-Models/" | head -5
```

If all 3 succeed → you're ready.
