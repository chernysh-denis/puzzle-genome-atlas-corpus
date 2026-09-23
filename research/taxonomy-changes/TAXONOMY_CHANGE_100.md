# Taxonomy Change 100: Isolate fixed starting skill specialisations

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: `2026-09-22`
- Trigger: `GAME-0361` Fallout: New Vegas complete lower-ID transfer test.
- Scope: one new Active action; no lifecycle or earlier-signature change.

## Problem

The vocabulary can distribute one numeric starting attribute pool, spend later
advancement points, select a match character or train a prerequisite skill. It
cannot represent a creation screen that requires exactly a fixed number of
distinct skills to receive persistent starting specialisation bonuses without
spending a numeric pool or selecting a class.

## Accepted change

- Add `ACT-497` for committing a fixed-count set of distinct starting skill
  specialisations.
- Reuse `ACT-401`, `SYS-740`, `CON-572` and the existing dialogue-information
  boundary unchanged for the separate numeric profile and later eligibility.

## Complete lower-ID transfer test

- `ACT-401` distributes a numeric point pool across named attributes; tagged
  skills select three identities and do not consume that pool.
- `ACT-146` trains one existing agent in a prerequisite skill during play;
  this action occurs before campaign entry and has no training cost or timer.
- `ACT-188` commits a match-local hero and build option; it neither chooses a
  fixed set of skills nor persists as a campaign character profile.
- `ACT-220` and other advancement actions spend earned points after play has
  begun, which would add a resource and progression semantics absent here.

## Migration and validation expectation

Append `ACT-497`, preserve every lower-ID signature, provide complete reviewed
Ukrainian coverage and require a 27-gene `GAME-0361` signature. The dedicated
control must reject duplicate or non-three tag sets, preserve the accepted tag
set, expose the Speech-gated recruitment, settle the Goodsprings defence branch
and retain the result through one manual save/reload.
