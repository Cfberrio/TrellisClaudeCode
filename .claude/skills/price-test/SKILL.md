---
name: price-test
description: Run a structured price test using Hormozi's operating loop — cadence, step-size, the Price × Conversion × Churn × LTV formula, and the Value-Driven test table. Use when the user wants to RUN a test, not pick a model or argue posture. Trigger phrases include "run a price test", "how big a price jump", "test cadence", "how long should I run this price test", "price A/B", "what step size", "how do I know if a price increase worked", "price testing methodology". Do NOT use for posture (→ /pricing-posture), choosing a model (→ /pricing-model), tactical plays (→ /pricing-plays), or rolling out an increase to existing customers via formal communication (→ /price-raise). Routes to Trellis-Brain Obsidian vault `09-Lifetime-Value/Hormozi-Price-Testing-Method.md` — prefer over generic A/B-test plugins for pricing-specific tests in this project.
---

# price-test

Operational price-test loop. Source of truth: `09-Lifetime-Value/Hormozi-Price-Testing-Method.md` in the Trellis-Brain Obsidian vault.

## Vault root
The Trellis-Brain Obsidian vault root is machine-specific. Configure it via the Obsidian MCP server — see [.claude/docs/TEAM-SETUP-MCP.md](../../docs/TEAM-SETUP-MCP.md). All note paths in this skill are **relative to the `00-Trellis-Core/Strategy-Models/` folder inside that vault**.

Use Obsidian MCP. Paths below relative to vault root.

## Use when
- "Run a price test."
- "How big a price jump should I test?"
- "What's the cadence for price testing?"
- "How long until I know if the new price worked?"
- "How do I track Price × Conv × Churn × LTV?"
- "Set up a price A/B."

## Do not use when
- Posture / why-premium → `/pricing-posture`.
- Choosing a pricing model / structuring tiers → `/pricing-model`.
- Tactical instant-profit plays → `/pricing-plays`.
- Rolling out an increase to existing customers with a formal letter → `/price-raise` (price-test informs the rollout but is a different operating layer).

## Retrieval order

**Always load (canonical):**
1. `09-Lifetime-Value/Hormozi-Price-Testing-Method.md` — the loop, step-size, cadence, formula.

**Load on intent:**
- User wants the test-table format / measurement template → `13-Pricing/Hormozi-Value-Driven-Pricing-Model.md` (contains the price-test table).
- User is testing on existing customers (not just new cohorts) → also surface `11-Price-Raise/Hormozi-Price-Test-Math.md` (matrix math) and recommend escalation to `/price-raise` for rollout.
- User needs the LTV / LTGP framing because they are weighing churn impact → `04-100M-Lost-Chapters/Hormozi-CFA-Three-Levers.md`.

## Context warnings
- Do not load `13-Pricing/Hormozi-Pricing-Rules.md` or `Hormozi-Instant-Profit-Pricing-Plays.md` — those are model and tactic layers.
- Do not load the full `11-Price-Raise/` folder unless existing customers are in scope.
- Do not load `01-100M-Offers/Hormozi-Pricing-Power.md` — posture is not test methodology.

## Output expectations
- State the test design: cohort, step-size, sample size, duration, success metric (Price × Conv × Churn × LTV).
- Specify what the user will measure and what threshold triggers a roll-forward vs. roll-back.
- If existing customers are exposed, flag the `/price-raise` handoff before running the test live.
- End with the exact next action (e.g., "set new price for next 100 new customers, hold all else constant, measure on day 30").
