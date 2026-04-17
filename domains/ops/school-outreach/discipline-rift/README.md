# School Outreach — Discipline Rift (DR)

## Overview
Pipeline de discovery, verificación y enriquecimiento de escuelas elementales candidatas para el programa after-school de Discipline Rift en Orlando, Florida.

Este dominio NO es parte del pipeline de ads ni de social automation. Es un pipeline de sales outreach: el output final es una lista limpia, verificada y lista para importar a CRM.

**Status: Scaffold — setup inicial**

---

## Pipeline architecture

```
Apify (raw school discovery)
  ↓
data/raw/apify/         ← JSON/CSV crudos de Apify
  ↓
Phase 1 — Discovery + cleaning
  ↓
output/fase-1/          ← lista limpia de candidatas + rechazadas
  ↓
Phase 2 — Website verification
  ↓
output/fase-2/          ← lista verificada con grados + contacto
  ↓
Phase 3 — Enrichment + CRM prep
  ↓
output/fase-3/          ← dataset listo para importar a CRM
```

---

## Phases

| Phase | Name | Input | Output |
|---|---|---|---|
| 1 | Discovery + cleaning | Apify raw data | `phase1_discovery.csv` + `rejected.csv` |
| 2 | Website verification | Phase 1 output | `phase2_verified.csv` |
| 3 | Enrichment + CRM prep | Phase 2 output | `phase3_crm_ready.csv` |

---

## Directory structure

```
discipline-rift/
├── CLAUDE.md                              # Domain AI context
├── README.md                              # This file
├── .env.example                           # Credentials/config template
├── scripts/                               # Future scripts (Python, bash)
│   └── .gitkeep
├── prompts/                               # Claude prompt templates for each phase
│   └── .gitkeep
├── data/
│   ├── raw/
│   │   └── apify/                         # Raw exports from Apify tasks
│   │       └── .gitkeep
│   └── processed/                         # Intermediate cleaned data
│       └── .gitkeep
└── output/
    ├── fase-1/                            # Discovery outputs
    │   └── .gitkeep
    ├── fase-2/                            # Verification outputs
    │   └── .gitkeep
    └── fase-3/                            # CRM-ready outputs
        └── .gitkeep
```

---

## Expected inputs

- **Apify task output**: JSON or CSV from a Google Maps or school directory scraper. Place raw files in `data/raw/apify/`.
- **Manual additions**: schools found outside Apify can be added directly to Phase 1 output with `source_url` filled.

---

## Expected outputs

| File | Fields |
|---|---|
| `phase1_discovery.csv` | school_name, address, city, state, zip, phone, website, school_type, grades_served, source_query, source_url, notes, status |
| `phase2_verified.csv` | + website_confirmed, grades_served (verified), has_competing_afterschool, contact_name, contact_email, contact_phone, verification_notes |
| `phase3_crm_ready.csv` | + enrollment_estimate, district, priority_score, crm_pipeline, crm_stage |
| `rejected.csv` | All columns + rejection_reason |

---

## Relationship to Apify

Apify is the primary data source for Phase 1. It runs automated scraping tasks (Google Maps school search, school directory scrapers) and exports structured data.

- Raw Apify outputs go to `data/raw/apify/`
- Task IDs and dataset IDs are tracked in `.env`
- Future: Apify MCP integration via `.cursor/mcp.json` for direct Claude Code access to Apify task results

---

## Relationship to Claude Code MCP (future)

The `.cursor/mcp.json` file in the workspace root will configure the Apify MCP server, allowing Claude Code to:
- Browse Apify task results directly
- Pull dataset rows without manual export
- Trigger or monitor Apify runs from within the IDE

This integration is planned but not yet active.

---

## Naming conventions

```
YYYY-MM-DD_dr_school_outreach_phase{N}_{descriptor}.csv

Examples:
2026-04-08_dr_school_outreach_phase1_discovery.csv
2026-04-08_dr_school_outreach_phase2_verified.csv
2026-04-08_dr_school_outreach_phase3_crm_ready.csv
2026-04-08_dr_school_outreach_rejected.csv
```

---

## Suggested next steps

1. Run an Apify task (Google Maps scraper or school directory) for elementary schools in Orlando, FL
2. Export raw results to `data/raw/apify/`
3. Run Phase 1 cleaning — filter by grade range, remove obvious mismatches, flag rejected rows
4. Run Phase 2 verification — visit each school website to confirm grades served
5. Run Phase 3 enrichment — normalize for CRM import, assign pipeline stage
6. Import Phase 3 output to GHL or CRM of choice

---

## Notes

- Emails of principals/coordinators are often not published on school websites. Collect them via phone call during outreach. Mark `email_source: to_call` when not found online.
- Keep rejected rows — they serve as a dedupe reference for future runs.
- This pipeline is brand-specific to Discipline Rift (DR). Do not import OEV or CTS data into this domain.
