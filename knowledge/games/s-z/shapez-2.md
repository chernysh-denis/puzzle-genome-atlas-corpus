---
game_id: GAME-0122
slug: shapez-2
game_title: shapez 2 - Factory
analysis_status: reviewed
reviewed: 2026-08-18
combination_ids:
  - COMB-0120
gene_ids:
  action:
    - ACT-119
    - ACT-133
    - ACT-134
  system:
    - SYS-040
    - SYS-157
    - SYS-170
    - SYS-171
  constraint:
    - CON-062
    - CON-172
  information:
    - INF-001
    - INF-060
    - INF-063
  objective:
    - OBJ-015
    - OBJ-056
  time:
    - TIM-003
---

# Game: shapez 2 - Factory

## Analysis scope

- Version / ruleset: released shapez 2 version 1.0, ordinary single-player
  Classic mode on Regular difficulty from the initial certification through
  the finite Final Qualification milestone.
- Included: infinite asteroid shape sources; belts, lifts, pipes, platforms,
  space belts and trains; three machine layers; cutting, rotating, stacking,
  swapping, painting, colour mixing, pins and crystals as they enter the
  Regular milestone chain; exact Vortex quotas; jobs, research points,
  upgrades, blueprints and the finite qualification sequence.
- Excluded: experimental Hexagonal and Manufacturing modes; Hard and Insane
  scenario parameters; custom modes, sandbox, wires and Make-Anything-Machines
  as an optional post-unlock optimisation layer; mods, Workshop, achievements,
  cosmetics, DLC and the infinite Operator Level after qualification.
- Direct-play status: not conducted. The current developer description and
  official 1.0 site establish the overall factory rules; the official wiki
  linked as the product manual establishes exact milestones, Vortex credit,
  blueprints, upgrades, platforms and the bounded post-qualification boundary.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SHZ-001` | The player edits a running multi-layer factory by placing, rotating and freely deleting persistent machines and transport entities | Confirmed | Corroborated | High | P1, P2 |
| `SHZ-002` | Infinite asteroid sources and live belts, lifts, pipes, space belts and trains continuously move shapes or fluids without a power requirement | Confirmed | Corroborated | High | P1, P2, P8 |
| `SHZ-003` | Fixed-purpose machines repeatedly cut, rotate, stack, swap, paint or otherwise transform compatible geometric shape structure | Confirmed | Corroborated | High | P1, P2, P3 |
| `SHZ-004` | The Vortex credits only delivered shapes relevant to an active exact schema and counts them toward its disclosed quota | Confirmed | Direct | High | P4 |
| `SHZ-005` | Completing milestone quotas persistently unlocks machines, floors, platforms, trains, jobs and later progression | Confirmed | Direct | High | P5 |
| `SHZ-006` | Research points buy eligible permanent shop upgrades, separately from automatic milestone rewards | Confirmed | Direct | High | P6 |
| `SHZ-007` | Blueprints capture and paste reusable factory regions, subject to the save's configured blueprint-point rule | Confirmed | Direct | High | P7 |
| `SHZ-008` | Buildings are free, extraction sources do not deplete, and ordinary play has no enemies or time limit | Confirmed | Direct | High | P1, P2 |
| `SHZ-009` | Regular progression ends with Final Qualification, after which infinite Operator goals become the main optional pursuit | Confirmed | Direct | High | P5, P9 |
| `SHZ-010` | At Atlas resolution the game shares live construction and logistics with Factorio but not Factorio's power, finite-resource, pollution, enemy or rocket genes | Observation | Corroborated | High | P1–P9, GAME-0119 |

## Basic data

- Release / origin: tobspr Games released the 1.0 version on 23 April 2026,
  after an Early Access launch on 15 August 2024.
- Platform or physical form: top-down three-dimensional factory construction
  and real-time automation simulation in space.
- Puzzle family: automation and spatial programming; route and network
  construction; ordered dependency sequencing; exact-output production.
- Primary and first-party sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/2162800/shapez_2/),
    current title, release, live multi-layer factory, infinite resources,
    no-threat boundary, research and blueprint features.
  - **[P2]** [official shapez 2 site](https://shapez2.com/), 1.0 scope,
    transformations, transport, platforms, research and rebuild rules.
  - **[P3]** [Official Shapez 2 Wiki: Shapes](https://shapez2.wiki.gg/wiki/Shapes),
    structured shape layers, quadrants, colours, pins and crystals.
  - **[P4]** [Official Shapez 2 Wiki: Vortex](https://shapez2.wiki.gg/wiki/Vortex),
    recurrent source-to-receiver flow, exact credit and delivery indicators.
  - **[P5]** [Official Shapez 2 Wiki: Milestones](https://shapez2.wiki.gg/wiki/Milestones),
    ordered Regular rewards, quotas and Final Qualification.
  - **[P6]** [Official Shapez 2 Wiki: Shop](https://shapez2.wiki.gg/wiki/Shop),
    research-point costs, prerequisites and persistent upgrades.
  - **[P7]** [Official Shapez 2 Wiki: Blueprints](https://shapez2.wiki.gg/wiki/Blueprints),
    blueprint points and reusable layout placement.
  - **[P8]** [Official Shapez 2 Wiki: Trains](https://shapez2.wiki.gg/wiki/Trains),
    train transport and bulk Vortex delivery.
  - **[P9]** [Official Shapez 2 Wiki: Operator Level](https://shapez2.wiki.gg/wiki/Operator_Level),
    infinite post-milestone continuation boundary.
- Claim IDs: `SHZ-001`–`SHZ-010`.

## Mechanical decomposition

### Action Genes

- `ACT-119` places, rotates, removes or replaces machines, belts, lifts,
  platforms and transport entities while the rest of the factory continues.
- `ACT-133` captures and immediately pastes compatible reusable factory
  regions rather than creating material-supply ghost requests.
- `ACT-134` spends research points on one eligible permanent shop upgrade.
- Candidate genes: none.
- Parameters: entity class, floor, orientation, blueprint transform, point
  cost, prerequisite and upgrade level.
- Claim IDs: `SHZ-001`, `SHZ-006`, `SHZ-007`.

### System Behaviour Genes

- `SYS-040` couples recurring asteroid sources with the exact-product Vortex
  sink; a credited shape is consumed while sources remain available.
- `SYS-157` continuously transports shapes and fluids through live belts,
  lifts, pipes, space belts and trains while construction remains editable.
- `SYS-170` repeatedly applies the fixed structural operation of each supplied
  cutting, rotating, stacking, swapping, painting, pin or crystal machine.
- `SYS-171` converts a completed exact-shape quota into persistent milestone
  rewards and the next progression options.
- Resolution order: accept construction; advance transport; admit compatible
  machine inputs; emit transformed outputs; move delivery into the Vortex;
  credit active schemas; apply a completed quota and expose its rewards.
- Claim IDs: `SHZ-002`–`SHZ-005`.

### Constraint Genes

- `CON-062` rejects incompatible overlapping machine, belt, platform and
  transport footprints while allowing only declared layer connections.
- `CON-172` holds an operator when the wrong structural input arrives, a
  required second input is absent or the output cannot accept the result.
- Infinite sources, free buildings and the lack of power are deliberate
  absences, not finite-resource or budget genes.
- Scarce strategic resources: platform capacity, belt and train throughput,
  machine footprint, three-layer routing, Vortex input ports, blueprint points
  where enabled and research points for optional upgrades.
- Claim IDs: `SHZ-001`–`SHZ-008`.

### Information Genes

- `INF-001` exposes the current factory, moving shapes, machine interiors and
  transport state; difficulty is not produced by hidden local transitions.
- `INF-060` exposes live flow, blockage and throughput diagnostics through open
  buildings, shape previews and transport state.
- `INF-063` shows the exact current milestone shape, quota progress and reward
  that will become available on completion.
- Candidate genes: none.
- Claim IDs: `SHZ-003`–`SHZ-006`.

### Objective Genes

- `OBJ-015` requires automatic repeated construction and delivery of each
  exact target assembly until its active quota is satisfied.
- `OBJ-056` orders those production goals toward the finite Regular Final
  Qualification; infinite Operator goals are explicitly outside scope.
- Success and failure: a quota completes when enough matching shapes are
  credited. A stalled or wrong factory remains editable without terminal loss;
  the player can delete and rebuild freely.
- Claim IDs: `SHZ-004`, `SHZ-005`, `SHZ-008`, `SHZ-009`.

### Time Genes

- `TIM-003` keeps extraction, transport, transformation and delivery live while
  the player builds, diagnoses or replaces other parts of the factory.
- It is not `TIM-006`: there is no separate locked deterministic test phase
  that must be reset before editing resumes.
- Claim IDs: `SHZ-001`–`SHZ-004`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| An extractor faces an infinite asteroid patch and a belt has free output | Place and connect the extractor | raw shapes enter the moving belt repeatedly without reducing the source | extraction is recurrent and logistics remain live | `SHZ-001`, `SHZ-002` |
| A whole shape enters a correctly oriented cutter | Let the line advance | the machine emits the declared separated parts at its output positions | machine identity fixes a repeatable structural transform | `SHZ-003` |
| Two compatible partial shapes reach a supplied stacker | Continue the live tick | the machine places one accepted assembly above the other and emits the resulting layered shape | stacking changes structured layer state, not inventory quantity alone | `SHZ-003` |
| The current milestone requests one exact shape and its counter is incomplete | Deliver that shape to the Vortex | the receiver consumes it and increments that milestone's visible count | exact schema and quota govern credit | `SHZ-004` |
| A geometrically different shape reaches the same Vortex | Deliver it | it is consumed but does not advance the active milestone counter | receiver occupancy alone is insufficient | `SHZ-004` |
| The last required copy of a milestone shape arrives | Advance delivery | the quota completes and the listed machines, mechanics or rewards become available | progression is caused by exact production volume | `SHZ-005` |
| A shop node is visible but its point cost exceeds the balance | Try to buy it, then earn points and retry | the first request is rejected; the second persists the declared upgrade | milestone disclosure and optional research purchase are distinct | `SHZ-006` |
| A working factory module has been selected as a blueprint | Paste it on compatible free space | another live instance appears and begins operating with connected inputs | reusable layouts directly scale production | `SHZ-007` |
| A congested line is feeding too slowly | Delete and rebuild part of the route | removed buildings incur no material loss and the rest of the world keeps running | iteration is live, reversible and not power- or cost-gated | `SHZ-008` |

## Strategic and experiential structure

- Local decision: align one operator with compatible shape quadrants, layers,
  colours and output lanes without blocking the neighbouring line.
- Medium-term planning: balance belt rates, machine ratios, vertical lifts,
  fluid supply and platform interfaces so every intermediate reaches the next
  fixed transform at sufficient throughput.
- Long-term structure: preserve reusable modules and space-scale transport as
  milestone shapes demand deeper dependency graphs and larger delivery quotas.
- Common heuristics: verify one transformation visually; isolate each
  intermediate; calculate ratios; reserve platform interfaces; blueprint a
  stable module; scale only the current bottleneck.
- Failure attribution: open machines, visible shapes and explicit quota
  indicators usually distinguish wrong geometry, missing input, blocked output
  and insufficient throughput.
- Player-trust factors: quadrant and layer transforms, stack order, crystal
  support, belt rate, train unloading, receiver equivalence and quota credit
  must agree at every scale.
- Claim IDs: `SHZ-001`–`SHZ-009`.

## Replay and variation

- What changes between saves: map seed and source positions, selected
  difficulty, platform layouts, routing topology, research order and chosen
  throughput scale.
- Randomness or procedural generation: resource placement and later excluded
  Operator shapes may vary; the scoped machine transitions and disclosed
  milestone schemas remain deterministic.
- Multiple viable strategies: compact local lines, modular platforms, trains,
  direct belts, vertical stacking and different upgrade orders can satisfy the
  same exact quotas.
- Typical replay motive: attempt another difficulty or topology, improve
  throughput and clarity, or replace a large bespoke line with reusable modules.
- Claim IDs: `SHZ-001`–`SHZ-009`.

## Adjacent systems and history

- Factorio shares live construction and logistics, but its scoped path couples
  selected recipes to power, finite deposits, science, pollution, enemies and
  a rocket. shapez 2 removes those pressures and makes exact geometric
  transformation plus delivery volume the progression test.
- Opus Magnum and SpaceChem also repeat exact structured output, but they lock
  an authored puzzle machine into a resettable deterministic run. shapez 2
  leaves the spatial factory continuously active while it is edited and scaled.
- Infinifactory transforms and submits exact voxel assemblies inside authored
  production puzzles; shapez 2 replaces finite chambers and collision faults
  with a persistent open world and milestone-linked throughput progression.
- Hexagonal and Manufacturing modes change the shape vocabulary or source
  model enough to require separate scopes and are not parameters of this genome.
- Claim IDs: `SHZ-001`–`SHZ-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-119`, `ACT-133`, `ACT-134` | placement, blueprint and shop parameters |
| System Behaviour | `SYS-040`, `SYS-157`, `SYS-170`, `SYS-171` | transport, transform and quota rules |
| Constraint | `CON-062`, `CON-172` | footprint and input-output compatibility |
| Information | `INF-001`, `INF-060`, `INF-063` | diagnostic and milestone disclosure |
| Objective | `OBJ-015`, `OBJ-056` | exact quota and qualification boundary |
| Time | `TIM-003` | live simulation tick |

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`: `ACT-119,ACT-133,ACT-134; SYS-040,SYS-157,SYS-170,SYS-171; CON-062,CON-172; INF-001,INF-060,INF-063; OBJ-015,OBJ-056; TIM-003`.
- Indexed games scanned: 122, including this record.
- Indexed combinations scanned: 120.
- Exact genome matches: none.
- Near matches and similarity scores: `GAME-0119` Factorio at
  `7 / 31 = 0.225806`, `GAME-0042` Infinifactory at `4 / 20 = 0.200000`,
  `GAME-0022` Opus Magnum at `4 / 23 = 0.173913` and `GAME-0032` SpaceChem at
  `3 / 23 = 0.130435`.
- Supported combination subsets: `COMB-0120`.
- Scan date: 2026-08-18.

### Full prior-game Jaccard scan

- `GAME-0001`: `1 / 28 = 0.035714`; `GAME-0002`: `1 / 21 = 0.047619`; `GAME-0003`: `0 / 24 = 0.000000`; `GAME-0004`: `2 / 28 = 0.071429`; `GAME-0005`: `1 / 21 = 0.047619`; `GAME-0006`: `1 / 23 = 0.043478`; `GAME-0007`: `1 / 22 = 0.045455`; `GAME-0008`: `1 / 21 = 0.047619`.
- `GAME-0009`: `1 / 30 = 0.033333`; `GAME-0010`: `1 / 23 = 0.043478`; `GAME-0011`: `1 / 27 = 0.037037`; `GAME-0012`: `1 / 23 = 0.043478`; `GAME-0013`: `1 / 27 = 0.037037`; `GAME-0014`: `1 / 29 = 0.034483`; `GAME-0015`: `1 / 28 = 0.035714`; `GAME-0016`: `2 / 28 = 0.071429`.
- `GAME-0017`: `0 / 28 = 0.000000`; `GAME-0018`: `2 / 32 = 0.062500`; `GAME-0019`: `1 / 24 = 0.041667`; `GAME-0020`: `1 / 28 = 0.035714`; `GAME-0021`: `2 / 22 = 0.090909`; `GAME-0022`: `4 / 23 = 0.173913`; `GAME-0023`: `0 / 25 = 0.000000`; `GAME-0024`: `1 / 26 = 0.038462`.
- `GAME-0025`: `2 / 24 = 0.083333`; `GAME-0026`: `2 / 25 = 0.080000`; `GAME-0027`: `2 / 25 = 0.080000`; `GAME-0028`: `2 / 30 = 0.066667`; `GAME-0029`: `2 / 25 = 0.080000`; `GAME-0030`: `2 / 27 = 0.074074`; `GAME-0031`: `1 / 25 = 0.040000`; `GAME-0032`: `3 / 23 = 0.130435`.
- `GAME-0033`: `2 / 26 = 0.076923`; `GAME-0034`: `2 / 27 = 0.074074`; `GAME-0035`: `2 / 31 = 0.064516`; `GAME-0036`: `1 / 26 = 0.038462`; `GAME-0037`: `1 / 23 = 0.043478`; `GAME-0038`: `2 / 29 = 0.068966`; `GAME-0039`: `1 / 23 = 0.043478`; `GAME-0040`: `1 / 22 = 0.045455`.
- `GAME-0041`: `2 / 24 = 0.083333`; `GAME-0042`: `4 / 20 = 0.200000`; `GAME-0043`: `1 / 28 = 0.035714`; `GAME-0044`: `1 / 24 = 0.041667`; `GAME-0045`: `1 / 28 = 0.035714`; `GAME-0046`: `1 / 24 = 0.041667`; `GAME-0047`: `1 / 28 = 0.035714`; `GAME-0048`: `1 / 28 = 0.035714`.
- `GAME-0049`: `0 / 24 = 0.000000`; `GAME-0050`: `1 / 29 = 0.034483`; `GAME-0051`: `2 / 29 = 0.068966`; `GAME-0052`: `1 / 24 = 0.041667`; `GAME-0053`: `1 / 23 = 0.043478`; `GAME-0054`: `1 / 25 = 0.040000`; `GAME-0055`: `1 / 24 = 0.041667`; `GAME-0056`: `1 / 22 = 0.045455`.
- `GAME-0057`: `1 / 22 = 0.045455`; `GAME-0058`: `1 / 23 = 0.043478`; `GAME-0059`: `1 / 21 = 0.047619`; `GAME-0060`: `1 / 21 = 0.047619`; `GAME-0061`: `1 / 24 = 0.041667`; `GAME-0062`: `1 / 22 = 0.045455`; `GAME-0063`: `1 / 21 = 0.047619`; `GAME-0064`: `1 / 19 = 0.052632`.
- `GAME-0065`: `0 / 22 = 0.000000`; `GAME-0066`: `0 / 25 = 0.000000`; `GAME-0067`: `0 / 23 = 0.000000`; `GAME-0068`: `0 / 23 = 0.000000`; `GAME-0069`: `1 / 22 = 0.045455`; `GAME-0070`: `1 / 22 = 0.045455`; `GAME-0071`: `1 / 21 = 0.047619`; `GAME-0072`: `1 / 22 = 0.045455`.
- `GAME-0073`: `1 / 21 = 0.047619`; `GAME-0074`: `1 / 23 = 0.043478`; `GAME-0075`: `1 / 23 = 0.043478`; `GAME-0076`: `1 / 21 = 0.047619`; `GAME-0077`: `1 / 21 = 0.047619`; `GAME-0078`: `1 / 21 = 0.047619`; `GAME-0079`: `1 / 21 = 0.047619`; `GAME-0080`: `1 / 21 = 0.047619`.
- `GAME-0081`: `1 / 22 = 0.045455`; `GAME-0082`: `1 / 22 = 0.045455`; `GAME-0083`: `1 / 22 = 0.045455`; `GAME-0084`: `1 / 24 = 0.041667`; `GAME-0085`: `0 / 26 = 0.000000`; `GAME-0086`: `1 / 27 = 0.037037`; `GAME-0087`: `2 / 23 = 0.086957`; `GAME-0088`: `1 / 23 = 0.043478`.
- `GAME-0089`: `1 / 23 = 0.043478`; `GAME-0090`: `1 / 29 = 0.034483`; `GAME-0091`: `2 / 22 = 0.090909`; `GAME-0092`: `2 / 23 = 0.086957`; `GAME-0093`: `1 / 23 = 0.043478`; `GAME-0094`: `2 / 23 = 0.086957`; `GAME-0095`: `2 / 25 = 0.080000`; `GAME-0096`: `2 / 23 = 0.086957`.
- `GAME-0097`: `2 / 21 = 0.095238`; `GAME-0098`: `2 / 20 = 0.100000`; `GAME-0099`: `1 / 22 = 0.045455`; `GAME-0100`: `1 / 25 = 0.040000`; `GAME-0101`: `0 / 25 = 0.000000`; `GAME-0102`: `0 / 22 = 0.000000`; `GAME-0103`: `1 / 23 = 0.043478`; `GAME-0104`: `1 / 23 = 0.043478`.
- `GAME-0105`: `1 / 24 = 0.041667`; `GAME-0106`: `0 / 22 = 0.000000`; `GAME-0107`: `1 / 22 = 0.045455`; `GAME-0108`: `1 / 24 = 0.041667`; `GAME-0109`: `1 / 30 = 0.033333`; `GAME-0110`: `2 / 21 = 0.095238`; `GAME-0111`: `1 / 21 = 0.047619`; `GAME-0112`: `2 / 21 = 0.095238`.
- `GAME-0113`: `2 / 27 = 0.074074`; `GAME-0114`: `2 / 20 = 0.100000`; `GAME-0115`: `1 / 20 = 0.050000`; `GAME-0116`: `2 / 19 = 0.105263`; `GAME-0117`: `1 / 22 = 0.045455`; `GAME-0118`: `1 / 30 = 0.033333`; `GAME-0119`: `7 / 31 = 0.225806`; `GAME-0120`: `0 / 44 = 0.000000`.
- `GAME-0121`: `1 / 37 = 0.027027`.

## Taxonomy impact

- Registry changes: six new Active genes and nine reused Active genes.
- Taxonomy-change record: none.
- Candidate terms affected: reusable immediate factory blueprint; purchased
  factory upgrade; fixed geometric transform; milestone delivery unlock;
  disclosed exact quota; finite factory qualification.
- Family membership: `FAM-005` route and network construction, `FAM-008`
  automation and spatial programming, `FAM-010` real-time system pressure and
  `FAM-017` ordered dependency sequencing.
- Similarity alone did not assign these families; the decision loop satisfies
  each family boundary directly.
- Claim IDs: `SHZ-001`–`SHZ-010`.

## Combination analysis

- `COMB-0120` is a proper twelve-gene subset that preserves the live exact-
  shape production, receiver quota and finite unlock chain.
- No previous registered combination is a complete subset of this genome.
  `COMB-0118` fails because shapez 2 lacks its power, science-pack, finite-
  reserve, robot-ghost and rocket dependencies; `COMB-0022`, `COMB-0032` and
  `COMB-0042` fail because this live world has no separate resettable test phase.
- The shared genes with Factorio remain meaningful individual recurrence, not
  evidence that the two full production interactions are identical.

## Novelty assessment

- The game does not prove that geometric automation is historically novel.
- Within the current Atlas it is the first carrier to make fixed geometric
  transformation and exact Vortex delivery quotas the unlock engine of one
  persistent live factory.
- Strongest falsification target: the original shapez or another pure factory
  game with infinite sources, exact-shape quotas and a finite unlock chain.
- Confidence: high for the scoped rules and classification; exact performance
  constants remain version and difficulty parameters.

## Verification summary

- [Confirmed | Corroborated | High] Live placement, multi-layer transport,
  fixed shape transforms and unrestricted rebuilding are documented by the
  current developer product sources (`SHZ-001`–`SHZ-003`, `SHZ-008`).
- [Confirmed | Direct | High] The official product manual documents Vortex
  credit, milestones, shop upgrades, blueprints and post-qualification
  Operator progression (`SHZ-004`–`SHZ-009`).
- [Observation | Corroborated | High] Full-corpus comparison separates the
  exact-shape unlock loop from Factorio and resettable production puzzles
  (`SHZ-010`).

## Open questions

- Do future 1.x updates change the Regular milestone count or only numerical
  quotas and reward costs?
- Which later pure-automation game will independently repeat enough of
  `COMB-0120` to promote it from a single-carrier verified interaction to a
  recurring combination?
- Would a separately scoped Manufacturing mode require a different recurrent
  source gene because its converter hub changes the input model?

## Research notes

- `shapez 2 - Factory` is the current official store title; the stable slug
  remains `shapez-2` so title changes do not break URLs.
- The Ukrainian display keeps the brand and adds the explanatory translation
  `Форми 2 — Фабрика` in parentheses.
- Official wiki pages are treated as first-party product documentation because
  the Steam listing exposes them through its “View the manual” link and the
  wiki identifies itself as the Official Shapez 2 Wiki.

## Negative results

- `SYS-156` is absent: shape machines apply a fixed structural operation
  rather than a player-selected item recipe that consumes declared quantities
  and energy.
- `ACT-120` is absent from the bounded core: optional filters and wires do not
  define ordinary milestone progression, while most scoped operators have a
  fixed function.
- `SYS-158`, `SYS-161`, `CON-173` and `OBJ-054` are absent because there is no
  electric network, resource depletion, extractor-locus exhaustion or rocket
  objective.
- `ACT-124` and `SYS-162` are absent: pasted blueprints immediately place free
  compatible entities instead of creating inventory-backed robot requests.
- `TIM-006` is absent because editing and execution are simultaneous.

## Delta summary

- Added one reviewed game, `GAME-0122`, and one verified proper-subset
  interaction, `COMB-0120`.
- Added six Active genes: `ACT-133`, `ACT-134`, `SYS-170`, `SYS-171`,
  `INF-063` and `OBJ-056`; reused nine existing genes.
- Added bilingual game presentation, all-role plain-language explanations,
  salience roles and four existing family memberships.
- No prior gene boundary or game signature was rewritten.

## Нові факти

- Версія 1.0 вийшла 23 квітня 2026 року; звичайна Regular-прогресія має
  скінченну Final Qualification, після якої починаються необов'язкові
  нескінченні Operator-цілі.
- Форми надходять із невичерпних джерел, перетворюються живими машинами й
  зараховуються Вихором лише за відповідною структурою та квотою.
- Безкоштовні будівлі, відсутність електрики, ворогів і таймера роблять
  пропускну здатність та геометрію мережі основними обмеженнями.

## Нові гени

- `ACT-133`, `ACT-134`, `SYS-170`, `SYS-171`, `INF-063`, `OBJ-056`.

## Нові комбінації

- `COMB-0120` — жива фабрика повторно перетворює структуровані форми й
  доставляє точні квоти, що відкривають наступні можливості до фінальної
  кваліфікації.

## Зміни таксономії

- Нової родини не потрібно. `GAME-0122` безпосередньо входить до `FAM-005`,
  `FAM-008`, `FAM-010` і `FAM-017`.
