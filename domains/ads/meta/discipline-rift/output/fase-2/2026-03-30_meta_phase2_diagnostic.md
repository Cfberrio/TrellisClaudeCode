# Meta Ads Phase 2 Diagnostic — Discipline Rift
**Batch:** 20260330_105907
**Period:** 2026-02-28 to 2026-03-29
**Generated:** 2026-03-30

---

## A. Executive Read

This is a small local account at its earliest observable stage: one paused campaign, one ad set, one ad, $110 in total spend over ~29 days. The performance data is directional, not conclusive — volume is too low to draw strong creative or audience conclusions.

The single most concrete and actionable finding is a severe placement cost imbalance: 81.8% of spend went to Instagram feed at a CPM of $162, while Facebook feed delivered at $34 CPM with comparable click engagement. That gap is not marginal — it is structural, and it means the account is paying a significant premium for placements that Meta's auto-placement system chose without explicit budget guardrails.

Secondary risks that need resolution before any relaunch: geo targeting is not visible in the extracted data (critical for a local Orlando brand), LPV signal has not been confirmed from this data set, and there is zero creative diversity. The campaign is currently paused. There is no basis for scaling or deeper optimization decisions yet. The right posture here is: resolve setup, validate tracking, then relaunch with basic controls in place.

---

## B. Campaign Setup Read

| Field | Value |
|---|---|
| Campaign name | DR SPRING 2 |
| Status | **PAUSED** |
| Objective | OUTCOME_TRAFFIC |
| Buying type | AUCTION |
| Special ad categories | None |

**Objective read:** OUTCOME_TRAFFIC is a reasonable starting point if the goal is driving qualified parent traffic to a landing page. It signals top-of-funnel intent, which is appropriate for a local brand without an established pixel history.

**Status read:** Campaign is currently paused. All spend occurred within the Feb 28 – Mar 29 window. The pause could reflect a budget cap hit, a manual pause, or a scheduled end — the data doesn't reveal which. Before relaunching, this should be confirmed intentionally, not assumed.

**Coherence with business:** OUTCOME_TRAFFIC with a landing page view optimization goal is a coherent pairing for DR at this stage — provided geo and tracking are confirmed. The objective itself is not the problem.

---

## C. Ad Set Setup Read

| Field | Value |
|---|---|
| Ad set name | New Traffic Ad Set |
| Status | ACTIVE |
| Optimization goal | LANDING_PAGE_VIEWS |
| Billing event | IMPRESSIONS |
| Daily budget | Not visible in extracted data |
| Lifetime budget | Not visible in extracted data |
| Custom audience seed | DR HISTORIC |
| Advantage Audience | ON |
| Age targeting | 18–65 (age_range preference [28–40] noted) |
| Brand safety | RELAXED (Facebook + AN) |
| Geo | **NOT VISIBLE in extracted data** |

**Optimization goal:** LANDING_PAGE_VIEWS with IMPRESSIONS billing is a standard, appropriate pairing for a traffic campaign. No issue with this choice — provided the LPV signal is actually firing (see Section F).

**Budget:** Not visible in the objects CSV. This is a data gap — cannot confirm whether a daily or lifetime budget was applied, or at which level. Budget logic cannot be evaluated from available data.

**Targeting analysis:**
- **Advantage Audience ON**: Meta can expand delivery beyond the DR HISTORIC custom audience seed. For a local Orlando brand, this creates a real geo risk if no location constraint is applied at the ad set level. Advantage Audience expansion is designed for broad targeting — without a geo filter, delivery could extend well beyond the intended market.
- **Age 18–65 with [28–40] preference**: The hard cap is 18–65. The age_range [28–40] appears to be an optimization preference within that range, not a hard restriction. Parents of kids 6–12 can reasonably fall in this range, but the hard cap allows delivery outside it.
- **DR HISTORIC seed**: Using a historical custom audience as a seed is a reasonable starting point for a small account — it signals to Meta's algorithm who to look for. However, with Advantage Audience ON, this audience is a starting signal, not a hard constraint.
- **Geo not visible**: This is the highest-risk setup issue in the account. DR is a local Orlando business. If no geo filter is active, the budget may be reaching parents outside any serviceable market. This cannot be confirmed from the CSV data — it must be verified directly in Ads Manager.

**Setup verdict:** Directionally reasonable objective and optimization pairing. The targeting setup has a material risk in geo visibility and Advantage Audience expansion behavior that must be validated before drawing any audience-level conclusions.

---

## D. Placement Read

| Platform | Position | Spend | % of Total | Impressions | Reach | Clicks | CTR | CPM | CPC |
|---|---|---|---|---|---|---|---|---|---|
| Instagram | feed | $90.18 | **81.8%** | 556 | 185 | 7 | 1.26% | **$162.19** | $12.88 |
| Instagram | stories | $11.01 | 10.0% | 330 | 154 | 2 | 0.61% | $33.36 | $5.51 |
| Instagram | reels | $5.21 | 4.7% | 140 | 68 | 1 | 0.71% | $37.21 | $5.21 |
| Facebook | feed | $3.24 | 2.9% | 95 | 53 | 1 | 1.05% | $34.11 | $3.24 |
| Others (6 placements) | — | $0.65 | 0.6% | ~32 | ~20 | 0 | — | varies | — |

**Key observation — IG feed cost anomaly:**
Instagram feed consumed 81.8% of total spend at a CPM of $162.19. Every other placement delivered at CPMs between $20 and $45. The gap is ~4.75x between IG feed and the next most expensive placement (Facebook instream at $45, though with negligible spend).

Facebook feed delivered comparable CTR (1.05% vs. 1.26% for IG feed) at $34 CPM and $3.24 CPC — vs. $162 CPM and $12.88 CPC on IG feed. The efficiency difference is substantial.

**Interpretation:** Meta's auto-placement algorithm routed the majority of budget to Instagram feed — likely driven by the custom audience seed and Advantage Audience behavior favoring IG inventory. The result is that the account spent $90 to reach 185 unique people on IG feed, when FB feed reached 53 unique people for $3.24 with similar engagement signal.

**Placement verdict:**
- IG feed: **dominant and expensive** — signal insufficient to declare it a clear winner; CPM is directionally high for a small local account at this spend level.
- FB feed: **directionally more efficient** — too low volume to confirm, but the cost gap warrants attention.
- IG stories / reels: **secondary placements with limited signal** — CPMs are in a reasonable range, but click volume is minimal.
- Audience Network and others: **negligible spend, no return** — not a priority.

Do not declare IG feed as "waste" without more volume — but the current cost concentration without placement controls is a setup risk worth addressing.

---

## E. Creative Signal Read

**Single ad: "DR SPRING"**
No creative variants. No A/B test. No format diversity.

Account-level CTR: 0.95%
Click volume: 11 clicks over 29 days

**What this data does and does not tell us:**
- With 1 ad and 11 total clicks, there is no statistically meaningful creative signal. CTR is directional only.
- The 0.95% overall CTR is likely inflated by the DR HISTORIC warm custom audience — this is not evidence of cold creative performance.
- There is no basis for evaluating creative quality, message-market fit, or format preference from a single ad at this spend level.
- The account cannot learn anything about creative performance until there are multiple creatives running simultaneously.

**Creative testing verdict:** Not ready. Running creative tests before resolving geo, tracking, and placement controls would produce noise, not insight. The first move is not more creatives — it's validating the signal environment they'd run in.

---

## F. What the Data Does NOT Tell Us Yet

- **Geo of actual delivery**: No geo breakdown in the batch. Cannot confirm impressions landed in Orlando.
- **LPV confirmation**: Optimization goal is LPV, but no LPV metric appears in the insights CSV. Cannot confirm whether the LPV signal is firing and populating in Ads Manager.
- **Post-click behavior**: No data on bounce rate, time on page, form submissions, or downstream conversion actions.
- **Lead quality**: No evidence of lead volume, lead source, or quality from this data.
- **CAC or revenue**: Not available.
- **Whether the 260 unique people reached are the right 260 people**: Cannot confirm geo accuracy from available data.

---

## G. Priority Actions

**1. Validate geo targeting in Ads Manager — highest priority.**
The objects CSV shows no geo filter on the ad set. For DR (local Orlando), this is the most consequential setup risk in the account. Open Ads Manager, confirm a geo filter is applied (Orlando / specific zip codes or radius), and if it's missing, add it before any relaunch. If Advantage Audience is ON without a geo constraint, the algorithm can and likely will serve outside the target market.

**2. Validate LPV signal — required before any optimization conclusions.**
Optimization goal is LANDING_PAGE_VIEWS, but no LPV data appears in the extracted insights. In Ads Manager, confirm: (a) the base pixel PageView event fires correctly when someone lands on the page, and (b) Landing Page Views are populating in campaign reporting when traffic exists. If LPV isn't reporting, the campaign is optimizing blind. This is not necessarily a broken pixel — it may be a reporting gap — but it must be confirmed before LPV-based conclusions are drawn.

**3. Landing page audit — required before relaunching.**
Before spending more budget on this campaign, verify the destination page on mobile:
- Does it load fully and quickly on mobile?
- Above-the-fold: is the sport named clearly? Is it obvious this is an after-school, on-campus program for kids?
- Is the Orlando / local relevance visible early (not buried)?
- Is the season / program structure framed clearly (not vague)?
- Is there a clear CTA visible without scrolling?
- Does the ad message match what the landing page says?
A post-click clarity gap would invalidate any interpretation of CTR or LPV performance.

**4. Add placement controls or budget constraints.**
IG feed consumed 82% of spend at a CPM 4-5x higher than FB feed, with comparable engagement signal. For the next run, either: (a) test with explicit placement inclusion of FB feed and IG feed separately at equal budget to confirm the efficiency gap, or (b) exclude IG feed temporarily to validate performance without the premium CPM. Do not continue full auto-placement at this budget level without this knowledge.

**5. Prepare 2–3 creative variants before relaunching.**
Once geo, LPV, and landing page are confirmed, the account needs at least 2–3 ads to generate any meaningful creative learning. Each variant should anchor to one of DR's 3 core deliverables: on-campus convenience, beginner-friendly structure, or trained coaches + season clarity. Keep format simple first — static or short-form video matched to feed placement.

---

## H. Next Test Logic

**Prerequisite conditions before any meaningful test:**
1. Geo confirmed in Ads Manager (Orlando filter verified)
2. LPV signal validated (PageView fires, LPV populates in reporting)
3. Landing page audited on mobile (clarity, CTA, message match confirmed)

**A landing page audit is a required condition before stronger testing decisions are made.** If the landing page doesn't deliver post-click clarity, any improvement in CTR or LPV volume is not actionable — it just moves the bottleneck downstream.

**First test that makes sense after prerequisites are resolved:**
Placement-controlled run: separate FB feed vs. IG feed with equal budget allocation (~$50–$75 each), same ad, same targeting. Goal: confirm whether the CPM and CPC efficiency gap observed in auto-placement holds up when forced independently. This test requires minimal setup change and answers the most concrete question the current data raises.

**What does NOT make sense to test yet:**
- Creative A/B testing (no confirmed signal environment)
- Audience expansion or lookalike testing (geo not confirmed, LPV not validated)
- Retargeting or warm audience layering (too early; no confirmed top-of-funnel volume)
- Budget scaling (not until geo, tracking, and placement efficiency are understood)

---

## I. Final Call

The primary focus for this account is **setup + tracking**, in that order. The campaign ran on auto-placement without visible geo constraints, and the LPV optimization signal hasn't been confirmed from the available data. Spending more budget before those two conditions are resolved will produce more noise, not more signal.

Secondary focus is **placement control** — the cost concentration in IG feed at $162 CPM is the most concrete structural issue visible in the data and the easiest to address in the next run.

Creative and audience work come after setup and tracking are confirmed. Not before.
