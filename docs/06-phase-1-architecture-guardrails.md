# Phase 1 Architecture Guardrails

Last updated: 2026-04-22

## Purpose

Phase 1 is intentionally small in user-facing scope, but it must sit on top of domain primitives that can support later automation, delegated access, richer messaging, and portfolio expansion without forcing a rebuild.

## Core Principle

Build a narrow product on top of a durable model.

Do:

- keep the user-facing surface tight
- model the core household domain correctly
- share backend actions across UI and SMS

Do not:

- build future product surfaces too early
- fake the domain model with temporary hacks
- confuse a narrow Phase 1 with a disposable prototype

## Phase 1 User-Facing Scope

Phase 1 should let the primary household manager:

- sign up and establish the house context
- enter or import existing vendors
- define recurring service cadence
- see the household operating plan in calendar form
- set reminders easily
- text the agent to make simple updates to that plan

## Primary User

Existing homeowner who carries most of the household coordination burden.

Anchor persona:

- mid-30s mother of two
- existing homeowner
- already managing vendors, appointments, and reminders manually

## Phase 1 Relief Moment

`I can finally see the full operating plan for my house in one place, and I can keep it current without effort.`

## Durable Domain Primitives Required In Phase 1

### Households

The top-level shared scope. The product should not be built as single-user first.

### Household Members

Even if only one person uses it initially, roles must be modeled cleanly.

### Properties

The house needs a real model, even if Phase 1 only uses a subset of it.

### Vendors

Vendors must be first-class entities with stable IDs.

### Household-Vendor Relationships

The relationship between a household and a vendor is distinct from the global vendor record.

### Cadence / Service Plans

Recurring household work should be modeled explicitly.

### Calendar Events

Events must be real records, not derived on the fly from loose text.

### Recurring Series Model

Need a real series structure plus support for per-instance overrides.

### Reminders

Reminders should be their own records with channel and timing behavior.

### Activity Log

Key actions should be durably logged from day one.

### Messaging Command Layer

SMS should call shared domain actions, not mutate data via special-case code.

## Shared Domain Actions To Define Early

These do not have to be fancy, but they should be explicit and shared:

- `create_household_vendor`
- `update_household_vendor`
- `create_service_plan`
- `update_service_plan`
- `create_event`
- `move_event`
- `update_event_series`
- `mark_event_done`
- `create_reminder`
- `update_reminder`
- `get_upcoming_schedule`

The app UI and the SMS layer should both resolve into these same actions.

## Architectural Commitments To Lock Now

- `household_id` is the top-level shared scope
- `user_id` is subordinate for attribution and preferences
- `portfolio_id` can remain deferred functionally but should stay conceptually accounted for
- vendors are first-class entities
- recurrence is modeled properly
- reminders are separate from events
- event edits support scoped recurrence logic
- SMS and UI share the same backend mutation paths
- core objects have stable IDs and timestamps
- app objects are deep-linkable
- key actions are logged

## What Can Stay Thin In Phase 1

- auth UX sophistication
- member invite UX
- advanced analytics
- rich Home tab logic
- broad Settings surface
- polished Inbox architecture
- recommendation logic
- automation workflows

These can stay thin as long as the underlying model is sound.

## Explicit Deferrals

- DAL implementation
- AI orchestrator / multi-agent execution
- vendor outreach automation
- vendor portal
- broad recommendation engine
- full notification matrix
- external calendar write-back
- vendor monetization systems
- portfolio product behavior

## Tech Debt Red Flags

If we do any of these, we are taking the wrong shortcut:

- vendors stored as strings inside events
- recurrence stored as plain-English notes
- reminders stored as ad hoc fields on events without a model
- SMS edits implemented as separate data mutation code from UI edits
- no activity log
- single-user-first schema that later "adds" households
- calendar rendered from fragile front-end-only state with no durable event model

## Decision Test

Before any Phase 1 build decision, ask:

`Does this keep the product surface narrow while protecting the long-term domain model?`

If no, it is probably wrong.
