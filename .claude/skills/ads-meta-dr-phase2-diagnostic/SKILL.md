---
name: ads-meta-dr-phase2-diagnostic
description: Analiza el batch más reciente de Meta Ads para Discipline Rift y genera un diagnóstico útil, aterrizado y accionable para una cuenta local y pequeña.
disable-model-invocation: true
---

# ads-meta-dr-phase2-diagnostic

Objetivo:
Analizar el batch más reciente de Meta Ads para Discipline Rift (DR) y generar un diagnóstico de valor real, no un reporte decorativo.

Este diagnóstico debe usar solo la data disponible en:
- `domains/ads/meta/discipline-rift/data/raw/`
- campaign insights
- adset insights
- ad insights
- ad insights by placement
- campaign objects snapshot
- adset objects snapshot

## Marco AI Playbook (obligatorio)
- Context engineering > prompt engineering.
- Usar estructura mental de **Role + Context + Task + Format**.
- Priorizar estrategia, signal quality, tracking y lectura de negocio sobre métricas de vanity.
- Si la data no soporta una conclusión, degradarla a **riesgo**, **hipótesis de validación** o **evidencia insuficiente**.
- No mezclar contexto irrelevante del negocio solo porque existe en otros documentos.
- El valor aquí no está en “sonar experto”, sino en detectar el cuello de botella real de una cuenta pequeña.
- Conectar pre-click performance con post-click reality siempre que aplique.
- No producir un “audit dump”; producir criterio útil para decisiones reales.

## Regla principal
No generar un reporte bonito.
Generar un diagnóstico útil para tomar decisiones reales en una cuenta pequeña de paid social.

## Contexto de negocio relevante para esta fase
- Discipline Rift (DR) es una marca local de youth sports en Orlando, Florida.
- No es una marca nacional ni multistate.
- El pagador es el padre / madre; el participante es el niño o niña.
- Público principal: padres de kids 6–12.
- La oferta principal que sí importa para esta fase es: programa / temporada deportiva after-school, on-campus, fun-first, beginner-friendly, coach-led.
- Lo que realmente vende DR se resume en 3 deliverables:
  1. On-campus convenience
  2. Beginner-friendly, safe-to-learn structure
  3. Trained coaches + clear season structure / Tier System
- “Confidence”, “friends”, “sportsmanship”, “respect” o “discipline” deben tratarse como support outcomes o byproducts, no como promesa principal, salvo que exista medición real.
- Si la garantía no está finalizada, no asumirla ni usarla en el análisis.

## Contexto que esta fase SÍ puede usar
- Geo real del negocio: Orlando.
- Parent payer + kid 6–12.
- Oferta principal actual.
- Los 3 deliverables de DR.
- Alineación o desalineación entre mensaje, setup y oferta real.

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
- Lead scoring o etapas de lead que los CSV no pueden demostrar.
- CRM follow-up cadence.
- SLA de respuesta.
- Teoría estratégica que no sea visible en los datos de la cuenta.

## Reglas permanentes
- No mutar campañas, ad sets, ads, budgets ni creatives.
- No asumir que CTR alto = éxito de negocio.
- No liderar el diagnóstico con métricas de vanity.
- No fingir que sabemos lead quality, CAC real, ROI o revenue final si esa data no está en los CSV.
- No sonar como consultor genérico.
- No forzar frameworks de escala si la cuenta todavía no está en etapa de escala.
- No repetir la data sin interpretación.
- Siempre aterrizar el análisis a decisiones reales.
- Si la evidencia no alcanza para una conclusión fuerte, decir “evidencia insuficiente” o “riesgo a verificar”, no inventar certeza.
- Tratar “geo no visible” como riesgo a validar en Ads Manager, no como hecho confirmado.
- No concluir que “creative no es el problema”; si solo hay un anuncio, decir explícitamente que no hay evidencia suficiente para evaluar creative de forma comparativa.
- Conectar siempre la lectura de performance con signal quality y post-click reality cuando aplique.
- No convertir esta fase en una fase de copywriting.
- No recomendar reestructuras grandes si primero no se resuelven setup, tracking o learning conditions.
- Never treat “LandingPageView” as the required pixel event name that must appear in Events Manager.
- When discussing LPV, always distinguish between:
  - base pixel validation = `PageView` firing correctly on the landing page
  - reporting / optimization validation = Landing Page Views populating in Ads Manager when traffic exists
- If `PageView` exists but LPV signal or reporting is still unclear, describe it as “LPV signal / reporting to validate,” not “broken pixel.”
- `ViewContent` may be useful if implemented, but it must not be treated as a required condition for LPV discussion.
- Do not present age bands, CTR, frequency, LPV cost, budget minimums, or audience size as universal hard thresholds.
- If heuristics are used, label them explicitly as directional heuristics for this account.
- When discussing learning conditions, use language such as “likely,” “unlikely,” “insufficient volume,” or “limited learning conditions” instead of absolute language.
- If the post-click journey has not been verified, elevate “landing page audit required” as a priority action instead of assuming the landing page is fine.

## Qué debe leer
Usar el batch más reciente disponible en:
`domains/ads/meta/discipline-rift/data/raw/`

Archivos requeridos:
- `meta_campaign_insights_*.csv`
- `meta_adset_insights_*.csv`
- `meta_ad_insights_*.csv`
- `meta_ad_insights_by_placement_*.csv`
- `meta_campaign_objects_*.csv`
- `meta_adset_objects_*.csv`

Si falta alguno, reportarlo claramente y continuar con lo disponible solo si el análisis sigue teniendo sentido.

## Qué tipo de diagnóstico debe producir
Este diagnóstico es de tipo:

**small-account traffic diagnosis**

Eso significa:
- leer setup
- leer targeting
- leer budget logic
- leer tracking risk / signal quality
- leer placement concentration / waste
- leer señal creativa básica
- leer coherencia entre objective, optimization y negocio
- terminar en acciones concretas

No significa:
- hablar como si hubiera evidencia de revenue o scale
- recomendar reestructuraciones enormes sin data suficiente
- inventar causalidad donde solo hay indicios
- redactar ad copy
- contaminar el análisis con school logic, franchise logic o growth-model logic

## Preguntas que sí debe responder
1. ¿La campaña está configurada con una lógica coherente para el negocio actual?
2. ¿El objective y el optimization event parecen razonables para la etapa actual?
3. ¿El ad set setup tiene sentido para una marca local de Orlando?
4. ¿El targeting parece demasiado estrecho, demasiado amplio o razonable?
5. ¿El gasto está demasiado concentrado en un placement?
6. ¿Hay placements que aparentan gastar sin devolver una señal suficiente?
7. ¿Hay suficiente creative diversity para aprender algo real?
8. ¿El diagnóstico apunta más a un problema de setup, tracking, placement o creative?
9. ¿Qué 3 a 5 acciones concretas se deberían considerar primero?
10. ¿Qué NO tiene sentido testear todavía con la data y setup actuales?
11. ¿Cuál debería ser el siguiente test correcto después de resolver el principal cuello de botella?
12. Is there an unverified landing page / post-click clarity risk that should be checked before stronger conclusions are made?

## Estructura exacta del output
Entregar exactamente estas secciones y ninguna más:

### A. Executive read
Explica en 1–2 párrafos:
- qué está pasando realmente
- cuál parece ser el principal problema o cuello de botella observable
- qué tipo de cuenta estamos viendo (cuenta pequeña / tráfico / aprendizaje / etc.)

### B. Campaign setup read
Analiza:
- objective
- status
- buying type
- si la campaña parece coherente con el negocio actual

### C. Ad set setup read
Analiza:
- optimization goal
- billing event
- budget logic
- targeting
- si la configuración parece razonable para Orlando / DR
- si hay señales de setup débil o setup aceptable

### D. Placement read
Usa el CSV de placement breakdown para responder:
- dónde se está yendo realmente el gasto
- qué placements dominan
- si la distribución parece sana o demasiado concentrada
- qué placements parecen winners, neutrals o likely waste
- no declarar waste absoluto sin contexto; usar lenguaje preciso

### E. Creative signal read
Usa `ad_insights` para leer:
- señal básica del anuncio actual
- dependencia excesiva en una sola pieza creativa
- si la cuenta tiene o no suficiente creative diversity para aprender
- si el siguiente paso debería ser creative testing o si todavía no tiene sentido testear creativos

### F. What the data does NOT tell us yet
Lista corta y explícita de lo que no sabemos todavía.
Ejemplos:
- lead quality
- conversion quality
- downstream funnel quality
- revenue
- CAC real
Solo incluir lo que realmente no está en la data.

### G. Priority actions
Dame 3 a 5 acciones concretas, en orden.
Deben ser accionables y realistas para una cuenta pequeña.
No meter 12 recomendaciones.
No sonar genérico.
Cada acción debe decir:
- qué revisar o cambiar
- por qué
- qué problema intenta resolver

Reglas adicionales para esta sección:
- At least one action may be a landing page audit if post-click clarity has not been verified.
- If a landing page audit is recommended, it should focus on:
  - mobile load / successful full load
  - above-the-fold clarity
  - sport clarity
  - age / parent fit clarity
  - Orlando / on-campus clarity
  - season / program framing clarity
  - CTA visibility
  - message match between ad and landing
- Do not use hard pass/fail thresholds as the basis for these actions unless the data clearly supports them.

### H. Next test logic
Explica:
- qué test sí tendría sentido hacer después
- qué condición previa debe resolverse antes de ese test
- qué test NO tiene sentido correr todavía

Also state explicitly whether a landing page audit is a required condition before stronger testing decisions are made.
Do not recommend deeper creative or audience testing as if post-click clarity were already confirmed when it has not been verified.

### I. Final call
Cierra con un párrafo corto que diga cuál es el siguiente foco real:
- setup
- tracking
- placement
- creative
- o una combinación de esos

## Formato de salida
Además de mostrar el diagnóstico en consola, guardar un archivo Markdown en:

`domains/ads/meta/discipline-rift/output/fase-2/`

Nombre:
`YYYY-MM-DD_meta_phase2_diagnostic.md`

Si la carpeta `output/fase-2/` no existe, crearla.

## Estilo obligatorio
- Directo
- Específico
- Nada de relleno
- Nada de “best practices” genéricas sin conexión con la data
- Nada de palabras lindas por sonar profesionales
- Mucho valor por línea
- Mucha precisión cuando la evidencia es débil

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

## Proceso sugerido
1. Detectar el timestamp más reciente compartido entre los CSV del batch.
2. Leer primero:
   - campaign objects
   - adset objects
3. Luego:
   - campaign insights
   - adset insights
   - ad insights
4. Finalmente:
   - placement breakdown
5. Cruzar setup + performance + placement antes de concluir.
6. Si una conclusión fuerte no está respaldada por la data, degradarla a “riesgo” o “hipótesis de validación”.
7. Escribir el markdown en `output/fase-2/`.
8. En consola devolver solo:
   - archivo generado
   - batch usado
   - principales hallazgos resumidos en bullets cortos