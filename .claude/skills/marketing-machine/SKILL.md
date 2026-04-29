---
name: marketing-machine
description: Build the system that produces customer-generated ad creative continuously using Hormozi's Marketing Machine playbook (12-Marketing-Machine) — UGC sourcing, lifecycle ads (before/during/after), social/event/comms scrape, bonus/award mechanism, testimonial competition, 6-point testimonial script, cadence. Use when the user wants steady flow of testimonial/UGC ads, lifecycle-ads system, testimonial competition, event capture, social-scrape for organic winners, or scale ad creative without founder on camera. Trigger phrases include "UGC system", "testimonial pipeline", "marketing machine", "lifecycle ads", "testimonial competition", "event capture", "scrape social", "founder not on camera". Do NOT use for paid-ad assembly (→ /ads), single-customer testimonial extraction (load only the 6-point script note), or pure brand strategy (→ /branding). Routes to Trellis-Brain Obsidian vault `12-Marketing-Machine/` notes.
---

# marketing-machine

UGC sourcing system + customer-evidence ad pipeline + lifecycle ads. Source of truth: `12-Marketing-Machine/` in the Trellis-Brain Obsidian vault.

## Vault root
The Trellis-Brain Obsidian vault root is machine-specific. Configure it via the Obsidian MCP server — see [.claude/docs/TEAM-SETUP-MCP.md](../../docs/TEAM-SETUP-MCP.md). All note paths in this skill are **relative to the `00-Trellis-Core/Strategy-Models/` folder inside that vault**.

## Use when
- "How do I get a steady flow of testimonial / UGC / customer-evidence ads?"
- "Build a lifecycle-ads system."
- "Run a testimonial competition."
- "Capture event content."
- "Scrape social media for organic winners that should become paid ads."
- Founder-not-on-camera scaling questions.

## Do not use when
- Pure paid-ad assembly / hook × meat × CTA construction → `/ads`.
- Pure brand strategy → `/branding`.
- Single-customer testimonial extraction (just the script) → load only `12-Marketing-Machine/Hormozi-6-Point-Testimonial-Script.md`.

## Canonical-home logic
12-Marketing-Machine canonical for the UGC sourcing system. Hooks canonical in 07. Ad assembly canonical in 08. Bonuses canonical in 01.

## Retrieval order

**Always load (umbrella + cadence):**
1. `12-Marketing-Machine/Hormozi-Marketing-Machine-System.md` — umbrella + 7 nodes.
2. `12-Marketing-Machine/Hormozi-Marketing-Machine-Cadence.md` — operational rhythm.

**Load on intent (the node the user is working on):**
- Lifecycle ads (before/during/after moments) → `Hormozi-Lifecycle-Ads.md`.
- Organic-to-paid sourcing → `Hormozi-Social-Media-Scrape.md`.
- Event content capture → `Hormozi-Event-Capture-Playbook.md`.
- Support/comms scraping for testimonial seeds → `Hormozi-Communications-Scrape.md`.
- Bonus-unlock as testimonial-trade currency → `Hormozi-Bonus-And-Award-Mechanism.md`.
- Run a competition → `Hormozi-Testimonial-Competition.md`.
- Extraction script for one customer → `Hormozi-6-Point-Testimonial-Script.md`.

**Optional — only when composing a full ad downstream:**
- Hook layer → `07-Hooks/Hormozi-Hook-Definition.md`.
- Assembly target → `08-GOATed-Ads/Hormozi-Ad-Assembly-Process.md`.
- Bonus-unlock currency canonical → `01-100M-Offers/Hormozi-Bonuses.md`.

## Context warnings
- Do not collapse with `/branding` — different layer. This is asset *production*, not brand *strategy*.
- Lifecycle-Ads is canonical here, not in `/ads`. `/ads` should *reference* but not duplicate.
- Do not load all 7 nodes by default. Route by intent.

## Output expectations
- For a system build: state which of the 7 nodes the user is missing, prescribe the activation sequence (which node to install first based on existing customer base + ad cadence target).
- For a testimonial competition: walk Bonus-And-Award + Testimonial-Competition + 6-Point-Script as one unit, name the prize structure and timing.
- For a single testimonial extraction: 6-Point-Script only — verbatim, no paraphrasing.
- End with the next operational install (node, cadence, owner), not a strategy paragraph.
