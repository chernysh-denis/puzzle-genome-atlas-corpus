# Taxonomy Change 071: Generalise survival and ownership-core reserve boundaries

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-13
- Trigger: `GAME-0294` V Rising complete lower-ID System Behaviour and
  Constraint scan.
- Scope: wording and support for `SYS-327`, `SYS-332`, `CON-281` and
  `CON-295`; no earlier game signature, combination gene set, family membership
  or lifecycle changes.

## Problem

Two accepted portable boundaries were phrased in terms narrower than their
actual invariant. `SYS-327` and `CON-281` already join the personal reserves,
exposures and protections that determine whether a survival avatar remains
viable, but enumerate food, hydration and climate rather than a blood reserve
and direct sunlight. `SYS-332` and `CON-295` already join an ownership core's
consumed reserve to building protection and shortage decay, but name Rust's Tool
Cupboard, grade materials and connected blocks in the portable wording.

V Rising supplies both transitions without justifying duplicate genes: blood
drains as a personal reserve while direct sun creates a recoverable exposure,
and a Castle Heart consumes Blood Essence to power and protect its claimed
territory from decay.

## Accepted change

- Rename `SYS-327` to “Advance personal survival reserves and environmental
  exposure”; replace the closed meter list with a parameterised reserve and
  exposure boundary and add V Rising blood/sun support.
- Rename `CON-281` to “Avatar survival depends on compatible protection and
  reserve state”; preserve the viability predicate while admitting blood,
  direct-sun exposure, shade and mist.
- Rename `SYS-332` to “Consume an ownership-core reserve and decay unprotected
  construction”; replace Tool Cupboard- and grade-only wording with a core,
  reserve, protected class and shortage consequence. Rust's exposed-layer order
  remains a parameter.
- Rename `CON-295` to “Building protection requires connected ownership-core
  reserve coverage”; admit either connected building membership or claimed-
  territory membership and either material-grade or Blood Essence reserve.

The invariants remain unchanged. The first pair governs a currently controlled
avatar's own survival state, not building decay or direct hostile damage. The
second pair governs reserve-backed protection projected by an ownership core,
not construction cost, raid damage or ordinary equipment durability.

## Complete lower-ID transfer test

- Every earlier `SYS-327` / `CON-281` carrier still continuously updates or
  constrains health through its relevant hunger, hydration, temperature,
  fatigue, radiation, load, protection or recovery parameters. No earlier
  signature changes.
- `SYS-632` stays distinct: it transforms a selected timed food set into
  decaying health/stamina bounds rather than advancing the complete personal
  survival state.
- `SYS-698` stays distinct: it is DayZ's coupled consciousness pipeline across
  health, blood, shock and bleeding, including incapacitation, not a generic
  replenishable blood-food profile or environmental exposure.
- Every earlier `SYS-332` / `CON-295` carrier remains Rust. Its Tool Cupboard,
  connected grades, material-specific shortages and outer-layer decay are
  retained parameter values under the broader ownership-core boundary.
- `SYS-331` / `CON-294` stay distinct: they resolve identity authority, locks
  and protected construction permissions, whereas this change concerns ongoing
  reserve coverage and its shortage consequence.
- `SYS-333` stays distinct because a private V Rising LAN world pauses when its
  host is absent; no always-running offline-world simulation is claimed.
- `SYS-857` is new and distinct: it creates ownership of a predefined Build
  Location. Paying the Heart after ownership exists does not create the claim.

No earlier game signature, lifecycle, combination or family membership changes.

## Evidence and confidence

- Evidence quality: `Corroborated`.
- Confidence: `High` for the portable invariants. Stunlock directly documents
  blood drain and sunlight as adjustable personal pressures, direct-sun damage,
  Mist Brazier protection and Blood Essence-powered Castle Heart decay;
  player-maintained current references provide the selected early route.
- Source: [V Rising decomposition](../../knowledge/games/s-z/v-rising.md),
  claims `VRS-006`, `VRS-009` and `VRS-011`–`VRS-012`.

## Migration and compatibility

- Stable IDs: all four IDs are retained.
- Registry: wording and evidence support change only.
- Existing signatures: unchanged.
- New signature: `GAME-0294` reuses all four owners.
- Public consumers: resolve by stable ID, so the wording change is compatible.

## Validation expectation

- Repository validation must report no duplicate active definition.
- Lower-ID comparison must scan all 293 earlier game signatures.
- Ukrainian canonical wording must preserve the personal-versus-building split,
  reserve-backed protection, shortage consequence and Rust-specific parameters
  without treating every survival game as blood- or upkeep-driven.
