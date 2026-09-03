---
game_id: GAME-0074
slug: bridges
game_title: Bridges
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0074
gene_ids:
  action:
    - ACT-080
  system: []
  constraint:
    - CON-001
    - CON-030
    - CON-114
    - CON-121
    - CON-122
  information:
    - INF-001
  objective:
    - OBJ-006
  time:
    - TIM-002
---

# Game: Bridges

## Analysis scope

- Version / ruleset: Simon Tatham's Portable Puzzle Collection, current default
  `7 × 7 Easy`, at most two parallel bridges and loops allowed, game ID
  `7x7m2:2b4b4a2b2b2e3a2a2j3b2d2b5a3`, from its fixed fourteen-island field
  to the accepted complete network.
- Included: cycling a connection between two nearest visible orthogonal
  islands through zero, one and two bridges; exact island degree; prohibition
  of horizontal / vertical crossings; connectivity of all islands; revisable
  entries, complete visible state and self-paced solving.
- Excluded: non-default bridge limits; non-default loop prohibition; other
  sizes and difficulties; non-bridge marks, completed-island locks, hints,
  Solve, Undo, Redo, Restart and warning colours as interface support; setup
  generation as an in-solve mechanic; presentation and preferences.
- Direct-play status: the current official playable page was inspected and its
  default rules confirmed. The exact ID was generated from the current source
  with deterministic seed `gamma`. An independent exhaustive solver decoded
  fourteen islands and seventeen possible nearest-neighbour edges, verified
  five genuine crossing conflicts and found exactly one connected solution.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BRG-001` | The default preset is `7 × 7 Easy`, permits loops and limits each island pair to two bridges | Confirmed | Direct | High | P1, P2, P3, local control |
| `BRG-002` | One action cycles the nearest island pair in a chosen orthogonal direction through zero, one and two parallel bridges | Confirmed | Direct | High | P1, P2, P3 |
| `BRG-003` | Every island's weighted incident bridge count must equal its displayed clue | Confirmed | Direct | High | P1, P2, local control |
| `BRG-004` | Positive horizontal and vertical bridge corridors may not cross | Confirmed | Direct | High | P1, P2, local control |
| `BRG-005` | All islands must belong to one connected component; loops remain legal in this scope | Confirmed | Direct | High | P1, P2, P3 |
| `BRG-006` | The recorded fourteen-island control has exactly one complete connected network | Observation | Direct | High | P1, P2, P3, local exhaustive control |
| `BRG-007` | Bridges adds bounded parallel-edge multiplicity and global spanning connectivity while reusing exact incident degree and non-crossing occupancy | Observation | Corroborated | High | `BRG-001`–`BRG-006` |

## Basic data

- Release / origin: the official manual credits the puzzle to Nikoli and notes
  that James Harvey contributed this implementation.
- Platform or physical form: open-source desktop and official JavaScript
  single-player graph-construction puzzle.
- Puzzle family: weighted orthogonal network completion under exact island
  degrees, non-crossing corridors and spanning connectivity.
- Primary sources:
  - **[P1] Simon Tatham:** [official Bridges manual](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/bridges.html),
    specifying exact degrees, single / double bridges, non-crossing and global
    connectivity plus the default loop policy.
  - **[P2] Simon Tatham / James Harvey:** [current `bridges.c` implementation](https://git.tartarus.org/?p=simon/puzzles.git;a=blob;f=bridges.c;hb=HEAD),
    defining the `7 × 7 Easy` default, `maxb=2`, loop allowance, codec,
    nearest-island edges, crossings and connected completion.
  - **[P3] Simon Tatham:** [official playable JavaScript version](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/bridges.html),
    confirming the current controls and visible default rules.
- Secondary sources: none required for the bounded transition claims.
- Reproducible artefact: `scripts/verify_bridges_control.py` decodes the exact
  field, derives every nearest orthogonal edge and crossing pair, enumerates
  edge multiplicities `0..2`, tests all clue equations and connectivity, and
  searches to a second-solution limit.
- Claim IDs: `BRG-001`–`BRG-007`.

## Mechanical decomposition

### Action Genes

- `ACT-080` — cycle bounded nearest-vertex linkage multiplicity. The player
  chooses one orthogonal direction from an island, targeting the first island
  on that ray, and cycles their edge through `0 → 1 → 2 → 0`.
- Drag distance, keyboard shortcuts, completed-island locking and a right-drag
  non-bridge mark are input and notation policies rather than distinct actions.
- Claim IDs: `BRG-002`, `BRG-007`.

### System Behaviour Genes

- Existing gene IDs: none.
- The new multiplicity is recorded directly. Red warnings and locks expose or
  protect current predicates without producing a puzzle-state transition.
- Claim IDs: `BRG-002`–`BRG-005`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The control has a fixed 7 × 7 spatial
  field with fourteen immutable island vertices.
- `CON-030` — exclusive path-cell occupancy. A horizontal and vertical bridge
  corridor may not occupy the same ordinary intervening grid position.
- `CON-114` — exact incident-edge degree at marked vertex. Each island clue is
  the sum of all incident edge multiplicities, so a double bridge contributes
  two to both endpoints.
- `CON-121` — bounded parallel-link multiplicity. Each permitted nearest-island
  edge has integer multiplicity zero, one or two; a third cycle clears it.
- `CON-122` — spanning connectivity of required vertices. Every island must be
  reachable from every other via positive-multiplicity bridges.
- Claim IDs: `BRG-001`, `BRG-003`–`BRG-005`.

### Information Genes

- `INF-001` — fully visible current state. Every clue, current bridge and
  potential spatial corridor is inspectable before each revision.
- Claim IDs: `BRG-001`–`BRG-006`.

### Objective Genes

- `OBJ-006` — complete constraint-satisfying assignment. Acceptance requires
  all island degrees, non-crossing corridors, multiplicity bounds and spanning
  connectivity simultaneously.
- Claim IDs: `BRG-003`–`BRG-006`.

### Time Genes

- `TIM-002` — self-paced sequential action. Link multiplicities can be revised
  without a deadline or autonomous world advance.
- Claim IDs: `BRG-002`, `BRG-006`.

## Reproducible transitions

Coordinates name rows `A`–`G` and columns `1`–`7`.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| No bridge on `A1-A4` | drag right from `A1` | one bridge links the nearest island `A4`; both endpoint degrees increase by one | directional input targets the first orthogonal island | `BRG-002`, `BRG-003` |
| One bridge on `A1-A4` | repeat the same drag | the edge becomes double and contributes two at both ends | multiplicity is bounded and weighted | `BRG-001`–`BRG-003` |
| Two bridges on `A1-A4` | repeat the same drag | the whole edge returns to zero | the bounded linkage is directly revisable | `BRG-002`, `BRG-006` |
| Two geometrically crossing candidate corridors active | evaluate field | their intervening cells conflict even though the four endpoints are distinct | non-crossing is a corridor predicate, not vertex capacity | `BRG-004` |
| Synthetic field of four clue-1 islands with two disjoint one-bridge pairs | evaluate completion | every local clue is exact, but two components remain, so the field is incomplete | local exact degrees do not replace global connectivity | `BRG-005` |
| Fixed control | assign the verifier's thirteen positive edges | fourteen vertices become one component; all clues and five crossing exclusions hold | one complete accepted network | `BRG-003`–`BRG-006` |
| Fixed control after first branching choice | continue exhaustive search to a second solution or exhaustion | no second connected satisfying edge assignment remains | the recorded control is unique | `BRG-006` |

The verifier prints every positive edge and multiplicity, and independently
asserts the fourteen clue equations, five crossing conflicts, connectivity and
uniqueness.

## Strategic and experiential structure

- Local decision: compare an island's remaining degree with the number and
  capacities of still-available nearest-neighbour edges.
- Medium-term planning: a chosen positive corridor disables every crossing
  candidate, while a double bridge consumes two degree units at both ends.
- Long-term structure: preserve at least one external positive edge for every
  incomplete component. Degree-saturated cycles or pairs can isolate a closed
  subnetwork even when all local clues are correct.
- Common heuristics: fill forced degree, cap saturated islands, remove crossing
  corridors, then apply component cuts before committing the last local units.
- Failure attribution: over-degree, blocked under-degree, crossing and closed
  components correspond to visible predicates in the current proposal.
- Player-trust factors: a double bridge must count twice at both ends, only the
  nearest island is eligible on a ray, and loops must not be rejected in the
  default rules.
- Claim IDs: `BRG-002`–`BRG-006`.

## Replay and variation

- What changes between sessions: island coordinates, clue degrees and the
  unique connected bridge network generated for the selected preset.
- Randomness or procedural generation: setup-only. The descriptive game ID
  makes this control deterministic.
- Multiple viable strategies: the same unique network can be derived through
  degree saturation, crossing elimination or component-cut reasoning.
- Typical replay motive: solve a different visible network or select Medium /
  Hard, different sizes, a different parallel limit or the no-loop variant.
- Claim IDs: `BRG-001`, `BRG-006`.

## Adjacent systems and history

- Slant and Bridges both use exact incident degree at marked graph vertices.
  Slant assigns one binary diagonal per cell and prohibits cycles; Bridges
  assigns multiplicity `0..2` to sparse orthogonal edges and requires all
  vertices connected while allowing cycles.
- Flow Free and Bridges both forbid ordinary path crossings. Flow Free builds
  labelled simple routes covering cells; Bridges builds one weighted network
  over fixed islands and need not cover the field.
- LYNE and Bridges both connect visible vertices and share non-crossing path
  space, but LYNE has typed endpoint paths and counted nexus exceptions rather
  than exact degrees plus one spanning component.
- Claim IDs: `BRG-003`–`BRG-007`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-080` | source island, orthogonal ray, `0→1→2→0` |
| System Behaviour | none | no automatic state transition |
| Constraint | `CON-001`, `CON-030`, `CON-114`, `CON-121`, `CON-122` | 14 vertices; five crossing pairs; max two |
| Information | `INF-001` | visible clues and link proposal |
| Objective | `OBJ-006` | satisfy all local and global predicates |
| Time | `TIM-002` | self-paced editing |

Canonical signature:

`ACT-080; none; CON-001,CON-030,CON-114,CON-121,CON-122; INF-001; OBJ-006; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `73` (`GAME-0001`–`GAME-0073`).
- Exact genome matches: none.
- Tied near matches: `GAME-0071` — Slant (`5 / 11 = 0.454545`).
- Supported combination subsets: `COMB-0074`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0071` — Slant | `CON-001`, `CON-114`, `INF-001`, `OBJ-006`, `TIM-002` | Slant uses binary diagonals and forbids cycles; Bridges uses multiplicity 0–2, forbids crossings and requires connectivity while allowing cycles | Near, `0.454545` |

## Taxonomy impact

- Added `ACT-080`, `CON-121` and `CON-122` as active genes.
- Extended `CON-001`, `CON-030`, `CON-114`, `INF-001`, `OBJ-006` and
  `TIM-002` with bounded Bridges support.
- Added `COMB-0074`; no existing record required split, merge or deprecation.

## Negative results

- Bridge drawing is not freehand path construction: the action targets the
  first island in one orthogonal direction and chooses only multiplicity.
- `CON-114` is reusable from Slant because both clues count incident selected
  edges; the Bridges edge domain and multiplicity are parameters and new
  constraints, not a new degree definition.
- Non-crossing reuses `CON-030`: ordinary corridor cells are mutually exclusive
  and there is no grade-separated crossing exception.
- Connectivity cannot be inferred from exact clue degrees in general and is
  retained as its own global predicate.
- Global acyclicity is explicitly absent: default Bridges permits loops.
- Non-bridge marks, island-complete locks and red warnings are notation and
  interface policy rather than new mechanical genes.
