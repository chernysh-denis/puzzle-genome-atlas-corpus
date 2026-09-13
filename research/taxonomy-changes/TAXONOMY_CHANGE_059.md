# Taxonomy Change 059: Separate stagger-window access from combat settlement

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-09-10
- Trigger: card `C-03` of
  [`BATCH_017_FULL_TAXONOMY_AUDIT_001`](../normalisation/BATCH_017_FULL_TAXONOMY_AUDIT_001.md),
  inherited as card `C-14` from the first full taxonomy duplicate audit.
- Scope: `ACT-419`/`ACT-426`, `CON-589`/`CON-595`,
  `INF-295`/`INF-304`, `GAME-0249` and `COMB-0247`; the five other
  command/disclosure carriers and four other legality carriers keep their
  signatures.

## Current classification

The three pairs repeat one typed boundary at Action, Constraint and
Information level:

1. A living hostile enters a temporary stagger or equivalent disrupted state.
2. Local feedback exposes one contextual close command.
3. The command is legal only while the target remains alive, reachable and in
   that state.
4. The player commits the prompted close action before the opportunity closes.

The higher-ID Resident Evil 4 records attempted to distinguish a
non-guaranteed close follow-up from a defeating finisher. That distinction is a
real difference between product outcomes, but it was placed in the wrong gene
types. Defeat, damage, knockback and recovery drops are System settlement. They
do not change the player operation, the legality predicate or the information
available before commitment.

## Primary settlement evidence

- Bethesda's official [single-player campaign
  account](https://bethesda.net/en-US/news/inside-doom%27s-brutally-fast-single-player-campaign),
  accessed 2026-09-10, calls Glory Kills finishing moves, contrasts them with a
  final shot, and states that they produce additional health and ammunition.
- Bethesda's official [Glory Kill
  feature](https://bethesda.net/en-EU/news/the-guts-and-gore-of-doom-glory-kills),
  accessed 2026-09-10, describes a position-dependent close-quarter finishing
  move with a strict short duration.
- Capcom's official [Resident Evil 4 release
  account](https://news.capcomusa.com/2023/03/24/resident-evil-4-is-out-now/),
  accessed 2026-09-10, describes careful aim stunning enemies and opening
  follow-up melee moves. The same primary text separately calls a ground-knife
  action a way to dispatch certain enemies, so it does not equate every
  stagger follow-up with guaranteed defeat.
The existing reviewed game ledgers remain the evidence for the other carriers:
DOOM Eternal, Batman: Arkham Asylum, God of War and Sekiro. Their game-scoped
finisher or execution descriptions remain valid instances of the broader typed
boundaries.

## Two-way transfer test

### Action

- `ACT-419` and `ACT-426` both require the player to accept a separately
  exposed close command on a living, reachable, temporarily staggered hostile.
- Removing the words `finisher` and `follow-up` changes no input, target,
  timing or positional decision.
- Whether the accepted attack defeats, damages, knocks back or affects nearby
  actors is downstream resolution and remains outside the Action boundary.

### Constraint

- `CON-589` and `CON-595` both require the same live target, temporary stagger
  state, reach and still-open opportunity.
- Recovery, distance or prior defeat closes either command.
- Guaranteed defeat is not a legality predicate and therefore cannot justify
  two Constraint records.

### Information

- `INF-295` and `INF-304` both expose that the temporary stagger-window close
  command is currently available.
- Neither display has to guarantee the resulting damage or defeat. Those
  effects can vary after the same pre-commit disclosure.
- Presentation, prompt, colour and product-specific finisher vocabulary remain
  parameters.

## Decision

- Generalise `ACT-419` to **Perform a prompted close action on a staggered
  hostile**. Merge `ACT-426` into it.
- Generalise `CON-589` to **Prompted close action requires a live reachable
  stagger window**. Merge `CON-595` into it.
- Generalise `INF-295` to **Expose a temporary contextual close-action
  opportunity**. Merge `INF-304` into it.
- Preserve all three higher IDs as historical aliases. They may not enter a
  current signature, combination or Ukrainian Active registry.
- Keep source, damage, knockback, target defeat, resource drops and multi-actor
  effects in the relevant System behaviours and game-scoped parameters.

## Genome and combination impact

- `GAME-0249` replaces the three merged IDs one-for-one with `ACT-419`,
  `CON-589` and `INF-295`. Its genome remains 42 Active genes.
- Its current decomposition becomes eleven game-introduced Active genes and
  thirty-one reused genes. The initial three result-specific records are no
  longer counted as new Active genes.
- `COMB-0247` performs the same three one-for-one substitutions and remains a
  strict seventeen-gene subset of `GAME-0249`.
- The other five `ACT-419`/`INF-295` carriers and four `CON-589` carriers keep
  their stable IDs and signatures. No other reviewed signature changes.
- Global comparison and combination-support recomputation is required after
  migration because formerly separate IDs can now contribute shared genes.

## Corpus accounting

- Canonical definitions: 2,453 → 2,453.
- Active definitions: 2,399 → 2,396.
- Inactive definitions: 54 → 57.
- Active Actions: 443 → 442; Active Constraints: 612 → 611; Active
  Information genes: 328 → 327.
- Active singleton definitions: 1,762 → 1,759; singleton share becomes
  `1,759 / 2,396 = 0.734140`.
- Game gene slots remain 6,179. Games, combinations and families remain 288,
  274 and 17.

## Localisation disposition

- `ACT-419`, `CON-589` and `INF-295`: `corrected` in Ukrainian against the
  settlement-neutral English boundaries.
- `ACT-426`, `CON-595` and `INF-304`: removed from the current Ukrainian
  Active registry because they are lifecycle aliases.
- `GAME-0249`, `COMB-0247`, salience and plain-language records: `corrected`
  by one-for-one stable-ID replacement; the game-scoped close-follow-up wording
  remains natural and mechanically accurate.
- All unaffected carrier-local wording: `verified`; official product names,
  `Glory Kill`, `Chapter 1`, stable IDs and interface names are
  `retained-with-reason`.

## Rejection condition

Reopen any merge only if a later carrier demonstrates a decision-relevant
difference in the pre-commit command, live/reach/stagger legality or disclosed
opportunity that cannot be expressed as target, prompt, range, timing or
presentation parameters. A different damage, defeat, knockback or reward
settlement alone does not reopen these Action, Constraint or Information
boundaries; it belongs to a System review.

## Change history

- 2026-09-10 — accepted as `BATCH_017_TAXONOMY_CORRECTION_003` after the
  Batch 017 full audit, primary settlement review and complete carrier test.
