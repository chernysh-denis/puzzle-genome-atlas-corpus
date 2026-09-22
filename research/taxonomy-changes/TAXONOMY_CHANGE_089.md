# Taxonomy Change 089: Bound one equipment-reset first-boss route

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: `2026-09-21`
- Trigger: `GAME-0347` Castlevania: Symphony of the Night complete lower-ID
  transfer test.
- Scope: two new Active System boundaries and supporting-carrier evidence for
  reused exploration, equipment, persistence and combat boundaries.

## Problem

The vocabulary represented exploration, live combat, equipment, experience,
retained interaction capabilities, capacity boosters, fixture saves and death
reloads. It did not represent an authored event that removes a living
character's equipped starting set while control and the equipment model
continue. It also lacked restoration at a save fixture that fills HP and MP
without owning enemy respawn or the separate save-write predicate.

## Accepted change

- `SYS-972` owns authored removal of the currently equipped loadout while the
  character and route continue.
- `SYS-973` owns current-resource restoration at an eligible save fixture.
- Reused boundaries receive explicit carrier evidence without an operational
  definition or earlier-signature change.

## Complete lower-ID transfer test

- `SYS-631` removes borrowed machinery only when a paid contract settles;
  Death removes personal equipment during a continuing route with no contract.
- Defeat-loss genes remove carried state because a life ends; this event occurs
  to a living controlled character and is not failure.
- `SYS-364` combines rest restoration with ordinary-enemy respawn. The save
  room restores HP/MP but does not own such repopulation.
- `CON-621` owns save legality and its retained write, not the independent
  resource refill.
- `OBJ-080` already owns mandatory-guardian defeat followed by crossing its
  opened progression threshold.

## Migration and validation expectation

Both boundaries append as Active. Existing lifecycle states, lower-ID
signatures, combinations and families remain unchanged. Validation must find
complete Ukrainian coverage, a nineteen-gene `GAME-0347` signature and a
deterministic executable reconstruction covering equipment removal, Cube
retention, restorative save, reload, boss clearance, Life Max Up and first
Marble Gallery control.
