# Taxonomy Change 009: Merge carried sweep clearance into coupled-body clearance

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-08-14
- Trigger: `REGISTRY_NORMALISATION_005` residual Constraint transfer test

## Current classification

- `CON-090` required destination and swept-cell clearance for the permanently
  attached front fork in Stephen's Sausage Roll.
- `CON-100` required destination and swept-corner clearance for a reversibly
  front-carried crate in Bonfire Peaks.
- Both constrained translation and quarter-turn commands of an oriented agent
  coupled to one occupied front-offset body.

## Detected problem

The two records encoded attachment lifetime twice. Permanent attachment and
reversible grab/release determine when the compound footprint exists, but once
coupled they do not change the clearance question: every destination cell and
every cell swept by the oriented body must be compatible.

The distinction fails the two-way transfer test. Parameterising `CON-090` with
Bonfire Peaks' grabbed crate reproduces its blocked translations and pivots.
Substituting Stephen's permanent fork into `CON-100` reproduces its complete
two-by-two turn-clearance test. No legal transition is accepted by one
predicate and rejected by the other after footprint, collision class and
contact exceptions are supplied.

## Evidence

- [`GAME-0043` — Stephen's Sausage Roll](../../knowledge/games/s-z/stephens-sausage-roll.md)
  directly establishes the persistent player/fork destinations and full
  two-by-two quarter-turn sweep.
- [`GAME-0055` — Bonfire Peaks](../../knowledge/games/a-f/bonfire-peaks.md)
  establishes the front-held crate destination and swept corner during a
  quarter-turn.
- `ACT-048` already records reversible pickup/release; `ACT-058` records the
  fork-bearing turn that can contact a sausage; `CON-101` separately records
  Bonfire Peaks' carry-conditioned elevation legality.

## Change

- Generalise `CON-090` to **oriented agent-plus-body sweep clearance**.
- Treat attachment permanence, coupling action, body identity, front offset,
  footprint, sweep geometry and contact exceptions as parameters.
- Replace `CON-100` with `CON-090` in Bonfire Peaks and `COMB-0055`.
- Mark `CON-100` as `Merged` and retain it as a historical alias.
- Update the reviewed Ukrainian registry layer and generated indexes.

## What does not change

- Stephen's Sausage Roll retains fork-mediated sausage contact, cooking and
  exact-return rules; Bonfire Peaks does not acquire them.
- Bonfire Peaks retains reversible pickup/release, carry-conditioned elevation
  and destructive fixed-receiver delivery; Stephen's Sausage Roll does not
  acquire them.
- `CON-011` continues to own ordinary exclusive occupancy and static barriers.
- `CON-101` continues to own support/elevation decisions rather than swept
  clearance.
- Each game and combination retains the same number of active genes.

## Impact

- Stable gene records: unchanged at 490.
- Active genes: 482 → 481.
- Reused active genes: 121 → 122 because `CON-090` gains Bonfire Peaks support.
- Active singleton genes: 361 → 359.
- Active-gene usages: unchanged at 1,031.
- Stephen's Sausage Roll/Bonfire Peaks similarity: `5 / 19 = 0.263158` →
  `6 / 18 = 0.333333`.
- No combination gains another complete supporting genome; recurring
  combination count remains thirteen.

## Decision

- Decision: `Accepted`.
- Rationale: attachment lifetime belongs to the coupling action/state, while
  the Constraint asks the same destination-and-sweep legality question in
  both games.
