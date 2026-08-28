# ADR-003 — Atlas Explorer web boundary

- Status: Accepted
- Date: 2026-08-12

Transition note (2026-08-27): the ADR-009 production cutover completed on
2026-08-26. ADR-010 now supersedes permanent PostgreSQL authority while
retaining a versioned Go API over an immutable artifact. This ADR's static
HTML, bounded-browser-data and no-second-editor constraints remain accepted.

Transition note (2026-08-28): ADR-011 restores the direct build-time corpus
adapter and removes the corpus API while retaining immutable revision and
public-release provenance.

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
