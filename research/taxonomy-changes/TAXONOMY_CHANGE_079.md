# Taxonomy Change 079: Generalise portable companion-battle boundaries

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-09-21
- Trigger: `GAME-0336` Pokémon Red Version lower-ID scan.
- Scope: wording and support for `ACT-019`, `ACT-194`, `ACT-258`, `SYS-307`,
  `CON-276`, `CON-277`, `CON-384` and `INF-123`; supporting-carrier evidence
  for `ACT-008`, `ACT-130`, `ACT-259`, `SYS-004`, `SYS-299`, `SYS-362`,
  `SYS-854`, `CON-210`, `CON-282` and `TIM-001`; no earlier game signature,
  combination, family or lifecycle change.

## Problem

Eight transferable companion-battle boundaries named Pokémon Legends: Z-A or
Palworld's live-world carrier too narrowly. The original Pokémon Red Version
preserves the same player operations and storage constraints through a
menu-driven turn battle: an ability may target an actor, a Ball is committed
through ITEM rather than physically thrown, switching is not live, and a
captured creature may enter the party or current Box. The old wording would
mistake interface and timing for gene identity.

## Accepted change

- `ACT-019` permits an eligible actor, position or area target.
- `ACT-194` requires a committed carried capture device but not a physical
  live-world throw.
- `ACT-258` permits any battle timing while preserving one commanded active
  companion and persistent member state.
- `SYS-307` begins from an eligible committed device rather than requiring a
  device hit.
- `CON-276` requires a legal wild target and device commitment; Trainer-owned
  creatures remain excluded.
- `CON-277` admits the six-member party/current-Box destination and rejection
  when both capacities are exhausted.
- `CON-384` removes the unnecessary live-battle qualifier while retaining one
  living eligible commanded active slot.
- `INF-123` covers any owned companion profile inspected before party, roster
  or assignment decisions rather than only captured-assignment panels.

## Complete lower-ID transfer test

- Into the Breach, Bad North, Tactical Breach Wizards and Darkest Dungeon keep
  their actor, position, area, range and rank targets under `ACT-019`.
- Palworld and Pokémon Legends: Z-A still satisfy `ACT-194`, `SYS-307` and
  `CON-276`: their world throws are one supported interaction carrier, not the
  portable boundary. Scripted or Trainer-owned targets remain excluded.
- Palworld retains distinct Palbox, party and base capacities under `CON-277`;
  Pokémon Legends: Z-A retains Boxes and its six-member party.
- Pokémon Legends: Z-A retains one living active commanded battler under
  `ACT-258` and `CON-384` despite its live timing.
- Palworld and Pokémon Legends: Z-A retain their detail/summary panels under
  `INF-123`; Pokémon Red adds independent pre-switch party-summary evidence.
- Pokémon Red Version adds only menu-driven carriers and no retroactive gene
  membership for an earlier game.

## Migration and compatibility

Stable IDs are retained. English and Ukrainian labels, definitions,
parameters and carrier support change for the eight generalised boundaries.
`GAME-0336` reuses them. Every earlier signature and comparison remains
unchanged.

## Validation expectation

Repository validation must report no duplicate Active definition. The
complete lower-ID scan and Ukrainian review must preserve actor/target,
device/eligibility, active-slot, capacity and disclosure gates while admitting
Pokémon Red Version without importing its menu layout as gene identity.
