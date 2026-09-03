---
game_id: GAME-0073
slug: dominosa
game_title: Dominosa
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0073
gene_ids:
  action:
    - ACT-079
  system: []
  constraint:
    - CON-001
    - CON-119
    - CON-120
  information:
    - INF-001
  objective:
    - OBJ-006
  time:
    - TIM-002
---

# Game: Dominosa

## Analysis scope

- Version / ruleset: Simon Tatham's Portable Puzzle Collection, current
  standard desktop order-six `Basic` Dominosa puzzle, game ID
  `6:26324225316504330211040351263344652066136514454550102061`, from its
  fixed 8 × 7 number field to the accepted complete tiling.
- Included: pairing two orthogonally adjacent cells; removing or replacing a
  proposed pair; covering every cell exactly once; using every unordered
  number pair from `0-0` through `6-6` exactly once; fully visible state and
  self-paced solving.
- Excluded: Hard difficulty; other orders; forbidden-edge pencil marks, Solve,
  Undo, Redo, Restart and warning colours as interface support; setup
  generation as an in-solve mechanic; presentation and preferences.
- Direct-play status: the official JavaScript implementation was opened and
  its exact game ID captured. The current source and manual were inspected. An
  independent exact-cover solver found exactly one 28-domino tiling and
  separately demonstrated two disjoint placements with the same `2-6` type,
  proving that non-overlap alone is insufficient.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DOM-001` | Standard order six uses an 8 × 7 field containing 56 cells, and every digit 0–6 occurs eight times | Confirmed | Direct | High | P1, P2, P3, local control |
| `DOM-002` | One player placement pairs exactly two orthogonally adjacent cells as one domino | Confirmed | Direct | High | P1, P2 |
| `DOM-003` | A completed tiling covers every cell exactly once with 28 non-overlapping dominoes | Confirmed | Direct | High | P1, P2, local control |
| `DOM-004` | Every unordered pair from `0-0` through `6-6`, including doubles, occurs exactly once | Confirmed | Direct | High | P1, P2, local control |
| `DOM-005` | The recorded control has exactly one complete valid tiling | Observation | Direct | High | P1, P2, P3, local exhaustive control |
| `DOM-006` | Dominosa combines editable adjacent pairing, exact cell cover and exact-once pair identities | Observation | Corroborated | High | `DOM-001`–`DOM-005` |

## Basic data

- Release / origin: the official manual credits the puzzle to O. S. Adler;
  this record makes no broader historical priority claim.
- Platform or physical form: open-source desktop and official JavaScript
  single-player grid puzzle.
- Puzzle family: orthogonal domino exact cover with exact-once unordered pair
  identities.
- Primary sources:
  - **[P1] Simon Tatham:** [official Dominosa manual](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/dominosa.html),
    specifying adjacent pairing, complete coverage and one use of each domino.
  - **[P2] Simon Tatham:** [current `dominosa.c` implementation](https://git.tartarus.org/?p=simon/puzzles.git;a=blob;f=dominosa.c;hb=HEAD),
    defining the order-six Basic default, number multiplicities, pair set,
    input semantics and completion checks.
  - **[P3] Simon Tatham:** [official playable JavaScript version](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/dominosa.html),
    which produced the exact game ID used here.
- Secondary sources: none required for the bounded transition claims.
- Reproducible artefact: `scripts/verify_dominosa_control.py` reconstructs all
  legal adjacent placements, solves the joint cell-and-pair exact cover to a
  second-solution limit, validates the unique result and checks a duplicated
  pair-type counterexample.
- Claim IDs: `DOM-001`–`DOM-006`.

## Mechanical decomposition

### Action Genes

- `ACT-079` — toggle orthogonal adjacent-cell pairing. The player chooses one
  boundary between two edge-adjacent cells to place or remove a 1 × 2 domino.
- Marking a boundary impossible is optional notation rather than a separate
  mechanical action.
- Claim IDs: `DOM-002`, `DOM-006`.

### System Behaviour Genes

- Existing gene IDs: none.
- A placement records one proposed pair; automatic overlap replacement and
  violation highlighting are editor feedback, not puzzle-state production.
- Claim IDs: `DOM-002`, `DOM-003`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The control contains 56 immutable
  addressed cells in an 8 × 7 orthogonal topology.
- `CON-119` — exact-once adjacent-pair cover. Every cell must belong to exactly
  one selected orthogonal pair; no cell may be uncovered or shared.
- `CON-120` — complete unordered pair-type usage. Across the 28 selected
  dominoes, each unordered numeric type `(low, high)` for `0 ≤ low ≤ high ≤ 6`
  must occur exactly once.
- Claim IDs: `DOM-001`, `DOM-003`, `DOM-004`.

### Information Genes

- `INF-001` — fully visible current state. All 56 digits and every current
  selected or forbidden boundary remain inspectable before each edit.
- Claim IDs: `DOM-001`–`DOM-005`.

### Objective Genes

- `OBJ-006` — complete constraint-satisfying assignment. Acceptance requires
  the whole cell cover and the whole unordered pair inventory simultaneously.
- Claim IDs: `DOM-003`–`DOM-005`.

### Time Genes

- `TIM-002` — self-paced sequential action. Pair proposals can be revised
  without a deadline or autonomous state advance.
- Claim IDs: `DOM-002`, `DOM-005`.

## Reproducible transitions

Coordinates name rows `A`–`G` and columns `1`–`8`.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Empty control | pair `A1-A2` | adjacent digits `2` and `6` become one proposed domino | one input selects an orthogonal 1 × 2 relation | `DOM-002` |
| Pair `A1-A2` already selected | pair any placement using `A1` or `A2` | the proposals overlap and cannot coexist in a valid cover | cell capacity belongs to the pair cover, not only to the board | `DOM-003` |
| Pair `A1-A2` selected | also pair disjoint `D3-D4` | both placements spell unordered type `2-6`; geometry is legal but the joint proposal violates exact-once type usage | non-overlap is weaker than the domino inventory rule | `DOM-004` |
| Fixed control | assign the verifier's 28 printed placements | all 56 cells are covered once and all 28 unordered types occur once | one complete accepted tiling | `DOM-003`–`DOM-005` |
| Fixed control after first branching choice | continue exact-cover search to a second solution or exhaustion | no second satisfying tiling remains | the recorded control is unique, not merely solvable | `DOM-005` |

The verifier prints the full 7 × 8 domino-label matrix and every coordinate /
number pair, then independently asserts coverage, adjacency, inventory and
uniqueness.

## Strategic and experiential structure

- Local decision: eliminate a boundary when its number pair has already been
  committed elsewhere or either endpoint is already covered.
- Medium-term planning: treat every cell and every unordered number pair as a
  separate exact-cover column; a placement consumes one of each endpoint and
  one pair identity.
- Long-term structure: propagate rare pair identities and bottleneck cells
  together. A geometrically complete tiling may still duplicate one pair and
  omit another.
- Common heuristics: resolve digits with one remaining neighbour, then pair
  types with one remaining location; use contradiction on short alternating
  chains of possible dominoes.
- Failure attribution: uncovered cells, overlap, duplicate types and missing
  types are all visible consequences of the current proposal.
- Player-trust factors: digit order must not matter, doubles must count once,
  and no decorative gap may be mistaken for a selected boundary.
- Claim IDs: `DOM-002`–`DOM-005`.

## Replay and variation

- What changes between sessions: the visible number arrangement and unique
  tiling generated for the selected order and difficulty.
- Randomness or procedural generation: setup-only. The descriptive game ID
  makes this control deterministic.
- Multiple viable strategies: the same unique tiling can be derived by cell
  bottlenecks, pair-type bottlenecks or alternating exact-cover chains.
- Typical replay motive: solve a different visible exact-cover instance or use
  Hard generation, which requires deeper deductions.
- Claim IDs: `DOM-001`, `DOM-005`.

## Adjacent systems and history

- Sudoku and Dominosa both complete a visible exact assignment with exact-once
  identities, but Sudoku assigns symbols to cells inside all-different units;
  Dominosa selects spatial pairs that jointly consume cells and pair types.
- Nonogram assigns binary cells under line clues; Dominosa instead chooses a
  perfect matching of the grid and couples it to a global domino inventory.
- Slant also selects one local relation per cell and adds a global predicate;
  its global predicate is graph acyclicity rather than exact pair-type usage.
- Claim IDs: `DOM-003`, `DOM-004`, `DOM-006`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-079` | selected cell boundary; place / remove pair |
| System Behaviour | none | no automatic state transition |
| Constraint | `CON-001`, `CON-119`, `CON-120` | 56 cells; exact cover; unordered types 0–6 |
| Information | `INF-001` | visible digits and pair proposals |
| Objective | `OBJ-006` | satisfy the complete joint exact cover |
| Time | `TIM-002` | self-paced editing |

Canonical signature:

`ACT-079; none; CON-001,CON-119,CON-120; INF-001; OBJ-006; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `72` (`GAME-0001`–`GAME-0072`).
- Exact genome matches: none.
- Tied near matches: `GAME-0005` — Sudoku (`4 / 10 = 0.400000`); `GAME-0008` — Nonogram (`4 / 10 = 0.400000`); `GAME-0071` — Slant (`4 / 10 = 0.400000`).
- Supported combination subsets: `COMB-0073`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0005` — Sudoku | `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | Sudoku assigns symbols in intersecting all-different units; Dominosa selects adjacent pairs with a global type inventory | Near, `0.400000` |
| `GAME-0008` — Nonogram | `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | Nonogram satisfies ordered line runs; Dominosa satisfies cell and pair-type exact cover | Near, `0.400000` |
| `GAME-0071` — Slant | `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | Slant selects diagonals under degrees and acyclicity; Dominosa selects dominoes under two exact-once universes | Near, `0.400000` |

## Taxonomy impact

- Added `ACT-079`, `CON-119` and `CON-120` as active genes.
- Extended `CON-001`, `INF-001`, `OBJ-006` and `TIM-002` with bounded
  Dominosa support.
- Added `COMB-0073`; no existing record required split, merge or deprecation.

## Negative results

- The action is not selection from a finite physical domino hand: the pieces
  are latent relations between fixed numbered cells.
- Ordinary single-cell capacity does not express exact pair cover, because
  every accepted unit consumes two adjacent cells simultaneously.
- Exact cover does not imply exact pair-type usage: `A1-A2` and `D3-D4` are
  disjoint but duplicate `2-6`.
- Pair identity is unordered; `2-6` and `6-2` are the same required type.
- Forbidden-edge pencil marks and automatic overlap removal are notation and
  editor policy, not new genes.
- Basic procedural generation is setup provenance, not runtime randomness.
