---
game_id: GAME-0044
slug: a-good-snowman-is-hard-to-build
game_title: A Good Snowman Is Hard to Build
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0044
gene_ids:
  action:
    - ACT-008
    - ACT-009
  system:
    - SYS-080
    - SYS-081
  constraint:
    - CON-001
    - CON-013
    - CON-092
  information:
    - INF-001
  objective:
    - OBJ-004
  time:
    - TIM-001
---

# Game: A Good Snowman Is Hard to Build

## Analysis scope

- Version / ruleset: the ordinary main-world rules of the original 2015 game,
  bounded to one authored garden puzzle with one monster, three initially
  separate snowballs, snow-covered and bare cells, and one completed snowman.
- Included: orthogonal monster movement; one-ball push; persistent snow removal;
  small-to-medium-to-large growth; maximum size; legal placement onto a larger
  top ball; top-ball knock-off; fixed walls; visible state; undo / restart as
  recovery controls; completion by one three-size stack at any legal location.
- Excluded: the dream-world rule variants, post-game and secrets, multiple-
  snowman levels, multiplayer / Remote Play, campaign routing, hugging, benches,
  achievements, narrative interpretation and move-count optimisation.
- Direct-play status: not conducted. The official press kit and storefront
  establish the product and Sokoban-style premise; a formal planning account
  gives exact growth, occupancy and goal transitions; a peer-reviewed
  complexity paper specifies push / stack legality; Thinky Games corroborates
  the main-world growth and three-ball assembly sequence.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `AGS-001` | The scoped puzzle is a fixed orthogonal maze with one monster and three visible snowballs | Confirmed | Corroborated | High | P1, P2, A1, A2 |
| `AGS-002` | The monster walks through free cells and pushes only one exposed snowball per command | Confirmed | Direct | High | A1, A2 |
| `AGS-003` | Moving a ball onto snow removes that snow and advances small to medium or medium to large | Confirmed | Direct | High | A1, S1 |
| `AGS-004` | A large ball remains large, so snow is a consumable opportunity rather than an unbounded value source | Confirmed | Corroborated | High | A1, S1 |
| `AGS-005` | A ball may enter a stack only when smaller than every ball below it | Confirmed | Direct | High | A1, A2 |
| `AGS-006` | Only a topmost ball is directly movable; an incomplete stack can have its top ball knocked to the far side when clear | Confirmed | Direct | High | A1, A2 |
| `AGS-007` | One large-medium-small stack forms the scoped snowman, and its ground location is not predesignated | Confirmed | Direct | High | A1, A2, S1 |
| `AGS-008` | Wrong growth, stack order or parking can leave moves available while making the snowman unreachable | Observation | Corroborated | High | A1, A2, S1 |
| `AGS-009` | Terrain, remaining snow, ball sizes / stacks and monster position are visible before each decision | Observation | Corroborated | High | P2, A1, S1 |
| `AGS-010` | One input resolves movement, snow consumption, growth, stacking / unstacking and completion before the next input | Observation | Corroborated | High | A1, A2 |
| `AGS-011` | Growth is unary terrain-triggered state change, not collision replacement of two equal objects | Observation | Corroborated | High | AGS-003, AGS-004 |
| `AGS-012` | The game shares a push-planning core with Sokoban while replacing fixed goals and exclusive cells with flexible ordered stacking | Observation | Corroborated | High | AGS-001–AGS-011 |

## Basic data

- Release / origin: Alan Hazelden and Benjamin Davis created the game; the
  official press kit records its 25 February release and original mobile and PC
  platforms. The scoped rules are those of the 2015 product.
- Platform or physical form: deterministic single-player digital grid puzzle.
- Puzzle family: terrain-transforming, size-ordered Sokoban-like assembly.
- Primary and platform sources:
  - **[P1]** [official press kit](https://agoodsnowman.com/press/index.php),
    identifying the creators, platforms and snowman-building premise.
  - **[P2]** [Nintendo's publisher-supplied listing](https://www.nintendo.com/us/store/products/a-good-snowman-is-hard-to-build-switch/),
    describing limited snow and space and Sokoban-style block pushing.
- Formal rules evidence:
  - **[A1]** Bofill et al.,
    [A Good Snowman is Hard to Plan](https://arxiv.org/abs/2310.01471),
    specifying the discrete grid, one-ball move, snow removal, bounded growth,
    stack preconditions and location-flexible goal.
  - **[A2]** He, Liu and Yang,
    [Snowman is PSPACE-complete](https://sokoban.cn/paper/snowman_is_pspace_complete.pdf),
    specifying one-ball pushes, smaller-on-larger stacks, top-ball knock-off and
    the completed decreasing-size stack. Its complexity conclusion is not used
    to rate this fixed level's human difficulty.
- Specialist corroboration:
  - **[S1]** [Thinky Games overview](https://thinkygames.com/games/a-good-snowman-is-hard-to-build/),
    describing small-to-medium-to-large growth on fresh snow and the required
    large / medium / small assembly order.
- Claim IDs: `AGS-001`–`AGS-012`.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. The monster moves one cardinal cell
  through free garden terrain to obtain the required side of a ball or stack.
- `ACT-009` — push adjacent movable object. Commanding the monster toward one
  exposed adjacent snowball moves that one ball one logical position; the
  destination may be empty or the top of a compatible stack.
- `ACT-018` is absent. The rules allow only one ball to be pushed; a stack is
  not translated as a contiguous movable chain.
- Undo and restart restore state but remain recovery interface controls.
- Claim IDs: `AGS-001`, `AGS-002`, `AGS-005`, `AGS-006`.

### System Behaviour Genes

- `SYS-080` — consumable-terrain bounded object growth. When a small or medium
  ball enters a snow-covered cell, the cell becomes bare and the ball advances
  exactly one step on the three-state size ladder; large is absorbing.
- `SYS-081` — push-resolved ordered stack transfer. A pushed exposed ball lands
  atop a compatible larger stack, or the top of an incomplete stack is knocked
  to the opposite free cell; object identity and size persist through transfer.
- `SYS-002` is absent: growth consumes a terrain state and changes one surviving
  ball; no equal pair collides and no two elements are replaced by one output.
- Resolution order: validate monster access and exposed ball; validate empty or
  compatible target; move the ball; consume target snow and apply at most one
  size increase; update stack relation; test the three-size completion state.
- Claim IDs: `AGS-002`–`AGS-007`, `AGS-010`, `AGS-011`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The scoped garden retains one finite
  authored grid of walls and addressable ground cells while snow cover changes.
- `CON-013` — irrecoverable objective deadlock. A legal push may consume needed
  snow, overgrow the intended head or strand a ball / stack without terminating
  ordinary monster movement.
- `CON-092` — size-ordered top-access stack geometry. Only an exposed top ball
  may move; entry onto a stack requires it to be smaller than all balls below;
  a ball already on one stack cannot transfer directly to another stack.
- `CON-011` is absent: one ground cell may legally contain an ordered stack of
  several balls, so general entity occupancy is not exclusive.
- `CON-012` is absent: although ordinary pushes use rear access, the destination
  need not be free, and pushing a stack can eject its top ball across the
  monster rather than displacing the contacted base in the usual direction.
- Scarce strategic resources: unconsumed snow cells, approach sides, empty
  landing cells, ball-size assignments and retrievable stack locations.
- Claim IDs: `AGS-001`, `AGS-003`–`AGS-008`.

### Information Genes

- `INF-001` — fully visible current state. The monster, walls, snow / bare
  ground, each ball's size and every stack are inspectable before the next move.
- Future solvability is derived from visible deterministic state, not hidden or
  random content.
- Claim IDs: `AGS-008`, `AGS-009`.

### Objective Genes

- `OBJ-004` — reconstruct specified configuration. The existing three balls
  must become one ordered large-base, medium-middle, small-top configuration.
  Its target-equivalence parameter is generalised to permit any legal ground
  location rather than marked goal cells.
- This is not a new scalar-growth objective: growth prepares typed components,
  while completion is evaluated only from their final stack relation.
- Claim IDs: `AGS-005`, `AGS-007`, `AGS-012`.

### Time Genes

- `TIM-001` — discrete turn with automatic resolution. Each movement input
  completes any push, snow depletion, growth, stack transition and completion
  check before another command is accepted.
- `TIM-002` is absent under the registry's exclusive boundary: decisions are
  untimed, but a valid push has decision-relevant automatic terrain, size and
  stack resolution.
- Claim IDs: `AGS-003`, `AGS-005`–`AGS-007`, `AGS-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Monster faces an empty traversable cell | Move toward it | Monster advances one cell | direct grid navigation | `AGS-002` |
| Small ball faces snowy free ground | Push it onto snow | Ball moves, snow disappears and size becomes medium | terrain consumption causes unary growth | `AGS-003` |
| Medium ball faces snowy free ground | Push it onto snow | Ball moves, snow disappears and size becomes large | growth has a second bounded step | `AGS-003` |
| Large ball enters snow | Complete the push | Ball remains large while the destination snow is removed | maximum size is absorbing | `AGS-004` |
| Medium ball is pushed toward a large ball | Complete the push | Medium occupies the top relation over the large ball | strict compatible stacking | `AGS-005` |
| Large or equal ball is pushed toward a smaller / equal top ball | Attempt the push | Transition is rejected | stacking is ordered, not collision merging | `AGS-005`, `AGS-011` |
| Incomplete stack has a clear cell beyond the monster | Push into the stack | Its exposed top ball is knocked to the far free cell | unstacking moves one top ball | `AGS-006` |
| Large, medium and small occupy one decreasing stack | Complete the final push | The stack becomes a completed snowman | flexible-location assembly is the goal | `AGS-007` |

## Strategic and experiential structure

- Local decision: choose whether a ball should cross snow now and whether the
  destination is empty, a compatible stack or a recoverable parking cell.
- Medium-term planning: assign the three eventual sizes, reserve enough snow
  for each and preserve approach geometry for medium-on-large then small-on-top.
- Long-term structure: construct the decreasing stack at any location that is
  reachable from the available push sides, not at a premarked Sokoban goal.
- Common heuristics: count required growth steps; avoid rolling a future head
  over snow; build from the large base upward; preserve a clear knock-off lane.
- Failure attribution: visible deterministic transitions make the immediate
  growth or illegal stack clear, while the decisive mistake can be an earlier
  irreversible snow consumption or parking push.
- Player-trust factors: snow-removal timing, one-step growth, large-size cap,
  stack compatibility, exposed-ball choice, knock-off direction and undo must
  remain stable.
- Claim IDs: `AGS-003`–`AGS-010`.

## Replay and variation

- What changes between puzzles: walls, snow coverage, initial ball sizes and
  positions, required snowman count and available approach / parking space.
- Randomness or procedural generation: none in the scoped authored puzzle.
- Multiple viable strategies: the final snowman position is disjunctive, but
  limited snow and push access can narrow viable growth and assembly orders.
- Typical replay motive: undo an overgrowth or deadlock, try another final
  stack location, or reduce ball pushes.
- Claim IDs: `AGS-001`, `AGS-007`–`AGS-010`.

## Adjacent systems and history

- Sokoban is the closest mathematical neighbour through direct navigation,
  one-object pushing, fixed cells, visible state and non-terminal deadlock.
  Snowman replaces marked crate goals with consumed snow, mutable ball sizes
  and multi-occupant ordered stacks.
- Stephen's Sausage Roll also transforms a pushed object's state after contact,
  but tracks elongated-body orientation and exact-once surfaces. Snowman grows
  one ball from terrain state and assembles a location-flexible tower.
- 2048 also increases values, yet combines two compatible objects during a
  board-wide automatic compression. Snowman changes one pushed ball from snow
  contact and preserves all three ball identities for the objective.
- Patrick's Parabox shares navigation, one-object push and visible deadlock
  planning. Its stacks are recursive spatial containers and it supports chain
  pushing; Snowman's same-cell relation is a bounded size-ordered stack.
- Claim IDs: `AGS-002`–`AGS-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-009` | cardinal step; one exposed ball |
| System Behaviour | `SYS-080`, `SYS-081` | three sizes; snow consumption; ordered landing / knock-off |
| Constraint | `CON-001`, `CON-013`, `CON-092` | fixed ground cells; top access; strict size order |
| Information | `INF-001` | simultaneous visible garden state |
| Objective | `OBJ-004` | large-medium-small stack at any legal location |
| Time | `TIM-001` | one input followed by complete deterministic resolution |

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`:
  `ACT-008,ACT-009; SYS-080,SYS-081; CON-001,CON-013,CON-092; INF-001;
  OBJ-004; TIM-001`.
- Indexed games scanned: all 43 prior reviewed records, `GAME-0001`–`GAME-0043`.
- Indexed combinations scanned: `COMB-0001`–`COMB-0043`.
- Exact genome matches: none.
- Near matches and similarity scores: Sokoban is the unique maximum at
  `6 / 13 = 0.461538`; Stephen's Sausage Roll follows at
  `6 / 18 = 0.333333`; Patrick's Parabox shares `5 / 18 = 0.277778`; 2048
  shares `3 / 21 = 0.142857`.
- Supported combination subsets: new recurring `COMB-0044` only.
- Scan date: 2026-08-12.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0006` — Sokoban | `ACT-008`, `ACT-009`, `CON-001`, `CON-013`, `INF-001`, `OBJ-004` | Sokoban uses exclusive cells, strict free-ahead pushes, fixed goals and no automatic terrain / size / stack transition | Unique near match, `0.461538` |
| `GAME-0043` — Stephen's Sausage Roll | `ACT-008`, `ACT-009`, `CON-001`, `CON-013`, `INF-001`, `TIM-001` | elongated roll and exact-once cooking versus unary growth and ordered stack assembly | Second, `0.333333` |
| `GAME-0036` — Patrick's Parabox | `ACT-008`, `ACT-009`, `CON-013`, `INF-001`, `OBJ-004` | recursive containment / chains and self-paced transitions versus bounded vertical stack and automatic resolution | Controlled comparison, `0.294118` |
| `GAME-0001` — 2048 | `CON-001`, `TIM-001` and final-value preparation only conceptually | collision merge, random spawn and line compression do not match snow-driven unary growth | Non-near, `0.142857` |

The complete numeric scan is: `GAME-0001` `3 / 21 = 0.142857`;
`GAME-0002` `3 / 14 = 0.214286`; `GAME-0003` `2 / 17 = 0.117647`;
`GAME-0004` `2 / 23 = 0.086957`; `GAME-0005` `2 / 15 = 0.133333`;
`GAME-0006` `6 / 13 = 0.461538`; `GAME-0007` `2 / 16 = 0.125000`;
`GAME-0008` `2 / 15 = 0.133333`; `GAME-0009` `3 / 23 = 0.130435`;
`GAME-0010` `3 / 16 = 0.187500`; `GAME-0011` `2 / 21 = 0.095238`;
`GAME-0012` `2 / 17 = 0.117647`; `GAME-0013` `4 / 19 = 0.210526`;
`GAME-0014` `2 / 23 = 0.086957`; `GAME-0015` `3 / 21 = 0.142857`;
`GAME-0016` `2 / 23 = 0.086957`; `GAME-0017` `1 / 22 = 0.045455`;
`GAME-0018` `1 / 28 = 0.035714`; `GAME-0019` `5 / 15 = 0.333333`;
`GAME-0020` `2 / 22 = 0.090909`; `GAME-0021` `1 / 18 = 0.055556`;
`GAME-0022` `1 / 21 = 0.047619`; `GAME-0023` `0 / 20 = 0.000000`;
`GAME-0024` `1 / 21 = 0.047619`; `GAME-0025` `1 / 20 = 0.050000`;
`GAME-0026` `1 / 21 = 0.047619`; `GAME-0027` `2 / 20 = 0.100000`;
`GAME-0028` `2 / 25 = 0.080000`; `GAME-0029` `3 / 19 = 0.157895`;
`GAME-0030` `1 / 23 = 0.043478`; `GAME-0031` `1 / 20 = 0.050000`;
`GAME-0032` `2 / 19 = 0.105263`; `GAME-0033` `2 / 21 = 0.095238`;
`GAME-0034` `2 / 22 = 0.090909`; `GAME-0035` `2 / 26 = 0.076923`;
`GAME-0036` `5 / 17 = 0.294118`; `GAME-0037` `2 / 17 = 0.117647`;
`GAME-0038` `2 / 24 = 0.083333`; `GAME-0039` `2 / 17 = 0.117647`;
`GAME-0040` `2 / 16 = 0.125000`; `GAME-0041` `2 / 19 = 0.105263`;
`GAME-0042` `1 / 18 = 0.055556`; `GAME-0043` `6 / 18 = 0.333333`.

- New genes: `SYS-080`, `SYS-081`, `CON-092`.
- Classification result: `New gene` and a recurring combination of known genes.
- Evidence and reasoning: the formal transitions distinguish terrain-triggered
  bounded growth and strict top-access stacking from every earlier automatic
  merge, cooking, recursive-containment and exclusive-occupancy record.

## Combination record

- Registered recurring `COMB-0044` — visible direct-navigation push-deadlock
  planning, supported exhaustively by Sokoban, Patrick's Parabox, Stephen's
  Sausage Roll and A Good Snowman Is Hard to Build.
- The four-gene core excludes objectives, time models, fixed versus recursive
  topology and every game-specific object transformation.

## Taxonomy impact

- Registry changes: added `SYS-080`, `SYS-081` and `CON-092`; added Snowman
  evidence to six reused genes; generalised `OBJ-004`'s target-equivalence
  parameter to include flexible target location without changing prior genomes.
- Taxonomy-change record: none; no earlier classification or signature changes.
- Candidate terms affected: promoted consumable-terrain bounded growth,
  push-resolved ordered stack transfer and size-ordered top-access geometry.

## Negative results

- `ACT-018`, `SYS-002`, `CON-011`, `CON-012` and `TIM-002` are rejected by
  explicit one-ball, multi-ball-stack and automatic-resolution counterexamples.
- `COMB-0036` does not recur because it requires `CON-011` and `TIM-002`.
- No separate negative-result record is needed: no prior candidate or accepted
  distinction is overturned.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Snow is removed and advances only the pushed
  ball through a bounded size ladder (`AGS-003`, `AGS-004`).
- [Confirmed | Direct | High] A snowman is a decreasing three-size stack at
  any legal location, with movement restricted to exposed top balls
  (`AGS-005`–`AGS-007`).

## Нові гени

- [Observation | Corroborated | High] Added `SYS-080`, `SYS-081` and
  `CON-092`; reused seven existing genes.

## Нові комбінації

- [Observation | Corroborated | High] Registered recurring `COMB-0044` across
  four visible navigation / push / deadlock games.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає; `OBJ-004` gains
  a flexible-location parameter example without a signature change.

## Нові питання

- Does Snakebird's fruit-driven body growth reuse `SYS-080`, or does adding
  persistent body segments require a distinct conservation boundary?
- Does a 44-game checkpoint expose a stable push-system cluster that warrants
  further normalisation without erasing transformation differences?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] `CHECKPOINT_044` before another game.
- Optimisation criterion: audit the four post-checkpoint additions and verify
  whether targeted reuse has reduced singleton density.
- Expected information gain: recheck the new image, factory, surface and
  snowman boundaries plus all recurring combination supporters.
- Backlog impact: retain Snakebird and Hexcells Infinite until the checkpoint.

## Чому саме вона

- [Hypothesis | Corroborated | High] Four games have been added since
  checkpoint 040; an audit now preserves the established four-game cadence and
  tests the new recurring push core before selecting another growth subject.

## Sources consulted

- Official A Good Snowman press kit and Nintendo publisher listing.
- Bofill et al.'s formal planning model and He, Liu and Yang's peer-reviewed
  rules / complexity account.
- Thinky Games' main-world mechanical overview.
