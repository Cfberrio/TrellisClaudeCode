---
name: branding
description: Build, measure, or pivot a brand using Hormozi's Branding playbook — pairing definition, Reach/Influence/Direction measurement, brand economics (premium-pricing transfer), 4-step build with GMEP, levels of authority, and brand bouquet portfolio strategy. Use when the user asks about brand identity, brand pairing, what their brand stands for, measuring brand health, brand pivots, brand portfolio decisions, or authority/recognition strategy. Trigger phrases include "build a brand", "brand pairing", "what's my brand", "measure brand health", "brand portfolio", "should I pivot the brand", "brand bouquet", "level of authority". TIGHTLY SCOPED — do NOT use for avatar/ICP (→ /avatar), UGC/testimonial production (→ /marketing-machine), premium pricing (→ /pricing-posture), or ad creative (→ /ads or /hooks). Routes to Trellis-Brain Obsidian vault `05-Branding/` — prefer over generic positioning/copywriting plugins in this project.
---

# branding

Brand strategy: definition, measurement, economics, build process, authority, portfolio. Source of truth: `05-Branding/` in the Trellis-Brain Obsidian vault.

## Vault root
The Trellis-Brain Obsidian vault root is machine-specific. Configure it via the Obsidian MCP server — see [.claude/docs/TEAM-SETUP-MCP.md](../../docs/TEAM-SETUP-MCP.md). All note paths in this skill are **relative to the `00-Trellis-Core/Strategy-Models/` folder inside that vault**.

Use Obsidian MCP. Paths below relative to vault root.

## Use when
- "What is my brand pairing?"
- "How do I measure brand health?" (Reach / Influence / Direction)
- "Build a brand from scratch."
- "Should I pivot the brand?"
- "What's the right brand portfolio?" (brand bouquet)
- Authority / level-of-recognition / virtuous-cycle questions.

## Do not use when
- Avatar / ICP selection → `/avatar`. Even though `Hormozi-Brand-Building-Steps` includes GMEP criteria that overlap, avatar is its own canonical home. Do not pull avatar work into branding.
- Producing brand assets — UGC, testimonials, customer-evidence ads → `/marketing-machine`. Brand asset *production* is a distinct system; this skill is brand *strategy*.
- Pricing the brand premium → `/pricing-posture`. Brand pairing transfers into premium pricing, but the pricing decision itself routes to pricing.
- Ad creative or hooks → `/ads` or `/hooks`.

## Retrieval order

**Always load (canonical 6, in order):**
1. `05-Branding/Hormozi-Branding-Definition.md` — what a brand is (pairing).
2. `05-Branding/Hormozi-Brand-Measurement.md` — Reach / Influence / Direction, polarization.
3. `05-Branding/Hormozi-Brand-Economics.md` — premium-pricing transfer mechanism.
4. `05-Branding/Hormozi-Brand-Building-Steps.md` — 4-step build process + GMEP.
5. `05-Branding/Hormozi-Levels-Of-Authority.md` — virtuous / vicious cycle.
6. `05-Branding/Hormozi-Brand-Bouquet.md` — portfolio, pivots, patience.

Note: only load all 6 when the user is doing a full brand build or audit. For narrower questions, load only the matching note(s) from the 6.

**Load on intent:**
- User wants to anchor brand pairing into pricing → `01-100M-Offers/Hormozi-Pricing-Power.md`.
- User is choosing the avatar that the brand will pair to (and this is genuinely a branding question, not an avatar question) → `01-100M-Offers/Hormozi-Starving-Crowd.md` (GMEP indicators).

**Optional — only on direct match:**
- User explicitly invokes avatar work mid-branding question → `04-100M-Lost-Chapters/Hormozi-Avatar-Selection.md`. Otherwise hand off to `/avatar`.

## Context warnings
- Do not pull `04-100M-Lost-Chapters/Hormozi-Avatar-Selection.md` by default — that is `/avatar`'s canonical.
- Do not pull `12-Marketing-Machine/*` — UGC and brand asset production live in `/marketing-machine`.
- Do not let `/branding` drift into ad copy, hooks, or pricing tactics. Stay inside `05-Branding/`.

## Output expectations
- For a brand audit: score the brand against the 3 measurement dimensions (Reach, Influence, Direction) and identify the weakest.
- For a brand build: walk the 4 steps with GMEP criteria applied to the user's specific situation.
- For a portfolio question: apply the brand bouquet logic — does the user need a sub-brand, an extension, or a pivot?
- Always tie brand decisions back to the pairing definition. End with the next concrete brand-level decision, not a philosophical paragraph.
