# Metric Definitions

## Purpose

Definiciones canónicas de las métricas usadas en este pipeline. Cuando un término tiene interpretación distinta en Facebook vs Instagram, se documenta la diferencia.

---

## Account-Level Metrics

| Metric | Definition | Facebook | Instagram | Notes |
|---|---|---|---|---|
| `followers` | Número de seguidores activos de la cuenta | `fan_count` | `followers_count` | FB puede tener diferencia entre likes y followers |
| `page_likes` | Número de likes de página (FB only) | `fan_count` | N/A | Solo aplica a Facebook Pages |
| `reach_total` | Personas únicas que vieron cualquier contenido de la cuenta | `page_impressions_unique` | `reach` | Período: 28 días o período reportado |
| `impressions_total` | Total de veces que se mostró contenido (no único) | `page_impressions` | `impressions` | Incluye repetidas |
| `engaged_users` | Usuarios únicos que interactuaron con la cuenta | `page_engaged_users` | No disponible directo | |
| `follower_growth` | Nuevos seguidores en el período | `page_fan_adds` | (calculado: end - start) | |
| `follower_growth_pct` | Crecimiento porcentual de seguidores | Calculado | Calculado | `(end - start) / start` |

---

## Post-Level Metrics

| Metric | Definition | Facebook | Instagram |
|---|---|---|---|
| `impressions` | Veces que se mostró el post (no único) | `post_impressions` | `impressions` |
| `reach` | Personas únicas que vieron el post | `post_impressions_unique` | `reach` |
| `likes` | Reacciones positivas | `post_reactions_like_total` (+ other reactions) | `like_count` |
| `comments` | Comentarios en el post | `post_comments` | `comments_count` |
| `shares` | Veces compartido | `post_shares` | N/A (Reels: `shares`) |
| `saves` | Guardados | N/A | `saved` |
| `engagement_rate` | Interacciones totales / reach | Calculado | Calculado |

### Engagement Rate Formula
```
engagement_rate = (likes + comments + shares + saves) / reach
```
Nota: se usa `reach` como denominador (no followers) para comparabilidad entre posts con diferente distribución.

---

## Audience Metrics

| Metric | Definition |
|---|---|
| `top_cities` | Top 5 ciudades por volumen de seguidores |
| `top_countries` | Top 5 países por volumen de seguidores |
| `age_gender` | Distribución de seguidores por rango de edad y género |

---

## Messaging Metrics (Facebook only)

| Metric | Definition |
|---|---|
| `conversations_total` | Total de conversaciones en el inbox en el período |
| `messages_received` | Total de mensajes recibidos |
| `messages_sent` | Total de mensajes enviados desde la página |
| `avg_response_time_hrs` | Tiempo promedio de primera respuesta en horas |

---

## Composite / Calculated Metrics

| Metric | Formula | Notes |
|---|---|---|
| `blended_engagement_rate` | Promedio ponderado de engagement rate FB + IG | Ponderado por reach de cada plataforma |
| `total_followers` | FB followers + IG followers | Cross-platform follower count |
| `total_reach` | FB reach + IG reach | No deduplicado (audiencias se pueden superponer) |

---

## Reporting Thresholds

Definidos en `config/reporting.json`. Resumen:

| Level | Engagement Rate |
|---|---|
| Low | < 1% |
| Good | 1–3% |
| Excellent | > 6% |

---

## Platform Limitations

- Instagram no provee datos de `shares` en posts estándar (solo en Reels)
- Facebook Stories tienen métricas distintas a posts estándar (no se incluyen en top content)
- Instagram Stories métricas expiran a los 7 días — requieren extracción frecuente
- Facebook API v19+ deprecó `post_story_adds` — usar `post_shares` como alternativa
