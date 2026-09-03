# ADR-012 — Locale-separated public research

- Status: `Accepted`
- Date: 2026-09-03
- Decision owner: Puzzle Genome Atlas maintainer
- Baseline: public corpus `r000009`, 243 reviewed games

## Context

The site has separate `/ua/` and `/en/` route trees, but every source-record
link previously opened the same canonical English Markdown file. Historical
game records also ended with a Ukrainian maintainer delta ledger, so the public
corpus mixed languages inside files while describing Ukrainian translation as
a separate presentation layer.

This made the language switch incomplete. A visitor could read a fully
Ukrainian game, gene or combination page and then cross into an English or
mixed-language research record through a link labelled in Ukrainian.

## Decision

Keep canonical research records English-only and publish a distinct reviewed
Ukrainian research view:

```text
/en/ site -> knowledge/{games,genes,combinations}/...
/ua/ site -> knowledge/locales/uk/research/{games,genes,combinations}/...
```

The Ukrainian view is generated deterministically from the reviewed game, gene
and combination localisation JSON. It preserves stable IDs, complete game
signatures, combination membership and the reviewed analysis boundary. It is a
locale-specific research presentation, not a second taxonomy or evidence
authority.

Publication fails when any canonical game, active gene or verified combination
lacks the reviewed Ukrainian data required for its public overview. The export
also rejects Cyrillic in canonical public game Markdown. Historical Ukrainian
delta ledgers remain private authoring history and are omitted from the English
public projection; future canonical delta ledgers use English headings and
prose.

All site source links are resolved at build time from the URL locale and the
same immutable public-corpus commit. Ukrainian links cannot silently fall back
to English. English links cannot enter the Ukrainian tree.

## Consequences

- Ukrainian visitors reach Ukrainian game, gene, combination and corpus-index
  research views from every public source-data link.
- English public records contain no Ukrainian headings or summaries.
- Official product names, stable IDs, versions and other policy-approved exact
  tokens may remain untranslated in Ukrainian research views.
- Public-corpus payload size grows because the locale view is materialised as
  human-readable Markdown; corpus entity counts do not change.
- Published revisions remain immutable. The first public correction requires a
  new corpus revision rather than rewriting `r000009`.

## Verification

- Export the corpus twice and require byte-identical output.
- Require one Ukrainian research file for every game and combination, complete
  Ukrainian coverage for every active gene, and no Cyrillic in exported
  canonical game Markdown.
- Build both locale trees with an exact public commit and assert locale-specific
  source URLs for game, gene, combination, Method and footer links.
- Run repository, web, browser and accessibility gates before publication.
