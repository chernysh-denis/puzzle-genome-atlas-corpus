# Taxonomy Change 067: Separate charged recovery, earned charge and lock clearance

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-09-13
- Trigger: card `C-11` of
  [`BATCH_017_FULL_TAXONOMY_AUDIT_001`](../normalisation/BATCH_017_FULL_TAXONOMY_AUDIT_001.md).
- Scope: `SYS-035`, `SYS-364`, `SYS-848`, new `SYS-853`, their three
  performance-replenishment carriers, the sole charged-recovery carrier and
  `COMB-0274`; no later normalisation unit enters this commit.

## Current classification

`SYS-848` joined four independently changing transitions in one Sekiro owner:

1. a confirmed in-place recovery consumed one ready charge, restored health
   and returned control to the same live encounter;
2. that recovery applied a separate consecutive-use lock;
3. qualifying combat progress cleared the lock even when charge was already
   present; and
4. idol rest restored the base charge while hostile defeats built an
   additional charge.

The command already belongs to `ACT-452`, while `CON-628` already owns the
joint legality test that requires both ready charge and a cleared lock. The
compound System boundary therefore repeated those owners while preventing the
automatic settlement, charge supply and lock state from transferring
independently.

## Detected problem

The three automatic responsibilities fail an independence test:

- the in-place recovery can settle once from an already ready charge without
  proving how that charge will later be replenished;
- a remaining ready charge can still be unusable while the post-use lock is
  active;
- qualifying combat progress can clear the lock without adding a charge, while
  ordinary hostile defeats can add recovery power independently of the lock;
  and
- checkpoint rest restores the base charge through the already carried
  `SYS-364` rest-and-field-reset transition rather than through the live-combat
  lock lifecycle.

Charge amount, lock state and the source that changes each state therefore
alter future recovery legality separately. Keeping them in one System gene
hides distinct decisions rather than merely compressing terminology.

## Evidence and independence test

- FromSoftware's official
  [PC mechanics manual](https://www.fromsoftware.jp/manual/sekiroshadowsdietwice/win/basic.html),
  rechecked 2026-09-13, states separately that available recovery power may be
  spent to revive the player, that recovery temporarily makes another recovery
  unavailable until enemies are defeated or critical executions are performed,
  and that the base power is replenished by idol rest while the remainder is
  obtained by defeating enemies.
- Sekiro claim `SEK-010` and three separate transition-ledger rows preserve the
  charged settlement, combat-earned lock clearance and combat-earned charge
  replenishment. Claim `SEK-012` separately preserves the idol-rest reset.
- The official Japanese page was retrieved as static text. No video or audio
  was opened, played, heard or analysed for this correction.

The settlement, charge and lock can each change while at least one of the other
two remains fixed. The compound therefore fails the one-gene test.

## Complete lower-ID and all-carrier scan

All 826 lower-ID Active System definitions preceding `SYS-848` were checked.
The closest portable owners resolve as follows:

- `SYS-035` already adds finite future-action supply after an in-session
  performance condition. Dorfromantik quest or placement quality adds tiles,
  Loop Hero hostile defeat can add playable world cards, and Sekiro hostile
  defeat adds power toward an additional recovery charge. The supplied unit,
  partial progress, trigger and later action vary without changing the
  transition, so the three carriers pass the transfer test.
- `SYS-364` already restores declared resources and replenishable items at
  checkpoint rest while repopulating eligible ordinary field encounters. The
  Sekiro base recovery charge remains a resource parameter of that carried
  owner; no second rest-refill gene is needed.
- `SYS-376` spends an equipped item charge and schedules time-based recharge;
  it imports an item effect and cooldown absent from the split boundary.
- `SYS-397` and `SYS-707` replenish broader attack-spent effect reserves
  through direct strikes, not a discrete post-defeat recovery charge earned by
  defeating hostiles.
- `SYS-540` requires spatial pad contact and pad recharge; `SYS-640` resets a
  shared aerial movement budget through ground, wall or hit state.
- `SYS-606`, `SYS-659` and `SYS-732` bind lethal protection or return to prior
  failures, a mode-owned rebirth or an acquired extra life rather than a
  player-confirmed same-position settlement with an independent live lock.
- `SYS-720` probabilistically resets all skill cooldowns; `SYS-798` passively
  regenerates a shared exertion reserve; neither records event-cleared
  consecutive-use prohibition.
- `SYS-820` suspends lethal defeat into a counter-condition window paid from
  carried restorative stock rather than returning control immediately after a
  confirmed recovery.

No lower-ID System owns applying a consecutive-use self-recovery lock and
clearing it through combat progress while keeping charge supply independent.
New `SYS-853` is therefore required.

## Decision

- Generalise `SYS-035` to **Replenish future-action supply through in-session
  performance** and add `GAME-0288` as its third carrier.
- Retain `SYS-364` unchanged for the base recovery charge restored at idol
  rest.
- Narrow `SYS-848` to **Resolve charged in-place self-recovery after lethal
  defeat** and retain it in `GAME-0288`.
- Add `SYS-853` for **Apply and clear a consecutive-use self-recovery lock**
  and assign it only to `GAME-0288`.
- Keep `ACT-452` as the command and `CON-628` as the charge-plus-lock legality
  predicate; neither automatic System transition absorbs them.
- Keep every other reviewed game, family and lifecycle unchanged.

## Genome, combination and comparison impact

- `GAME-0288` grows from 36 to 38 Active genes by adding reused `SYS-035` and
  new `SYS-853` while retaining narrowed `SYS-848` and unchanged `SYS-364`.
- `COMB-0274` grows from 13 to 15 genes because its repeated charged
  continuation requires both performance-earned charge and independently
  cleared lock state. It remains a strict proper subset of `GAME-0288`.
- `COMB-0020` retains `SYS-035` and its existing eleven-gene set; `GAME-0020`,
  `GAME-0028` and their other combination relations retain their signatures.
- The exhaustive containment scan creates no new combination supporter, exact
  signature match or combination collision.
- God of War remains `GAME-0288`'s selected lower-ID neighbour at
  `14 / 49 = 0.285714`.
- No other game signature, combination gene set or selected neighbour changes.

## Corpus accounting

- Canonical definitions: 2,457 → 2,458.
- Active definitions: 2,399 → 2,400; inactive definitions remain 58.
- Active System definitions: 831 → 832.
- Active singleton definitions: 1,758 → 1,759; singleton share becomes
  `1,759 / 2,400 = 0.732917` rounded to six decimals.
- Active game-gene usages: 6,186 → 6,188.
- `SYS-035` support grows from two to three games; `SYS-848` remains a
  singleton and new `SYS-853` is a singleton.
- Games, combinations and families remain 288, 274 and 17.

## Localisation disposition

- `SYS-035`: `corrected` in Ukrainian for the three-carrier future-action
  supply boundary.
- `SYS-848`: `corrected` for the charged in-place settlement only.
- `SYS-853`: `corrected` as the new independent lock lifecycle.
- `GAME-0288`, `COMB-0274`, salience, plain-language and bilingual presentation:
  `corrected` in the same unit.
- `SYS-364`, `ACT-452`, `CON-628`, `GAME-0020`, `GAME-0028`, `COMB-0020` and
  their unaffected carrier-local presentation: `verified` without boundary
  changes.
- Sekiro, Dorfromantik, Loop Hero, Resurrection, Deathblow, Gyoubu, Posture,
  idol, route, product, version and stable-ID names are
  `retained-with-reason` only in scoped evidence and examples. No localisation
  work is deferred.

## Rejection condition

Reopen the split only if a later carrier proves that charged in-place recovery
settlement, performance-earned charge, checkpoint-rest refill and the
event-cleared consecutive-use lock cannot exist or vary independently after
charge count, health, trigger, position, encounter and presentation are
substituted. A shared interface marker or one event changing two states is
insufficient.

## Change history

- 2026-09-13 — accepted as `BATCH_017_TAXONOMY_CORRECTION_011` after a fresh
  complete lower-ID System scan, three-carrier supply transfer test and
  in-carrier independence test.
