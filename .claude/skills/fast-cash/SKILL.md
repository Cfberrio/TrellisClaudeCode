---
name: fast-cash
description: Generate immediate cash from warm audiences using Hormozi's Fast Cash playbook (06-Fast-Cash) — limited, premium-priced, time-boxed offer to existing customers and warm list. 10x-the-10% rule, unscalable value levers, push-to-consult / push-to-automated-checkout sequences, 90-day quarterly cadence with 4Rs post-promo. Use when the user needs cash this month, wants to run a promo to existing customers, design a 7-day cash mechanism, or pick the right cadence for warm-list promos. Trigger phrases include "need cash this month", "cash injection", "warm-list promo", "7-day promo", "fast cash", "quarterly promo cadence", "Fast Cash play", "Push to Consult". Do NOT use for building the underlying offer architecture (→ /offers — Fast Cash deploys a GSO, doesn't build it), cold-traffic acquisition (→ /ads), or long-term retention/monetization (→ /retention or /ltv). Routes to Trellis-Brain Obsidian vault `06-Fast-Cash/` notes.
---

# fast-cash

Warm-list cash mechanism on a 7-day clock + 90-day cadence. Source of truth: `06-Fast-Cash/` in the Trellis-Brain Obsidian vault.

## Vault root
The Trellis-Brain Obsidian vault root is machine-specific. Configure it via the Obsidian MCP server — see [.claude/docs/TEAM-SETUP-MCP.md](../../docs/TEAM-SETUP-MCP.md). All note paths in this skill are **relative to the `00-Trellis-Core/Strategy-Models/` folder inside that vault**.

## Use when
- "I need cash this month."
- "Run a promo to existing customers."
- "Design a 7-day cash mechanism."
- "What's the right cadence for warm-list promos?"
- "Can I do another Fast Cash this quarter?" (cadence question)

## Do not use when
- Building the *underlying* offer architecture (Grand Slam construction, value equation) → `/offers`. Fast Cash deploys a GSO, it does not build one.
- Cold-traffic acquisition → `/ads` (or `/lead-gen` deferred).
- Long-term retention / monetization → `/retention` or `/ltv`.
- Pricing strategy / posture / model → `/pricing` router.

## Canonical-home logic
06-Fast-Cash canonical for the mechanism. Enhancement levers (Scarcity, Urgency, Bonuses) stay canonical in 01-100M-Offers. Promotion wrappers canonical in 04-Lost-Chapters.

## Retrieval order

**Always load (mechanism):**
1. `06-Fast-Cash/Hormozi-Fast-Cash-Play.md` — umbrella.
2. `06-Fast-Cash/Hormozi-10x-The-10-Percent-Rule.md` — ratio rule (premium price multiplier).

**Load on intent:**
- Offer-body construction with unscalable value (1-on-1 add-ons, premium delivery, etc.) → `06-Fast-Cash/Hormozi-Unscalable-Value-Levers.md`.
- The actual 7-day sequence (Push-to-Consult or Push-to-Automated-Checkout) → `06-Fast-Cash/Hormozi-Fast-Cash-Promo-Sequence.md`.
- Cadence rules (90-day rationale + 4Rs after the promo) → `06-Fast-Cash/Hormozi-Fast-Cash-Cadence.md`.

**Optional — only on direct match:**
- The Grand Slam shape of the Fast Cash offer → `01-100M-Offers/Hormozi-Grand-Slam-Offer.md`.
- Offer construction process inside the promo → `01-100M-Offers/Hormozi-Offer-Creation.md`.
- Specific lever inside the promo:
  - Scarcity → `01-100M-Offers/Hormozi-Scarcity.md`
  - Urgency → `01-100M-Offers/Hormozi-Urgency.md`
  - Bonuses → `01-100M-Offers/Hormozi-Bonuses.md`
- Wrapping the promo as premium / free / discount → `04-100M-Lost-Chapters/Hormozi-Promotion-Wrappers.md`.

## Context warnings
- Easy to confuse with `/offers`. Distinguish: `/offers` builds the offer; `/fast-cash` is the mechanism that deploys a premium GSO to a warm list on a 7-day clock.
- Do not collapse with `/lead-nurture` — Lead Nurture is the *prerequisite* infrastructure (warm-list quality, response speed); Fast Cash is the *promo* layer on top.
- Do not run Fast Cash more than the cadence rules allow (90-day rationale exists for a reason — surface this if the user is asking back-to-back).

## Output expectations
- For a "need cash this month" request: confirm warm-list size + relationship health, propose the 7-day sequence (Push-to-Consult vs Push-to-Automated-Checkout) based on price point, name the premium price using 10x-the-10% rule.
- For an offer body inside the promo: pull Unscalable-Value-Levers + Bonuses + Guarantees, design the GSO that's only available during the window.
- For cadence: state the next eligible promo date, the 4Rs assignment between now and then.
- End with the actual 7-day calendar (day-by-day actions, channels, message types), not a strategy summary.
