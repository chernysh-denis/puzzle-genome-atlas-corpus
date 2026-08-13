# Taxonomy Change 003: Merge duplicate contiguous-chain push actions

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-08-12
- Trigger: `GAME-0037` boundary audit before Cosmic Express classification

## Current classification

- `ACT-018` described one directional input shifting an aligned contiguous
  chain of pushable Baba Is You objects when the free end accepts movement.
- `ACT-053` described one directional input shifting an aligned contiguous
  chain of Patrick's Parabox boxes when the distal destination and any
  containment transition resolve legally.
- Both records excluded a one-object-only push, pulling, remote relocation and
  automatic force propagation.

## Detected problem

The two records encode the same direct player command and differ only in the
destination topology available to the final chain member. Crossing a recursive
container boundary is already represented by `SYS-069` and constrained by
`CON-082`; keeping a second Action ID duplicates the command because of its
game-specific resolution context.

The overlap was found while comparing Cosmic Express path propagation with all
existing Action definitions. It affects decision representation: two games
that let one local input push a complete contiguous chain should share the same
Action gene, while their automatic destination resolution remains distinct.

## Evidence

- [`GAME-0013` — Baba Is You](../../knowledge/games/a-f/baba-is-you.md) shifts
  every contiguous `PUSH` object one cell when the free end accepts movement.
- [`GAME-0036` — Patrick's Parabox](../../knowledge/games/m-r/patricks-parabox.md)
  shifts a contiguous aligned row under one directional push; its distal member
  may additionally cross a nested boundary through `SYS-069`.
- In both games the player selects direction by moving the controlled actor
  into the proximal object, does not select chain members independently and
  receives all-or-nothing chain displacement.

## Change

- Generalise `ACT-018` wording from cell-only displacement to one logical
  position under the destination topology.
- Add Patrick's Parabox as corroborating evidence for `ACT-018`.
- Replace `ACT-053` with `ACT-018` in `GAME-0036` and its game-index signature.
- Mark `ACT-053` as `Merged` and retain it as a historical alias.
- Preserve `SYS-069`, `SYS-070` and `CON-082`; they continue to encode nested
  boundary transfer, containment reparenting and centre-aligned access.

## What does not change

- Patrick's Parabox retains the same number of decision-relevant genes and no
  rule is removed from its genome.
- `COMB-0036` does not contain either chain-push Action and is unchanged.
- No novelty claim or gene type is created.

## Impact

- Stable genes: unchanged at 258.
- Active genes: 257 → 256.
- Reused active genes: 51 → 52 because `ACT-018` gains a second supporter.
- Active singleton genes: 206 → 204.
- Total active-gene usages: unchanged at 436.
- Singleton share: `206 / 257 = 80.2%` → `204 / 256 = 79.7%`.
- Baba Is You / Patrick's Parabox similarity increases from
  `2 / 23 = 0.086957` to `3 / 22 = 0.136364`; Sokoban remains Patrick's
  Parabox's unique near match at `7 / 14 = 0.500000`.

## Decision

- Decision: `Accepted`.
- Rationale: one shared Action plus game-specific System / Constraint genes is
  the smallest representation that preserves both command and resolution.
