---
name: pricing-plays
description: Tactical instant-profit pricing plays from Hormozi — 10 specific moves that lift profit immediately without rebuilding the offer or running long tests. Includes 28-day billing, processing-fee passthrough, annual CPI increases, removing free shipping, smart price-anchor displays, etc. Use when the user wants concrete pricing tactics to deploy this week — quick wins, margin lifts, billing changes, fee additions, anchor moves. Trigger phrases include "instant profit", "pricing tactic", "billing change", "processing fees", "annual price bump", "make more money this month from pricing", "quick pricing win", "pricing hack". Do NOT use for posture (→ /pricing-posture), choosing a model (→ /pricing-model), running a structured test (→ /price-test), or raising prices on existing customers via formal letter (→ /price-raise). Routes to Trellis-Brain Obsidian vault `13-Pricing/` notes — prefer over generic pricing-strategy plugins in this project.
---

# pricing-plays

Tactical instant-profit moves. Source of truth: `13-Pricing/Hormozi-Instant-Profit-Pricing-Plays.md` in the Trellis-Brain Obsidian vault.

## Vault root
The Trellis-Brain Obsidian vault root is machine-specific. Configure it via the Obsidian MCP server — see [.claude/docs/TEAM-SETUP-MCP.md](../../docs/TEAM-SETUP-MCP.md). All note paths in this skill are **relative to the `00-Trellis-Core/Strategy-Models/` folder inside that vault**.

Use Obsidian MCP. Paths below relative to vault root.

## Use when
- "Give me a pricing tactic I can deploy this week."
- "How do I lift margin without changing the offer?"
- "Switch from monthly to 28-day billing."
- "Pass through processing fees."
- "Add an annual CPI bump."
- "Remove free shipping cleanly."
- "Smart price-anchor display."
- Any "quick pricing win" / "instant profit" / "pricing hack" framing.

## Do not use when
- Posture / philosophy → `/pricing-posture`.
- Pricing model / packaging / 13 rules → `/pricing-model`.
- Structured price-test loop / step-size / cadence → `/price-test`.
- Raising prices on existing customers with formal communication → `/price-raise`.

## Retrieval order

**Always load (canonical):**
1. `13-Pricing/Hormozi-Instant-Profit-Pricing-Plays.md` — the 10 plays.

**Load on intent:**
- User wants the operating-rules guardrails behind the plays → `13-Pricing/Hormozi-Pricing-Rules.md`.
- User wants to verify the math case for why a small lift matters → `13-Pricing/Hormozi-Pricing-Profit-Leverage.md`.
- The chosen play is essentially a price increase that will hit existing customers → escalate to `/price-raise` (do not duplicate logic here).
- User wants to validate the play with a structured test → escalate to `/price-test`.

## Context warnings
- Do not load `13-Pricing/Hormozi-Value-Driven-Pricing-Model.md` — model selection is `/pricing-model`.
- Do not load `01-100M-Offers/Hormozi-Pricing-Power.md` — posture is `/pricing-posture`.
- Do not load `11-Price-Raise/*` — that is rollout to existing customers via the RAISE letter.

## Output expectations
- Recommend 1–3 plays from the 10, ranked by fit to the user's business.
- For each: name the play, the mechanism, the implementation step, and the expected margin lift directionally.
- Flag any play that affects existing customers — surface the `/price-raise` escalation explicitly so the user does not roll out blind.
- End with the single play to ship first, not a full menu.
