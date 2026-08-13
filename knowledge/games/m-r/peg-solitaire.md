---
game_id: GAME-0019
slug: peg-solitaire
game_title: Peg Solitaire
analysis_status: reviewed
reviewed: 2026-08-11
combination_ids:
  - COMB-0019
gene_ids:
  action:
    - ACT-014
  system:
    - SYS-033
  constraint:
    - CON-001
    - CON-013
    - CON-053
    - CON-054
    - CON-055
  information:
    - INF-001
  objective:
    - OBJ-004
  time:
    - TIM-001
---

# Game: Peg Solitaire

## Analysis scope

- Version / ruleset: the traditional English central game on the fixed
  cross-shaped 33-hole board, beginning with 32 pegs and the centre hole empty.
- Included: selecting one peg; jumping it horizontally or vertically over one
  adjacent peg into the empty hole immediately beyond; automatic removal of
  the jumped peg; one jump per decision; termination when no legal jump exists;
  success only with one peg remaining in the centre.
- Excluded: French and triangular boards, diagonal and long jumps, reverse
  jumps or “unjumps”, multi-jump sequences counted as one move, arbitrary start
  vacancies or final holes, hints, undo, restart, timers, move-count ratings and
  software-specific score.
- Direct-play status: not conducted for this record. Public implementation
  rules, academic transition encodings and mathematical analyses provide
  reproducible rule and reachability evidence.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PEG-001` | The English central game uses a fixed cross-shaped board of 33 holes, with every hole except the centre initially occupied | Confirmed | Corroborated | High | F1, F3, F4 |
| `PEG-002` | The player selects an occupied source and an empty destination exactly two holes away horizontally or vertically | Confirmed | Direct | High | F1–F3, F5 |
| `PEG-003` | A jump is legal only when the intervening adjacent hole is occupied | Confirmed | Direct | High | F1–F3, F5 |
| `PEG-004` | Resolution empties the source and intervening holes and fills the destination, leaving all other holes unchanged | Confirmed | Direct | High | F1, F2 |
| `PEG-005` | Every legal forward jump removes exactly one peg, and the scoped rules provide no move that restores it | Confirmed | Direct | High | F1–F3, F5 |
| `PEG-006` | Reducing the 32-peg start to one peg therefore requires exactly 31 single-jump decisions | Observation | Corroborated | High | PEG-001, PEG-005 |
| `PEG-007` | The central-game objective is the exact complementary state with only the centre hole occupied | Confirmed | Corroborated | High | F3, F4 |
| `PEG-008` | Play terminates when no legal jump remains; a terminal state with several pegs or a lone off-centre peg does not satisfy the scoped objective | Confirmed | Corroborated | High | F2, F5, PEG-007 |
| `PEG-009` | Every hole occupancy is visible and jump resolution is deterministic; the scoped puzzle has no hidden or random event | Observation | Direct | High | F1, F2 |
| `PEG-010` | A legal jump can create a non-terminal board from which the centre-complement target is unreachable | Confirmed | Corroborated | High | F3, F4 |
| `PEG-011` | Strict peg-count decrease makes the forward state graph acyclic even though different jump sequences may converge on one occupancy | Observation | Corroborated | High | PEG-004–PEG-006 |
| `PEG-012` | Moving and capture are mechanically distinct: the player names source and destination, while the rules remove the intervening peg automatically | Observation | Direct | High | F1, F2 |

## Basic data

- Origin: Peg Solitaire is a historical single-player peg-jumping puzzle. This
  record concerns the standard English cross board and its central complement
  problem rather than making a claim about the earliest physical artefact.
- Physical form: 33 addressable holes and 32 identical pegs; digital controls
  are treated only as implementations of the physical jump.
- Puzzle family: deterministic jump-and-remove reduction puzzle.
- Sources:
  - **[F1]** [Simon Tatham's Pegs documentation](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/pegs.html),
    implementation rules for orthogonal two-hole jumps, vacant landing holes,
    intervening removal and the traditional English board shape.
  - **[F2]** [Stanford — Satisfiability and Peg Solitaire](https://ai.stanford.edu/~chuongdo/satpage/index.html),
    explicit ordered-triple transition encoding, unchanged-hole boundary,
    single-survivor objective and no-jump termination.
  - **[F3]** [“Modelling and solving English Peg Solitaire”](https://www.sciencedirect.com/science/article/pii/S0305054805000195),
    peer-reviewed description of the 33-hole English board, orthogonal moves,
    central complement objective and dead-end modelling.
  - **[F4]** [George Bell — “Notes on solving and playing peg solitaire on a computer”](https://arxiv.org/abs/0903.3696),
    analysis of winning and dead positions in the 33-hole central game.
  - **[F5]** [UC Berkeley GamesCrafters rules](https://gamescrafters.berkeley.edu/games.php?puzzle=pegsolitaire),
    academic-project corroboration of start occupancy, jump removal and the
    one-peg goal.
- Claim IDs: `PEG-001`–`PEG-012`.

## Mechanical decomposition

### Action Genes

- `ACT-014` — relocate selected controlled board piece. The player selects one
  occupied source and the eligible empty destination two orthogonal holes away.
  The intervening peg is not independently selected for removal.
- `ACT-009` and `ACT-018` are absent. No agent pushes the adjacent peg or a
  contiguous chain into free space; the jumping peg passes over it.
- Claim IDs: `PEG-002`, `PEG-003`, `PEG-012`.

### System Behaviour Genes

- `SYS-033` — jump-triggered intervening removal. After the legal relocation,
  the system removes the middle peg, transforming the local triple from
  `occupied–occupied–empty` to `empty–empty–occupied`.
- The destination relocation itself remains player-commanded `ACT-014`; only
  the uncommanded capture consequence belongs here.
- Claim IDs: `PEG-004`, `PEG-005`, `PEG-012`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. Exactly 33 cross-arranged holes retain
  their addresses throughout the problem; positions outside the cross are not
  holes and cannot be entered.
- `CON-053` — occupied-middle empty-landing jump predicate. Source and middle
  must contain pegs, destination must be an addressable empty hole, distance is
  exactly two and direction is horizontal or vertical.
- `CON-054` — forward-only monotonic material reduction. Every accepted jump
  permanently reduces the peg count by one; reverse jumps are outside scope.
- `CON-055` — no-jump terminal exhaustion. Absence of any legal occupancy
  triple ends play regardless of the remaining peg count.
- `CON-013` — irrecoverable objective deadlock. Some legal choices preserve
  further jumps yet eliminate every continuation to the exact centre target.
- `CON-005` is absent: a primitive jump has no legal forward inverse because
  the captured peg cannot be restored.
- Claim IDs: `PEG-001`–`PEG-010`.

### Information Genes

- `INF-001` — fully visible current state. Every hole, peg and legal geometric
  relation is inspectable before selecting a jump.
- No Information gene for “future pieces” is assigned: there is no future
  random generation, preview queue or concealed current occupancy.
- Claim IDs: `PEG-001`–`PEG-003`, `PEG-009`.

### Objective Genes

- `OBJ-004` — reconstruct specified configuration. The accepted target is the
  exact one-peg centre occupancy, which is the complement of the 32-peg start.
- Merely minimising the number of remaining pegs is a useful partial metric but
  not the scoped success condition. A single survivor elsewhere is therefore
  not an exact target match.
- Claim IDs: `PEG-006`–`PEG-008`.

### Time Genes

- `TIM-001` — discrete turn with automatic resolution. Each selected jump
  completes source relocation and intervening removal before another source is
  chosen.
- There is no in-rules clock, opponent turn or simultaneous unresolved motion.
  A physical player may deliberate indefinitely between jumps.
- Claim IDs: `PEG-002`–`PEG-005`, `PEG-009`.

## Reproducible transitions

| Before | Player command | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Horizontal holes read `peg, peg, empty` | Move the first peg to the third hole | Local occupancy becomes `empty, empty, peg` | Destination command and automatic middle removal are distinct | `PEG-002`–`PEG-004` |
| Horizontal holes read `peg, empty, empty` | Attempt the same two-hole relocation | Move is illegal | Occupied intervening hole is mandatory | `PEG-003` |
| Horizontal holes read `peg, peg, peg` | Attempt to jump into the third hole | Move is illegal | Destination must already be empty | `PEG-002`, `PEG-003` |
| A diagonal `peg, peg, empty` triple exists | Attempt the diagonal jump | Move is illegal in the English central rules | Geometry is orthogonal, not merely collinear | `PEG-002` |
| A legal jump leaves 31 pegs | Complete its automatic removal | No rule can return the count to 32 | Forward play is strictly monotonic | `PEG-005`, `PEG-011` |
| Several isolated pegs remain | Search all orthogonal triples | No legal jump exists and play terminates unsuccessfully | Terminal exhaustion and objective differ | `PEG-008` |
| One off-centre peg remains | Evaluate final occupancy | No jumps remain, but the centre-complement target is false | One survivor alone is insufficient in scope | `PEG-007`, `PEG-008` |
| The thirty-first jump lands in the centre | Resolve removal | Exactly the centre remains occupied and the puzzle succeeds | Exact target configuration | `PEG-006`, `PEG-007` |

## Strategic and experiential structure

- Local decision: select which of the few current vacancies will be filled and
  which adjacent peg will disappear, recognising that both emptied holes alter
  later jump access.
- Medium-term planning: preserve pairs that can feed pegs inward and avoid
  isolating edge-arm material before it has a route back toward the centre.
- Long-term structure: construct a 31-edge path through a finite directed
  acyclic state graph from the central vacancy to its exact complement.
- Common heuristic: work outer pegs inward and reserve the centre region for
  the final sequence; this is strategy, not a legality rule.
- Failure attribution: every state is visible and deterministic, but a legal
  move may create an objective deadlock whose proof is non-local.
- Player-trust factor: the intervening peg and only that peg must disappear on
  every accepted jump.
- Claim IDs: `PEG-001`–`PEG-012`.

## Replay and variation

- What changes: only the player's chosen jump sequence in this fixed problem.
- What remains stable: board, start, exact target, legal triples and one-peg
  decrement.
- Randomness: none.
- Multiple viable strategies: many distinct jump sequences solve the central
  game, and symmetry can map solutions to equivalent rotations or reflections.
- Typical replay motive: find a first solution, avoid known dead positions or
  produce a different or more memorable sequence.
- Claim IDs: `PEG-001`, `PEG-006`–`PEG-011`.

## Adjacent systems and history

- Sokoban also exposes deterministic non-local deadlocks, but its crates are
  preserved and displaced through agent access geometry. Peg Solitaire directly
  relocates a peg and irreversibly deletes the jumped neighbour.
- Rubik's Cube has a fixed visible state space and an exact target, but every
  face turn is reversible and component count is invariant. Peg Solitaire's
  directed state graph is acyclic because material strictly decreases.
- Chess uses selected-piece relocation and capture, but captures normally
  remove a piece on the destination and occur within alternating adversarial
  play. Peg Solitaire removes the intervening piece in a one-player puzzle.
- French, triangular, diagonal and reversible variants change topology,
  movement directions or monotonicity and are not silently treated as
  parameters of this central-game genome.
- Claim IDs: `PEG-001`–`PEG-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-014` | source and destination input method |
| System Behaviour | `SYS-033` | one intervening removal per jump |
| Constraint | `CON-001`, `CON-013`, `CON-053`, `CON-054`, `CON-055` | 33-hole cross, orthogonal directions and exact decrement |
| Information | `INF-001` | simultaneous physical visibility |
| Objective | `OBJ-004` | centre-complement target |
| Time | `TIM-001` | one jump per completed resolution |

Canonical signature:

`ACT-014; SYS-033; CON-001,CON-013,CON-053,CON-054,CON-055; INF-001; OBJ-004; TIM-001`

## Corpus comparison

- Indexed games scanned: `GAME-0001`–`GAME-0018`.
- Indexed combinations scanned: `COMB-0001`–`COMB-0018`.
- Exact genome matches: none.
- Existing combination subsets: none.
- Jaccard scores against complete genomes:
  - `GAME-0001`: shared `CON-001`, `INF-001`, `TIM-001`; `3 / 21 = 0.142857`.
  - `GAME-0002`: shared `CON-001`, `INF-001`, `OBJ-004`; `3 / 14 = 0.214286`.
  - `GAME-0003`: shared `CON-001`, `TIM-001`; `2 / 17 = 0.117647`.
  - `GAME-0004`: shared `CON-001`, `INF-001`; `2 / 23 = 0.086957`.
  - `GAME-0005`: shared `CON-001`, `INF-001`; `2 / 15 = 0.133333`.
  - `GAME-0006`: shared `CON-001`, `CON-013`, `INF-001`, `OBJ-004`; `4 / 15 = 0.266667`.
  - `GAME-0007`: shared `INF-001`, `OBJ-004`; `2 / 16 = 0.125000`.
  - `GAME-0008`: shared `CON-001`, `INF-001`; `2 / 15 = 0.133333`.
  - `GAME-0009`: shared `CON-001`, `INF-001`, `TIM-001`; `3 / 23 = 0.130435`.
  - `GAME-0010`: shared `CON-001`, `INF-001`, `TIM-001`; `3 / 16 = 0.187500`.
  - `GAME-0011`: shared `ACT-014`, `CON-001`, `INF-001`; `3 / 20 = 0.150000`.
  - `GAME-0012`: shared `CON-001`, `INF-001`; `2 / 17 = 0.117647`.
  - `GAME-0013`: shared `CON-001`, `INF-001`, `TIM-001`; `3 / 20 = 0.150000`.
  - `GAME-0014`: shared `ACT-014`, `CON-001`, `INF-001`; `3 / 22 = 0.136364`.
  - `GAME-0015`: shared `CON-001`, `INF-001`, `TIM-001`; `3 / 21 = 0.142857`.
  - `GAME-0016`: shared `CON-001`, `INF-001`; `2 / 23 = 0.086957`.
  - `GAME-0017`: shared `TIM-001`; `1 / 22 = 0.045455`.
  - `GAME-0018`: shared `INF-001`; `1 / 28 = 0.035714`.
- Mathematically selected near match: `GAME-0006` — Sokoban at
  `4 / 15 = 0.266667`.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0006` — Sokoban | `CON-001`, `CON-013`, `INF-001`, `OBJ-004` | Sokoban navigates an agent to push preserved crates on goals and has no automatic resolution; Peg Solitaire directly jumps a peg, automatically removes the middle occupant and strictly decreases material | Near match only |

- New genes: `SYS-033`, `CON-053`, `CON-054`, `CON-055`.
- Classification result: `New gene` and a new verified combination.
- Evidence and reasoning: the existing relocation Action covers the command,
  while the intervening capture, local triple predicate, forward-only material
  loss and no-jump termination require independent bounded records.
- Scan date: 2026-08-11.

## Taxonomy impact

- Registry changes: four new bounded IDs; `ACT-014`, `CON-001`, `CON-013`,
  `INF-001`, `OBJ-004` and `TIM-001` gain a Peg Solitaire example.
- Taxonomy-change record: none. No prior classification changed.
- Candidate terms affected: intervening capture, jump occupancy, monotonic
  reduction and terminal jump exhaustion are promoted to stable IDs.

## Negative results

- No structured negative-result file was required. `CON-005` was explicitly
  rejected because forward jumps cannot restore captured pegs; `ACT-009` and
  `ACT-018` were rejected because the jumped peg is removed rather than pushed;
  `TIM-002` was rejected because automatic middle removal completes each
  command before the next decision.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] One jump maps the local occupancy triple
  `110 → 001`, removing exactly the intervening peg (`PEG-002`–`PEG-005`).
- [Confirmed | Corroborated | High] Legal jumps can enter non-terminal states
  from which the exact centre target is unreachable (`PEG-010`).

## Нові гени

- [Observation | Direct / Corroborated | High] Added `SYS-033`, `CON-053`,
  `CON-054` and `CON-055`.

## Нові комбінації

- [Observation | Direct / Corroborated | High] `COMB-0019` captures visible
  discrete jump-and-remove reduction toward an exact complementary occupancy.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає.

## Нові питання

- Will another capture puzzle reuse intervening removal while allowing reverse
  material growth, separating `SYS-033` from `CON-054` empirically?
- Should multi-jump-as-one-move variants receive a distinct Time boundary when
  they enter the corpus?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] `GAME-0020` — Dorfromantik, standard scored
  Classic mode.
- Optimisation criterion: return from a fixed deterministic reduction puzzle
  to stochastic constructive placement before the 20-game checkpoint.
- Expected information gain: test rotatable hex-tile placement, local edge
  matching, connected landscape groups, finite stack extension and quests.
- Backlog impact: Dorfromantik leaves the pool; new candidates should be
  selected by the checkpoint after `GAME-0020`.

## Чому саме вона

- [Hypothesis | Limited | High] Dorfromantik should contrast Peg Solitaire's
  shrinking fixed board with an expanding landscape whose score and continued
  action supply depend on placement quality.
