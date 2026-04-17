# Meta Social Metrics

Extracción, normalización y reporte mensual de métricas orgánicas de Facebook e Instagram para las marcas del portafolio Trellis.

**Marcas activas:** Cheese To Share · Discipline Rift · DR Volleyball Club

---

## Architecture

```
Meta Graph API
  ↓
data/raw/meta/{brand}/{platform}/     — respuestas crudas (JSON por endpoint)
  ↓
data/staging/meta/{brand}/            — datos normalizados a schema común
  ↓
data/processed/meta/{brand}/          — datos mergeados FB + IG
  ↓
output/meta/{brand}/YYYY-MM/          — output final consolidado por marca, versionado por mes
```

---

## Output per Brand

```
output/meta/{brand}/
└── YYYY-MM/
    ├── account_summary.json       — KPIs de cuenta consolidados
    ├── content_summary.json       — métricas de contenido consolidadas
    ├── audience_summary.json      — demografía cruzada
    ├── messages_summary.json      — señales de inbox (Facebook)
    ├── top_content.json           — top 5 posts por engagement_rate (FB + IG)
    ├── monthly_metrics_flat.csv   — tabla plana de todas las métricas
    ├── monthly_metrics_pretty.xlsx — versión presentable con formato
    └── monthly_analysis.md        — reporte humano principal
```

---

## Brands

| Brand | Facebook | Instagram |
|---|---|---|
| Cheese To Share | TBD | TBD |
| Discipline Rift | TBD | TBD |
| DR Volleyball Club | TBD | TBD |

---

## Separation from Adjacent Domains

| Domain | Path | Env var prefix |
|---|---|---|
| Paid Ads (Meta) | `domains/ads/meta/` | `META_*` |
| Social Automation | `domains/ops/social-automation/` | — |
| **This project** | `domains/ops/social-metrics/` | `SOCIAL_METRICS_*` |

The workspace uses a **single global `.env`**. This project exclusively reads variables prefixed `SOCIAL_METRICS_` — it never reads bare `META_*` variables, which belong to the Ads pipeline.

---

## Setup

```bash
# Install dependencies
pip install -r requirements.txt

# Copy env variables into your global .env at the workspace root
# The runner finds .env automatically — no manual source needed
cat domains/ops/social-metrics/.env.example
# Add the SOCIAL_METRICS_* variables to your global .env and fill them in
```

## Running a Monthly Report

```bash
# From the domain directory
cd domains/ops/social-metrics/

# Extract all 3 brands for April 2026
python scripts/meta/run_monthly.py --month 2026-04

# Extract a single brand
python scripts/meta/run_monthly.py --month 2026-04 --brand discipline_rift
```

The runner auto-loads `.env` from the workspace root. No `source .env` step needed.

Output is written to `output/meta/{brand}/YYYY-MM/`.

## Validate Config

```bash
python -c "from src.config.meta_config import validate_all; validate_all(); print('Config OK')"
```

---

## Status

**Phase 1 — Implementation complete.** Runner, extractors, consolidator, and reporter are all functional. Tests: 61 passing.

See `docs/setup.md` for full credential setup instructions.
