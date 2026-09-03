---
game_id: GAME-0057
slug: golf-peaks
game_title: Golf Peaks
analysis_status: reviewed
reviewed: 2026-08-13
combination_ids:
  - COMB-0057
gene_ids:
  action:
    - ACT-061
  system:
    - SYS-100
  constraint:
    - CON-001
    - CON-011
    - CON-103
  information:
    - INF-001
  objective:
    - OBJ-014
  time:
    - TIM-001
---

# Game: Golf Peaks

## Analysis scope

- Version / ruleset: Afterburn's current released base game, restricted to the
  nine ordinary holes of World 1 that form its required half-course.
- Included: one golf ball and one fixed hole; authored isometric grid terrain;
  flat cells, height bands, slopes and blocking edges; a finite visible hand of
  one-use roll cards with exact distances; selecting one held card and one of
  four directions; deterministic stepwise travel, slope redirection and exact
  hole entry; one-step undo and full restart.
- Excluded: World 1's three bonus short-course holes; airborne, compound and
  later card modules; sand, water, pits, springs, mud, portals, conveyors and
  ice from later worlds; optional completion, achievements, speedrunning,
  soundtrack and presentation.
- Direct-play status: not conducted. The developer storefront fixes the
  card-plus-direction grammar and nine-hole ordinary course. A creator-assisted
  solver report isolates World 1's flat ground, walls and slopes; four hands-on
  reviews independently corroborate exact distances, one-use card order, hole
  completion and undo / restart.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `GPK-001` | Each location has nine required ordinary holes and three optional bonus holes | Confirmed | Direct | High | P1 |
| `GPK-002` | Every scoped hole begins with one fixed board, ball, hole and visible finite card selection | Confirmed | Corroborated | High | P1, S1-S4 |
| `GPK-003` | A move selects one held card and one cardinal direction, then consumes that card | Confirmed | Corroborated | High | P1, S1-S4 |
| `GPK-004` | A World 1 card declares an exact ground-roll distance rather than free shot strength | Confirmed | Corroborated | High | S1-S4 |
| `GPK-005` | The complete selected movement resolves before another card can be played | Confirmed | Corroborated | High | S1-S4 |
| `GPK-006` | World 1 slopes and walls can redirect or reject the ball's staged travel | Confirmed | Corroborated | High | S1, S2, S4 |
| `GPK-007` | A hole completes only when the ball enters the fixed hole, not when it passes beside or beyond it | Confirmed | Corroborated | High | P1, S1-S4 |
| `GPK-008` | Card order and chosen direction jointly determine whether the finite hand reaches the hole | Confirmed | Corroborated | High | P1, S1-S4 |
| `GPK-009` | Board geometry, ball, hole, card identities and remaining cards are visible before each move | Observation | Corroborated | High | P1, S1-S4 |
| `GPK-010` | Undo restores the consumed card and prior ball position; restart restores the authored level | Confirmed | Corroborated | High | S1, S3, S4 |

## Basic data

- Release / origin: Polish studio Afterburn released Golf Peaks for iOS on 12
  November 2018 and for Windows and macOS on 13 November 2018.
- Platform or physical form: deterministic single-player digital card-command
  spatial puzzle on an isometric heightfield.
- Puzzle family: finite card-sequenced ball routing.
- Primary source:
  - **[P1]** [Official Afterburn page](https://afterburn.itch.io/golf-peaks),
    documenting card selection, directional launch, handcrafted levels,
    textless tutorial and the nine-hole plus three-bonus-hole location format.
- Reproducible and hands-on corroboration:
  - **[S1]** Nicholas Whittaker,
    [Building a Solver for Golf Peaks](https://nicholas.cloud/blog/building-a-solver-for-golf-peaks/), for the completed World 1 boundary, flat levels, walls, slopes, card order and deterministic state search.
  - **[S2]** [Play Critically review](https://playcritically.com/2024/03/30/golf-peaks-review/), for exact card distances, directional choice, slope continuation, precise hole entry and recovery.
  - **[S3]** [Pixel Poppers review](https://pixelpoppers.com/review/golf-peaks/), for one-use cards, visible finite selection, cardinal targeting, no time limit and unlimited undo.
  - **[S4]** [AppUnwrapper review](https://www.appunwrapper.com/2018/11/12/golf-peaks-review/), for card selection, direction, elevation interaction, slope rollback and undo.
- Claim IDs: `GPK-001`-`GPK-010`.

## Mechanical decomposition

### Action Genes

- `ACT-061` - play held spatial action card. The player selects one visible
  roll card and one of four directions; the card is consumed to issue its exact
  movement transition to the ball.
- The gene is generalised from a tactical entity or cell target to a legal
  spatial target parameter that may be a direction. Its bounded card-mediated
  control remains unchanged.
- `ACT-008` is absent: the player does not step an avatar to an adjacent cell
  through an always-available navigation command.
- Claim IDs: `GPK-003`, `GPK-004`.

### System Behaviour Genes

- `SYS-100` - card-parametrised staged ball traversal on a heightfield. After a
  card and direction are committed, the system advances the ball stepwise for
  the declared roll distance, applying fixed support, wall and slope geometry
  until it stops, leaves the course or enters the hole.
- No physics-integration gene is assigned: the scoped motion is grid-step and
  deterministic rather than continuously integrated force simulation.
- Resolution order: consume selected card; set cardinal travel direction;
  advance the declared ground steps; apply each encountered wall or slope
  transition; test boundary and hole contact; settle; accept the next input.
- Claim IDs: `GPK-004`-`GPK-007`.

### Constraint Genes

- `CON-001` - fixed occupancy capacity. Every hole has one finite authored
  grid, fixed heightfield, start and receiver.
- `CON-011` - exclusive occupancy with static barriers. The ball can occupy one
  supported cell while authored walls, missing support and incompatible height
  boundaries block or constrain travel.
- `CON-103` - finite non-renewing spatial-command hand. A hole supplies a
  visible multiset of one-use movement cards; each forward action removes
  exactly one chosen identity, and no card is drawn or replenished during the
  attempt outside undo.
- `CON-020` is absent because exhausting the last card is not itself the
  canonical success or explicit failure trigger; it is a resource state whose
  usefulness depends on whether the hole has already been reached.
- Scarce strategic resources: exact movement distances, compatible directions
  and card order.
- Claim IDs: `GPK-002`-`GPK-004`, `GPK-008`, `GPK-010`.

### Information Genes

- `INF-001` - fully visible current state. The course geometry, elevation,
  slopes, ball, hole and every remaining card are visible before selection.
- No preview gene is assigned: the final trajectory is inferred from fixed
  rules rather than displayed as an authoritative successor trace.
- Claim IDs: `GPK-002`, `GPK-009`.

### Objective Genes

- `OBJ-014` - deliver designated payload to fixed receiver. Complete the
  bounded level by using spatial commands and deterministic terrain response to
  make the one required ball enter its authored hole.
- Card-directed displacement is an Action/System distinction; the terminal
  predicate remains delivery of one designated payload to one fixed receiver.
- Claim IDs: `GPK-007`, `GPK-008`.

### Time Genes

- `TIM-001` - discrete turn with automatic resolution. One card-direction
  commitment resolves its complete roll, terrain response, stopping position
  and completion check before the next decision.
- Unlimited thinking time and ordinary undo are parameters, not separate time
  genes within this exclusive action-resolution boundary.
- Claim IDs: `GPK-005`, `GPK-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Ball is two flat cells from the hole; roll-2 is held | Play roll-2 toward the hole | Card leaves the hand; ball advances two cells and enters the hole | card identity and direction jointly command exact travel | `GPK-003`, `GPK-004`, `GPK-007` |
| Ball is two cells from the hole; roll-3 is held | Play roll-3 through the same line | Ball passes the target distance unless terrain changes the path | proximity alone does not satisfy the objective | `GPK-004`, `GPK-007` |
| Ball reaches a descending slope during a roll | Continue automatic resolution | Fixed slope geometry redirects or extends the staged route | heightfield participates in system response | `GPK-006` |
| A wall rejects the current direction | Commit that card-direction pair | Ball cannot complete the nominal straight displacement | cards do not override static geometry | `GPK-006` |
| Two distinct cards remain | Play either one in one legal direction | Only that selected card is removed; the other remains visible | finite hand is selectable, not a fixed queue | `GPK-003`, `GPK-008` |
| Previous play created an unhelpful position | Undo once | Ball and selected card return to their immediately prior states | recovery restores both spatial and resource state | `GPK-010` |

## Strategic and experiential structure

- Local decision: choose the card-distance and direction whose fully resolved
  endpoint leaves a useful next shot.
- Medium-term planning: reserve exact distances for height transitions and the
  final hole approach, accounting for slope redirection.
- Long-term structure: permute the finite cards and directions into one route
  whose last required transition enters the hole precisely.
- Common heuristics: reason backward from the hole; match a remaining distance
  to each likely approach; use slopes to transform the nominal straight path;
  undo early when a necessary distance has been consumed.
- Failure attribution: the complete deterministic shot and restored card on
  undo make a wrong distance, direction or order identifiable.
- Player-trust factors: icon meaning, distance count, wall rejection, slope
  transition and hole-entry timing must remain stable.
- Claim IDs: `GPK-003`-`GPK-010`.

## Replay and variation

- World 1 uses nine fixed authored ordinary holes; setup and card multisets do
  not vary between attempts.
- No random draw, procedural board or concealed event affects scoped play.
- A hole may admit more than one ordering only when the fixed geometry and card
  multiset permit it; the Atlas makes no universal uniqueness claim.
- Replay comes from revising a failed sequence and optional later content, not
  from stochastic variation.
- Claim IDs: `GPK-001`, `GPK-002`, `GPK-008`, `GPK-010`.

## Adjacent systems and history

- Fights in Tight Spaces shares held spatial action-card play, but its cards
  target a tactical actor or cell, spend renewable momentum and feed a hostile
  phase. Golf Peaks has a non-renewing level hand and one ball receiver.
- Bonfire Peaks shares visible elevation-constrained spatial planning and
  discrete recovery, but continuously available avatar / carry commands do not
  encode movement in consumed cards.
- Balatro also commits visible held cards, yet it evaluates card subsets as
  poker patterns and refills from concealed order instead of executing a
  directional board trajectory.
- Can of Wormholes is the closest complete signature by formula because both
  are fixed, visible, discrete spatial puzzles; its articulated body and
  reversible endpoint control are mechanically different.
- Claim IDs: `GPK-002`-`GPK-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-061` | selected one-use roll card plus cardinal target |
| System Behaviour | `SYS-100` | exact staged roll under wall and slope geometry |
| Constraint | `CON-001`, `CON-011`, `CON-103` | fixed course and finite non-renewing card multiset |
| Information | `INF-001` | visible course, ball, hole and remaining cards |
| Objective | `OBJ-014` | put the designated ball into the fixed hole |
| Time | `TIM-001` | one card followed by complete deterministic resolution |

Canonical signature:

`ACT-061; SYS-100; CON-001,CON-011,CON-103; INF-001; OBJ-014; TIM-001`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `56` (`GAME-0001`–`GAME-0056`).
- Exact genome matches: none.
- Tied near matches: `GAME-0055` — Bonfire Peaks (`5 / 13 = 0.384615`).
- Supported combination subsets: `COMB-0057`.
- Scan date: 2026-08-13.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0055` - Bonfire Peaks | `CON-001`, `CON-011`, `INF-001`, `OBJ-014`, `TIM-001` | oriented avatar carrying under clearance versus card-parametrised ball traversal; both deliver one payload to a fixed receiver | Near, `0.384615` |

### Preserved research notes

- New genes originally included `SYS-100`, `CON-103`, `OBJ-036`;
  normalisation 004 later merged `OBJ-036` into `OBJ-014`.
- Classification result: `New gene` and `New combination of known and new
  genes`.
- Evidence and reasoning: no prior System record makes one held card declare a
  complete staged ball route over a heightfield; no Constraint record captures
  a selectable, strictly decreasing spatial-command multiset; and no Objective
  record isolates direct card-command delivery into a fixed hole.

## Taxonomy impact

- Registry changes originally added `SYS-100`, `CON-103` and `OBJ-036`;
  normalisation 004 later merged `OBJ-036` into `OBJ-014`. Generalise
  `ACT-061` to include a legal direction as a spatial target parameter.
- Taxonomy-change record: none. The action's card-mediated target-and-consume
  identity is preserved, and no earlier signature changes.
- Candidate terms affected: promote card-parametrised heightfield traversal,
  finite non-renewing spatial-command hand and directly commanded ball-to-hole
  completion.

## Negative results

- `ACT-008` rejected: no always-available one-cell avatar navigation.
- `CON-020` rejected: card exhaustion is a resource state, not the defined
  terminal budget predicate.
- The earlier `OBJ-014` rejection was superseded by normalisation 004: control
  method belongs to Action/System rather than the receiver objective.
- `none` as a separate negative-result record; these boundary decisions are
  local to this decomposition.
