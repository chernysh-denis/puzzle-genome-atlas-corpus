---
game_id: GAME-0410
slug: halo-wars
game_title: Halo Wars
analysis_status: reviewed
reviewed: 2026-09-26
combination_ids: []
gene_ids:
  action:
    - ACT-139
    - ACT-189
    - ACT-316
  system:
    - SYS-215
    - SYS-297
    - SYS-305
    - SYS-551
    - SYS-755
    - SYS-1094
  constraint:
    - CON-001
    - CON-136
    - CON-273
    - CON-467
  information:
    - INF-224
    - INF-225
  objective:
    - OBJ-185
  time:
    - TIM-003
---

# Game: Halo Wars

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Named squads,
structures, prices and mission waypoints are parameters, not genes.

## Analysis scope

- Version / ruleset: original English 2009 Xbox 360 *Halo Wars* campaign,
  mission 02, `Relic Approach`, on Normal difficulty, from the first
  controllable Alpha Base construction site through destruction of the
  Covenant Detonator. The original Microsoft manual establishes general
  rules and Prima's official original-game guide bounds this mission. No
  *Definitive Edition*, multiplayer or later sequel rules are imported.
- Structured analysis target: `PLAT-XBOX-360` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: select a unit or group with controller commands;
  claim the outlined base site; allocate finite base sockets to a Supply Pad
  and Barracks; let the Pad deliver resources, then train the required five
  Marine squads; after the gates open, use sight-limited movement and
  focused attacks to move a surviving force to the barrier, remove its
  power source and destroy the designated Detonator.
- Entry: start the original Xbox 360 solo campaign's second mission on
  Normal, at first player control with the outlined Alpha Base site,
  before a building order. Record the
  actual disc revision, initial resources, population, base sockets and
  mission objective display rather than assuming exact values.
- Positive terminal: destroy the Detonator after the access steps; the
  campaign marks mission 02 complete and retains the next mission. Other
  Covenant troops need not all be eliminated.
- Failure and recovery control: if the only base is destroyed, the manual
  grants a short opportunity to build another before defeat; this packet
  does not claim that every mission-state permits such recovery. Units can
  also be lost in combat, forcing replacement or a restarted mission.
- Included: controller group selection and movement/attack orders, automated
  pathing and combat, allied sight/fog and remembered terrain, fixed base
  sockets, base-site claim, paid Supply Pad/Barracks construction, passive
  Supply Pad income, site-bound Marine training and population/resource
  gates, the authored five-Marine gate-opening prerequisite, targetable
  barrier power source and Detonator, mission objectives/HUD and live time.
- Excluded: optional supply-crate collection, trapped-Warthog rescue,
  Black Box, Skull, score and medal optimisation, optional tech/vehicle
  branches and expansion bases as mandatory steps; exact build costs,
  initial resources, enemy positions, damage, AI timings and base-loss
  countdown of an unplayed disc; later campaign missions, co-op, Skirmish,
  multiplayer, downloadable content, *Definitive Edition* and *Halo Wars 2*.
- Potential scoped modules: optional vehicle production and Reactor tech;
  a fixed Skirmish economy; optional rescue and reinforcement route.
- Reproducible parameterisation: record disc revision, Normal setting,
  selected unit/group and controller order, chosen base socket and building,
  resource/income/population display, completion of five Marine orders,
  gate transition, allied sight and route, barrier-source damage, Detonator
  damage and mission-complete flag. Compare a base-destruction failure
  branch separately and reset before the positive route.
- Direct-play status: none. No Xbox 360 disc, executable, controller trace,
  save, screenshot, gameplay video or audio was inspected. The document is
  a source-bounded reconstruction, not a claim of played or frame-verified
  behaviour.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `HW-001` | Original Xbox 360 campaign mission 02 is `Relic Approach`, distinct from Skirmish and later editions. | Observation | Corroborated | High | P1, P2 |
| `HW-002` | A selected unit or group receives destination or attack orders; its movement and basic attacks then resolve in real time. | Confirmed | Direct | High | P1 |
| `HW-003` | Allied units and buildings reveal nearby hostiles, while previously explored terrain persists under fog. | Confirmed | Direct | High | P1 |
| `HW-004` | Bases occupy outlined sites with finite building sockets; buildings, units and upgrades cost resources, and units consume population. | Confirmed | Direct | High | P1 |
| `HW-005` | A UNSC Supply Pad supplies resources over time without a worker's gather-and-return trip. | Confirmed | Direct | High | P1 |
| `HW-006` | The mission first requires a base, Supply Pad, Barracks and five trained Marines before the base gates open. | Observation | Corroborated | High | P2 |
| `HW-007` | The route can disable the barrier power source and then destroy the designated Detonator to end the mission. | Observation | Corroborated | High | P2 |
| `HW-008` | The HUD discloses current resources, population, tech tier, selected units and mission objectives; the original manual gives an only-base loss recovery timer. | Confirmed | Direct | High | P1 |
| `HW-009` | This packet's base production and combat route is a bounded campaign objective, not a claim of complete-map extermination. | Strong Pattern | Corroborated | High | `HW-002`–`HW-008` |

## Basic data

- Release / origin: Ensemble Studios and Microsoft Game Studios, original
  Xbox 360 *Halo Wars*, 2009.
- Platform or physical form: original Xbox 360 disc; exact revision untested.
- Puzzle families: tactical forecast and counterplay (`FAM-009`), real-time
  system pressure (`FAM-010`), agent routing and coordination (`FAM-015`)
  and ordered dependency sequencing (`FAM-017`).
- Primary rules source, accessed 2026-09-26: **P1** — [Microsoft's original
  Xbox 360 *Halo Wars* Planetary Operations Manual](https://download.microsoft.com/download/F/9/9/F99AB8F0-5191-4EDD-B312-7A9B9E4784FA/HaloWars_MNL_EN-US.pdf),
  especially printed pp. 6–13 and 22–23. The Microsoft-hosted original
  PDF establishes orders, fog, base sockets, resources, population and
  Supply Pads; it is not itself a direct play trace.
- Primary mission route, accessed 2026-09-26: **P2** — [Prima's official
  *Halo Wars* guide, mission 02 `Relic Approach`](https://primagames.com/eguides/halo-wars-eguide/campaign-act-1/02-relic-approach).
  It identifies the required five-Marine opening, barrier approach and
  Detonator terminal; its optional tactical suggestions are not rules.
- Claim IDs: `HW-001`–`HW-009`.

## Mechanical decomposition

### Action Genes

- `ACT-139`: commit the outlined base site and select a finite compatible
  building socket for the Supply Pad or Barracks. The fixed socket relation
  is `CON-001`, not a free-form land placement claim.
- `ACT-189`: select a squad or group, order a navigable destination or
  visible target, and redirect the force as threats appear.
- `ACT-316`: queue Marine training at the completed Barracks; the order is
  distinct from automatic queue completion.
- Candidate action genes: none. Controller buttons and radial menus are
  an input surface for existing order commitments.
- Claim IDs: `HW-002`, `HW-004`, `HW-006`.

### System Behaviour Genes

- `SYS-297` and `SYS-215`: commanded paths, target acquisition and damage
  resolve while the player makes further base and combat decisions.
- `SYS-305`: allied sight reveals live hostiles; fog closes outside sight.
- `SYS-551`: paid Marine orders complete in the Barracks over live time.
- `SYS-755`: attacks on the eligible barrier power source and Detonator
  reduce durability until their route effect or mission terminal occurs.
- New `SYS-1094`: a completed UNSC Supply Pad adds recurring supplies to
  the shared stockpile without worker trips; building more Pads competes
  with scarce production sockets.
- Resolution order: claim site → complete Pad/Barracks → accrue and spend
  supplies → train Marines → satisfy five-Marine gate → reveal/advance →
  remove barrier source → attack Detonator → settle mission.
- Claim IDs: `HW-002`–`HW-007`.

### Constraint Genes

- `CON-001`: each built base has a finite set of persistent addressed
  building sockets, one ordinary facility per socket.
- `CON-467`: training requires Barracks, sufficient supplies and population
  headroom; the exact cap and cost are unverified parameters.
- `CON-136`: the gate-opening step is unavailable until the authored base,
  Pad, Barracks and five-Marine prerequisites have been fulfilled.
- `CON-273`: current hostile positions outside allied sight cannot be
  targeted as currently known positions merely because terrain was explored.
- Scarce strategic resources: socket capacity, current supplies, available
  population, production time and surviving fighting units.
- Claim IDs: `HW-003`–`HW-006`.

### Information Genes

- `INF-224`: the command view exposes selected-unit state, resources,
  population, technology and current production/mission order.
- `INF-225`: explored ground remains mapped while live unseen enemies do
  not remain disclosed.
- Claim IDs: `HW-003`, `HW-008`.

### Objective and Time Genes

- `OBJ-185`: the declared Detonator is the single terminal structure;
  disabling the barrier source is a prerequisite, not a demand to defeat
  every hostile in the valley. The successor mission is retained.
- `TIM-003`: income, production, movement and hostile action advance in
  real time during command selection.
- Claim IDs: `HW-007`, `HW-009`.

## Reproducible transitions

| Before | Action | Bounded resolution | Establishes | Claim |
|---|---|---|---|---|
| Alpha Base site is outlined | Select the site | A base appears with a finite set of building sockets | site claim precedes facilities | `HW-004`, `HW-006` |
| An empty socket and enough supplies exist | Order a Supply Pad | The Pad completes on that socket; shared supplies then rise over time | socket trade-off and passive income | `HW-004`, `HW-005` |
| A second eligible socket exists | Order Barracks, then queue Marines | Barracks completes; each paid Marine order advances before a squad appears | site-bound production | `HW-004`, `HW-006` |
| Fewer than five required Marines are trained | Inspect base gates | Gates stay shut despite an army already being present | authored prerequisite, not generic path collision | `HW-006` |
| Fifth Marine training requirement completes | Inspect gates and order units outward | Gates open; selected squads may follow a traversable route | staged opening reaches combat route | `HW-006` |
| Enemy sector lies outside allied sight | Move a squad toward it | Terrain and enemies enter current vision; leaving sight restores fog | sight-limited command information | `HW-003` |
| Barrier source remains intact | Order eligible units to attack it | Durability falls and barrier access becomes possible when destroyed | destructible route gate | `HW-007` |
| Detonator is accessible | Focus surviving force on it | Its destruction completes mission 02 and retains the successor | bounded terminal, not map clearance | `HW-007`, `HW-009` |

## Strategic and experiential structure

- Local decision: choose a safe route and focused target while keeping
  selected squads alive under fog-limited information.
- Medium-term planning: allocate sockets between economy and production;
  let Supply Pad income fund Marines before trying to leave the base.
- Long-term structure: complete the mission 02 Detonator objective and stop
  before mission 03 or any broader campaign result.
- Failure attribution: insufficient supplies, no eligible socket/Barracks
  or population headroom reject production for different reasons. A lost
  squad reduces fighting force; loss of the sole base starts a manual-listed
  recovery clock rather than automatically proving immediate defeat.
- Player trust: resource, population and objective displays make the base
  gate and queue state legible; enemy state remains sight-limited.
- Claim IDs: `HW-002`–`HW-009`.

## Replay and variation

- Pad count, combat mix, route and losses may change. The required initial
  build/training chain and Detonator terminal remain fixed in this packet.
- The official guide suggests optional flank and vehicle routes, but this
  record neither requires them nor claims their exact timings.

## Adjacent systems and history

- `GAME-0397` *Red Alert 2* and `GAME-0179` *Age of Empires II* share
  selected-unit orders, live queues, fog and paid production. *Halo Wars*
  instead binds facilities to prelocated base sockets and receives recurring
  Supply Pad income without assigned harvesters or an ore-return trip.
- `OBJ-185` already covers a designated mission structure. `OBJ-166`
  would incorrectly require clearing all declared hostiles, and a new
  Detonator-named objective would duplicate an existing boundary.
- `SYS-549` requires a worker's finite gather-and-return cycle; that is
  not the Supply Pad mechanism. The Pad's automatic shared income is the
  only new gene in this unit.

## Normalised genome

The front matter is canonical: seventeen Active genes. Sixteen reuse
reviewed command, vision, production, constraint, information, objective
and real-time boundaries. One new system boundary isolates passive
building-generated shared resources.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `409` (`GAME-0001`–`GAME-0409`).
- Exact genome matches: none.
- Tied near matches: `GAME-0397` — Command & Conquer: Red Alert 2 (`12 / 21 = 0.571429`).
- Supported combination subsets: none.
- Scan date: 2026-09-26.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0397` — Command & Conquer: Red Alert 2 | `ACT-139`, `ACT-189`, `ACT-316`, `SYS-215`, `SYS-297`, `SYS-305`, `SYS-551`, `CON-273`, `CON-467`, `INF-224`, `INF-225`, `TIM-003` | Both issue group orders under fog and spend stockpiles on live production. Red Alert 2's first Allied mission gains Fort Bradley, places a Barracks freely, trains an Engineer and repairs a bridge before clearing a hostile supply base; Halo Wars claims fixed base sockets, grows supplies through a passive Pad, trains five Marines to open its gate and targets one Detonator. | Near, `12 / 21 = 0.571429` |

## Taxonomy impact

`TAXONOMY_CHANGE_148` adds `SYS-1094` without changing an earlier
signature or a verified combination.

## Negative results

- No original Xbox 360 build was played. Exact starting stockpile,
  population, costs, enemy routes, damage and base-loss countdown remain
  unverified; Prima's tactical recommendations are not mandatory rules.
- Optional supply crates, Warthog rescue, score medals and tech branches
  remain outside the required transition path.
- The Detonator is a parameter of `OBJ-185`, not a newly named objective.

## Delta summary

Controller group orders, fixed-site base construction and passive Supply
Pad income feed a paid Marine-training gate before a sight-limited assault
on one designated campaign structure.

## New facts

- [Confirmed | Direct | High] Microsoft's original manual distinguishes
  finite base sockets, resource/technology/population displays, Supply
  Pads and site-bound training (`HW-002`–`HW-005`, `HW-008`).
- [Observation | Corroborated | High] Prima's original-game mission route
  establishes the five-Marine gate and Detonator terminal (`HW-006`,
  `HW-007`).

## New genes

- [Observation | Direct | High] `SYS-1094` isolates recurring base-facility
  income from worker harvesting or finite crate pickup.

## New combinations

- [Observation | Direct | High] No new verified combination.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_148` admits the Supply Pad
  income boundary; older signatures remain unchanged.

## New questions

- How do exact Xbox 360 disc revisions differ in initial stockpile and
  base-loss recovery timing for this Normal mission?
- Which optional flank route produces a materially different unit economy
  under the same mission terminal?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0411` *Bejeweled 3*.
- Optimisation criterion: change from live army production to a bounded
  PC match-resolution and score loop.
- Expected information gain: compare mode-specific cascades and evaluation
  against the existing match-three genome.
- Backlog impact: no selected subject displaced.

## Why this game

- [Hypothesis | Corroborated | Medium] A fixed-base RTS packet tests
  whether automatically accruing facility income can be separated from
  already-reviewed unit command and paid-queue rules without assigning
  genre labels to genes.
