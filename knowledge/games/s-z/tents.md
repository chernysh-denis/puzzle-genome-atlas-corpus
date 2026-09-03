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

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `71` (`GAME-0001`–`GAME-0071`).
- Exact genome matches: none.
- Tied near matches: `GAME-0062` — Hexologic (`6 / 10 = 0.600000`).
- Supported combination subsets: `COMB-0072`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0062` — Hexologic | `ACT-007`, `CON-001`, `CON-109`, `INF-001`, `OBJ-006`, `TIM-002` | Hexologic assigns one-to-three pip values and exposes directional sum clues; Tents assigns binary occupancy and adds separation plus tree matching | Near, `0.600000` |

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
