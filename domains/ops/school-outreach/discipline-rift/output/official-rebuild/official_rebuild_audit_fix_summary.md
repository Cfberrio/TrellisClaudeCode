# DR School Outreach — Official Rebuild Audit & Fix Summary
**Date:** 2026-04-08  
**Scope:** Audit and repair of three working CSVs. Archive structure untouched.

---

## Files Repaired

| File | Pre-repair rows | Post-repair rows | Schema fixed |
|---|---|---|---|
| `data/processed/official/master_official_universe.csv` | 329 | 329 | Yes |
| `data/processed/verification/unresolved_website_verification.csv` | 185 | 182 | Yes |
| `data/processed/verification/validated_schools_for_schooldigger.csv` | 144 | 301 | Yes |

---

## Issues Found and Fixed

### 1. All statuses were "confirmed" — not a valid status

**Before:** All 329 rows had `verification_status = confirmed`.  
**After:** Statuses distributed per new rules:

| Status | Count | Meaning |
|---|---|---|
| `VALID` | 301 | Passes all three filters; ready for SchoolDigger enrichment |
| `REVIEW` | 25 | Passes grade/county filter but entity type is ambiguous or grade scope is very narrow |
| `INVALID_SCHOOL_TYPE` | 3 | Not a school entity — excluded from outreach pipeline |

---

### 2. Private school universe was overinclusive — 28 rows corrected

**INVALID_SCHOOL_TYPE (3 private schools removed from active pipeline):**

| School | Reason |
|---|---|
| Huntington Learning Center | Franchised tutoring center — not a school entity |
| Empowerment Counseling And Educational Cent | Counseling center — not a standard school |
| TTS Mentoring & Development Services LLC | Mentoring/services org — not a school entity |

**REVIEW (25 private schools flagged — not removed, pending human decision):**

- **18 PK-K or K-K only** — technically qualifies (K is in-scope) but serves no grades 1–5. Limited after-school fit for DR program. Requires manual confirm before outreach.
  - All Saints School, Baldwin Oaks Academy, Big Stars Learning Center, Blue Jay Academy 4 Kidz, Early Education Station Preschool, Firm Foundation, Growing Minds Montessori School, Hand 'N Hand Child Enrichment Center, Kids R Kids Learning Academy, Little People Learning Center, Maitland Community Preschool, Ocoee Oaks School, Royalty Harvest Academy, Spring Of Life Early Learning Center, Storybook School Conway LLC, Storybook School LLC, The Goddard School Winter Garden, Top Spot Academy

- **7 ambiguous entities** — serve K-12 grades but entity type unclear from name alone:
  - Academy For Autism (special needs facility)
  - Bridge To Independence Inc. (special needs org)
  - Conductive Ed Ctr Of Orlando Inc. (special ed center)
  - E. H. Mott Learning Center (learning center, possibly tutoring)
  - Exclusive Hoops Basketball Academy LLC (sports-focused academy)
  - Homelife Academy (possible homeschool co-op)
  - New Wings Educational Services LLC (educational services org)

---

### 3. Schema inconsistency — all three files now share canonical schema

**Before:** Each file had a different column order and missing fields.  
**After:** All three files use the canonical 16-column schema:
`school_name, school_type, source_system, source_url, official_website, phone, email, address, city, county, grades_raw, county_fit, grade_fit, school_type_fit, verification_status, notes`

---

### 4. OCPS email enrichment

**Source:** OCPS official "School Email Addresses" page (`ocps.net/school-email-addresses`) — 257 generic school emails published for community use.

| Segment | With email | Total | Coverage |
|---|---|---|---|
| OCPS public elementary | 133 | 134 | 99% |
| OCPS K-8 | 10 | 10 | 100% |
| Charter (OCPS-affiliated) | 15 | 24 | 63% |
| **Total enriched** | **143** | **144** | **99%** |

**1 school not found in OCPS directory:** Dommerich Elementary — email left blank, to be sourced via school website in Phase 2.

Charter schools already had director-level emails from the FLDOE Charter Portal. The OCPS email enrichment added the generic school inbox (@ocps.net) for the 15 OCPS-affiliated charters where that email was available.

---

### 5. validated_schools_for_schooldigger.csv rebuilt with correct filter

**Before:** 144 rows (OCPS public schools only, all with confirmed-but-wrong status).  
**After:** 301 rows — all rows where `county_fit=YES`, `grade_fit=YES`, `school_type_fit=YES`, `verification_status=VALID`.

Breakdown:
- Public elementary: 134
- Public K-8: 10
- Charter elementary: 24
- Private elementary (confirmed): 133

---

### 6. unresolved_website_verification.csv — Apify still needed

182 schools have no confirmed website URL and remain in the active pipeline:

| Segment | Status | Count |
|---|---|---|
| Charter elementary | VALID | 24 |
| Private elementary | VALID | 133 |
| Private elementary | REVIEW | 25 |
| **Total** | | **182** |

**Apify website lookup batch files remain valid:**
- `prompts/2026-04-08_apify_batch_charter_website_lookup.json` — 24 charter schools
- `prompts/2026-04-08_apify_batch_private_website_lookup.json` — 161 private schools (133 VALID + 25 REVIEW + 3 now INVALID — filter INVALID rows before running)

> Action before running Apify: remove the 3 INVALID_SCHOOL_TYPE rows from the private batch file (`Huntington Learning Center`, `Empowerment Counseling And Educational Cent`, `TTS Mentoring & Development Services LLC`).

---

## Next Step

Phase 2 (website verification) is unblocked for all 301 VALID schools. Priority:
1. Run Apify batch on 24 charter schools → find official website URLs
2. Run Apify batch on 133 VALID private schools → find website URLs + confirm grades
3. Manual review of 25 REVIEW schools before including in outreach
4. SchoolDigger enrichment (enrollment + contact signals) on all 301 VALID rows via `validated_schools_for_schooldigger.csv`
