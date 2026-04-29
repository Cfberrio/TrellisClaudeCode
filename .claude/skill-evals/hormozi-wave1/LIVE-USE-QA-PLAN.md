# Live-Use QA Plan — Hormozi Wave 1

Lightweight protocol. Validate 8 first-wave skills against real Trellis work. Improve only from observed failures.

Scope: `offers`, `pricing`, `pricing-posture`, `pricing-model`, `pricing-plays`, `price-test`, `price-raise`, `branding`.

---

## What to watch for

Four failure modes. Each has a tell.

| Failure | Tell |
|---|---|
| **Wrong trigger** | A Hormozi skill fires but you wanted a different one. Output cites wrong vault folder or wrong concept. |
| **No trigger** | You ask a clear Hormozi question, no skill fires, model freelances or pulls a generic plugin (`hormozi-monetization-value`, `marketing-skills:pricing-strategy`, etc.). |
| **Overtrigger** | Skill fires on tangential mention. Example: `/branding` activates because user said "brand" while really asking about avatar/ICP. |
| **Router collapse** | `/pricing` fires and starts reading `13-Pricing/*` itself instead of handing off to a subskill. |

---

## How to detect each, fast

**Wrong trigger** → output names a vault path that doesn't match user intent. Check first paragraph of response.

**No trigger** → no `Skill` tool call in transcript, or output sounds generic-Hormozi (book-summary tone) instead of Trellis-routed (specific note paths, brand context).

**Overtrigger** → response opens with a do-not-use-when handoff or contradicts itself ("you're asking about X but this skill is for Y"). That self-correction = the skill fired wrong.

**Router collapse on `/pricing`** → see "router failure shape" below.

---

## Router failure shape (`/pricing`)

`/pricing` is correct when its response is short:
1. One sentence diagnosing intent.
2. One sentence naming the chosen subskill + canonical note.
3. Handoff.

`/pricing` has failed when response:
- Loads or quotes content from `13-Pricing/*`, `01-100M-Offers/Hormozi-Pricing-Power.md`, `09-Lifetime-Value/Hormozi-Price-Testing-Method.md`, or `11-Price-Raise/*` directly.
- Recommends pricing actions without first naming a subskill.
- Lists all 5 subskills as "consider any of these" instead of picking one.
- Asks more than one disambiguating question (one is fine; two = stalling).

If you see any of these → log as Router Collapse, severity High.

---

## Capture protocol (low-friction)

Don't write essays. When skill misfires:

1. Open `live-failure-log-template.md`.
2. Copy template block, fill 8 lines, paste into a daily notes file or `.claude/skill-evals/hormozi-wave1/failures-YYYY-MM.md`.
3. Move on. Triage weekly.

Cap at 60 seconds per failure. If it takes longer, you're over-thinking it.

---

## When to revise a skill

Three signals. Need at least 2 of 3 before touching a SKILL.md.

1. **Frequency** — same failure mode appears ≥3 times across different real prompts in 2 weeks.
2. **Consistency** — failure reproduces on similar phrasings, not just one weird prompt.
3. **Cost** — failure caused real rework (wrong note loaded, wrong recommendation given, time wasted).

If only 1 of 3 → it's user-phrasing noise. Log and move on.

If 2 of 3 → patch description (add trigger phrase, sharpen do-not-use clause).

If 3 of 3 → patch description AND body (retrieval order, scope language). Update routing manifest if the boundary itself was wrong.

---

## Triage cadence

Weekly. 15 minutes max.

1. Open the month's failure log.
2. Group by skill.
3. Apply 2-of-3 test.
4. Patch any skill that crosses threshold.
5. Add the failing prompt to `trigger-evals.json` so it won't regress.
6. If you patched, re-run `scripts/run_loop.py` for that skill's description only.

---

## What NOT to do

- Don't revise a skill on first failure. Single failures are noise.
- Don't broaden a description to "catch more" if overtriggering. Tighten instead.
- Don't add a 6th pricing subskill because of one weird prompt. Update existing scope first.
- Don't run quantitative benchmarks without real failure data feeding them.
- Don't rewrite the routing manifest from a single live failure. Manifest changes need a documented overlap pattern.

---

## Pressure-test starter set

`live-prompt-batch.json` ships with 30 realistic Trellis prompts to run through the skills before live use begins. Run them in normal sessions and log misfires using the template.

Goal of starter set: shake out the obvious collisions before real work depends on the skills. Not a benchmark — a sanity check.
