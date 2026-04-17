# Phase 3 — Summaries

## Input
`data/processed/verification/validated_schools_for_schooldigger.csv` is the only input for Phase 3. No batching by default — process the full file in one pass.

## Determinants for business_fit

1. `students_count >= 200`
2. White must be the highest racial percentage in the school's demographic breakdown
3. If the school is not found in SchoolDigger or demographic data is unclear, set `notes = "Not found or no data"`

## Note
Do not run unresolved website lookup before Phase 3 finishes. Those are independent tracks.
