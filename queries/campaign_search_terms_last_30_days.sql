-- Phase 1 | OEV | Read-only
-- Extrae términos de búsqueda con métricas de rendimiento, últimos 30 días.
-- GAQL: campaign_search_term_view.status no existe en v23 del API. Campo omitido.
SELECT
  campaign.id,
  campaign.name,
  campaign_search_term_view.search_term,
  metrics.impressions,
  metrics.clicks,
  metrics.ctr,
  metrics.average_cpc,
  metrics.cost_micros,
  metrics.conversions,
  segments.date
FROM campaign_search_term_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.impressions DESC
