# Taxonomy Change 076: Generalise strategic settlement and army interfaces

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-09-21
- Trigger: `GAME-0332` Heroes of Might and Magic III: Complete lower-ID scan.
- Scope: wording and support for `ACT-281`, `ACT-345`, `ACT-347`, `SYS-616`,
  `CON-510`, `CON-514`, `INF-244` and `TIM-018`; no earlier game signature,
  combination, family or lifecycle change.

## Problem

Eight valid boundaries named their first carrier too narrowly. Civilization
turns named only civilizations; campaign construction required a fixed slot and
delayed queue; recruitment required denars and a party; campaign battle transfer
and information named Total War details. Heroes III preserves the causal
boundaries while using kingdoms, immediate one-per-day town construction,
typed resources, dwelling stock, same-type troop stacks and a nested day cycle.

## Accepted change

- `ACT-281` and `TIM-018` name a polity-level multi-command strategic turn.
- `ACT-345` and `CON-510` admit either fixed settlement slots or a daily build
  capacity, immediate or delayed resolution and typed resource costs.
- `ACT-347` and `CON-514` admit local offer or dwelling stock, typed payment and
  compatible force slots or stacks.
- `SYS-616` carries survivors, casualties, experience, rewards and ownership
  consequences through a separate tactical battle and back.
- `INF-244` exposes applicable force, map/fog, date, settlement, recruit,
  resource, progression and objective state rather than one tutorial layout.

## Complete lower-ID transfer test

- Civilization VI retains whole-civilization command sets and sequential rivals.
- Total War: WARHAMMER III retains fixed settlement slots, queued duration and
  its campaign/battle transition.
- Mount & Blade II: Bannerlord retains denar-priced local offers and party cap.
- Heroes III adds daily capacity, typed costs, dwellings, seven-slot creature
  stacks and a sequential kingdom cycle within each day.

## Migration and compatibility

Stable IDs are retained. English and Ukrainian definitions, parameters and
carrier support change. `GAME-0332` reuses all eight boundaries; every earlier
signature and comparison remains unchanged.

## Validation expectation

Repository validation must report no duplicate active definition. The complete
lower-ID scan and Ukrainian review must preserve each earlier carrier's exact
gates while admitting Heroes III's documented variants.
