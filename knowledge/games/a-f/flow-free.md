---
game_id: GAME-0012
slug: flow-free
game_title: Flow Free
analysis_status: reviewed
reviewed: 2026-08-11
combination_ids:
  - COMB-0012
  - COMB-0039
gene_ids:
  action:
    - ACT-016
  system:
    - SYS-016
  constraint:
    - CON-001
    - CON-028
    - CON-029
    - CON-030
  information:
    - INF-001
  objective:
    - OBJ-006
  time:
    - TIM-002
---

# Game: Flow Free

## Analysis scope

- Version / ruleset: the classic square-grid Flow Free Free Play rules published
  by Big Duck Games, using ordinary cells without Bridges, Warps, hexagons or
  other variant topology.
- Included: fixed pairs of coloured dots; dragging a pipe from either dot;
  orthogonal cell-by-cell paths; matching-colour endpoints; non-crossing and
  non-overlap; pipes breaking on conflict; completion only when every pair is
  connected and the entire board is covered.
- Excluded: Time Trial, move-efficiency stars, hints, reset and menu commands,
  Daily Puzzles, pack progression, achievements, ads, purchases, labels as an
  accessibility presentation option and all non-classic level packs.
- Direct-play status: not conducted. Input semantics are corroborated by a
  contemporary gameplay reference; the final-state model is supported by the
  developer's rules and peer-reviewed Zig-Zag Numberlink literature.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FLO-001` | A classic puzzle exposes fixed pairs of matching coloured endpoints on a finite square grid | Confirmed | Corroborated | High | D1, D2, S1 |
| `FLO-002` | The player draws a pipe by dragging from either endpoint through grid squares to its matching endpoint | Confirmed | Corroborated | High | D2, S1 |
| `FLO-003` | Every pair must be connected to solve the puzzle | Confirmed | Direct | High | D1, D2 |
| `FLO-004` | Connecting every pair is insufficient unless the paths also cover the entire board | Confirmed | Direct | High | D1, D2, A1 |
| `FLO-005` | Pipes cannot coexist where they cross or overlap; a conflicting pipe breaks | Confirmed | Direct | High | D1, D2 |
| `FLO-006` | The formal solution is a set of vertex-disjoint simple paired paths whose union covers the grid | Confirmed | Corroborated | High | A1 |
| `FLO-007` | Free Play is self-paced, whereas Time Trial is a separate excluded mode | Confirmed | Direct | High | D1, D2 |
| `FLO-008` | The scoped level contains no random in-play state transition | Observation | Corroborated | High | FLO-001–FLO-007 |
| `FLO-009` | One drag expresses an ordered route rather than independent symbol assignments to unrelated cells | Observation | Corroborated | High | FLO-002, S1 |
| `FLO-010` | Bridge crossings belong to a distinct variant and are outside the classic non-overlap boundary | Confirmed | Direct | High | D3 |
| `FLO-011` | Conflict-triggered pipe breaking is a System Behaviour, while route tracing remains an Action | Observation | Corroborated | Medium | FLO-002, FLO-005 |
| `FLO-012` | Existing six gene types represent the classic rules without a taxonomy change | Observation | Corroborated | Medium | FLO-001–FLO-011 |

## Basic data

- Release / origin: developed and published by Big Duck Games; the iOS release
  dates to 2012. This record treats current classic Free Play rules as the
  canonical product scope rather than preserving one historical build.
- Platform or physical form: digital touch puzzle on mobile platforms.
- Puzzle family: Zig-Zag Numberlink / disjoint covering-path puzzle.
- Primary developer sources:
  - **[D1]** [Big Duck Games — Flow Free](https://www.bigduckgames.com/flowfree),
    requiring matching-colour pipes, all pairs, full-board coverage and warning
    that crossing or overlap breaks pipes.
  - **[D2]** [official Google Play listing](https://play.google.com/store/apps/details?id=com.bigduckgames.flow),
    corroborating the rules and separating Free Play from Time Trial.
  - **[D3]** [Big Duck Games — Flow Free: Bridges](https://www.bigduckgames.com/bridges),
    explicitly presenting bridge crossings as a different game variant.
- Input corroboration:
  - **[S1]** [StrategyWiki gameplay reference](https://strategywiki.org/wiki/Flow_Free/Walkthrough),
    documenting finger-drag input from either dot and path construction through
    touched grid squares.
- Academic source:
  - **[A1]** Adcock et al.,
    [“Zig-Zag Numberlink is NP-Complete”](https://doi.org/10.2197/ipsjjip.23.239),
    formalising the Flow Free-style problem as paired vertex-disjoint paths
    covering every vertex of a rectangular grid. Its general complexity result
    does not measure each curated app level.
- Claim IDs: `FLO-001`–`FLO-012`.

## Mechanical decomposition

### Action Genes

- `ACT-016` — trace a path from a fixed endpoint. The player begins at either
  coloured dot and drags an ordered route across successive grid cells toward
  its matching dot.
- The drag is one variable-length compound action. Treating every crossed cell
  as an independent `ACT-007` assignment would lose continuity, origin and
  ordering, which are selected together by the gesture.
- Reset, hint, pack selection and accessibility labels are excluded interface
  or meta commands.
- Claim IDs: `FLO-002`, `FLO-009`.

### System Behaviour Genes

- `SYS-016` — overlap-triggered path break. When an active pipe conflicts by
  crossing or overlapping another pipe, the rules break the conflict rather
  than preserving two routes through one cell.
- The system does not choose a path, propagate flow through empty cells or
  generate a successor state randomly.
- Exact visual trimming and animation are implementation parameters; the gene
  boundary is the automatic invalidation caused by route conflict.
- Claim IDs: `FLO-005`, `FLO-008`, `FLO-011`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. Every cell remains an individually
  addressed position on one fixed rectangular board.
- `CON-028` — fixed paired-endpoint identity. Each colour has exactly two
  immutable terminals, and its path must join those matching endpoints.
- `CON-029` — orthogonally contiguous simple path. A pipe is one unbranched
  sequence of distinct edge-adjacent cells; diagonals and disconnected pieces
  are invalid.
- `CON-030` — exclusive path-cell occupancy. Distinct completed pipes cannot
  share or cross in a classic cell.
- `CON-018` is absent: Flow Free does not constrain row and column run-length
  descriptions. Its orthogonality belongs to path adjacency, not coupled clue
  satisfaction.
- Board size, pair count, endpoint placement, route length and turn count are
  parameters rather than additional genes.
- Claim IDs: `FLO-001`, `FLO-003`–`FLO-006`, `FLO-010`.

### Information Genes

- `INF-001` — fully visible current state. All endpoints, current pipe cells,
  open cells and conflicts are visible before and during path tracing.
- A difficult future routing is not concealed information: it is a consequence
  of visible geometry and the player's unresolved choices.
- Colour-blind labels change the encoding channel but not which endpoint
  identities are disclosed.
- Claim IDs: `FLO-001`, `FLO-008`.

### Objective Genes

- `OBJ-006` — complete constraint-satisfying assignment. Every board cell must
  belong to exactly one path, all matching endpoint pairs must be connected,
  and all path constraints must hold simultaneously.
- Merely connecting every pair by short routes does not complete a board with
  gaps. Conversely, filling cells cannot compensate for an unconnected pair.
- Fewest moves and shortest path length are excluded evaluation layers, not the
  scoped completion objective.
- Claim IDs: `FLO-003`, `FLO-004`, `FLO-006`.

### Time Genes

- `TIM-002` — self-paced sequential action. Free Play has no forced clock or
  time-driven board change; the player may pause between route gestures.
- Cells sampled during one continuous drag are internal action granularity,
  not automatic turns. Conflict breaking occurs as a consequence of that
  trace without introducing real-time progression.
- Time Trial would require a separate scoped decomposition and is excluded.
- Claim IDs: `FLO-002`, `FLO-007`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Two red dots with an open orthogonal route | Drag from one red dot through adjacent cells to the other | One connected red pipe occupies the traced cells | Endpoint identity and ordered tracing | `FLO-002`, `FLO-003` |
| Active red trace enters a cell occupied by blue pipe | Continue the red drag into that cell | A conflicting pipe breaks; two pipes do not persist in the cell | System response and exclusive occupancy | `FLO-005` |
| Every colour pair is connected but one cell remains empty | Finish the final pair | Level remains incomplete | Full-board coverage is conjunctive | `FLO-004` |
| Every cell is occupied but one colour has two disconnected partial routes | End the trace | Level remains incomplete | Coverage cannot replace pairing and continuity | `FLO-003`, `FLO-006` |
| A proposed route would use diagonal-only contact | Trace toward the diagonal cell | It does not form the required adjacent path step | Orthogonal adjacency | `FLO-006` |
| Every pair is connected and every cell belongs to exactly one pipe | Complete the last route | Level completes | Full constraint-satisfying assignment | `FLO-003`, `FLO-004` |

## Strategic and experiential structure

- Local decision: choose the next orthogonal cell while preserving an open
  continuation to the matching endpoint.
- Medium-term planning: route constrained pairs around corners and edges while
  reserving corridors for other colours.
- Long-term structure: partition the entire grid into disjoint paths without
  isolating an empty pocket or separating a terminal pair.
- Common heuristics: start with endpoints having few exits; inspect narrow
  corridors; avoid closing regions with an odd or unreachable remainder; delay
  flexible short pairs until longer routes define the remaining space.
- Failure attribution: a locally valid connection can block another pair or
  leave uncovered cells. Because routes can be redrawn and conflicts break
  visibly, failure follows from routing choices rather than randomness.
- Player-trust factors: endpoint identity, occupied cells and completion
  requirements are public; accessibility labels should preserve identity when
  colour alone is insufficient.
- Claim IDs: `FLO-001`–`FLO-009`.

## Replay and variation

- What changes between instances: board dimensions, number of colour pairs,
  endpoint placement and required path geometry.
- Randomness or procedural generation: none during a scoped curated level.
- Multiple viable strategies: construction order and intermediate paths may
  differ; a level may admit more than one complete covering.
- Typical replay motive: repair a blocked route, find a cleaner gesture
  sequence or solve a different endpoint layout.
- Claim IDs: `FLO-001`, `FLO-007`, `FLO-008`.

## Adjacent systems and history

- The peer-reviewed Zig-Zag Numberlink formulation matches the final-state
  requirement: paired vertex-disjoint paths cover the entire grid.
- Classical Numberlink variants may optimise turns or omit full coverage; those
  rule changes alter the objective or constraints and need separate scopes.
- Flow Free: Bridges explicitly permits two pipes to cross at special bridge
  cells, violating classic `CON-030` at declared positions.
- Pipe Mania places or rotates pipe pieces to conduct a time-driven flow. It
  does not ask the player to trace several paired covering paths and is kept as
  a separate backlog subject.
- Complexity caveat: NP-completeness describes scalable general instances and
  does not prove that every curated Flow Free level is difficult.
- Claim IDs: `FLO-006`, `FLO-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-016` | drag sampling, backtracking and route resumption |
| System Behaviour | `SYS-016` | exact conflicting-pipe trimming |
| Constraint | `CON-001`, `CON-028`, `CON-029`, `CON-030` | board size, pair count and endpoint layout |
| Information | `INF-001` | colour plus optional identity labels |
| Objective | `OBJ-006` | full coverage and pair count |
| Time | `TIM-002` | gesture as one compound action |

Canonical signature:

`ACT-016; SYS-016; CON-001,CON-028,CON-029,CON-030; INF-001; OBJ-006; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `11` (`GAME-0001`–`GAME-0011`).
- Exact genome matches: none.
- Tied near matches: `GAME-0005` — Sudoku (`4 / 12 = 0.333333`); `GAME-0008` — Nonogram (`4 / 12 = 0.333333`).
- Supported combination subsets: `COMB-0012`, `COMB-0039`.
- Scan date: 2026-08-11.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0005` — Sudoku | `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | Both complete visible fixed-grid assignments; Sudoku selects independent symbols under all-different units, while Flow Free traces ordered paths under global spatial routing | Near, `0.333333` |
| `GAME-0008` — Nonogram | `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | Both cover a visible grid under orthogonally coupled constraints; Nonogram satisfies disclosed run sequences, while Flow Free creates paired disjoint paths with no clue layer | Near, `0.333333` |

### Preserved research notes

- New combination: `COMB-0012`, whose six genes are a proper subset of this
  nine-gene genome.
- Later corpus update: `COMB-0039` records the five-gene visible self-paced
  simple-path constraint-completion core shared with The Witness.
- New genes: `ACT-016`, `SYS-016`, `CON-028`, `CON-029`, `CON-030`.
- Classification result: `New gene`.
- Reused genes: `CON-001`, `INF-001`, `OBJ-006`, `TIM-002`.
- Evidence and reasoning: path tracing is one ordered compound Action; overlap
  breaking is an automatic response; complete coverage reuses the existing
  general assignment objective rather than multiplying objective synonyms.

## Taxonomy impact

- Registry changes: five bounded genes added and four reused.
- Taxonomy-change record: none. Compound drag, automatic conflict response,
  path constraints and completion each fit an existing type boundary.
- Candidate terms affected: connect, path tracing, conflict breaking, paired
  endpoints, path continuity, exclusive path occupancy and complete routes now
  have bounded mappings.
- Board dimensions, pair count, path lengths and endpoint positions remain
  parameters.
- Claim IDs: `FLO-011`, `FLO-012`.

## Negative results

Flow Free does not reuse `ACT-007`: route order and continuity make a drag more
than independent cell assignment. It does not reuse `CON-018`, because rows and
columns carry no ordered clues. Bridge crossings are absent from the classic
scope, and move efficiency is not a completion Objective.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] A solution requires both all paired connections
  and full-board coverage (`FLO-003`, `FLO-004`).
- [Confirmed | Corroborated | High] The final state is a vertex-disjoint path
  cover, not merely a set of non-crossing lines (`FLO-006`).
- [Observation | Corroborated | High] Dragging selects one ordered compound
  path rather than unrelated cell values (`FLO-009`).

## Нові гени

- [Observation | Corroborated | High] `ACT-016`, `SYS-016`, `CON-028`,
  `CON-029` and `CON-030`.
- [Observation | Corroborated | High] `CON-001`, `INF-001`, `OBJ-006` and
  `TIM-002` are reused.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0012` — paired disjoint paths
  covering a fixed grid.
- [Observation | Corroborated | High] `COMB-0039` was added later as the
  recurring simple-path constraint-completion core with The Witness.

## Зміни таксономії

- [Observation | Corroborated | Medium] Змін таксономії немає. Continuous
  touch input remains an Action parameter rather than a new Time type.

## Нові питання

- TODO: compare Flow Free: Bridges to test whether declared crossing cells
  parameterise or partially replace `CON-030`.
- TODO: test a path puzzle that connects pairs without covering every cell to
  isolate the contribution of `OBJ-006`.
- TODO: verify exact rerouting and pipe-trimming behaviour through direct play
  before narrowing `SYS-016` beyond conflict-triggered breakage.

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] `GAME-0013` — Baba Is You.
- Optimisation criterion: maximise mechanical distance and test dynamic rule
  mutation before the 14-game registry checkpoint.
- Expected information gain: distinguish rule-word movement, automatic rule
  parsing, mutable object properties, controllability reassignment and
  condition-defined objectives.
- Backlog impact: Baba Is You moves from the coverage pool to the immediate
  task; Flow Free leaves the pool after completion.

## Чому саме вона

- [Hypothesis | Limited | Medium] Baba Is You introduces rules as manipulable
  board state, a boundary not exercised by any current game, while avoiding a
  second consecutive connection / pipe system.
