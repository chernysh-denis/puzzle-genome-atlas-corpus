---
game_id: GAME-0056
slug: railbound
game_title: Railbound
analysis_status: reviewed
reviewed: 2026-08-13
combination_ids:
  - COMB-0056
gene_ids:
  action:
    - ACT-028
  system:
    - SYS-099
  constraint:
    - CON-001
    - CON-047
    - CON-102
  information:
    - INF-001
  objective:
    - OBJ-035
  time:
    - TIM-009
---

# Game: Railbound

## Analysis scope

- Version / ruleset: Afterburn's current released base game, restricted to the
  fifteen ordinary levels of World 1 and excluding its optional A branches.
- Included: fixed isometric tile boards; fixed locomotive and one to four
  numbered self-propelled carriages; placing, removing and orienting a finite
  inventory of rail pieces; pre-placed immutable rail; editable junction
  direction; explicit run; simultaneous automatic carriage motion; collision
  failure; coupling every carriage to the locomotive in ascending numerical
  order; retry, reset and pre-run revision.
- Excluded: optional World 1 bonus levels; tunnels, barriers, buttons, stations,
  passengers and trolleys introduced in later worlds; level editor and Workshop;
  hints, achievements, least-rail optimisation, overworld progress, story and
  presentation.
- Direct-play status: not conducted. The developer storefront and creator
  interview establish finite rail placement followed by automatic execution.
  Three hands-on reviews corroborate the numbered-order, simultaneous movement,
  collision and locked-run boundaries; a level-by-level World 1 guide binds
  junction editing, movable versus fixed rails and the first multi-car lessons.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `RLB-001` | World 1 is the first complete authored rules block and introduces ordinary rails, editable junctions and multiple numbered carriages | Confirmed | Corroborated | High | P1, S1–S4 |
| `RLB-002` | Every level starts from one fixed finite board with declared locomotive, carriages and pre-placed rail | Confirmed | Corroborated | High | S1–S4 |
| `RLB-003` | The player places, removes and reorients rail from a finite per-level inventory before execution | Confirmed | Corroborated | High | P2, S1–S3 |
| `RLB-004` | Some authored rail is immutable while designated pieces and junction directions remain editable | Confirmed | Corroborated | High | S3, S4 |
| `RLB-005` | Starting a run advances all free carriages automatically along the configured rail without live steering or editing | Confirmed | Corroborated | High | P2, S1–S3 |
| `RLB-006` | Two carriages occupying an incompatible shared place at the same execution time crash and fail the attempt | Confirmed | Corroborated | High | P1, S1, S2 |
| `RLB-007` | Success requires every numbered carriage to reach and couple behind the locomotive in ascending order | Confirmed | Corroborated | High | P1, S1–S4 |
| `RLB-008` | Route length and junction choice delay later carriages so the required arrival order can differ from geometric distance | Confirmed | Corroborated | High | S1, S3, S4 |
| `RLB-009` | Board, inventory, rail geometry, junction state, carriage identity and failed trajectory are visible | Observation | Corroborated | High | RLB-001–RLB-008 |
| `RLB-010` | A failed run preserves a revisable authored puzzle rather than permitting edits during execution | Confirmed | Corroborated | High | P2, S1–S3 |

## Basic data

- Release / origin: Polish studio Afterburn released Railbound on 6 September
  2022; the current developer build lists more than 240 authored puzzles.
- Platform or physical form: deterministic single-player digital spatial
  machine-construction puzzle with a locked automatic execution phase.
- Puzzle family: finite-rail simultaneous carriage scheduling.
- Primary and creator sources:
  - **[P1]** [Official Afterburn page](https://afterburn.itch.io/railbound), for
    placement, removal and rerouting, safe carriage connection and later-world
    mechanics excluded from this scope.
  - **[P2]** [Afterburn creator interview](https://gameworldobserver.com/2022/06/03/afterburn-railbound-making-of-interview), documenting limited rail tiles and the prepare-then-watch execution structure.
- Hands-on and bounded corroboration:
  - **[S1]** [Nintendo Life review](https://www.nintendolife.com/reviews/switch-eshop/railbound), for fixed track inventory, branching, explicit run, numbered ascending coupling and later-world exclusions.
  - **[S2]** [Tech-Gaming review](https://www.tech-gaming.com/railbound/), for automatic junction construction, restricted rail inventory, no interaction during execution and up to four simultaneously moving carriages.
  - **[S3]** [Neoseeker World 1 guide](https://www.neoseeker.com/railbound/World_1_Puzzle_Solutions), for the precise 1-1–1-15 boundary, editable junctions, movable and immutable track, multi-car introduction and delay loops.
  - **[S4]** [TheXboxHub review](https://www.thexboxhub.com/railbound-review/), for the opening board, drag placement, finite inventory, ordered arrivals, loops and forks.
- Claim IDs: `RLB-001`–`RLB-010`.

## Mechanical decomposition

### Action Genes

- `ACT-028` — configure spatial machine layout. Before a run, the player places,
  removes and orients persistent rail components and selects junction geometry;
  their relative topology controls later automatic reachability and timing.
- `ACT-016` is absent because the player does not trace one fixed-endpoint simple
  route as one compound answer. The layout may branch and is assembled from a
  finite component inventory.
- Claim IDs: `RLB-003`, `RLB-004`.

### System Behaviour Genes

- `SYS-099` — synchronous automatic rail-car traversal. Starting the run makes
  every free carriage advance on the configured rail under one shared clock,
  follow the selected branch at junctions and couple when it reaches the
  locomotive through the currently valid approach.
- `SYS-031` is absent: the carriages are themselves routed objects and do not
  automatically board or deliver passengers in World 1.
- Resolution order: start all uncoupled carriages; advance one shared movement
  step; resolve selected junction exits; reject temporal occupancy conflicts;
  couple any eligible next carriage; test ordered completion or crash; repeat.
- Claim IDs: `RLB-005`–`RLB-008`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. Each level has a finite unchanged tile
  board with fixed vehicle starts, locomotive and immutable components.
- `CON-047` — finite reassignable network inventory. A placed rail piece leaves
  the per-level inventory and must be removed before it can be used elsewhere.
- `CON-102` — collision-free synchronous vehicle occupancy. All trajectories
  must remain mutually compatible at every shared-clock step; a geometric
  connection is insufficient if two carriages reach the same conflict region
  together.
- `CON-048` is absent: the result is one physical rail graph, not a named
  service line whose ordered station list defines its topology.
- Scarce strategic resources: rail pieces, non-branching board area, junction
  states and arrival-time separation.
- Claim IDs: `RLB-002`–`RLB-006`, `RLB-008`.

### Information Genes

- `INF-001` — fully visible current state. The board, numbered carriages,
  locomotive, rail inventory, placed geometry and junction state are visible;
  automatic failure exposes the realised trajectories.
- No future-preview gene is assigned: arrival times are derived by mentally or
  experimentally simulating deterministic motion, not displayed before run.
- Claim IDs: `RLB-002`, `RLB-009`, `RLB-010`.

### Objective Genes

- `OBJ-035` — assemble numbered vehicles at receiver in declared order. Every
  required carriage must couple behind the locomotive with `1` first and each
  successor following in ascending order.
- Merely connecting all starts to the locomotive is insufficient, and no
  passenger delivery occurs in the scoped world.
- Claim IDs: `RLB-007`, `RLB-008`.

### Time Genes

- `TIM-009` — self-paced route design before locked one-shot traversal. The
  player can revise the complete rail layout without time pressure, starts one
  deterministic multi-car run, and cannot edit until success, crash or reset.
- The gene is generalised from one vehicle / route to one committed transport
  layout; this parameter change preserves Cosmic Express's signature.
- Claim IDs: `RLB-005`, `RLB-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| One required gap and one rail piece remain | Place the piece in the gap | Inventory decreases and connected edges persist | rail is a finite machine component | `RLB-003` |
| A placed removable curve is no longer useful | Remove and replace it elsewhere | The same inventory unit returns and is redeployed | scarcity is reassignable, not consumable | `RLB-003` |
| A junction exposes the wrong exit | Toggle or reorient it before run | Its selected outgoing continuation changes | topology includes authored switch state | `RLB-004` |
| Two carriages have connected paths of unequal length | Press run | Both advance on the shared clock; the shorter arrival occurs first | layout geometry is a schedule | `RLB-005`, `RLB-008` |
| Two routes reach one conflict region on the same step | Let execution advance | The carriages crash and the attempt fails | connectivity alone is insufficient | `RLB-006` |
| Carriage 2 reaches the locomotive before carriage 1 | Let it arrive | The required train is not accepted as completed | coupling order is an objective predicate | `RLB-007` |
| Every carriage reaches the locomotive as 1, 2, … | Let the final carriage arrive | All cars couple and the level completes | ordered assembly is terminal | `RLB-007` |
| A run crashes or produces the wrong order | Retry and revise rail | The authored start returns with the layout editable | execution is locked but recoverable | `RLB-010` |

## Strategic and experiential structure

- Local decision: orient each rail piece and junction so every carriage has one
  usable continuation without spending a needed piece elsewhere.
- Medium-term planning: add or remove route length to order arrival times and
  keep simultaneous trajectories clear at shared junctions.
- Long-term structure: encode both connectivity and a complete temporal sorting
  schedule into one finite layout before committing the run.
- Common heuristics: solve backward from the required coupling order; reserve
  short paths for low numbers; use loops to delay later cars; check each shared
  tile by time step, not only by route.
- Failure attribution: deterministic playback reveals the first collision,
  wrong branch or out-of-order arrival.
- Player-trust factors: track snapping, junction direction, movement cadence,
  collision timing and coupling acceptance must remain stable.
- Claim IDs: `RLB-003`–`RLB-010`.

## Replay and variation

- World 1 levels are fixed authored instances; boards, inventories, starts and
  immutable rails change between levels but not between attempts.
- No random event or procedural setup affects the scoped transitions.
- Some levels permit spare-track solutions, but minimum-rail optimisation and
  its achievements are explicitly excluded.
- Replay comes from revising a failed schedule and optional later levels, not
  from variance within one attempt.
- Claim IDs: `RLB-001`–`RLB-004`, `RLB-010`.

## Adjacent systems and history

- Cosmic Express shares self-paced layout followed by locked automatic rail
  traversal. It traces one non-branching route to deliver typed passengers;
  Railbound assembles a finite rail graph that schedules several vehicles.
- Infinifactory and Opus Magnum share spatial machine configuration before a
  run, but execute productive component transformations rather than vehicle
  arrivals and coupling.
- Mini Metro shares rail topology but stays editable during recurring service;
  its trains carry passengers and do not solve an authored simultaneous sort.
- Freeways also converts topology into automatic traffic, but repeatedly
  evaluates weighted throughput rather than one collision-free ordered run.
- Claim IDs: `RLB-003`–`RLB-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-028` | finite rail-component layout and junction orientation |
| System Behaviour | `SYS-099` | synchronous autonomous carriage traversal and coupling |
| Constraint | `CON-001`, `CON-047`, `CON-102` | fixed board, finite rails and temporal collision avoidance |
| Information | `INF-001` | visible identities, geometry, inventory and playback |
| Objective | `OBJ-035` | couple every numbered carriage in ascending order |
| Time | `TIM-009` | self-paced design followed by locked one-shot execution |

Canonical signature:

`ACT-028; SYS-099; CON-001,CON-047,CON-102; INF-001; OBJ-035; TIM-009`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `55` (`GAME-0001`–`GAME-0055`).
- Exact genome matches: none.
- Tied near matches: `GAME-0037` — Cosmic Express (`3 / 14 = 0.214286`).
- Supported combination subsets: `COMB-0056`.
- Scan date: 2026-08-13.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0037`.

### Preserved research notes

- New genes: `SYS-099`, `CON-102`, `OBJ-035`.
- Reused genes: `ACT-028`, `CON-001`, `CON-047`, `INF-001`, `TIM-009`.
- Classification result: three `New gene` records and one new verified
  interaction; no novelty claim.

## Combination record

- `COMB-0056` captures finite rail-machine construction, synchronous vehicle
  traversal, temporal collision avoidance, ordered coupling and locked run.
- Exhaustive supporter scan: only `GAME-0056` contains the complete proper
  subset; no previous verified combination is a subset of this genome.

## Taxonomy impact

- Generalised `ACT-028` from production machinery to any persistent spatial
  machine layout whose geometry controls a later run.
- Generalised `TIM-009` from one route and vehicle to one committed transport
  layout and one or more vehicles. No prior signature changes.
- Added traversal, collision and ordered-assembly boundaries instead of treating
  them as parameters of passenger service or generic connectivity.

## Negative results

- `ACT-016`, `SYS-031`, `CON-048`, `CON-050`, `CON-051`, `OBJ-024` and later
  tunnel / barrier / station mechanics fail the declared World 1 boundary.
