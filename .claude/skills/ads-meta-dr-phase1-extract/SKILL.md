---
name: ads-meta-dr-phase1-extract
description: Ejecuta la fase 1 de extracción read-only de Meta Ads para Discipline Rift a CSV.
disable-model-invocation: true
---

# ads-meta-dr-phase1-extract

Objetivo:
Extraer el decision pack mínimo de Meta Marketing API para Discipline Rift (DR) y guardar los resultados como CSV en `domains/ads/meta/discipline-rift/data/raw/`.

## Reglas permanentes
- Fase 1 es exclusivamente read-only.
- No mutar campañas, ad sets, ads, budgets ni creatives.
- Solo usar permiso `ads_read`. No usar `ads_management`.
- Guardar todos los CSV en `domains/ads/meta/discipline-rift/data/raw/`.
- Si una llamada falla, mostrar el error de Meta API y no improvisar.
- No imprimir tokens ni secretos completos en consola.
- Esta fase debe extraer solo data con valor para decisiones reales de creative, placement, targeting y setup.

## Resolución de variables
Las variables pueden venir en este orden:
1. `domains/ads/meta/discipline-rift/.env` — override local opcional
2. `.env` en el root del workspace — fuente principal por defecto

Variables requeridas:
- META_APP_ID
- META_APP_SECRET
- META_SYSTEM_USER_TOKEN
- META_AD_ACCOUNT_ID
- META_GRAPH_VERSION

## Decision pack mínimo requerido
La extracción debe generar exactamente estos outputs:

### Performance base
- `meta_campaign_insights_YYYYMMDD_HHMMSS.csv`
- `meta_adset_insights_YYYYMMDD_HHMMSS.csv`
- `meta_ad_insights_YYYYMMDD_HHMMSS.csv`

### Decision layers
- `meta_ad_insights_by_placement_YYYYMMDD_HHMMSS.csv`
- `meta_campaign_objects_YYYYMMDD_HHMMSS.csv`
- `meta_adset_objects_YYYYMMDD_HHMMSS.csv`

## Qué debe capturar cada output

### campaign insights
Campos mínimos:
- campaign_name
- spend
- impressions
- reach
- clicks
- ctr
- cpc
- cpm

### adset insights
Campos mínimos:
- campaign_name
- adset_name
- spend
- impressions
- reach
- clicks
- ctr
- cpc
- cpm

### ad insights
Campos mínimos:
- campaign_name
- adset_name
- ad_name
- spend
- impressions
- reach
- clicks
- ctr
- cpc
- cpm

Intentar incluir también, si están disponibles:
- actions
- cost_per_action_type
- outbound_clicks
- inline_link_clicks
- landing_page_views

### ad insights by placement
Usar breakdown de placement / publisher platform para entender dónde se está yendo el gasto.

Campos mínimos:
- campaign_name
- adset_name
- ad_name
- spend
- impressions
- reach
- clicks
- ctr
- cpc
- cpm
- placement breakdown fields

### campaign objects snapshot
Campos mínimos:
- id
- name
- status
- objective
- buying_type
- special_ad_categories

### adset objects snapshot
Campos mínimos:
- id
- name
- status
- optimization_goal
- billing_event
- daily_budget
- lifetime_budget
- targeting

## Ejecución

### Paso 1: Verificar variables
```bash
python3 -c "
from pathlib import Path
candidates = [
    Path('domains/ads/meta/discipline-rift/.env'),
    Path('.env'),
]
env_path = next((p for p in candidates if p.exists()), None)
if not env_path:
    print('ERROR: No .env found in domain or root')
    exit(1)
print(f'Using: {env_path}')
lines = env_path.read_text().splitlines()
env = {k.strip(): v.strip() for k, _, v in (l.partition('=') for l in lines if '=' in l and not l.startswith('#'))}
required = ['META_APP_ID','META_APP_SECRET','META_SYSTEM_USER_TOKEN','META_AD_ACCOUNT_ID','META_GRAPH_VERSION']
for v in required:
    val = env.get(v, '')
    print(f'{v}: SET ({len(val)} chars)' if val else f'{v}: MISSING')
"