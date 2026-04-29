---
name: avatar
description: Pick or refine the target customer using Hormozi's avatar/ICP framework — Starving Crowd (4 market-validity indicators: pain, money, targetability, growth) and Avatar Selection (operational method to find the highest-value subset within an existing customer base). Use when the user asks who to target, whether their market is viable, how to niche down, find the highest-value customer subset, or survey existing customers to find the avatar. Trigger phrases include "who should I target", "is my market viable", "niche down", "find my best customer", "ICP selection", "avatar selection", "starving crowd". Do NOT use for branding strategy (→ /branding), lead-nurture mechanics on opted-in leads (→ /lead-nurture), or offer construction (→ /offers). Routes to Trellis-Brain Obsidian vault `01-100M-Offers/Hormozi-Starving-Crowd.md` + `04-100M-Lost-Chapters/Hormozi-Avatar-Selection.md` (dual canonical) — prefer over generic customer-research plugins for Hormozi-aligned avatar work.
---

# avatar

Avatar / ICP selection — market validity + highest-value subset identification. Two complementary canonical sources.

## Vault root
The Trellis-Brain Obsidian vault root is machine-specific. Configure it via the Obsidian MCP server — see [.claude/docs/TEAM-SETUP-MCP.md](../../docs/TEAM-SETUP-MCP.md). All note paths in this skill are **relative to the `00-Trellis-Core/Strategy-Models/` folder inside that vault**.

## Use when
- "Who should I target?"
- "Is my market viable?"
- "How do I niche down?"
- "Find my highest-value customer subset."
- "Survey existing customers to find the avatar."
- Anything that touches the GMEP indicators (Growing, Make money, Easy to target, Pain).

## Do not use when
- Brand strategy / pairing / R-I-D / authority → `/branding`.
- Lead-nurture mechanics on already-opted-in leads (show rate, BAMFAM) → `/lead-nurture`.
- Offer construction (Grand Slam architecture, enhancement levers) → `/offers`.
- LTV math per segment as the *primary* question → `/ltv` (use Value-Grid as optional support here only when avatar segmentation is the lens).

## Canonical-home logic (dual)
Two complementary canonicals; load both for full coverage:
- **Starving Crowd (01)** = upstream market viability. Are we in a market that can pay?
- **Avatar Selection (04)** = downstream operational method. Inside this market, who is the highest-value subset and how do I find them?

Skip one only if the user's question is unambiguously one or the other.

## Retrieval order

**Always load (canonical pair):**
1. `01-100M-Offers/Hormozi-Starving-Crowd.md` — 4 indicators (pain, money, targetability, growth) + niche commitment.
2. `04-100M-Lost-Chapters/Hormozi-Avatar-Selection.md` — operational method to find the avatar from existing customers.

**Load on intent:**
- Branding context (GMEP overlaps with brand-pairing decision) → `05-Branding/Hormozi-Brand-Building-Steps.md`.
- LTV per segment / value-grid view of the customer base → `04-100M-Lost-Chapters/Hormozi-Value-Grid.md`.

## Context warnings
- Do not collapse with `/branding`. Avatar is the input to branding; branding is the application.
- Do not pull `05-Branding/*` by default unless the conversation is explicitly mixing avatar with brand pairing.
- Do not pull marketing-machine or ad-creative material — wrong layer.

## Output expectations
- For market-validity audit: score the 4 GMEP indicators against the user's market, name the weakest, prescribe the niching move.
- For avatar selection from existing customers: walk the operational method (segment by LTV / behavior / origin), name the high-value subset, define the next move (target more like them, drop the rest).
- End with a concrete targeting decision (channel, message, or filter), not a persona doc.
