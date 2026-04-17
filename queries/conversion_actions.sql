-- Phase 1 | OEV | Read-only
-- Extrae el catálogo de conversion actions configuradas en la cuenta.
-- Sin segmentación de fecha: es un snapshot del estado actual de configuración.
SELECT
  conversion_action.id,
  conversion_action.name,
  conversion_action.status,
  conversion_action.type,
  conversion_action.category,
  conversion_action.counting_type,
  conversion_action.include_in_conversions_metric,
  conversion_action.value_settings.default_value,
  conversion_action.value_settings.always_use_default_value
FROM conversion_action
WHERE conversion_action.status != 'REMOVED'
ORDER BY conversion_action.name
