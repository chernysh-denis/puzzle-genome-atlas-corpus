# Taxonomy Change 084: Isolate the first-maze PAC-MAN pursuit loop

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-21
- Trigger: `GAME-0342` PAC-MAN lower-ID scan.
- Scope: seven new System Behaviour genes; supporting-carrier evidence for
  reused genes; no earlier signature, lifecycle, combination or family change.

## Problem

The vocabulary represented continuous movement, contact collection, visible
boards, finite-life return, score and target clearance, but not the compact
causal rules that distinguish the original first PAC-MAN maze: four pursuers
with different target functions under one timed schedule, temporary edible
reversal, progress-and-time release from a protected home, dot-triggered timed
fruit, a class-sensitive wrap tunnel, a one-time score life and same-maze
rebuilding after exhaustive collection.

## Accepted change

- `SYS-960` owns the timed Scatter/Chase schedule, role-specific targets and
  forced reversals.
- `SYS-961` owns Power-Pellet contact reversal, escalating capture score and
  returning-eye restoration.
- `SYS-962` owns collection-counter or timeout release from the ghost house.
- `SYS-963` owns optional timed bonus objects at collection milestones.
- `SYS-964` owns paired edge-tunnel mapping with actor-class speed.
- `SYS-965` owns one extra life from a non-consuming score threshold.
- `SYS-966` owns rebuilding a fully cleared fixed collectible maze while
  retaining run-level score and life stock.

## Complete lower-ID transfer test

- `GAME-0114` Peggle Deluxe shares only visible current state, score, declared
  target clearance and real-time resolution; its aimed ball and orange-peg
  field do not support any of the seven additions.
- Existing autonomous-routing carriers lack four role-specific target
  functions under a common alternating mode schedule.
- Existing temporary-power and invulnerability carriers lack escalating
  counter-capture plus autonomous hostile restoration.
- Existing wave, portal, milestone-life and stage-settlement carriers fail the
  protected-home counters, class-speed tunnel, aggregate-score or same-maze
  rebuild boundaries respectively.
- No lower-ID signature changes.

## Migration and compatibility

All seven IDs are appended as Active definitions. English and Ukrainian
records are introduced together. Existing signatures, verified combinations
and lifecycle states remain unchanged; GAME-0342 is the initial carrier.

## Validation expectation

Repository validation must find no exact Active-definition collision, all
seven Ukrainian definitions and the complete GAME-0342 signature. The
deterministic comparison must select Peggle Deluxe alone at `4 / 19 = 0.210526`.
