# Phase 3 — Business Fit Summary v_lunch
**Date:** 2026-04-09
**Pipeline:** Discipline Rift School Outreach — Orange County, FL
**Version:** Lunch criteria (replaces racial breakdown)

---

## Business Criteria (v_lunch)

1. **students_count >= 200**
2. **Free/discounted lunch recipients <= 45%**

If either criterion fails → REJECTED.
If schooldigger_url is missing OR lunch data not reported → REVIEW.

Source: SchoolDigger (all existing SD URLs reused — no new SD matches performed).

---

## Results Overview

| Classification | Count | % of Total |
|---|---|---|
| GOOD_MATCH | 79 | 26.2% |
| REJECTED | 88 | 29.2% |
| REVIEW | 134 | 44.5% |
| **TOTAL** | **301** | **100%** |

---

## GOOD_MATCH: 79 Schools

| School Type | Count |
|---|---|
| public_elementary (OCPS) | 58 |
| public_k8 (OCPS) | 9 |
| charter_elementary | 12 |
| private_elementary | 0 |

All schools: students >= 200 AND free/discounted lunch <= 45%.

**Private schools in GOOD_MATCH:** (none)

---

## REJECTED: 88 Schools

| School Type | Count |
|---|---|
| public_elementary / public_k8 | 76 |
| charter_elementary | 12 |
| private_elementary | 0 |

**Common rejection reasons:** lunch > 45% (most common), students < 200, or both.

---

## REVIEW: 134 Schools (unresolved)

| Category | Count |
|---|---|
| No SchoolDigger URL (never matched) | 56 |
| SD URL exists but no lunch data reported | 78 |

**Large private schools in REVIEW (students >= 200, no lunch data reported to SchoolDigger):**
- Lake Highland Preparatory School (Orlando) — 2072 students
- Windermere Preparatory School (Windermere) — 1606 students
- The First Academy (Orlando) — 1176 students
- Orlando Christian Prep (Orlando) — 662 students
- Faith Christian Academy (Orlando) — 594 students
- Central Florida Christian Academy (Orlando) — 518 students
- Central Florida Preparatory School (Apopka) — 462 students
- Trinity Christian School (Apopka) — 457 students
- West Oaks Academy (Orlando) — 420 students
- Pine Castle Christian Academy (Orlando) — 406 students
- The Conrad Academy (Orlando) — 405 students
- Vanguard Preparatory Academy (Windermere) — 395 students
- Living Word Academy (Orlando) — 357 students
- Elite Preparatory Academy (Orlando) — 356 students
- Ibn Seena Academy Inc. (Orlando) — 343 students
- Growing Together Academy Inc. (Orlando) — 331 students
- South Orlando Christian Academy (Orlando) — 322 students
- Potter'S House Academy (Orlando) — 293 students
- Leaders Preparatory School (Orlando) — 279 students
- Hampden Dubose Academy (Zellwood) — 278 students

---

## Is This List Ready to Use?

**Yes — GOOD_MATCH list (79 schools) is ready for outreach.**
- All passed both criteria with verified SchoolDigger data.
- Public and charter schools: lunch data consistently reported.
- No private schools are in GOOD_MATCH — private schools do not report lunch data to SchoolDigger.

**REVIEW list (134 schools) requires manual verification.**
- 56 schools have no SchoolDigger URL — enrollment unknown.
- 78 private schools have SD profiles but do not report free/reduced lunch data. Manual lookup or direct contact needed.

**Recommended next action:**
1. Import `phase3_full_good_match_v_lunch.csv` (79 schools) into GHL as the primary outreach list.
2. For REVIEW private schools with large enrollment (Lake Highland Prep 2072, Windermere Prep 1606, The First Academy 1176, etc.) — manually verify socioeconomic fit via NCES or direct contact if they are priority targets.
3. Do not outreach REJECTED schools.

---

## Output Files

| File | Rows | Description |
|---|---|---|
| phase3_full_good_match_v_lunch.csv | 79 | Primary outreach list |
| phase3_full_rejected_v_lunch.csv | 88 | Confirmed disqualified |
| phase3_full_review_v_lunch.csv | 134 | Unresolved — do not outreach yet |
| phase3_full_enriched_v_lunch.csv | 301 | Full dataset (all 301 schools) |
