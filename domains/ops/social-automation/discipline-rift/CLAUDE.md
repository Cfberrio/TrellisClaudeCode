# Discipline Rift — Social Automation Domain Context

## Scope
Este dominio controla la automatización de interacciones sociales orgánicas para Discipline Rift en Instagram y Facebook.

**Path:** `domains/ops/social-automation/discipline-rift/`

Este dominio pertenece a `ops/social-automation`, NO a `ads`. No comparte pipeline, scripts, skills ni credenciales con `domains/ads/meta/discipline-rift/`. Son dominios completamente separados:
- **ads/meta/discipline-rift** = extracción y diagnóstico de campañas publicitarias pagadas
- **ops/social-automation/discipline-rift** = automatización de respuestas orgánicas a comentarios, DMs y seguimientos

---

## Runtime model
El runtime de este sistema es **automático y event-driven**. No depende de ejecutar skills manualmente en Claude Code ni en Cursor.

El flujo real es:
1. Un usuario comenta en un post de Instagram o Facebook
2. Meta envía un webhook a una Supabase Edge Function
3. La Edge Function procesa el comentario, evalúa keywords y ejecuta la lógica
4. La acción resultante (DM, reply, log) ocurre automáticamente

Claude Code / Cursor sirve para **construir, mantener, debuggear y evolucionar** el sistema. No es el runtime de producción.

---

## Stack
- Supabase Edge Functions (TypeScript / Deno)
- Supabase Postgres (storage de eventos, keyword rules, logs)
- Supabase Cron (triggers periódicos para follow-up)
- Meta Graph API (webhooks de Instagram y Facebook)

---

## Phase 1 — Comment keyword automation

### Qué hace
Detecta keywords específicas en comentarios de posts de Instagram y Facebook y responde automáticamente vía DM privado con información relevante.

### Keywords activas
| Keyword | Respuesta esperada |
|---|---|
| COACH | Información sobre coaches y estructura del programa |
| PROGRAM | Detalles del programa, formato de temporada, qué incluye |
| LOCATION | Ubicaciones activas, escuelas participantes |
| SEASON | Fechas de la próxima temporada, registro |

### Reglas de matching
- Normalized whole-word match (case-insensitive, trimmed)
- 1 reply máximo por usuario por post (dedup por `user_id + post_id`)
- Si el comentario es spam o no contiene keyword válida: no reply
- Storage de cada evento en Supabase Postgres para auditoría

### Reglas de mensajería DR
- Claridad primero, persuasión después
- Lenguaje de padre, no de ego atlético
- Local: Orlando, Florida
- Oferta principal: on-campus after-school sports season
- Beginner-friendly, fun-first, coach-led
- No usar: "next level", "elite", "serious athlete", "future champion"
- No inventar claims que el negocio no mide

---

## Phase 2 — Follow-up engine (conceptual)
Motor de seguimiento automático para leads que interactuaron pero no convirtieron. Cron-driven. No implementado todavía.

## Phase 3 — Chatbot assistant (conceptual)
Asistente conversacional para DMs de Instagram. Responde preguntas frecuentes y redirige a registro. No implementado todavía.

---

## Operating rules
- Este dominio NO toca nada en `domains/ads/`
- Este dominio NO usa el `.env` del root del workspace
- Las credenciales viven en `domains/ops/social-automation/discipline-rift/.env`
- No crear lógica de producción sin tener las tablas de Supabase definidas primero
- No hacer deploy de Edge Functions desde Claude Code — usar Supabase CLI
