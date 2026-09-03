---
game_id: GAME-0075
slug: light-up
game_title: Light Up
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0075
gene_ids:
  action:
    - ACT-007
  system:
    - SYS-111
  constraint:
    - CON-001
    - CON-123
    - CON-124
    - CON-125
  information:
    - INF-001
  objective:
    - OBJ-006
  time:
    - TIM-002
---

# Game: Light Up

## Analysis scope

- Version / ruleset: Simon Tatham's Portable Puzzle Collection, current default
  `7 × 7 Easy`, game ID `7x7:e0a21c0w1c2BaBe`, from its fixed field to the
  accepted unique seven-bulb assignment.
- Included: toggling bulbs in white cells; orthogonal illumination until a
  black wall; exact bulb counts next to numbered walls; mutual bulb-visibility
  exclusion; illumination of every white cell; complete visibility, revision
  and self-paced solving.
- Excluded: Tricky and Hard; other dimensions, wall densities and symmetries;
  right-click non-bulb marks, red error highlights, Solve, Undo, Redo and
  Restart as interface support; generation during solving and presentation.
- Direct-play status: the official playable page and manual were inspected.
  The exact ID was generated from current source with deterministic seed
  `epsilon`. An independent solver decoded 41 white cells, eight walls and six
  numbered walls, then proved exactly one valid seven-bulb assignment.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `LUP-001` | The current default is `7 × 7 Easy` with 20% target black-square density and fourfold rotational symmetry | Confirmed | Direct | High | P1, P2, P3 |
| `LUP-002` | A bulb illuminates its own white cell and visible orthogonal white cells until a black square blocks the ray | Confirmed | Direct | High | P1, P2, P3 |
| `LUP-003` | Every numbered black square requires exactly that many orthogonally adjacent bulbs | Confirmed | Direct | High | P1, P2 |
| `LUP-004` | Two bulbs may not illuminate each other | Confirmed | Direct | High | P1, P2 |
| `LUP-005` | Every non-black square must be illuminated | Confirmed | Direct | High | P1, P2 |
| `LUP-006` | The recorded control has exactly one complete seven-bulb solution | Observation | Direct | High | P1, P2, P3, local exhaustive control |
| `LUP-007` | Light Up combines visible ray coverage with exact local cardinality and mutual visibility exclusion | Observation | Corroborated | High | `LUP-002`–`LUP-006` |

## Basic data

- Release / origin: the official manual credits Nikoli; James Harvey
  contributed this implementation to Simon Tatham's collection.
- Platform or physical form: open-source desktop and official JavaScript
  single-player binary-assignment puzzle.
- Puzzle family: orthogonal illumination cover under exact wall counts and
  mutual source visibility exclusion.
- Primary sources:
  - **[P1] Simon Tatham:** [official Light Up manual](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/lightup.html),
    specifying illumination, blocking walls, all-white coverage, mutual
    exclusion, exact numbered-wall adjacency and controls.
  - **[P2] Simon Tatham / James Harvey:** [current `lightup.c` implementation](https://git.tartarus.org/?p=simon/puzzles.git;a=blob;f=lightup.c;hb=HEAD),
    defining the default preset, codec, ray geometry, clue checks and generator.
  - **[P3] Simon Tatham:** [official playable JavaScript version](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/lightup.html),
    confirming the current visible rules and input.
- Secondary sources: none required.
- Reproducible artefact: `scripts/verify_light_up_control.py` decodes the exact
  field, derives every wall-bounded visibility set and clue neighbourhood,
  enumerates bulb assignments to a second-solution limit and checks the three
  independent completion predicates.
- Claim IDs: `LUP-001`–`LUP-007`.

## Mechanical decomposition

### Action Genes

- `ACT-007` — assign symbol to open position. A white cell receives the binary
  proposal bulb / no bulb; clicking again removes the bulb.
- The optional dot is excluded notation, not a required solution symbol.
- Claim IDs: `LUP-002`, `LUP-006`.

### System Behaviour Genes

- `SYS-111` — wall-bounded orthogonal illumination propagation. Each proposed
  bulb deterministically lights its own cell and every white cell on four rays
  until the boundary or first black wall.
- Claim IDs: `LUP-002`, `LUP-007`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The control exposes 49 addressed cells,
  41 white assignment positions and eight immutable black walls.
- `CON-123` — exact orthogonal-neighbour assignment cardinality. Each numbered
  wall requires exactly its displayed count of bulbs in existing cardinally
  adjacent white cells.
- `CON-124` — mutual source visibility exclusion. No bulb may occur in the
  wall-bounded orthogonal visibility set of another bulb.
- `CON-125` — complete visibility-ray coverage. Every white cell must belong to
  the illumination set of at least one selected bulb.
- Claim IDs: `LUP-001`, `LUP-003`–`LUP-005`.

### Information Genes

- `INF-001` — fully visible current state. Walls, clues, bulbs and illumination
  are visible before every revision.
- Claim IDs: `LUP-001`–`LUP-006`.

### Objective Genes

- `OBJ-006` — complete constraint-satisfying assignment. Acceptance requires
  all clue counts, no mutually visible bulb pair and illumination of every
  white cell simultaneously.
- Claim IDs: `LUP-003`–`LUP-006`.

### Time Genes

- `TIM-002` — self-paced sequential action. No clock or autonomous step
  advances between assignments.
- Claim IDs: `LUP-006`.

## Reproducible transitions

Coordinates name rows `A`–`G` and columns `1`–`7`.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Empty control | place bulb at `A1` | `A1` and visible cells through `A5` and down through `G1` light; wall `A6` stops the row ray | illumination propagates orthogonally and walls occlude it | `LUP-002` |
| Bulb at `A1` | also place bulb at `A5` | the two bulbs see and illuminate each other, invalidating the proposal | light coverage does not override mutual source exclusion | `LUP-004` |
| Clue-0 wall `A6` | place bulb at adjacent `A5` | its local bulb count becomes one instead of zero | wall clues count orthogonally adjacent bulbs exactly | `LUP-003` |
| Fixed control | assign bulbs at `A1,B3,C1,D7,E2,F5,G6` | every white cell is lit, no bulb sees another and all six clues are exact | one complete accepted assignment | `LUP-002`–`LUP-006` |
| Fixed control after first branch | search to second solution or exhaustion | no second satisfying bulb set remains | the recorded control is unique | `LUP-006` |

The verifier independently asserts 41 coverage predicates, every pairwise
visibility exclusion, six exact clue equations and uniqueness.

## Strategic and experiential structure

- Local deduction: clue zero forbids adjacent bulbs; saturated clues forbid
  further neighbours; unmet clues can force remaining candidates.
- Ray deduction: an unlit cell may force the only white position capable of
  illuminating it, but that source can affect a long row and column.
- Global coupling: one bulb simultaneously covers several cells, excludes
  every visible source position and contributes to adjacent wall clues.
- Failure is legible because darkness, conflicting bulbs and incorrect clue
  counts identify different predicates.
- Claim IDs: `LUP-002`–`LUP-007`.

## Replay and variation

- Generated walls, numbered subsets and clues change both visibility segments
  and local equations.
- Width, height, black-square percentage, symmetry and difficulty are setup
  parameters outside the bounded default control.
- Easy constrains generator solvability technique, not the transition rules.
- Claim IDs: `LUP-001`, `LUP-006`.

## Adjacent systems and history

- Lights Out also uses lamps and a binary field, but one press flips a local
  neighbourhood toward a fixed all-off pattern; Light Up assigns stationary
  sources whose wall-bounded rays define coverage and exclusion.
- Slant, Sudoku and Nonogram share complete visible assignments under exact
  constraints but not illumination propagation.
- Bridges shares orthogonal wall-like occlusion boundaries only superficially:
  its objects are weighted edges and it seeks graph connectivity.
- Claim IDs: `LUP-002`–`LUP-007`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-007` | white cell; bulb / no bulb |
| System Behaviour | `SYS-111` | four rays; first-wall occlusion |
| Constraint | `CON-001`, `CON-123`, `CON-124`, `CON-125` | 41 white cells; six clues |
| Information | `INF-001` | visible clues, sources and lit field |
| Objective | `OBJ-006` | satisfy all three predicates |
| Time | `TIM-002` | self-paced editing |

Canonical signature:

`ACT-007; SYS-111; CON-001,CON-123,CON-124,CON-125; INF-001; OBJ-006; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `74` (`GAME-0001`–`GAME-0074`).
- Exact genome matches: none.
- Tied near matches: `GAME-0005` — Sudoku (`5 / 11 = 0.454545`); `GAME-0008` — Nonogram (`5 / 11 = 0.454545`); `GAME-0071` — Slant (`5 / 11 = 0.454545`).
- Supported combination subsets: `COMB-0075`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0005` — Sudoku | `ACT-007`, `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | Sudoku assigns digits under all-different units; Light Up assigns ray sources under coverage and visibility predicates | Near, `0.454545` |
| `GAME-0008` — Nonogram | `ACT-007`, `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | Nonogram reconstructs ordered filled runs; Light Up propagates illumination from sparse sources | Near, `0.454545` |
| `GAME-0071` — Slant | `ACT-007`, `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | Slant assigns one diagonal per cell and forbids cycles; Light Up permits empty cells and requires visible-ray cover | Near, `0.454545` |

## Taxonomy impact

- Added `SYS-111`, `CON-123`, `CON-124`, `CON-125` and `COMB-0075`.
- Extended `ACT-007`, `CON-001`, `INF-001`, `OBJ-006` and `TIM-002`.
- No existing record required split, merge or deprecation.

## Negative results

- Illumination is not hidden-ray probing: the entire field and deterministic
  ray result are visible, so `SYS-105` is absent.
- Mutual visibility exclusion is not ordinary occupancy or route crossing; it
  forbids sources anywhere on one unobstructed row / column segment.
- Exact numbered-wall adjacency is not graph incident degree: bulbs occupy
  cells rather than edges terminating at a vertex.
- Complete illumination is not graph connectivity and does not require every
  white cell to contain an object.
- Optional non-bulb dots and red warnings do not enter the required genome.
