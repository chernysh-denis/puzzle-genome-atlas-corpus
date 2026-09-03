---
game_id: GAME-0006
slug: sokoban
game_title: Sokoban
analysis_status: reviewed
reviewed: 2026-08-11
combination_ids:
  - COMB-0006
  - COMB-0036
  - COMB-0044
gene_ids:
  action:
    - ACT-008
    - ACT-009
  system: []
  constraint:
    - CON-001
    - CON-011
    - CON-012
    - CON-013
  information:
    - INF-001
  objective:
    - OBJ-004
  time:
    - TIM-002
---

# Game: Sokoban

## Analysis scope

- Version / ruleset: classic single-level Sokoban on a fixed orthogonal grid,
  following the official core rules: move the keeper through floor cells and
  push every crate onto a designated storage goal.
- Included: one-cell orthogonal walking, pushing one adjacent crate into one
  free cell, static walls, exclusive occupancy, push-only manipulation, visible
  goals and completion when every crate occupies a goal.
- Excluded: undo, restart and move counters as interface controls; pulling,
  multi-crate pushes, ice, teleporters, switches, multiple keepers, automatic
  movement, timers, hints and procedural level generation.
- Direct-play status: not conducted. Rules were triangulated from the official
  Sokoban site, the University of Alberta rules page and peer-reviewed motion-
  planning and search literature. No particular commercial level set is used
  to claim a universal difficulty.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SOK-001` | The keeper moves orthogonally through free floor and may push one adjacent crate into a free cell beyond it | Confirmed | Corroborated | High | P1, P2, A1, A2 |
| `SOK-002` | Crates cannot be pulled and two or more crates cannot be pushed together | Confirmed | Corroborated | High | P1, P2, A1, A2 |
| `SOK-003` | Success requires every crate to occupy a designated storage goal | Confirmed | Corroborated | High | P1, P2, A1 |
| `SOK-004` | A legal push can make the completion objective unreachable without terminating play or eliminating all legal movement | Confirmed | Corroborated | High | P2, A1, A3 |
| `SOK-005` | Walking and crate pushing have different state effects and decision consequences | Observation | Corroborated | High | SOK-001–SOK-004 |
| `SOK-006` | Player access behind crates, crate-goal ordering and deadlock avoidance are central planning structures | Pattern | Corroborated | Medium | A1, A3, A4 |
| `SOK-007` | The complete current level state is visible and deterministic, with no in-play random event | Confirmed | Corroborated | High | P1, P2, A1 |
| `SOK-008` | The six-type model represents indirect pushing and objective deadlock without a taxonomy change | Observation | Corroborated | Medium | SOK-001–SOK-007 |
| `SOK-009` | The official history records December 1982 Thinking Rabbit releases for PC-8801, FM-7 and PC-8001mk2 and credits Hiroyuki Imabayashi | Confirmed | Direct | High | P3 |
| `SOK-010` | Complexity results for generalised Sokoban do not establish the difficulty of every finite published level | Confirmed | Corroborated | High | A2, A4 |

## Basic data

- Release / origin: the official history lists the first releases in December
  1982 by Thinking Rabbit and identifies Hiroyuki Imabayashi in the copyright.
- Platform or physical form: originally a computer grid puzzle; the analysed
  mechanics are platform-independent discrete motion rules.
- Puzzle family: deterministic push-block motion planning.
- Primary and official sources:
  - **[P1] Official rules:** Falcon / Thinking Rabbit,
    [“What is Sokoban?”](https://www.sokoban.jp/rule.html), stating that the
    keeper may push one crate, may not push two or more and may not pull.
  - **[P2] University of Alberta Games Group:**
    [“Rules of the Game”](https://webdocs.cs.ualberta.ca/~games/Sokoban/thegame.html),
    stating the all-boxes-on-goals objective and the possibility of unsolvable
    positions under push-only movement.
  - **[P3] Official history:** Falcon / Thinking Rabbit,
    [“History of Sokoban”](https://www.sokoban.jp/history.html), listing the
    December 1982 releases and subsequent platforms.
- Academic sources:
  - **[A1]** Andreas Junghanns and Jonathan Schaeffer,
    [“Single-Agent Search in the Presence of Deadlocks”](https://sokoban.dk/wp-content/uploads/2016/02/Junghanns-and-Schaeffer-Single-agent-search-in-the-presence-of-deadlocks.pdf),
    AAAI 1998, defining occupancy, push rules and reachable unsolvable states.
  - **[A2]** Dorit Dor and Uri Zwick,
    [“SOKOBAN and other motion planning problems”](https://www.ic.unicamp.br/~santiago/assets/mc558/2024%20-%202%20-%20projects/sokoban%20and%20other%20motion%20plannig%20problems.pdf),
    *Computational Geometry* 13, 1999, formalising the keeper, walls, packages,
    single pushes and no-pull rule.
  - **[A3]** Andreas Junghanns and Jonathan Schaeffer,
    [“Sokoban: Enhancing General Single-Agent Search Methods Using Domain Knowledge”](https://doi.org/10.1016/S0004-3702(01)00109-6),
    *Artificial Intelligence* 129, 2001.
  - **[A4]** Robert A. Hearn and Erik D. Demaine,
    [“PSPACE-Completeness of Sliding-Block Puzzles and Other Problems”](https://arxiv.org/abs/cs/0205005),
    *Theoretical Computer Science* 343, 2005, strengthening a generalised
    Sokoban complexity result.
- Claim IDs: `SOK-001`–`SOK-010`.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. One directional command moves the
  keeper into an adjacent unoccupied floor cell without changing crate
  positions.
- `ACT-009` — push adjacent movable object. When the commanded adjacent cell
  contains one crate and the cell beyond is free, the same directional input
  moves the crate forward and the keeper into its former cell.
- These are separate genes because walking changes only future keeper access,
  while a push changes the persistent crate configuration and may irreversibly
  remove every solution path.
- Undo and restart are interface recovery commands outside the scoped primitive
  action set.
- Claim IDs: `SOK-001`, `SOK-002`, `SOK-004`, `SOK-005`.

### System Behaviour Genes

- Existing gene IDs: none.
- Candidate genes: none.
- A legal push moves both keeper and crate as the commanded result; it is not an
  automatic collision response. Nothing moves after the input completes.
- Goal cells do not absorb, lock or remove crates. A crate on a goal remains an
  ordinary movable crate and may be pushed off again.
- Completion checking may be implemented digitally, but it does not introduce
  an intermediate state transition and is not treated as a System Behaviour.
- Claim IDs: `SOK-001`, `SOK-003`, `SOK-007`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. Each level has one finite unchanging
  floor-and-wall topology.
- `CON-011` — exclusive occupancy with static barriers. Walls cannot be entered
  or moved, and a floor cell cannot simultaneously contain the keeper and a
  crate or two crates.
- `CON-012` — push-only access geometry. Moving a crate requires keeper access
  to the cell behind it, one free destination cell ahead and no intervening
  second crate; pulling is unavailable.
- `CON-013` — irrecoverable objective deadlock. A legal push can leave some
  walking moves available while making it impossible for every crate to reach a
  goal.
- `CON-005` is absent: ordinary walking often has an inverse, but a primitive
  push does not always have a legal inverse because the keeper may be unable to
  reach the opposite side and cannot pull.
- Crate count, goal count, wall layout and orthogonal topology are parameters.
- Scarce strategic resource: keeper access to the required pushing side of each
  crate. Empty floor alone is insufficient if walls or crates cut off that
  access.
- Claim IDs: `SOK-001`, `SOK-002`, `SOK-004`, `SOK-006`.

### Information Genes

- `INF-001` — fully visible current state. Walls, floor, goals, crate positions
  and keeper position are inspectable before every move.
- Deadlock is not hidden system information. It is a reachability property of
  the visible state that may be difficult for the player to prove.
- The future is deterministic once a legal input is chosen. No random outcome,
  concealed content or preview queue exists.
- Claim IDs: `SOK-004`, `SOK-007`.

### Objective Genes

- `OBJ-004` — reconstruct specified configuration. Every crate must occupy a
  designated goal cell; individual crates are interchangeable and the final
  keeper position is irrelevant.
- This extends the evidenced boundary of `OBJ-004`: the target may be an
  equivalence class over interchangeable components, not only one labelled
  permutation.
- A crate reaching a goal is not permanently completed. Intermediate plans may
  move it away when necessary, provided the final state covers all goals.
- `OBJ-003` is absent. Preserving any legal keeper move is not sufficient:
  a deadlocked level may still allow indefinite walking.
- Claim IDs: `SOK-003`, `SOK-004`.

### Time Genes

- `TIM-002` — self-paced sequential action. Walking and pushes occur one at a
  time; the player may pause indefinitely and the level does not advance.
- Move or push counts can evaluate solution efficiency, but the core objective
  accepts any finite valid solution and no timer changes the state.
- Claim IDs: `SOK-001`, `SOK-007`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Adjacent floor cell is empty | Move toward it | Keeper occupies that cell; crates stay fixed | Direct navigation | `SOK-001` |
| One crate is adjacent and the cell beyond is empty | Move toward the crate | Crate shifts one cell; keeper takes its former cell | Body-mediated push | `SOK-001` |
| One crate is adjacent and a second crate is immediately beyond | Move toward them | Input is rejected | Only one crate may be pushed | `SOK-002` |
| One crate is adjacent but the keeper is on its destination side | Move away from the crate | Keeper moves; crate does not follow | Pulling is unavailable | `SOK-002` |
| Crate is pushed into a non-goal corner bounded on two axes | Continue walking elsewhere | Keeper may move, but that crate can never leave the corner | Non-terminal objective deadlock | `SOK-004` |
| Every crate occupies a goal | Complete the final push | Objective is satisfied regardless of keeper location | Target equivalence | `SOK-003` |

The corner case is the smallest static deadlock. More complex deadlocks may
depend on several crates, corridors and the keeper's reachable region, so not
every unsolvable state is locally obvious.

## Strategic and experiential structure

- Local decision: choose whether to walk or push and verify both the crate's
  destination and the keeper's post-push position.
- Medium-term planning: create access to the pushing sides needed for later
  moves, order crates through narrow passages and avoid occupying staging cells
  too early.
- Long-term structure: match crates to reachable goals, reserve corridors and
  reason backward from the final push direction into constrained goal cells.
- Common heuristics: never push a crate into a non-goal static corner; prefer
  plans that preserve multiple keeper routes; distinguish harmless walking
  cycles from state-changing pushes; analyse interacting crate patterns rather
  than only nearest-goal distance.
- Failure attribution: the decisive error is often an earlier legal push, not
  the later position where progress becomes visibly impossible. Without undo,
  recovery requires restarting the level.
- Player-trust factors: the deterministic rules and fully visible state make
  failure attributable in principle, but deep multi-crate deadlocks can be
  difficult to recognise without extensive lookahead.
- Claim IDs: `SOK-004`, `SOK-006`.

Academic solvers often collapse equivalent sequences of keeper walking into a
single push-level search decision. That is an optimisation of the state graph,
not evidence that navigation is absent from the player-facing rules.

## Replay and variation

- What changes between sessions: the level layout, initial crate and keeper
  positions, and goal placement.
- Randomness or procedural generation: none within a level.
- Multiple viable strategies: some levels admit different crate-goal
  assignments or push orders; others force a narrow sequence. Equivalent
  walking routes may reach the same push position.
- Typical replay motive: recover from a deadlock, find any solution, reduce
  pushes or reduce total keeper moves.
- Claim IDs: `SOK-004`, `SOK-006`, `SOK-007`.

## Adjacent systems and history

- Direct origin: the official product history records three December 1982
  computer releases by Thinking Rabbit and credits Hiroyuki Imabayashi.
- Variants: pull-enabled puzzles, multi-push rules, ice, teleporters, switches,
  multiple agents and automatic floors change the action or system genome and
  require separate analyses.
- Similar games: block-pushing and transport puzzles may share target placement
  while changing how the agent accesses objects. The 15-puzzle moves pieces
  through one empty space and does not share Sokoban's push-only geometry.
- Complexity caveat: Dor and Zwick, Culberson as cited by later work, and Hearn
  and Demaine analyse scalable formal families. Their hardness results do not
  establish that every fixed commercial level is hard for a human solver.
- Claim IDs: `SOK-009`, `SOK-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-009` | orthogonal step, one-cell push |
| System Behaviour | none | completion check only |
| Constraint | `CON-001`, `CON-011`, `CON-012`, `CON-013` | walls, layout, crate and goal counts |
| Information | `INF-001` | all current occupancy visible |
| Objective | `OBJ-004` | interchangeable crates, keeper position ignored |
| Time | `TIM-002` | optional move/push counts |

Canonical signature:

`ACT-008,ACT-009; ; CON-001,CON-011,CON-012,CON-013; INF-001; OBJ-004; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `5` (`GAME-0001`–`GAME-0005`).
- Exact genome matches: none.
- Tied near matches: `GAME-0002` — Rubik’s Cube (`4 / 12 = 0.333333`).
- Supported combination subsets: `COMB-0006`, `COMB-0036`, `COMB-0044`.
- Scan date: 2026-08-11.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0002` — Rubik's Cube | `CON-001`, `INF-001`, `OBJ-004`, `TIM-002` | Both reconstruct a visible state self-pacedly; every Cube turn has an inverse, while a Sokoban push may destroy objective reachability | Near, `0.333333` |

### Preserved research notes

- New combination: `COMB-0006`, whose seven genes are a proper subset of this
  nine-gene genome.
- New genes: `ACT-008`, `ACT-009`, `CON-011`, `CON-012`, `CON-013`.
- Classification result: `New gene`.
- Evidence and reasoning: navigation, body-mediated pushing, exclusive
  occupancy, push-only access and non-terminal objective deadlock have distinct
  typed boundaries. Grid size, wall arrangement, object count and target
  equivalence remain parameters.

## Taxonomy impact

- Registry changes: five bounded genes added; `CON-001`, `INF-001`, `OBJ-004`
  and `TIM-002` reused.
- Taxonomy-change record: none. A reachability property can be represented as a
  Constraint without changing the six-type model, consistent with `CON-004`.
- Candidate terms affected: move, push, static collision, push-only access and
  irreversibility now have bounded mappings.
- `CON-013` is not the negation of `CON-005`. The signature records active
  mechanics, not every absent opposite; Sokoban positively demonstrates legal
  transitions into objective-unreachable non-terminal states.
- `OBJ-003` remains absent because availability of any move does not express
  Sokoban success or even continued solvability.
- Claim IDs: `SOK-008`.

## Negative results

None. Sokoban confirms the planned distinction between legal-move availability
and objective reachability. It does not reject a prior gene; it provides a new
bounded constraint and a counter-boundary to primitive reversibility.
