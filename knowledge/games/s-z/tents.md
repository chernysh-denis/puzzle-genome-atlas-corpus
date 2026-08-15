---
game_id: GAME-0072
slug: tents
game_title: Tents
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0072
gene_ids:
  action:
    - ACT-007
  system: []
  constraint:
    - CON-001
    - CON-109
    - CON-117
    - CON-118
  information:
    - INF-001
  objective:
    - OBJ-006
  time:
    - TIM-002
---

# Game: Tents

## Analysis scope

- Version / ruleset: Simon Tatham's Portable Puzzle Collection, current
  standard desktop `8 × 8 Easy` Tents puzzle, game ID
  `8x8:badecbgbin_ab,1,2,1,0,3,1,2,2,3,0,3,0,2,1,1,2`, from its fixed
  twelve-tree field to one accepted complete tent assignment.
- Included: choosing tent or empty for non-tree cells; exact row and column
  quotas; no horizontal, vertical or diagonal tent contact; existence of a
  bijection pairing every tent with one orthogonally adjacent tree; revisable
  entries; complete visible state and self-paced solving.
- Excluded: Tricky generation difficulty; other dimensions; Solve, Undo, Redo,
  Restart, drag-to-mark and warning colours as interface support; setup
  generation as an in-solve mechanic; presentation and preferences.
- Direct-play status: the current official JavaScript implementation was
  opened and its displayed game ID captured. The description codec and rules
  were independently reproduced from the current MIT-licensed source. A local
  exhaustive solver decoded twelve trees and sixteen quotas, found exactly one
  twelve-tent solution and separately rejected a set with local tree adjacency
  but no perfect tree-to-tent matching.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TNT-001` | The standard desktop preset is an `8 × 8 Easy` grid and the fixed control contains twelve trees | Confirmed | Direct | High | P1, P2, P3, local control |
| `TNT-002` | Every tent occupies a non-tree cell and no two tents touch in any of the eight neighbouring directions | Confirmed | Direct | High | P1, P2, local control |
| `TNT-003` | Every row and column contains exactly its displayed tent quota | Confirmed | Direct | High | P1, P2, local control |
| `TNT-004` | The complete tents and trees must admit a one-to-one pairing in which each pair is orthogonally adjacent | Confirmed | Direct | High | P1, P2, local control |
| `TNT-005` | The fixed control has exactly one complete twelve-tent assignment | Observation | Direct | High | P1, P2, P3, local exhaustive control |
| `TNT-006` | Tents adds exact line cardinality, king-neighbourhood exclusion and adjacency-constrained perfect matching while reusing visible binary assignment | Observation | Corroborated | High | `TNT-001`–`TNT-005` |

## Basic data

- Release / origin: Simon Tatham notes that the puzzle appears in several
  places and does not claim an identified inventor; this record covers his
  current implementation without making an origin claim.
- Platform or physical form: open-source desktop and official JavaScript
  single-player grid puzzle.
- Puzzle family: binary spatial assignment under exact line quotas,
  non-touching placement and tree-to-tent perfect matching.
- Primary sources:
  - **[P1] Simon Tatham:** [official Tents manual](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/tents.html),
    directly specifying equal tree / tent counts, one-to-one orthogonal pairing,
    eight-neighbour tent exclusion and exact side quotas.
  - **[P2] Simon Tatham:** [current `tents.c` implementation](https://git.tartarus.org/?p=simon/puzzles.git;a=blob;f=tents.c;hb=HEAD),
    defining the `8 × 8 Easy` default, description codec, matching solver,
    quota checks, adjacency checks and completion.
  - **[P3] Simon Tatham:** [official playable JavaScript version](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/tents.html),
    which produced the exact descriptive game ID used here.
- Secondary sources: none required for the bounded transition claims.
- Reproducible artefact: `scripts/verify_tents_control.py` decodes the board,
  enumerates quota-valid non-touching row assignments, checks a perfect
  matching and searches until a second solution or exhaustion.
- Claim IDs: `TNT-001`–`TNT-006`.

## Mechanical decomposition

### Action Genes

- `ACT-007` — assign symbol to open position. The player assigns a tent or an
  explicit non-tent mark to one non-tree cell, and may clear or replace it.
- Mouse-button cycling and green certainty marks are input / notation
  parameters, not separate mechanical actions.
- Claim IDs: `TNT-002`, `TNT-006`.

### System Behaviour Genes

- Existing gene IDs: none.
- A placement changes only that cell's proposal. Red warnings and matching
  highlights report violated predicates without transforming puzzle state.
- Claim IDs: `TNT-002`–`TNT-004`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The control has 64 addressed cells in
  one immutable `8 × 8` topology, twelve of them occupied by fixed trees.
- `CON-109` — overlapping exact line-aggregate satisfaction. Each row and each column
  requires exactly its displayed number of tent-valued cells; every placed
  tent contributes to both one row and one column equation.
- `CON-117` — king-neighbourhood exclusion for selected cells. Two tents may
  not occupy cells sharing an edge or a corner.
- `CON-118` — adjacency-constrained perfect bipartite matching. All twelve
  tents must be paired one-to-one with all twelve trees, and each pair must be
  orthogonally adjacent. A tent may still touch another tree not chosen as its
  pair.
- Claim IDs: `TNT-001`–`TNT-004`.

### Information Genes

- `INF-001` — fully visible current state. All trees, sixteen side quotas and
  current tent / non-tent marks remain inspectable before every edit.
- Matching identity need not be drawn: validity asks whether a perfect matching
  exists in the fully visible adjacency graph.
- Claim IDs: `TNT-001`–`TNT-005`.

### Objective Genes

- `OBJ-006` — complete constraint-satisfying assignment. The accepted field
  simultaneously meets every quota, excludes all tent contact and admits a
  complete tree-to-tent matching.
- Claim IDs: `TNT-002`–`TNT-005`.

### Time Genes

- `TIM-002` — self-paced sequential action. Marks may be placed, erased or
  revised without a deadline or autonomous world advance.
- Claim IDs: `TNT-002`, `TNT-005`.

## Reproducible transitions

Coordinates name rows `A`–`H` and columns `1`–`8`.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Empty non-tree cell `A2`, adjacent to tree `A3` | assign tent | `A2` becomes a tent candidate and its row / column counts each increase by one | one addressed binary assignment contributes to two exact quotas | `TNT-002`, `TNT-003` |
| Tent already at `A2` | assign tent to `B1`, `B2` or `B3` | the new tent shares an edge or corner with `A2`, so the assignment violates non-touching placement | exclusion uses the full eight-cell neighbourhood | `TNT-002` |
| Twelve proposed tents each lie beside at least one tree, but two trees depend on the same only available tent | evaluate matching | local adjacency succeeds for every tree, yet augmenting-path search cannot pair all twelve identities | local coverage is weaker than the required perfect matching | `TNT-004` |
| Fixed control | assign verifier solution `A2 A6 A8 / C2 C5 C8 / E1 E7 / F5 / G3 / H5 H7` | all row / column quotas are exact, no tents touch and all twelve tree pairs can be matched | one complete accepted assignment | `TNT-005` |
| Fixed control with the first undecided placement forced opposite | continue exhaustive row-option search | no second satisfying complete assignment remains | the recorded solution is unique, not merely one witness | `TNT-005` |

The verifier prints the exact eight rows and asserts uniqueness, all sixteen
quotas, eight-neighbour exclusion and perfect matching independently.

## Strategic and experiential structure

- Local decision: exclude every tree cell and every eight-neighbour cell around
  a placed tent; retain only cells orthogonally adjacent to at least one tree.
- Medium-term planning: use zero, saturated and deficit-equals-capacity side
  quotas across intersecting row and column candidate sets.
- Long-term structure: reason about groups of trees and their union of possible
  tent cells. A set of several trees needs at least as many distinct candidate
  tents, not merely one adjacent candidate per tree.
- Common heuristics: resolve zero lines, mark the full neighbourhood of every
  tent empty, then apply matching bottlenecks before guessing.
- Failure attribution: a touching warning, exceeded side count or deficient
  tree / tent group reflects a visible violated predicate; no hidden event
  changes the result.
- Player-trust factors: diagonal tent contact must be rejected, a tent adjacent
  to several trees must count once, and pairing must be global rather than a
  greedy nearest-tree choice.
- Claim IDs: `TNT-002`–`TNT-005`.

## Replay and variation

- What changes between sessions: tree positions, row / column quotas and the
  resulting unique tent assignment generated for the selected size.
- Randomness or procedural generation: setup-only. The descriptive game ID
  makes the bounded control deterministic.
- Multiple viable strategies: the same unique assignment can be derived in
  different orders; Easy generation is intended for direct deductions.
- Typical replay motive: solve a different visible constraint intersection or
  select Tricky, where deeper deductions are required.
- Claim IDs: `TNT-001`, `TNT-005`.

## Adjacent systems and history

- Nonogram and Tents both assign binary cells under overlapping row / column
  clues. Nonogram specifies ordered runs; Tents specifies only cardinalities,
  then couples them to trees and non-touching geometry.
- Slant likewise assigns one of two states per cell and mixes local with global
  predicates. Its global structure is graph acyclicity; Tents instead requires
  one perfect matching between two spatial identity sets.
- Sudoku shares exact completion across intersecting line units, but its units
  enforce all-different symbol coverage rather than selected-cell counts.
- Claim IDs: `TNT-003`, `TNT-004`, `TNT-006`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-007` | tent / explicit empty; revisable cell assignment |
| System Behaviour | none | no automatic state transition |
| Constraint | `CON-001`, `CON-109`, `CON-117`, `CON-118` | 64 cells; line quotas; no touching; perfect matching |
| Information | `INF-001` | visible trees, quotas and assignments |
| Objective | `OBJ-006` | satisfy all predicates over the complete field |
| Time | `TIM-002` | self-paced editing |

Canonical signature:

`ACT-007; none; CON-001,CON-109,CON-117,CON-118; INF-001; OBJ-006; TIM-002`

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`:
  `ACT-007; none; CON-001,CON-109,CON-117,CON-118; INF-001; OBJ-006; TIM-002`.
- Indexed games scanned: `GAME-0001`–`GAME-0071`.
- Indexed combinations scanned: `COMB-0001`–`COMB-0071`.
- Exact genome matches: none.
- Unique nearest game: `GAME-0062` Hexologic at `6 / 10 = 0.600000`, sharing
  assignment, fixed capacity, overlapping exact line aggregates, full
  visibility, complete constraint satisfaction and self-paced time.
- Next nearest games: `GAME-0005` Sudoku, `GAME-0008` Nonogram and
  `GAME-0071` Slant, each at `5 / 10 = 0.500000`.
- Supported combination subsets: none before `COMB-0072`; its three defining
  spatial predicates do not occur together in any earlier combination.
- Scan date: 2026-08-14.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0005` — Sudoku | `ACT-007`, `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | Sudoku covers all symbols in all-different units; Tents selects a quota subset with non-touching and perfect matching | tied near match, `5 / 10 = 0.500000` |
| `GAME-0008` — Nonogram | `ACT-007`, `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | Nonogram constrains ordered runs; Tents constrains cardinality plus spatial pairing | tied near match, `5 / 10 = 0.500000` |
| `GAME-0062` — Hexologic | `ACT-007`, `CON-001`, `CON-109`, `INF-001`, `OBJ-006`, `TIM-002` | Hexologic assigns one-to-three pip values and exposes directional sum clues; Tents assigns binary occupancy and adds separation plus tree matching | unique nearest, `6 / 10 = 0.600000` |
| `GAME-0071` — Slant | `ACT-007`, `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | Slant assigns graph edges under degree and acyclicity; Tents assigns occupancy under quotas, separation and matching | tied near match, `5 / 10 = 0.500000` |

- Full numeric scan (`intersection / union = Jaccard`):
  - `GAME-0001`: `2 / 20 = 0.100000`; `GAME-0002`: `3 / 12 = 0.250000`; `GAME-0003`: `1 / 16 = 0.062500`; `GAME-0004`: `2 / 21 = 0.095238`.
  - `GAME-0005`: `5 / 10 = 0.500000`; `GAME-0006`: `3 / 14 = 0.214286`; `GAME-0007`: `2 / 14 = 0.142857`; `GAME-0008`: `5 / 10 = 0.500000`.
  - `GAME-0009`: `2 / 22 = 0.090909`; `GAME-0010`: `2 / 15 = 0.133333`; `GAME-0011`: `3 / 18 = 0.166667`; `GAME-0012`: `4 / 13 = 0.307692`.
  - `GAME-0013`: `2 / 19 = 0.105263`; `GAME-0014`: `2 / 21 = 0.095238`; `GAME-0015`: `2 / 20 = 0.100000`; `GAME-0016`: `2 / 21 = 0.095238`.
  - `GAME-0017`: `0 / 21 = 0.000000`; `GAME-0018`: `1 / 26 = 0.038462`; `GAME-0019`: `2 / 16 = 0.125000`; `GAME-0020`: `1 / 21 = 0.047619`.
  - `GAME-0021`: `1 / 16 = 0.062500`; `GAME-0022`: `1 / 19 = 0.052632`; `GAME-0023`: `1 / 17 = 0.058824`; `GAME-0024`: `2 / 18 = 0.111111`.
  - `GAME-0025`: `1 / 18 = 0.055556`; `GAME-0026`: `1 / 19 = 0.052632`; `GAME-0027`: `2 / 18 = 0.111111`; `GAME-0028`: `2 / 23 = 0.086957`.
  - `GAME-0029`: `2 / 18 = 0.111111`; `GAME-0030`: `1 / 21 = 0.047619`; `GAME-0031`: `1 / 18 = 0.055556`; `GAME-0032`: `2 / 17 = 0.117647`.
  - `GAME-0033`: `1 / 20 = 0.050000`; `GAME-0034`: `1 / 21 = 0.047619`; `GAME-0035`: `1 / 25 = 0.040000`; `GAME-0036`: `2 / 18 = 0.111111`.
  - `GAME-0037`: `2 / 15 = 0.133333`; `GAME-0038`: `1 / 23 = 0.043478`; `GAME-0039`: `4 / 13 = 0.307692`; `GAME-0040`: `2 / 14 = 0.142857`.
  - `GAME-0041`: `1 / 18 = 0.055556`; `GAME-0042`: `1 / 16 = 0.062500`; `GAME-0043`: `2 / 20 = 0.100000`; `GAME-0044`: `2 / 16 = 0.125000`.
  - `GAME-0045`: `2 / 20 = 0.100000`; `GAME-0046`: `2 / 16 = 0.125000`; `GAME-0047`: `2 / 20 = 0.100000`; `GAME-0048`: `2 / 20 = 0.100000`.
  - `GAME-0049`: `1 / 16 = 0.062500`; `GAME-0050`: `2 / 21 = 0.095238`; `GAME-0051`: `1 / 23 = 0.043478`; `GAME-0052`: `1 / 17 = 0.058824`.
  - `GAME-0053`: `2 / 15 = 0.133333`; `GAME-0054`: `2 / 17 = 0.117647`; `GAME-0055`: `2 / 16 = 0.125000`; `GAME-0056`: `2 / 14 = 0.142857`.
  - `GAME-0057`: `2 / 14 = 0.142857`; `GAME-0058`: `2 / 15 = 0.133333`; `GAME-0059`: `2 / 13 = 0.153846`; `GAME-0060`: `1 / 14 = 0.071429`.
  - `GAME-0061`: `4 / 14 = 0.285714`; `GAME-0062`: `6 / 10 = 0.600000`; `GAME-0063`: `3 / 12 = 0.250000`; `GAME-0064`: `2 / 11 = 0.181818`.
  - `GAME-0065`: `1 / 14 = 0.071429`; `GAME-0066`: `2 / 16 = 0.125000`; `GAME-0067`: `0 / 16 = 0.000000`; `GAME-0068`: `1 / 15 = 0.066667`.
  - `GAME-0069`: `3 / 13 = 0.230769`; `GAME-0070`: `2 / 14 = 0.142857`; `GAME-0071`: `5 / 10 = 0.500000`.

## Taxonomy impact

- Originally added `CON-116`, `CON-117` and `CON-118`; normalisation later
  merged `CON-116` into parameterised line-aggregate gene `CON-109`.
- Extended `ACT-007`, `CON-001`, `INF-001`, `OBJ-006` and `TIM-002` with
  bounded Tents support.
- Added `COMB-0072`; no existing record required split, merge or deprecation.

## Negative results

- Tent-to-tree pairing is not an objective-only phrase: Hall-style bottlenecks
  can invalidate a complete quota-correct spatial proposal.
- The rule is not “exactly one adjacent tree per tent”. Extra adjacent trees
  are allowed if some complete one-to-one pairing exists.
- Side numbers are not ordered-run clues and therefore do not reuse `CON-018`.
- Red warnings, green non-tent marks and drag gestures do not add system genes.
- Easy procedural generation is setup provenance, not runtime randomness.

## Delta summary

- Added one reviewed game, three active genes and one verified combination.
- Added one exact control verifier and one rule-checked visual representation.
- Corpus size becomes 72 reviewed games, 391 active genes and 72 combinations.

## Нові факти

- Зафіксовано точний стандартний `8 × 8 Easy` control із дванадцятьма деревами
  та шістнадцятьма квотами.
- Незалежний перебір довів єдиний дванадцятимісний розв’язок і окремо показав,
  чому локальна суміжність не замінює взаємно-однозначного matching.

## Нові гени

- `CON-109` — точний агрегат значень у перетинних лініях; у Tents це сума
  бінарних індикаторів намету.
- `CON-117` — взаємне виключення вибраних клітин в околі короля.
- `CON-118` — досконале двочасткове matching за дозволеною суміжністю.

## Нові комбінації

- `COMB-0072` — повне розміщення під квотами, розділенням і matching.

## Зміни таксономії

- Під час первинного аналізу активовано три constraints; нормалізація 003
  пізніше об'єднала `CON-116` із `CON-109` без втрати правила Tents.
