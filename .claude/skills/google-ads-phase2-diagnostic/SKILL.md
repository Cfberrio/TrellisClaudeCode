---
name: google-ads-phase2-diagnostic
description: Analiza el batch más reciente de CSV de Google Ads para OEV y genera un diagnóstico con propuesta de reestructuración.
disable-model-invocation: true
---

# google-ads-phase2-diagnostic

Objetivo:
Leer el batch más reciente de CSV extraídos en fase 1 y producir un diagnóstico operativo con propuesta de reestructuración para OEV.

## Contexto de negocio
- OEV prioriza corporate/workshops.
- El negocio no debe optimizarse hacia leads genéricos baratos.
- `deposit paid` es la north star conversion de negocio a futuro.
- La cuenta actual puede tener solo una campaña, así que el análisis debe adaptarse a una estructura mínima y no asumir múltiples campañas complejas.
- Personal events / celebrations son un path secundario al posicionamiento principal.

## Reglas permanentes
- Fase 2 es análisis, no implementación.
- No mutar campañas, conversiones, assets ni configuración.
- No proponer cambios "por intuición" sin apoyarse en los CSV.
- No asumir que más conversiones = mejores conversiones.
- Priorizar signal quality, search intent, structure quality y post-click fit.
- Si un CSV falta, dilo claramente y continúa con lo disponible.
- Si un CSV está vacío, dilo claramente y no inventes conclusiones.

## Archivos esperados
Buscar en `data/raw/` el batch más reciente de:
- campaigns_last_30_days_*.csv
- pmax_asset_groups_last_30_days_*.csv
- conversion_actions_*.csv
- campaign_conversions_by_action_last_30_days_*.csv
- campaign_search_terms_last_30_days_*.csv
- landing_pages_last_30_days_*.csv
- geographic_performance_last_30_days_*.csv
- call_conversions_last_30_days_*.csv

## Qué debe hacer
1. Identificar el timestamp más reciente disponible en `data/raw/`.
2. Leer los CSV correspondientes a ese batch.
3. Diagnóstico de:
   - structure
   - search intent
   - conversion signals
   - landing page fit
   - geography / call signals
4. Generar una propuesta de reestructuración, no implementación.

## Output requerido
Entregar exactamente estas secciones:

### A. Executive Read
- qué está pasando realmente
- principal problema
- principal oportunidad

### B. Search Term Cost Map
- términos más relevantes
- términos más caros
- términos con intención corporate/workshop
- términos genéricos o de baja calidad
- patrones claros de desperdicio o oportunidad

### C. Current Structure Read
- qué estructura existe hoy
- qué papel está jugando PMax / asset groups
- si la cuenta está demasiado mezclada o no

### D. Conversion Signal Audit
- qué conversion actions existen
- cuál parece ser la señal dominante hoy
- qué falta para alinear mejor la cuenta con `deposit paid`

### E. Landing / Post-Click Read
- qué páginas reciben tráfico
- si el tráfico parece bien alineado con el destino
- qué gaps de landing page son evidentes

### F. Restructuring Proposal
- qué mantener
- qué separar más adelante
- qué enfoque debe dominar
- qué tipo de estructura recomendarías para la siguiente fase
- no implementar todavía

### G. Priority Actions
- 3 a 5 acciones prioritarias
- ordenadas por impacto

## Restricciones
- No des teoría general de Google Ads.
- No hagas un reporte "bonito" vacío.
- No escribas demasiado.
- Sé concreto, apoyado en datos.
- Si hay solo una campaña, el diagnóstico debe adaptarse a eso y no forzar un framework multi-campaign.
- No ejecutes cambios.
- No uses MCP si no hace falta.

## Output al finalizar

Al terminar el diagnóstico, hacer lo siguiente en este orden:

### 1. Guardar el documento completo en Markdown
Determinar la fecha actual en formato YYYY-MM-DD.
Guardar el documento completo (todas las secciones A–G) en:
`output/fase-2/YYYY-MM-DD_phase2_diagnostic.md`

El archivo debe comenzar con este frontmatter:
```
# Phase 2 Diagnostic — OEV
**Fecha:** YYYY-MM-DD
**Batch analizado:** [timestamp del batch]
**Campaña:** [nombre exacto]

---
```

Seguido del contenido completo de todas las secciones.

### 2. Mostrar resumen en consola
Imprimir solo esto en la conversación (no el documento completo):
- Timestamp del batch analizado
- Campaña analizada
- Principal problema detectado (1 línea)
- Principal oportunidad detectada (1 línea)
- Sección G: Priority Actions (lista corta)
- Ruta del archivo generado: `output/fase-2/YYYY-MM-DD_phase2_diagnostic.md`
