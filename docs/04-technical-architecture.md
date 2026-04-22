# Housemate Technical Architecture

Last updated: 2026-04-22

## Architecture Principle

Build the simplest architecture that can support a trustworthy homeowner loop now while preserving the structural decisions that would be painful to retrofit later.

## Current Stack Direction

- Next.js
- shadcn/ui
- Tailwind CSS
- Inngest
- Twilio
- Stripe
- Novu
- Typesense
- Tiptap
- pgvector
- Redis
- ATTOM Data
- Google Places API
- Anthropic Claude API

## Core Technical Decisions Already Locked

- Household model: `household_id` above `user_id`
- Future extension path: `portfolio_id` above household
- Settings is a navigation destination, not a data store
- Permissions use the three-state model at the action level
- Household proxy identity is required:
  - dedicated Twilio number
  - dedicated agent email
- `recommendation_source` on `vendor_shown` is required to prevent monetization drift

## Delegated Access Layer

DAL remains the most strategically differentiated architectural layer.

Key principles:

- authorized-agent legal framing
- per-site consent, not blanket consent
- credentials encrypted at rest
- just-in-time decryption in memory only
- auditability of every consequential action

Current position:

- DAL is a core long-term moat
- DAL does not need to be the first large implementation burden if a narrower lovable loop can be proven first

## Data Model Truths

Must be designed correctly early:

- `household_id` as the core shared scope
- service-connection level permissions
- recurring event support with proper series and scope handling
- vendor relationship model separated from household-specific relationship state
- typed notification objects
- event instrumentation that can support attribution later

## Notifications And Messaging

- SMS is a primary surface, not an afterthought
- agent-initiated communication and system notification pings are different products and should stay separate
- notification fatigue is a real trust risk

## Analytics Guidance

Treat analytics as architecture, but do not overbuild it before launch.

Minimum launch metrics:

- signup completion
- onboarding completion
- time to first useful outcome
- weekly active households
- trial-to-paid conversion

Build richer investor and vendor instrumentation after the primary loop is working.

## Reliability Priorities

The first version must be strong on:

- reminder reliability
- vendor communication logging
- status clarity
- error recovery
- auditability

The first version does not need maximum breadth.

## Architectural Smell To Avoid

- building heavy DAL machinery before proving the homeowner loop
- over-instrumenting before usage exists
- building too many product surfaces in parallel
- conflating polished component work with shipped product capability
