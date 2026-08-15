---
game_id: GAME-0084
slug: netslide
game_title: Netslide
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0084
gene_ids:
  action:
    - ACT-084
  system: []
  constraint:
    - CON-001
    - CON-004
    - CON-005
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

# Game: Netslide

## Analysis scope

- Version / ruleset: Simon Tatham's Portable Puzzle Collection, current desktop
  default `3 × 3 easy`; non-wrapping network edges, barrier probability `1`,
  automatic eight-move shuffle; exact game ID
  `3x3b1:cvah28cv1bv36`.
- Included: cyclic one-position displacement of one non-central row or column;
  unchanged tile orientation and port mask; fixed centre tile; stationary
  barrier hints on all four solved non-edges; mutual orthogonal port matching;
  one spanning connected acyclic network; complete visibility, revision,
  move counting and self-paced solving.
- Excluded: medium and hard presets, larger fields, wrapping network edges,
  custom barrier probabilities and shuffle counts, Solve, Undo, Redo and
  Restart as interface support.
- Direct-play status: the current official manual, JavaScript version and source
  were inspected at revision `3c3632259d298ab62aafa8a5858823569ab1af46`.
  The exact control was constructed from seed `202608140084` under the current
  description codec and default generator invariants. An exhaustive
  move-graph traversal visited all 20,160 reachable arrangements, proved one
  accepted 9-tile network and found its shortest distance of five moves.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `NSL-001` | The current desktop default is `3 × 3 easy`, with non-wrapping network edges and barrier probability one | Confirmed | Direct | High | S1, S2, S3 |
| `NSL-002` | One action cyclically shifts every tile in one non-central row or column by one position | Confirmed | Direct | High | S1, S2, S3 |
| `NSL-003` | A shifted tile preserves its orientation and port mask | Confirmed | Direct | High | S1, S2 |
| `NSL-004` | The centre tile stays fixed because its row and column have no move arrows | Confirmed | Direct | High | S2, S3 |
| `NSL-005` | Completion requires every tile to be reachable from the centre through reciprocal unbarred ports | Confirmed | Direct | High | S2 |
| `NSL-006` | The inherited generated network is acyclic; with total port degree 16, full connectivity induces exactly eight edges and no loop | Confirmed | Corroborated | High | S1, S2, local exhaustive control |
| `NSL-007` | Every primitive line shift has the opposite shift as an exact inverse | Observation | Direct | High | S2, local exhaustive control |
| `NSL-008` | With eight distinct outer tiles, legal three-cycles reach exactly the 20,160 even permutations and exclude the other half of `8!` | Observation | Direct | High | local exhaustive control |
| `NSL-009` | The exact control has one accepted arrangement at shortest distance five | Observation | Direct | High | local exhaustive control |

## Basic data

- Release / origin: contributed to Simon Tatham's collection by Richard
  Boulton; the manual describes it as Net generation combined with Sixteen
  movement.
- Platform or physical form: open-source desktop and official JavaScript
  single-player cyclic-line permutation puzzle.
- Puzzle family: toroidal row-column permutation of fixed-orientation network
  tiles under a stationary barrier graph.
- Primary sources:
  - **[S1] Simon Tatham:** [official Netslide manual](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/netslide.html),
    defining the Net / Sixteen hybrid and controls.
  - **[S2] Simon Tatham and Richard Boulton:** [current `netslide.c` implementation](https://git.tartarus.org/?p=simon/puzzles.git;a=blob;f=netslide.c;hb=HEAD),
    defining defaults, generator, cyclic shifts, codec and completion traversal.
  - **[S3] Simon Tatham:** [official playable JavaScript version](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/netslide.html),
    confirming the current arrows, fixed centre and presentation.
- Reproducible artefact: `scripts/verify_netslide_control.py` regenerates the
  exact tree, barrier graph and shuffle, decodes the public ID, exhausts the
  full reachable move graph, reconstructs a shortest solution and checks the
  parity boundary independently of the web presentation.
- Claim IDs: `NSL-001`–`NSL-009`.

## Mechanical decomposition

### Action Genes

- `ACT-084` — cyclically shift addressed line. The player selects one eligible
  row or column and translates every tile in it one position in the same
  direction, wrapping the displaced end tile to the opposite end.
- The action changes tile positions but never rotates their port masks.
- Claim IDs: `NSL-002`–`NSL-004`.

### System Behaviour Genes

- None promoted. Centre-component highlighting and the short slide animation
  render the result of a committed line permutation without adding a second
  state transition.
- Claim IDs: `NSL-005`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. Nine addressed cells stay occupied by
  the same finite inventory; the centre occupant is fixed and eight outer tile
  identities are permuted.
- `CON-004` — invariant-constrained reachability. Every length-three line move
  is an even 3-cycle, so the eight distinct outer tiles occupy only the 20,160
  even permutations rather than all 40,320 arrangements.
- `CON-005` — primitive action reversibility. Shifting the same line one step
  in the opposite direction restores the immediately preceding state exactly.
- `CON-058` — typed shared-edge compatibility. Reciprocal ports connect only
  across an unbarred orthogonal edge; all four easy-mode barriers stay fixed
  while tiles move.
- `CON-115` — global acyclicity of selected linkage graph. The inherited Net
  solution is one tree; total fixed port degree prevents a connected accepted
  arrangement from also containing a cycle.
- `CON-122` — spanning connectivity of required vertices. All nine tiles must
  be reachable from the fixed centre through reciprocal unbarred ports.
- Claim IDs: `NSL-001`–`NSL-009`.

### Information Genes

- `INF-001` — fully visible current state. All tile masks, positions, fixed
  barriers, movement arrows, move count and the centre-connected component are
  visible before the next shift.
- Claim IDs: `NSL-001`–`NSL-005`, `NSL-009`.

### Objective Genes

- `OBJ-006` — complete constraint-satisfying assignment. Success requires one
  reachable tile arrangement whose reciprocal unbarred ports connect every
  position into the accepted spanning tree.
- Claim IDs: `NSL-005`, `NSL-006`, `NSL-008`, `NSL-009`.

### Time Genes

- `TIM-002` — self-paced sequential action. The board changes only after one
  discrete line shift and waits indefinitely for the next choice.
- Claim IDs: `NSL-002`, `NSL-007`, `NSL-009`.

## Reproducible transitions

Rows are `A`–`C`, columns are `1`–`3`; `R0-` means top row left and `C2+`
means right column down.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| top row masks `c,a,2` | `R0-` | top row becomes `a,2,c`; every port mask is unchanged | cyclic coupled line displacement | `NSL-002`, `NSL-003` |
| any state after `R0-` | `R0+` | the preceding arrangement is restored exactly | primitive inverse | `NSL-007` |
| centre mask `c` at `B2` | inspect available arrows | neither row `B` nor column `2` can shift | fixed centre anchor | `NSL-004` |
| a port pair across a `v` or `h` marker | inspect connection | traversal stops even when both ports face one another | barriers remain stationary edge constraints | `NSL-001`, `NSL-005` |
| start `ca28c1b36` | `R0-, C2-, R0-, C0-, C2+` | masks become `81cbca236` | one shortest five-move solution | `NSL-009` |
| solved masks `81cbca236` | traverse from `B2` | all nine cells are reached through eight reciprocal unbarred edges | complete spanning tree | `NSL-005`, `NSL-006` |
| full move graph | exhaust all line shifts | exactly 20,160 arrangements are reachable and only `81cbca236` is accepted | parity boundary and uniqueness | `NSL-008`, `NSL-009` |

The four internal easy-mode barriers decode from `v` and `h` suffixes in
`cvah28cv1bv36`. The verifier additionally asserts eight distinct outer tile
masks, fixed centre mask `c`, total port degree 16 and no second accepted
arrangement anywhere in the reachable component.

## Strategic and experiential structure

- Coupled displacement: improving one local port match moves two other tiles
  in the same line and may break their adjacencies.
- Fixed-centre planning: the middle tile is an immovable reference around
  which the four movable lines permute the outer ring indirectly.
- Barrier anchoring: easy-mode walls identify edges that can never carry the
  final network even while different tiles pass beside them.
- Parity reasoning: an apparently correct odd swap is mechanically unreachable;
  progress must be expressed as compositions of even three-cycles.
- Component feedback: newly centre-connected branches reveal structural
  progress, but a large component can still require deliberate temporary
  disconnection to permute its tiles.
- Claim IDs: `NSL-002`–`NSL-009`.

## Replay and variation

- New generated trees, barrier placements and shuffle sequences change the
  target arrangement and shortest route while preserving line-shift semantics.
- Medium removes barrier hints; hard lets network edges wrap across boundaries.
  Larger grids change cycle lengths and therefore the permutation invariants.
- Custom shuffle count changes the generation walk and displayed move target,
  not the primitive action.
- Claim IDs: `NSL-001`–`NSL-009`.

## Adjacent systems and history

- Net shares the same reciprocal-port spanning-tree target, but changes one
  tile's orientation in place; Netslide preserves orientation and instead
  permutes three tiles together.
- Rubik's Cube shares reversible coupled permutations and parity-constrained
  reachability, but rotates a three-dimensional layer toward a specified
  sticker arrangement rather than validating a port graph.
- 2048 and Threes apply one direction globally across all eligible lines and
  then resolve compression or merging; Netslide selects exactly one line and
  performs a fixed cyclic permutation with no merge.
- Lights Out shares reversible invariant-constrained reachability, but one
  addressed press toggles binary values instead of permuting persistent tiles.
- Claim IDs: `NSL-002`–`NSL-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-084` | eligible line; direction; one-position cyclic distance |
| System Behaviour | none | animation and component highlight are presentation |
| Constraint | `CON-001`, `CON-004`, `CON-005`, `CON-058`, `CON-115`, `CON-122` | 3 × 3; fixed centre; four barriers; non-wrapping network |
| Information | `INF-001` | masks, positions, barriers and component visible |
| Objective | `OBJ-006` | one reachable spanning tree |
| Time | `TIM-002` | self-paced line shifts |

Canonical signature:

`ACT-084; CON-001,CON-004,CON-005,CON-058,CON-115,CON-122; INF-001; OBJ-006; TIM-002`

## Corpus comparison

- Indexed games and combinations scanned: `GAME-0001`–`GAME-0083` and
  `COMB-0001`–`COMB-0083`.
- Exact genome matches: none.
- Near match: `GAME-0083` Net is uniquely nearest at
  `7 / 11 = 0.636364`.
- Slant and Rubik's Cube tie next at `5 / 12 = 0.416667`; Lights Out follows at
  `5 / 13 = 0.384615`, then Bridges at `5 / 14 = 0.357143`.
- Supported combination subsets: none before `COMB-0084`.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0083` — Net | `CON-001`, `CON-058`, `CON-115`, `CON-122`, `INF-001`, `OBJ-006`, `TIM-002` | rotates one tile; no permutation-reachability or primitive-inverse genes | nearest, `7 / 11 = 0.636364` |
| `GAME-0002` — Rubik's Cube | `CON-001`, `CON-004`, `CON-005`, `INF-001`, `TIM-002` | rotates a coupled 3D layer toward an exact sticker arrangement; no port graph | tied next, `5 / 12 = 0.416667` |
| `GAME-0071` — Slant | `CON-001`, `CON-115`, `INF-001`, `OBJ-006`, `TIM-002` | directly assigns diagonals under degree clues; disconnected forest allowed | tied next, `5 / 12 = 0.416667` |
| `GAME-0069` — Lights Out | `CON-001`, `CON-004`, `CON-005`, `OBJ-006`, `TIM-002` | toggles binary neighbourhoods; no moving inventory or network target | next invariant match, `5 / 13 = 0.384615` |

- Full numeric scan (`intersection / union = Jaccard`):
  - `GAME-0001`: `2 / 22 = 0.090909`; `GAME-0002`: `5 / 12 = 0.416667`; `GAME-0003`: `1 / 18 = 0.055556`; `GAME-0004`: `2 / 23 = 0.086957`; `GAME-0005`: `4 / 13 = 0.307692`; `GAME-0006`: `3 / 16 = 0.187500`; `GAME-0007`: `2 / 16 = 0.125000`; `GAME-0008`: `4 / 13 = 0.307692`.
  - `GAME-0009`: `2 / 24 = 0.083333`; `GAME-0010`: `2 / 17 = 0.117647`; `GAME-0011`: `3 / 20 = 0.150000`; `GAME-0012`: `4 / 15 = 0.266667`; `GAME-0013`: `2 / 21 = 0.095238`; `GAME-0014`: `2 / 23 = 0.086957`; `GAME-0015`: `2 / 22 = 0.090909`; `GAME-0016`: `2 / 23 = 0.086957`.
  - `GAME-0017`: `0 / 23 = 0.000000`; `GAME-0018`: `1 / 28 = 0.035714`; `GAME-0019`: `2 / 18 = 0.111111`; `GAME-0020`: `2 / 22 = 0.090909`; `GAME-0021`: `1 / 18 = 0.055556`; `GAME-0022`: `1 / 21 = 0.047619`; `GAME-0023`: `1 / 19 = 0.052632`; `GAME-0024`: `2 / 20 = 0.100000`.
  - `GAME-0025`: `1 / 20 = 0.050000`; `GAME-0026`: `1 / 21 = 0.047619`; `GAME-0027`: `2 / 20 = 0.100000`; `GAME-0028`: `2 / 25 = 0.080000`; `GAME-0029`: `2 / 20 = 0.100000`; `GAME-0030`: `1 / 23 = 0.043478`; `GAME-0031`: `1 / 20 = 0.050000`; `GAME-0032`: `2 / 19 = 0.105263`.
  - `GAME-0033`: `1 / 22 = 0.045455`; `GAME-0034`: `1 / 23 = 0.043478`; `GAME-0035`: `1 / 27 = 0.037037`; `GAME-0036`: `2 / 20 = 0.100000`; `GAME-0037`: `2 / 17 = 0.117647`; `GAME-0038`: `1 / 25 = 0.040000`; `GAME-0039`: `4 / 15 = 0.266667`; `GAME-0040`: `3 / 15 = 0.200000`.
  - `GAME-0041`: `1 / 20 = 0.050000`; `GAME-0042`: `1 / 18 = 0.055556`; `GAME-0043`: `2 / 22 = 0.090909`; `GAME-0044`: `2 / 18 = 0.111111`; `GAME-0045`: `2 / 22 = 0.090909`; `GAME-0046`: `2 / 18 = 0.111111`; `GAME-0047`: `2 / 22 = 0.090909`; `GAME-0048`: `2 / 22 = 0.090909`.
  - `GAME-0049`: `1 / 18 = 0.055556`; `GAME-0050`: `2 / 23 = 0.086957`; `GAME-0051`: `1 / 25 = 0.040000`; `GAME-0052`: `1 / 19 = 0.052632`; `GAME-0053`: `2 / 17 = 0.117647`; `GAME-0054`: `2 / 19 = 0.105263`; `GAME-0055`: `2 / 18 = 0.111111`; `GAME-0056`: `2 / 16 = 0.125000`.
  - `GAME-0057`: `2 / 16 = 0.125000`; `GAME-0058`: `2 / 17 = 0.117647`; `GAME-0059`: `2 / 15 = 0.133333`; `GAME-0060`: `1 / 16 = 0.062500`; `GAME-0061`: `4 / 16 = 0.250000`; `GAME-0062`: `4 / 14 = 0.285714`; `GAME-0063`: `3 / 14 = 0.214286`; `GAME-0064`: `2 / 13 = 0.153846`.
  - `GAME-0065`: `1 / 16 = 0.062500`; `GAME-0066`: `1 / 19 = 0.052632`; `GAME-0067`: `0 / 18 = 0.000000`; `GAME-0068`: `1 / 17 = 0.058824`; `GAME-0069`: `5 / 13 = 0.384615`; `GAME-0070`: `2 / 16 = 0.125000`; `GAME-0071`: `5 / 12 = 0.416667`; `GAME-0072`: `4 / 14 = 0.285714`.
  - `GAME-0073`: `4 / 13 = 0.307692`; `GAME-0074`: `5 / 14 = 0.357143`; `GAME-0075`: `4 / 15 = 0.266667`; `GAME-0076`: `4 / 13 = 0.307692`; `GAME-0077`: `4 / 13 = 0.307692`; `GAME-0078`: `4 / 13 = 0.307692`; `GAME-0079`: `4 / 13 = 0.307692`; `GAME-0080`: `4 / 13 = 0.307692`.
  - `GAME-0081`: `4 / 14 = 0.285714`; `GAME-0082`: `4 / 14 = 0.285714`; `GAME-0083`: `7 / 11 = 0.636364`.

## Combination candidate

- Candidate ID: `COMB-0084`.
- Gene set: `ACT-084`, `CON-004`, `CON-005`, `CON-058`, `CON-115`,
  `CON-122`, `OBJ-006`, `TIM-002`.
- Decision structure: compose reversible cyclic line permutations inside an
  even-parity reachable component until fixed-orientation ports form one
  reciprocal, connected and acyclic network.
- Supporting games: `GAME-0084` only.
- Distinctness: Net supplies the target graph but not permutation actions;
  Rubik's Cube and Lights Out supply reversible invariant-constrained action
  spaces but not a shared-edge spanning-tree validity predicate.

## Outcome

- Reused genes: `CON-001`, `CON-004`, `CON-005`, `CON-058`, `CON-115`,
  `CON-122`, `INF-001`, `OBJ-006`, `TIM-002`.
- Added gene: `ACT-084`.
- Rejected candidates: cyclic end wrap as a separate System Behaviour;
  stationary barriers as immutable assignments; fixed centre as its own gene;
  connected-component highlighting as autonomous propagation.
- Registered combination: `COMB-0084`.
- Taxonomy change: none beyond adding the new line-permutation action and new
  evidence for the existing invariant / reversibility boundaries.
- Next falsification target: The Room remains the high-information candidate
  for diegetic multi-part mechanism manipulation after this controlled
  network-family contrast.

## Taxonomy impact

- Added `ACT-084` and `COMB-0084`.
- Extended `CON-001`, `CON-004`, `CON-005`, `CON-058`, `CON-115`, `CON-122`,
  `INF-001`, `OBJ-006` and `TIM-002` with Netslide evidence.
- No lifecycle changes, merges or deprecations.

## Negative results

- Netslide does not rotate tiles despite sharing Net's port graphics.
- Cyclic arrival at the opposite end of a shifted line is part of one atomic
  permutation action, not automatic spawning or transport.
- Full connectivity is sufficient in the implementation because fixed total
  port degree then leaves exactly eight edges; a separate hidden loop state is
  not maintained.
- The parity result uses eight distinct outer masks. Without distinguishable
  outer states, an abstract tile-identity parity claim would be mechanically
  invisible and would not support `CON-004`.

## Delta summary

- Corpus: 83 → 84 reviewed games.
- Active genes: 414 → 415.
- Registered combinations: 83 → 84.
- New operational boundary: cyclically displace every persistent element in
  one selected addressed line while keeping each orientation unchanged.

## Нові факти

- Netslide не обертає плитки: один хід циклічно зсуває цілий крайній рядок або
  стовпець, а маски портів зберігають орієнтацію.
- Центральна плитка нерухома; вісім різних зовнішніх плиток мають рівно 20 160
  досяжних парних перестановок замість усіх 40 320.
- Контроль `3x3b1:cvah28cv1bv36` має єдиний розв’язок на мінімальній відстані
  п’ять ходів.

## Нові гени

- `ACT-084` — циклічно зсунути адресований рядок або стовпець.
- Паритет і точний обернений хід повторно використовують `CON-004` і
  `CON-005`; нових constraint-генів не потрібно.

## Нові комбінації

- `COMB-0084` — оборотні паритетно обмежені зсуви ліній до одного покривного
  портового дерева.

## Зміни таксономії

- Нову дію відокремлено від глобального свайпу `ACT-001`, повороту шару
  `ACT-002` і повороту однієї плитки `ACT-083`.
- Зсув із появою плитки на протилежному кінці лишається однією атомарною дією,
  а не системним переміщенням після команди.

## Український підсумок

Netslide бере ціль Net, але повністю змінює простір рішень. Плитки не можна
обертати: треба переставляти їх циклічними зсувами цілих зовнішніх рядків і
стовпців навколо нерухомого центра. Кожен хід оборотний і є парною
перестановкою трьох плиток, тому половина зовні можливих розкладок недосяжна.
Унікальний контроль поєднує цю алгебру рухів зі стаціонарними бар’єрами та
локальними портами, які мають скластися в одне дерево з дев’яти плиток.
