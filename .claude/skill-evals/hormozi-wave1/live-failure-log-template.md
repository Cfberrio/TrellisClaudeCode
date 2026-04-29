# Live Failure Log — Hormozi Wave 1

Paste this block per failure. Fill 8 lines. 60 seconds max.

---

```
Date: 2026-MM-DD
Brand context: (Trellis Fields | CTS | DR | OEV)
User prompt: <one line, exact wording>
Skill that fired: <skill-name | none | wrong-plugin:name>
Skill that should have fired: <skill-name>
What went wrong: (wrong trigger | no trigger | overtrigger | router collapse | wrong vault note loaded | scope drift)
Failure type: (trigger | routing | both)
Fix hypothesis: <one sentence — e.g. "add 'instant profit' phrase to /pricing-plays trigger" | "tighten /branding do-not-use to exclude positioning copy" | "router loaded 13-Pricing/Pricing-Rules instead of handing off to /pricing-model">
Severity: (low: noise, single occurrence | med: repeated phrasing pattern | high: blocked real work or router collapse)
```

---

## Worked example

```
Date: 2026-05-03
Brand context: DR
User prompt: we want to lift OEV booking fees on new bookings only — quick processing fee passthrough this week
Skill that fired: pricing
Skill that should have fired: pricing-plays
What went wrong: router collapse — /pricing read 13-Pricing/Hormozi-Instant-Profit-Pricing-Plays.md itself instead of routing to /pricing-plays
Failure type: routing
Fix hypothesis: router body needs stronger anti-load language for "instant profit" / "processing fee" intents that map cleanly to /pricing-plays — currently router treats them as ambiguous
Severity: high
```

---

## Triage rules (cross-reference LIVE-USE-QA-PLAN.md)

- **1 occurrence** → log only.
- **≥3 of same pattern in 2 weeks** → patch SKILL.md.
- **Router collapse** → always high severity, even on first occurrence.
- **Wrong vault note loaded** → routing failure, not trigger failure. Patch retrieval order.
- **No skill fired but should have** → trigger failure. Patch description (add the missing phrase).
- **Skill fired but should not have** → trigger failure. Tighten description's do-not-use clause.

---

## Where to file

Monthly file: `.claude/skill-evals/hormozi-wave1/failures-YYYY-MM.md`
- New month → new file.
- One file per month keeps triage scannable.
- Append blocks chronologically.

Don't create per-skill files. Cross-skill collisions only show up when failures sit next to each other.
