---
game_id: GAME-0039
slug: the-witness
game_title: The Witness
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0039
gene_ids:
  action:
    - ACT-016
  system:
    - SYS-073
  constraint:
    - CON-001
    - CON-029
    - CON-087
  information:
    - INF-001
    - INF-023
  objective:
    - OBJ-006
  time:
    - TIM-002
---

# Game: The Witness

## Analysis scope

- Version / ruleset: Thekla's 2016 base game, scoped to one foundational
  authored panel with one visible start circle, one end cap and only black /
  white square clues.
- Included: initiating and tracing one line; orthogonal grid-graph adjacency;
  retracting the current trace before submission; no branching, revisiting or
  self-intersection; endpoint submission; path-induced cell regions; separation
  of square-clue colours; conjunctive validation; violated-clue feedback; valid
  panel persistence / activation; self-paced retry.
- Excluded: free island traversal, environmental lines, broken edges, hexagon
  dots, audio, symmetry, suns / stars, polyominoes, triangles, erasers,
  generated challenge panels, timed doors, obelisks, lasers, endings, secrets
  and platform presentation.
- Direct-play status: not conducted. The official PlayStation page establishes
  the authored-puzzle corpus; creator Jonathan Blow directly describes drawing
  a line to separate black and white spots. A peer-reviewed formal study defines
  the start-to-destination simple path and monochromatic regions, while
  contemporary TIME and Ars Technica reviews corroborate tracing,
  self-noncrossing and panel progression. Thinky Games supplies the bounded
  post-submit red-blink feedback detail.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `WIT-001` | The scoped panel is a fixed finite rectangular grid graph with visible start circle, end cap and black / white square clues | Confirmed | Corroborated | High | P1, P3, S1–S3 |
| `WIT-002` | The player begins at the start circle and traces one contiguous line along adjacent grid edges toward the end cap | Confirmed | Direct | High | P2, P3, S1 |
| `WIT-003` | The candidate line is a simple path: it does not branch, revisit a vertex or cross itself | Confirmed | Corroborated | High | P3, S1, S2 |
| `WIT-004` | Before committing at the end cap, the active line can be retracted along its current route and redirected | Confirmed | Corroborated | High | S1, S3 |
| `WIT-005` | The completed path acts as barriers that partition panel cells into connected regions | Confirmed | Corroborated | High | P2, P3 |
| `WIT-006` | Every resulting region may contain square clues of only one colour; black and white squares cannot share a region | Confirmed | Direct | High | P2, P3, S2 |
| `WIT-007` | Blank cells need not be visited or assigned a colour, and the trace need not cover every grid cell or edge | Confirmed | Corroborated | High | P3, WIT-002–WIT-006 |
| `WIT-008` | Reaching the end cap submits the complete path for conjunctive topology-and-clue validation | Confirmed | Corroborated | High | P3, S1, S3 |
| `WIT-009` | A valid submission remains lit and activates the linked panel progression; an invalid submission is rejected | Confirmed | Corroborated | High | S1, S3 |
| `WIT-010` | After an invalid clue-bearing submission, implicated symbols can blink red without exposing the corrected path | Confirmed | Corroborated | High | S3 |
| `WIT-011` | The panel has no forced clock or changing hidden state; the player may inspect and retry at their own pace | Observation | Corroborated | High | P1–P3, S1–S3 |
| `WIT-012` | Flow Free is structurally close but adds paired endpoint identities, multiple routes and whole-board coverage absent from this scope | Observation | Corroborated | High | WIT-001–WIT-011 |

## Basic data

- Release / origin: Thekla, Inc. released The Witness for PlayStation 4 and
  Windows in January 2016; Jonathan Blow directed its design.
- Platform or physical form: first-person island game containing authored
  two-dimensional line panels; this unit treats only the declared panel as the
  puzzle boundary.
- Puzzle family: simple-path region-partition constraint satisfaction.
- Primary, creator and formal sources:
  - **[P1]** [Official PlayStation product page](https://www.playstation.com/en-us/games/the-witness/),
    identifying the single-player open world and more than 500 authored puzzles.
  - **[P2]** [TIME interview with Jonathan Blow](https://time.com/4355763/the-witness-jonathan-blow-interview/),
    where the designer describes drawing a line that separates black and white
    spots and the panel grammar's deliberately untimed focus.
  - **[P3]** Abel et al., [“Who witnesses The Witness?”](https://arxiv.org/abs/1804.10193),
    formalising every panel as a simple start-to-destination path and square
    clues as constraints making path-induced regions partially monochromatic.
- Contemporary and specialist corroboration:
  - **[S1]** [TIME review, 25 January 2016](https://time.com/4191490/the-witness-review/),
    documenting line tracing, self-noncrossing and activation of nearby doors or
    following panels.
  - **[S2]** [Ars Technica review](https://arstechnica.com/gaming/2016/01/the-witness-review-an-island-where-knowledge-mystery-are-the-treasures/),
    corroborating black / white teaching panels and the non-overlap rule.
  - **[S3]** [Thinky Games catalogue analysis](https://thinkygames.com/games/the-witness/),
    documenting valid-panel progression and red blinking of unmet clue symbols
    after an invalid line.
- Claim IDs: `WIT-001`–`WIT-012`.

## Mechanical decomposition

### Action Genes

- `ACT-016` — trace path from fixed endpoint. The player selects the visible
  start circle and directly traces one variable-length ordered line through
  adjacent grid vertices toward the end cap as a compound gesture.
- Backtracking along the currently active line is a parameter of the same
  compound trace: it edits the unfinished suffix without creating a second
  independent route action.
- `ACT-008` is absent because island navigation is outside the panel scope.
- Claim IDs: `WIT-002`–`WIT-004`.

### System Behaviour Genes

- `SYS-073` — commit-time panel path validation. On end-cap submission the
  system jointly checks the start / end simple-path topology and every active
  square-region constraint. It retains and activates a valid line; an invalid
  one does not progress the panel.
- `SYS-016` is absent: there is no second path whose overlap automatically
  breaks. Self-revisit is prevented within the one active simple trace and
  belongs to `CON-029`.
- Resolution order: capture the final ordered path; confirm valid start and end;
  derive connected cell regions after treating path edges as barriers; inspect
  the square colours in each region; accept only if every region is
  monochromatic; otherwise reject and emit bounded clue feedback.
- Claim IDs: `WIT-003`, `WIT-005`, `WIT-006`, `WIT-008`–`WIT-010`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The panel exposes one finite immutable
  grid graph and fixed clue cells throughout the attempt.
- `CON-029` — orthogonally contiguous simple path. The line is one unbranched
  start-to-end sequence of distinct adjacent vertices with no self-crossing.
- `CON-087` — path-partitioned monochromatic clue regions. Path edges divide
  cells; no resulting connected region may contain square clues of two colours.
- `CON-028` is absent: the start and end have roles, not matching pair labels.
  `CON-030` is absent because only one path exists; it does not compete with
  another route for cells. Whole-board coverage is also absent.
- Scarce strategic resources: grid edges, turns, access to the unique end cap
  and the boundary segments needed to separate opposed clue colours without
  trapping the trace.
- Claim IDs: `WIT-001`–`WIT-007`, `WIT-012`.

### Information Genes

- `INF-001` — fully visible current state. Grid, start, end, square clues and
  every segment of the candidate line are inspectable; no random or concealed
  state changes during the panel attempt.
- `INF-023` — post-commit violated-clue indication. A rejected completed trace
  can blink implicated square clues red, locating a violated condition without
  drawing a valid replacement line.
- The rule is learned rather than textually stated, but once inferred the
  current instance data are fully visible; hidden instruction is not hidden
  board state.
- Claim IDs: `WIT-001`, `WIT-010`, `WIT-011`.

### Objective Genes

- `OBJ-006` — complete constraint-satisfying assignment. The traced answer
  implicitly assigns every panel edge as selected or unselected and succeeds
  only when the resulting finite path satisfies topology and every square clue.
- This generalises `OBJ-006` from explicit cell entries and whole-board routes
  to a complete traced answer object. It does not imply that every cell must be
  visited; completeness means every declared variable and constraint has a
  determined result.
- Fewest turns, shortest line and island-wide completion are excluded.
- Claim IDs: `WIT-005`–`WIT-009`.

### Time Genes

- `TIM-002` — self-paced sequential action. The player may inspect, trace,
  retract and retry without a forced clock or time-driven panel mutation.
- Cursor motion occurs continuously as an input gesture, but nothing advances
  independently while the player pauses; this is not `TIM-003`.
- Claim IDs: `WIT-004`, `WIT-008`, `WIT-011`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Empty panel with start and end | Select start and drag one edge | Ordered trace begins from the fixed start | fixed-endpoint compound action | `WIT-002` |
| Active trace has several segments | Drag backward along its suffix | Recent segments retract and a different continuation can be chosen | pre-commit revision parameter | `WIT-004` |
| Active trace would revisit one of its vertices | Drag toward that vertex | A branched or self-crossing completed path cannot be formed | simple-path boundary | `WIT-003` |
| Trace reaches end but leaves black and white squares connected in one region | Submit at end cap | Path is rejected and implicated clues may blink | region constraint plus validation feedback | `WIT-006`, `WIT-008`, `WIT-010` |
| Trace separates every black square from every differently coloured square | Submit at end cap | Path is accepted, remains lit and activates linked progression | objective completion | `WIT-006`, `WIT-009` |
| Valid partition leaves several blank cells in one region and crosses no interior cell | Submit | Blank cells do not invalidate the answer | no full-board coverage | `WIT-007` |
| Trace starts correctly but stops before the end cap | Release / leave incomplete | No complete solution is accepted | endpoint completion is required | `WIT-002`, `WIT-008` |

## Strategic and experiential structure

- Local decision: choose the next orthogonal edge while preserving both access
  to the end cap and the future boundary needed between opposed clue colours.
- Medium-term planning: grow partial walls around one colour without enclosing
  the active endpoint on the wrong side or forcing a self-intersection.
- Long-term structure: find one simple start-to-end separator whose induced
  connected components are all monochromatic with respect to square clues.
- Common heuristics: identify adjacent opposed colours that force a boundary;
  reason from bottlenecks and end-cap access; treat the line as a wall rather
  than a route that must visit symbols; revise the unfinished suffix early.
- Failure attribution: endpoint rejection and red clue feedback distinguish an
  invalid partition from a mere incomplete trace, while visible geometry lets
  the player reconstruct the cause.
- Player-trust factors: vertex sampling, self-contact prevention, region
  connectivity, boundary treatment and which violated clues blink must remain
  stable across retries.
- Claim IDs: `WIT-001`–`WIT-012`.

## Replay and variation

- What changes between panels: grid dimensions, start / end locations, square
  colours and positions; excluded later panels add independent clue families.
- Randomness or procedural generation: none in the scoped authored panel.
- Multiple viable strategies: a panel may admit several different separator
  paths, all accepted if they induce valid monochromatic regions.
- Typical replay motive: infer the rule from feedback, shorten an exploratory
  route, test another valid partition or revisit an optional panel.
- Claim IDs: `WIT-001`, `WIT-006`, `WIT-009`–`WIT-011`.

## Adjacent systems and history

- Flow Free shares fixed visible geometry, a self-paced fixed-endpoint simple
  path and constraint-completion objective. It requires several labelled
  endpoint pairs, disjoint path occupancy and whole-board coverage; The Witness
  uses one role-labelled start / end line as a region boundary.
- Cosmic Express also traces one simple entrance-to-exit path, but the route
  encodes a later locked passenger-service order. The Witness validates the
  path itself against static clue regions with no execution phase.
- Sudoku and Nonogram share complete visible constraint satisfaction but assign
  cell states directly. The Witness selects a path whose boundaries induce
  region properties indirectly.
- Claim IDs: `WIT-001`–`WIT-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-016` | one start-to-end compound trace with suffix retraction |
| System Behaviour | `SYS-073` | submit-time path and clue validation |
| Constraint | `CON-001`, `CON-029`, `CON-087` | fixed grid, simple path and monochromatic regions |
| Information | `INF-001`, `INF-023` | visible instance plus rejected-clue feedback |
| Objective | `OBJ-006` | complete clue-valid traced assignment |
| Time | `TIM-002` | untimed tracing and retry |

Canonical signature:

`ACT-016; SYS-073; CON-001,CON-029,CON-087; INF-001,INF-023; OBJ-006; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `38` (`GAME-0001`–`GAME-0038`).
- Exact genome matches: none.
- Tied near matches: `GAME-0012` — Flow Free (`6 / 12 = 0.500000`).
- Supported combination subsets: `COMB-0039`.
- Scan date: 2026-08-12.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0012`.

## Combination record

- Registered recurring `COMB-0039` — visible self-paced simple-path constraint
  completion, supported by Flow Free and The Witness.
- The five-gene core omits fixed-grid representation, paired endpoints,
  multiple-route exclusivity, region-clue grammar, system validation and each
  game's distinct feedback.

## Taxonomy impact

- Registry changes: three stable genes added: `SYS-073`, `CON-087` and
  `INF-023`; six existing genes reused.
- `ACT-016` and `CON-029` receive representation-neutral wording broad enough
  for vertex-edge panels as well as cell routes.
- `OBJ-006` is generalised from explicit cell assignments and total-coverage
  paths to a complete finite traced answer whose implied selected / unselected
  positions satisfy all declared constraints. No earlier signature changes.

## Negative results

- `CON-028` is rejected because start and end are role-distinct, not one of
  several immutable matching labelled pairs.
- `CON-030` and Flow Free's full-board condition are rejected because the scope
  contains one path and permits untouched cells / edges.
- `SYS-016` is rejected because no competing route is automatically broken.
- `TIM-003` is rejected because cursor motion does not create independent
  time-driven state progression.
