# Taxonomy Change 096: Isolate wanted-tier display and opening bicycle-follow terminal

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: `2026-09-22`
- Trigger: `GAME-0357` Grand Theft Auto: San Andreas complete lower-ID transfer test.
- Scope: two new Active boundaries; no lifecycle or earlier-signature change.

## Problem

The vocabulary already represents police escalation/search, health, direct
vehicle operation, ambient traffic, authored mission order and detailed
navigation surfaces. It does not isolate the compact wanted-star tier shown by
the original San Andreas HUD without importing a calculated GPS route or a
ticket/arrest taxonomy. It also lacks an objective for two consecutive
moving-leader bicycle stages whose settlement unlocks the first persistent home
and successor mission.

## Accepted change

- Add `INF-371` for a compact wanted-star display that exposes current police
  pressure and clearance state without revealing future police locations.
- Add `OBJ-207` for mounting the supplied bicycle, following the first and then
  second authored leader, reaching the final marker and retaining the declared
  Respect, safehouse and successor-mission state.
- Reuse the existing foot movement, vehicle operation, vehicle motion, skill,
  traffic, police, health, ordered-gate, vehicle-legality, wanted-clearance,
  character-resource, mission-marker and shared-time boundaries unchanged.

## Complete lower-ID transfer test

- `INF-144` requires a calculated road route together with wanted-search state;
  the original San Andreas opening has local radar and markers but no equivalent
  calculated GPS line.
- `INF-273` distinguishes a payable citation, arrest demand and continuing
  search; San Andreas wanted stars expose police pressure without that Mafia
  road-law classification.
- `INF-119` retains health and personal statistics. It does not tell the player
  the current law-response tier, so `INF-371` is not a resource duplicate.
- `INF-125` retains mission markers and current authored gates. It does not
  expose whether ordinary travel is under one or more tiers of police pressure.
- Existing follow, escort and route objectives either retain cargo, protect an
  actor, reach a static exit or settle a race. None requires a Sweet-to-Ryder
  moving-reference handoff followed by a first-home and next-mission unlock.
- `OBJ-207` therefore owns the complete terminal rather than the individual
  bicycle, marker or story-reward parameters.

## Migration and validation expectation

Append two Active IDs, preserve every lower-ID signature, add complete reviewed
Ukrainian coverage and require a fifteen-gene `GAME-0357` signature. The
dedicated state reconstruction must cover BMX entry, Cycling gain, traffic
collision, wanted activation/search/clearance, Sweet-to-Ryder order, zero-health
and arrest failure, and the retained Respect/Johnson House/`Ryder` terminal.
