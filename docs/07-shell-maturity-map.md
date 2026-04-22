# Phase 1 Shell Maturity Map

Last updated: 2026-04-22

## Principle

The full Housemate shell exists in Phase 1, but not all surfaces carry the same depth. The shell should already communicate the full product vision, while depth is concentrated where first value lives.

## Top-Level Shell In Phase 1

- Home
- Inbox
- Schedule
- Pros
- Property
- Payments
- Settings
- Agent entry point / SMS continuity

## Tier 1 — Deep Surfaces

These carry the actual Phase 1 value.

### Onboarding

Needs to feel real and polished.

Includes:

- signup / auth
- household setup
- property / address capture
- vendor import or entry
- cadence setup starter flow

### Schedule

One of the deepest pages in Phase 1.

Includes:

- real calendar views
- recurring events
- event detail / edit
- reminders
- vendor linkage
- visible plan-of-record feel

### Pros

Also a deep page in Phase 1.

Includes:

- vendor roster
- vendor detail pages or cards
- category
- contact details
- associated cadence / services
- quick way to edit relationship details
- visible connection to schedule and reminders

### Reminders

May live inside Schedule and Settings rather than as standalone nav.

Must feel real:

- create / edit reminder
- attach to event or series
- clear lead time and channel behavior

### SMS Edit Loop

Not a page, but a deep product surface.

Includes:

- narrow command support
- shared backend action path
- confirmation replies
- visible reflection in Schedule and Pros context

## Tier 2 — Medium Surfaces

These should feel intentional and useful, but not overbuilt.

### Home

Should feel polished and credible.

Includes:

- upcoming events
- reminders coming soon
- setup gaps or prompts where useful
- maybe one simple summary or status line

Not yet:

- full intelligence layer
- rich prioritization engine
- heavy activity logic

### Property

Useful, but not yet deep.

Includes:

- house basics
- service categories or home summary
- relationship to vendors and cadence where useful

Not yet:

- full asset intelligence
- deep memory layer
- advanced property recommendations

### Settings

Focused, not broad.

Includes:

- profile / household basics
- reminder defaults
- basic preferences
- SMS preferences

Not yet:

- full settings universe
- deep DAL permissions
- advanced notification matrix

## Tier 3 — Thin But Present

These should exist in the shell, but be intentionally light.

### Inbox

Exists because it is part of the eventual product language.

In Phase 1 it can be:

- agent confirmations
- reminder notices
- SMS history / message transcript
- light organization

Not yet:

- full triage architecture
- advanced filters / search
- rich multi-channel communications product

### Payments

Exists, but thin.

Can include:

- subscription / billing basics
- future-facing vendor payment area if needed

Not yet:

- payment workflows
- waterfall logic
- advanced transaction handling

## Tier 4 — Present As Intentional Stubs

These can exist as shell-level placeholders or partial settings destinations.

### Integrations / DAL

- visible enough to signal future direction
- not functionally built

### Advanced Notification Controls

- maybe placeholder or thin scaffolding
- not deeply configurable yet

### Automation Controls

- not a Phase 1 depth area

## What "Good Enough" Means Per Tier

### Deep

A user could reasonably use this as the product's core value surface.

### Medium

A user understands why it exists and gets light utility from it.

### Thin

The page is real and coherent, but clearly not where the current product depth lives.

### Stub

The page signals direction without pretending full functionality exists.

## Design Order

1. shell and navigation system across all top-level pages
2. deep surfaces:
   - onboarding
   - Schedule
   - Pros
   - reminders
   - SMS-connected edits
3. medium surfaces:
   - Home
   - Property
   - Settings
4. thin surfaces:
   - Inbox
   - Payments

## Core Behavioral Signals To Track

- signed up
- completed household setup
- added first vendor
- added second vendor
- created first recurring cadence
- viewed populated Schedule
- opened Pros page after setup
- created first reminder
- sent first SMS edit
- SMS edit success
- returned within 7 days
