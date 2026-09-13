# Taxonomy Change 036: Generalise site-bound RTS production carriers

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-09-07
- Trigger: independent closure review of `GAME-0275` Command & Conquer
  Remastered Collection.

## Current classification

- `ACT-139`, `ACT-316`, `SYS-551`, `CON-467` and `INF-224` described Age of
  Empires II or settlement-specific building and production carriers.
- `ACT-315` required a floating portable fabrication fixture, `SYS-158`
  required a connected power network and `CON-292` described modular building
  blocks with structural support.

## Detected problem

- The standard opening X16-Y42 route in Tiberian Dawn Remastered deploys a
  mobile fabrication vehicle, places completed buildings, balances owner-wide
  power, submits paid site-bound structure and infantry orders, and reads that
  state through one RTS command view.
- Creating Command & Conquer-only genes would duplicate the same player verbs,
  transition functions, legality predicates and exposed decision state merely
  because structures can be produced before placement, the power pool is
  owner-wide, and the mobile fixture operates on land.

## Evidence

- EA's released Tiberian Dawn DLL source directly records mobile-construction
  deployment, building placement, production progress, progressive credit
  debit, prerequisites and the owner-wide power fraction:
  <https://github.com/electronicarts/CnC_Remastered_Collection>.
- Carrier evidence: the bounded decompositions for
  [`GAME-0119`](../../knowledge/games/a-f/factorio.md),
  [`GAME-0124`](../../knowledge/games/a-f/against-the-storm.md),
  [`GAME-0141`](../../knowledge/games/m-r/rust.md),
  [`GAME-0178`](../../knowledge/games/s-z/subnautica.md),
  [`GAME-0179`](../../knowledge/games/a-f/age-of-empires-ii-definitive-edition.md)
  and [`GAME-0275`](../../knowledge/games/a-f/command-and-conquer-remastered-collection.md).
- Counterevidence considered: a free scripted arrival remains excluded from
  production; a repeated automatic recipe remains excluded from the finite
  queue; terrain transformation remains excluded from building placement; and
  an independent burner remains excluded from a bounded power domain.

## Proposed change

- Generalise `ACT-139` to ordinary owned-building placement, `ACT-315` to a
  portable or mobile fabrication fixture, and `ACT-316` to one unit-or-structure
  production order at an eligible site.
- Generalise `SYS-158` to a bounded owner or network power domain and `SYS-551`
  to a site-bound queue whose completion may release a unit or make a structure
  ready for placement.
- Generalise `CON-292` to a legal clear building footprint, `CON-467` to
  unit/structure/research production legality, and `INF-224` to portable RTS
  economy, selection and production state.
- Keep topology, medium, reversibility, structure/unit product class,
  population, technology tier and exact stockpile count as carrier parameters.

## Genome and combination impact

- `GAME-0275` reuses all eight generalised IDs and ten further lower-ID Active
  genes; it creates no gene.
- No earlier reviewed signature, combination gene set or lifecycle changes.
- The surviving IDs, definition count and Active total remain unchanged.

## Decision

- Decision: `Accepted`.
- Decided by: complete lower-ID scan, two-way transfer test and direct released
  source-code comparison.
- Rationale: the same portable mechanics govern player action, transition,
  eligibility and visible state across the carriers. Product-specific building
  names, land/water medium and owner/network topology are parameters.
- Implementation links: `ACT-139`, `ACT-315`, `ACT-316`, `SYS-158`, `SYS-551`,
  `CON-292`, `CON-467`, `INF-224`, `GAME-0275`.

## Change history

- 2026-09-07 — created and accepted during the independent `GAME-0275`
  closure unit.
