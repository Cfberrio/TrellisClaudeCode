# Meta Social Metrics — Project Overview

## Purpose

Este proyecto extrae, normaliza, consolida y reporta métricas orgánicas de Facebook e Instagram para tres marcas del portafolio Trellis:

- **Cheese To Share**
- **Discipline Rift**
- **DR Volleyball Club**

El objetivo es producir reportes mensuales consolidados por marca que combinen datos de ambas plataformas en una sola vista operacional.

---

## Scope

**In scope:**
- Facebook Page Insights (alcance, engagement, seguidores, contenido, mensajes)
- Instagram Business Account Insights (alcance, engagement, seguidores, contenido)
- Métricas orgánicas — no paid ads

**Out of scope (por ahora):**
- TikTok (arquitectura preparada, no activo)
- Paid media de Meta — eso vive en `domains/ads/meta/`
- Automatización de comentarios — eso vive en `domains/ops/social-automation/`

---

## Pipeline Overview

```
Meta Graph API (Facebook + Instagram)
  → data/raw/meta/{brand}/{platform}/        — respuestas crudas de API
  → data/staging/meta/{brand}/               — datos normalizados por plataforma
  → data/processed/meta/{brand}/             — datos mergeados y enriquecidos
  → output/meta/{brand}/YYYY-MM/              — output final consolidado por marca, versionado por mes
```

---

## Output Structure per Brand

| File | Description |
|---|---|
| `account_summary.json` | KPIs de cuenta: seguidores, alcance, engagement rate |
| `content_summary.json` | Métricas de contenido: posts, impresiones, interacciones |
| `audience_summary.json` | Demografía y comportamiento de audiencia |
| `messages_summary.json` | Volumen y tiempos de respuesta en inbox |
| `top_content.json` | Top 5 posts por engagement rate, cruzado FB + IG |
| `monthly_metrics_flat.csv` | Tabla plana con todas las métricas del período |
| `monthly_metrics_pretty.xlsx` | Versión presentable con formato |
| `monthly_analysis.md` | Reporte humano principal con insights y recomendaciones |

---

## Platform Separation Strategy

- **raw/** separa por plataforma (facebook/, instagram/) — las APIs son distintas y los schemas también
- **staging/** normaliza a schema común — las diferencias de plataforma se absorben aquí
- **processed/** mergea ambas plataformas — un solo dataset por marca
- **output/** es siempre consolidado — nunca separado por plataforma

---

## Adding TikTok Later

TikTok ya tiene un slot reservado en `config/platforms.json` (inactive). Para activarlo:
1. Agregar `tiktok/` en `data/raw/meta/{brand}/`
2. Crear extractor en `src/tiktok/` (o `src/meta/tiktok/` si se integra bajo Meta Business)
3. Agregar normalización en staging
4. El processed/ y output/ ya están estructurados para absorberlo sin cambios

---

## Dependencies

- Python 3.10+
- Meta Graph API access token (Long-Lived Token o System User Token)
- Facebook Developer App con permisos de Page Insights e Instagram Insights
- Ver `.env.example` para variables requeridas
