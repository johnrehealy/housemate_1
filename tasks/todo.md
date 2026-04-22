# Session Tasks

## Plan (2026-04-22 — Normalize source of truth and create phased roadmap)

Source hierarchy for this session:

1. `CLAUDE.md`
2. `tasks/todo.md`
3. `references/palette/Color-System.html`
4. Active source docs:
   - `references/legacy-docx/product/housemate_requirements_v1_2-2.docx`
   - `references/legacy-docx/engineering/housemate_tech_v0_9-2.docx`
   - `references/legacy-docx/strategy/housemate_strategy_v0.4-2.docx`
   - `references/legacy-docx/brand/housemate_brand_v0_8-2.docx`

Working goals:

- Create a canonical Markdown doc layer inside the Housemate workspace.
- Reconcile inconsistencies across strategy, brand, product, and architecture docs using the hierarchy above.
- Define how the CLAUDE folder should relate to GitHub going forward.
- Draft a phased walk-up plan from minimum lovable product to full vision.
- Prepare the project for later import into Linear.

Planned canonical docs:

- `docs/00-source-of-truth.md`
- `docs/01-product-strategy.md`
- `docs/02-brand.md`
- `docs/03-product-scope.md`
- `docs/04-technical-architecture.md`
- `docs/05-roadmap.md`

## In Progress

- [ ] Translate the refined Phase 1 MLP into concrete Linear projects and issues.

## Done

- [x] Prior session: propagated Ember Signal v1.5 palette truth across active files and prototype tokens.
- [x] Created canonical Markdown docs under `docs/` for source of truth, strategy, brand, scope, architecture, and roadmap.
- [x] Repointed `CLAUDE.md` to the canonical doc set and current legacy input file names.
- [x] Marked legacy `.docx` files as reference inputs rather than living truth.
- [x] Wrote the GitHub operating model recommendation: Markdown in-repo should become canonical, `.docx` export-only.
- [x] Drafted the phased walk-up plan from canonical foundation to full Housemate vision.
- [x] Added an initial Linear translation model to the roadmap.
- [x] Created the `housemate_1` GitHub repo scaffold as the new canonical source-of-truth base.
- [x] Imported the living Markdown docs, task files, palette reference, legacy `.docx` inputs, and helper script into the repo.
- [x] Updated internal doc paths so the repo is self-contained rather than pointing back to the old local workspace.
- [x] Refined Phase 1 around planning visibility for the primary household manager rather than AI orchestration.
- [x] Added Phase 1 architecture guardrails to protect durable domain modeling while keeping product scope narrow.
- [x] Added a shell maturity map so the full Housemate frame can ship in Phase 1 with selective depth by page.
- [x] Added a canonical decision log and first ADR set for key product and architecture decisions.

## Session Review

Prior session summary preserved here for continuity:

User delivered an updated palette spec as `references/palette/Color-System.html`. We found drift between the HTML spec, memory docs, and the UI prototype token layer. The active palette truth is now Ember Signal v1.5 with warm-tinted neutrals, Dusk dark surfaces, `#FFFFFF` on-sunset text, and the rose-to-orange agent gradient reserved for agent-present contexts. Older "Mint" wording in legacy docs should be treated as stale unless explicitly reconfirmed.

Current session summary:

We established a canonical Markdown product brain under `docs/` and updated `CLAUDE.md` so future sessions stop defaulting to stale `.docx` names or dead brand references. The current operating model is now explicit: use the CLAUDE folder as the local working homebase for now, but move the project into a real GitHub repo and keep Markdown as the living source of truth. The first execution decision still pending is narrower and more important than tooling: define the exact Phase 1 minimum lovable product boundary before creating Linear issues at scale.

GitHub move summary:

The empty `housemate_1` repo is now scaffolded as a clean docs-first source-of-truth base. The canonical docs, working task files, palette reference, legacy source `.docx` files, and migration helper script were copied in and repointed so the repo can stand on its own. The old local `Documents/.../CLAUDE/Housemate` workspace is now a secondary copy, not the primary truth.

Phase 1 refinement summary:

The MLP is now explicitly defined for the real first user: the household manager who already carries the coordination load. The first value is not AI orchestration; it is relief through visibility. The user signs up, loads existing vendors and maintenance cadence, sees the full plan for the specific house in a calendar view, and can set reminders easily. This reframes Housemate's first job from "automate the home" to "become the clean system of record for how this home runs."

Planning maturity summary:

The repo now captures the planning nuance we were missing: Phase 1 should ship the full Housemate shell, but not every page should be equally mature. We also now have explicit architecture guardrails and a real decision log so future design and build work can move faster without rediscovering why foundational choices were made.
