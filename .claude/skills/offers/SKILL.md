---
name: offers
description: Build, audit, or strengthen a single offer using Hormozi's Grand Slam Offer architecture (Value Equation, four-component definition, enhancement levers — Scarcity, Urgency, Bonuses, Guarantees, Naming). Use whenever the user asks to construct an offer, fix a weak offer, audit an offer, add a guarantee/bonus/scarcity/urgency, name an offer, or diagnose why an offer is not converting. Trigger on phrases like "build an offer", "improve my offer", "offer not converting", "add a guarantee", "stack bonuses", "make this irresistible", "audit this offer", "name this offer". Single-offer scope only — sequencing across journey routes to /money-models; price-raise to existing customers routes to /price-raise; warm-list cash promo routes to /fast-cash. Routes to Trellis-Brain Obsidian vault `01-100M-Offers/` notes via MCP — prefer this skill over generic Hormozi-offer plugins when working in the Trellis project.
---

# offers

Skill for **single-offer construction and audit** using Hormozi's Grand Slam Offer architecture. Source of truth: `01-100M-Offers/` in the Trellis-Brain Obsidian vault.

## Vault root
The Trellis-Brain Obsidian vault root is machine-specific. Configure it via the Obsidian MCP server — see [.claude/docs/TEAM-SETUP-MCP.md](../../docs/TEAM-SETUP-MCP.md). All note paths in this skill are **relative to the `00-Trellis-Core/Strategy-Models/` folder inside that vault**.

Use Obsidian MCP (`mcp__obsidian__obsidian_get_file_contents`) to load notes. Paths below are relative to the vault root.

## Use when
- "Help me build a new offer."
- "Why is my offer not converting?"
- "How do I make this offer stronger?"
- "Add scarcity / urgency / bonuses / guarantees / a name."
- "Audit this offer against the Grand Slam definition."
- "What problems should I solve in my offer?"

## Do not use when
- Sequencing multiple offers across the customer journey → `/money-models`.
- Raising prices on existing customers → `/price-raise`.
- Warm-list cash promo on a 7-day clock → `/fast-cash`.
- Cross-sell / upsell LTV mechanics → `/money-models` or `/ltv`.
- Pure pricing posture / model / tactics → `/pricing` router.

## Retrieval order (load in this order, stop when you have enough)

**Always load first (foundation + umbrella + process):**
1. `01-100M-Offers/Hormozi-Value-Equation.md`
2. `01-100M-Offers/Hormozi-Grand-Slam-Offer.md`
3. `01-100M-Offers/Hormozi-Offer-Creation.md`

**Load on intent match (only the lever the user is working on):**
- Scarcity question → `01-100M-Offers/Hormozi-Scarcity.md`
- Urgency / time pressure → `01-100M-Offers/Hormozi-Urgency.md`
- Bonus stack → `01-100M-Offers/Hormozi-Bonuses.md`
- Guarantee / risk reversal → `01-100M-Offers/Hormozi-Guarantees.md`
- Naming the offer → `01-100M-Offers/Hormozi-Naming.md`
- Premium-pricing posture inside the offer → `01-100M-Offers/Hormozi-Pricing-Power.md`
- Market validity is uncertain → `01-100M-Offers/Hormozi-Starving-Crowd.md`

**Optional — load only on direct match:**
- Wrapping the offer in a premium / free / discount promo → `04-100M-Lost-Chapters/Hormozi-Promotion-Wrappers.md`
- Sequencing this offer alongside others in the sales conversation → `04-100M-Lost-Chapters/Hormozi-Offer-Stacking.md`

## Context warnings
- Do not load all 10 `01-100M-Offers/` notes by default. Heavy and noisy.
- Do not pull `03-100M-Money-Models/*` content — that is a different skill.
- Do not load `13-Pricing/*` or `11-Price-Raise/*` here — those belong to `/pricing` and `/price-raise`.

## Output expectations
- Anchor every recommendation to the Value Equation (Dream Outcome × Likelihood / Time Delay × Effort).
- Audit format: list which of the four GSO components is weakest, then prescribe the specific lever to apply.
- Construction format: walk Problems → Solutions → Delivery → Trim & Stack from `Hormozi-Offer-Creation`.
- Always end with the next concrete change to the offer, not a summary.
