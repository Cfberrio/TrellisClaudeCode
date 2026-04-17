# Phase 1 Refinement Summary — 2026-04-08

## Counts
| Metric | Count |
|---|---|
| Original cleaned candidates | 254 |
| **High-confidence school candidates** | **107** |
| **Manual review candidates** | **147** |

---

## High-Confidence Split Breakdown
| Confidence Signal | Count |
|---|---|
| `school_keyword_in_domain:academy` | 37 |
| `school_keyword_in_domain:school` | 19 |
| `school_keyword_in_domain:prep` | 12 |
| `school_keyword_in_domain:montessori` | 10 |
| `official_ocps_school_subdomain` | 8 |
| `title_school+fl_signal:"charter school" + "orlando"` | 4 |
| `school_keyword_in_domain:charter` | 4 |
| `school_keyword_in_domain:christian` | 3 |
| `title_school+fl_signal:"academy" + "orlando"` | 3 |
| `title_school+fl_signal:"christian school" + "orlando"` | 2 |
| `school_keyword_in_domain:educati` | 2 |
| `title_school+fl_signal:"private school" + "orlando"` | 1 |
| `title_school+fl_signal:"christian school" + "central florida"` | 1 |
| `title_school+fl_signal:"elementary school" + "orlando"` | 1 |

---

## Manual Review — Reasons by Category
| Category | Count |
|---|---|
| Aggregators / directories | 60 |
| Out-of-area domains (wrong state/county) | 51 |
| Needs location/type verification | 24 |
| No strong domain or title signal | 7 |
| Out-of-area title signal | 5 |

---

## Manual Review — Top Patterns
| Reason | Count |
|---|---|
| `needs_location_or_type_verification:ocps.net` | 10 |
| `aggregator_or_directory:nces.ed.gov` | 6 |
| `aggregator_or_directory:fldoe.org` | 4 |
| `out_of_area_domain:heritagemontessori.com` | 3 |
| `aggregator_or_directory:cfpublic.org` | 3 |
| `aggregator_or_directory:orangecountyfirst.com` | 2 |
| `aggregator_or_directory:movoto.com` | 2 |
| `aggregator_or_directory:mapquest.com` | 2 |
| `aggregator_or_directory:elementaryschools.org` | 2 |
| `out_of_area_domain:alpha.school` | 2 |
| `out_of_area_domain:osceolaschools.net` | 2 |
| `out_of_area_domain:orangeusd.org` | 2 |
| `aggregator_or_directory:stepupforstudents.org` | 2 |
| `out_of_area_title_signal:"seminole county"` | 2 |
| `out_of_area_domain:oneclay.net` | 2 |
| `needs_location_or_type_verification:orangecounty.net` | 1 |
| `needs_location_or_type_verification:floridaschoolchoice.org` | 1 |
| `out_of_area_title_signal:"orange county, ca"` | 1 |
| `no_strong_signal:tcsapopka.org` | 1 |
| `no_strong_signal:princeton-house.org` | 1 |

---

## Manual Review — Rows Worth Human Eyeball (not obvious aggregators/out-of-area)
These are the ambiguous rows that survived cleaning but couldn't be auto-classified. Quickest to verify:

| Host | Title | Reason |
|---|---|---|
| `ocps.net` | Orange County Public Schools - Private Schools | needs_location_or_type_verification:ocps.net |
| `orangecounty.net` | Private Schools in Orange County | needs_location_or_type_verification:orangecounty.net |
| `floridaschoolchoice.org` | Florida Private Schools Directory - School Choice | needs_location_or_type_verification:floridaschoolchoice.org |
| `tcsapopka.org` | Trinity Christian School | no_strong_signal:tcsapopka.org |
| `ocps.net` | Current List of Charter Schools | needs_location_or_type_verification:ocps.net |
| `ocps.net` | Charter Schools Home | needs_location_or_type_verification:ocps.net |
| `princeton-house.org` | Princeton House Charter School | no_strong_signal:princeton-house.org |
| `ocps.net` | Orange County Public Schools - Home | needs_location_or_type_verification:ocps.net |
| `ocps.net` | Orange County Public Schools - Schools Home | needs_location_or_type_verification:ocps.net |
| `liftorlando.org` | Lift Orlando & Orange Center Elementary | needs_location_or_type_verification:liftorlando.org |
| `ocps.net` | Scholastic Academies | needs_location_or_type_verification:ocps.net |
| `ocps.net` | Find My School Home | needs_location_or_type_verification:ocps.net |
| `ocps.net` | Middle School & K-8 Cadres | needs_location_or_type_verification:ocps.net |
| `scacrusaders.com` | Elementary | no_strong_signal:scacrusaders.com |
| `lecs.org` | Lake Eola Charter School – Tuition Free K-8 Public School In | no_strong_signal:lecs.org |
| `mdcacademy.org` | Mount Dora Christian Academy: Home | needs_location_or_type_verification:mdcacademy.org |
| `orlandotorah.com` | Elementary School: Ages 5 – 10 | no_strong_signal:orlandotorah.com |
| `ocps.net` | School Directory Home | needs_location_or_type_verification:ocps.net |
| `zfc.com` | Elementary Schools in Orange County | needs_location_or_type_verification:zfc.com |
| `ocps.net` | Charter Schools | needs_location_or_type_verification:ocps.net |
| `cca.education` | Central Christian Academy | needs_location_or_type_verification:cca.education |
| `montverde.org` | Montverde Academy | Excellence in Education, Athletics ... | no_strong_signal:montverde.org |
| `btischool.com` | Bridge to Independence Private School | needs_location_or_type_verification:btischool.com |
| `pcaknights.org` | pcaknights.org - Home | needs_location_or_type_verification:pcaknights.org |
| `wiseprivateschool.org` | WISE Private School | needs_location_or_type_verification:wiseprivateschool.org |

---

## Recommended Next Step — Phase 2 Automatic Verification

Run Phase 2 website verification against **`phase1_high_confidence_candidates.csv`** only (107 rows).

For each candidate, Phase 2 should confirm:
1. Site resolves and is a live school website (not a redirect or placeholder)
2. Grades served include K-5, K-8, PK-5, PK-8, or equivalent elementary range
3. School is located in Orange County FL or adjacent area (confirm from website)
4. No competing after-school program that would block DR outreach

Manual review file (`phase1_manual_review_candidates.csv`, 147 rows) should be spot-checked by a human before or in parallel with Phase 2. Priority: verify the 31 rows under "needs_location/no_strong_signal" — these are fastest to confirm and may add high-quality candidates to the Phase 2 batch.

**Owner:** TBD  
**Input for Phase 2:** `data/processed/phase1_high_confidence_candidates.csv`
