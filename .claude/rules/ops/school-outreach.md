---
paths:
  - "domains/ops/school-outreach/**"
---

# School Outreach — Operations Rules

## Domain
Pipeline de discovery, verificación y enriquecimiento de escuelas candidatas para el programa de Discipline Rift. Orientado a sales outreach directo.

## Phases
- **Phase 1 — Discovery**: identificación y limpieza inicial de escuelas candidatas en el área objetivo (Orlando, Florida). Fuente principal: Apify.
- **Phase 2 — Website verification**: verificación manual o semi-automatizada de cada escuela en su sitio web oficial para confirmar tipo de escuela (elementary / lower school) y grados servidos (K-5, K-8, PK-5, PK-8, o equivalentes).
- **Phase 3 — Enrichment + CRM prep**: enriquecimiento estadístico (tamaño, matrícula, contacto) y preparación del dataset para importación a CRM.

## Data principles
- Prefer official school websites over third-party directories (GreatSchools, Niche, etc.).
- Preserve `source_query`, `source_url`, `notes`, and `rejection_reason` in every row.
- Never invent or assume data that is not explicitly available from the source.
- Keep rejected schools in a separate file — never delete them from the dataset.
- Rejected rows must include a rejection reason (e.g., wrong grade range, private-only, closed, duplicate).

## Output principles
- Outputs should be concise and operational — ready to hand off or import.
- No bloated reports. No speculative analysis.
- Each phase output must be clearly named with date and phase number.
- Naming convention: `YYYY-MM-DD_dr_school_outreach_phase{N}_{descriptor}.csv`

## Separation
- Este dominio NO mezcla con `domains/ads/` ni con `domains/ops/social-automation/`.
- No usar credenciales de Meta Ads ni de Google Ads en este pipeline.
- No cruzar datos de este dominio con datos de paid media sin una tarea explícita.
