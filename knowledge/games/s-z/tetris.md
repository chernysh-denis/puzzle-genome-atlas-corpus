---
game_id: GAME-0004
slug: tetris
game_title: Tetris
analysis_status: reviewed
reviewed: 2026-08-11
combination_ids:
  - COMB-0004
gene_ids:
  action:
    - ACT-005
    - ACT-006
  system:
    - SYS-004
    - SYS-006
    - SYS-007
    - SYS-008
    - SYS-009
  constraint:
    - CON-001
    - CON-007
    - CON-008
  information:
    - INF-001
    - INF-005
  objective:
    - OBJ-002
    - OBJ-003
  time:
    - TIM-003
---

# Game: Tetris

## Analysis scope

- Version / ruleset: Nintendo's 1989 North American NES Tetris, single-player
  A-Type, NTSC, starting at level 0 with the `NEXT` display enabled.
- Included: the 10 × 20 visible playfield, seven tetrominoes, lateral movement,
  clockwise and counter-clockwise rotation, soft drop, automatic gravity,
  blocked-descent locking, line removal, collapse, score, level-speed increase,
  one-piece preview and top-out.
- Excluded: B-Type, PAL timing, unfinished two-player code, pause-assisted input,
  high-level arithmetic defects and crashes, Game Boy rules, modern hold, hard
  drop, ghost piece, multi-piece queue, seven-bag generator, lock delay, wall
  kicks and Super Rotation System.
- Direct-play status: not conducted. The scoped rules were triangulated from
  Nintendo's contemporary manual, the official Tetris description, a
  ROM-oriented technical analysis and peer-reviewed models. Implementation
  edge cases outside ordinary intended play remain excluded unless they define
  the top-out boundary.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TET-001` | A-Type repeatedly introduces one of seven falling tetrominoes that the player may move and rotate | Confirmed | Corroborated | High | P1, P2, P3 |
| `TET-002` | Gravity changes the active piece without input, while lateral movement and rotation remain player commands | Confirmed | Corroborated | High | P1, P2, T1 |
| `TET-003` | A blocked downward attempt locks the active piece; completed horizontal rows are removed and higher occupancy shifts down | Confirmed | Corroborated | High | P1, T1, A1 |
| `TET-004` | The successor piece is pseudorandomly selected and exactly one successor is shown by the enabled `NEXT` display | Confirmed | Corroborated | High | P1, T1, A2 |
| `TET-005` | A-Type ends when stack occupancy prevents a spawned piece from establishing continued play at the entry region | Confirmed | Corroborated | High | P1, P2, T1 |
| `TET-006` | The six-type model separates player transformation, automatic motion, collision legality and real-time scheduling without a taxonomy change | Observation | Corroborated | Medium | TET-001–TET-005 |
| `TET-007` | Managing height, holes, wells and surface structure supports effective placement decisions | Pattern | Corroborated | Medium | A2, A3 |
| `TET-008` | Tetris combines placement strategy with speed-dependent execution demands | Pattern | Corroborated | Medium | P1, A3, A4 |
| `TET-009` | Pajitnov created the first Tetris in Moscow in 1984; Nintendo published the scoped NES version in 1989 | Confirmed | Corroborated | High | P1, P2, P3 |
| `TET-010` | Complexity results for offline and generalised Tetris do not establish the difficulty of every ordinary NES position | Confirmed | Corroborated | High | A1 |
| `TET-011` | A-Type has no finite completion target; it evaluates score and continued play until top-out | Confirmed | Corroborated | High | P1, P2 |

## Basic data

- Release / origin: Alexey Pajitnov created the first version in Moscow in
  1984. Nintendo's licensed NES version was published in North America in 1989.
- Platform or physical form: Nintendo Entertainment System cartridge using one
  digital controller.
- Puzzle family: stochastic real-time falling-block packing.
- Primary and official sources:
  - **[P1] Nintendo manual scan:** [*Tetris Instruction Booklet*](https://www.gamingalexandria.com/highquality/NES/Tetris/Tetris%20-%20Manual.pdf),
    Nintendo of America, 1989. It documents the two modes, controls, speed,
    preview, line clear, score and game-over rules.
  - **[P2] Official rules summary:** The Tetris Company,
    [“About Tetris”](https://tetris.com/about), describing movement, rotation,
    falling pieces, line completion, increasing speed and skyline failure.
  - **[P3] Official history:** The Tetris Company,
    [“The History of Tetris”](https://tetris.com/news/the-history-of-tetris),
    recording Pajitnov's 1984 Electronika 60 version and later releases.
- Technical source:
  - **[T1] ROM-oriented analysis:** negative-seven,
    [“Nintendo NES Tetris bugs and mechanics explained”](https://negative-seven.github.io/tetris_explained/),
    documenting frame-driven logic, exact top-out, piece selection, soft drop
    and line-shift behaviour. This is an independent reverse-engineering
    account, not Nintendo documentation.
- Academic sources:
  - **[A1]** Erik D. Demaine, Susan Hohenberger and David Liben-Nowell,
    [“Tetris is Hard, Even to Approximate”](https://arxiv.org/abs/cs/0210020),
    defining an offline generalisation and proving bounded complexity results.
  - **[A2]** Özgür Şimşek, Simón Algorta and Amit Kothiyal,
    [“Why Most Decisions Are Easy in Tetris”](https://proceedings.mlr.press/v48/simsek16.html),
    ICML 2016, analysing dominance relations and board features in Tetris
    decisions.
  - **[A3]** John K. Lindstedt and Wayne D. Gray,
    [“Distinguishing experts from novices by the Mind's Hand and Mind's Eye”](https://doi.org/10.1016/j.cogpsych.2018.11.003),
    *Cognitive Psychology* 109, 2019.
  - **[A4]** Aaron Isaksen et al.,
    [“Simulating Strategy and Dexterity for Puzzle Games”](https://pixl.cs.princeton.edu/pubs/Isaksen_2017_SSA/index.php),
    IEEE CIG 2017.
- Claim IDs: `TET-001`–`TET-011`.

## Mechanical decomposition

### Action Genes

- `ACT-005` — reposition active falling element. Left and right translate the
  active tetromino; A and B rotate it 90 degrees in opposite directions while
  it remains active.
- `ACT-006` — accelerate automatic progression. Holding down produces a soft
  drop: the same downward process occurs faster and can contribute score.
- Horizontal motion and rotation share one gene because both directly choose a
  collision-valid pose of the same temporary active element during the same
  falling interval. Translation range, rotation states and input repeat remain
  parameters.
- Soft drop is separate because it changes the rate of a system-driven process
  rather than selecting another pose axis. Hard drop is absent.
- Claim IDs: `TET-001`, `TET-002`, `TET-008`.

### System Behaviour Genes

- `SYS-004` — random outcome selection. The system pseudorandomly chooses the
  successor tetromino; the NES selection algorithm is not a modern seven-bag.
- `SYS-006` — time-driven automatic descent. Gravity periodically attempts to
  lower the active tetromino, with a shorter interval at higher levels.
- `SYS-007` — blocked-descent locking. When a scheduled or accelerated downward
  attempt is blocked, the active cells become fixed board occupancy.
- `SYS-008` — completed-line removal and collapse. After lock, filled rows are
  removed and retained blocks above them shift downward before the next piece.
- `SYS-009` — successor active-element introduction. After resolution, the
  previewed successor enters as the new controllable piece and another
  successor is selected.
- `SYS-003` does not apply: introduction follows the active element's lock
  cycle, not every valid player action.
- Resolution order: accept frame inputs and gravity; on blocked descent, lock;
  detect and clear completed lines; update score, line and level state;
  introduce the successor; continue or terminate on the top-out test.
- Claim IDs: `TET-002`–`TET-005`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. Ordinary play uses a finite 10 × 20
  visible field; hidden implementation storage is not additional playable
  capacity.
- `CON-007` — collision-valid active transformation. A translation, rotation or
  descent must keep the complete active footprint out of walls, floor and fixed
  blocks.
- `CON-008` — terminal active-element entry obstruction. Continued accumulation
  can make the spawn region unusable and terminate the attempt.
- Tetromino geometry and the seven-piece set are parameters of active-element
  transformation and random selection, not ten additional genes.
- Scarce strategic resource: accessible low-height empty volume. Enclosed holes
  consume capacity but cannot be filled directly from above without first
  clearing supporting structure.
- Claim IDs: `TET-001`, `TET-005`, `TET-007`.

### Information Genes

- `INF-001` — fully visible current state. The settled occupancy, current piece
  and its visible pose provide the decision-relevant current board.
- `INF-005` — exact ordered successor preview. At depth one, the default `NEXT`
  panel identifies
  one successor. The manual permits turning it off, but this analysis fixes it
  on.
- `INF-002` does not apply: the next incoming random outcome is already shown.
  Later pieces are beyond the one-element preview horizon; preview depth is a
  parameter, not simultaneous presence of contradictory information genes.
- Claim IDs: `TET-004`.

### Objective Genes

- `OBJ-002` — maximise accumulated score. Line clears, especially multi-line
  clears, and qualifying soft drops increase the A-Type score.
- `OBJ-003` — preserve move availability. Keeping the entry region usable
  prolongs the sequence of placement decisions and permits further scoring.
- A-Type has no finite success state. Clearing lines is the principal scoring
  event and the mechanism that restores capacity, rather than a separate
  completion objective in this ruleset.
- Claim IDs: `TET-005`, `TET-011`.

### Time Genes

- `TIM-003` — real-time input during forced progression. Gravity advances the
  active piece while the player may translate, rotate or accelerate it during
  the remaining placement window.
- Increasing level speed changes the duration and execution difficulty but not
  the identity of the time gene.
- Pause temporarily suspends the loop and is treated as a parameter. Inputs
  intentionally timed around pause are excluded from ordinary play.
- Claim IDs: `TET-002`, `TET-006`, `TET-008`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Active tetromino above empty cells | No input until the gravity interval elapses | Piece descends one row | Descent is automatic, not an action | `TET-002` |
| Active tetromino with empty space to its left | Press left | Piece shifts left while gravity scheduling continues | Direct pose control during progression | `TET-002` |
| Active tetromino beside a wall where rotation would overlap it | Press rotate | Rotation is rejected | Complete-footprint collision constraint | `TET-001` |
| Active tetromino resting above occupied cells | Wait for the next downward attempt | Descent fails and the piece locks | Blocked-descent locking | `TET-003` |
| Lock fills one horizontal row | Complete the lock | Row disappears and higher occupancy shifts down | Line removal and collapse | `TET-003` |
| Fixed stack occupies the entry region | Allow the spawned piece to remain obstructed and lock | Attempt ends | Terminal entry obstruction | `TET-005` |
| `NEXT` shows an I tetromino | Lock the current piece without terminating | The shown I becomes active | Preview identifies the exact successor | `TET-004` |

These transitions omit extreme-level bugs and modern rotation corrections. A
rejected move leaves the active pose unchanged but does not pause gravity.

## Strategic and experiential structure

- Local decision: select a reachable orientation and column for the active
  tetromino before the placement window closes.
- Medium-term planning: use the next-piece preview, preserve accessible wells,
  avoid covered holes and keep the surface compatible with several possible
  successors.
- Long-term structure: trade immediate line clears against a stack prepared for
  higher-scoring multi-line clears while keeping total height below the entry
  region.
- Common evaluated features in Tetris research include height, holes, wells,
  row transitions and landing consequences. Their exact weighting is strategy,
  not part of the genome.
- Failure attribution: cavities and high stacks are usually traceable to prior
  placements, but execution failure becomes more important as gravity reduces
  the available input window. Random successor order constrains planning
  without concealing the already previewed next piece.
- Player-trust factors: collision and line-clear rules remain deterministic;
  uncertainty comes from later piece selection. The manual exposes both score
  and next-piece information rather than altering outcomes after placement.
- Claim IDs: `TET-007`, `TET-008`.

The academic results use formalised or instrumented Tetris environments and do
not prove one universal human strategy for the exact NES ruleset. They support
the bounded claims that board features affect placement quality and that
real-time execution is analytically distinct from placement choice.

## Replay and variation

- What changes between sessions: the pseudorandom tetromino sequence and the
  resulting player-created stack.
- Randomness or procedural generation: one successor is selected as each piece
  cycle advances. The scoped generator is history-dependent and biased rather
  than a uniform permutation bag.
- Multiple viable strategies: players may prioritise immediate safety, line
  count, score-efficient multi-line clears or stack surfaces that reduce
  execution risk.
- Typical replay motive: improve score, survive higher speeds and execute
  placements more reliably.
- A-Type has no designed completion state. The run ends through top-out or
  voluntary termination; high-level implementation failures are outside scope.
- Claim IDs: `TET-004`, `TET-007`, `TET-008`, `TET-011`.

## Adjacent systems and history

- Direct origin: Pajitnov's 1984 Electronika 60 design established the falling
  tetromino and completed-line loop; the scoped Nintendo version is a later
  implementation with its own timing, generator and controls.
- Variants: NES B-Type adds a 25-line completion target and random starting
  garbage. Game Boy multiplayer, modern Guideline games, Tetris Effect and
  Tetris 99 alter objectives, information, timing or opponent interaction.
- Similar games: Dr. Mario, Puyo Puyo and Columns use falling active pieces but
  resolve compatibility, gravity and chains differently. They require separate
  decompositions rather than inheriting this genome.
- Complexity caveat: Demaine and colleagues study an offline generalised model
  with a supplied sequence and board. Their hardness results do not establish
  that every fixed NES position or real-time human decision is computationally
  hard.
- Claim IDs: `TET-009`, `TET-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-005`, `ACT-006` | translation directions, rotations, soft-drop rate |
| System Behaviour | `SYS-004`, `SYS-006`, `SYS-007`, `SYS-008`, `SYS-009` | generator, gravity curve, resolution delays |
| Constraint | `CON-001`, `CON-007`, `CON-008` | 10 × 20 field, piece set, collision model |
| Information | `INF-001`, `INF-005` | one-piece preview, `NEXT` toggle fixed on |
| Objective | `OBJ-002`, `OBJ-003` | score table, indefinite survival |
| Time | `TIM-003` | frame rate, repeat timing, level-speed progression |

Canonical signature:

`ACT-005,ACT-006; SYS-004,SYS-006,SYS-007,SYS-008,SYS-009; CON-001,CON-007,CON-008; INF-001,INF-005; OBJ-002,OBJ-003; TIM-003`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `3` (`GAME-0001`–`GAME-0003`).
- Exact genome matches: none.
- Tied near matches: `GAME-0001` — 2048 (`5 / 24 = 0.208333`).
- Supported combination subsets: `COMB-0004`.
- Scan date: 2026-08-11.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0001` — 2048 | `SYS-004`, `CON-001`, `INF-001`, `OBJ-002`, `OBJ-003` | 2048 resolves one global turn before another input; Tetris accepts pose inputs while gravity advances one temporary active piece | Near, `0.208333` |

### Preserved research notes

- New combination: `COMB-0004`, whose eight genes are a proper subset of this
  fifteen-gene genome.
- New genes: `ACT-005`, `ACT-006`, `SYS-006`, `SYS-007`, `SYS-008`,
  `SYS-009`, `CON-007`, `CON-008`, `INF-005`, `TIM-003`.
- Classification result: `New gene`.
- Evidence and reasoning: the new genes separate direct pose control, rate
  control, automatic descent, fixation, line resolution, successor
  introduction, collision legality, top-out, preview and concurrent real-time
  scheduling. Speed values, board dimensions, piece shapes and generator bias
  remain parameters.

## Taxonomy impact

- Registry changes: ten bounded genes added; `SYS-004`, `CON-001`, `INF-001`,
  `OBJ-002` and `OBJ-003` reused.
- Taxonomy-change record: none. Action, automatic behaviour, constraints,
  information, objectives and scheduling remain separable in the scoped loop.
- Candidate terms affected: falling-element repositioning, accelerated
  progression, gravity, locking, line clearing, spawning, placement geometry,
  previewed future information and real-time scheduling now have bounded
  mappings.
- Rotation remains broader candidate vocabulary. `ACT-005` does not replace
  `ACT-002`: rotating a temporary falling element under collision constraints
  is not coupled layer rotation within a persistent permutation puzzle.
- Gravity rate is a parameter of `SYS-006`; the fact that player input remains
  available during gravity is encoded separately by `TIM-003`.
- Line removal and its uniform collapse remain one gene at current resolution.
  Split them only if another analysed system preserves one behaviour without
  the other in a decision-relevant way.
- Claim IDs: `TET-006`.

## Negative results

None. The analysis confirms the planned model test: real-time scheduling can be
represented without adding a seventh gene type or reclassifying earlier genes.
No concrete prior claim, candidate or gene distinction was rejected.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] NES A-Type interleaves direct pose control
  with frame-driven automatic descent and blocked-descent locking (`TET-002`,
  `TET-003`).
- [Confirmed | Corroborated | High] One randomly selected successor is exactly
  previewed while later sequence outcomes remain outside the preview horizon
  (`TET-004`).
- [Pattern | Corroborated | Medium] Placement strategy and execution pressure
  are distinct but interacting contributors to performance (`TET-008`).

## Нові гени

- [Observation | Corroborated | High] `ACT-005`, `ACT-006`, `SYS-006`,
  `SYS-007`, `SYS-008`, `SYS-009`, `CON-007`, `CON-008`, `INF-005` and
  `TIM-003`.
- [Observation | Corroborated | High] `SYS-004`, `CON-001`, `INF-001`,
  `OBJ-002` and `OBJ-003` are reused.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0004` — timed falling-piece
  placement, locking and completed-line collapse.

## Зміни таксономії

- [Observation | Corroborated | Medium] Змін таксономії немає. Tetris supplies
  the first real-time concurrent-input case without requiring a seventh type.

## Нові питання

- TODO: test whether line removal and uniform collapse remain one reusable gene
  in a system where removal does not shift retained occupancy.
- TODO: compare soft drop with a system that permits a true instantaneous hard
  drop before deciding whether both are parameters of rate control.
- TODO: analyse a modern Guideline ruleset separately before classifying hold,
  multi-piece preview, bag generation, lock delay and wall kicks.

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] `GAME-0005` — Sudoku.
- Optimisation criterion: maximise information gain after the first real-time
  system by returning to a self-paced puzzle with global symbolic constraints.
- Expected information gain: test the boundary between fixed hidden state and
  values that are not yet assigned but are logically constrained; test whether
  inscription and reversible candidate notation require distinct Action genes.
- Backlog impact: Sudoku moves from the coverage pool to the immediate task;
  Tetris leaves the pool after completion.

## Чому саме вона

- [Hypothesis | Limited | Medium] Sudoku is mechanically distant from Tetris
  and from Minesweeper's concealed pre-existing hazards. It can reveal whether
  the current Information genes distinguish unknown solution values from hidden
  current contents without forcing uncertainty into the wrong category.
