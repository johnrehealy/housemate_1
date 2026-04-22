# Housemate Product Scope

Last updated: 2026-04-22

## Scope Philosophy

Housemate should be built as a sequence of complete trust-building loops, not as a simultaneous rollout of every planned surface. The product is broad in vision but should be narrow in execution at each stage.

## Core Product Domains

The long-term product has six major domains:

1. Home briefing and agent status
2. Inbox and communication triage
3. Schedule and service coordination
4. Property memory and records
5. Permissions, settings, and notifications
6. Delegated access and deeper automation

## Core User Experience

The foundational experience is:

- a homeowner can text Housemate
- Housemate remembers context about the home
- Housemate helps coordinate a real home-management task
- Housemate follows through and closes the loop

If that loop is weak, adding more tabs will not fix the product.

## Locked Product Truths

### Home

- Home is a morning briefing, not a widget dashboard.
- The agent status line is the most important sentence in the product.
- Empty sections should stay hidden rather than render as empty shells.

### Inbox

- Inbox is triage-first.
- Desktop model is three-column.
- Tabs are: All, Agent, Action, Awareness, Archive.
- Threading is conversation-based, not workflow-based.

### Schedule

- Schedule is a personal superintendent's calendar.
- Manual event creation remains important even with automation.
- Color rules can become saved agent memory.
- Recurring-event note scope must be modeled correctly from day one.

### Settings

- Settings is a navigation destination, not a dumping ground.
- DAL management belongs in `Settings > Integrations`.
- Light/dark mode is controlled in nav chrome, not buried in Settings.
- Agent-initiated outreach and system notifications are distinct controls.

### Permissions

- Three-state model: Always allow / Ask me first / Don't do
- Permission defaults:
  - information retrieval -> Always allow
  - scheduling -> Ask me first
  - financial -> Ask me first
  - communication -> Ask me first

## What Is In Scope For The Minimum Lovable Product

The minimum lovable product should prove one tight homeowner loop:

- property-aware onboarding
- one clear communication channel
- one reliable workflow for vendor coordination or service follow-through
- reminders and status that reduce real cognitive load
- evidence that the agent can hold the thread

The MLP does not need the entire long-range system to exist.

## What Should Be Deferred

These belong after the first complete lovable loop unless proven necessary sooner:

- broad DAL coverage across many third-party systems
- sophisticated vendor monetization
- portfolio / multi-property management
- family-manager expansion
- overly broad analytics taxonomy
- feature-complete versions of every planned tab

## Operational Truth

The product promise is premium service, but the product risk is operational failure. Reliability, follow-through, reminders, and graceful recovery matter more than feature count.
