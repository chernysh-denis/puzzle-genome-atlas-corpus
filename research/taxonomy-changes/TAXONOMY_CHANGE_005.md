# Taxonomy Change 005: Merge binary line cardinality into exact line aggregate

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-08-14
- Trigger: `REGISTRY_NORMALISATION_003` full-corpus boundary audit

## Current classification

- `CON-109` required every declared Hexologic line to reach one exact sum of
  assigned numeric cell values.
- `CON-116` required every Tents row and column to contain one exact number of
  cells assigned the selected binary state.
- In both records, one position shared by multiple lines contributed the same
  current assignment independently to every line containing it.

## Detected problem

The records encoded the value domain twice. A count of selected binary cells is
the sum of their indicator values: selected contributes `1`, unselected
contributes `0`. Changing the domain from `{1, 2, 3}` pips to `{0, 1}` occupancy
does not change the constraint's subject, trigger, overlap semantics, completion
timing or exact-equality consequence.

The distinction also failed the transfer test. Substituting the Tents binary
domain and row / column membership into `CON-109` reproduces every line-quota
decision. Substituting Hexologic's pip domain into the old `CON-116` title makes
the word “cardinality” inaccurate, but the underlying exact aggregate remains
unchanged. The narrow Tents record is therefore a parameter-specific duplicate.

## Evidence

- [`GAME-0062` — Hexologic](../../knowledge/games/g-l/hexologic.md) assigns
  values in `{1, 2, 3}` to cells shared by horizontal and diagonal equations.
- [`GAME-0072` — Tents](../../knowledge/games/s-z/tents.md) assigns binary
  occupancy indicators to cells shared by one row and one column quota.
- Both require simultaneous exact equality across intersecting declared lines.
  Neither record owns ordered runs, local vertex / face degree or matching.

## Change

- Generalise `CON-109` to **overlapping exact line-aggregate satisfaction**.
- Treat numeric domain, selected-state indicator and line topology as
  parameters.
- Replace `CON-116` with `CON-109` in Tents and `COMB-0072`.
- Mark `CON-116` as `Merged` and retain it as a historical alias.
- Update the reviewed Ukrainian registry layer and generated indexes.

## What does not change

- Tents retains eight active genes and `COMB-0072` retains six genes.
- `CON-117` still owns eight-neighbour tent separation.
- `CON-118` still owns adjacency-constrained one-to-one tree matching.
- `CON-018` remains ordered run satisfaction rather than an aggregate total.
- `CON-114` and `CON-126` remain local graph-incidence constraints rather than
  overlapping declared-line equations.
- No gene type, combination role or novelty claim changes.

## Impact

- Stable gene records: unchanged at 490.
- Active genes: 487 → 486.
- Reused active genes: 117 → 118 because `CON-109` gains Tents support.
- Active singleton genes: 370 → 368.
- Active-gene usages: unchanged at 1031.
- Hexologic/Tents Jaccard similarity: `5 / 11 = 0.454545` →
  `6 / 10 = 0.600000`; the new shared gene states the real common line-equation
  structure while clue presentation, separation and matching remain distinct.

## Decision

- Decision: `Accepted`.
- Rationale: one parameterised exact-aggregate predicate is the smallest
  representation that preserves both rulesets and their decision boundaries.
