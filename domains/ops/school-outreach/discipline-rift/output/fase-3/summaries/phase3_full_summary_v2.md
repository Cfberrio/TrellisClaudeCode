# Phase 3 — Full Summary v2 (Post Private-Review Merge)
**Date:** 2026-04-09
**Pipeline:** Discipline Rift School Outreach — Orange County, FL

---

## Before vs. After

| Classification | Before | After | Change |
|---|---|---|---|
| GOOD_MATCH | 32 | 35 | +3 |
| REJECTED | 135 | 195 | +60 |
| REVIEW | 134 | 71 | -63 |
| **TOTAL** | **301** | **301** | 0 |

**63 private schools moved out of REVIEW** (3 → GOOD_MATCH, 60 → REJECTED).

---

## GOOD_MATCH: 35 Schools

| School Type | Count |
|---|---|
| public_elementary (OCPS) | 21 |
| public_k8 (OCPS) | 7 |
| charter_elementary | 4 |
| private_elementary | 3 |

**Private GOOD_MATCH schools added:**
- Family Christian Academy Orlando (Orlando) — 259 students, White 62.5%
- Faith Christian Academy (Orlando) — 594 students, White 33.3%
- Vanguard Preparatory Academy (Windermere) — 395 students, White 47.6%

---

## REJECTED: 195 Schools

| School Type | Count |
|---|---|
| public_elementary / public_k8 | 115 |
| charter_elementary | 20 |
| private_elementary | 60 |

---

## REVIEW: 71 Schools (still unresolved)

| Category | Count |
|---|---|
| Public school not in SchoolDigger (Luminary Elementary) | 1 |
| Private — found in SD but no racial data reported | 15 |
| Private — not found in SchoolDigger | 55 |

**Notable private schools still in REVIEW (large enrollment, no demographics):**
- Lake Highland Preparatory School (Orlando) — 2072 students
- Windermere Preparatory School (Windermere) — 1606 students
- The First Academy (Orlando) — 1176 students
- Central Florida Christian Academy (Orlando) — 518 students
- Trinity Christian School (Apopka) — 457 students
- West Oaks Academy (Orlando) — 420 students
- Pine Castle Christian Academy (Orlando) — 406 students
- The Conrad Academy (Orlando) — 405 students

---

## Business Criteria Applied

1. **students_count >= 200**
2. **White is highest racial group by percentage**

Source: SchoolDigger public district listing (public/charter) + SchoolDigger private school city pages.

---

## Is Phase 3 Ready to Use as the Business Shortlist?

**Yes — for the GOOD_MATCH list (35 schools).**

- All 35 schools passed both criteria with verified data.
- Public and charter schools were matched against the Orange County district listing (reliable, district-sourced).
- Private schools were matched against SchoolDigger private pages (city-level search, name-verified).
- No invented or assumed data.

**REVIEW list (71 schools) should NOT be treated as qualified leads yet.**
- 15 large private schools (including Lake Highland Prep, Windermere Prep, The First Academy) have confirmed enrollment but no demographic breakdown reported to SchoolDigger. These are candidates for manual lookup.
- 55 micro-schools were not found in any public database — most are unlikely to meet the ≥200 threshold.
- 1 public school (Luminary Elementary) is too new to have SchoolDigger data.

**Recommended next action:**
1. Import `phase3_full_good_match.csv` (35 schools) into GHL as the primary outreach list.
2. Optionally: manually look up demographics for the 15 large private schools in REVIEW — if confirmed, they move to GOOD_MATCH and expand the list by up to 15 more.
3. Do not pursue the 55 not-found private schools until enrollment can be confirmed via direct contact.

---

## Output Files

| File | Rows | Description |
|---|---|---|
| phase3_full_good_match.csv | 35 | Primary outreach list |
| phase3_full_rejected.csv | 195 | Confirmed disqualified |
| phase3_full_review.csv | 71 | Unresolved — do not outreach yet |
| phase3_full_enriched.csv | 301 | Full dataset (all 301 schools) |
