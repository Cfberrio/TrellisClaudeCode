---
name: google-ads-phase1-extract
description: Monta y ejecuta la fase 1 de extracción read-only de Google Ads para OEV a CSV.
disable-model-invocation: true
---

# google-ads-phase1-extract

Objetivo:
Montar y ejecutar la fase 1 de extracción de Google Ads para OEV en este workspace, usando una capa read-only que exporte datos a CSV sin hacer reportes todavía.

## Reglas permanentes
- Fase 1 es exclusivamente read-only.
- No mutar campañas, conversiones, assets ni configuraciones.
- Guardar todos los CSV en `data/raw/`.
- Si una query falla, reducir complejidad antes de volver a intentar.
- No asumir que más conversiones = mejores conversiones.
- OEV prioriza corporate/workshops. `sit paid` es la north star conversion de negocio a futuro.

## Estructura requerida
Crear o verificar:
- `scripts/`
- `queries/`
- `data/raw/`
- `prompts/`
- `CLAUDE.md`
- `requirements.txt`
- `.env.example`

## Script principal
Crear `scripts/run_gaql.py` con estas reglas:
- usar `GoogleAdsClient.load_from_env()`
- aceptar `--query-file`
- aceptar `--out`
- aceptar `--customer-id` opcional
- ejecutar con `GoogleAdsService.SearchStream`
- aplanar cada row a un dict simple
- exportar CSV
- imprimir número de filas exportadas
- manejar errores con mensajes claros

## Queries de fase 1
Crear estas queries:
- `queries/campaigns_last_30_days.sql`
- `queries/pmax_asset_groups_last_30_days.sql`
- `queries/conversion_actions.sql`
- `queries/campaign_conversions_by_action_last_30_days.sql`
- `queries/campaign_search_terms_last_30_days.sql`
- `queries/landing_pages_last_30_days.sql`
- `queries/geographic_performance_last_30_days.sql`
- `queries/call_conversions_last_30_days.sql`

## Reglas de diseño para las queries
- Mantenerlas simples y compatibles con fase 1.
- Usar recursos adecuados por dataset.
- Incluir métricas base cuando apliquen:
  - impressions
  - clicks
  - ctr
  - average_cpc
  - cost_micros
  - conversions
  - conversions_value
  - segments.date (últimos 30 días)
- Si algún field rompe compatibilidad, removerlo y continuar.

## Recursos esperados
- campañas: `campaign`
- PMax: `asset_group`
- conversiones: `conversion_action`
- conversiones por campaña/acción: segmentado por `segments.conversion_action`
- search terms: `campaign_search_term_view`
- landing pages: `expanded_landing_page_view`
- geografía: `geographic_view`
- llamadas: `call_view`

## Output esperado
Al terminar la creación:
- muéstrame la ruta exacta del archivo creado
- confirma que existe `.claude/skills/google-ads-phase1-extract/SKILL.md`
- no ejecutes nada todavía
