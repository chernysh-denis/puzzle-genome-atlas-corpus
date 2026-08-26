---
game_id: GAME-0008
slug: nonogram
game_title: Nonogram
analysis_status: reviewed
reviewed: 2026-08-11
combination_ids:
  - COMB-0008
gene_ids:
  action:
    - ACT-007
  system: []
  constraint:
    - CON-001
    - CON-018
  information:
    - INF-001
    - INF-006
  objective:
    - OBJ-006
  time:
    - TIM-002
---

# Game: Nonogram

## Analysis scope

- Version / ruleset: classic black-and-white rectangular Nonogram represented
  as a printed logic puzzle.
- Included: a fixed grid; one ordered numeric clue sequence for every row and
  column; binary filled / empty cell assignment; one or more empty cells
  separating consecutive filled runs; completion when every line matches its
  clue sequence.
- Excluded: colour Nonograms, triangular grids, missing or ambiguous clues,
  hints, lives, timers, automatic error checking, automatic line completion,
  animation and a requirement that the resulting image be recognisable.
- Direct-play status: not conducted. Rules were triangulated from a public
  rules reference and peer-reviewed formal descriptions. No specific published
  puzzle is used to claim universal uniqueness or human-solvability.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `NON-001` | Every row and column has a visible ordered sequence describing lengths of consecutive filled runs | Confirmed | Corroborated | High | P1, A1, A2 |
| `NON-002` | Consecutive runs in one line are separated by at least one empty cell | Confirmed | Corroborated | High | P1, A1, A2 |
| `NON-003` | Every cell has a binary filled or empty solution value shared by one row and one column | Confirmed | Corroborated | High | A1, A2 |
| `NON-004` | Completion requires a full grid whose row and column patterns all match their clues | Confirmed | Corroborated | High | P1, A1 |
| `NON-005` | Clues expose run order and length but not absolute run positions | Observation | Corroborated | High | NON-001–NON-004 |
| `NON-006` | Cross marks are a representation of confirmed empty assignments, not a second objective or automatic behaviour | Observation | Corroborated | Medium | P1, A1 |
| `NON-007` | The puzzle has no concealed pre-existing cell contents in the scoped decision state | Observation | Corroborated | High | A1, A2 |
| `NON-008` | Generalised hardness results do not establish difficulty or uniqueness for every published instance | Confirmed | Corroborated | High | A1, A3 |
| `NON-009` | Historical accounts place the modern form in Japan in the late 1980s and associate it with Non Ishida and Tetsuya Nishio | Pattern | Limited | Medium | H1 |
| `NON-010` | The six-type model represents ordered clues and cross-line coupling without a taxonomy change | Observation | Corroborated | Medium | NON-001–NON-008 |

## Basic data

- Release / origin: secondary historical accounts associate the modern puzzle
  with independent late-1980s Japanese work by Non Ishida and Tetsuya Nishio.
  This is contextual only and does not support a mechanical priority claim.
- Platform or physical form: print logic puzzle, later widely implemented
  digitally; the scoped mechanics are medium-independent.
- Puzzle family: binary constraint satisfaction and image reconstruction.
- Rules source:
  - **[P1] Nonogram.com:**
    [“Nonogram Rules”](https://nonogram.com/?hl=en), stating that row and column
    numbers give consecutive filled-run lengths and separated runs occur in the
    listed order.
- Academic sources:
  - **[A1]** K. Joost Batenburg and Walter A. Kosters,
    [“Solving Nonograms by combining relaxations”](https://homepages.cwi.nl/~kbatenbu/papers/bako_pr_2009.pdf),
    *Pattern Recognition* 42, 2009, formalising binary pixels, ordered line
    descriptions and intersecting row / column constraints.
  - **[A2]** K. Joost Batenburg and Walter A. Kosters,
    [“Nonograms”](https://liacs.leidenuniv.nl/~kosterswa/nvti2012.pdf),
    formalising the order, lengths and required white separation of black
    segments.
  - **[A3]** Nobuhisa Ueda and Tadaaki Nagao,
    [“NP-completeness Results for NONOGRAM via Parsimonious Reductions”](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=1bb23460c7f0462d95832bb876ec2ee0e5bc46cf),
    Technical Report TR96-0008, 1996.
- Historical source:
  - **[H1] Puzzly Game:**
    [“The History and Origin of Nonogram”](https://puzzlygame.com/pages/nonogram_history/),
    a secondary account of Ishida, Nishio and early publication.
- Claim IDs: `NON-001`–`NON-010`.

## Mechanical decomposition

### Action Genes

- `ACT-007` — assign symbol to open position. The solver records one binary
  value for an unresolved cell: filled or confirmed empty.
- On paper, shading represents filled and an X commonly represents confirmed
  empty. These are two values in one assignment domain, not separate action
  genes. Erasing or replacing a tentative assignment is a parameter already
  allowed by `ACT-007`.
- Pencil annotations about possible run starts are reasoning aids rather than
  required state changes and remain outside the genome.
- Claim IDs: `NON-003`, `NON-006`.

### System Behaviour Genes

- Existing gene IDs: none.
- Candidate genes: none.
- The printed grid does not validate, propagate, reveal or assign cells after a
  mark. All deductions and assignments are performed by the solver.
- Digital error highlighting, auto-crossing completed clues and automatic fill
  are excluded implementation behaviours and would require a separate scope.
- Claim IDs: `NON-004`, `NON-006`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The puzzle has a finite rectangular
  grid whose dimensions and cell topology do not change during play.
- `CON-018` — orthogonally coupled ordered-run satisfaction. Every cell's
  binary value must simultaneously contribute to its row and column pattern;
  each pattern must realise the listed run lengths in order with at least one
  empty separator between adjacent runs.
- Grid dimensions, clue-list lengths and individual run values are parameters.
  The defining decision structure is simultaneous line satisfaction, not any
  particular image or density.
- This is distinct from `CON-010`: a Nonogram line does not require every
  symbol exactly once and repeated run lengths are allowed.
- Claim IDs: `NON-001`–`NON-004`.

### Information Genes

- `INF-001` — fully visible current state. All clue sequences and all current
  filled, empty-confirmed and unresolved cell records are inspectable.
- `INF-006` — visible ordered run-length description. A clue such as `3 1 2`
  specifies exact run lengths and order while leaving their positions unknown.
- `INF-003` is absent. The solution values are not pre-existing concealed
  contents waiting to be revealed; they are variables to be assigned under
  visible constraints, as in Sudoku.
- `INF-004` is absent. Minesweeper reports one local unordered hazard total for
  a neighbourhood; Nonogram discloses an ordered sequence for an entire line.
- Claim IDs: `NON-001`, `NON-005`, `NON-007`.

### Objective Genes

- `OBJ-006` — complete constraint-satisfying assignment. Every grid cell must
  receive a filled or empty solution value and all row and column descriptions
  must hold simultaneously.
- Revealing a recognisable picture is presentation and feedback, not a separate
  objective. A valid abstract pattern remains complete even if it depicts
  nothing recognisable.
- `OBJ-004` is absent because the target arrangement is not separately shown
  and reconstructed; it is inferred from constraints.
- Claim IDs: `NON-003`, `NON-004`.

### Time Genes

- `TIM-002` — self-paced sequential action. The solver may pause indefinitely
  between cell assignments and the printed puzzle does not advance itself.
- External solve timing and move counting are excluded evaluation layers.
- Claim IDs: `NON-003`, `NON-006`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Five-cell line has clue `5` | Assign each cell filled | One run of five satisfies the line | Exact run length | `NON-001` |
| Five-cell line has clue `1 1 1` | Apply minimum separators | Pattern must be filled-empty-filled-empty-filled | Ordered separated runs | `NON-002` |
| Five-cell line has clue `3` | Compare all legal placements | Centre cell is filled in every placement | Overlap deduction | `NON-005` |
| A row assignment forces one cell empty | Record X / empty | Its column loses that possible filled position | Orthogonal coupling | `NON-003` |
| Row pattern matches but one crossing column does not | Attempt completion | Grid is invalid | Both axes must hold | `NON-004` |
| Every cell is binary-assigned and every line matches | Finish final assignment | Objective is satisfied | Complete constrained assignment | `NON-004` |

## Strategic and experiential structure

- Local decision: determine whether one cell has the same value in every legal
  placement of the current line's remaining runs.
- Medium-term planning: propagate filled and empty conclusions between rows and
  columns, repeatedly shrinking feasible placements.
- Long-term structure: resolve interactions that no single line can determine
  alone and avoid guesses that create an untracked branch.
- Common heuristics: fill overlap shared by all placements of a long run; mark
  separators around completed runs; use confirmed empties to split a line;
  revisit crossing lines after every new assignment.
- Failure attribution: a wrong binary assignment may remain locally plausible
  until a distant crossing line becomes impossible. Without automatic checking,
  the solver must locate and erase the unsupported inference.
- Player-trust factors: every given clue is stable and visible, but a puzzle
  with multiple solutions or one requiring guessing may violate expectations
  not guaranteed by the core rules.
- Claim IDs: `NON-005`, `NON-008`.

## Replay and variation

- What changes between sessions: grid dimensions, ordered line descriptions,
  resulting binary pattern and logical difficulty.
- Randomness or procedural generation: none within a printed instance.
- Multiple viable strategies: deduction order may vary even for a unique final
  grid; the rules alone do not guarantee uniqueness.
- Typical replay motive: correct an inconsistent branch, improve solve time or
  solve a different clue set.
- Claim IDs: `NON-004`, `NON-008`.

## Adjacent systems and history

- Secondary histories place the modern format in late-1980s Japan and associate
  early versions with Non Ishida and Tetsuya Nishio.
- Colour Nonograms change the assignment domain and separator rule because
  adjacent runs of different colours may not require a blank separator; they
  need separate analysis.
- Minesweeper also uses grid numbers but its clues are revealed locally from a
  concealed hazard field. Sudoku shares visible assignment but its units use
  all-different coverage rather than ordered binary runs.
- Complexity caveat: Ueda and Nagao and later work concern scalable formal
  instances. Hardness does not imply that every published finite puzzle is
  difficult, unique or impossible to solve by line deductions.
- Claim IDs: `NON-008`, `NON-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-007` | filled / confirmed-empty binary values |
| System Behaviour | none | excluded validation and propagation |
| Constraint | `CON-001`, `CON-018` | grid dimensions and clue sequences |
| Information | `INF-001`, `INF-006` | ordered lengths without positions |
| Objective | `OBJ-006` | all orthogonal lines satisfied |
| Time | `TIM-002` | optional external timing |

Canonical signature:

`ACT-007; ; CON-001,CON-018; INF-001,INF-006; OBJ-006; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `7` (`GAME-0001`–`GAME-0007`).
- Exact genome matches: none.
- Tied near matches: `GAME-0005` — Sudoku (`5 / 9 = 0.555556`).
- Supported combination subsets: `COMB-0008`.
- Scan date: 2026-08-11.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0005` — Sudoku | `ACT-007`, `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | Both visibly complete constrained assignments; Sudoku uses immutable givens and all-different symbols, while Nonogram uses ordered binary runs across rows and columns | Near, `0.555556` |

### Preserved research notes

- New combination: `COMB-0008`, whose five genes are a proper subset of this
  seven-gene genome.
- New genes: `CON-018`, `INF-006`.
- Classification result: `New gene`.
- Evidence and reasoning: visible ordered run descriptions differ from both
  exact local aggregate clues and a fully specified target. Their orthogonal
  simultaneous satisfaction is a bounded constraint. Binary values, dimensions
  and clue magnitudes remain parameters of reused assignment genes.

## Taxonomy impact

- Registry changes: two bounded genes added; `ACT-007`, `CON-001`, `INF-001`,
  `OBJ-006` and `TIM-002` reused.
- Taxonomy-change record: none. Clue disclosure fits Information and assignment
  validity fits Constraint without changing the six-type model.
- Candidate terms affected: exact run clue, ordered line satisfaction and
  binary fill / empty assignment now have bounded mappings.
- `INF-006` and `CON-018` are not duplicates: one describes what the instance
  reveals; the other describes which complete and partial states are valid.
- Claim IDs: `NON-010`.

## Negative results

The hidden-picture interpretation was rejected as `INF-003`: no decision-
relevant cell value exists behind the paper waiting for a reveal transition.
Cross marks were rejected as a separate action because they encode the empty
member of the same binary assignment domain. Recognisability of the final image
was rejected as an objective because clue satisfaction is sufficient.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Nonogram clues disclose ordered run lengths
  but not positions (`NON-001`, `NON-005`).
- [Confirmed | Corroborated | High] Every binary cell couples one row and one
  column constraint (`NON-003`, `NON-004`).
- [Observation | Corroborated | High] The apparent hidden picture is inferred,
  not a concealed current state revealed by play (`NON-007`).

## Нові гени

- [Observation | Corroborated | High] `CON-018` and `INF-006`.
- [Observation | Corroborated | High] `ACT-007`, `CON-001`, `INF-001`,
  `OBJ-006` and `TIM-002` are reused.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0008` — binary reconstruction from
  orthogonal ordered-run descriptions.

## Зміни таксономії

- [Observation | Corroborated | Medium] Змін таксономії немає. Clue semantics
  and assignment validity remain distinguishable Information and Constraint.

## Нові питання

- TODO: test whether colour Nonograms require a new separator constraint or
  only parameters of `CON-018`.
- TODO: compare an exact-sum line puzzle whose clues omit run order to sharpen
  the exclusion boundary of `INF-006`.
- TODO: audit whether Information / Constraint pairs are treated consistently
  across Minesweeper, Sudoku and Nonogram.

## Наступна рекомендована гра

- None before the scheduled eight-game taxonomy checkpoint.
- The next bounded unit is a corpus-wide audit of six gene types, gene
  boundaries, reuse and systematic classification distortion across
  `GAME-0001`–`GAME-0008`.
- `GAME-0009` must be selected only after that audit updates the research plan.

## Чому саме вона

- The plan explicitly schedules the first taxonomy checkpoint after eight
  reviewed games. Beginning another decomposition now would bypass the recorded
  quality gate and could compound any boundary inconsistency found in this
  first diverse sample.
