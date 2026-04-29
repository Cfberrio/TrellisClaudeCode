---
name: sales
description: Close deals on the live sales call using Hormozi's Closing playbook (15-Closing) — the 3-bucket maybe model + Power thesis + Blame Onion (Circumstances / Other-People / Self) + 28 operating rules + All-Purpose closes (7 universal) + branch-specific close libraries (Time, Money 4-flavor, Decision-Makers, Bad-Experiences, Preferences, Rushed-Decisions, Guarantee Closes) + closing-training system. Use when the user asks how to handle a specific objection, why their close rate is low, how to respond to "let me think about it" / "too expensive" / "I need to talk to my spouse" / "I've been burned before", how to train a sales team to close, or how to deploy guarantees during the close. Do NOT use for offer construction (→ /offers), pre-call lead nurture (→ /lead-nurture), post-purchase save flows (→ /retention), pricing decisions (→ /pricing), or lead acquisition (→ /lead-gen deferred). Routes to Trellis-Brain Obsidian vault `15-Closing/` notes.
---

# sales

Live-call objection handling and closing mechanics. Source of truth: `15-Closing/` in the Trellis-Brain Obsidian vault.

## Vault root
The Trellis-Brain Obsidian vault root is machine-specific. Configure it via the Obsidian MCP server — see [.claude/docs/TEAM-SETUP-MCP.md](../../docs/TEAM-SETUP-MCP.md). All note paths in this skill are **relative to the `00-Trellis-Core/Strategy-Models/` folder inside that vault**.

## Use when
- "Why aren't we closing?"
- "Train my sales team to handle objections."
- "How do I respond to '[specific objection — too expensive / let me think about it / I need to talk to my spouse / I've been burned before / etc.]'?"
- "Build the close library for our sales script."
- "Diagnose why our close rate is X% and what to do about it."
- "What's the right way to deploy guarantees during the close?"
- "BAMFAM — they need to bring the decision-maker, how do I re-book without losing them?" (BAMFAM is canonical in `/lead-nurture` but invoked from sales contexts.)

## Do not use when
- Building the *offer* being sold → `/offers`. (Different layer: offers build the thing; sales handles objections during the act of selling it. Operators conflate these constantly.)
- Pre-call lead nurture (show rate, response speed, opt-in cadence, 4 pillars) → `/lead-nurture`.
- Post-purchase cancellation save / vent-then-validate / save-with-redo / save-with-upsell → `/retention` (the cancellation-saves note is canonical there; adjacent objection pattern but different operating moment).
- Setting initial pricing or pricing structure on a new offer → `/pricing-model` or `/pricing` router.
- Existing-customer price-raise rollout (RAISE letter) → `/price-raise`.
- Lead acquisition / Core Four channels / lead magnets → `/lead-gen` (deferred; `02-100M-Leads/` not extracted yet).
- General sales-team execution culture (cadence, dashboards, accountability — NOT on-call objection handling) → `/lead-nurture` loads `Hormozi-Lead-Nurture-Execution-Culture.md` for that.

## Canonical-home logic
15-Closing is canonical for live-call objection handling and closing mechanics. Guarantees / Value Equation / Bonuses canonical in `01-100M-Offers/`. BAMFAM canonical in `10-Lead-Nurture/`. Cancellation-Saves canonical in `14-Retention/`. /sales links out to those, never duplicates them.

## Retrieval order

**Always load (foundation trio):**
1. `15-Closing/Hormozi-Closing-Definition.md` — 3-bucket maybe model + Power thesis + Blame Onion + ethics + STAR qualification.
2. `15-Closing/Hormozi-Closing-Rules.md` — 28 operating rules (conversation hygiene + closing mechanics + tactical discipline + operator character + observation).
3. `15-Closing/Hormozi-All-Purpose-Closes.md` — 7 universal closes (Main Concern, Reason, Hypothetical, Zoom Out, 1-to-10, Best-Case-Worst-Case, Card-Not-On-Me).

**Load on intent (only the branch matching the user's named obstacle):**
- Time / Money objections (any flavor: not-enough-value, can't-afford, cheaper-elsewhere, haggling) → `15-Closing/Hormozi-Closing-Circumstances-Closes.md`.
- Decision-makers ("I need to talk to my spouse / partner / boss") OR bad-experiences ("I've been burned before") → `15-Closing/Hormozi-Closing-Other-People-Closes.md`.
- Preferences ("I want it but my way" / "this isn't right for me") OR rushed decisions ("let me think about it" / "this is happening too fast") OR guarantee closes (when a guarantee is on the offer) → `15-Closing/Hormozi-Closing-Self-Closes.md`.

**Load when user is asking about training / building a closing program (not about a specific objection):**
- `15-Closing/Hormozi-Closing-Training-System.md` — operator economics of trained-vs-untrained closing + drill cadence + Gym Launch case + record-everything discipline.

**Optional — only on direct match:**
- Risk reversal underlying the Guarantee Closes section → `01-100M-Offers/Hormozi-Guarantees.md`.
- Translation rule for money objections ("value too low ≠ price too high") → `01-100M-Offers/Hormozi-Value-Equation.md`.
- Re-booking when decision-maker absent → `10-Lead-Nurture/Hormozi-BAMFAM.md`.
- Adjacent objection pattern when composing a save flow that resembles a close → `14-Retention/Hormozi-Cancellation-Saves.md`.
- 1-on-1 vs. group bonus sequencing inside the close → `01-100M-Offers/Hormozi-Bonuses.md`.
- Sales choreography across multiple offers in the same conversation → `04-100M-Lost-Chapters/Hormozi-Offer-Stacking.md`.

## Context warnings
- Do not load all 4 close libraries by default. Branch-specific. Route by named obstacle. Loading all 4 produces 800+ lines of overlapping scripts and degrades close recommendation quality.
- Do not load Training-System for tactical close questions. Different operating layer — operator running the org vs. closer running the call.
- Do not pull `10-Lead-Nurture/Hormozi-Lead-Nurture-Execution-Culture.md` by default. It is adjacent (both about sales-team operations) but canonical in `/lead-nurture`. Sales execution culture and on-call objection handling are different operating moments.
- Do not collapse `/sales` with `/offers`. The most common /sales misroute is when the user says "my sales aren't working" — that's almost always an *offer* problem (weak value), not a *closing* problem. Diagnose which layer is broken before deploying close scripts.
- Closing scripts are reproduced verbatim from source where the exact words are the deliverable. Preserve verbatim wording; do not paraphrase the canonical scripts unless explicitly adapting them to the user's brand voice.

## Output expectations
- For a "why aren't we closing" diagnosis: confirm STAR qualification first; if STAR is broken, this is an advertising/lead-nurture problem, not a closing problem — escalate. If STAR is satisfied, identify which blame branch the rep is failing to handle, prescribe the specific 2-3 closes from that branch's library.
- For a specific objection: identify the branch + flavor → pull the matching close library section → recommend 2-3 verbatim closes the operator should drill (per Rule 6 — "two or three closes per obstacle is enough").
- For a training program build: walk the drill cadence (single-obstacle-per-day huddle + tape review + record-everything + practice on unqualified leads + operator stays current). Reference the Gym Launch case as the proof point.
- For a specific script writing request: deploy the relevant verbatim close from the library (don't paraphrase Hormozi's exact wording — the words are the deliverable). Adapt only the bracketed variables ([X], [goal], [outcome]) to the user's context.
- Always end with a concrete next operator move (which close to drill this week, which call to record-and-review, which prospect to test the script on), not a strategic summary.
