# ADR-001: GitHub Markdown Docs Are Canonical

Status: Accepted
Date: 2026-04-22
Owner: John / Housemate

## Context

Housemate product thinking had spread across local folders, `.docx` files, task notes, and ad hoc references. That made diffing, review, and decision tracking difficult.

## Decision

All living product, brand, roadmap, and architecture truth lives in Markdown inside the GitHub repo. Legacy `.docx` files are reference artifacts, not the primary source of truth.

## Why

Markdown in git is easier to diff, review, link, and keep consistent than parallel `.docx` sources.

## Alternatives Considered

- keep `.docx` as the primary source of truth
- maintain both `.docx` and Markdown as equal authorities

## Consequences

This makes GitHub the canonical workspace for humans and agents. `.docx` files can still exist, but they should be exports or legacy references, not the default place where new decisions are made.
