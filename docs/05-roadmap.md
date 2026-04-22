# Housemate Roadmap

Last updated: 2026-04-22

## Roadmap Principle

The roadmap should move from a minimum lovable homeowner loop to the full Housemate vision by adding trust, reliability, automation depth, and monetization in that order.

## Phase 0 — Canonical Foundation

Goal: clean source of truth, tighten scope, and define trust boundaries before product build.

Includes:

- canonical Markdown docs
- source-of-truth rules
- GitHub operating model
- phased roadmap
- explicit trust boundaries
- initial Linear structure design

Exit criteria:

- one authoritative doc set exists
- stale contradictions are resolved
- the MLP boundary is clear enough to defend

## Phase 1 — Minimum Lovable Product

Goal: give the household manager a clear operating picture of the home and a useful first planning tool, not a full automation layer.

Anchor user:

- existing homeowner
- primary household coordinator
- mid-30s mother of two
- already juggling vendors, maintenance cadence, and reminders manually

Candidate MLP outcome:

- user signs up
- property context is established for the specific house
- user loads existing vendors and recurring service cadence
- Housemate reflects that plan in a calendar view
- user sets reminders with very low friction
- user feels immediate relief because the home plan is finally visible and organized

Likely scope:

- onboarding with property context
- vendor list creation or import
- recurring cadence modeling
- a focused calendar / schedule surface
- a full shell with selective maturity across Home, Inbox, Schedule, Pros, Property, Payments, and Settings
- a dedicated Pros surface as part of the main nav
- basic reminders
- enough home memory structure to support future automation
- simple SMS-based edits to the plan of record

Deferred from Phase 1 unless required:

- AI orchestrator
- deep autonomous coordination
- inbox complexity
- broad DAL
- advanced vendor monetization
- portfolio management
- broad family-manager ambitions

Exit criteria:

- early users can successfully map their real home plan into the product
- the calendar view feels meaningfully more useful than their current ad hoc system
- reminders are easy enough to set that the plan becomes actionable
- users say some version of "I can finally see it all in one place"

## Phase 2 — Reliability And Habit Loop

Goal: make the planning layer dependable enough to become the household manager's default home operating system.

Includes:

- better status and summary surfaces
- stronger reminder reliability
- better editing and upkeep of cadence and vendors
- clearer audit trail and activity view
- cleaner failure handling
- stronger repeat usage patterns
- tighter onboarding-to-first-value path
- lightweight workflow support around overdue, upcoming, and seasonal items

Exit criteria:

- repeat use becomes visible
- time-to-first-useful-outcome falls materially
- support burden is understandable and manageable

## Phase 3 — Deeper Automation And Delegated Access

Goal: add true automation depth once the user already trusts Housemate as the system of record for the home plan.

Includes:

- AI orchestration where it clearly reduces work
- service connection model
- DAL consent flow
- per-site authorization
- JIT credential handling
- action-level permissions
- initial high-value delegated workflows

Exit criteria:

- DAL works on a narrow, defensible set of services
- users understand and trust the permission model
- the legal and support posture is explicit

## Phase 4 — Vendor Platform And Monetization Layer

Goal: introduce monetization that rides on homeowner trust and the household plan of record rather than weakening either.

Includes:

- attribution chain
- vendor placement controls
- quality floor enforcement
- basic vendor reporting
- recommendation-source governance

Exit criteria:

- placements can be measured without distorting recommendations
- quality controls are active
- vendor revenue is additive, not steering product truth

## Phase 5 — Portfolio / Multi-Property

Goal: expand the same operating model to property managers and small investors.

Includes:

- `portfolio_id` layer
- multi-property dashboard
- per-property attribution and activity views
- commercial packaging and pricing

Exit criteria:

- residential foundation is strong enough that the commercial wrapper is credible

## Phase 6 — Full Housemate Vision

Goal: move from home manager to broader household operating system only after trust is deeply earned.

Includes:

- broader automation coverage
- richer home memory
- deeper vendor ecosystem
- adjacent life-management expansion if justified

Exit criteria:

- Housemate has already won in home
- expansion feels earned, not opportunistic

## Recommended Next Practical Step

Before opening Linear in earnest, define the first build around Phase 1 and break it into 3-5 concrete workstreams:

- onboarding and household / property context
- vendor import and Pros experience
- cadence and calendar modeling
- reminders and status surfaces
- app shell and selective page maturity
- SMS command loop
- baseline analytics and billing

Linear should track execution of those workstreams after the scope line is stable.

## Linear Translation

Recommended Linear structure once the Phase 1 scope is approved:

### Initiatives

- Phase 0 — Canonical Foundation
- Phase 1 — Minimum Lovable Product
- Phase 2 — Reliability And Habit Loop
- Phase 3 — Delegated Access
- Phase 4 — Vendor Platform
- Phase 5 — Portfolio

### Phase 1 Projects

- Product Shell And Selective Maturity
- Onboarding And Household Context
- Vendor Import And Pros Experience
- Cadence And Calendar Modeling
- Reminders And Status Surfaces
- SMS Command Loop
- Billing And Baseline Analytics

### First Issue Groups

Use issue groups or labels to separate:

- product decisions
- design
- engineering
- copy and messaging
- instrumentation
- legal / trust review

### Important Rule

Linear should track execution work, not become the primary source of product truth. Decisions should still land in the Markdown docs first, then get converted into Linear issues.
