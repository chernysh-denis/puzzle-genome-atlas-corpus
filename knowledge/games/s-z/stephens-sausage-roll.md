---
game_id: GAME-0043
slug: stephens-sausage-roll
game_title: Stephen’s Sausage Roll
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0043
  - COMB-0044
gene_ids:
  action:
    - ACT-008
    - ACT-009
    - ACT-058
  system:
    - SYS-078
    - SYS-079
  constraint:
    - CON-001
    - CON-011
    - CON-013
    - CON-061
    - CON-090
    - CON-091
  information:
    - INF-001
  objective:
    - OBJ-027
  time:
    - TIM-001
---

# Game: Stephen's Sausage Roll

## Analysis scope

- Version / ruleset: the original 2016 PC release, scoped to World 1's
  `Maiden's Walk`, an ordinary early level containing one sausage and basic
  ground grills.
- Included: fixed orthogonal terrain; the persistent player-and-fork footprint;
  forward / backward movement and quarter-turns; fork-mediated sausage push;
  axial sliding versus lateral rolling of one two-cell sausage; independent
  top / bottom state for both sausage cells; grill contact; repeat-cook burn;
  sausage boundary loss; exact start-pose return after cooking; discrete undo
  and restart as recovery controls.
- Excluded: every later use of fork spearing, carried sausages, sausage stacks,
  walking on sausages, vertical falling interactions, fork detachment, ladders,
  multiple sausages, overworld progression, final-world state, secrets,
  narrative interpretation and speedrunning.
- Direct-play status: not conducted. The creator page establishes rolling and
  the permanently held fork; a formal academic rules account establishes the
  transition system and exact objective; contemporary reviews corroborate
  grilling, burning, pushing, turning and boundary loss. A specialist count
  record bounds `Maiden's Walk` to one sausage.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SSR-001` | Maiden's Walk is a fixed early World 1 puzzle containing one two-cell sausage, ground grills and one start pose | Confirmed | Corroborated | High | A1, S4, C1 |
| `SSR-002` | The player moves forward or backward and rotates ninety degrees while a fork remains attached in the facing cell | Confirmed | Corroborated | High | P1, A1, S1, S3 |
| `SSR-003` | A quarter-turn requires the complete two-by-two swept footprint of player, current fork, future fork and corner to be clear | Confirmed | Direct | High | A1, S3 |
| `SSR-004` | Contact from the fork displaces the sausage; axial contact slides it while lateral contact rolls it and changes which face is down | Confirmed | Direct | High | P1, A1, S1–S3 |
| `SSR-005` | The sausage occupies two grid cells and each cell has independently cookable top and bottom faces | Confirmed | Direct | High | A1, S2, S3 |
| `SSR-006` | A grill cooks the contacting face once; cooking the same face again burns the sausage and fails the attempt | Confirmed | Corroborated | High | A1, S1–S3 |
| `SSR-007` | Pushing the sausage off the supported level boundary fails the attempt | Confirmed | Corroborated | High | S1, S2 |
| `SSR-008` | Completion requires all four sausage faces cooked exactly once and the player restored to the exact starting position and orientation | Confirmed | Direct | High | A1, S3 |
| `SSR-009` | A legal push can strand an uncooked face or block the required return while leaving other player movement available | Observation | Corroborated | High | S1, S3, S4 |
| `SSR-010` | Every input and its roll / grill resolution completes before the next input; no clock or random event changes scoped state | Observation | Corroborated | High | A1, S1–S3 |
| `SSR-011` | Current terrain, pose, sausage orientation and cook marks are visible | Observation | Corroborated | High | P1, A1, S1–S3 |
| `SSR-012` | The scope shares push-planning genes with Sokoban but not its generic target-arrangement objective or self-paced-without-resolution time gene | Observation | Corroborated | High | SSR-001–SSR-011 |

## Basic data

- Release / origin: Stephen Lavelle developed and Increpare Games published
  Stephen's Sausage Roll on 18 April 2016.
- Platform or physical form: digital three-dimensional presentation of a
  deterministic orthogonal-grid movement puzzle.
- Puzzle family: oriented rigid-body push and exact-once surface processing.
- Primary and creator sources:
  - **[P1]** [Stephen Lavelle's official game page](https://www.stephenssausageroll.com/about.html),
    identifying the creator, permanently held bidirectional fork and round
    rollable sausage.
  - **[P2]** [creator-published Steam listing](https://store.steampowered.com/app/353540/Stephens_Sausage_Roll/),
    confirming developer / publisher, release and the original PC product.
- Formal rules evidence:
  - **[A1]** Jason Liu,
    [Further Hardness Results for Stephen's Sausage Roll](https://erikdemaine.org/theses/jliuM.pdf),
    MIT master's thesis, formally specifying player / fork rotation and
    clearance, axial slide, lateral roll, four independent sausage faces,
    grills, repeat-cook burning and exact return-pose completion. Complexity
    results are not used to rate the fixed level's human difficulty.
- Contemporary corroboration:
  - **[S1]** [PC Gamer, 9 May 2016](https://www.pcgamer.com/stephens-sausage-roll-is-a-breakfast-that-will-break-you/),
    documenting fork pushing and turning, rolling, two-side cooking, repeat-
    contact burning and water-edge failure.
  - **[S2]** [The Guardian review, 18 April 2016](https://www.theguardian.com/technology/2016/apr/18/stephens-sausage-roll-review-stephen-lavelle-puzzle-game),
    corroborating two-cell / four-section cooking and burned-state recovery.
  - **[S3]** [The Stack review, 2016](https://www.wurb.com/stack/archives/3136),
    detailing the two-cell sausage, face changes under lateral rolling, fork
    footprint, impassable grills, cooked-sausage persistence and return to the
    start after all cooking.
- Bounded scope evidence:
  - **[S4]** [World 1 spoiler-light mechanical guide](https://steamcommunity.com/sharedfiles/filedetails/?id=2019667067),
    used to corroborate early fork clearance, push access and grill approach
    boundaries while excluding its later-world rules.
  - **[C1]** [community sausage-count audit](https://gaming.stackexchange.com/questions/266985/how-many-sausages-are-there-in-stephens-sausage-roll),
    used only to establish that `Maiden's Walk` contains one sausage.
- Claim IDs: `SSR-001`–`SSR-012`.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. Forward or backward input moves the
  persistent player / fork assembly one cardinal cell when both required
  destinations are traversable.
- `ACT-009` — push adjacent movable object. Moving or sweeping the attached fork
  into one sausage cell commands the sausage one logical position away. The
  existing wording is generalised from direct body contact to body-attached
  tool contact; one adjacent object's player-commanded displacement remains the
  boundary.
- `ACT-058` — rotate agent with body-attached tool sweep. A quarter-turn keeps
  the player cell fixed, moves the fork between adjacent cells and can contact
  a sausage along the swept direction.
- `ACT-018` is absent: the scoped level has one sausage and no contiguous chain
  of separately movable objects.
- Undo and restart restore prior state but remain recovery interface controls,
  not extra manipulation genes or branchable simulation time.
- Claim IDs: `SSR-002`–`SSR-004`.

### System Behaviour Genes

- `SYS-078` — orientation-dependent elongated-body displacement. A contact
  along the sausage axis slides its two-cell footprint unchanged; a lateral
  contact rolls it one cell and swaps its top / bottom faces.
- `SYS-079` — contact-triggered per-surface cooking. Occupying a grill updates
  only the contacting face of each sausage cell, preserving all other face
  states for later rolls.
- The displacement is automatic resolution of one fork command, not a second
  player action. Grill state does not behave like a Sokoban goal: a cooked
  sausage stays movable and can be ruined later.
- Resolution order at the scoped boundary: validate player / fork destinations
  and turn sweep; identify fork-sausage contact; resolve sausage slide or roll
  if its two-cell destination is supported and clear; update any contacting
  face on grills; fail on repeated cooking or boundary loss; then test all-four-
  cooked plus exact-start-pose completion.
- Claim IDs: `SSR-003`–`SSR-008`, `SSR-010`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. Maiden's Walk has one finite authored
  terrain grid with fixed support, barriers, grills and start pose.
- `CON-011` — exclusive occupancy with static barriers. Player, fork and both
  sausage cells require compatible cells; fixed terrain blocks entry, while
  grills are entity-specific barriers to the player / fork but support sausage
  faces.
- `CON-013` — irrecoverable objective deadlock. A legal push can leave ordinary
  walking available while making an uncooked face or the exact return pose
  unreachable without undo / restart.
- `CON-061` — terminal payload boundary escape. Moving the required sausage
  beyond supported terrain into water immediately fails the attempt.
- `CON-090` — oriented agent-plus-body sweep clearance. The player and attached
  fork occupy two ordered adjacent cells; translation preserves facing and a
  turn is legal only when the whole two-by-two sweep is free. Permanent
  attachment is a coupling parameter shared with a reversibly carried occupied
  body, not a separate clearance rule.
- `CON-091` — exact-once surface heat capacity. Each of four identified sausage
  faces may contact a grill once; a second cook is terminal rather than merely
  inefficient.
- `CON-012` is absent: manipulation does not always require the player's body
  immediately behind the sausage or one free cell in front. The attached fork
  can push from a corner during a legal turn, and sausage destination validity
  uses its two-cell footprint.
- Scarce strategic resources: turn-clearance cells, access for the fork to the
  required contact side, supported parking space, the one remaining legal grill
  contact for each face and a route back to the start pose.
- Claim IDs: `SSR-001`, `SSR-003`, `SSR-006`–`SSR-009`.

### Information Genes

- `INF-001` — fully visible current state. Terrain, grill positions, player and
  fork pose, sausage footprint / orientation and cooked face markings are
  inspectable before the next move.
- Deadlock and burn risk are derived from visible deterministic state rather
  than hidden content or a random successor.
- Claim IDs: `SSR-010`, `SSR-011`.

### Objective Genes

- `OBJ-027` — exact-once surface processing plus return pose. Success requires
  all four identified faces of the scoped sausage to be cooked exactly once and
  the player / fork assembly to occupy its exact starting position and
  orientation afterward.
- `OBJ-004` is absent: the essential target is irreversible per-surface process
  history plus a return condition, not merely a final arrangement of existing
  component positions. Two visually identical layouts can differ by face-state
  completion or burn history.
- `OBJ-014` is absent because the sausage has no single receiver; distinct
  faces must contact one or more grills in a planned sequence.
- Claim IDs: `SSR-006`, `SSR-008`, `SSR-012`.

### Time Genes

- `TIM-001` — discrete turn with automatic resolution. Each movement or turn
  input completes fork contact, sausage slide / roll, cooking, burn / fall and
  completion checks before the next input.
- `TIM-002` is absent under the registry's exclusive boundary: decisions are
  untimed, but each command triggers decision-relevant automatic roll and grill
  state resolution rather than changing state without a system step.
- `TIM-007` is absent. Discrete undo reverses a self-paced move; it does not
  expose continuously lived history as a player-navigable simulation axis.
- Claim IDs: `SSR-004`–`SSR-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Player / fork destinations are clear | Move forward or backward | Both ordered footprint cells translate one step with facing preserved | direct navigation uses an oriented two-cell assembly | `SSR-002`, `SSR-003` |
| Future fork cell or swept corner is blocked | Command a quarter-turn | Turn is rejected; player and fork pose remain fixed | rotation needs full two-by-two clearance | `SSR-003` |
| Fork contacts a sausage end along its axis | Move toward it | Sausage slides one cell without changing which faces are top / bottom | axial push is translation | `SSR-004` |
| Fork contacts one sausage side laterally | Move or turn toward it | Sausage rolls one cell and its top / bottom faces swap | lateral contact changes pose and face exposure | `SSR-004`, `SSR-005` |
| One uncooked face rests on a grill | Complete the contact move | Only that identified face becomes cooked | cooking state is per surface | `SSR-005`, `SSR-006` |
| An already cooked face contacts a grill | Complete the contact move | Sausage burns and the current attempt fails | grill use has exact-once capacity | `SSR-006` |
| Sausage is pushed beyond supported terrain | Complete the push | It falls into water and the attempt fails | boundary escape is terminal | `SSR-007` |
| All four faces are cooked but player pose differs from start | Continue moving | Level remains incomplete | processing alone is insufficient | `SSR-008` |
| All four faces are cooked exactly once and start pose is restored | Enter exact position / orientation | Level completes | success is a conjunctive processed-state and return target | `SSR-008` |

## Strategic and experiential structure

- Local decision: choose whether the next fork contact slides or rolls the
  sausage and identify which physical face will touch a grill.
- Medium-term planning: schedule four distinct face contacts while preserving
  fork access, turn clearance and a supported place from which the sausage can
  be moved again.
- Long-term structure: solve a state-space tour that processes every face once
  and still restores the player's oriented two-cell footprint to its entrance.
- Common heuristics: label the four faces mentally; distinguish axial push from
  lateral roll; work backward from the required return pose; never cook a face
  unless the sausage remains retrievable; reserve the few viable turn squares.
- Failure attribution: visible deterministic state makes burn and fall locally
  explicit, while a deeper failure may originate in an earlier legal roll that
  removed access to one remaining face.
- Player-trust factors: turn sweep, contact direction, face permutation,
  support tests, grill timing, burn precedence, undo restoration and start-pose
  equality must remain stable.
- Claim IDs: `SSR-003`–`SSR-011`.

## Replay and variation

- What changes between puzzles: terrain / grill layout, sausage count and pose,
  start pose, available clearance and later excluded emergent interactions.
- Randomness or procedural generation: none in the scoped authored level.
- Multiple viable strategies: local walking detours can differ, but the single
  sausage's face-cooking order is strongly constrained by access and return.
- Typical replay motive: undo a burn or stranding move, reconstruct a valid
  face order or replay with fewer exploratory inputs.
- Claim IDs: `SSR-001`, `SSR-009`–`SSR-011`.

## Adjacent systems and history

- Sokoban is the mathematical near match through navigation, one-object push,
  fixed occupancy, visible state and non-terminal deadlock. Its one-cell crates
  translate without orientation-dependent system response, targets care about
  final occupancy and time has no post-input system transition.
- Baba Is You shares adjacent object pushing and automatic resolution after one
  input, but dynamically recomputes spatial syntax. It has no elongated rigid
  body, persistent surface processing or fixed body-attached tool footprint.
- Patrick's Parabox shares navigation, single-object push, occupancy, visible
  deadlock and compound chain possibilities. It mutates containment across
  nested grids; Maiden's Walk instead transforms one object's orientation and
  per-face cook history on one fixed grid.
- The later excluded game layers exploit spearing, stacking and vertical
  support. They may add genes and are not silently projected onto World 1.
- Claim IDs: `SSR-001`–`SSR-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-009`, `ACT-058` | cardinal motion, fork contact and quarter-turn direction |
| System Behaviour | `SYS-078`, `SYS-079` | axial slide / lateral roll and per-face grill update |
| Constraint | `CON-001`, `CON-011`, `CON-013`, `CON-061`, `CON-090`, `CON-091` | terrain, tool sweep, supported footprint and heat capacity |
| Information | `INF-001` | visible current pose, face marks and terrain |
| Objective | `OBJ-027` | four exact-once faces plus exact start pose |
| Time | `TIM-001` | discrete input then complete automatic resolution |

Canonical signature:

`ACT-008,ACT-009,ACT-058; SYS-078,SYS-079; CON-001,CON-011,CON-013,CON-061,CON-090,CON-091; INF-001; OBJ-027; TIM-001`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `42` (`GAME-0001`–`GAME-0042`).
- Exact genome matches: none.
- Tied near matches: `GAME-0006` — Sokoban (`6 / 17 = 0.352941`).
- Supported combination subsets: `COMB-0043`, `COMB-0044`.
- Scan date: 2026-08-12.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0006` — Sokoban | `ACT-008`, `ACT-009`, `CON-001`, `CON-011`, `CON-013`, `INF-001` | Sokoban translates one-cell crates toward goal occupancy under self-paced actions; Maiden's Walk rotates a player-fork footprint, slides or rolls a two-cell body, records per-face heat and resolves exact-once burn / return conditions after every input | Near, `0.352941` |

### Preserved research notes

- New genes: `ACT-058`, `SYS-078`, `SYS-079`, `CON-090`, `CON-091` and
  `OBJ-027`.
- Classification result: `New gene` and a new combination of known and new
  genes.
- Evidence and reasoning: ordinary navigation, fork-mediated one-object push,
  occupancy, visible state and deadlock recur. Tool rotation, elongated-body
  response, face-state cooking, heat capacity and conjunctive return completion
  create independently testable decisions rather than cosmetic sausage
  parameters.

## Combination record

- Registered [`COMB-0043`](../../combinations/COMB-0043.md), the eight-gene
  oriented-tool exact-once surface-processing core.
- No earlier complete genome contains this set. It remains verified for one
  game until an independently analysed supporter appears.

## Taxonomy impact

- Registry changes: added six active IDs; reused eight existing genes.
- `ACT-009` is generalised to include an attached tool as the player's contact
  body while retaining adjacent, player-commanded, one-position displacement.
- `CON-061` is generalised from a receiver-bound payload to any required moving
  puzzle object lost beyond the spatial boundary; Cut the Rope remains inside
  the unchanged terminal-loss contract.
- `CON-011` gains a multi-cell occupant and entity-specific barrier example
  without changing exclusive occupancy.
- Taxonomy-change record: none; no prior signature, lifecycle, merge or split
  changes.
- Candidate terms affected: six terms promoted to active IDs.

## Negative results

- `ACT-018` is absent because the scope never pushes a chain of distinct
  movable objects.
- `CON-012` is absent because an attached fork can push during a corner turn;
  strict body-behind-object access and a one-cell destination are false.
- `OBJ-004` is absent because success depends on irreversible per-face process
  state plus exact avatar return, not only a final component arrangement.
- `TIM-002` is absent because every input triggers decision-relevant roll,
  cooking and failure resolution before the next command.
- `TIM-007` is absent because ordinary discrete undo is expressly outside the
  branchable continuous-history boundary.
- `COMB-0036` does not recur; its target-reconstruction and time requirements
  are preserved rather than weakened to force a Sokoban-family match.
