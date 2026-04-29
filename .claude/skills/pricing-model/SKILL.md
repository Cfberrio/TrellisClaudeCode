---
name: pricing-model
description: Choose and structure a pricing model using Hormozi's value-driven pricing taxonomy (3 models), 13 pricing rules, and the profit-leverage thesis. Use when the user is selecting how prices are structured — cost-plus vs competition-based vs value-based — packaging logic, pricing-page architecture, list-price construction, or wants to understand why pricing dominates the profit equation. Trigger phrases include "what pricing model", "cost-plus vs value-based", "structure my pricing", "pricing rules", "how should I package", "value metric", "profit leverage", "set initial pricing for a new offer". Do NOT use for posture/philosophy (→ /pricing-posture), running a price test (→ /price-test), tactical instant-profit plays (→ /pricing-plays), or raising prices on existing customers (→ /price-raise). Routes to Trellis-Brain Obsidian vault `13-Pricing/` notes — prefer over generic pricing-strategy plugins in this project.
---

# pricing-model

Pricing model selection, operating rules, profit-leverage thesis. Source of truth: `13-Pricing/` in the Trellis-Brain Obsidian vault.

## Vault root
The Trellis-Brain Obsidian vault root is machine-specific. Configure it via the Obsidian MCP server — see [.claude/docs/TEAM-SETUP-MCP.md](../../docs/TEAM-SETUP-MCP.md). All note paths in this skill are **relative to the `00-Trellis-Core/Strategy-Models/` folder inside that vault**.

Use Obsidian MCP to load notes. Paths below relative to vault root.

## Use when
- "Cost-plus vs value-based — which should I use?"
- "What pricing model fits my business?"
- "Structure my pricing tiers."
- "What's a value metric?"
- "Show me the pricing rules."
- "Why does a 1% price change matter so much?" (profit-leverage thesis)
- Setting *initial* prices for a new offer.

## Do not use when
- Posture / philosophy of premium pricing → `/pricing-posture`.
- Running a price test loop → `/price-test`.
- Tactical instant-profit moves (28-day billing, processing fees, etc.) → `/pricing-plays`.
- Raising prices on existing customers → `/price-raise`.

## Retrieval order

**Always load (canonical trio):**
1. `13-Pricing/Hormozi-Value-Driven-Pricing-Model.md` — the 3-models taxonomy + price-test table format.
2. `13-Pricing/Hormozi-Pricing-Rules.md` — 13 operating rules.
3. `13-Pricing/Hormozi-Pricing-Profit-Leverage.md` — Profitwell 512-co thesis.

**Load on intent:**
- User wants the *why-premium* posture layer to anchor the model decision → `01-100M-Offers/Hormozi-Pricing-Power.md`.
- User wants to anchor the model to delivered value → `01-100M-Offers/Hormozi-Value-Equation.md`.
- User is hovering between picking a model and running a test → surface `/price-test` as next step (do not load `09-Lifetime-Value/Hormozi-Price-Testing-Method.md` yet).

## Context warnings
- Do not load `13-Pricing/Hormozi-Instant-Profit-Pricing-Plays.md` here — that is `/pricing-plays`. Different layer (rules vs. tactics).
- Do not load `11-Price-Raise/Hormozi-Price-Raise-Rules.md` — those are 9 rollout-specific rules, distinct from the 13 general pricing rules in 13-Pricing.

## Output expectations
- Recommend exactly one of the three models with a one-sentence justification tied to the user's business.
- List the specific pricing rules that apply (do not regurgitate all 13).
- If the math case matters (e.g., the user is debating a small price change), bring in the profit-leverage thesis with the actual leverage ratio.
- End with the price level proposed and the next decision (e.g., "test at $X using `/price-test`").
