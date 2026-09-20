# Taxonomy Change 077: Generalise platform attack, power, checkpoint and settlement boundaries

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-09-21
- Trigger: `GAME-0333` Sonic the Hedgehog lower-ID scan.
- Scope: wording and support for `ACT-295`, `SYS-902`, `SYS-905`, `SYS-933`,
  `SYS-935` and `INF-347`; no earlier game signature, combination, family or
  lifecycle change.

## Problem

Six valid boundaries named their first carrier too narrowly. Character attacks
named fighters despite accepted Crash and Donkey Kong platform attacks.
Temporary capability, stage settlement, checkpoint, collectible-life and HUD
boundaries named Mario or Crash parameters as requirements. Sonic preserves
their causal operations while using jump-spins, shoes/shield states, a
signpost, lamppost, retained ring milestones and elapsed rather than remaining
time.

## Accepted change

- `ACT-295` admits directly controlled character-owned attack states including
  jump-spins, rolls and cartwheels as well as fighter commands.
- `SYS-902` admits pickup-applied temporary movement, protection or contact
  capabilities removed by expiry or compatible damage.
- `SYS-905` admits an authored stage marker that settles declared spatial,
  elapsed/remaining-time or collectible measures into score before successor
  transfer.
- `SYS-933` admits activated or breakable checkpoint fixtures and explicitly
  parameterises retained versus reset state.
- `SYS-935` makes rollover, subtraction or retention a counter parameter; each
  newly reached milestone still yields exactly one finite life.
- `INF-347` admits elapsed or remaining time and generic route-resource counts,
  plus world feedback for temporary and checkpoint states.

## Complete lower-ID transfer test

- Street Fighter 6, Brawlhalla, TEKKEN 8 and Battletoads retain their directly
  commanded fighting attacks; Crash and Donkey Kong now fit their already
  admitted spin, roll and cartwheel uses explicitly.
- Super Mario Bros. retains its ordered avatar forms, Star timer, flag height,
  remaining-time settlement and coin/area HUD.
- Crash Bandicoot retains its breakable counted checkpoint and one-hundred-
  fruit rollover; Donkey Kong Country retains Star Barrel and banana rollover.
- Sonic adds independent temporary states, signpost settlement, a non-
  breakable lamppost, retained 100/200-ring milestones and elapsed-time HUD.

## Migration and compatibility

Stable IDs are retained. English and Ukrainian definitions, parameters and
carrier support change. `GAME-0333` reuses all six boundaries; every earlier
signature and comparison remains unchanged.

## Validation expectation

Repository validation must report no duplicate Active definition. The complete
lower-ID scan and Ukrainian review must preserve each earlier carrier's gates
while admitting Sonic's documented parameter variants.
