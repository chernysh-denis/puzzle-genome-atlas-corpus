---
game_id: GAME-0078
slug: galaxies
game_title: Galaxies
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0078
gene_ids:
  action:
    - ACT-081
  system: []
  constraint:
    - CON-001
    - CON-129
    - CON-130
  information:
    - INF-001
  objective:
    - OBJ-006
  time:
    - TIM-002
---

# Game: Galaxies

## Analysis scope

- Version / ruleset: Simon Tatham's Portable Puzzle Collection, current desktop
  default `7 × 7 Normal`, exact game ID `7x7dn:iddupugwliut`, from its 12 fixed
  centre dots to the accepted 12-region partition.
- Included: independently selecting or clearing any of 84 internal cell edges;
  components induced by unselected orthogonal contacts; exactly one fixed dot
  per component; connectedness and 180-degree rotational symmetry about that
  dot; complete visibility, revision and self-paced solving.
- Excluded: Unreasonable difficulty; 10 × 10 and 15 × 15 presets; right-drag
  association arrows, valid-region highlighting, conflict display, keyboard
  cursor, Solve, Undo, Redo and Restart as interface support; generation and
  presentation.
- Direct-play status: the official current manual, JavaScript version and
  source were inspected. The exact control was generated from current source
  with deterministic seed `202608140078`. An independent enumerator decoded 12
  centre dots, generated every connected symmetric candidate region, proved
  one exact 49-cell partition and verified its 40 internal boundary edges.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `GAL-001` | The current desktop default is `7 × 7 Normal` | Confirmed | Direct | High | P1, P2, P3 |
| `GAL-002` | The player draws or clears fixed cell edges, and completion edges are precisely inter-region boundaries | Confirmed | Direct | High | P1, P2, P3 |
| `GAL-003` | Every resulting region is an orthogonally connected cell component | Confirmed | Direct | High | P1, P2 |
| `GAL-004` | Every region contains exactly one dot at its centre | Confirmed | Direct | High | P1, P2 |
| `GAL-005` | Every region is invariant under a 180-degree rotation about its own dot | Confirmed | Direct | High | P1, P2 |
| `GAL-006` | The recorded control has one unique complete 12-region partition | Observation | Direct | High | P1, P2, P3, local exhaustive control |
| `GAL-007` | One-dot ownership and half-turn closure are independent completion predicates | Observation | Corroborated | High | `GAL-003`–`GAL-006` |

## Basic data

- Release / origin: the manual identifies Nikoli's *Tentai Show*, commonly
  translated as *Spiral Galaxies*, and credits James Harvey for the collection
  implementation.
- Platform or physical form: open-source desktop and official JavaScript
  single-player edge-partition puzzle.
- Puzzle family: centre-seeded connected polyomino partition under half-turn
  symmetry.
- Primary sources:
  - **[P1] Simon Tatham:** [official Galaxies manual](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/galaxies.html),
    specifying connected regions, exactly one centre dot, half-turn symmetry,
    boundary input and completion semantics.
  - **[P2] Simon Tatham / James Harvey:** [current `galaxies.c` implementation](https://git.tartarus.org/?p=simon/puzzles.git;a=blob;f=galaxies.c;hb=HEAD),
    defining default parameters, dot codec, solver deductions and completion
    check.
  - **[P3] Simon Tatham:** [official playable JavaScript version](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/galaxies.html),
    confirming current presentation and independent edge editing.
- Secondary source: [Nikoli's official Tentai Show description](https://www.nikoli.co.jp/en/puzzles/tentai_show/).
- Reproducible artefact: `scripts/verify_galaxies_control.py` decodes every dot
  on the doubled coordinate grid, enumerates all connected half-turn-closed
  regions that contain their own centre cells and no other dot, exact-covers
  all 49 cells to a second-solution limit and derives inter-region edges.
- Claim IDs: `GAL-001`–`GAL-007`.

## Mechanical decomposition

### Action Genes

- `ACT-081` — toggle independently addressed binary edge. Each of 84 internal
  cell boundaries may be drawn or cleared without tracing from an endpoint or
  automatically changing another edge.
- Right-drag association arrows are excluded candidate notation rather than
  accepted boundary values.
- Claim IDs: `GAL-002`, `GAL-006`.

### System Behaviour Genes

- None promoted. An edge edit persists directly; automatic highlighting only
  reports that a completed component currently passes the region predicates.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The control preserves 49 square cells,
  84 internal adjacencies and 12 immutable centre dots.
- `CON-129` — exactly one centre marker per edge-bounded component. Every cell
  belongs to one orthogonally connected region induced by the edge proposal,
  and that region must contain its one designated dot but no other dot.
- `CON-130` — half-turn closure about component centre. For every cell in a
  region, rotating its centre 180 degrees around the region's dot lands on
  another cell of the same region.
- Claim IDs: `GAL-001`, `GAL-003`–`GAL-007`.

### Information Genes

- `INF-001` — fully visible current state. The complete cell grid, all 12 dots,
  every selected boundary and every optional validity highlight remain visible.
- Claim IDs: `GAL-001`–`GAL-006`.

### Objective Genes

- `OBJ-006` — complete constraint-satisfying assignment. Acceptance requires
  all 49 cells to form valid regions and the selected edges to be exactly the
  40 boundaries separating those regions.
- Claim IDs: `GAL-002`–`GAL-007`.

### Time Genes

- `TIM-002` — self-paced sequential action. No clock or autonomous state step
  advances between edge revisions.
- Claim IDs: `GAL-002`, `GAL-006`.

## Reproducible transitions

Cell coordinates use rows `A`–`G` and columns `1`–`7`; doubled dot coordinates
use the verifier's `1`–`13` lattice.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Empty control | select the edge between `A4` and `A5` | one persistent boundary separates the large top-left region from singleton `A5` | edges are independently addressed | `GAL-002` |
| Cells `A1,A2,A3,A4,B1,B2,B3,B4` are one component | inspect dot `(4,2)` | it is the component's only dot and lies at its half-turn centre | one centre marker per component | `GAL-004` |
| The same eight-cell component | remove `A1` while retaining its opposite `B4` | rotation about `(4,2)` maps an included cell to an excluded cell | one-dot ownership does not imply symmetry | `GAL-005`, `GAL-007` |
| The same eight-cell component | add an internal edge between `A1` and `A2` | the edge is extraneous because both cells belong to the same valid region | completion edges must equal component boundaries | `GAL-002`, `GAL-003` |
| Fixed control | select the verifier's 40 internal boundary edges | 49 cells form connected regions of sizes `1,1,8,4,2,8,6,1,1,6,8,3`, each with one centre and half-turn closure | one complete accepted partition | `GAL-003`–`GAL-006` |
| Fixed control after first partition | continue exact-cover search to a second solution or exhaustion | every alternative candidate overlap leaves a cell uncovered or contradicts a centre / symmetry predicate | the recorded control is unique | `GAL-006` |

The verifier independently asserts complete disjoint coverage, component
connectedness, own-centre inclusion, exclusion of every other dot, half-turn
closure, 40 derived internal boundaries and second-solution exhaustion.

## Strategic and experiential structure

- Centre seeding: a dot on a cell centre, edge or vertex immediately owns one,
  two or four surrounding cells respectively.
- Paired growth: assigning one cell to a dot simultaneously commits its
  half-turn opposite cell to that same prospective region.
- Boundary propagation: once two adjacent cells can no longer share a dot,
  their common edge is forced; an edge may then close a complete component.
- Global exact cover: locally plausible symmetric components compete for the
  same cells, so the final choice must partition the entire board without gaps
  or overlaps.
- Claim IDs: `GAL-003`–`GAL-007`.

## Replay and variation

- Generated dot count, placement and cell/edge/vertex centres change the set of
  feasible symmetric regions and their overlap graph.
- Width, height and difficulty are setup parameters outside the bounded default
  control.
- Normal constrains permitted deduction techniques during generation, not the
  region completion predicates.
- Claim IDs: `GAL-001`, `GAL-006`.

## Adjacent systems and history

- Loopy uses the same independent binary edge action, but interprets selected
  edges as one cycle constrained by face counts; Galaxies interprets them as
  boundaries of many centre-seeded cell components.
- The Witness also lets a line partition cells into clue regions, but its path
  must run continuously from start to end and its square clues constrain colour
  cohabitation rather than rotational geometry.
- Dominosa exact-covers every cell with fixed-size adjacent pairs; Galaxies
  exact-covers the grid with variable-size connected symmetric components whose
  shapes are inferred from fixed centres.
- Claim IDs: `GAL-002`–`GAL-007`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-081` | fixed internal edge; boundary / open |
| System Behaviour | none | validity highlighting is feedback |
| Constraint | `CON-001`, `CON-129`, `CON-130` | 49 cells; 12 dots; half-turn closure |
| Information | `INF-001` | visible grid, dots and edge marks |
| Objective | `OBJ-006` | complete valid region partition |
| Time | `TIM-002` | self-paced editing |

Canonical signature:

`ACT-081; CON-001,CON-129,CON-130; INF-001; OBJ-006; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `77` (`GAME-0001`–`GAME-0077`).
- Exact genome matches: none.
- Tied near matches: `GAME-0076` — Loopy (`5 / 9 = 0.555556`).
- Supported combination subsets: `COMB-0078`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0076` — Loopy | `ACT-081`, `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | requires exact face-edge counts and one simple cycle instead of centre-seeded symmetric regions | Near, `0.555556` |

## Taxonomy impact

- Added `CON-129`, `CON-130` and `COMB-0078`.
- Extended `ACT-081`, `CON-001`, `INF-001`, `OBJ-006` and `TIM-002`.
- No existing record required split, merge or deprecation.

## Negative results

- Association arrows are optional hypothesis notation and do not determine the
  accepted component assignment, so they do not add an Action gene.
- Automatic valid-region highlighting reports a predicate without advancing or
  transforming the decision state, so it is not System Behaviour.
- The player selects boundaries, not a dot identity for each cell; direct symbol
  assignment would misclassify the action even though the verifier uses region
  ownership internally.
- Complete coverage does not instantiate Dominosa's exact adjacent-pair cover:
  Galaxies regions have variable size and are induced by edge components.
- Visual bilateral symmetry is insufficient. The constraint is exact half-turn
  closure around each region's own dot.

## Delta summary

- Added one reviewed game, two active genes and one verified combination.
- Added one exact-control verifier and one deterministic rule-valid artwork.
- Corpus size becomes 78 reviewed games, 407 active genes and 78 combinations.

## Нові факти

- Зафіксовано точний стандартний контроль із 49 клітинами, 12 центральними
  крапками, 12 зв’язними регіонами та 40 внутрішніми межами.
- Незалежний повний перебір довів один поділ, у якому кожен регіон містить одну
  крапку й замкнений відносно повороту на 180 градусів навколо неї.

## Нові гени

- `CON-129` — рівно один центральний маркер у компоненті, обмеженій ребрами.
- `CON-130` — замкненість компоненти відносно повороту на пів оберту.

## Нові комбінації

- `COMB-0078` — поділ межами на регіони з одним центром і поворотною
  симетрією.

## Зміни таксономії

- Дві нові межі активовано без зміни попередніх визначень.

## Open ambiguities

- None at the current evidence threshold. Optional arrow semantics and coloured
  picture-generator dots remain outside the bounded default control.

## Sources

1. Simon Tatham, [official Galaxies manual](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/galaxies.html).
2. Simon Tatham / James Harvey, [current `galaxies.c` implementation](https://git.tartarus.org/?p=simon/puzzles.git;a=blob;f=galaxies.c;hb=HEAD).
3. Simon Tatham, [official playable Galaxies](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/galaxies.html).
4. Nikoli, [Tentai Show](https://www.nikoli.co.jp/en/puzzles/tentai_show/).
5. Local control verifier: `scripts/verify_galaxies_control.py`.

## Verification status

- Structure validated locally against the repository schema.
- Claims `GAL-001`–`GAL-005` are directly supported by current official rules,
  source and presentation.
- Claims `GAL-006`–`GAL-007` are independently checked on exact control
  `7x7dn:iddupugwliut`.
- Full corpus comparison completed through `GAME-0077`.
