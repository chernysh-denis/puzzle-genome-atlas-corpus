# Taxonomy Change 074: Generalise finite-life respawn from vehicle to body

## Status

- Proposal status: `Accepted`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-20
- Trigger: `GAME-0318` Battletoads complete lower-ID scan.
- Scope: wording and support for `SYS-911`; no earlier game signature,
  combination gene set, family membership or lifecycle change.

## Problem

`SYS-911` was isolated from Tank 1990 and named a controlled vehicle even
though its causal boundary is a finite stage-life stock: lethal state removes
the controlled body, one life is spent, and a replacement returns only while
the current stage remains viable. Battletoads Stage 1 supplies the same
transition with an embodied Toad rather than a tank. Creating a second gene
would encode presentation instead of a different rule.

## Accepted change

- Rename the boundary from “controlled vehicle” to “controlled body”.
- Accept either restoration or instantiation at the declared stage return
  point while finite lives and stage viability remain.
- Keep health loss, checkpoint restoration without stock, ally revival,
  Continue after stock exhaustion and protected-object replacement excluded.
- Add Battletoads as a second carrier without changing Tank 1990's signature.

## Complete lower-ID transfer test

- Tank 1990 remains valid: an eligible lethal hit removes the player tank,
  spends one life and creates a replacement at its stage start while lives and
  the eagle remain.
- Battletoads adds an embodied carrier: zero energy spends one life and returns
  the Toad inside the same Stage 1 route while stock remains; no Continue is
  included.
- `SYS-369` remains distinct because it restores an authored checkpoint without
  charging a finite life stock.
- `SYS-638` remains distinct because a blast-zone knockout resets accumulated
  platform-fighter damage and weapon state and directly settles the match on
  final stock.
- `SYS-732` remains distinct because an acquired optional extra-life source
  interrupts battle-royale elimination and settlement.

## Evidence and confidence

Tank 1990's pinned inherited logic and corroborating reimplementation remain
the original direct/corroborated basis. Battletoads' original manual establishes
finite lives and energy categories; two independent written NES guides establish
ordinary three-life entry and Stage 1 life recovery. The broader noun therefore
passes a two-carrier transfer test without weakening the transition.

## Migration and compatibility

- Stable ID `SYS-911` is retained.
- English and Ukrainian wording, parameters and carrier support change.
- No game signature, combination, comparison score or lifecycle changes.
- `GAME-0318` reuses `SYS-911`; `GAME-0313` remains its lower-ID carrier.

## Validation expectation

- Repository validation must report no duplicate active definition.
- The `GAME-0318` comparison must scan all 317 lower-ID signatures.
- Ukrainian wording must keep finite life payment, body replacement, stage
  viability and final-stock terminal distinct from free checkpoint reload.
