---
game_id: GAME-0079
slug: filling
game_title: Filling
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0079
gene_ids:
  action:
    - ACT-007
  system: []
  constraint:
    - CON-001
    - CON-009
    - CON-131
  information:
    - INF-001
  objective:
    - OBJ-006
  time:
    - TIM-002
---

# Game: Filling

## Analysis scope

- Version / ruleset: Simon Tatham's Portable Puzzle Collection, current desktop
  default `13 × 9`, exact game ID
  `13x9:7b424d7a4b77a4b3c4d3c7a43a6c2c5b73b646b5a47b888a6a3b7a77d8a7b8e4a2a3578e3b5e22`.
- Included: assigning or clearing one digit from 1 through 9 in an editable
  cell; immutable given digits; orthogonal equal-digit components; the rule
  that every component's area equals its digit; complete visibility, revision
  and self-paced solving.
- Excluded: multi-cell selection as input batching; error highlighting,
  pencils, keyboard navigation, Solve, Undo, Redo and Restart as interface
  support; other sizes and generated instances.
- Direct-play status: current official rules, JavaScript version and source
  were inspected. The control was generated from current source with seed
  `202608140079`. An independent exhaustive cell-value solver proved exactly
  one completion, then verified 47 givens and 27 valid regions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FIL-001` | The current desktop default is `13 × 9` | Confirmed | Direct | High | P1, P2, P3 |
| `FIL-002` | The player assigns or clears a digit from 1 through 9 in an editable cell | Confirmed | Direct | High | P1, P2, P3 |
| `FIL-003` | Equal digits connect only across orthogonal contacts, not diagonals | Confirmed | Direct | High | P1, P2 |
| `FIL-004` | Every orthogonally connected equal-digit region has area equal to that digit | Confirmed | Direct | High | P1, P2 |
| `FIL-005` | Given digits are immutable, while a completed region may contain multiple givens or none | Observation | Direct | High | P1, P2, local exhaustive control |
| `FIL-006` | The exact control has one unique completion with 47 givens and 27 regions | Observation | Direct | High | P1, P2, P3, local exhaustive control |
| `FIL-007` | Connectivity, equality and numeric area form one coupled region predicate | Observation | Corroborated | High | `FIL-003`–`FIL-006` |

## Basic data

- Release / origin: the manual credits Nikoli's *Fillomino* and Jonas Kölker
  for the collection implementation.
- Platform or physical form: open-source desktop and official JavaScript
  single-player numeric region-filling puzzle.
- Puzzle family: connected equal-label region completion under exact area
  values.
- Primary sources:
  - **[P1] Simon Tatham:** [official Filling manual](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/filling.html),
    specifying digit input, orthogonal regions and exact region area.
  - **[P2] Simon Tatham / Jonas Kölker:** [current `filling.c` implementation](https://git.tartarus.org/?p=simon/puzzles.git;a=blob;f=filling.c;hb=HEAD),
    defining defaults, codec, immutable clues and completion checks.
  - **[P3] Simon Tatham:** [official playable JavaScript version](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/filling.html),
    confirming current presentation and editing semantics.
- Secondary source: [Nikoli's official Fillomino description](https://www.nikoli.co.jp/en/puzzles/fillomino/).
- Reproducible artefact: `scripts/verify_filling_control.py` decodes all 117
  cells, preserves every given, enumerates assignments to a second-solution
  limit and verifies every final equal-digit component independently.
- Claim IDs: `FIL-001`–`FIL-007`.

## Mechanical decomposition

### Action Genes

- `ACT-007` — assign symbol to open position. The player places one numeric
  label from 1 through 9 in an editable cell or clears that assignment.
- Applying a digit to a temporary multi-cell selection batches the same action
  and does not create a distinct simultaneous-assignment mechanic.
- Claim IDs: `FIL-002`, `FIL-006`.

### System Behaviour Genes

- None promoted. A digit persists directly; conflict colouring only reports
  whether the current proposal violates a visible rule.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The control retains exactly 117 cells;
  assigning one cell never creates, removes or relocates a position.
- `CON-009` — immutable given assignments. The 47 printed digits cannot be
  cleared or replaced and constrain the editable cells around them.
- `CON-131` — connected equal-label region area equals label. Each maximal
  orthogonally connected component of digit `n` must contain exactly `n`
  cells. Equal diagonal neighbours remain separate regions.
- Claim IDs: `FIL-001`, `FIL-003`–`FIL-007`.

### Information Genes

- `INF-001` — fully visible current state. The grid, 47 givens and every
  current assignment remain visible throughout the solve.
- Claim IDs: `FIL-001`, `FIL-002`, `FIL-005`, `FIL-006`.

### Objective Genes

- `OBJ-006` — complete constraint-satisfying assignment. Every editable cell
  must contain a digit and all 27 induced regions must satisfy exact area.
- Claim IDs: `FIL-003`–`FIL-007`.

### Time Genes

- `TIM-002` — self-paced sequential action. No clock or autonomous state step
  advances between digit revisions.
- Claim IDs: `FIL-002`, `FIL-006`.

## Reproducible transitions

Coordinates use rows `A`–`I` and columns `1`–`13`.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Given `A1=7` | attempt to clear or overwrite `A1` | the printed value remains `7` | givens are immutable | `FIL-005` |
| Empty editable `A2` | assign `4` | `A2` joins `A3,A4,B2` into a four-cell component | direct digit assignment and exact area | `FIL-002`, `FIL-004` |
| Digit `7` at `A1` and `7` at `B2` | inspect their diagonal contact | the cells remain in different regions because they share no edge | diagonal equality does not connect | `FIL-003` |
| Editable `E13` | assign `1` | a one-cell component is complete without containing any original clue | regions are induced by assignments, not seeded one-to-one by clues | `FIL-005`, `FIL-007` |
| Fixed control | assign the verifier's complete 117-cell solution | all 27 components have areas `1` through `8` equal to their labels | complete accepted assignment | `FIL-003`–`FIL-006` |
| Fixed control after the first solution | continue exhaustive search to a second solution or exhaustion | every alternative branch violates a component bound or final exact-area check | the recorded completion is unique | `FIL-006` |

The verifier asserts the exact solution string, all fixed clues, component
connectedness, exact area, digit-region counts, the clue-free singleton at
`E13` and exhaustion after the first solution.

## Strategic and experiential structure

- Region growth: a digit proposes both the value of one cell and the target
  size of the component it may join.
- Separation: two same-valued cells may need another value between them to
  prevent an oversized component, while diagonal contact is harmless.
- Ghost regions: not every final component grows from a printed clue; the
  control's `E13=1` region must be inferred entirely from surrounding limits.
- Global coupling: locally viable components compete for the same remaining
  cells, so exact areas constrain the complete partition.
- Claim IDs: `FIL-003`–`FIL-007`.

## Replay and variation

- Generated clue positions, values and multiplicity change the component
  geometry and which clue-free regions must be inferred.
- Width and height are setup parameters outside the bounded default control.
- The maximum digit is nine because the interface stores single decimal
  labels; the control happens to use no nine-region.
- Claim IDs: `FIL-001`, `FIL-005`, `FIL-006`.

## Adjacent systems and history

- Sudoku shares digit assignment, immutable clues and global completion, but
  constrains fixed rows, columns and boxes instead of components induced by
  equal values.
- Map colours fixed pre-existing regions and excludes equal colours across an
  adjacency edge; Filling creates the regions from equal cell labels and
  requires each region's area to equal that label.
- Galaxies creates variable regions through selected boundaries around centre
  dots; Filling has no boundary action or one-centre-per-region predicate.
- Claim IDs: `FIL-002`–`FIL-007`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-007` | digit 1–9; assign / clear |
| System Behaviour | none | conflict colour is feedback |
| Constraint | `CON-001`, `CON-009`, `CON-131` | 117 cells; 47 givens; exact component area |
| Information | `INF-001` | visible grid, givens and assignments |
| Objective | `OBJ-006` | complete valid numeric partition |
| Time | `TIM-002` | self-paced editing |

Canonical signature:

`ACT-007; CON-001,CON-009,CON-131; INF-001; OBJ-006; TIM-002`

## Corpus comparison

- Indexed games and combinations scanned: `GAME-0001`–`GAME-0078` and
  `COMB-0001`–`COMB-0078`.
- Exact genome matches: none.
- Near matches: `GAME-0005` Sudoku and `GAME-0077` Map tie at the positive
  maximum, `6 / 8 = 0.750000`.
- Nearest prior games: Sudoku and Map tie at `6 / 8 = 0.750000`.
- Next near games: Nonogram and Slant tie at `5 / 9 = 0.555556`; Hexologic
  and Tents tie at `5 / 10 = 0.500000`.
- Supported combination subsets: none before `COMB-0079`.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0005` — Sudoku | `ACT-007`, `CON-001`, `CON-009`, `INF-001`, `OBJ-006`, `TIM-002` | fixed all-different rows, columns and boxes instead of induced equal-digit regions | tied nearest, `6 / 8 = 0.750000` |
| `GAME-0077` — Map | `ACT-007`, `CON-001`, `CON-009`, `INF-001`, `OBJ-006`, `TIM-002` | assigns four colours to fixed regions under adjacency exclusion | tied nearest, `6 / 8 = 0.750000` |
| `GAME-0008` — Nonogram | `ACT-007`, `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | binary cell marks satisfy ordered row and column runs | tied next, `5 / 9 = 0.555556` |
| `GAME-0071` — Slant | `ACT-007`, `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | assigns diagonals under vertex degrees and global acyclicity | tied next, `5 / 9 = 0.555556` |
| `GAME-0078` — Galaxies | `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | draws boundaries around centre-seeded half-turn-symmetric regions | `4 / 10 = 0.400000` |

- Full numeric scan (`intersection / union = Jaccard`):
  - `GAME-0001`: `2 / 19 = 0.105263`; `GAME-0002`: `3 / 11 = 0.272727`; `GAME-0003`: `1 / 15 = 0.066667`; `GAME-0004`: `2 / 20 = 0.100000`; `GAME-0005`: `6 / 8 = 0.750000`; `GAME-0006`: `3 / 13 = 0.230769`; `GAME-0007`: `2 / 13 = 0.153846`; `GAME-0008`: `5 / 9 = 0.555556`.
  - `GAME-0009`: `2 / 21 = 0.095238`; `GAME-0010`: `2 / 14 = 0.142857`; `GAME-0011`: `3 / 17 = 0.176471`; `GAME-0012`: `4 / 12 = 0.333333`; `GAME-0013`: `2 / 18 = 0.111111`; `GAME-0014`: `2 / 20 = 0.100000`; `GAME-0015`: `2 / 19 = 0.105263`; `GAME-0016`: `2 / 20 = 0.100000`.
  - `GAME-0017`: `0 / 20 = 0.000000`; `GAME-0018`: `1 / 25 = 0.040000`; `GAME-0019`: `2 / 15 = 0.133333`; `GAME-0020`: `1 / 20 = 0.050000`; `GAME-0021`: `1 / 15 = 0.066667`; `GAME-0022`: `1 / 18 = 0.055556`; `GAME-0023`: `1 / 16 = 0.062500`; `GAME-0024`: `2 / 17 = 0.117647`.
  - `GAME-0025`: `1 / 17 = 0.058824`; `GAME-0026`: `1 / 18 = 0.055556`; `GAME-0027`: `2 / 17 = 0.117647`; `GAME-0028`: `2 / 22 = 0.090909`; `GAME-0029`: `2 / 17 = 0.117647`; `GAME-0030`: `1 / 20 = 0.050000`; `GAME-0031`: `1 / 17 = 0.058824`; `GAME-0032`: `2 / 16 = 0.125000`.
  - `GAME-0033`: `1 / 19 = 0.052632`; `GAME-0034`: `1 / 20 = 0.050000`; `GAME-0035`: `1 / 24 = 0.041667`; `GAME-0036`: `2 / 17 = 0.117647`; `GAME-0037`: `2 / 14 = 0.142857`; `GAME-0038`: `1 / 22 = 0.045455`; `GAME-0039`: `4 / 12 = 0.333333`; `GAME-0040`: `2 / 13 = 0.153846`.
  - `GAME-0041`: `1 / 17 = 0.058824`; `GAME-0042`: `1 / 15 = 0.066667`; `GAME-0043`: `2 / 19 = 0.105263`; `GAME-0044`: `2 / 15 = 0.133333`; `GAME-0045`: `2 / 19 = 0.105263`; `GAME-0046`: `2 / 15 = 0.133333`; `GAME-0047`: `2 / 19 = 0.105263`; `GAME-0048`: `2 / 19 = 0.105263`.
  - `GAME-0049`: `1 / 15 = 0.066667`; `GAME-0050`: `2 / 20 = 0.100000`; `GAME-0051`: `1 / 22 = 0.045455`; `GAME-0052`: `1 / 16 = 0.062500`; `GAME-0053`: `2 / 14 = 0.142857`; `GAME-0054`: `2 / 16 = 0.125000`; `GAME-0055`: `2 / 15 = 0.133333`; `GAME-0056`: `2 / 13 = 0.153846`.
  - `GAME-0057`: `2 / 13 = 0.153846`; `GAME-0058`: `2 / 14 = 0.142857`; `GAME-0059`: `2 / 12 = 0.166667`; `GAME-0060`: `1 / 13 = 0.076923`; `GAME-0061`: `4 / 13 = 0.307692`; `GAME-0062`: `5 / 10 = 0.500000`; `GAME-0063`: `3 / 11 = 0.272727`; `GAME-0064`: `2 / 10 = 0.200000`.
  - `GAME-0065`: `1 / 13 = 0.076923`; `GAME-0066`: `2 / 15 = 0.133333`; `GAME-0067`: `0 / 15 = 0.000000`; `GAME-0068`: `1 / 14 = 0.071429`; `GAME-0069`: `3 / 12 = 0.250000`; `GAME-0070`: `2 / 13 = 0.153846`; `GAME-0071`: `5 / 9 = 0.555556`; `GAME-0072`: `5 / 10 = 0.500000`.
  - `GAME-0073`: `4 / 10 = 0.400000`; `GAME-0074`: `4 / 12 = 0.333333`; `GAME-0075`: `5 / 11 = 0.454545`; `GAME-0076`: `4 / 10 = 0.400000`; `GAME-0077`: `6 / 8 = 0.750000`; `GAME-0078`: `4 / 10 = 0.400000`.
- Scan date: 2026-08-14.

## Taxonomy impact

- Added `CON-131` and `COMB-0079`.
- Extended `ACT-007`, `CON-001`, `CON-009`, `INF-001`, `OBJ-006` and
  `TIM-002`.
- No existing record required split, merge or deprecation.

## Negative results

- Multi-cell selection batches repeated symbol assignments, so it does not add
  a new mass-assignment Action gene.
- Conflict highlighting reports the current proposal and does not transform
  decision state, so no System Behaviour gene is promoted.
- The regions are induced by equal digits rather than pre-drawn boundaries.
- One clue-free singleton proves that the game does not require one given per
  component: `CON-009` governs only fixed cells, while `CON-131` governs every
  final component.
- Diagonal equal digits do not share a region.

## Delta summary

- Added one reviewed game, one active gene and one verified combination.
- Added one exact-control verifier and one deterministic rule-valid artwork.
- Corpus size becomes 79 reviewed games, 408 active genes and 79 combinations.

## Нові факти

- Зафіксовано точний стандартний контроль зі 117 клітинами, 47 незмінними
  підказками та 27 зв’язними регіонами.
- Незалежний повний перебір довів один розв’язок і один регіон без початкової
  підказки: ізольовану одиницю в `E13`.

## Нові гени

- `CON-131` — площа зв’язного регіону однакових міток дорівнює самій мітці.

## Нові комбінації

- `COMB-0079` — повне числове заповнення під незмінними підказками й
  саморозмірними регіонами однакових міток.

## Зміни таксономії

- Нову межу активовано без зміни попередніх визначень.

## Open ambiguities

- None at the current evidence threshold. Multi-cell input and optional error
  display remain outside the bounded mechanic.

## Sources

1. Simon Tatham, [official Filling manual](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/filling.html).
2. Simon Tatham / Jonas Kölker, [current `filling.c` implementation](https://git.tartarus.org/?p=simon/puzzles.git;a=blob;f=filling.c;hb=HEAD).
3. Simon Tatham, [official playable Filling](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/filling.html).
4. Nikoli, [Fillomino](https://www.nikoli.co.jp/en/puzzles/fillomino/).
5. Local control verifier: `scripts/verify_filling_control.py`.

## Verification status

- Structure validated locally against the repository schema.
- Claims `FIL-001`–`FIL-005` are supported by current official rules, source
  and presentation.
- Claims `FIL-006`–`FIL-007` are independently checked on the exact control.
- Full corpus comparison completed through `GAME-0078`.
