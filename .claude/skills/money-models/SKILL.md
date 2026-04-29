---
name: money-models
description: Sequence multiple offers across the customer's first 30 days using Hormozi's Money Model architecture (03-100M-Money-Models) — Attraction → Upsell → Downsell → Continuity, plus full Money Model assembly and Customer-Financed Acquisition (CFA) economics. Use when the user is designing the offer sequence, asking why CAC > LTGP, working on day-0 / day-30 break-even, building or fixing specific offer slots (classic upsell, anchor upsell, payment plan, trial-with-penalty, feature downsell, continuity bonus), or assembling the full sequence. Trigger phrases include "money model", "offer sequence", "first 30 days", "CFA", "customer-financed acquisition", "upsell architecture", "downsell", "continuity offer", "break even on day 30". Do NOT use for building a single offer (→ /offers), pure LTV-lifting levers (→ /ltv), retention/churn (→ /retention), or pricing decisions (→ /pricing). Routes to Trellis-Brain Obsidian vault `03-100M-Money-Models/` notes.
---

# money-models

Multi-offer sequencing across the first 30 days. Source of truth: `03-100M-Money-Models/` in the Trellis-Brain Obsidian vault. CFA economics canonical in `04-100M-Lost-Chapters/`.

## Vault root
The Trellis-Brain Obsidian vault root is machine-specific. Configure it via the Obsidian MCP server — see [.claude/docs/TEAM-SETUP-MCP.md](../../docs/TEAM-SETUP-MCP.md). All note paths in this skill are **relative to the `00-Trellis-Core/Strategy-Models/` folder inside that vault**.

## Use when
- "Design a money model for my business."
- "What should the offer sequence look like across the first 30 days?"
- "Why is my CAC > LTGP?"
- "How do I get to CFA / break even on day 30?"
- Specific mechanism questions: classic upsell, anchor upsell, payment plan, trial-with-penalty, feature downsell, continuity bonus.

## Do not use when
- Building a *single* offer (Grand Slam construction, enhancement levers) → `/offers`.
- Pure LTV-lifting levers (price, cost, frequency, cross-sell) without sequencing context → `/ltv`.
- Pure retention / churn → `/retention`.
- Pricing strategy / model / posture → `/pricing`.

## Retrieval order

**Always load (umbrella + math):**
1. `03-100M-Money-Models/Hormozi-Money-Model.md` — umbrella.
2. `04-100M-Lost-Chapters/Hormozi-CFA-Three-Levers.md` — LTGP / CAC / PPD math.

**Load on intent (only the slot the user is working on):**
- Acquisition / front-end → `03-100M-Money-Models/Hormozi-Attraction-Offers.md`.
- Upsell architecture → `03-100M-Money-Models/Hormozi-Upsell-Offers.md`.
- Downsell architecture → `03-100M-Money-Models/Hormozi-Downsell-Offers.md`.
- Continuity / recurring → `03-100M-Money-Models/Hormozi-Continuity-Offers.md`.
- Designing the full sequence → `03-100M-Money-Models/Hormozi-Money-Model-Assembly.md`.

**Optional — only on direct match (specialized 04-Lost-Chapters mechanics):**
- Free presentations → `04-100M-Lost-Chapters/Hormozi-Attraction-Free-Presentations.md`.
- Freemium → `04-100M-Lost-Chapters/Hormozi-Attraction-Freemium.md`.
- Pick-your-price → `04-100M-Lost-Chapters/Hormozi-Attraction-Pick-Your-Price.md`.
- Free-with-alt-revenue upsell → `04-100M-Lost-Chapters/Hormozi-Upsell-Free-Alt-Revenue.md`.
- Lifetime upgrades / lifetime discounts / discount-plus-fee continuity → `04-100M-Lost-Chapters/Hormozi-Continuity-*.md`.
- CFA umbrella → `04-100M-Lost-Chapters/Hormozi-Customer-Financed-Acquisition.md`.
- LTV per segment → `04-100M-Lost-Chapters/Hormozi-Value-Grid.md`.
- Sales choreography across multiple offers → `04-100M-Lost-Chapters/Hormozi-Offer-Stacking.md`.

**Cross-skill anchors (load only when user is also building underlying offers):**
- `01-100M-Offers/Hormozi-Grand-Slam-Offer.md` — every Money Model offer is a GSO at its own slot.
- `01-100M-Offers/Hormozi-Value-Equation.md` — foundation lens.

## Context warnings
- Lots of overlap with `/offers`. Load `01-100M-Offers/Offer-Creation.md` only when the user explicitly needs to *build* the underlying offer; otherwise stay at the sequencing layer.
- Continuity architecture is canonical in 03; specialized variants (Lifetime Upgrades, Lifetime Discounts, Discount + Fee) live in 04. Match by intent.
- Bonuses / Guarantees / Pricing-Power stay canonical in 01. Do NOT re-define them here.

## Output expectations
- For a money-model design: state CAC and target LTGP, propose the Attract / Upsell / Downsell / Continuity slots, and show the day-30 math.
- For a single-slot question: load only that slot's note, prescribe the specific mechanism, and tie back to the assembly logic.
- End with the next concrete change to the sequence (slot to add, mechanism to swap, math to validate), not a summary.
