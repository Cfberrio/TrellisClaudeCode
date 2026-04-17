---
name: google-ads-phase3-campaign-rehab
description: Usa la data de fase 1, el diagnóstico de fase 2 y el feedback de negocio para generar un SOP manual, ultra específico y de alto valor, de qué cambiar dentro de la campaña actual de Google Ads para OEV.
disable-model-invocation: true
---

# google-ads-phase3-campaign-rehab

Objetivo:
Tomar el batch más reciente de fase 1, el último output de fase 2 disponible y el feedback de negocio ya definido para producir un SOP manual, ultra detallado y ejecutable, de qué cambiar dentro de la campaña actual de Google Ads para OEV.

## Prioridad de fuentes
Usar esta prioridad exacta para reducir gasto y evitar reconstruir desde cero:
1. último archivo en `output/fase-2/*.md`
2. último archivo en `output/fase-3/*.md` si existe
3. solo si falta algo importante, revisar `data/raw/`

No explorar el proyecto completo.
No usar Explore salvo que falte un archivo clave.
No releer todos los CSV si ya existe un output de fase 2.

## Contexto de negocio
- OEV NO es exclusivamente corporate/workshops.
- Corporate/workshops sigue siendo una prioridad fuerte, pero baby showers y otros personal events siguen aportando una parte material del ingreso.
- La cuenta actual tiene una sola campaña, así que esta fase debe mejorar esa campaña actual y no proponer una reestructura multi-campaign todavía.
- El problema principal actual es: asset quality / ad strength pobre, mezcla de intención y desperdicio por búsquedas irrelevantes.
- `deposit paid` es la north star conversion de negocio a futuro, pero no es el foco principal de esta fase.
- Weddings / Disney wedding y ciertos términos realmente fuera de categoría sí pueden mantenerse como off-target.
- Competitor conquesting es una jugada válida y no debe bloquearse por defecto.
- La audience strategy no puede ser solo business/professional; debe reflejar la mezcla real del negocio sin contaminar la señal.

## Reglas permanentes
- Esta fase no es analítica; es de implementación guiada.
- No des teoría general de Google Ads.
- No repetir el diagnóstico completo.
- No proponer muchas campañas nuevas todavía.
- No centrar esta fase en calls/offline conversion architecture.
- Priorizar cambios que puedan hacerse hoy dentro de la campaña actual.
- Si recomiendas algo, di exactamente dónde tocarlo dentro de Google Ads.
- Sé extremadamente específico.
- No ejecutes cambios automáticos.
- No uses MCP si no hace falta.
- No inventes assets ni decisiones sin explicar por qué.
- Si una recomendación depende de una decisión humana, dilo claramente.
- No tratar personal events rentables como basura automática.
- No bloquear competitors por defecto si la estrategia sí quiere aparecer en esas búsquedas.

## Archivos esperados
Leer en este orden:
- `output/fase-2/*.md`
- `output/fase-3/*.md`
Y solo si hace falta:
- `campaigns_last_30_days_*.csv`
- `pmax_asset_groups_last_30_days_*.csv`
- `conversion_actions_*.csv`
- `campaign_search_terms_last_30_days_*.csv`
- `landing_pages_last_30_days_*.csv`
- `geographic_performance_last_30_days_*.csv`
- `call_conversions_last_30_days_*.csv`

## Qué debe hacer
Generar un SOP manual para rehabilitar la campaña actual de PMax, protegiendo revenue lanes reales y cortando solo el desperdicio con alta certeza.

## Restricciones críticas
- Debe adaptarse a una sola campaña y al asset group actual.
- No debe asumir que ya existen múltiples asset groups.
- No debe hablar como consultor abstracto; debe hablar como operador que va a entrar a la UI.
- Debe priorizar acciones de esta semana.
- Debe decir qué NO tocar todavía durante el próximo ciclo de aprendizaje.
- Debe usar el lenguaje real del negocio OEV, no lenguaje genérico de venue.
- Debe evitar recomendaciones vagas como "mejora los assets" o "optimiza audiencias".
- Personal events rentables no deben bloquearse automáticamente.
- Debe respetar que competitor targeting no debe bloquearse por defecto si la estrategia sí quiere aparecer en esas búsquedas.

## Output requerido
Entregar exactamente estas secciones:

### A. Qué sí vamos a tocar ahora
Lista de 3 a 5 cambios que sí se harán esta semana.

### B. Qué NO vamos a tocar todavía
Lista corta de cambios que se posponen para fases futuras.

### C. Campaign Snapshot Used
- nombre exacto de la campaña actual
- nombre exacto del asset group actual
- ad strength / estado leído o asumido
- principal problema detectado
- principal oportunidad detectada

### D. Revenue Truth
Explica en 1 bloque corto:
- qué revenue lanes reales deben protegerse
- cuáles no deben bloquearse por error
- qué sí es claramente desperdicio

### E. Asset Group Rehab Plan
Explica paso a paso:
- cómo renombrar el asset group actual
- qué assets faltan exactamente
- cuántos headlines hacen falta
- cuántos long headlines hacen falta
- cuántas descriptions hacen falta
- si faltan imágenes, logos o video
- qué assets actuales probablemente deben reemplazarse
- cuál debe ser el enfoque dominante del asset group

Importante:
- el asset group no debe quedar framed como corporate-only si eso mata revenue real
- debe buscar una lógica hybrid demand limpia y útil

### F. Ready-to-Paste Messaging Pack
Dame assets listos para usar:
- 15 headlines sugeridos
- 5 long headlines sugeridos
- 5 descriptions sugeridas
- CTA direction
- business name guidance
- what to avoid

Todo aterrizado a OEV y a una estrategia hybrid demand:
- corporate/workshops
- private events de valor
sin convertirse en venue genérico barato.

### G. Negative Keywords Pack
Con base en los search terms reales, clasifica exactamente en 4 grupos:

#### 1. BLOCK NOW
Solo términos con alta certeza de irrelevancia o desperdicio.
Ejemplo: convention center / OCCC / términos claramente fuera de categoría.

#### 2. REVIEW FIRST
Términos que podrían tener valor dependiendo del revenue mix o de paquetes futuros.
Aquí deben caer:
- banquet hall / orlando banquet hall
- event planner / orlando event planner
- party house rentals
- team building activities
- otros términos similares si todavía pueden generar revenue o vendor-led packages

#### 3. DO NOT BLOCK BY DEFAULT
Incluye:
- competitor terms si la estrategia sí quiere aparecer en búsquedas de otros venues
- personal event demand que hoy sí aporta ingreso
- términos que mezclan corporate + private y todavía no se deben amputar

#### 4. CONQUESTING / MONITOR
Lista separada para competitor terms:
- no tratarlos como basura
- explicar cómo monitorearlos
- explicar cuándo sí valdría la pena bloquearlos más adelante

Incluye los términos concretos sugeridos, no solo categorías.

### H. Audience Signal Setup
Explica paso a paso:
- si conviene crear audience signal ahora o no
- cómo debería llamarse
- cómo construirlo de forma minimalista
- qué seed terms / URLs / audience ideas usar
- cómo reflejar hybrid demand sin contaminar la señal

La lógica debe respetar:
- menos señales, pero mejores
- no solo business/corporate
- no mezclar señales contradictorias sin justificación
- opcionalmente una segunda capa si realmente aporta valor claro

### I. Landing Alignment
Explica:
- si la homepage aguanta un poco más o no
- qué sección o landing hace falta después
- cuál debería ser la URL ideal para este asset group cuando exista
- qué mensaje debe reflejar esa página
- cómo alinear mejor corporate demand sin matar private event demand útil

### J. Exact Manual Checklist
Esto es lo más importante.
Dame una checklist secuencial, de principio a fin, para entrar a Google Ads y ejecutar los cambios.

Para cada paso, incluye:
1. pantalla o menú exacto a abrir
2. qué sección tocar
3. qué cambiar
4. qué guardar
5. qué validar antes de salir

No generalidades. Debe sonar como una guía de operación real.

### K. Revenue Protection Notes
Explica claramente:
- qué no bloquear por error
- qué revenue lanes se deben proteger
- qué decisiones pueden ser costosas si se implementan de forma demasiado rígida

### L. 14–21 Day Review Plan
Dime:
- qué NO tocar en el período de aprendizaje
- qué métricas revisar después
- qué señales indicarían que el rehab funcionó
- qué señales indicarían que hay que pasar a una fase más estructural

### M. Priority Final
Dame el orden exacto de implementación para esta semana.

## Restricciones finales
- No convertir esto en un reporte largo.
- No hablar demasiado de calls, CRM, GHL o deposit tracking en esta fase.
- Esta fase debe estar centrada en mejorar la campaña actual que ya existe.
- Debe ser realista para una cuenta pequeña y una sola campaña.
- Debe ser útil mañana mismo dentro de Google Ads.
- Debe generar valor operativo, no solo explicación.

## Guardado
- Guardar el output solo en Markdown dentro de `output/fase-3/`
- En consola mostrar solo:
  - archivos usados como fuente
  - si trabajó desde fase 2 / fase 3 previo o desde raw
  - ruta del archivo generado

Al final:
- confirma la ruta exacta del archivo generado
- confirma que sigue siendo una project skill
- no hagas nada más
