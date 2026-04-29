---
name: ltv
description: Lift LTV / LTGP using Hormozi's Lifetime Value playbook (09-Lifetime-Value) — Crazy Eight (8 LTV-lifting levers), cost reduction palette (Lever 2), CFA-Three-Levers math (LTGP / CAC / PPD). Use when the user asks to increase customer value, reduce fulfillment costs, get customers to buy more often, lift LTV/LTGP, or work on the LTV math itself. Trigger phrases include "increase customer value", "raise LTV", "LTGP", "fulfillment cost reduction", "buy more often", "cross-sell more", "customer value math", "Crazy Eight". Do NOT use for pure churn reduction (→ /retention; Lever 3 of Crazy Eight delegates to it), designing the offer sequence (→ /money-models), running a price test as the operational loop (→ /price-test), or strategic pricing posture (→ /pricing-posture). Routes to Trellis-Brain Obsidian vault `09-Lifetime-Value/` notes — prefer over generic monetization plugins for Hormozi-aligned LTV work.
---

# ltv

LTV / LTGP lift via the Crazy Eight + cost reduction. Source of truth: `09-Lifetime-Value/` in the Trellis-Brain Obsidian vault. CFA math canonical in `04-100M-Lost-Chapters/`.

## Vault root
The Trellis-Brain Obsidian vault root is machine-specific. Configure it via the Obsidian MCP server — see [.claude/docs/TEAM-SETUP-MCP.md](../../docs/TEAM-SETUP-MCP.md). All note paths in this skill are **relative to the `00-Trellis-Core/Strategy-Models/` folder inside that vault**.

## Use when
- "How do I increase customer value?"
- "Reduce my fulfillment costs."
- "Get customers to buy more often."
- LTV / LTGP math questions.
- Working through the 8 levers (price, cost, frequency, churn, etc.) at a strategic level.

## Do not use when
- Pure churn reduction (Crazy Eight Lever 3) → `/retention` is canonical for the deeper mechanism.
- Designing the customer-journey offer sequence → `/money-models`.
- Running a structured price test (Lever 1 operational loop) → `/price-test`.
- Strategic pricing posture (Lever 1 strategic layer) → `/pricing-posture`.
- Tactical instant-profit pricing moves → `/pricing-plays`.
- Existing-customer price raise rollout → `/price-raise`.

## Canonical-home logic
Crazy Eight canonical in 09. LTV math canonical in 04. Each lever's deeper mechanism lives in its respective canonical home (Money Models for upsell/downsell/continuity; Retention for churn; Fast Cash for follow-up; Pricing for price levers). This skill **delegates** rather than duplicates.

## Retrieval order

**Always load (canonical):**
1. `09-Lifetime-Value/Hormozi-Crazy-Eight.md` — umbrella, 8 levers.
2. `04-100M-Lost-Chapters/Hormozi-CFA-Three-Levers.md` — LTV / LTGP / CAC math.

**Load on intent (the lever the user is working on):**
- Lever 1 (price) at math/strategy level → keep here; for action route to `/pricing-posture` (philosophy), `/price-test` (operational), `/price-raise` (existing customers), `/pricing-plays` (tactical).
- Lever 2 (cost reduction) → `09-Lifetime-Value/Hormozi-Cost-Reduction-Levers.md`.
- Lever 3 (decrease churn) → hand off to `/retention` for the 9-lever Churn Checklist.
- Lever 4 (increase frequency) → `03-100M-Money-Models/Hormozi-Continuity-Offers.md`.
- Lever 5/6 (quantity / quality up — cross-sell, ascension) → `03-100M-Money-Models/Hormozi-Upsell-Offers.md`.
- Lever 7/8 (downsell / win-back / follow-up) → `03-100M-Money-Models/Hormozi-Downsell-Offers.md` + `06-Fast-Cash/Hormozi-Fast-Cash-Play.md` + `Hormozi-Fast-Cash-Cadence.md`.

**Optional — only on direct match:**
- Cost-reduction operational loop / vendor-renegotiation tactic → `Hormozi-Cost-Reduction-Levers.md` (already in primary).

## Context warnings
- Crazy Eight delegates depth on most levers to other folders. Skill must follow the delegation, not duplicate.
- Do not pull `09-Lifetime-Value/Hormozi-Price-Testing-Method.md` here — that is `/price-test`'s canonical.
- Do not pull all 9 retention levers — that's `/retention`'s scope.

## Output expectations
- For an LTV diagnosis: name the lever from Crazy Eight with the highest expected lift given the user's unit economics, justify with CFA math.
- For a cross-skill question: identify the lever, hand off to the canonical skill (`/retention`, `/money-models`, `/pricing-*`, `/fast-cash`).
- For a cost-reduction question: walk Cost-Reduction-Levers, name the 1-2 highest-leverage cuts.
- End with the next operational LTV lift (lever, mechanism, instrumentation), not a math summary.
