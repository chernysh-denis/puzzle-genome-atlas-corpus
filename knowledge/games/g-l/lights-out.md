---
game_id: GAME-0069
slug: lights-out
game_title: Lights Out
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0069
gene_ids:
  action:
    - ACT-077
  system:
    - SYS-109
  constraint:
    - CON-001
    - CON-004
    - CON-005
  information:
    - INF-001
  objective:
    - OBJ-004
  time:
    - TIM-002
---

# Game: Lights Out

## Analysis scope

- Version / ruleset: Tiger Electronics' original `5 × 5` handheld Lights Out,
  one ordinary solvable board from a fixed displayed pattern until every light
  is off.
- Included: 25 addressed on / off buttons; pressing either a lit or unlit
  button; simultaneous inversion of the pressed button and its existing
  orthogonal neighbours; clipped corner and edge neighbourhoods; complete
  visible state; repeated presses; all-off completion; self-paced play and the
  fewest-press ideal as a strategy criterion.
- Excluded: the handheld's Mode 2 random selection and Mode 3 authoring as
  separate game structures; puzzle progression, minimum-step display, Help,
  save memory, sound and inactivity shutdown; opening chase animation; Deluxe,
  Mini, 2000, Cube and Game.com editions; hints, score metagame and speed play.
- Direct-play status: no physical handheld was operated. The bounded transition
  system was reproduced from Tiger's official instruction scan, the primary
  patent and published algebraic models. The control state is `11111 / 10101 /
  11011 / 10101 / 11111`; pressing `A1, A5, B3, C2, C4, D3, E1, E5` in any
  order turns every light off.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `LGT-001` | The classic Tiger device has one square `5 × 5` field of 25 two-state lights that are also buttons | Confirmed | Direct | High | P1, P2, A1 |
| `LGT-002` | Pressing one button inverts that button and every existing neighbour directly above, below, left or right | Confirmed | Direct | High | P1, P2, A1 |
| `LGT-003` | Corner and edge presses are clipped by the field boundary rather than wrapping to another row or edge | Confirmed | Corroborated | High | P1, P2, local control |
| `LGT-004` | The ordinary objective is to transform the complete visible pattern into all lights off | Confirmed | Direct | High | P1, P2, A1 |
| `LGT-005` | Press order is immaterial and pressing one button twice cancels because state addition occurs over `GF(2)` | Confirmed | Corroborated | High | A1, A2, local control |
| `LGT-006` | The `5 × 5` toggle matrix has rank 23 and nullity 2, so every solvable state has four press-set solutions and only one quarter of all visible states can reach all-off | Confirmed | Corroborated | High | A2, local control |
| `LGT-007` | The control border pattern has four solutions and an eight-press minimum; the single-lit-corner state is not solvable | Observation | Corroborated | High | local exhaustive control |
| `LGT-008` | Lights Out reuses invariant reachability and primitive reversibility while adding addressed binary press and atomic neighbourhood-toggle boundaries | Observation | Corroborated | High | `LGT-001`–`LGT-007` |

## Basic data

- Release / origin: Tiger Electronics issued the classic handheld in 1995.
- Platform or physical form: a stand-alone electronic device with a square
  grid of illuminated push buttons and separate mode controls.
- Puzzle family: binary linear neighbourhood toggling.
- Primary and official sources:
  - **[P1] Tiger Electronics / Hasbro:** [Lights Out instruction manual](https://www.hasbro.com/common/instruct/LIGHTOUT.PDF).
    The original instruction scan directly specifies the all-off objective,
    on / off inversion, self-plus-adjacent effect, 25 numbered buttons and
    solvable pre-programmed puzzles.
  - **[P2] Michael Ganor:** [US Patent 5,417,425, “Puzzle device”](https://patents.google.com/patent/US5417425A/en).
    The primary patent specifies selectable two-state indicators, preferred
    `4 × 4` or `5 × 5` arrays and the selected-plus-orthogonal-neighbour
    transition pattern.
- Formal and academic sources:
  - **[A1] Anna Adamaszek et al.:** [“Lights Out on graphs”](https://doi.org/10.1007/s00591-021-00297-5),
    *Mathematische Semesterberichte* 69, 2022. It identifies the 1995 Tiger
    `5 × 5` edition and formalises every press as addition of one closed-
    neighbourhood column over `GF(2)`, proving order independence, even-press
    cancellation and the reachability test.
  - **[A2] William Boyles:** [“Most Clicks Problem in Lights Out”](https://arxiv.org/abs/2201.03452).
    It treats the commercial `5 × 5` grid, records nullity 2, four solutions per
    solvable position and the proper solvable subspace.
- Reproducible artefact: `scripts/verify_lights_out_control.py` constructs and
  row-reduces the exact `25 × 25` binary toggle matrix.
- Claim IDs: `LGT-001`–`LGT-008`.

## Mechanical decomposition

### Action Genes

- `ACT-077` — press addressed binary-state cell. The player chooses any one of
  the 25 current buttons. A lit and an unlit button are equally legal inputs;
  the command names a position, not a desired value.
- `ACT-007` does not apply. The player does not assign a proposed on / off
  symbol to only that cell, and no editable hypothesis layer exists.
- Claim IDs: `LGT-001`, `LGT-002`, `LGT-008`.

### System Behaviour Genes

- `SYS-109` — simultaneous closed-neighbourhood binary toggle. One press
  atomically flips the selected cell plus its orthogonal neighbours. Interior,
  edge and corner actions therefore affect five, four and three cells.
- The response is fixed by position and XOR state. It neither follows connected
  lit regions nor activates a changing linkage graph.
- Claim IDs: `LGT-002`, `LGT-003`, `LGT-005`, `LGT-008`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The same 25 addressed positions persist
  throughout the puzzle; only their binary states change.
- `CON-004` — invariant-constrained reachability. The classic matrix has rank
  23, so its image contains `2^23 = 8,388,608` of the `2^25 = 33,554,432`
  visible states. Two independent parity invariants partition all patterns into
  four reachability classes.
- `CON-005` — primitive action reversibility. Pressing the same position twice
  XORs the same neighbourhood twice and restores the immediately prior state.
- The manual promises solvable pre-programmed boards, but the transition rule
  itself does not make every representable pattern solvable.
- Claim IDs: `LGT-001`, `LGT-003`, `LGT-005`–`LGT-007`.

### Information Genes

- `INF-001` — fully visible current state. Every lit and unlit button is visible
  before each press; no secret state or future random successor is required to
  evaluate the immediate result.
- The invariant class is not explicitly displayed, but it is derived from the
  complete visible pattern rather than hidden information.
- Claim IDs: `LGT-001`, `LGT-004`.

### Objective Genes

- `OBJ-004` — reconstruct specified configuration. All 25 persistent binary
  components must match the one declared all-off state.
- Fewest presses is an optimisation criterion in the manual, not a separate
  authored threshold in this scoped board.
- Claim IDs: `LGT-004`, `LGT-007`.

### Time Genes

- `TIM-002` — self-paced sequential action. The board waits unchanged between
  inputs, and one neighbourhood toggle resolves completely before another
  button may be pressed.
- Animation, sound and inactivity shutdown do not add a decision-time system.
- Claim IDs: `LGT-002`, `LGT-005`.

## Reproducible transitions

Rows are `A`–`E`, columns are `1`–`5`; `1` means lit and `0` unlit. The fixed
control begins as `11111 / 10101 / 11011 / 10101 / 11111`.

| Before | Press | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| All off | `C3` | `C3`, `B3`, `D3`, `C2`, `C4` become lit; all other buttons remain off | selected-plus-orthogonal atomic stencil | `LGT-002` |
| Any state | `A1` | only `A1`, `A2` and `B1` invert | boundary clipping at a corner | `LGT-003` |
| Any state | `C3`, then `C3` | the second press restores every affected bit | primitive self-inverse action | `LGT-005` |
| Control border state | `A1, A5, B3, C2, C4, D3, E1, E5` | every cell becomes `0` | one exact minimum solution | `LGT-004`, `LGT-007` |
| Same control state | the same eight positions in reverse order | every cell again becomes `0` | commutative press composition | `LGT-005` |
| Only `A1` lit | solve `Na = i` over `GF(2)` | inconsistent system; no press set reaches all-off | invariant reachability boundary | `LGT-006`, `LGT-007` |

The verifier row-reduces the matrix to rank 23, enumerates the four affine
solutions of the control state, confirms their press counts `8, 8, 8, 16`,
checks reverse-order equality and double-press cancellation, and rejects the
single-corner state.

## Strategic and experiential structure

- Local decision: choose one button while accounting for every current light
  in its cross, not merely the selected cell.
- Medium-term planning: exploit cancellation and commutativity, often deciding
  a row's presses from the unresolved row above rather than reacting to the
  visually brightest area.
- Long-term structure: identify one press-set vector in the target state's
  affine solution class, then prefer the member with least Hamming weight.
- Failure attribution: reaching a nearly dark board can be misleading; the
  last one or two lights may lie in another invariant class and cannot be fixed
  by local intuition alone.
- Player-trust factors: every identical cell press must apply the same clipped
  cross, simultaneous changes must not cascade, and a pre-programmed board must
  belong to the all-off reachability class.
- Claim IDs: `LGT-002`–`LGT-007`.

## Replay and variation

- What changes between ordinary boards: only the initial reachable binary
  pattern and its minimum solution length; topology, toggle matrix and target
  remain fixed.
- Randomness or procedural generation: excluded from the bounded transition
  sequence. Mode 2 may select a new puzzle before play, but no random event
  occurs after the fixed state is displayed.
- Multiple viable strategies: row chasing, Gaussian elimination, memorised
  invariant patterns and direct search all compose the same commutative press
  set. A solvable `5 × 5` state has four algebraic solutions.
- Typical replay motive: solve another pattern, reduce the press count or learn
  the relationships between visible motifs and parity classes.
- Claim IDs: `LGT-005`–`LGT-007`.

## Adjacent systems and history

- Rubik's Cube is the nearest prior complete genome. Both expose a visible
  fixed field, reversible primitive transformations, global unreachable states
  and a specified solved configuration. Cube directly rotates coupled layers;
  Lights Out addresses one cell and the system applies a binary cross toggle.
- HOOK also begins from a visible trigger field, but pressing a trigger starts
  linked swept retraction and irreversibly removes mechanisms. Linkage can span
  remote positions and collision matters; Lights Out uses one fixed local
  stencil and XOR cancellation.
- Hexcells Infinite uses binary cells and orthogonal clue reasoning, but the
  player asserts concealed truth one cell at a time. A correct assertion is
  retained; it does not invert a visible neighbourhood or preserve a toggle
  invariant.
- KAMI changes a connected region chosen by current colour and coalesces it
  with adjacent regions. Lights Out ignores connected components and toggles a
  fixed geometric cross even when its states differ.
- Claim IDs: `LGT-005`, `LGT-008`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-077` | any addressed lit or unlit cell |
| System Behaviour | `SYS-109` | self plus clipped orthogonal neighbourhood |
| Constraint | `CON-001`, `CON-004`, `CON-005` | 25 fixed cells; rank-23 image; self-inverse press |
| Information | `INF-001` | complete visible binary field |
| Objective | `OBJ-004` | all 25 lights off |
| Time | `TIM-002` | self-paced fully resolved presses |

Canonical signature:

`ACT-077; SYS-109; CON-001,CON-004,CON-005; INF-001; OBJ-004; TIM-002`

## Corpus comparison

- Indexed games scanned: `GAME-0001`–`GAME-0068`.
- Indexed combinations scanned: `COMB-0001`–`COMB-0068`.
- Exact genome matches: none.
- Unique nearest game: `GAME-0002` Rubik's Cube at `6 / 9 = 0.666667`,
  sharing fixed capacity, invariant reachability, primitive reversibility,
  complete current visibility, configuration reconstruction and self-paced
  action.
- Near match: `GAME-0002` is the sole maximum-score prior genome; no other
  record ties it.
- Next matches: `GAME-0006` Sokoban at `4 / 13 = 0.307692`; then Sudoku,
  Nonogram and Rush Hour at `3 / 12 = 0.250000` each.
- Supported prior combination subsets: none. `COMB-0002` additionally requires
  direct layer rotation `ACT-002`, which Lights Out replaces with `ACT-077` and
  `SYS-109`.
- Full numeric scan (`intersection / union = Jaccard`):
  - `GAME-0001`: `2 / 20 = 0.100000`; `GAME-0002`: `6 / 9 = 0.666667`; `GAME-0003`: `1 / 16 = 0.062500`; `GAME-0004`: `2 / 21 = 0.095238`.
  - `GAME-0005`: `3 / 12 = 0.250000`; `GAME-0006`: `4 / 13 = 0.307692`; `GAME-0007`: `3 / 13 = 0.230769`; `GAME-0008`: `3 / 12 = 0.250000`.
  - `GAME-0009`: `2 / 22 = 0.090909`; `GAME-0010`: `2 / 15 = 0.133333`; `GAME-0011`: `3 / 18 = 0.166667`; `GAME-0012`: `3 / 14 = 0.214286`.
  - `GAME-0013`: `2 / 19 = 0.105263`; `GAME-0014`: `2 / 21 = 0.095238`; `GAME-0015`: `2 / 20 = 0.100000`; `GAME-0016`: `2 / 21 = 0.095238`.
  - `GAME-0017`: `0 / 21 = 0.000000`; `GAME-0018`: `1 / 26 = 0.038462`; `GAME-0019`: `3 / 15 = 0.200000`; `GAME-0020`: `1 / 21 = 0.047619`.
  - `GAME-0021`: `1 / 16 = 0.062500`; `GAME-0022`: `1 / 19 = 0.052632`; `GAME-0023`: `1 / 17 = 0.058824`; `GAME-0024`: `2 / 18 = 0.111111`.
  - `GAME-0025`: `1 / 18 = 0.055556`; `GAME-0026`: `1 / 19 = 0.052632`; `GAME-0027`: `2 / 18 = 0.111111`; `GAME-0028`: `2 / 23 = 0.086957`.
  - `GAME-0029`: `2 / 18 = 0.111111`; `GAME-0030`: `1 / 21 = 0.047619`; `GAME-0031`: `1 / 18 = 0.055556`; `GAME-0032`: `2 / 17 = 0.117647`.
  - `GAME-0033`: `1 / 20 = 0.050000`; `GAME-0034`: `1 / 21 = 0.047619`; `GAME-0035`: `1 / 25 = 0.040000`; `GAME-0036`: `3 / 17 = 0.176471`.
  - `GAME-0037`: `2 / 15 = 0.133333`; `GAME-0038`: `1 / 23 = 0.043478`; `GAME-0039`: `3 / 14 = 0.214286`; `GAME-0040`: `2 / 14 = 0.142857`.
  - `GAME-0041`: `1 / 18 = 0.055556`; `GAME-0042`: `1 / 16 = 0.062500`; `GAME-0043`: `2 / 20 = 0.100000`; `GAME-0044`: `3 / 15 = 0.200000`.
  - `GAME-0045`: `2 / 20 = 0.100000`; `GAME-0046`: `2 / 16 = 0.125000`; `GAME-0047`: `2 / 20 = 0.100000`; `GAME-0048`: `2 / 20 = 0.100000`.
  - `GAME-0049`: `1 / 16 = 0.062500`; `GAME-0050`: `2 / 21 = 0.095238`; `GAME-0051`: `1 / 23 = 0.043478`; `GAME-0052`: `1 / 17 = 0.058824`.
  - `GAME-0053`: `3 / 14 = 0.214286`; `GAME-0054`: `2 / 17 = 0.117647`; `GAME-0055`: `2 / 16 = 0.125000`; `GAME-0056`: `2 / 14 = 0.142857`.
  - `GAME-0057`: `2 / 14 = 0.142857`; `GAME-0058`: `3 / 14 = 0.214286`; `GAME-0059`: `2 / 13 = 0.153846`; `GAME-0060`: `1 / 14 = 0.071429`.
  - `GAME-0061`: `3 / 15 = 0.200000`; `GAME-0062`: `3 / 13 = 0.230769`; `GAME-0063`: `3 / 12 = 0.250000`; `GAME-0064`: `2 / 11 = 0.181818`.
  - `GAME-0065`: `1 / 14 = 0.071429`; `GAME-0066`: `1 / 17 = 0.058824`; `GAME-0067`: `0 / 16 = 0.000000`; `GAME-0068`: `1 / 15 = 0.066667`.
- Interpretation: Lights Out becomes the second independent carrier of
  `CON-004` and `CON-005`, validating that reachability invariants and primitive
  reversibility generalise beyond permutation puzzles while preserving a clear
  action / system boundary.

## Taxonomy impact

- Added `ACT-077` and `SYS-109`.
- Reused `CON-001`, `CON-004`, `CON-005`, `INF-001`, `OBJ-004` and `TIM-002`.
- Expanded `CON-004`, `CON-005` and `OBJ-004` evidence beyond Rubik's Cube or
  object-arrangement puzzles without changing their operational definitions.
- Registered `COMB-0069` as a verified interaction. At the individual-gene
  level, invariant reachability and primitive reversibility now have two
  independent game carriers.

## Negative results

- A pressed cell is not an editable binary assignment and does not instantiate
  `ACT-007`.
- Neighbour changes are simultaneous; newly lit buttons do not cascade within
  the same press.
- Only orthogonal neighbours change. Diagonal cells and wrapped opposite-edge
  cells remain untouched.
- Not every visible `5 × 5` binary pattern is solvable; random visual artwork
  or user-authored states cannot be assumed valid.
- The fewest-press ideal does not create an authored finite budget or failure
  threshold for the scoped board.

## Delta summary

- New game: `GAME-0069` Lights Out.
- New genes: `ACT-077`, `SYS-109`.
- Reused genes: `CON-001`, `CON-004`, `CON-005`, `INF-001`, `OBJ-004`,
  `TIM-002`.
- New combination: `COMB-0069`.
- New reproducible artefact: `scripts/verify_lights_out_control.py`.
- Nearest prior genome: Rubik's Cube at `6 / 9 = 0.666667`; no exact match and
  no earlier supported combination subset.

## Нові факти

- Одне натискання одночасно інвертує вибрану кнопку та наявних ортогональних
  сусідів; порядок натискань не має значення, а подвійне натискання скасовується.
- Для класичного поля `5 × 5` ранг матриці дорівнює 23: до all-off належить
  лише чверть усіх видимих станів, а кожен розв'язний стан має чотири набори
  натискань.
- Контрольна світна рамка розв'язується мінімум за вісім натискань; стан з
  єдиною світною кутовою кнопкою недосяжний до all-off.

## Нові гени

- `ACT-077` — натиснути адресовану клітинку з бінарним станом.
- `SYS-109` — одночасно перемкнути замкнений ортогональний окіл.

## Нові комбінації

- `COMB-0069` — оборотне перемикання околу під інваріантами досяжності.

## Зміни таксономії

- `CON-004` і `CON-005` отримали другого незалежного носія поза перестановками
  Кубика Рубіка; `OBJ-004` тепер явно охоплює бінарний all-off стан.
