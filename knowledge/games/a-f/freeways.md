---
game_id: GAME-0052
slug: freeways
game_title: Freeways
analysis_status: reviewed
reviewed: 2026-08-13
combination_ids:
  - COMB-0052
gene_ids:
  action:
    - ACT-068
    - ACT-069
  system:
    - SYS-093
    - SYS-094
  constraint:
    - CON-099
  information:
    - INF-001
    - INF-028
  objective:
    - OBJ-002
    - OBJ-033
  time:
    - TIM-011
---

# Game: Freeways

## Analysis scope

- Version / ruleset: current desktop base game after the January 2025 update,
  scoped to one ordinary early authored interchange from the original map.
- Included unit: inspect the fixed road signs and weighted destination arrows;
  draw a directed freeform network; change stroke elevation for one grade-
  separated crossing; reach `Network Complete`; run one accelerated simulated
  day; inspect speed, concrete, complexity and total efficiency; then revise
  with Undo or added road and evaluate again.
- Excluded: the second 80-level map, toll booths, world-map progression, later
  intersection layouts, achievements, best-design restoration, exact platform
  gestures and presentation. Undo is included because it changes the current
  released desktop edit boundary; toll scoring is not.
- Direct-play status: not conducted. Official product and update notes establish
  freeform construction, simulation, 160 levels and current Undo. Five hands-on
  sources independently reproduce signs, elevation, connectivity, traffic,
  evaluation metrics and retry. No particular authored road layout or exact
  pathfinding tie-break is claimed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FRW-001` | A level begins with fixed entrances or buildings whose signs disclose required destinations and relative traffic frequencies | Confirmed | Corroborated | High | P1, R2, R3 |
| `FRW-002` | The player freehand-draws a persistent directed branching road graph rather than placing tile roads | Confirmed | Corroborated | High | P1, P2, R1 |
| `FRW-003` | Raise and lower controls make crossing strokes grade-separated instead of connected at the same elevation | Confirmed | Corroborated | High | R1, R4 |
| `FRW-004` | Cars enter automatically, choose connected routes to declared destinations and can queue at merges or intersections | Confirmed | Corroborated | High | P1, R1–R4 |
| `FRW-005` | Every required directed connection must exist before `Network Complete` enables the full evaluation | Confirmed | Corroborated | High | R3, R4 |
| `FRW-006` | The bounded traffic run reports traffic speed, concrete use, network complexity and a combined efficiency result | Confirmed | Corroborated | High | R1, R3–R5 |
| `FRW-007` | A jam exposes a throughput failure but retains the design for revision or full restart | Confirmed | Corroborated | High | R2, R5 |
| `FRW-008` | Current desktop Freeways includes ordered Undo and retains a best-scoring design, unlike the original 2017 release | Confirmed | Direct | High | P2 |
| `FRW-009` | The loop is neither Mini Motorways live growth nor Cosmic Express locked one-shot traversal: authored demand is fixed and the same network is repeatedly evaluated | Observation | Corroborated | High | FRW-001–FRW-008 |

## Basic data

- Release / origin: Captain Games released Freeways on 1 October 2017; the
  January 2025 update added 80 levels, Undo, toll booths and best-design restore.
- Platform or physical form: single-player digital interchange-design and
  traffic-simulation puzzle for desktop and mobile.
- Puzzle family: weighted directed-network design under bounded traffic tests.
- Primary and official sources:
  - **[P1]** [Official Steam page](https://store.steampowered.com/app/780210/Freeways/),
    for freehand road drawing, traffic simulation, jam avoidance and 160 levels.
  - **[P2]** [Official Big Update notes](https://captaingames.itch.io/freeways/devlog/876469/big-update),
    for current Undo, the second map, toll booths and best-design restoration.
- Hands-on corroboration:
  - **[R1]** [Pocket Gamer review](https://www.pocketgamer.com/freeways/review/),
    for drag drawing, raise/lower controls, automatic traffic and efficiency.
  - **[R2]** [Stuff review](https://www.stuff.tv/review/app-of-the-week-freeways-review/),
    for sign inspection, cars after connections, the full-day run and retry.
  - **[R3]** [Player.One review](https://www.player.one/freeways-game-mobile-traffic-engineer-simulation-review-ios-android-windows-120251),
    for `Network Complete` and the three evaluation components.
  - **[R4]** [WIRED account](https://www.wired.com/story/freeways-traffic-engineer-game/),
    for endpoint connectivity, overpasses, merges and reported metrics.
  - **[R5]** [Hyperallergic review](https://hyperallergic.com/design-an-efficient-highway-system-or-gridlocked-nightmare-in-this-video-game/),
    for time-lapse evaluation, concrete, jams and restart.
- Claim IDs: `FRW-001`–`FRW-009`.

## Mechanical decomposition

### Action Genes

- `ACT-068` — edit persistent branching road network. Freeways generalises the
  representation from Mini Motorways tiles to freehand directed curves; Undo
  revises the retained graph but does not turn it into simulation-history rewind.
- `ACT-069` — adjust active road-stroke elevation. Raising or lowering the
  drawn segment changes crossing connectivity, not merely rendering.
- `ACT-006` is absent: the fast simulated day is the fixed evaluation phase of
  `TIM-011`, not a reusable command for changing ongoing progression speed.
- Claim IDs: `FRW-002`, `FRW-003`, `FRW-008`.

### System Behaviour Genes

- `SYS-093` — automatic weighted origin-destination road traffic. Authored
  demand introduces cars at endpoints, chooses legal directed routes and moves
  them to required exits without direct steering.
- `SYS-094` — shared-road traffic congestion resolution. Physical cars slow
  and queue at merging or intersecting flows even when reachability is valid.
- `SYS-092` is absent: there are no colour-compatible house-bound cars or
  destination pins. `SYS-031` is absent because no passenger boards a vehicle.
- Resolution order: validate reachability; spawn vehicles from weighted demand;
  choose routes on the directed graph; advance with spacing and merge rules;
  accumulate traffic statistics; detect jams; report the bounded result.
- Claim IDs: `FRW-001`, `FRW-004`–`FRW-007`.

### Constraint Genes

- `CON-099` — elevation-conditioned road-crossing connectivity. Same-level
  strokes join; separated levels cross without exchanging traffic.
- Concrete and geometric complexity are evaluation penalties, not finite
  construction budgets. `CON-047` is therefore absent.
- The current release's Undo makes original no-undo descriptions historical;
  no active irreversibility constraint is assigned.
- Claim IDs: `FRW-003`, `FRW-006`, `FRW-008`.

### Information Genes

- `INF-001` — endpoints, roads, elevation, cars, queues, connection state and
  evaluation results are visible.
- `INF-028` — selecting a sign or building exposes required destinations and
  relative traffic frequency before construction is evaluated.
- Exact spawn times and pathfinding tie-breaks are not claimed as previewed.
- Claim IDs: `FRW-001`, `FRW-004`–`FRW-006`.

### Objective Genes

- `OBJ-033` — establish every declared directed network connection. This is the
  functional gate represented by `Network Complete`.
- `OBJ-002` — maximise the combined efficiency result by improving traffic
  speed while avoiding excessive concrete and complexity.
- The three components feed one reported total, so `OBJ-016` is absent: they
  are not independent histogram objectives like Opus Magnum's metrics.
- Claim IDs: `FRW-005`, `FRW-006`.

### Time Genes

- `TIM-011` — editable network with repeatable bounded traffic evaluation.
  Construction is self-paced; light traffic may expose connections, while the
  complete network enables a fast simulated day whose retained design can be
  revised and rerun.
- `TIM-003` is absent because demand and topology do not grow indefinitely
  during an endless scored session. `TIM-006` is absent because there is no
  deterministic cyclic machine program. `TIM-009` is absent because the graph
  branches and persists through repeated evaluations rather than one traversal.
- Claim IDs: `FRW-004`–`FRW-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| An entrance sign is selected | Inspect its arrows | Required destinations and relative weights appear | demand is declared before design | `FRW-001` |
| Two road endpoints are disconnected | Drag a continuous road between them | A directed graph edge persists and cars may use it | freehand graph editing | `FRW-002` |
| A ground stroke crosses another ground stroke | Complete the crossing | The graph gains a same-level junction | geometry can create routing choices | `FRW-003` |
| The active stroke approaches that crossing | Raise it, cross, then lower it | Two routes overlap visually but have no exchange edge | elevation controls connectivity | `FRW-003` |
| One required destination is unreachable | Finish all other links | `Network Complete` remains unavailable | every declared pair is conjunctive | `FRW-005` |
| All directed requirements are reachable | Complete the final link | `Network Complete` appears and evaluation becomes available | reachability gates evaluation | `FRW-005` |
| Two high-volume routes share a merge | Run the simulated day | Cars slow and a queue can propagate upstream | connectivity is not throughput | `FRW-004`, `FRW-007` |
| A complete network finishes its run | Inspect the result | Speed, concrete, complexity and total efficiency are reported | optimisation is composite | `FRW-006` |
| A retained result has a poor merge | Undo or add a bypass, then rerun | The revised graph receives another bounded result | iterative evaluation timing | `FRW-008`, `FRW-009` |

## Strategic and experiential structure

- Local decision: choose whether a crossing should merge at ground level or
  pass above / below, and shape the curve without accidental junctions.
- Medium-term planning: separate high-frequency flows, lengthen merge space and
  preserve direct routes without spending excessive concrete.
- Long-term structure: satisfy all directed pairs, then iterate on bottlenecks
  revealed by the full-day evaluation rather than merely adding connectivity.
- Common heuristics: inspect every sign first; reserve elevation for conflicting
  heavy flows; avoid short weave sections; revise the first persistent queue.
- Failure attribution: moving cars and component metrics usually expose whether
  congestion, distance, concrete or graph complexity caused the poor result;
  route-choice quirks remain a trust-sensitive parameter.
- Player-trust factors: stroke snapping, directed-edge orientation, crossing
  elevation, path selection, merge priority and Undo order must remain stable.
- Claim IDs: `FRW-001`–`FRW-009`.

## Replay and variation

- Authored endpoint layout and demand weights change by level; the scoped level
  itself contains no procedural topology or demand surprise.
- Many geometrically distinct interchanges can meet connectivity, while their
  congestion and concrete results differ.
- Replay is driven by improving efficiency, repairing a jam, reducing concrete
  or complexity and comparing a revision with the retained best result.
- Claim IDs: `FRW-001`, `FRW-006`–`FRW-009`.

## Adjacent systems and history

- Mini Motorways shares a branching road graph and physical congestion, but its
  map grows under unpreviewed live demand, uses finite tiles and ends on overload.
- Mini Metro uses named lines, trains and passengers under live growth rather
  than freehand roads and fixed origin-destination weights.
- Pipe Mania edits a queued tile route while an advancing flow forces timing;
  Freeways permits self-paced construction before repeatable evaluation.
- Cosmic Express locks one unbranched route for a single passenger-service
  traversal; Freeways retains a branching graph across many-vehicle tests.
- Claim IDs: `FRW-001`–`FRW-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-068`, `ACT-069` | curve gesture, Undo order |
| System Behaviour | `SYS-093`, `SYS-094` | path choice, merge priority |
| Constraint | `CON-099` | elevation bands and snapping |
| Information | `INF-001`, `INF-028` | demand-weight rendering |
| Objective | `OBJ-002`, `OBJ-033` | metric weights |
| Time | `TIM-011` | construction traffic and run horizon |

Canonical signature:

`ACT-068,ACT-069; SYS-093,SYS-094; CON-099; INF-001,INF-028; OBJ-002,OBJ-033; TIM-011`

## Corpus comparison

- Indexed games scanned: every prior record `GAME-0001`–`GAME-0051`.
- Exact genome matches: none.
- Existing combination subsets: none. `COMB-0051` fails its random growth,
  finite inventory, overload and live-time requirements; `COMB-0037` fails its
  passenger and capacity core. Every other verified proper subset was tested.
- Unique near match: `GAME-0051` — Mini Motorways at intersection `3`, union
  `23`, `3 / 23 = 0.130435`, sharing road-graph editing, physical congestion
  and numerical optimisation while differing on authored demand and evaluation
  timing. Cut the Rope follows at `2 / 17 = 0.117647` through only visibility
  and score.
- Full numeric scan (`intersection / union = Jaccard`):
  - `GAME-0001`: `2 / 22 = 0.090909`.
  - `GAME-0002`: `1 / 16 = 0.062500`.
  - `GAME-0003`: `0 / 19 = 0.000000`.
  - `GAME-0004`: `2 / 23 = 0.086957`.
  - `GAME-0005`: `1 / 16 = 0.062500`.
  - `GAME-0006`: `1 / 18 = 0.055556`.
  - `GAME-0007`: `1 / 17 = 0.058824`.
  - `GAME-0008`: `1 / 16 = 0.062500`.
  - `GAME-0009`: `1 / 25 = 0.040000`.
  - `GAME-0010`: `1 / 18 = 0.055556`.
  - `GAME-0011`: `1 / 22 = 0.045455`.
  - `GAME-0012`: `1 / 18 = 0.055556`.
  - `GAME-0013`: `1 / 22 = 0.045455`.
  - `GAME-0014`: `1 / 24 = 0.041667`.
  - `GAME-0015`: `2 / 22 = 0.090909`.
  - `GAME-0016`: `2 / 23 = 0.086957`.
  - `GAME-0017`: `0 / 23 = 0.000000`.
  - `GAME-0018`: `2 / 27 = 0.074074`.
  - `GAME-0019`: `1 / 19 = 0.052632`.
  - `GAME-0020`: `2 / 22 = 0.090909`.
  - `GAME-0021`: `2 / 17 = 0.117647`.
  - `GAME-0022`: `1 / 21 = 0.047619`.
  - `GAME-0023`: `0 / 20 = 0.000000`.
  - `GAME-0024`: `0 / 22 = 0.000000`.
  - `GAME-0025`: `1 / 20 = 0.050000`.
  - `GAME-0026`: `1 / 21 = 0.047619`.
  - `GAME-0027`: `1 / 21 = 0.047619`.
  - `GAME-0028`: `1 / 26 = 0.038462`.
  - `GAME-0029`: `1 / 21 = 0.047619`.
  - `GAME-0030`: `1 / 23 = 0.043478`.
  - `GAME-0031`: `1 / 20 = 0.050000`.
  - `GAME-0032`: `1 / 20 = 0.050000`.
  - `GAME-0033`: `1 / 22 = 0.045455`.
  - `GAME-0034`: `1 / 23 = 0.043478`.
  - `GAME-0035`: `1 / 27 = 0.037037`.
  - `GAME-0036`: `1 / 21 = 0.047619`.
  - `GAME-0037`: `1 / 18 = 0.055556`.
  - `GAME-0038`: `1 / 25 = 0.040000`.
  - `GAME-0039`: `1 / 18 = 0.055556`.
  - `GAME-0040`: `1 / 17 = 0.058824`.
  - `GAME-0041`: `1 / 20 = 0.050000`.
  - `GAME-0042`: `1 / 18 = 0.055556`.
  - `GAME-0043`: `1 / 23 = 0.043478`.
  - `GAME-0044`: `1 / 19 = 0.052632`.
  - `GAME-0045`: `1 / 23 = 0.043478`.
  - `GAME-0046`: `1 / 19 = 0.052632`.
  - `GAME-0047`: `1 / 23 = 0.043478`.
  - `GAME-0048`: `1 / 23 = 0.043478`.
  - `GAME-0049`: `1 / 18 = 0.055556`.
  - `GAME-0050`: `1 / 24 = 0.041667`.
  - `GAME-0051`: `3 / 23 = 0.130435`.
- Scan date: 2026-08-13.
- New genes: `ACT-069`, `SYS-093`, `SYS-094`, `CON-099`, `INF-028`, `OBJ-033`,
  `TIM-011`.
- Reused genes: `ACT-068`, `INF-001`, `OBJ-002`.
- Classification result: `New gene` and a new verified combination; no novelty
  claim.

## Combination record

- `COMB-0052` captures weighted road requirements, persistent graph editing,
  automatic traffic, functional reachability and repeatable bounded evaluation.
- Exhaustive supporter scan: only `GAME-0052` contains the complete proper subset.

## Taxonomy impact

- Generalised `ACT-068` from tile-based roads to spatial road graphs while
  retaining tile / freehand geometry and edit timing as parameters. No prior
  signature or classification changes.
- Added seven separately observable action, system, constraint, information,
  objective and time records. No merge, split, lifecycle or type change.

## Negative results

- The planned strict build-then-simulate classification is rejected: current
  evidence shows cars after connections, a later bounded full-day evaluation
  and post-result revision rather than one permanently locked run.
- `CON-047`, `TIM-003`, `TIM-006` and `TIM-009` fail the bounded current scope.
  This correction is preserved here rather than promoted to a separate
  negative-result file because it rejects only the unit's provisional scope.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] `Network Complete` requires every declared
  directed pair, after which the retained graph can be evaluated and revised.
- [Confirmed | Direct | High] Current desktop Freeways includes Undo; original
  no-undo reviews describe a superseded release boundary.

## Нові гени

- `ACT-069`, `SYS-093`, `SYS-094`, `CON-099`, `INF-028`, `OBJ-033`, `TIM-011`.

## Нові комбінації

- `COMB-0052` — weighted interchange design under repeatable traffic evaluation.

## Зміни таксономії

- [Observation | Corroborated | High] `ACT-068` now admits tile and continuous
  spatial road geometry as parameters; existing signatures are unchanged.

## Нові питання

- Which traffic-design game independently repeats weighted declared demand and
  repeatable bounded evaluation without inheriting Freeways directly?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] `GAME-0053` — Can of Wormholes.

## Чому саме вона

- It leaves road networks after two adjacent transport games and tests a
  retained high-information recursive-body candidate under a bounded chapter.
