# DR School Outreach — Phase 1 Summary
**Date:** 2026-04-08  
**Pipeline:** Official rebuild (OCPS + FLDOE Charter + FLDOE Private)

---

## Output Files

| File | Count | Notes |
|---|---|---|
| `2026-04-08_dr_school_outreach_phase1_discovery.csv` | 329 schools | All confirmed county_fit + grade_fit + school_type_fit |
| `2026-04-08_dr_school_outreach_rejected.csv` | 160 schools | Excluded from discovery — grade range outside K-5 |

---

## Confirmed Schools by Source

| Source | Type | Count |
|---|---|---|
| OCPS official directory | Public elementary (K-5) | 134 |
| OCPS official directory | Public K-8 | 10 |
| FLDOE Charter School Portal (Orange County) | Charter elementary/K-8 | 24 |
| FLDOE Private School Directory (Orange County) | Private elementary | 161 |
| **Total** | | **329** |

---

## Filter Logic Applied

All 329 schools passed three independent checks:

- **county_fit:** Orange County, FL (all sourced from Orange County official directories)
- **grade_fit:** Serves at least one grade in K–5 range (confirmed from official grade level data)
- **school_type_fit:** Public elementary, public K-8, charter elementary, or private elementary

---

## Data Quality Notes

- **OCPS public schools:** Grade ranges (K-5 or K-8) confirmed by OCPS directory classification. Addresses, phones, and emails not available from the list page — require individual school site visit or direct contact.
- **Charter schools:** Full contact data (address, phone, director email) from FLDOE Charter Portal. No official website URLs in source — need Phase 2 lookup.
- **Private schools:** Contact data from FLDOE Private School Annual Survey (self-reported). Grade levels are self-reported — some may need Phase 2 confirmation. Website URLs not in source.

---

## Rejected Schools

160 schools excluded:
- **144** FLDOE private schools with grade ranges outside K-5 (e.g., PK-PK, 6-12, 9-12, PK only)
- **16** FLDOE charter schools with grade ranges outside K-5 (e.g., 6-12, 9-12, 7-12, 11-12)

All rejected schools preserved in `2026-04-08_dr_school_outreach_rejected.csv` with rejection reasons.

---

## Phase 2 — Next Steps

Phase 2 (website verification) should confirm for each school:
1. Official website URL
2. Grade range confirmation from school's own site
3. Public / private / charter classification
4. After-school program presence (competition check)
5. Contact name and email (director/principal) — expect most not published; mark `email_source: to_call`

Priority order for Phase 2:
- Charter schools (24) — contact data available, website lookup needed
- Private schools (161) — website lookup needed, grade confirmation recommended
- OCPS public schools (144) — websites known via OCPS subdomain; verification is lower priority

**Recommended Apify task:** crawl charter and private school websites to extract grades, contact info, and after-school program signals.
