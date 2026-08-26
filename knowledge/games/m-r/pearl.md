---
game_id: GAME-0081
slug: pearl
game_title: Pearl
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0081
gene_ids:
  action:
    - ACT-081
  system: []
  constraint:
    - CON-001
    - CON-127
    - CON-133
    - CON-134
  information:
    - INF-001
  objective:
    - OBJ-006
  time:
    - TIM-002
---

# Game: Pearl

## Analysis scope

- Version / ruleset: Simon Tatham's Portable Puzzle Collection, current desktop
  default `8 × 8 Tricky`, exact game ID
  `8x8dt:BbBaWaBeWdWWkBbBdBbBeWWkWaB`.
- Included: independently selecting or clearing orthogonal links between
  adjacent cell centres; one simple closed loop that may omit unmarked cells;
  eight black turn clues; seven white straight clues; complete visibility,
  revision and self-paced solving.
- Excluded: `6 × 6`, `10 × 10`, `12 × 8` and Easy presets; Allow unsoluble;
  Loopy-style presentation; exclusion crosses, drag batching, error colours,
  Solve, Undo, Redo and Restart as interface support.
- Direct-play status: current official manual, JavaScript version and source
  were inspected. The control was generated from source revision
  `3c3632259d298ab62aafa8a5858823569ab1af46` with seed `202608140081`.
  An independent cell-state constraint solver proved exactly one 60-cell,
  60-edge cycle and separately verified every clue-relative turn predicate.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PEA-001` | The current desktop default is `8 × 8 Tricky` | Confirmed | Direct | High | P1, P2, P3 |
| `PEA-002` | Selected orthogonal links must form one closed loop, which need not visit every cell | Confirmed | Direct | High | P1, P2 |
| `PEA-003` | A black clue is a turn whose two next loop cells are both straight | Confirmed | Direct | High | P1, P2 |
| `PEA-004` | A white clue is straight and at least one of its two next loop cells is a turn | Confirmed | Direct | High | P1, P2 |
| `PEA-005` | “Next” refers to adjacency along the loop, not every grid neighbour | Confirmed | Direct | High | P1, P2 |
| `PEA-006` | The exact control has 8 black clues, 7 white clues and one unique 60-edge solution | Observation | Direct | High | P2, local exhaustive control |
| `PEA-007` | Local clue geometry constrains the same selected subgraph as the global one-cycle rule | Observation | Corroborated | High | `PEA-002`–`PEA-006` |

## Basic data

- Release / origin: the manual credits Nikoli's *Masyu* and James Harvey's
  implementation assistance.
- Platform or physical form: open-source desktop and official JavaScript
  single-player loop-deduction puzzle.
- Puzzle family: single-cycle graph completion under clue-conditioned local
  straight / turn patterns.
- Primary sources:
  - **[P1] Simon Tatham:** [official Pearl manual](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/pearl.html),
    specifying the loop and both clue predicates.
  - **[P2] Simon Tatham:** [current `pearl.c` implementation](https://git.tartarus.org/?p=simon/puzzles.git;a=blob;f=pearl.c;hb=HEAD),
    defining defaults, codec, generator, solver and completion checks.
  - **[P3] Simon Tatham:** [official playable JavaScript version](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/pearl.html),
    confirming current presentation and edge-editing semantics.
- Secondary source: [Nikoli's official Masyu rules](https://www.nikoli.co.jp/en/puzzles/masyu/).
- Reproducible artefact: `scripts/verify_pearl_control.py` independently
  decodes 64 clue states, propagates reciprocal cell-centre links, enumerates
  all local path shapes to a second-solution limit and verifies one connected
  degree-two component plus both clue predicates.
- Claim IDs: `PEA-001`–`PEA-007`.

## Mechanical decomposition

### Action Genes

- `ACT-081` — toggle independently addressed binary edge. One click changes
  one permitted link between adjacent cell centres without tracing from an
  endpoint or automatically editing another edge.
- Left-drag batches the same edge toggles. Right-click crosses are optional
  working notation and not required solution values.
- Claim IDs: `PEA-002`, `PEA-006`.

### System Behaviour Genes

- None promoted. Edge selections persist directly; conflict colouring and
  optional drag behaviour do not transform the puzzle state autonomously.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The control preserves 64 cell-centre
  vertices and their fixed orthogonal adjacency graph.
- `CON-127` — exactly one simple selected-edge cycle. Every used cell centre
  has selected degree two, and all 60 selected edges belong to one component.
- `CON-133` — marked turn flanked by straight path cells. Every black clue is
  a corner, and the next loop cell on each of its two incident directions is
  straight.
- `CON-134` — marked straight adjacent to a path turn. Every white clue is
  straight, and at least one of the two next cells along the loop is a corner.
- The clue predicates follow selected links. Merely sharing a grid edge with a
  clue does not make a cell its constrained neighbour.
- Claim IDs: `PEA-002`–`PEA-007`.

### Information Genes

- `INF-001` — fully visible current state. The grid, every black or white clue
  and every current selected link remain visible before each revision.
- Claim IDs: `PEA-001`–`PEA-006`.

### Objective Genes

- `OBJ-006` — complete constraint-satisfying assignment. Acceptance requires
  one simple loop that visits every clue and satisfies every local shape rule.
- Claim IDs: `PEA-002`–`PEA-007`.

### Time Genes

- `TIM-002` — self-paced sequential action. No clock or automatic simulation
  advances between edge edits.
- Claim IDs: `PEA-002`, `PEA-006`.

## Reproducible transitions

Coordinates use rows `A`–`H` and columns `1`–`8`.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Empty control | select the link `A1-A2` | one fixed orthogonal edge changes from unknown to selected | independently addressed binary edge | `PEA-002` |
| Black clue `A1` | route the loop right then down | `A1` is a corner; `A2` and `B1` must be straight on the loop | black turn with two straight flanks | `PEA-003`, `PEA-005` |
| White clue `A6` | route the loop horizontally through it | the clue is straight; the solution turns at `A7` while `A5` remains straight | at least one adjacent loop turn | `PEA-004`, `PEA-005` |
| White clue `C3` | make both loop-neighbour cells straight | the local path contradicts the white clue even though `C3` itself is straight | a straight clue needs an adjacent turn | `PEA-004` |
| Fixed control | select the verifier's complete 60-edge solution | all 15 clues lie on one connected degree-two component | complete accepted loop | `PEA-002`–`PEA-006` |
| Fixed control after first solution | continue exhaustive search | every alternative local state branch contradicts reciprocity, a clue or the one-cycle test | unique recorded solution | `PEA-006` |

The verifier asserts the exact hexadecimal cell-state string, all reciprocal
links, degrees, connectedness, eight black predicates, seven white predicates
and exhaustion after the first solution.

## Strategic and experiential structure

- Black-clue propagation: choosing its corner orientation immediately fixes a
  straight continuation on both sides.
- White-clue disjunction: the marked cell's axis is fixed, but either or both
  adjacent loop cells may supply the required turn.
- Loop-relative adjacency: the path determines which two neighbours a clue
  constrains, coupling local shape and edge-selection decisions.
- Premature closure: a locally valid smaller cycle strands remaining clues and
  fails the global one-component rule.
- Claim IDs: `PEA-002`–`PEA-007`.

## Replay and variation

- Generated clue positions, colours and loop geometry change the deduction
  chain while preserving the scoped gene set.
- Width, height and difficulty are setup parameters. Allow unsoluble removes
  the generator's uniqueness / deductive-solvability guarantee, not the
  completion predicate, and is excluded.
- Traditional versus Loopy-style drawing changes presentation coordinates but
  not the abstract cell-centre graph in this scope.
- Claim IDs: `PEA-001`, `PEA-006`.

## Adjacent systems and history

- Loopy shares independent edge selection and the exact-one-cycle rule, but
  constrains edge counts around faces instead of clue-relative path shapes.
- Galaxies shares boundary-edge editing but completes a symmetric region
  partition rather than one degree-two selected subgraph.
- Slant assigns one diagonal per cell and forbids every cycle, the opposite
  global topology from Pearl's required single cycle.
- Claim IDs: `PEA-002`–`PEA-007`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-081` | permitted orthogonal link; selected / unknown |
| System Behaviour | none | error colours are feedback |
| Constraint | `CON-001`, `CON-127`, `CON-133`, `CON-134` | 64 vertices; 15 clues; one loop |
| Information | `INF-001` | visible grid, clues and links |
| Objective | `OBJ-006` | satisfy local path shapes and global cycle |
| Time | `TIM-002` | self-paced editing |

Canonical signature:

`ACT-081; CON-001,CON-127,CON-133,CON-134; INF-001; OBJ-006; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `80` (`GAME-0001`–`GAME-0080`).
- Exact genome matches: none.
- Tied near matches: `GAME-0076` — Loopy (`6 / 9 = 0.666667`).
- Supported combination subsets: `COMB-0081`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0076` — Loopy | `ACT-081`, `CON-001`, `CON-127`, `INF-001`, `OBJ-006`, `TIM-002` | exact face-edge counts replace black and white path-shape clues | Near, `0.666667` |

## Taxonomy impact

- Added `CON-133`, `CON-134` and `COMB-0081`.
- Extended `ACT-081`, `CON-001`, `CON-127`, `INF-001`, `OBJ-006` and
  `TIM-002`.
- No existing record required split, merge or deprecation.

## Negative results

- Dragging several edges batches repeated `ACT-081` operations and does not
  create a separate continuous-path action.
- A clue constrains the two neighbours actually connected through the loop,
  not all orthogonal grid neighbours.
- Black and white clues are not parameters of one equality rule: one requires
  a turn with two straight flanks, while the other requires a straight with a
  disjunctive turn on at least one flank.
- Optional crosses and error colours are notation and feedback, not canonical
  completion-state genes.

## Delta summary

- Added one reviewed game, two active genes and one verified combination.
- Added one exact-control verifier and one deterministic rule-valid artwork.
- Corpus size becomes 81 reviewed games, 411 active genes and 81 combinations.

## Нові факти

- Зафіксовано точний контроль `8 × 8 Tricky` із 8 чорними та 7 білими
  підказками.
- Незалежний перебір довів один цикл із 60 клітин і 60 ребер та відсутність
  другого розв’язку.

## Нові гени

- `CON-133` — позначений поворот із прямими клітинами шляху по обидва боки.
- `CON-134` — позначена пряма з поворотом шляху щонайменше з одного боку.

## Нові комбінації

- `COMB-0081` — один цикл за взаємодією чорних і білих підказок форми шляху.

## Зміни таксономії

- Повторно використано глобальний цикл Loopy, але локальні геометричні
  підказки Pearl активовано як дві окремі перевірювані межі.
