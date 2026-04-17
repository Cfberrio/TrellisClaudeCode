# Data Contracts

## Purpose

Este documento define los schemas esperados en cada etapa del pipeline. Sirve como contrato entre extracción, normalización y reporting.

---

## 1. Raw Data (data/raw/meta/{brand}/{platform}/)

Raw data se almacena como JSON exactamente como viene de la API. No se modifica. El schema varía por plataforma y endpoint.

### Facebook — Naming convention
```
{YYYY-MM-DD}_{endpoint}_{brand}.json
```
Ejemplos:
- `2026-04-01_page_insights_cheese_to_share.json`
- `2026-04-01_posts_discipline_rift.json`

### Instagram — Naming convention
```
{YYYY-MM-DD}_{endpoint}_{brand}.json
```
Ejemplos:
- `2026-04-01_account_insights_discipline_rift.json`
- `2026-04-01_media_cheese_to_share.json`

---

## 2. Staging Schema (data/staging/meta/{brand}/)

Staging normaliza raw data de ambas plataformas a un schema común. Un archivo por tipo de dato.

### account_metrics.json
```json
{
  "brand": "string",
  "period_start": "YYYY-MM-DD",
  "period_end": "YYYY-MM-DD",
  "facebook": {
    "followers": null,
    "page_likes": null,
    "reach_total": null,
    "impressions_total": null,
    "engaged_users": null
  },
  "instagram": {
    "followers": null,
    "reach_total": null,
    "impressions_total": null,
    "profile_views": null,
    "website_clicks": null
  }
}
```

### posts.json
```json
[
  {
    "post_id": "string",
    "platform": "facebook | instagram",
    "published_at": "ISO8601",
    "type": "image | video | carousel | reel | story",
    "message": "string | null",
    "permalink": "string",
    "metrics": {
      "impressions": null,
      "reach": null,
      "likes": null,
      "comments": null,
      "shares": null,
      "saves": null,
      "engagement_rate": null
    }
  }
]
```

### audience_demographics.json
```json
{
  "brand": "string",
  "period_end": "YYYY-MM-DD",
  "facebook": {
    "age_gender": {},
    "top_cities": [],
    "top_countries": []
  },
  "instagram": {
    "age_gender": {},
    "top_cities": [],
    "top_countries": []
  }
}
```

---

## 3. Processed Schema (data/processed/meta/{brand}/)

Processed mergea Facebook + Instagram en un único dataset por marca.

### consolidated_metrics.json
Merge de `account_metrics.json` de staging con campos calculados:
- `total_followers` (FB + IG)
- `total_reach`
- `blended_engagement_rate`
- `follower_growth_pct`

### consolidated_posts.json
Lista unificada de posts de ambas plataformas, ordenada por `engagement_rate` desc.

---

## 4. Output Files (output/meta/{brand}/YYYY-MM/)

| File | Source | Notes |
|---|---|---|
| `account_summary.json` | processed/consolidated_metrics | KPIs de período |
| `content_summary.json` | processed/consolidated_posts | Agregados de contenido |
| `audience_summary.json` | staging/audience_demographics | Demografía cruzada |
| `messages_summary.json` | raw/facebook/messages | Solo FB por ahora |
| `top_content.json` | processed/consolidated_posts | Top 5 por engagement_rate |
| `monthly_metrics_flat.csv` | processed/* | Tabla plana de todas las métricas |
| `monthly_metrics_pretty.xlsx` | monthly_metrics_flat.csv | Versión con formato |
| `monthly_analysis.md` | Todos los outputs | Reporte humano final |

---

## Field Conventions

- Fechas: `YYYY-MM-DD` o ISO8601 para timestamps
- Tasas y porcentajes: decimales (0.035 = 3.5%), no strings con %
- Valores nulos: `null` explícito, nunca string vacío ni cero implícito
- IDs: siempre strings, aunque sean numéricos en la API
