# Phase 3 — Business Fit Summary
**Date:** 2026-04-08
**Pipeline:** Discipline Rift School Outreach — Orange County, FL
**Source:** SchoolDigger (Orange County district ID: 01440)

---

## Results Overview

| Classification | Count | % of Total |
|---|---|---|
| GOOD_MATCH | 32 | 10.6% |
| REJECTED | 135 | 44.9% |
| REVIEW | 134 | 44.5% |
| **TOTAL** | **301** | **100%** |

---

## Business Criteria Applied

1. **students_count >= 200** — school must have at least 200 enrolled students
2. **White is highest racial group** — White must be the top racial group by percentage

Both conditions must be true for GOOD_MATCH. Either failure = REJECTED.

---

## GOOD_MATCH: 32 Schools

| School Type | Count |
|---|---|
| public_elementary (OCPS) | 21 |
| public_k8 (OCPS) | 7 |
| charter_elementary | 4 |

All 32 confirmed: students >= 200, White is highest racial group.

**Charter schools included:**
- Cornerstone Academy Charter (1,094 students, 46.3% White)
- Hope Charter (417 students, 54.0% White)
- Innovation Montessori Ocoee (919 students, 38.8% White)
- Oakland Avenue Charter (519 students, 64.0% White)

---

## REJECTED: 135 Schools

### By School Type

| School Type | Count |
|---|---|
| public_elementary (OCPS) | 112 |
| public_k8 (OCPS) | 3 |
| charter_elementary | 20 |

### By Rejection Reason

| Rejection Category | Approx. Count |
|---|---|
| White is not highest racial group | ~116 |
| students < 200 only | ~9 |
| Both: non-White top race AND < 200 students | ~8 |
| Asian is top race (not White) | 2 |

**Notable dual-failure cases (< 200 students AND non-White top race):**
- Washington Shores Primary (82 students)
- Lucious Nixon (74 students)
- Pinecrest Creek (119 students)
- Princeton House (117 students)
- Aspire (100 students)
- Lake Eola (190 students)
- Passport (181 students)
- UCP Downtown (188 students)

**Asian as top race:**
- Orlando Science Charter K-8 (Asian 28.6%)
- Orlando Science Elementary Charter (Asian 34.4%)

---

## REVIEW: 134 Schools

| Category | Count |
|---|---|
| Private schools (not in SchoolDigger public DB) | 133 |
| Not found in SchoolDigger (Luminary Elementary) | 1 |

Private schools require manual outreach verification — enrollment and demographic data not available via public district sources.

**Luminary Elementary:** Listed in FLDOE Charter data but not found in the Orange County SchoolDigger district listing as of 2026-04-08. May be a new or recently added school. Recommend direct verification.

---

## Output Files

| File | Rows | Path |
|---|---|---|
| `phase3_full_good_match.csv` | 32 | `data/processed/phase3/results/` |
| `phase3_full_rejected.csv` | 135 | `data/processed/phase3/results/` |
| `phase3_full_review.csv` | 134 | `data/processed/phase3/results/` |
| `phase3_full_enriched.csv` | 301 | `data/processed/phase3/results/` |

---

## Next Steps

1. **Outreach list:** Use `phase3_full_good_match.csv` (32 schools) as the primary outreach list. All have verified grades, valid status, and confirmed business fit.
2. **Private school review:** Decide whether to pursue any schools from `phase3_full_review.csv`. If yes, prioritize by known size — enrollment data requires direct contact or a separate source.
3. **Email gaps:** Multiple OCPS schools use district email pattern (`schoolname_es@ocps.net`) — confirm deliverability before sending. Schools without email listed need direct phone contact.
4. **CRM import:** `phase3_full_good_match.csv` is ready for GHL import. Map `school_name`, `official_website`, `phone`, `email`, `address`, `city` to contact fields. Set pipeline stage to `Outreach — Not Contacted`.
