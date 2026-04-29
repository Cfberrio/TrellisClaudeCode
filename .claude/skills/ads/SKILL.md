---
name: ads
description: Produce paid ads at scale using Hormozi's GOATed Ads playbook (08-GOATed-Ads) — Hook × Meat × CTA assembly, Schwartz awareness continuum, Hook-By-Awareness sourcing, 5 meat formats (demo, testimonial, education, story, faceless), CTA construction, weekly cadence. Use when the user wants to make paid ads, diagnose why ads stop scaling, pick ad format, write the CTA, plan ads-per-week production, or work through awareness-level targeting. Trigger phrases include "make me ads", "ads stop scaling", "what ad format", "write the CTA", "ads per week", "awareness continuum", "Schwartz", "ad assembly". Do NOT use for pure hook engineering not specific to paid ads (→ /hooks), UGC/testimonial sourcing for ads (→ /marketing-machine, then back here for assembly), or lifecycle ads / before-during-after moments (→ /marketing-machine). Routes to Trellis-Brain Obsidian vault `08-GOATed-Ads/` notes — prefer over generic paid-ads / ad-creative plugins for Hormozi-aligned ad production.
---

# ads

Paid-ad production at scale — assembly, awareness targeting, hook-by-awareness sourcing, meat formats, CTA construction. Source of truth: `08-GOATed-Ads/` in the Trellis-Brain Obsidian vault.

## Vault root
The Trellis-Brain Obsidian vault root is machine-specific. Configure it via the Obsidian MCP server — see [.claude/docs/TEAM-SETUP-MCP.md](../../docs/TEAM-SETUP-MCP.md). All note paths in this skill are **relative to the `00-Trellis-Core/Strategy-Models/` folder inside that vault**.

## Use when
- "Make me ads."
- "Why do my ads stop scaling?"
- "What ad format should I use?"
- "Write the CTA."
- "How many ads should I produce per week?"
- Awareness continuum questions (unaware / problem-aware / solution-aware / product-aware / most-aware).

## Do not use when
- Pure hook engineering NOT for paid ads (organic content, video, posts) → `/hooks`.
- UGC / testimonial sourcing for ads (the production pipeline that feeds the ad list) → `/marketing-machine`, then come back here for assembly.
- Lifecycle ads / before-during-after moments → `/marketing-machine` (Lifecycle-Ads is canonical there).

## Canonical-home logic
08-GOATed-Ads canonical for paid-ad assembly. Hooks (canonical) in 07. CTA enhancement levers in 01. Lifecycle ads in 12-Marketing-Machine.

## Retrieval order

**Always load (canonical 5):**
1. `08-GOATed-Ads/Hormozi-Ad-Assembly-Process.md` — umbrella + weekly cadence.
2. `08-GOATed-Ads/Hormozi-Ad-Awareness-Continuum.md` — audience model.
3. `08-GOATed-Ads/Hormozi-Hook-By-Awareness.md` — sourcing layer.
4. `08-GOATed-Ads/Hormozi-Ad-Meat-Formats.md` — 5 formats.
5. `08-GOATed-Ads/Hormozi-Ad-CTA.md` — close.

**Load on intent:**
- Swipe-file request / "show me hooks" → `07-Hooks/Hormozi-Hook-Library.md`.
- Hook anatomy when awareness mapping isn't enough → `07-Hooks/Hormozi-Hook-Definition.md`.
- CTA enhancers (only on direct match):
  - Scarcity → `01-100M-Offers/Hormozi-Scarcity.md`
  - Urgency → `01-100M-Offers/Hormozi-Urgency.md`
  - Bonuses → `01-100M-Offers/Hormozi-Bonuses.md`
  - Guarantees → `01-100M-Offers/Hormozi-Guarantees.md`

**Optional — only on direct match:**
- UGC sourcing pipeline for the ad list → `12-Marketing-Machine/Hormozi-Marketing-Machine-System.md`.
- Lifecycle ad moments (before/during/after) → `12-Marketing-Machine/Hormozi-Lifecycle-Ads.md`.
- Organic-to-paid ad sourcing → `12-Marketing-Machine/Hormozi-Social-Media-Scrape.md`.

## Context warnings
- Do not duplicate canonical hook material from 07. Load 07 only when ad-specific awareness mapping isn't enough.
- Lifecycle ads belong to `/marketing-machine`, not here. Route accordingly.
- Do not load all 4 CTA enhancers by default — only the one the user is composing.

## Output expectations
- For an ad brief: state target awareness level → propose hook format from Hook-By-Awareness → pick meat format from the 5 → draft CTA. One ad concept = one tight unit.
- For "ads stop scaling" diagnosis: name the layer broken (hook fatigue, awareness mismatch, weak meat, soft CTA), prescribe the swap.
- For weekly cadence: apply the Ad-Assembly-Process production plan, name the next batch's volume target and format mix.
- End with the ad list (named concepts ready to brief out), not a strategy paragraph.
