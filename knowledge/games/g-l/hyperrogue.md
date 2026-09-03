---
game_id: GAME-0099
slug: hyperrogue
game_title: HyperRogue
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0099
gene_ids:
  action:
    - ACT-008
  system:
    - SYS-131
  constraint:
    - CON-150
  information:
    - INF-001
    - INF-049
  objective:
    - OBJ-002
    - OBJ-003
  time:
    - TIM-001
---

# Game: HyperRogue

## Analysis scope

- Version / ruleset: standard grid-based, turn-based HyperRogue, bounded to one
  local rules packet: the player moves from one open cell onto one treasure,
  the treasure total rises by one, every surviving pursuer takes its automatic
  shortest-route response step, and the visible projection remains centred on
  the player's new neighbourhood.
- Included: one adjacent player move; one treasure contact; the standard
  bitruncated `{7,3}` hyperbolic tiling; graph distance; one automatic hostile
  response; current-state visibility; a player-centred finite projection;
  treasure-score accumulation; survival; one discrete turn.
- Excluded: individual land terrain rules, Orbs, ranged attacks, waiting,
  checkmate protection beyond the local safety test, procedural spawn rates,
  quests, alternate geometries and projections, multiplayer, shmup and 3D/VR.
- Direct-play status: not conducted. Creator documentation and the authors'
  paper directly establish the standard tiling, adjacent movement, turn order,
  shortest-route pursuit, treasure objective, player-centred view and lazy
  neighbourhood generation. The executable control is an authored rules
  fixture, not a production seed, map coordinate or claim about enemy tie
  breaking in the shipped build.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `HRG-001` | The first Hyperbolic Rogue draft appeared in November 2011 and HyperRogue reached Steam in January 2015 | Confirmed | Direct | High | P1, P2 |
| `HRG-002` | Standard play is grid-based and turn-based: the player may move to an open adjacent tile, then each enemy moves | Confirmed | Direct | High | P3, P4 |
| `HRG-003` | Pursuers try to reduce shortest-path distance to the player | Confirmed | Direct | High | P4 |
| `HRG-004` | The standard world is the bitruncated order-three heptagonal tiling derived from `{7,3}`, not Hyperbolica's `{4,5}` square tiling | Confirmed | Direct | High | P4, P5 |
| `HRG-005` | Ordinary play accumulates treasure while preserving survival; collecting more treasure increases same-land pressure | Confirmed | Direct | High | P3, P6 |
| `HRG-006` | The implementation generates only a finite neighbourhood on demand although the represented hyperbolic world is effectively unbounded | Confirmed | Direct | High | P5 |
| `HRG-007` | One bounded control accepts an adjacent treasure step, advances one pursuer, recentres the view and rejects six invalid transitions | Observation | Direct | High | V1 |

## Basic data

- Release / origin: Zeno Rogue's first technical draft appeared in November
  2011; the expanded game entered Steam in January 2015.
- Platform or physical form: desktop and mobile turn-based roguelike with a
  browser demo and optional experimental modes.
- Puzzle family: discrete hyperbolic-grid pursuit and treasure routing.
- Creator and primary sources:
  - **[P1]** [HyperRogue history](https://roguetemple.com/z/hyper/history.php),
    for the 2011 draft and January 2015 Steam history.
  - **[P2]** [HyperRogue on Steam](https://store.steampowered.com/app/342610/HyperRogue/),
    for the current official product record.
  - **[P3]** [HyperRogue FAQ](https://roguetemple.com/z/hyper/faq.php), for
    adjacent-cell controls, turn waiting, view recentering, treasure goals,
    escalating monsters and the standard turn-based mode boundary.
  - **[P4]** [HyperRogue: Playing with Hyperbolic Geometry](https://roguetemple.com/z/hyper/papers/hyperrogue.pdf),
    the authors' account of adjacent movement, post-player enemy motion,
    shortest-route pursuit, the truncated order-seven triangular tiling and
    its tactical heptagons.
  - **[P5]** [Experiments with geometry](https://roguetemple.com/z/hyper/geoms.php)
    and [Programming HyperRogue](https://roguetemple.com/z/hyper/dev.php), for
    the bitruncated `{7,3}` standard map, tile generation and finite generated
    neighbourhood.
  - **[P6]** [Official HyperRogue project page](https://roguetemple.com/z/),
    for land-specific treasure, enemies and the emphasis on tactics.
  - **[V1]** [`verify_hyperrogue_control.py`](../../../scripts/verify_hyperrogue_control.py),
    an executable one-turn control with six rejected invalid cases.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. One click or directional input
  selects one traversable adjacent cell for the persistent player character.
- The action is one graph edge, not continuous curved-metric integration and
  not a remote destination followed by automatic multi-step pathfinding.

### System Behaviour Genes

- `SYS-131` — shortest-route hostile step after a player turn. Once the
  player's move, attack or wait resolves, every eligible enemy automatically
  takes its one-turn response, normally choosing a step that reduces current
  graph distance to the player.
- Scoped resolution order: validate the adjacent player destination; move the
  player; credit treasure contact; recalculate shortest-path distances; advance
  the pursuer; check immediate danger; expose the next input state.

### Constraint Genes

- `CON-150` — bitruncated `{7,3}` cell adjacency. Standard play uses the
  hyperbolic soccer-ball tiling derived from three heptagons meeting at each
  vertex before bitruncation, yielding decision-bearing hexagonal and
  heptagonal cells rather than a flat hex grid or `{4,5}` squares.
- Hyperbolica's `CON-149` therefore fails the transfer test: both games are
  hyperbolic, but their polygon family and local incidence are different.

### Information Genes

- `INF-001` — visible current state. Nearby traversable cells, walls,
  treasures and hostiles are shown before the move.
- `INF-049` — player-centred finite projection of an unbounded tiling. The
  display projects a generated local neighbourhood around the player; cells
  shrink toward the boundary while the implementation generates only a finite
  radius and may recenter the view on the character.
- This is not `INF-048`: no continuous first-person pose or collision metric is
  required for standard grid play.

### Objective Genes

- `OBJ-002` — maximise accumulated score. Treasure contact increases the run's
  treasure total; ordinary play invites the player to collect as much as can
  be survived.
- `OBJ-003` — preserve move availability. The run must avoid the checkmated
  state where every available move leads to death.

### Time Genes

- `TIM-001` — discrete turn with automatic resolution. One player command is
  followed by treasure, hostile and terminal-state resolution before the next
  command is accepted.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Player at `P0`, treasure at adjacent `P1`, enemy three graph steps from `P1` | Move `P0 → P1` | Player reaches `P1`, treasure score becomes one, enemy advances one shortest-route step and view centre becomes `P1` | complete bounded turn order | `HRG-002`, `HRG-003`, `HRG-007` |
| Same state, target is not adjacent | Attempt remote move | Reject before any state mutation | navigation is one cell edge | `HRG-002`, `HRG-007` |
| `{6,3}` flat control or unbitruncated `{7,3}` control | Substitute geometry | Reject standard-geometry predicate | curvature theme alone does not define `CON-150` | `HRG-004`, `HRG-007` |
| Enemy would finish adjacent after the scoped response | Commit unsafe fixture | Reject bounded safe-route control | survival remains decision-bearing | `HRG-003`, `HRG-007` |

## Strategic and experiential structure

- Local decision: choose an adjacent cell that collects value without allowing
  the automatic response to remove every safe continuation.
- Medium-term planning: exploit divergent routes and tactical heptagons rather
  than assuming Euclidean parallel pursuit.
- Long-term structure: spread treasure collection across lands because local
  treasure counts raise local hostile pressure and unlock later goals.
- Failure attribution: an unsafe move is legible from current adjacency and
  pursuer distance, while procedural population affects the broader run.
- Player-trust factors: movement, attack and hostile response share one visible
  cell graph; projection distortion must not alter the underlying adjacency.

## Replay and variation

- The world and inhabitants are generated as exploration approaches them.
- Land mix, treasure placement and pursuer configuration vary between runs.
- Alternate routes proliferate exponentially, but local action remains one
  adjacent move per turn in the scoped mode.

## Adjacent systems and history

- Direct predecessor: Zeno Rogue's 2011 Hyperbolic Rogue draft established the
  one-piece, adjacent-move hyperbolic rules core.
- Variants: the game exposes unbitruncated heptagonal, Euclidean, spherical,
  real-time shmup and many other geometry experiments outside this boundary.
- Similar games: Hyperbolica supplies the corpus's nearest thematic control.
- Important difference: Hyperbolica continuously integrates a first-person
  pose in `{4,5}` space; standard HyperRogue advances tokens over a discrete
  bitruncated `{7,3}` graph and then resolves hostile turns.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008` | adjacent click / keyboard direction |
| System Behaviour | `SYS-131` | enemy order and shortest-path tie breaking |
| Constraint | `CON-150` | bitruncated `{7,3}`, hexagon/heptagon cell class |
| Information | `INF-001`, `INF-049` | projection model and generated radius |
| Objective | `OBJ-002`, `OBJ-003` | treasure total and survival horizon |
| Time | `TIM-001` | one player command then hostile response |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `98` (`GAME-0001`–`GAME-0098`).
- Exact genome matches: none.
- Tied near matches: `GAME-0001` — 2048 (`4 / 18 = 0.222222`); `GAME-0015` — Threes (`4 / 18 = 0.222222`); `GAME-0020` — Dorfromantik (`4 / 18 = 0.222222`).
- Supported combination subsets: `COMB-0099`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| 2048 (`GAME-0001`) | `INF-001`, `OBJ-002`, `OBJ-003`, `TIM-001` | value merges on a finite square board versus avatar pursuit on an expanding hyperbolic graph | Near, `0.222222` |
| Threes (`GAME-0015`) | `INF-001`, `OBJ-002`, `OBJ-003`, `TIM-001` | one-step number merging versus hostile response on hyperbolic adjacency | Near, `0.222222` |
| Dorfromantik (`GAME-0020`) | `INF-001`, `OBJ-002`, `OBJ-003`, `TIM-001` | landscape placement versus player-centred pursuit routing | Near, `0.222222` |

### Preserved research notes

- New genes: `SYS-131`, `CON-150`, `INF-049`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: continuous hyperbolic integration, order-five square
  incidence and continuous first-person curvature cues all fail explicit
  transfer tests. Discrete pursuit, bitruncated topology and finite projected
  neighbourhood remain independently decision-bearing.

## Taxonomy impact

- Registry changes: add `SYS-131`, `CON-150`, `INF-049` with HyperRogue as
  evidence.
- Taxonomy-change record: none; all three distinctions fit existing types.
- Candidate terms affected: retain the continuous/discrete hyperbolic boundary.

## Negative results

- `CON-149` does not transfer from Hyperbolica: `{4,5}` squares and standard
  HyperRogue's bitruncated `{7,3}` grid are not the same incidence rule.
- `SYS-130` and `INF-048` do not transfer: standard HyperRogue resolves cell
  adjacency and a projected local view without a continuous first-person pose.
