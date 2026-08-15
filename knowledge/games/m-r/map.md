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

- Indexed games and combinations scanned: `GAME-0001`–`GAME-0076` and
  `COMB-0001`–`COMB-0076`.
- Exact genome matches: none.
- Near match: `GAME-0005` Sudoku at `6 / 8 = 0.750000`, sharing every gene
  except Map's pairwise region-adjacency exclusion versus Sudoku's
  all-different unit coverage.
- Next near games: Nonogram and Slant tie at `5 / 9 = 0.555556`; Hexologic and
  Tents tie at `5 / 10 = 0.500000`.
- Supported combination subsets: none before `COMB-0077`.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0005` — Sudoku | `ACT-007`, `CON-001`, `CON-009`, `INF-001`, `OBJ-006`, `TIM-002` | Sudoku requires all-different coverage in 27 overlapping units; Map only separates graph-adjacent region pairs | unique nearest, `6 / 8 = 0.750000` |
| `GAME-0008` — Nonogram | `ACT-007`, `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | Nonogram has ordered binary runs and no immutable assigned values | tied next, `5 / 9 = 0.555556` |
| `GAME-0071` — Slant | `ACT-007`, `CON-001`, `INF-001`, `OBJ-006`, `TIM-002` | Slant constrains diagonal incidence and forbids cycles | tied next, `5 / 9 = 0.555556` |

- Full numeric scan (`intersection / union = Jaccard`):
  - `GAME-0001`: `2 / 19 = 0.105263`; `GAME-0002`: `3 / 11 = 0.272727`; `GAME-0003`: `1 / 15 = 0.066667`; `GAME-0004`: `2 / 20 = 0.100000`; `GAME-0005`: `6 / 8 = 0.750000`; `GAME-0006`: `3 / 13 = 0.230769`; `GAME-0007`: `2 / 13 = 0.153846`; `GAME-0008`: `5 / 9 = 0.555556`.
  - `GAME-0009`: `2 / 21 = 0.095238`; `GAME-0010`: `2 / 14 = 0.142857`; `GAME-0011`: `3 / 17 = 0.176471`; `GAME-0012`: `4 / 12 = 0.333333`; `GAME-0013`: `2 / 18 = 0.111111`; `GAME-0014`: `2 / 20 = 0.100000`; `GAME-0015`: `2 / 19 = 0.105263`; `GAME-0016`: `2 / 20 = 0.100000`.
  - `GAME-0017`: `0 / 20 = 0.000000`; `GAME-0018`: `1 / 25 = 0.040000`; `GAME-0019`: `2 / 15 = 0.133333`; `GAME-0020`: `1 / 20 = 0.050000`; `GAME-0021`: `1 / 15 = 0.066667`; `GAME-0022`: `1 / 18 = 0.055556`; `GAME-0023`: `1 / 16 = 0.062500`; `GAME-0024`: `2 / 17 = 0.117647`.
  - `GAME-0025`: `1 / 17 = 0.058824`; `GAME-0026`: `1 / 18 = 0.055556`; `GAME-0027`: `2 / 17 = 0.117647`; `GAME-0028`: `2 / 22 = 0.090909`; `GAME-0029`: `2 / 17 = 0.117647`; `GAME-0030`: `1 / 20 = 0.050000`; `GAME-0031`: `1 / 17 = 0.058824`; `GAME-0032`: `2 / 16 = 0.125000`.
  - `GAME-0033`: `1 / 19 = 0.052632`; `GAME-0034`: `1 / 20 = 0.050000`; `GAME-0035`: `1 / 24 = 0.041667`; `GAME-0036`: `2 / 17 = 0.117647`; `GAME-0037`: `2 / 14 = 0.142857`; `GAME-0038`: `1 / 22 = 0.045455`; `GAME-0039`: `4 / 12 = 0.333333`; `GAME-0040`: `2 / 13 = 0.153846`.
  - `GAME-0041`: `1 / 17 = 0.058824`; `GAME-0042`: `1 / 15 = 0.066667`; `GAME-0043`: `2 / 19 = 0.105263`; `GAME-0044`: `2 / 15 = 0.133333`; `GAME-0045`: `2 / 19 = 0.105263`; `GAME-0046`: `2 / 15 = 0.133333`; `GAME-0047`: `2 / 19 = 0.105263`; `GAME-0048`: `2 / 19 = 0.105263`.
  - `GAME-0049`: `1 / 15 = 0.066667`; `GAME-0050`: `2 / 20 = 0.100000`; `GAME-0051`: `1 / 22 = 0.045455`; `GAME-0052`: `1 / 16 = 0.062500`; `GAME-0053`: `2 / 14 = 0.142857`; `GAME-0054`: `2 / 16 = 0.125000`; `GAME-0055`: `2 / 15 = 0.133333`; `GAME-0056`: `2 / 13 = 0.153846`.
  - `GAME-0057`: `2 / 13 = 0.153846`; `GAME-0058`: `2 / 14 = 0.142857`; `GAME-0059`: `2 / 12 = 0.166667`; `GAME-0060`: `1 / 13 = 0.076923`; `GAME-0061`: `4 / 13 = 0.307692`; `GAME-0062`: `5 / 10 = 0.500000`; `GAME-0063`: `3 / 11 = 0.272727`; `GAME-0064`: `2 / 10 = 0.200000`.
  - `GAME-0065`: `1 / 13 = 0.076923`; `GAME-0066`: `2 / 15 = 0.133333`; `GAME-0067`: `0 / 15 = 0.000000`; `GAME-0068`: `1 / 14 = 0.071429`; `GAME-0069`: `3 / 12 = 0.250000`; `GAME-0070`: `2 / 13 = 0.153846`; `GAME-0071`: `5 / 9 = 0.555556`; `GAME-0072`: `5 / 10 = 0.500000`.
  - `GAME-0073`: `4 / 10 = 0.400000`; `GAME-0074`: `4 / 12 = 0.333333`; `GAME-0075`: `5 / 11 = 0.454545`; `GAME-0076`: `4 / 10 = 0.400000`.
- Scan date: 2026-08-14.

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

## Delta summary

- Added one reviewed game, one active gene and one verified combination.
- Added one exact-control verifier and one deterministic rule-valid artwork.
- Corpus size becomes 77 reviewed games, 405 active genes and 77 combinations.

## Нові факти

- Зафіксовано точний стандартний контроль із 300 клітинами, 30 регіонами, 66
  суміжностями, 13 незмінними кольорами й одним повним розв’язком.
- Дві пари з кутовим контактом окремо підтвердили, що точка не є спільною межею.

## Нові гени

- `CON-128` — виключення однакового класу для регіонів зі спільною межею.

## Нові комбінації

- `COMB-0077` — повне розфарбування регіонів із незмінними стартовими кольорами.

## Зміни таксономії

- Одну нову межу активовано без зміни попередніх визначень.
