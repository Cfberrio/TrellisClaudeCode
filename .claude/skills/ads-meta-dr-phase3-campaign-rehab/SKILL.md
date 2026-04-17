---
name: ads-meta-dr-phase3-campaign-rehab
description: Usa el batch más reciente de Meta Ads para Discipline Rift y el diagnóstico de fase 2 para generar un SOP manual, específico y accionable de qué cambiar dentro de la campaña actual en Meta Ads.
disable-model-invocation: true
---

# ads-meta-dr-phase3-campaign-rehab

Objetivo:
Usar el batch más reciente de Meta Ads para Discipline Rift (DR) y el diagnóstico de fase 2 para generar un SOP manual, ultra específico y accionable de qué cambiar dentro de la campaña actual de Meta Ads.

## Marco AI Playbook (obligatorio)
- Context engineering > prompt engineering.
- Operar con estructura de **Role + Context + Task + Format**.
- El valor aquí no está en “escribir bonito”, sino en convertir diagnóstico en decisiones manuales de implementación.
- Priorizar estrategia, tracking, signal quality y learning conditions sobre recomendaciones vistosas.
- No mezclar contexto irrelevante del negocio.
- La IA no está aquí para “reemplazar criterio”; está aquí para traducir evidencia en una secuencia accionable.
- Conectar pre-click performance con post-click reality siempre que aplique.
- Favorecer los tests y cambios que tienen mayor impacto real sobre claridad, señal y capacidad de aprendizaje.

## Regla principal
Esto NO es un reporte.
Esto es un SOP manual de implementación.

## Contexto de negocio relevante para esta fase
- Discipline Rift es una marca local de youth sports en Orlando, Florida.
- No es una marca nacional ni multistate.
- La cuenta actual es pequeña y de bajo volumen.
- El objetivo no es impresionar con teoría sino mejorar el setup y la capacidad de aprendizaje real.
- El resultado debe servir para editar o reactivar la campaña actual con mejores fundamentos.
- Público pagador: padres de kids 6–12.
- La oferta principal relevante para esta fase es: programa / temporada deportiva after-school, on-campus, fun-first, beginner-friendly, coach-led.
- Lo que realmente vende DR se resume en 3 deliverables:
  1. On-campus convenience
  2. Beginner-friendly, safe-to-learn structure
  3. Trained coaches + clear season structure / Tier System
- “Confidence”, “friends”, “sportsmanship”, “respect” o “discipline” deben tratarse como support outcomes o byproducts, no como promesa principal, salvo que exista medición real.
- Si la garantía no está finalizada, no asumirla ni usarla.

## Contexto que esta fase SÍ puede usar
- Geo real del negocio: Orlando.
- Parent payer + kid 6–12.
- Oferta principal actual.
- Los 3 deliverables de DR.
- El diagnóstico más reciente de fase 2.
- Solo el contexto necesario para que el SOP sea más preciso y más útil.

## Contexto que esta fase NO debe usar
- Franchise / licensing / expansión.
- School pitch.
- School objections.
- School risk language.
- School proof kits.
- Money model DNA.
- Upsells.
- Continuity.
- Downsells.
- Home Playbook / Home Club / digital-lite offers.
- Lead scoring o etapas de lead que esta fase no puede validar.
- CRM follow-up cadence.
- SLA de respuesta.
- Revenue projections.
- Revenue protection notes.
- Messaging packs.
- Ready-to-paste ad copy.
- Headlines lists.
- Scripts completos.
- Cualquier sección extra que saque al output de su función central.

## Lo que esta fase sí debe hacer
- Decir qué cambiar ahora
- Decir qué NO cambiar todavía
- Priorizar setup y signal quality antes de escalar
- Traducir el diagnóstico a pasos manuales concretos en Meta Ads Manager
- Dar dirección creativa útil, no ad copy terminado al azar
- Decir cómo reactivar y qué observar después
- Incluir verificación explícita del post-click journey cuando haga falta
- Mantener el rehab enfocado en una secuencia pequeña de cambios de alto valor

## Lo que esta fase NO debe hacer
- No prometer escala con data insuficiente
- No inventar CAC, ROI ni revenue
- No forzar una reestructura gigante si no hay evidencia suficiente
- No proponer 20 cambios simultáneos
- No sonar como consultor genérico
- No generar un SOP bonito pero inútil
- No mezclar rehab con estrategia general de negocio
- No convertir esta fase en un deliverable de copywriting
- No recomendar lenguaje “elite”, “next level”, “compete”, “serious athlete” o “tryouts” salvo que el offer real activo lo justifique explícitamente
- Do not instruct the user to look for a required event literally called `LandingPageView` inside Events Manager.
- Do not present budget levels, CTR, frequency, LPV cost, audience seed size, or age ranges as hard pass/fail thresholds.
- If heuristics are used, label them as directional heuristics, not universal rules.
- Do not use absolute language such as “won’t learn,” “cannot learn,” or “must switch” unless the evidence is unusually strong.
- Do not assume the landing page is acceptable if post-click clarity has not been manually verified.

## Inputs esperados
Leer el batch más reciente desde:
`domains/ads/meta/discipline-rift/data/raw/`

Y también leer el diagnóstico más reciente desde:
`domains/ads/meta/discipline-rift/output/fase-2/`

Archivos esperados del batch:
- `meta_campaign_insights_*.csv`
- `meta_adset_insights_*.csv`
- `meta_ad_insights_*.csv`
- `meta_ad_insights_by_placement_*.csv`
- `meta_campaign_objects_*.csv`
- `meta_adset_objects_*.csv`

## Filosofía obligatoria
Este SOP debe seguir esta lógica:
1. Fix setup before scale
2. Fix signal quality before optimization
3. Fix learning conditions before over-testing
4. Use creative as a real lever, but only after the account can actually learn
5. Favor a small number of high-value changes over a long wish list
6. Verify post-click clarity before over-interpreting pre-click performance

## Preguntas que el SOP debe responder
1. ¿Qué cambios sí deben hacerse ahora mismo?
2. ¿Qué cambios NO deben hacerse todavía?
3. ¿Qué debe verificarse primero en Ads Manager antes de reactivar?
4. ¿Qué cambiar en campaña vs ad set vs ad?
5. ¿Qué hacer con geo?
6. ¿Qué hacer con Advantage+ Audience?
7. ¿Qué hacer con placements?
8. ¿Qué hacer con creative diversity?
9. ¿Qué hacer con pixel / LPV signal?
10. ¿Cómo reactivar la cuenta sin quemar presupuesto?
11. ¿Qué observar durante los siguientes 14 días?
12. ¿Qué test sí tiene sentido y cuál no?
13. ¿Hace falta un landing page audit antes de sacar conclusiones más agresivas o abrir nuevos tests?

## Estructura exacta del output
Entregar exactamente estas secciones y ninguna más:

### A. What we are fixing now
Lista corta de lo que sí se va a cambiar ya.

### B. What we are NOT fixing yet
Lista corta de lo que se pospone y por qué.

### C. Campaign-level decision
Explica si la campaña actual:
- se mantiene
- se reactiva
- se duplica
- o solo se ajusta

Con una recomendación clara y realista.

### D. Ad set rehab plan
Debe decir específicamente:
- qué validar en geo
- qué hacer con Advantage+ Audience
- qué hacer con optimization goal
- qué hacer con budget logic
- qué mantener
- qué cambiar

### E. Placement decision
Con base en placement breakdown:
- qué placements no se deben tocar todavía
- qué placements hay que vigilar
- si conviene o no intervenir manualmente ya
- cómo interpretar la concentración en Instagram Feed sin sobreconcluir

### F. Creative rehab plan
Debe decir:
- por qué el setup creativo actual no permite aprender
- cuántas variaciones mínimas crear
- qué tipo de variaciones crear
- qué NO hacer todavía
- qué tipo de hooks o angle testing sí tiene sentido
- cómo mantener el creative alineado con el offer real de DR

Restricciones obligatorias dentro de esta sección:
- NO escribir primary text completo
- NO escribir headlines
- NO escribir scripts
- NO escribir messaging packs
- NO inventar lenguaje de “elite / next level / tryouts” si no está en la oferta real activa
- Toda recomendación creativa debe anclarse a uno o más de estos 3 deliverables:
  1. On-campus convenience
  2. Beginner-friendly, safe-to-learn structure
  3. Trained coaches + clear season structure / Tier System

### G. Tracking / signal quality checks
This section must clearly distinguish between:
- base pixel validation
- LPV reporting / optimization validation
- post-click experience validation

It must tell the user to verify:
1. that the pixel is installed on the landing page
2. that `PageView` fires correctly when the landing page loads
3. that the correct landing page URL fully loads on mobile
4. that there are no obvious redirect, slow-load, or broken-page issues
5. that Landing Page Views can populate in Ads Manager once traffic is active
6. that any additional event such as `ViewContent` is treated as optional enhancement, not required proof of LPV

Rules for this section:
- Never tell the user that a literal `LandingPageView` event must appear in Events Manager.
- If `PageView` is firing but LPV signal is still uncertain, describe that state as “LPV reporting / optimization signal needs validation.”
- Keep the explanation practical and implementation-focused.

### H. Exact manual checklist
Esto es lo más importante.

Dame una checklist secuencial, manual, paso a paso, en orden:
1. qué abrir en Meta Ads Manager
2. qué revisar
3. qué cambiar
4. qué guardar
5. qué duplicar o no duplicar
6. cómo reactivar
7. qué no tocar todavía

Nada de generalidades.
Quiero instrucciones manuales concretas.

Before reactivation, the checklist must include a manual landing page audit covering:
- mobile full-load confirmation
- headline clarity
- sport clarity
- age / parent fit clarity
- Orlando / on-campus clarity
- season / program framing clarity
- CTA above the fold
- match between ad promise and landing page message

### I. 14-day observation plan
Dime exactamente qué mirar durante las siguientes 2 semanas después de reactivar:
- qué métricas sí revisar
- qué señales observar
- qué conclusiones NO sacar todavía
- cuándo sí tomar una nueva decisión

Do not use single hard pass/fail cutoffs for CTR, frequency, LPV cost, or spend.
Use directional patterns across 7–14 days and tie interpretation back to:
- setup quality
- signal quality
- creative clarity
- placement concentration
- landing page clarity

### J. Final call
Una conclusión corta con el foco principal:
- setup
- signal quality
- creative
- placement
- o combinación de esos

## Formato de salida
Además de mostrar el SOP, guardar un archivo Markdown en:

`domains/ads/meta/discipline-rift/output/fase-3/`

Nombre:
`YYYY-MM-DD_meta_phase3_campaign_rehab.md`

Si la carpeta `output/fase-3/` no existe, crearla.

## Estilo obligatorio
- Directo
- Específico
- Manual
- Sin relleno
- Sin consejos vacíos
- Mucho valor por línea
- Sin lenguaje inflado
- Sin parecer un deck de agencia
- Heuristic, not dogmatic
- Precise without pretending certainty
- Strategic without turning heuristics into rigid laws

## Heuristic language rule
When using operational benchmarks, treat them as directional heuristics for this account, not as universal platform laws.
If the evidence is weak, say:
- likely
- unlikely
- directional signal
- evidence insufficient
- needs validation

Avoid writing:
- always
- never
- guaranteed
- impossible
- must

unless the conclusion is directly supported by the available data or platform reality.

## Proceso de ejecución
Seguir este orden exacto:

### Paso 1: Detectar batch más reciente
```bash
ls domains/ads/meta/discipline-rift/data/raw/ | sort | tail -20
```

### Paso 2: Leer el diagnóstico de fase 2 más reciente
```bash
ls domains/ads/meta/discipline-rift/output/fase-2/ | sort | tail -5
```
Leer el archivo más reciente antes de proceder.

### Paso 3: Cruzar diagnóstico + setup + performance + placement
Antes de recomendar cambios, confirmar:
- qué es bloqueo de setup
- qué es bloqueo de signal quality
- qué es bloqueo de learning
- qué sí merece ajuste ahora
- qué se debe posponer
- qué parte del riesgo puede venir del post-click journey

### Paso 4: Escribir el SOP
Generar el markdown final en `output/fase-3/`.

### Paso 5: Responder en consola
Devolver solo:
- archivo generado
- batch usado
- 3 a 5 bullets con la lógica principal del rehab