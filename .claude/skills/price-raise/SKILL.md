---
name: price-raise
description: Roll out a price increase to EXISTING customers without losing them. Hormozi Price-Raise Play, 9 rollout-specific rules, Price × Conv × Churn × LTV math matrix, and the 5-section RAISE letter (Remind / Address / Invest / Soften / Explain). Use when the user has current paying customers and needs to lift their prices — communication, math, sequencing, objection handling during the raise. Trigger phrases include "raise prices on existing customers", "send a price-raise letter", "RAISE letter", "price increase letter", "how do I raise prices without churning everyone", "grandfather pricing decision", "tell my customers about a price hike". Do NOT use for setting initial prices on a new offer (→ /pricing-model or /offers), philosophy of premium pricing (→ /pricing-posture), running a structured cohort price test (→ /price-test), or tactical instant-profit moves on new customers only (→ /pricing-plays). Routes to Trellis-Brain Obsidian vault `11-Price-Raise/` notes.
---

# price-raise

Existing-customer price raise — math, rollout, communication. Source of truth: `11-Price-Raise/` in the Trellis-Brain Obsidian vault.

## Vault root
The Trellis-Brain Obsidian vault root is machine-specific. Configure it via the Obsidian MCP server — see [.claude/docs/TEAM-SETUP-MCP.md](../../docs/TEAM-SETUP-MCP.md). All note paths in this skill are **relative to the `00-Trellis-Core/Strategy-Models/` folder inside that vault**.

Use Obsidian MCP. Paths below relative to vault root.

## Use when
- "I want to raise prices on my current customer base."
- "Write me a price-raise letter."
- "What math do I need to run before raising?"
- "How do I handle objections during a price raise?"
- "Should I grandfather existing customers?"
- "How long do I give before the new price kicks in?"

## Do not use when
- Setting *initial* pricing for a new offer → `/pricing-model` or `/offers`.
- Philosophy of premium pricing → `/pricing-posture`.
- Running a structured cohort price test → `/price-test`.
- Tactical instant-profit moves that affect only new customers → `/pricing-plays`.

## Retrieval order

**Always load (canonical, full folder):**
1. `11-Price-Raise/Hormozi-Price-Raise-Play.md` — umbrella mechanism.
2. `11-Price-Raise/Hormozi-Price-Raise-Rules.md` — 9 rollout-specific operating rules.
3. `11-Price-Raise/Hormozi-Price-Test-Math.md` — Price × Conv × Churn × LTV matrix.
4. `11-Price-Raise/Hormozi-RAISE-Letter.md` — 5-section communication template (Remind / Address / Invest / Soften / Explain).

**Load on intent:**
- User wants posture-anchor language for the "Remind" or "Invest" section of the RAISE letter → `01-100M-Offers/Hormozi-Pricing-Power.md`.
- User wants the Value Equation framing for the "Invest" section (showing what value has accumulated) → `01-100M-Offers/Hormozi-Value-Equation.md`.
- User wants to validate the increase with a small cohort first → `09-Lifetime-Value/Hormozi-Price-Testing-Method.md`.

## Context warnings
- Do not load `13-Pricing/Hormozi-Pricing-Rules.md` — those are 13 *general* pricing rules, distinct from the 9 *rollout-specific* rules in this folder. Loading both creates confusion.
- Do not load `13-Pricing/Hormozi-Instant-Profit-Pricing-Plays.md` — those are tactical moves on new pricing, not communication to existing customers.

## Output expectations
- Run the Price × Conv × Churn × LTV math first. Show the breakeven churn the raise can absorb.
- Recommend the rollout sequence: notice window, effective date, grandfathering decision (yes/no with rationale), objection-handling script.
- Draft the RAISE letter using all 5 sections: Remind (relationship), Address (raise itself), Invest (what they get), Soften (grace period / opt-out), Explain (why now).
- End with the next concrete action (e.g., "send letter to top 10% by tenure first as canary cohort").
