# Taxonomy Change 083: Generalise proximity-collected defeat resources and isolate Essence-funded charge

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-21
- Trigger: `GAME-0341` Ninja Gaiden Black lower-ID scan.
- Scope: wording and second-carrier support for `SYS-574`; new `SYS-959`;
  supporting-carrier evidence for the remaining reused genes; no earlier game
  signature, combination, family or lifecycle change.

## Problem

The stable vocabulary already represented a defeated enemy leaving a world
resource that is attracted and credited on proximity, but `SYS-574` named only
Vampire Survivors experience gems even though Ninja Gaiden Black uses the same
causal boundary for typed currency, health and Ki Essence. It did not represent
the distinct alternative resolution: holding a weapon charge pulls in those
still-uncollected resources, forfeits their ordinary benefits and accelerates
an Ultimate Technique.

## Accepted change

- `SYS-574` now names a typed proximity-collected run resource. Resource type,
  destination and cap become parameters; enemy defeat, a world drop,
  attraction and contact credit remain mandatory.
- `SYS-959` isolates consumption of nearby uncollected defeat resources into a
  held weapon charge. The charged strike input remains `ACT-161`; ordinary
  resource attraction remains `SYS-574`.

## Complete lower-ID transfer test

- Vampire Survivors keeps `SYS-574`: defeated enemies leave Experience Gems,
  proximity attracts them and contact credits run-local experience.
- Ordinary contact pickups, direct kill rewards, container loot, contextual
  recovery drops and boss chests do not gain `SYS-574` without the complete
  defeated-enemy world-resource attraction boundary.
- No lower-ID carrier was found in which a held weapon charge consumes nearby
  still-uncollected defeat resources while sacrificing their ordinary pickup
  effect, so no prior signature gains `SYS-959`.
- Ninja Gaiden Black's attack command, Essence creation/collection and charge
  conversion stay separate causal transitions; move and resource names remain
  parameters.

## Migration and compatibility

`SYS-574` retains its stable ID and Vampire Survivors signature. English and
Ukrainian wording broaden only its resource destination. `SYS-959` is appended
as one Active ID. Existing game signatures, comparisons, families and verified
combinations remain unchanged.

## Validation expectation

Repository validation must report no duplicate Active definition. Both genes
must have reviewed Ukrainian copy; `GAME-0341` must be the only initial carrier
of `SYS-959`; and the complete lower-ID scan must preserve Vampire Survivors as
the only earlier `SYS-574` carrier.
