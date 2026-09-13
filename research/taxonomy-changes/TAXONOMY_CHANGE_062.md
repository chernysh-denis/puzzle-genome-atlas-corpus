# Taxonomy Change 062: Separate portable-light drain from recovery

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Date: 2026-09-10
- Trigger: card `C-06` of
  [`BATCH_017_FULL_TAXONOMY_AUDIT_001`](../normalisation/BATCH_017_FULL_TAXONOMY_AUDIT_001.md),
  inherited from card `C-22` of the first full taxonomy audit.
- Scope: `ACT-409`, `SYS-754`, `SYS-791`, their two carriers and combinations,
  plus one Action and one System extraction; no other signature may change.

## Confirmed compound boundary

`SYS-754` and `SYS-791` each joined the same active drain transition to a
different recovery rule. In both carriers, active personal portable
illumination converts positive bounded internal charge into a local light field
and decreases that charge. Half-Life then restores charge automatically while
the device is inactive. Alien: Isolation instead requires a separate player
command whose accepted settlement irreversibly consumes one carried battery.

The shared transition is portable; the recovery transitions are not
interchangeable. Leaving either original compound intact would duplicate the
drain boundary, while merging the compounds would falsely equate automatic
off-state recovery with finite-stock manual refill.

## Evidence and transfer test

- Half-Life claim `HL1-009` is Direct/High evidence that the HEV flashlight is
  manually toggled, drains visible reserve while active and restores that
  reserve automatically while inactive. Valve's SDK and preserved original
  manual are already recorded as primary sources `P3` and `P8` in the reviewed
  game ledger.
- Alien: Isolation claim `AI-009` is Direct/High evidence that its flashlight is
  manually toggled, drains separate charge and consumes one carried battery to
  refill. The publisher-linked current manual is already recorded as primary
  source `P3` in that reviewed game ledger.
- Both ledgers keep the command, System mutation and legality layers observable:
  `ACT-409` owns only toggling; `CON-601` owns positive-charge emission and
  refill eligibility; the current change separates the remaining drain,
  recovery command and recovery settlement.
- The correction changes abstraction of accepted observations, not build,
  platform, ruleset or route claims. No new audiovisual evidence or direct-play
  claim is introduced.

The two-carrier transfer test passes for `SYS-754`: both devices are personal,
portable and player-toggled; active state plus positive internal charge emits a
bounded local light field; continued emission decreases that charge; inactive
or empty state ends the drain. Device identity, rate, cap and empty response are
parameters.

The recovery tests then diverge cleanly:

1. Half-Life alone supports automatic charge restoration while inactive without
   consuming a carried unit.
2. Alien: Isolation alone supports a player-commanded refill whose accepted
   System result consumes one compatible carried battery and raises internal
   charge.
3. Neither recovery rule is required to describe the shared active drain.

## Manual-command lower-ID scan

All 452 lower-ID Action definitions were checked before adding an Action owner.
The closest boundaries remain distinct:

- `ACT-131` consumes a carried item for its immediate external or bodily effect;
  it does not transfer a replacement unit into an existing portable device.
- `ACT-183` reloads reserve ammunition into an active magazine-fed weapon and
  temporarily gives up fire readiness; the target carrier and combat readiness
  are defining predicates absent from the flashlight refill.
- `ACT-199` transfers or equips a compatible found item into carried state; it
  does not spend already carried stock to change another device's internal
  charge.
- `ACT-341` operates a reachable authored world object; the flashlight is
  carried personal equipment rather than the addressed world fixture.
- `ACT-435` replaces a finite filter in breathing equipment and restores usable
  exposure duration. A discarded cartridge, hazardous-atmosphere protection
  and replacement state are defining predicates that the battery-to-charge
  refill does not share.

No lower-ID Action preserves the portable-device target, finite carried input
and explicit refill command without importing a different carrier or result.
The manual command therefore requires new `ACT-453`.

## Decision

- Generalise `SYS-754` to **Convert bounded device charge into portable
  illumination**. It owns active charge-to-light drain and now has both
  carriers.
- Narrow `SYS-791` to **Refill portable illumination from finite carried battery
  stock**. It owns only the accepted System settlement in Alien: Isolation.
- Add `ACT-453` — **Commit one finite carried unit to refill a portable
  device** — for the separate player command in Alien: Isolation.
- Add `SYS-851` — **Automatically recharge inactive portable illumination** —
  for Half-Life's off-state recovery.
- Clarify `ACT-409` so toggling excludes `ACT-453` and does not claim the charge
  transitions.
- Add `SYS-851` to `GAME-0239` and `COMB-0237`.
- Add `ACT-453` and `SYS-754` to `GAME-0257` and `COMB-0255`; retain `SYS-791`
  there under its narrowed boundary.
- Keep `CON-601` unchanged as the two-predicate legality owner. No gene is
  merged, deprecated or made inactive.

## Genome, combination and comparison impact

- `GAME-0239` grows from 27 to 28 Active genes. `COMB-0237` grows from 16 to 17
  and remains a strict subset. Half-Life 2 remains the selected lower-ID
  neighbour; the unchanged 18-gene intersection now scores
  `18 / 34 = 0.529412`.
- `GAME-0257` grows from 32 to 34 Active genes. `COMB-0255` grows from 28 to 30
  and remains a strict subset. BioShock Remastered becomes the selected
  lower-ID neighbour at `13 / 53 = 0.245283`, narrowly exceeding Fallout 4
  after the signature gains the separately represented drain and refill
  command.
- No other game signature or combination gene set changes. A full deterministic
  comparison migration and combination-support check remain mandatory.

## Corpus accounting

- Canonical definitions: 2,453 → 2,455.
- Active definitions: 2,396 → 2,398; inactive definitions remain 57.
- Action definitions: 452 → 453; Active Actions: 442 → 443.
- System definitions: 850 → 851; Active Systems: 830 → 831.
- Active singleton definitions: 1,759 → 1,760; singleton share becomes
  `1,760 / 2,398 = 0.733945`.
- Active game-gene usages: 6,179 → 6,182.
- Games, combinations and families remain 288, 274 and 17.
- Earlier reviewed signatures changed: `2`, exactly `GAME-0239` and
  `GAME-0257`.

## Localisation disposition

- `ACT-409`, `SYS-754` and `SYS-791`: `corrected` to preserve the new typed
  boundaries in Ukrainian.
- `ACT-453` and `SYS-851`: `corrected` as new reviewed Ukrainian records.
- `SYS-829`: `corrected` only to name the newly separated `SYS-851` boundary in
  its Ukrainian exclusion list.
- `GAME-0239`, `GAME-0257`, `COMB-0237`, `COMB-0255`, their salience notes and
  plain-language cards: `corrected` for the decomposed representation.
- `CON-601` and all other carrier-local language: `verified` without change.
- Half-Life, HEV, Alien: Isolation, flashlight, battery, chapter, mission,
  device, version and build names remain `retained-with-reason` only in scoped
  evidence, examples and product presentation. No translation work is deferred.

## Rejection condition

Reopen the shared drain only if a later carrier cannot express its transition
through device, active state, local field, bounded internal charge, rate, cap
and empty response. Reopen either recovery owner only if evidence shows that
automatic off-state restoration and player-commanded finite-stock replacement
are the same transition. A common light field, battery noun or charge display
alone is insufficient to merge the Action, System and Constraint layers.

## Change history

- 2026-09-10 — accepted as `BATCH_017_TAXONOMY_CORRECTION_006` after the
  two-carrier transfer test and complete lower-ID Action scan separated active
  drain, automatic recovery, manual refill command and finite-stock settlement.
