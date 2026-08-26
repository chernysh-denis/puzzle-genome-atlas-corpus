---
game_id: GAME-0133
slug: timberborn
game_title: Timberborn
analysis_status: reviewed
reviewed: 2026-08-21
combination_ids:
  - COMB-0131
gene_ids:
  action:
    - ACT-006
    - ACT-068
    - ACT-120
    - ACT-139
    - ACT-144
    - ACT-145
    - ACT-148
    - ACT-175
    - ACT-176
  system:
    - SYS-156
    - SYS-162
    - SYS-186
    - SYS-192
    - SYS-196
    - SYS-255
    - SYS-256
    - SYS-257
    - SYS-258
    - SYS-259
    - SYS-260
    - SYS-262
    - SYS-263
  constraint:
    - CON-062
    - CON-172
    - CON-173
    - CON-184
    - CON-185
    - CON-193
    - CON-229
    - CON-230
    - CON-231
    - CON-232
    - CON-233
    - CON-234
    - CON-235
  information:
    - INF-001
    - INF-060
    - INF-086
    - INF-091
    - INF-092
    - INF-094
    - INF-095
    - INF-096
  objective:
    - OBJ-068
  time:
    - TIM-003
---

# Game: Timberborn

## Analysis scope

- Version / ruleset: released PC version `1.0`, current main branch after the
  6 May 2026 patch; a fresh single-player Folktails settlement on the revised
  Waterfalls map at Normal settings, through first Earth Recultivator activation.
- Included: 3D water and badwater; temperate weather, droughts and badtides;
  dams, levees, floodgates, pumps, storage and irrigation; paths and vertical
  construction; staffed jobs, hauling and build errands; food, water, sleep,
  well-being, housing-bound Folktail reproduction and death; trees and crops;
  recipes, Science Point unlocks, shaft power, one sensor-controlled water
  facility, and every production chain required for the Folktails wonder.
- Excluded: Iron Teeth; custom maps or settings; Creative mode; mods; optional
  bots, ziplines, multi-district transfer and exhaustive terraforming;
  achievements, repeated wonder launches and post-victory optimisation.
- Direct-play status: not conducted. Official release and development notes
  establish the version, water, weather, automation and wonder; the maintained
  official wiki corroborates Normal settings and exact mechanical gates.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TIMBER-001` | Timberborn left Early Access as version 1.0 on 12 March 2026; the scoped branch includes the 6 May patch | Confirmed | Direct | High | P1–P3 |
| `TIMBER-002` | Waterfalls is the revised beginner map; Normal alternates temperate weather with escalating droughts and probabilistic badtides | Confirmed | Corroborated | High | P2, P7, P8 |
| `TIMBER-003` | Water and badwater flow and mix through 3D terrain; barriers, openings and pumps alter their live state | Confirmed | Direct | High | P2, P4 |
| `TIMBER-004` | Irrigation, submersion and contamination determine crop and tree growth or death | Confirmed | Corroborated | High | P4, P8 |
| `TIMBER-005` | Beavers claim reachable jobs and errands by priority; paths and stairs determine access | Confirmed | Corroborated | High | P4, P9 |
| `TIMBER-006` | Folktail housing bounds reproduction; individual needs and well-being modify work and lifespan | Confirmed | Corroborated | High | P10, P11 |
| `TIMBER-007` | Staffed buildings repeat recipes, haulers move goods, and builders consume delivered materials | Confirmed | Corroborated | High | P4, P9 |
| `TIMBER-008` | Shafts distribute variable power; Gravity Batteries absorb surplus and release it during deficits | Confirmed | Corroborated | High | P12, P13 |
| `TIMBER-009` | Staffed science buildings accumulate points which the player spends to unlock constructions | Confirmed | Corroborated | High | P14 |
| `TIMBER-010` | 1.0 sensors and logic propagate signals that control pumps, floodgates and valves | Confirmed | Direct | High | P2, P5 |
| `TIMBER-011` | Earth Recultivator costs 20,000 science to unlock; 2,000 gears, 2,000 treated planks and 1,500 metal blocks to build; then 500 Extract and 500 Paper to launch | Confirmed | Direct | High | P6, P15 |
| `TIMBER-012` | First launch declares the map won, grants its badge and flexible start, while allowing continued play | Confirmed | Direct | High | P6, P15 |
| `TIMBER-013` | First launch captures the water-weather-population-production dependency without treating endless play as completion | Observation | Corroborated | High | P6, P15 |

## Basic data

- Release / origin: Mechanistry; Steam Early Access began 15 September 2021;
  full version `1.0` released 12 March 2026.
- Platform or physical form: pausable real-time PC colony and water-engineering
  simulation on a fixed three-dimensional map.
- Puzzle family: spatial network construction; resource and logistics
  optimisation; agent routing; real-time system pressure; ordered dependencies.
- Primary and official sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/1062090/Timberborn/),
    release state, developer, platform and premise.
  - **[P2]** [official 1.0 release notes](https://store.steampowered.com/news/posts/?appgroupname=Timberborn&appids=1062090&enddate=1774263893&feed=steam_community_announcements),
    release date, Waterfalls revision, automation and water systems.
  - **[P3]** [official update feed](https://store.steampowered.com/news/app/1062090),
    6 May 2026 main-branch maintenance boundary.
  - **[P4]** [official 1.0 gameplay overview](https://store.steampowered.com/news/posts/?appgroupname=Timberborn&appids=1062090&enddate=1774263893&feed=steam_community_announcements),
    3D water, drought, badtide, settlement and production.
  - **[P5]** [official automation overview](https://store.steampowered.com/news/posts/?appgroupname=Timberborn&appids=1062090&enddate=1774263893&feed=steam_community_announcements),
    sensors, relays, logic and controlled buildings.
  - **[P6]** [official Wonders preview](https://store.steampowered.com/news/posts/?appgroupname=Timberborn&appids=1062090&enddate=1718364121&feed=steam_community_announcements),
    faction wonders and first-activation completion.
- Current mechanics references:
  - **[P7]** [Game Settings](https://timberborn.wiki.gg/wiki/Game_Settings),
    Normal population, supplies and weather parameters.
  - **[P8]** [Weather](https://timberborn.wiki.gg/wiki/Weather), forecast,
    drought, badtide, contamination and plant effects.
  - **[P9]** [Building](https://timberborn.wiki.gg/wiki/Building), access,
    staffing, priorities, construction and operation.
  - **[P10]** [Folktails](https://timberborn.wiki.gg/wiki/Folktails),
    housing-bound reproduction.
  - **[P11]** [Well-Being](https://timberborn.wiki.gg/wiki/Well-Being), needs
    and work, movement, growth and lifespan modifiers.
  - **[P12]** [Power](https://timberborn.wiki.gg/wiki/Power), connected shafts,
    generation and consumption.
  - **[P13]** [Gravity Battery](https://timberborn.wiki.gg/wiki/Gravity_Battery),
    surplus storage and deficit release.
  - **[P14]** [Science Points](https://timberborn.wiki.gg/wiki/Science_Points),
    staffed production and construction unlocks.
  - **[P15]** [Earth Recultivator](https://timberborn.wiki.gg/wiki/Earth_Recultivator),
    exact unlock, construction, launch and victory requirements.
- Claim IDs: `TIMBER-001`–`TIMBER-013`.

## Mechanical decomposition

### Action Genes

- Reused: `ACT-006` changes speed; `ACT-068` edits paths; `ACT-120` sets
  recipes, storage filters and operating rules; `ACT-139` places settlement
  buildings; `ACT-144` marks natural objects for work; `ACT-145` changes task
  priority; `ACT-148` commits material-backed construction plans.
- New: `ACT-175` purchases a construction unlock with Science Points;
  `ACT-176` connects and configures a sensor, logic node and target.
- Claim IDs: `TIMBER-003`–`TIMBER-011`.

### System Behaviour Genes

- Reused: `SYS-156` runs staffed recipes; `SYS-162` fulfils supplied build
  plans; `SYS-186` routes agents to ranked errands; `SYS-192` propagates
  automation signals; `SYS-196` routes hauling.
- New: `SYS-255`–`SYS-260`, `SYS-262` and `SYS-263` cover terrain water, weather, plant growth,
  individual needs, Folktail reproduction, shaft power, automation signals,
  Science Points and the Earth Recultivator.
- Resolution order: accept edits; advance weather and water; update soil and
  plants; route jobs, hauling and construction; run recipes, science and power;
  resolve needs and population; propagate automation; advance and test wonder.
- Claim IDs: `TIMBER-002`–`TIMBER-013`.

### Constraint Genes

- Reused: `CON-062` footprint; `CON-172` recipe flow; `CON-173` extraction
  locus; `CON-184` unlocked design and build materials; `CON-185` finite
  workers and job slots; `CON-193` compatible cells and delivered material.
- New: `CON-229` water geometry; `CON-230` plant water state; `CON-231`
  housing-bound reproduction; `CON-232` connected power; `CON-233` automation
  compatibility; `CON-234` science cost; `CON-235` exact wonder gates.
- Claim IDs: `TIMBER-003`–`TIMBER-012`.

### Information Genes

- Reused: `INF-001` exposes the map; `INF-060` exposes production bottlenecks;
  `INF-086` exposes population, well-being and work allocation.
- New: `INF-091`, `INF-092`, `INF-094`–`INF-096` expose weather, water, goods
  and power, automation, and wonder progress.
- Claim IDs: `TIMBER-002`–`TIMBER-012`.

### Objective Genes

- `OBJ-068` completes the scoped map on first Earth Recultivator activation.
- Claim IDs: `TIMBER-011`–`TIMBER-013`.

### Time Genes

- `TIM-003` advances water, weather, work, needs, plants, power and production.
- Claim IDs: `TIMBER-002`–`TIMBER-012`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh Waterfalls settlement, Folktails, Normal | Start and advance one cycle | Fixed terrain starts with the declared population; mode bounds the first temperate period and later events | reproducible setup and weather boundary | `TIMBER-002` |
| Water source above a basin; compatible cells and logs | Plan dam, levee and floodgate | Builders deliver materials; the barrier retains live water up to its geometry and opening | construction edits conserved water | `TIMBER-003`, `TIMBER-005` |
| Crops or trees beside retained water | Advance temperate time | Irrigation enables growth; dryness halts it and contamination kills susceptible plants | water drives biological production | `TIMBER-004` |
| Several reachable jobs and idle adults | Raise one priority | Eligible beavers claim higher-ranked errands; one staffed slot removes that adult from competitors | labour is finite and indirect | `TIMBER-005`, `TIMBER-007` |
| Free lodge bed and sustained adult population | Advance life-cycle time | Folktails reproduce toward capacity; children mature and deaths reopen space with delay | housing is a population cap, not instant growth | `TIMBER-006` |
| Supplied advanced-material workplaces joined to storage | Select recipes and advance | Haulers supply inputs, staff repeat recipes and outputs stop at storage or input bottlenecks | production couples labour and logistics | `TIMBER-007` |
| Variable generators, consumers and Gravity Battery share shafts | Advance through surplus and deficit | Surplus raises the weight; later deficit releases stored energy until exhausted | power is a live connected balance | `TIMBER-008` |
| Staffed Inventor and enough points; building locked | Pay its Science Point price | Points fall once and the construction remains plan-ready | research production and unlock purchase differ | `TIMBER-009` |
| Sensor, relay and compatible pump or floodgate | Connect and set threshold | Measurements propagate and toggle the target when the predicate changes | automation closes an environmental feedback loop | `TIMBER-010` |
| 20,000 science and advanced chains | Unlock and plan Earth Recultivator | Beavers deliver 2,000 gears, 2,000 treated planks and 1,500 metal blocks | wonder aggregates the economy | `TIMBER-011` |
| Completed wonder with 500 Extract and 500 Paper | Activate it | Supplies are consumed, congratulations appear, map win and flexible start unlock | first launch is a bounded endpoint | `TIMBER-012`, `TIMBER-013` |

## Strategic and experiential structure

- Local decision: place or prioritise one path, barrier, pump, store, workplace,
  home, power link, sensor or construction plan.
- Medium-term planning: retain clean water through drought, divert badwater,
  stabilise food and population, and balance labour, hauling, storage and power.
- Long-term structure: unlock advanced chains, automate a water response,
  accumulate the wonder's large material phases and provision its first launch.
- Failure attribution: forecasts, overlays, status panels, job counts, needs,
  inventories, power and automation expose bottlenecks; event draws retain pressure.

## Replay and variation

- What changes: reservoir geometry, crop and housing layout, priorities,
  production ratios, power mix and automation topology.
- Randomness: Waterfalls terrain is fixed; Normal draws escalating drought and
  badtide durations and order within declared bounds.
- Multiple viable strategies: yes; water, population, power and manufacturing
  layouts can reach the same first wonder launch.

## Adjacent systems and history

- Similar games: Oxygen Not Included, Dwarf Fortress, Against the Storm,
  Frostpunk, Factorio and Anno 1800.
- Important differences: conserved surface water, seasonal source substitution
  and vertical dam geometry jointly govern survival, crops, power and automation.

## Adjacent comparison

- Oxygen Not Included routes autonomous errands through fluids, but simulates
  multi-element cells, gases and heat rather than outdoor river impoundment.
- Against the Storm and Frostpunk share staffed weather pressure, but neither
  lets barriers reshape a persistent 3D water body that irrigates and powers.
- Factorio and Anno 1800 share recipes and logistics; Timberborn uses beaver
  hauling, housing-bound reproduction and a faction wonder.

## Taxonomy impact

- Existing construction, priority, hauling, recipe, placement and real-time
  genes retain their boundaries and gain another evidence case.
- New genes isolate terrain water, seasonal sources, plant contamination,
  housing reproduction, shaft power, signal automation, science and wonder gates.

## Negative results

- `SYS-187` was rejected: Timberborn has dedicated terrain water, not Oxygen
  Not Included's multi-element gas/liquid cell simulation.
- `SYS-229` was rejected: weather escalates partly randomly rather than following
  Frostpunk's authored scenario timeline.
- `SYS-157` was rejected: ordinary goods move by agents, not belts or pipes.
- Optional bots, ziplines, districts and exhaustive terraforming were excluded
  because the declared Folktails wonder route does not require them.

## Delta summary

## Нові факти

- Зафіксовано `1.0`, revised Waterfalls, Normal weather, terrain water/badwater,
  Folktail population, automation і точні Earth Recultivator gates.

## Нові гени

- Додано `ACT-175`–`ACT-176`, `SYS-255`–`SYS-260`, `SYS-262`, `SYS-263`,
  `CON-229`–`CON-235`, `INF-091`, `INF-092`, `INF-094`–`INF-096` та `OBJ-068`.

## Нові комбінації

- `COMB-0131` фіксує шлях від seasonal water engineering через settlement
  automation і advanced production до першого запуску wonder.

## Зміни таксономії

- Межі наявних генів не змінено; taxonomy-change record не потрібен.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-006`, `ACT-068`, `ACT-120`, `ACT-139`, `ACT-144`, `ACT-145`, `ACT-148`, `ACT-175`, `ACT-176` | water, job, storage, science and automation parameters |
| System Behaviour | `SYS-156`, `SYS-162`, `SYS-186`, `SYS-196`, `SYS-255`–`SYS-263` | water, weather, work, population, power, science and wonder parameters |
| Constraint | `CON-062`, `CON-172`, `CON-173`, `CON-184`, `CON-185`, `CON-193`, `CON-229`–`CON-235` | geometry, staffing, ecology, power and wonder gates |
| Information | `INF-001`, `INF-060`, `INF-091`–`INF-096` | forecast, water, colony, networks and wonder disclosure |
| Objective | `OBJ-068` | first Earth Recultivator activation |
| Time | `TIM-003` | continuous pausable simulation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `132` (`GAME-0001`–`GAME-0132`).
- Exact genome matches: none.
- Tied near matches: `GAME-0126` — Dwarf Fortress (`15 / 73 = 0.205479`).
- Supported combination subsets: `COMB-0131`.
- Scan date: 2026-08-21.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0126`.
