# Taxonomy Change 011: Merge object-named death-currency marks

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-08-21
- Trigger: pre-push audit of `GAME-0150` Hollow Knight: Silksong and
  `GAME-0152` Elden Ring

## Current classification

- `SYS-399` encodes Silksong ordinary death returning Hornet to a Bench,
  storing Rosaries in one recoverable Cocoon and attaching a temporary Silk
  capacity penalty.
- `SYS-410` encodes Elden Ring death returning the Tarnished to an eligible
  Grace or Stake and storing runes in one recoverable spatial mark.
- `CON-352` and `CON-361` separately state that only the latest unrecovered
  Cocoon or rune mark persists and that a later death destroys the old stock.

## Detected problem

The two System records share the same decision-relevant transition: ordinary
death preserves campaign progress, returns the avatar to an eligible checkpoint
and externalises carried spendable currency into one recoverable world mark.
The two Constraint records share the same one-mark replacement predicate.
Checkpoint choice, mark object, currency name, protected banking and the
Silksong-only capacity penalty are parameters, not reasons to split the causal
rule by game vocabulary.

## Evidence

- [`GAME-0150` — Hollow Knight: Silksong](../../knowledge/games/g-l/hollow-knight-silksong.md)
  establishes Bench return, one Rosary Cocoon, replacement loss and the
  Cocoon-linked temporary Silk cap.
- [`GAME-0152` — Elden Ring](../../knowledge/games/a-f/elden-ring.md)
  establishes Grace-or-Stake return, one rune mark and replacement of the old
  mark even when the new carried rune stock is zero.
- Both games preserve retained route or campaign state and exclude
  inventory-wide drops and permanent one-life defeat in the audited scope.

## Change

- Generalise `SYS-399` to checkpoint return with one recoverable
  death-currency mark and parameterise checkpoint options, currency, mark
  object, recovery interaction and optional capacity penalty.
- Merge `SYS-410` into `SYS-399` and retain `SYS-410` as a lifecycle alias.
- Generalise `CON-352` to one unrecovered death-currency mark with replacement
  loss and parameterise old/new stock plus protected banking.
- Merge `CON-361` into `CON-352` and retain `CON-361` as a lifecycle alias.
- Replace both merged IDs in Elden Ring's genome, combination, salience and
  public presentation, then recalculate its exhaustive comparison.

## What does not change

- Silksong's temporary Silk cap remains represented as an optional parameter
  of `SYS-399`; Elden Ring does not gain that effect.
- Elden Ring's Grace-or-Stake choice and Silksong's fixed Bench return remain
  separate parameter values.
- Currency protected in a Silksong String and non-currency inventory remain
  outside the dropped stock.
- Neither game changes its scoped objective or total genome size.

## Impact

- Active gene count decreases by two, from 1,298 to 1,296.
- Gene usages remain 2,626 because Elden Ring replaces each merged ID with its
  surviving shared gene.
- Reused genes increase from 310 to 312 and singletons decrease from 988 to
  984.
- Elden Ring's nearest complete genome changes from Monster Hunter Wilds to
  Hollow Knight: Silksong at `12 / 55 = 0.218182`; `COMB-0150` remains a
  36-gene strict subset of its 45-gene genome.

## Decision

- Decision: `Accepted`.
- Decided by: repository maintainer-authorised pre-push audit correction.
- Rationale: checkpoint selection, currency identity, mark presentation and
  optional recovery penalties are parameters of the same death-risk loop.
- Implementation links: `SYS-399`, `SYS-410`, `CON-352`, `CON-361`,
  `GAME-0150`, `GAME-0152` and `COMB-0150`.
