# Taxonomy Change 004: Merge pairwise collision-merge compatibility

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-08-12
- Trigger: `REGISTRY_NORMALISATION_002` singleton boundary-cluster audit

## Current classification

- `CON-002` allowed only equal current values to merge in 2048.
- `CON-037` allowed the complementary Threes base pair `1 + 2` and equal pairs
  from rank `3` upward.
- Both constraints governed eligibility for the shared automatic transition
  `SYS-002`, which replaces a compatible colliding pair with one output.

## Detected problem

The records encoded two values of one compatibility relation as two Constraint
genes. Equality-only versus a declared complementary base pair changes which
pairs are legal, but not the predicate's subject, trigger, timing or
consequence. The existing `SYS-002` already treats the compatibility relation
as a parameter while preserving the shared collision-merge transition.

Keeping both Constraint IDs therefore duplicated a ruleset parameter. The
actual 2048/Threes differences remain represented by maximal versus one-step
movement, spawn eligibility, preview and objective genes.

## Evidence

- [`GAME-0001` — 2048](../../knowledge/games/0-9/2048.md) admits equal-value
  collision pairs.
- [`GAME-0015` — Threes](../../knowledge/games/s-z/threes.md) admits one
  complementary base pair plus equality at higher ranks.
- Both games use `SYS-002`; neither exposes a separate player action, timing
  phase or state consequence for testing compatibility.

## Change

- Generalise `CON-002` to declared pairwise merge compatibility.
- Treat equality-only, complementary base pairs and rank thresholds as
  parameters of the compatibility relation.
- Replace `CON-037` with `CON-002` in Threes and `COMB-0015`.
- Mark `CON-037` as `Merged` and retain it as a historical alias.
- Recompute the 2048/Threes comparison and generated indexes.

## What does not change

- Threes retains fourteen active genes and `COMB-0015` retains nine genes.
- `SYS-002` continues to own collision-triggered replacement, not eligibility.
- `SYS-001`/`SYS-023`, `CON-038`, `INF-002`/`INF-010` and the objective genes
  preserve the two games' decision-relevant differences.
- No gene type, combination role or novelty claim changes.

## Impact

- Stable gene records: unchanged at 300.
- Active genes: 298 → 297.
- Reused active genes: 66 → 67 because `CON-002` gains a second supporter.
- Active singleton genes: 232 → 230.
- Active-gene usages: unchanged at 546.
- 2048/Threes Jaccard similarity: `10 / 18 = 0.555556` →
  `11 / 17 = 0.647059`; it becomes the strongest current pair.

## Decision

- Decision: `Accepted`.
- Rationale: one parameterised eligibility predicate plus the shared automatic
  transition is the smallest representation that preserves both rulesets.
