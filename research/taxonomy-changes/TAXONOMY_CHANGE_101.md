# Taxonomy Change 101: Isolate a skill-weighted finite lock attempt

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: `2026-09-22`
- Trigger: `GAME-0362` The Elder Scrolls III: Morrowind complete lower-ID
  transfer test.
- Scope: one new Active System Behaviour; no lifecycle or earlier-signature
  change.

## Problem

The vocabulary can represent a generic random result, a visible fixed dice
check, a retry-class rule and Skyrim's continuous angular lock probing. It
cannot represent one discrete lock attempt whose hidden chance is jointly
conditioned by a persistent character skill, supporting attributes, current
fatigue, tool quality and lock difficulty while every success or failure
unconditionally consumes one use of that same equipped tool.

## Accepted change

- Add `SYS-993` for the complete skill-weighted finite-tool resolution.
- Reuse `SYS-004` for the random branch, `ACT-341` for the addressed contextual
  interaction and `INF-119`/`INF-128` for exposed character and tool state.
- Do not create a separate action, constraint or information boundary.

## Complete lower-ID transfer test

- `SYS-004` selects a probabilistic outcome but does not bind its probability
  inputs or mandatory resource consumption.
- `SYS-387` resolves one visible d20 against authored difficulty and can spend
  Inspiration; Morrowind exposes neither die, difficulty nor reroll.
- `SYS-801` visibly sums a fixed two-die roll and modifiers against a declared
  difficulty with automatic extremes; Morrowind uses a concealed chance.
- `SYS-613`, `ACT-344`, `CON-508` and `INF-243` jointly model Skyrim's continuous
  angle, torque, resistance and graded feedback; Morrowind accepts one discrete
  attempt and returns only success or failure.
- Contextual finite lockpicks and multitools in Deus Ex are treated as bypass
  parameters because that packet does not establish this character-stat,
  condition, quality and lock-level probability relation.

## Migration and validation expectation

Append `SYS-993`, preserve every lower-ID signature, provide complete reviewed
Ukrainian coverage and require a 17-gene `GAME-0362` signature. The dedicated
control must consume one use for both failed and successful attempts, reject
missing or exhausted tools, preserve authored package order and reproduce the
Blades/successor terminal through manual reload.
