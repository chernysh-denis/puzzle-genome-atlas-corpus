---
game_id: GAME-0135
slug: captain-of-industry
game_title: "Captain of Industry"
analysis_status: reviewed
reviewed: 2026-08-21
combination_ids:
  - COMB-0133
gene_ids:
  action:
    - ACT-006
    - ACT-096
    - ACT-120
    - ACT-121
    - ACT-124
    - ACT-144
    - ACT-145
    - ACT-148
    - ACT-177
    - ACT-179
  system:
    - SYS-156
    - SYS-157
    - SYS-158
    - SYS-159
    - SYS-161
    - SYS-275
    - SYS-276
    - SYS-277
    - SYS-278
    - SYS-279
    - SYS-280
    - SYS-281
    - SYS-282
  constraint:
    - CON-062
    - CON-172
    - CON-173
    - CON-185
    - CON-193
    - CON-194
    - CON-245
    - CON-246
    - CON-247
    - CON-248
    - CON-249
    - CON-250
    - CON-251
    - CON-252
  information:
    - INF-001
    - INF-059
    - INF-060
    - INF-071
    - INF-104
    - INF-105
    - INF-106
    - INF-107
    - INF-108
  objective:
    - OBJ-054
  time:
    - TIM-003
---

# Game: Captain of Industry

## Analysis scope

- Version / ruleset: Windows base game Update 4.2, released 20 July 2026;
  fresh standard New Haven run from the abandoned island state through the
  first successful rocket launch.
- Included: construction plans and blueprints; mining and dumping designations;
  excavators, trucks, storages, conveyors, pipes and power; production and
  research chains; housing, food, services, Unity, health, pollution and
  maintenance; main-ship exploration, resource locations, quick trade and
  contracts; rocket assembly, level-ground transfer, fuelling and launch.
- Excluded: Trains Expansion and Supporter Edition content; Sandbox; mods and
  community maps or blueprints; alternate difficulty settings; exhaustive
  optional train and nuclear routes; space-station upkeep, asteroid delivery,
  repeatable research and throughput optimisation after the first launch.
- Direct-play status: not conducted. Current official update notes establish
  the build boundary; the official game wiki and developer diaries establish
  the reproducible terrain, logistics, settlement, trade, research and launch
  transitions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `COI-001` | Update 4.2 is the current documented base update and released 20 July 2026 | Confirmed | Direct | High | P1–P2 |
| `COI-002` | Mining removes typed terrain volume and dumping builds persistent slopes, ramps or reclaimed land | Confirmed | Corroborated | High | P3–P5 |
| `COI-003` | A Mine Control Tower bounds designations and dispatches assigned excavators and trucks | Confirmed | Corroborated | High | P3–P4 |
| `COI-004` | Recipes, belts, pipes and automatically matched truck jobs form the live island factory | Confirmed | Corroborated | High | P2, P6–P7 |
| `COI-005` | Settlements convert supplied food and services into Unity and health while pollution and shortages threaten population | Confirmed | Corroborated | High | P8–P10 |
| `COI-006` | Maintenance is produced into global pools and shortages temporarily break machines or vehicles | Confirmed | Corroborated | High | P11 |
| `COI-007` | Tiered staffed labs consume research equipment and Unity to advance a queued prerequisite tree | Confirmed | Corroborated | High | P12–P14 |
| `COI-008` | The main ship explores fuel- and strength-gated world nodes that unlock villages, cargo ships and resource sites | Confirmed | Corroborated | High | P15 |
| `COI-009` | Contracts require reputation, a cargo depot, dedicated ship and recurring Unity to exchange physical goods | Confirmed | Corroborated | High | P16 |
| `COI-010` | A completed rocket needs level-ground transport from assembly depot plus compatible pad fuel and water | Confirmed | Corroborated | High | P17–P19 |
| `COI-011` | The first rocket launch is a bounded credits endpoint while the later space station is an open-ended scaling loop | Confirmed | Corroborated | High | P19–P20 |

## Basic data

- Release / origin: developed and published by MaFi Games; Windows Early
  Access release 31 May 2022; still in Early Access in the scoped update.
- Form: pausable real-time factory, terrain, logistics and settlement simulation.
- Puzzle family: live production-network construction; resource and logistics
  optimisation; terrain transformation; ordered dependencies; system pressure.
- Primary and official sources:
  - **[P1]** [official roadmap](https://coigame.com/Roadmap), Update 4 and 4.2 position.
  - **[P2]** [official Update 4.2 notes](https://coigame.com/Blog/update42-is-out), release and current base-game changes.
  - **[P3]** [official wiki: Designations](https://wiki.coigame.com/Designations), mining, dumping, heights and slopes.
  - **[P4]** [official wiki: Mine Control Tower](https://wiki.coigame.com/Mine_Control_Tower), control area and assigned vehicles.
  - **[P5]** [official wiki: Rock](https://wiki.coigame.com/Rock), finite terrain material and strategic dumping.
  - **[P6]** [official wiki: Ore Sorting Plant](https://wiki.coigame.com/Ore_Sorting_Plant), mixed excavator loads and outputs.
  - **[P7]** [official Update 4.1 notes](https://coigame.com/Blog/update41-is-out), reservations and buffer-driven dispatch.
  - **[P8]** [official wiki: Settlement](https://wiki.coigame.com/Settlement), food, services, Unity and health.
  - **[P9]** [official wiki: Unity](https://wiki.coigame.com/Unity), income and operating uses.
  - **[P10]** [official wiki: Health](https://wiki.coigame.com/Health), pollution, growth and mortality.
  - **[P11]** [official wiki: Maintenance Depot](https://wiki.coigame.com/Maintenance_Depot), global maintenance and breakdowns.
  - **[P12]** [official wiki: Research](https://wiki.coigame.com/Research), queue and research-point progression.
  - **[P13]** [official wiki: Research Lab Basic](https://wiki.coigame.com/Research_Lab_%28Basic%29), staffing, power and Unity.
  - **[P14]** [official wiki: Research Lab IV](https://wiki.coigame.com/Research_Lab_IV), equipment and advanced gates.
  - **[P15]** [official wiki: World Map](https://wiki.coigame.com/World_Map), exploration, combat and resource nodes.
  - **[P16]** [official wiki: Trade](https://wiki.coigame.com/Trade), quick trades, reputation and contracts.
  - **[P17]** [official wiki: Rocket Assembly Depot](https://wiki.coigame.com/Rocket_Assembly_Depot), construction and level transfer.
  - **[P18]** [official wiki: Rocket Launch Pad](https://wiki.coigame.com/Rocket_Launch_Pad), propellant and water gates.
  - **[P19]** [developer diary 22](https://coigame.com/Blog/captain-diary-22), rocket construction and transporter geometry.
  - **[P20]** [developer diary 48](https://coigame.com/Blog/cd-48), post-launch space station and infinite research boundary.
- Claim IDs: `COI-001`–`COI-011`.

## Mechanical decomposition

### Action Genes

- Reused: `ACT-006` changes speed; `ACT-096` selects a reachable world node;
  `ACT-120` configures recipes, filters, buffers and routes; `ACT-121` queues
  research; `ACT-124` stamps blueprints; `ACT-144` paints mining, dumping,
  harvesting and deconstruction work; `ACT-145` changes entity or vehicle
  priority; `ACT-148` places material-backed structures and transports;
  `ACT-177` configures a mine tower's area, fleet and destinations.
- New: `ACT-179` commits one quick trade or a persistent island contract.

### System Behaviour Genes

- Reused: `SYS-156` runs supplied recipes; `SYS-157` moves items and fluids;
  `SYS-158` distributes and throttles network power; `SYS-159` converts supplied
  lab equipment into queued unlocks; `SYS-161` depletes finite deposits.
- New: `SYS-275`–`SYS-282` cover conserved cut-and-fill terrain, mine-pair
  dispatch, island truck jobs, settlement and Unity state, pooled maintenance,
  world-map operation, island trade and the first rocket chain.
- Resolution order: accept edits; advance time; settle terrain and vehicle jobs;
  run logistics, power and recipes; update maintenance, settlement and Unity;
  advance research and world operations; resolve assembly, transfer and launch.

### Constraint Genes

- Reused: `CON-062` footprint; `CON-172` recipe flow; `CON-173` extraction
  locus; `CON-185` finite workers; `CON-193` construction materials and cells;
  `CON-194` conduit capacity and compatible product state.
- New: `CON-245`–`CON-252` separate tower-bounded terrain work, vehicle-job
  compatibility, settlement survival, Unity balance, world-node support,
  contracts, tiered research and level-ground rocket launch gates.

### Information Genes

- Reused: `INF-001` exposes current state; `INF-059` recipes and technologies;
  `INF-060` live factory diagnostics; `INF-071` colony-wide reports.
- New: `INF-104`–`INF-108` expose terrain and mine state, vehicle jobs,
  settlement/Unity/maintenance, world trade and rocket readiness.

### Objective and Time Genes

- Reused `OBJ-054` ends the scoped run at the first rocket launch; `TIM-003`
  advances the pausable real-time island.

## Reproducible transitions

| Before | Action | Bounded resolution | Establishes | Claims |
|---|---|---|---|---|
| Visible ore under sloped ground | Paint mining planes inside a tower and assign excavator plus trucks | excavator removes typed volume; trucks receive buckets and unload or idle | physical mine dispatch | `COI-002`–`003` |
| Low coast and available rock | Paint a dumping plane and allow rock | truck load becomes terrain, settles and expands usable land | conserved cut-and-fill | `COI-002` |
| Producer, storage and consumer | Set filters, import/export modes and buffers | dispatcher reserves a compatible truck job; belts or pipes handle connected flow | hybrid logistics | `COI-004` |
| Operating machines and low maintenance stock | Interrupt maintenance inputs and advance | global pool drains and uncovered entities begin temporary breakdowns | maintenance cascade | `COI-006` |
| Housing and food market | Add food variety and waste/health services while reducing pollution | fulfilment changes Unity and health; population trend follows health | settlement funds industry | `COI-005` |
| Reachable queued technology | Staff and supply the required lab tier | lab equipment is consumed into research points until unlock | industrial research chain | `COI-007` |
| Repaired main ship | Select a reachable unknown or hostile node | fuel is spent; exploration, battle, loot or repair state resolves | world-resource expansion | `COI-008` |
| Revealed village and cargo depot | Raise reputation and establish a compatible contract | dedicated ship cycles export/import cargo and recurring Unity | finite-resource replacement | `COI-009` |
| Rocket technology and supplied depot | Build a rocket and keep a flat path to a free pad | transporter carries the assembled rocket to the pad | geometry-bound transfer | `COI-010` |
| Rocket on pad | Supply matching propellant and water, then launch | launch resolves and the first-launch credits endpoint fires | bounded victory | `COI-010`–`011` |

## Strategic and experiential structure

- Local: place or configure one machine, plan, filter, buffer, designation,
  vehicle assignment, trade or research node.
- Medium term: keep excavation, haulage, construction, recipes, power,
  maintenance, labour and settlement Unity in a stable material loop.
- Long term: extend finite island resources through exploration and trade,
  build advanced lab-equipment and propellant chains, then preserve a level
  rocket corridor and launch the first assembled vehicle.
- Failure attribution: overlays and panels distinguish missing input, blocked
  output, unreachable route, maintenance deficit, workforce, Unity, health,
  terrain, research and launch-gate failures.

## Replay and variation

- What changes: map and terrain, mine geometry, factory topology, fleet and
  buffer policy, settlement services, research order, resource sites and trade.
- Randomness: map and world nodes are seed-dependent; job timing and breakdowns
  emerge from the live simulation, while recipes and the first-launch gate are fixed.
- Multiple viable strategies: yes; alternative production, transport, power,
  import and land-reclamation layouts can reach the same first launch.

## Adjacent systems and history

- Similar games: Factorio, Satisfactory, Dyson Sphere Program, Anno 1800,
  Timberborn and Workers & Resources: Soviet Republic.
- Historical position: the 2022 Early Access factory sim made excavated and
  dumped terrain part of the conserved industrial material economy; Update 3
  extended the post-launch loop and Update 4.2 is the current scoped build.

## Adjacent comparison

- Factorio shares live recipes, logistics and first-rocket completion but not
  terrain-volume haulage or settlement-funded Unity; Satisfactory shares
  spatial production but not autonomous mine fleets; Workers & Resources
  shares staffed industry and dispatch but construction offices and border
  currencies differ from CoI's island truck jobs and cargo contracts.

## Taxonomy impact

- Existing live-factory, research, construction and objective genes retain
  their boundaries. New genes isolate terrain as conserved cargo, tower-paired
  mine work, pooled maintenance, population-to-Unity conversion, island
  contracts and the assembly-depot-to-pad launch dependency.

## Negative results

- Rejected: `SYS-186` because workers are abstract slots rather than agents
  claiming errands; `SYS-268` because CoI job matching is island-wide and
  building-buffer-driven rather than a distribution office comparing assigned
  storage percentages; `SYS-269` because contracts spend Unity and goods rather
  than settle at a two-currency border; `SYS-270` because CoI has factory power
  and product conduits, not the combined republic utility model.

## Delta summary

## Нові факти

- Зафіксовано Update 4.2, фізичне cut-and-fill terrain, mine-fleet dispatch,
  settlement-to-Unity economy, pooled maintenance та first-rocket endpoint.

## Нові гени

- Додано `ACT-179`, `SYS-275`–`SYS-282`, `CON-245`–`CON-252` та
  `INF-104`–`INF-108`; `OBJ-054` коректно повторно використано.

## Нові комбінації

- `COMB-0133` фіксує шлях від tower-bounded excavation і settlement-funded
  industry через world supply до geometry-gated first rocket launch.

## Зміни таксономії

- Межі наявних генів не змінено; taxonomy-change record не потрібен.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | `ACT-006`, `ACT-096`, `ACT-120`, `ACT-121`, `ACT-124`, `ACT-144`, `ACT-145`, `ACT-148`, `ACT-177`, `ACT-179` | plans, designations, buffers, research, trade |
| System Behaviour | `SYS-156`–`SYS-159`, `SYS-161`, `SYS-275`–`SYS-282` | terrain, logistics, settlement, world, launch |
| Constraint | `CON-062`, `CON-172`, `CON-173`, `CON-185`, `CON-193`, `CON-194`, `CON-245`–`CON-252` | placement, supply, access and progression gates |
| Information | `INF-001`, `INF-059`, `INF-060`, `INF-071`, `INF-104`–`INF-108` | island, world and launch disclosure |
| Objective | `OBJ-054` | first rocket launch |
| Time | `TIM-003` | pausable real-time simulation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `134` (`GAME-0001`–`GAME-0134`).
- Exact genome matches: none.
- Tied near matches: `GAME-0119` — Factorio (`16 / 55 = 0.290909`).
- Supported combination subsets: `COMB-0133`.
- Scan date: 2026-08-21.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0119`.
