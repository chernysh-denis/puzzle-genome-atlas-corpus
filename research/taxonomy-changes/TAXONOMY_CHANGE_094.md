# Taxonomy Change 094: Isolate target-relative lock and typed visor scans

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: `2026-09-22`
- Trigger: `GAME-0355` Metroid Prime complete lower-ID transfer test.
- Scope: four new Active boundaries and two evidence-backed generalisations.

## Problem

The vocabulary represented direct movement and attacks, held Subnautica
blueprint scanning, quickhack scanning, persistent surveys, generic active
abilities, combat-room clearance and an authored removal of equipped gear. It
did not separately represent Metroid Prime's target-relative lock/orbit/dash,
one completed held scan resolving into typed data or fixture effects, the Scan
Visor's bounded disclosure surface, or a prologue whose required terminal is
escape plus an authored reduced-capability landing.

## Accepted change

- Add `ACT-494` for holding one world target lock so movement and dash inputs
  are resolved relative to that target.
- Add `SYS-982` for completing a held world scan into the target's typed
  information, weak-point lock or fixture-control response.
- Add `INF-368` for the Scan Visor's target eligibility, progress and completed
  disclosure boundary.
- Add `OBJ-205` for the complete guardian-clearance, timed evacuation,
  capability-malfunction and reduced-loadout landing terminal.
- Generalise `ACT-313` from a powered handheld scanner with resumable blueprint
  evidence to any equipped powered analyser whose held in-range target scan
  advances persistent target progress. Blueprint settlement remains `SYS-544`;
  Metroid Prime's typed target result is `SYS-982`.
- Generalise `SYS-972` from removal of an equipped item set to removal of a
  declared equipped or acquired capability set at an authored continuing-route
  event. The living actor, base control and future replacement or reacquisition
  model must remain.

## Complete lower-ID transfer test

- `ACT-008` owns free direct movement but not a held relation that continually
  reinterprets orbit and dash relative to one target.
- `ACT-161` owns the aimed attack after targeting; it does not create or
  maintain target-relative locomotion.
- `ACT-313` already owns the held in-range observation and is therefore
  generalised rather than duplicated. Its old Subnautica carrier remains
  unchanged because `SYS-544` still owns fragment counting and blueprint
  unlock.
- `ACT-481` and `INF-360` own instant Starfield survey samples, not held target
  scans whose completed target may operate a fixture or rewrite a lock point.
- `INF-147` joins target disclosure with available quickhacks and cyberdeck
  state. It cannot absorb a visor target that exposes information or an
  authored control response without a hack menu.
- `SYS-972` already captures the closest authored nonterminal reset. Extending
  its removed set from equipment slots to intrinsic capability flags preserves
  its causal boundary and avoids a carrier-specific duplicate.
- `OBJ-156` ends on escape from a boss-gated region before health loss; it does
  not require a later authored capability reset and successor landing state.
- Existing target, cockpit and homing-missile genes either concern craft
  systems or resolve guided projectiles; none changes avatar movement into a
  persistent orbit/dash relation around the selected target.

## Migration and validation expectation

Append four Active IDs, revise only `ACT-313` and `SYS-972`, and add complete
reviewed Ukrainian coverage. Earlier game signatures, combinations and family
definitions remain unchanged. Validation must find a twenty-gene
`GAME-0355` signature and an executable reconstruction that covers held scan,
weak-point retargeting, target-relative combat, finite missiles, seven-minute
escape, Grapple traversal, authored ability loss and reduced-loadout landing.
