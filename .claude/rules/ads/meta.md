---
paths:
  - "domains/ads/meta/**"
---

# Meta Ads — Platform Rules

## Status
Scaffold stage. No active pipeline yet.

## Future Pipeline Location
`domains/ads/meta/discipline-rift/` — Meta Ads pipeline for the Discipline Rift (DR) brand.

## Brand Context
DR is youth sports, recruiting, franchise/license growth, and conversion-heavy marketing. Content should feel energetic, clear, trustworthy, and conversion-aware. Parents need clarity, cold audiences need specifics, recruiting content needs opportunity clarity early.

## Expected Architecture
When the pipeline becomes active, it will follow the same phase pattern as Google Ads:
- Phase 1: extraction (read-only) → `data/raw/`
- Phase 2: diagnostic → `output/`
- Phase 3: campaign rehab SOP → `output/`

## Authentication
Meta Ads API credentials will use a separate `.env.example` inside the domain directory. Do not mix with Google Ads credentials in root `.env`.

## Default Posture
Read-only by default. Do not mutate campaigns, ad sets, ads, or audiences unless an explicit skill authorizes it.
