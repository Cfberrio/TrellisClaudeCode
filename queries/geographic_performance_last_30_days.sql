-- Phase 1 | OEV | Read-only
-- Extrae rendimiento geográfico por campaña, últimos 30 días.
-- Incluye país y tipo de ubicación (presencia física vs. interés).
SELECT
  campaign.id,
  campaign.name,
  geographic_view.country_criterion_id,
  geographic_view.location_type,
  metrics.impressions,
  metrics.clicks,
  metrics.ctr,
  metrics.average_cpc,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value,
  segments.date
FROM geographic_view
WHERE segments.date DURING LAST_30_DAYS
ORDER BY metrics.cost_micros DESC
