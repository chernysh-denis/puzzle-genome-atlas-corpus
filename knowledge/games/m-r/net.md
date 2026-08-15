---
game_id: GAME-0083
slug: net
game_title: Net
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0083
gene_ids:
  action:
    - ACT-083
  system: []
  constraint:
    - CON-001
    - CON-058
    - CON-115
    - CON-122
  information:
    - INF-001
  objective:
    - OBJ-006
  time:
    - TIM-002
---

# Game: Net

## Analysis scope

- Version / ruleset: Simon Tatham's Portable Puzzle Collection, current desktop
  default `5 × 5`, non-wrapping, unique solution, no optional barriers; exact
  game ID `5x5:1319827eb3e918b6ae4b1a326`.
- Included: clockwise, anticlockwise and half-turn rotation of one addressed
  tile; immutable straight, corner, endpoint and T-junction port shapes; mutual
  orthogonal port matching; one spanning connected network; global loop
  prohibition; visible centre-reachability highlighting; locking and revision;
  self-paced solving.
- Excluded: wrapping presets, barrier hints, non-unique mode, changing the
  highlight source, shifting a wrapping grid, jumbling unlocked tiles, Solve,
  Undo, Redo and Restart as interface support.
- Direct-play status: the current official manual, JavaScript version and source
  were inspected at revision `3c3632259d298ab62aafa8a5858823569ab1af46`.
  The exact control was constructed from seed `202608140083` under the current
  hexadecimal description codec and non-wrapping generator invariants. An
  independent row-major orientation enumerator proved exactly one accepted
  25-tile, 24-edge spanning tree.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `NET-001` | The current desktop default is a non-wrapping `5 × 5` grid with uniqueness enabled and barrier probability zero | Confirmed | Direct | High | S1, S2, S3 |
| `NET-002` | Each tile preserves its port shape and may only rotate in place | Confirmed | Direct | High | S1, S2, S3 |
| `NET-003` | A connection exists only when two orthogonally adjacent ports face one another with no barrier between them | Confirmed | Direct | High | S1, S2 |
| `NET-004` | Completion requires every tile to belong to one connected network | Confirmed | Direct | High | S1, S2 |
| `NET-005` | The completed network may contain no closed loop | Confirmed | Direct | High | S1, S2 |
| `NET-006` | Centre-reachable tiles are highlighted from the fully visible current state | Confirmed | Direct | High | S1, S2, S3 |
| `NET-007` | Locking records confidence but neither chooses nor validates an orientation | Confirmed | Direct | High | S1, S2, S3 |
| `NET-008` | The exact control has one unique accepted orientation assignment | Observation | Direct | High | S2, local exhaustive control |
| `NET-009` | In a 25-vertex connected acyclic solution the reciprocal ports induce exactly 24 edges | Observation | Corroborated | High | `NET-003`–`NET-005`, local exhaustive control |

## Basic data

- Release / origin: Simon Tatham credits Pavils Jurjans's Flash game *FreeNet*;
  related implementations are commonly known as *NetWalk*.
- Platform or physical form: open-source desktop and official JavaScript
  single-player network-rotation deduction puzzle.
- Puzzle family: rotate-in-place reciprocal-port spanning-tree reconstruction.
- Primary sources:
  - **[S1] Simon Tatham:** [official Net manual](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/net.html),
    specifying the network, loop prohibition, controls and parameters.
  - **[S2] Simon Tatham:** [current `net.c` implementation](https://git.tartarus.org/?p=simon/puzzles.git;a=blob;f=net.c;hb=HEAD),
    defining defaults, codec, generator, solver and completion traversal.
  - **[S3] Simon Tatham:** [official playable JavaScript version](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/net.html),
    confirming current presentation, rotation and locking semantics.
- Reproducible artefact: `scripts/verify_net_control.py` deterministically
  reconstructs the control, enumerates every locally compatible orientation to
  a second-solution limit, and independently checks connectivity, acyclicity,
  25-tile coverage and 24 reciprocal edges.
- Claim IDs: `NET-001`–`NET-009`.

## Mechanical decomposition

### Action Genes

- `ACT-083` — rotate addressed tile in place. The player selects exactly one
  fixed-position tile and cycles its immutable port mask clockwise,
  anticlockwise or by 180 degrees.
- Lock / unlock is excluded as a confidence annotation: it prevents accidental
  input but does not alter the candidate network.
- Claim IDs: `NET-002`, `NET-007`.

### System Behaviour Genes

- None promoted. Centre-reachability highlighting deterministically renders
  the candidate graph; it neither changes a tile nor selects an orientation.
- Claim IDs: `NET-006`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The 25 addressed positions and their
  immutable tile-shape inventory never change.
- `CON-058` — typed shared-edge compatibility. A port edge must meet the
  reciprocal port of the adjacent tile; the outer boundary behaves as an
  immutable no-port edge in the scoped non-wrapping control.
- `CON-115` — global acyclicity of selected linkage graph. No reciprocal-port
  component may close a cycle.
- `CON-122` — spanning connectivity of required vertices. Every one of the 25
  tiles must be reachable through reciprocal ports in a single component.
- Tile degree is preserved by rotation and is a parameter of the fixed piece,
  not a separately promoted degree-clue constraint.
- Claim IDs: `NET-001`–`NET-005`, `NET-008`, `NET-009`.

### Information Genes

- `INF-001` — fully visible current state. Every tile shape, orientation,
  reciprocal connection, lock and centre-connected highlight is visible before
  the next rotation.
- Claim IDs: `NET-002`, `NET-003`, `NET-006`, `NET-007`.

### Objective Genes

- `OBJ-006` — complete constraint-satisfying assignment. Acceptance requires an
  orientation for every tile whose reciprocal-port graph is one spanning tree.
- Claim IDs: `NET-003`–`NET-005`, `NET-008`, `NET-009`.

### Time Genes

- `TIM-002` — self-paced sequential action. Nothing rotates or advances between
  player edits, and every orientation remains revisable unless voluntarily
  locked.
- Claim IDs: `NET-002`, `NET-007`, `NET-008`.

## Reproducible transitions

Coordinates use rows `A`–`E` and columns `1`–`5`; directions are `R`, `U`, `L`
and `D`.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| `A3=R` | rotate anticlockwise once | endpoint becomes `D`, matching solved mask | one addressed shape rotates without moving | `NET-002` |
| `A2=RU` | half-turn | corner becomes `LD` | degree and corner shape remain invariant | `NET-002` |
| `B2=RUL` | rotate anticlockwise once | T-junction becomes `RUD` | one local edit can change three candidate adjacencies | `NET-002`, `NET-003` |
| `A1=R`, `A2=LD` | inspect their shared edge | `A1.R` meets `A2.L`, creating one reciprocal link | adjacency requires facing ports on both tiles | `NET-003` |
| `A5=L` at the right boundary | inspect exterior edge | no port leaves the grid | non-wrapping boundary rejects outward ports | `NET-001`, `NET-003` |
| Any correctly oriented tile | lock, then attempt rotation | orientation remains fixed until explicitly unlocked | locking is reversible input protection | `NET-007` |
| Exact solved masks | traverse from `A1` | all 25 tiles are reached through 24 reciprocal edges | one connected acyclic spanning network | `NET-004`, `NET-005`, `NET-009` |
| Fixed control after first solution | continue exhaustive enumeration | every other branch violates a boundary, reciprocal edge or spanning-tree test | unique recorded solution | `NET-008` |

The unique solution mask is `1c8948b77cb681e35e1e15616`. The verifier
asserts 25 fixed positions, total port degree 48, exactly 24 reciprocal edges,
complete reachability and exhaustion after the first solution.

## Strategic and experiential structure

- Boundary anchoring: endpoints, corners and T-junctions near an outer edge
  lose every orientation that points outside the grid.
- Reciprocal propagation: fixing one port immediately constrains whether the
  neighbour must face back toward it or avoid that edge.
- Component pressure: locally compatible clusters are insufficient if they
  cannot eventually join the centre-reachable component.
- Loop avoidance: a final tempting edge may be locally reciprocal yet invalid
  because its endpoints are already in the same component.
- Shape conservation: the tile's degree never changes, so each rotation spends
  the same fixed number of incident ports in different directions.
- Claim IDs: `NET-002`–`NET-009`.

## Replay and variation

- A new generated spanning tree changes tile shapes, their shuffled
  orientations and the deduction order while preserving the scoped gene set.
- Width and height alter the fixed topology. Wrapping changes boundary
  adjacency; barriers add immutable forbidden edges; disabling uniqueness
  changes the solution-set guarantee rather than the basic rotation action.
- Moving the highlight centre, locking tiles and jumbling only unlocked tiles
  are inference or interface aids, not required answer state.
- Claim IDs: `NET-001`, `NET-006`–`NET-008`.

## Adjacent systems and history

- Slant shares global acyclicity, but assigns one diagonal edge per cell under
  local vertex clues and may finish as several disconnected trees.
- Bridges shares spanning connectivity, but directly edits multiplicities
  between clue vertices; cycles are permitted and pieces do not rotate.
- Pipe Mania has rotatable-looking pipe geometry, but its scoped queue action
  places supplied pieces before irreversible live flow instead of rotating a
  complete static inventory into an undirected tree.
- Dorfromantik and Carto share typed edge compatibility, but place or rearrange
  terrain tiles and do not require every tile to form one acyclic network.
- Claim IDs: `NET-002`–`NET-005`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-083` | tile address; clockwise, anticlockwise or half-turn |
| System Behaviour | none | connectivity highlight is presentation |
| Constraint | `CON-001`, `CON-058`, `CON-115`, `CON-122` | 5 × 5 topology; fixed port masks; no wrap; zero barriers |
| Information | `INF-001` | shapes, ports, locks and connected component visible |
| Objective | `OBJ-006` | one complete spanning tree |
| Time | `TIM-002` | self-paced reversible rotation |

Canonical signature:

`ACT-083; CON-001,CON-058,CON-115,CON-122; INF-001; OBJ-006; TIM-002`

## Corpus comparison

- Indexed games and combinations scanned: `GAME-0001`–`GAME-0082` and
  `COMB-0001`–`COMB-0082`.
- Exact genome matches: none.
- Near match: `GAME-0071` Slant is uniquely nearest at
  `5 / 10 = 0.500000`.
- Next structural match: `GAME-0074` Bridges at `5 / 12 = 0.416667`.
- Nine assignment puzzles tie at `4 / 11 = 0.363636`; Signpost, Pearl, Tents
  and Hexologic follow at `4 / 12 = 0.333333`.
- Supported combination subsets: none before `COMB-0083`.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0071` — Slant | `CON-001`, `CON-115`, `INF-001`, `OBJ-006`, `TIM-002` | binary diagonal assignment with vertex degrees; spanning connectivity is absent | nearest, `5 / 10 = 0.500000` |
| `GAME-0074` — Bridges | `CON-001`, `CON-122`, `INF-001`, `OBJ-006`, `TIM-002` | multiplicity editing between clue islands; cycles allowed and no tile ports rotate | next, `5 / 12 = 0.416667` |
| `GAME-0040` — Carto | `CON-058`, `INF-001`, `TIM-002` | persistent map fragments move and rotate under terrain-edge matching without one spanning tree | structural contrast, `3 / 13 = 0.230769` |
| `GAME-0016` — Pipe Mania | `INF-001`, `TIM-002` | supplied tiles are placed before live directed flow; no static full-grid reconstruction | family-name contrast, `2 / 21 = 0.095238` |

- Full numeric scan (`intersection / union = Jaccard`):
  - `GAME-0001`: `2 / 20 = 0.100000`; `GAME-0002`: `3 / 12 = 0.250000`; `GAME-0003`: `1 / 16 = 0.062500`; `GAME-0004`: `2 / 21 = 0.095238`; `GAME-0005`: `4 / 11 = 0.363636`; `GAME-0006`: `3 / 14 = 0.214286`; `GAME-0007`: `2 / 14 = 0.142857`; `GAME-0008`: `4 / 11 = 0.363636`.
  - `GAME-0009`: `2 / 22 = 0.090909`; `GAME-0010`: `2 / 15 = 0.133333`; `GAME-0011`: `3 / 18 = 0.166667`; `GAME-0012`: `4 / 13 = 0.307692`; `GAME-0013`: `2 / 19 = 0.105263`; `GAME-0014`: `2 / 21 = 0.095238`; `GAME-0015`: `2 / 20 = 0.100000`; `GAME-0016`: `2 / 21 = 0.095238`.
  - `GAME-0017`: `0 / 21 = 0.000000`; `GAME-0018`: `1 / 26 = 0.038462`; `GAME-0019`: `2 / 16 = 0.125000`; `GAME-0020`: `2 / 20 = 0.100000`; `GAME-0021`: `1 / 16 = 0.062500`; `GAME-0022`: `1 / 19 = 0.052632`; `GAME-0023`: `1 / 17 = 0.058824`; `GAME-0024`: `2 / 18 = 0.111111`.
  - `GAME-0025`: `1 / 18 = 0.055556`; `GAME-0026`: `1 / 19 = 0.052632`; `GAME-0027`: `2 / 18 = 0.111111`; `GAME-0028`: `2 / 23 = 0.086957`; `GAME-0029`: `2 / 18 = 0.111111`; `GAME-0030`: `1 / 21 = 0.047619`; `GAME-0031`: `1 / 18 = 0.055556`; `GAME-0032`: `2 / 17 = 0.117647`.
  - `GAME-0033`: `1 / 20 = 0.050000`; `GAME-0034`: `1 / 21 = 0.047619`; `GAME-0035`: `1 / 25 = 0.040000`; `GAME-0036`: `2 / 18 = 0.111111`; `GAME-0037`: `2 / 15 = 0.133333`; `GAME-0038`: `1 / 23 = 0.043478`; `GAME-0039`: `4 / 13 = 0.307692`; `GAME-0040`: `3 / 13 = 0.230769`.
  - `GAME-0041`: `1 / 18 = 0.055556`; `GAME-0042`: `1 / 16 = 0.062500`; `GAME-0043`: `2 / 20 = 0.100000`; `GAME-0044`: `2 / 16 = 0.125000`; `GAME-0045`: `2 / 20 = 0.100000`; `GAME-0046`: `2 / 16 = 0.125000`; `GAME-0047`: `2 / 20 = 0.100000`; `GAME-0048`: `2 / 20 = 0.100000`.
  - `GAME-0049`: `1 / 16 = 0.062500`; `GAME-0050`: `2 / 21 = 0.095238`; `GAME-0051`: `1 / 23 = 0.043478`; `GAME-0052`: `1 / 17 = 0.058824`; `GAME-0053`: `2 / 15 = 0.133333`; `GAME-0054`: `2 / 17 = 0.117647`; `GAME-0055`: `2 / 16 = 0.125000`; `GAME-0056`: `2 / 14 = 0.142857`.
  - `GAME-0057`: `2 / 14 = 0.142857`; `GAME-0058`: `2 / 15 = 0.133333`; `GAME-0059`: `2 / 13 = 0.153846`; `GAME-0060`: `1 / 14 = 0.071429`; `GAME-0061`: `4 / 14 = 0.285714`; `GAME-0062`: `4 / 12 = 0.333333`; `GAME-0063`: `3 / 12 = 0.250000`; `GAME-0064`: `2 / 11 = 0.181818`.
  - `GAME-0065`: `1 / 14 = 0.071429`; `GAME-0066`: `1 / 17 = 0.058824`; `GAME-0067`: `0 / 16 = 0.000000`; `GAME-0068`: `1 / 15 = 0.066667`; `GAME-0069`: `3 / 13 = 0.230769`; `GAME-0070`: `2 / 14 = 0.142857`; `GAME-0071`: `5 / 10 = 0.500000`; `GAME-0072`: `4 / 12 = 0.333333`.
  - `GAME-0073`: `4 / 11 = 0.363636`; `GAME-0074`: `5 / 12 = 0.416667`; `GAME-0075`: `4 / 13 = 0.307692`; `GAME-0076`: `4 / 11 = 0.363636`; `GAME-0077`: `4 / 11 = 0.363636`; `GAME-0078`: `4 / 11 = 0.363636`; `GAME-0079`: `4 / 11 = 0.363636`; `GAME-0080`: `4 / 11 = 0.363636`.
  - `GAME-0081`: `4 / 12 = 0.333333`; `GAME-0082`: `4 / 12 = 0.333333`.

## Combination candidate

- Candidate ID: `COMB-0083`.
- Gene set: `ACT-083`, `CON-058`, `CON-115`, `CON-122`, `OBJ-006`,
  `TIM-002`.
- Decision structure: rotate fixed-position port masks until their reciprocal
  adjacencies simultaneously form one connected acyclic graph over every tile.
- Supporting games: `GAME-0083` only.
- Distinctness: no prior combination couples local port compatibility with
  both spanning connectivity and acyclicity through rotation-only editing.

## Outcome

- Reused genes: `CON-001`, `CON-058`, `CON-115`, `CON-122`, `INF-001`,
  `OBJ-006`, `TIM-002`.
- Added gene: `ACT-083`.
- Rejected candidates: reachability highlighting as System Behaviour; lock /
  unlock as a mechanical action; tile degree as a clue constraint; reciprocal
  port matching as a new constraint instead of extending `CON-058`.
- Registered combination: `COMB-0083`.
- Taxonomy change: broadened `CON-058` from terrain types to static binary port
  compatibility while preserving its shared-edge boundary.
- Next falsification target: the next adaptive-selection candidate will test a
  different sparse action / constraint region after the 83-game map refresh.

## Taxonomy impact

- Added `ACT-083` and `COMB-0083`.
- Extended `CON-058`, `CON-115`, `CON-122`, `CON-001`, `INF-001`, `OBJ-006`
  and `TIM-002` with Net evidence.
- No lifecycle changes or merges.

## Negative results

- No hidden state, automatic progression, resource economy, score optimisation
  or failure clock belongs to the scoped control.
- A visually connected subset is not success; all 25 tiles must be in one
  component and that component must remain acyclic.
- A local dangling port is not a separate terminal rule: it fails reciprocal
  edge compatibility and prevents the spanning-tree objective.
- Locks and connected-colour highlighting are optional inference aids.

## Delta summary

- Corpus: 82 → 83 reviewed games.
- Active genes: 413 → 414.
- Registered combinations: 82 → 83.
- New operational boundary: rotate exactly one fixed-position tile while
  preserving its port shape.

## Нові факти

- Стандартна гра Net — це поле `5 × 5`, де кожна плитка зберігає форму портів і
  лише обертається на місці.
- Перемога вимагає одного зв’язного дерева: усі 25 плиток, 24 взаємні ребра і
  жодного циклу.
- Контроль `5x5:1319827eb3e918b6ae4b1a326` має рівно один розв’язок.

## Нові гени

- `ACT-083` — обертати адресовану плитку на місці.
- Нового constraint-гену не потрібно: сумісність портів, ациклічність і повна
  зв’язність уже точно покривають `CON-058`, `CON-115` та `CON-122`.

## Нові комбінації

- `COMB-0083` — поворот портових плиток у зв’язне ациклічне покривне дерево.

## Зміни таксономії

- Межу `CON-058` розширено на бінарні порт / не-порт ребра без живого потоку.
- Підсвічування компоненти й блокування плитки залишено інформаційними
  засобами, а не окремими механіками.

## Український підсумок

Net дає Атласу чисту механіку обертання нерухомих плиток. Гравець не малює
ребра й не пересуває деталі: він змінює орієнтацію сталої форми портів. Локальні
взаємні стики мають зійтися у глобально єдину мережу без циклів, тому задача
поєднує крайові дедукції, поширення сумісності та контроль компонент. Повний
перебір підтверджує, що зафіксований контроль має один розв’язок.
