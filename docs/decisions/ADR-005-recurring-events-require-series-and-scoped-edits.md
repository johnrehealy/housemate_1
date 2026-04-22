# ADR-005: Recurring Events Require Series And Scoped Edits

Status: Accepted
Date: 2026-04-22
Owner: John / Housemate

## Context

The home plan is built around recurring maintenance and service cadence. Users also need to change one occurrence without breaking the full series.

## Decision

Recurring household work is modeled with proper series support and scoped edits for single occurrence, this-and-following, and whole-series changes.

## Why

The legacy product docs explicitly call this expensive to retrofit. It is core to Schedule and SMS edit behavior.

## Alternatives Considered

- represent recurrence loosely in text or reminder rules
- defer scoped recurrence behavior until later

## Consequences

Phase 1 schedule editing becomes more structurally sound and can support later automation without a schema rewrite.
