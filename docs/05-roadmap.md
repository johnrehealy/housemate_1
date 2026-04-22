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

Goal: deliver one complete homeowner loop that feels genuinely relieving, not merely promising.

Candidate MLP outcome:

- user signs up
- property context is established
- user adds or confirms one real vendor/service need
- Housemate sends or manages one useful reminder, follow-up, or coordination thread
- user feels Housemate reduced real cognitive load

Likely scope:

- onboarding with property context
- SMS-first interaction
- a lightweight Home briefing
- a narrow Inbox / action surface
- a focused Schedule or coordination flow
- basic reminders
- household memory for one real workflow

Deferred from Phase 1 unless required:

- broad DAL
- advanced vendor monetization
- portfolio management
- broad family-manager ambitions

Exit criteria:

- early users complete the loop
- users return because it helped, not because they were asked to explore
- the product reliably closes the thread on a narrow set of tasks

## Phase 2 — Reliability And Habit Loop

Goal: make the first loop dependable enough to become behavior.

Includes:

- better status surfaces
- stronger reminder reliability
- clearer audit trail and activity feed
- better failure handling
- stronger repeat usage patterns
- tighter onboarding-to-first-value path

Exit criteria:

- repeat use becomes visible
- time-to-first-automation or first-useful-outcome falls materially
- support burden is understandable and manageable

## Phase 3 — Deeper Automation And Delegated Access

Goal: add true automation depth once trust and core value are established.

Includes:

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

Goal: introduce monetization that rides on homeowner trust rather than weakening it.

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

- onboarding and property context
- messaging and follow-through loop
- reminders and status surfaces
- narrow coordination workflow
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

- Onboarding And Property Context
- Messaging And Follow-Through Loop
- Reminders And Status Surfaces
- Narrow Coordination Workflow
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
