# Social Automation — Discipline Rift (DR)

## Overview
Automatización de interacciones sociales orgánicas para Discipline Rift en Instagram y Facebook. Este dominio detecta keywords en comentarios de posts y responde automáticamente vía DM con información relevante del programa.

Este proyecto NO es parte del pipeline de ads. Vive en `domains/ops/social-automation/`, no en `domains/ads/`.

## Status: Scaffold (pre-implementation)

La estructura de carpetas y contexto están listos. No hay código de producción todavía.

---

## Target architecture

```
Instagram/Facebook comment
  ↓
Meta Webhook (HTTPS POST)
  ↓
Supabase Edge Function: meta-webhook
  ↓
  ├─ Validate signature (app_secret)
  ├─ Parse comment text
  ├─ Match keywords (COACH, PROGRAM, LOCATION, SEASON)
  ├─ Dedup check (user_id + post_id)
  ├─ Log event to Postgres
  └─ Send private reply via Meta API
```

El sistema corre automáticamente. No requiere intervención manual ni ejecución de skills. Meta envía webhooks en tiempo real cuando alguien comenta.

---

## Stack

| Component | Role |
|---|---|
| Supabase Edge Functions | Webhook receiver + business logic (TypeScript / Deno) |
| Supabase Postgres | Event storage, keyword rules, dedup tracking, logs |
| Supabase Cron | Triggers periódicos para follow-up engine (Phase 2) |
| Meta Graph API | Webhooks de comentarios + envío de DMs |

---

## Phases

| Phase | Name | Status |
|---|---|---|
| 1 | Comment keyword automation | **Scaffold ready** — pendiente implementación |
| 2 | Follow-up engine | Conceptual — solo placeholder |
| 3 | Chatbot assistant | Conceptual — solo placeholder |

---

## Directory structure

```
discipline-rift/
├── CLAUDE.md                          # Domain context
├── README.md                          # This file
├── .env.example                       # Credentials template
├── supabase/
│   ├── config.toml                    # Supabase project config
│   ├── functions/
│   │   ├── meta-webhook/index.ts      # Phase 1: webhook handler (placeholder)
│   │   ├── followup-engine/.gitkeep   # Phase 2: future
│   │   └── chatbot-assistant/.gitkeep # Phase 3: future
│   └── migrations/.gitkeep            # SQL migrations (future)
├── sql/.gitkeep                       # Ad-hoc queries, seeds, views
├── data/.gitkeep                      # Local debug exports
└── output/.gitkeep                    # Diagnostic outputs
```

---

## What's needed before Phase 1 implementation

1. **Supabase project creado** — URL, service role key, anon key disponibles
2. **Meta App configurada** — con Instagram Graph API y Webhooks habilitados
3. **Instagram Business Account** conectada a una Facebook Page
4. **Page Access Token** de larga duración con permisos:
   - `instagram_manage_comments`
   - `instagram_manage_messages`
   - `pages_messaging`
   - `pages_read_engagement`
5. **Webhook Verify Token** definido (string arbitrario para handshake)
6. **Tablas de Postgres** definidas: `comment_events`, `keyword_rules`, `dm_log`
7. **SQL migrations** escritas y aplicadas antes de deploy

---

## How to run (future)

### Local development
```bash
cd domains/ops/social-automation/discipline-rift/
cp .env.example .env
# Fill in real values
supabase functions serve meta-webhook --env-file .env
```

### Deploy
```bash
supabase functions deploy meta-webhook
```

### Testing webhook locally
```bash
# Use ngrok or Supabase's built-in tunnel for local webhook testing
```

---

## Relationship to other domains

| Domain | Relationship |
|---|---|
| `domains/ads/meta/discipline-rift/` | Same brand (DR), completely separate pipeline. Ads = paid campaigns. This = organic automation. |
| `domains/ops/ghl/` | Future: follow-up engine may feed leads into GHL pipeline |
| `domains/ops/clickup/` | Future: task creation from automation events |
