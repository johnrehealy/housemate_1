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

- a household manager can sign up and orient Housemate around a specific home
- Housemate can ingest existing vendors and maintenance cadence
- Housemate can reflect that plan in a calendar view that makes the home's operating rhythm visible
- Housemate can help the user set reminders so the plan becomes usable, not just documented
- Housemate can support simple SMS-based updates so the plan stays current without app friction

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

The minimum lovable product should prove one tight homeowner loop for a very specific user:

- primary user: an existing homeowner who carries most of the household coordination burden
- anchor persona: mid-30s mother of two who already manages the home's vendors, schedules, and reminders manually

The Phase 1 job to be done is:

- "Show me the full plan for my specific house, with my real vendors and cadence, in one place."

The Phase 1 relief moment is:

- the user signs up
- loads existing vendors and recurring service cadence
- sees the house's full operating plan reflected in a calendar view
- can easily add reminders so nothing important is easy to miss

This is intentionally not an AI-orchestration-first product. Phase 1 is about identifying the need, organizing it cleanly, and showing a credible path toward a smarter future product.

Phase 1 in-scope capabilities:

- property-aware onboarding
- vendor import / entry for the household's real service providers
- recurring service cadence entry and editing
- calendar visualization of the home's existing plan
- a full product shell with selective maturity by page
- a dedicated Pros surface as part of the Phase 1 shell
- reminder setup that makes the calendar operationally useful
- enough structure to make future automation believable
- simple SMS edits to the plan of record

Phase 1 explicitly does not need:

- AI orchestrator behavior
- deep autonomous coordination
- vendor outreach automation
- broad inbox or multi-surface complexity
- delegated access
- a fully realized "digital superintendent" experience on day one

The MLP does not need the entire long-range system to exist.

## Phase 1 Shell Principle

Phase 1 should ship the full Housemate shell so the product already feels like Housemate, not a tool fragment.

The shell should include:

- Home
- Inbox
- Schedule
- Pros
- Property
- Payments
- Settings
- Agent entry point / SMS continuity

These surfaces should not all have equal depth. Phase 1 should use selective maturity:

- deep: onboarding, Schedule, Pros, reminders, SMS edit loop
- medium: Home, Property, Settings
- thin: Inbox, Payments
- stubbed / future-facing: Integrations / DAL and advanced automation controls

## What Should Be Deferred

These belong after the first complete lovable loop unless proven necessary sooner:

- broad DAL coverage across many third-party systems
- AI orchestrator / multi-agent execution
- sophisticated vendor monetization
- portfolio / multi-property management
- family-manager expansion
- overly broad analytics taxonomy
- feature-complete versions of every planned tab

## Operational Truth

The product promise is premium service, but the first product risk is ambiguity. Phase 1 has to show a real household manager: "this understands my house, my vendors, and my cadence." After that, reliability, follow-through, reminders, and graceful recovery matter more than feature count.
