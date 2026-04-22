# ADR-002: Household ID Above User ID

Status: Accepted
Date: 2026-04-22
Owner: John / Housemate

## Context

Housemate is fundamentally a household product, not a single-user productivity app. Shared schedules, vendors, reminders, and property data need a common scope.

## Decision

Housemate is modeled household-first. Shared resources are scoped to `household_id`, while `user_id` handles attribution, membership, and personal preferences.

## Why

This aligns the schema with the actual customer problem and avoids a later household retrofit.

## Alternatives Considered

- single-user-first model with household features added later
- equal top-level treatment of household and user resources

## Consequences

This supports shared home management cleanly and preserves the future path to portfolio-level modeling.
