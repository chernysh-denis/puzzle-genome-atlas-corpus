---
game_id: GAME-0016
slug: pipe-mania
game_title: Pipe Mania / Pipe Dream
analysis_status: reviewed
reviewed: 2026-08-11
combination_ids:
  - COMB-0016
gene_ids:
  action:
    - ACT-006
    - ACT-020
  system:
    - SYS-004
    - SYS-024
    - SYS-025
  constraint:
    - CON-001
    - CON-039
    - CON-040
    - CON-041
    - CON-042
  information:
    - INF-001
    - INF-005
  objective:
    - OBJ-002
    - OBJ-012
  time:
    - TIM-003
---

# Game: Pipe Mania / Pipe Dream

## Analysis scope

- Version / ruleset: the classic single-player Pipe Dream core documented in
  the Lucasfilm Games NES instruction manual, corresponding to The Assembly
  Line's Pipe Mania design.
- Included: one ordinary A Game round with the fixed start section, the seven
  basic fixed-orientation pipe pieces, visible five-piece dispenser, placement
  into empty cells, blasting an unfilled ordinary pipe, start delay, real-time
  Flooz propagation, FAST mode, minimum-distance completion and score.
- Excluded: two-player play, B and C modes, the multi-round life / wrench
  economy, obstacles, one-way sections, reservoirs, pumps, tunnels, end pieces,
  late-level speed comparison, ports and later remakes.
- Direct-play status: not conducted for this record. The contemporary manual is
  treated as primary rules evidence and checked against a manual transcription
  and original-platform documentation.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PIP-001` | The round begins on a fixed grid with a start section and a visible ordered dispenser of upcoming pipe pieces | Confirmed | Direct | High | F1, F2 |
| `PIP-002` | The player must place the current bottom dispenser piece in its supplied orientation and cannot choose or rotate a later piece | Confirmed | Direct | High | F1, F2 |
| `PIP-003` | Placing a piece advances the queue and exposes a newly selected tail piece | Confirmed | Direct | High | F1, F2 |
| `PIP-004` | Before Flooz enters an ordinary placed pipe, the player may replace it with the current dispenser piece at a time and score penalty | Confirmed | Direct | High | F1, F2 |
| `PIP-005` | Once Flooz fills a section, that section can no longer be replaced | Confirmed | Direct | High | F1, F2 |
| `PIP-006` | After a real-time delay Flooz leaves the start and continues through reciprocally connected pipe ports | Confirmed | Direct | High | F1, F2, F3 |
| `PIP-007` | The player may continue placing pieces while Flooz advances and may deliberately accelerate the flow in FAST mode | Confirmed | Direct | High | F1, F2 |
| `PIP-008` | The round terminates when Flooz reaches an open, incompatible or boundary-facing pipe end | Confirmed | Direct | High | F1, F3 |
| `PIP-009` | Success requires Flooz to traverse at least the displayed minimum number of pipe sections before termination | Confirmed | Direct | High | F1, F2 |
| `PIP-010` | Traversed pieces award score while replacement and unused-piece rules can impose penalties | Confirmed | Direct | High | F1, F2 |
| `PIP-011` | The exact visible queue supports planning, while pieces beyond its horizon remain unresolved | Observation | Corroborated | High | PIP-001–PIP-003 |
| `PIP-012` | Continuous flow changes placement legality over time, distinguishing Pipe Dream from static path construction | Observation | Corroborated | High | PIP-004–PIP-009 |

## Basic data

- Origin: Pipe Mania was developed by The Assembly Line and first released in
  1989; Lucasfilm Games distributed ports under the Pipe Dream title.
- Platform scope: NES rules are used because the contemporary manual is fully
  inspectable. Platform-specific control details remain parameters.
- Puzzle family: queued tile placement under delayed real-time flow pressure.
- Sources:
  - **[F1]** [Pipe Dream NES instruction manual](https://www.digitpress.com/library/manuals/nes/Pipe%20Dream.pdf),
    Lucasfilm Games. Primary evidence for dispenser, placement, blasting,
    timing, Flooz, distance, score and modes.
  - **[F2]** [World of Nintendo manual transcription](https://www.world-of-nintendo.com/manuals/nes/pipe_dream.shtml),
    searchable corroboration of the same instruction booklet.
  - **[F3]** [Pipe Mania Amiga manual](https://www.lemonamiga.com/doc/pipe-mania/1222),
    original-title documentation corroborating start, flow, connection and
    termination rules while exposing port differences as version parameters.
  - **[F4]** [Pipe Mania historical summary](https://lucasfilm.fandom.com/wiki/Pipe_Mania),
    secondary release and title context.
- Claim IDs: `PIP-001`–`PIP-012`.

## Mechanical decomposition

### Action Genes

- `ACT-020` — place queue-head tile at selected board position. The player
  chooses the cell, but the dispenser fixes which pipe and orientation must be
  placed. Selecting an unfilled ordinary pipe blasts and replaces it through
  the same action boundary.
- `ACT-006` — accelerate automatic progression. FAST mode increases the Flooz
  rate and changes its score multiplier without selecting a different route.
- Rotation is absent. The seven basic orientations are separate queued element
  identities, not player transformations.
- Claim IDs: `PIP-002`, `PIP-004`, `PIP-007`.

### System Behaviour Genes

- `SYS-004` — random outcome selection. The system supplies the pipe sequence;
  exact distribution is a parameter outside the player command.
- `SYS-024` — visible supplied-sequence advance. Each placement consumes the
  bottom piece, shifts the remaining preview and appends a newly selected pipe.
- `SYS-025` — time-driven directed flow propagation. After the countdown,
  Flooz repeatedly fills a section and advances through reciprocal ports until
  no continuation exists.
- Filling, score credit and queue movement are automatic consequences rather
  than additional placement actions.
- Claim IDs: `PIP-003`, `PIP-006`–`PIP-010`.

### Constraint Genes

- `CON-001` — fixed occupancy capacity. One persistent addressed grid bounds
  all ordinary placed pipe positions.
- `CON-039` — forced queue-head orientation. The current bottom dispenser
  piece must be used as shown; later pieces and rotations are unavailable.
- `CON-040` — port-compatible flow continuation. Neighbouring pipes conduct
  only when exit and entry ports reciprocate; basic crossovers preserve their
  two straight channels rather than branching.
- `CON-041` — flow-locked placed tile. An ordinary unfilled section may be
  replaced, but a section already reached by Flooz is immutable.
- `CON-042` — open-end flow termination. Vacant, incompatible or out-of-board
  continuation ends the round.
- `CON-029` and `CON-030` are absent. The route is not required to be a simple
  player-traced path, and crossover tiles may carry two channels through one
  cell.
- Claim IDs: `PIP-001`, `PIP-002`, `PIP-004`–`PIP-009`.

### Information Genes

- `INF-001` — fully visible current state. Current pipes, fill state, start,
  distance, timer and dispenser are public.
- `INF-005` — exact ordered successor preview. The dispenser exposes the exact
  identities and order of five upcoming fixed-orientation pipes.
- Pieces beyond the visible queue are outside the preview horizon, so
  `INF-002` is not simultaneously assigned; this follows the same boundary as
  Tetris's one-piece preview.
- Claim IDs: `PIP-001`, `PIP-003`, `PIP-011`.

### Objective Genes

- `OBJ-012` — sustain flow through minimum connected distance. The round
  succeeds only after the DIST counter reaches zero through filled sections.
- `OBJ-002` — maximise accumulated score. Traversed pipes and optional FAST
  scoring reward extension beyond the minimum, while replacement and unused
  sections can reduce the result.
- Reaching the distance threshold does not immediately stop Flooz; it secures
  advancement when the current pipeline eventually terminates.
- Claim IDs: `PIP-009`, `PIP-010`.

### Time Genes

- `TIM-003` — real-time input during forced progression. A countdown provides
  initial construction time, after which the player continues placing and
  replacing while Flooz advances independently.
- This differs from Flow Free's `TIM-002`: the board can become irreversibly
  filled while the player is still deciding. It shares Tetris's real-time
  forced-progression structure without sharing gravity or a controllable active
  piece.
- Claim IDs: `PIP-006`, `PIP-007`, `PIP-012`.

## Reproducible transitions

| Before | Player action or elapsed event | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Bottom dispenser piece is a fixed elbow | Select an empty cell | Elbow is placed unchanged; queue advances and refills | Cell choice is player-owned; identity and orientation are forced | `PIP-002`, `PIP-003` |
| An ordinary pipe is placed but unfilled | Place the queue-head pipe over it | Old pipe is blasted; replacement appears after the declared delay and penalty | Replacement is legal only before flow | `PIP-004` |
| Flooz has entered a placed pipe | Attempt replacement | Action is unavailable | Flow creates an expanding immutable prefix | `PIP-005` |
| Countdown reaches zero | No player command | Flooz begins at the fixed start and fills the connected next section | Flow is system-driven real-time state | `PIP-006` |
| Current exit faces a neighbour with no reciprocal port | Allow fill to reach the exit | Flow cannot continue and the round ends | Visual adjacency is insufficient | `PIP-008` |
| DIST counter is still positive when the route ends | Resolve termination | Round is unsuccessful | Minimum traversal is the completion objective | `PIP-009` |
| DIST counter reached zero before the route ends | Resolve later termination | Round is successful and its score is evaluated | Threshold success can precede terminal flow | `PIP-009`, `PIP-010` |

## Strategic and experiential structure

- Local decision: place the forced orientation where it extends the current
  frontier, prepares a later connection or safely stores an awkward piece.
- Medium-term planning: use the exact queue to reserve cells for upcoming
  corners and straights, while preserving access to the active flow front.
- Long-term structure: exceed the minimum distance by constructing loops and
  detours without allowing the real-time frontier to catch an unfinished gap.
- Scarce resources: unfilled cells near the frontier, replaceable time and
  queue flexibility. A speculative section becomes irreversible once filled.
- Failure attribution: random queue order constrains options, but the exact
  visible horizon and deterministic port rule make immediate leaks traceable.
- Claim IDs: `PIP-001`–`PIP-012`.

## Replay and variation

- What changes: queued pipe order, start placement between rounds, player
  layout and the point at which real-time pressure overtakes construction.
- What remains stable: forced queue order, fixed orientations, reciprocal port
  rule, fill locking and minimum-distance evaluation.
- Randomness: successor pipe selection feeds the visible queue. The player
  plans exactly within the displayed horizon and contingently beyond it.
- Typical replay motive: reach later rounds, improve score and build longer or
  more looped routes under faster flow.
- Claim IDs: `PIP-001`, `PIP-003`, `PIP-006`, `PIP-009`, `PIP-010`.

## Adjacent systems and history

- Flow Free constructs several paired disjoint paths in self-paced play and
  requires full-board coverage. Pipe Dream constructs one system-traversed
  route from a source, permits unused pieces and introduces real-time failure.
- Tetris shares random exact-preview successors, acceleration and input during
  forced progression. It controls the pose of one falling active piece, while
  Pipe Dream chooses cells for a forced queue-head piece and later locks them
  through flow.
- Later Pipe Mania variants add end pieces, obstacles, directional pipes,
  reservoirs, pumps and different success rules; they require a broader scope
  or separate parameter review.
- Claim IDs: `PIP-001`–`PIP-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-006`, `ACT-020` | cell input, replacement delay and FAST trigger |
| System Behaviour | `SYS-004`, `SYS-024`, `SYS-025` | queue generator and Flooz speed |
| Constraint | `CON-001`, `CON-039`, `CON-040`, `CON-041`, `CON-042` | grid size, pipe port set and replacement penalty |
| Information | `INF-001`, `INF-005` | queue depth and display order |
| Objective | `OBJ-002`, `OBJ-012` | minimum distance and score table |
| Time | `TIM-003` | start delay, propagation rate and pause |

Canonical signature:

`ACT-006,ACT-020; SYS-004,SYS-024,SYS-025; CON-001,CON-039,CON-040,CON-041,CON-042; INF-001,INF-005; OBJ-002,OBJ-012; TIM-003`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `15` (`GAME-0001`–`GAME-0015`).
- Exact genome matches: none.
- Tied near matches: `GAME-0004` — Tetris (`7 / 23 = 0.304348`).
- Supported combination subsets: `COMB-0016`.
- Scan date: 2026-08-11.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0004`.

### Preserved research notes

- Result: no exact signature or existing combination match. Similarity is a
  scheduling and preview relation, not a claim of genre identity or novelty.

## Combination record

- Registered [`COMB-0016`](../../combinations/COMB-0016.md), a proper
  ten-gene subset centred on forced preview-queue construction ahead of a live
  directed flow.
- Fixed capacity, acceleration, score and open-end termination remain in the
  complete genome but are not all required to identify the core interaction.

## Taxonomy impact

- Seven existing genes are reused and eight bounded genes are added.
- The definition of `INF-005` is clarified to cover an exact ordered preview
  horizon of one or more successors; no taxonomy-change record is needed.

## Negative results

- `ACT-002` is absent because supplied pipes cannot be rotated. `ACT-016` is
  absent because the player places discrete tiles rather than tracing a path.
- `CON-029`, `CON-030` and `OBJ-006` are absent because crossings, unused cells
  and one source-driven route violate Flow Free's simple full-cover model.
- `INF-002` is absent: unresolved pieces beyond an exact preview horizon do not
  contradict `INF-005`, following the existing Tetris boundary.
- Queue depth is retained as an `INF-005` parameter. Its definition was
  clarified from a one-element preview to an exact ordered preview of one or
  more successors; Tetris and Pipe Dream signatures remain valid.
- No taxonomy change is required. Placement, automatic queue and flow,
  connectivity, information, objectives and real-time scheduling remain
  separable within the six types.

## Research notes

- Strongest finding: the active flow converts spatial history into an expanding
  immutable prefix while the player continues building its future. This is not
  captured by connectivity alone.
- Registry consequence: seven genes are reused and eight bounded genes are
  admitted. `ACT-006`, `INF-005` and `TIM-003` gain a second supporting game.
- Next selection should test either persistent-network demand or hand / deck
  information without immediately adding another path puzzle.
