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

- Indexed games and combinations scanned: `GAME-0001`–`GAME-0075` and
  `COMB-0001`–`COMB-0075`.
- Exact genome matches: none.
- Near matches: `GAME-0005` Sudoku, `GAME-0008` Nonogram, `GAME-0071` Slant
  and `GAME-0073` Dominosa tie at `4 / 10 = 0.400000`, sharing fixed capacity,
  full visibility, complete satisfaction and self-paced time.
- Next near games: Hexologic and Tents tie at `4 / 11 = 0.363636`.
- Supported combination subsets: none before `COMB-0076`.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0005` — Sudoku | `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | assigns digits under all-different units rather than selecting graph edges | tied nearest, `4 / 10 = 0.400000` |
| `GAME-0008` — Nonogram | `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | reconstructs ordered cell runs rather than one global cycle | tied nearest, `4 / 10 = 0.400000` |
| `GAME-0071` — Slant | `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | assigns one diagonal per cell and forbids every cycle | tied nearest, `4 / 10 = 0.400000` |
| `GAME-0073` — Dominosa | `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | pairs cells under exact-cover inventory rather than graph topology | tied nearest, `4 / 10 = 0.400000` |

- Full numeric scan (`intersection / union = Jaccard`):
  - `GAME-0001`: `2 / 19 = 0.105263`; `GAME-0002`: `3 / 11 = 0.272727`; `GAME-0003`: `1 / 15 = 0.066667`; `GAME-0004`: `2 / 20 = 0.100000`; `GAME-0005`: `4 / 10 = 0.400000`; `GAME-0006`: `3 / 13 = 0.230769`; `GAME-0007`: `2 / 13 = 0.153846`; `GAME-0008`: `4 / 10 = 0.400000`.
  - `GAME-0009`: `2 / 21 = 0.095238`; `GAME-0010`: `2 / 14 = 0.142857`; `GAME-0011`: `3 / 17 = 0.176471`; `GAME-0012`: `4 / 12 = 0.333333`; `GAME-0013`: `2 / 18 = 0.111111`; `GAME-0014`: `2 / 20 = 0.100000`; `GAME-0015`: `2 / 19 = 0.105263`; `GAME-0016`: `2 / 20 = 0.100000`.
  - `GAME-0017`: `0 / 20 = 0.000000`; `GAME-0018`: `1 / 25 = 0.040000`; `GAME-0019`: `2 / 15 = 0.133333`; `GAME-0020`: `1 / 20 = 0.050000`; `GAME-0021`: `1 / 15 = 0.066667`; `GAME-0022`: `1 / 18 = 0.055556`; `GAME-0023`: `1 / 16 = 0.062500`; `GAME-0024`: `2 / 17 = 0.117647`.
  - `GAME-0025`: `1 / 17 = 0.058824`; `GAME-0026`: `1 / 18 = 0.055556`; `GAME-0027`: `2 / 17 = 0.117647`; `GAME-0028`: `2 / 22 = 0.090909`; `GAME-0029`: `2 / 17 = 0.117647`; `GAME-0030`: `1 / 20 = 0.050000`; `GAME-0031`: `1 / 17 = 0.058824`; `GAME-0032`: `2 / 16 = 0.125000`.
  - `GAME-0033`: `1 / 19 = 0.052632`; `GAME-0034`: `1 / 20 = 0.050000`; `GAME-0035`: `1 / 24 = 0.041667`; `GAME-0036`: `2 / 17 = 0.117647`; `GAME-0037`: `2 / 14 = 0.142857`; `GAME-0038`: `1 / 22 = 0.045455`; `GAME-0039`: `4 / 12 = 0.333333`; `GAME-0040`: `2 / 13 = 0.153846`.
  - `GAME-0041`: `1 / 17 = 0.058824`; `GAME-0042`: `1 / 15 = 0.066667`; `GAME-0043`: `2 / 19 = 0.105263`; `GAME-0044`: `2 / 15 = 0.133333`; `GAME-0045`: `2 / 19 = 0.105263`; `GAME-0046`: `2 / 15 = 0.133333`; `GAME-0047`: `2 / 19 = 0.105263`; `GAME-0048`: `2 / 19 = 0.105263`.
  - `GAME-0049`: `1 / 15 = 0.066667`; `GAME-0050`: `2 / 20 = 0.100000`; `GAME-0051`: `1 / 22 = 0.045455`; `GAME-0052`: `1 / 16 = 0.062500`; `GAME-0053`: `2 / 14 = 0.142857`; `GAME-0054`: `2 / 16 = 0.125000`; `GAME-0055`: `2 / 15 = 0.133333`; `GAME-0056`: `2 / 13 = 0.153846`.
  - `GAME-0057`: `2 / 13 = 0.153846`; `GAME-0058`: `2 / 14 = 0.142857`; `GAME-0059`: `2 / 12 = 0.166667`; `GAME-0060`: `1 / 13 = 0.076923`; `GAME-0061`: `4 / 13 = 0.307692`; `GAME-0062`: `4 / 11 = 0.363636`; `GAME-0063`: `3 / 11 = 0.272727`; `GAME-0064`: `2 / 10 = 0.200000`.
  - `GAME-0065`: `1 / 13 = 0.076923`; `GAME-0066`: `1 / 16 = 0.062500`; `GAME-0067`: `0 / 15 = 0.000000`; `GAME-0068`: `1 / 14 = 0.071429`; `GAME-0069`: `3 / 12 = 0.250000`; `GAME-0070`: `2 / 13 = 0.153846`; `GAME-0071`: `4 / 10 = 0.400000`; `GAME-0072`: `4 / 11 = 0.363636`.
  - `GAME-0073`: `4 / 10 = 0.400000`; `GAME-0074`: `4 / 12 = 0.333333`; `GAME-0075`: `4 / 12 = 0.333333`.
- Scan date: 2026-08-14.

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

## Delta summary

- Added one reviewed game, three active genes and one verified combination.
- Added one exact-control verifier and one deterministic rule-valid artwork.
- Corpus size becomes 76 reviewed games, 404 active genes and 76 combinations.

## Нові факти

- Зафіксовано точний стандартний контроль із 100 гранями, 45 числовими
  підказками, 220 ребрами й унікальним циклом зі 112 ребер.
- Незалежний solver окремо довів усі локальні числа, степені `0/2`, зв’язність
  та відсутність другого розв’язку.

## Нові гени

- `ACT-081` — перемикання незалежно адресованого бінарного ребра.
- `CON-126` — точна кількість вибраних ребер навколо позначеної грані.
- `CON-127` — рівно один простий цикл вибраних ребер.

## Нові комбінації

- `COMB-0076` — один цикл за точними підказками граней.

## Зміни таксономії

- Три нові межі активовано без зміни попередніх визначень.
