# Taxonomy Change 104: Isolate timed trick-chain and partial Tour settlement

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: `2026-09-23`
- Trigger: `GAME-0365` Tony Hawk's Pro Skater 1 + 2 PS5 Warehouse Tour
  lower-ID transfer test.
- Scope: eight new Active boundaries; no earlier lifecycle or signature
  changes.

## Problem

The corpus already has real-time movement, compatible rail/wall carriage,
a breakable traversal trick chain and score maximisation from Jet Set Radio.
It does not separately encode directional skateboard trick/transfer commands,
continuous rail/manual balance correction and limits, history-sensitive
trick value, multiple retained Tour goals of different kinds, a fixed park
clock with partial credit, or the joint trick/balance/goal HUD.

## Accepted change

- Add `ACT-500` for contextual trick selection and line transfers, and
  `ACT-501` for active rail/manual balance correction.
- Add `SYS-998` for spin, stance, gap and repetition-sensitive trick value,
  and `SYS-999` for independent retained park-goal credit.
- Add `CON-665` for live contact-trick balance validity and `CON-666` for
  two-minute Tour-run expiry with partial goal retention.
- Add `INF-374` for trick, balance, clock and goal disclosure, and `OBJ-211`
  for one retained goal from the bounded run.
- Reuse `ACT-008`, `SYS-974`, `SYS-975`, `OBJ-002` and `TIM-003` unchanged.
  Trick names, park props, score thresholds and exact coefficients remain
  parameters, not new gene IDs.

## Complete lower-ID transfer test

- `GAME-0350` Jet Set Radio supplies the genuinely shared `SYS-974` rail/wall
  contact and `SYS-975` breakable traversal score chain. Its graffiti
  command (`ACT-492`), spray reserve, police response and all-tags mission
  terminal do not transfer to a Warehouse Tour run.
- `ACT-471` braces an on-foot cargo load rather than correcting a skater's
  grind/manual balance; `SYS-717` multiplies rapid-kill experience rather
  than valuing landed traversal tricks.
- `CON-068` ends an attempt unsuccessfully on a fixed deadline unless a
  single completion objective has been satisfied. Warehouse's incomplete
  goals remain individually credited for later runs, so no wording change
  can make that existing all-or-nothing boundary fit.
- `OBJ-002` fits optional score maximisation, but does not replace
  `OBJ-211`'s retained partial Tour goal. `TIM-003` fits the live input
  window without encoding the special expiry rule.
- No verified combination is added merely because these genes co-occur
  in one newly reviewed game.

## Evidence limits and migration

PlayStation Store establishes the PS5 Bundle identity; Activision directly
documents Tours, controls, score modifiers, HUD and optional balance assists.
The exact Warehouse two-minute goal packet is corroborated by a written
independent guide. No console executable or save was obtained, and no
coefficient or end-of-clock landing order is invented. Append the eight
definitions, review their Ukrainian translations and validate the thirteen-
gene genome without editing any earlier signature.
