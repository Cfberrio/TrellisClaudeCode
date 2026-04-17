# Phase 1 Cleaning Summary — 2026-04-08

## Counts
| Metric | Value |
|---|---|
| Total raw SERP rows | 60 |
| Total organic result slots | 10 per row (600 max) |
| Extracted candidates (with URL) | 595 |
| After URL deduplication | 371 |
| **Kept (school candidates)** | **254** |
| **Rejected** | **117** |

## Top Rejection Reasons
| Reason | Count |
|---|---|
| junk_host:niche.com | 21 |
| junk_host:facebook.com | 11 |
| junk_host:usnews.com | 10 |
| junk_host:yelp.com | 10 |
| junk_host:youtube.com | 10 |
| junk_host:greatschools.org | 6 |
| junk_host:instagram.com | 6 |
| junk_host:reddit.com | 3 |
| junk_host:wikipedia.org | 3 |
| junk_host:mynews13.com | 3 |
| junk_host:homes.com | 3 |
| junk_host:trulia.com | 3 |
| junk_host:clickorlando.com | 3 |
| no_school_signal | 3 |
| junk_host:privateschoolreview.com | 2 |

## Top Rejected Domains
| Host | Count |
|---|---|
| niche.com | 21 |
| usnews.com | 10 |
| yelp.com | 10 |
| facebook.com | 10 |
| youtube.com | 10 |
| greatschools.org | 6 |
| instagram.com | 6 |
| reddit.com | 3 |
| en.wikipedia.org | 3 |
| mynews13.com | 3 |
| homes.com | 3 |
| trulia.com | 3 |
| clickorlando.com | 3 |
| privateschoolreview.com | 2 |
| fox35orlando.com | 2 |

## Ambiguous Domains — Manual Review Recommended
These kept candidates lack obvious school identifiers in their host domain name. Verify during Phase 2:

| Title | URL | Host |
|---|---|---|
| Pinecrest Preparatory Academy Orlando Campus | https://www.pinecrestorlando.org/ | pinecrestorlando.org |
| Orlando Science Elementary School - Seminole ... | https://orlandoscience.org/elementary/ | orlandoscience.org |
| Orange County Public Schools - Private Schools | https://www.ocps.net/private-schools | ocps.net |
| Private Schools in Orange County | https://www.orangecounty.net/html/edu_private2.html | orangecounty.net |
| Trinity Christian School | https://www.tcsapopka.org/ | tcsapopka.org |
| Central Florida Christian Academy: Homepage | https://cfcaeagles.org/ | cfcaeagles.org |
| Current List of Charter Schools | https://www.ocps.net/current-list-of-charter-schools | ocps.net |
| Charter Schools Home | https://www.ocps.net/charter-schools-home | ocps.net |
| Orlando Science Schools: OSS Main Campus | https://orlandoscience.org/ | orlandoscience.org |
| Princeton House Charter School | https://www.princeton-house.org/ | princeton-house.org |
| Orlando: Charter Schools | https://fun4orlandokids.com/Education-Childcare/Charter-Schools/ | fun4orlandokids.com |
| Orange County Public Schools - Home | https://www.ocps.net/ | ocps.net |
| Orange County Public Schools - Schools Home | https://www.ocps.net/schools | ocps.net |
| Private School | Montessori School of East Orlando | United  | https://www.mseastorlando.com/ | mseastorlando.com |
| Montessori Schools | EdGuideCF | https://www.edguidecf.com/copy-of-early-learning | edguidecf.com |
| Family Christian Academy: www.fcaorlando.com Private ... | https://www.fcaorlando.com/ | fcaorlando.com |
| Faith Christian Academy | Orlando – A Ministry of Faith ... | https://fcalions.org/ | fcalions.org |
| Berean Christian Academy | Orange Park, FL Private School | https://bccanes.org/ | bccanes.org |
| K-12 Private Schools | https://www.fldoe.org/schools/school-choice/private-schools/ | fldoe.org |
| Lift Orlando & Orange Center Elementary | https://www.liftorlando.org/eduupdate | liftorlando.org |
| Home - Orange County School District | https://www.orangecountyfirst.com/ | orangecountyfirst.com |
| Scholastic Academies | https://www.ocps.net/scholasticacademies | ocps.net |
| Living Word Academy – Orlando, FL | https://lwaorlando.com/ | lwaorlando.com |
| PreK-12 Private School in Orange Park | St. Johns Country Da | https://www.sjcds.net/ | sjcds.net |
| The Bolles School: Home | https://www.bolles.org/ | bolles.org |
| Find My School Home | https://www.ocps.net/find-my-school-home | ocps.net |
| Orange County Public Schools: Home | https://www.ocss-va.org/ | ocss-va.org |
| Orange County Public Schools release 'potential uses' for .. | https://www.wusf.org/education/2026-01-07/orange-county-public-schools-release-p | wusf.org |
| Middle School & K-8 Cadres | https://www.ocps.net/126617_3 | ocps.net |
| Windy Ridge K-8 - Home - Orange County Public Schools | https://windyridgek8.ocps.net/ | windyridgek8.ocps.net |

## Next Step
Hand `phase1_candidates_cleaned.csv` to Phase 2 (website verification).
Priority: confirm grades served (K-5 / K-8 / PK-8) and flag any after-school program conflicts.
Verify ambiguous domains manually before Phase 2 scrape.
