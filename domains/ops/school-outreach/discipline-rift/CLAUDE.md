# Discipline Rift — School Outreach Domain Context

## Scope
Este dominio maneja el pipeline de discovery, verificación y enriquecimiento de escuelas candidatas para el programa after-school de Discipline Rift en Orlando, Florida.

**Path:** `domains/ops/school-outreach/discipline-rift/`

Este dominio pertenece a `ops/school-outreach`. NO comparte datos, scripts ni credenciales con:
- `domains/ads/meta/discipline-rift/` — pipeline de paid ads
- `domains/ops/social-automation/discipline-rift/` — automatización de comentarios sociales

---

## Pipeline overview

El objetivo es construir una lista limpia, verificada y enriquecida de escuelas candidatas para hacer outreach directo del programa DR.

Flujo general:
```
Apify (raw school data)
  → Phase 1: Discovery + cleaning
  → Phase 2: Website verification
  → Phase 3: Enrichment + CRM import
```

---

## Phase 1 — Discovery

**Qué entra:** búsquedas de escuelas en el área objetivo (Orlando, FL) usando Apify como fuente principal. Puede incluir directorios de Google Maps, school finders, y búsquedas por distrito.

**Qué produce:**
- Lista raw de escuelas candidatas con campos mínimos: nombre, dirección, website, phone, tipo estimado
- Archivo de rechazadas con motivo de rechazo
- Output: `YYYY-MM-DD_dr_school_outreach_phase1_discovery.csv`

**Criterio de inclusión inicial:**
- Ubicación: Orlando, FL (radio razonable, confirmar en Phase 2)
- Tipo probable: elementary / lower school / K-5 / K-8 / PK-5 / PK-8
- Excluir: high schools, middle schools exclusivos, colegios, daycares sin grados K+

---

## Phase 2 — Website verification

**Qué valida:** para cada escuela candidata del output de Phase 1, verificar en el sitio web oficial:
- ¿Existe sitio web?
- ¿Sirve grados elementales / lower school? (K-5, K-8, PK-5, PK-8, o equivalente)
- ¿Es pública, privada o charter? (todos son válidos)
- ¿Tiene programa after-school propio que pueda ser competencia?

**Nota importante sobre emails:** los emails de contacto de directores o coordinadores muchas veces NO están publicados en el website. En la mayoría de los casos se obtienen por llamada directa a la escuela. No forzar la extracción de emails desde el website si no están disponibles — registrar el intento en `notes`.

**Output:** `YYYY-MM-DD_dr_school_outreach_phase2_verified.csv`
Campos adicionales: `website_confirmed`, `grades_served`, `school_type`, `has_competing_afterschool`, `contact_name`, `contact_email`, `contact_phone`, `verification_notes`

---

## Phase 3 — Enrichment + CRM prep

**Qué hace:**
- Enriquecimiento estadístico: matrícula estimada, tamaño de escuela, datos de distrito si disponibles
- Normalización de campos para importación a CRM
- Asignación de pipeline stage y score de prioridad
- Output final listo para importar

**Output:** `YYYY-MM-DD_dr_school_outreach_phase3_crm_ready.csv`

---

## Reglas operativas

1. **Preservar trazabilidad:** todos los outputs deben incluir `source_query`, `source_url`, y `notes`. Nunca borrar filas — mover rechazadas a archivo separado.
2. **No inventar datos:** si un campo no está disponible en la fuente, dejarlo vacío o marcar `N/A`. No asumir ni rellenar.
3. **Preferir fuente oficial:** sitio web de la escuela > directorio del distrito > Google Maps > directorios terceros.
4. **Outputs concisos:** sin análisis redundante. Cada output debe ser directamente utilizable o importable.
5. **Emails por llamada:** no bloquear el pipeline si el email no está en el website. Registrar `email_source: to_call` cuando aplique.
6. **Nomenclatura consistente:** `YYYY-MM-DD_dr_school_outreach_phase{N}_{descriptor}.csv`

---

## Formatos de output

| Fase | Archivo | Destino |
|---|---|---|
| Phase 1 | `YYYY-MM-DD_dr_school_outreach_phase1_discovery.csv` | `output/fase-1/` |
| Phase 2 | `YYYY-MM-DD_dr_school_outreach_phase2_verified.csv` | `output/fase-2/` |
| Phase 3 | `YYYY-MM-DD_dr_school_outreach_phase3_crm_ready.csv` | `output/fase-3/` |
| Rechazadas | `YYYY-MM-DD_dr_school_outreach_rejected.csv` | `output/fase-1/` o `fase-2/` según fase de rechazo |

---

## Campos mínimos esperados (todas las fases)

`school_name`, `address`, `city`, `state`, `zip`, `phone`, `website`, `school_type`, `grades_served`, `source_query`, `source_url`, `notes`, `rejection_reason` (si aplica), `status`
