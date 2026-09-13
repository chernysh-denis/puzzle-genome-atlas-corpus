# Taxonomy Change 063: Separate remote mount call from direct riding

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-10
- Trigger: card `C-07` of
  [`BATCH_017_FULL_TAXONOMY_AUDIT_001`](../normalisation/BATCH_017_FULL_TAXONOMY_AUDIT_001.md),
  inherited from card `C-20` of the first full taxonomy audit.
- Scope: `ACT-271`, `ACT-348`, their two carriers and combinations; no other
  signature may change.

## Confirmed compound boundary

`ACT-271` joined two independent player commands in Red Dead Redemption 2. A
whistle first asks the persistent owned horse to approach Arthur. Only after
the horse is reachable can Arthur mount it, steer its movement directly and
dismount. The first command changes the mount's approach state without
transferring control; the second transfers embodied movement authority while
the actor is mounted.

`ACT-348` already owned the latter operation in Mount & Blade II: Bannerlord.
Its original battle-horse wording encoded carrier and context parameters that
do not change the player's Action. Persistence, bond, cores and saddle cargo
belong to System, Constraint and Information genes in the Red Dead Redemption
2 signature; battle context and weapon access are likewise not discriminators
of mounting and direct riding.

## Evidence and transfer test

- Red Dead Redemption 2 claim `RDR2-003` is Corroborated/High evidence that
  Arthur can call the current saddled horse toward him, then separately mount,
  directly ride and dismount it. Rockstar's official Companion manual listing
  and Story Mode material are primary sources `P4` and `P6`; the maintained
  horse transition guide is reproducible source `S3`.
- Mount & Blade II: Bannerlord claim `BANNERLORD-002`, its transition ledger and
  official product source `P2` establish riding as direct first/third-person
  embodied control of an available horse inside the bounded tutorial packet.
- The correction changes the abstraction of accepted observations, not build,
  platform, ruleset, route or direct-play claims. No audiovisual evidence is
  introduced.

The cross-carrier test for the residual riding operation passes: the controlled
actor is beside an available rideable creature; mounting begins direct control
of its movement while the actor remains embodied on it; dismounting ends that
control. Horse identity, gait, combat use, persistence and attached inventories
are parameters or separate genes.

The call operation does not transfer to Bannerlord's packet because no separate
remote command to an owned persistent mount is evidenced there. It therefore
remains the sole-carrier `ACT-271` boundary.

## Lower-ID and adjacent-boundary scan

All 270 lower-ID Action definitions were checked before retaining `ACT-271` in
its narrowed form. The closest adjacent boundaries remain distinct:

- `ACT-197` orders or triggers a partner's contextual ability; it does not ask a
  persistent owned mount to approach as a precursor to later mounting.
- `ACT-201` enters and operates a road vehicle; its vehicle carrier and driving
  interaction do not subsume rideable-creature mounting.
- `ACT-243` calls and rides a target-routed field mount. Its defining command
  commits a destination and delegates route traversal, changing player
  authority rather than merely bringing a mount into reach.
- `ACT-247` uses a dedicated item-mediated invocation to introduce or recall an
  absent spectral mount. Bandai Namco's official
  [Elden Ring starter guide](https://en.bandainamcoent.eu/elden-ring/news/elden-ring-starter-guide-tips-know-playing-the-game)
  documents the Spectral Steed Whistle as the summon carrier and the mounted
  movement, jump and dismount controls. That invocation boundary is not the
  remote approach of an already present persistent mount and is not plain
  mounting of an available mount.

No existing Action combines only the remote-approach predicates of `ACT-271`.
No lower-ID Action can replace the portable mounting operation in `ACT-348`
without importing a distinct carrier or authority transition.

## Decision

- Narrow `ACT-271` to **Call a persistent owned mount toward the controlled
  actor**. It owns the remote approach command only.
- Generalise `ACT-348` to **Mount, directly ride and dismount an available
  mount**. It owns the portable residual operation across both carriers.
- Add `ACT-348` to `GAME-0165` and `COMB-0163`.
- Keep `GAME-0194` and `COMB-0192` on `ACT-348`; their gene sets do not change.
- Keep `ACT-243` and `ACT-247` unchanged as adjacent, authority-distinct
  operations.
- Do not create, merge, split, deprecate or make inactive any gene ID.

## Genome, combination and comparison impact

- `GAME-0165` grows from 54 to 55 Active genes. `COMB-0163` grows from 44 to 45
  and remains a strict subset. Grand Theft Auto V remains the selected lower-ID
  neighbour; its unchanged 28-gene intersection now scores
  `28 / 75 = 0.373333`.
- `GAME-0194` remains at 31 Active genes. `COMB-0192` remains at 28 and remains
  a strict subset. Skyrim Special Edition remains its selected lower-ID
  neighbour at `12 / 46 = 0.260870`.
- The complete deterministic comparison migration changes no selected
  neighbour; the combination-support check confirms both subsets.
- No other game signature or combination gene set changes.

## Corpus accounting

- Canonical definitions remain 2,455.
- Active definitions remain 2,398; inactive definitions remain 57.
- Active singleton definitions: 1,760 → 1,759; singleton share becomes
  `1,759 / 2,398 = 0.733528`.
- Active game-gene usages: 6,182 → 6,183.
- Games, combinations and families remain 288, 274 and 17.
- Earlier reviewed signatures changed: `1`, exactly `GAME-0165`.

## Localisation disposition

- `ACT-271` and `ACT-348`: `corrected` to preserve the separated portable
  boundaries in Ukrainian.
- `GAME-0165`, `COMB-0163`, their salience and plain-language cards:
  `corrected` for the added residual riding owner.
- `GAME-0194`, `COMB-0192`, its salience and `ACT-348` plain-language card:
  `corrected` for the generalised interpretation without a signature change.
- All unaffected carrier-local translations: `verified`.
- Red Dead Redemption 2, Mount & Blade II: Bannerlord, Elden Ring, Arthur,
  whistle, horse, Story Mode, Campaign and stable identifiers remain
  `retained-with-reason` only in scoped evidence, examples and product
  presentation. No translation work is deferred.

## Rejection condition

Reopen `ACT-271` only if a later carrier proves that a remote approach command
cannot be represented independently of mounting. Reopen `ACT-348` only if
mounting, direct riding and dismounting cannot transfer without one of the
rejected persistence, cargo, combat or creature-identity predicates. Shared
horse vocabulary or adjacency in one control sequence alone is insufficient to
recombine the Actions.

## Change history

- 2026-09-10 — accepted as `BATCH_017_TAXONOMY_CORRECTION_007` after the
  split-first prerequisite and two-carrier residual transfer test.
