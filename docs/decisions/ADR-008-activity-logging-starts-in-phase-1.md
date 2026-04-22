# ADR-008: Activity Logging Starts In Phase 1

Status: Accepted
Date: 2026-04-22
Owner: John / Housemate

## Context

Even before full audit logging or DAL exists, Housemate benefits from a durable record of key user and system actions.

## Decision

Housemate records a durable action trail for key user and system actions from Phase 1 onward, even before full audit or DAL logging exists.

## Why

This supports debugging, trust, and future activity surfaces without requiring the full later-phase logging architecture.

## Alternatives Considered

- rely on raw analytics only
- defer activity logging until automation exists

## Consequences

The product gets a lightweight but durable operational history from the start.
