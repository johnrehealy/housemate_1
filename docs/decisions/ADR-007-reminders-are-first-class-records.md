# ADR-007: Reminders Are First-Class Records

Status: Accepted
Date: 2026-04-22
Owner: John / Housemate

## Context

The Phase 1 relief moment depends on reminders being easy to create and trustworthy enough to matter.

## Decision

Reminders are modeled separately from calendar events so they can support channel, timing, delivery state, and later reliability instrumentation.

## Why

This matches the long-term reliability goals without requiring the full future notification system in Phase 1.

## Alternatives Considered

- store reminders as ad hoc event fields
- defer reminder modeling until after the calendar is built

## Consequences

Reminder behavior can evolve without restructuring the event model.
