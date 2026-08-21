---
game_id: GAME-0128
slug: satisfactory
game_title: Satisfactory
analysis_status: reviewed
reviewed: 2026-08-20
combination_ids:
  - COMB-0126
gene_ids:
  action:
    - ACT-119
    - ACT-120
    - ACT-122
    - ACT-123
  system:
    - SYS-156
    - SYS-157
    - SYS-210
    - SYS-211
  constraint:
    - CON-062
    - CON-172
    - CON-173
  information:
    - INF-001
    - INF-059
    - INF-060
  objective:
    - OBJ-054
  time:
    - TIM-003
---

# Game: Satisfactory

## Analysis scope

- Version / ruleset: released Satisfactory 1.0 base game, ordinary single-player
  progression from onboarding through launching Project Assembly.
- Included: manual extraction and hand crafting; placing, rotating, removing and
  configuring factory entities; infinite resource nodes; belts, lifts, pipelines,
  pumps and item/fluid logistics; solid and fluid recipes, by-products and
  automated production; connected power grids and power trips; HUB Milestones;
  Space Elevator Project Assembly deliveries; the final launch.
- Excluded: multiplayer; alternate recipes, MAM research, AWESOME Shop and
  cosmetic customisation; vehicles, trains, drones, nuclear processing,
  combat, exploration, creatures, narrative collectibles, mods, advanced-game
  efficiency challenges and post-ending free play. They change breadth and
  parameters, not the bounded factory-progression core analysed here.
- Direct-play status: not conducted. The developer-published Steam description
  establishes the released first-person factory premise; the official
  Satisfactory Wiki establishes the reproducible construction, production,
  logistics, pipeline, fluid-recipe, milestone, power, resource-node and Project
  Assembly transitions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SAT-001` | The pioneer hand-mines/crafts, and places, rotates, dismantles and configures persistent factory entities while the world runs | Confirmed | Corroborated | High | P1, P2, P3 |
| `SAT-002` | A compatible powered production building repeatedly turns supplied solid/fluid inputs into its selected outputs, while belts and pipelines move accepted materials between ports subject to capacity and head lift | Confirmed | Corroborated | High | P3, P4, P9, P10 |
| `SAT-003` | A miner must cover a compatible resource node; those nodes are infinite, with purity changing extraction rate | Confirmed | Direct | High | P5 |
| `SAT-004` | The connected power graph exposes capacity and consumption; if demand exceeds production and storage cannot cover it, the grid trips instead of proportionally throttling each consumer | Confirmed | Direct | High | P6 |
| `SAT-005` | The player pays the currently selected HUB Milestone's declared materials; completion persistently unlocks its listed capabilities, and Space Elevator phase delivery exposes later tiers | Confirmed | Corroborated | High | P2, P7, P8 |
| `SAT-006` | The Space Elevator accepts the required Project Assembly parts, including fluid-dependent Phase 5 production, and completing Phase 5 permits the final Project Assembly launch and ending | Confirmed | Direct | High | P8, P11 |
| `SAT-007` | Current factory entities, recipes, milestones, resource loci, belt/pipeline flow and power diagnostics are inspectable before a local factory decision | Confirmed | Corroborated | High | P2, P3, P6, P7, P9 |
| `SAT-008` | At Atlas resolution the game shares live recipe production and logistics with Factorio, but it has infinite nodes and all-grid power trips rather than finite extraction and proportional shortage throttling | Observation | Corroborated | High | P3–P6, GAME-0119 |

## Basic data

- Release / origin: Coffee Stain Studios; full 1.0 release on 10 September 2024.
- Platform or physical form: first-person open-world factory construction and
  real-time automation simulation.
- Puzzle family: automation and spatial programming; route and network
  construction; ordered dependency sequencing.
- Primary and official sources:
  - **[P1]** [developer-published Steam product page](https://store.steampowered.com/app/526870/Satisfactory/),
    released title, developer, first-person factory premise and conveyor focus.
  - **[P2]** [official Satisfactory Wiki overview](https://satisfactory.wiki.gg/wiki/Satisfactory),
    linked official manual overview of construction, logistics, mining,
    production and power.
  - **[P3]** [official wiki: Constructor](https://satisfactory.wiki.gg/wiki/Constructor),
    automated compatible recipe production, belt input/output and power use.
  - **[P4]** [official wiki: Conveyor Belts](https://satisfactory.wiki.gg/wiki/Conveyor_Belts),
    belt transport and accepted destination-port boundary.
  - **[P5]** [official wiki: Resource Node](https://satisfactory.wiki.gg/wiki/Purity),
    extractor placement on spatial nodes, purity and infinite reserves.
  - **[P6]** [official wiki: Power](https://satisfactory.wiki.gg/wiki/Power_trip),
    graph diagnostics, generation/consumption and deficit power-trip rule.
  - **[P7]** [official wiki: Milestones](https://satisfactory.wiki.gg/wiki/Milestones),
    selected material costs, HUB rewards, tier progression and Space Elevator
    gating.
  - **[P8]** [official wiki: Space Elevator](https://satisfactory.wiki.gg/wiki/Space_Elevator),
    Project Assembly deliveries, tier unlocks and final Phase 5 launch.
  - **[P9]** [official wiki: Pipelines](https://satisfactory.wiki.gg/wiki/Pipelines),
    fluid transport, throughput, single-fluid occupancy, flow indicators and
    liquid head-lift boundary.
  - **[P10]** [official wiki: Refinery](https://satisfactory.wiki.gg/wiki/Refinery),
    mixed solid/fluid recipe ports, buffers, by-products and blocked-output
    shutdown.
  - **[P11]** [official wiki: Biochemical Sculptor](https://satisfactory.wiki.gg/wiki/Biochemical_Sculptor),
    mandatory Phase 5 quantity and its water-consuming Blender recipe, making
    fluid production mandatory for the scoped ending.
- Claim IDs: `SAT-001`–`SAT-008`.

## Mechanical decomposition

### Action Genes

- `ACT-119` places, rotates or dismantles live factory entities; `ACT-120`
  selects a local production recipe or comparable operating rule; `ACT-122`
  manually extracts a resource or dismantles a placed entity; `ACT-123`
  hand-crafts a selected carried-inventory recipe.
- Candidate genes: none. Selecting a HUB Milestone or pulling the Space
  Elevator send handle changes the target of an existing material-delivery
  transition; it is not a new independently authored factory rule.
- Parameters: entity footprint/orientation, recipe, node purity, belt rate,
  power-graph topology, selected milestone and delivery quantities.
- Claim IDs: `SAT-001`, `SAT-003`, `SAT-005`.

### System Behaviour Genes

- `SYS-156` repeatedly executes a supplied solid or fluid production recipe;
  `SYS-157` moves eligible item and fluid quantities through persistent belts
  and pipelines; `SYS-210` turns a selected,
  fully paid material requirement into its persistent milestone or tier unlock;
  `SYS-211` trips an undersupplied connected power grid.
- `SYS-161` is absent: the resource nodes in this scope do not deplete.
  `SYS-158` is absent: Satisfactory's uncovered deficit disconnects the grid,
  rather than distributing insufficient generation by slowing consumers.
  `SYS-159` is absent: milestones consume their listed materials directly,
  rather than laboratories consuming supplied science packs over time.
- Resolution order: accept placement/configuration; advance the real-time
  world; extract from a compatible node; move items through eligible logistics;
  execute each powered compatible recipe; update power capacity, production,
  consumption and any trip; credit fulfilled selected material deliveries and
  persistently unlock their reward set.
- Claim IDs: `SAT-002`–`SAT-006`.

### Constraint Genes

- `CON-062` rejects incompatible static entity footprints; `CON-172` requires
  a compatible entity, recipe, inputs, output capacity and operating state;
  `CON-173` requires a miner or extractor to cover the compatible resource
  locus.
- Scarce strategic resources: carried/build materials, space, production time,
  belt and pipeline capacity, liquid head lift, machine throughput, fuel and
  electrical capacity. World-node reserves are explicitly not scarce.
- Claim IDs: `SAT-001`–`SAT-004`.

### Information Genes

- `INF-001` exposes the relevant current factory state; `INF-059` exposes
  known recipes, milestone prerequisites and their required materials;
  `INF-060` exposes production, belt/pipeline logistics and power-network
  diagnostics.
- Candidate genes: none. Milestone requirements are disclosed rather than
  hidden future-state deduction.
- Claim IDs: `SAT-004`, `SAT-005`, `SAT-007`.

### Objective Genes

- `OBJ-054` completes the bounded base-game progression by manufacturing and
  delivering the ordered Project Assembly parts through Phase 5, then launching
  Project Assembly.
- Success, evaluation and failure: the final launch presents the ending;
  blocked factories, empty fuel, unavailable inputs and a tripped grid are
  recoverable local states before it.
- Claim IDs: `SAT-005`, `SAT-006`.

### Time Genes

- `TIM-003` keeps extraction, logistics, recipes, power and delivery progress
  active while the pioneer can continue constructing or changing the factory.
- Candidate genes: none.
- Claim IDs: `SAT-001`, `SAT-002`, `SAT-004`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A valid node is visible but production has no ore | Place a compatible Miner on that node and connect its output | The miner continuously emits its resource at the node's purity-dependent rate without exhausting the node | spatial extractor compatibility and non-depletion | `SAT-003` |
| A Constructor has its selected recipe but lacks its input | Connect a belt carrying the accepted input to its port | The belt transfers items; the powered Constructor repeatedly consumes them and emits its declared output | logistics and recipe execution are coupled but distinct | `SAT-002` |
| A required liquid recipe is above its source and receives too little fluid | Connect compatible Pipelines and place a powered Pump within the disclosed head-lift limit | The pipe network carries the accepted fluid within its throughput and head-lift boundary, allowing the supplied Refinery or Blender recipe to run | fluid logistics are mandatory factory flow, not optional breadth | `SAT-002`, `SAT-006` |
| Machines are attached to a power grid whose demand exceeds its available production and storage | Allow the deficit to persist | The grid trips and its consumers stop operating until reset and sufficient supply exist | all-grid deficit response differs from proportional throttling | `SAT-004` |
| A HUB Milestone is selected and its disclosed cost is incomplete | Submit the remaining listed materials at the HUB Terminal | The milestone completes and its listed buildings, recipes or equipment persistently become available | material requirement becomes a capability unlock | `SAT-005` |
| The Space Elevator has received every Project Assembly part for the current phase | Send the completed delivery | The phase completes and later HUB tiers become available; its next disclosed delivery becomes the new long-term requirement | phase delivery orders factory progression | `SAT-005`, `SAT-006` |
| Phase 5 is complete | Perform the final Space Elevator launch sequence | Project Assembly launches and the ending/credits are presented | bounded terminal objective | `SAT-006` |

## Strategic and experiential structure

- Local decision: identify whether a stopped output is caused by recipe,
  compatible input/output, belt capacity, power, node location or construction
  geometry.
- Medium-term planning: balance infinite source rates, processing ratios, belt
  and pipeline throughput, liquid head lift, by-product removal and power so
  each material delivery is met without destabilising the factory.
- Long-term structure: replace manual bootstrap labour with a scalable network
  that produces successively complex Project Assembly parts and launches them.
- Common heuristics: automate repeatable recipes, preserve expansion space,
  segment and diagnose power, read dependencies backward from the next delivery,
  then relieve the first bottleneck.
- Failure attribution: visible belts, machine states, milestone costs and the
  power graph make most stalls locally diagnosable.
- Claim IDs: `SAT-001`–`SAT-007`.

## Replay and variation

- What changes between sessions: spawn region, chosen resource nodes, topology,
  factory geometry, throughput ratios, delivery route and degree of automation.
- Randomness or procedural generation: the fixed world presents different
  accessible choices by landing area and exploration route; the scoped factory
  transitions are deterministic once entities, recipes and resources are set.
- Multiple viable strategies: yes; manual bootstrap duration, belt layout,
  verticality, machine ratio, power source and delivery routing may all differ.
- Typical replay motive: make the same dependency network more compact,
  legible, resilient, scalable or aesthetically organised.
- Claim IDs: `SAT-001`–`SAT-007`.

## Adjacent systems and history

- Direct predecessors: open-world factory construction and logistics
  simulation, rather than a discrete authored-puzzle sequence.
- Similar games: Factorio, Dyson Sphere Program, shapez 2 and Infinifactory.
- Important differences: Satisfactory keeps a first-person build/exploration
  setting, infinite resource nodes and a hard all-grid power-trip rule; its
  deliveries gate a finite Project Assembly ending rather than a rocket silo or
  exact geometric-shape qualification.
- Claim IDs: `SAT-002`–`SAT-008`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-119`, `ACT-120`, `ACT-122`, `ACT-123` | entity, recipe, node and delivery parameters |
| System Behaviour | `SYS-156`, `SYS-157`, `SYS-210`, `SYS-211` | rate, power graph, reward and phase parameters |
| Constraint | `CON-062`, `CON-172`, `CON-173` | footprint, flow and resource-locus compatibility |
| Information | `INF-001`, `INF-059`, `INF-060` | production, milestone and diagnostic detail |
| Objective | `OBJ-054` | phase deliveries and final launch |
| Time | `TIM-003` | real-time live factory tick |

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`: `ACT-119,ACT-120,ACT-122,ACT-123; SYS-156,SYS-157,SYS-210,SYS-211; CON-062,CON-172,CON-173; INF-001,INF-059,INF-060; OBJ-054; TIM-003`.
- Indexed games scanned: 128, including this record.
- Indexed combinations scanned: 126.
- Exact genome matches: none.
- Near matches and similarity scores: GAME-0119 at 13 / 26 = 0.500000; GAME-0122 at 7 / 24 = 0.291667; GAME-0125 at 8 / 50 = 0.160000.
- Supported combination subsets: `COMB-0126`.
- Scan date: 2026-08-20.

### Full prior-game Jaccard scan

- GAME-0001: 1 / 29 = 0.034483; GAME-0002: 1 / 22 = 0.045455; GAME-0003: 0 / 25 = 0.000000; GAME-0004: 2 / 29 = 0.068966.
- GAME-0005: 1 / 22 = 0.045455; GAME-0006: 1 / 24 = 0.041667; GAME-0007: 1 / 23 = 0.043478; GAME-0008: 1 / 22 = 0.045455.
- GAME-0009: 1 / 31 = 0.032258; GAME-0010: 1 / 24 = 0.041667; GAME-0011: 1 / 28 = 0.035714; GAME-0012: 1 / 24 = 0.041667.
- GAME-0013: 1 / 28 = 0.035714; GAME-0014: 1 / 30 = 0.033333; GAME-0015: 1 / 29 = 0.034483; GAME-0016: 2 / 29 = 0.068966.
- GAME-0017: 0 / 29 = 0.000000; GAME-0018: 2 / 33 = 0.060606; GAME-0019: 1 / 25 = 0.040000; GAME-0020: 1 / 29 = 0.034483.
- GAME-0021: 2 / 23 = 0.086957; GAME-0022: 2 / 26 = 0.076923; GAME-0023: 0 / 26 = 0.000000; GAME-0024: 1 / 27 = 0.037037.
- GAME-0025: 2 / 25 = 0.080000; GAME-0026: 2 / 26 = 0.076923; GAME-0027: 2 / 26 = 0.076923; GAME-0028: 2 / 31 = 0.064516.
- GAME-0029: 2 / 26 = 0.076923; GAME-0030: 2 / 28 = 0.071429; GAME-0031: 1 / 26 = 0.038462; GAME-0032: 1 / 26 = 0.038462.
- GAME-0033: 2 / 27 = 0.074074; GAME-0034: 2 / 28 = 0.071429; GAME-0035: 2 / 32 = 0.062500; GAME-0036: 1 / 27 = 0.037037.
- GAME-0037: 1 / 24 = 0.041667; GAME-0038: 2 / 30 = 0.066667; GAME-0039: 1 / 24 = 0.041667; GAME-0040: 1 / 23 = 0.043478.
- GAME-0041: 2 / 25 = 0.080000; GAME-0042: 2 / 23 = 0.086957; GAME-0043: 1 / 29 = 0.034483; GAME-0044: 1 / 25 = 0.040000.
- GAME-0045: 1 / 29 = 0.034483; GAME-0046: 1 / 25 = 0.040000; GAME-0047: 1 / 29 = 0.034483; GAME-0048: 1 / 29 = 0.034483.
- GAME-0049: 0 / 25 = 0.000000; GAME-0050: 1 / 30 = 0.033333; GAME-0051: 2 / 30 = 0.066667; GAME-0052: 1 / 25 = 0.040000.
- GAME-0053: 1 / 24 = 0.041667; GAME-0054: 1 / 26 = 0.038462; GAME-0055: 1 / 25 = 0.040000; GAME-0056: 1 / 23 = 0.043478.
- GAME-0057: 1 / 23 = 0.043478; GAME-0058: 1 / 24 = 0.041667; GAME-0059: 1 / 22 = 0.045455; GAME-0060: 1 / 22 = 0.045455.
- GAME-0061: 1 / 25 = 0.040000; GAME-0062: 1 / 23 = 0.043478; GAME-0063: 1 / 22 = 0.045455; GAME-0064: 1 / 20 = 0.050000.
- GAME-0065: 0 / 23 = 0.000000; GAME-0066: 0 / 26 = 0.000000; GAME-0067: 0 / 24 = 0.000000; GAME-0068: 0 / 24 = 0.000000.
- GAME-0069: 1 / 23 = 0.043478; GAME-0070: 1 / 23 = 0.043478; GAME-0071: 1 / 22 = 0.045455; GAME-0072: 1 / 23 = 0.043478.
- GAME-0073: 1 / 22 = 0.045455; GAME-0074: 1 / 24 = 0.041667; GAME-0075: 1 / 24 = 0.041667; GAME-0076: 1 / 22 = 0.045455.
- GAME-0077: 1 / 22 = 0.045455; GAME-0078: 1 / 22 = 0.045455; GAME-0079: 1 / 22 = 0.045455; GAME-0080: 1 / 22 = 0.045455.
- GAME-0081: 1 / 23 = 0.043478; GAME-0082: 1 / 23 = 0.043478; GAME-0083: 1 / 23 = 0.043478; GAME-0084: 1 / 25 = 0.040000.
- GAME-0085: 0 / 27 = 0.000000; GAME-0086: 1 / 28 = 0.035714; GAME-0087: 2 / 24 = 0.083333; GAME-0088: 1 / 24 = 0.041667.
- GAME-0089: 1 / 24 = 0.041667; GAME-0090: 1 / 30 = 0.033333; GAME-0091: 2 / 23 = 0.086957; GAME-0092: 2 / 24 = 0.083333.
- GAME-0093: 1 / 24 = 0.041667; GAME-0094: 2 / 24 = 0.083333; GAME-0095: 2 / 26 = 0.076923; GAME-0096: 2 / 24 = 0.083333.
- GAME-0097: 2 / 22 = 0.090909; GAME-0098: 2 / 21 = 0.095238; GAME-0099: 1 / 23 = 0.043478; GAME-0100: 1 / 26 = 0.038462.
- GAME-0101: 0 / 26 = 0.000000; GAME-0102: 0 / 23 = 0.000000; GAME-0103: 1 / 24 = 0.041667; GAME-0104: 1 / 24 = 0.041667.
- GAME-0105: 1 / 25 = 0.040000; GAME-0106: 0 / 23 = 0.000000; GAME-0107: 1 / 23 = 0.043478; GAME-0108: 1 / 25 = 0.040000.
- GAME-0109: 1 / 31 = 0.032258; GAME-0110: 2 / 22 = 0.090909; GAME-0111: 1 / 22 = 0.045455; GAME-0112: 2 / 22 = 0.090909.
- GAME-0113: 2 / 28 = 0.071429; GAME-0114: 2 / 21 = 0.095238; GAME-0115: 1 / 21 = 0.047619; GAME-0116: 2 / 20 = 0.100000.
- GAME-0117: 1 / 23 = 0.043478; GAME-0118: 1 / 31 = 0.032258; GAME-0119: 13 / 26 = 0.500000; GAME-0120: 0 / 45 = 0.000000.
- GAME-0121: 1 / 38 = 0.026316; GAME-0122: 7 / 24 = 0.291667; GAME-0123: 0 / 54 = 0.000000; GAME-0124: 8 / 55 = 0.145455.
- GAME-0125: 8 / 50 = 0.160000; GAME-0126: 6 / 53 = 0.113208; GAME-0127: 7 / 57 = 0.122807.

### Registry normalisation 006 score corrections

These recomputed values supersede the pre-normalisation fractions above:

- `GAME-0119`: `14 / 25 = 0.560000`
- Current prior-corpus near match after normalisation 006: `GAME-0119`.

## Evidence and unknowns

- The official product page establishes release and overall form. The official
  Wiki provides the operational node, machine, belt, pipeline, fluid recipe,
  power, milestone and Space Elevator rules used by the scope.
- Direct play would improve confidence in rare delivery/UI ordering details;
  those details are parameters and do not alter the admitted boundaries.

## Verification status

- Structure: reviewed.
- Evidence coverage: corroborated for all active claims.
- Novelty: new boundaries remain unassessed outside this corpus comparison.
- Web presentation and localisation: reviewed and complete for this game unit.

## Next useful test

Compare Dyson Sphere Program's interplanetary factory logistics against this
infinite-node, hard-power-trip production core without treating world scale as
an independent causal rule.

## Taxonomy impact

- New genes: `SYS-210`, `SYS-211`.
- Reused genes: `ACT-119`, `ACT-120`, `ACT-122`, `ACT-123`, `SYS-156`,
  `SYS-157`, `CON-062`, `CON-172`, `CON-173`, `INF-001`, `INF-059`,
  `INF-060`, `OBJ-054`, `TIM-003`.
- New family: none; Satisfactory belongs to the existing
  `FAM-008 automation-and-spatial-programming` boundary.
- `COMB-0118` does not recur exactly because Satisfactory has infinite nodes,
  no science-pack laboratory queue, no construction robots and a Project
  Assembly launch rather than Factorio's first rocket.

## Negative results

- `SYS-158` rejected: its proportional consumer-throttling boundary conflicts
  with Satisfactory's complete power-grid trip.
- `SYS-161` rejected: resource nodes are explicitly infinite.
- `SYS-159` rejected: the selected HUB requirement directly consumes declared
  materials rather than laboratory science packs over time.
- `SYS-171` rejected: Project Assembly parts are typed material products, not
  an exact geometric-shape schema accepted by the Vortex.

## Delta summary

## Нові факти

- Satisfactory зводить безперервну фабрику навколо нескінченних вузлів,
  конвеєрів, рецептів і залежної від мережі електрики.
- Відсутня генерація не сповільнює всю фабрику пропорційно: незабезпечена
  мережа аварійно вимикається.
- HUB та Space Elevator перетворюють повні поставки конкретних матеріалів на
  сталі можливості й, зрештою, запуск Project Assembly.

## Нові гени

- `SYS-210`, `SYS-211`; `OBJ-054` is reused for the terminal factory project.

## Нові комбінації

- `COMB-0126` — live factory із нескінченними вузлами, аварійним power-trip і
  поставками Project Assembly.

## Зміни таксономії

- Нових родин не створено. Гра включена до `FAM-008`.

## Нові питання

- Чи повторить Dyson Sphere Program живу виробничу логіку, але відокремить її
  міжпланетною доставкою та іншою енергетичною межею?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] Minecraft.
- Optimisation criterion: test broad global-search adjacency through a compact,
  reproducible survival-crafting scope without conflating crafting with factory
  automation.
- Expected information gain: distinguish player-operated crafting and world
  transformation from autonomous recipe logistics.

## Чому саме вона

- [Hypothesis | Limited | High] Minecraft is a globally searched adjacent game
  whose construction and resource loop should contrast with Satisfactory's
  persistent machine-led production network.
