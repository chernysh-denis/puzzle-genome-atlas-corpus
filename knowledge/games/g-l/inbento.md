---
game_id: GAME-0058
slug: inbento
game_title: inbento
analysis_status: reviewed
reviewed: 2026-08-13
combination_ids:
  - COMB-0058
gene_ids:
  action:
    - ACT-070
  system:
    - SYS-101
  constraint:
    - CON-001
    - CON-104
    - CON-105
  information:
    - INF-001
    - INF-011
  objective:
    - OBJ-004
  time:
    - TIM-001
---

# Game: inbento

## Analysis scope

- Version / ruleset: Afterburn's released base game, restricted to all nine
  authored puzzles of Chapter 1 / World 1.
- Included: one fixed rectangular bento grid and its initial contents; one
  visible target recipe; a finite visible cutting-board inventory of food
  pieces made from one or more orthogonally addressed ingredient blocks;
  selection, quarter-turn rotation and placement of an available piece; full-
  footprint container inclusion; overlap that replaces earlier ingredient
  blocks; mandatory use of every supplied piece; exact visible final-grid
  matching; undo and restart.
- Excluded: rotation-lock pieces introduced in Chapter 2; swap, move, grab and
  copy action pieces; every later ingredient and chapter; chapter-unlock
  thresholds, hidden level, achievements, story images, speedrunning and
  presentation.
- Direct-play status: not conducted. A peer-reviewed paper co-authored by the
  game's developer formalises the state, placement, rotation, replacement and
  completion rules. The official product page fixes the pattern-matching
  premise; a complete Chapter 1 index and four hands-on accounts independently
  corroborate the nine-puzzle scope, rotation, overlap, finite-piece order,
  recipe matching and recovery.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `INB-001` | Chapter 1 contains nine authored puzzles and serves as the complete basic-placement tutorial | Confirmed | Corroborated | High | P1, S1, S2 |
| `INB-002` | Every scoped puzzle exposes an initial bento grid, an exact recipe and a finite set of available food pieces | Confirmed | Direct | High | P1, P2 |
| `INB-003` | The player may select an available food piece, rotate it through quarter-turn orientations and place it at an addressed grid offset | Confirmed | Direct | High | P1, S2-S4 |
| `INB-004` | A placement is accepted only when every block of the transformed piece lies inside the bento boundary | Confirmed | Direct | High | P1 |
| `INB-005` | Accepted piece blocks replace the previous contents of every covered cell rather than stacking as simultaneously visible layers | Confirmed | Direct | High | P1, S2-S4 |
| `INB-006` | Every supplied piece must be used; the inventory therefore fixes the ordinary forward-action horizon | Confirmed | Direct | High | P1, S3 |
| `INB-007` | Completion requires the final visible bento grid to match the recipe exactly and contain no empty cells | Confirmed | Direct | High | P1, P2 |
| `INB-008` | Placement order can change the final grid because later food overwrites earlier food in shared cells | Confirmed | Corroborated | High | P1, S2-S4 |
| `INB-009` | All decision-relevant current pieces, grid cells and recipe cells are visible before placement | Observation | Corroborated | High | P1, P2, S2-S4 |
| `INB-010` | Undo restores a previous placement state and restart restores the authored initial puzzle | Confirmed | Corroborated | High | S3, S4 |

## Basic data

- Release / origin: Polish studio Afterburn released inbento on 3 September
  2019; the current official Steam page lists Afterburn as developer and
  publisher.
- Platform or physical form: deterministic single-player digital pattern-
  reconstruction puzzle on a small rectangular grid.
- Puzzle family: finite overlay-ordered recipe reconstruction.
- Primary and reproducible sources:
  - **[P1]** Łukasz Spierewka et al.,
    [Procedural Level Generation with Difficulty Level Estimation for inbento](https://www.iccs-meeting.org/archive/iccs2021/papers/127460103.pdf),
    ICCS 2021, pp. 1-3 and 8, for the exact recipe, bento and cutting-board
    state, all-piece requirement, rotation, container validation, replacement
    rule, filled final grids and nine-level chapter structure.
  - **[P2]** [Official inbento Steam page](https://store.steampowered.com/app/1567440/inbento/),
    for developer, release, product boundary and recipe-reconstruction premise.
- Hands-on and scope corroboration:
  - **[S1]** [inbento Wiki: World 1](https://inbento.fandom.com/wiki/World_1),
    for levels 1-1 through 1-9 and the placement, rotation and overlap tutorial
    boundary.
  - **[S2]** Andrew Brown,
    [inbento Review](https://playcritically.com/2023/07/02/inbento-review/),
    for the visible recipe, first-level baseline, finite pieces, rotation,
    overlap and replacement.
  - **[S3]** Russell Troxel,
    [inbento Review](https://www.russelltroxel.com/writing/2020/3/19/inbento-review),
    for visible initial grid, piece inventory, replacement, limited moves and
    undo.
  - **[S4]** [Witch's Review Corner: inbento](https://witchsreviewcorner.com/2021/07/14/inbento-review-switch/),
    for recipe display, empty or pre-filled boxes, overlap order and the later-
    mechanic exclusion boundary.
- Claim IDs: `INB-001`-`INB-010`.

## Mechanical decomposition

### Action Genes

- `ACT-070` - select, orient and place a finite footprint piece. The player
  chooses any remaining food piece, selects one of its permitted quarter-turn
  orientations and commits its anchor to a chosen bento offset.
- Parameters: piece identity, typed block footprint, orientation equivalence,
  anchor convention, placement offset and input method.
- Claim IDs: `INB-003`.

### System Behaviour Genes

- `SYS-101` - later-footprint overwrite of addressed cell contents. After a
  legal placement, each non-empty food block replaces the ingredient identity
  currently visible in its corresponding bento cell; unaffected cells persist.
- Resolution order: validate the full transformed footprint; consume and place
  the selected piece; overwrite covered cells simultaneously; then test the
  remaining inventory and exact target state.
- Parameters: empty piece blocks, replacement atomicity, visual transition and
  objective-check priority.
- Claim IDs: `INB-005`, `INB-008`.

### Constraint Genes

- `CON-001` - fixed occupancy capacity. Each puzzle preserves one authored
  finite bento lattice of individually addressed ingredient cells.
- `CON-104` - finite all-used construction inventory. Every ordinary placement
  consumes one selected supplied piece, no new piece is drawn in Chapter 1 and
  successful completion requires that none remain unused.
- `CON-105` - complete footprint must remain within the container. Overlap with
  food is legal, but any placement whose transformed non-empty footprint
  extends outside the bento is rejected and returned to the cutting board.
- Scarce strategic resources: the complete piece multiset and the last-write
  opportunity for every ingredient cell.
- Claim IDs: `INB-002`, `INB-004`, `INB-006`.

### Information Genes

- `INF-001` - fully visible current state: the current bento, its empty or
  filled cells and all remaining pieces are shown before each choice.
- `INF-011` - exact visible input-output assembly schema: the available typed
  footprints and the complete per-cell target recipe are disclosed together.
- Claim IDs: `INB-002`, `INB-009`.

### Objective Genes

- `OBJ-004` - reconstruct specified configuration. Use the supplied components
  to make every final visible bento cell equal the corresponding recipe cell.
- Success, evaluation and failure: after the final supplied piece resolves, the
  complete non-empty grid must equal the recipe. An unequal exhausted state is
  recoverable through undo or restart rather than a time-driven terminal loss.
- Claim IDs: `INB-006`, `INB-007`.

### Time Genes

- `TIM-001` - discrete turn with automatic resolution. One placement fully
  validates, consumes the piece, overwrites covered cells and checks completion
  before another piece may be selected.
- Claim IDs: `INB-003`-`INB-008`, `INB-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| One food piece remains on the cutting board | Rotate it by 90 degrees without placing | Its footprint orientation changes; bento contents and inventory do not | Orientation belongs to the selected placement action | `INB-003` |
| The selected footprint would cross the bento edge | Release it at that offset | The placement is rejected and the piece returns to the inventory | Full-footprint container inclusion | `INB-004` |
| A two-block piece covers one empty cell and one filled cell | Commit the legal placement | Both target cells take the incoming block identities; the previous covered ingredient disappears | Per-cell overwrite rather than exclusive packing | `INB-005` |
| Two available pieces can cover the same cell with different ingredients | Place A then B, versus B then A | The final shared-cell identity equals the later piece in each sequence | Placement order is mechanically material | `INB-008` |
| Final visible cells match the recipe but a supplied piece remains | Stop placing | The all-piece completion predicate is not yet satisfied | Inventory exhaustion is required, not optional efficiency | `INB-006` |
| No pieces remain and every visible cell matches the recipe | Resolve the final placement | The puzzle completes | Exact filled target reconstruction | `INB-007` |

## Strategic and experiential structure

- Local decision: choose a remaining footprint, orientation and legal offset.
- Medium-term planning: reserve final writes for cells whose target ingredient
  differs from unavoidable earlier coverage.
- Long-term structure: treat the target as a last-writer schedule over a fixed
  lattice rather than as a conventional non-overlapping packing problem.
- Common heuristics: place broad underlayers first, identify cells touched by
  several pieces, and postpone the piece that carries their required final
  identities.
- Failure attribution: wrong ingredient or empty target cells can be traced to
  an illegal footprint choice, unused component or incorrect overwrite order.
- Player-trust factors: complete current and target state, deterministic
  replacement, no timer, undo and restart.
- Claim IDs: `INB-002`-`INB-010`.

## Replay and variation

- What changes between sessions: nothing within a selected authored Chapter 1
  puzzle unless the player chooses a different placement order.
- Randomness or procedural generation: none in the released scoped levels; the
  cited paper's generator is research tooling, not part of this ruleset.
- Multiple viable strategies: some early tutorials admit symmetrical poses,
  but the analysis makes no universal uniqueness claim.
- Typical replay motive: try another legal construction order or replay the
  chapter; score, time and move optimisation are outside scope.
- Claim IDs: `INB-001`-`INB-010`.

## Adjacent systems and history

- Direct predecessor: Afterburn's Golf Peaks shares the studio's small visible
  finite-inventory puzzle design but not its spatial command grammar.
- Variants: later inbento chapters add locked orientation and swap, move, grab
  and copy pieces; none are projected backward into Chapter 1.
- Similar games: polyomino packing, exact target reconstruction and layered
  collage placement.
- Important differences: occupied bento cells do not block placement; the
  later food replaces them, making the order of complete footprints part of
  the solution. All supplied pieces must be consumed even if the visible target
  appears earlier.
- Claim IDs: `INB-001`-`INB-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-070` | selected piece, quarter-turn orientation and anchor |
| System Behaviour | `SYS-101` | atomic covered-cell overwrite |
| Constraint | `CON-001`, `CON-104`, `CON-105` | grid size, piece multiset and boundary test |
| Information | `INF-001`, `INF-011` | current grid, remaining inputs and exact recipe |
| Objective | `OBJ-004` | exact per-cell ingredient equality |
| Time | `TIM-001` | placement, overwrite and completion resolution |

Canonical signature:

`ACT-070; SYS-101; CON-001,CON-104,CON-105; INF-001,INF-011; OBJ-004; TIM-001`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `57` (`GAME-0001`–`GAME-0057`).
- Exact genome matches: none.
- Tied near matches: `GAME-0053` — Can of Wormholes (`4 / 14 = 0.285714`).
- Supported combination subsets: `COMB-0058`.
- Scan date: 2026-08-13.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0053` - Can of Wormholes | `CON-001`, `INF-001`, `OBJ-004`, `TIM-001` | ordered-body motion into one shape versus finite overlay footprints reconstructing typed cells | Near, `0.285714` |

### Preserved research notes

- New genes: `ACT-070`, `SYS-101`, `CON-104`, `CON-105`.
- Reused genes: `CON-001`, `INF-001`, `INF-011`, `OBJ-004`, `TIM-001`.
- Classification result: four `New gene` records and one new verified
  interaction; no novelty claim.

## Combination record

- `COMB-0058` captures exact visible recipe reconstruction through selectable
  finite footprint consumption and order-dependent covered-cell overwrite.
- Exhaustive supporter scan: only `GAME-0058` contains the complete proper
  subset; no previous verified combination is a subset of this genome.

## Taxonomy impact

- Generalised `INF-011` from machine input-output diagrams to an exact visible
  assembly schema independent of whether construction is automated. Generalised
  `OBJ-004` to include typed per-cell target identity. No prior signature
  changes.
- Added one Action, one System and two Constraint boundaries instead of
  treating overlay replacement or the mandatory finite inventory as ordinary
  non-overlapping packing.
- Taxonomy-change record: none; the existing definitions expand without moving
  or splitting an earlier supporter.
- Candidate terms affected: promote selectable finite footprint placement,
  covered-cell overwrite, all-used construction inventory and whole-footprint
  container inclusion.

## Negative results

- `ACT-026` rejected: inbento lets the player choose any remaining piece and
  permits overlap; it does not impose one mandatory supply-head tile.
- `CON-007` rejected: occupied cells are legal targets and are overwritten,
  whereas collision-valid transformation forbids overlap with fixed occupancy.
- `CON-020` rejected: exhaustion is part of the exact completion check and
  remains undoable, not a separately charged move allowance with immediate
  terminal failure.
- `CON-103` rejected: food pieces are persistent construction footprints, not
  spatial command cards that parameterise another moving entity.
