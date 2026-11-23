---
game_id: GAME-0521
slug: wii-sports-resort
game_title: Wii Sports Resort
analysis_status: reviewed
reviewed: 2026-11-16
combination_ids: []
gene_ids:
  action:
    - ACT-716
    - ACT-717
    - ACT-718
  system:
    - SYS-1033
    - SYS-1489
    - SYS-1490
    - SYS-1491
    - SYS-1492
  constraint:
    - CON-800
  information:
    - INF-505
  objective:
    - OBJ-014
    - OBJ-294
  time:
    - TIM-001
---

# Game: Wii Sports Resort

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The course, disc classes, throw count, launch inputs and par are parameters.

## Analysis scope

- Version / ruleset: original North American English 2009 Nintendo Wii retail
  release RVL-RZTE-USA. Ordinary solo Frisbee Golf, manual right-handed mode,
  three-hole Classic A selection, hole 1 only. A calibrated Wii Remote with Wii
  MotionPlus supplies input. The original disc executable and sensor trace were
  not examined.
- Structured analysis target: `PLAT-NINTENDO-WII`, North American retail disc.
- Primary decision loop: read the current lie, wind and remaining route,
  choose one of three distance-class discs and aim from the fixed lie. Swing
  the calibrated controller, then release B to commit the gesture. The disc
  flies and may roll, enter the target, or incur a hazard. Use the resulting
  lie and count to plan the next throw until the hole result.
- Entry and exit: unlock Frisbee Golf by playing Frisbee Dog, select one player
  and the manual control style, calibrate, then select Classic A in the
  three-hole menu. Start with control at the first tee and finish at that
  hole's settled result, before the second tee. The setup is a prerequisite.
- Included: three selectable disc ranges, suggested disc, aim, gesture and
  explicit release, wind, curve, terrain flight and ground response, next lie,
  out-of-bounds and water penalties, light-volume entry, par and the limit on
  repeated misses.
- Excluded: automatic and left-handed control, later holes, other sports,
  multiplayer and aggregate course scoring, stamps and rating progression,
  modifiers that hide UI, other regional versions and successor products. The
  exact sensor algorithm, flight coefficients, limit threshold in the
  North American build and edge-case water drop coordinates are unverified.
- Potential scoped modules: automatic release, an extended multiplayer card,
  ball golf, and the distinct Frisbee Dog scoring task.
- Direct-play status: no console, disc or audiovisual playback. Nintendo's
  English manual fixes the hardware, manual release, target and disc classes.
  Nintendo Spain documents penalty categories. Period written guides support
  course selection, flight and follow-through. Regional rules were not measured.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `WSR-001` | The original Wii release has a calibrated MotionPlus setup and Frisbee Golf unlocks after Frisbee Dog. This unit uses a solo manual tee on the first Classic A hole. | Confirmed | Corroborated | High | P1, P4, R2, R4, R5 |
| `WSR-002` | Before a throw the player chooses Driver, Midrange or Putter for different reach, can override the suggested class and aims without moving the starting lie. | Observation | Corroborated | High | P1, P2, P3, R1, R3 |
| `WSR-003` | In manual mode, hold B through the horizontal throw motion and release B to let go. The player chooses the release sample. The controller angle affects trajectory. | Confirmed | Corroborated | High | P1, P3, R1, R2 |
| `WSR-004` | Flight depends on released orientation and wind. Trees may stop flight. The disc can skid or roll after surface contact, and supporting terrain matters. | Observation | Corroborated | Medium | P2, P3, R1, R2, R3 |
| `WSR-005` | The official guide uses the resting legal position for the next throw. Official documentation distinguishes out-of-bounds return and water entry-side placement, each with one penalty. A community guide simplifies both placements to rethrow from the same spot. | Observation | Conflicting | Medium | P2, R1, R3 |
| `WSR-006` | The disc can complete the hole by entering the luminous target volume, including from above ground or by rolling in. Touching the green outside it is not completion. | Confirmed | Corroborated | High | P1, P2, R1, R2 |
| `WSR-007` | Fewer counted throws are better. The first Classic A hole is par four. Each scored throw and penalty increases the count, and the display compares the count with par. | Observation | Corroborated | High | P2, R2, R4, R6 |
| `WSR-008` | Nintendo's guide records a maximum-count end without entering the target. Its threshold prose and numerical example differ, so the exact threshold and displayed result in the North American SKU are not asserted. | Observation | Limited | Medium | P2 |
| `WSR-009` | The shot display includes a recommended disc, aiming direction and wind. Flight settlement exposes whether play continues at a lie or the hole is complete. | Observation | Corroborated | Medium | P2, R1, R3 |
| `WSR-010` | A throw runs to a settled result before preparation of another; released attitude influences the curve and the player cannot steer that disc in flight. | Observation | Corroborated | High | P1, P2, R1, R2 |

## Basic data

- Release / origin: Nintendo, Wii optical disc. Nintendo lists July 26, 2009
  in North America, and the product catalogue identifies RVL-RZTE-USA.
- Platform or physical form: Wii with Wii Remote and Wii MotionPlus.
- Puzzle family: spatial physics and acting under a scored attempt budget.
- Primary sources:
  - **P1** [Nintendo of America, Wii Sports Resort manual](https://csassets.nintendo.com/noaext/image/private/t_KA_PDF/Wii_Wii_Sports_Resort?_a=BATCtdAA0),
    calibration and the Frisbee entries.
  - **P2** [Nintendo Spain, Frisbee Golf rules](https://www.guiasnintendo.com/2a_WII/wii_sports_resort/wii_sports_resort_sp/dep_frisbee_golf.html),
    disc choice, lie, penalty branches and par. The exact cutoff boundary
    differs between the prose and example. North American edge parity is limited.
  - **P3** [Nintendo Spain, Frisbee controls](https://www.guiasnintendo.com/2a_WII/wii_sports_resort/wii_sports_resort_sp/dep_frisbee.html).
  - **P4** [Nintendo regional launch schedule, July 2009](https://www.nintendo.co.jp/ir/pdf/2009/090731e.pdf).
- Secondary sources:
  - **R1** [GameSpot's 2009 walkthrough, Frisbee Golf section](https://www.gamespot.com/articles/wii-sports-resort-walkthrough/1100-6213637/),
    the disc class names, angle, tree contact, air capture and roll-in.
  - **R2** [Ringworm's 2009 Wii FAQ, section 6.3](https://gamefaqs.gamespot.com/wii/950923-wii-sports-resort/faqs/57355),
    manual input, scoring, terrain-dependent skid and hazard penalty context.
  - **R3** [StrategyWiki, Frisbee controls and course reference](https://strategywiki.org/wiki/Wii_Sports_Resort/Frisbee),
    manual aim, wind indicator, lie and simplified hazard description.
  - **R4** [Contemporary Classic A Frisbee Golf run description](https://www.youtube.com/watch?v=frayWSB0GyI)
    confirms the selected course is a three-hole preset. Only the description
    was consulted.
  - **R5** [GameFAQs release catalogue](https://gamefaqs.gamespot.com/wii/950923-wii-sports-resort/data).
  - **R6** [Frisbee Golf hole par table](https://www.supercheats.com/wii/wii-sports-resort/4716/frisbee-golf-par-for-each-hole/),
    checked against the Classic A layout in the [community score discussion](https://www.speedrun.com/wsr/forums/wnbbe).
- Claim IDs: `WSR-001` to `WSR-010`.

## Mechanical decomposition

### Action Genes

- `ACT-716`: select one shot-specific distance class from the reusable set.
- `ACT-717`: adjust the horizontal bearing of the preparation while the lie
  stays fixed. This aiming input is distinct from tilting during the swing.
- `ACT-718`: hold B, swing the calibrated Wii Remote, then release B to launch
  at the selected point in the physical gesture. No exact sensor model is assumed.
- Parameters: disc class, bearing, gesture, release moment and remote attitude.
- Claim IDs: `WSR-001` to `WSR-003`.

### System Behaviour Genes

- `SYS-1033`: currently disclosed wind influences the released disc.
- `SYS-1489`: banked release and chosen disc yield a flight. Solid terrain
  interrupts or redirects it and ground contact can lead to skid or roll.
- `SYS-1490`: a legal resting position outside the target becomes the next lie.
- `SYS-1491`: a prohibited resting outcome adds one penalty and selects a
  legal fallback. Nintendo documents a prior valid lie for out of bounds and
  the entry-side shore after a water landing. Exact North American edge
  coordinates are not established by the European guide.
- `SYS-1492`: reaching the target's three-dimensional region settles the
  shot as a capture whether the disc arrives by air or along the ground.
- Resolution order: choose and aim, release, advance the disc and evaluate
  contact, then settle target, legal rest or hazard. Update count and next lie
  or terminal result before another preparation.
- Claim IDs: `WSR-003` to `WSR-010`.

### Constraint Genes

- `CON-800`: a bounded maximum for an unfinished hole can force settlement.
  The exact maximum and inclusivity in the scoped SKU remain unverified.
- No resource stock of Driver, Midrange or Putter is consumed. A throw and any
  attached penalty affect the score rather than limiting physical disc supply.
- Claim IDs: `WSR-002`, `WSR-007`, `WSR-008`.

### Information Genes

- `INF-505`: before a shot, direction, terrain, the recommended disc and
  currently disclosed wind inform the choice. The displayed lie, throw count
  and target feedback update after settlement. No perfect trajectory preview
  is implied.
- Claim IDs: `WSR-002`, `WSR-004`, `WSR-007`, `WSR-009`.

### Objective Genes

- `OBJ-014`: send the disc into the fixed receiver on the green.
- `OBJ-294`: minimize throw count plus penalties relative to the given par.
  Four counted throws is level par. Three gives one under; five, one over.
  A completed higher-count result remains valid unless the cap ends the hole.
- Claim IDs: `WSR-006` to `WSR-008`.

### Time Genes

- `TIM-001`: each B release commits one delivery. Preparation of the next
  delivery follows flight, contact and settlement of that shot.
- Claim IDs: `WSR-003`, `WSR-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Ready at the tee | Override the disc recommendation and turn the aim line | The disc class and aim change while the tee position stays fixed | Selection and bearing do not spend a throw | `WSR-002` |
| Aim set and B held through the swing | Release B during the intended outward gesture | One disc launches and flight resolves from the sampled state | This route uses explicit commitment, not an automatic release | `WSR-003` |
| A flight banks or meets a tree and stops in play off the green | Wait for settlement | The next throw begins from the legal final position, even if nearer the tee than hoped | Advancement follows the lie, not progress along an abstract distance track | `WSR-004`, `WSR-005` |
| A throw exits play or fails in a water hazard | Allow hazard settlement | The throw counts and one penalty is added. For the fallback the official guide distinguishes the prior valid lie and the entry-side shore | The two failures do not imply identical placement | `WSR-005` |
| Disc above the green or rolling along its surface | Let the disc intersect the lit receiver | The target accepts the disc and ends the hole | The target is a volume, and a ground stop elsewhere is not a success | `WSR-006` |
| Par four, one penalty already charged and three physical deliveries made | With the fourth physical throw enter the target | Score is one over par | Penalties contribute to the same total as throws | `WSR-007` |
| Target not reached and the maximum is met | Allow the automatic termination | The hole closes without an entered disc | The count is not unbounded; the exact local cutoff is unverified | `WSR-008` |

## Strategic and experiential structure

- Local decision: choose reach, prethrow bearing and a release angle suited to
  current wind and clearance.
- Medium-term planning: aim to leave a safe next lie rather than sacrificing
  it for nominal range, then move from a long disc to a shorter approach.
- Long-term structure: subsequent holes and a cumulative round are separate
  from the one-hole packet.
- Common heuristics: take the range recommendation as advice, check obstacles,
  and account for the cost of a poor lie and penalty rather than just distance.
- Failure attribution: distinguish aim and release errors from a tree,
  drift, hazard penalty, or a pass beside the target.
- Player-trust factors: visible target and explicit B commitment distinguish
  aiming, launch and settlement. Feedback exposes the resulting lie or end.
- Claim IDs: `WSR-002` to `WSR-010`.

## Replay and variation

- What changes: the chosen disc and gesture, the shown wind and the sequence
  of resulting lies. The first hole and benchmark remain fixed.
- Randomness or procedural generation: exact wind sampling distribution and
  seed are unverified. The documented course layout is authored.
- Multiple viable strategies: safe legal lies and more ambitious curves can
  trade range against exposure to a poor position or penalty.
- Typical replay motive: reach the receiver in fewer counted throws.
- Claim IDs: `WSR-002`, `WSR-004` to `WSR-010`.

## Adjacent systems and history

- Direct predecessor: original Wii Sports provides inherited golf holes,
  while this packet applies the sequel's disc and MotionPlus mechanics.
- Variants: this title also contains ball golf and automatic disc release.
- Similar games: Golf Peaks shares a fixed receiver and committed shot
  settlement. The independently analysed original Wii Sports packet uses
  related gesture input but releases a rolling bowling ball down a lane.
- Important differences: the chosen disc, curve and wind alter a projectile
  trajectory and next lie. There is no card draw or grid-step travel.
- Claim IDs: `WSR-001` to `WSR-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-716`, `ACT-717`, `ACT-718` | class selection, bearing and sampled B release |
| System Behaviour | `SYS-1033`, `SYS-1489`, `SYS-1490`, `SYS-1491`, `SYS-1492` | wind, flight, lie, penalties and capture |
| Constraint | `CON-800` | bounded unfinished-hole settlement |
| Information | `INF-505` | prethrow aids and settlement feedback |
| Objective | `OBJ-014`, `OBJ-294` | target and penalty-adjusted par |
| Time | `TIM-001` | one settled delivery at a time |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `520` (`GAME-0001`–`GAME-0520`).
- Exact genome matches: none.
- Tied near matches: `GAME-0057` — Golf Peaks (`2 / 19 = 0.105263`).
- Supported combination subsets: none.
- Scan date: 2026-11-16.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0057` — Golf Peaks | `OBJ-014`, `TIM-001` place a payload in a fixed receiver after a discrete delivery commitment. | Golf Peaks spends movement cards over a grid with authored rollover and elevation rules. Frisbee Golf uses three reselectable disc ranges, manual motion-sampled throw, wind, continuous flight and successive legal lies, penalties and par. | Near, `0.105263` |

## Taxonomy impact

- Registry changes: `ACT-716` to `ACT-718`, `SYS-1489` to `SYS-1492`,
  `CON-800`, `INF-505`, and `OBJ-294`.
- Taxonomy-change record: [TAXONOMY_CHANGE_268](../../../research/taxonomy-changes/TAXONOMY_CHANGE_268.md).
- Candidate terms affected: none.

## Negative results

- No verified combination is a proper subset. The scoped evidence does not
  establish the numeric give-up threshold, water-placement parity on the
  North American SKU, exact flight coefficients or a guaranteed ace route.

## Delta summary

The unit adds a single manual disc-golf hole with ten new definitions.

## New facts

- [Observation | Corroborated | High] A disc can complete the hole by entering
  the vertical receiver during unsettled flight or by rolling (`WSR-006`).

## New genes

- [Observation | Corroborated | Medium] Disc class and bearing, gesture
  release, flight-to-ground response, lie transfer, typed penalty placement,
  in-flight target capture, unfinished count cap, readout and par objective.

## New combinations

- [Observation | Corroborated | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | Medium] `TAXONOMY_CHANGE_268` admits ten
  definitions and transfers three unchanged.

## New questions

- On the North American release, exactly when does the unfinished hole force
  settlement, and which water entry reference is used at a corner boundary?

## Next recommended game

- [Hypothesis | Limited | Medium] Returnal.
- Optimisation criterion: sample a documented beginning of a live reset loop.
- Expected information gain: distinguish retained capabilities from the
  failed cycle's removed equipment and positions.
- Backlog impact: `GAME-0522` follows acceptance of this unit.

## Why this game

- [Hypothesis | Limited | Medium] Motion sampling, continuous flight and
  a discrete next lie provide a usable comparison to board-based golf.
