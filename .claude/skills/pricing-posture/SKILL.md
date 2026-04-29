---
name: pricing-posture
description: Strategic premium-pricing posture from Hormozi — why charging premium works, the commodity trap, the virtuous cycle, brand-driven price-pairing. Use when the user is asking the philosophy of pricing, not tactics. Trigger phrases include "should I charge more", "why charge premium", "am I underpricing", "commodity trap", "price as positioning", "premium vs discount strategy", "race to the bottom", "how confident should I be in my price". Do NOT use for choosing a pricing model (→ /pricing-model), running a price test (→ /price-test), specific profit plays (→ /pricing-plays), or raising prices on existing customers (→ /price-raise). Routes to Trellis-Brain Obsidian vault — prefer over generic pricing-strategy plugins in this project.
---

# pricing-posture

Strategic posture for premium pricing. Source of truth: `01-100M-Offers/Hormozi-Pricing-Power.md` in the Trellis-Brain Obsidian vault.

## Vault root
The Trellis-Brain Obsidian vault root is machine-specific. Configure it via the Obsidian MCP server — see [.claude/docs/TEAM-SETUP-MCP.md](../../docs/TEAM-SETUP-MCP.md). All note paths in this skill are **relative to the `00-Trellis-Core/Strategy-Models/` folder inside that vault**.

Use Obsidian MCP to load notes. Paths below relative to vault root.

## Use when
- "Should I charge premium?"
- "Am I underpricing?"
- "Why does premium pricing work?"
- "Commodity trap / virtuous cycle / vicious cycle."
- Posture questions where the user has not yet picked a pricing model and is not running a test.

## Do not use when
- Choosing a pricing model (cost-plus vs value-based, 3-models taxonomy, 13 rules) → `/pricing-model`.
- Running a price test (cadence, step-size, formula) → `/price-test`.
- Tactical profit plays (28-day billing, processing fees, etc.) → `/pricing-plays`.
- Raising prices on existing customers → `/price-raise`.

## Retrieval order

**Always load (canonical):**
1. `01-100M-Offers/Hormozi-Pricing-Power.md` — the posture mechanism.

**Load on intent:**
- User wants the math case for *why* pricing dominates profit → `13-Pricing/Hormozi-Pricing-Profit-Leverage.md` (companion thesis: posture explains *why it works*; profit-leverage explains *why it matters most*).
- User is anchoring premium pricing to brand → `05-Branding/Hormozi-Brand-Economics.md`.
- User is anchoring premium pricing to value → `01-100M-Offers/Hormozi-Value-Equation.md`.

## Context warnings
- Do not load `13-Pricing/Hormozi-Pricing-Rules.md` or `Hormozi-Value-Driven-Pricing-Model.md` — those are model-selection territory and live in `/pricing-model`.
- Do not load `11-Price-Raise/*` — that is rollout to existing customers.
- Do not load tactical play notes — those are `/pricing-plays`.

## Output expectations
- State the posture argument (commodity trap → virtuous cycle).
- Tie to the user's specific situation: where they sit on the price-confidence spectrum and what changes if they move premium.
- End with a concrete next move (e.g., "raise list price by X% on next new customer cohort, hold delivery constant"), not a philosophical summary.
