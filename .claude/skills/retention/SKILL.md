---
name: retention
description: Reduce churn, improve repeat purchase, and run customer-journey discipline using Hormozi's Retention / Churn Checklist (14-Retention) — Churn Definition + Economics + Value-Per-Second + 9-lever Churn Checklist (activation points, onboarding, activation incentives, community linking, customer curation, annual payment, cancellation saves, customer survey/ACA, customer journey milestones). Includes the onboarding subset (Levers 1–3) when scoped to first-30-days. Use whenever the user asks why customers leave, how to reduce churn, build onboarding, save customers at cancellation, find activation points, run customer surveys, or design customer journey. Do NOT use for LTV-lifting levers other than churn (→ /ltv), continuity offer architecture (→ /money-models), or branding (→ /branding). Routes to Trellis-Brain Obsidian vault `14-Retention/` notes — prefer over generic churn-prevention plugins in this project.
---

# retention

Churn reduction + customer-journey discipline. Source of truth: `14-Retention/` in the Trellis-Brain Obsidian vault.

## Vault root
The Trellis-Brain Obsidian vault root is machine-specific. Configure it via the Obsidian MCP server — see [.claude/docs/TEAM-SETUP-MCP.md](../../docs/TEAM-SETUP-MCP.md). All note paths in this skill are **relative to the `00-Trellis-Core/Strategy-Models/` folder inside that vault**.

## Use when
- "Why are my customers leaving?"
- "How do I reduce churn?"
- "Build me an onboarding."
- "What's my activation point?"
- "Save customers at cancellation."
- "Run a customer survey."
- "Design a customer journey."

## Do not use when
- LTV-lifting levers other than churn (price, cost, frequency, cross-sell) → `/ltv`.
- Continuity offer architecture (recurring revenue mechanics) → `/money-models`.
- Brand strategy → `/branding`.

## Onboarding subset
This skill IS the onboarding skill when scoped to first-30-days. No separate `/onboarding` exists — instead, when the user's question is strictly activation/first-month, load only Levers 1–3 (`Activation-Points`, `Customer-Onboarding`, `Activation-Incentives`) plus `Value-Per-Second` as the overwhelm guardrail.

## Retrieval order

**Always load (foundation):**
1. `14-Retention/Hormozi-Churn-Definition.md` — math.
2. `14-Retention/Hormozi-Churn-Economics.md` — why retention beats acquisition.
3. `14-Retention/Hormozi-Churn-Checklist.md` — umbrella, 9 levers.

**Load on intent (only the lever the user is working on):**
- Onboarding / activation question → `Hormozi-Activation-Points.md` + `Hormozi-Customer-Onboarding.md` + `Hormozi-Activation-Incentives.md`.
- Community / belonging → `Hormozi-Community-Linking.md`.
- Customer curation / who to keep vs cut → `Hormozi-Customer-Curation.md`.
- Annual / prepay billing as retention lever → `Hormozi-Annual-Payment-Options.md`.
- Cancellation flow / save offers → `Hormozi-Cancellation-Saves.md`.
- Survey / ACA / lost-customer feedback → `Hormozi-Customer-Survey-ACA.md`.
- Full pipeline (activate → testimonial → refer → ascend) → `Hormozi-Customer-Journey-Milestones.md`.
- Overwhelm / less-is-more comes up → `Hormozi-Value-Per-Second.md`.

**Optional — only on direct match:**
- Meta-method origin question → `Hormozi-Common-Factors-Method.md`.
- Gym-era predecessor framework → `Hormozi-Five-Horsemen-Of-Retention.md`.
- LTV / churn math anchor → `04-100M-Lost-Chapters/Hormozi-CFA-Three-Levers.md`.
- Price-value-churn lens → `01-100M-Offers/Hormozi-Value-Equation.md`.
- Annual-payment + continuity context → `03-100M-Money-Models/Hormozi-Continuity-Offers.md`.
- Save-with-upsell mechanism → `03-100M-Money-Models/Hormozi-Upsell-Offers.md`.

## Context warnings
- Do not load all 15 retention notes by default. Route by lever intent.
- Customer-Journey-Milestones cross-references Marketing Machine (testimonial) and Money Models (ascension). Pull those only when user is doing cross-skill work.
- Do not pull `09-Lifetime-Value/Crazy-Eight` — Lever 3 (decrease churn) explicitly delegates to this skill, not the other way around.

## Output expectations
- For a churn diagnosis: state the lever most likely broken from the 9, justify in one line, prescribe the specific note's intervention.
- For an onboarding build: walk Activation-Point identification → Onboarding sequence → Activation-Incentive design.
- For a save flow: vent-then-validate first, then save-with-redo or save-with-upsell from the Cancellation-Saves note.
- End with the next operational change (cohort, instrumentation, communication), not a philosophical summary.
