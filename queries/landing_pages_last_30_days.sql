-- Phase 1 | OEV | Read-only
-- Extrae rendimiento por URL de landing page expandida, últimos 30 días.
-- Útil para identificar qué destinos reciben tráfico y cómo convierten.
SELECT
  campaign.id,
  campaign.name,
  expanded_landing_page_view.expanded_final_url,
  metrics.impressions,
  metrics.clicks,
  metrics.ctr,
  metrics.average_cpc,
  metrics.cost_micros,
  metrics.conversions,
  segments.date
FROM expanded_landing_page_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.clicks DESC
