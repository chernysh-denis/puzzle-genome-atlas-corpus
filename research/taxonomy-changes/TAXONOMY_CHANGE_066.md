# Taxonomy Change 066: Split hostile stability from remaining executions

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-09-10
- Trigger: card `C-10` of
  [`BATCH_017_FULL_TAXONOMY_AUDIT_001`](../normalisation/BATCH_017_FULL_TAXONOMY_AUDIT_001.md).
- Scope: `INF-334`, new `INF-335`, their sole carrier and `COMB-0274`; no
  later correction enters this unit.

## Current classification

`INF-334` joined two disclosures on one Sekiro combat surface:

1. a continuously changing Posture state that can recover away from its break
   threshold; and
2. a discrete Deathblow-marker count that states how many critical executions
   remain before a protected hostile is finally defeated.

The first disclosure informs whether to maintain pressure now. The second
informs whether the next accepted execution is intermediate or terminal. A
shared screen position does not make those questions one Information gene.

## Detected problem

The compound boundary could not transfer either disclosure independently:

- an ordinary engaged hostile can expose a breakable Posture state without
  requiring a multi-execution defeat sequence; and
- after one accepted Deathblow on a protected hostile, the remaining marker
  still communicates another required execution even when Posture has reset
  and the pressure cycle must begin again.

The two displays also have different owners around them. `SYS-409` owns
threshold crossing into a temporary critical opening, `INF-295` exposes that
opening, `SYS-847` owns consumption of sequential execution requirements, and
the split Information genes report the state needed to choose between those
transitions without duplicating them.

## Evidence and independence test

- FromSoftware's official
  [PC mechanics manual](https://www.fromsoftware.jp/manual/sekiroshadowsdietwice/win/basic.html),
  rechecked 2026-09-10, separately describes enemy Posture damage, recovery and
  break; then states that strong enemies display Deathblow markers above the
  health gauge and require as many Deathblows as the displayed count.
- The official
  [PC advanced-action manual](https://www.fromsoftware.jp/manual/sekiroshadowsdietwice/win/action2.html),
  rechecked 2026-09-10, separately requires every Deathblow marker to be
  consumed before the finishing Deathblow is accepted.
- Sekiro claim `SEK-007` and the transition ledger establish the live Posture
  pressure-and-recovery decision. Claim `SEK-009` establishes the displayed
  marker sequence and the distinction between an intermediate and final
  Deathblow.
- No video or audio was opened, played, heard or analysed for this correction.

Posture direction, recovery rate and break threshold can vary without changing
the discrete execution count. Marker form and count can vary without changing
how stability accumulates or recovers. The displays therefore fail the
one-gene independence test and require separate Information owners.

## Complete lower-ID and adjacent-boundary scan

All 326 lower-ID Active Information definitions preceding `INF-334` were
checked before retaining it as the stability owner and allocating `INF-335`.
The closest meaningful boundaries remain distinct:

- `INF-129` reports the number of living match participants and public
  eliminations, not repeated executions required on one surviving hostile.
- `INF-141` is a compound turn-based HUD with order, Action Points, party state
  and a selected target's Break state; reusing it would import a turn queue and
  party command surface absent from Sekiro.
- `INF-156` highlights wounds and breakable body regions, not a scalar
  recoverable stability state.
- `INF-157` reports a hunt's faint allowance and observable monster condition,
  not executions still owed by the target.
- `INF-210` exposes accumulated round wins inside a paired duel HUD; a round
  marker settles one match round rather than one requirement on the same live
  hostile.
- `INF-254` exposes remaining participant stocks across knockout and respawn,
  not critical executions on an unchanged protected actor.
- `INF-282` and `INF-329` expose challenge or task-component progress outside
  the live hostile-specific execution boundary.
- `INF-295` exposes a temporary contextual close-action opportunity while
  explicitly withholding whether taking it will defeat the target.
- `INF-313` exposes regional body degradation and capability contribution,
  not the target's aggregate stability threshold.
- `INF-318` exposes remaining guardian health, which can change independently
  of both Posture and Deathblow count.
- `INF-333` marks which units still have an action in a round and deliberately
  withholds their order; it is not a defeat requirement.

No lower-ID Information gene accepts either new boundary without importing a
different actor set, temporal unit, interface purpose or progress object.

## Decision

- Narrow `INF-334` to **An engaged hostile's breakable stability state is
  visible**.
- Add `INF-335` for **Remaining critical executions required to defeat a
  protected hostile are visible**.
- Treat bar direction, recovery, threshold, marker shape, marker count and
  visibility timing as parameters of their respective disclosures.
- Retain both genes in `GAME-0288` and in the strict interaction subset
  `COMB-0274`.
- Keep `INF-129`, `INF-141`, `INF-156`, `INF-157`, `INF-210`, `INF-254`,
  `INF-282`, `INF-295`, `INF-313`, `INF-318`, `INF-329` and `INF-333`
  unchanged.
- Keep `SYS-409`, `SYS-847` and every lifecycle unchanged.

## Genome, combination and comparison impact

- `GAME-0288` grows from 35 to 36 Active genes by adding `INF-335` while
  retaining narrowed `INF-334`.
- `COMB-0274` grows from 12 to 13 genes and remains a strict proper subset of
  `GAME-0288`; both disclosures belong because the interaction requires the
  player to read pressure toward a break and whether the resulting execution
  will settle the guardian.
- The exhaustive containment scan creates no new supporter, exact signature
  match or combination collision.
- God of War remains `GAME-0288`'s selected lower-ID neighbour at
  `14 / 47 = 0.297872`.
- No other game signature, combination gene set or selected neighbour changes.

## Corpus accounting

- Canonical definitions: 2,456 → 2,457.
- Active definitions: 2,398 → 2,399; inactive definitions remain 58.
- Active Information definitions: 327 → 328.
- Active singleton definitions: 1,757 → 1,758; singleton share becomes
  `1,758 / 2,399 = 0.732805` rounded to six decimals.
- Active game-gene usages: 6,185 → 6,186.
- Games, combinations and families remain 288, 274 and 17.

## Localisation disposition

- `INF-334`: `corrected` in Ukrainian for the independently visible Posture
  state and its pressure decision.
- `INF-335`: `corrected` as the new remaining-execution disclosure.
- `GAME-0288`, `COMB-0274`, salience and plain-language presentation:
  `corrected` in the same unit.
- `INF-295`, `SYS-409`, `SYS-847` and unaffected carrier-local records:
  `verified` without boundary changes.
- Sekiro, Posture, Deathblow, Gyoubu, product, route and stable-ID names are
  `retained-with-reason` only in game-scoped evidence and examples. No
  localisation work is deferred.

## Rejection condition

Reopen the split only if a later carrier proves that the current breakable
stability display and remaining critical-execution count cannot exist, update
or change independently after hostile identity, thresholds, marker form and
counts are substituted. Co-location in one HUD is insufficient.

## Change history

- 2026-09-10 — accepted as `BATCH_017_TAXONOMY_CORRECTION_010` after a fresh
  complete lower-ID Information scan and an in-carrier independence test.
