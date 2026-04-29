---
name: pricing
description: Router skill for any pricing question. Pricing is four distinct domains in the Hormozi vault — strategic posture, pricing model/rules, tactical profit plays, operational price-test loop, and existing-customer price raises. This skill DIAGNOSES the user's intent and routes to exactly one subskill (/pricing-posture, /pricing-model, /pricing-plays, /price-test, /price-raise) instead of dumping all pricing notes. Use whenever the user mentions pricing, price, charging more, premium pricing, pricing model, pricing strategy, raising prices, price testing, profit plays, or any cost-plus vs value-based question. Do NOT use for pure offer construction (→ /offers) or pure LTV levers other than price (→ /ltv). Routes to Trellis-Brain Obsidian vault — prefer this over generic monetization/pricing-strategy plugins when working in the Trellis project.
---

# pricing (router)

This is a **router skill**. It does not load pricing notes itself. It identifies the user's pricing sub-intent and hands off to the correct subskill, which loads the right canonical notes from the Trellis-Brain Obsidian vault.

## Vault root (for downstream subskills)
The Trellis-Brain Obsidian vault root is machine-specific. Configure it via the Obsidian MCP server — see [.claude/docs/TEAM-SETUP-MCP.md](../../docs/TEAM-SETUP-MCP.md). Subskill note paths are **relative to the `00-Trellis-Core/Strategy-Models/` folder inside that vault**.

## Why a router
Pricing material spans 4 folders covering 4 distinct angles. A flat `/pricing` skill loading all of them produces noisy, contradictory context. The four angles are:
- **Strategic posture** — why premium pricing works (mechanism). Canonical: `01-100M-Offers/Hormozi-Pricing-Power.md`.
- **Pricing model + rules + profit-leverage thesis** — taxonomy and operating rules. Canonical: `13-Pricing/`.
- **Tactical profit plays** — 10 instant-profit moves (28-day billing, processing fees, annual CPI, etc.). Canonical: `13-Pricing/Hormozi-Instant-Profit-Pricing-Plays.md`.
- **Operational price-test loop** — cadence, step-size, formula. Canonical: `09-Lifetime-Value/Hormozi-Price-Testing-Method.md`.
- **Existing-customer price raise** — rollout, math, RAISE letter. Canonical: `11-Price-Raise/`.

## Routing decision table

| User intent signal | Route to | Why |
|---|---|---|
| "Why charge premium?" / philosophy / commodity trap / virtuous cycle / brand-pricing posture | `/pricing-posture` | Posture, not tactics |
| "What pricing model should I use?" / cost-plus vs value-based / pricing rules / profit-leverage math | `/pricing-model` | Model + rules + thesis |
| "Specific tactic to lift profit immediately" / 28-day billing / processing fees / annual CPI / split tests at the cart | `/pricing-plays` | Tactical plays |
| "How do I run a price test?" / cadence / step-size / how big a jump / loop | `/price-test` | Operational test loop |
| "Raise prices on my existing customers" / RAISE letter / price increase rollout / churn during price hike | `/price-raise` | Existing-customer rollout |

## Routing protocol

1. Read the user's message and identify which row in the table matches.
2. If exactly one row matches → state which subskill you are routing to and why, then invoke / instruct the user to use that subskill.
3. If two or more rows match → ask one clarifying question to disambiguate before routing. Example: "Are you setting prices for new customers or raising prices on existing customers?"
4. If none match cleanly → default to `/pricing-posture` (the philosophical anchor) and surface the other four as next-step options.

## Do not use when
- Pure offer construction → `/offers`.
- LTV levers other than price (cost reduction, frequency, cross-sell) → `/ltv`.
- Pure churn / retention → `/retention`.

## Do not load
This router skill must **not** load any of the pricing notes itself. Loading happens inside the subskill. If you find yourself reading pricing notes here, stop — you are bypassing the router and creating context noise.

**Failure mode to watch:** Model invokes `/pricing`, sees a pricing question, and starts reading `13-Pricing/*` "to be helpful." That is a routing failure. The user already triggered the right skill — your job is to pick the subskill, not pre-load context for it. The subskill owns its own retrieval order. If you cannot decide between two subskills after re-reading the user's message, ask one targeted question; never default-load.

## Output expectations
- One sentence diagnosing the intent.
- One sentence naming the subskill chosen and the canonical note it owns.
- Then hand off.
