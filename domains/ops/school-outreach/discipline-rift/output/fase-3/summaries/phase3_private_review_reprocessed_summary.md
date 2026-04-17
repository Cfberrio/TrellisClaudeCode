# Phase 3 — Private School Review Reprocessed
**Date:** 2026-04-09
**Source:** SchoolDigger private school pages (ID prefix: 9999)
**Input:** phase3_full_review.csv (private_elementary rows only)

---

## Results

| Classification | Count |
|---|---|
| GOOD_MATCH | 3 |
| REJECTED | 60 |
| REVIEW (still) | 70 |
| **TOTAL processed** | **133** |

---

## GOOD_MATCH (3 schools)

| School | City | Students | White % |
|---|---|---|---|
| Faith Christian Academy | Orlando | 594 | 33.3% |
| Family Christian Academy Orlando | Orlando | 259 | 62.5% |
| Vanguard Preparatory Academy | Windermere | 395 | 47.6% |

---

## REJECTED (60 schools)

### Top rejection reasons

| Reason Category | Count |
|---|---|
| students < 200 only | 7 |
| White not highest (size OK) | 12 |
| students < 200 AND White not highest | 41 |

**Dominant non-White demographics in rejected schools:**
- Hispanic is top race: 20 schools
- African American is top race: 26 schools
- White highest but too small (< 200): 7 schools

---

## REVIEW — Still Unresolved (70 schools)

### Why still REVIEW

| Reason | Count |
|---|---|
| Found in SchoolDigger but racial breakdown not reported | 15 |
| Not found in SchoolDigger (no match by name + city) | 55 |

**Schools found but racial data missing (private schools that didn't report demographics):**
- Brush Arbor Christian School (Orlando) — 208 students enrolled
- Central Florida Christian Academy (Orlando) — 518 students enrolled
- Cvv Preschool And Academy (Orlando) — 225 students enrolled
- Glad Tidings Academy- East (Orlando) — 212 students enrolled
- Hampden Dubose Academy (Zellwood) — 278 students enrolled
- Ibn Seena Academy Inc. (Orlando) — 343 students enrolled
- Lake Highland Preparatory School (Orlando) — 2072 students enrolled
- Leaders Preparatory School (Orlando) — 279 students enrolled
- Pine Castle Christian Academy (Orlando) — 406 students enrolled
- Regency Christian Academy (Orlando) — 230 students enrolled
- The Conrad Academy (Orlando) — 405 students enrolled
- The First Academy (Orlando) — 1176 students enrolled
- Trinity Christian School (Apopka) — 457 students enrolled
- West Oaks Academy (Orlando) — 420 students enrolled
- Windermere Preparatory School (Windermere) — 1606 students enrolled

**Top schools not found in SchoolDigger:**
- Amazing Hope School Academy (Apopka)
- Apopka Christian Academy- West Campus (Apopka)
- Apopka Innovation  Technology Academy (Apopka)
- Bethany Christian Academy Inc (Orlando)
- Calvary Christian Academy And Preschool (Orlando)
- Cid Academy (Orlando)
- Circle Christian School Winter Garden (Winter Garden)
- Circle Christian School Winter Park (Winter Park)
- Core Prep (Oviedo)
- Covenant Journey Academy (Maitland)
- Crenshaw Academy (Gotha)
- Crenshaw School (Orlando)
- Destiny Academy (Davenport)
- Divine Knowledge Institute (Orlando)
- Divinely Ordered Prep School (Orlando)
- Domdidi Academy (Orlando)
- Edna Academy (Orlando)
- Elisha American Artistic Preparatory Academ (Winter Garden)
- Greater Vision Preparatory Academy (Ocoee)
- Heritage Preparatory School (Orlando)
- Hope Bridge Academy (Orlando)
- Hope Preparatory Academy (Orlando)
- Horace Grace Christian Academy (Orlando)
- I Can Do It Academy (Winter Garden)
- Illuminated Path International Academy (Orlando)
- Inspire Preparatory Academy (Orlando)
- Jmj Academy (Orlando)
- Kidz College Primary School (Orlando)
- L.J Preparatory Christian Academy Llc (Orlando)
- Learning Ladder Academy (Orlando)
- Light Christian Academy - South Campus (Gotha)
- Lighthouse City School Of Excellence (Orlando)
- Ls Academy (Orlando)
- Mighty Minds Christian Academy (Orlando)
- Miracle Grace Academy (Orlando)
- Monte Ararat School (Orlando)
- Murphy Christian Academy (Orlando)
- New Heights Preparatory Academy (Orlando)
- New World Dream Academy (Orlando)
- Ocala Christian Learning Academy Inc. (Apopka)
- Orlando Private School (Orlando)
- Pathways School (Orlando)
- Phoenix Freedom Academy (Orlando)
- Renaissance School Of The Arts (Orlando)
- Riverside Preparatory Academy (Orlando)
- S.H.I.P. Academy (Orlando)
- Sancta Familia Academy (Orlando)
- Saneaux Christian Academy (Orlando)
- Santiago Friends Academy (Orlando)
- Streamline Learning (Apopka)
- Teach Enrich Focus Academy (Orlando)
- The International School Of First Orlando (Ocoee)
- The Paramount School/Isa (Orlando)
- Thomas Leadership Academy (Eatonville)
- Transformation Academy Of The Arts (Orlando)

---

## Does This Fix the Prior Private-School Gap?

**Materially: yes, partially.**

- 78 of 133 private schools were matched in SchoolDigger.
- 60 were definitively classified (GOOD_MATCH or REJECTED) with hard data.
- 3 GOOD_MATCH schools were identified — these are now actionable.
- 55 schools remain unresolvable: not in SchoolDigger at all (very small, micro-schools, or too new).
- 15 schools are in SchoolDigger but did not report racial demographics — these remain REVIEW pending manual verification or alternative data source.

**The 55 not-found schools are predominantly micro-operations** (directors running small academies out of commercial spaces, churches, or homes). Most will not meet the ≥200 student threshold even if demographics were available.

**Recommended next step:** Use the 3 GOOD_MATCH private schools from this file alongside the 32 from phase3_full_good_match.csv (total 35 confirmed schools). The 15 still-REVIEW with large enrollment (especially Lake Highland Prep at 2,072, Windermere Prep at 1,606, The First Academy at 1,176) are worth manual demographic lookup.

---

## Output Files

| File | Rows | Path |
|---|---|---|
| phase3_private_review_reprocessed.csv | 133 | data/processed/phase3/results/ |
| phase3_private_review_good_match.csv | 3 | data/processed/phase3/results/ |
| phase3_private_review_rejected.csv | 60 | data/processed/phase3/results/ |
| phase3_private_review_still_review.csv | 70 | data/processed/phase3/results/ |
