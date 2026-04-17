-- Phase 1 | OEV | Read-only
-- Extrae rendimiento diario por asset group de campañas Performance Max.
-- Filtra solo campañas de tipo PERFORMANCE_MAX con asset groups activos.
SELECT
  campaign.id,
  campaign.name,
  asset_group.id,
  asset_group.name,
  asset_group.status,
  metrics.impressions,
  metrics.clicks,
  metrics.ctr,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value,
  segments.date
FROM asset_group
WHERE segments.date DURING LAST_30_DAYS
  AND campaign.advertising_channel_type = 'PERFORMANCE_MAX'
  AND asset_group.status != 'REMOVED'
ORDER BY metrics.cost_micros DESC
