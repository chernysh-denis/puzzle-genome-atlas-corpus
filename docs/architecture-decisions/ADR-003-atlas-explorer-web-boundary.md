# ADR-003 — Atlas Explorer web boundary

- Status: Accepted
- Date: 2026-08-12

Transition note (2026-08-26): ADR-009 supersedes the direct-Markdown and
no-corpus-API clauses for the accepted backend-first target. This ADR still
describes current production until an explicitly authorised cutover and parity
window complete; its static HTML, bounded-browser-data and no-second-editor
constraints remain accepted.

## Context

The validated Atlas corpus is useful as research, but its Markdown-first form
does not provide approachable discovery, filtering or game comparison. A web
application must expose those capabilities without introducing a second
editable catalogue or weakening the repository's evidence rules.

## Decision

Build a static Astro and TypeScript application in `web/`.

- `knowledge/` remains the only canonical source for games, genes and
  combinations.
- A build-time adapter parses canonical Markdown into typed, immutable view
  models and fails on structural errors.
- The existing Python generator and validator run before web checks and remain
  authoritative for corpus integrity.
- Dependency and generated-output directories (`node_modules`, `dist` and
  `.astro`) are outside the canonical Markdown validation boundary.
- The browser receives only the bounded data required by interactive search,
  comparison and map views.
- The initial product has no database, authentication, editing API or runtime
  AI dependency.

## Consequences

The application can be hosted as static files and every corpus change is
versioned with its presentation. Node code must maintain contract tests against
the Markdown structure, while canonical validation is not reimplemented in
full. A future API, editor or separate client requires a new ADR.
