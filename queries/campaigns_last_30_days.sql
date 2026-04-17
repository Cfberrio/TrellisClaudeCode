-- Phase 1 | OEV | Read-only
-- Extrae rendimiento diario por campaña activa en los últimos 30 días.
-- Incluye canal, estrategia de puja, impresiones, clics, costo y conversiones.
SELECT
  campaign.id,
  campaign.name,
  campaign.status,
  campaign.advertising_channel_type,
  campaign.bidding_strategy_type,
  metrics.impressions,
  metrics.clicks,
  metrics.ctr,
  metrics.average_cpc,
  metrics.cost_micros,
  metrics.conversions,
  metrics.conversions_value,
  segments.date
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
  AND campaign.status != 'REMOVED'
ORDER BY metrics.cost_micros DESC
