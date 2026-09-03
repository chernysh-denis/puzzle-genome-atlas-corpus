---
game_id: GAME-0125
slug: oxygen-not-included
game_title: Oxygen Not Included
analysis_status: reviewed
reviewed: 2026-08-18
combination_ids:
  - COMB-0123
gene_ids:
  action:
    - ACT-006
    - ACT-120
    - ACT-140
    - ACT-144
    - ACT-145
    - ACT-146
    - ACT-147
    - ACT-148
    - ACT-149
  system:
    - SYS-004
    - SYS-045
    - SYS-156
    - SYS-157
    - SYS-158
    - SYS-161
    - SYS-185
    - SYS-186
    - SYS-187
    - SYS-188
    - SYS-189
    - SYS-190
    - SYS-191
    - SYS-192
    - SYS-193
    - SYS-194
  constraint:
    - CON-062
    - CON-172
    - CON-192
    - CON-193
    - CON-194
    - CON-195
    - CON-196
    - CON-197
  information:
    - INF-001
    - INF-002
    - INF-003
    - INF-059
    - INF-069
    - INF-070
    - INF-071
  objective:
    - OBJ-060
  time:
    - TIM-003
---

# Game: Oxygen Not Included

## Analysis scope

- Version / ruleset: current PC base game observed on 2026-08-18; ordinary
  Survival colony on one base-game asteroid from the initial three Duplicants
  through the base-game Temporal Tear ending.
- Included: excavation and construction errands; Duplicant priorities, skills,
  schedules, needs, morale and stress; material-cell gases, liquids, heat,
  phase changes and germs; recipes, storage, pipes, power and automation;
  Printing Pod offers, research, rockets and the Temporal Tear.
- Excluded: Spaced Out! and all paid content packs; multi-asteroid DLC
  progression; Sandbox and Debug; mods, achievements, special challenge
  settings and the separate Monument imperative.
- Direct-play status: not conducted. The official product description and
  maintained current mechanics reference jointly specify the scoped transitions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `ONI-001` | A seed creates a concealed asteroid made of typed material cells | Confirmed | Corroborated | High | P1, P3 |
| `ONI-002` | Marked errands are claimed autonomously through priorities, skills and reachability | Confirmed | Corroborated | High | P4, P5 |
| `ONI-003` | Duplicants consume oxygen and food, produce waste and interrupt work for personal needs | Confirmed | Corroborated | High | P1, P6 |
| `ONI-004` | Gas, liquid, heat and phase state continue changing during construction | Confirmed | Corroborated | High | P1, P7, P8 |
| `ONI-005` | Skills unlock work but increase the trained Duplicant's morale expectation | Confirmed | Corroborated | High | P9, P10 |
| `ONI-006` | Production, conduits, electricity and automation form coupled live infrastructure | Confirmed | Corroborated | High | P11, P12, P13 |
| `ONI-007` | Staffed stations consume typed inputs to complete selected research | Confirmed | Corroborated | High | P14, P15 |
| `ONI-008` | Printing Pod alternatives are bounded, mutually exclusive and refresh after cooldown | Confirmed | Corroborated | High | P5 |
| `ONI-009` | Germ carriers and exposure can produce disease | Confirmed | Corroborated | High | P16 |
| `ONI-010` | Sending a Duplicant through the Temporal Tear provides the base-game ending milestone | Confirmed | Corroborated | High | P17 |

## Basic data

- Release / origin: Klei Entertainment; base game released in 2019 and actively maintained.
- Platform or physical form: real-time desktop space-colony simulation.
- Puzzle family: automation and spatial programming; real-time system pressure;
  agent routing and coordination; ordered dependency sequencing.
- Primary sources: **[P1]** [official Steam page](https://store.steampowered.com/app/457140/Oxygen_Not_Included/);
  **[P2]** [official Klei Spaced Out! boundary](https://support.klei.com/hc/en-us/articles/360057640052-Oxygen-Not-Included-Spaced-Out);
  **[P3]** [Getting Started](https://oxygennotincluded.wiki.gg/wiki/Guide/Getting_Started);
  **[P4]** [Errand](https://oxygennotincluded.wiki.gg/wiki/Errand);
  **[P5]** [Duplicant](https://oxygennotincluded.wiki.gg/wiki/Duplicant);
  **[P6]** [Oxygen](https://oxygennotincluded.wiki.gg/wiki/Oxygen);
  **[P7]** [Elements](https://oxygennotincluded.wiki.gg/wiki/Elements);
  **[P8]** [Units and heat](https://oxygennotincluded.wiki.gg/wiki/Units);
  **[P9]** [Priority](https://oxygennotincluded.wiki.gg/wiki/Priority);
  **[P10]** [Morale](https://oxygennotincluded.wiki.gg/wiki/Morale);
  **[P11]** [Power buildings](https://oxygennotincluded.wiki.gg/wiki/Power_(Building));
  **[P12]** [Automation buildings](https://oxygennotincluded.wiki.gg/wiki/Automation_(Building));
  **[P13]** [Power Transformer](https://oxygennotincluded.wiki.gg/wiki/Power_Transformer);
  **[P14]** [Research](https://oxygennotincluded.wiki.gg/wiki/Research);
  **[P15]** [Research Station](https://oxygennotincluded.wiki.gg/wiki/Research_Station);
  **[P16]** [Germ](https://oxygennotincluded.wiki.gg/wiki/Germ);
  **[P17]** [Temporal Tear](https://oxygennotincluded.wiki.gg/wiki/Temporal_Tear).
- Claim IDs: `ONI-001`–`ONI-010`.

## Mechanical decomposition

### Action Genes

- Reused: `ACT-006` changes simulation speed; `ACT-120` configures recipes,
  filters and automation rules; `ACT-140` commits one Printing Pod choice.
- New: `ACT-144` marks spatial work; `ACT-145` sets priorities; `ACT-146`
  trains one Duplicant; `ACT-147` edits schedules; `ACT-148` places a
  material-backed plan; `ACT-149` selects research.
- Parameters: target cells, errand type, agent, priority, skill, schedule,
  structure, material, recipe, threshold and research node.
- Claim IDs: `ONI-002`, `ONI-005`–`ONI-008`.

### System Behaviour Genes

- Reused: `SYS-004`, `SYS-045`, `SYS-156`–`SYS-158` and `SYS-161` cover seeded
  variation, autonomous movement, recipes, logistics, power and depletion.
- New: `SYS-185`–`SYS-194` cover material-cell generation, errand routing,
  open fluids, thermal state, metabolism, stress, germs, automation, Printing
  Pod refresh and staffed research.
- Resolution order: accept orders and settings; assign eligible errands; move
  Duplicants and materials; execute work and recipes; settle open and conduit
  flows, power, heat, phase and germs; update needs, morale and stress; test
  survival and research or space milestones.
- Claim IDs: `ONI-001`–`ONI-010`.

### Constraint Genes

- Reused: `CON-062` footprint compatibility and `CON-172` recipe-flow compatibility.
- New: `CON-192`–`CON-197` bind errands, construction, networks, survival,
  skill expectations and operating environments.
- Scarce strategic resources: Duplicant time, breathable oxygen, calories,
  water, power, heat capacity, accessible material, storage and buildable space.
- Claim IDs: `ONI-002`–`ONI-007`, `ONI-009`.

### Information Genes

- `INF-001`–`INF-003` distinguish explored current state, unknown later offers
  and unexplored asteroid cells; `INF-059` shows dependency references;
  `INF-069`–`INF-071` expose overlays, agent causes and colony reports.
- Claim IDs: `ONI-001`–`ONI-009`.

### Objective Genes

- `OBJ-060` sustains the colony through research and rocket construction until
  one Duplicant breaches the base-game Temporal Tear; the save can continue.
- Claim IDs: `ONI-010`.

### Time Genes

- `TIM-003`: the asteroid, errands, metabolism, production, heat and networks
  advance in real time, with pause and speed controls.
- Claim IDs: `ONI-002`–`ONI-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A reachable sandstone cell is intact and one Duplicant may dig | Mark the cell for digging | the errand enters the ranked pool; an eligible Duplicant paths to it, excavates it and creates debris | orders and priorities route autonomous labour | `ONI-002` |
| A construction plan has valid cells but no material at its site | Leave the order active | a supplier delivers the selected material, then a builder completes the structure | construction couples logistics, reach and labour | `ONI-002`, `ONI-006` |
| A low pocket contains carbon dioxide below breathable oxygen | Open a passage between them | gases redistribute by cell mass and density while Duplicants consume oxygen and add carbon dioxide | atmosphere is live infrastructure | `ONI-003`, `ONI-004` |
| Water in a pipe crosses its freezing threshold | Continue cooling the segment | the packet changes phase and can damage the liquid pipe | heat, phase and conduit constraints interact | `ONI-004`, `ONI-006` |
| A Duplicant learns an advanced skill without added morale | Spend the skill point and advance cycles | its expectation rises; insufficient morale increases stress toward its response | an upgrade creates a welfare obligation | `ONI-005` |
| A powered research station has dirt and an eligible researcher | Select a reachable technology | the worker produces the required points until the node unlocks | research is staffed material production | `ONI-007` |
| The Printing Pod presents Duplicants and a care package | Accept one option | the chosen agent or goods enter the colony, alternatives disappear and cooldown begins | population growth is a bounded commitment | `ONI-008` |
| A prepared base-game rocket can reach the farthest destination | Launch it with a Duplicant | arrival at the Temporal Tear triggers the ending milestone and removes the one-way crew | the colony's dependency graph has an explicit horizon | `ONI-010` |

## Strategic and experiential structure

- Local decision: decide which cell, errand or failing machine deserves scarce
  Duplicant time before oxygen, food, heat or storage crosses a threshold.
- Medium-term planning: close material loops for oxygen, sanitation, food,
  cooling and power while keeping routes short and skill expectations supportable.
- Long-term structure: turn local life-support loops into research, industrial
  materials and a staffed rocket programme capable of reaching the Temporal Tear.
- Common heuristics: inspect overlays before expansion; avoid adding population
  without oxygen and food margin; separate heat producers; automate generators;
  treat every advanced skill as both permission and morale debt.
- Failure attribution: overlays, errand lists, need meters and cycle reports
  usually reveal causal shortages, although many delayed interactions can make
  the originating design decision several cycles old.
- Player-trust factors: material quantities and thresholds are inspectable;
  emergent chains remain complex rather than arbitrary.
- Claim IDs: `ONI-001`–`ONI-010`.

## Replay and variation

- What changes between sessions: asteroid seed, biome distribution, buried
  resources, geysers, ruins, starting Duplicants and later Printing Pod offers.
- Randomness or procedural generation: geography and offers vary while material,
  errand, survival and network rules remain stable and inspectable.
- Multiple viable strategies: yes; oxygen, food, cooling, power, transport and
  rocket chains admit materially different loops and degrees of automation.
- Typical replay motive: solve the same survival dependencies with a different
  asteroid inventory, colony roster and engineering architecture.
- Claim IDs: `ONI-001`, `ONI-008`.

## Adjacent systems and history

- Direct predecessors: colony simulations, cellular falling-material sandboxes,
  production-chain games and autonomous-worker management.
- Variants: Spaced Out! distributes the colony across smaller asteroids and
  changes rocketry and research; it is outside this record.
- Similar games: Factorio, RimWorld, Dwarf Fortress and Against the Storm.
- Important differences: Oxygen Not Included makes atmosphere, temperature and
  bodily survival part of the same engineered material graph as production.
- Claim IDs: `ONI-001`–`ONI-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-006`, `ACT-120`, `ACT-140`, `ACT-144`–`ACT-149` | order, priority, skill, schedule, plan and research parameters |
| System Behaviour | `SYS-004`, `SYS-045`, `SYS-156`–`SYS-158`, `SYS-161`, `SYS-185`–`SYS-194` | material, route, need, stress and network rates |
| Constraint | `CON-062`, `CON-172`, `CON-192`–`CON-197` | eligibility, capacity and survival thresholds |
| Information | `INF-001`–`INF-003`, `INF-059`, `INF-069`–`INF-071` | overlay and diagnostic granularity |
| Objective | `OBJ-060` | one-way ending destination |
| Time | `TIM-003` | live simulation with pause and speed |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `124` (`GAME-0001`–`GAME-0124`).
- Exact genome matches: none.
- Tied near matches: `GAME-0119` — Factorio (`11 / 54 = 0.203704`).
- Supported combination subsets: `COMB-0123`.
- Scan date: 2026-08-18.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0119` Factorio | `ACT-006`, `ACT-120`, `SYS-045`, `SYS-156`, `SYS-157`, `SYS-158`, `SYS-161`, `CON-062`, `CON-172`, `INF-001`, `INF-059`, `TIM-003` | Factorio's machines and logistics primarily optimise item throughput against pollution and enemies; Oxygen Not Included routes need-bearing workers through an open material-cell atmosphere whose heat, pressure and life support can kill them | Near, `0.203704` |

## Evidence and unknowns

- The official product description is authoritative for the colony-simulation
  premise; current wiki.gg references are maintained community evidence for
  exact mechanics and are cited only where corroborated across related pages.
- Exact numeric rates are parameters, not gene boundaries, because current
  updates and traits can alter them.
- The Temporal Tear is treated as the scoped base-game completion horizon, not
  as a hard save termination and not as the DLC opener sequence.
- Direct play would still improve UI timing observations and edge-case ordering.

## Verification status

- Structure: reviewed.
- Evidence coverage: corroborated for all active claims.
- Novelty: candidate only until recurrence appears in another analysed game.
- Web presentation and localisation: reviewed in the same game unit.

## Next useful test

Compare Oxygen Not Included with Dwarf Fortress to determine whether autonomous
labour under bodily and environmental simulation recurs as one family pattern,
or whether ONI's conserved cell mass and engineered life support remain the
decisive boundary.

## Taxonomy impact

- Added six Action, ten System Behaviour, six Constraint, three Information
  and one Objective gene because no active definition covered autonomous
  errand brokerage, cellular life support or the skill–morale tradeoff.
- Reused factory genes only where their boundaries genuinely recur: repeated
  recipes, live transport, network power, finite extraction and configuration.
- `COMB-0123` is retained as a candidate interaction pattern pending the
  immediately scheduled Dwarf Fortress recurrence test.

## Negative results

- `ACT-036` and `SYS-046` were rejected: ONI workers do not receive one fixed
  Lemmings-like behavioural role; they repeatedly choose from a shared errand pool.
- `ACT-119` was rejected: ONI construction is not immediate inventory
  placement but a supplied and staffed plan.
- `CON-185` was rejected: Duplicants are not locked into bounded permanent job
  slots; their labour is dynamically rebrokered among errands.
- `OBJ-053` was rejected: a survivable colony is not a municipal city-growth
  objective, and the scoped explicit horizon is the Temporal Tear.
