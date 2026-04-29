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
