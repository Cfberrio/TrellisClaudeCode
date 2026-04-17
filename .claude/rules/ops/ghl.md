---
paths:
  - "domains/ops/ghl/**"
---

# GHL (Go High Level) — Operations Rules

## Role
GHL is the CRM, funnel, follow-up, and conversion operations layer. Use for lead capture, nurture, stage logic, reminders, and pipeline handling.

## Principles
- The inbox runtime defaults to: AI drafts first, human review next.
- Lead-heavy workflows must prioritize speed, trust, logistics clarity, and booking movement.
- Operational emails and reminders should be clean and unambiguous.
- Do not build automations in GHL that duplicate what n8n already handles.

## Pipeline Logic
- Define clear stage transitions with trigger conditions.
- Every pipeline should answer: what triggers entry, what moves a lead forward, what triggers exit, what happens on stall.
