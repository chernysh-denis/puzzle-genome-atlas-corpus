# Taxonomy Change 078: Generalise person-state and managed-domain boundaries

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-09-21
- Trigger: `GAME-0335` RollerCoaster Tycoon Deluxe lower-ID scan.
- Scope: wording and support for `SYS-198`, `CON-171`, `INF-058` and
  `INF-072`; supporting-carrier evidence for `ACT-139`; no earlier game
  signature, combination, family or lifecycle change.

## Problem

Four transferable boundaries named their first management carrier too
narrowly. `SYS-198` and `INF-072` said resident even though the accepted
operation is personal needs, thoughts and resulting behaviour. `CON-171` and
`INF-058` said municipal even though recurring construction solvency and an
itemised managed budget also govern a privately operated park. Forest
Frontiers preserves the causal operations while using guests, rides, staff,
admission and a park treasury rather than households or a city.

## Accepted change

- `SYS-198` admits autonomous people whose personal needs, experiences,
  preferences and remembered reactions alter later choices, departure, stress
  or breakdown; Dwarf Fortress stress remains one parameterisation.
- `CON-171` admits any player-managed domain whose construction, retained
  infrastructure, services or staff spend one treasury through upfront and
  recurring costs, debt and declared deficit consequences.
- `INF-058` admits an itemised managed-domain finance ledger independent of
  whether the domain is a city, empire, island or private park.
- `INF-072` admits a causal profile for any autonomous person whose current
  activity, needs, thoughts and relevant capabilities or preferences are
  inspectable.
- `ACT-139` gains Forest Frontiers fixed-footprint rides and stalls as carrier
  support without a definition change; custom track geometry remains separate
  under new `ACT-485`.

## Complete lower-ID transfer test

- Dwarf Fortress retains personal needs, memories, stress, creature work and
  relationships; RimWorld and The Sims 4 retain their already admitted
  resident/active-person profiles and personal-state outcomes.
- SimCity 4 and Cities: Skylines retain construction, service upkeep,
  borrowing, taxes and municipal budget panels. Anno 1800, Civilization VI
  and Stellaris retain managed-domain recurring ledgers and stockpiles.
- Against the Storm, Age of Empires II, Command & Conquer and Animal Crossing
  retain ordinary owned building placement. RollerCoaster Tycoon adds only
  fixed-footprint rides and stalls to that existing carrier class.
- RollerCoaster Tycoon Deluxe adds independent evidence for guests whose
  hunger, thirst, nausea, happiness, recent experiences and remaining money
  inform choices, and for a park treasury that pays construction, ride upkeep
  and wages while reporting itemised income and expenditure.

## Migration and compatibility

Stable IDs are retained. English and Ukrainian labels, definitions,
parameters and carrier support change for the four generalised boundaries.
`GAME-0335` reuses them. Every earlier signature and comparison remains
unchanged.

## Validation expectation

Repository validation must report no duplicate Active definition. The
complete lower-ID scan and Ukrainian review must preserve each earlier
carrier's actor, treasury, recurring-cost and disclosure gates while admitting
Forest Frontiers without treating park-specific values as gene identity.
