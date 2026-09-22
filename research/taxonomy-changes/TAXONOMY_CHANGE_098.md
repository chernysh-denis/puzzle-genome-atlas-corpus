# Taxonomy Change 098: Isolate Crimson Skies manoeuvre energy, magnetic missiles and Pandora terminal

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: `2026-09-22`
- Trigger: `GAME-0359` Crimson Skies: High Road to Revenge complete lower-ID
  transfer test.
- Scope: six new Active boundaries; no lifecycle or earlier-signature change.

## Problem

The vocabulary already represents direct four-axis craft flight, live combat,
checkpoint restoration, craft motion/collision, legal attack resources,
authored order, finite ammunition, local view, objective/radar information,
staged instruction, cockpit status and shared real time. Three mechanisms still
fail transfer:

- one discrete command requests a preprogrammed Immelmann/roll or a turbo burst
  inside continuous flight;
- finite magnetic missiles correct from a near-aim relation without the full
  selected-lock / incoming-threat / countermeasure chain of `SYS-726`;
- turbo and special manoeuvres consume the same bounded energy reserve.

No existing settlement converts an ordered opening sortie through an accepted
airborne-base return marker into recapture, one retained Upgrade Token and
ordinary interior control.

## Accepted change

- Add `ACT-496` for commanded authored aircraft manoeuvres or turbo bursts.
- Add `SYS-987` for finite near-aim magnetic projectile correction.
- Add `SYS-988` for the shared turbo/manoeuvre energy process.
- Add `SYS-989` for ordered sortie settlement into Pandora recapture, token and
  returned control.
- Add `CON-662` for the shared turbo/manoeuvre reserve legality.
- Add `OBJ-209` for the complete Pandora recapture terminal.
- Reuse existing flight, combat, checkpoint, collision, authored-order,
  finite-ammunition, information and time boundaries unchanged.

## Complete lower-ID transfer test

- `ACT-392` composes continuous throttle/pitch/yaw/roll; it does not represent
  one authored manoeuvre or turbo command. Drift and grounded-vehicle boost
  actions have incompatible carrier and charge boundaries.
- `SYS-726` couples selected-target lock, guided offence, incoming threat and a
  finite countermeasure. Crimson Skies establishes near-aim magnetic correction
  but no countermeasure branch in the packet; partial reuse would assert absent
  state.
- `ACT-393`, `SYS-724` and `CON-565` distribute one budget among engines,
  weapons and shields. The brown Crimson Skies reserve is instead consumed by
  two commanded movement classes and is not player-allocated among subsystems.
- `SYS-540` and `CON-457` require spatial boost pads; no such refill source
  governs the first-mission special reserve. Generic ability-resource gates do
  not preserve the explicit cross-action competition.
- `SYS-728`/`OBJ-141` end in a debrief medal. Other mission objectives settle a
  region, extraction, safehouse or invitation. None requires the Pandora marker,
  recaptured airborne home, Upgrade Token and restored interior control.
- `SYS-738`, `CON-571` and `INF-280` remain excluded: one independent route's
  primary-gun overheating note does not establish the complete first-mission
  heat/cooling information loop across the primary packet.

## Migration and validation expectation

Append six Active IDs, preserve every lower-ID signature, add complete reviewed
Ukrainian coverage and require a twenty-gene `GAME-0359` signature. The
dedicated state reconstruction must cover ordered lessons, finite magnetic
missiles, shared turbo/manoeuvre energy, two fighter waves, checkpoint failure
and the Pandora/token/post-mission terminal.
