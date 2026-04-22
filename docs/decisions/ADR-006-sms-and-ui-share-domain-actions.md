# ADR-006: SMS And UI Share Domain Actions

Status: Accepted
Date: 2026-04-22
Owner: John / Housemate

## Context

Phase 1 includes a narrow SMS edit loop. If SMS and UI mutate data through separate code paths, the product will accumulate brittle behavior quickly.

## Decision

User actions performed through SMS and the app UI must resolve into the same backend domain actions. No duplicate mutation logic by channel.

## Why

This reduces tech debt and keeps the plan of record consistent regardless of how the user interacts with the product.

## Alternatives Considered

- build a separate SMS-specific mutation layer
- use UI actions as the only source of mutation in Phase 1

## Consequences

The backend action layer becomes a durable interface that later automation can also build on.
