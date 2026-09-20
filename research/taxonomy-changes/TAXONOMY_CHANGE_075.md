# Taxonomy Change 075: Generalise live craft systems across starfighters and ships

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-21
- Trigger: `GAME-0331` Starfield complete lower-ID scan.
- Scope: wording and support for `ACT-210`, `ACT-393`, `SYS-723`, `SYS-724`,
  `CON-364` and `INF-277`; no earlier game signature, combination, family or
  lifecycle change.

## Problem

Two existing boundaries encoded their first carrier too narrowly. Character
creation required an occupation and point-balanced traits even though Starfield
uses the same persistent-background invariant with optional compatible traits.
The live craft-power, flight and cockpit boundaries named a starfighter and
exactly three channels even though Starfield's Frontier exposes the same shared
finite-power decision across more live subsystems. Fast travel also named only
discovered destinations although a currently tracked quest destination can be
an explicitly eligible target.

## Accepted change

- `ACT-210` now configures one starting background plus an optional legal trait
  set; point balance is a carrier parameter, not part of the boundary.
- `ACT-393` and `SYS-724` now accept any directly controlled craft and any
  finite set of live subsystems. Squadrons keeps its engines/lasers/shields and
  overcharge parameters; Starfield adds engines, shields, weapons and grav drive.
- `SYS-723` names a directly controlled craft rather than only a starfighter.
- `INF-277` exposes currently relevant cockpit systems, target, objective and
  threats without requiring every carrier to have shield facings, auxiliaries,
  countermeasures or missile warnings.
- `CON-364` accepts a discovered or explicitly offered quest destination while
  retaining the live-hostile-state travel lock.

## Complete lower-ID transfer test

- Project Zomboid remains valid: occupation, point-balanced positive and
  negative traits, starting skills and persistent modifiers are one carrier.
- STAR WARS: Squadrons remains valid: the X-wing has three power channels,
  overcharge, direct six-degree flight and its full cockpit threat surface.
- Elden Ring remains valid: discovered Sites of Grace are its eligible travel
  destinations and live combat blocks map travel.
- Starfield adds a background with up to three compatible optional traits, a
  Frontier with several finite live power channels, direct spaceflight and a
  cockpit that exposes only its applicable systems and threats.

## Migration and compatibility

Stable IDs are retained. English and Ukrainian definitions, parameters and
carrier support change. `GAME-0331` reuses the six boundaries; all earlier
signatures and comparisons remain unchanged.

## Validation expectation

Repository validation must report no duplicate active definition. Starfield's
comparison must scan every lower-ID signature. Ukrainian wording must preserve
the optional trait set, finite shared craft power and destination eligibility.
