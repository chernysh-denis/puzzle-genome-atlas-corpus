# Taxonomy Change 081: Generalise field interaction and command-combat carriers

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-21
- Trigger: `GAME-0338` Final Fantasy VII lower-ID scan.
- Scope: wording and support for `ACT-341`, `SYS-381`, `SYS-453`, `SYS-854`,
  `SYS-954`, `CON-175` and `INF-179`; new `OBJ-199` and `TIM-026`;
  supporting-carrier evidence for the remaining reused genes; no earlier game
  signature, combination, family or lifecycle change.

## Problem

Seven stable boundaries named their first carriers too narrowly. Contextual
world interaction assumed a player-created object rather than an authored
actor or fixture. Special readiness assumed damage dealt or healing but not
harm received. Equipment-derived combat state omitted embedded ability
components. Typed affinity and local encounters were worded as strictly
turn-based or wild-terrain systems. Persistent health and current-room
information named run/floor or room-only carriers although the same causal
boundaries operate across an authored field route.

## Accepted change

- `ACT-341` admits one reachable authored actor, fixture or player-created
  stateful object when the contextual interaction changes local route,
  objective, actor, fixture or inventory state.
- `SYS-381` admits eligible harm received as well as damage dealt or healing;
  the earning channel and cross-encounter retention rule remain parameters.
- `SYS-453` admits socketed or embedded ability components alongside item
  properties, attributes and passives when they derive legal combat commands.
- `SYS-854` uses command-combat rather than turn-based presentation as its
  boundary; affinity still modifies damage before defeat state.
- `SYS-954` samples a weighted local formation after eligible traversal,
  whether eligibility is terrain-specific or field-danger driven.
- `CON-175` terminates an authored route or run when the declared persistent
  actor/party health threshold is exhausted.
- `INF-179` applies to a current field or room that exposes actionable threats,
  interactables, pickups and exits.
- `OBJ-199` isolates the complete arm-response-evacuate mission terminal.
- `TIM-026` isolates concurrent actor-local readiness before command
  commitment; it is not a fixed alternating turn order or the Limit meter.

## Complete lower-ID transfer test

- Every earlier `ACT-341` carrier remains a contextual stateful-entity
  interaction; generic dialogue, contact pickup and direct construction do not
  gain the gene.
- Marvel Rivals retains `SYS-381` through contribution-earned ultimate energy;
  ordinary cooldowns and account experience remain excluded.
- Path of Exile 2 retains `SYS-453`; cosmetic loadouts and one attack
  resolution remain excluded.
- Persona 5 Royal and Pokémon Red Version retain `SYS-854`; live collision
  damage without a committed typed command does not gain it.
- Pokémon Red Version retains `SYS-954`; fixed Trainer battles and gifts remain
  excluded.
- Slay the Spire retains `CON-175`, and The Binding of Isaac: Rebirth retains
  `INF-179`; neither earlier signature changes.
- No lower-ID game receives `OBJ-199` or `TIM-026` merely because it has a
  timer, a mission device, a conventional turn order or a cooldown.

## Migration and compatibility

Stable IDs are retained. English and Ukrainian labels, definitions, parameters
and carrier support change only for the seven generalised boundaries.
`GAME-0338` adds the two independent new genes. Earlier signatures and
comparisons remain unchanged.

## Validation expectation

Repository validation must report no duplicate Active definition. The complete
lower-ID scan and Ukrainian review must preserve each earlier carrier while
admitting Final Fantasy VII without conflating ATB Time, Limit readiness,
affinity, persistent HP, encounter sampling or mission countdown.
