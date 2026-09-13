# Taxonomy Change 065: Split the common recoverable-health core from erosion

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-10
- Trigger: card `C-09` of
  [`BATCH_017_FULL_TAXONOMY_AUDIT_001`](../normalisation/BATCH_017_FULL_TAXONOMY_AUDIT_001.md).
- Scope: `SYS-832`, `SYS-836`, new `SYS-852`, their two carriers and affected
  presentation; no later correction enters this unit.

## Current classification

- `SYS-832` joined three Dead Cells transitions: eligible health loss became a
  recoverable bank, outgoing attacks restored health from it, and the bank
  drained with time or was replaced by later damage.
- `SYS-836` independently joined four TEKKEN 8 transitions: declared damage
  became a recoverable bank, outgoing attacks restored health from it, later
  incoming attacks eroded it, and a Rage Art erased it. It also repeated the
  round reset already owned by `SYS-522` and encoded the absence of passive
  drain as if absence were a positive System rule.

The two records therefore duplicated a common recoverable-health lifecycle but
combined it with mutually different expiry rules.

## Detected problem

Both carriers accept the same portable common trace:

1. an actor loses health through an eligible damage class;
2. a declared portion of the loss becomes recoverable rather than immediately
   irrecoverable;
3. the actor makes an eligible outgoing attack; and
4. health returns from that bank, bounded by the bank and health cap.

Dead Cells then removes opportunity continuously after a delay and replaces an
old bank when another hit creates a new one. TEKKEN 8 instead lets later
incoming attacks reduce the bank and lets a declared finisher erase it. Those
post-bank transitions change when recovery remains legal and cannot be folded
into one parameter without hiding different decision rules.

## Evidence and two-way transfer test

- Dead Cells claim `DC-012b` establishes that 80% of recent loss becomes an
  orange recoverable portion, outgoing hits restore a fraction of damage dealt,
  the portion drains after a delay, and later damage replaces the earlier
  portion. This exact behaviour rests on the community-maintained official
  [Dead Cells Wiki mechanics page](https://deadcells.wiki.gg/wiki/Mechanics),
  rechecked 2026-09-10; it remains `Limited` evidence for the carrier-specific
  values. The page refused automated retrieval during this correction, so the
  already accepted static textual evidence and claim ledger were re-audited;
  no new audiovisual evidence was introduced.
- Bandai Namco's official
  [TEKKEN 8 battle-system page](https://tk8.tekken-official.jp/en/battle/system.php)
  and official
  [starter guide](https://en.bandainamcoent.eu/tekken/news/tekken-8-the-guide-start-playing),
  rechecked 2026-09-10, state that aerial, downed and qualifying blocked damage
  creates Recoverable Gauge and that hitting the opponent or forcing a block
  restores it. The battle-system page also states that a landed Rage Art erases
  the opponent's gauge. The current community mechanics page remains the sole
  source for ordinary hit erosion and therefore keeps `SYS-836` `Limited`.
- Dead Cells transfers into the common boundary with broad eligible damage,
  percentage banking and hit-damage-based recovery as parameters.
- TEKKEN 8 transfers with selected source classes, hit-or-block recovery and a
  larger Heat Engager recovery as parameters.

The transfer is symmetric only for bank creation and attack-based recovery.
Timed drain, replacement, hit erosion and finisher erasure fail the two-way test
and therefore remain separate owners.

## Complete lower-ID and adjacent-boundary scan

All 831 lower-ID Active System definitions preceding `SYS-832` were checked
before retaining it as the common-core owner. The closest meaningful
neighbours remain distinct:

- `SYS-165` consumes temporary Block before health; it does not bank lost
  health or return it through outgoing attacks.
- `SYS-319` and `SYS-376` resolve restorative items or their rechargeable
  charges; neither needs eligible prior health loss or offensive contact.
- `SYS-391` restores state at a rest fixture rather than through attacks.
- `SYS-397` earns a separate reserve through direct strikes and later spends
  that reserve by command; health loss is not the capacity of that reserve.
- `SYS-473` maintains a core and outer meter pair rather than a recoverable
  subset of one health loss.
- `SYS-578` owns the continuous health pool and defeat threshold, not the
  temporary recoverability of selected loss.
- `SYS-655` consumes armour before health and never restores lost health
  through an outgoing attack.
- `SYS-737` restores health after a quiet interval, the opposite activity
  condition from counterattacking.
- `SYS-750` accepts an item's pending restorative amount over time; it neither
  banks damage nor requires offensive contact.
- `SYS-820` pays a stock to downgrade lethal defeat, not ordinary recoverable
  damage.

No lower-ID System other than `SYS-832` accepts both carriers without importing
an item, a separate reserve, passive waiting, armour, a lethal-save stock or the
whole health-pool lifecycle.

## Decision

- Generalise `SYS-832` to **Bank eligible health loss as recoverable health and
  regain it by attacking**.
- Treat eligible damage classes, recoverable share, bank cap, qualifying
  outgoing contact and recovery amount as parameters.
- Add `SYS-832` to `GAME-0283`; retain it in `GAME-0282`.
- Narrow `SYS-836` to **Erode or erase recoverable health through later
  incoming attacks** and retain it only in `GAME-0283`.
- Add `SYS-852` for **Expire recoverable health through time or replacement
  damage** and assign it only to `GAME-0282`.
- Keep round adjudication and recoverable-gauge reset in `SYS-522`; do not
  encode the absence of passive drain as another gene.
- Keep `SYS-165`, `SYS-319`, `SYS-376`, `SYS-391`, `SYS-397`, `SYS-473`,
  `SYS-578`, `SYS-655`, `SYS-737`, `SYS-750` and `SYS-820` unchanged.
- Make no lifecycle merge, combination change or family change.

## Genome, combination and comparison impact

- `GAME-0282` grows from 39 to 40 Active genes by adding `SYS-852` while
  retaining generalised `SYS-832`.
- `GAME-0283` grows from 19 to 20 Active genes by adding `SYS-832` while
  retaining narrowed `SYS-836`.
- Neither game has a combination. The exhaustive containment scan creates no
  new supporter, exact signature match or new combination.
- Hades remains `GAME-0282`'s selected lower-ID neighbour at
  `18 / 52 = 0.346154`.
- Street Fighter 6 remains `GAME-0283`'s selected lower-ID neighbour at
  `14 / 26 = 0.538462`.
- Exactly two reviewed signatures change, each through one added independent
  System owner.

## Corpus accounting

- Canonical definitions: 2,455 → 2,456.
- Active definitions: 2,397 → 2,398; inactive definitions remain 58.
- Active System definitions: 830 → 831.
- Active singleton definitions remain 1,757: `SYS-832` ceases to be a
  singleton while new `SYS-852` becomes one. Singleton share becomes
  `1,757 / 2,398 = 0.732694` rounded to six decimals.
- Active game-gene usages: 6,183 → 6,185.
- Games, combinations and families remain 288, 274 and 17.

## Localisation disposition

- `SYS-832`: `corrected` in Ukrainian for the portable two-carrier common
  boundary.
- `SYS-836`: `corrected` for TEKKEN 8's later-attack erosion and erasure only.
- `SYS-852`: `corrected` as the new Dead Cells expiry owner.
- `GAME-0282`, `GAME-0283`, their salience and plain-language records:
  `corrected` in the same unit.
- `SYS-522` and unaffected carrier-local boundaries: `verified`.
- Dead Cells, TEKKEN 8, Prisoners' Quarters, Recoverable Gauge, Heat Engager,
  Rage Art, character, mode and stable-ID names are `retained-with-reason`
  only in game-scoped evidence and examples. No localisation work is deferred.

## Rejection condition

Reopen the three-way split only if a later carrier demonstrates that bank
creation, attack-based recovery and one of the two expiry rules cannot occur or
vary independently after damage class, proportions, timing and move identity
are substituted. A shared coloured health-bar overlay is not enough; the
counterexample must change the legality or settlement of recovery.

## Change history

- 2026-09-10 — accepted as `BATCH_017_TAXONOMY_CORRECTION_009` after a fresh
  complete lower-ID System scan and two-way carrier transfer test.
