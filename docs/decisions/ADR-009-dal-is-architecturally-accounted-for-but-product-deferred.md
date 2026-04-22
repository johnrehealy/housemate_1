# ADR-009: DAL Is Architecturally Accounted For But Product-Deferred

Status: Accepted
Date: 2026-04-22
Owner: John / Housemate

## Context

DAL remains central to the long-term moat, but including it in Phase 1 would overwhelm the first product loop.

## Decision

The data model and planning acknowledge future service connections and delegated access, but DAL is not built into the Phase 1 user-facing scope.

## Why

This preserves the future architecture without forcing early legal, trust, and implementation complexity into the first release.

## Alternatives Considered

- make DAL part of the first shippable product
- ignore DAL entirely until later

## Consequences

Phase 1 stays focused while later automation remains a clean extension path rather than a surprise retrofit.
