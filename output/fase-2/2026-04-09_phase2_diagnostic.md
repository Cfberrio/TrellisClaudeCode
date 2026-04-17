# Phase 2 Diagnostic — OEV
**Fecha:** 2026-04-09
**Batch analizado:** 20260409_144111 (2026-03-15 → 2026-04-08, 25 días)
**Batch comparación:** 20260324_173331 (2026-03-15 → 2026-03-23, 9 días)
**Campaña:** Event Venue Orlando (ID: 23652899436)
**Rehab plan aplicado:** output/fase-3/2026-03-26_phase3_campaign_rehab_v2.md

---

## A. Executive Read

**Qué está pasando realmente:**
El rehab tuvo efecto visible. La cuenta pasó de 0 conversiones en los primeros 9 días (pre-rehab) a 13 conversiones en los 13 días post-rehab, con una mejora dramática en la calidad de las llamadas: de 2 llamadas con <80 segundos a 18 llamadas de las cuales 14 tienen duración significativa y 5 superan los 5 minutos. El asset group fue renombrado y casi con certeza se aplicaron las negativas de alta certeza (los términos de convention center cayeron de >100 impresiones en el período de marzo a 80 totales en 25 días).

Sin embargo, hay dos problemas abiertos que frenan el siguiente nivel:

1. **"booking_deposit_paid" está activo pero ha generado 0 conversiones atribuidas.** Las llamadas largas indican que hay conversaciones de venta reales, pero el depósito nunca se conecta como señal. Si los clientes están pagando el depósito por fuera del web flow (teléfono, transferencia, GHL), el algoritmo nunca aprenderá de esas conversiones.

2. **Waste residual activo:** "gathering place near me" ($14.38, 0 conv) es el término más caro del período. "orlando events & promotions" ($4.63) estaba en la lista BLOCK NOW y sigue activo. "orlando convention center" ($2.63) también persiste. No son catástrofes, pero son señales de que las negativas no se aplicaron al 100%.

**Principal problema:**
La señal de conversión está fluyendo por llamadas, pero no está conectada al depósito. Mientras "Calls from ads" sea la única señal contable, el algoritmo no puede optimizar hacia el comportamiento de mayor valor (quién paga el depósito, no solo quién llama).

**Principal oportunidad:**
13 conversiones en 13 días establece una base de señal real. Si se conecta el depósito — o al menos se mejora la calidad de la señal de llamada (duración mínima de conversión a 60s) — el algoritmo ya tiene suficiente historial para empezar a aprender en serio. El siguiente ciclo debe aprovechar esa señal antes de que el período de aprendizaje se resetee.

---

## B. Search Term Cost Map

### Comparación directa vs. marzo: Términos de waste

El mayor waste del diagnóstico de marzo era "orlando convention center" y variantes, con hasta 36 impresiones/día en un solo día y gasto sustancial. En el nuevo batch:

| Término waste | Batch marzo (9d) | Batch abril (25d) | Estado |
|---|---|---|---|
| orlando convention center (+ variantes) | ~$2.20+ en 9 días | $3.60 total en 25 días | Reducido, no eliminado |
| orange county convention center y variantes | Presente múltiples días | No aparece en top 50 | Efectivamente bloqueado |
| civic centers municipales | Presentes con impresiones | No aparecen | Bloqueados |
| disney wedding pavilion | 0 clicks | No aparece | Sin tráfico |

**Conclusión waste histórico:** Las negativas de alta certeza tuvieron efecto. OCCC y variantes desaparecieron casi por completo. "Orlando convention center" sigue con $3.60 total pero es residual comparado con lo que hubiera sido sin negativas en 25 días.

---

### Términos con mayor gasto en nuevo batch (top por costo agregado)

| Término | Gasto | Clicks | Impr | Conv | Diagnóstico |
|---|---|---|---|---|---|
| orlando event venue | $40.38 | 24 | 88 | **6** | Intención directa, señal real — PROTEGER |
| **gathering place near me** | **$14.38** | 1 | 1 | 0 | Ambiguo — puede ser Gathering Place (Tulsa, OK). INVESTIGAR antes de bloquear. Si es búsqueda del nonprofit, bloquear. |
| majestic orlando | $9.93 | 1 | 7 | **1** | Competitor (Majestic Event Center). Generó conversión — MANTENER activo |
| the celebration banquet hall | $9.39 | 2 | 14 | **1** | Era "REVIEW FIRST" en rehab plan. Generó conversión — MOVER A DO NOT BLOCK |
| event venues orlando | $7.91 | 4 | 24 | 0 | Intención válida, 0 conv — monitorear |
| the lair venue | $6.52 | 2 | 29 | 0 | Competitor. Alto CPC sin conv — evaluar en próximo ciclo |
| **orlando events & promotions** | **$4.63** | 1 | 8 | 0 | Estaba en BLOCK NOW. Término de promotor/organizador, no venue rental. Bloquear ahora. |
| repass locations | $3.35 | 1 | 2 | 0 | Nuevo. Repass = reunión post-funeral. Revenue lane real para venues — DECIDIR con operador |
| clubhouse for rent orlando | $3.21 | 2 | 7 | 0 | Gray area — venue similar a OEV. No bloquear por defecto |
| d space orlando | $3.02 | 2 | 13 | 0 | Competitor. En lista MONITOR. Sin conv pero razonable |
| **orlando convention center** | **$2.63** | 7 | 80 | 0 | Debía estar bloqueado. Waste residual. Confirmar negativa activa. |
| orlando banquet halls | $2.96 | 1 | 5 | 0 | Gray area — puede incluir corporate dinners |
| rental event space | $2.65 | 3 | 4 | 0 | Intención real — MANTENER |
| baby shower venues orlando | $1.94 | 2 | 11 | 0 | DO NOT BLOCK — revenue lane |
| birthday venues orlando | $2.22 | 1 | 2 | 0 | DO NOT BLOCK — revenue lane |
| venue near me | $1.78 | 1 | 11 | 0 | Intención directa — MANTENER |
| peerspace | $2.16 | 1 | 7 | 0 | Competitor. En lista MONITOR. CPC razonable |
| peerspace orlando | $1.45 | 1 | 23 | 0 | Mismo |
| casas de renta para fiestas | $1.61 | 1 | 2 | 0 | Estaba en BLOCK NOW — confirmar negativa activa |
| cheap small party venues in orlando fl | $2.36 | 1 | 3 | 0 | En "REVIEW FIRST" — sin conv, price-shopper profile |

### Nuevos patrones de intención

Términos nuevos que no aparecían en el batch de marzo:
- **"to rent a certain meeting room"** ($1.41) — posiblemente query asistida por AI. Intención de meeting room, relevante para OEV.
- **"repass locations"** ($3.35) — primer avistamiento. Repass/repast son reuniones post-funeral en un venue. Revenue lane real.
- **"estate rentals for events"** ($2.11) — intención de venue exclusivo para evento. Alta calidad de intención.
- **"legency event hall"** ($2.78) — competitor desconocido o mal-escrito. Monitorear.

### Términos con conversiones atribuidas (Calls from ads)

Solo 4 términos únicos tuvieron conversiones atribuidas en el batch:
1. `orlando event venue` — 6 conversiones (múltiples días)
2. `majestic orlando` — 1 conversión (competitor)
3. `the celebration banquet hall` — 1 conversión (competitor, era "review first")
4. Resto de conversiones sin término de search atribuido directamente (posiblemente display/YouTube surfaces de PMax)

---

## C. Current Structure Read

**Estructura confirmada:**
- 1 campaña PMax activa: "Event Venue Orlando" (ID: 23652899436)
- 1 asset group: **"OEV Event Bookers — Corporate & Private"** (ID: 6688507024, status=ENABLED)
  - Cambio confirmado vs. marzo: era "Asset Group 1"
  - Nombre elegido difiere del rehab plan ("Orlando Event Venue — Private & Corporate Events") pero refleja el mismo posicionamiento hybrid

**Qué cambió en la estructura:**
El rehab plan recomendaba renombrar el asset group. El nombre actual ("OEV Event Bookers — Corporate & Private") corresponde al nombre recomendado para el audience signal en la Sección H del rehab plan, no al nombre del asset group. Es posible que se hayan fusionado ambos en un solo nombre, lo cual es aceptable operativamente. Lo importante es que el asset group ya no se llama "Asset Group 1".

**PMax surfaces activas:**
El batch de landing pages muestra campaignid distintos al ID principal (23652899436): aparecen `23662973023`, `23662974871`, `23682688449`. Esto es comportamiento estándar — PMax crea sub-campañas internas para Search, Display, YouTube, Maps y Shopping. La estructura sigue siendo 1 campaña, 1 asset group.

**Estado de mezcla:**
Sin un segundo asset group, toda la intención (corporate + personal events + competitors) sigue bajo el mismo pool de assets. Dado que ahora hay conversiones, esto es manejable en este ciclo pero la separación seguirá siendo relevante a medida que el volumen aumente.

---

## D. Conversion Signal Audit

### Cambios en conversion actions vs. marzo

| Conversion Action | Status marzo | Status abril | Include in conv |
|---|---|---|---|
| Calls from ads | ENABLED | ENABLED | Sí |
| **orlandoeventvenue.org (web) booking_deposit_paid** | **No existía** | **ENABLED** | **Sí** |
| Purchase | ENABLED | ENABLED | Sí |
| Clicks to call | ENABLED | ENABLED | No (excluido) |
| Local actions | ENABLED | ENABLED | No (excluido) |
| orlandoeventvenue.org (web) purchase | REMOVED | REMOVED | No |

**Cambio crítico: "booking_deposit_paid" ahora existe y está activo.**
Esta es la conversión norte mencionada en el diagnóstico de marzo como la meta a largo plazo. No existía en el batch de marzo. Ahora está activa, habilitada, e incluida en el conteo de conversiones de la campaña.

### Señal dominante actual
- **Calls from ads**: 14 conversiones en el período (todas las conversiones del batch provienen de esta acción)
- **booking_deposit_paid**: 0 conversiones atribuidas — la acción existe pero no ha disparado

### Por qué booking_deposit_paid no ha generado conversiones

Tres hipótesis posibles:
1. El pixel/tag está implementado pero el flujo de pago en web no ha sido completado por ningún usuario (los clientes pagan vía otros medios — teléfono, transferencia, GHL)
2. El tag está mal configurado y no dispara aunque el depósito se complete en la web
3. El tag está correcto pero el volumen de bookings completados en web es genuinamente 0

La presencia de llamadas largas (hasta 9 minutos) sugiere que hay conversaciones de venta reales y potencialmente depósitos que se cierran — pero probablemente fuera del flujo web. Si ese es el caso, la señal de conversión más valiosa nunca llega al algoritmo.

**Qué falta:**
- Verificar si booking_deposit_paid dispara en el flujo web real (test de compra o revisión de tag manager)
- Si los depósitos se cierran por teléfono o manualmente, implementar conversiones offline importadas desde GHL con la fecha del depósito y el valor real

### Calidad actual de la señal "Calls from ads"

Con la configuración actual, "Calls from ads" cuenta cualquier llamada completada — incluyendo llamadas de 12 segundos que claramente no son ventas. Esto le da al algoritmo señal de baja calidad.

Distribución de duración de llamadas en el período:
- Pre-rehab (3/15-3/26): 6 llamadas, solo 2 >30 segundos (79s, 56s)
- Post-rehab (3/27-4/8): 18 llamadas, 14 >30 segundos, **5 >300 segundos (5 minutos)**

Las llamadas >5 minutos son casi con certeza conversaciones de venta reales: 568s (4/7), 539s (4/6), 527s (3/30), 445s (3/30), 433s (4/6).

**Acción recomendada:** Configurar un umbral de duración mínima en "Calls from ads" (mínimo 60 segundos) para eliminar llamadas triviales de la señal de conversión. Actualmente una llamada de 12 segundos cuenta igual que una de 9 minutos.

---

## E. Landing / Post-Click Read

**Páginas que reciben tráfico:**
Todo el tráfico orgina desde PMax y llega a variantes de `https://orlandoeventvenue.org` con parámetros de tracking automáticos (wbraid, gbraid, gad_source). No hay landing pages separadas.

**Cambios vs. marzo:**
Sin cambios estructurales en el destino. Misma homepage, mismas variantes de URL por superficie de PMax.

**Alineación actual:**
Los usuarios que generan llamadas de 5-9 minutos están llegando a la homepage y convirtiéndose. Esto confirma que la homepage no es el cuello de botella principal en este ciclo — el tráfico más relevante está convirtiendo.

**Gaps que se mantienen:**
1. No hay página `/corporate` ni ancla dedicada a corporate/workshops — sigue siendo la recomendación del siguiente ciclo, pero no es el bottleneck urgente ahora
2. No hay formulario de inquiry rastreable — "booking_deposit_paid" parece ser el primer punto rastreable, pero si el flujo nunca se usa, la señal no llega
3. No hay landing específica para "team off-sites" o "workshops" aunque esos términos tendrían alta intención si aparecieran

---

## F. Restructuring Proposal

### Qué mantener (sin cambios)
- La campaña PMax activa con el historial acumulado de 14 conversiones
- El asset group único "OEV Event Bookers — Corporate & Private" — no tocar mientras se está en la fase de aprendizaje activo
- Competitor terms activos (Peerspace, The Abbey, etc.) — la conversión atribuida a "majestic orlando" confirma que vale la pena mantenerlos
- Personal event terms activos — baby shower y birthday siguen generando tráfico legítimo sin señal negativa

### Qué ajustar en el próximo ciclo (sin crear estructura nueva)
- Threshold de duración mínima en "Calls from ads" → 60 segundos
- Agregar las 3-4 negativas que no se aplicaron o se cayeron ("orlando events & promotions", confirmar "casas de renta", confirmar "orlando convention center")
- Investigar "gathering place near me" — si es el Gathering Place de Tulsa, bloquear

### Qué separar cuando haya 20+ conversiones totales
- Un segundo asset group para corporate/workshops con landing dedicada — aún no es el momento, pero la base de señal ya está cerca del umbral mínimo para hacerlo de forma informada
- Potencialmente un tercer asset group para personal events de alto valor si los datos de cierre confirman que representan >30% del ingreso

### Enfoque para el siguiente ciclo
**Conectar la señal de depósito.** El trabajo de estructura está avanzado. El gap principal ahora es de señal, no de arquitectura. Si el algoritmo puede aprender de quién paga el depósito (no solo quién llama), el CPA mejora y el gasto se concentra en usuarios con mayor intent de cierre.

---

## G. Priority Actions

**1. Verificar e implementar negativas faltantes (15 min)**
- "orlando events & promotions" — estaba en BLOCK NOW, sigue activo ($4.63 gasto)
- "orlando convention center" — confirmar que la negativa existe y tiene el formato correcto (broad match sin comillas)
- "gathering place near me" — investigar: si es búsqueda del Gathering Place (Tulsa, OK) → bloquear; si es intención genérica de venue → dejar
- "casas de renta para fiestas cerca de mi" — confirmar negativa activa

**2. Conectar booking_deposit_paid con el flujo real de depósito (mayor impacto a mediano plazo)**
- Verificar si el tag dispara cuando un usuario completa el pago en la web
- Si los depósitos se cierran por GHL o manualmente: configurar conversión offline importada en Google Ads desde GHL con fecha y valor del depósito
- Este es el cambio de mayor impacto para el siguiente ciclo — es lo que convierte señal telefónica en señal de revenue real

**3. Aumentar duración mínima de "Calls from ads" a 60 segundos**
- Ir a: Google Ads → Tools → Conversions → Calls from ads → Edit settings
- Cambiar "Call length" threshold de lo que sea actualmente a **60 seconds**
- Esto elimina las llamadas de 12-22 segundos (que claramente no son ventas) del conteo de conversiones, mejorando la pureza de la señal

**4. Mover "the celebration banquet hall" a DO NOT BLOCK activo (confirmación)**
- Fue en la lista "REVIEW FIRST" del rehab plan de marzo
- Generó 1 conversión en este período con $9.39 de gasto
- Confirmar que no está en ninguna lista de negativas y dejarlo activo intencionalmente

**5. Decidir sobre "repass locations" con el operador**
- Nuevo término: repass/repast = reunión post-funeral en venue (~$3.35, 1 click, 0 conv)
- Si OEV acepta estos eventos, es un revenue lane legítimo con baja competencia online
- Si no, bloquear el término: "repass," "repast," "repass locations," "repast venues near me"

---

## Apéndice — Comparación de métricas directa

| Métrica | Batch marzo (3/15–3/23, 9d) | Post-rehab (3/27–4/8, 13d) | Delta |
|---|---|---|---|
| Costo diario | $16.03 | $17.04 | +6.3% |
| Clicks diarios | 21.4 | 16.3 | −24.0% |
| CPC promedio | $0.75 | $1.04 | +39.7% |
| CTR | 3.6% | 3.1% | −12.1% |
| Conversiones | **0** | **13** | +∞ |
| Costo por conversión | N/A | **$17.04** | — |
| Llamadas significativas (>30s) | 2 | 14 | +600% |
| Llamadas >5 min | 0 | 5 | — |

**Nota sobre las métricas negativas (CPC, CTR, clicks diarios):**
Los tres bajaron relativos al período de marzo, pero eso era el objetivo. El batch de marzo tenía alto tráfico de convention centers — impresiones baratas de usuarios sin ninguna posibilidad de convertir. Eliminar ese tráfico sube el CPC promedio (ahora el gasto restante va a usuarios más costosos y más relevantes) y baja el CTR (menos clics de baja calidad). La señal real de si el rehab funcionó es el resultado de conversión, no el CTR.

**Advertencia sobre el período:**
La comparación no es apples-to-apples perfecto: periodos distintos, estacionalidad semanal diferente, y el volumen post-rehab incluye el período mientras las negativas comenzaban a tener efecto. Las tendencias son suficientemente fuertes para tener confianza en la dirección (especialmente en conversiones y calidad de llamadas), pero no son conclusivas para declarar una tasa de mejora exacta.
