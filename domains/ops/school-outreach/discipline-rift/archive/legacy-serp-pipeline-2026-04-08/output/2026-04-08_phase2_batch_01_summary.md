# Phase 2 Batch 01 Verification Summary — 2026-04-08

## Results
| Status | Count |
|---|---|
| YES — confirmed elementary candidate | 6 |
| NO — disqualified | 5 |
| NOT_SURE — insufficient evidence | 14 |
| **Total** | **25** |

---

## YES — Confirmed Elementary Candidates (6)
| School | Host | Key Evidence |
|---|---|---|
| Aspire Charter Academy | `aspirecharteracademy.com` | K-5 public charter elementary school in Orlando FL. Multiple pages confirm "Serv |
| Central Florida Preparatory School | `cfprep.org` | PreK-12 private school in Apopka (Orange County FL). Grade selector explicitly l |
| Family Christian Academy | `fcaorlando.com` | K-12 private Christian school in East Orlando (15060 Old Cheney Hwy, FL 32828).  |
| Foundation Academy | `foundationacademy.net` | PK-12 private Christian school in Winter Garden (Orange County FL). Dedicated el |
| Heritage Prep School | `heritageprep.com` | K-12 Independent Baptist private school in West Orlando (Pine Hills, Ocoee, Orlo |
| Jewish Academy of Orlando | `jewishacademyorlando.org` | Explicitly an elementary school in Central Florida. Title: "The Premier Elementa |

---

## NO — Disqualified (5)
| School | Host | Reason | Flag |
|---|---|---|---|
| American Heritage Schools | `ahschool.com` | Out of area. All campuses listed are in South Florida: Tampa, Fort Mye | `out_of_area` |
| Central Florida Leadership Academy | `cflacademy.org` | Grades 6-12 only. Homepage states "COLLEGE PREP CHARTER SCHOOL FOR STU | `not_elementary` |
| Center Academy | `centeracademy.com` | Special education school for autism/ADHD/learning disabilities. Neares | `not_elementary` |
| Keystone Academy | `keystone-academy.com` | Homeschool co-op providing weekly academic classes to homeschooled stu | `homeschool_or_nontraditional` |
| Cornerstone Charter Academy | `cornerstonecharter.com` | Evidence points to middle/high school only: Bright Futures scholarship | `not_elementary` |

---

## NOT_SURE — Ambiguous / Insufficient Evidence (14)
| School | Host | Issue | Flag |
|---|---|---|---|
| Audubon Park School | `audubonparkk8.ocps.net` | No crawl data returned. Domain name "audubonparkk8.ocps.net" stro | `weak_grade_signal` |
| Bridge Prep Academy Orange Campus | `bridgepreporange.com` | Single crawled page returned only summer program announcement. "O | `weak_grade_signal` |
| Bridgeprep Academy Charter Schools | `bridgeprepacademy.com` | Single page crawled. Multi-campus charter school — grade range an | `weak_grade_signal` |
| Camen Academy | `camenacademy.com` | Specialty school for neurodiverse students using performing arts  | `homeschool_or_nontraditional` |
| Central Florida Christian Academy | `cfcaeagles.org` | No crawl data returned. Phase 1 title confirms "Central Florida C | `weak_grade_signal` |
| Circle Christian Schools | `circlechristianschool.org` | Single homepage crawled. No grade range mentioned in crawl text.  | `weak_grade_signal` |
| Core FL Academy | `coreflacademy.org` | No crawl data returned. Phase 1 title: "Elementary School in Orla | `weak_grade_signal` |
| Eastland Christian School | `eastlandchristian.org` | Homepage crawled but grade range not stated. School confirmed in  | `weak_grade_signal` |
| Faith Christian Academy | `fcalions.org` | Homepage crawled. Orlando FL confirmed (Ministry of Faith Assembl | `weak_grade_signal` |
| Hillcrest Elementary | `hillcrestes.ocps.net` | No crawl data returned. Phase 1 title: "Hillcrest Elementary - Ho | `weak_grade_signal` |
| Hope Charter School | `hopecharter.org` | Single page crawled. Site references "Legacy Charter High School" | `weak_grade_signal` |
| Innovation Montessori Ocoee | `innovationmontessori.com` | Montessori school confirmed in Ocoee FL (Orange County). Crawled  | `weak_grade_signal` |
| Lake Forrest Prep | `lakeforrestprep.com` | Orlando private school confirmed but grade range not stated in cr | `weak_grade_signal` |
| Trinity Prep | `trinityprep.org` | No crawl data returned. Phase 1 title: "Best Private School In Or | `weak_grade_signal` |

---

## Flags Summary
| Flag | Count |
|---|---|
| `weak_grade_signal` | 13 |
| `not_elementary` | 3 |
| `homeschool_or_nontraditional` | 2 |
| `out_of_area` | 1 |

---

## Rerun Recommendation

**Rerun size: 14 URLs** — all NOT_SURE rows should be re-crawled before Phase 3.

### Priority split:
- **5 schools returned no crawl data at all** — simple re-crawl required:
  - `audubonparkk8.ocps.net` — Audubon Park School
  - `cfcaeagles.org` — Central Florida Christian Academy
  - `coreflacademy.org` — Core FL Academy
  - `hillcrestes.ocps.net` — Hillcrest Elementary
  - `trinityprep.org` — Trinity Prep

- **9 schools had crawl data but insufficient grade evidence** — re-crawl targeting admissions or curriculum page:
  - `bridgepreporange.com` — Bridge Prep Academy Orange Campus (weak_grade_signal)
  - `bridgeprepacademy.com` — Bridgeprep Academy Charter Schools (weak_grade_signal)
  - `camenacademy.com` — Camen Academy (homeschool_or_nontraditional)
  - `circlechristianschool.org` — Circle Christian Schools (weak_grade_signal)
  - `eastlandchristian.org` — Eastland Christian School (weak_grade_signal)
  - `fcalions.org` — Faith Christian Academy (weak_grade_signal)
  - `hopecharter.org` — Hope Charter School (weak_grade_signal)
  - `innovationmontessori.com` — Innovation Montessori Ocoee (weak_grade_signal)
  - `lakeforrestprep.com` — Lake Forrest Prep (weak_grade_signal)

### Suggested approach for rerun:
- For no-data schools: retry homepage with longer timeout
- For weak-signal schools: crawl `/admissions`, `/academics`, `/about`, or `/grades` sub-pages specifically
- Bridgeprep (`bridgepreporange.com`, `bridgeprepacademy.com`): crawl the grades or programs page — known K-8 charter chain but confirm OC campus grades explicitly
- Camen Academy (`camenacademy.com`): confirm if it qualifies as a traditional school for DR outreach purposes — may be a hard NO given nontraditional/ABA model

### Do not rerun:
- 6 YES schools — move to Phase 3
- 5 NO schools — move to rejected file

**Input for Phase 3:** `phase2_batch_01_verified.csv` (YES rows only)  
**Owner:** TBD
