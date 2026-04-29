# Hormozi Skill Routing Manifest

Routing manifest for proposed task-first Claude Code skills against the completed Hormozi Obsidian domain.

All paths rooted at the `00-Trellis-Core/Strategy-Models/` folder inside the Trellis-Brain Obsidian vault. Vault root is machine-specific — see [TEAM-SETUP-MCP.md](TEAM-SETUP-MCP.md).

For domain context and overlap analysis, see `HORMOZI-DOMAIN-OVERVIEW.md`.

**Build order (recommended).** First wave: `/offers`, `/pricing`, `/retention`, `/branding`, `/hooks`, `/ads`. Second wave: `/money-models`, `/ltv`, `/lead-nurture`, `/marketing-machine`, `/fast-cash`, `/avatar`. Third wave: `/sales` (anchored to `15-Closing/`, extracted 2026-04-29). Deferred: `/lead-gen` (no canonical home in vault yet — `02-100M-Leads/` slot reserved but not populated).

---

## /offers

### Purpose
Build, audit, or improve a single offer (Grand Slam Offer architecture). Apply when working on one offer at a time — the construction, the four-component definition, the enhancement levers, the value-equation lens.

### Use when
- "Help me build a new offer."
- "Why is my offer not converting?"
- "How do I make this offer stronger?"
- "Add scarcity / urgency / bonuses / guarantees / a name to my offer."
- "Audit this offer against the Grand Slam definition."
- "What problems should I solve in my offer?"

### Do not use when
- Sequencing multiple offers across customer journey → `/money-models`.
- Specifically raising prices on existing customers → `/price-raise` (or `/pricing` router).
- Producing a quarterly cash promo on a warm list → `/fast-cash`.
- Optimizing LTV through cross-sell / upsell mechanics → `/money-models` or `/ltv`.

### Primary notes
- `Strategy-Models/01-100M-Offers/Hormozi-Grand-Slam-Offer.md`
- `Strategy-Models/01-100M-Offers/Hormozi-Value-Equation.md`
- `Strategy-Models/01-100M-Offers/Hormozi-Offer-Creation.md`

### Secondary notes
- `Strategy-Models/01-100M-Offers/Hormozi-Pricing-Power.md`
- `Strategy-Models/01-100M-Offers/Hormozi-Starving-Crowd.md`
- `Strategy-Models/01-100M-Offers/Hormozi-Scarcity.md`
- `Strategy-Models/01-100M-Offers/Hormozi-Urgency.md`
- `Strategy-Models/01-100M-Offers/Hormozi-Bonuses.md`
- `Strategy-Models/01-100M-Offers/Hormozi-Guarantees.md`
- `Strategy-Models/01-100M-Offers/Hormozi-Naming.md`

### Optional support notes
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-Promotion-Wrappers.md` — premium / free / discount wrappers around the Grand Slam Offer.
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-Offer-Stacking.md` — sequencing across multiple Grand Slam Offers in sales.
- `Strategy-Models/01-100M-Offers/00-Book-Home.md` — book hub for orientation.

### Canonical-home logic
01-100M-Offers is the umbrella offer canonical. Every later book references back to it. Always anchor here.

### Retrieval order
1. Value Equation (foundation lens — load first).
2. Grand Slam Offer (umbrella definition).
3. Offer Creation (construction process).
4. Whichever enhancement lever the user is currently asking about (Scarcity / Urgency / Bonuses / Guarantees / Naming).
5. Pricing Power if pricing is implicit in the question.
6. Starving Crowd only if upstream market validity is uncertain.

### Context warnings
- Do not load all 10 notes by default. Heavy. Route by intent.
- Loading Money Models content while the user is on a single-offer question creates confusion — keep `/offers` and `/money-models` strictly separate.

---

## /money-models

### Purpose
Sequence multiple offers across the customer's first 30 days. Customer-Financed Acquisition. Attract → Upsell → Downsell → Continuity.

### Use when
- "Design a money model for my business."
- "What should the offer sequence look like?"
- "Why is my CAC > LTGP?"
- "How do I get to CFA / break even on day 30?"
- Questions about specific mechanisms: classic upsell, anchor upsell, payment plan, trial-with-penalty, feature downsell, continuity bonus, etc.

### Do not use when
- Building a single offer → `/offers`.
- Pure LTV-lift levers (price, cost, frequency) without sequencing context → `/ltv`.
- Specifically about retention / churn — `/retention`.

### Primary notes
- `Strategy-Models/03-100M-Money-Models/Hormozi-Money-Model.md`
- `Strategy-Models/03-100M-Money-Models/Hormozi-Money-Model-Assembly.md`
- `Strategy-Models/03-100M-Money-Models/Hormozi-Attraction-Offers.md`
- `Strategy-Models/03-100M-Money-Models/Hormozi-Upsell-Offers.md`
- `Strategy-Models/03-100M-Money-Models/Hormozi-Downsell-Offers.md`
- `Strategy-Models/03-100M-Money-Models/Hormozi-Continuity-Offers.md`

### Secondary notes
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-Customer-Financed-Acquisition.md`
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-CFA-Three-Levers.md`
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-Value-Grid.md`
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-Offer-Stacking.md`

### Optional support notes
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-Attraction-Free-Presentations.md`
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-Attraction-Freemium.md`
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-Attraction-Pick-Your-Price.md`
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-Upsell-Free-Alt-Revenue.md`
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-Continuity-Lifetime-Upgrades.md`
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-Continuity-Lifetime-Discounts.md`
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-Continuity-Discount-Plus-Fee.md`
- `Strategy-Models/01-100M-Offers/Hormozi-Grand-Slam-Offer.md` — every Money Model offer is a GSO at its own slot.
- `Strategy-Models/01-100M-Offers/Hormozi-Value-Equation.md` — foundation.

### Canonical-home logic
Money Model architecture canonical in 03. CFA economics canonical in 04. Specialized mechanics canonical in 04 sub-notes. Money Models is *not* the canonical for Bonuses / Guarantees / Pricing-Power — those stay in 01.

### Retrieval order
1. Hormozi-Money-Model (umbrella).
2. CFA-Three-Levers (math).
3. The four offer-type notes — load only the slot the user is asking about.
4. Money-Model-Assembly when designing the full sequence.
5. Specialized 04-Lost-Chapters mechanics only on direct match.

### Context warnings
- Lots of overlap with `/offers`. Load offer-construction (01-100M-Offers/Offer-Creation) only when user explicitly needs to build the underlying offer; otherwise stay at the sequencing layer.
- Continuity offer architecture is canonical in 03, but specialized variants (Lifetime Upgrades, Lifetime Discounts, Discount + Fee) live in 04. Match by intent.

---

## /pricing (router)

### Purpose
Pricing is four distinct domains in this vault. This skill is a **router** that selects the right sub-context based on user intent.

### Use when
- Any pricing question.

### Do not use when
- Question is purely about offer construction (use `/offers`).
- Question is purely about LTV-lifting levers other than price (use `/ltv`).

### Sub-routing logic

| User intent | Route to | Primary notes |
|---|---|---|
| "Why charge premium?" / philosophy / commodity trap / virtuous cycle | `/pricing-posture` | `01-100M-Offers/Hormozi-Pricing-Power.md` |
| "What pricing model should I use?" / cost-plus vs. value-based / 3-models taxonomy / pricing rules | `/pricing-model` | `13-Pricing/Hormozi-Value-Driven-Pricing-Model.md` + `13-Pricing/Hormozi-Pricing-Rules.md` + `13-Pricing/Hormozi-Pricing-Profit-Leverage.md` |
| "Specific tactics to lift profit immediately" / 28-day billing / processing fees / annual CPI / etc. | `/pricing-plays` | `13-Pricing/Hormozi-Instant-Profit-Pricing-Plays.md` |
| "How do I run a price test?" / operating loop / cadence / step-size | `/price-test` | `09-Lifetime-Value/Hormozi-Price-Testing-Method.md` |
| "How do I raise prices on existing customers?" / RAISE letter / rollout / handle objections | `/price-raise` | `11-Price-Raise/*` (full folder) |

### Canonical-home logic
- Strategic posture → `01-100M-Offers/Hormozi-Pricing-Power` (canonical).
- Pricing model taxonomy + measurement → `13-Pricing/Hormozi-Value-Driven-Pricing-Model` (canonical).
- Profit-leverage thesis → `13-Pricing/Hormozi-Pricing-Profit-Leverage` (canonical).
- Operating rules → `13-Pricing/Hormozi-Pricing-Rules` (canonical).
- Tactical plays → `13-Pricing/Hormozi-Instant-Profit-Pricing-Plays` (canonical).
- Operational test loop → `09-Lifetime-Value/Hormozi-Price-Testing-Method` (canonical).
- Existing-customer rollout → `11-Price-Raise/*` (canonical).

### Recommended pattern
**Router + 5 subskills** (`/pricing-posture`, `/pricing-model`, `/pricing-plays`, `/price-test`, `/price-raise`). A flat `/pricing` skill loading all 4 folders simultaneously will produce noisy context.

### Context warnings
- Without sub-routing, `/pricing` becomes a junk drawer.
- Pricing-Power (01) and Pricing-Profit-Leverage (13) are complementary, not redundant: one is *why* premium pricing works (mechanism); the other is *why* pricing dominates the profit equation (math). Both can coexist for posture-level questions.

---

## /price-raise

### Purpose
Roll out a price increase to existing customers without losing them.

### Use when
- "I want to raise prices on my current customer base."
- "Write me a price-raise letter."
- "What math do I need to run before raising?"
- "How do I handle objections during a price raise?"

### Do not use when
- Setting initial pricing for a new offer → `/pricing-posture` or `/offers`.
- Raising prices for new customers only (no existing-customer impact) → `/pricing-plays` or `/pricing-model`.

### Primary notes
- `Strategy-Models/11-Price-Raise/Hormozi-Price-Raise-Play.md`
- `Strategy-Models/11-Price-Raise/Hormozi-Price-Raise-Rules.md`
- `Strategy-Models/11-Price-Raise/Hormozi-Price-Test-Math.md`
- `Strategy-Models/11-Price-Raise/Hormozi-RAISE-Letter.md`

### Secondary notes
- `Strategy-Models/01-100M-Offers/Hormozi-Pricing-Power.md` — virtuous cycle posture.
- `Strategy-Models/01-100M-Offers/Hormozi-Value-Equation.md` — Invest section of RAISE letter applies this.

### Optional support notes
- `Strategy-Models/09-Lifetime-Value/Hormozi-Price-Testing-Method.md` — loop test before rolling out.

### Canonical-home logic
11-Price-Raise is canonical for existing-customer raises. Pricing posture stays in 01.

### Retrieval order
1. Price-Raise-Play (umbrella).
2. Price-Raise-Rules (operating constraints).
3. Price-Test-Math (run the math first).
4. RAISE-Letter (communication mechanism).

### Context warnings
- Do not load all 13 Pricing-Rules from 13-Pricing — those are different rules (general pricing) than 11-Price-Raise's 9 rules (rollout-specific).

---

## /retention

### Purpose
Reduce churn. Increase repeat purchase. Build a customer-journey discipline.

### Use when
- "Why are my customers leaving?"
- "How do I reduce churn?"
- "Build me an onboarding."
- "Save customers at cancellation."
- "What is my activation point?"
- "Run a customer survey."
- "Design a customer journey."

### Do not use when
- LTV-lifting levers other than churn (price, cost, frequency, cross-sell) → `/ltv`.
- Continuity offer architecture (recurring revenue mechanics) → `/money-models`.
- Branding / reputation building → `/branding`.

### Primary notes
- `Strategy-Models/14-Retention/Hormozi-Churn-Checklist.md`
- `Strategy-Models/14-Retention/Hormozi-Churn-Definition.md`
- `Strategy-Models/14-Retention/Hormozi-Churn-Economics.md`
- `Strategy-Models/14-Retention/Hormozi-Value-Per-Second.md`

### Secondary notes (the 9 lever notes — load by intent)
- `Strategy-Models/14-Retention/Hormozi-Activation-Points.md`
- `Strategy-Models/14-Retention/Hormozi-Customer-Onboarding.md`
- `Strategy-Models/14-Retention/Hormozi-Activation-Incentives.md`
- `Strategy-Models/14-Retention/Hormozi-Community-Linking.md`
- `Strategy-Models/14-Retention/Hormozi-Customer-Curation.md`
- `Strategy-Models/14-Retention/Hormozi-Annual-Payment-Options.md`
- `Strategy-Models/14-Retention/Hormozi-Cancellation-Saves.md`
- `Strategy-Models/14-Retention/Hormozi-Customer-Survey-ACA.md`
- `Strategy-Models/14-Retention/Hormozi-Customer-Journey-Milestones.md`

### Optional support notes
- `Strategy-Models/14-Retention/Hormozi-Common-Factors-Method.md` — meta problem-solving used to derive the checklist.
- `Strategy-Models/14-Retention/Hormozi-Five-Horsemen-Of-Retention.md` — gym-era predecessor framework.
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-CFA-Three-Levers.md` — LTV / churn math.
- `Strategy-Models/01-100M-Offers/Hormozi-Value-Equation.md` — price-value-churn relationship anchor.
- `Strategy-Models/06-Fast-Cash/Hormozi-Fast-Cash-Play.md` — cited as gym-launch activation-point case.
- `Strategy-Models/03-100M-Money-Models/Hormozi-Continuity-Offers.md` — recurring architecture context for annual-payment lever.
- `Strategy-Models/03-100M-Money-Models/Hormozi-Upsell-Offers.md` — save-with-upsell mechanism.

### Canonical-home logic
14-Retention is canonical for churn mechanics. LTV math canonical in 04. Pricing posture canonical in 01.

### Retrieval order
1. Churn-Definition (math) + Churn-Economics (why retention beats acquisition).
2. Churn-Checklist (umbrella, 9 levers).
3. Whichever lever is the user's question.
4. Value-Per-Second when overwhelm / less-is-more comes up.
5. Customer-Journey-Milestones for full-pipeline questions.
6. Five Horsemen + Common Factors Method only when user asks for meta-method or origin.

### Context warnings
- Avoid loading all 15 retention notes by default — context bloat. Route by lever intent.
- Customer-Journey-Milestones links to Marketing Machine (testimonial milestone) and Money Models (ascension milestone) — pull those only when user is doing cross-skill work.

---

## /ltv

### Purpose
Lift LTV / LTGP via the 8 Crazy Eight levers. Cost reduction, frequency, cross-sell, quantity / quality up, etc.

### Use when
- "How do I increase customer value?"
- "Reduce my fulfillment costs."
- "Get customers to buy more often."
- "Run a price test." (operational loop)
- LTV / LTGP math questions.

### Do not use when
- Pure churn reduction → `/retention`.
- Designing the offer sequence → `/money-models`.
- Strategic pricing posture → `/pricing-posture`.

### Primary notes
- `Strategy-Models/09-Lifetime-Value/Hormozi-Crazy-Eight.md`
- `Strategy-Models/09-Lifetime-Value/Hormozi-Cost-Reduction-Levers.md`
- `Strategy-Models/09-Lifetime-Value/Hormozi-Price-Testing-Method.md`

### Secondary notes
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-CFA-Three-Levers.md` — LTV / LTGP / CAC math.
- `Strategy-Models/03-100M-Money-Models/Hormozi-Upsell-Offers.md` — quantity / quality up mechanisms.
- `Strategy-Models/03-100M-Money-Models/Hormozi-Downsell-Offers.md` — quantity / quality down.
- `Strategy-Models/03-100M-Money-Models/Hormozi-Continuity-Offers.md` — frequency lever.

### Optional support notes
- `Strategy-Models/14-Retention/Hormozi-Churn-Checklist.md` — Crazy Eight Lever 3 (decrease churn) delegates here.
- `Strategy-Models/06-Fast-Cash/Hormozi-Fast-Cash-Play.md` + `Hormozi-Fast-Cash-Cadence.md` — Lever 3 follow-up sub-mechanic.
- `Strategy-Models/01-100M-Offers/Hormozi-Pricing-Power.md` — Lever 1 posture.

### Canonical-home logic
Crazy Eight canonical in 09. LTV math canonical in 04. Each lever's deeper mechanism lives in its respective canonical home (Money Models for upsell/downsell/continuity; Retention for churn; Fast Cash for follow-up).

### Retrieval order
1. Crazy Eight (umbrella, 8 levers).
2. Whichever lever is the user's question.
3. The lever's deeper canonical (e.g., Lever 3 → Retention or Fast Cash).
4. Cost-Reduction-Levers for Lever 2.
5. Price-Testing-Method for Lever 1 operational loop.

### Context warnings
- Crazy Eight delegates depth on most levers to other folders. Skill must follow the delegation, not duplicate.

---

## /branding

### Purpose
Build, measure, or pivot a brand. Pairing logic, authority dynamics, portfolio (brand bouquet).

### Use when
- "What is my brand pairing?"
- "How do I measure brand health?"
- "Build a brand from scratch."
- "Should I pivot the brand?"
- "What's the right brand portfolio?"
- Authority / level-of-recognition questions.

### Do not use when
- Avatar / ICP selection → `/avatar`.
- Producing brand assets (testimonials, UGC, ads) → `/marketing-machine`.
- Pricing the brand premium → `/pricing-posture`.

### Primary notes
- `Strategy-Models/05-Branding/Hormozi-Branding-Definition.md`
- `Strategy-Models/05-Branding/Hormozi-Brand-Measurement.md`
- `Strategy-Models/05-Branding/Hormozi-Brand-Economics.md`
- `Strategy-Models/05-Branding/Hormozi-Brand-Building-Steps.md`
- `Strategy-Models/05-Branding/Hormozi-Levels-Of-Authority.md`
- `Strategy-Models/05-Branding/Hormozi-Brand-Bouquet.md`

### Secondary notes
- `Strategy-Models/01-100M-Offers/Hormozi-Pricing-Power.md` — brand pairing transfers into premium pricing.
- `Strategy-Models/01-100M-Offers/Hormozi-Starving-Crowd.md` — GMEP avatar criteria overlap.

### Optional support notes
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-Avatar-Selection.md`.

### Canonical-home logic
05-Branding is canonical for branding-specific frameworks. Avatar is canonical in 04-Lost-Chapters; do not duplicate here. Pricing posture stays in 01.

### Retrieval order
1. Branding-Definition.
2. Brand-Measurement (R/I/D, polarization).
3. Brand-Economics (premium-pricing mechanism via pairing).
4. Brand-Building-Steps (4-step + GMEP).
5. Levels-Of-Authority (virtuous/vicious cycle).
6. Brand-Bouquet (portfolio / pivots / patience).

### Context warnings
- Do not pull avatar material into `/branding` by default — `/avatar` is separate.
- Brand asset production (testimonials, UGC) is `/marketing-machine`, not `/branding`.

---

## /hooks

### Purpose
Engineer hooks. Two-part anatomy, 8-format palette, 70-20-10 production process, 121-hook swipe library.

### Use when
- "Write me hooks."
- "Why are my hooks not working?"
- "What hook formats are there?"
- "Show me high-performing hook examples."
- Any opener / first 3-5 seconds / first sentence question.

### Do not use when
- Hook *for paid ads specifically*, mapped to awareness levels → `/ads` (which loads `08-GOATed-Ads/Hook-By-Awareness` as primary).
- Whole-ad construction (hook + meat + CTA) → `/ads`.

### Primary notes
- `Strategy-Models/07-Hooks/Hormozi-Hook-Definition.md`
- `Strategy-Models/07-Hooks/Hormozi-Hook-Types-Palette.md`
- `Strategy-Models/07-Hooks/Hormozi-Hook-70-20-10-Process.md`
- `Strategy-Models/07-Hooks/Hormozi-Hook-Library.md`

### Secondary notes
- `Strategy-Models/08-GOATed-Ads/Hormozi-Hook-By-Awareness.md` — load only when context is paid ads + awareness levels.

### Optional support notes
- `Strategy-Models/07-Hooks/00-Book-Home.md` — hub orientation.

### Canonical-home logic
07-Hooks is canonical for everywhere-hooks. 08-GOATed-Ads/Hook-By-Awareness is a paid-ads application that explicitly defers to 07.

### Retrieval order
1. Hook-Definition (anatomy).
2. Hook-Types-Palette (8 formats).
3. Hook-70-20-10-Process (production).
4. Hook-Library (swipe-file).
5. Hook-By-Awareness only on paid-ad signal.

### Context warnings
- Do not load 121-hook library by default — large. Load on direct request ("show me examples").
- `/hooks` and `/ads` overlap intentionally on Hook-By-Awareness. Route by primary context.

---

## /ads

### Purpose
Produce paid ads at scale. Hook × meat × CTA assembly. Awareness-level targeting.

### Use when
- "Make me ads."
- "Why do my ads stop scaling?"
- "What ad format should I use?"
- "Write the CTA."
- "How many ads should I produce per week?"
- Awareness continuum questions.

### Do not use when
- Pure hook engineering (not for paid ads) → `/hooks`.
- UGC / testimonial sourcing for ads → `/marketing-machine` (then back here for assembly).
- Lifecycle ads / before-during-after moments → `/marketing-machine` (Lifecycle-Ads is canonical there).

### Primary notes
- `Strategy-Models/08-GOATed-Ads/Hormozi-Ad-Assembly-Process.md`
- `Strategy-Models/08-GOATed-Ads/Hormozi-Ad-Awareness-Continuum.md`
- `Strategy-Models/08-GOATed-Ads/Hormozi-Hook-By-Awareness.md`
- `Strategy-Models/08-GOATed-Ads/Hormozi-Ad-Meat-Formats.md`
- `Strategy-Models/08-GOATed-Ads/Hormozi-Ad-CTA.md`

### Secondary notes
- `Strategy-Models/07-Hooks/Hormozi-Hook-Definition.md` — anatomy layer.
- `Strategy-Models/07-Hooks/Hormozi-Hook-Library.md` — swipe file as 70%-bucket starting point.
- `Strategy-Models/01-100M-Offers/Hormozi-Scarcity.md` — CTA enhancer.
- `Strategy-Models/01-100M-Offers/Hormozi-Urgency.md` — CTA enhancer.
- `Strategy-Models/01-100M-Offers/Hormozi-Bonuses.md` — CTA enhancer.
- `Strategy-Models/01-100M-Offers/Hormozi-Guarantees.md` — CTA enhancer.

### Optional support notes
- `Strategy-Models/12-Marketing-Machine/Hormozi-Marketing-Machine-System.md` — bottom-of-journey UGC sourcing for ads.
- `Strategy-Models/12-Marketing-Machine/Hormozi-Lifecycle-Ads.md` — before/during/after moments.
- `Strategy-Models/12-Marketing-Machine/Hormozi-Social-Media-Scrape.md` — organic ads → paid creative.

### Canonical-home logic
08-GOATed-Ads canonical for paid-ad assembly. Hooks (canonical) in 07. CTA enhancement levers in 01. Lifecycle ads in 12-Marketing-Machine.

### Retrieval order
1. Ad-Assembly-Process (umbrella, weekly cadence).
2. Ad-Awareness-Continuum (audience model).
3. Hook-By-Awareness (sourcing layer).
4. Ad-Meat-Formats (5 formats).
5. Ad-CTA (close).
6. Pull CTA enhancers from 01 only on direct match.
7. Pull 07-Hooks/Hook-Library on swipe-file request.

### Context warnings
- Do not duplicate canonical hook material from 07. Load 07 only when ad-specific awareness mapping isn't enough.
- Lifecycle ads belong to `/marketing-machine`, not `/ads`. Route accordingly.

---

## /marketing-machine

### Purpose
Build the system that produces customer-generated ad creative continuously. UGC, testimonials, support clips, event clips, community wins, awards, competitions.

### Use when
- "How do I get a steady flow of testimonial / UGC / customer-evidence ads?"
- "Build a lifecycle-ads system."
- "Run a testimonial competition."
- "Capture event content."
- "Scrape social media for organic winners."
- Founder-not-on-camera scaling questions.

### Do not use when
- Pure ad assembly / paid-ad construction → `/ads`.
- Pure brand strategy → `/branding`.
- Single-customer testimonial extraction (just the script) → load only `Hormozi-6-Point-Testimonial-Script.md`.

### Primary notes
- `Strategy-Models/12-Marketing-Machine/Hormozi-Marketing-Machine-System.md`
- `Strategy-Models/12-Marketing-Machine/Hormozi-Marketing-Machine-Cadence.md`

### Secondary notes (the 7 nodes — load by intent)
- `Strategy-Models/12-Marketing-Machine/Hormozi-Lifecycle-Ads.md`
- `Strategy-Models/12-Marketing-Machine/Hormozi-Social-Media-Scrape.md`
- `Strategy-Models/12-Marketing-Machine/Hormozi-Event-Capture-Playbook.md`
- `Strategy-Models/12-Marketing-Machine/Hormozi-Communications-Scrape.md`
- `Strategy-Models/12-Marketing-Machine/Hormozi-Bonus-And-Award-Mechanism.md`
- `Strategy-Models/12-Marketing-Machine/Hormozi-Testimonial-Competition.md`
- `Strategy-Models/12-Marketing-Machine/Hormozi-6-Point-Testimonial-Script.md`

### Optional support notes
- `Strategy-Models/07-Hooks/Hormozi-Hook-Definition.md` — first 3-5 sec of UGC ad.
- `Strategy-Models/08-GOATed-Ads/Hormozi-Ad-Assembly-Process.md` — assembly target.
- `Strategy-Models/01-100M-Offers/Hormozi-Bonuses.md` — bonus-unlock currency.

### Canonical-home logic
12-Marketing-Machine canonical for UGC sourcing system. Hooks canonical in 07. Ad assembly canonical in 08. Bonuses canonical in 01.

### Retrieval order
1. Marketing-Machine-System (umbrella + 7 nodes).
2. The node the user is asking about.
3. 6-Point-Testimonial-Script if extraction-script is needed.
4. Marketing-Machine-Cadence for operational rhythm.
5. Cross-skill loads (hooks, ad assembly) only when user is composing a full ad.

### Context warnings
- Do not collapse with `/branding` — different layer.
- Lifecycle-Ads is canonical here, not in `/ads`. `/ads` should *reference* but not duplicate.

---

## /lead-nurture

### Purpose
Convert opted-in leads into shows / closes. Optimize 30-day show rate. Distinct operational layer between advertising and sales.

### Use when
- "Why aren't leads showing up?"
- "How do I follow up faster?"
- "Build a reminder cadence."
- "Optimize show rate."
- "Train an SDR / sales team execution culture."
- BAMFAM / book-meeting-from-meeting questions.

### Do not use when
- Lead generation / acquisition mechanics → no canonical home (see `/lead-gen` deferred note).
- Sales close / objection handling on the call → see `/sales` (deferred).
- Long-term retention / churn → `/retention`.

### Primary notes
- `Strategy-Models/10-Lead-Nurture/Hormozi-Lead-Nurture-Four-Pillars.md`
- `Strategy-Models/10-Lead-Nurture/Hormozi-Lead-Nurture-Availability.md`
- `Strategy-Models/10-Lead-Nurture/Hormozi-Lead-Nurture-Speed.md`
- `Strategy-Models/10-Lead-Nurture/Hormozi-Lead-Nurture-Personalization.md`
- `Strategy-Models/10-Lead-Nurture/Hormozi-Lead-Nurture-Volume.md`

### Secondary notes
- `Strategy-Models/10-Lead-Nurture/Hormozi-BAMFAM.md` — standalone, reusable tactic.
- `Strategy-Models/10-Lead-Nurture/Hormozi-Lead-Nurture-Execution-Culture.md`

### Optional support notes
- `Strategy-Models/06-Fast-Cash/Hormozi-Fast-Cash-Play.md` — Lead Nurture is prerequisite for Fast Cash on warm lists.

### Canonical-home logic
10-Lead-Nurture is canonical for post-opt-in nurture. BAMFAM is canonical here even though it's reusable across sales contexts.

### Retrieval order
1. Four-Pillars (umbrella).
2. Whichever pillar matches user intent.
3. BAMFAM on direct request or any "next call booking" intent.
4. Execution-Culture on team / SDR / training questions.

### Context warnings
- 10-Lead-Nurture covers a specific, distinct layer. Do not dump into `/sales` or `/lead-gen`.

---

## /fast-cash

### Purpose
Generate immediate cash from warm audiences via limited, premium-priced, time-boxed offers. Quarterly cadence.

### Use when
- "I need cash this month."
- "Run a promo to existing customers."
- "Design a 7-day cash mechanism."
- "What's the right cadence for warm-list promos?"

### Do not use when
- Building the underlying offer architecture → `/offers`.
- Cold-traffic acquisition → `/ads` or (deferred) `/lead-gen`.
- Long-term retention / monetization → `/retention` or `/ltv`.

### Primary notes
- `Strategy-Models/06-Fast-Cash/Hormozi-Fast-Cash-Play.md`
- `Strategy-Models/06-Fast-Cash/Hormozi-10x-The-10-Percent-Rule.md`
- `Strategy-Models/06-Fast-Cash/Hormozi-Unscalable-Value-Levers.md`
- `Strategy-Models/06-Fast-Cash/Hormozi-Fast-Cash-Promo-Sequence.md`
- `Strategy-Models/06-Fast-Cash/Hormozi-Fast-Cash-Cadence.md`

### Secondary notes
- `Strategy-Models/01-100M-Offers/Hormozi-Scarcity.md`
- `Strategy-Models/01-100M-Offers/Hormozi-Urgency.md`
- `Strategy-Models/01-100M-Offers/Hormozi-Bonuses.md`
- `Strategy-Models/01-100M-Offers/Hormozi-Offer-Creation.md` — used as offer-body construction tool.
- `Strategy-Models/01-100M-Offers/Hormozi-Grand-Slam-Offer.md` — Fast Cash offers are GSO-shaped.

### Optional support notes
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-Promotion-Wrappers.md`

### Canonical-home logic
06-Fast-Cash canonical for the mechanism. Enhancement levers stay canonical in 01.

### Retrieval order
1. Fast-Cash-Play (umbrella).
2. 10x-The-10% (ratio rule).
3. Unscalable-Value-Levers (offer construction palette).
4. Fast-Cash-Promo-Sequence (Push-to-Consult / Push-to-Automated-Checkout).
5. Fast-Cash-Cadence (90-day rationale + 4Rs post-promo).

### Context warnings
- Easy to confuse with `/offers`. Distinguish: `/offers` builds the offer; `/fast-cash` is the mechanism that *deploys* a premium GSO to a warm list on a 7-day clock.

---

## /avatar

### Purpose
Pick or refine the target customer. Avatar selection, market validity, GMEP criteria, niching.

### Use when
- "Who should I target?"
- "Is my market viable?"
- "How do I niche down?"
- "Find my highest-value customer subset."
- "Survey existing customers to find the avatar."

### Do not use when
- Branding strategy → `/branding`.
- Lead nurture mechanics on already-opted-in leads → `/lead-nurture`.

### Primary notes
- `Strategy-Models/01-100M-Offers/Hormozi-Starving-Crowd.md`
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-Avatar-Selection.md`

### Secondary notes
- `Strategy-Models/05-Branding/Hormozi-Brand-Building-Steps.md` — GMEP overlaps Starving-Crowd's four indicators.

### Optional support notes
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-Value-Grid.md` — LTV per customer segment.

### Canonical-home logic
Two complementary canonicals: 01 for market viability (4 indicators); 04 for finding the highest-value subset within an existing customer base. Both are canonical; load both for full coverage.

### Retrieval order
1. Starving-Crowd (4 indicators, niche commitment).
2. Avatar-Selection (operational method to find avatar from existing customers).
3. Brand-Building-Steps GMEP only when branding context is involved.

### Context warnings
- Do not collapse with `/branding`. Avatar is the input to branding; branding is the application.

---

## /onboarding

### Purpose
Drive new customers to their activation point. First-30-day discipline.

### Use when
- "How do I onboard new customers?"
- "What's my activation point?"
- "Build an unlockable schedule."
- "Reduce early churn."
- "Why are new customers not sticking?"

### Do not use when
- Long-term retention beyond activation → `/retention`.
- Sales / closing on the call → `/sales` (deferred).
- Marketing onboarding (lead nurture) → `/lead-nurture`.

### Primary notes
- `Strategy-Models/14-Retention/Hormozi-Activation-Points.md`
- `Strategy-Models/14-Retention/Hormozi-Customer-Onboarding.md`
- `Strategy-Models/14-Retention/Hormozi-Activation-Incentives.md`

### Secondary notes
- `Strategy-Models/14-Retention/Hormozi-Value-Per-Second.md` — overwhelm = #1 churn cause.
- `Strategy-Models/14-Retention/Hormozi-Customer-Journey-Milestones.md` — activation is milestone #1.
- `Strategy-Models/06-Fast-Cash/Hormozi-Fast-Cash-Play.md` — gym-launch activation case.

### Optional support notes
- `Strategy-Models/14-Retention/Hormozi-Common-Factors-Method.md` — meta method to find activation points.

### Canonical-home logic
14-Retention Levers 1–3 are the canonical onboarding stack. `/onboarding` is a tightly-scoped subset of `/retention`.

### Retrieval order
1. Activation-Points (find the leading indicator).
2. Customer-Onboarding (drive customers there).
3. Activation-Incentives (unlockable rewards).
4. Value-Per-Second (overwhelm guardrail).

### Context warnings
- Do not load all 9 retention levers — `/onboarding` is bounded.
- Could be a subskill of `/retention` rather than standalone, depending on usage frequency.

---

## /promotion-architecture

### Purpose
Wrap an existing GSO in a premium / free / discount promotion. Friction levers. Discount display forms.

### Use when
- "Should I run a free promo?"
- "How do I price-discount without commoditizing?"
- "Premium vs. free vs. discount — which wrapper?"
- "What friction should I add to a free offer?"

### Do not use when
- Building the underlying offer → `/offers`.
- Naming the offer → `/offers` (Naming note).
- Quarterly cash mechanism → `/fast-cash`.

### Primary notes
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-Promotion-Wrappers.md`

### Secondary notes
- `Strategy-Models/01-100M-Offers/Hormozi-Naming.md`
- `Strategy-Models/01-100M-Offers/Hormozi-Grand-Slam-Offer.md`

### Optional support notes
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-Attraction-Free-Presentations.md`
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-Attraction-Freemium.md`
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-Attraction-Pick-Your-Price.md`

### Canonical-home logic
Promotion Wrappers canonical in 04. Specialized free/freemium/pick-your-price mechanics also canonical in 04.

### Retrieval order
1. Promotion-Wrappers (the three wrappers + friction logic).
2. Specialized variant on direct match.
3. Naming for execution.

### Context warnings
- Small skill. Could be a subskill of `/offers` instead of standalone.

---

## /team

### Purpose
Hire and manage. Specifically: hire as customer-acquisition; founder calendar discipline.

### Use when
- "How should I hire?"
- "Why is my team not producing?"
- "Maker vs. manager calendar."
- "Lead-getter hiring framework."
- Founder time-management questions.

### Do not use when
- Sales-team execution culture (specific to lead nurture) → `/lead-nurture`.
- General business operations / strategy.

### Primary notes
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-Lead-Getting-Employees.md`
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-Maker-vs-Manager.md`

### Secondary notes
- `Strategy-Models/10-Lead-Nurture/Hormozi-Lead-Nurture-Execution-Culture.md` — sales-team specific.

### Canonical-home logic
04-Lost-Chapters canonical for hiring + calendar. 10-Lead-Nurture canonical for sales-team execution culture (different scope).

### Retrieval order
1. Lead-Getting-Employees (Internal Core Four, 3Ds, Performance Diamond).
2. Maker-vs-Manager.
3. Lead-Nurture-Execution-Culture only when sales-team specific.

### Context warnings
- Small skill. Limited scope. Could remain standalone or fold into a broader `/operations` skill in future.

---

## /sales

### Purpose
Close deals on the live sales call. Objection handling. Closing mechanics. Anchored to the *Closing* playbook (`15-Closing/`).

### Use when
- "Why aren't we closing?"
- "Train my sales team to handle objections."
- "How do I respond to '[specific objection — too expensive / let me think about it / I need to talk to my spouse / I've been burned before / etc.]'?"
- "Build the close library for our sales script."
- "Diagnose why our close rate is X% and what to do about it."
- "What's the right way to deploy guarantees during the close?"
- BAMFAM / re-book questions (canonical home in `/lead-nurture`, but invoked from sales when a decision-maker is missing).

### Do not use when
- Building the offer being sold → `/offers`.
- Pre-call lead nurture (show rate, response speed, opt-in cadence) → `/lead-nurture`.
- Post-purchase cancellation save / vent-then-validate → `/retention` (the cancellation-saves note is canonical there).
- Setting initial pricing / pricing structure on a new offer → `/pricing-model` or `/pricing`.
- Existing-customer price raise rollout (RAISE letter) → `/price-raise`.
- Acquiring more leads in the first place → `/lead-gen` (deferred — see below).

### Primary notes
- `Strategy-Models/15-Closing/Hormozi-Closing-Definition.md` — foundation: 3-bucket maybe model + Power thesis + Blame Onion + ethics + STAR qualification.
- `Strategy-Models/15-Closing/Hormozi-Closing-Rules.md` — 28 operating rules.
- `Strategy-Models/15-Closing/Hormozi-All-Purpose-Closes.md` — 7 universal closes (80/20 library).
- Whichever blame-branch close library matches the user's named obstacle:
  - `Strategy-Models/15-Closing/Hormozi-Closing-Circumstances-Closes.md` — Time + Money (4 flavors).
  - `Strategy-Models/15-Closing/Hormozi-Closing-Other-People-Closes.md` — Decision-Makers + Bad-Experiences.
  - `Strategy-Models/15-Closing/Hormozi-Closing-Self-Closes.md` — Preferences + Rushed-Decisions + Guarantee Closes.

### Secondary notes
- `Strategy-Models/15-Closing/Hormozi-Closing-Training-System.md` — for "train the team" / "build a closing program" / drill cadence questions.
- `Strategy-Models/01-100M-Offers/Hormozi-Guarantees.md` — risk reversal underlying the Guarantee Closes section.
- `Strategy-Models/01-100M-Offers/Hormozi-Value-Equation.md` — translation rule for money objections ("value too low ≠ price too high").

### Optional support notes
- `Strategy-Models/10-Lead-Nurture/Hormozi-BAMFAM.md` — invoked when a close requires re-booking with a missing decision-maker.
- `Strategy-Models/14-Retention/Hormozi-Cancellation-Saves.md` — adjacent objection-handling pattern (vent-then-validate); load only when user is composing a save flow that resembles a close.
- `Strategy-Models/01-100M-Offers/Hormozi-Bonuses.md` — 1-on-1 vs. group bonus sequencing inside the close.
- `Strategy-Models/04-100M-Lost-Chapters/Hormozi-Offer-Stacking.md` — sales choreography across multiple offers within the same conversation.

### Canonical-home logic
15-Closing is canonical for live-call objection handling and closing mechanics. Guarantees / Value Equation / Bonuses canonical in `01-100M-Offers/`. BAMFAM canonical in `10-Lead-Nurture/`. Cancellation-Saves canonical in `14-Retention/`. /sales links out, never duplicates.

### Retrieval order
1. Closing-Definition (foundation lens — load first).
2. Closing-Rules (operator-character constraints — load second).
3. All-Purpose-Closes (7 universal closes — load whenever the obstacle is unclear or as the opening layer).
4. Whichever blame-branch close library matches the user's named obstacle.
5. Closing-Training-System if the user is asking about training the team or building a closing program (operator-side question, not script-deployment).
6. Cross-skill anchors (`/offers` Guarantees, `/lead-nurture` BAMFAM, `/retention` Cancellation-Saves) only when the conversation explicitly bridges into them.

### Context warnings
- Do not load all 4 close libraries by default. Branch-specific. Route by named obstacle.
- Do not load Training-System for tactical close questions — that's a different operating layer (operator running the org, not closer running the call).
- Do not pull `/lead-nurture` Lead-Nurture-Execution-Culture into `/sales` by default. They are adjacent (both about sales-team operations) but Execution-Culture is canonical in 10-Lead-Nurture and serves a different operating moment (cadence/dashboards/accountability, not on-call objection handling).
- Do not collapse `/sales` with `/offers`. /offers builds the thing being sold; /sales handles objections during the act of selling it. Operators conflate these constantly; the manifest does not.

---

## /lead-gen (DEFERRED — no canonical home)

### Purpose
Generate leads. Core Four channels. Lead magnet design.

### Status
**`$100M Leads` is not extracted in this vault.** Folder slot `02-` is reserved but not populated.

### Available adjacent material (does not cover Core Four / lead-magnet design directly)
- `Strategy-Models/08-GOATed-Ads/*` — paid-ad creative (one of Core Four).
- `Strategy-Models/12-Marketing-Machine/*` — UGC / warm-list creative.
- `Strategy-Models/06-Fast-Cash/*` — warm-list activation.

### Recommendation
**Do not build `/lead-gen` as a top-level skill yet.** Build `/ads`, `/fast-cash`, `/marketing-machine` as scoped substitutes, and surface the gap honestly. After `$100M Leads` is extracted, return and scaffold `/lead-gen` properly.

---

## Summary table

| Skill | Build wave | Pattern | Primary folder |
|---|---|---|---|
| `/offers` | 1 | single skill | `01-100M-Offers/` |
| `/pricing` | 1 | router + 5 subskills | `01`, `09`, `11`, `13` |
| `/retention` | 1 | single skill | `14-Retention/` |
| `/branding` | 1 | single skill | `05-Branding/` |
| `/hooks` | 1 | single skill | `07-Hooks/` |
| `/ads` | 1 | single skill | `08-GOATed-Ads/` |
| `/money-models` | 2 | single skill | `03-100M-Money-Models/` |
| `/ltv` | 2 | single skill | `09-Lifetime-Value/` |
| `/lead-nurture` | 2 | single skill | `10-Lead-Nurture/` |
| `/marketing-machine` | 2 | single skill | `12-Marketing-Machine/` |
| `/fast-cash` | 2 | single skill | `06-Fast-Cash/` |
| `/avatar` | 2 | single skill | `01` + `04` |
| `/onboarding` | 3 | could fold into `/retention` | `14-Retention/` |
| `/promotion-architecture` | 3 | could fold into `/offers` | `04-100M-Lost-Chapters/` |
| `/team` | 3 | small standalone | `04-100M-Lost-Chapters/` |
| `/sales` | 3 | single skill | `15-Closing/` |
| `/lead-gen` | DEFERRED | — | no canonical home |
