---
game_id: GAME-0071
slug: slant
game_title: Slant
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0071
gene_ids:
  action:
    - ACT-007
  system: []
  constraint:
    - CON-001
    - CON-114
    - CON-115
  information:
    - INF-001
  objective:
    - OBJ-006
  time:
    - TIM-002
---

# Game: Slant

## Analysis scope

- Version / ruleset: Simon Tatham's Portable Puzzle Collection, current
  standard desktop `8 × 8 Easy` Slant puzzle, game ID
  `8x8:a0a1c1a032a1a3a1a21a222a2d21c2a2c21a1a11a11a1a12b1b113b2a12f0a11`,
  from its empty 64-cell field to one accepted complete orientation assignment.
- Included: assigning `/` or `\` to every cell; visible numbered grid vertices;
  exact incident-line counts; one global no-loop rule; revisable entries;
  complete visible state and self-paced solving.
- Excluded: Hard generation difficulty; other dimensions; Solve, Undo, Redo,
  Restart, cursor and error colouring as interface support; random generation
  as an in-solve mechanic; preference settings and presentation.
- Direct-play status: the current official JavaScript implementation was
  opened and its displayed game ID captured. The description and transition
  semantics were independently reproduced from the current MIT-licensed
  source. A local constraint solver decoded all 39 clues, proved that the
  64-cell control has exactly one solution and separately rejected a four-edge
  diamond cycle.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SLT-001` | The standard desktop preset is an `8 × 8 Easy` grid and the fixed control contains 64 cells plus 39 visible vertex clues | Confirmed | Direct | High | P1, P2, P3, local control |
| `SLT-002` | Every cell must receive exactly one of two diagonals, `/` or `\` | Confirmed | Direct | High | P1, P2 |
| `SLT-003` | A numbered vertex must have exactly that many incident diagonals in the complete assignment | Confirmed | Direct | High | P1, P2, local control |
| `SLT-004` | The graph formed by all chosen diagonals must contain no cycle | Confirmed | Direct | High | P1, P2, local control |
| `SLT-005` | The fixed 64-cell control has exactly one complete satisfying assignment | Observation | Direct | High | P1, P2, P3, local exhaustive control |
| `SLT-006` | Slant adds exact vertex-degree and global acyclicity constraints while reusing generic visible symbol assignment | Observation | Corroborated | High | `SLT-001`–`SLT-005` |

## Basic data

- Release / origin: Simon Tatham credits the puzzle to Nikoli, where it is
  known as Gokigen Naname; this record covers Tatham's implementation rather
  than making a historical authorship claim.
- Platform or physical form: open-source desktop and official JavaScript
  single-player grid puzzle.
- Puzzle family: binary diagonal assignment under local degree and global
  acyclicity constraints.
- Primary sources:
  - **[P1] Simon Tatham:** [official Slant manual](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/slant.html),
    directly specifying the two cell orientations, exact numbered incidence
    and no-loop completion rules.
  - **[P2] Simon Tatham:** [current `slant.c` implementation](https://git.tartarus.org/?p=simon/puzzles.git;a=blob;f=slant.c;hb=HEAD),
    defining the `8 × 8 Easy` desktop default, description codec, player
    transitions, degree checks, loop detection and full-field completion.
  - **[P3] Simon Tatham:** [official playable JavaScript version](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/slant.html),
    which produced the exact descriptive game ID used here.
- Secondary sources: none required for the bounded transition claims.
- Reproducible artefact: `scripts/verify_slant_control.py` decodes the 81 grid
  vertices, applies exact clue bounds and union-find cycle rejection, then
  exhaustively searches until a second solution or exhaustion.
- Claim IDs: `SLT-001`–`SLT-006`.

## Mechanical decomposition

### Action Genes

- `ACT-007` — assign symbol to open position. The player assigns one of the
  two diagonal symbols to one cell and may clear or replace that tentative
  value before completion.
- Mouse-button cycling and direct keyboard entry are input parameters, not
  separate actions.
- Claim IDs: `SLT-002`, `SLT-006`.

### System Behaviour Genes

- Existing gene IDs: none.
- Placing a diagonal changes only that cell's proposed value. Constraint
  highlighting is feedback, not an automatic puzzle-state transformation.
- Solver deductions and propagation are work performed by the player and are
  not classified as System Behaviours.
- Claim IDs: `SLT-002`–`SLT-004`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The control has exactly 64 square
  variables in one immutable `8 × 8` topology.
- `CON-114` — exact incident-edge degree at marked vertex. Each numbered
  intersection constrains the number of chosen cell diagonals terminating
  there to equal its displayed value.
- `CON-115` — global acyclicity of selected linkage graph. Across numbered and
  unnumbered vertices alike, no connected component may close a loop.
- The `/` versus `\` domain is a parameter of `ACT-007`; clue values zero
  through four and boundary degree are parameters of `CON-114`.
- Claim IDs: `SLT-001`–`SLT-004`.

### Information Genes

- `INF-001` — fully visible current state. All clue numbers, empty cells and
  player-assigned diagonals are inspectable before the next edit.
- The solution is unknown but not a fixed concealed board state waiting to be
  revealed; it is a constraint-satisfying assignment constructed from visible
  information.
- Claim IDs: `SLT-001`–`SLT-005`.

### Objective Genes

- `OBJ-006` — complete constraint-satisfying assignment. Every one of the 64
  cells must be oriented, every numbered degree must be exact and the complete
  diagonal graph must remain acyclic.
- No prescribed image or literal target arrangement is displayed in advance.
- Claim IDs: `SLT-002`–`SLT-005`.

### Time Genes

- `TIM-002` — self-paced sequential action. Entries may be placed, erased or
  revised without a deadline, and the board does not advance with elapsed time.
- Claim IDs: `SLT-002`, `SLT-005`.

## Reproducible transitions

Coordinates name cells by row `A`–`H` and column `1`–`8`; vertices use their
zero-based source coordinates where needed.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Empty cell `A1` | assign `\` | the cell links its north-west and south-east vertices; no other cell changes | one addressed binary symbol assignment | `SLT-002` |
| Four cells around an interior vertex with clue `2`, one incident and two non-incident orientations fixed | orient the last cell toward the vertex | incident degree becomes exactly two | local clue constrains shared cell variables | `SLT-003` |
| Cells `A1`, `A2`, `B1` form three sides of one four-vertex diamond | assign the fourth diamond side in `B2` | the new edge joins vertices already connected and creates a cycle, so the state violates the global rule | acyclicity applies beyond numbered points | `SLT-004` |
| Fixed 39-clue control | assign the verifier's 64-symbol solution | all 64 cells are filled, every clue degree is exact and union-find finds no cycle | one complete accepted assignment | `SLT-005` |
| Fixed control with the first still-undecided cell forced opposite to the unique solution | continue exhaustive propagation and branching | no complete satisfying assignment remains | the recorded solution is unique, not merely one witness | `SLT-005` |

The verifier prints the eight exact solution rows and asserts both uniqueness
and the independent four-cell loop counterexample.

## Strategic and experiential structure

- Local decision: determine which of the two diagonals a cell can take from
  adjacent clue deficits and already excluded incidence.
- Medium-term planning: propagate exact-degree consequences through shared
  cells; a clue whose quota is filled excludes every other incident edge,
  while a clue whose remaining capacity equals its undecided neighbours forces
  all of them inward.
- Long-term structure: maintain a forest across the entire vertex graph. A
  locally degree-compatible edge may still be impossible because its endpoints
  already belong to one connected component.
- Common heuristics: resolve zero and saturated clues first, track connected
  components, then combine equality relations among still-undecided cells.
- Failure attribution: red clue or loop feedback reflects a visible violated
  predicate; no hidden or random in-move event changes the result.
- Player-trust factors: boundary vertices must count only existing incident
  cells, `/` and `\` endpoints must not be swapped, and loop detection must
  include unnumbered vertices.
- Claim IDs: `SLT-002`–`SLT-005`.

## Replay and variation

- What changes between sessions: the visible clue positions and values, and
  therefore the unique diagonal assignment generated for the selected size.
- Randomness or procedural generation: setup-only. The descriptive game ID
  makes the bounded control deterministic.
- Multiple viable strategies: the same unique solution can be derived in
  different orders; Easy generation is intended to permit direct deductions.
- Typical replay motive: solve a different visible constraint graph or select
  Hard, where relational deductions between cells are required.
- Claim IDs: `SLT-001`, `SLT-005`.

## Adjacent systems and history

- Sudoku and Nonogram share visible, self-paced symbol assignment and complete
  CSP satisfaction. Sudoku constrains all-different units; Nonogram constrains
  ordered filled runs; neither treats assignments as graph edges or forbids
  cycles.
- Hexologic likewise shares variables between exact numeric constraints, but
  sums cell values along lines. Slant instead counts incident chosen edges at
  vertices and adds a separate non-local topology predicate.
- The Witness forbids path self-intersection while tracing one connected path.
  Slant assigns every cell independently, then requires the union of all those
  edges to be a forest; there is no single player-drawn route.
- Claim IDs: `SLT-003`, `SLT-004`, `SLT-006`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-007` | `/` or `\`; revisable cell assignment |
| System Behaviour | none | no automatic state transition |
| Constraint | `CON-001`, `CON-114`, `CON-115` | 64 cells; clue degree; no cycles |
| Information | `INF-001` | complete visible clues and assignments |
| Objective | `OBJ-006` | fill every cell and satisfy all predicates |
| Time | `TIM-002` | self-paced editing |

Canonical signature:

`ACT-007; none; CON-001,CON-114,CON-115; INF-001; OBJ-006; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `70` (`GAME-0001`–`GAME-0070`).
- Exact genome matches: none.
- Tied near matches: `GAME-0005` — Sudoku (`5 / 9 = 0.555556`); `GAME-0008` — Nonogram (`5 / 9 = 0.555556`).
- Supported combination subsets: `COMB-0071`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0005` — Sudoku | `ACT-007`, `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | Sudoku covers overlapping units with one complete all-different domain; Slant imposes exact vertex degrees plus graph-wide acyclicity | Near, `0.555556` |
| `GAME-0008` — Nonogram | `ACT-007`, `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | Nonogram satisfies ordered run descriptions on rows and columns; Slant treats assigned diagonals as edges and forbids cycles | Near, `0.555556` |

### Preserved research notes

- New genes: `CON-114`, `CON-115`.
- Classification result: `New gene` and new verified combination.
- Evidence and reasoning: neither exact incidence at graph vertices nor the
  acyclicity of a union of independently assigned edges is represented by a
  prior constraint; generic assignment and CSP completion remain reusable.

## Taxonomy impact

- Registry changes: add `CON-114` and `CON-115`; extend `ACT-007`, `CON-001`,
  `INF-001`, `OBJ-006` and `TIM-002` with Slant evidence.
- Taxonomy-change record: none. No prior classification is rewritten.
- Candidate terms affected: exact incident-edge degree and global selected-
  linkage acyclicity are promoted to stable IDs.

## Negative results

- Rejected a new binary orientation action: `ACT-007` already covers assigning
  one symbol from a finite domain to one editable cell.
- Rejected `CON-010`: exact degree around one graph vertex is not all-different
  coverage of a complete symbol domain.
- Rejected `CON-029`: Slant does not construct one simple endpoint-to-endpoint
  path; it fills every cell and permits multiple forest components.
- Rejected a new objective: `OBJ-006` already requires a full assignment that
  satisfies every declared constraint.
- Rejected loop highlighting as a System Behaviour: it reports a violated
  static predicate without transforming another game element.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Поточний стандартний контроль `8 × 8 Easy`
  містить 64 клітинки та 39 видимих вершинних підказок (`SLT-001`).
- [Observation | Direct | High] Незалежний повний пошук знайшов рівно один
  64-символьний розв’язок і відхилив замкнений ромб (`SLT-004`, `SLT-005`).

## Нові гени

- [Observation | Direct | High] `CON-114` — точний степінь інцидентних ребер
  у позначеній вершині.
- [Observation | Direct | High] `CON-115` — глобальна ациклічність графа
  вибраних зв’язків.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0071` — повне двійкове призначення
  діагоналей під локальними степенями та глобальною ациклічністю.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає; нові обмеження
  додаються без перепризначення попередніх генів.

## Нові питання

- Чи повторить майбутня гра `CON-115` у задачі побудови лісу без числових
  степенів, щоб відокремити топологічний контроль від Slant-підказок?

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] Tents.
- Optimisation criterion: retain exact reproducibility while moving from graph
  orientation to bijective adjacency placement and row / column quotas.
- Expected information gain: one-to-one tree–tent matching, non-touching
  placement and simultaneous marginal counts.
- Backlog impact: The Room remains retained pending a stronger first-box scope
  packet; Tents becomes the reproducible lead for `GAME-0072`.

## Чому саме вона

- [Hypothesis | Limited | Medium] Tents shares visible self-paced deduction but
  should add a distinct matching relation and exclusion geometry without
  repeating Slant's assigned-edge graph.
