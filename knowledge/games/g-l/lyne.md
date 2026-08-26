---
game_id: GAME-0061
slug: lyne
game_title: LYNE
analysis_status: reviewed
reviewed: 2026-08-13
combination_ids:
  - COMB-0012
  - COMB-0039
  - COMB-0061
gene_ids:
  action:
    - ACT-016
  system: []
  constraint:
    - CON-001
    - CON-028
    - CON-029
    - CON-030
    - CON-107
    - CON-108
  information:
    - INF-001
  objective:
    - OBJ-006
  time:
    - TIM-002
---

# Game: LYNE

## Analysis scope

- Version / ruleset: Thomas Bowker's released LYNE, restricted to the complete
  authored set A, puzzles `A-01`–`A-25`, as represented by the current
  tenth-anniversary build and its updated solution set.
- Included: one fixed finite arrangement of shape positions; two route families
  in set A; two hollow fixed endpoints per family; every solid same-family
  waypoint; direct route tracing through successively adjacent positions;
  horizontal, vertical and diagonal links; ordinary-position exclusivity;
  neutral nexus nodes with an exact visible traversal count; completion only
  when every family is connected through all of its markers and every nexus
  capacity is filled; partial route retraction and consequence-free retries in
  the player's own time.
- Excluded: set B onward and its third route family; later authored layouts and
  all Daily procedurally generated puzzles; set unlocking, Trytes, palettes,
  achievements, sound, presentation, platform gestures and speedrunning.
- Direct-play status: not conducted. The creator's product pages establish the
  connect-shapes / fill-board objective and authored-plus-Daily structure. The
  versioned 650-image solution guide provides a reproducible `A-01`–`A-25`
  boundary and shows the first set's two families, diagonal links and exact-two
  nexus nodes before set B adds a third family. Four contemporary hands-on
  reviews independently corroborate route tracing, typed waypoint inclusion,
  non-crossing ordinary positions, counted nexus sharing, local retraction and
  self-paced play.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `LYN-001` | Set A is one complete 25-puzzle authored set and set B begins after `A-25` | Confirmed | Direct | High | P2, S1, S3, S6 |
| `LYN-002` | Every scoped puzzle exposes its complete fixed arrangement, endpoints, typed markers, nexus counts and current paths | Confirmed | Corroborated | High | S1-S5 |
| `LYN-003` | One route is directly dragged from one hollow fixed endpoint toward the other endpoint of the same family | Confirmed | Corroborated | High | S2-S5 |
| `LYN-004` | A valid family route must visit every solid marker carrying that family's shape and cannot substitute another family | Confirmed | Corroborated | High | S2-S5 |
| `LYN-005` | Set A permits horizontal, vertical and diagonal adjacency between displayed positions | Confirmed | Direct | High | S1, S3, S5 |
| `LYN-006` | A route remains one unbranched non-self-crossing ordered path and ordinary positions cannot be shared by routes | Confirmed | Corroborated | High | S2-S5 |
| `LYN-007` | A neutral nexus is an explicit exception that admits several route passages | Confirmed | Corroborated | High | S2-S5 |
| `LYN-008` | Visible pips on a nexus are an exact required traversal count, not merely optional capacity | Confirmed | Corroborated | High | S2-S5 |
| `LYN-009` | Completion requires every shape family and every required nexus passage to be satisfied together | Confirmed | Direct | High | P1, P2, S2-S5 |
| `LYN-010` | A drawn route can be locally backed up or cleared without advancing a time-driven system | Confirmed | Corroborated | High | S2, S4, S5 |
| `LYN-011` | The scoped authored puzzles are deterministic and impose no game clock or score target | Observation | Corroborated | High | P1, P2, S2, S4 |
| `LYN-012` | Set B introduces a third route family and therefore lies beyond the selected two-family teaching boundary | Confirmed | Direct | High | S1, S6 |

## Basic data

- Release / origin: designed and published by Thomas Bowker; first released in
  early 2014, with the Steam version released on 17 March 2014 and a tenth-
  anniversary update published in 2024.
- Platform or physical form: deterministic single-player digital line-drawing
  puzzle for mouse and touch input.
- Puzzle family: typed waypoint paths with counted shared junctions.
- Primary creator sources:
  - **[P1]** [LYNE official site](https://lynegame.com/), for creator identity
    and the canonical “Connect the shapes / Fill the board” objective.
  - **[P2]** [LYNE on Steam](https://store.steampowered.com/app/266010/), for
    developer, release date, single-player product boundary, hundreds of
    authored puzzles and distinct procedurally generated Daily supply.
- Reproducible solution evidence:
  - **[S1]** [Jepp — LYNE Picture Walkthrough](https://steamcommunity.com/sharedfiles/filedetails/?id=263776595),
    a versioned complete guide whose current images enumerate `A-01`–`A-25`,
    show the set A mechanic progression and begin set B with a third family.
- Contemporary and specialised corroboration:
  - **[S2]** [Pocket Gamer review](https://www.pocketgamer.com/lyne/review/),
    for drag-to-connect families, 25-level sets and counted nexus sharing.
  - **[S3]** [Gamezebo review](https://www.gamezebo.com/reviews/lyne-review/),
    for paired paths, diagonal links, mandatory typed markers, non-crossing,
    route retraction and 25-level sets.
  - **[S4]** [iDownloadBlog review](https://www.idownloadblog.com/2014/01/09/lyne-review/),
    for endpoint families, ordinary non-crossing, exact nexus pips, set
    progression and Daily separation.
  - **[S5]** [Thinky Games entry](https://thinkygames.com/games/lyne/), for
    hollow endpoints, inclusion of every same-family marker and exact-count
    octagonal nexus nodes.
  - **[S6]** [MobyGames screenshot catalogue](https://www.mobygames.com/game/64654/lyne/screenshots/),
    for the documented transition from set A to set B and the third shape /
    colour family first introduced there.
- Claim IDs: `LYN-001`–`LYN-012`.

## Mechanical decomposition

### Action Genes

- `ACT-016` — trace a path from a fixed endpoint. A drag begins on one hollow
  terminal, successively claims adjacent displayed positions and aims at the
  other hollow terminal of the same family.
- Diagonal segments do not require a new action: adjacency topology is a
  parameter of the same ordered compound trace used by Flow Free and The
  Witness.
- Tapping or dragging backward only edits the current trace and remains inside
  this route-authoring action rather than becoming a separate deletion gene.
- Claim IDs: `LYN-003`, `LYN-005`, `LYN-010`.

### System Behaviour Genes

- None. The scoped rules continuously expose route validity but do not require
  a distinct automatic transformation, agent step or random successor.
- Flow Free's `SYS-016` is rejected: LYNE's ordinary crossing restriction and
  editable trace do not establish that the system breaks a different retained
  pipe under the same conflict policy.
- Claim IDs: `LYN-006`, `LYN-010`, `LYN-011`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. Every authored marker is a persistent
  addressed position in one finite relation graph.
- `CON-028` — fixed paired-endpoint identity. The two hollow markers of each
  shape family are its immutable route terminals.
- `CON-029` — topology-contiguous simple path. Each family creates one
  unbranched path through distinct successively adjacent positions; set A's
  declared topology includes horizontal, vertical and diagonal links.
- `CON-030` — exclusive ordinary path-position occupancy. Ordinary typed
  positions cannot carry two routes; only declared neutral nexus nodes are
  exceptions.
- `CON-107` — exact shared-junction traversal capacity. Every nexus pip must be
  consumed by one passage, and a nexus is incomplete below or above that exact
  count.
- `CON-108` — typed waypoint inclusion on matched path. Every solid triangle
  belongs to the triangle path and every solid diamond to the diamond path.
- Board geometry, family colours, waypoint counts and nexus placement are
  parameters rather than further genes.
- Claim IDs: `LYN-002`, `LYN-004`–`LYN-008`, `LYN-012`.

### Information Genes

- `INF-001` — fully visible current state. Endpoints, every typed marker, every
  nexus count, current segments and unused positions are visible before each
  route decision.
- A route becoming impossible after a poor partition is deduction from public
  geometry, not hidden state.
- Claim IDs: `LYN-002`, `LYN-011`.

### Objective Genes

- `OBJ-006` — complete constraint-satisfying assignment. All family paths must
  simultaneously connect their endpoints, include all typed waypoints, obey
  ordinary exclusivity and satisfy every nexus traversal count.
- “Fill the board” means exhaust the complete declared marker-and-nexus answer
  set; it does not require painting unmarked background pixels.
- Shortest routes, fewest redraws and completion speed are excluded evaluation
  layers rather than functional completion requirements.
- Claim IDs: `LYN-004`, `LYN-008`, `LYN-009`.

### Time Genes

- `TIM-002` — self-paced sequential action. The player can pause, extend one
  route, retract it and work on another without any clock-driven state change.
- Touch sampling during a drag is internal gesture granularity, not a forced
  real-time system.
- Claim IDs: `LYN-010`, `LYN-011`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Two hollow triangles with one solid triangle between them | Drag from one hollow triangle through the solid triangle to the other hollow triangle | One complete triangle path occupies all three markers | Fixed pairing and typed waypoint inclusion | `LYN-003`, `LYN-004` |
| Two markers lie diagonally adjacent in the authored graph | Continue the active path diagonally between them | The diagonal segment is accepted as one adjacent step | Declared non-orthogonal topology | `LYN-005` |
| A triangle route attempts to claim an ordinary diamond marker | Continue the triangle trace onto the diamond | The state does not satisfy the typed route | Family-exclusive waypoint identity | `LYN-004` |
| An ordinary position already belongs to the diamond path | Trace the triangle route through that position | Two routes cannot remain there | Ordinary-position exclusivity | `LYN-006` |
| One neutral nexus shows two pips | Route triangle and diamond paths through it once each | Both pips are filled and the declared shared node is satisfied | Exact shared-junction capacity | `LYN-007`, `LYN-008` |
| All endpoint pairs are joined but one same-family waypoint or nexus pip is unused | End the final trace | Puzzle remains incomplete | Conjunctive complete assignment | `LYN-009` |
| Every typed marker and exact nexus passage belongs to a valid family path | Complete the last missing segment | Puzzle completes | Full functional objective | `LYN-009` |
| A partial path blocks the remaining family | Tap or drag back to an earlier position | The suffix retracts while the authored puzzle remains available | Local revisability without time pressure | `LYN-010`, `LYN-011` |

## Strategic and experiential structure

- Local decision: choose the next visible adjacent position while preserving a
  non-self-crossing continuation to the matching hollow endpoint.
- Medium-term planning: order every typed waypoint and reserve ordinary
  positions for the other family while allocating required nexus passages.
- Long-term structure: partition all required positions into two simple family
  paths whose declared intersections occur only at exactly filled nexus nodes.
- Common heuristics: start from constrained endpoints; identify markers with
  few legal neighbours; treat nexus pips as mandatory shared resources; test
  diagonal shortcuts without sealing the other family; retract only to the
  earliest wrong branch.
- Failure attribution: a locally legal segment may strand a later waypoint,
  consume a critical nexus entry or separate the other endpoint pair. Since all
  geometry is visible and revision is consequence-free, failure is attributable
  to routing choices rather than randomness.
- Claim IDs: `LYN-002`–`LYN-011`.

## Replay and variation

- What changes between scoped instances: marker positions, family waypoint
  counts, endpoint placement, allowed adjacency geometry, nexus count and
  required routing order.
- Randomness or procedural generation: none during one scoped authored set A
  puzzle. Daily procedural puzzles are explicitly excluded.
- Multiple viable strategies: route construction order and temporary traces
  can differ; the evidence does not claim every authored puzzle has a unique
  final path set.
- Typical replay motive: revise a blocked partition or solve another authored
  set A graph.
- Claim IDs: `LYN-001`, `LYN-010`–`LYN-012`.

## Adjacent systems and history

- Flow Free is the closest corpus control: both draw matched simple paths over
  fixed visible positions, but Flow Free requires orthogonal full-cell coverage
  and forbids all classic cell sharing, whereas LYNE permits diagonal adjacency,
  requires typed intermediate markers and declares exact-capacity shared nexus
  exceptions.
- Numberlink-style full rectangular occupancy is therefore not copied as a
  hidden assumption. LYNE's answer domain is the displayed marker graph.
- The Witness shares fixed-origin tracing and global constraint completion but
  uses one path to partition clue regions rather than several typed paired paths.
- Daily generation affects instance supply, not in-play transition randomness,
  and remains outside the selected authored set.
- Claim IDs: `LYN-001`–`LYN-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-016` | mouse / touch sampling and partial retraction |
| System Behaviour | none | completion animation and invalid-trace feedback |
| Constraint | `CON-001`, `CON-028`, `CON-029`, `CON-030`, `CON-107`, `CON-108` | graph geometry, two families, nexus count and diagonal availability |
| Information | `INF-001` | colours, shapes, endpoint outlines and nexus pips |
| Objective | `OBJ-006` | required marker set and accepted completion timing |
| Time | `TIM-002` | trace granularity and pause duration |

Canonical signature:

`ACT-016; none; CON-001,CON-028,CON-029,CON-030,CON-107,CON-108; INF-001; OBJ-006; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `60` (`GAME-0001`–`GAME-0060`).
- Exact genome matches: none.
- Tied near matches: `GAME-0012` — Flow Free (`8 / 11 = 0.727273`).
- Supported combination subsets: `COMB-0012`, `COMB-0039`, `COMB-0061`.
- Scan date: 2026-08-13.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0012` — Flow Free | `ACT-016`, `CON-001`, `CON-028`, `CON-029`, `CON-030`, `INF-001`, `OBJ-006`, `TIM-002` | Flow Free covers every rectangular cell by orthogonal mutually disjoint pipes; LYNE covers typed markers over diagonal-capable adjacency and permits only exact-count nexus sharing | Near, `0.727273` |

### Preserved research notes

- New genes: `CON-107`, `CON-108`.
- Generalised genes: `CON-029` from orthogonal-only to declared adjacency
  topology; `CON-030` from universal route-position exclusivity to ordinary-
  position exclusivity with separately declared shared-junction exceptions.
- Classification result: two new constraint genes, one new verified
  combination and two recurring existing combination supports.
- Evidence and reasoning: exact nexus multiplicity and mandatory typed waypoint
  inclusion change route feasibility independently of path adjacency, pairing
  and ordinary exclusivity.

## Taxonomy impact

- Registry changes: add `CON-107` and `CON-108`; generalise `CON-029` and
  `CON-030` representation-neutrally while preserving all earlier signatures.
- Taxonomy-change record: none. The prior Flow Free / Cosmic Express / Witness
  instances remain strict orthogonal and no-exception parameter cases.
- Candidate terms affected: topology path tracing, diagonal simple paths,
  shared counted junctions and typed mandatory waypoints.
- Claim IDs: `LYN-004`–`LYN-009`.

## Negative results

- `SYS-016` rejected: the evidence does not establish Flow Free's specific
  overlap-triggered breaking of another retained pipe.
- `CON-029` retained rather than split: orthogonal versus diagonal adjacency is
  an authored topology parameter of the same unbranched simple-path invariant.
- `CON-030` retained rather than rejected: ordinary positions remain exclusive;
  only visible nexus nodes provide a typed exception governed by `CON-107`.
- `OBJ-006` retained: “fill the board” is a complete declared assignment over
  all markers and nexus capacities, not a separate score or shortest-path goal.
- Daily procedural supply is excluded and therefore creates neither an
  information gene nor in-play randomness.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Set A is a complete 25-puzzle teaching module
  with two families, diagonal adjacency and exact-count nexus nodes; set B adds
  the third family (`LYN-001`–`LYN-012`).

## Нові гени

- [Observation | Corroborated | High] `CON-107` — exact shared-junction
  traversal capacity.
- [Observation | Direct | High] `CON-108` — typed waypoint inclusion on the
  matching endpoint path.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0061` — typed paired paths through
  exact-capacity shared junctions.
- [Strong Pattern | Corroborated | High] LYNE also supports recurring
  `COMB-0012` and `COMB-0039`.

## Зміни таксономії

- [Observation | Corroborated | High] `CON-029` now names topology-contiguous
  rather than orthogonal-only simple paths; `CON-030` explicitly permits
  separately declared shared-junction exceptions.

## Нові питання

- Does a later LYNE layout require one route to traverse the same nexus more
  than once, or are visible pips normally distributed across route families?
- Does the third family introduced in set B change only instance parameters or
  produce qualitatively new congestion structures worth a separate scope?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] Hexologic.
- Optimisation criterion: move from traced path constraints to local arithmetic
  constraints over a hexagonal adjacency graph while retaining complete visible
  assignment as the control.
- Expected information gain: test whether existing neighbour-count and exact-
  assignment genes cover binary cell sums or require a bounded arithmetic clue
  distinction.
- Backlog impact: retain later LYNE sets and Daily generation as optional
  expansions rather than blending them into set A.

## Чому саме вона

- [Hypothesis | Corroborated | High] Hexologic is mechanically distant from
  LYNE's route construction yet keeps a fully visible finite constraint field,
  giving the next unit a clean recurrence-versus-new-boundary test.
