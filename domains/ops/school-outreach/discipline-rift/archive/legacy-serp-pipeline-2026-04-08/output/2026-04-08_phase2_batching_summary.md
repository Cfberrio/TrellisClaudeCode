# Phase 2 Batching Summary — 2026-04-08

## Counts
| Metric | Count |
|---|---|
| High-confidence candidate rows (input) | 107 |
| After school-level deduplication | 78 |
| Excluded sub-pages / duplicates | 5 |
| **Clean school start URLs (batched)** | **71** |
| **Flagged / manual review** | **7** |
| Batches created | 3 × 25 rows |

---

## Batch Files
| File | Rows | Status |
|---|---|---|
| `phase2_batch_01.csv` | 25 | Ready for Phase 2 |
| `phase2_batch_02.csv` | 25 | Ready for Phase 2 |
| `phase2_batch_03.csv` | 21 | Ready for Phase 2 |
| `phase2_start_urls.csv` | 78 | Full list incl. flagged |

---

## Deduplication Logic
- One URL per school (grouped by domain host).
- Preferred URL: shallowest path depth (homepage over sub-pages).
- Explicit excludes: OCPS calendar page, duplicate Orlando Gifted Academy entry (kept official OCPS subdomain), The First Academy high school page, financial aid page.
- School names: derived from page title; overrides applied for ~12 hosts where title was generic or a sub-page label (e.g., "Contact Us", "Lower School", "Admissions").

---

## Flagged Domains — Do Not Include in Automatic Phase 2
These 7 rows are in `phase2_start_urls.csv` with `batch_id = manual_review`. Resolve before or after Phase 2 runs:

| School / Site | Host | Reason |
|---|---|---|
| International Montessori Academy Schools: USA | `intmontessori.com` | national_chain:verify_orlando_location |
| ORANGE COUNTY PREPARATORY ACADEMY CHARTER | `mahadevmaitri.org` | directory_page:not_official_school_site |
| Orlando Christian Elementary School,Orange County FL | `learn4good.com` | directory_site:missed_in_phase1_rejection |
| Osceola Christian Preparatory School | `christianprepschools.com` | wrong_county:osceola_christian_preparatory |
| Oxford Preparatory Academy | `opaschools.org` | verify_location:oxford_prep_fl_unconfirmed |
| Port Orange, FL | `gardenfaithpreschool.com` | wrong_county:port_orange_volusia |
| Windermere Preparatory School | `nordangliaeducation.com` | parent_company_site:windermere_prep_subpage_only |

### Resolution guidance
- **`learn4good.com`** — reject. It's a directory, not a school. Check if Orange County Preparatory Academy (the underlying school) has its own website.
- **`mahadevmaitri.org`** — reject. The URL points to a third-party info page for Orange County Preparatory Academy Charter. Find the school's direct site.
- **`nordangliaeducation.com`** — the school is Windermere Preparatory School. Visit `nordangliaeducation.com/wps-florida` and find whether the school has an independent domain (`windermereprep.com` or similar). If not, the parent site URL is the start URL.
- **`intmontessori.com`** — confirm there is an Orlando/OC FL campus. If yes, find the campus-specific page and add to Phase 2.
- **`christianprepschools.com`** — Osceola Christian Preparatory School is in Osceola County, not OC. Exclude unless DR wants adjacent-county outreach.
- **`gardenfaithpreschool.com`** — Port Orange = Volusia County. Exclude.
- **`opaschools.org`** — Oxford Preparatory Academy may refer to the CA chain. Verify FL location before including.

---

## Ambiguous Candidates Still in Batches (spot-check recommended)
These passed high-confidence filtering but have minor uncertainties:

| School | Host | Note |
|---|---|---|
| Montessori FL | `montessorifl.com` | Domain with no school name — verify it's a real school site and confirm OC FL location |
| Montessori Academy | `montessori-academy.org` | Generic domain — confirm OC FL location |
| OCPS Academic Center For Excellence | `ocpsace.ocps.net` | Verify grades served include elementary range |
| UCP Charter Schools | `ucpcharter.org` | Multi-campus charter org — Phase 2 should identify the specific West Orange campus |
| Orlando Science East Campus | `east.orlandoscience.org` | Already included as separate school from `orlandoscience.org` main campus — both valid if grades confirmed |
| Lake Highland Preparatory School | `lhprep.org` | Primarily middle/upper school — lower school exists but confirm enrollment is open for elementary |
| American Heritage Schools | `ahschool.com` | Plantation FL school. Confirm if there is an Orlando-area campus |

---

## Recommended Next Step — Phase 2 Execution

Run Phase 2 against the 3 batch files in order:
1. `phase2_batch_01.csv` — 25 schools
2. `phase2_batch_02.csv` — 25 schools
3. `phase2_batch_03.csv` — 21 schools

For each URL, Phase 2 verifies:
- Site resolves to a live school website
- Grades served include elementary range (K-5, K-8, PK-5, PK-8, or equivalent)
- Location confirmed in Orange County FL or adjacent target area
- No competing after-school program

**Input for Phase 2:** `data/processed/phase2_batch_01.csv` → `phase2_batch_03.csv`  
**After Phase 2:** Merge verified rows into a single `phase2_verified.csv` and move to Phase 3 enrichment.
