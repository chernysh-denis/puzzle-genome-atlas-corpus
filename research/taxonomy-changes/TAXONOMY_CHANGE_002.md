# Taxonomy Change 002: Merge supplied-head commitment constraints

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-08-12
- Trigger: `REGISTRY_NORMALISATION_001`

## Current classification

- `CON-039` combined mandatory Pipe Dream queue order with fixed orientation.
- `CON-057` combined mandatory Dorfromantik supply order with free orientation.
- `ACT-020` already excludes rotation for Pipe Dream placement.
- `ACT-026` already includes orientation choice for Dorfromantik placement.

## Detected problem

The two Constraint records differ only by transform permission, but that
permission is already represented by their Action genes. Keeping two
game-specific constraints duplicates the same decision restriction: later
supplied elements are preview-only until the current head is committed.

## Evidence

- [`GAME-0016`](../../knowledge/games/m-r/pipe-mania.md) must place the bottom
  dispenser piece next and cannot select, store or discard a later piece.
- [`GAME-0020`](../../knowledge/games/a-f/dorfromantik.md) must place the current
  tile next and cannot exchange, store or discard it, although `ACT-026`
  permits rotation.
- Both games already reuse `SYS-024` for sequence advance and `INF-005` for
  exact successor preview. Constraint identity should likewise follow the
  shared commitment rule rather than orientation.

## Change

- Generalise `CON-039` to **Mandatory supplied-head commitment**.
- Add Dorfromantik as corroborating evidence for `CON-039`.
- Replace `CON-057` with `CON-039` in `GAME-0020` and `COMB-0020`.
- Mark `CON-057` as `Merged` and retain it as a historical alias.
- Preserve `ACT-020` and `ACT-026`; they continue to encode fixed-orientation
  placement versus player-selected orientation.

## What does not change

- No game gains or loses a decision-relevant rule.
- Every complete genome and combination remains the same size.
- The six gene types remain unchanged.
- No novelty claim is created.

## Impact

- Active genes: 198 → 197.
- Reused active genes: 30 → 31.
- Active singleton genes: 168 → 166.
- Total active gene usages in game signatures: unchanged at 302.
- Dorfromantik / Pipe Dream Jaccard similarity: `5 / 24 = 0.208333` →
  `6 / 23 = 0.260870`; Pipe Dream becomes Dorfromantik's unique near match.
- Combination reuse: unchanged; `COMB-0016` and `COMB-0020` still have
  different decision structures and neither becomes a subset of a second
  complete genome.

## Decision

- Decision: `Accepted`.
- Rationale: one shared Constraint plus distinct Action genes is the smallest
  representation that preserves both games' actual choices.
