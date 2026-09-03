---
game_id: GAME-0077
slug: map
game_title: Map
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0077
gene_ids:
  action:
    - ACT-007
  system: []
  constraint:
    - CON-001
    - CON-009
    - CON-128
  information:
    - INF-001
  objective:
    - OBJ-006
  time:
    - TIM-002
---

# Game: Map

## Analysis scope

- Version / ruleset: Simon Tatham's Portable Puzzle Collection, current desktop
  default `20 × 15, 30 regions, Normal`, exact game ID
  `20x15n30:ecdanaaaaalchbaabcfbabbaabdabbbaaaabaacabacbcaabbabdfabbqefcbhbedafcaacabbdddcaanaaadaadcabaaaaadacaababgdbaebecdabafaaabbbeaafbdababdcaaacbcbeeibdbaacbbdhabababfeacanabbdadaabbfeababhaaaajaaadabadaabdceacaea,01b0d2a2b2e3a1a020a32`,
  from 13 immutable colour seeds to the accepted complete four-colouring.
- Included: assigning one of four colours to any of 17 editable regions;
  preserving 13 visible immutable region colours; unequal colours for every
  pair sharing a positive-length boundary; point-only contacts ignored;
  complete visibility, revision and self-paced solving.
- Excluded: Easy, Hard and Unreasonable; 75-region and portrait presets;
  right-drag pencil stipples, numbered display, conflict markers, completion
  flash, keyboard cursor, Solve, Undo, Redo and Restart as interface support;
  generation and presentation.
- Direct-play status: the official current manual, JavaScript version and
  source were inspected. The exact control was generated from current source
  with deterministic seed `202608140077`. An independent decoder reconstructed
  all 300 cells, 30 regions and 66 adjacency edges, then proved one unique
  four-colouring consistent with all 13 givens and verified two point-only
  region contacts are correctly absent from the graph.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MAP-001` | The current desktop default is `20 × 15`, 30 regions, Normal | Confirmed | Direct | High | P1, P2, P3 |
| `MAP-002` | Every region must receive one of four colours | Confirmed | Direct | High | P1, P2 |
| `MAP-003` | Regions sharing a positive-length boundary must have different colours | Confirmed | Direct | High | P1, P2 |
| `MAP-004` | Regions meeting only at one point may share a colour | Confirmed | Direct | High | P1, P2 |
| `MAP-005` | Initially coloured regions are visible, immutable and sufficient to make the remaining solution unique | Confirmed | Direct | High | P1, P2 |
| `MAP-006` | The recorded control has exactly one complete four-colouring | Observation | Direct | High | P1, P2, P3, local exhaustive control |
| `MAP-007` | The rule is pairwise graph adjacency exclusion, not an all-different unit | Observation | Corroborated | High | `MAP-002`–`MAP-006` |

## Basic data

- Release / origin: Simon Tatham describes the puzzle as original, credits
  Alexandra Lanes for suggesting a four-colouring puzzle, and credits Nikoli
  and Verity Allan for inspiration.
- Platform or physical form: open-source desktop and official JavaScript
  single-player region-assignment puzzle.
- Puzzle family: seed-constrained four-colouring of a planar region graph.
- Primary sources:
  - **[P1] Simon Tatham:** [official Map manual](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/map.html),
    specifying the four-colour domain, shared-boundary adjacency, point-contact
    exception, immutable givens and controls.
  - **[P2] Simon Tatham:** [current `map.c` implementation](https://git.tartarus.org/?p=simon/puzzles.git;a=blob;f=map.c;hb=HEAD),
    defining default parameters, codec, graph construction, solver and
    completion test.
  - **[P3] Simon Tatham:** [official playable JavaScript version](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/map.html),
    confirming current visible interaction.
- Secondary sources: none required.
- Reproducible artefact: `scripts/verify_map_control.py` decodes the exact
  run-length boundary stream, reconstructs regions with disjoint sets, derives
  adjacency only from orthogonal cell borders, decodes immutable colours and
  enumerates four-colour assignments to a second-solution limit.
- Claim IDs: `MAP-001`–`MAP-007`.

## Mechanical decomposition

### Action Genes

- `ACT-007` — assign symbol to open position. The player addresses one editable
  region and assigns one value from the common four-colour domain; dragging
  from an existing colour is the input modality, not a copied object.
- Optional multi-colour stipples are excluded candidate notation rather than
  accepted region values.
- Claim IDs: `MAP-002`, `MAP-006`.

### System Behaviour Genes

- None promoted. Assigning a colour changes that region's recorded proposal;
  error highlighting and completion flash report predicates without creating
  a decision-relevant automatic transition.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The control preserves a `20 × 15` cell
  field partitioned into 30 persistent addressed regions.
- `CON-009` — immutable given assignments. Thirteen regions begin with fixed
  visible colours, including at least one source of each palette colour.
- `CON-128` — shared-boundary adjacent-class exclusion. The derived graph has
  66 distinct region pairs that must differ; the corner-only pairs `9–18` and
  `12–20` create no constraint.
- Claim IDs: `MAP-001`, `MAP-003`–`MAP-007`.

### Information Genes

- `INF-001` — fully visible current state. Every region boundary, immutable
  seed, current editable colour and empty region remains visible.
- Claim IDs: `MAP-001`–`MAP-006`.

### Objective Genes

- `OBJ-006` — complete constraint-satisfying assignment. Acceptance requires
  all 30 regions coloured, all 13 seeds unchanged and all 66 inequalities true.
- Claim IDs: `MAP-002`–`MAP-006`.

### Time Genes

- `TIM-002` — self-paced sequential action. No clock or autonomous state step
  advances between region assignments.
- Claim IDs: `MAP-002`, `MAP-006`.

## Reproducible transitions

Region IDs are the decoder's stable row-major component labels `0`–`29`.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Region `2` is empty | assign palette colour `3` | only region `2` receives proposed colour `3` | direct bounded-domain region assignment | `MAP-002` |
| Adjacent regions `1` and `2` | assign region `2` colour `1`, already fixed on region `1` | their shared boundary becomes a conflict | positive-length border creates pairwise inequality | `MAP-003` |
| Corner-only regions `9` and `18` | give both colour `2` | no adjacency predicate is violated | point contact is not adjacency | `MAP-004` |
| Immutable region `0` is colour `0` | attempt to recolour it | the assignment action is unavailable for that region | givens constrain but are not editable | `MAP-005` |
| Fixed control | assign regions to `0,1,3,1,0,0,1,2,3,2,2,2,0,0,2,0,1,3,2,1,3,1,1,2,0,2,0,3,3,2` | all regions are coloured, givens match and every one of 66 adjacent pairs differs | one complete accepted assignment | `MAP-002`–`MAP-006` |
| Fixed control after first solution | continue search to a second colouring or exhaustion | every alternative contradicts a seed or adjacency inequality | the recorded control is unique | `MAP-006` |

The verifier independently asserts 13 immutable assignments, 66 graph-edge
inequalities, complete four-value coverage and second-solution exhaustion.

## Strategic and experiential structure

- Local deduction: a region adjacent to three differently coloured neighbours
  is forced to the fourth colour.
- Constraint propagation: assigning one region removes its colour from every
  adjacent unassigned region but not from point-only contacts.
- Seed anchoring: at least one immutable region of each colour fixes palette
  identity and prevents whole-solution colour permutation.
- Global uniqueness emerges from overlapping pairwise inequalities rather than
  one large unit requiring all colours.
- Claim IDs: `MAP-003`–`MAP-007`.

## Replay and variation

- Generated region shapes, adjacency graph and immutable seed placement vary.
- Width, height, region count and difficulty are setup parameters outside the
  bounded default control.
- Normal constrains permitted deduction techniques during generation, not the
  four-colouring completion rules.
- Claim IDs: `MAP-001`, `MAP-005`, `MAP-006`.

## Adjacent systems and history

- Sudoku is the closest prior genome because both assign a finite visible
  domain around immutable givens, but Sudoku's row, column and block units are
  all-different; Map enforces only pairwise inequalities on graph edges.
- KAMI also displays coloured regions, but one action recolours an entire
  current connected component and changes future region topology; Map assigns
  one persistent region without coalescence.
- Four-colour theorem context does not replace the puzzle rule: the scoped
  instance provides exactly four named values and fixed seeds, then requires
  one unique completion.
- Claim IDs: `MAP-002`–`MAP-007`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-007` | one region; four palette values |
| System Behaviour | none | no autonomous transition |
| Constraint | `CON-001`, `CON-009`, `CON-128` | 30 regions; 13 seeds; 66 adjacencies |
| Information | `INF-001` | visible boundaries and assignments |
| Objective | `OBJ-006` | complete valid four-colouring |
| Time | `TIM-002` | self-paced editing |

Canonical signature:

`ACT-007; CON-001,CON-009,CON-128; INF-001; OBJ-006; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `76` (`GAME-0001`–`GAME-0076`).
- Exact genome matches: none.
- Tied near matches: `GAME-0005` — Sudoku (`6 / 8 = 0.750000`).
- Supported combination subsets: `COMB-0077`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0005` — Sudoku | `ACT-007`, `CON-001`, `CON-009`, `INF-001`, `OBJ-006`, `TIM-002` | Sudoku requires all-different coverage in 27 overlapping units; Map only separates graph-adjacent region pairs | Near, `0.750000` |

## Taxonomy impact

- Added `CON-128` and `COMB-0077`.
- Extended `ACT-007`, `CON-001`, `CON-009`, `INF-001`, `OBJ-006` and
  `TIM-002`.
- No existing record required split, merge or deprecation.

## Negative results

- Dragging a visible colour does not move or duplicate an object; it is the
  input modality for assigning that palette value, so no new action is needed.
- Point-only contact is not adjacency. The two decoded corner-only pairs prove
  the boundary predicate cannot be approximated by diagonal cell proximity.
- Pairwise inequality is not all-different unit coverage: distant regions may
  repeat colours freely, and even neighbours of one region may match each other
  when they do not share their own boundary.
- Pencil stipples, conflict markers and the completion flash are optional
  notation or feedback, not required solution-state genes.
- Map generation does not occur during solving and is outside the genome.
