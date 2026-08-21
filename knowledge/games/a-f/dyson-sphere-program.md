---
game_id: GAME-0131
slug: dyson-sphere-program
game_title: Dyson Sphere Program
analysis_status: reviewed
reviewed: 2026-08-20
combination_ids:
  - COMB-0129
gene_ids:
  action:
    - ACT-008
    - ACT-119
    - ACT-120
    - ACT-121
    - ACT-122
    - ACT-123
    - ACT-124
    - ACT-161
    - ACT-169
    - ACT-170
  system:
    - SYS-051
    - SYS-156
    - SYS-157
    - SYS-158
    - SYS-159
    - SYS-161
    - SYS-162
    - SYS-215
    - SYS-236
    - SYS-237
    - SYS-238
    - SYS-239
    - SYS-240
    - SYS-241
    - SYS-242
    - SYS-243
  constraint:
    - CON-062
    - CON-136
    - CON-172
    - CON-173
    - CON-217
    - CON-218
    - CON-219
    - CON-220
    - CON-221
    - CON-222
  information:
    - INF-001
    - INF-059
    - INF-060
    - INF-081
    - INF-082
    - INF-083
    - INF-084
    - INF-085
  objective:
    - OBJ-066
  time:
    - TIM-003
---

# Game: Dyson Sphere Program

## Analysis scope

- Version / ruleset: current Early Access PC build `0.10.34.28524`, ordinary
  single-player new game with default resource multiplier and Regular Dark Fog,
  from Icarus landing in a seeded cluster through researching `Mission Completed!`.
- Included: direct Icarus movement, flight and warp; mecha energy; manual mining
  and replicator crafting; spherical-grid construction and blueprints; finite
  veins; powered recipe production; belts, sorters, stations, drones and vessels;
  matrix research; interplanetary and interstellar expansion; Dark Fog threat,
  direct combat and automated defence; swarm or sphere planning, solar sails,
  carrier rockets, Ray Receivers, Critical Photons, antimatter, Universe Matrix
  and the main-mission research.
- Excluded: customised seeds, resource multipliers or combat parameters; Peace
  and Sandbox modes; metadata reconstruction after destruction; optional Dark
  Fog farming and complete hive eradication; proliferator optimisation, rare
  resource shortcuts, Holo Beacon notes, cosmetic mecha customisation, achievements,
  mods, speedruns, post-mission infinite research and megabase optimisation.
  Announced vehicles, space stations, comprehensive combat revision and space
  combat are explicitly future systems and are not imported into this record.
- Direct-play status: not conducted. Official product and update pages establish
  the current Early Access boundary, default combat-bearing factory premise and
  future exclusions. Current maintained mechanics references corroborate the
  reproducible production, travel, logistics, sphere and mission transitions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DSP-001` | `0.10.34.28524` is the latest published build; vehicles, space stations and complete space combat remain future work | Confirmed | Direct | High | P1, P2 |
| `DSP-002` | A setup seed deterministically creates the persistent cluster's stars, planets and resource distribution | Confirmed | Corroborated | High | P3 |
| `DSP-003` | Icarus is directly steered across surface, flight, sail and warp states while a fuel-backed core-energy reserve pays for high-load activity | Confirmed | Corroborated | High | P4, P5 |
| `DSP-004` | Supplied construction drones materialise individual or blueprint requests on a latitude-banded spherical grid | Confirmed | Corroborated | High | P4, P6, P7 |
| `DSP-005` | Powered miners deplete finite veins; supplied machines repeat recipes while belts and sorters move discrete materials and power shortage proportionally throttles consumers | Confirmed | Corroborated | High | P8–P10 |
| `DSP-006` | Matrix Labs either produce typed matrices or consume the selected technology's required matrices as hashes until its persistent unlock | Confirmed | Corroborated | High | P11, P12 |
| `DSP-007` | Station supply and demand settings dispatch powered drones locally and vessels remotely; practical interstellar service requires researched warping and Space Warpers | Confirmed | Corroborated | High | P13–P15 |
| `DSP-008` | Ejectors insert finite-lived sails into configured orbits; rockets construct planned nodes and frames, completed frames absorb sails, and receivers turn stellar output into power or Critical Photons | Confirmed | Corroborated | High | P16–P18 |
| `DSP-009` | Universe Matrix combines all five coloured matrices with antimatter; consuming 2,000 completes the main mission, without requiring a completely filled solid shell | Confirmed | Corroborated | High | P12, P19, P20 |
| `DSP-010` | On default combat settings, industrial activity raises Dark Fog pressure and dispatched waves attack Icarus or factories, while direct weapons and automated defences resolve live damage | Confirmed | Direct | High | P1, P21 |
| `DSP-011` | Factory, power, recipes, research, logistics, navigation, sphere and threat states are inspectable before the relevant decision | Confirmed | Corroborated | High | P4, P11, P13, P16–P18 |
| `DSP-012` | The scoped game shares factory genes with Factorio and Satisfactory but adds spherical, interstellar and stellar-output construction boundaries | Observation | Corroborated | High | GAME-0119, GAME-0128 |

## Basic data

- Release / origin: Youthcat Studio and Gamera Games; Early Access began
  21 January 2021; latest scoped patch published 27 April 2026.
- Platform or physical form: single-player real-time PC factory, exploration and
  construction simulation across a generated star cluster.
- Puzzle family: automation and spatial programming; route and network
  construction; real-time system pressure; ordered dependency sequencing.
- Primary and official sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/1366540/Dyson_Sphere_Program/),
    Early Access status, factory/cluster/sphere premise, interstellar logistics,
    blueprints and Dark Fog defence.
  - **[P2]** [official announcements](https://steamcommunity.com/app/1366540/announcements/),
    patch `0.10.34.28524` and explicit future Creation-system boundary.
- Current mechanics references:
  - **[P3]** [Cluster](https://dyson-sphere-program.fandom.com/wiki/Cluster),
    seeded repeatable cluster generation.
  - **[P4]** [Icarus](https://dyson-sphere-program.fandom.com/wiki/Icarus),
    core energy, fuel and construction drones.
  - **[P5]** [Space Warper](https://dyson-sphere-program.fandom.com/wiki/Space_Warper),
    Drive Engine and consumable warp activation.
  - **[P6]** [Buildings](https://dyson-sphere-program.fandom.com/wiki/Buildings),
    planetary construction categories and spherical grid.
  - **[P7]** [Mass Construction](https://dyson-sphere-program.fandom.com/wiki/Mass_Construction_%28Lv1%29),
    saved blueprint layout, settings and placement requests.
  - **[P8]** [Mining Machine](https://dyson-sphere-program.fandom.com/wiki/Mining_Machine),
    vein coverage, extraction rate and depletion.
  - **[P9]** [Factorio-style production evidence on the official page](https://store.steampowered.com/app/1366540/Dyson_Sphere_Program/),
    belts, automated facilities and stable output.
  - **[P10]** [Power](https://wikiwiki.jp/dsp/%E9%9B%BB%E5%8A%9B),
    connected-grid satisfaction.
  - **[P11]** [Research](https://dyson-sphere-program.fandom.com/wiki/Research),
    queue, matrix consumption, hashes and unlocks.
  - **[P12]** [Matrix Lab](https://dyson-sphere-program.fandom.com/wiki/Matrix_Lab),
    matrix-production and research modes including Universe Matrix recipe.
  - **[P13]** [Planetary Logistics Station](https://dyson-sphere-program.fandom.com/wiki/Planetary_Logistics_Station),
    typed supply/demand and drone dispatch.
  - **[P14]** [Interstellar Logistics Station](https://dyson-sphere-program.fandom.com/wiki/Interstellar_Logistics_Station),
    local/remote slots, vessels, range, charge and warpers.
  - **[P15]** [Logistics Drone](https://dyson-sphere-program.fandom.com/wiki/Logistics_Drone),
    charge-backed bounded cargo trips.
  - **[P16]** [Dyson Sphere](https://dyson-sphere-program.fandom.com/wiki/Dyson_Sphere),
    free-form plan, rockets, frames and sail absorption.
  - **[P17]** [Ray Receiver](https://dyson-sphere-program.fandom.com/wiki/Ray_Receiver),
    continuous receiving, power and Critical Photon modes.
  - **[P18]** [Dyson Sphere overview](https://dyson-sphere-program.fandom.com/wiki/Dyson_Sphere),
    stellar output and antimatter route.
  - **[P19]** [Universe Matrix](https://dyson-sphere-program.fandom.com/wiki/Universe_Matrix),
    five matrices plus antimatter and mission role.
  - **[P20]** [technology list](https://wikiwiki.jp/dsp/%E6%8A%80%E8%A1%93%E7%A0%94%E7%A9%B6),
    `Mission Completed!` cost and prerequisites.
  - **[P21]** [official Rise of the Dark Fog product text](https://store.steampowered.com/app/1366540/Dyson_Sphere_Program/),
    activity-linked assaults, Icarus targeting and defence structures.
- Claim IDs: `DSP-001`–`DSP-012`.

## Mechanical decomposition

### Action Genes

- Reused: `ACT-008` steers Icarus; `ACT-119` places and removes live factory and
  defence entities; `ACT-120` configures recipes, station slots, filters and
  receiver or launcher modes; `ACT-121` queues research; `ACT-122` manually
  extracts; `ACT-123` uses the replicator; `ACT-124` stamps blueprints;
  `ACT-161` targets and attacks live enemies.
- New: `ACT-169` edits persistent swarm and sphere plans; `ACT-170` changes
  Icarus between flight, sail and warp regimes.
- Parameters: seed-specific world, building, recipe, item, plan geometry,
  research queue, weapon, drive, energy and warper.
- Claim IDs: `DSP-002`–`DSP-010`.

### System Behaviour Genes

- Reused: `SYS-051` automated defence engagement; `SYS-156` repeated recipe
  production; `SYS-157` belt and sorter flow; `SYS-158` proportional power
  satisfaction; `SYS-159` matrix research; `SYS-161` vein depletion; `SYS-162`
  supplied construction-drone fulfilment; `SYS-215` direct live combat.
- New: `SYS-236`–`SYS-243` cover seeded clusters, mecha energy, cross-frame
  travel, station dispatch, sail orbits, structural launches, receiver conversion
  and industrially generated Dark Fog waves.
- Resolution order: accept player edits and movement; construction drones fulfil
  valid requests; miners, logistics, production, power and research advance;
  Icarus energy and travel advance; stations dispatch carriers; launchers update
  swarm and sphere state; receivers convert output; Dark Fog threat and combat
  resolve; test main-mission research completion.
- Claim IDs: `DSP-002`–`DSP-010`.

### Constraint Genes

- Reused: `CON-062` ordinary footprint compatibility; `CON-136` persistent
  technology dependencies; `CON-172` compatible recipe and inventory flow;
  `CON-173` extractor-to-resource-locus compatibility.
- New: `CON-217` spherical band placement; `CON-218` Icarus warp inputs;
  `CON-219` logistics match and carrier eligibility; `CON-220` ejector orbit
  window; `CON-221` rocket target plan; `CON-222` receiver access and mode.
- Scarce strategic resources: finite ores and oil rate, land and grid bands,
  Icarus energy, fuels, factory power, belts and sorter throughput, station
  charge, carriers, warpers, matrices, sails, rockets, receiver time, ammunition,
  defence coverage and production time.
- Claim IDs: `DSP-003`–`DSP-010`.

### Information Genes

- Reused: `INF-001` exposes the current world; `INF-059` exposes recipes and
  technology dependencies; `INF-060` exposes production, power and factory
  bottlenecks.
- New: `INF-081`–`INF-085` expose the star map and resources, Icarus travel and
  energy, station slots and carriers, Dyson plans and output, and Dark Fog threat.
- Claim IDs: `DSP-002`–`DSP-011`.

### Objective Genes

- `OBJ-066` completes the bounded run by producing and consuming 2,000 Universe
  Matrices for `Mission Completed!`; it does not require filling an entire shell.
- Claim ID: `DSP-009`.

### Time Genes

- `TIM-003` keeps factory, logistics, research, travel, orbital construction,
  energy and threats live while the player moves or edits.
- Claim IDs: `DSP-003`–`DSP-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| New default game with a declared cluster seed | Start the run | The same stars, planets, orbit relations and deposits instantiate and persist | setup creates strategic spatial topology | `DSP-002` |
| Reachable iron veins; Mining Machine in inventory | Place and rotate the miner over several veins | Drones consume the building item; powered operation produces ore per covered vein and decreases those reserves | construction, locus compatibility and depletion are distinct | `DSP-004`, `DSP-005` |
| Smelter, belts and sorters powered and supplied | Select an ingot recipe and advance time | Inputs move into the smelter, repeat into outputs and leave on the configured belt; insufficient power lowers satisfaction and speed | live factory and proportional power are coupled but separate | `DSP-005` |
| Saved compatible factory blueprint; buildings in Icarus inventory | Stamp it within one spherical grid band | Persistent requests appear; available construction drones consume matching inventory and materialise valid entities | blueprint, curved placement and agent fulfilment are distinct | `DSP-004` |
| Matrix Labs supplied with the selected technology's cube set | Queue the technology | Researching labs consume matrices into hashes until the unlock persists, then the queue advances | research is material and time based | `DSP-006` |
| Titanium station is remote Supply; home station remote Demand; powered vessel available | Advance logistics | A matching load triggers a vessel trip, transfers bounded cargo and returns; interstellar distance additionally consumes warpers under the station rule | remote mode is a dispatch rule with explicit eligibility | `DSP-007` |
| Icarus in sail mode with Drive Engine 4, core energy and a Space Warper | Activate warp toward another star | One warper is consumed and accelerated steered travel drains core energy until deactivation or arrival | warp is controlled travel, not fast travel | `DSP-003` |
| Configured swarm orbit; powered ejector supplied with sails and inside pitch window | Advance time | Each shot consumes a sail, inserts it into orbit and adds finite-lived output | orbit plan, firing gate and sail ageing are distinct | `DSP-008` |
| Planned sphere nodes and frames; powered silo supplied with rockets | Advance time | Rockets launch only toward unfinished planned structure, increment nodes and frames, and completed regions begin absorbing available sails | material launches fulfil persistent orbital geometry | `DSP-008` |
| Swarm or partial sphere output available; receiver continuously aligned in Photon mode | Advance time | Allocated stellar output becomes Critical Photons; collider products yield antimatter for Universe Matrix | the stellar structure is an upstream production system | `DSP-008`, `DSP-009` |
| Regular Dark Fog base present and industrial power raises threat to threshold | Advance time and defend | A bounded hostile wave dispatches; Icarus attacks selected targets while powered turrets automatically engage eligible units | industrial growth creates live defensive pressure | `DSP-010` |
| All five matrices and antimatter feed Universe Matrix labs; 2,000 white matrices reach research labs | Queue `Mission Completed!` | Required hashes consume the declared matrices and present main-mission completion while the factory remains playable | the scoped ending is research, not a full-shell occupancy test | `DSP-009` |

## Strategic and experiential structure

- Local decision: place or configure one machine, belt, station, defence, recipe,
  blueprint, orbit, sphere element, research or Icarus movement regime.
- Medium-term planning: balance finite deposits, power, throughput, interplanetary
  titanium and silicon, matrices, station capacity, warpers, defence and mecha fuel.
- Long-term structure: expand from one spherical factory to a multi-planet and
  then interstellar supply graph, create enough stellar output for photons and
  antimatter, and sustain 2,000 Universe Matrices under ongoing threat.
- Failure attribution: visible production, power, resource, logistics, energy,
  orbit, receiver and threat panels expose most bottlenecks; travel steering and
  generated cluster topology preserve execution and planning uncertainty.

## Replay and variation

- What changes: cluster seed, planet and resource topology, factory layout,
  star choice, research order, logistics architecture, sphere geometry, defence
  footprint and Dark Fog encounters.
- Randomness: the declared seed fixes initial topology; default hostile activity
  and combat outcomes vary during live play.
- Multiple viable strategies: yes; local belts versus stations, power sources,
  star and sphere design, swarm-versus-shell timing, resource routes and defence
  posture vary under the same Mission Completed boundary.

## Adjacent systems and history

- Similar games: Factorio, Satisfactory, shapez 2 and Oxygen Not Included.
- Important differences: Dyson Sphere Program retains an embodied mecha and
  finite powered factory while changing the build surface from one plane to
  multiple curved planets, matching station requests across space and turning
  a player-authored stellar structure into a required upstream production source.

## Adjacent comparison

- Factorio shares powered finite-resource automation, research, blueprints and
  industrial attack pressure, but remains one flat map and ends at a rocket.
- Satisfactory shares direct embodied factory construction but uses infinite
  resource nodes, pipeline/head-lift logistics and binary power trips.
- shapez 2 shares live spatial production without finite materials, power,
  embodied travel, research logistics or hostile pressure.
- Dyson Sphere Program's distinguishing structure is a continuous factory graph
  that grows across curved planets and star systems, then materialises an
  editable stellar plan whose output becomes the antimatter input to its ending.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-119`–`ACT-124`, `ACT-161`, `ACT-169`, `ACT-170` | factory, combat, orbit and travel parameters |
| System Behaviour | `SYS-051`, `SYS-156`–`SYS-159`, `SYS-161`, `SYS-162`, `SYS-215`, `SYS-236`–`SYS-243` | production, travel, logistics, orbital and threat parameters |
| Constraint | `CON-062`, `CON-136`, `CON-172`, `CON-173`, `CON-217`–`CON-222` | grid, flow, travel, dispatch and launch gates |
| Information | `INF-001`, `INF-059`, `INF-060`, `INF-081`–`INF-085` | factory, star, mecha, station, sphere and threat disclosure |
| Objective | `OBJ-066` | Universe Matrix mission research |
| Time | `TIM-003` | continuous pausable simulation |

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`: `ACT-008,ACT-119,ACT-120,ACT-121,ACT-122,ACT-123,ACT-124,ACT-161,ACT-169,ACT-170; SYS-051,SYS-156,SYS-157,SYS-158,SYS-159,SYS-161,SYS-162,SYS-215,SYS-236,SYS-237,SYS-238,SYS-239,SYS-240,SYS-241,SYS-242,SYS-243; CON-062,CON-136,CON-172,CON-173,CON-217,CON-218,CON-219,CON-220,CON-221,CON-222; INF-001,INF-059,INF-060,INF-081,INF-082,INF-083,INF-084,INF-085; OBJ-066; TIM-003`.
- Indexed games scanned: 131, including this record.
- Indexed combinations scanned: 129.
- Exact genome matches: none.
- Near matches and similarity scores: `GAME-0119` is highest at
  `20 / 49 = 0.408163`.
- Supported combination subsets: `COMB-0129`.
- Scan date: 2026-08-20.

### Full prior-game Jaccard scan

- GAME-0001: 1 / 59 = 0.016949; GAME-0002: 1 / 52 = 0.019231; GAME-0003: 0 / 55 = 0.000000; GAME-0004: 2 / 59 = 0.033898.
- GAME-0005: 1 / 52 = 0.019231; GAME-0006: 2 / 53 = 0.037736; GAME-0007: 1 / 53 = 0.018868; GAME-0008: 1 / 52 = 0.019231.
- GAME-0009: 1 / 61 = 0.016393; GAME-0010: 1 / 54 = 0.018519; GAME-0011: 1 / 58 = 0.017241; GAME-0012: 1 / 54 = 0.018519.
- GAME-0013: 1 / 58 = 0.017241; GAME-0014: 1 / 60 = 0.016667; GAME-0015: 1 / 59 = 0.016949; GAME-0016: 2 / 59 = 0.033898.
- GAME-0017: 0 / 59 = 0.000000; GAME-0018: 2 / 63 = 0.031746; GAME-0019: 1 / 55 = 0.018182; GAME-0020: 1 / 59 = 0.016949.
- GAME-0021: 2 / 53 = 0.037736; GAME-0022: 2 / 56 = 0.035714; GAME-0023: 0 / 56 = 0.000000; GAME-0024: 1 / 57 = 0.017544.
- GAME-0025: 2 / 55 = 0.036364; GAME-0026: 2 / 56 = 0.035714; GAME-0027: 3 / 55 = 0.054545; GAME-0028: 3 / 60 = 0.050000.
- GAME-0029: 3 / 55 = 0.054545; GAME-0030: 2 / 58 = 0.034483; GAME-0031: 1 / 56 = 0.017857; GAME-0032: 1 / 56 = 0.017857.
- GAME-0033: 3 / 56 = 0.053571; GAME-0034: 3 / 57 = 0.052632; GAME-0035: 3 / 61 = 0.049180; GAME-0036: 2 / 56 = 0.035714.
- GAME-0037: 1 / 54 = 0.018519; GAME-0038: 3 / 59 = 0.050847; GAME-0039: 1 / 54 = 0.018519; GAME-0040: 2 / 52 = 0.038462.
- GAME-0041: 3 / 54 = 0.055556; GAME-0042: 2 / 53 = 0.037736; GAME-0043: 2 / 58 = 0.034483; GAME-0044: 2 / 54 = 0.037037.
- GAME-0045: 2 / 58 = 0.034483; GAME-0046: 1 / 55 = 0.018182; GAME-0047: 1 / 59 = 0.016949; GAME-0048: 1 / 59 = 0.016949.
- GAME-0049: 0 / 55 = 0.000000; GAME-0050: 2 / 59 = 0.033898; GAME-0051: 2 / 60 = 0.033333; GAME-0052: 1 / 55 = 0.018182.
- GAME-0053: 2 / 53 = 0.037736; GAME-0054: 2 / 55 = 0.036364; GAME-0055: 2 / 54 = 0.037037; GAME-0056: 1 / 53 = 0.018868.
- GAME-0057: 1 / 53 = 0.018868; GAME-0058: 1 / 54 = 0.018519; GAME-0059: 1 / 52 = 0.019231; GAME-0060: 1 / 52 = 0.019231.
- GAME-0061: 1 / 55 = 0.018182; GAME-0062: 1 / 53 = 0.018868; GAME-0063: 1 / 52 = 0.019231; GAME-0064: 1 / 50 = 0.020000.
- GAME-0065: 0 / 53 = 0.000000; GAME-0066: 0 / 56 = 0.000000; GAME-0067: 0 / 54 = 0.000000; GAME-0068: 0 / 54 = 0.000000.
- GAME-0069: 1 / 53 = 0.018868; GAME-0070: 1 / 53 = 0.018868; GAME-0071: 1 / 52 = 0.019231; GAME-0072: 1 / 53 = 0.018868.
- GAME-0073: 1 / 52 = 0.019231; GAME-0074: 1 / 54 = 0.018519; GAME-0075: 1 / 54 = 0.018519; GAME-0076: 1 / 52 = 0.019231.
- GAME-0077: 1 / 52 = 0.019231; GAME-0078: 1 / 52 = 0.019231; GAME-0079: 1 / 52 = 0.019231; GAME-0080: 1 / 52 = 0.019231.
- GAME-0081: 1 / 53 = 0.018868; GAME-0082: 1 / 53 = 0.018868; GAME-0083: 1 / 53 = 0.018868; GAME-0084: 1 / 55 = 0.018182.
- GAME-0085: 1 / 56 = 0.017857; GAME-0086: 2 / 57 = 0.035088; GAME-0087: 3 / 53 = 0.056604; GAME-0088: 2 / 53 = 0.037736.
- GAME-0089: 2 / 53 = 0.037736; GAME-0090: 3 / 58 = 0.051724; GAME-0091: 3 / 52 = 0.057692; GAME-0092: 2 / 54 = 0.037037.
- GAME-0093: 1 / 54 = 0.018519; GAME-0094: 3 / 53 = 0.056604; GAME-0095: 3 / 55 = 0.054545; GAME-0096: 3 / 53 = 0.056604.
- GAME-0097: 3 / 51 = 0.058824; GAME-0098: 3 / 50 = 0.060000; GAME-0099: 2 / 52 = 0.038462; GAME-0100: 1 / 56 = 0.017857.
- GAME-0101: 0 / 56 = 0.000000; GAME-0102: 0 / 53 = 0.000000; GAME-0103: 1 / 54 = 0.018519; GAME-0104: 2 / 53 = 0.037736.
- GAME-0105: 2 / 54 = 0.037037; GAME-0106: 0 / 53 = 0.000000; GAME-0107: 2 / 52 = 0.038462; GAME-0108: 2 / 54 = 0.037037.
- GAME-0109: 1 / 61 = 0.016393; GAME-0110: 2 / 52 = 0.038462; GAME-0111: 3 / 50 = 0.060000; GAME-0112: 3 / 51 = 0.058824.
- GAME-0113: 3 / 57 = 0.052632; GAME-0114: 2 / 51 = 0.039216; GAME-0115: 1 / 51 = 0.019608; GAME-0116: 3 / 49 = 0.061224.
- GAME-0117: 2 / 52 = 0.038462; GAME-0118: 1 / 61 = 0.016393; GAME-0119: 20 / 49 = 0.408163; GAME-0120: 0 / 75 = 0.000000.
- GAME-0121: 1 / 68 = 0.014706; GAME-0122: 7 / 54 = 0.129630; GAME-0123: 1 / 83 = 0.012048; GAME-0124: 9 / 84 = 0.107143.
- GAME-0125: 10 / 78 = 0.128205; GAME-0126: 9 / 80 = 0.112500; GAME-0127: 10 / 84 = 0.119048; GAME-0128: 13 / 49 = 0.265306.
- GAME-0129: 6 / 75 = 0.080000; GAME-0130: 10 / 89 = 0.112360.

## Evidence and unknowns

- Official sources establish the current build, Early Access boundary, core
  factory/interstellar/sphere premise, Dark Fog pressure and which announced
  systems remain absent. Community-maintained references supply reproducible
  values and gates; those details should be re-reviewed after the announced
  final major update or full release.
- Direct play was not conducted. No claim is made about optimal ratios, minimum
  research route, complete sphere percentage, exact wave cadence or novelty.
- The record deliberately rejects the common overstatement that a fully filled
  Dyson shell is necessary for the ending: a working swarm or partial sphere can
  provide receiver photons, and `Mission Completed!` is a matrix-research gate.

## Verification checklist

- [x] Current version and future-content boundary are explicit.
- [x] Complete scoped rules decompose into atomic canonical genes.
- [x] Reproducible transitions cover production, travel, logistics, sphere,
  combat and ending.
- [x] Full prior-game Jaccard scan is recorded.
- [x] `COMB-0129` is a proper subset of the admitted genome.
- [x] No novelty claim is made.
- [x] Reviewed Ukrainian and bilingual presentation layers are required in the
  same unit.

## Taxonomy decisions

- Reused `SYS-158`, not Satisfactory's hard-trip `SYS-211`: insufficient Dyson
  grid power lowers satisfaction and throttles consumers proportionally.
- Reused `SYS-161`, not infinite-node parameters: default mineral reserves are
  finite even though Veins Utilization can improve consumption efficiency.
- Generalised `SYS-162` from network-only robots to supplied construction agents
  so Icarus drones and Factorio network robots share the same fulfilment boundary.
- Kept station supply/demand dispatch separate from belts in `SYS-239`; its
  two-ended matching, carrier eligibility and energy-backed trip are causal.
- Kept orbital plan, sail orbit, structural launches and receiver conversion
  separate; none is a mere animation of another.

## Taxonomy impact

- New genes: `ACT-169`, `ACT-170`, `SYS-236`–`SYS-243`, `CON-217`–`CON-222`,
  `INF-081`–`INF-085`, `OBJ-066`.
- Revised reuse boundary: `SYS-162` now covers supplied construction agents,
  including owner-supplied Icarus drones and network-supplied Factorio robots.
- New family: none; existing `FAM-008`, `FAM-010`, `FAM-015` and `FAM-017` fit.

## Negative results

- Rejected `SYS-160`: Dark Fog threat is not a spatially diffusing pollution
  cloud, despite the shared industry-to-attack consequence.
- Rejected `SYS-210`: technology unlocks consume matrices over research time,
  not one selected direct-delivery milestone.
- Rejected `SYS-211`: a deficit throttles a Dyson grid instead of tripping the
  whole connected network.
- Rejected a mandatory-complete-sphere constraint: receiver photons and the
  main mission do not test every planned shell cell.
- Rejected future vehicles, space stations and comprehensive space combat:
  official 2026 notes say they are still in development.

## Delta summary

## Нові факти

- The stable scoped end is `Mission Completed!` research with 2,000 Universe
  Matrices, not visual completion of a solid Dyson shell.
- Default Regular Dark Fog belongs to ordinary current progression and cannot
  be silently omitted as an optional side system.
- Spherical factory bands, interstellar carrier matching and material orbital
  construction create causal boundaries absent from the closest factory games.

## Нові гени

- Added `ACT-169`, `ACT-170`, `SYS-236`–`SYS-243`, `CON-217`–`CON-222`,
  `INF-081`–`INF-085` and `OBJ-066`.
- Revised `SYS-162` to admit both network-supplied and owner-supplied
  construction-agent fulfilment without merging direct placement.

## Нові комбінації

- Added `COMB-0129`, the interstellar finite-resource factory whose orbital
  launches create the photon/antimatter input for its final matrix research.

## Зміни таксономії

- Assigned the game to existing automation, network, real-time pressure and
  ordered dependency families. No one-game family was created.
