# Taxonomy Change 064: Merge hostile component destruction into SYS-794

## Status

- Proposal status: `Accepted`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Date: 2026-09-10
- Trigger: card `C-08` of
  [`BATCH_017_FULL_TAXONOMY_AUDIT_001`](../normalisation/BATCH_017_FULL_TAXONOMY_AUDIT_001.md).
- Scope: `SYS-794`, `SYS-842`, their two carriers and affected presentation;
  no later correction enters this unit.

## Current classification

- `SYS-794` was introduced for Dead Space (2023) as accumulated damage to an
  attached body region crossing a severance threshold and removing its movement
  or attack capability while the hostile remained alive.
- `SYS-842` was introduced later for DOOM Eternal as accumulated compatible
  damage destroying an attached turret and removing its long-range attack while
  the hostile remained alive.
- Both records owned the same System transition. Their only purported
  discriminators were anatomical limb versus mounted weapon, visible tissue
  layers versus an ordinary break state, and detachment versus destruction.

## Detected problem

The two boundaries accept the same before/action/after trace after parameters
are substituted:

1. a living hostile has an attached, spatially targetable component;
2. compatible attacks accumulate enough damage on that component;
3. the component crosses its destruction or detachment threshold;
4. the capability carried by the component becomes unavailable; and
5. the hostile remains alive with a reduced capability set until a separate
   defeat transition.

Whether the component is biological or mechanical changes its presentation and
damage layers, not the decision structure. `INF-313` independently owns Dead
Space's visible layered regional degradation. Neither carrier requires that
every component detach visibly, and both distinguish component settlement from
whole-hostile defeat.

## Evidence and two-way transfer test

- Dead Space claim `DSR-005` and its transition ledger establish regional
  damage reaching severance, removal of the corresponding locomotion or attack
  option, and a still-viable carrier. EA Motive's official
  [remake account](https://www.ea.com/inside-ea/news/inside-dead-space-1-remaking-a-classic)
  and [peeling-system account](https://careers.ea.com/ea-studios/motive/news/inside-dead-space-2-new-necromorph-nightmare),
  rechecked 2026-09-10, establish retained tissue layers, weakened-region
  inspection, broken bone and actual limb removal. The accepted static route
  evidence supplies the scoped capability consequence.
- DOOM Eternal claim `DE-007` and its transition ledger establish enough aimed
  damage breaking an Arachnotron turret, disabling its long-range attack and
  leaving the body as an active hostile. The two accepted independent static
  first-mission routes agree on that transition. No audiovisual evidence is
  introduced by this correction.
- Dead Space transfers into the general boundary with `component = limb`,
  `destroyed state = severed` and `capability = locomotion or attack reach`.
- DOOM Eternal transfers with `component = mounted turret`,
  `destroyed state = broken` and `capability = long-range attack`.

The transfer is symmetric. Removing either carrier's noun and visual treatment
does not leave a rule that the other carrier fails. Keeping two IDs therefore
encoded content identity as taxonomy.

## Complete lower-ID and adjacent-boundary scan

All 793 lower-ID System definitions were checked before selecting the earlier
`SYS-794` as survivor. The closest meaningful neighbours remain distinct:

- `SYS-208` resolves a ranged attack through cover, armour and hit location
  into a wound; it does not require component destruction or functional loss.
- `SYS-347` is the entire ARC perception, targeting, armour, weak-point and
  attack cycle. Its weak point is a parameter inside that compound actor loop,
  not this portable component-settlement rule.
- `SYS-580` projects a ground-vehicle round through layered armour into a
  continuing spatial path across crew, ammunition and modules. Penetration and
  the post-penetration path are defining rules absent here.
- `SYS-701` combines an aggregate vehicle durability pool with separately
  impaired modules and crew roles. That vehicle damage model is broader than
  attached-component destruction on a living actor.
- `SYS-755` removes an eligible inanimate world object's solid body at a damage
  threshold and may resolve debris, links or contents. It explicitly excludes
  defeating or functionally reducing a living combatant.
- `SYS-215` remains the live-combat clock and general hit/damage/defeat owner;
  it does not replace the persistent capability-set change caused by destroying
  one attached component.

No lower-ID System other than `SYS-794` accepts both carriers without importing
vehicle penetration, compound actor behaviour, inanimate-object removal or
undifferentiated combat resolution.

## Decision

- Generalise `SYS-794` to **Destroy an attached spatial component and remove
  its capability**.
- Treat anatomical or mechanical identity, tissue layers, mounted-weapon type,
  accepted damage and the exact removed capability as parameters.
- Mark `SYS-842` `Merged` into `SYS-794`; preserve the stable alias and never
  reuse its ID.
- Replace `SYS-842` with `SYS-794` in `GAME-0286`.
- Keep the `GAME-0259` and `COMB-0257` gene sets unchanged.
- Keep `COMB-0235` and `COMB-0243` unchanged; the replaced gene lies outside
  both strict subsets.
- Keep `SYS-208`, `SYS-347`, `SYS-580`, `SYS-701`, `SYS-755` and `INF-313`
  unchanged.

## Genome, combination and comparison impact

- `GAME-0259` remains at 35 Active genes; `COMB-0257` remains at 29 and a
  strict proper subset.
- `GAME-0286` remains at 28 Active genes through a one-for-one substitution.
  Its `COMB-0235` and `COMB-0243` membership is unchanged because neither
  combination contains `SYS-794` or the merged alias.
- The global containment scan creates no new combination supporter and no
  exact combination collision.
- DOOM (2016) remains `GAME-0286`'s selected lower-ID neighbour at
  `23 / 28 = 0.821429`; the shared set does not contain either component gene.
- Dead Space's signature does not change, so its selected lower-ID neighbour
  remains Prey (2017) at `22 / 39 = 0.564103`.
- Exactly one reviewed signature changes, `GAME-0286`, and only by replacing
  the merged alias with its survivor.

## Corpus accounting

- Canonical definitions remain 2,455.
- Active definitions: 2,398 → 2,397.
- Inactive definitions: 57 → 58; `Merged` records: 52 → 53.
- Active System definitions: 831 → 830.
- Active singleton definitions: 1,759 → 1,757; both former singletons collapse
  into one two-carrier survivor. Singleton share becomes
  `1,757 / 2,397 = 0.733000` rounded to six decimals.
- Active game-gene usages remain 6,183 because the carrier substitution is
  one-for-one.
- Games, combinations and families remain 288, 274 and 17.

## Localisation disposition

- `SYS-794`: `corrected` in Ukrainian for the portable component boundary and
  two-carrier range.
- `SYS-842`: its active Ukrainian record is removed because the ID is now a
  lifecycle alias, not a public current gene.
- `GAME-0259`, `GAME-0286`, `COMB-0257`, both salience records and both
  plain-language component cards: `corrected` or reverified in-unit.
- `COMB-0235` and `COMB-0243`: `verified`; their gene sets and Ukrainian public
  meanings are unchanged.
- Dead Space, DOOM Eternal, Plasma Cutter, Arachnotron, turret, Campaign,
  chapter, mission and stable identifiers are `retained-with-reason` only in
  scoped carrier evidence and presentation. No localisation work is deferred.

## Rejection condition

Reopen the merge only if a later carrier demonstrates that destroying or
detaching an attached spatial component can remove its capability while the
carrier remains alive in one record but not the other after component identity,
visual layers and capability type are substituted. Shared vocabulary alone is
not evidence; the counterexample must change legality, resolution or retained
state. Vehicle penetration, inanimate breakables and temporary intact-component
effects remain outside the boundary and do not reopen it.

## Change history

- 2026-09-10 — accepted as `BATCH_017_TAXONOMY_CORRECTION_008` after a fresh
  complete lower-ID System scan and two-way carrier transfer test.
