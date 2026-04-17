-- Phase 1 | OEV | Read-only
-- Extrae conversiones por campaña segmentadas por conversion action, últimos 30 días.
-- GAQL: metrics.cost_micros es incompatible con segments.conversion_action en este recurso.
--       Se omite cost_micros para mantener compatibilidad. Solo campañas con conversiones > 0.
SELECT
  campaign.id,
  campaign.name,
  segments.conversion_action,
  segments.conversion_action_name,
  metrics.conversions,
  metrics.conversions_value,
  segments.date
FROM campaign
WHERE segments.date DURING LAST_30_DAYS
  AND campaign.status != 'REMOVED'
  AND metrics.conversions > 0
ORDER BY metrics.conversions DESC
