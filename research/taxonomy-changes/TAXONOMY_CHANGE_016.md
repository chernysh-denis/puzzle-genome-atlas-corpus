# Taxonomy Change 016: Deprecate the orphaned Street Cred offer gene

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: `2026-08-22`
- Trigger: accepted `GAME_SIGNATURE_MIGRATION_001` removes the only reviewed
  carrier of `SYS-377`.

## Current classification

- Exact wording or stable ID: `SYS-377` — Convert Street Cred into
  offered-world unlocks.
- Files and entries affected: System Behaviour registry, generated indexes,
  active-gene localisation coverage and same-count analysis artifacts.
- Original evidence or rationale: the original broad Cyberpunk 2077 product
  inventory admitted Street Cred offer progression into `GAME-0146`.

## Detected problem

- `SYS-377` would remain `Active` with zero canonical carriers after the
  separately approved GAME-0146 signature migration.
- The public corpus contract requires every active gene to have a reviewed game
  carrier. Keeping an orphan active or weakening that check would misstate the
  accepted registry.
- The mechanical boundary remains evidence-backed as a product feature, but it
  no longer belongs to any admitted game packet.

## Evidence

- Primary sources: official Cyberpunk 2077 Update 2.0 notes retain the product
  fact that Street Cred gates offers.
- Reproducible transitions: none inside the accepted Arasaka critical-path
  packet.
- Analysed games checked: all 153 canonical signatures; no other game carries
  `SYS-377`.
- External systems or literature checked: not required for an orphan-lifecycle
  disposition.
- Counterevidence: none supporting an existing canonical carrier.

## Proposed change

- Old classification: `SYS-377`, lifecycle `Active`.
- Proposed classification: retain `SYS-377` with lifecycle `Deprecated`.
- Definitions and boundaries: unchanged.
- Lifecycle effects: the stable ID leaves active genome encoding and remains
  recoverable for historical compatibility.
- What does not change: no merge target, replacement gene, signature addition,
  module ID or new game.

## Genome and combination impact

- Genes added, deprecated, merged or split: one deprecation, `SYS-377`.
- Games requiring annotation: `GAME-0146` only, already handled by
  `GAME_SIGNATURE_MIGRATION_001`.
- Combinations affected: `COMB-0144` already removes `SYS-377`.
- Novelty claims affected: none.

## Decision

- Decision: accepted as the necessary stable-ID lifecycle consequence of the
  maintainer-approved atomic migration.
- Decided by: maintainer authority for all necessary downstream dependencies,
  applied under the repository's active-carrier invariant.
- Rationale: deprecation preserves evidence and history without admitting an
  out-of-scope mechanic or weakening public corpus validation.
- Implementation links:
  [`GAME_SIGNATURE_MIGRATION_001`](../checkpoints/GAME_SIGNATURE_MIGRATION_001.md).

## Change history

- `2026-08-22`: accepted and implemented in the GAME-0146 migration unit.
