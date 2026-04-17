---
paths:
  - "domains/ops/social-automation/**"
---

# Social Automation — Operations Rules

## Domain
Automatización de interacciones sociales orgánicas en Instagram y Facebook. Actualmente solo para Discipline Rift (DR).

## Stack
Supabase Edge Functions (TypeScript / Deno), Supabase Postgres, Supabase Cron, Meta Graph API.

## Runtime model
Este sistema es event-driven y automático. Meta envía webhooks cuando hay comentarios. Las Edge Functions procesan y responden. Claude Code NO es el runtime de producción — es la herramienta de desarrollo y mantenimiento.

## Principles
- Event-driven: toda la lógica se dispara por webhooks o cron, nunca manualmente.
- Keyword matching: normalized whole-word match, case-insensitive.
- Dedup obligatorio: 1 reply máximo por usuario por post (key: `user_id + post_id`).
- Spam = no reply. Si el comentario no contiene keyword válida, se ignora.
- Rate limiting: respetar los límites de la Meta API. No enviar DMs en ráfagas.
- Signature validation: todo webhook POST debe validar `X-Hub-Signature-256` con el app secret.
- Storage first: loguear cada evento en Postgres antes de actuar. Si el DM falla, el evento queda registrado.
- No mutations en cuentas de ads: este dominio no toca campañas, ad sets, presupuestos ni creativos.

## Meta Platform Policy
- Private replies solo se permiten dentro de 7 días del comentario original.
- No enviar contenido promocional agresivo por DM sin opt-in previo.
- El mensaje debe ser relevante al comentario del usuario.
- Respetar las Community Standards de Meta.

## Brand rules (DR)
- Claridad primero, persuasión después.
- Lenguaje de padre, no de ego atlético.
- Local: Orlando, Florida.
- No usar: "next level", "elite", "serious athlete", "future champion".
- Oferta principal: on-campus, after-school, beginner-friendly, fun-first, coach-led.

## Separation from ads
Este dominio NO comparte nada con `domains/ads/meta/discipline-rift/`. Credenciales separadas, pipeline separado, skills separados (cuando se creen).
