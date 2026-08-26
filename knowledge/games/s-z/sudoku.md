---
game_id: GAME-0005
slug: sudoku
game_title: Sudoku
analysis_status: reviewed
reviewed: 2026-08-11
combination_ids:
  - COMB-0005
gene_ids:
  action:
    - ACT-007
  system: []
  constraint:
    - CON-001
    - CON-009
    - CON-010
  information:
    - INF-001
  objective:
    - OBJ-006
  time:
    - TIM-002
---

# Game: Sudoku

## Analysis scope

- Version / ruleset: standard printed 9 × 9 Sudoku as published by Nikoli: 81
  cells divided into nine 3 × 3 blocks, a visible set of fixed clue digits and
  the domain 1–9.
- Included: assigning one digit to each empty cell, immutable givens, row,
  column and block constraints, complete valid-grid objective and self-paced
  paper solving.
- Excluded: diagonal, irregular, killer, overlapping and other variants;
  competition timing; digital conflict highlighting, automatic candidate
  removal, hints and mistake counters; pencil marks as explicit game state;
  puzzle construction and clue-symmetry requirements.
- Direct-play status: not conducted. The rules and solving boundaries were
  checked against Nikoli's rules, a World Puzzle Federation instruction set and
  mathematical treatments. This analysis does not rate one particular puzzle's
  difficulty.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SDK-001` | Standard Sudoku requires a digit from 1 to 9 in every empty cell and every row, column and 3 × 3 block to contain all nine digits | Confirmed | Corroborated | High | P1, P2, A1 |
| `SDK-002` | Printed clues are visible fixed assignments; player entries fill previously unassigned cells rather than reveal concealed contents | Confirmed | Corroborated | High | P1, P2, A1 |
| `SDK-003` | The printed rules perform no automatic state transition after an entry; deductions are work done by the solver | Observation | Direct | High | P1, P2 |
| `SDK-004` | Candidate elimination, forced placements and preemptive sets derive consequences from overlapping all-different units | Pattern | Corroborated | Medium | A1, A2 |
| `SDK-005` | Optional pencil candidates externalise reasoning but are not required by the standard completion rule | Observation | Corroborated | Medium | P1, A1 |
| `SDK-006` | The complete current puzzle state is visible even though the completed assignment is not initially known | Observation | Corroborated | High | P1, P2, A1 |
| `SDK-007` | The six-type model distinguishes unassigned variables from Minesweeper's fixed concealed contents without a taxonomy change | Observation | Corroborated | Medium | SDK-001–SDK-006 |
| `SDK-008` | Nikoli introduced the American puzzle Number Place to Japanese readers in 1984 and abbreviated its Japanese title to Sudoku | Confirmed | Direct | High | P1 |
| `SDK-009` | NP-completeness results for generalised Sudoku do not establish the difficulty of every fixed 9 × 9 instance | Confirmed | Corroborated | High | A3, A4 |
| `SDK-010` | A standard printed Sudoku is self-paced and has no in-play random event | Confirmed | Corroborated | High | P1, P2 |

## Basic data

- Release / origin: Nikoli reports finding the puzzle as “Number Place” in an
  American puzzle magazine and introducing it in Japan in 1984 under a longer
  title later abbreviated to “Sudoku”. The exact authorship of that American
  source is outside this record's supported historical claim.
- Platform or physical form: printed pencil puzzle; the mechanical unit does
  not depend on a digital implementation.
- Puzzle family: finite constraint-satisfaction / number-placement puzzle.
- Primary and official sources:
  - **[P1] Nikoli:** [“Sudoku”](https://www.nikoli.co.jp/en/puzzles/sudoku/),
    giving the two canonical rules and Nikoli's account of its 1984
    introduction and naming.
  - **[P2] World Puzzle Federation:**
    [2018 Sudoku Grand Prix instruction booklet](https://gp.worldpuzzle.org/sites/default/files/Puzzles/2018/2018_SudokuRound1.pdf),
    applying the classic row, column and 3 × 3 region rule before variant
    additions.
- Academic and mathematical sources:
  - **[A1]** J. F. Crook,
    [“A Pencil-and-Paper Algorithm for Solving Sudoku Puzzles”](https://www.ams.org/notices/200904/tx090400460p.pdf),
    *Notices of the AMS* 56(4), 2009, defining the board and formalising
    candidates, forced values and preemptive sets.
  - **[A2]** Radek Pelánek,
    [“Difficulty Rating of Sudoku Puzzles: An Overview and Evaluation”](https://arxiv.org/abs/1403.7373),
    reviewing human-oriented strategies and difficulty measures from extensive
    solving data.
  - **[A3]** Takayuki Yato and Takahiro Seta,
    [“Complexity and Completeness of Finding Another Solution and Its Application to Puzzles”](https://ipsj.ixsq.nii.ac.jp/records/31947),
    2002–2003, establishing complexity results for generalised Sudoku.
  - **[A4]** Michael Haythorpe,
    [“Reducing the generalised Sudoku problem to the Hamiltonian cycle problem”](https://arxiv.org/abs/1603.03019),
    restating the unbounded generalisation and its row, column and block
    constraints.
- Claim IDs: `SDK-001`–`SDK-010`.

## Mechanical decomposition

### Action Genes

- `ACT-007` — assign symbol to open position. The solver selects an empty cell
  and records one digit from 1 to 9 as its value.
- Erasing or replacing a tentative player entry is an input-medium parameter.
  It does not change the canonical success condition or create a second
  decision structure.
- Candidate pencil marks are excluded from the genome. They may record several
  still-possible values but do not themselves assign the cell and are not
  required by Nikoli's rules.
- `ACT-003` does not apply: entering a digit does not expose a pre-existing
  value stored under the cell.
- `ACT-004` does not apply: a candidate mark neither represents a suspected
  hazard nor protects the cell from an ordinary assignment.
- Claim IDs: `SDK-001`, `SDK-002`, `SDK-005`.

### System Behaviour Genes

- Existing gene IDs: none.
- Candidate genes: none.
- Writing a digit changes only the recorded assignment. The paper puzzle does
  not automatically eliminate candidates, propagate values, reject conflicts
  or fill forced cells.
- Constraint propagation is a solving method: the player infers consequences
  from static rules. Calling it a System Behaviour would confuse reasoning with
  an automatic game-state transition.
- Digital highlighting, auto-notes and mistake feedback are excluded variant or
  interface behaviours.
- Claim IDs: `SDK-003`, `SDK-004`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The standard grid has exactly 81 cells
  in a fixed topology.
- `CON-009` — immutable given assignments. Printed clue digits constrain the
  completion and are not targets of `ACT-007`.
- `CON-010` — all-different unit coverage. Each of 27 overlapping units—nine
  rows, nine columns and nine blocks—must contain the complete domain 1–9
  exactly once.
- The 9 × 9 dimensions, 3 × 3 block geometry and digit domain are parameters.
  They do not require separate genes for rows, columns and blocks because all
  three instantiate the same unit rule.
- A well-formed published puzzle's solution count is an instance property and
  editorial precondition. It is not another action-time constraint on the
  solver.
- Scarce strategic resource: useful deductions from the remaining candidate
  domains. There is no consumable board space, life or time resource.
- Claim IDs: `SDK-001`, `SDK-002`, `SDK-004`.

### Information Genes

- `INF-001` — fully visible current state. Every immutable given, empty cell
  and player-entered value can be inspected before another assignment.
- `INF-003` is absent. An empty Sudoku cell does not contain a fixed concealed
  current digit waiting for a reveal action; its value is an unassigned part of
  the sought completion.
- Candidate sets are derivable knowledge produced by applying `CON-009` and
  `CON-010` to the visible partial assignment. Writing those sets on paper
  externalises solver memory but does not reveal new system-held information.
- No future random event or preview queue exists.
- Claim IDs: `SDK-002`, `SDK-005`, `SDK-006`, `SDK-010`.

### Objective Genes

- `OBJ-006` — complete constraint-satisfying assignment. Success requires all
  81 cells to be assigned and every row, column and block rule to hold.
- The target is defined intensionally by constraints, not supplied as a
  separately visible final arrangement. Therefore `OBJ-004` does not apply.
- There is no score or built-in failure state in the printed rules. An invalid
  partial entry can be revised; an invalid full grid simply fails the objective.
- Claim IDs: `SDK-001`, `SDK-003`.

### Time Genes

- `TIM-002` — self-paced sequential action. The solver may pause indefinitely
  between entries, and no state changes because time passes.
- A newspaper or tournament timer measures performance externally but is not
  part of the scoped puzzle state.
- Claim IDs: `SDK-003`, `SDK-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Empty cell with digit 5 absent from its row, column and block | Assign 5 | Record 5 in that cell; nothing else changes automatically | Direct assignment without system propagation | `SDK-003` |
| Printed given containing 5 | Attempt to replace it | Action is outside the rules | Immutable given boundary | `SDK-002` |
| Row already containing 5 | Assign 5 to another cell in that row | Recorded state violates the row rule | All-different legality is a constraint | `SDK-001` |
| Empty cell whose peers contain digits 1–8 | Infer its domain | Only 9 remains possible; the board is unchanged until 9 is assigned | Deduction is player reasoning | `SDK-004` |
| Two cells in one unit have the same two remaining candidates | Record or mentally retain the pair | Those digits can be excluded from other cells in the unit; no system action occurs | Preemptive-set reasoning | `SDK-004` |
| All cells assigned and every unit contains 1–9 | Finish the final assignment | Completion condition is satisfied | Constraint-defined objective | `SDK-001` |

An illegal duplicate can be physically written on paper, but it does not become
a valid move toward the objective. Digital implementations that prevent or flag
it add system behaviour outside this scope.

## Strategic and experiential structure

- Local decision: determine whether one cell has a single admissible digit or
  one digit has a single admissible position within a unit.
- Medium-term planning: update candidate domains across intersecting rows,
  columns and blocks, looking for subsets whose values are confined to the same
  number of cells.
- Long-term structure: choose deductions that expose further forced
  assignments while preserving an auditable chain from givens to entries.
- Common methods include scanning, naked and hidden singles, candidate
  elimination, preemptive sets and—when elementary propagation stalls—more
  complex chains or controlled search.
- Failure attribution: a contradiction can often be traced to an earlier
  unsupported assignment. Attribution becomes harder when the solver records
  insufficient candidate history or branches without preserving assumptions.
- Player-trust factors: givens and constraints do not change. A properly edited
  puzzle is expected to support a coherent completion, but this record does not
  infer quality or uniqueness from the rules alone.
- Claim IDs: `SDK-004`, `SDK-005`.

Crook's algorithm establishes that candidates and preemptive sets are useful
representations; it does not make pencil marks mandatory game actions. Likewise,
computational backtracking can solve instances but does not describe the only
human decision structure.

## Replay and variation

- What changes between sessions: the placement of givens and the resulting
  constraint structure.
- Randomness or procedural generation: none during the solve. Construction may
  be manual or computational, but it occurs before the scoped decision loop.
- Multiple viable strategies: different forced deductions can often be applied
  in different orders; advanced puzzles may admit several proof paths to the
  same completion.
- Typical replay motive: solve a new instance, improve recognition of deduction
  patterns or reduce completion time under an optional external measure.
- Claim IDs: `SDK-004`, `SDK-010`.

## Adjacent systems and history

- Direct lineage: Nikoli explicitly identifies an American “Number Place”
  source and its own 1984 Japanese introduction. This record avoids attributing
  authorship beyond that primary account.
- Structural predecessors: Latin squares share row and column uniqueness;
  Sudoku adds overlapping block units and fixed partial assignments.
- Variants: diagonal and irregular Sudoku alter unit topology; Killer Sudoku
  adds arithmetic cages; Samurai Sudoku overlaps grids; digital versions may
  add notes, validation, hints, lives or timers.
- Similar games: Latin-square completion, Kakuro and Futoshiki use symbolic
  assignments under different global or arithmetic constraints. Minesweeper
  instead reveals evidence about a concealed fixed field.
- Complexity caveat: NP-completeness concerns an unbounded generalisation whose
  grid size grows with the input. A fixed 9 × 9 state space is finite, and the
  theorem does not rate any particular newspaper puzzle or human technique.
- Claim IDs: `SDK-008`, `SDK-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-007` | digit domain, replacement and erasure affordance |
| System Behaviour | none | digital validation and auto-notes excluded |
| Constraint | `CON-001`, `CON-009`, `CON-010` | 9 × 9 grid, 3 × 3 blocks, givens |
| Information | `INF-001` | optional external candidate notation |
| Objective | `OBJ-006` | complete valid assignment, solution-count precondition |
| Time | `TIM-002` | optional external timer excluded |

Canonical signature:

`ACT-007; ; CON-001,CON-009,CON-010; INF-001; OBJ-006; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `4` (`GAME-0001`–`GAME-0004`).
- Exact genome matches: none.
- Tied near matches: `GAME-0002` — Rubik’s Cube (`3 / 11 = 0.272727`).
- Supported combination subsets: `COMB-0005`.
- Scan date: 2026-08-11.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0002` — Rubik's Cube | `CON-001`, `INF-001`, `TIM-002` | Both are self-paced and fully inspectable; Cube permutes a complete persistent state through reversible turns, while Sudoku completes initially unassigned variables | Near, `0.272727` |

### Preserved research notes

- New combination: `COMB-0005`, whose five genes are a proper subset of this
  seven-gene genome.
- New genes: `ACT-007`, `CON-009`, `CON-010`, `OBJ-006`.
- Classification result: `New gene`.
- Evidence and reasoning: direct symbolic assignment, immutable givens,
  overlapping all-different coverage and complete valid assignment each define
  a distinct typed boundary. Grid size, digit domain, unit geometry, clue count
  and solution count remain parameters or instance properties.

## Taxonomy impact

- Registry changes: four bounded genes added; `CON-001`, `INF-001` and
  `TIM-002` reused.
- Taxonomy-change record: none. The apparent “unknown values” do not require a
  new Information type because no current contents are hidden: the visible
  partial assignment is complete current-state information.
- Candidate terms affected: place values, fixed clues, uniqueness constraints
  and complete assignment now have bounded mappings.
- Candidate notation remains outside the genome at this scope. A future digital
  system where notes change legal input or trigger automatic behaviour may
  justify a separate analysis, not retroactive promotion here.
- Constraint propagation is not promoted to `SYS`: it is a solver's inference
  over static constraints unless an implementation automatically changes
  candidates or assignments.
- Claim IDs: `SDK-007`.

## Negative results

None. Sudoku supplies the planned boundary case and confirms that
`INF-003` means a fixed concealed current state, not every unknown answer. It
does not reject a concrete prior claim, candidate or gene distinction.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Empty Sudoku cells are unassigned positions,
  not concealed pre-existing values (`SDK-002`).
- [Observation | Direct | High] Deductive propagation changes solver knowledge
  but causes no automatic state transition in the printed puzzle (`SDK-003`).
- [Pattern | Corroborated | Medium] Overlapping all-different units support
  forced placements and candidate-subset deductions (`SDK-004`).

## Нові гени

- [Observation | Corroborated | High] `ACT-007`, `CON-009`, `CON-010` and
  `OBJ-006`.
- [Observation | Corroborated | High] `CON-001`, `INF-001` and `TIM-002` are
  reused.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0005` — self-paced completion of
  overlapping all-different units from immutable givens.

## Зміни таксономії

- [Observation | Corroborated | Medium] Змін таксономії немає. The current
  Information boundary distinguishes unassigned values from hidden state.

## Нові питання

- TODO: analyse a digital Sudoku ruleset before deciding whether automatic
  conflict feedback or candidate maintenance adds System Behaviour genes.
- TODO: test `CON-010` against Latin-square and irregular-region puzzles to
  determine whether unit topology remains a parameter across families.
- TODO: compare optional candidate notation with a game where annotations alter
  legal actions before considering a separate annotation Action gene.

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] `GAME-0006` — Sokoban.
- Optimisation criterion: test action consequence and irreversibility after a
  static symbolic constraint system.
- Expected information gain: distinguish direct avatar movement from indirect
  crate pushing, characterise static collision and goal occupancy, and test
  deadlocks that preserve legal moves while making the objective unreachable.
- Backlog impact: Sokoban moves from the coverage pool to the immediate task;
  Sudoku leaves the pool after completion.

## Чому саме вона

- [Hypothesis | Limited | Medium] Sokoban introduces spatial navigation,
  asymmetric push-only interaction and irreversible strategic deadlocks without
  hidden information, randomness or real-time pressure. It directly tests
  whether `CON-005` reversibility and `OBJ-003` move availability are distinct
  from preserving objective reachability.
