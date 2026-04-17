# GHL (Go High Level) — Domain Context

## Status
Scaffold stage. No active integration yet.

## Role
GHL is the CRM, funnel, follow-up, and conversion operations layer. Use for lead capture, nurture, stage logic, reminders, and pipeline handling.

## Purpose
When activated, this domain will handle:
- Lead capture and pipeline management
- Funnel building and optimization
- Follow-up sequence automation
- Booking and payment flow operations
- Inbox runtime (AI drafts first, human review next)

## Brand Applications
- **OEV / RV**: inquiry flow, booking pipeline, reminders, fast-response operational messaging
- **DR**: ad-to-lead funnel follow-up, recruiting pipeline
- **CTS**: inquiry and conversion support for catering/events

## Principles
- Prioritize speed, trust, logistics clarity, and booking movement.
- Operational emails and reminders must be clean and unambiguous.
- Define clear pipeline stages: entry trigger, forward trigger, exit trigger, stall handler.
- Do not build automations in GHL that duplicate what n8n handles.
