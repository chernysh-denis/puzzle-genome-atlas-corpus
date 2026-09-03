---
game_id: GAME-0015
slug: threes
game_title: Threes
analysis_status: reviewed
reviewed: 2026-08-11
combination_ids:
  - COMB-0015
gene_ids:
  action:
    - ACT-001
  system:
    - SYS-002
    - SYS-003
    - SYS-004
    - SYS-023
  constraint:
    - CON-001
    - CON-002
    - CON-003
    - CON-038
  information:
    - INF-001
    - INF-010
  objective:
    - OBJ-002
    - OBJ-003
  time:
    - TIM-001
---

# Game: Threes

## Analysis scope

- Version / ruleset: the original core 4 × 4 endless Threes game released by
  Asher Vollmer, Greg Wohlwend and Jimmy Hinson in 2014.
- Included: four directional swipes; one-cell coupled movement; `1 + 2` and
  equal-ranked-card merging; valid-move insertion from an eligible trailing
  edge; next-card preview; rank-weighted score and no-move termination.
- Excluded: achievements, challenges, leaderboards, platform services,
  tutorial scripting, menu flow, character dialogue and animation, audio,
  later platform-specific presentation and all clone rules.
- Direct-play status: not conducted for this record. The developer history and
  official scoring FAQ are primary evidence; transition details are
  corroborated by contemporary and specialist rules accounts.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `THR-001` | One swipe chooses a global orthogonal direction and affects every card that can move | Confirmed | Corroborated | High | F2, F4 |
| `THR-002` | Each eligible card moves at most one grid cell per swipe rather than compressing maximally | Confirmed | Corroborated | High | F2, F4 |
| `THR-003` | Base cards 1 and 2 merge only with one another; cards from 3 upward merge only with an equal rank | Confirmed | Corroborated | High | F2, F4 |
| `THR-004` | A card produced by one collision cannot merge again during the same swipe | Confirmed | Corroborated | High | F4 |
| `THR-005` | A valid swipe inserts one successor at the trailing edge in a row or column that changed | Confirmed | Corroborated | High | F4 |
| `THR-006` | Successor identity and eligible insertion lane involve system selection rather than player choice | Confirmed | Corroborated | High | F2, F4 |
| `THR-007` | The Next display constrains the incoming card's category but can withhold the exact value of a higher card and its position | Confirmed | Corroborated | High | F2, F4, F5 |
| `THR-008` | A no-effect swipe is invalid and inserts no successor | Confirmed | Corroborated | High | F2, F4 |
| `THR-009` | Play ends when the filled board has no movement or compatible merge available | Confirmed | Corroborated | High | F2, F4 |
| `THR-010` | Score is the sum of rank-weighted card values, with rank `r` worth `3^r` | Confirmed | Direct | High | F3 |
| `THR-011` | Threes predates 1024 and 2048; its creators identify full-distance movement and unrestricted spawn location as changes made by those descendants | Confirmed | Direct | High | F2 |
| `THR-012` | Threes reuses the global command and compatible-merge structure of 2048 but falsifies maximal compression, equality-only compatibility and no-preview assumptions | Observation | Corroborated | High | THR-001–THR-011 |

## Basic data

- Release: 6 February 2014 on iOS; subsequent platforms are outside the
  mechanical scope.
- Creators: Asher Vollmer (design and programming), Greg Wohlwend (art) and
  Jimmy Hinson (music), presented as Sirvo.
- Puzzle family: stochastic single-player slide-and-merge survival scoring.
- Sources:
  - **[F1]** [Official playable Threes site](https://play.threesgame.com/threes/index.html),
    retained as the product reference.
  - **[F2]** Asher Vollmer and Greg Wohlwend,
    [The Rip-offs & Making Our Original Game](https://www.asherv.com/threes/threemails/),
    the creators' development record. It documents the valid-move spawn rule,
    hidden high-card preview, bag discussion and the full-distance / global-
    spawn changes in 1024 and 2048.
  - **[F3]** [Official Threes support FAQ](https://asherv.com/threes/support/),
    which defines rank scoring as powers of three.
  - **[F4]** [Gamezebo Threes walkthrough](https://www.gamezebo.com/walkthroughs/threes-walkthrough/),
    detailed swipe, collision, insertion, preview and terminal examples.
  - **[F5]** [Game Developer — Threes: Puzzle Elegance](https://www.gamedeveloper.com/game-platforms/threes-puzzle-elegance),
    corroborating one-cell movement, entry edge and the higher-card preview
    range.
  - **[F6]** Stefan Langerman and Yushi Uno,
    [Threes!, Fives, 1024!, and 2048 are Hard](https://arxiv.org/abs/1505.04274),
    a formal family comparison. Generalised complexity is not applied to the
    fixed 4 × 4 game.
- Claim IDs: `THR-001`–`THR-012`.

## Mechanical decomposition

### Action Genes

- `ACT-001` — global directional slide. The player supplies one of four
  directions; the command applies to every card that can legally shift or
  merge along its parallel row or column.
- The player does not select individual cards, collision pairs, successor
  identity or insertion cell.
- Claim IDs: `THR-001`, `THR-006`.

### System Behaviour Genes

- `SYS-023` — single-step coupled directional shift. Every eligible card moves
  at most one cell. This explicitly rejects 2048's `SYS-001` maximal
  compression.
- `SYS-002` — collision-triggered compatible merge. When the one-step shift
  brings a compatible leading pair together, the system replaces it with the
  next ranked card.
- `SYS-003` — element spawn after valid action. Exactly one successor enters
  after a state-changing swipe; no-effect input does not spawn.
- `SYS-004` — random outcome selection. The system selects the preview-bounded
  successor and one eligible changed line; the player does not choose either.
- Claim IDs: `THR-002`, `THR-003`, `THR-005`, `THR-006`, `THR-008`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. Sixteen persistent addressed cells
  bound the board.
- `CON-003` — single merge participation per resolution. A newly created card
  cannot immediately combine again in the same swipe.
- `CON-002` — declared pairwise merge compatibility. The Threes parameter
  relation admits `1 + 2` and equal ranked pairs from `3` upward.
- `CON-038` — opposite-edge moved-line spawn eligibility. The successor may
  enter only at the edge behind the movement and in a line that changed.
- Claim IDs: `THR-003`–`THR-005`, `THR-008`, `THR-009`.

### Information Genes

- `INF-001` — fully visible current state. Every current card, value and empty
  cell is inspectable before a swipe.
- `INF-010` — category-bounded next-element preview. The Next display provides
  useful guaranteed category information: base colours identify low cards,
  while a higher white / `+` preview may stand for more than one exact rank.
  The insertion lane also remains unresolved until the valid move completes.
- `INF-002` is absent because the next event is not wholly unpreviewed.
  `INF-005` is absent because the preview does not always disclose one exact
  successor identity.
- Claim IDs: `THR-006`, `THR-007`.

### Objective Genes

- `OBJ-002` — maximise accumulated score. The game evaluates the surviving
  board through the sum of rank scores; each rank above 3 is worth triple the
  preceding rank, not its printed face value.
- `OBJ-003` — preserve move availability. Continued scoring requires avoiding
  a board on which no direction can move or merge a card.
- `OBJ-001` is absent: the original endless mode presents no single declared
  target rank equivalent to 2048's named milestone.
- Claim IDs: `THR-009`, `THR-010`.

### Time Genes

- `TIM-001` — discrete turn with automatic resolution. One swipe is followed
  by the one-cell shift, collisions, scoring and successor insertion before
  the next command.
- There is no real-time state progression or independent opponent.
- Claim IDs: `THR-001`, `THR-005`, `THR-008`.

## Reproducible transitions

`·` is an empty cell. Rows below are considered under a left swipe before the
random successor enters.

| Before | Deterministic shift / merge result | What it establishes | Claim ID |
|---|---|---|---|
| `· 3 · ·` | `3 · · ·` | A card advances one cell, not necessarily to a distant boundary in one command | `THR-002` |
| `· · 1 2` under a right swipe | `· · · 3` | Unequal complementary bases merge | `THR-003` |
| `· · 3 3` under a right swipe | `· · · 6` | Equal ranked cards merge | `THR-003` |
| `· · 1 1` under a right swipe | `· · 1 1` | Equal base cards do not merge | `THR-003` |
| `3 3 3 3` | `6 3 3 ·` | One-cell order differs from 2048's maximal two-pair compression | `THR-002`, `THR-004` |
| A left swipe changes only rows 1 and 3 | Resolve the move | New card enters from the right edge of row 1 or 3, not an arbitrary empty cell | `THR-005`, `THR-006` |
| Every card is blocked and no adjacent compatible pair exists | Swipe any direction | No state change, no insertion; game is terminal | `THR-008`, `THR-009` |

## Strategic and experiential structure

- Local decision: compare which adjacent compatible pairs will collide after
  exactly one step and which lines become eligible for the previewed card.
- Medium-term planning: keep 1 and 2 cards mutually accessible, build equal
  ranked pairs, and use the constrained entry edge to place rather than merely
  tolerate low cards.
- Long-term structure: retain an ordered rank gradient and empty cells while
  preventing isolated base cards from filling critical lanes.
- Scarce resource: empty space remains important, but unlike 2048 the player
  also manages entry-lane eligibility. A swipe controls a probability support,
  not just the post-merge board.
- Failure attribution: the preview reduces successor-value surprise, while
  unresolved lane and high-card identity preserve stochastic risk.
- Claim IDs: `THR-002`–`THR-010`.

## Replay and variation

- What changes: starting arrangement, successor sequence, eligible-lane choice
  and resulting merge order.
- What remains stable: one-cell movement, asymmetric base compatibility,
  ranked equality, trailing-edge insertion and rank scoring.
- Randomness: the creator log describes a bag-like system used to limit
  destructive runs of identical bases. The exact production distribution is a
  parameter and is not needed for the `SYS-004` boundary.
- Typical replay motive: improve highest card and total score through better
  control of rank order, base pairing and entry lanes.
- Claim IDs: `THR-006`, `THR-007`, `THR-010`.

## Adjacent systems and history

- The creators identify 1024 as the first released descendant and 2048 as a
  subsequent derivative of that full-distance system.
- 2048 preserves the global direction, automatic collision merge and random
  successor pressure but changes movement to maximal compression, compatibility
  to universal equality, insertion to any empty cell and preview to none.
- The difference is therefore not one parameter or theme: three constraints
  and information boundaries change the set of controllable future states.
- Complexity results for generalised Threes and 2048 support formal family
  comparison but do not establish difficulty of one fixed 4 × 4 session.
- Claim IDs: `THR-011`, `THR-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-001` | four orthogonal directions |
| System Behaviour | `SYS-002`, `SYS-003`, `SYS-004`, `SYS-023` | bag distribution and resolution order |
| Constraint | `CON-001`, `CON-002`, `CON-003`, `CON-038` | 4 × 4 size and eligible lanes |
| Information | `INF-001`, `INF-010` | high-card category range |
| Objective | `OBJ-002`, `OBJ-003` | rank score and highest-card records |
| Time | `TIM-001` | animation does not advance state independently |

Canonical signature:

`ACT-001; SYS-002,SYS-003,SYS-004,SYS-023; CON-001,CON-002,CON-003,CON-038; INF-001,INF-010; OBJ-002,OBJ-003; TIM-001`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `14` (`GAME-0001`–`GAME-0014`).
- Exact genome matches: none.
- Tied near matches: `GAME-0001` — 2048 (`11 / 17 = 0.647059`).
- Supported combination subsets: `COMB-0015`.
- Scan date: 2026-08-11.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0001`.

### Preserved research notes

- Result: no exact signature or existing combination match. The close score is
  a successful reuse test, not a novelty claim.

## Combination record

- Registered [`COMB-0015`](../../combinations/COMB-0015.md), a proper
  nine-gene subset centred on one-step global movement, pairwise merging and
  preview-bounded constrained insertion.
- `COMB-0001` remains supported only by 2048 because its maximal compression,
  equality constraint and unpreviewed event are not present here.

## Taxonomy impact

- Ten existing genes gain a second or later use and four bounded genes are
  added without changing the six-type taxonomy.
- The comparison sharpens definitions for maximal compression, merge
  compatibility, spawn eligibility and preview scope.

## Negative results

- `SYS-001`, `CON-002`, `INF-002`, `INF-005` and `OBJ-001` were explicitly
  tested and rejected for the scoped rules.
- The bag distribution and high-card candidate range remain parameters rather
  than separate genes; exact probabilities are unnecessary for the decisions
  distinguished here.
- Character faces, voices and animation do not mutate the decision state and
  remain outside the genome.
- No taxonomy change is required. The checkpoint's existing genes capture ten
  shared structures, while four new bounded genes encode the falsified
  assumptions rather than variants named only for Threes.

## Research notes

- Strongest finding: a high genome similarity can coexist with materially
  different control. One-cell movement and constrained entry make each swipe
  manage where randomness may occur, not merely the arrangement before a
  random board-wide spawn.
- Registry consequence: ten genes gain Threes evidence and four new genes are
  admitted. `SYS-002`, `SYS-003` and `SYS-004` now have stronger cross-family
  support without broadening their definitions.
- Next subject should return to mechanical distance while still targeting
  singleton System Behaviour or combination reuse.
