---
name: lead-nurture
description: Convert opted-in leads into shows / closes using Hormozi's Lead Nurture playbook (10-Lead-Nurture) — 4 pillars (Availability, Speed, Personalization, Volume) + BAMFAM (book-meeting-from-meeting) + sales-team execution culture. Distinct operational layer between advertising and sales. Use when the user asks why leads aren't showing up, how to follow up faster, build a reminder cadence, optimize show rate, train an SDR / sales team execution culture, or anything BAMFAM. Trigger phrases include "leads not showing", "follow up faster", "reminder cadence", "show rate", "BAMFAM", "book meeting from meeting", "SDR culture", "lead nurture pillars", "speed to lead". Do NOT use for lead generation / acquisition mechanics (no canonical home — see /lead-gen deferred), sales close / objection handling on the call (→ /sales deferred), or long-term retention / churn (→ /retention). Routes to Trellis-Brain Obsidian vault `10-Lead-Nurture/` notes.
---

# lead-nurture

Post-opt-in lead conversion — the operational layer between ads and the sale. Source of truth: `10-Lead-Nurture/` in the Trellis-Brain Obsidian vault.

## Vault root
The Trellis-Brain Obsidian vault root is machine-specific. Configure it via the Obsidian MCP server — see [.claude/docs/TEAM-SETUP-MCP.md](../../docs/TEAM-SETUP-MCP.md). All note paths in this skill are **relative to the `00-Trellis-Core/Strategy-Models/` folder inside that vault**.

## Use when
- "Why aren't leads showing up?"
- "How do I follow up faster?"
- "Build a reminder cadence."
- "Optimize show rate."
- "Train an SDR / sales team execution culture."
- BAMFAM / book-meeting-from-meeting questions.

## Do not use when
- Lead generation / acquisition mechanics (Core Four channels, lead-magnet design) → no canonical home; see `/lead-gen` deferred status.
- Sales close / objection handling on the live call → `/sales` deferred status.
- Long-term retention / churn (post-purchase) → `/retention`.
- Cold-traffic acquisition or paid-ad construction → `/ads`.

## Canonical-home logic
10-Lead-Nurture is canonical for post-opt-in nurture. BAMFAM is canonical here even though it's reusable across sales contexts.

## Retrieval order

**Always load (umbrella):**
1. `10-Lead-Nurture/Hormozi-Lead-Nurture-Four-Pillars.md` — umbrella.

**Load on intent (the pillar matching user's question):**
- Hours of operation, channel coverage, response windows → `Hormozi-Lead-Nurture-Availability.md`.
- Speed-to-lead, the 5-outcome call decision tree, hot handoff → `Hormozi-Lead-Nurture-Speed.md`.
- Personal first message, video DM, voice note, lead detail mining → `Hormozi-Lead-Nurture-Personalization.md`.
- Touch-volume cadence, multi-channel orchestration → `Hormozi-Lead-Nurture-Volume.md`.

**Load on direct request:**
- BAMFAM (any "next call booking" intent) → `Hormozi-BAMFAM.md`.
- Team / SDR / training questions → `Hormozi-Lead-Nurture-Execution-Culture.md`.

**Optional — only on direct match:**
- Warm-list activation prerequisite → `06-Fast-Cash/Hormozi-Fast-Cash-Play.md` (Lead Nurture is prerequisite for Fast Cash).

## Context warnings
- 10-Lead-Nurture covers a specific, distinct layer (post-opt-in, pre-sale). Do not dump into `/sales` or `/lead-gen`.
- Do not pull all 4 pillars by default. Route by the broken pillar.
- BAMFAM may be invoked from sales contexts even though it lives here — load just BAMFAM in that case, not the full 4 pillars.

## Output expectations
- For "leads not showing": diagnose which of the 4 pillars is broken, prescribe the specific pillar's fix.
- For BAMFAM: walk the book-meeting-from-meeting tactic verbatim, name the script and the timing.
- For SDR training: walk Execution-Culture, prescribe the daily/weekly cadence and accountability.
- End with the next operational change (script update, channel install, dashboard metric), not a summary.
