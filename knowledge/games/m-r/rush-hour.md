---
game_id: GAME-0063
slug: rush-hour
game_title: Rush Hour
analysis_status: reviewed
reviewed: 2026-08-13
combination_ids:
  - COMB-0063
gene_ids:
  action:
    - ACT-014
  system: []
  constraint:
    - CON-001
    - CON-007
    - CON-024
  information:
    - INF-001
  objective:
    - OBJ-039
  time:
    - TIM-002
---

# Game: Rush Hour

## Analysis scope

- Version / ruleset: ThinkFun's 2010 standard `#5000` physical edition,
  restricted to Beginner Challenge 1 and the rules printed for that edition.
- Included: the reproducible Challenge 1 start state on a 6 × 6 traffic grid;
  cars of length two and trucks of length three; immutable horizontal or
  vertical orientation; selecting one vehicle and sliding it any unobstructed
  positive distance only along its long axis; complete rigid-footprint and
  swept-lane collision checks; the fixed opening at the right of the red car's
  row; completion by sliding the red car through that opening; visible current
  state; reset and self-paced deterministic play.
- Excluded: Challenges 2–40; expansion cards and their special vehicles; Rush
  Hour Junior, Deluxe, Shift, Safari and every digital implementation; hints
  beyond the printed reverse-side sequence; competitive timing, minimum-move
  evaluation, manufacturing tolerances, storage and presentation.
- Direct-play status: not conducted. The edition's official instruction sheet
  establishes setup, sliding, lane, lifting and exit rules. Photographs of both
  sides of Challenge 1 reproduce the complete starting arrangement and printed
  solution. A computational sliding-block definition, three independent
  hands-on descriptions and the manufacturer's current product description
  corroborate the 6 × 6 geometry, 2 × 1 / 3 × 1 rigid footprints, fixed axis,
  unobstructed movement and red-car escape.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `RUS-001` | The selected edition uses one challenge card to define a fixed traffic-grid start state | Confirmed | Corroborated | High | P1, P2, S1, S2 |
| `RUS-002` | Challenge 1 is reproducible as eight labelled vehicles on a 6 × 6 grid | Confirmed | Corroborated | High | P1, R1, R2 |
| `RUS-003` | Cars occupy two collinear cells and trucks occupy three | Confirmed | Corroborated | High | P1, S1, S2, S3 |
| `RUS-004` | Every vehicle preserves its horizontal or vertical orientation and moves only forward or backward along that axis | Confirmed | Corroborated | High | P1, S1-S4 |
| `RUS-005` | A move may span several empty cells but may not pass through or finish on another vehicle | Confirmed | Corroborated | High | P1, S1-S4 |
| `RUS-006` | Vehicles stay on the grid except for the completing red-car escape through the fixed right opening | Confirmed | Corroborated | High | P1, P2, S1-S4 |
| `RUS-007` | The complete current arrangement and all empty cells are visible before each move | Observation | Corroborated | High | P1, R1, R2, S1-S3 |
| `RUS-008` | Challenge 1 has a printed eight-move solution ending with the red car moving right through the exit | Confirmed | Direct | High | R2 |
| `RUS-009` | No random event or time-driven state change occurs between physical slides | Observation | Corroborated | High | P1, S1-S4 |
| `RUS-010` | Reset discards the current arrangement and reconstructs the card state | Confirmed | Direct | High | P1 |
| `RUS-011` | Other card sets and variants add instance supply or rules outside this fixed-card boundary | Confirmed | Corroborated | High | P2, S3, S4 |

## Basic data

- Release / origin: Rush Hour derives from Nob Yoshigahara's Tokyo Parking
  puzzle, brought to Binary Arts in 1995 and released by the company later
  known as ThinkFun. This analysis uses the copyright-2010 standard card set.
- Platform or physical form: single-player physical sliding-block puzzle with
  moulded vehicles, a 6 × 6 tray and two-sided challenge cards.
- Puzzle family: axis-locked rigid-block escape planning.
- Primary and edition sources:
  - **[P1]** [ThinkFun `#5000` instruction sheet](https://legacy.thinkfun.com/wp-content/uploads/2015/09/RushH-5000-IN02.pdf),
    for card-defined setup, the red-car exit objective, forward/backward lane
    slides, no sideways motion, no lifting, reset and reverse-side solutions.
  - **[P2]** [ThinkFun / Ravensburger standard product page](https://www.thinkfun.co.uk/en-GB/products/logic-games/rush-hour-76436),
    for the 40-card standard product, four difficulty bands, blocking vehicles,
    grid confinement and complete sequences on card backs.
- Reproducible Challenge 1 evidence:
  - **[R1]** [Photograph of the 2010 Beginner Challenge 1 front](https://i.ebayimg.com/images/g/a0sAAOSw-o9kJEll/s-l400.jpg),
    for the exact labelled start arrangement.
  - **[R2]** [Photograph of Challenge 1's solution side](https://storage.googleapis.com/ludopedia-imagens-jogo/a4db9_13136.jpg),
    for the same arrangement and the printed sequence `C←3, O↓3, A→1,
    P↑1, B↑1, R←2, Q↓2, X→4/out`.
- Independent and technical corroboration:
  - **[S1]** [Spaans, *Improving sliding-block puzzle solving using meta-level reasoning*](https://www.pvv.org/~spaans/master-cs.pdf),
    section 3.1.2, for the 6 × 6 board, 2 × 1 / 3 × 1 slider blocks,
    orientation-preserving axial movement and one specific block exiting.
  - **[S2]** [UltraBoardGames rules transcription](https://www.ultraboardgames.com/rush-hour/game-rules.php),
    for components, card setup, forward/backward-only slides, no lifting, reset
    and the solution sequence on each card back.
  - **[S3]** [Zatu hands-on review](https://zatu.com/blogs/reviews/rush-hour-review),
    for the 6 × 6 lattice, 12 length-two cars, four length-three trucks,
    empty-space slides and permanent row / column identity.
  - **[S4]** [GeekDad hands-on rules description](https://geekdad.com/2017/06/thinkfun-puzzles/),
    for card reconstruction, 6 × 6 play, back-and-forth row / column motion,
    no turns or sideways movement, and fixed-gap escape.
- Claim IDs: `RUS-001`–`RUS-011`.

## Mechanical decomposition

### Action Genes

- `ACT-014` — relocate selected controlled board piece. The player selects one
  car or truck and directly chooses a reachable position on its invariant row
  or column; no automatic vehicle then moves.
- A multi-cell slide of any positive unobstructed distance is one move in the
  printed solution notation. Distance, vehicle length and fixed axis are action
  parameters, while footprint validity and obstruction are constraints.
- Claim IDs: `RUS-004`, `RUS-005`, `RUS-008`.

### System Behaviour Genes

- None. Releasing a legal physical slide leaves exactly that arrangement. The
  next vehicle, distance and direction all require another player choice.
- Collision rejection is legality, not an automatic resolution step; reset is
  an attempt-level restoration control rather than ordinary system evolution.
- Claim IDs: `RUS-005`, `RUS-009`, `RUS-010`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. Challenge 1 preserves 36 individually
  addressable cells and one declared boundary opening.
- `CON-007` — collision-valid active transformation. Every intermediate and
  final footprint of the selected length-two or length-three vehicle must fit
  the board and avoid every other current vehicle, except that the red car may
  cross the designated exit after its lane is clear.
- `CON-024` — piece-class movement and line obstruction. Each vehicle's start
  orientation permanently chooses one horizontal or vertical movement line;
  it cannot rotate, move sideways or pass through intervening occupancy.
- Vehicle colours and the car/truck theme identify pieces and lengths but do
  not create mechanics beyond these operational constraints.
- Claim IDs: `RUS-002`–`RUS-006`.

### Information Genes

- `INF-001` — fully visible current state. All vehicle footprints, orientations,
  occupied cells, empty cells, grid boundaries and the exit are inspectable
  before the next slide.
- The reverse-side sequence is excluded from ordinary solve-state information:
  consulting it reveals an answer, not an in-state clue.
- Claim IDs: `RUS-001`, `RUS-002`, `RUS-007`, `RUS-008`.

### Objective Genes

- `OBJ-039` — extract designated sliding block through fixed boundary gap. The
  challenge completes only when the red length-two car leaves through the one
  opening on its invariant row after blockers have been displaced.
- This is not `OBJ-022`: the red car is a remotely selected board piece, not a
  continuously navigated avatar or actor set. It is not target reconstruction,
  because the final positions of every blocking vehicle are unconstrained.
- Claim IDs: `RUS-006`, `RUS-008`.

### Time Genes

- `TIM-002` — self-paced sequential action. The physical state remains fixed
  for any pause between slides and no clock advances the traffic.
- Informal solve timing and counting alternative step granularity are excluded
  external evaluations.
- Claim IDs: `RUS-005`, `RUS-009`.

## Reproducible transitions

Challenge 1 coordinates use rows top-to-bottom and columns left-to-right:
`A r1c1-c2`, `O c6r1-r3`, `P c1r2-r4`, `X r3c2-c3`,
`Q c4r2-r4`, `C r4c5-c6`, `B c1r5-r6`, `R r6c3-c5`.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Challenge 1 is reconstructed from the card | Try to rotate `Q` or move it horizontally | The move is illegal and the arrangement remains unchanged | Orientation and movement axis persist | `RUS-004` |
| `C` occupies row 4 columns 5–6 | Slide `C` left three cells | `C` ends at row 4 columns 2–3 and frees column 6 below `O` | One selected rigid footprint may traverse several empty cells | `RUS-005`, `RUS-008` |
| `O` occupies column 6 rows 1–3 and `C` has moved | Slide `O` down three cells | `O` ends at column 6 rows 4–6 | Length-three truck translates intact on one axis | `RUS-003`–`RUS-005` |
| `A` occupies row 1 columns 1–2 | Slide `A` right one cell | `A` ends at columns 2–3 and frees the top of `P`'s column | Slides reveal spaces used by later dependencies | `RUS-005`, `RUS-008` |
| `P` occupies column 1 rows 2–4 | Slide `P` up one cell | `P` ends at rows 1–3 and frees row 4 column 1 | Full-footprint boundary and occupancy check | `RUS-004`, `RUS-005` |
| `B` occupies column 1 rows 5–6 | Slide `B` up one cell | `B` ends at rows 4–5 and frees row 6 column 1 | Reversible temporary displacement | `RUS-005`, `RUS-008` |
| `R` occupies row 6 columns 3–5 | Slide `R` left two cells | `R` ends at columns 1–3 and frees column 4 at row 6 | A truck preserves its three-cell footprint | `RUS-003`, `RUS-005` |
| `Q` occupies column 4 rows 2–4 | Slide `Q` down two cells | `Q` ends at rows 4–6 and clears red-car row 3 column 4 | Ordered blocker dependency opens the exit lane | `RUS-004`, `RUS-008` |
| Red `X` occupies row 3 columns 2–3 and row 3 columns 4–6 are clear | Slide `X` right through the opening | `X` crosses the right boundary and the challenge completes | Designated-block boundary extraction | `RUS-006`, `RUS-008` |

## Strategic and experiential structure

- Local decision: identify which vehicle currently has empty cells on its
  fixed axis and whether moving it creates or consumes space needed elsewhere.
- Medium-term planning: trace a dependency chain backwards from the red car's
  row. Clearing `Q` requires space below it; producing that space requires
  moving `R`, which in turn requires moving `B`, `P`, `A`, `O` and `C` in order.
- Long-term structure: redistribute a small number of empty cells across fixed
  row/column subspaces until every blocker intersecting the exit row can leave.
- Common heuristics: inspect the red-car corridor first; follow each blocking
  vehicle's axis to its next required vacancies; distinguish a move that only
  moves a blocker from one that creates useful cross-axis space; avoid restoring
  a previously cleared dependency too early.
- Failure attribution: there is no randomness. A dead end follows from a prior
  displacement consuming a required vacancy or from overlooking a vehicle's
  immutable row / column.
- Player-trust factors: the complete state is tactile and visible, every legal
  slide has a direct physical result, and reset exactly reconstructs the card.
- Claim IDs: `RUS-004`–`RUS-010`.

## Replay and variation

- What changes between scoped attempts: nothing unless the player deliberately
  chooses another legal sequence or resets Challenge 1.
- Randomness or procedural generation: none in setup, action or resolution.
- Multiple viable strategies: individual distances can sometimes be split
  into smaller slides, but the reverse-side sequence provides one reproducible
  eight-move solution rather than proving a unique path or unique optimum.
- Typical replay motive: recover from an unproductive displacement, solve
  without the printed answer or minimise moves under an external convention.
- Challenges 2–40 vary vehicle membership, orientation and arrangement but are
  excluded rather than silently used as evidence for this genome.
- Claim IDs: `RUS-001`, `RUS-008`–`RUS-011`.

## Adjacent systems and history

- The 15-puzzle also translates rigid blocks into vacancies, but every tile is
  one cell and can change rows and columns; Rush Hour pieces retain an axis and
  multi-cell footprint.
- Sokoban also plans around obstruction, but a navigated keeper pushes an
  adjacent crate one cell and cannot pull it. Rush Hour directly selects any
  vehicle and slides it in either axial direction without a pusher.
- Chess shares selected-piece relocation and line obstruction, but adds sides,
  capture, attack legality and alternating opposition. Rush Hour instead uses
  rigid footprints and one designated boundary escape.
- Tetris validates a moving multi-cell footprint against occupancy, but an
  automatically falling active element can rotate and later locks; Rush Hour
  keeps every placed vehicle persistent, selectable and permanently axis-locked.
- Freeways uses a car theme but builds a road graph and evaluates autonomous
  traffic; no vehicle is directly slid through a grid exit.
- ThinkFun's history traces the product to Yoshigahara's Tokyo Parking, but
  inventor history does not by itself establish a separate gene.
- Claim IDs: `RUS-003`–`RUS-009`, `RUS-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-014` | selected vehicle, signed axial distance |
| System Behaviour | none | none |
| Constraint | `CON-001`, `CON-007`, `CON-024` | `6 × 6`, footprint length `2/3`, invariant axis, swept occupancy, exit exception |
| Information | `INF-001` | simultaneous physical visibility |
| Objective | `OBJ-039` | red vehicle, right boundary gap, complete exit |
| Time | `TIM-002` | physical slide granularity, unrestricted pause |

Canonical signature:

`ACT-014; none; CON-001,CON-007,CON-024; INF-001; OBJ-039; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `62` (`GAME-0001`–`GAME-0062`).
- Exact genome matches: none.
- Tied near matches: `GAME-0011` — Chess (`5 / 15 = 0.333333`).
- Supported combination subsets: `COMB-0063`.
- Scan date: 2026-08-13.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0011` — Chess | `ACT-014`, `CON-001`, `CON-024`, `INF-001`, `TIM-002` | Chess alternates owned single-cell pieces under capture, check and class-specific geometry; Rush Hour controls all rigid vehicles and requires one boundary extraction | Near, `0.333333` |

### Preserved research notes

- New genes: `OBJ-039`.
- Generalised genes: `ACT-014` gains a non-capturing physical slider support;
  `CON-007` now explicitly covers selected as well as automatically active
  multi-cell elements; `CON-024` gains invariant-axis rigid sliders;
  `CON-001`, `INF-001` and `TIM-002` gain corroborating support.
- Classification result: one new objective gene and one new combination of
  known action / constraint / information / time genes.
- Evidence and reasoning: axial geometry and full-footprint obstruction are
  already independently operational in the vocabulary. Designated block
  extraction cannot be reduced to actor evacuation or target reconstruction.

## Taxonomy impact

- Registry changes: add `OBJ-039`; generalise the wording and evidence of
  `ACT-014`, `CON-007` and `CON-024` without changing prior signatures.
- Taxonomy-change record: none. Chess and Tetris remain valid narrower
  parameter cases; their action or collision semantics are not merged.
- Candidate terms affected: sliding block, invariant movement axis, swept
  rigid footprint and designated-block boundary extraction.
- Claim IDs: `RUS-003`–`RUS-008`.

## Negative results

- `ACT-001` rejected: one selected vehicle moves; no direction command applies
  globally to every movable element.
- `ACT-008` rejected: there is no permanently controlled avatar taking local
  navigation steps.
- `ACT-009` and `CON-012` rejected: no agent pushes an adjacent vehicle, and
  vehicles may move in both axial directions.
- `CON-005` rejected: the completing red-car exit is terminal, so not every
  legal primitive action has an in-attempt inverse.
- `CON-011` rejected as redundant here: `CON-007` validates the complete moving
  footprint and `CON-024` validates its swept line against occupancy; there are
  no internal static barrier cells beyond the board boundary.
- `OBJ-004` rejected: blocking vehicles have no prescribed final arrangement.
- `OBJ-022` rejected: the target is a directly selected sliding board block,
  not a navigated actor or avatar set.
- Printed move numbers and reverse-side answer lookup do not create an authored
  optimal-count objective or a concealed-state information gene in this scope.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Standard Beginner Challenge 1 is a fully
  reproducible 6 × 6 axis-locked sliding-block instance with an eight-move
  printed escape sequence (`RUS-001`–`RUS-010`).

## Нові гени

- [Observation | Corroborated | High] `OBJ-039` — extract designated sliding
  block through fixed boundary gap.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0063` — axis-locked rigid-block
  clearance for designated boundary extraction.

## Зміни таксономії

- [Observation | Corroborated | High] `ACT-014`, `CON-007` and `CON-024` now
  explicitly cover non-capturing selected sliders, persistent multi-cell
  footprints and invariant-axis movement without altering earlier signatures.

## Нові питання

- Do any standard later cards introduce a mechanically relevant distinction
  between move-count and cell-step solution conventions?
- Does an expansion's special vehicle require a different footprint or motion
  constraint rather than only a new instance parameter?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] SET, bounded to the official Basic SET
  solitaire procedure with one visible 12-card field.
- Optimisation criterion: move from spatial reachability to visual relational
  classification while retaining a finite, fully visible, self-paced state.
- Expected information gain: test whether the vocabulary can express an
  exactly-three selection whose four attributes must each be all equal or all
  different, without confusing that predicate with ordinary matching.
- Backlog impact: retain Rush Hour Challenges 2–40 and expansions as optional
  instance / variant audits rather than blending them into Challenge 1.

## Чому саме вона

- [Hypothesis | Corroborated | High] SET has mechanically distant primary
  rules, a reproducible solo boundary and a crisp multi-attribute predicate,
  making it a high-information ninth unit for the current Goal.
