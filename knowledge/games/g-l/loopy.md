---
game_id: GAME-0076
slug: loopy
game_title: Loopy
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0076
gene_ids:
  action:
    - ACT-081
  system: []
  constraint:
    - CON-001
    - CON-126
    - CON-127
  information:
    - INF-001
  objective:
    - OBJ-006
  time:
    - TIM-002
---

# Game: Loopy

## Analysis scope

- Version / ruleset: Simon Tatham's Portable Puzzle Collection, current default
  desktop `10 × 10 Squares — Easy`, exact game ID
  `10x10t0:a3b2a222d12223a33b23e3a221b3a2b2c3b0b2a12a2b222a1a2c3e1b3a2b1a2d333a2002a`,
  from its fixed 11 × 11 dot lattice to the accepted single loop.
- Included: independently selecting or clearing any of 220 permitted square-
  grid edges; exact selected-edge counts around 45 numbered faces; the global
  requirement that all 112 selected edges form one unbroken simple cycle;
  complete visibility, revision and self-paced solving.
- Excluded: Normal, Tricky and Hard; other dimensions and non-square tilings;
  right-click exclusion marks, auto-follow, error colours, Solve, Undo, Redo
  and Restart as interface support; generation and presentation.
- Direct-play status: the official current manual, JavaScript version and
  source were inspected. The exact control was generated from current source
  with deterministic seed `202608140076`. An independent solver decoded all
  100 faces and 220 edges, proved exactly one valid 112-edge solution and
  separately checked every clue, vertex degree and connected component.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `LOO-001` | The current desktop default is `10 × 10 Squares — Easy` | Confirmed | Direct | High | P1, P2, P3 |
| `LOO-002` | The player independently marks fixed permitted edges as loop / unknown, with optional explicit exclusion notation | Confirmed | Direct | High | P1, P2, P3 |
| `LOO-003` | Each numbered face requires exactly that many of its boundary edges in the loop | Confirmed | Direct | High | P1, P2 |
| `LOO-004` | Completion requires one unbroken loop containing every selected edge | Confirmed | Direct | High | P1, P2 |
| `LOO-005` | The recorded control has one unique 112-edge single-cycle solution | Observation | Direct | High | P1, P2, P3, local exhaustive control |
| `LOO-006` | Exact local face counts and global single-cycle topology are independent completion predicates | Observation | Corroborated | High | `LOO-003`–`LOO-005` |

## Basic data

- Release / origin: the manual credits Nikoli for the basic Slitherlink puzzle
  idea, Mike Pinna for the original collection implementation and Lambros
  Lambrou for later non-square tilings.
- Platform or physical form: open-source desktop and official JavaScript
  single-player edge-assignment puzzle.
- Puzzle family: single-cycle graph completion under exact face-boundary clues.
- Primary sources:
  - **[P1] Simon Tatham:** [official Loopy manual](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/loopy.html),
    specifying the single-loop objective, face clues and controls.
  - **[P2] Simon Tatham / Mike Pinna / Lambros Lambrou:** [current `loopy.c` implementation](https://git.tartarus.org/?p=simon/puzzles.git;a=blob;f=loopy.c;hb=HEAD),
    defining default parameters, codec, generation and completion checks.
  - **[P3] Simon Tatham:** [official playable JavaScript version](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/loopy.html),
    confirming current presentation and independent edge input.
- Secondary sources: none required.
- Reproducible artefact: `scripts/verify_loopy_control.py` decodes the exact
  square-grid instance, propagates face equations and vertex-degree domains,
  enumerates valid subgraphs to a second-solution limit and independently
  verifies one non-empty connected degree-two component.
- Claim IDs: `LOO-001`–`LOO-006`.

## Mechanical decomposition

### Action Genes

- `ACT-081` — toggle independently addressed binary edge. Each permitted
  lattice segment is edited without tracing from an endpoint or modifying a
  neighbour automatically.
- The right-click excluded state is optional working notation, not a required
  solution value.
- Claim IDs: `LOO-002`, `LOO-005`.

### System Behaviour Genes

- None promoted. In the scoped default, an edge edit persists directly; clue
  colouring and optional auto-follow are excluded interface assistance.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The instance exposes 121 fixed dots,
  220 independently addressed edges and 100 faces.
- `CON-126` — exact selected-edge cardinality around marked face. Each of 45
  numbered squares counts its four shared boundary edges exactly.
- `CON-127` — exactly one simple selected-edge cycle. Every selected vertex
  has degree two and all 112 selected edges belong to one component.
- Claim IDs: `LOO-001`, `LOO-003`–`LOO-006`.

### Information Genes

- `INF-001` — fully visible current state. The complete grid, every number and
  every current edge mark remain visible before each revision.
- Claim IDs: `LOO-001`–`LOO-005`.

### Objective Genes

- `OBJ-006` — complete constraint-satisfying assignment. Acceptance requires
  all marked-face counts and the single-cycle predicate simultaneously.
- Claim IDs: `LOO-003`–`LOO-006`.

### Time Genes

- `TIM-002` — self-paced sequential action. No timer or autonomous simulation
  advances between edge edits.
- Claim IDs: `LOO-002`, `LOO-005`.

## Reproducible transitions

Coordinates name face rows `A`–`J` and columns `1`–`10`.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Empty control | select the top edge of numbered face `A2` | that edge changes from unknown to selected and contributes one to `A2` only | edges are independently addressed assignments | `LOO-002` |
| Face `E10` shows `0` | select any one of its four boundary edges | its selected-edge count becomes one instead of zero | a face clue counts boundary edges exactly | `LOO-003` |
| Locally legal partial paths | connect three selected edges at one dot | selected degree becomes three, so the subgraph cannot be a simple cycle | exact face counts do not replace vertex topology | `LOO-004`, `LOO-006` |
| Fixed control | select the verifier's 112 edge indices | all 45 clues are exact; 112 selected edges span one connected degree-two component | one complete accepted loop | `LOO-003`–`LOO-005` |
| Fixed control after first solution | continue search to a second solution or exhaustion | every alternative branch contradicts a clue, degree domain or one-cycle test | the recorded control is unique | `LOO-005` |

The verifier independently asserts 45 face equations, 121 degree domains,
non-empty connectivity and second-solution exhaustion.

## Strategic and experiential structure

- Local clue deduction: zero excludes all four sides; a satisfied clue excludes
  remaining sides; an unmet clue can force every remaining boundary edge.
- Vertex deduction: an entered dot must be exited once, while a third selected
  incident edge is immediately impossible.
- Global deduction: closing a small loop too early strands every selected or
  still-required edge outside it, even if the nearby numbers look correct.
- Shared edges couple two neighbouring face equations, so one selection may
  satisfy one clue while exhausting another.
- Claim IDs: `LOO-003`–`LOO-006`.

## Replay and variation

- Generated clue positions and values change the interacting local equations.
- Width, height, difficulty and tiling type are setup parameters outside the
  exact square-grid control.
- Easy constrains generator deduction technique, not the completion rules.
- Claim IDs: `LOO-001`, `LOO-005`.

## Adjacent systems and history

- Slant also assigns binary graph-like strokes and constrains local incidence,
  but every face receives one diagonal and the global rule forbids all cycles;
  Loopy selects a subset of shared boundaries and requires exactly one cycle.
- Bridges uses exact degrees at numbered vertices and requires connectivity,
  but permits branches and cycles and has link multiplicity up to two.
- Flow Free and The Witness require paths, yet their action is continuous
  tracing and their endpoint / region predicates differ from face-edge counts.
- Claim IDs: `LOO-002`–`LOO-006`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-081` | fixed permitted edge; loop / unknown |
| System Behaviour | none | no autonomous state transition |
| Constraint | `CON-001`, `CON-126`, `CON-127` | 220 edges; 45 clues; one loop |
| Information | `INF-001` | visible grid, clues and marks |
| Objective | `OBJ-006` | satisfy local and global predicates |
| Time | `TIM-002` | self-paced editing |

Canonical signature:

`ACT-081; CON-001,CON-126,CON-127; INF-001; OBJ-006; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `75` (`GAME-0001`–`GAME-0075`).
- Exact genome matches: none.
- Tied near matches: `GAME-0005` — Sudoku (`4 / 10 = 0.400000`); `GAME-0008` — Nonogram (`4 / 10 = 0.400000`); `GAME-0071` — Slant (`4 / 10 = 0.400000`); `GAME-0073` — Dominosa (`4 / 10 = 0.400000`).
- Supported combination subsets: `COMB-0076`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0005` — Sudoku | `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | assigns digits under all-different units rather than selecting graph edges | Near, `0.400000` |
| `GAME-0008` — Nonogram | `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | reconstructs ordered cell runs rather than one global cycle | Near, `0.400000` |
| `GAME-0071` — Slant | `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | assigns one diagonal per cell and forbids every cycle | Near, `0.400000` |
| `GAME-0073` — Dominosa | `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | pairs cells under exact-cover inventory rather than graph topology | Near, `0.400000` |

## Taxonomy impact

- Added `ACT-081`, `CON-126`, `CON-127` and `COMB-0076`.
- Extended `CON-001`, `INF-001`, `OBJ-006` and `TIM-002`.
- No existing record required split, merge or deprecation.

## Negative results

- Edge selection is not continuous path tracing: any permitted segment may be
  edited independently, so existing trace actions are absent.
- A numbered face is not a numbered graph vertex: it counts its boundary,
  including edges shared with neighbouring faces, so `CON-114` is absent.
- Connectivity alone is insufficient because branches are forbidden; degree
  two alone is insufficient because two disconnected cycles are forbidden.
- Optional excluded-edge crosses / faded lines and error colours are working
  notation and feedback, not completion-state genes.
- No autonomous system transition occurs in the bounded default.
