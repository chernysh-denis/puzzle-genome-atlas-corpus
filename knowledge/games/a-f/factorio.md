---
game_id: GAME-0119
slug: factorio
game_title: Factorio
analysis_status: reviewed
reviewed: 2026-08-18
combination_ids:
  - COMB-0118
gene_ids:
  action:
    - ACT-119
    - ACT-120
    - ACT-121
    - ACT-122
    - ACT-123
    - ACT-124
  system:
    - SYS-045
    - SYS-051
    - SYS-156
    - SYS-157
    - SYS-158
    - SYS-159
    - SYS-160
    - SYS-161
    - SYS-162
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

# Game: Factorio

## Analysis scope

- Version / ruleset: stable Factorio 2.0 base game, ordinary single-player
  freeplay on Nauvis through the first rocket launch.
- Included: manual mining and crafting; entity construction and configuration;
  recipes, belts, inserters, pipes, trains and logistic robots; electricity;
  science and research; finite resources; blueprints and construction robots;
  pollution, enemies and defence; first-rocket victory.
- Excluded: Space Age, quality, elevated rails, other planets and space
  platforms; mods; multiplayer; campaigns, tutorials and scenarios; map editor;
  console commands, achievement rules, speedrunning and post-victory megabase
  optimisation.
- Direct-play status: not conducted. The official product documentation and
  first-party wiki jointly specify the scoped production, logistics, research,
  power, pollution, combat and launch transitions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FAC-001` | The player places, rotates, removes and locally configures live factory entities | Confirmed | Corroborated | High | P1, P7 |
| `FAC-002` | Machines repeatedly execute supplied recipes while logistics move their inputs and outputs | Confirmed | Corroborated | High | P1, P7 |
| `FAC-003` | Connected electrical supply is distributed across consumers and shortage throttles operation | Confirmed | Direct | High | P6 |
| `FAC-004` | Science packs are consumed over time to complete queued technologies | Confirmed | Direct | High | P4 |
| `FAC-005` | Extraction depletes finite spatial resource deposits | Confirmed | Direct | High | P5 |
| `FAC-006` | Blueprints preserve layouts and construction robots fulfil compatible ghost requests | Confirmed | Corroborated | High | P1, P2 |
| `FAC-007` | Production pollution diffuses through chunks and can trigger hostile attack groups | Confirmed | Direct | High | P8, P10 |
| `FAC-008` | Turrets automatically engage enemies within their operating conditions | Confirmed | Corroborated | High | P1, P10 |
| `FAC-009` | Base freeplay victory requires constructing a silo and launching the first rocket | Confirmed | Direct | High | P9 |
| `FAC-010` | Stable 2.0 base-game scope is distinct from the optional Space Age expansion | Confirmed | Corroborated | High | P2, P3 |

## Basic data

- Release / origin: Wube Software, first public release 2016 and 1.0 release
  2020; scoped here to the stable 2.0 base game.
- Platform or physical form: real-time desktop automation and construction game.
- Puzzle family: automation and spatial programming; route and network
  construction; real-time system pressure; ordered dependency sequencing.
- Primary sources: **[P1]** [official game-content overview](https://www.factorio.com/game/content);
  **[P2]** [official Factorio 2.0 release post](https://www.factorio.com/blog/post/factorio-space-age-release);
  **[P3]** [official stable download channel](https://www.factorio.com/download);
  **[P4]** [official wiki: Research](https://wiki.factorio.com/Research);
  **[P5]** [official wiki: Mining](https://wiki.factorio.com/Mining);
  **[P6]** [official wiki: Electric system](https://wiki.factorio.com/Electric_system);
  **[P7]** [official wiki: Inserters](https://wiki.factorio.com/Inserters);
  **[P8]** [official wiki: Pollution](https://wiki.factorio.com/Pollution);
  **[P9]** [official wiki: Rocket silo](https://wiki.factorio.com/Rocket_silo);
  **[P10]** [official wiki: Enemies](https://wiki.factorio.com/Enemies).
- Claim IDs: `FAC-001`–`FAC-010`.

## Mechanical decomposition

### Action Genes

- `ACT-119` places, rotates or deconstructs live entities; `ACT-120` configures
  an entity's local rule; `ACT-121` queues research; `ACT-122` manually extracts
  or dismantles world entities; `ACT-123` hand-crafts recipes; `ACT-124` stamps
  reusable construction or deconstruction plans.
- Candidate genes: none.
- Parameters: entity type, orientation, recipe, filter, circuit condition,
  technology order, crafting queue and blueprint transform.
- Claim IDs: `FAC-001`, `FAC-004`, `FAC-005`, `FAC-006`.

### System Behaviour Genes

- `SYS-156` repeatedly executes supplied production recipes; `SYS-157`
  transports items through live logistics; `SYS-158` distributes and throttles
  electrical power; `SYS-159` converts science into research progress;
  `SYS-160` converts pollution diffusion into hostile pressure; `SYS-161`
  depletes resource reserves; `SYS-162` lets construction robots satisfy ghost
  requests; `SYS-045` moves attack groups; `SYS-051` runs turret engagement.
- Resolution order: accept construction or configuration; advance the live
  tick; extract resources; transport available items and fluids; execute
  powered recipes; consume science; update pollution and hostile agents; apply
  robot and defence work.
- Claim IDs: `FAC-002`–`FAC-008`.

### Constraint Genes

- `CON-062` rejects incompatible machine footprints; `CON-172` requires recipe,
  input, output and operating compatibility; `CON-173` binds extraction to a
  compatible resource locus.
- Scarce strategic resources: ore, oil, space, power, machine time, transport
  capacity, science throughput and defensive attention.
- Claim IDs: `FAC-001`–`FAC-005`.

### Information Genes

- `INF-001` exposes the explored live factory state; `INF-059` exposes recipe
  and technology dependencies; `INF-060` exposes production, power and logistics
  diagnostics.
- Candidate genes: none.
- Claim IDs: `FAC-001`–`FAC-006`.

### Objective Genes

- `OBJ-054` requires researching, constructing and launching the first rocket.
- Success, evaluation and failure: the first valid launch presents victory and
  permits continued play; local shortages, destruction and death usually remain
  recoverable before that terminal milestone.
- Claim IDs: `FAC-009`, `FAC-010`.

### Time Genes

- `TIM-003` keeps production, transport, power, research, pollution and enemies
  active while the player edits the factory.
- Candidate genes: none.
- Claim IDs: `FAC-002`–`FAC-008`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A powered assembler has a recipe but lacks one ingredient | Connect a belt and inserter carrying that ingredient | Items enter until the recipe is supplied; the assembler produces and repeats | configuration, logistics and production are separate coupled rules | `FAC-001`, `FAC-002` |
| A connected factory demands more electricity than generation supplies | Add consumers without adding generation | the electric network divides insufficient supply and machine speed falls | power shortage throttles live production rather than merely blocking placement | `FAC-003` |
| Labs are powered and supplied with the selected technology's science packs | Queue that technology | packs are consumed over time until the technology unlocks | research is a supplied production-like dependency | `FAC-004` |
| A drill covers a finite ore tile and has an output path | Power the drill and advance time | ore is emitted while the tile amount decreases | extraction consumes a spatial reserve | `FAC-005` |
| A blueprint ghost lies inside a supplied construction network | Make the required item available | a construction robot travels to the ghost and places the entity | reusable plans become asynchronously fulfilled requests | `FAC-006` |
| Pollution reaches an enemy expansion and is absorbed | Continue polluting without eliminating the base | an attack group forms, paths toward the pollution source and can meet turret fire | production externality becomes autonomous hostile pressure | `FAC-007`, `FAC-008` |

## Strategic and experiential structure

- Local decision: diagnose whether a machine is blocked by material, output,
  power, recipe or placement state.
- Medium-term planning: balance extraction, transport, intermediate recipes,
  science, power and defence so one bottleneck does not idle downstream systems.
- Long-term structure: turn manual bootstrapping into a scalable self-running
  dependency network capable of producing and launching a rocket.
- Common heuristics: automate repeated work, preserve expandable lanes, use
  ratios and diagnostics, buffer selectively and blueprint stable modules.
- Failure attribution: detailed entity and network diagnostics make most stalls
  traceable, although congestion and circuit interactions can be distributed.
- Player-trust factors: visible item motion and explicit recipe dependencies let
  the player connect local causes to global throughput.
- Claim IDs: `FAC-001`–`FAC-009`.

## Replay and variation

- What changes between sessions: map seed, resource layout, enemy pressure,
  factory topology, technology route and chosen automation scale.
- Randomness or procedural generation: the world and resource distribution are
  generated; the scoped factory rules remain stable.
- Multiple viable strategies: yes; belt, train, robot, module, defence and
  production layouts can satisfy the same launch goal.
- Typical replay motive: improve throughput, compactness, robustness,
  scalability or self-imposed constraints.
- Claim IDs: `FAC-001`–`FAC-010`.

## Adjacent systems and history

- Direct predecessors: factory and logistics simulation traditions rather than
  one discrete puzzle lineage.
- Variants: Space Age extends progression beyond Nauvis; it is excluded here.
- Similar games: shapez 2, Dyson Sphere Program, Satisfactory and Mindustry.
- Important differences: Factorio combines freely constructed production
  logistics with finite extraction, research, pollution and active hostile
  pressure in one persistent real-time world.
- Claim IDs: `FAC-002`–`FAC-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-119`–`ACT-124` | entity, recipe, technology and plan parameters |
| System Behaviour | `SYS-045`, `SYS-051`, `SYS-156`–`SYS-162` | rates, routes, priorities and attack thresholds |
| Constraint | `CON-062`, `CON-172`, `CON-173` | footprint, flow and resource compatibility |
| Information | `INF-001`, `INF-059`, `INF-060` | diagnostic granularity |
| Objective | `OBJ-054` | rocket payload and continuation |
| Time | `TIM-003` | live simulation tick |

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`: `ACT-119,ACT-120,ACT-121,ACT-122,ACT-123,ACT-124; SYS-045,SYS-051,SYS-156,SYS-157,SYS-158,SYS-159,SYS-160,SYS-161,SYS-162; CON-062,CON-172,CON-173; INF-001,INF-059,INF-060; OBJ-054; TIM-003`.
- Indexed games scanned: 119, including this record.
- Indexed combinations scanned: 118.
- Exact genome matches: none.
- Near matches and similarity scores: `GAME-0027` at `4 / 31 = 0.129032`.
- Supported combination subsets: `COMB-0118`.
- Scan date: 2026-08-18.

### Full prior-game Jaccard scan

- `GAME-0001`: `1 / 36 = 0.027778`; `GAME-0002`: `1 / 29 = 0.034483`; `GAME-0003`: `0 / 32 = 0.000000`; `GAME-0004`: `2 / 36 = 0.055556`.
- `GAME-0005`: `1 / 29 = 0.034483`; `GAME-0006`: `1 / 31 = 0.032258`; `GAME-0007`: `1 / 30 = 0.033333`; `GAME-0008`: `1 / 29 = 0.034483`.
- `GAME-0009`: `1 / 38 = 0.026316`; `GAME-0010`: `1 / 31 = 0.032258`; `GAME-0011`: `1 / 35 = 0.028571`; `GAME-0012`: `1 / 31 = 0.032258`.
- `GAME-0013`: `1 / 35 = 0.028571`; `GAME-0014`: `1 / 37 = 0.027027`; `GAME-0015`: `1 / 36 = 0.027778`; `GAME-0016`: `2 / 36 = 0.055556`.
- `GAME-0017`: `0 / 36 = 0.000000`; `GAME-0018`: `2 / 40 = 0.050000`; `GAME-0019`: `1 / 32 = 0.031250`; `GAME-0020`: `1 / 36 = 0.027778`.
- `GAME-0021`: `2 / 30 = 0.066667`; `GAME-0022`: `2 / 33 = 0.060606`; `GAME-0023`: `0 / 33 = 0.000000`; `GAME-0024`: `1 / 34 = 0.029412`.
- `GAME-0025`: `3 / 31 = 0.096774`; `GAME-0026`: `2 / 33 = 0.060606`; `GAME-0027`: `4 / 31 = 0.129032`; `GAME-0028`: `4 / 36 = 0.111111`.
- `GAME-0029`: `3 / 32 = 0.093750`; `GAME-0030`: `3 / 34 = 0.088235`; `GAME-0031`: `2 / 32 = 0.062500`; `GAME-0032`: `1 / 33 = 0.030303`.
- `GAME-0033`: `2 / 34 = 0.058824`; `GAME-0034`: `3 / 34 = 0.088235`; `GAME-0035`: `3 / 38 = 0.078947`; `GAME-0036`: `1 / 34 = 0.029412`.
- `GAME-0037`: `1 / 31 = 0.032258`; `GAME-0038`: `2 / 37 = 0.054054`; `GAME-0039`: `1 / 31 = 0.032258`; `GAME-0040`: `1 / 30 = 0.033333`.
- `GAME-0041`: `2 / 32 = 0.062500`; `GAME-0042`: `2 / 30 = 0.066667`; `GAME-0043`: `1 / 36 = 0.027778`; `GAME-0044`: `1 / 32 = 0.031250`.
- `GAME-0045`: `1 / 36 = 0.027778`; `GAME-0046`: `1 / 32 = 0.031250`; `GAME-0047`: `1 / 36 = 0.027778`; `GAME-0048`: `1 / 36 = 0.027778`.
- `GAME-0049`: `0 / 32 = 0.000000`; `GAME-0050`: `1 / 37 = 0.027027`; `GAME-0051`: `2 / 37 = 0.054054`; `GAME-0052`: `1 / 32 = 0.031250`.
- `GAME-0053`: `1 / 31 = 0.032258`; `GAME-0054`: `1 / 33 = 0.030303`; `GAME-0055`: `1 / 32 = 0.031250`; `GAME-0056`: `1 / 30 = 0.033333`.
- `GAME-0057`: `1 / 30 = 0.033333`; `GAME-0058`: `1 / 31 = 0.032258`; `GAME-0059`: `1 / 29 = 0.034483`; `GAME-0060`: `1 / 29 = 0.034483`.
- `GAME-0061`: `1 / 32 = 0.031250`; `GAME-0062`: `1 / 30 = 0.033333`; `GAME-0063`: `1 / 29 = 0.034483`; `GAME-0064`: `1 / 27 = 0.037037`.
- `GAME-0065`: `0 / 30 = 0.000000`; `GAME-0066`: `0 / 33 = 0.000000`; `GAME-0067`: `0 / 31 = 0.000000`; `GAME-0068`: `0 / 31 = 0.000000`.
- `GAME-0069`: `1 / 30 = 0.033333`; `GAME-0070`: `1 / 30 = 0.033333`; `GAME-0071`: `1 / 29 = 0.034483`; `GAME-0072`: `1 / 30 = 0.033333`.
- `GAME-0073`: `1 / 29 = 0.034483`; `GAME-0074`: `1 / 31 = 0.032258`; `GAME-0075`: `1 / 31 = 0.032258`; `GAME-0076`: `1 / 29 = 0.034483`.
- `GAME-0077`: `1 / 29 = 0.034483`; `GAME-0078`: `1 / 29 = 0.034483`; `GAME-0079`: `1 / 29 = 0.034483`; `GAME-0080`: `1 / 29 = 0.034483`.
- `GAME-0081`: `1 / 30 = 0.033333`; `GAME-0082`: `1 / 30 = 0.033333`; `GAME-0083`: `1 / 30 = 0.033333`; `GAME-0084`: `1 / 32 = 0.031250`.
- `GAME-0085`: `0 / 34 = 0.000000`; `GAME-0086`: `1 / 35 = 0.028571`; `GAME-0087`: `2 / 31 = 0.064516`; `GAME-0088`: `1 / 31 = 0.032258`.
- `GAME-0089`: `1 / 31 = 0.032258`; `GAME-0090`: `1 / 37 = 0.027027`; `GAME-0091`: `2 / 30 = 0.066667`; `GAME-0092`: `3 / 30 = 0.100000`.
- `GAME-0093`: `1 / 31 = 0.032258`; `GAME-0094`: `2 / 31 = 0.064516`; `GAME-0095`: `2 / 33 = 0.060606`; `GAME-0096`: `2 / 31 = 0.064516`.
- `GAME-0097`: `2 / 29 = 0.068966`; `GAME-0098`: `2 / 28 = 0.071429`; `GAME-0099`: `1 / 30 = 0.033333`; `GAME-0100`: `1 / 33 = 0.030303`.
- `GAME-0101`: `0 / 33 = 0.000000`; `GAME-0102`: `0 / 30 = 0.000000`; `GAME-0103`: `1 / 31 = 0.032258`; `GAME-0104`: `1 / 31 = 0.032258`.
- `GAME-0105`: `1 / 32 = 0.031250`; `GAME-0106`: `0 / 30 = 0.000000`; `GAME-0107`: `1 / 30 = 0.033333`; `GAME-0108`: `1 / 32 = 0.031250`.
- `GAME-0109`: `1 / 38 = 0.026316`; `GAME-0110`: `2 / 29 = 0.068966`; `GAME-0111`: `1 / 29 = 0.034483`; `GAME-0112`: `2 / 29 = 0.068966`.
- `GAME-0113`: `2 / 35 = 0.057143`; `GAME-0114`: `2 / 28 = 0.071429`; `GAME-0115`: `1 / 28 = 0.035714`; `GAME-0116`: `2 / 27 = 0.074074`.
- `GAME-0117`: `1 / 30 = 0.033333`; `GAME-0118`: `1 / 38 = 0.026316`.

## Taxonomy impact

- Registry changes: eighteen new Active genes and five reused Active genes.
- Taxonomy-change record: none.
- Candidate terms affected: live production recipe; factory logistics; power
  throttling; science consumption; pollution pressure; finite resource reserve;
  robot-fulfilled construction ghost.

## Negative results

- `ACT-068` was not reused: belts, pipes and rails participate in heterogeneous
  material systems rather than only editing one route-network abstraction.
- `OBJ-053` was not reused: Factorio has an authored first-rocket victory even
  though the save can continue indefinitely.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Factorio couples constructed production,
  logistics, power, research, finite extraction, pollution and defence in a
  live path to first-rocket victory (`FAC-001`–`FAC-010`).

## Нові гени

- [Observation | Corroborated | High] `ACT-119`–`ACT-124`, `SYS-156`–`SYS-162`,
  `CON-172`–`CON-173`, `INF-059`–`INF-060`, `OBJ-054`.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0118`.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає.

## Нові питання

- Which later factory games preserve the same live recipe-and-logistics core
  while removing extraction, enemies or embodied construction?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] Slay the Spire.
- Optimisation criterion: switch from continuous spatial automation to a
  popular run-based deckbuilding decision system.
- Expected information gain: test card reward, deck composition and encounter
  sequencing against the factory family's persistent world state.
- Backlog impact: continues the approved editorial batch as `GAME-0120`.

## Чому саме вона

- [Hypothesis | Corroborated | High] Slay the Spire introduces a commercially
  important mechanical family and should recur with later deckbuilders while
  remaining distant from Factorio's real-time automation genome.
