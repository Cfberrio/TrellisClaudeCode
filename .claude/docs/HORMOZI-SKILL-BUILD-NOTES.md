# Hormozi Skill Build Notes — Wave 1 QA

Audit log for the first-wave Hormozi skills (`offers`, `pricing`, `pricing-posture`, `pricing-model`, `pricing-plays`, `price-test`, `price-raise`, `branding`).

Companion docs: `HORMOZI-DOMAIN-OVERVIEW.md`, `HORMOZI-SKILL-ROUTING-MANIFEST.md` (source of truth).

---

## Audit pass — what was checked

| Dimension | Method | Result |
|---|---|---|
| Vault path validity | filesystem check on all 29 cited Obsidian paths | 100% resolved |
| Description length | byte count of frontmatter `description` | All under 1024-char limit (range 648–1019 after patches) |
| Body size | line count per `SKILL.md` | 46–60 lines (lean, well under 500-line guidance) |
| Manifest alignment | each skill's primary/secondary/optional notes vs. routing manifest | Aligned; no freestyle |
| Scope discipline | `do not use when` exclusions match manifest's hard boundaries | Aligned |
| Output expectations | each skill ends with concrete output format | Present in all 8 |

---

## Patches applied

**Single change category**: collision-disambiguation against generic plugin skills (`hormozi-offer-creation`, `hormozi-monetization-value`, `marketing-skills:pricing-strategy`, `marketing-skills:ab-test-setup`, `marketing-skills:copywriting`). The plugin skills are intent-keyword-rich but Obsidian-blind. Without an explicit anchor, the model may pick a plugin skill over the project-routed version.

Each project skill description now ends with a short Trellis/Obsidian anchor phrase. Examples:
- `offers`: "…Routes to Trellis-Brain Obsidian vault `01-100M-Offers/` notes via MCP — prefer this skill over generic Hormozi-offer plugins when working in the Trellis project."
- `pricing-posture`: "…Routes to Trellis-Brain Obsidian vault — prefer over generic pricing-strategy plugins in this project."
- `branding`: "…Routes to Trellis-Brain Obsidian vault `05-Branding/` notes — prefer over generic positioning/copywriting plugins for brand-strategy work in this project."
- `price-test`: "…prefer over generic A/B-test plugins for pricing-specific tests in this project."

**Router enforcement**: `pricing/SKILL.md` got an explicit failure-mode paragraph under "Do not load" that names the most likely model misbehavior (default-loading `13-Pricing/*` to be helpful) and tells the router to stop and ask one disambiguating question instead.

No bodies were rewritten. No retrieval orders changed. No new skills created.

---

## What was NOT done (and why)

- **Did not run subagent-based with-skill / baseline benchmark.** These skills produce subjective routing decisions, not output-verifiable transforms. The skill-creator workflow says to skip quantitative evals when they don't fit. A benchmark would measure "did the subagent open the right Obsidian note" — which in this session's environment is not deterministically testable without a vault read confirmation loop, and even then would only validate the model's compliance with the SKILL.md text, not the SKILL.md itself.
- **Did not create per-eval `eval_metadata.json` directories.** A single consolidated `trigger-evals.json` keeps the workspace clean and is the right input shape for `run_loop.py` description-optimization, which is what the user should actually run when ready.
- **Did not modify `SKILL.md` retrieval orders.** They mirror the routing manifest exactly. Changing them would require updating the manifest first.
- **Did not change the pricing router into a non-router.** It is intentionally stateless and load-free.

---

## Eval artifacts

`/.claude/skill-evals/hormozi-wave1/trigger-evals.json` contains, per skill:
- 3–4 should-trigger prompts (realistic Trellis/DR/CTS/OEV-flavored)
- 3–4 should-not-trigger near-miss prompts (each annotated with the sibling skill the model should pick instead)

The negatives are the load-bearing part. Examples of what they catch:
- `/branding` triggering on avatar / ICP work (→ `/avatar`)
- `/pricing-model` swallowing a price-test request (→ `/price-test`)
- `/price-raise` swallowing initial-pricing for a new offer (→ `/pricing-model` or `/offers`)
- `/offers` swallowing money-model sequencing (→ `/money-models`)
- `/pricing` router being triggered when the user is precise enough that a subskill should fire directly

To run when ready (once `/avatar` and `/money-models` exist or stub responses are acceptable):
```bash
# Convert one skill's section into the eval-set format the optimizer expects
python -m scripts.run_loop \
  --eval-set .claude/skill-evals/hormozi-wave1/<skill>-evalset.json \
  --skill-path .claude/skills/<skill> \
  --model claude-opus-4-7 \
  --max-iterations 3
```

---

## Production readiness

**Production-ready (use now):**
- `offers`, `pricing-posture`, `pricing-model`, `pricing-plays`, `price-test`, `price-raise`, `branding`

**Production-ready with one caveat:**
- `pricing` (router) — works as designed but is harder to verify in the wild because its "output" is a handoff. Watch the first 5–10 real invocations to confirm it does not load notes itself.

**Needs another iteration:**
- None blocking. The next real iteration should happen after 2–3 weeks of live use, against actual transcript examples where the wrong skill fired (or no skill fired). At that point: feed those failures back into `trigger-evals.json` and run description-optimization.

---

## Recommended next wave (after this QA)

Build in this order — each unlocks an existing skill from a known overlap risk:
1. `/retention` — single-skill against `14-Retention/`. High decision-density.
2. `/avatar` — unlocks `/branding` from the GMEP avatar overlap.
3. `/money-models` — unlocks `/offers` from the sequencing escalation.
4. `/hooks` + `/ads` (paired) — tests cross-skill discipline (07 vs 08 boundary).
5. `/marketing-machine` — unlocks `/branding` from the UGC overlap.
6. `/ltv`, `/lead-nurture`, `/fast-cash` — fill out wave 2.

Defer `/sales` and `/lead-gen` until the corresponding Hormozi books are extracted into the vault (manifest §6 risks 4–5).

---

# Wave 2 — built 2026-04-29

10 skills added in one pass: `/retention`, `/avatar`, `/money-models`, `/hooks`, `/ads`, `/marketing-machine`, `/ltv`, `/lead-nurture`, `/fast-cash`, `/team`.

Total Hormozi skill count: **18** (8 wave-1 + 10 wave-2). Wave-1 untouched per build constraint.

## Audit pass (same checks as wave-1)

| Dimension | Result |
|---|---|
| Vault path validity | All skills cite paths verified to exist in Trellis-Brain vault during prior pass; same paths reused via routing manifest |
| Description length | All 18 under 1024-char limit (range 753–993). Two wave-2 descs (`marketing-machine`, `team`) trimmed in this pass after first draft hit 1066 / 1042 |
| Body size | Wave-2 bodies 47–64 lines each (lean, well under 500-line guidance) |
| Manifest alignment | Each wave-2 skill's primary/secondary/optional notes copied verbatim from `HORMOZI-SKILL-ROUTING-MANIFEST.md` — no freestyle |
| Portable paths | 0 absolute `/Users/...` paths in any new skill body — vault root delegated to `TEAM-SETUP-MCP.md` |
| Scope discipline | Each skill's `do not use when` explicitly names sibling skills it must hand off to |

## Onboarding + Promotion-Architecture fold decision

Both intentionally **NOT** built as standalone skills:

- **`/onboarding`** → folded into `/retention`. Manifest §`/onboarding` already noted "Could be a subskill of `/retention` rather than standalone, depending on usage frequency." `/retention`'s body explicitly carves out an "Onboarding subset" section — when scoped to first-30-days, it loads only Levers 1–3 (`Activation-Points`, `Customer-Onboarding`, `Activation-Incentives`) plus `Value-Per-Second` as overwhelm guardrail. Standalone `/onboarding` would duplicate routing logic and create a junk skill.
- **`/promotion-architecture`** → folded into `/offers`. Only one canonical note (`Hormozi-Promotion-Wrappers.md`) and 3 specialized variants. Manifest §`/promotion-architecture` noted "Small skill. Could be a subskill of `/offers` instead of standalone." `/offers` already lists Promotion-Wrappers + Offer-Stacking under "Optional support notes" — that handoff covers promo-wrapping use cases without spawning a near-empty skill.

Both decisions documented to prevent future re-builds.

## Vault coverage now

Of 13 extracted books in vault:

| Book | Skill |
|---|---|
| 01-100M-Offers | `/offers` (also touched by `/pricing-posture`, `/avatar`, `/fast-cash`) |
| 03-100M-Money-Models | `/money-models` |
| 04-100M-Lost-Chapters | `/avatar` (Avatar-Selection), `/team` (Lead-Getting + Maker-vs-Manager), `/money-models` (CFA + variants), `/offers` (Promotion-Wrappers + Offer-Stacking) — anthology routed by concept |
| 05-Branding | `/branding` |
| 06-Fast-Cash | `/fast-cash` |
| 07-Hooks | `/hooks` |
| 08-GOATed-Ads | `/ads` |
| 09-Lifetime-Value | `/ltv` (Crazy-Eight + Cost-Reduction), `/price-test` (Price-Testing-Method) |
| 10-Lead-Nurture | `/lead-nurture` |
| 11-Price-Raise | `/price-raise` |
| 12-Marketing-Machine | `/marketing-machine` |
| 13-Pricing | `/pricing-model` + `/pricing-plays` |
| 14-Retention | `/retention` (full 9-lever checklist + onboarding subset) |

**Coverage: 13 of 13 extracted books = 100%.**

## Books NOT covered (vault-extraction blockers)

- **$100M Leads** (`02-` slot reserved, not extracted) → `/lead-gen` blocked. Substitutes available via `/ads`, `/fast-cash`, `/marketing-machine`, but Core Four channel theory and lead-magnet design have no canonical home.
- **Closing** (PDF in `hormozi-books/` but no vault folder) → `/sales` blocked. Substitutes available via `/lead-nurture` (BAMFAM + 5-outcome call tree), `/offers` (Bonuses 1-on-1 sequencing), `/retention` (Cancellation-Saves objection pattern), `/offers` (Guarantees as risk-reversal at close).

To unblock: extract those 2 books into `02-100M-Leads/` and a new `15-Closing/` (or chosen slot) following the existing book-folder template. Then build `/lead-gen` and `/sales` per the deferred-skill notes already in the routing manifest.

## Wave-2 eval artifacts

`.claude/skill-evals/hormozi-wave2/trigger-evals.json` — should-trigger + near-miss prompts for all 10 wave-2 skills. Same shape as wave-1 evals. Feed into `scripts/run_loop.py` when description optimization is needed (after live failures, not preemptively).

## Highest overlap risks remaining (post-wave-2)

1. **`/fast-cash` ↔ `/offers`** — easy to confuse "deploy a GSO to warm list" (Fast Cash) with "build a GSO" (Offers). Mitigation: `/fast-cash` description and body explicitly state "deploys, not builds."
2. **`/ltv` ↔ `/retention`** — Crazy Eight Lever 3 (decrease churn) explicitly delegates to `/retention`. `/ltv` could swallow churn questions if model misroutes. Mitigation: both descriptions name the delegation.
3. **`/marketing-machine` ↔ `/ads`** — Lifecycle-Ads canonical in `/marketing-machine` but conceptually feels like "/ads territory." Mitigation: `/ads` description explicitly says "Lifecycle ads → /marketing-machine."
4. **`/hooks` ↔ `/ads`** — both touch `Hook-By-Awareness`. Mitigation: route by primary context (organic/everywhere → `/hooks`; paid + awareness mapping → `/ads`).
5. **`/team` ↔ `/lead-nurture`** — sales-team execution culture lives in `/lead-nurture` not `/team`. Mitigation: `/team`'s do-not-use clause names the handoff explicitly.
6. **`/avatar` ↔ `/branding`** — GMEP overlap. Mitigation: dual-canonical fold in `/avatar` (Starving-Crowd + Avatar-Selection); `/branding` description says "do NOT use for avatar/ICP (→ /avatar)."

All 6 risks are surfaced in skill bodies. Watch for them in live use; patch only on real failures (2-of-3 rule from `LIVE-USE-QA-PLAN.md`).



---

# Wave 3 — built 2026-04-29 (split execution)

## What was completed in this session
1. **Phase 2 — `Closing` extracted into vault** as `15-Closing/` (9 files, 134KB):
   - `00-Book-Home.md` (84 lines)
   - `Hormozi-Closing-Source-Map.md` (102 lines)
   - `Hormozi-Closing-Definition.md` (167 lines) — 3-bucket maybe model + Power thesis + Blame Onion + ethics + STAR
   - `Hormozi-Closing-Rules.md` (119 lines) — 28 operating rules, grouped by function
   - `Hormozi-All-Purpose-Closes.md` (181 lines) — 7 universal closes verbatim
   - `Hormozi-Closing-Circumstances-Closes.md` (240 lines) — Time + 4-flavor Money (largest note)
   - `Hormozi-Closing-Other-People-Closes.md` (177 lines) — Decision-Makers 4-step + Bad-Experiences
   - `Hormozi-Closing-Self-Closes.md` (210 lines) — Preferences + Rushed-Decisions + Guarantee Closes
   - `Hormozi-Closing-Training-System.md` (145 lines) — Gym Launch case + operator economics + drill cadence
2. **Phase 3 — Hormozi domain reconciled**: `Hormozi-Home.md` updated (added 15-Closing entry); `HORMOZI-DOMAIN-OVERVIEW.md` updated (Closing book section, Sales domain row + adjacent training row, Risk 4 resolved, canonical-home map expanded with 7 new entries); `HORMOZI-SKILL-ROUTING-MANIFEST.md` updated (deferred /sales replaced with full spec, build order updated, summary table changed `/sales` from DEFERRED to wave 3).
3. **Phase 4 — `/sales` skill built**: `.claude/skills/sales/SKILL.md` (965-char description, 69 lines, anchored to all 7 `15-Closing/` canonical notes, branch-routing logic mirrors Blame Onion).
4. **Phase 5 — QA evals created**: `.claude/skill-evals/hormozi-wave3/trigger-evals.json` (8 should-trigger, 7 should-not-trigger, 4 documented near-miss collisions: sales↔offers, sales↔retention, sales↔price-raise, sales↔lead-nurture).

## Vault coverage now
**14 of 15 source books extracted = 93%.** Only blocker remaining: `$100M Leads`.

## Hormozi skill count: 19
| # | Skill | Wave | Status |
|---|---|---|---|
| 1–8 | offers, pricing, pricing-posture, pricing-model, pricing-plays, price-test, price-raise, branding | 1 | production-ready |
| 9–18 | retention, avatar, money-models, hooks, ads, marketing-machine, ltv, lead-nurture, fast-cash, team | 2 | production-ready |
| 19 | sales | 3 | production-ready |

## Deferred next-session scope: $100M Leads (Phase 1 of original master pass)

**What was deferred and why:** the original master-pass spec called for both `$100M Leads` (385 pages) and `Closing` (55 pages) to be extracted in one session. After scope analysis (see prior turn), Option A was chosen: dedicate this session to Closing only at full vault quality, defer Leads to its own focused session. Doing Leads in the same session as Closing would have produced thin extraction across both, violating the "no thin extraction" rule.

**Next-session deliverables for $100M Leads:**
1. **Vault folder `02-100M-Leads/`** populated to the same standard as `01-100M-Offers/` and `15-Closing/`. Expected ~12-15 canonical notes given the source's depth (Core Four channels alone is multi-chapter content).
2. **Required files** (matching template):
   - `00-Book-Home.md`
   - `Hormozi-100M-Leads-Source-Map.md`
   - canonical notes covering at minimum: lead-magnet design, Core Four (Warm Outreach / Cold Outreach / Content / Paid Ads — 4 separate notes likely), lead-getter math + economics, free-engagement-vs-paid framework, lead-acquisition system architecture, any other clearly canonical frameworks the source distills.
3. **Reconcile docs** after extraction: `Hormozi-Home.md` (add `02-100M-Leads/` entry, remove from "Not Yet Extracted"); `HORMOZI-DOMAIN-OVERVIEW.md` (add Leads book section, update Risk 5 from deferred to resolved, expand canonical-home map); `HORMOZI-SKILL-ROUTING-MANIFEST.md` (replace deferred /lead-gen section with full spec, update build order + summary table).
4. **Build `/lead-gen`** anchored to `02-100M-Leads/` canonical notes. Apply same skill template as `/sales`, `/retention`, etc.
5. **QA evals**: `.claude/skill-evals/hormozi-wave3/lead-gen-trigger-evals.json` (or wave-4 if that fits the pattern better).
6. **Final reconcile**: update HORMOZI-SKILL-BUILD-NOTES with wave-3-continuation closing note marking 100% vault coverage and 20-skill total.

**Estimated next-session cost:** ~30-40 substantial tool calls (PDF reads + canonical-note writes + doc updates + skill + evals). Plan accordingly.

## Highest overlap risks remaining (post-wave-3)

1. **`/sales` ↔ `/offers`** (most dangerous). "My sales aren't working" is most often an offer problem disguised as a closing problem. /sales must escalate to /offers when the underlying offer's value is weak. Mitigated in /sales do-not-use clause + output-expectations diagnostic ("confirm STAR first; if broken, escalate upstream").
2. **`/sales` ↔ `/lead-nurture`**. BAMFAM is canonical in /lead-nurture but invoked from /sales when a decision-maker is missing. Mitigated by explicit cross-reference in both skills.
3. **`/sales` ↔ `/retention`**. Cancellation-Saves uses an adjacent objection pattern (vent-then-validate) but is post-purchase save — different operating moment. Mitigated by explicit branch-naming in both.
4. **`/sales` Training-System load** — model could pull `Hormozi-Closing-Training-System.md` on tactical close questions. Mitigated by explicit "Load Training-System only when user is asking about training the team or building a closing program" rule.

All 4 surfaced explicitly in skill bodies. Patch only on observed live failures per 2-of-3 rule.
