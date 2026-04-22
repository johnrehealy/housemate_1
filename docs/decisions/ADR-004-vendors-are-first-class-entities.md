# ADR-004: Vendors Are First-Class Entities

Status: Accepted
Date: 2026-04-22
Owner: John / Housemate

## Context

Vendors are central to the household operating plan. They appear in onboarding, cadence setup, calendar context, reminders, and future coordination.

## Decision

Vendors are durable records with stable IDs and are linked to households through a relationship model. They are not stored as plain text on events or notes.

## Why

This avoids fragile data modeling and supports future schedule, reminder, and communication features cleanly.

## Alternatives Considered

- store vendor names directly on events
- defer vendor modeling until later phases

## Consequences

Phase 1 can stay narrow while still building on a durable vendor foundation.
