---
game_id: GAME-0407
slug: plants-vs-zombies
game_title: Plants vs. Zombies
analysis_status: reviewed
reviewed: 2026-09-26
combination_ids: []
gene_ids:
  action:
    - ACT-441
    - ACT-546
    - ACT-547
  system:
    - SYS-051
    - SYS-1086
    - SYS-1087
    - SYS-1088
    - SYS-1089
  constraint:
    - CON-696
  information:
    - INF-403
  objective:
    - OBJ-020
  time:
    - TIM-003
---

# Game: Plants vs. Zombies

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Plant prices,
specific zombies, lane counts and wave lengths are parameters, not genes.

## Analysis scope

- Version / ruleset: the English Windows *Plants vs. Zombies GOTY Edition*
  sold as Steam application `3590`, restricted to a regular five-row daytime
  level of its first Adventure stage after the shovel has been awarded and
  before the seed tray requires pre-level loadout selection. The concrete
  replay target is level `1-6`, entered from an ordinary profile that has
  completed `1-5`. This is not the later *Replanted* remaster or a mobile
  economy. PopCap's public readme is for the Mac `1.0.40` build; it directly
  documents the original Adventure rules but does not establish byte-level
  identity with the uninspected Windows executable. Version-specific claims
  beyond that common rules surface are deliberately withheld.
- Structured analysis target: `PLAT-WINDOWS-PC` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: click transient sun before it disappears; compare
  the sun balance and seed-packet recharge against the current lane threat;
  place a selected plant in an eligible lawn cell; let it produce more sun,
  automatically shoot, or block while zombies advance and chew; reposition
  future commitments as the progress bar approaches larger waves.
- Entry: begin level `1-6` with its ordinary unlocked seed tray, all five
  lawnmowers unused, the original sun balance and an empty five-row lawn.
  The packet follows a route using Sunflowers, Peashooters and Wall-nuts; a
  player may leave other unlocked packets unused. It does not assert exact
  numeric starting sun, seed prices, spawn times or plant availability from
  an unobserved executable state; the tray must be logged at reproduction.
- Positive terminal: defeat every zombie released for this one level before
  any reaches the house, then accept the level-clear transition. Merely
  reaching the last wave's flag is not sufficient.
- Negative terminal: a zombie crosses the left house boundary after that
  lane's one lawnmower has already fired or otherwise failed to stop it.
- Included: mouse collection of falling or Sunflower-produced sun; transient
  sun expiry and no between-level carry; priced, cooldown-gated planting on
  vacant lawn cells; optional shovel removal of an existing plant to free a
  cell; Sunflower production, Peashooter lane fire and Wall-nut obstruction;
  finite increasing zombie waves, visible progress and flag warnings;
  leftward lane movement and chewing; one-shot row-clearing lawnmowers; and
  live-time level clear or house breach.
- Excluded: exact wave script and numerical timings not documented by the
  readme; optional Cherry Bomb, Potato Mine and Snow Pea use on this route;
  level `1-5`'s Wall-nut Bowling, later stages with nighttime, pool, fog or
  roof rules, pre-level seed selection after `1-7`, shop, coins, Almanac,
  achievements, Zen Garden, Survival, Puzzle, Mini-Games, replay modifiers,
  mobile monetisation and sequel/remaster mechanics.
- Potential scoped modules: one night level's absent sky sun and gravestones;
  a pool level's water placement and cleaners; a conveyor-belt level; or one
  post-`1-7` seed-selection packet.
- Reproducible parameterisation: record the displayed Windows edition/build,
  profile unlocks, actual `1-6` seed tray, starting sun, five rows and mower
  count; timestamp each clicked sun, plant type and cell, packet readiness,
  zombie spawn and lane, flag/wave indicator, plant loss, mower activation
  and final clear or house breach. If an installed revision's `1-6` differs
  materially from this documented first-stage packet, reopen the scope rather
  than silently replacing its rules.
- Direct-play status: none. No Windows binary, video, audio or gameplay trace
  was opened. The publisher's rules text and product listing support a
  bounded reconstruction, not a claimed playthrough or exact build audit.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PVZ-001` | Steam app `3590` is PopCap's Windows GOTY product and lists Adventure separately from four other modes. | Confirmed | Direct | High | P1 |
| `PVZ-002` | The publisher describes a five-row daytime lawn with left house, right street, sun-funded planted defenders and leftward zombies; all zombies cleared wins, a zombie reaching the house loses. | Confirmed | Direct | High | P2 |
| `PVZ-003` | Mouse clicks collect transient 25-sun sky or Sunflower units; unused units vanish and surplus does not carry to the next level. | Confirmed | Direct | High | P2 |
| `PVZ-004` | Seed packets recharge, plant placement debits sun, and the shovel awarded after `1-4` removes a plant to free space. | Confirmed | Direct | High | P2 |
| `PVZ-005` | The level begins with a preview of its zombie types and shows progress flags for larger waves; waves begin sparsely and grow. | Confirmed | Direct | High | P2 |
| `PVZ-006` | Zombies chew plants in their lane; a lane's lawnmower clears all current zombies once and leaves that lane exposed thereafter. | Confirmed | Direct | High | P2 |
| `PVZ-007` | Sunflowers produce sun, Peashooters automatically attack their lane and Wall-nuts obstruct an advancing zombie; this route can use those roles without claiming all unlocks or exact combat values. | Observation | Corroborated | Medium | P2, S1 |
| `PVZ-008` | The Mac `1.0.40` public readme and the uninspected Windows GOTY executable are separate evidence objects; exact `1-6` roster, prices, timings and executable parity remain unverified. | Observation | Direct | High | P1, P2, R1 |

## Basic data

- Release / origin: PopCap Games; Steam lists the PC product's release as
  2009-05-05. Its current storefront title is *GOTY Edition*; this record
  does not assert that every GOTY extra existed at initial release.
- Platform or physical form: Windows mouse-driven single-player PC game,
  Steam application `3590`; regular first-stage daytime Adventure level.
- Mechanical family: real-time system pressure; agent routing and
  coordination.
- Primary and official sources, accessed 2026-09-26:
  - **P1:** [PopCap/EA's Steam product page](https://store.steampowered.com/app/3590/Plants_vs_Zombies_GOTY_Edition/),
    for application, edition, developer, Windows support, single-player and
    distinct modes. Its marketing claim of replayability is not used to
    infer a random wave algorithm.
  - **P2:** [PopCap's *Plants vs. Zombies* public
    readme](https://akamai.cdn.ea.com/eadownloads/u/f/manuals/GAME-PVZ/en_US_readme.html),
    version `1.0.40`/Mac build dated 2012-10-17, sections “The Basics”,
    “Sun”, “Plants and Planting”, “Zombies”, “Shovel”, “Lawnmowers” and
    “Adventure”. The publisher-authored rules text describes the original
    game loop; its Mac build identifier is not transferred to Windows.
- Independent contemporary firsthand source, accessed 2026-09-26:
  - **S1:** [Tom Francis, *Plants vs. Zombies* review for *PC Gamer*](https://www.pcgamer.com/games/strategy/plants-vs-zombies-review-2009/),
    originally published May 2009 (later republished online). The critic
    describes collecting sun from Sunflowers, straight-row Peashooter fire
    and Wall-nut blocking from play; the article does not establish the
    precise `1-6` packet roster or numeric timings. Specific Windows `1-6`
    data still require direct executable review.
- **R1:** local bounded-scope and cross-edition transfer audit in this
  record. No audiovisual evidence was used.
- Claim IDs: `PVZ-001`–`PVZ-008`.

## Mechanical decomposition

### Action Genes

- Reused `ACT-441`: commit a priced persistent defender to one legal cell
  on a known, fixed hostile route. Here each row is one leftward lane rather
  than Bloons TD 6's winding track; the player chooses Sunflower,
  Peashooter or Wall-nut for its future economic, firing or blocking role.
- New `ACT-546`: explicitly click a visible transient sun unit to transfer
  it into the spendable balance. Production alone does not credit the player.
- New `ACT-547`: use the shovel on an occupied lawn cell to remove its plant
  and free the cell for a different future commitment. It is not a refund or
  Factorio-style extraction into inventory.
- Claim IDs: `PVZ-002`–`PVZ-004`.

### System Behaviour Genes

- Reused `SYS-051`: an established Peashooter automatically acquires a
  hostile in its lane and fires without individually commanded shots. The
  precise projectile interval and damage are unasserted parameters.
- New `SYS-1086`: daytime sky arrivals and placed Sunflowers create
  click-to-collect sun units; each uncollected unit expires after a short
  interval and collected surplus is not transferred to another level.
- New `SYS-1087`: release a finite level's zombies in a slow-to-heavier
  wave sequence with flagged surges, not player-triggered numbered Bloons
  rounds or an unbounded survival stream.
- New `SYS-1088`: each zombie advances left in its row, stops to chew a
  blocking plant, then continues if that plant is destroyed. A Peashooter
  may kill it before contact; Wall-nut occupation buys time, not a new lane.
- New `SYS-1089`: the first zombie reaching an unused mower activates a
  one-time sweep of that row's current zombies, after which that row has no
  mower reserve. House breach is checked after this protection is gone.
- Resolution order: sun arrival/production → click collection and spending →
  placement or shovel removal → plant automatic action and zombie movement/
  eating on live time → mower or house-boundary resolution → all released
  zombies eliminated for a level clear.
- Claim IDs: `PVZ-002`–`PVZ-006`.

### Constraint Genes

- New `CON-696`: planting requires an unlocked/available packet, sufficient
  current sun, completed packet recharge and an eligible unoccupied lawn
  cell. The exact price, recharge period, cell count and packet roster are
  parameters. Shovelling clears occupancy but does not generate sun.
- Claim IDs: `PVZ-003`, `PVZ-004`.

### Information Genes

- New `INF-403`: current sun, packet availability/recharge, visible plants
  and zombies by lane, initial enemy preview and flagged level-progress bar
  expose both immediate affordability and approaching wave pressure. The
  exact next spawn time or whole future schedule is not revealed.
- Claim IDs: `PVZ-002`–`PVZ-005`.

### Objective and Time Genes

- Reused `OBJ-020`: neutralise the finite assault before the house defence
  is defeated. Unlike Bloons TD 6's stock endpoint, a surviving zombie
  cannot be deliberately leaked through the house at a numeric cost.
- Reused `TIM-003`: sky sun, recharge, zombie movement, firing and waves
  progress while mouse choices are made, not after player turns.
- Claim IDs: `PVZ-002`–`PVZ-006`.

## Reproducible transitions

| Before | Action | Bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Day level and empty eligible cell | Wait for sky sun or place Sunflower | A transient sun unit appears; if clicked before expiry, the shared balance increases | Sun generation and collection are distinct | `PVZ-003` |
| Sun lies on the lawn | Ignore it past its collection interval | The unit disappears without credit and cannot fund later planting | Real-time opportunity cost | `PVZ-003` |
| Peashooter packet ready, affordable and cell empty | Select packet and click the cell | Balance decreases, packet recharges and placed plant later fires along its row | Priced spatial commitment | `PVZ-002`, `PVZ-004`, `PVZ-007` |
| Packet grayed out or balance below its displayed price | Attempt another placement | No new plant is committed until recharge or balance recovers | Dual readiness gate | `PVZ-004` |
| Wall-nut blocks an advancing zombie | Let live play continue | Zombie chews that plant; if it is destroyed, movement resumes left | Obstacle buys firing time | `PVZ-006`, `PVZ-007` |
| Occupied lawn cell | Use the shovel on its plant | Plant is removed and the cell becomes available again | Reconfiguration, not inventory extraction | `PVZ-004` |
| Zombie passes the last plants in a lane with unused mower | Let it reach mower | Mower fires once and destroys current zombies in that row; it is then spent | One-use lane reserve | `PVZ-006` |
| A later zombie reaches a now-unprotected house edge | No successful interception | Level fails even if other rows are clear | House breach terminal | `PVZ-002`, `PVZ-006` |
| Final flagged assault has released its finite members | Eliminate all remaining zombies | Level clears; sun surplus is not carried to the next level | Actual clearance, not flag-only success | `PVZ-002`, `PVZ-003`, `PVZ-005` |

## Strategic and experiential structure

- Local decision: collect current sun before it fades and plant in the row
  whose arrival-to-house time has become shortest relative to current fire.
- Medium-term planning: early Sunflowers trade present defence for later
  purchasing power, while Peashooters and Wall-nuts turn that balance into
  lane-specific damage and delay. A wall in one row cannot defend another.
- Long-term structure: reserve packet readiness and sun for the flagged
  surge, then finish the finite level without a breach. This does not imply
  an exact known wave composition.
- Common heuristic: use the initial zombie preview and live lane positions
  to avoid over-investing in a quiet row; do not treat a mower as renewable.
- Failure attribution: an exposed row may result from missed sun, a
  mistimed packet recharge, under-defence of that row, or prior mower use.
  Exact numerical optimisation is not inferred without executable review.
- Player trust: visibly grayed seed packets, the sun counter, flags and
  mower loss disclose most immediate constraints while precise future spawn
  timing remains unshown.
- Claim IDs: `PVZ-002`–`PVZ-008`.

## Replay and variation

- Different placement, collection timing and mower use change outcomes.
  The publisher's “never the same experience twice” marketing does not
  establish that the bounded level's enemy schedule is random.
- Exact `1-6` zombie composition, packet cost and update build were not
  independently recorded and must be logged in a future played trace.

## Adjacent systems and history

- Bloons TD 6 shares priced placed defenders (`ACT-441`), automatic defence
  (`SYS-051`) and live play (`TIM-003`), but its fixed track, layer-pop
  income, round-indexed schedule, stock-debit leaks and cover-radius preview
  do not describe PvZ's separate rows, collectable sun and one-shot mowers.
- Bad North shares a finite hostile assault (`OBJ-020`) and direct concern
  for a protected boundary, but its squads can be repositioned and enemies
  land via carriers rather than advancing in planted lanes.

## Normalised genome

The front matter is canonical: twelve Active genes. `ACT-441`, `SYS-051`,
`OBJ-020` and `TIM-003` transfer; eight new boundaries describe sun
collection/production, shovel replacement, staged lane threats,
chewing, mower loss, plant legality and decision-state disclosure.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `406` (`GAME-0001`–`GAME-0406`).
- Exact genome matches: none.
- Tied near matches: `GAME-0027` — Bad North: Jotunn Edition (`3 / 21 = 0.142857`).
- Supported combination subsets: none.
- Scan date: 2026-09-26.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0027` — Bad North | `SYS-051`, `OBJ-020`, `TIM-003` | Both keep a finite live assault moving while defenders automatically engage, and the player must repel all attackers. Bad North relocates squads among islands, responds to visible landing carriers and preserves houses; this lawn commits plants to separate rows, requires manually collected transient sun and packet recharge, lets the player shovel one cell, and spends a mower once per breached row. | Near, `3 / 21 = 0.142857` |

## Taxonomy impact

`TAXONOMY_CHANGE_145` adds eight bounded Active genes without modifying a
lower-ID signature or any verified combination.

## Negative results

- A level `1-6` walkthrough from the Windows executable was not performed;
  exact plant roster, cost values, timing and wave composition are unresolved.
- The publisher readme is a Mac `1.0.40` source. It directly supports the
  described original rules but not byte-identical Windows GOTY behavior.
- No distinct gene is added for a named plant or zombie merely because its
  artwork or numeric statistics differ. Night, pool, roof and shop loops
  are outside this packet.

## Delta summary

This first-stage defence packet uses manually collected, perishable sun to
fund plants committed to separate lanes while a finite live assault grows.
Automatic shooting and disposable mower protection make a missed purchase
or poorly covered row causally visible.

## New facts

- [Confirmed | Direct | High] The publisher separates sky and Sunflower sun,
  packet recharge, visible larger-wave flags and one-use lawnmowers
  (`PVZ-003`–`PVZ-006`).

## New genes

- [Observation | Direct | High] `ACT-546`, `ACT-547`, `SYS-1086`,
  `SYS-1087`, `SYS-1088`, `SYS-1089`, `CON-696` and `INF-403` isolate
  this packet's collection, reconfiguration, lane defence and disclosure.

## New combinations

- [Observation | Direct | High] No new verified combination.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_145` adds eight Active
  boundaries; older signatures stay unchanged.

## New questions

- What exact Windows build and seed-packet roster appear on an original
  Steam GOTY installation at level `1-6`?
- What are that build's actual spawn timings, packet recharge durations and
  zombie/plant combat values? None are inferred from the Mac readme.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0408` *Kirby's Adventure*.
- Optimisation criterion: change from mouse-planted lane defence to
  controller-led platform movement, inhalation and copied ability on NES.
- Expected information gain: test whether acquired ability ownership and
  traversal transfer beyond the existing platformer signatures.
- Backlog impact: no selected subject displaced.

## Why this game

- [Hypothesis | Limited | Medium] Separate lanes, manually collected
  perishable production and one-shot emergency sweep yield causal
  distinctions not supplied by a single-track tower defence genome.

## Next test

Install an identified Windows GOTY build, capture the level `1-6` tray and
full play trace including sun expiry, packet recharge, shovel removal,
flagged waves and mower breach, and revise only claims contradicted by that
specific observed build.
