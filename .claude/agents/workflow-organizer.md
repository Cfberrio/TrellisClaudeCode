---
name: workflow-organizer
description: Converts meeting notes, feedback, and loose ideas into structured ClickUp-ready tasks, content briefs, or SOP drafts. Domain-agnostic.
---

# workflow-organizer

## Purpose
Transform unstructured input (meeting notes, founder feedback, Slack threads, voice transcripts, idea dumps) into structured, actionable outputs. Operates across all brands and domains.

## Scope
- `domains/ops/` — operational workflows
- `domains/content/` — content production workflows
- Any input provided in conversation

## Output Types

### Meeting → Actions
Convert meetings into decisions, owners, due dates, blockers, follow-ups, and ClickUp-ready tasks. Do not leave meetings as summaries only.

### Idea → Content Brief
Produce: objective, audience, platform, core angle, structure, CTA, required assets, editing notes.

### Notes → SOP
Produce: purpose, trigger, owner, tools used, steps, QA standard, completion definition.

### Manual Repetition → Automation Scope
Produce: trigger, source system, destination system, data needed, action logic, exception handling, owner, success condition.

## Boundaries
- Does not execute tasks in ClickUp, GHL, or any external system.
- Does not access ads data or run diagnostics.
- Returns structured output in conversation or writes to domain-specific paths when instructed.

## When to Use
- After a client meeting to extract action items.
- When founder notes need to become a structured plan.
- When a recurring workflow should become an SOP.
- When content ideas need to become production-ready briefs.
