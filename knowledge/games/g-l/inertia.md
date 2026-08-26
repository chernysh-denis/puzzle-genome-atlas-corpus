---
game_id: GAME-0070
slug: inertia
game_title: Inertia
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0070
gene_ids:
  action:
    - ACT-078
  system:
    - SYS-037
    - SYS-110
  constraint:
    - CON-001
    - CON-113
  information:
    - INF-001
  objective:
    - OBJ-007
  time:
    - TIM-001
---

# Game: Inertia

## Analysis scope

- Version / ruleset: Simon Tatham's Portable Puzzle Collection, current
  standard desktop `10 × 8` Inertia board, game ID
  `10x8:sggsbgsgsgmggwwmbbmmswggsmwwwsbbwgmsbwgmswwbbbbwSmgsmwbwgsgwmsssmmmgbwgsbbmsmbwm`,
  from its initial state until every gem is collected or the ball hits a mine.
- Included: one designated green ball; eight-direction launch input; forced
  straight-line motion; walls and field edges; stop squares; transit through
  blank and gem cells; contact collection; visible mines; fatal contact;
  all-gem completion; complete visible state and one resolved move at a time.
- Excluded: Solve and hint arrows; Space auto-follow; Undo, Redo, Restart,
  death counter and save history as interface recovery; random generation as a
  decision-time mechanic; alternative dimensions, ports and presentation.
- Direct-play status: the current official JavaScript implementation was opened
  and its displayed `10 × 8` game ID captured. The 80-cell description and
  transition order were reproduced from the current MIT-licensed source. A
  local breadth-first search verified a 24-launch safe route that collects all
  16 gems and separately exercised blocked and fatal inputs.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `INE-001` | The standard desktop board is `10 × 8`, and the fixed control contains one start plus 16 each of gems, mines, stops and walls | Confirmed | Direct | High | P1, P2, local control |
| `INE-002` | The player launches one ball in any of eight orthogonal or diagonal directions | Confirmed | Direct | High | P1, P2 |
| `INE-003` | The ball retains that heading until it enters a stop or the next cell is a wall or board edge | Confirmed | Direct | High | P1, P2, local control |
| `INE-004` | Passing through a gem collects it without stopping the ball | Confirmed | Direct | High | P1, P2, local control |
| `INE-005` | Entering a mine is fatal, and death takes precedence even if the final gem was acquired earlier in that move | Confirmed | Direct | High | P1, P2 |
| `INE-006` | The control board has a safe 24-launch solution `044506054661700142572222` that collects all 16 gems | Observation | Direct | High | P1, P2, local exhaustive control |
| `INE-007` | Inertia adds player-launched forced travel and visible-trajectory fatality while reusing contact collection and visible target clearing | Observation | Corroborated | High | `INE-001`–`INE-006` |

## Basic data

- Release / origin: Ben Olmstead created the original Windows game and released
  its source on request; Simon Tatham reimplemented it for the Portable Puzzle
  Collection.
- Platform or physical form: open-source desktop and official JavaScript
  single-player grid puzzle.
- Puzzle family: direction-launched inertial collection routing.
- Primary sources:
  - **[P1] Simon Tatham:** [official Inertia manual](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/doc/inertia.html).
    It directly specifies eight-direction input, continued travel, stops,
    walls, transit collection, mines and death-over-victory precedence.
  - **[P2] Simon Tatham:** [current `inertia.c` implementation](https://git.tartarus.org/?p=simon/puzzles.git;a=blob;f=inertia.c;hb=HEAD).
    The MIT-licensed source fixes desktop defaults at `10 × 8`, defines the
    five cell classes, serialises game IDs and exposes exact move resolution.
  - **[P3] Simon Tatham:** [official playable JavaScript version](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/inertia.html).
    It produced the fixed descriptive game ID used by this record.
- Secondary sources: none required for the bounded transition claims.
- Reproducible artefact: `scripts/verify_inertia_control.py` parses the exact
  80-cell description, implements the source transition order and proves the
  recorded shortest route by breadth-first search over position and gem mask.
- Claim IDs: `INE-001`–`INE-007`.

## Mechanical decomposition

### Action Genes

- `ACT-078` — launch designated slider in chosen direction. Input chooses one
  of eight headings from the ball's current stationary cell; it does not name
  a landing square or permit steering after commitment.
- `ACT-001` does not apply: only the designated ball moves, not every movable
  field element.
- Claim IDs: `INE-002`, `INE-007`.

### System Behaviour Genes

- `SYS-110` — straight-line travel until declared stop condition. The system
  advances the ball cell by cell on the chosen heading. It settles upon
  entering a stop, or in its current cell when the following cell is a wall or
  beyond the board.
- `SYS-037` — contact-triggered collectible acquisition. Each traversed gem is
  removed and credited, but it does not interrupt the current slide.
- Resolution order per traversed cell is enter, collect gem if present, test
  mine, then test stop or forward wall. That order makes the manual's
  final-gem-then-mine edge case deterministic.
- Claim IDs: `INE-003`–`INE-005`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. The same `10 × 8` cell topology,
  walls, stops and mines persist; only ball position and remaining gems change.
- `CON-113` — visible trajectory hazard contact is terminal. Every mine is
  visible before launch, but entering one anywhere along committed travel
  kills the ball and wins no priority race against the final-gem objective.
- A direction whose immediately adjacent cell is a wall or outside the field
  is rejected without changing state.
- Claim IDs: `INE-001`, `INE-003`, `INE-005`.

### Information Genes

- `INF-001` — fully visible current state. Ball, uncollected gems, walls, stops
  and mines are all displayed. No concealed content or random in-move outcome
  changes a committed path.
- Hint arrows are excluded; complete visibility does not reveal a safe global
  route automatically.
- Claim IDs: `INE-001`–`INE-005`.

### Objective Genes

- `OBJ-007` — clear declared board-element targets. Every visible gem is a
  mandatory target and contact removes it from the active board. The bounded
  puzzle succeeds when the count reaches zero without terminal mine contact.
- No exit or prescribed final ball position remains after the last safe gem.
- Claim IDs: `INE-004`–`INE-006`.

### Time Genes

- `TIM-001` — discrete turn with automatic resolution. One directional input
  commits the complete slide, all transit collection and terminal checks before
  the next direction is accepted.
- Animation speed does not create real-time steering or a response deadline.
- Claim IDs: `INE-002`–`INE-005`.

## Reproducible transitions

Coordinates use rows `A`–`H` and columns `1`–`10`. Direction digits match the
source: `0` north, then clockwise through `7` north-west.

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Initial ball at `E9`, 16 gems | `0` north | enter gem `D9`, collect it and stop there because `D9` is a stop | collection precedes stop and a gem does not prevent credit | `INE-003`, `INE-004` |
| Initial ball at `E9` | `1` north-east | enter visible mine `D10` and die | hazards are evaluated anywhere on the committed line | `INE-005` |
| Initial ball at `E9` | `7` north-west | input rejected because adjacent `D8` is a wall | blocked direction does not launch or change state | `INE-003` |
| Fixed control | `044506054661700142572222` | all 16 gems are removed safely in 24 resolved launches, finishing at `A10` | one exact complete safe route | `INE-006` |
| Hypothetical move that collects the final gem and later enters a mine | commit its heading | gem count reaches zero, then mine contact marks death before victory | terminal precedence is not inferred from count alone | `INE-005` |

The verifier confirms the exact cell histogram, executes the stated route,
reconstructs it as the first shortest route under source direction order and
asserts the three local edge cases.

## Strategic and experiential structure

- Local decision: project one of eight complete rays from the current stop,
  including transit gems, the first stop condition and every mine before it.
- Medium-term planning: choose stopping positions that expose useful future
  headings rather than greedily crossing the nearest gem.
- Long-term structure: cover all required gems through a tour of reachable stop
  states while preserving at least one safe continuation to the remainder.
- Common heuristics: work backward from hard-to-approach gems, use stops as
  routing nodes and treat walls as useful brakes rather than only obstacles.
- Failure attribution: a mine is visible, so death follows from an overlooked
  ray or from assuming collection stops motion; the system contributes no
  hidden chance after launch.
- Player-trust factors: diagonal gaps must not inherit orthogonal collision,
  every gem on a ray must be collected once, and stop / mine precedence must
  follow the documented order.
- Claim IDs: `INE-002`–`INE-006`.

## Replay and variation

- What changes between sessions: generated arrangements of blanks, gems,
  mines, stops, walls and the start, within the selected dimensions.
- Randomness or procedural generation: setup-only. The fixed descriptive ID
  makes the entire bounded attempt deterministic.
- Multiple viable strategies: different safe stop tours may collect the same
  gems; the verifier establishes one shortest route under its state model, not
  a claim that the implementation advertises optimality.
- Typical replay motive: solve another visible routing graph or reduce the
  number and total distance of launches.
- Claim IDs: `INE-001`, `INE-006`.

## Adjacent systems and history

- Golf Peaks is the nearest expected structural neighbour: both commit one
  direct command and let a designated ball finish staged travel before the next
  input. Golf Peaks consumes finite movement cards and follows heightfield
  stages toward a hole; Inertia freely chooses a direction, moves until a stop
  condition and clears distributed gems.
- 2048 and Threes also start from direction input, but they move a whole field
  and resolve merges plus spawning. Inertia moves only one persistent body and
  never changes heading during a launch.
- Snakebird reuses contact collection and visible clearing, but each input
  directly advances the head one cell before body and gravity resolution; its
  final fruit activates a separate exit.
- Minesweeper's mine is concealed until selected and therefore instantiates
  `CON-006`. Inertia's mine is fully visible and may be crossed part-way through
  a longer committed trajectory, which supports the distinct `CON-113`.
- Claim IDs: `INE-003`–`INE-007`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-078` | eight headings from one stationary ball |
| System Behaviour | `SYS-037`, `SYS-110` | transit collection; stop / forward-wall termination |
| Constraint | `CON-001`, `CON-113` | fixed 80 cells; visible fatal mines |
| Information | `INF-001` | complete visible field |
| Objective | `OBJ-007` | clear all 16 gems |
| Time | `TIM-001` | full slide resolves between inputs |

Canonical signature:

`ACT-078; SYS-037,SYS-110; CON-001,CON-113; INF-001; OBJ-007; TIM-001`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `69` (`GAME-0001`–`GAME-0069`).
- Exact genome matches: none.
- Tied near matches: `GAME-0045` — Snakebird (`5 / 17 = 0.294118`).
- Supported combination subsets: `COMB-0070`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0045` — Snakebird | `SYS-037`, `CON-001`, `INF-001`, `OBJ-007`, `TIM-001` | Snakebird accepts one-cell head steps, grows a retained body, applies gravity and requires a later exit; Inertia commits full straight trajectories for one ball and has visible fatal mines | Near, `0.294118` |

### Preserved research notes

- New genes: `ACT-078`, `SYS-110`, `CON-113`.
- Classification result: `New gene` and new verified combination.
- Evidence and reasoning: the complete official rule packet requires a
  player-launched single body, forced travel termination and visible in-path
  terminal hazards not jointly represented by any prior genome.

## Taxonomy impact

- Registry changes: add `ACT-078`, `SYS-110` and `CON-113`; reuse `SYS-037`,
  `CON-001`, `INF-001`, `OBJ-007` and `TIM-001` without changing boundaries.
- Taxonomy-change record: none. No prior classification is rewritten.
- Candidate terms affected: directional inertial launch, straight-line travel
  until stop and visible trajectory hazard contact are promoted to stable IDs.

## Negative results

- Rejected `ACT-001`: the direction does not translate every movable element.
- Rejected `CON-006`: Inertia mines are visible and contacted during committed
  motion rather than exposed from concealment.
- Rejected a new collection objective: `OBJ-007` already covers removing every
  declared visible gem target, while `SYS-037` owns contact acquisition.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Стандартна десктопна дошка `10 × 8` має по 16
  самоцвітів, мін, стопів і стін; точний ID відтворює її без випадковості
  (`INE-001`).
- [Observation | Direct | High] Маршрут із 24 напрямів безпечно збирає всі 16
  самоцвітів; локальний BFS підтвердив його мінімальну довжину (`INE-006`).

## Нові гени

- [Observation | Direct | High] `ACT-078` — запуск призначеного ковзного тіла
  у вибраному напрямі.
- [Observation | Direct | High] `SYS-110` — прямолінійний рух до оголошеної
  умови зупинки.
- [Observation | Direct | High] `CON-113` — видимий небезпечний контакт на
  траєкторії є кінцевим.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0070` — напрямлений запуск із
  примусовим проходженням, збором цілей і видимою смертельною траєкторією.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає; три нові межі не
  перепризначають жоден попередній ген.

## Нові питання

- Чи повторить майбутня гра `SYS-110` без контакту-збору, щоб відокремити
  інерційне маршрутизування від цільового прибирання?

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] The Room.
- Optimisation criterion: restore mechanical distance after a deterministic
  grid-routing subject and test direct diegetic mechanism manipulation.
- Expected information gain: visible 3D object-state inspection, multi-part
  latches and spatially embedded clue-to-mechanism dependencies.
- Backlog impact: retained from checkpoint 065, pending a precise first-box
  scope packet and primary documentation.

## Чому саме вона

- [Hypothesis | Limited | Medium] The Room should challenge whether current
  spatial transformation and information genes cover direct inspection and
  nested physical mechanisms without inheriting hidden-query or grid-routing
  structures.
