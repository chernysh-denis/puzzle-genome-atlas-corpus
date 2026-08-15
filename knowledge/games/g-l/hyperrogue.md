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

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`:
  `ACT-008; SYS-131; CON-150; INF-001,INF-049; OBJ-002,OBJ-003; TIM-001`.
- Indexed games scanned: 98.
- Indexed combinations scanned: 98.
- Exact genome matches: none.
- Supported combination subset: `COMB-0099`.
- Scan date: 2026-08-14.

### Full prior-game Jaccard scan

- `GAME-0001`: `4 / 18 = 0.222222`; `GAME-0002`: `1 / 14 = 0.071429`.
- `GAME-0003`: `1 / 16 = 0.062500`; `GAME-0004`: `3 / 20 = 0.150000`.
- `GAME-0005`: `1 / 14 = 0.071429`; `GAME-0006`: `2 / 15 = 0.133333`.
- `GAME-0007`: `1 / 15 = 0.066667`; `GAME-0008`: `1 / 14 = 0.071429`.
- `GAME-0009`: `2 / 22 = 0.090909`; `GAME-0010`: `2 / 15 = 0.133333`.
- `GAME-0011`: `1 / 20 = 0.050000`; `GAME-0012`: `1 / 16 = 0.062500`.
- `GAME-0013`: `2 / 19 = 0.105263`; `GAME-0014`: `1 / 22 = 0.045455`.
- `GAME-0015`: `4 / 18 = 0.222222`; `GAME-0016`: `2 / 21 = 0.095238`.
- `GAME-0017`: `1 / 20 = 0.050000`; `GAME-0018`: `2 / 25 = 0.080000`.
- `GAME-0019`: `2 / 16 = 0.125000`; `GAME-0020`: `4 / 18 = 0.222222`.
- `GAME-0021`: `2 / 15 = 0.133333`; `GAME-0022`: `1 / 19 = 0.052632`.
- `GAME-0023`: `0 / 18 = 0.000000`; `GAME-0024`: `0 / 20 = 0.000000`.
- `GAME-0025`: `1 / 18 = 0.055556`; `GAME-0026`: `1 / 19 = 0.052632`.
- `GAME-0027`: `1 / 19 = 0.052632`; `GAME-0028`: `1 / 24 = 0.041667`.
- `GAME-0029`: `2 / 18 = 0.111111`; `GAME-0030`: `1 / 21 = 0.047619`.
- `GAME-0031`: `1 / 18 = 0.055556`; `GAME-0032`: `1 / 18 = 0.055556`.
- `GAME-0033`: `2 / 19 = 0.105263`; `GAME-0034`: `2 / 20 = 0.100000`.
- `GAME-0035`: `2 / 24 = 0.083333`; `GAME-0036`: `2 / 18 = 0.111111`.
- `GAME-0037`: `1 / 16 = 0.062500`; `GAME-0038`: `2 / 22 = 0.090909`.
- `GAME-0039`: `1 / 16 = 0.062500`; `GAME-0040`: `2 / 14 = 0.142857`.
- `GAME-0041`: `2 / 17 = 0.117647`; `GAME-0042`: `1 / 16 = 0.062500`.
- `GAME-0043`: `3 / 19 = 0.157895`; `GAME-0044`: `3 / 15 = 0.200000`.
- `GAME-0045`: `3 / 19 = 0.157895`; `GAME-0046`: `1 / 17 = 0.058824`.
- `GAME-0047`: `1 / 21 = 0.047619`; `GAME-0048`: `1 / 21 = 0.047619`.
- `GAME-0049`: `2 / 15 = 0.133333`; `GAME-0050`: `3 / 20 = 0.150000`.
- `GAME-0051`: `2 / 22 = 0.090909`; `GAME-0052`: `2 / 16 = 0.125000`.
- `GAME-0053`: `3 / 14 = 0.214286`; `GAME-0054`: `3 / 16 = 0.187500`.
- `GAME-0055`: `3 / 15 = 0.200000`; `GAME-0056`: `1 / 15 = 0.066667`.
- `GAME-0057`: `2 / 14 = 0.142857`; `GAME-0058`: `2 / 15 = 0.133333`.
- `GAME-0059`: `2 / 13 = 0.153846`; `GAME-0060`: `2 / 13 = 0.153846`.
- `GAME-0061`: `1 / 17 = 0.058824`; `GAME-0062`: `1 / 15 = 0.066667`.
- `GAME-0063`: `1 / 14 = 0.071429`; `GAME-0064`: `1 / 12 = 0.083333`.
- `GAME-0065`: `0 / 15 = 0.000000`; `GAME-0066`: `0 / 18 = 0.000000`.
- `GAME-0067`: `1 / 15 = 0.066667`; `GAME-0068`: `0 / 16 = 0.000000`.
- `GAME-0069`: `1 / 15 = 0.066667`; `GAME-0070`: `2 / 14 = 0.142857`.
- `GAME-0071`: `1 / 14 = 0.071429`; `GAME-0072`: `1 / 15 = 0.066667`.
- `GAME-0073`: `1 / 14 = 0.071429`; `GAME-0074`: `1 / 16 = 0.062500`.
- `GAME-0075`: `1 / 16 = 0.062500`; `GAME-0076`: `1 / 14 = 0.071429`.
- `GAME-0077`: `1 / 14 = 0.071429`; `GAME-0078`: `1 / 14 = 0.071429`.
- `GAME-0079`: `1 / 14 = 0.071429`; `GAME-0080`: `1 / 14 = 0.071429`.
- `GAME-0081`: `1 / 15 = 0.066667`; `GAME-0082`: `1 / 15 = 0.066667`.
- `GAME-0083`: `1 / 15 = 0.066667`; `GAME-0084`: `1 / 17 = 0.058824`.
- `GAME-0085`: `0 / 19 = 0.000000`; `GAME-0086`: `1 / 20 = 0.050000`.
- `GAME-0087`: `1 / 17 = 0.058824`; `GAME-0088`: `1 / 16 = 0.062500`.
- `GAME-0089`: `1 / 16 = 0.062500`; `GAME-0090`: `2 / 21 = 0.095238`.
- `GAME-0091`: `2 / 15 = 0.133333`; `GAME-0092`: `1 / 17 = 0.058824`.
- `GAME-0093`: `1 / 16 = 0.062500`; `GAME-0094`: `2 / 16 = 0.125000`.
- `GAME-0095`: `2 / 18 = 0.111111`; `GAME-0096`: `2 / 16 = 0.125000`.
- `GAME-0097`: `2 / 14 = 0.142857`; `GAME-0098`: `2 / 13 = 0.153846`.

- Near matches: `GAME-0001`, `GAME-0015` and `GAME-0020`, tied at
  `4 / 18 = 0.222222`.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| 2048 (`GAME-0001`) | `INF-001`, `OBJ-002`, `OBJ-003`, `TIM-001` | value merges on a finite square board versus avatar pursuit on an expanding hyperbolic graph | tied nearest at `4 / 18 = 0.222222` |
| Threes (`GAME-0015`) | `INF-001`, `OBJ-002`, `OBJ-003`, `TIM-001` | one-step number merging versus hostile response on hyperbolic adjacency | tied nearest at `4 / 18 = 0.222222` |
| Dorfromantik (`GAME-0020`) | `INF-001`, `OBJ-002`, `OBJ-003`, `TIM-001` | landscape placement versus player-centred pursuit routing | tied nearest at `4 / 18 = 0.222222` |
| Hyperbolica (`GAME-0098`) | `ACT-008`, `INF-001` | continuous `{4,5}` metric and real time versus discrete bitruncated `{7,3}` turns and hostile response | thematic boundary control at `2 / 13 = 0.153846` |

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

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Стандартний HyperRogue є дискретною покроковою
  грою на bitruncated `{7,3}`-мапі, де після ходу гравця рухаються переслідувачі.

## Нові гени

- [Observation | Corroborated | High] `SYS-131`, `CON-150`, `INF-049`.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0099` — зібрати скарб і зберегти
  шлях відступу після автоматичного кроку переслідувача.

## Зміни таксономії

- [Observation | Direct | High] Змін типів немає; зафіксовано негативну межу
  переносу трьох безперервних генів Hyperbolica.

## Нові питання

- Чи повторюються `SYS-131` та `INF-049` в інших дискретних неевклідових іграх?

## Наступна рекомендована гра

- Післяцільовий аудит 99-ігрового корпусу; нову гру не починати до рішення
  власника.
- Optimisation criterion: singleton burden, translation consistency, web UX
  and evidence-boundary audit at the promised stopping point.
- Expected information gain: identify which new genes need comparison games
  before any further corpus expansion.
- Backlog impact: closes the 35-game local Goal at exactly 99 games.

## Чому саме вона

- [Hypothesis | Limited | High] Audit now has a stable 99-game boundary and is
  more valuable than adding an unreviewed hundredth record.
