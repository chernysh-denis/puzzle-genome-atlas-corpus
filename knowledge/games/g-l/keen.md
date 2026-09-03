---
game_id: GAME-0080
slug: keen
game_title: Keen
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0080
gene_ids:
  action:
    - ACT-007
  system: []
  constraint:
    - CON-001
    - CON-010
    - CON-132
  information:
    - INF-001
  objective:
    - OBJ-006
  time:
    - TIM-002
---

# Game: Keen

## Analysis scope

- Version / ruleset: Simon Tatham's Portable Puzzle Collection, current desktop
  default `6 × 6 Normal`, exact game ID
  `6dn:a__a__a_14ba4_a4ca__a__b__,d3a9m180d3s1d3a11a7m10s1s2d3m24a9s4m12`.
- Included: assigning or clearing one digit from 1 through 6; all-different
  rows and columns; 16 fixed connected cages; exact addition, multiplication,
  subtraction and division clues; complete visibility, revision and self-paced
  solving.
- Excluded: multiplication-only *Inshi No Heya*; other sizes, difficulties and
  generated instances; pencil marks, error highlighting, keyboard navigation,
  Solve, Undo, Redo and Restart as interface support.
- Direct-play status: current official manual, JavaScript version and source
  were inspected. The control was generated from source revision
  `3c3632259d298ab62aafa8a5858823569ab1af46` with seed `202608140080`.
  An independent row-permutation solver decoded every cage, exhausted the
  search at a second-solution limit and proved exactly one completion.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `KEN-001` | The current desktop default is `6 × 6 Normal`, not multiplication-only | Confirmed | Direct | High | P1, P2, P3 |
| `KEN-002` | Each row and column contains each digit 1–6 exactly once | Confirmed | Direct | High | P1, P2 |
| `KEN-003` | Every fixed cage combines its digits to the displayed target with its displayed operation | Confirmed | Direct | High | P1, P2 |
| `KEN-004` | Subtraction and division cages contain two cells and accept either digit order | Confirmed | Direct | High | P1, P2 |
| `KEN-005` | A cage may repeat a digit when those occurrences share neither row nor column | Confirmed | Direct | High | P1, P2 |
| `KEN-006` | The exact control has 16 cages, four of each operation, and one unique completion | Observation | Direct | High | P2, local exhaustive control |
| `KEN-007` | Latin coverage and cage arithmetic constrain the same assignments simultaneously | Observation | Corroborated | High | `KEN-002`–`KEN-006` |

## Basic data

- Release / origin: the collection manual identifies the newspaper puzzle as
  *KenKen* and the multiplication-only variant as *Inshi No Heya*.
- Platform or physical form: open-source desktop and official JavaScript
  single-player arithmetic Latin-square puzzle.
- Puzzle family: complete Latin-square assignment under connected arithmetic
  cage equations.
- Primary sources:
  - **[P1] Simon Tatham:** [official Keen manual](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/keen.html),
    specifying the digit domain, row and column uniqueness and all four cage
    operations.
  - **[P2] Simon Tatham:** [current `keen.c` implementation](https://git.tartarus.org/?p=simon/puzzles.git;a=blob;f=keen.c;hb=HEAD),
    defining the default, codec, generator, solver and completion check.
  - **[P3] Simon Tatham:** [official playable JavaScript version](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/keen.html),
    confirming the current default presentation and editing semantics.
- Reproducible artefact: `scripts/verify_keen_control.py` independently decodes
  the block structure and clues, enumerates Latin-compatible row permutations
  to a second-solution limit and verifies every final cage equation.
- Claim IDs: `KEN-001`–`KEN-007`.

## Mechanical decomposition

### Action Genes

- `ACT-007` — assign symbol to open position. The player records one digit
  from 1 through 6 in one cell, then may clear or replace that proposal.
- Pencil marks retain hypotheses but do not assign the cell, so they remain an
  excluded reasoning aid rather than another mechanical action.
- Claim IDs: `KEN-002`, `KEN-006`.

### System Behaviour Genes

- None promoted. A main digit persists directly; conflict colouring only
  reports a violated row, column or cage and performs no state transformation.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The control preserves exactly 36
  individually addressable cells and 16 immutable cage memberships.
- `CON-010` — all-different unit coverage. Every six-cell row and column must
  contain the complete domain 1–6 exactly once.
- `CON-132` — exact arithmetic cage evaluation. Every fixed connected cage
  must evaluate to its displayed target under its displayed operation.
  Addition and multiplication accept any cage size present in the control;
  subtraction is absolute difference and division is integer quotient in
  either order for two-cell cages.
- Cage clues constrain equations rather than pre-assigning cell values, so
  `CON-009` does not apply.
- Claim IDs: `KEN-002`–`KEN-007`.

### Information Genes

- `INF-001` — fully visible current state. The complete grid, cage boundaries,
  operation targets and every current digit remain visible before each entry.
- Claim IDs: `KEN-001`, `KEN-003`, `KEN-006`.

### Objective Genes

- `OBJ-006` — complete constraint-satisfying assignment. All 36 cells must be
  assigned while all 12 Latin units and all 16 cage equations hold together.
- Claim IDs: `KEN-002`–`KEN-007`.

### Time Genes

- `TIM-002` — self-paced sequential action. No clock or autonomous state step
  advances between digit revisions.
- Claim IDs: `KEN-006`, `KEN-007`.

## Reproducible transitions

Coordinates use rows `A`–`F` and columns `1`–`6`.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Blank `A1` in cage `A1-A2 = 3÷` | assign `6` to `A1` and `2` to `A2` | the quotient cage is satisfied | direct assignment and order-insensitive division | `KEN-003`, `KEN-004` |
| The same cage | swap its two digits | `2` and `6` still satisfy `3÷` | cage order is not operand order | `KEN-004` |
| Blank cage `A3-B3 = 9+` | assign `4` and `5` | the cage sum is nine while both values also enter their row and column units | simultaneous arithmetic and Latin constraints | `KEN-002`, `KEN-003`, `KEN-007` |
| Cage `A4,B4,B5,C4 = 180×` | assign solution digits `5,2,3,6` | their product is 180 and the repeated-unit rules remain satisfied | a four-cell multiplication cage | `KEN-003`, `KEN-006` |
| Fixed control | enter the verifier's 36-cell solution | every row and column is 1–6 and all 16 cages evaluate exactly | complete accepted assignment | `KEN-002`, `KEN-003`, `KEN-006` |
| Fixed control after the first solution | continue exhaustive search | every alternative row permutation conflicts with a column or cage before another completion | unique recorded solution | `KEN-006` |

The exact solution is `624513 / 415236 / 531624 / 246351 / 362145 /
153462`. The verifier asserts all rows, columns, cage memberships, targets,
operation semantics and exhaustion after the first solution.

## Strategic and experiential structure

- Latin propagation: every placement removes one digit from the remaining
  domain of its row and column.
- Cage factoring: multiplication and division restrict factor pairs, while
  addition and subtraction restrict additive pairs or tuples.
- Cross-constraint coupling: a cage may permit several arithmetic tuples, but
  row and column exclusions decide which tuple and ordering survive.
- Repetition boundary: equal digits can occur in one cage when the cells do
  not share a Latin unit; a cage is not itself all-different.
- Claim IDs: `KEN-002`–`KEN-007`.

## Replay and variation

- Generated cage geometry, operation distribution and targets change the
  arithmetic decompositions without changing the scoped gene set.
- Grid size and difficulty are setup parameters. Multiplication-only mode is a
  named excluded ruleset because it removes three operation classes.
- Pencil automation and mistake highlighting change assistance, not the
  canonical completion predicate.
- Claim IDs: `KEN-001`, `KEN-003`, `KEN-006`.

## Adjacent systems and history

- Sudoku shares direct digit assignment and all-different units, but adds
  immutable given digits and fixed subgrid units instead of arithmetic cages.
- Hexologic also combines cell assignments through exact numeric clues, but
  its domain is 1–3, repetition is unrestricted and only overlapping sums are
  required; it has no all-different units.
- Filling induces regions from equal labels and sizes each by its digit; Keen
  fixes cage boundaries before play and evaluates their values arithmetically.
- Claim IDs: `KEN-002`–`KEN-007`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-007` | digit 1–6; assign / clear |
| System Behaviour | none | conflict colour is feedback |
| Constraint | `CON-001`, `CON-010`, `CON-132` | 36 cells; 12 Latin units; 16 cages |
| Information | `INF-001` | visible grid, cages, clues and assignments |
| Objective | `OBJ-006` | complete valid arithmetic Latin square |
| Time | `TIM-002` | self-paced editing |

Canonical signature:

`ACT-007; CON-001,CON-010,CON-132; INF-001; OBJ-006; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `79` (`GAME-0001`–`GAME-0079`).
- Exact genome matches: none.
- Tied near matches: `GAME-0005` — Sudoku (`6 / 8 = 0.750000`).
- Supported combination subsets: `COMB-0080`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0005` — Sudoku | `ACT-007`, `CON-001`, `CON-010`, `INF-001`, `OBJ-006`, `TIM-002` | immutable givens and 3 × 3 all-different boxes replace arithmetic cages | Near, `0.750000` |

## Taxonomy impact

- Added `CON-132` and `COMB-0080`.
- Extended `ACT-007`, `CON-001`, `CON-010`, `INF-001`, `OBJ-006` and
  `TIM-002`.
- No existing record required split, merge or deprecation.

## Negative results

- Cage boundaries and targets are immutable information and constraints, not
  player-authored region actions.
- A cage may legally repeat a digit, so `CON-010` applies only to rows and
  columns, never to cages.
- A cage clue narrows several values jointly and is not an immutable cell
  assignment; `CON-009` is absent.
- Conflict highlighting reports invalidity and does not automatically change
  any digit, so no System Behaviour gene is promoted.
