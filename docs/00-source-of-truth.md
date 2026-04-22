# Housemate Source Of Truth

Last updated: 2026-04-22

## Purpose

This file defines which Housemate documents are authoritative, how conflicts are resolved, and how GitHub now functions as the canonical source of truth.

## Current Working Rule

This git repository is the canonical product brain for Housemate. Markdown files in this repo are the living documents. Older local workspace copies are now secondary and should not drift from this repo.

## Canonical Document Hierarchy

When documents disagree, resolve conflicts in this order:

1. `CLAUDE.md`
2. `tasks/todo.md`
3. `docs/00-source-of-truth.md`
4. `docs/01-product-strategy.md`
5. `docs/02-brand.md`
6. `docs/03-product-scope.md`
7. `docs/04-technical-architecture.md`
8. `docs/05-roadmap.md`
9. `references/palette/Color-System.html`
10. Active legacy `.docx` inputs:
   - `references/legacy-docx/product/housemate_requirements_v1_2-2.docx`
   - `references/legacy-docx/engineering/housemate_tech_v0_9-2.docx`
   - `references/legacy-docx/strategy/housemate_strategy_v0.4-2.docx`
   - `references/legacy-docx/brand/housemate_brand_v0_8-2.docx`

## Canonical Docs

The living Markdown set is:

- `docs/00-source-of-truth.md`
- `docs/01-product-strategy.md`
- `docs/02-brand.md`
- `docs/03-product-scope.md`
- `docs/04-technical-architecture.md`
- `docs/05-roadmap.md`
- `docs/06-phase-1-architecture-guardrails.md`
- `docs/07-shell-maturity-map.md`
- `docs/decision-log.md`

These files should be edited first. If a polished `.docx` artifact is still needed later, it should be generated from or manually synced to these Markdown docs, not the other way around.

## Legacy Inputs

The `.docx` files remain valuable as source material, but they are no longer the default living truth because:

- they contain stale version labels and older naming in places
- they are harder to diff and review
- they encourage duplicate truth across formats

Use them as reference inputs, not as the first place to make new decisions.

## Brand Truth

For brand tokens and palette rules, the authority is:

1. `docs/02-brand.md`
2. `references/palette/Color-System.html`

If an older doc still says "Mint" or uses cool-gray neutrals, that is stale unless explicitly reconfirmed.

## Product And Architecture Truth

For product and technical decisions, the authority is:

1. `CLAUDE.md`
2. `docs/03-product-scope.md`
3. `docs/04-technical-architecture.md`
4. `docs/05-roadmap.md`

## GitHub Operating Model

The operating model is now:

- GitHub is the single source of truth for docs and code.
- The Housemate working docs live inside the repo, not beside it.
- Markdown becomes canonical.
- `.docx` becomes export-only for investor, partner, or presentation artifacts.

Recommended structure once the repo exists:

```text
housemate/
  docs/
    00-source-of-truth.md
    01-product-strategy.md
    02-brand.md
    03-product-scope.md
    04-technical-architecture.md
    05-roadmap.md
  product/
  apps/
  packages/
```

## Operating Rules Going Forward

- Make new product, brand, and architecture decisions in Markdown first.
- Update `tasks/todo.md` before any non-trivial work session.
- Only update `.docx` files if there is a real external need.
- If GitHub and local docs diverge, GitHub should win once the repo exists.
- Do not maintain parallel "official" versions of the same strategy doc in both Markdown and `.docx`.

## Immediate Next Step

Refine the exact Phase 1 minimum lovable product boundary, then translate that scope into Linear. Linear should track execution, not hold the primary product logic.
