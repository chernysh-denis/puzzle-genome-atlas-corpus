# Constraint Genes

## CON-001 — Fixed occupancy capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the playable topology exposes a fixed finite set of individually
  addressable positions whose occupancy identities persist throughout play.
- Includes: the 16 cells of the standard 2048 board; the fixed corner and edge
  positions of the standard 3 × 3 Rubik's Cube; the fixed cells of a
  Minesweeper board; the 10 × 20 visible NES Tetris playfield; the 81 cells of
  a standard Sudoku grid; the fixed floor-and-wall layout of a Sokoban level;
  the fixed rectangular cell grid of a Nonogram; the fixed addressed cells of
  a scoped Royal Match level board; the fixed unit slots of a Water Sort tube
  set; the 64 squares of a standard chessboard; the cells of a classic Flow
  Free board; the fixed cells of a scoped Baba Is You level; the tactical grid
  of an Into the Breach battle; the finite arena cells of a Fights in Tight
  Spaces encounter; the 16 cells of the Threes board; the 33
  addressable holes of the traditional English Peg Solitaire board; the four
  persistent top-level panel slots of Gorogoa's two-by-two workspace; the
  persistent island positions of a Bad North battle; the generated-but-fixed
  route and surrounding placement positions of a Loop Hero expedition; the
  authored terrain, goal and command cells of a HUMANITY trial; the fixed
  addressed reactor cells of a SpaceChem waldo program; the fixed gridded dome,
  passengers, homes, entrance and exit of a scoped Cosmic Express puzzle.
- Excludes: a move limit or timer; a board that expands during play; finite
  component count alone; dynamically deep stacks represented by order rather
  than persistent addressed slots, such as FreeCell cascades.
- Parameters: addressed capacity and topology.
- Evidence: [2048 decomposition](../games/0-9/2048.md) and
  [Rubik's Cube decomposition](../games/m-r/rubiks-cube.md), and
  [Minesweeper decomposition](../games/m-r/minesweeper.md), and
  [Tetris decomposition](../games/s-z/tetris.md), and
  [Sudoku decomposition](../games/s-z/sudoku.md), and
  [Sokoban decomposition](../games/s-z/sokoban.md), and
  [Nonogram decomposition](../games/m-r/nonogram.md), and
  [Royal Match decomposition](../games/m-r/royal-match.md), and
  [Water Sort decomposition](../games/s-z/water-sort.md), and
  [Chess decomposition](../games/a-f/chess.md), and
  [Flow Free decomposition](../games/a-f/flow-free.md), and
  [Baba Is You decomposition](../games/a-f/baba-is-you.md), and
  [Into the Breach decomposition](../games/g-l/into-the-breach.md), and
  [Threes decomposition](../games/s-z/threes.md), and
  [Peg Solitaire decomposition](../games/m-r/peg-solitaire.md), and
  [Gorogoa decomposition](../games/g-l/gorogoa.md), and
  [Bad North decomposition](../games/a-f/bad-north.md), and
  [Loop Hero decomposition](../games/g-l/loop-hero.md), and
  [HUMANITY decomposition](../games/g-l/humanity.md), and
  [SpaceChem decomposition](../games/s-z/spacechem.md), and
  [Cosmic Express decomposition](../games/a-f/cosmic-express.md), and
  [Tactical Breach Wizards decomposition](../games/s-z/tactical-breach-wizards.md).
- Novelty: not assessed.

## CON-002 — Declared pairwise merge compatibility

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: two elements may participate in collision-triggered merging only
  when their current values form a pair in the ruleset's declared compatibility
  relation.
- Includes: equal-value pairs such as `2 + 2` and `4 + 4` in 2048; the `1 + 2`
  base pair and equal ranked pairs from `3 + 3` upward in Threes.
- Excludes: adjacency without merging; arbitrary unequal-value addition; a
  player directly selecting two elements and a result.
- Parameters: compatibility relation, including equality-only, complementary
  base pairs and rank thresholds.
- Evidence: [2048 decomposition](../games/0-9/2048.md) and
  [Threes decomposition](../games/s-z/threes.md).
- Novelty: not assessed; this is part of the baseline genome.

## CON-003 — Single merge participation per resolution

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an element created by a merge cannot merge again during the same
  automatic resolution.
- Includes: `[2, 2, 2, 2]` resolving to `[4, 4]`, not `[8]`, in 2048; a newly
  formed Threes card not merging again during the same swipe.
- Excludes: restrictions that apply across multiple turns.
- Evidence: [2048 decomposition](../games/0-9/2048.md) and
  [Threes decomposition](../games/s-z/threes.md).
- Novelty: not assessed; this is part of the baseline genome.

## CON-004 — Invariant-constrained reachability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: legal actions preserve global invariants, so only a proper subset
  of otherwise representable component arrangements is reachable.
- Includes: Rubik's Cube parity agreement, total corner-twist and total
  edge-flip constraints.
- Excludes: capacity alone; a local collision rule; a target that is difficult
  but not structurally unreachable.
- Parameters: component classes, permutation representation, orientation
  coordinates and invariant equations.
- Evidence: [Rubik's Cube decomposition](../games/m-r/rubiks-cube.md).
- Novelty: not assessed.

## CON-005 — Primitive action reversibility

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: every primitive legal state-changing action has a legal inverse
  that restores the immediately preceding state without a random or irreversible
  side effect.
- Includes: a Rubik's Cube face turn followed by the opposite turn.
- Excludes: undo supplied as an interface convenience; a move followed by an
  automatic random spawn; recoverability only through a restart.
- Parameters: inverse notation and primitive-action granularity.
- Evidence: [Rubik's Cube decomposition](../games/m-r/rubiks-cube.md).
- Novelty: not assessed.

## CON-006 — Terminal hazard exposure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: exposing any concealed hazard immediately ends the current
  attempt before the completion objective is met.
- Includes: detonating a mine by revealing its Minesweeper cell.
- Excludes: an incorrect marker by itself; a recoverable damage or lives system;
  random setup that does not expose a hazard.
- Parameters: hazard count, any first-action safety exception and terminal
  feedback.
- Evidence: [Minesweeper decomposition](../games/m-r/minesweeper.md).
- Novelty: not assessed.

## CON-007 — Collision-valid active transformation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a commanded transformation of the active multi-cell element is
  legal only when its complete transformed footprint remains inside the
  permitted field and does not overlap fixed occupancy.
- Includes: rejecting a tetromino translation or rotation through a wall,
  floor or settled block in NES Tetris.
- Excludes: capacity without an active element; global reachability invariants;
  collision that automatically merges compatible elements.
- Parameters: element geometry, field boundary, rotation model and collision
  sampling time.
- Evidence: [Tetris decomposition](../games/s-z/tetris.md).
- Novelty: not assessed.

## CON-008 — Terminal active-element entry obstruction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an attempt ends when required fixed occupancy prevents a newly
  introduced active element from establishing a playable placement in its
  entry region.
- Includes: the NES Tetris top-out condition reached when a spawned piece locks
  while overlapping the existing stack.
- Excludes: exposing a concealed hazard; exhausting a move counter; a high
  stack that still permits the incoming element to continue play.
- Parameters: entry region, overlap test and exact termination timing.
- Evidence: [Tetris decomposition](../games/s-z/tetris.md).
- Novelty: not assessed.

## CON-009 — Immutable given assignments

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: some positions begin with visible assigned values that constrain
  the solution and cannot be changed by the player's assignment action.
- Includes: the printed clue digits in a standard Sudoku puzzle.
- Excludes: player-entered tentative values; concealed values revealed later;
  fixed obstacles that carry no value from the assignment domain.
- Parameters: number, placement and symmetry of the given assignments.
- Evidence: [Sudoku decomposition](../games/s-z/sudoku.md).
- Novelty: not assessed.

## CON-010 — All-different unit coverage

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: every declared unit must contain each symbol in the finite domain
  exactly once, so assigning a symbol excludes it from every other position in
  each unit containing that position.
- Includes: the row, column and 3 × 3 block constraints of standard 9 × 9
  Sudoku.
- Excludes: approximate totals; pairwise inequality without complete domain
  coverage; exact local counts of concealed hazards.
- Parameters: symbol domain, unit size, unit topology and overlap pattern.
- Evidence: [Sudoku decomposition](../games/s-z/sudoku.md).
- Novelty: not assessed.

## CON-011 — Exclusive occupancy with static barriers

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each traversable position may contain at most one occupying
  entity, and declared barrier positions cannot be entered or displaced.
- Includes: Sokoban floor cells occupied by at most the keeper or one crate,
  with walls blocking both; Into the Breach units ending on exclusive cells
  while declared terrain and unit traits constrain traversal; Fights in Tight
  Spaces occupants ending on exclusive arena cells while walls and invalid
  boundaries constrain movement; each local
  Patrick's Parabox grid cell holding at most one occupant with walls fixed;
  Stephen's Sausage Roll player, fork and sausage cells requiring exclusive
  compatible occupancy while grills block some entity classes but support the
  sausage; Snakebird terrain and current body cells blocking head entry while
  every ordered body segment occupies a distinct cell.
- Excludes: finite capacity alone; compatibility-based collision merging;
  invariant restrictions over otherwise representable arrangements.
- Parameters: board topology, barrier geometry and occupying entity classes.
- Evidence: [Sokoban decomposition](../games/s-z/sokoban.md) and
  [Into the Breach decomposition](../games/g-l/into-the-breach.md), and
  [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md), and
  [Patrick's Parabox decomposition](../games/m-r/patricks-parabox.md), and
  [Stephen's Sausage Roll decomposition](../games/s-z/stephens-sausage-roll.md),
  [Snakebird decomposition](../games/s-z/snakebird.md), and
  [Tactical Breach Wizards decomposition](../games/s-z/tactical-breach-wizards.md).
- Novelty: not assessed.

## CON-012 — Push-only access geometry

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a movable object may change position only when the agent can
  occupy the position immediately behind it and the position immediately ahead
  is free; only one object may be displaced and pulling is unavailable.
- Includes: the single-crate push restriction in Sokoban.
- Excludes: direct object selection; pulling from an adjacent cell; pushing a
  chain of two or more objects; automatic gravity.
- Parameters: adjacency topology, object count per push and access direction.
- Evidence: [Sokoban decomposition](../games/s-z/sokoban.md).
- Novelty: not assessed.

## CON-013 — Irrecoverable objective deadlock

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a legal action can reach a non-terminal state from which the
  completion objective is unreachable, even though other legal actions may
  remain available.
- Includes: pushing a Sokoban crate into a non-goal corner from which it cannot
  be pulled or redirected; making a Peg Solitaire jump that leaves a board
  position from which the one-centre-peg target is unreachable even if legal
  jumps remain; stranding a required Patrick's Parabox occupant from its goal
  within the current world state despite remaining walking moves; consuming
  needed snow or stranding a required A Good Snowman Is Hard to Build ball
  while ordinary monster movement remains available; growing or folding a
  Snakebird into a pose from which fruit or exit is unreachable despite other
  legal head moves.
- Excludes: an explicit terminal-loss transition; a reversible setback; a state
  that merely requires more moves than expected.
- Parameters: deadlock pattern, target equivalence and whether the system
  detects the deadlock.
- Evidence: [Sokoban decomposition](../games/s-z/sokoban.md) and
  [Peg Solitaire decomposition](../games/m-r/peg-solitaire.md), and
  [Patrick's Parabox decomposition](../games/m-r/patricks-parabox.md), and
  [A Good Snowman Is Hard to Build decomposition](../games/a-f/a-good-snowman-is-hard-to-build.md),
  and [Snakebird decomposition](../games/s-z/snakebird.md).
- Novelty: not assessed.

## CON-014 — Exposed-only stack access

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: only the currently exposed end element of an ordered stack may
  be transferred directly, so deeper elements require removal of every element
  above them.
- Includes: access to the bottom exposed card of a FreeCell cascade; access to
  the contiguous top colour segment of a Water Sort tube.
- Excludes: concealed contents; selecting any visible element regardless of
  depth; moving an already legal ordered run as a state-equivalent macro.
- Parameters: stack orientation, accessible end and whether compound transfers
  are interface shortcuts.
- Evidence: [FreeCell decomposition](../games/a-f/freecell.md) and
  [Water Sort decomposition](../games/s-z/water-sort.md).
- Novelty: not assessed.

## CON-015 — Bounded single-element temporary buffer

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a fixed set of temporary storage zones may each hold at most one
  element and impose no ordering relation among their occupants.
- Includes: the four free cells in standard FreeCell.
- Excludes: a tableau column that may hold an ordered stack; generic finite
  board capacity; a hand whose contents are not individually accessible.
- Parameters: number of buffers, accepted element classes and retrieval rule.
- Evidence: [FreeCell decomposition](../games/a-f/freecell.md).
- Novelty: not assessed.

## CON-016 — Alternating-colour descending tableau build

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an element may be placed on a tableau stack only when its rank is
  exactly one lower than the exposed destination and its colour differs from
  that destination.
- Includes: placing a red five on a black six in standard FreeCell.
- Excludes: same-suit descending construction; any lower rank; foundation
  construction; placement into an empty cascade.
- Parameters: rank step, colour classes and empty-stack acceptance.
- Evidence: [FreeCell decomposition](../games/a-f/freecell.md).
- Novelty: not assessed.

## CON-017 — Same-suit ascending foundation build

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each completion stack accepts cards from one suit in exact
  ascending rank order from its lowest rank to its highest.
- Includes: building a FreeCell foundation from ace through king by suit.
- Excludes: alternating-colour tableau construction; placing a higher card
  before its lower same-suit predecessor; score-only collection zones.
- Parameters: suit classes, rank order and starting rank.
- Evidence: [FreeCell decomposition](../games/a-f/freecell.md).
- Novelty: not assessed.

## CON-018 — Orthogonally coupled ordered-run satisfaction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: every binary cell assignment must simultaneously belong to a row
  pattern and a column pattern whose filled runs have the declared lengths and
  order, with at least one empty cell between consecutive runs.
- Includes: satisfying every horizontal and vertical clue sequence in a
  classic black-and-white Nonogram.
- Excludes: an exact count that omits run order; a constraint applied along only
  one axis; all-different symbol coverage; the visible clue values themselves.
- Parameters: grid dimensions, line topology, binary values, run sequences and
  minimum separator length.
- Evidence: [Nonogram decomposition](../games/m-r/nonogram.md).
- Novelty: not assessed.

## CON-019 — Match-valid adjacent swap

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an ordinary adjacent-element exchange is accepted as a
  state-changing move only when the resulting board contains a declared
  horizontal or vertical contiguous group of at least the minimum same-type
  size involving the exchange.
- Includes: a Royal Match colour-item swap that creates a group of at least
  three same-coloured items.
- Excludes: activating a board power-up; non-adjacent exchange; a legal swap
  whose result need not match; automatic cascade formation.
- Parameters: minimum group size, line directions, special-element exceptions
  and invalid-swap feedback.
- Evidence: [Royal Match decomposition](../games/m-r/royal-match.md).
- Novelty: not assessed.

## CON-020 — Finite action budget with terminal exhaustion

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an attempt begins with a finite action allowance, accepted
  chargeable actions reduce it, and reaching zero before the completion
  objective is satisfied ends the attempt unsuccessfully.
- Includes: the displayed move limit of a standard Royal Match level; the
  remaining scoring Hands in a Balatro Blind.
- Excludes: elapsed real time; optional solution-efficiency scoring; a resource
  that can reach zero without terminating the attempt.
- Parameters: initial allowance, charged action classes, extension rules and
  exact objective-check timing.
- Evidence: [Royal Match decomposition](../games/m-r/royal-match.md) and
  [Balatro decomposition](../games/a-f/balatro.md).
- Novelty: not assessed.

## CON-021 — Per-container occupancy capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each declared container has a fixed unit capacity, and no
  transfer may increase its occupancy beyond that capacity.
- Includes: four-unit tubes in the scoped Water Sort ruleset.
- Excludes: total board capacity without container boundaries; a one-element
  free cell; a move budget; a container whose capacity expands during play.
- Parameters: capacity per container, heterogeneous capacities and whether
  partial transfers are permitted.
- Evidence: [Water Sort decomposition](../games/s-z/water-sort.md).
- Novelty: not assessed.

## CON-022 — Empty-or-matching-top destination compatibility

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a container may receive the accessible source type only when it
  is empty or its current exposed top type equals the source type, in addition
  to having remaining capacity.
- Includes: pouring blue water into an empty Water Sort tube or onto exposed
  blue water.
- Excludes: pouring onto a different exposed colour; compatibility based only
  on available capacity; matching elements that merge or disappear.
- Parameters: type domain, empty-container rule and any locked-complete rule.
- Evidence: [Water Sort decomposition](../games/s-z/water-sort.md).
- Novelty: not assessed.

## CON-023 — Side-owned piece control

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: on a participant's turn, only pieces assigned to that participant
  may be selected for movement, while opposing pieces may only be affected
  through declared interaction rules.
- Includes: White moving only white pieces and Black moving only black pieces
  in chess.
- Excludes: a single player controlling every movable piece; temporarily
  acquiring direct control of an opposing piece; turn order itself.
- Parameters: number of sides, ownership classes and control-transfer rules.
- Evidence: [Chess decomposition](../games/a-f/chess.md).
- Novelty: not assessed.

## CON-024 — Piece-class movement and line obstruction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: each piece class has a declared destination geometry, and pieces
  with line-based movement cannot pass through intervening occupancy unless
  their class explicitly permits it.
- Includes: chess rook, bishop, queen, knight, king and pawn movement, including
  the knight's ability to cross intervening squares.
- Excludes: one shared adjacency rule for every piece; collision constraints on
  a freely transformed multi-cell object; ownership and king safety.
- Parameters: piece classes, movement vectors, path rule, directionality and
  initial-move exceptions.
- Evidence: [Chess decomposition](../games/a-f/chess.md).
- Novelty: not assessed.

## CON-025 — Own-king attack prohibition

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a move is illegal when its resulting position leaves or places
  the moving side's designated royal piece under attack.
- Includes: rejecting a chess move that exposes one's king or fails to answer
  an existing check; attack restrictions on castling transit and destination.
- Excludes: avoiding loss as strategy when the move remains legal; capturing
  the opponent's king; generic collision or occupancy rules.
- Parameters: royal piece, attack relation and compound-move transit test.
- Evidence: [Chess decomposition](../games/a-f/chess.md).
- Novelty: not assessed.

## CON-026 — History-sensitive position rights and counters

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: legal options or terminal evaluation depend on public facts from
  the move sequence that are not recoverable from piece placement alone.
- Includes: chess castling rights, one-reply en-passant eligibility, position
  occurrence count and the count since the last pawn move or capture.
- Excludes: concealed history; current occupancy that fully determines
  legality; an external clock or score counter.
- Parameters: retained event types, expiry rule, equivalence test and threshold.
- Evidence: [Chess decomposition](../games/a-f/chess.md).
- Novelty: not assessed.

## CON-027 — Non-winning terminal draw predicate

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: play can terminate with neither side winning when a declared
  position or public-history predicate is satisfied.
- Includes: chess stalemate, dead position, automatic fivefold repetition and
  the automatic 75-move rule.
- Excludes: a player-negotiated draw; resignation; a temporary state from which
  winning remains legally possible and no threshold has been reached.
- Parameters: terminal predicates, repetition threshold, no-progress threshold
  and precedence of a simultaneous win.
- Evidence: [Chess decomposition](../games/a-f/chess.md).
- Novelty: not assessed.

## CON-028 — Fixed paired-endpoint identity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: immutable labelled endpoints occur in declared pairs, and a
  completed route is valid only when its two ends are the matching pair.
- Includes: connecting the two dots of one colour in Flow Free.
- Excludes: connecting arbitrary terminals; a route whose destination is not
  fixed by its source identity; movable endpoints.
- Parameters: number of pairs, label domain and endpoint placement.
- Evidence: [Flow Free decomposition](../games/a-f/flow-free.md).
- Novelty: not assessed.

## CON-029 — Orthogonally contiguous simple path

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each route is one unbranched sequence of distinct grid cells or
  graph vertices in which consecutive positions share an orthogonal edge.
- Includes: a classic Flow Free pipe turning through horizontally or vertically
  adjacent squares without branching or revisiting a cell; one Cosmic Express
  route traversing logically edge-adjacent isometric grid cells without a
  junction, revisit or self-crossing; a The Witness trace following adjacent
  grid-graph vertices from a start circle to an end cap without branching,
  revisiting or self-crossing.
- Excludes: diagonal adjacency; branched networks; disconnected cells of one
  colour; paths that leave and re-enter the board.
- Parameters: adjacency topology, turn count, route length and board boundary.
- Evidence: [Flow Free decomposition](../games/a-f/flow-free.md) and
  [Cosmic Express decomposition](../games/a-f/cosmic-express.md), and
  [The Witness decomposition](../games/s-z/the-witness.md).
- Novelty: not assessed.

## CON-030 — Exclusive path-cell occupancy

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: each board position may belong to at most one completed route, so
  distinct routes cannot cross or overlap within the same position.
- Includes: non-crossing, non-overlapping Flow Free pipes on a classic board.
- Excludes: bridge cells that carry two routes on separate layers; paths that
  share junctions; ordinary piece occupancy without route continuity.
- Parameters: position capacity, permitted bridge classes and endpoint sharing.
- Evidence: [Flow Free decomposition](../games/a-f/flow-free.md).
- Novelty: not assessed.

## CON-031 — Shared-input simultaneous controllability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: membership in a current controlled set makes every member receive
  the same directional or jump input simultaneously, even when only one member
  carries a privileged interaction or viewpoint locus.
- Includes: zero, one or multiple Baba Is You objects controlled through active
  `NOUN IS YOU` rules; every extant The Swapper body receiving the active
  body's movement and jump commands.
- Excludes: permanent control of one designated avatar only; autonomous
  movement without player input; issuing separate commands to selected units.
- Parameters: membership rule, controlled classes or instances, privileged
  locus, input channels and simultaneous collision handling.
- Evidence: [Baba Is You decomposition](../games/a-f/baba-is-you.md) and
  [The Swapper decomposition](../games/s-z/the-swapper.md).
- Novelty: not assessed.

## CON-032 — Property-conditioned movement blocking

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: entry into a cell is blocked by an occupant only while that
  occupant currently bears the declared blocking property; otherwise spatial
  overlap may be permitted.
- Includes: `STOP`-assigned objects blocking movement in Baba Is You until the
  active rule is broken or changed.
- Excludes: permanent static barriers; universal exclusive occupancy; blocking
  caused solely by an unmovable push chain.
- Parameters: blocking property, overlap layers, property precedence and
  interaction with simultaneous movement.
- Evidence: [Baba Is You decomposition](../games/a-f/baba-is-you.md).
- Novelty: not assessed.

## CON-033 — Contiguous push-chain free-end requirement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a contiguous chain of pushable occupants can shift only when
  every member can move in the commanded direction and the cell beyond the
  chain accepts the final member.
- Includes: pushing several aligned text or `PUSH` objects by one cell in Baba
  Is You.
- Excludes: a push restricted to exactly one object; pulling; chain movement
  through a blocking boundary; remote displacement.
- Parameters: chain length, cell occupancy layers, accepted destination and
  simultaneous pushes.
- Evidence: [Baba Is You decomposition](../games/a-f/baba-is-you.md).
- Novelty: not assessed.

## CON-034 — Per-unit move-then-ability allowance

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during one player phase, each controlled unit may relocate at
  most once and use at most one ability, with relocation unavailable after
  that unit commits its ability.
- Includes: ordering the movement and weapon or repair action of each available
  mech in Into the Breach.
- Excludes: a shared pool of interchangeable action points; one global move
  limit; real-time cooldowns.
- Parameters: unit count, movement allowance, ability count, action order and
  undo boundary.
- Evidence: [Into the Breach decomposition](../games/g-l/into-the-breach.md).
- Novelty: not assessed.

## CON-035 — Finite mission-round horizon

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a tactical attempt ends successfully after a declared finite
  number of rounds if its protected failure condition has not occurred.
- Includes: surviving the bounded turn count of an Into the Breach battle.
- Excludes: a finite budget of player moves spent one action at a time; an
  endless survival mode; an external speedrun timer.
- Parameters: round count, final-phase boundary and early-completion cases.
- Evidence: [Into the Breach decomposition](../games/g-l/into-the-breach.md).
- Novelty: not assessed.

## CON-036 — Shared infrastructure depletion failure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: damage to protected infrastructure reduces one shared integrity
  resource, and reaching zero terminates the attempt regardless of how many
  controlled units remain operational.
- Includes: civilian-building damage reducing the Power Grid to zero in Into
  the Breach.
- Excludes: individual unit health; a score that may fall without terminating
  play; the objective of preserving the resource above zero.
- Parameters: starting integrity, damage amounts, resistance exceptions and
  terminal threshold.
- Evidence: [Into the Breach decomposition](../games/g-l/into-the-breach.md).
- Novelty: not assessed.

## CON-037 — Base-complement or equal-rank merge compatibility

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical Threes-specific form of declared pairwise merge
  compatibility, merged into `CON-002` after equality-only and base-complement
  relations were confirmed to be parameters of the same legality predicate.
- Includes: historical references to `1 + 2 → 3`, `3 + 3 → 6` and the
  continuing Threes rank sequence.
- Excludes: new game signatures; use `CON-002` for pairwise collision-merge
  eligibility and `SYS-002` for the automatic replacement transition.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Threes decomposition](../games/s-z/threes.md).
- Merged into: `CON-002` by
  [`TAXONOMY_CHANGE_004`](../../research/taxonomy-changes/TAXONOMY_CHANGE_004.md).
- Novelty: not assessed.

## CON-038 — Opposite-edge moved-line spawn eligibility

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a valid directional shift, a successor may enter only from
  the edge opposite the movement direction and only into a line that changed
  during that shift.
- Includes: the constrained candidate entry cells for a new Threes card.
- Excludes: choosing any empty board cell; a fixed single entry position;
  insertion into a line that did not move or merge.
- Parameters: eligible lines, entry edge and random selection among candidates.
- Evidence: [Threes decomposition](../games/s-z/threes.md).
- Novelty: not assessed.

## CON-039 — Mandatory supplied-head commitment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the current first element of a supplied sequence must be
  committed before later elements become available; the player may not reorder,
  store, skip or discard it.
- Includes: using the bottom Pipe Dream dispenser piece next; consuming
  Dorfromantik's current tile while visible successors remain preview-only.
- Excludes: choosing any item from a hand; freely skipping an unwanted current
  element; whether the current element may be rotated or transformed before
  commitment, which belongs to the action boundary.
- Parameters: sequence order, preview depth, storage and discard policy.
- Evidence: [Pipe Mania decomposition](../games/m-r/pipe-mania.md) and
  [Dorfromantik decomposition](../games/a-f/dorfromantik.md).
- Novelty: not assessed.

## CON-040 — Port-compatible flow continuation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a flow may advance from one occupied cell to the next only when
  the current tile has an exit toward that neighbour and the neighbouring tile
  has a reciprocal entry port.
- Includes: straight and corner Pipe Dream sections conducting Flooz only
  through their printed connections, with crossover channels continuing
  straight.
- Excludes: visual adjacency without matching ports; branching into every open
  exit; endpoint identity between several player-drawn routes.
- Parameters: port set, directionality, crossover channels and branch policy.
- Evidence: [Pipe Mania decomposition](../games/m-r/pipe-mania.md).
- Novelty: not assessed.

## CON-041 — Flow-locked placed tile

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an ordinary placed tile may be replaced only before the active
  flow enters it; once filled, its position and orientation are immutable for
  the remainder of the attempt.
- Includes: blasting an unfilled Pipe Dream pipe while prohibiting replacement
  after Flooz fills it.
- Excludes: globally immutable givens; undo after a completed attempt; a tile
  locked immediately on placement without a flow boundary.
- Parameters: lock trigger, replaceable tile classes, penalty and replacement
  delay.
- Evidence: [Pipe Mania decomposition](../games/m-r/pipe-mania.md).
- Novelty: not assessed.

## CON-042 — Open-end flow termination

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the current attempt terminates when an advancing flow reaches a
  tile exit without a reciprocal traversable continuation, including a vacant
  cell, incompatible tile or board boundary.
- Includes: a Pipe Dream round ending when Flooz reaches the open end of the
  constructed pipeline.
- Excludes: voluntary early stopping; a recoverable leak that preserves the
  same attempt; completion merely because a target distance was reached.
- Parameters: terminal exit classes, grace period and evaluation order against
  the minimum-distance objective.
- Evidence: [Pipe Mania decomposition](../games/m-r/pipe-mania.md).
- Novelty: not assessed.

## CON-043 — Bounded visible hand and commit size

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player may hold at most a declared number of visible cards
  and may commit no more than a smaller declared subset in one play or discard.
- Includes: Balatro's ordinary hand-size limit and one-to-five-card play or
  discard selection; Fights in Tight Spaces exposing a bounded current hand
  and committing one held action card per play.
- Excludes: a one-card temporary buffer; hidden hand contents; an unlimited
  subset selected directly from the draw pile.
- Parameters: hand capacity, minimum and maximum commit size and effects that
  alter either limit.
- Evidence: [Balatro decomposition](../games/a-f/balatro.md) and
  [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md).
- Novelty: not assessed.

## CON-044 — Finite non-terminal redraw allowance

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an attempt begins with a finite allowance for discard-and-redraw
  actions; spending the final allowance removes that action option but does not
  itself terminate the attempt.
- Includes: Balatro's displayed Discards count within one Blind.
- Excludes: the scoring-Hand allowance whose exhaustion causes failure;
  unlimited redraw; a discarded card count rather than action count.
- Parameters: initial allowance, cards per discard, modifiers and refresh
  boundary.
- Evidence: [Balatro decomposition](../games/a-f/balatro.md).
- Novelty: not assessed.

## CON-045 — Ranked card-pattern predicates

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: rank, suit, equality and sequence relations define a hierarchy of
  recognised card subsets whose more specific satisfied predicate takes
  precedence over contained lower predicates.
- Includes: Balatro's standard High Card through Straight Flush poker-hand
  relations in the scoped Blind.
- Excludes: the automatic act of classifying a committed subset; betting-hand
  comparison against an opponent; arbitrary player-authored patterns.
- Parameters: rank order, suit set, ace treatment, pattern list and precedence.
- Evidence: [Balatro decomposition](../games/a-f/balatro.md).
- Novelty: not assessed.

## CON-046 — Fixed-capacity ordered modifier tableau

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: persistent modifiers occupy a bounded ordered set of slots, and
  their spatial order may change the result of a later automatic resolution.
- Includes: a Balatro Joker row in which additive and multiplicative scoring
  effects can be reordered within the available Joker slots.
- Excludes: an unordered inventory; modifiers consumed when played as part of
  the scoring hand; visible rule text manipulated into grammar.
- Parameters: slot count, modifier classes, reorder permissions and inactive
  slots.
- Evidence: [Balatro decomposition](../games/a-f/balatro.md).
- Novelty: not assessed.

## CON-047 — Finite reassignable network inventory

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: route, vehicle and infrastructure asset classes exist in finite
  counts, and deployed reusable assets cannot be used elsewhere until removed
  or reassigned.
- Includes: Mini Metro lines, locomotives, carriages, tunnels or bridges and
  interchanges available in inventory or deployed on the map; detachable
  green or Balloon Goo that cannot support another World of Goo location until
  reclaimed from its current attachment; Tin Hearts prism blocks and routing
  devices that must be moved away from one route position before serving at
  another.
- Excludes: a consumable action budget; fixed board occupancy alone; unlimited
  cosmetic route colours.
- Parameters: asset classes, initial counts, reclaim delay and per-map limits.
- Evidence: [Mini Metro decomposition](../games/m-r/mini-metro.md) and
  [World of Goo decomposition](../games/s-z/world-of-goo.md), and
  [Tin Hearts decomposition](../games/s-z/tin-hearts.md).
- Novelty: not assessed.

## CON-048 — Unbranched ordered route topology

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: each named service line is one ordered station sequence traversed
  by its assigned vehicles and cannot contain a branch with three independent
  continuations.
- Includes: open Mini Metro lines and permitted closed loops, with transfers
  formed by multiple named lines sharing a station.
- Excludes: arbitrary branching rail graphs within one line; simple paths that
  prohibit shared transfer nodes; pipe-port flow networks.
- Parameters: loop permission, station revisit rule, maximum stops and route
  geometry rendering.
- Evidence: [Mini Metro decomposition](../games/m-r/mini-metro.md).
- Novelty: not assessed.

## CON-049 — Geography-gated crossing consumption

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a route segment that crosses declared impassable geography is
  legal only when it consumes one available crossing asset for as long as that
  segment remains deployed.
- Includes: Mini Metro tunnel or bridge use across map water.
- Excludes: ordinary same-bank segments; visual line intersections at transfer
  stations; permanent walls that no resource can cross.
- Parameters: obstacle regions, crossing count, reclamation and map-specific
  bridge or tunnel terminology.
- Evidence: [Mini Metro decomposition](../games/m-r/mini-metro.md).
- Novelty: not assessed.

## CON-050 — Capacity-bounded passenger pickup

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a vehicle may carry only a bounded number of demand units, so
  eligible waiting units remain queued when available onboard capacity is
  exhausted.
- Includes: Mini Metro locomotive capacity enlarged by assigned carriages; the
  scoped one-seat Cosmic Express carriage leaving another alien waiting until
  its current passenger alights.
- Excludes: station crowd capacity; total vehicle inventory; route length.
- Parameters: base capacity, carriage increment, pickup priority and special
  rolling stock.
- Evidence: [Mini Metro decomposition](../games/m-r/mini-metro.md) and
  [Cosmic Express decomposition](../games/a-f/cosmic-express.md).
- Novelty: not assessed.

## CON-051 — Type-coded destination completion

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each demand unit names a destination class, and it leaves the
  transport system only upon reaching a service node of the matching class.
- Includes: a square Mini Metro passenger completing its trip at a square
  station, possibly after automatic transfers; a Cosmic Express alien leaving
  the carriage at a compatible same-colour home.
- Excludes: any connected node satisfying delivery; player-selected passenger
  destinations; colour used only to identify a route.
- Parameters: destination-class encoding, rare classes, route choice and
  transfer eligibility.
- Evidence: [Mini Metro decomposition](../games/m-r/mini-metro.md) and
  [Cosmic Express decomposition](../games/a-f/cosmic-express.md).
- Novelty: not assessed.

## CON-052 — Sustained station-overload termination

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: exceeding a node's waiting-demand capacity starts a visible
  grace countdown, relief can arrest or reverse it, and allowing any countdown
  to fill ends the session.
- Includes: Classic-mode Mini Metro overcrowding failure.
- Excludes: immediate failure at the first excess unit; vehicle capacity;
  non-terminal congestion penalties; a fixed external time limit.
- Parameters: station capacity, grace duration, recovery rate, train-presence
  interaction and interchange capacity.
- Evidence: [Mini Metro decomposition](../games/m-r/mini-metro.md).
- Novelty: not assessed.

## CON-053 — Occupied-middle empty-landing jump predicate

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a relocation is legal only across three collinear addressable
  positions whose source and adjacent middle positions are occupied and whose
  destination two steps away is empty.
- Includes: horizontal or vertical jumps on the traditional English Peg
  Solitaire board.
- Excludes: diagonal jumps; jumping over an empty middle position; landing on
  an occupied position; moving only one step.
- Parameters: permitted directions, topology and jump distance.
- Evidence: [Peg Solitaire decomposition](../games/m-r/peg-solitaire.md).
- Novelty: not assessed.

## CON-054 — Forward-only monotonic material reduction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: every legal forward action reduces the active material count by
  exactly one, and no legal in-scope action restores a removed element or
  increases that count.
- Includes: traditional Peg Solitaire without reverse jumps, where 32 pegs can
  reach one peg only after exactly 31 jumps.
- Excludes: an interface undo; reversible “unjump” variants; games whose count
  can both increase and decrease through ordinary actions.
- Parameters: initial count, per-action decrement and reverse-move policy.
- Evidence: [Peg Solitaire decomposition](../games/m-r/peg-solitaire.md).
- Novelty: not assessed.

## CON-055 — No-jump terminal exhaustion

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: play terminates when the current occupancy contains no legal
  source-middle-destination jump, whether or not the target configuration has
  been reached.
- Includes: an English Peg Solitaire position with multiple isolated pegs but
  no `occupied–occupied–empty` triple.
- Excludes: a finite move counter; voluntary stopping; a non-terminal state
  with no action from one optional action class.
- Parameters: legal-jump predicate and success evaluation order.
- Evidence: [Peg Solitaire decomposition](../games/m-r/peg-solitaire.md).
- Novelty: not assessed.

## CON-056 — Adjacent-frontier expanding placement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: every new tile must occupy an empty position sharing at least one
  boundary with the connected placed landscape, while successful placements
  create further addressable frontier positions rather than consuming a fixed
  board capacity.
- Includes: extending Dorfromantik's hex landscape one adjacent tile at a time.
- Excludes: placement anywhere on a fixed grid; tracing through existing cells;
  a pre-declared finite set of board positions (`CON-001`).
- Parameters: cell topology, minimum shared boundaries and any world border.
- Evidence: [Dorfromantik decomposition](../games/a-f/dorfromantik.md).
- Novelty: not assessed.

## CON-057 — Mandatory supply-head commitment with free orientation

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical Dorfromantik-specific form of mandatory supplied-head
  commitment, merged into `CON-039` after orientation was confirmed to be an
  Action parameter rather than a second Constraint boundary.
- Includes: historical references to consuming Dorfromantik's current tile.
- Excludes: new game signatures; use `CON-039` for the shared commitment rule
  and the relevant Action gene for transform permission.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Dorfromantik decomposition](../games/a-f/dorfromantik.md).
- Merged into: `CON-039` by
  [`TAXONOMY_CHANGE_002`](../../research/taxonomy-changes/TAXONOMY_CHANGE_002.md).
- Novelty: not assessed.

## CON-058 — Typed shared-edge compatibility

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each touching tile boundary compares two typed edge segments;
  compatible types connect into one landscape relation, incompatible types do
  not or make that adjacency illegal, and declared corridor types may
  additionally forbid blocked endings.
- Includes: Dorfromantik matching forests, houses, fields, water, rivers and
  railways across adjacent hex edges, including stricter river and rail exits.
- Includes: Carto permitting square map fragments to touch only where their
  road, river, forest, plain or other terrain boundary patterns match.
- Excludes: reciprocal pipe ports carrying a live directed flow; colour-only
  endpoint identity; visual adjacency with no mechanical evaluation.
- Parameters: tile topology, edge-type vocabulary, compatibility relation,
  corridor exceptions and whether a mismatch is forbidden or merely penalised.
- Evidence: [Dorfromantik decomposition](../games/a-f/dorfromantik.md) and
  [Carto decomposition](../games/a-f/carto.md).
- Novelty: not assessed.

## CON-059 — Replenishable finite supply with exhaustion termination

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: each ordinary action consumes one element from a finite supply,
  qualifying play can add elements back during the same attempt, and the
  attempt terminates only when no supplied element remains to enable another
  action.
- Includes: Dorfromantik Classic mode ending when its tile stack is empty while
  quests and perfect placements can extend that stack.
- Excludes: a strictly decreasing action allowance (`CON-020`); a finite
  optional allowance whose exhaustion leaves other actions available; an
  unlimited creative supply.
- Parameters: initial supply, reward quantities, maximum supply and terminal
  evaluation order.
- Evidence: [Dorfromantik decomposition](../games/a-f/dorfromantik.md).
- Novelty: not assessed.

## CON-060 — Irreversible support-link severing

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a severed support link is permanently removed from the current
  attempt, cannot transmit force again and cannot be restored by another
  ordinary forward action.
- Includes: a cut Cut the Rope rope remaining absent until level restart.
- Excludes: toggling a reusable connection; replacing an unfilled tile;
  interface undo; removing active material on every action regardless of the
  selected target.
- Parameters: cuttable link classes, multi-cut gestures and restart boundary.
- Evidence: [Cut the Rope decomposition](../games/a-f/cut-the-rope.md).
- Novelty: not assessed.

## CON-061 — Terminal required-object boundary escape

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the current attempt fails when a required moving puzzle object
  leaves the playable supported spatial boundary before its completion role is
  satisfied.
- Includes: Cut the Rope ending unsuccessfully when the candy falls outside
  the level canvas; a Stephen's Sausage Roll sausage falling into surrounding
  water before all its faces are correctly cooked; a required Snakebird falling
  beyond supported Level 1 space before entering the exit.
- Excludes: recoverable offscreen motion; fixed-board entry obstruction;
  exposing a concealed hazard; voluntary restart.
- Parameters: boundary geometry, required object, support rule, completion-
  check precedence and restart behaviour.
- Evidence: [Cut the Rope decomposition](../games/a-f/cut-the-rope.md) and
  [Stephen's Sausage Roll decomposition](../games/s-z/stephens-sausage-roll.md),
  and [Snakebird decomposition](../games/s-z/snakebird.md).
- Novelty: not assessed.

## CON-062 — Static machine-footprint placement compatibility

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: persistent machine components may be committed only when their
  declared static footprints and exclusive anchor positions do not overlap an
  incompatible placed component or fixed port.
- Includes: Opus Magnum preventing arm bases, glyphs, tracks and reagent or
  product ports from occupying forbidden shared hexes while allowing declared
  exceptions such as a track beneath an arm base; Infinifactory preventing a
  conveyor or support voxel from overlapping an incompatible component, fixed
  hatch, output device or immutable environment footprint.
- Excludes: collisions caused later by moving arms or molecules; finite board
  capacity; adjacency requirements between placed tiles.
- Parameters: footprint shapes, orientation, component-pair compatibility and
  allowed overlay exceptions.
- Evidence: [Opus Magnum decomposition](../games/m-r/opus-magnum.md) and
  [Infinifactory decomposition](../games/g-l/infinifactory.md).
- Novelty: not assessed.

## CON-063 — Kinematic-conflict execution halt

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an automatic machine run halts as invalid when scheduled motion
  would make incompatible physical bodies overlap or impose mutually
  inconsistent movement on one carried assembly.
- Includes: Opus Magnum stopping on atom-to-atom or atom-to-arm-base collision
  and on two arms attempting incompatible motion of the same molecule;
  SpaceChem stopping when a carried molecule intersects another atom or the
  reactor wall.
- Excludes: rejecting an editor placement before execution; harmless path
  crossing at different cycles; terminal loss from a payload leaving bounds.
- Parameters: collision shapes, swept-motion sampling, shared-grip rules,
  diagnostic timing and restart behaviour.
- Evidence: [Opus Magnum decomposition](../games/m-r/opus-magnum.md) and
  [SpaceChem decomposition](../games/s-z/spacechem.md).
- Novelty: not assessed.

## CON-064 — Immutable non-interactive evidence tableau

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while a bounded event-evidence representation is open,
  represented people, objects, poses and event time cannot be moved, altered or
  advanced; only observation focus and the information interface may change.
- Includes: walking through a frozen Return of the Obra Dinn death scene while
  being unable to manipulate its bodies or resume the event; opening fixed
  people, possessions and documents in a The Case of the Golden Idol tableau.
- Excludes: a paused live simulation that can resume from the same mutable
  state; a static board whose symbols are directly editable; read-only prose.
- Parameters: two- versus three-dimensional representation, viewpoint
  collision, pointer focus, allowed overlays and exit behaviour.
- Evidence: [Return of the Obra Dinn decomposition](../games/m-r/return-of-the-obra-dinn.md)
  and [The Case of the Golden Idol decomposition](../games/s-z/the-case-of-the-golden-idol.md).
- Novelty: not assessed.

## CON-065 — Visual seam-or-overlay composition compatibility

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a multi-panel composition becomes mechanically continuous only
  when its current crops, edges, apertures, scale and depicted geometry satisfy
  a authored adjacency or overlay relation.
- Includes: Gorogoa panels joining when a doorway frame overlays a compatible
  destination or when adjacent image edges align into one traversable scene.
- Excludes: any two neighbouring panels interacting regardless of contents;
  typed tile-edge matching on an expanding landscape; mere visual similarity
  with no continuation.
- Parameters: adjacency versus overlay, crop and scale tolerance, orientation,
  matching features and permitted multi-panel count.
- Evidence: [Gorogoa decomposition](../games/g-l/gorogoa.md).
- Novelty: not assessed.

## CON-066 — Cross-panel-only represented-world mutation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player cannot directly manipulate depicted world objects;
  any puzzle-relevant mutation or movement inside the represented world must
  arise from combining two or more panels in a valid relation.
- Includes: Gorogoa forbidding a direct crank turn or character command while
  allowing a connected counterweight panel to move the represented mechanism.
- Excludes: changing only the panel viewpoint; rearranging panel containers;
  puzzles that mix panel composition with direct in-world object controls.
- Parameters: permitted viewpoint actions, number of contributing panels and
  isolated timing-sequence exceptions.
- Evidence: [Gorogoa decomposition](../games/g-l/gorogoa.md).
- Novelty: not assessed.

## CON-067 — Finite typed role-assignment inventory

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an attempt supplies separate finite stocks for declared agent
  roles, and each accepted assignment consumes one unit of the selected type;
  stock exhaustion blocks that type without itself terminating the attempt.
- Includes: the displayed per-skill counts in an original Lemmings level.
- Excludes: a shared action allowance whose exhaustion ends the attempt; a
  reusable finite infrastructure item that can be detached and reassigned; an
  unlimited ability with a time cooldown.
- Parameters: role types, initial counts, consumption timing and replenishment.
- Evidence: [Lemmings decomposition](../games/g-l/lemmings.md).
- Novelty: not assessed.

## CON-068 — Fixed attempt deadline with terminal expiry

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a declared real-time allowance decreases while the attempt runs,
  and reaching zero terminates the attempt unsuccessfully unless its completion
  objective has already been satisfied.
- Includes: the remaining-time limit of an original Lemmings level.
- Excludes: an elapsed timer used only for performance scoring; a finite number
  of player actions; a deadline that merely changes rewards while play continues.
- Parameters: initial duration, pause rule, completion-check order and any time
  additions.
- Evidence: [Lemmings decomposition](../games/g-l/lemmings.md).
- Novelty: not assessed.

## CON-069 — Finite construction-or-extraction population

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an attempt supplies a finite countable population whose members
  may either be committed as structural material or remain available for
  terminal extraction, so each committed member reduces the maximum population
  still able to satisfy the extraction quota.
- Includes: ordinary countable Goo Balls used as World of Goo bridge or tower
  nodes instead of being left loose for pipe extraction.
- Excludes: a separate finite skill inventory applied to agents; construction
  currency that is never counted by the objective; reusable infrastructure
  whose deployment does not reduce a completion population.
- Parameters: countable types, commitment reversibility, extraction threshold
  and whether destroyed structure can return to the loose population.
- Evidence: [World of Goo decomposition](../games/s-z/world-of-goo.md).
- Novelty: not assessed.

## CON-070 — Type-and-range-bounded structural attachment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a live material node may attach only within a declared distance
  of eligible structural neighbours and may form no more than its type-specific
  maximum number of simultaneous support links.
- Includes: original World of Goo black Goo forming at most two strands and
  green Goo forming at most three within attachment range.
- Excludes: static component footprint non-overlap; typed edge matching on a
  discrete tile grid; unrestricted proximity links with no valence bound.
- Parameters: material types, maximum valence, link distance, neighbour
  priority and compatible node classes.
- Evidence: [World of Goo decomposition](../games/s-z/world-of-goo.md).
- Novelty: not assessed.

## CON-071 — Squad-level command granularity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: player-issued movement and ordinary combat authority addresses a
  persistent commander-led squad as one unit, while its individual members
  cannot receive separate destinations or per-strike commands.
- Includes: selecting and relocating a Bad North squad while its soldiers
  navigate, form and engage autonomously.
- Excludes: selecting any individual autonomous agent for a temporary role;
  directly steering one avatar; controlling each member of a group separately.
- Parameters: squad size, commander role, allowed squad commands, formation
  elasticity and member-level exceptions.
- Evidence: [Bad North decomposition](../games/a-f/bad-north.md).
- Novelty: not assessed.

## CON-072 — Card-type map-zone eligibility

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a held world card may be committed only to map positions in its
  declared spatial category, with road, route-adjacent and off-route regions
  remaining mechanically distinct.
- Includes: Loop Hero road cards placed on the circuit, roadside cards beside
  it and landscape cards in eligible surrounding space.
- Excludes: typed edge compatibility after placement; arbitrary static machine
  footprint overlap; mandatory placement at the current expansion frontier.
- Parameters: zone classes, card category, adjacency, occupied-position rule
  and card-specific exceptions.
- Evidence: [Loop Hero decomposition](../games/g-l/loop-hero.md).
- Novelty: not assessed.

## CON-073 — Fixed cyclic traversal route

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during one attempt, an autonomous actor repeatedly follows one
  closed ordered route in a fixed direction; player world edits may alter the
  route's contents but cannot branch, redirect or reorder its traversal.
- Includes: the predetermined Loop Hero expedition circuit.
- Excludes: an editable transit line; a player-built extraction structure;
  open paths whose endpoint terminates the attempt.
- Parameters: route length, direction, camp position, traversal speed and
  whether temporary stops preserve order.
- Evidence: [Loop Hero decomposition](../games/g-l/loop-hero.md).
- Novelty: not assessed.

## CON-074 — Location-conditioned retreat retention

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: ending an active expedition transfers only the resource share
  associated with the actor's current route state, with a declared safe
  boundary retaining more than mid-route retreat or involuntary defeat.
- Includes: Loop Hero campfire retreat banking all gathered resources while a
  mid-loop exit or death loses a larger share.
- Excludes: fixed death penalty independent of location; escape that preserves
  a combat unit but does not bank expedition resources; optional score bonus.
- Parameters: safe boundary, mid-route share, defeat share, protected resource
  classes and persistent modifiers.
- Evidence: [Loop Hero decomposition](../games/g-l/loop-hero.md).
- Novelty: not assessed.

## CON-075 — Avatar-local world-command placement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player may place or edit a persistent world instruction only
  at an eligible position physically reachable by the directly navigated
  command avatar.
- Includes: moving the HUMANITY Shiba Inu through the trial to bark a command
  onto its current grid position.
- Excludes: remote cursor placement anywhere on the visible board; assigning a
  command directly to an agent; route editing with no in-world avatar.
- Parameters: avatar movement rules, placement radius, occupied-support rule,
  vertical reach and time-stop exceptions.
- Evidence: [HUMANITY decomposition](../games/g-l/humanity.md).
- Novelty: not assessed.

## CON-076 — Actor-specific traversal and interaction permissions

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each controlled or commanded actor class can traverse, resist or
  activate only its declared subset of passages, hazards and world
  interactions, so success requires coordinating complementary permissions
  rather than treating all actor classes as substitutes.
- Includes: Timelie's cat using vents and meowing but not operating girl-only
  keypads, while the girl uses those controls but cannot traverse cat vents;
  Pikmin types and Oatchi providing different hazard, traversal and work
  permissions.
- Excludes: cosmetic character differences; identical units with different
  positions; combat-class effectiveness without traversal or interaction locks.
- Parameters: actor classes, traversal edges, interaction catalogue, carried
  state, switchability and whether permissions can change during a level.
- Evidence: [Timelie decomposition](../games/s-z/timelie.md) and
  [Pikmin 4 decomposition](../games/m-r/pikmin-4.md).
- Novelty: not assessed.

## CON-077 — Directed occlusion-bounded hostile perception

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: hostile detection requires a controlled actor to occupy the
  hostile observer's current directed perception region without an intervening
  opaque barrier.
- Includes: timing Timelie movement outside a robot's facing-dependent sight
  region or behind walls while its patrol direction changes.
- Excludes: global detection independent of geometry; exact hostile-intent
  preview; an explicit sound stimulus that bypasses ordinary sight.
- Parameters: field angle, range, facing update, occluder classes, boundary
  inclusion, detection delay and alert persistence.
- Evidence: [Timelie decomposition](../games/s-z/timelie.md).
- Novelty: not assessed.

## CON-078 — Surface-bounded portal endpoint eligibility

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a portal endpoint may persist only where the aimed world surface
  has an eligible material and enough contiguous, suitably planar area for the
  complete aperture footprint.
- Includes: Portal accepting shots on sufficiently large portal-conductive
  chamber panels while rejecting dark, moving, sharply interrupted or too-small
  surfaces.
- Excludes: route occupancy on a discrete board; support validity for a solid
  movable device; collision blocking after a valid portal already exists.
- Parameters: material classes, footprint dimensions, planarity tolerance,
  moving-surface rule, edge clearance and overlapping-endpoint policy.
- Evidence: [Portal decomposition](../games/m-r/portal.md).
- Novelty: not assessed.

## CON-079 — One replaceable endpoint per portal channel

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each portal channel can maintain at most one active endpoint, so
  a valid new placement removes that channel's previous endpoint and traversal
  requires the complementary channel to exist.
- Includes: Portal's single blue and single orange endpoints, with either
  colour replaced independently by firing it again.
- Excludes: capacity limits on interchangeable inventory; networks with any
  number of route nodes; one-use paired teleporters fixed by the level.
- Parameters: channel count, replacement timing, incomplete-pair visibility,
  invalid-shot effect and reset-field behaviour.
- Evidence: [Portal decomposition](../games/m-r/portal.md).
- Novelty: not assessed.

## CON-080 — Finite active follower and type capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: only a bounded number of followers and a bounded number of their
  distinct types may be active in the field, so taking out another member or
  type requires available capacity or returning current followers to reserve.
- Includes: Pikmin 4's upgradable field headcount and maximum of three active
  Pikmin types on an ordinary expedition.
- Excludes: finite role-use stock consumed on assignment; squad command
  granularity with no reserve roster; a limit on simultaneously held objects.
- Parameters: headcount cap, type cap, reserve access points, upgrade schedule,
  Oatchi equivalence and planted-versus-active accounting.
- Evidence: [Pikmin 4 decomposition](../games/m-r/pikmin-4.md).
- Novelty: not assessed.

## CON-081 — Day-end off-squad follower loss

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a fixed field-work interval ends at a declared boundary, and any
  vulnerable follower not returned to the protected squad or base at that
  boundary is permanently removed, while the broader campaign continues.
- Includes: surface Pikmin outside the safe group or base being lost at sunset
  in Pikmin 4.
- Excludes: a deadline whose expiry makes the whole attempt unsuccessful; an
  elapsed timer used only for score; ordinary lethal hazard contact before the
  interval ends.
- Parameters: interval duration, warning phase, protected states, vulnerable
  follower types, automatic gathering exceptions and campaign continuation.
- Evidence: [Pikmin 4 decomposition](../games/m-r/pikmin-4.md).
- Novelty: not assessed.

## CON-082 — Centre-aligned nested-boundary access

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: crossing between a container's parent and child spaces requires
  the source, destination and aperture at the designated centre position of the
  relevant side to be open; clearance elsewhere on that side cannot substitute.
- Includes: entering or exiting an enterable Patrick's Parabox box only through
  its centre-aligned edge mapping.
- Excludes: collision with any point of a continuous portal surface; choosing
  any open edge cell; visual compatibility between adjacent image panels.
- Parameters: grid dimensions, designated aperture cells, inward versus outward
  mapping, participant footprint and chain-transfer clearance.
- Evidence: [Patrick's Parabox decomposition](../games/m-r/patricks-parabox.md).
- Novelty: not assessed.

## CON-083 — Finite created-body capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: only a fixed maximum number of player-created bodies may coexist,
  so another can be instantiated only while an unused slot remains or after an
  existing created body is removed.
- Includes: The Swapper permitting up to four clones at once, in addition to
  the currently occupied body.
- Excludes: a field roster drawn from a persistent reserve; a limit on actor
  types; a consumable creation stock that does not recover when a body dies.
- Parameters: capacity, whether the original body counts, refund timing,
  reserved slots and scope across room transitions.
- Evidence: [The Swapper decomposition](../games/s-z/the-swapper.md).
- Novelty: not assessed.

## CON-084 — Unobstructed targeting path for remote body operation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a remote body operation is legal only when the aimed target lies
  within the operation's range and no opaque world barrier interrupts the
  direct targeting segment from the active body.
- Includes: The Swapper requiring line of sight both to create a clone at an
  aimed position and to transfer control into an existing clone.
- Excludes: hostile perception cones; portal-surface material eligibility;
  pathfinding reachability around corners; visibility used only as information.
- Parameters: range, ray origin, occluder classes, target footprint, boundary
  contact and separate operation channels.
- Evidence: [The Swapper decomposition](../games/s-z/the-swapper.md).
- Novelty: not assessed.

## CON-085 — Region-specific action-channel suppression

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: occupying or targeting a visibly marked spatial region disables
  a declared subset of otherwise available action channels while leaving other
  channels legal according to the region's type.
- Includes: blue The Swapper light preventing clone creation, red light
  preventing control transfer and purple light preventing both.
- Excludes: lethal hazard contact; one universal no-action zone; actor-class
  permissions that remain attached to an actor outside the region.
- Parameters: region geometry, suppressed action channels, source-versus-target
  evaluation, overlap composition, boundary inclusion and visual coding.
- Evidence: [The Swapper decomposition](../games/s-z/the-swapper.md).
- Novelty: not assessed.

## CON-086 — Active-body-exclusive device authority

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: within a synchronized controlled body set, exactly the body that
  currently holds the direct-control locus may originate a declared device
  action, while the other bodies remain movement-responsive but cannot use it.
- Includes: only the currently occupied The Swapper body creating clones or
  firing the swap beam.
- Excludes: permanent actor-class abilities; independent device use by every
  simultaneously controlled body; follower commands retained by several field
  leaders at once.
- Parameters: privileged locus, device channels, origin point, transfer timing,
  simultaneous input order and disabled-body feedback.
- Evidence: [The Swapper decomposition](../games/s-z/the-swapper.md).
- Novelty: not assessed.

## CON-087 — Path-partitioned monochromatic clue regions

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: treating the completed path as barriers between adjacent panel
  cells, every resulting connected region may contain square clues of at most
  one declared colour.
- Includes: drawing a The Witness line so no connected region contains both a
  black square and a white square, while multiple same-colour regions and blank
  cells remain permitted.
- Excludes: requiring the path to visit coloured clues; pairing two coloured
  endpoints; assigning every cell a colour; requiring one region per clue.
- Parameters: colour set, cell adjacency, path-boundary convention, blank
  cells, exterior boundary and interaction with other clue families.
- Evidence: [The Witness decomposition](../games/s-z/the-witness.md).
- Novelty: not assessed.

## CON-088 — Unique persistent map-fragment inventory

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each acquired map fragment is one persistent unique object that
  may be rearranged repeatedly but cannot be duplicated, subdivided or used in
  two map positions simultaneously.
- Includes: Carto solving with the finite set of map pieces found so far, each
  retaining its terrain and attached world contents across relocation.
- Excludes: consuming a tile from a replenishable supply; unlimited copies of a
  terrain brush; fixed board positions whose contents change identity; a limit
  on simultaneously controlled actors.
- Parameters: acquired fragment set, uniqueness identity, off-map storage,
  duplication exceptions, chapter reset and content persistence.
- Evidence: [Carto decomposition](../games/a-f/carto.md).
- Novelty: not assessed.

## CON-089 — Finite branch-local source-image stock

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a puzzle branch exposes only a finite set of source images for
  world placement, and committing one removes that source from the currently
  held stock until an allowed duplication or history restoration supplies it
  again.
- Includes: an early Viewfinder puzzle supplying one found photograph whose
  placement must create the required route; a wrong commitment is revised by
  rewinding to the state in which that image was still available.
- Excludes: persistent Carto fragments that can be lifted and rearranged again;
  reusable network assets reclaimed by detachment; an unlimited image brush;
  a generic action counter whose exhaustion alone terminates the attempt.
- Parameters: source identities, initial count, commitment consumption,
  duplication availability, rewind restoration and cross-level reset.
- Evidence: [Viewfinder decomposition](../games/s-z/viewfinder.md).
- Novelty: not assessed.

## CON-090 — Oriented player-tool footprint clearance

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a persistent agent and attached tool occupy an ordered oriented
  multi-cell footprint; translation and rotation are legal only when every
  destination and swept clearance cell is compatible.
- Includes: Stephen's Sausage Roll requiring the player cell, current fork,
  future fork and fourth corner of the two-by-two turn area to be clear.
- Excludes: ordinary single-cell avatar collision; viewpoint rotation; a
  temporary held item with no occupied world cell; object push access alone.
- Parameters: footprint, orientation set, sweep geometry, entity-specific
  terrain compatibility and contact exceptions.
- Evidence: [Stephen's Sausage Roll decomposition](../games/s-z/stephens-sausage-roll.md).
- Novelty: not assessed.

## CON-091 — Exact-once surface heat capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: every identified surface of a required object may receive one
  processing contact, while a second contact on the same surface immediately
  invalidates the attempt.
- Includes: each of four Stephen's Sausage Roll sausage faces being grilled
  once and burning on a repeated cook.
- Excludes: an ordinary goal that an object may leave and revisit; a total move
  budget; optional repeated scoring contact; irreversible processing with no
  penalty for repetition.
- Parameters: face identity set, allowed contact count, terminal timing,
  processed-state persistence and reset / undo behaviour.
- Evidence: [Stephen's Sausage Roll decomposition](../games/s-z/stephens-sausage-roll.md).
- Novelty: not assessed.

## CON-092 — Size-ordered top-access stack geometry

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a ground position may hold an ordered vertical stack of movable
  objects, but only its exposed top object may move and an incoming object is
  legal only when strictly smaller than every object below it.
- Includes: A Good Snowman Is Hard to Build allowing a small snowball on a
  medium or large top ball and a medium one on a large ball, while forbidding
  equal / larger placement and direct stack-to-stack transfer.
- Excludes: exclusive one-entity cell occupancy; unrestricted LIFO containers;
  same-value collision merging; translating a whole contiguous chain.
- Parameters: ordered size domain, maximum depth, top-access rule, incoming
  compatibility, stack-to-stack prohibition and completed-stack mutability.
- Evidence: [A Good Snowman Is Hard to Build decomposition](../games/a-f/a-good-snowman-is-hard-to-build.md).
- Novelty: not assessed.

## CON-093 — Case-local phrase vocabulary and typed answer slots

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: structured hypothesis blanks may be filled only from a finite set
  of terms extracted in the current evidence case, and each blank restricts
  eligible phrases by its declared grammatical or semantic role.
- Includes: The Case of the Golden Idol limiting prologue name, location and
  event Scroll blanks to collected case words and their compatible slot types.
- Excludes: unrestricted free-text entry; a complete roster whose labels may
  be assigned to any subject; ordinary cell symbol domains with global board
  constraints.
- Parameters: vocabulary size, phrase classes, token reuse, slot count,
  grammatical context and whether unused distractors remain.
- Evidence: [The Case of the Golden Idol decomposition](../games/s-z/the-case-of-the-golden-idol.md).
- Novelty: not assessed.

## CON-094 — Shared renewable card-play budget

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: all ordinary cards played during one player phase spend from one
  common numeric resource pool, and the pool restores by a declared amount at
  the next turn boundary rather than being assigned separately to actors.
- Includes: Fights in Tight Spaces movement, attack, defence and repositioning
  cards spending shared Momentum before its next-turn restoration.
- Excludes: one move and one ability allocated to each controlled unit; a
  finite non-renewing level move count; a card-use predicate based only on
  combo threshold with no shared payment pool.
- Parameters: starting value, maximum value, refresh amount, card costs,
  modifiers and permitted carry-over.
- Evidence: [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md).
- Novelty: not assessed.

## CON-095 — Per-character independent movement-and-action allowance

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during one player phase, each controlled character ordinarily
  receives one bounded movement use and one separate action allowance; either
  may be spent first and movement remains available after the action.
- Includes: Tactical Breach Wizards characters moving before or after spending
  their ordinary action point, subject to explicit ability/perk exceptions.
- Excludes: movement becoming unavailable after ability commitment; a shared
  pool of interchangeable actions; real-time locomotion and cooldowns.
- Parameters: unit count, movement distance, action count, interleaving,
  refresh effects, extra actions and rewind restoration.
- Evidence: [Tactical Breach Wizards decomposition](../games/s-z/tactical-breach-wizards.md).
- Novelty: not assessed.

## CON-096 — Bounded prepared-attack queue capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: no more than a fixed number of attack tiles may coexist in the
  player's prepared execution queue.
- Includes: the Shogun Showdown queue limit of three tiles.
- Excludes: a maximum hand size; one action point limiting immediate commands;
  an unbounded editable command timeline.
- Parameters: slot count, empty activation, duplicate eligibility and capacity
  upgrades.
- Evidence: [Shogun Showdown decomposition](../games/s-z/shogun-showdown.md).
- Novelty: not assessed.

## CON-097 — Turn-recharged attack-tile availability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an attack tile used in execution becomes unavailable for queue
  insertion until a declared number of subsequent turn-clock advances restore
  its readiness.
- Includes: Shogun Showdown attack-tile cooldown pips recharging by one at each
  turn end.
- Excludes: a finite tile consumed permanently; a shared renewable action
  budget; a cooldown measured by continuous real time.
- Parameters: cooldown length, per-turn increment, initial readiness, free-play
  exceptions and upgrades.
- Evidence: [Shogun Showdown decomposition](../games/s-z/shogun-showdown.md).
- Novelty: not assessed.
