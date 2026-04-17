-- Phase 1 | OEV | Read-only
-- Extrae llamadas rastreadas por Google Ads con duración, estado y origen.
-- GAQL: call_view no soporta segments.date. Se retorna el historial completo disponible.
SELECT
  campaign.id,
  campaign.name,
  call_view.call_duration_seconds,
  call_view.call_status,
  call_view.call_tracking_display_location,
  call_view.type,
  call_view.start_call_date_time,
  call_view.end_call_date_time
FROM call_view
ORDER BY call_view.start_call_date_time DESC
