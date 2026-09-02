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
  passengers, homes, entrance and exit of a scoped Cosmic Express puzzle; the
  authored platform, wall, void and target cells of a Can of Wormholes stage;
  the fixed land, water, rock, stump and target-shore cells of a scoped A
  Monster's Expedition lesson; the 64 addressed cells of a standard Slant
  field; the 64 cells and twelve fixed trees of a standard Tents field; the 56
  addressed numbered cells of the order-six Dominosa control; the fourteen
  fixed island vertices of the scoped Bridges field; the 49 addressed cells,
  41 white positions and eight walls of the scoped Light Up field; the 121
  dots, 220 permitted edges and 100 faces of the scoped Loopy field; the 300
  fixed cells and 30 persistent regions of the scoped Map field; the 49 cells,
  84 internal adjacencies and 12 centre dots of the scoped Galaxies field; the
  117 addressed cells of the scoped Filling field; the 36 cells and 16 fixed
  cage memberships of the scoped Keen field; the 64 cell-centre vertices and
  fixed orthogonal adjacency graph of the scoped Pearl field; the 25 fixed
  positions and immutable tile-shape inventory of the scoped Net field; the
  nine occupied cells and fixed finite tile inventory of scoped Netslide.
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
  [Can of Wormholes decomposition](../games/a-f/can-of-wormholes.md), and
  [A Monster's Expedition decomposition](../games/a-f/a-monsters-expedition.md),
  [Tactical Breach Wizards decomposition](../games/s-z/tactical-breach-wizards.md), and
  [Hexologic decomposition](../games/g-l/hexologic.md), and
  [Slant decomposition](../games/s-z/slant.md), and
  [Tents decomposition](../games/s-z/tents.md), and
  [Loopy decomposition](../games/g-l/loopy.md),
  [Map decomposition](../games/m-r/map.md), and
  [Galaxies decomposition](../games/g-l/galaxies.md), and
  [Filling decomposition](../games/a-f/filling.md), and
  [Keen decomposition](../games/g-l/keen.md), and
  [Signpost decomposition](../games/s-z/signpost.md), and
  [Net decomposition](../games/m-r/net.md), and
  [Netslide decomposition](../games/m-r/netslide.md), and
  [The Talos Principle decomposition](../games/s-z/the-talos-principle.md).
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
  edge-flip constraints; the two independent binary invariants that restrict a
  classic `5 × 5` Lights Out board to one of four reachability classes; the
  even outer-tile permutation class generated by length-three Netslide shifts.
- Excludes: capacity alone; a local collision rule; a target that is difficult
  but not structurally unreachable.
- Parameters: component classes, state representation, orientation or binary
  coordinates and invariant equations.
- Evidence: [Rubik's Cube decomposition](../games/m-r/rubiks-cube.md),
  [Lights Out decomposition](../games/g-l/lights-out.md), and
  [Netslide decomposition](../games/m-r/netslide.md).
- Novelty: not assessed.

## CON-005 — Primitive action reversibility

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: every primitive legal state-changing action has a legal inverse
  that restores the immediately preceding state without a random or irreversible
  side effect.
- Includes: a Rubik's Cube face turn followed by the opposite turn; pressing
  the same Lights Out button twice with no intervening input; shifting one
  Netslide line and then shifting that line one step in the opposite direction.
- Excludes: undo supplied as an interface convenience; a move followed by an
  automatic random spawn; recoverability only through a restart.
- Parameters: inverse notation and primitive-action granularity.
- Evidence: [Rubik's Cube decomposition](../games/m-r/rubiks-cube.md),
  [Lights Out decomposition](../games/g-l/lights-out.md), and
  [Netslide decomposition](../games/m-r/netslide.md).
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
- Definition: a commanded transformation of one currently active or selected
  multi-cell element is legal only when its complete transformed footprint and
  required swept region remain inside the permitted field and do not overlap
  other occupancy, except at a separately declared completion boundary.
- Includes: rejecting a tetromino translation or rotation through a wall,
  floor or settled block in NES Tetris; rejecting a Rush Hour vehicle slide
  whose rigid footprint would cross another vehicle or the closed grid wall.
- Excludes: capacity without an active element; global reachability invariants;
  collision that automatically merges compatible elements.
- Parameters: element geometry, field boundary, rotation model, swept-region
  rule, completion-boundary exception and collision sampling time.
- Evidence: [Tetris decomposition](../games/s-z/tetris.md) and
  [Rush Hour decomposition](../games/m-r/rush-hour.md).
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
- Includes: the printed clue digits in a standard Sudoku puzzle; the thirteen
  initially coloured, uneditable regions of the scoped Map control; the 47
  printed digits in the scoped Filling control.
- Excludes: player-entered tentative values; concealed values revealed later;
  fixed obstacles that carry no value from the assignment domain.
- Parameters: number, placement and symmetry of the given assignments.
- Evidence: [Sudoku decomposition](../games/s-z/sudoku.md) and
  [Map decomposition](../games/m-r/map.md), and
  [Filling decomposition](../games/a-f/filling.md).
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
  Sudoku; the row and column constraints of scoped 6 × 6 Keen; the complete
  16-cell Signpost field covering ordinal labels 1 through 16 exactly once.
- Excludes: approximate totals; pairwise inequality without complete domain
  coverage; exact local counts of concealed hazards.
- Parameters: symbol domain, unit size, unit topology and overlap pattern.
- Evidence: [Sudoku decomposition](../games/s-z/sudoku.md),
  [Keen decomposition](../games/g-l/keen.md), and
  [Signpost decomposition](../games/s-z/signpost.md).
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
  every ordered body segment occupies a distinct cell; Can of Wormholes walls
  and current worm segments rejecting endpoint entry while segments remain
  exclusively placed; A Monster's Expedition rock and stump cells stopping
  log motion while its monster, log and bridge occupy compatible positions.
- Excludes: finite capacity alone; compatibility-based collision merging;
  invariant restrictions over otherwise representable arrangements.
- Parameters: board topology, barrier geometry and occupying entity classes.
- Evidence: [Sokoban decomposition](../games/s-z/sokoban.md) and
  [Into the Breach decomposition](../games/g-l/into-the-breach.md), and
  [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md), and
  [Patrick's Parabox decomposition](../games/m-r/patricks-parabox.md), and
  [Stephen's Sausage Roll decomposition](../games/s-z/stephens-sausage-roll.md),
  [Snakebird decomposition](../games/s-z/snakebird.md), and
  [Tactical Breach Wizards decomposition](../games/s-z/tactical-breach-wizards.md), and
  [Can of Wormholes decomposition](../games/a-f/can-of-wormholes.md), and
  [A Monster's Expedition decomposition](../games/a-f/a-monsters-expedition.md).
- Novelty: not assessed.

## CON-012 — Push-only access geometry

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a movable object may change position only when the agent can
  occupy the position immediately behind it and the position immediately ahead
  is free; only one object may be displaced and pulling is unavailable.
- Includes: the single-crate push restriction in Sokoban; reaching the chosen
  side of one A Monster's Expedition log before tipping or rolling it.
- Excludes: direct object selection; pulling from an adjacent cell; pushing a
  chain of two or more objects; automatic gravity.
- Parameters: adjacency topology, object count per push and access direction.
- Evidence: [Sokoban decomposition](../games/s-z/sokoban.md) and
  [A Monster's Expedition decomposition](../games/a-f/a-monsters-expedition.md).
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
  legal head moves; settling the only A Monster's Expedition log in water with
  an orientation that leaves walking possible but denies the target bridge.
- Excludes: an explicit terminal-loss transition; a reversible setback; a state
  that merely requires more moves than expected.
- Parameters: deadlock pattern, target equivalence and whether the system
  detects the deadlock.
- Evidence: [Sokoban decomposition](../games/s-z/sokoban.md) and
  [Peg Solitaire decomposition](../games/m-r/peg-solitaire.md), and
  [Patrick's Parabox decomposition](../games/m-r/patricks-parabox.md), and
  [A Good Snowman Is Hard to Build decomposition](../games/a-f/a-good-snowman-is-hard-to-build.md),
  [Snakebird decomposition](../games/s-z/snakebird.md), and
  [A Monster's Expedition decomposition](../games/a-f/a-monsters-expedition.md).
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
  remaining scoring Hands in a Balatro Blind; the ten proposal rows of the
  scoped compact Mastermind board; Wordle's six accepted guess rows.
- Excludes: elapsed real time; optional solution-efficiency scoring; a resource
  that can reach zero without terminating the attempt.
- Parameters: initial allowance, charged action classes, extension rules and
  exact objective-check timing.
- Evidence: [Royal Match decomposition](../games/m-r/royal-match.md) and
  [Balatro decomposition](../games/a-f/balatro.md), and
  [Mastermind decomposition](../games/m-r/mastermind.md), and
  [Wordle decomposition](../games/s-z/wordle.md).
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
  the knight's ability to cross intervening squares; Rush Hour cars and trucks
  remaining on their initial horizontal or vertical axis and stopping before
  intervening vehicles.
- Excludes: one shared adjacency rule for every piece; collision constraints on
  a freely transformed multi-cell object; ownership and king safety.
- Parameters: piece classes, movement vectors, path rule, invariant or mutable
  orientation, directionality and initial-move exceptions.
- Evidence: [Chess decomposition](../games/a-f/chess.md) and
  [Rush Hour decomposition](../games/m-r/rush-hour.md).
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
- Includes: connecting the two dots of one colour in Flow Free; joining the two
  hollow terminals of one LYNE shape family.
- Excludes: connecting arbitrary terminals; a route whose destination is not
  fixed by its source identity; movable endpoints.
- Parameters: number of pairs, label domain and endpoint placement.
- Evidence: [Flow Free decomposition](../games/a-f/flow-free.md), and
  [LYNE decomposition](../games/g-l/lyne.md).
- Novelty: not assessed.

## CON-029 — Topology-contiguous simple path

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each route is one unbranched sequence of distinct board positions
  in which every consecutive pair is adjacent under the instance's declared
  path topology.
- Includes: a classic Flow Free pipe turning through horizontally or vertically
  adjacent squares without branching or revisiting a cell; one Cosmic Express
  route traversing logically edge-adjacent isometric grid cells without a
  junction, revisit or self-crossing; a The Witness trace following adjacent
  grid-graph vertices from a start circle to an end cap without branching,
  revisiting or self-crossing; a LYNE route using horizontal, vertical or
  diagonal neighbour links among its displayed shape positions; one Signpost
  sequence visiting distinct cells under directed arrow-ray adjacency; one
  Strands word path changing direction across horizontal, vertical or diagonal
  neighbours without revisiting a letter cell.
- Excludes: adjacency not declared by the instance; branched networks;
  disconnected cells of one route; paths that leave and re-enter the board.
- Parameters: adjacency topology, turn count, route length and board boundary.
- Evidence: [Flow Free decomposition](../games/a-f/flow-free.md) and
  [Cosmic Express decomposition](../games/a-f/cosmic-express.md), and
  [The Witness decomposition](../games/s-z/the-witness.md), and
  [LYNE decomposition](../games/g-l/lyne.md), and
  [Signpost decomposition](../games/s-z/signpost.md), and
  [Strands decomposition](../games/s-z/strands.md).
- Novelty: not assessed.

## CON-030 — Exclusive path-cell occupancy

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: every ordinary board position may belong to at most one completed
  route, so distinct routes cannot cross or overlap there; any explicitly
  shared junction is a separately declared exception with its own capacity.
- Includes: non-crossing, non-overlapping Flow Free pipes on a classic board.
- Includes: LYNE shape positions remaining exclusive except for neutral nexus
  nodes that explicitly admit several route traversals.
- Includes: horizontal and vertical Bridges corridors being unable to occupy
  the same ordinary intervening position.
- Includes: distinct accepted Strands theme-word paths claiming disjoint letter
  cells in the final grid partition.
- Excludes: unrestricted crossing; bridge cells carrying two routes on separate
  layers; ordinary piece occupancy without route continuity.
- Parameters: position capacity, permitted bridge classes and endpoint sharing.
- Evidence: [Flow Free decomposition](../games/a-f/flow-free.md), and
  [LYNE decomposition](../games/g-l/lyne.md), and
  [Bridges decomposition](../games/a-f/bridges.md), and
  [Strands decomposition](../games/s-z/strands.md).
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
  and committing one held action card per play; Slay the Spire exposing a
  bounded combat hand and committing one held card per ordinary play.
- Excludes: a one-card temporary buffer; hidden hand contents; an unlimited
  subset selected directly from the draw pile.
- Parameters: hand capacity, minimum and maximum commit size and effects that
  alter either limit.
- Evidence: [Balatro decomposition](../games/a-f/balatro.md),
  [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md),
  and [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
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
  formed by multiple named lines sharing a station; circular Cities: Skylines
  public-transport lines whose stops form one ordered route.
- Excludes: arbitrary branching rail graphs within one line; simple paths that
  prohibit shared transfer nodes; pipe-port flow networks.
- Parameters: loop permission, station revisit rule, maximum stops and route
  geometry rendering.
- Evidence: [Mini Metro decomposition](../games/m-r/mini-metro.md) and
  [Cities: Skylines decomposition](../games/a-f/cities-skylines.md).
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
  its current passenger alights; bounded bus, metro and train vehicle capacity
  in Cities: Skylines.
- Excludes: station crowd capacity; total vehicle inventory; route length.
- Parameters: base capacity, carriage increment, pickup priority and special
  rolling stock.
- Evidence: [Mini Metro decomposition](../games/m-r/mini-metro.md),
  [Cosmic Express decomposition](../games/a-f/cosmic-express.md) and
  [Cities: Skylines decomposition](../games/a-f/cities-skylines.md).
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

## CON-052 — Sustained service-node overload termination

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: exceeding a node's waiting-demand capacity starts a visible
  grace countdown, relief can arrest or reverse it, and allowing any countdown
  to fill ends the session.
- Includes: Classic-mode Mini Metro station overcrowding; a Mini Motorways
  destination retaining excess pins until its visible overload timer fills.
- Excludes: immediate failure at the first excess unit; vehicle capacity;
  non-terminal congestion penalties; a fixed external time limit.
- Parameters: station capacity, grace duration, recovery rate, train-presence
  interaction and interchange capacity.
- Evidence: [Mini Metro decomposition](../games/m-r/mini-metro.md) and
  [Mini Motorways decomposition](../games/m-r/mini-motorways.md).
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

## CON-054 — Forward-only monotonic active-set reduction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: every successful ordinary forward action removes a non-empty
  bounded set of active puzzle elements, and no ordinary forward action
  restores a removed element or increases that active set.
- Includes: traditional Peg Solitaire without reverse jumps, where each jump
  removes exactly one peg; HOOK levels 1–7, where an accepted trigger removes
  its one or several linked line mechanisms.
- Excludes: an interface undo; reversible “unjump” variants; games whose count
  can both increase and decrease through ordinary actions.
- Parameters: initial active set, per-action removal multiplicity, element
  identity and reverse-move policy.
- Evidence: [Peg Solitaire decomposition](../games/m-r/peg-solitaire.md) and
  [HOOK decomposition](../games/g-l/hook.md).
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
  compatible types connect into one relation, incompatible types do not or
  make that adjacency illegal, and declared corridor or port types may
  additionally forbid blocked endings.
- Includes: Dorfromantik matching forests, houses, fields, water, rivers and
  railways across adjacent hex edges, including stricter river and rail exits.
- Includes: Carto permitting square map fragments to touch only where their
  road, river, forest, plain or other terrain boundary patterns match.
- Includes: Net requiring a port on one tile edge to face a reciprocal port on
  its orthogonal neighbour, with no outward port at a non-wrapping boundary.
- Includes: Netslide evaluating the same reciprocal tile ports against a
  stationary easy-mode barrier graph after every line permutation.
- Excludes: reciprocal pipe ports carrying a live directed flow whose timing
  and termination matter; colour-only endpoint identity; visual adjacency with
  no mechanical evaluation.
- Parameters: tile topology, edge-type vocabulary, compatibility relation,
  corridor exceptions and whether a mismatch is forbidden or merely penalised.
- Evidence: [Dorfromantik decomposition](../games/a-f/dorfromantik.md),
  [Carto decomposition](../games/a-f/carto.md), and
  [Net decomposition](../games/m-r/net.md), and
  [Netslide decomposition](../games/m-r/netslide.md).
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
  beyond supported Level 1 space before entering the exit; a complete required
  Can of Wormholes body dissolving after it loses platform support.
- Excludes: recoverable offscreen motion; fixed-board entry obstruction;
  exposing a concealed hazard; voluntary restart.
- Parameters: boundary geometry, required object, support rule, completion-
  check precedence and restart behaviour.
- Evidence: [Cut the Rope decomposition](../games/a-f/cut-the-rope.md) and
  [Stephen's Sausage Roll decomposition](../games/s-z/stephens-sausage-roll.md),
  [Snakebird decomposition](../games/s-z/snakebird.md), and
  [Can of Wormholes decomposition](../games/a-f/can-of-wormholes.md).
- Novelty: not assessed.

## CON-062 — Static facility-footprint placement compatibility

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: persistent machine or facility components may be committed only
  when their declared static footprints and exclusive anchor positions do not
  overlap an incompatible placed component, terrain locus or fixed port.
- Includes: Opus Magnum preventing arm bases, glyphs, tracks and reagent or
  product ports from occupying forbidden shared hexes while allowing declared
  exceptions such as a track beneath an arm base; Infinifactory preventing a
  conveyor or support voxel from overlapping an incompatible component, fixed
  hatch, output device or immutable environment footprint; Factorio rejecting
  a live entity whose footprint overlaps an incompatible entity or terrain;
  Frostpunk rejecting a building that overlaps occupied crater space.
- Excludes: collisions caused later by moving arms or molecules; finite board
  capacity; adjacency requirements between placed tiles.
- Parameters: footprint shapes, orientation, component-pair compatibility and
  allowed overlay exceptions.
- Evidence: [Opus Magnum decomposition](../games/m-r/opus-magnum.md),
  [Infinifactory decomposition](../games/g-l/infinifactory.md), and
  [Factorio decomposition](../games/a-f/factorio.md).
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
  permissions; Split Fiction binding Chapter 1's temporary pilot and gunner
  interactions to different members of the Mio/Zoe pair.
- Excludes: cosmetic character differences; identical units with different
  positions; combat-class effectiveness without traversal or interaction locks.
- Parameters: actor classes, traversal edges, interaction catalogue, carried
  state, switchability and whether permissions can change during a level.
- Evidence: [Timelie decomposition](../games/s-z/timelie.md) and
  [Pikmin 4 decomposition](../games/m-r/pikmin-4.md), and
  [Split Fiction decomposition](../games/s-z/split-fiction.md).
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

## CON-090 — Oriented agent-plus-body sweep clearance

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an oriented agent and one directly coupled front-offset body
  occupy an ordered multi-cell footprint; translation and rotation are legal
  only when every destination and swept clearance cell is compatible.
- Includes: Stephen's Sausage Roll requiring the player cell, current fork,
  future fork and fourth corner of the two-by-two turn area to be clear;
  Bonfire Peaks requiring the avatar, front-carried crate and its swept corner
  to clear walls and occupied stair geometry.
- Excludes: ordinary single-cell avatar collision; viewpoint rotation; a
  held item with no occupied world cell; an independently pushed object; a
  coupled body's separate support or elevation rule.
- Parameters: attachment permanence, coupling action, body identity, offset,
  orientation set, sweep geometry, entity-specific terrain compatibility and
  contact exceptions.
- Evidence: [Stephen's Sausage Roll decomposition](../games/s-z/stephens-sausage-roll.md)
  and [Bonfire Peaks decomposition](../games/a-f/bonfire-peaks.md).
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
  cards spending shared Momentum before its next-turn restoration; Slay the
  Spire cards spending shared Energy that ordinarily resets each player turn.
- Excludes: one move and one ability allocated to each controlled unit; a
  finite non-renewing level move count; a card-use predicate based only on
  combo threshold with no shared payment pool.
- Parameters: starting value, maximum value, refresh amount, card costs,
  modifiers and permitted carry-over.
- Evidence: [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md)
  and [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
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

## CON-098 — Origin class restricts automatic demand service

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an automatically requested service trip may be supplied only by
  a currently available origin-bound vehicle whose declared class matches the
  requesting node's class.
- Includes: a red Mini Motorways destination dispatching a car from a connected
  red house while connected blue-house cars remain ineligible.
- Excludes: a passenger naming the class of destination where it exits;
  unrestricted nearest-vehicle dispatch; colour used only to decorate roads.
- Parameters: class encoding, origin choice, simultaneous requests and
  colour-blind representation.
- Evidence: [Mini Motorways decomposition](../games/m-r/mini-motorways.md).
- Novelty: not assessed.

## CON-099 — Elevation-conditioned road-crossing connectivity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: crossing road strokes connect and exchange traffic only when
  their local elevation bands coincide; a grade-separated crossing preserves
  two independent directed paths.
- Includes: a Freeways ground road forming an intersection with another ground
  road, while a raised ramp passing over it creates no turning connection.
- Excludes: a cosmetic bridge with no routing effect; two non-crossing paths;
  an inventory cost for crossing water.
- Parameters: elevation bands, snapping tolerance, slope limit, same-level
  junction construction and route-graph update order.
- Evidence: [Freeways decomposition](../games/a-f/freeways.md).
- Novelty: not assessed.

## CON-100 — Carried front-offset sweep clearance

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical Bonfire Peaks-specific form of oriented
  agent-plus-body sweep clearance, merged into `CON-090` after reversible
  carrying and permanent attachment were confirmed to be coupling parameters
  rather than different legality predicates.
- Includes: historical references to a carried Bonfire Peaks crate swinging
  around the avatar and being blocked by occupied stair or wall geometry.
- Excludes: new game signatures; use `CON-090` for destination and swept-cell
  clearance, and a separate gene for support or elevation legality.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Bonfire Peaks decomposition](../games/a-f/bonfire-peaks.md).
- Merged into: `CON-090` by
  [`TAXONOMY_CHANGE_009`](../../research/taxonomy-changes/TAXONOMY_CHANGE_009.md).
- Novelty: not assessed.

## CON-101 — Carry-conditioned elevation traversal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the avatar may traverse an adjacent one-step elevation change
  only when both its own destination and the vertically offset destination of
  any front-carried object satisfy the authored clearance relation; carrying
  therefore makes some forward ascents illegal while a differently oriented
  or backward approach remains legal.
- Includes: routing the Bonfire Peaks protagonist and belongings crate up the
  stepped `Burn Your Belongings` structure by respecting the crate's position
  in front of the climber.
- Excludes: unrestricted jumping; flat-grid push access; a global height limit
  unrelated to carried state; continuously simulated climbing physics.
- Parameters: permitted step height, avatar facing, carried-object offset,
  headroom, support cells and forward/backward asymmetry.
- Evidence: [Bonfire Peaks decomposition](../games/a-f/bonfire-peaks.md).
- Novelty: not assessed.

## CON-102 — Collision-free synchronous vehicle occupancy

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during a shared-clock multi-vehicle traversal, no two uncoupled
  vehicles may occupy or enter one declared conflict region at the same
  resolution step; a temporal conflict fails the bounded attempt even when
  every route is geometrically connected.
- Includes: routing Railbound carriages so they do not crash at a shared tile or
  junction while advancing simultaneously.
- Excludes: static exclusive occupancy without automatic motion; road-traffic
  queues that reduce throughput but remain valid; collision between opponents.
- Parameters: conflict-region geometry, movement step, edge-swap handling,
  junction priority, coupling exception and failure timing.
- Evidence: [Railbound decomposition](../games/m-r/railbound.md).
- Novelty: not assessed.

## CON-103 — Finite non-renewing spatial-command hand

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a bounded spatial puzzle begins with a visible finite multiset of
  selectable command cards; every ordinary forward action permanently removes
  exactly the chosen card identity from that attempt, with no draw, reward or
  replenishment before reset or interface undo.
- Includes: choosing and consuming one exact-distance movement card per shot in
  an ordinary Golf Peaks World 1 hole.
- Excludes: a renewable turn hand; a fixed ordered queue; a numeric move counter
  whose actions are otherwise always available; a replenishable tile supply.
- Parameters: card multiset, selectable order, duplicate identities, target
  parameter, undo restoration, zero-card state and completion priority.
- Evidence: [Golf Peaks decomposition](../games/g-l/golf-peaks.md).
- Novelty: not assessed.

## CON-104 — Finite all-used construction inventory

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a bounded construction puzzle begins with a visible finite
  multiset of persistent pieces; each ordinary forward placement permanently
  consumes exactly the selected identity, no new piece is supplied during the
  attempt, and successful completion requires every supplied identity to have
  been placed.
- Includes: using all food pieces supplied for one Chapter 1 inbento recipe;
  using the collected green `L`, `J` and `Z` exactly once in The Talos
  Principle's first A1 arranger.
- Excludes: an optional finite inventory; a replenishable stack; a hand of
  command cards whose effects do not remain as the constructed output; a move
  counter whose actions are otherwise always available.
- Parameters: initial multiset, duplicate identities, selectable order,
  placement persistence, undo restoration and completion-check priority.
- Evidence: [inbento decomposition](../games/g-l/inbento.md) and
  [The Talos Principle decomposition](../games/s-z/the-talos-principle.md).
- Novelty: not assessed.

## CON-105 — Complete footprint contained by placement boundary

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a rigid multi-position piece may be committed only when every
  non-empty position of its transformed footprint maps to an address inside
  the fixed receiving container; compatible or replaceable existing contents
  do not relax the outer-boundary test.
- Includes: rejecting an inbento food-piece pose if any occupied block lies
  outside the bento grid, while permitting blocks wholly inside to cover food;
  retaining all four cells of each Talos sigil inside its 4 × 3 arranger.
- Excludes: collision-free placement that additionally forbids occupied cells;
  fitting an articulated body to a target; clipping a visual layer at a frame;
  a capacity total with no addressed outer boundary.
- Parameters: footprint geometry, orientation, anchor, container topology,
  empty piece blocks and rejection behaviour.
- Evidence: [inbento decomposition](../games/g-l/inbento.md) and
  [The Talos Principle decomposition](../games/s-z/the-talos-principle.md).
- Novelty: not assessed.

## CON-106 — Unobstructed swept withdrawal path

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a triggered mechanism can be removed successfully only if every
  point of its declared withdrawal sweep is free of every still-active
  blocking line, hook or trigger-linked mechanism.
- Includes: retracting a HOOK line only after the line or hook caught across
  its withdrawal path has already been removed.
- Excludes: static placement overlap; two independently moving vehicles sharing
  a clock; a path that remains legal but slow under congestion; collision after
  a mechanism has already disappeared.
- Parameters: moving footprint, sweep curve, blocking classes, crossing depth,
  simultaneous linked motion and collision-reset policy.
- Evidence: [HOOK decomposition](../games/g-l/hook.md).
- Novelty: not assessed.

## CON-107 — Exact shared-junction traversal capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a declared neutral junction exposes an exact positive traversal
  count, may be shared across otherwise exclusive routes, and is satisfied only
  when the completed route set passes through it exactly that many times.
- Includes: a LYNE nexus carrying two visible pips and receiving exactly two
  route passages from the scoped triangle and diamond families.
- Excludes: an ordinary exclusive path position; an unlimited crossing; two
  routes crossing on separate bridge layers; a maximum capacity that need not
  be filled.
- Parameters: required count, eligible route families, whether one route may
  contribute more than once, entry reuse and displayed notation.
- Evidence: [LYNE decomposition](../games/g-l/lyne.md).
- Novelty: not assessed.

## CON-108 — Typed waypoint inclusion on matched path

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: every ordinary marker of one declared route family must be
  visited by that family's single endpoint-to-endpoint path, and no other
  family may claim that typed marker.
- Includes: one LYNE triangle path visiting every solid triangle between its
  two hollow triangle terminals, and the diamond path doing the same for every
  diamond.
- Excludes: optional waypoints; full occupancy of unmarked board space; pairing
  endpoints without required intermediate markers; neutral shared junctions
  with no route-family identity.
- Parameters: family vocabulary, marker count, endpoint notation, visitation
  multiplicity and whether every board position is a marker.
- Evidence: [LYNE decomposition](../games/g-l/lyne.md).
- Novelty: not assessed.

## CON-109 — Overlapping exact line-aggregate satisfaction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: every declared line constrains the sum of one numeric value or
  selected-state indicator from each member position to equal one exact target,
  and a position shared by several lines contributes its same single assigned
  value to every such equation.
- Includes: assigning one, two or three pips to Hexologic cells so each visible
  horizontal or diagonal arrow-line reaches its exact edge total; assigning
  tent / non-tent binary states so every Tents row and column contains its
  displayed exact number of tents.
- Excludes: all-different unit coverage; an ordered run-length description; a
  count of concealed members of one target class; inequalities or approximate
  totals; a local count around one vertex or face; independent arithmetic
  questions with no shared assignment.
- Parameters: numeric or binary-indicator domain, selected state, line
  membership, orientation, target total, intersection topology, completeness
  rule, partial-violation feedback and whether targets are unique.
- Evidence: [Hexologic decomposition](../games/g-l/hexologic.md) and
  [Tents decomposition](../games/s-z/tents.md).
- Novelty: not assessed.

## CON-110 — Coordinate-wise ternary same-or-all-different subset predicate

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: exactly three distinct elements form a legal subset only when,
  for every declared three-valued coordinate independently, the three values
  are either all equal or all different.
- Includes: validating three SET cards across number, colour, shape and shading,
  where a two-plus-one split in any attribute rejects the whole candidate.
- Excludes: ordinary equality matching; a ranked hierarchy of card patterns;
  all-different coverage across more than three assigned positions; similarity
  scoring that allows some coordinates to fail.
- Parameters: coordinate count, value labels, eligible element zone, fixed
  subset size and whether a valid subset is removed after acceptance.
- Evidence: [SET decomposition](../games/s-z/set.md).
- Novelty: not assessed.

## CON-111 — Exact cardinality of spatial hypothesis

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a complete spatial occupancy proposal must mark exactly the
  declared number of distinct positions before global adjudication is
  available.
- Includes: default Black Box requiring exactly five guessed ball cells before
  Check can evaluate the layout.
- Excludes: a maximum number of optional annotations; a finite action budget;
  placing all pieces from a visible inventory; exact coverage whose members
  are already revealed.
- Parameters: required count, field size, allowed position classes,
  duplicate-position policy and incomplete-submission feedback.
- Evidence: [Black Box decomposition](../games/a-f/black-box.md).
- Novelty: not assessed.

## CON-112 — Fixed-length lexicon membership gate

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a complete ordered-symbol proposal becomes an eligible query
  only when it has the declared exact length and belongs to the system's
  accepted lexicon; rejected strings do not consume the query allowance.
- Includes: Wordle accepting a recognised five-letter word as a scored guess
  while rejecting incomplete or unrecognised entries without spending a row.
- Excludes: unrestricted sequences over a finite symbol vocabulary; typed
  semantic slots with separately visible admissible tokens; a clue-reuse rule
  imposed on otherwise recognised words; answer frequency as a strategy.
- Parameters: sequence length, language, accepted-guess lexicon, answer-pool
  relation, normalisation, proper-name policy and rejection feedback.
- Evidence: [Wordle decomposition](../games/s-z/wordle.md).
- Novelty: not assessed.

## CON-113 — Visible trajectory hazard contact is terminal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: if a designated moving body contacts any currently visible
  hazard anywhere along one committed trajectory, the current attempt ends
  before completion can be credited.
- Includes: Inertia's ball entering a displayed mine while sliding, including
  after collecting the final remaining gem earlier in the same move; a
  Stereo Madness cube or ship touching a visible spike before the finish.
- Excludes: exposing a previously concealed hazard; falling beyond a supported
  boundary; recoverable damage; a blocked command that never enters a hazard;
  a hazard that merely removes optional score.
- Parameters: hazard class, contact geometry, completion-versus-failure
  precedence, feedback and recovery interface.
- Evidence: [Inertia decomposition](../games/g-l/inertia.md) and
  [Geometry Dash decomposition](../games/g-l/geometry-dash.md).
- Novelty: not assessed.

## CON-114 — Exact incident-edge degree at marked vertex

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: each marked graph vertex requires the number of selected edges
  terminating at that vertex to equal its displayed integer exactly, while one
  selected edge may contribute to the degree of both endpoints.
- Includes: a numbered Slant intersection requiring exactly zero through four
  incident cell diagonals; a Bridges island requiring the sum of incident
  single and double bridge multiplicities to equal its clue.
- Excludes: an arithmetic sum of values along a line; ordered run lengths; an
  all-different unit; an unmarked vertex with no local degree requirement.
- Parameters: edge domain, maximum boundary degree, clue range, incidence
  geometry, whether every vertex is marked and partial-violation feedback.
- Evidence: [Slant decomposition](../games/s-z/slant.md) and
  [Bridges decomposition](../games/a-f/bridges.md).
- Novelty: not assessed.

## CON-115 — Global acyclicity of selected linkage graph

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: across the entire selected-edge graph, no newly selected linkage
  may connect two vertices already in the same connected component, so every
  completed component remains a tree rather than closing a cycle.
- Includes: forbidding every loop formed by Slant diagonals, including loops
  whose vertices carry no numeric clue; forbidding any closed reciprocal-port
  path in a completed Net or Netslide network.
- Excludes: preventing one traced path from visiting a position twice; a graph
  required to form exactly one cycle; geometric non-crossing without a cycle
  predicate; reachability invariants unrelated to linkage topology.
- Parameters: vertex and edge definitions, component scope, parallel-edge
  policy, whether disconnected trees are allowed and violation feedback.
- Evidence: [Slant decomposition](../games/s-z/slant.md),
  [Net decomposition](../games/m-r/net.md), and
  [Netslide decomposition](../games/m-r/netslide.md).
- Novelty: not assessed.

## CON-116 — Overlapping exact line cardinality

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: every declared line requires the number of positions assigned one
  selected binary value to equal its displayed integer exactly, while a shared
  position contributes once to every intersecting line that contains it.
- Includes: each Tents row and column containing exactly its displayed number
  of tents.
- Excludes: ordered filled-run descriptions; sums of non-binary numeric values;
  an all-different unit; a local count around one vertex.
- Parameters: line topology, selected value, target range, intersection pattern
  and partial-violation feedback.
- Evidence: [Tents decomposition](../games/s-z/tents.md).
- Replaced by: `CON-109`.
- Novelty: not assessed.

## CON-117 — King-neighbourhood exclusion for selected cells

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: assigning the selected occupancy value to one grid cell forbids
  that same value in every existing horizontally, vertically or diagonally
  neighbouring cell.
- Includes: no two Tents tents sharing an edge or corner.
- Excludes: ordinary single-occupancy capacity; orthogonal-only separation;
  collision between moving footprints; a minimum distance measured outside a
  fixed cell neighbourhood.
- Parameters: neighbourhood topology, selected identity, boundary clipping and
  violation feedback.
- Evidence: [Tents decomposition](../games/s-z/tents.md).
- Novelty: not assessed.

## CON-118 — Adjacency-constrained perfect bipartite matching

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: two complete finite identity sets are valid only when every
  member of each set can participate in exactly one pair and every chosen pair
  satisfies a declared spatial adjacency relation.
- Includes: pairing every Tents tent one-to-one with every tree through
  orthogonal cell adjacency, even when a tent is adjacent to additional trees.
- Excludes: requiring each member to have at least one neighbour without a
  global one-to-one pairing; matching fixed endpoint identities along paths;
  merging equal pieces; nearest-neighbour scoring.
- Parameters: two identity sets, allowed adjacency graph, equality of set
  cardinalities, whether pair identities must be displayed and failure
  feedback.
- Evidence: [Tents decomposition](../games/s-z/tents.md).
- Novelty: not assessed.

## CON-119 — Exact-once adjacent-pair cover

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a complete selection of allowed adjacent two-position relations
  is valid only when every position belongs to exactly one selected relation,
  leaving neither uncovered positions nor shared endpoints.
- Includes: covering all 56 cells of order-six Dominosa with 28 non-overlapping
  orthogonal dominoes.
- Excludes: ordinary one-object-per-cell capacity; covering a region with
  pieces of variable size; matching two pre-existing identity sets; allowing
  optional uncovered cells.
- Parameters: position topology, adjacency relation, pair count, boundary
  conditions and partial-violation feedback.
- Evidence: [Dominosa decomposition](../games/a-f/dominosa.md).
- Novelty: not assessed.

## CON-120 — Complete unordered pair-type usage

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: across a complete set of selected two-member relations, every
  unordered type drawn from a declared finite value domain must occur exactly
  once, including equal-value pairs.
- Includes: using each Dominosa domino type `0-0` through `6-6` exactly once.
- Excludes: using each individual object once without regard to pair type;
  ordered sequence pairs; merely forbidding duplicate pairs without requiring
  the complete type inventory; equality-only matching.
- Parameters: value domain, ordered-versus-unordered identity, treatment of
  doubles, required multiplicity and partial-violation feedback.
- Evidence: [Dominosa decomposition](../games/a-f/dominosa.md).
- Novelty: not assessed.

## CON-121 — Bounded parallel-link multiplicity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: every permitted vertex pair carries one integer linkage
  multiplicity from a fixed finite domain, with parallel links represented by
  increasing that value rather than creating independently addressed edges.
- Includes: each nearest-island pair in scoped Bridges carrying zero, one or
  two bridges.
- Excludes: one binary edge; an unlimited multigraph; several independently
  identified routes sharing endpoints; a visual double line with no numeric
  mechanical effect.
- Parameters: edge eligibility, minimum and maximum multiplicity, contribution
  to endpoint degree and editing cycle.
- Evidence: [Bridges decomposition](../games/a-f/bridges.md).
- Novelty: not assessed.

## CON-122 — Spanning connectivity of required vertices

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the subgraph induced by all required vertices and every selected
  positive-multiplicity linkage must form exactly one connected component.
- Includes: every island in Bridges being reachable from every other island by
  bridges, while cycles remain permitted in the scoped default rules.
- Includes: every fixed Net tile belonging to one reciprocal-port component,
  with acyclicity supplied separately by `CON-115`.
- Includes: every Netslide tile becoming reachable from its fixed centre through
  reciprocal unbarred ports after the line permutation is complete.
- Excludes: merely satisfying local degrees in several components; connecting
  only designated endpoint pairs; requiring acyclicity; connecting optional
  vertices only.
- Parameters: required vertex set, selected-link predicate, directionality,
  treatment of multiplicity and whether cycles are allowed.
- Evidence: [Bridges decomposition](../games/a-f/bridges.md),
  [Net decomposition](../games/m-r/net.md), and
  [Netslide decomposition](../games/m-r/netslide.md).
- Novelty: not assessed.

## CON-123 — Exact orthogonal-neighbour assignment cardinality

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: each marked blocking cell requires exactly its displayed number
  of existing orthogonally adjacent assignable cells to carry one declared
  selected value.
- Includes: a numbered Light Up wall requiring exactly zero through four bulbs
  immediately above, below, left and right.
- Excludes: incident-edge degree; a count across an entire row or column;
  diagonal neighbours; an unnumbered wall with no exact count.
- Parameters: neighbourhood topology, selected value, clue range, boundary
  clipping and partial-violation feedback.
- Evidence: [Light Up decomposition](../games/g-l/light-up.md).
- Novelty: not assessed.

## CON-124 — Mutual source visibility exclusion

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: no two selected source cells may share one unobstructed declared
  line of sight, even though overlapping their propagated effect elsewhere is
  permitted.
- Includes: forbidding two Light Up bulbs in the same wall-bounded row or
  column segment.
- Excludes: ordinary one-object-per-cell occupancy; route crossing exclusion;
  minimum geometric distance; collision between moving bodies.
- Parameters: source class, sight directions, blockers, range, endpoint
  inclusion and violation feedback.
- Evidence: [Light Up decomposition](../games/g-l/light-up.md).
- Novelty: not assessed.

## CON-125 — Complete visibility-ray coverage

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: every required traversable cell must belong to the declared
  propagation set of at least one selected source, including the source cell
  itself when specified.
- Includes: every white Light Up square being illuminated by a bulb in its own
  cell or on an unobstructed orthogonal ray.
- Excludes: occupying every cell with an object; connecting all graph vertices;
  covering only a target subset; revealing concealed contents.
- Parameters: required cell set, propagation geometry, blocker classes,
  source-cell inclusion and overlap allowance.
- Evidence: [Light Up decomposition](../games/g-l/light-up.md).
- Novelty: not assessed.

## CON-126 — Exact selected-edge cardinality around marked face

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: each marked face of a fixed embedded graph requires the number
  of selected boundary edges around that face to equal its displayed integer
  exactly.
- Includes: a numbered square in Loopy requiring exactly zero through three of
  its four sides to belong to the loop.
- Excludes: exact edge degree at a vertex; a count of selected cells in an
  orthogonal neighbourhood; a weighted sum of parallel links; an unmarked face
  with no local count.
- Parameters: face topology, boundary-edge multiplicity, clue range,
  contribution of shared edges and partial-violation feedback.
- Evidence: [Loopy decomposition](../games/g-l/loopy.md).
- Novelty: not assessed.

## CON-127 — Exactly one simple selected-edge cycle

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: every selected edge must belong to one non-empty connected
  component in which every incident vertex has selected degree two, so the
  complete selected subgraph is exactly one simple cycle.
- Includes: Loopy and Pearl accepting one unbroken loop and rejecting branches,
  open paths, isolated extra segments and two disjoint loops even when their
  respective local clues are satisfied.
- Excludes: merely requiring connectivity while permitting branches; global
  acyclicity; one traced endpoint-to-endpoint path; several independent cycles;
  a closed route that may revisit vertices.
- Parameters: selected-edge predicate, vertex and component scope, empty-state
  policy, parallel-edge policy and completion feedback.
- Evidence: [Loopy decomposition](../games/g-l/loopy.md) and
  [Pearl decomposition](../games/m-r/pearl.md).
- Novelty: not assessed.

## CON-128 — Shared-boundary adjacent-class exclusion

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: any two distinct fixed regions sharing a positive-length segment
  of boundary must receive different values from one common assignment domain.
- Includes: every boundary-adjacent pair of Map regions requiring different
  colours among the same four-colour palette.
- Excludes: regions that meet only at one point; all-different coverage across
  a multi-position unit; minimum-distance exclusion between selected cells;
  forbidding visual overlap without assigning region classes.
- Parameters: region topology, shared-boundary predicate, assignment domain,
  diagonal or point-contact policy and partial-conflict feedback.
- Evidence: [Map decomposition](../games/m-r/map.md).
- Novelty: not assessed.

## CON-129 — Exactly one centre marker per edge-bounded component

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: every orthogonally connected cell component induced by the
  selected boundary edges must contain exactly one fixed centre marker, so no
  completed component is markerless or contains multiple markers.
- Includes: every Galaxies region containing its one dot, including dots that
  lie at a cell centre, shared cell edge or grid vertex.
- Excludes: merely requiring one clue of any kind per region; assigning every
  cell directly to a marker without boundary-defined components; allowing a
  marker on a separating edge; requiring one selected object per fixed region.
- Parameters: component adjacency, marker positions, boundary convention,
  centre-cell ownership and partial-violation feedback.
- Evidence: [Galaxies decomposition](../games/g-l/galaxies.md).
- Novelty: not assessed.

## CON-131 — Connected equal-label region area equals label

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: every maximal component of positions joined through the declared
  adjacency relation and carrying one equal numeric label must contain exactly
  as many positions as that label specifies.
- Includes: every orthogonally connected region of digit `n` in Filling having
  exactly `n` cells, including a valid region with no original clue.
- Excludes: equal digits touching only diagonally; a pre-drawn region whose sum
  equals a clue; one clue per component; merely capping component size; a
  label that names a region without encoding its area.
- Parameters: adjacency relation, label domain, component maximality, clue
  requirement, partial-component feedback and completion timing.
- Evidence: [Filling decomposition](../games/a-f/filling.md).
- Novelty: not assessed.

## CON-130 — Half-turn closure about component centre

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: for every cell in a declared component, rotating that cell's
  centre by 180 degrees about the component's fixed centre marker must land on
  another cell in the same component.
- Includes: each connected Galaxies region being invariant under a half-turn
  about its own unique dot.
- Excludes: mirror symmetry; visual similarity without exact cell membership;
  rotating the whole board as an action; a symmetric initial layout whose
  completed regions need not preserve symmetry.
- Parameters: transformation angle, centre lattice, cell geometry, component
  definition, outer-boundary clipping and violation feedback.
- Evidence: [Galaxies decomposition](../games/g-l/galaxies.md).
- Novelty: not assessed.

## CON-132 — Exact arithmetic cage evaluation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the assigned numeric values in every fixed connected cage must
  combine under that cage's displayed arithmetic operation to equal its
  displayed target exactly.
- Includes: Keen addition and multiplication cages of two or more cells, and
  two-cell subtraction or division cages whose operand order is unrestricted.
- Excludes: one exact sum over a fixed straight line; a clue that pre-assigns
  one cell; all-different coverage within a cage; arithmetic performed only
  for scoring after an otherwise valid assignment.
- Parameters: cage topology, numeric domain, operation set, target, operand
  order, permitted cage size and partial-conflict feedback.
- Evidence: [Keen decomposition](../games/g-l/keen.md).
- Novelty: not assessed.

## CON-133 — Marked turn flanked by straight path cells

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: every marked path vertex must be a turn, and the immediately
  preceding and following vertices along the selected path must both be
  straight rather than turns.
- Includes: every black Pearl clue lying on a loop corner while both adjacent
  loop cells continue straight.
- Excludes: requiring only that the marked cell be a turn; testing geometric
  neighbours not consecutive on the selected path; requiring merely one
  straight neighbour; a turn prohibition around an unselected marker.
- Parameters: path topology, marker class, turn predicate, along-path adjacency,
  flanking distance and endpoint policy.
- Evidence: [Pearl decomposition](../games/m-r/pearl.md).
- Novelty: not assessed.

## CON-134 — Marked straight adjacent to a path turn

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: every marked path vertex must be straight, and at least one of
  its immediately preceding or following vertices along the selected path
  must be a turn.
- Includes: every white Pearl clue lying on a straight loop segment with a
  corner in at least one adjacent loop cell.
- Excludes: requiring both adjacent path cells to turn; testing every geometric
  neighbour rather than the two path neighbours; requiring only straightness;
  a clue outside the selected path.
- Parameters: path topology, marker class, straight predicate, along-path
  adjacency, existential side condition and endpoint policy.
- Evidence: [Pearl decomposition](../games/m-r/pearl.md).
- Novelty: not assessed.

## CON-135 — Arrow-ray consecutive-successor relation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: for every assigned ordinal value below the domain maximum, the
  position carrying its immediate successor must lie at positive distance on
  the fixed row, column or diagonal ray indicated by the first position.
- Includes: a Signpost cell numbered `n` pointing directly along its displayed
  arrow ray to the cell numbered `n+1`, with any number of intervening cells.
- Excludes: requiring geometric adjacency; merely increasing labels without a
  directional predicate; an arrow that moves an actor until collision; one
  fixed paired endpoint; selecting the nearest target only.
- Parameters: direction vocabulary, ray geometry, ordinal domain, permitted
  distance, endpoint convention and immutable-label positions.
- Evidence: [Signpost decomposition](../games/s-z/signpost.md).
- Novelty: not assessed.

## CON-136 — Persistent prerequisite-gated mechanism dependency

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an addressed mechanism operation is available only while every
  declared earlier exposure, acquisition, assembly or unlock state in its
  authored dependency set persists.
- Includes: The Room requiring the plate before screw removal, the recovered
  lens before eyepiece viewing, the crown-key unlock before ring access and all
  three matched rings before safe-door opening; Machinarium requiring torso
  exposure before assembly, the doll before leg recovery, both tool parts
  before combination and the prepared rig before arm recovery and exit.
  Cyberpunk 2077 likewise gates later main jobs, interactions and mechanisms
  behind persistent prior-job, acquisition and retained-choice state.
- Excludes: an action blocked only by current spatial collision; one fixed
  item–target type match with no earlier state; a purely presentational sequence
  that can be performed in any mechanical order.
- Parameters: dependency graph, prerequisite predicate, persistence, alternate
  branches, skipped states, reset scope and unavailable-action feedback.
- Evidence: [The Room decomposition](../games/s-z/the-room.md),
  [Machinarium decomposition](../games/m-r/machinarium.md),
  [The Longest Journey decomposition](../games/s-z/the-longest-journey.md), and
  [Day of the Tentacle decomposition](../games/a-f/day-of-the-tentacle.md), and
  [Stardew Valley decomposition](../games/s-z/stardew-valley.md), and
  [The Talos Principle decomposition](../games/s-z/the-talos-principle.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## CON-137 — Held-item configuration-to-fixture compatibility

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: applying one held articulated item to an addressed fixture is
  legal only when the item's committed functional configuration matches that
  fixture's fixed acceptance class.
- Includes: The Room's peculiar key requiring its spiral shape for the side
  lock and its crown shape for the front lock.
- Excludes: matching only item identity regardless of configuration; selecting
  an orientation after an item is already placed; static adjacent-edge matching;
  automatically consuming a carried key at any generic locked barrier.
- Parameters: item configuration domain, fixture class, symmetry equivalence,
  tolerance, rejection feedback, retention and post-use configuration.
- Evidence: [The Room decomposition](../games/s-z/the-room.md).
- Novelty: not assessed.

## CON-138 — Transient held-item state gates composite compatibility and use

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a held object may enter or enable a declared composite only while
  its temporary functional state satisfies compatibility, and the composite's
  addressed use remains legal only while that same state persists.
- Includes: The Longest Journey accepting the rubber ducky into the clamp-line
  assembly only while inflated and retrieving the track key only before the
  unpatched ducky's inflation expires.
- Excludes: permanent configuration-to-fixture matching; mere possession of
  two item identities; a recipe with no stateful constituent; a deadline that
  changes score but not action legality.
- Parameters: constituent identity, required temporary state, combination
  stage, usable interval, expiry transition, rejection feedback and retry rule.
- Evidence: [The Longest Journey decomposition](../games/s-z/the-longest-journey.md).
- Novelty: not assessed.

## CON-139 — Exact distinct typed hand-in set

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a disclosed multi-item commission completes only after one
  addressed recipient has accepted exactly one instance of every required
  distinct item type; unsupported identities, duplicate credit and incomplete
  proper subsets cannot satisfy the set.
- Includes: Day of the Tentacle requiring one oil, one vinegar and one
  gold-plated quill before Red Edison can construct the super-battery.
- Excludes: an unordered inventory retained by the player; a numeric resource
  cost; a single requested item; a recipe accepting substitutes; direct
  combination whose constituents are selected together by the player.
- Parameters: required type set, multiplicity, recipient, acceptance feedback,
  partial-set persistence, order freedom, substitutions and completion edge.
- Evidence: [Day of the Tentacle decomposition](../games/a-f/day-of-the-tentacle.md).
- Novelty: not assessed.

## CON-140 — Typed collection slots with fixed and alternative quotas

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each persistent collection group declares eligible inventory
  identities, per-identity quantities and any minimum quality; completion
  requires its slot quota, which may demand every displayed identity or a
  declared number of distinct choices from a larger displayed option set.
- Includes: Stardew Valley's Blacksmith's Bundle requiring all three displayed
  bars, Geologist's Bundle requiring all four minerals and Adventurer's Bundle
  accepting any two distinct options from Slime, Bat Wing, Solar Essence and
  Void Essence at their shown quantities.
- Excludes: one exact character commission with no substitutes; a scalar price;
  an item recipe selected and resolved atomically; an undisclosed random
  collection target.
- Parameters: eligible type set, required count per identity, minimum quality,
  slot quota, distinctness, fixed-versus-alternative mode and excess handling.
- Evidence: [Stardew Valley decomposition](../games/s-z/stardew-valley.md).
- Novelty: not assessed.

## CON-141 — Gapless non-overlapping finite-footprint exact cover

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a complete arrangement of a declared finite rigid-piece multiset
  is valid only when every receiving-board cell belongs to exactly one placed
  footprint, leaving neither multiply occupied nor uncovered positions.
- Includes: covering The Talos Principle's first A1 4 × 3 arranger with its
  collected green `L`, `J` and `Z` tetrominoes without overlap or gaps.
- Excludes: overwrite-order composition; exact-once cover restricted to
  two-cell adjacency relations; ordinary capacity that permits empty cells;
  matching a typed target while allowing footprints to overlap.
- Parameters: board topology, piece footprints, orientation sets, overlap
  rejection, required coverage, identity multiplicity and acceptance timing.
- Evidence: [The Talos Principle decomposition](../games/s-z/the-talos-principle.md).
- Novelty: not assessed.

## CON-142 — Four cardinal orthographic traversal frames

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: ordinary traversal is evaluated only in one of four horizontal
  axis-aligned orthographic views; a legal view command changes the frame by
  exactly one quarter-turn, and avatar movement is unavailable while the
  transition between settled frames is resolving.
- Includes: Fez limiting Gomez's platforming to four classic 2D perspectives
  and suspending movement and time during a view rotation.
- Excludes: unrestricted 3D camera orbit; eight-direction isometric facing;
  simultaneous movement during a continuously steerable camera turn; rotating
  the physical level as a gravity puzzle.
- Parameters: view count, turn increment, horizontal axis, transition lock,
  input buffering, view-restricted rooms and post-rotation action limits.
- Evidence: [Fez decomposition](../games/a-f/fez.md).
- Novelty: not assessed.

## CON-143 — Camera-only route control over autonomous walker

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player cannot issue directional locomotion commands to the
  represented walker; useful route control is limited to changing the
  perspective, pausing or resuming its automatic motion and optionally
  accelerating that unchanged motion.
- Includes: Echochrome's Walker advancing and turning under fixed locomotion
  rules while the player guides it by orbiting the stage and using thinking or
  speed controls.
- Excludes: directly steering an avatar; assigning behavioural roles to an
  autonomous population; drawing a route; placing persistent direction signs;
  choosing a remote destination for pathfinding.
- Parameters: default walking direction, dead-end turn rule, pause semantics,
  speed multiplier, fall handling and whether several walkers coexist.
- Evidence: [Echochrome decomposition](../games/a-f/echochrome.md).
- Novelty: not assessed.

## CON-144 — Traversal decisions require settled architecture

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: route connectivity and destination eligibility are evaluated
  only when every relevant manipulated architectural component occupies one of
  its authored snap poses; an intermediate gesture pose is not a legal
  traversal-decision state.
- Includes: Monument Valley waiting for the Chapter I bridge to settle before
  exposing the newly reachable pedestal route.
- Excludes: continuously changing topology while a free camera moves; physics
  traversal over every intermediate rigid-body pose; a turn animation that
  merely hides an already determined global collision slice.
- Parameters: legal pose set, snap tolerance, settle delay, input lock,
  destination invalidation, occupied-component policy and queued commands.
- Evidence: [Monument Valley decomposition](../games/m-r/monument-valley.md).
- Novelty: not assessed.

## CON-145 — Held perspective placement must remain collision-free

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: every live pose of a perspective-rescaled held object is bounded
  by the nearest sampled world geometry along its visible footprint; the object
  may approach that boundary but cannot be committed beyond it or intersect
  the blocking surface.
- Includes: Superliminal limiting a held Induction chess piece to the farthest
  depth at which its enlarged collision volume still clears the wall or other
  background geometry.
- Excludes: a fixed carry offset; a placement grid unrelated to camera depth;
  portal-surface eligibility; overlap removed destructively by a committed
  image; collision checks that occur only after an already accepted release.
- Parameters: ray origin, footprint sampling, occluder classes, safety margin,
  concavity approximation, candidate-pose correction, invalid feedback and
  release tolerance.
- Evidence: [Superliminal decomposition](../games/s-z/superliminal.md).
- Novelty: not assessed.

## CON-146 — Portable cube manipulation requires matching gravity colour

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a colour-addressed portable cube can be picked up and deliberately
  placed only while the currently selected global gravity frame has the same
  colour; in every other frame the cube remains non-manipulable world geometry.
- Includes: moving Manifold Garden's red cube only in red gravity and its blue
  cube only in blue gravity before placing each on a matching fixture.
- Excludes: colour-keyed doors with an inventory key; gravity affecting every
  object identically regardless of type; a cosmetic colour change; a cube that
  can always be carried but activates only a matching receiver.
- Parameters: colour domain, frame-to-colour map, eligible object classes,
  pickup rejection, held-object behaviour during frame change, target matching
  and visual feedback.
- Evidence: [Manifold Garden decomposition](../games/m-r/manifold-garden.md).
- Novelty: not assessed.

## CON-147 — Rigid-object pickup requires avatar-relative manageable scale

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a physical representation can be picked up only while its size
  relative to the current avatar lies inside the authored manipulation
  envelope; a homologous smaller representation may remain reachable even when
  the normal or outer one is too large.
- Includes: moving Maquette's oversized red blocker through its small model
  representation and leaving a giant key bridge fixed while its smaller
  homolog can still be handled.
- Excludes: weight capacity with no scale relation; colour-gated pickup;
  collision-bounded sightline placement; an object that is always portable but
  activates only a size-matched receiver.
- Parameters: avatar scale, minimum and maximum object extent, reach, mass
  override, held clearance, rejection feedback and recursion layer.
- Evidence: [Maquette decomposition](../games/m-r/maquette.md).
- Novelty: not assessed.

## CON-148 — Spatial replacement requires the affected threshold to be unobserved

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an armed authored room or doorway replacement may resolve only
  while the affected threshold is outside the player's current view; continuous
  observation preserves the present destination even when the other trigger
  prerequisites are satisfied.
- Includes: Antichamber preserving the usable `Now You See It` door while the
  player keeps looking at it, but permitting its destination to change after
  the player faces the glass window.
- Excludes: an object that exists only when centred in view; line-of-sight
  targeting; occlusion used only as information; a portal surface that remains
  traversable while watched; world changes hidden only by a cutscene.
- Parameters: visibility volume, occlusion policy, peripheral threshold,
  trigger ordering, minimum unobserved duration and reobservation behaviour.
- Evidence: [Antichamber decomposition](../games/a-f/antichamber.md).
- Novelty: not assessed.

## CON-149 — Order-five square incidence governs local route adjacency

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: traversable surfaces use the regular hyperbolic `{4,5}`
  incidence rule, so five equal regular quadrilateral sectors meet around one
  vertex and produce one more local branch than a flat square grid permits.
- Includes: Hyperbolica's square-tiled hyperbolic ground and maze neighbourhoods
  whose 72-degree square corners close only in groups of five.
- Excludes: four Euclidean squares around a point; five decorative paths that
  do not share a metric vertex; portal edges; periodic copies; an arbitrary
  graph laid out with curved artwork.
- Parameters: Schläfli pair, edge length, polygon angle, collision seams,
  branch labelling, authored obstacles and numerical tolerance.
- Evidence: [Hyperbolica decomposition](../games/g-l/hyperbolica.md).
- Novelty: not assessed.

## CON-150 — Bitruncated order-three heptagonal incidence governs cell adjacency

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the standard traversable cell graph is the bitruncation of the
  regular hyperbolic `{7,3}` tiling, so decision-bearing hexagonal and
  heptagonal cells inherit adjacency from three heptagons meeting at each
  underlying vertex.
- Includes: standard HyperRogue terrain and pursuit on its hyperbolic
  soccer-ball tiling.
- Excludes: the unbitruncated `{7,3}` experiment; a flat `{6,3}` hex grid;
  `{4,5}` square incidence; arbitrary graph art with no rule-bearing tiling;
  projection distortion alone.
- Parameters: source Schläfli pair, bitruncation, cell class, walls, land
  overlays, wrapping, alternate geometry mode and adjacency lookup.
- Evidence: [HyperRogue decomposition](../games/g-l/hyperrogue.md).
- Novelty: not assessed.

## CON-151 — Role-exclusive state and control authority

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: only one declared human role may inspect and manipulate the live
  problem object, while the other role has no direct view or control channel
  to that object and must act through communication.
- Includes: the Defuser alone viewing, rotating and operating the bomb while
  Experts cannot see or touch it.
- Excludes: two players sharing the same board; optional division of labour;
  switching among simulated bodies; an autonomous agent that receives a role.
- Parameters: acting-role count, allowed observers, view-sharing prohibition,
  controller handoff and remote-play medium.
- Evidence: [Keep Talking and Nobody Explodes decomposition](../games/g-l/keep-talking-and-nobody-explodes.md).
- Novelty: not assessed.

## CON-152 — First-applicable ordered module-rule precedence

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a module's accepted control is determined by testing a declared
  ordered list of state predicates and using the first matching branch;
  satisfying a later branch cannot override an earlier applicable one.
- Includes: the colour/count/position cases for Wires and the appearance,
  battery and indicator cases for the Button in Bomb Defusal Manual version 1.
- Excludes: a conjunction where all constraints must hold simultaneously; an
  unordered scoring table; player-authored rule order; random branch choice.
- Parameters: predicate order, inspected state fields, fallback branch,
  selected control and cross-module casing facts.
- Evidence: [Keep Talking and Nobody Explodes decomposition](../games/g-l/keep-talking-and-nobody-explodes.md).
- Novelty: not assessed.

## CON-153 — Finite recoverable-strike allowance

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an attempt permits a fixed positive number of incorrect committed
  controls to accumulate as persistent strikes, and reaching the declared
  strike threshold terminates the whole attempt unsuccessfully even if legal
  controls would otherwise remain.
- Includes: a standard Keep Talking and Nobody Explodes bomb exploding when
  the third strike is recorded.
- Excludes: one immediately terminal hazard; a move budget spent by both correct
  and incorrect actions; mistakes that affect score only; per-unit health.
- Parameters: threshold, starting strikes, persistence across modules, whether
  a mode omits the indicator and the interaction with countdown rate.
- Evidence: [Keep Talking and Nobody Explodes decomposition](../games/g-l/keep-talking-and-nobody-explodes.md).
- Novelty: not assessed.

## CON-154 — Complete one-to-one glyph-to-meaning page mapping

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: one validation page must assign every displayed unknown glyph to
  exactly one distinct illustrated meaning and fill every meaning slot exactly
  once before the mapping can be submitted as a complete interpretation.
- Includes: bijectively matching open, closed and door pictures to the first
  three discovered Devotee glyphs in Chants of Sennaar.
- Excludes: free-text annotation; repeated use of one glyph; a partially filled
  page; ordinary sentence order; an unconstrained many-to-many tag set.
- Parameters: glyph count, meaning-slot count, duplicate policy, empty-slot
  policy, reassignment and submission threshold.
- Evidence: [Chants of Sennaar decomposition](../games/a-f/chants-of-sennaar.md).
- Novelty: not assessed.

## CON-155 — First glyph-page validation gates onward traversal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the opening tutorial prevents onward world progression until the
  first bounded glyph page has been correctly validated, even if its associated
  environmental mechanism has already been configured.
- Includes: Chants of Sennaar requiring confirmation of open, closed and door
  before the player can continue beyond the tutorial gate.
- Excludes: an optional codex entry; a later page that can be postponed; a door
  opened solely by its world switch; a narrative checkpoint with no answer.
- Parameters: gated threshold, required page, mechanism prerequisite, retry
  policy, hint timing and persistence after success.
- Evidence: [Chants of Sennaar decomposition](../games/a-f/chants-of-sennaar.md).
- Novelty: not assessed.

## CON-156 — Revealed rules remain jointly binding on one mutable answer

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: every rule added to a sequential rule window remains active, and
  the one current mutable answer must satisfy their full conjunction rather
  than only the newest rule.
- Includes: The Password Game retaining Rules 1-9 so a later edit that solves
  one requirement may invalidate an earlier one.
- Excludes: replacing one challenge with the next; independent answer fields;
  optional achievements; a fixed rule set disclosed completely at the start.
- Parameters: rule count, predicate catalogue, shared answer scope, activation
  permanence and treatment of mutually interacting substrings.
- Evidence: [The Password Game decomposition](../games/s-z/the-password-game.md).
- Novelty: not assessed.

## CON-157 — Current-day policy jointly defines case admissibility

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: one case may receive the accepting verdict only when its visible
  documents, statements and identity satisfy the complete conjunction of rules
  active for the current workday; that conjunction may be replaced or amended
  at the next day boundary.
- Includes: Papers, Please Day 4 requiring a passport and current documents,
  an entry permit for foreigners, an identity card for Arstotzkans and refusal
  of wanted criminals, even though Day 3 used foreign entry tickets instead.
- Excludes: a rule stack that grows during one mutable answer; one immutable
  ruleset across every session; optional scoring conditions; a single selected
  fact-pair relation.
- Parameters: day, entrant class, required-document predicates, validity
  predicates, bulletin amendments, exceptions and policy replacement order.
- Evidence: [Papers, Please decomposition](../games/m-r/papers-please.md).
- Novelty: not assessed.

## CON-158 — Exact ordered cardinal trace for one patterned seal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: one addressed seal accepts exactly its authored finite cardinal
  sequence in order; changing, omitting, mirroring or reordering a direction
  does not satisfy that seal.
- Includes: `Down, Right, Up, Left, Up, Right` for TUNIC's scoped door beside
  the Overworld fountain.
- Excludes: any valid route to a destination; an unordered button set; a code
  shared automatically by every seal; possession of the clue page itself.
- Parameters: direction alphabet, sequence, length, symmetry, target identity,
  prefix handling and retry policy.
- Evidence: [TUNIC decomposition](../games/s-z/tunic.md).
- Novelty: not assessed.

## CON-159 — Learned credential gates access without current-loop reacquisition

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: access to one addressed route requires that its exact credential
  already be registered as learned, but does not require a matching inventory
  object or a repeat visit to the credential source in the current iteration.
- Includes: Outer Wilds requiring the launch codes for the launch lift while a
  post-reset Hatchling may use the codes learned from Hornfels in the first loop.
- Excludes: an ungated route; a consumable key; a code that must be manually
  re-entered from memory; a permanent door-open flag retained through reset.
- Parameters: credential identity, acquisition source, route identity, current-
  iteration requirement, inventory substitution and consumption policy.
- Evidence: [Outer Wilds decomposition](../games/m-r/outer-wilds.md).
- Novelty: not assessed.

## CON-160 — Earliest-five visibility cap per archive query

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: one archive query may expose for playback no more than the first
  five records in the system's fixed chronological match order, with no next
  page or repeated-query rotation even when additional records qualify.
- Includes: Her Story requiring a narrower word or phrase to reach matching
  clips beyond a broad query's five visible results.
- Excludes: five actions per attempt; five stored bookmarks; ordinary paginated
  search; a random sample of five; hiding records until a story flag unlocks.
- Parameters: cap value, ordering key, total-count visibility, pagination
  policy, repeat-query behaviour and whether refinement changes eligibility.
- Evidence: [Her Story decomposition](../games/g-l/her-story.md).
- Novelty: not assessed.

## CON-161 — One-to-one typed directional panel-port pairing

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an explicit traversal-panel link is legal only between two
  currently unpaired endpoints on different panels whose transport type and
  directional polarity are complementary.
- Includes: pairing a left-facing door with a right-facing door, or a downward
  ladder endpoint with an upward ladder endpoint, in The Pedestrian.
- Excludes: door-to-ladder links; reusing one endpoint in several links; joining
  ports within one panel; matching touching terrain edges or visual scene seams.
- Parameters: endpoint types, polarity vocabulary, per-port capacity,
  cross-panel rule, line crossing, distance and invalid-link feedback.
- Evidence: [The Pedestrian decomposition](../games/s-z/the-pedestrian.md).
- Novelty: not assessed.

## CON-162 — Mounted compatible world orb gates contained-world entry

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a contained world is enterable from an outer location only while
  its unique orb occupies a compatible world-jump pedestal; a loose, carried or
  mismatched orb does not create that entry, and one orb cannot be both mounted
  and carried.
- Includes: Cocoon rejecting world entry until the orange orb is inserted into
  its receptive jump mechanism and suspending that entry when the orb is taken.
- Excludes: centre-cell clearance for an enterable grid box; surface material
  eligibility for a portal shot; possession of a key that opens a separate door.
- Parameters: orb identity, pedestal acceptance class, occupancy capacity,
  mounted-versus-carried exclusivity, entry side and unavailable feedback.
- Evidence: [Cocoon decomposition](../games/a-f/cocoon.md).
- Novelty: not assessed.

## CON-163 — Unlocked carried orb and compatible locus gate its ability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an orb-specific world effect may resolve only when that orb's
  ability has been unlocked, the avatar currently carries that exact orb and
  the avatar occupies a compatible authored locus; losing any predicate makes
  the effect unavailable.
- Includes: Cocoon manifesting the orange orb's invisible bridge only after its
  ability is unlocked and while the orb is carried near a receptive route.
- Excludes: a permanent avatar upgrade; any carried object activating every
  receiver; a fixed switch whose state persists after the orb is set down.
- Parameters: unlock source, orb identity, carried-state predicate, locus type,
  activation radius, persistence after leaving and multiple-orb priority.
- Evidence: [Cocoon decomposition](../games/a-f/cocoon.md).
- Novelty: not assessed.

## CON-164 — Finite launched-body stock per attempt

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each committed launch irreversibly consumes one member of a
  visible finite attempt-local projectile stock, and no additional launch is
  available after the stock is exhausted.
- Includes: the ordered bird queue in Angry Birds Classic and the remaining
  ball count in Peggle Deluxe.
- Excludes: ammunition that regenerates during the same attempt; an unlimited
  launcher; a move budget where actions do not consume physical projectiles.
- Parameters: stock size, ordering, free-ball recovery, projectile identity and
  early-completion rule.
- Evidence: [Angry Birds Classic decomposition](../games/a-f/angry-birds-classic.md)
  and [Peggle Deluxe decomposition](../games/m-r/peggle-deluxe.md).
- Novelty: not assessed.

## CON-165 — Grip requires reachable contact and body leverage

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a hand grip exists only while that hand physically reaches an
  eligible surface and the player holds its channel; resulting motion remains
  limited by ragdoll mass, collision and available leverage.
- Includes: Human: Fall Flat ledge climbing and two-hand object manipulation.
- Excludes: magnetic attachment at range; scripted mantle animation; carrying
  an object without articulated contact.
- Parameters: contact distance, eligible materials, hand count, grip release,
  joint limits and body weight.
- Evidence: [Human: Fall Flat decomposition](../games/g-l/human-fall-flat.md).
- Novelty: not assessed.

## CON-166 — Two agents own four independent portal channels

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each of two controlled agents owns one replaceable pair of portal
  channels, and chamber solutions may require traversal through endpoints made
  by either owner while preserving all four identities.
- Includes: ATLAS and P-body in Portal 2's cooperative campaign.
- Excludes: one player controlling a single two-colour pair; two avatars sharing
  one undifferentiated portal pair; decorative team colours.
- Parameters: agent count, channels per agent, cross-owner traversal, placement
  authority and reset behaviour.
- Evidence: [Portal 2 cooperative decomposition](../games/m-r/portal-2-co-op.md).
- Novelty: not assessed.

## CON-167 — Household object must fit an accepted room support

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each unpacked object must occupy non-overlapping space on or in a
  support whose room and affordance classes accept that object.
- Includes: storing kitchenware in kitchen storage and clothes in suitable
  bedroom furniture in Unpacking.
- Excludes: one exact required coordinate; unrestricted decoration; inventory
  use on a single fixed mechanism.
- Parameters: room, support, containment, footprint, stacking and exceptions.
- Evidence: [Unpacking decomposition](../games/s-z/unpacking.md).
- Novelty: not assessed.

## CON-168 — Authored route thresholds delimit narrative choices

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a narrative choice is committed by entering one of the currently
  open authored routes; unavailable branches cannot be invented by free
  movement and a crossed threshold may close alternatives for that run.
- Includes: the two-door decision and downstream branch points in The Stanley
  Parable: Ultra Deluxe.
- Excludes: unconstrained open-world travel; text choices available regardless
  of position; merely missing optional scenery.
- Parameters: open routes, commit threshold, backtracking, branch closure and
  prior-run unlocks.
- Evidence: [The Stanley Parable: Ultra Deluxe decomposition](../games/s-z/the-stanley-parable-ultra-deluxe.md).
- Novelty: not assessed.

## CON-169 — External clue gates an in-world solution

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the information needed to complete an addressed in-world puzzle
  is intentionally absent from the ordinary world view and must be recovered
  from the game-authored external interface artefact.
- Includes: OneShot's host-file or mock-OS clue feeding a later in-game answer.
- Excludes: optional lore outside the game; an ordinary in-world manual; a clue
  available from an unauthorised guide.
- Parameters: clue channel, encoding, in-world receiver, platform equivalent
  and fallback accessibility channel.
- Evidence: [OneShot decomposition](../games/m-r/oneshot.md).
- Novelty: not assessed.

## CON-170 — Zoned development requires access and enabling services

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an authorised urban lot can develop only when its parcel has the
  required transport access and any utility or density prerequisites for that
  development stage.
- Includes: SimCity 4 and Cities: Skylines zones needing road frontage and
  suitable utilities or city conditions for development and upgrading.
- Excludes: aesthetic preference alone; a player-placed civic facility; a route
  that merely improves land value without gating the lot.
- Parameters: frontage, road access, power, water, density, parcel size and abandonment.
- Evidence: [SimCity 4 Deluxe Edition decomposition](../games/s-z/simcity-4-deluxe-edition.md)
  and [Cities: Skylines decomposition](../games/a-f/cities-skylines.md).
- Novelty: not assessed.

## CON-171 — Municipal construction and operation require solvency

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: construction requires sufficient treasury and every retained
  network or service commits recurring expenditure that must fit the municipal
  budget or suffer cuts and fiscal penalties.
- Includes: SimCity 4 and Cities: Skylines construction costs, recurring
  upkeep, service-budget reductions and borrowing.
- Excludes: an abstract score cost; private development paid directly by the
  player; a single consumable move budget.
- Parameters: treasury, build cost, upkeep, borrowing, deficit threshold and funding floor.
- Evidence: [SimCity 4 Deluxe Edition decomposition](../games/s-z/simcity-4-deluxe-edition.md)
  and [Cities: Skylines decomposition](../games/a-f/cities-skylines.md).
- Novelty: not assessed.

## CON-172 — Entity operation requires compatible recipe and flow state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a production or transfer entity performs its declared operation
  only when its entity class accepts that recipe or item, required inputs are
  present and the destination can accept the resulting output.
- Includes: Factorio assembling machines accepting only recipes in their
  crafting category, inserters refusing incompatible or full destinations and
  furnaces waiting when ingredients, fuel or output capacity are unavailable.
- Excludes: insufficient electric satisfaction, which changes operation speed;
  a finite resource patch beneath an extractor; static footprint placement.
- Parameters: entity category, recipe, ingredient inventory, item filter,
  input/output capacity, insertion limit and blocked-result behaviour.
- Evidence: [Factorio decomposition](../games/a-f/factorio.md).
- Novelty: not assessed.

## CON-173 — Extractor placement requires compatible resource locus

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a persistent extraction entity may be placed or operate only
  when its declared coverage intersects a compatible world resource locus and
  any special extraction prerequisites are satisfied.
- Includes: Factorio mining drills requiring mineable ore beneath their mining
  area and pumpjacks requiring an oil well under the attachment point.
- Excludes: ordinary factory footprint clearance; a hand-mining target within
  reach; running out of a previously valid finite reserve.
- Parameters: extractor class, resource type, coverage footprint, attachment
  point, fluid input, mining hardness and exhausted-locus response.
- Evidence: [Factorio decomposition](../games/a-f/factorio.md).
- Novelty: not assessed.

## CON-174 — Card play requires current cost and target compatibility

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a held card may be played only when the shared current resource
  can pay its effective cost and every required target satisfies that card's
  current eligibility rule.
- Includes: Slay the Spire cards requiring enough Energy and, for targeted
  attacks or skills, a living eligible enemy.
- Excludes: post-play effect resolution; selecting a card reward; a free-form
  spatial placement constraint.
- Parameters: effective cost, X-cost treatment, target count, target class,
  unplayable status and cost-changing effects.
- Evidence: [Slay the Spire decomposition](../games/s-z/slay-the-spire.md) and
  [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md),
  and [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md).
- Novelty: not assessed.

## CON-175 — Persistent health depletion terminates the run

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: health lost in one encounter remains lost at later nodes unless
  explicitly restored, and reaching the terminal health threshold ends the
  complete multi-node run.
- Includes: Slay the Spire damage persisting between floors and zero player HP
  ending the climb.
- Excludes: encounter-local health restored automatically after every battle;
  a recoverable life stock; score loss with no terminal survival threshold.
- Parameters: maximum health, terminal threshold, healing sources, revival
  exceptions and act-transition treatment.
- Evidence: [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
- Novelty: not assessed.

## CON-176 — Successor node must follow a visible route edge

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: ordinary progression may select only a node joined by a visible
  outgoing edge from the current route position; unconnected nodes on the next
  floor are inaccessible.
- Includes: Slay the Spire map traversal between connected successive floors.
- Excludes: drawing the route; unrestricted fast travel; choosing among
  outcomes within the current node.
- Parameters: edge direction, floor monotonicity, starting-node choice,
  exceptional route-changing modifiers and act boundary.
- Evidence: [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
- Novelty: not assessed.

## CON-177 — Bounded carried-consumable slot capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: persistent consumable items occupy a fixed number of carried
  slots, so acquiring another item requires a free slot or explicit disposal.
- Includes: Slay the Spire potion slots in an ordinary Ascension 0 run.
- Excludes: an unlimited general inventory; a bounded card hand replenished
  every turn; persistent passive relics with no shared slot cap.
- Parameters: slot count, empty-slot rule, replacement, disposal timing and
  modifiers.
- Evidence: [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
- Novelty: not assessed.

## CON-178 — Persistent deck membership defines combat draw supply

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: every ordinary combat begins from the current persistent run
  deck, and additions, removals, transformations and upgrades made between
  encounters change the card identities or versions that can be drawn later.
- Includes: Slay the Spire rebuilding the combat draw pile from the current
  deck at encounter start.
- Excludes: a fixed deck restored after every node; temporary generated cards
  that vanish after combat; drawing from a global collection without first
  adding cards to the run deck.
- Parameters: starting deck, persistent mutations, combat-only additions,
  curses, bottled cards and encounter setup effects.
- Evidence: [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
- Novelty: not assessed.

## CON-179 — Municipal tools and land purchases require population milestone

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a declared service, zone, policy, finance option or additional
  map-area purchase cannot be used until the current city has reached its
  associated population milestone.
- Includes: Cities: Skylines withholding higher-tier city services, dense
  zones, loans, policies and new area purchases before their milestones.
- Excludes: insufficient treasury after a tool is unlocked; a technology that
  must consume research resources; an authored scenario flag unrelated to
  city population.
- Parameters: threshold schedule, affected catalogue entries, area-purchase
  count, treasury cost after unlock and permanence after population decline.
- Evidence: [Cities: Skylines decomposition](../games/a-f/cities-skylines.md).
- Novelty: not assessed.

## CON-180 — Creature-card play requires open lane and declared cost payment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a held creature may enter combat only if the selected friendly
  lane is unoccupied and the card's complete current free, Blood or Bone cost
  has been legally satisfied before placement resolves.
- Includes: Act I Inscryption rejecting a Beast card when all four friendly
  lanes are occupied, too few eligible sacrifices exist or the Bone pool is
  below its printed cost.
- Excludes: a target predicate for an immediate effect card; card draw; a
  spatial overworld placement category.
- Parameters: lane capacity, occupancy, cost class, effective amount, free-card
  rule, discounts and rejection feedback.
- Evidence: [Inscryption decomposition](../games/g-l/inscryption.md).
- Novelty: not assessed.

## CON-181 — Blood payment requires sufficient eligible sacrifice value

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a pending Blood-cost card cannot be placed until the player has
  committed eligible controlled creatures whose declared sacrifice values meet
  or exceed every printed Blood pip.
- Includes: ordinary Act I Inscryption creatures contributing one Blood when
  sacrificed and Worthy Sacrifice contributing its declared greater value.
- Excludes: Bone costs paid from an accumulated pool; hostile kills; a map
  event that permanently removes a deck card for an upgrade.
- Parameters: required pips, eligible board cards, value modifiers,
  non-sacrificable cards, survival Sigils and overpayment.
- Evidence: [Inscryption decomposition](../games/g-l/inscryption.md).
- Novelty: not assessed.

## CON-182 — Fixed paired combat lanes constrain occupancy and attack relation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each side has one bounded row of mutually exclusive active card
  positions paired by index, and ordinary attacks interact only with the card
  or open scale path in the corresponding opposing lane.
- Includes: the four player and four Leshy active lanes in Act I Inscryption.
- Excludes: unrestricted target selection; multiple cards stacked in one active
  position; adjacency on a free-movement tactical grid.
- Parameters: lane count, paired index, occupancy, queued back row, movement
  Sigils, airborne bypass and multi-lane attacks.
- Evidence: [Inscryption decomposition](../games/g-l/inscryption.md).
- Novelty: not assessed.

## CON-183 — Finite recoverable life stock gates complete run failure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: losing an encounter consumes one member of a visible finite life
  stock and permits continuation while any remain; losing with none remaining
  terminates and resets the complete run, while declared milestones may refill
  the stock.
- Includes: Act I Inscryption's two candles, ordinary battle loss extinguishing
  one candle, a later loss ending the run and boss progression relighting them.
- Excludes: one persistent health total; an immediate one-error puzzle failure;
  unlimited encounter retries with no run consequence.
- Parameters: starting lives, loss predicate, refill events, boss exceptions,
  tutorial gates and terminal transition.
- Evidence: [Inscryption decomposition](../games/g-l/inscryption.md).
- Novelty: not assessed.

## CON-184 — Settlement building requires an owned design and construction materials

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an ordinary settlement building can be committed and completed
  only when its design is currently owned and every declared construction
  material cost is paid or delivered under that settlement's build process.
- Includes: Against the Storm buildings requiring an acquired blueprint and
  delivered goods, and Frostpunk buildings unlocked by base rules, research or
  law with wood, steel or Steam Core costs.
- Excludes: universally available roads and camps; a machine requiring only
  footprint compatibility; temporary preview ghosts with no material cost.
- Parameters: blueprint source, material list, delivery, construction labour,
  refund and universal-building exceptions.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## CON-185 — Finite reassignable population and staffed job slots

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: autonomous work requires assigning members of a finite population
  to bounded compatible job slots, and one worker cannot staff two jobs at once.
- Includes: assigning Against the Storm villagers to camps, production buildings
  and Glade Events.
- Excludes: machines operating without workers; cosmetic residents; direct
  control of one avatar.
- Parameters: species, worker count, job slots, proficiency, reassignment delay
  and housing or service capacity.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## CON-186 — Queen's Impatience threshold terminates settlement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: if the visible failure track reaches its maximum before the
  settlement success track is filled, the current settlement ends in failure.
- Includes: maximum Queen's Impatience ending an Against the Storm settlement.
- Excludes: population reaching zero through departures; abandoning manually;
  losing one timed Glade Event.
- Parameters: maximum, passive growth, event penalties, success reductions and
  difficulty.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## CON-187 — Timed event deadline activates declared threat

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a hazardous event becomes active, its visible countdown
  continues unless paused by the global time controls, and reaching zero before
  resolution applies the listed adverse effect.
- Includes: unresolved dangerous or forbidden Glade Events in Against the Storm.
- Excludes: a hidden random penalty; a production quota with no failure effect;
  a global run-loss timer.
- Parameters: duration, pause, repeatability, threat effect and removal condition.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## CON-188 — Bounded offer permits one persistent exclusive choice

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a declared offer remains unresolved until the player selects the
  permitted number of options, after which unselected alternatives are removed
  and the chosen result persists for its stated scope.
- Includes: one blueprint or cornerstone selected from an Against the Storm
  offer, subject to rerolls; one Grand Theft Auto V terminal Story Mode option;
  one Cyberpunk 2077 terminal alliance and final contract response; one of
  three room plans committed behind a Blue Prince doorway.
- Excludes: buying several affordable shop items; reversible settings; viewing
  options without committing any.
- Parameters: offer size, selections, rerolls, deferral, duration and duplicate
  rules.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md)
  [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [Blue Prince decomposition](../games/a-f/blue-prince.md).
- Novelty: not assessed.

## CON-189 — Event resolution requires compatible goods and staffed work duration

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a selected event resolution cannot complete until its declared
  goods are supplied and assigned workers perform the required uninterrupted or
  cumulatively tracked work.
- Includes: solving an Against the Storm Glade Event with workers and goods.
- Excludes: paying an instantaneous shop price; recipe production without an
  event deadline; a task completed solely by reaching a score.
- Parameters: goods, alternatives, worker slots, duration, interruption and
  consumption timing.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## CON-190 — Embark destination must be revealed and within foothold range

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a new bounded run may begin only on a revealed persistent-map tile
  whose distance is inside the embarkation range of a currently valid origin.
- Includes: Against the Storm embarkation from the Smoldering City or a completed
  settlement during one world-map cycle.
- Excludes: unrestricted fast travel; movement inside the run; hidden route
  selection that reveals the destination only after commitment.
- Parameters: origin, range, tile visibility, occupation, cycle and modifiers.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## CON-191 — Metaprogression upgrade requires resources and predecessor level

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a persistent upgrade cannot be bought until every listed resource
  cost is affordable and the preceding level or branch prerequisite is owned.
- Includes: Citadel upgrade levels in Against the Storm.
- Excludes: level-gated content that unlocks automatically; run-local trader
  purchases; a technology queue supplied over live time.
- Parameters: currencies, cost, predecessor, branch, level cap and refund.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## CON-192 — Errand requires permission, skill and reachable work cell

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an agent may claim a colony errand only if permissions and learned
  skills allow it and a valid path reaches its interaction cell.
- Includes: Oxygen Not Included work blocked by traits, skills, door access or reachability.
- Excludes: relative priority after eligibility; missing recipe inputs; a directly controlled route.
- Parameters: agent, task, permission, skill, path, interaction cell, door and suit.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## CON-193 — Construction requires compatible cells and delivered material

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a construction plan completes only when its footprint, support
  and orientation remain compatible and the selected material has been delivered.
- Includes: Oxygen Not Included buildings, tiles, pipes, wires and rocket modules.
- Excludes: instant inventory placement; operating recipe inputs; visual-only plans.
- Parameters: footprint, support, rotation, material, mass, delivery, skill and construction time.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## CON-194 — Conduit and circuit obey capacity and material state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a utility segment transfers only compatible payload within packet
  or wattage limits; overload, blockage or phase change can damage or halt it.
- Includes: Oxygen Not Included pipe packet capacity, bridge direction, wire overload and phase damage.
- Excludes: open-cell fluid movement; recipe storage; unbounded abstract connections.
- Parameters: network, direction, packet, state, wattage, rating, overload and damage.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## CON-195 — Agent survival requires breathable, fed and thermally viable state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a colony agent remains operational only while oxygen, calories,
  body temperature and health stay above failure thresholds.
- Includes: Oxygen Not Included suffocation, starvation, temperature injury and death.
- Excludes: recoverable stress responses; a colony-wide scripted timer; suit eligibility.
- Parameters: breath, pressure, calories, temperature, health, incapacitation, rescue and death.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## CON-196 — Trained skills raise individual morale expectation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: every learned skill contributes expectation cost, so training an
  agent without enough morale creates persistent stress pressure.
- Includes: Oxygen Not Included skill tiers and interest-adjusted morale requirements.
- Excludes: research cost; ordinary experience; global difficulty.
- Parameters: skill, tier, interest, expectation increase, morale and stress rate.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## CON-197 — Building operation requires compatible environment and flows

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a colony building operates only while declared worker, material,
  power, conduit, temperature and output conditions are satisfied.
- Includes: Oxygen Not Included pumps, generators, stations, production and life-support buildings.
- Excludes: construction; personal survival; network-wide capacity damage.
- Parameters: worker, input, output, power, port, temperature, flooding, storage and automation.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## CON-198 — Embark package shares one finite preparation budget

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: starting skills, items, animals and supplies all spend from one
  fixed preparation allowance before the site begins.
- Includes: Dwarf Fortress seven-dwarf embark preparation points.
- Excludes: free difficulty presets; later caravan purchases; fixed loadouts.
- Parameters: total points, skill costs, item costs, quantities and remainder.
- Evidence: [Dwarf Fortress decomposition](../games/a-f/dwarf-fortress.md).
- Novelty: not assessed.

## CON-199 — Fortress job claim requires labour, path, tool and material

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an autonomous job remains unavailable unless an eligible worker
  can reach its interaction point and every required tool, workshop and
  material is compatible and obtainable.
- Includes: Dwarf Fortress mining, hauling, construction and workshop jobs.
- Excludes: direct unit commands; machine recipes that need no worker.
- Parameters: labour, work detail, worker, path, tool, workshop, material and access.
- Evidence: [Dwarf Fortress decomposition](../games/a-f/dwarf-fortress.md).
- Novelty: not assessed.

## CON-200 — Stockpile filter, capacity and links constrain hauling

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an item may enter storage only if its category is accepted,
  usable capacity remains and any declared source or destination link permits it.
- Includes: Dwarf Fortress stockpile customisation, bins, barrels and links.
- Excludes: workshop recipe compatibility; unrestricted floor dumping.
- Parameters: category, material, quality, container, tile capacity and links.
- Evidence: [Dwarf Fortress decomposition](../games/a-f/dwarf-fortress.md).
- Novelty: not assessed.

## CON-201 — Fortress institutions require declared office, room and status

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: administrative actions and noble progression remain unavailable
  or penalised until a qualified officeholder, required room value and
  settlement threshold are satisfied.
- Includes: Dwarf Fortress manager validation, broker trading, noble quarters,
  mandates and monarch eligibility.
- Excludes: ordinary labour eligibility; cosmetic room labels.
- Parameters: office, appointee, population, wealth, room type, room value,
  mandate, deadline and penalty.
- Evidence: [Dwarf Fortress decomposition](../games/a-f/dwarf-fortress.md).
- Novelty: not assessed.

## CON-202 — Allowed area and policy bound autonomous interaction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an autonomous resident may perform ordinary work or consumption
  only where its allowed area and current personal policy permit the target.
- Includes: RimWorld allowed areas, forbidden items and food, drug, apparel or medicine policies.
- Excludes: drafted emergency action; pathfinding geometry itself; work priority.
- Parameters: area, resident, target, forbidden state, policy filter and exception.
- Evidence: [RimWorld decomposition](../games/m-r/rimworld.md).
- Novelty: not assessed.

## CON-203 — Mental break suspends ordinary player control

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: once mood remains below a resident-specific break threshold and a
  break fires, ordinary work, area and direct orders are unavailable until recovery or interruption.
- Includes: RimWorld minor, major and extreme mental breaks.
- Excludes: voluntary idling; combat stun; low morale that leaves control intact.
- Parameters: mood, threshold, severity, break type, duration and interruption.
- Evidence: [RimWorld decomposition](../games/m-r/rimworld.md).
- Novelty: not assessed.

## CON-204 — Caravan load and route require viable travelling group

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a world caravan must include a capable colonist and keep carried
  mass, food, movement and route conditions viable for formation and travel.
- Includes: RimWorld caravan membership, carrying capacity, supplies and terrain speed.
- Excludes: local stockpile hauling; an arriving non-player trader.
- Parameters: colonist, mass, nutrition, animals, terrain, weather and destination.
- Evidence: [RimWorld decomposition](../games/m-r/rimworld.md).
- Novelty: not assessed.

## CON-205 — Ship launch requires connected parts and completed reactor startup

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: launch remains unavailable until required connected ship parts
  exist, the reactor survives its startup interval and at least one casket is occupied.
- Includes: the RimWorld base-game constructed-ship ending.
- Excludes: reaching the prebuilt journey-offer ship; DLC endings; reactor activation alone.
- Parameters: parts, connectivity, caskets, occupants, startup duration and reactor survival.
- Evidence: [RimWorld decomposition](../games/m-r/rimworld.md).
- Novelty: not assessed.

## CON-206 — Terrain breaking requires a reachable mutable target and eligible tool

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a terrain-cell break succeeds only when the targeted block, wall
  or placed object is reachable and mutable and the held hand or tool satisfies
  its harvest rule.
- Includes: Minecraft Survival reach- and tool-dependent mining; Terraria tool
  range, pickaxe power, axe class and hammer-dependent wall removal.
- Excludes: unrestricted Creative-mode edits; a factory footprint check; a
  grid-puzzle placement with no embodied reach.
- Parameters: projection, layer, reach, line of sight, hardness, tool class,
  tool tier and protection rule.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md) and
  [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## CON-207 — Crafting result requires exact spatial ingredient arrangement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a crafting result is available only when a supported grid exposes
  the recipe's exact item identities, required quantities and required cell
  arrangement; missing, substituted or wrongly placed ingredients reject it.
- Includes: Minecraft 2×2 and crafting-table 3×3 recipes.
- Excludes: a queued recipe using ingredients from one inventory; a generic
  combination of two held objects; freeform machine configuration.
- Parameters: grid size, cell pattern, item identity, stack count, recipe-book
  state, result and remainder.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md).
- Novelty: not assessed.

## CON-208 — Tile placement requires reachable compatible space and support

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: tile placement is legal only when the addressed cell or footprint
  is within reach, accepts the held tile state, has any required support and is
  not occupied by incompatible world or entity geometry.
- Includes: Minecraft Survival adjacent block placement; Terraria block, wall,
  torch and support-dependent furniture placement.
- Excludes: tool-dependent breaking; unrestricted Creative edits; factory footprints.
- Parameters: projection, layer, reach, anchor, footprint, occupancy, collision,
  tile state and support.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md) and
  [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## CON-209 — Portal activation requires its complete typed frame condition

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a dimension portal activates only when its frame has the required
  type, geometry and completion input for that portal class.
- Includes: Minecraft Nether obsidian-frame ignition and twelve filled End
  portal frame slots, including any Eyes generated already inserted.
- Excludes: entering an active portal; a decorative incomplete frame.
- Parameters: portal class, frame blocks, geometry, filled slots and activator.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md).
- Novelty: not assessed.

## CON-210 — Inventory transfer is bounded by typed stack and slot capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: pickup or transfer accepts only item quantities that fit a
  compatible partial stack or free carried slot, leaving any excess outside.
- Includes: Minecraft Survival inventory pickup and carried stack limits.
- Excludes: an unlimited abstract resource counter; one container's fixed unit cells.
- Parameters: item type, stack limit, partial stack, free slot and remainder.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md),
  [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md)
  and [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Additional support: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md),
  for carried stacks and finite inventory slots.
- Novelty: not assessed.

## CON-211 — City facility operation requires a street connection to the generator

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a placed city facility can perform its ordinary powered function
  only while an adjacent street connects it through the street network to the
  central generator.
- Includes: Frostpunk workplaces, homes and services requiring street-carried
  heat and power connectivity.
- Excludes: footprint placement; carried-goods transport; heat-zone radius.
- Parameters: facility, adjacent segment, generator root, network continuity
  and disconnected response.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## CON-212 — Law signing requires cooldown, prerequisite and open branch

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a civic law may be signed only after predecessor conditions are
  satisfied, the signing cooldown has elapsed and no exclusive alternative has
  already closed its branch.
- Includes: Frostpunk Adaptation prerequisites, alternative pairs and exclusive
  Order-versus-Faith Purpose paths.
- Excludes: technology research cost; a temporary event choice; repealing a law.
- Parameters: predecessor, cooldown, branch, exclusive alternative, scenario
  availability and signed state.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## CON-213 — Critical generator stress permits only its remaining emergency outcome

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: at critical generator stress the run can continue only through a
  currently available declared emergency sacrifice; otherwise the generator
  explodes and the city is lost.
- Includes: Frostpunk's first Steam Core or child repair response and later
  unrecoverable Overdrive explosion.
- Excludes: ordinary coal exhaustion; The Fall of Winterhome's faulty generator.
- Parameters: threshold, rescue count, Steam Core, eligible child, consequence and explosion.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## CON-214 — Unresolved Hope or Discontent crisis terminates captaincy

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after Hope approaches zero or Discontent approaches maximum and
  starts its final warning, failure to restore the required track within the
  declared grace period ends the scenario through deposition or banishment.
- Includes: Frostpunk's two-day low-Hope and high-Discontent final warnings.
- Excludes: one unpopular law; population death without a civic crisis.
- Parameters: track, trigger, recovery target, grace period, suppression option
  and terminal consequence.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## CON-215 — Medical operation requires adequate heat, staff and compatible capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: treatment proceeds only while the facility remains warm enough,
  staffed by eligible workers and has an open bed whose rules accept the
  patient's illness stage.
- Includes: Frostpunk Medical Posts, Infirmaries and law-dependent grave care.
- Excludes: sickness creation; ordinary production; unlimited abstract healing.
- Parameters: heat threshold, staff type, efficiency, bed count, illness stage,
  law and interruption.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## CON-216 — Scout formation and travel require Beacon capacity and available people

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a scout team can be formed and sent only when a functioning
  Beacon exposes free team capacity, the required available population is
  committed and the destination is currently revealed and reachable.
- Includes: A New Home five-worker scout teams and known Frostland nodes.
- Excludes: arriving refugees; city worker assignment; world-map teleportation.
- Parameters: Beacon, team cap, population cost, team state, destination
  visibility and route availability.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## CON-217 — Spherical factory placement must fit the current grid band

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a planetary entity or copied layout is legal only when its
  complete footprint maps to compatible unoccupied cells in the current curved
  grid band and satisfies any terrain or latitude-specific requirement.
- Includes: Dyson Sphere Program buildings and blueprints constrained by
  spherical latitude bands, grid warping and foundation state.
- Excludes: extractor-to-resource compatibility; orbital sphere-plan geometry;
  collision-free placement on a uniform flat grid.
- Parameters: planet, latitude band, footprint, orientation, cell alignment,
  terrain, foundation, collision and blueprint span.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## CON-218 — Mecha warp requires unlocked drive, energy and a Space Warper

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the directly controlled mecha may enter warp only after the
  required drive technology is unlocked, sufficient core energy is available
  and one carried Space Warper can be consumed.
- Includes: Dyson Sphere Program Icarus Drive Engine level four warp activation.
- Excludes: ordinary interplanetary sailing; a logistics vessel's station
  dispatch gate; faster ground movement.
- Parameters: drive level, core energy, warper inventory, activation command
  and insufficient-input feedback.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## CON-219 — Logistics dispatch requires a matched slot and eligible carrier

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a station trip starts only when compatible supply and demand
  slots exist, an appropriate carrier and minimum cargo are available, the
  origin can pay its launch energy and the route satisfies range and warper rules.
- Includes: Dyson Sphere Program planetary drones and interplanetary or
  interstellar logistics vessels.
- Excludes: belt movement between adjacent entities; manually withdrawing one
  stack; choosing the station's slot mode.
- Parameters: item, local or remote slot, carrier type, load threshold, station
  charge, route range, warp distance and warper policy.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## CON-220 — Solar-sail launch requires a valid orbit and firing window

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an EM-Rail Ejector launches a supplied solar sail only while a
  configured swarm orbit exists and the ejector's current planetary pose gives
  a legal firing angle to that orbit.
- Includes: Dyson Sphere Program ejectors waiting for target-orbit pitch.
- Excludes: rocket launch toward planned sphere nodes; receiver visibility;
  manually editing the swarm orbit.
- Parameters: orbit, ejector latitude and heading, planet rotation, pitch,
  valid window, sail supply and power.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## CON-221 — Carrier-rocket launch requires unfinished planned structure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a supplied Vertical Launching Silo launches a Small Carrier Rocket
  only while its selected star has an accessible planned node or frame that
  still requires structural points.
- Includes: Dyson Sphere Program rockets fulfilling an edited Dyson Sphere plan.
- Excludes: launching free-orbit solar sails; producing the rocket in an
  assembler; drawing a new node.
- Parameters: star, layer, plan element, remaining points, silo power, rocket
  supply and target assignment.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## CON-222 — Ray-receiver mode requires continuous access and its unlock

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a Ray Receiver produces only while it has line-of-sight or an
  allowed lens-assisted continuous-receiving state to available swarm or sphere
  output; Critical Photon mode additionally requires its technology unlock.
- Includes: Dyson Sphere Program receiver power and photon-production gates.
- Excludes: connected power-grid satisfaction after generation; solar-sail
  launch visibility; antimatter conversion from stored photons.
- Parameters: receiver pose, line-of-sight, lens, atmosphere, continuous
  receiving, available output, mode and technology.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## CON-223 — Agricultural production requires island fertility

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a farm can grow a crop only on an island whose declared fertility
  includes that crop, unless a separately scoped modifier changes the rule.
- Includes: Anno 1800 Old and New World crop fertilities.
- Excludes: mines requiring a spatial mineral deposit; insufficient workforce;
  an input good delivered from another island.
- Parameters: island, crop, fertility set, farm, field and modifier.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## CON-224 — Residence upgrade requires needs, occupancy and materials

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a residence may advance to the next population tier only when
  its required basic needs are fulfilled, its occupancy threshold is met and
  the declared construction materials can be paid.
- Includes: Anno 1800 Farmer-to-Worker through Engineer-to-Investor upgrades.
- Excludes: residents moving into the current tier; population milestone
  unlocks; upgrading a production building.
- Parameters: source tier, basic needs, occupancy, destination tier, materials
  and upgrade availability.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## CON-225 — Strategic investment requires available influence

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an influence-bearing island claim, ship, defence, propaganda item
  or other strategic asset cannot be committed when its category cost exceeds
  currently unallocated influence.
- Includes: Anno 1800 expansion, military fleet and newspaper influence gates.
- Excludes: treasury or construction-material costs; workforce shortage;
  reputation with an AI competitor.
- Parameters: asset, category, influence cost, available pool, refund and
  temporary commitment.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## CON-226 — Trade-route orders require compatible cargo capacity and stock

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a scheduled port instruction transfers only its selected good,
  cannot exceed the assigned ship slot's capacity or island storage, and loading
  cannot reduce stock below an enabled minimum reserve.
- Includes: Anno 1800 slot-specific load and unload orders.
- Excludes: local cart flow; manual transfer without a schedule; influence cost.
- Parameters: good, slot, capacity, requested quantity, island stock, storage
  space, minimum stock and partial transfer.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## CON-227 — Expedition departure and continuation require finite ship support

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an expedition must use an eligible assigned ship whose finite
  cargo slots hold the supplies or specialists available to meet events, and
  reaching zero morale forces the voyage to fail or return.
- Includes: Anno 1800's New World discovery expedition.
- Excludes: trade-route cargo orders; direct naval combat; an unlimited skill pool.
- Parameters: ship eligibility, slots, rations, skill, morale, event loss and return.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## CON-228 — World’s Fair phases require population, inputs and utilities

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the World’s Fair construction and exhibition progression cannot
  advance until the relevant Investor threshold, phase materials, workforce,
  electricity or timed exhibition supplies are present.
- Includes: Anno 1800's five-stage monument construction and exhibition preparation.
- Excludes: ordinary residence upgrade; a cosmetic festival; DLC monuments.
- Parameters: investors, phase, materials, workforce, electricity, preparation
  window, supplied good and reward threshold.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## CON-229 — Water infrastructure obeys terrain and fluid geometry

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a barrier, outlet or extractor operates only where terrain
  support, orientation, depth, intake and opening geometry are compatible.
- Includes: Timberborn dams, levees, floodgates, pumps and valves.
- Excludes: ordinary dry-land footprints; pipe throughput alone.
- Parameters: elevation, support, depth, opening, pressure and direction.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## CON-230 — Plant viability requires compatible local water state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a plant grows only on compatible soil or water while irrigation
  or depth is in range and contamination stays below its survival limit.
- Includes: Timberborn terrestrial and aquatic crops and trees.
- Excludes: fixed island fertility; cosmetic vegetation.
- Parameters: plant, soil, irrigation, depth, contamination and viability.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## CON-231 — Folktail reproduction is bounded by available housing

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: natural population growth proceeds only while eligible adults
  and unused lodge capacity exist, with maturation and death resolved over time.
- Includes: controlling Timberborn Folktails by building or pausing lodges.
- Excludes: instant residents; Iron Teeth breeding pods; abstract occupancy.
- Parameters: adults, children, beds, free capacity and life-cycle delay.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## CON-232 — Powered operation requires connected supply and capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a mechanical consumer operates only while an enabled shaft path
  connects enough current generation or stored discharge for its demand.
- Includes: Timberborn powered workplaces, clutches and Gravity Batteries.
- Excludes: road-range electricity; isolated burner fuel.
- Parameters: connection, clutch, generation, discharge, demand and satisfaction.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## CON-233 — Automation requires a compatible signal path and predicate

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a target follows automation only when source and target are
  compatible, the signal graph connects them and configured logic is valid.
- Includes: Timberborn sensors and logic controlling water infrastructure.
- Excludes: manual toggles; decorative links; recipe input gates.
- Parameters: source, target, connection, threshold, logic and fallback.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## CON-234 — Construction unlock requires its Science Point price

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a locked construction cannot be planned until prerequisites hold
  and the settlement pays its declared Science Point price once.
- Includes: Timberborn catalogue and Earth Recultivator unlocks.
- Excludes: build materials after unlock; population milestones; queued research.
- Parameters: construction, prerequisite, price, balance and unlocked state.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## CON-235 — Earth Recultivator requires exact build and launch supplies

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the Folktails wonder requires 20,000 science, then 2,000 gears,
  2,000 treated planks and 1,500 metal blocks, then 500 Extract and 500 Paper.
- Includes: Timberborn Earth Recultivator first activation.
- Excludes: ordinary buildings; Iron Teeth's wonder; later launches.
- Parameters: science, build goods, launch goods, progress and eligibility.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## CON-236 — Real construction requires phase-specific deliveries and work

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a planned structure or network completes only after each active
  phase receives its compatible materials, mechanisms and required workdays.
- Includes: Workers & Resources groundworks and construction phases.
- Excludes: instant ruble/dollar construction or agent-carried single material.
- Parameters: phase, materials, mechanism, workers, workdays and access.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## CON-237 — Vehicle service requires compatible network and facilities

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a vehicle can serve a route only when its mode, connected path,
  station, cargo capability, fuel and destination are compatible.
- Includes: Workers & Resources road, rail, ship and aircraft transport.
- Excludes: citizen walking or abstract teleporting trade.
- Parameters: mode, path, station, cargo, fuel, depot and reachability.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## CON-238 — Citizen activity requires reachable eligibility within time limits

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a citizen fulfils work or a need only through a reachable eligible
  destination, compatible education or passenger type and declared wait and
  in-vehicle time limits.
- Includes: the one-hour wait and four-hour single-vehicle limits.
- Excludes: cosmetic commuters or fixed job assignment without travel.
- Parameters: purpose, education, capacity, walking reach, wait and ride time.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## CON-239 — Office dispatch requires configured remit and suitable fleet

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an office may dispatch only for assigned sources, destinations or
  sites and only with an available vehicle compatible with the task and cargo.
- Includes: construction and distribution offices.
- Excludes: vehicle lines whose stops are explicitly ordered.
- Parameters: remit, threshold, priority, vehicle, cargo and range.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## CON-240 — Utility service requires connected capacity and operating state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a building receives a utility only through compatible connections
  with enough generated or imported capacity and acceptable pressure,
  temperature or voltage state.
- Includes: power, heating, water and sewage in Workers & Resources.
- Excludes: isolated machine fuel or decorative coverage.
- Parameters: connection, capacity, loss, pressure, temperature and outage.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## CON-241 — Border trade requires compatible gateway and currency state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an import or export settles only at a compatible border gateway
  for its transport or utility and against the matching ruble or dollar balance.
- Includes: customs houses and foreign power connections.
- Excludes: domestic warehouse transfers.
- Parameters: bloc, gateway, mode, resource, currency, price and throughput.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## CON-242 — Research requires prerequisites, faculty and staffed workdays

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a project advances only after its prerequisite projects and while
  the correct university has eligible staff producing its required workdays.
- Includes: Workers & Resources nuclear research chain.
- Excludes: a population milestone or instant point purchase.
- Parameters: prerequisites, faculty, staff, workdays and unlock.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## CON-243 — Nuclear generation requires staff, fuel, cooling and waste capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a reactor generates only with qualified workers, nuclear fuel,
  operating cooling and free waste handling; failures stop output or create
  radiation risk.
- Includes: Workers & Resources single-reactor nuclear power plant.
- Excludes: ordinary recipe flow or coal generation.
- Parameters: workers, engineers, fuel, cooling, water, power, waste and radiation.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## CON-244 — Second campaign completion requires the first and all active branches

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the Soviet Revolution campaign is available after the introductory campaign,
  and its completion requires satisfying every mandatory objective branch.
- Includes: sequential completion of the two released base campaigns.
- Excludes: sandbox survival or optional post-campaign optimisation.
- Parameters: predecessor, branch, objective state and completion flag.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## CON-245 — Mine work requires tower coverage and reachable terrain volume

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: excavation or controlled dumping may resolve only inside its
  mine tower's operation area where the designated height and terrain face are
  reachable by the assigned compatible vehicles.
- Includes: Captain of Industry mining and dumping designations, tower areas,
  slopes and vehicle access.
- Excludes: placing a fixed extractor over a deposit; unrestricted cosmetic
  terraforming; storage that does not alter terrain.
- Parameters: tower, rectangular area, designation type, target height,
  material filter, slope, vehicle size and route.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## CON-246 — Island vehicle job requires compatible load, route and service state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an island vehicle may accept and complete a logistics job only
  when its class can carry the product, both endpoints and route are reachable,
  capacity is reserved and fuel and maintenance permit operation.
- Includes: Captain of Industry pickups, trucks, haul trucks and assigned mine
  vehicles serving machines, storages, construction or dumping.
- Excludes: conveyor or pipe capacity; cargo ships on world routes; a road
  vehicle line with authored stops.
- Parameters: vehicle class, product state, capacity, source, destination,
  terrain clearance, reservation, fuel and maintenance.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## CON-247 — Settlement survival requires housing and essential supply

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: population can remain and grow only within housing capacity and
  with essential food and waste service, while health determines whether the
  settlement grows or loses people.
- Includes: Captain of Industry housing, food demand, waste collection, health
  and pollution-driven mortality.
- Excludes: finite job slots alone; optional goods that only improve Unity;
  manually controlled individual survival needs.
- Parameters: population, housing capacity, food, waste, health, growth,
  mortality and beacon arrivals.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## CON-248 — Unity-funded operation requires sufficient recurring balance

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a research lab, world resource, edict, boost or contract remains
  active only while settlement-generated Unity covers its one-time and
  recurring charge.
- Includes: Captain of Industry research, outposts, quick trades, contracts,
  machine boosts and instant recovery.
- Excludes: material recipe inputs; electricity capacity; a foreign currency
  account settled at a border.
- Parameters: Unity income, establishment charge, monthly charge, action cost,
  priority, suspension and recovery.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## CON-249 — World-node operation requires ship range, strength and support

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a world-map destination can be reached or exploited only when
  the ship can pay the route fuel, defeat any blocking enemy and supply the
  repair, manpower and Unity requirements of the revealed node.
- Includes: Captain of Industry exploration, ship battles and resource locations.
- Excludes: home-island pathfinding; village reputation for contracts; rocket launch.
- Parameters: path, fuel, radar, ship strength, enemy, damage, repair materials,
  workers, Unity and cargo capacity.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## CON-250 — Island contract requires reputation, depot, ship and Unity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a recurring island trade can begin and cycle only after its
  village reputation gate is met and a compatible cargo module, dedicated ship,
  offered export and Unity costs are available.
- Includes: Captain of Industry product contracts through Cargo Depots.
- Excludes: immediate Trading Dock exchanges; outpost pickups; domestic storage transfers.
- Parameters: village, reputation, offer, module type, ship, export stock,
  import room, establishment Unity and recurring Unity.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## CON-251 — Industrial research requires lab tier and supplied research equipment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a queued technology advances only after its prerequisites and
  while a sufficiently advanced staffed lab receives its required equipment,
  power, computing and Unity.
- Includes: Captain of Industry Research Labs Basic through IV and their
  progressively supplied research points.
- Excludes: staffed university workdays; automatic milestone unlocks; infinite
  post-endpoint space research.
- Parameters: technology, prerequisite, lab tier, equipment recipe, workers,
  electricity, computing, Unity and research points.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## CON-252 — Rocket launch requires level transfer path, propellant and water

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a constructed rocket can launch only if its assembly depot and
  free launch pad share a traversable level route and the pad receives the
  rocket's compatible propellant and launch-water quantities.
- Includes: Captain of Industry Rocket Assembly Depot, specialised transporter
  and Rocket Launch Pad.
- Excludes: merely researching rocketry; repeated space-station supplies;
  launching a rocket assembled wholly inside its silo.
- Parameters: depot elevation, path roughness, pad state, rocket tier, fuel
  type, oxidiser, water, payload and launch command.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## CON-253 — Drone errand requires commander coverage and reachable resources

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a drone may claim construction, hauling or maintenance work only
  while both its interaction site and required resource lie within a compatible
  commander's service area and a traversable route exists.
- Includes: Surviving Mars: Relaunched rockets, RC Commanders and Drone Hubs
  controlling drones inside adjustable ranges.
- Excludes: a staffed human workplace; globally matched truck delivery;
  direct step-by-step drone control.
- Parameters: commander, service area, drone assignment, task, resource,
  interaction site, route, power and charging state.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## CON-254 — Occupied dome requires sealed life support and food

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: colonists can safely occupy a dome only while housing and food
  are available and connected power, water and oxygen supply or stored reserve
  cover its current demand.
- Includes: Surviving Mars: Relaunched occupied surface domes and their life
  support dependencies.
- Excludes: optional comfort services; an unoccupied dome under construction;
  one abstract settlement-health total.
- Parameters: dome, population, housing, food, power, water, oxygen, storage,
  leak, outage duration, health and death.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## CON-255 — Colonist work requires compatible access, shift and capability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a staffed building receives productive labour only from an
  eligible working-age colonist who can reach it during an open shift, with
  specialization, traits, health and morale modifying performance.
- Includes: Surviving Mars: Relaunched dome workplaces, outside extractors,
  passages, shuttles and specialist bonuses or penalties.
- Excludes: drone errands; one abstract workforce pool; autonomous unstaffed
  production.
- Parameters: colonist, age, specialization, trait, health, morale, dome,
  route, shift, job slot and performance.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## CON-256 — Mars rocket operation requires vehicle, manifest, fuel and site

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a rocket flight or landing resolves only when an eligible rocket
  can carry the selected manifest, the origin supplies required fuel, the
  destination is currently available and a compatible landing site is reserved.
- Includes: Surviving Mars: Relaunched patch 1.0.7 Earth, Mars, asteroid-capable
  and planetary-project universal rocket operations.
- Excludes: local shuttle flights; a rocket assembled for one terminal launch;
  direct spacecraft piloting.
- Parameters: rocket class, capacity, manifest, fuel, destination, project
  requirements, landing pad, obstruction, automation and return eligibility.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## CON-257 — Mars research requires reveal, prerequisites and point cost

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a technology can enter and advance through the queue only after
  it is revealed and its positional or explicit prerequisites permit access;
  completion requires its full research-point cost.
- Includes: Surviving Mars: Relaunched shuffled fields, anomaly reveals,
  breakthroughs and five-slot queue.
- Excludes: a construction material delivery; an unrevealed technology guessed
  by the player; instant catalogue purchase.
- Parameters: field, shuffled position, reveal source, prerequisite, queue
  capacity, cost, progress and unlock.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## CON-258 — Martian law requires preparation, eligibility and voting support

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a law option can be enacted only after its chamber, preparation
  and state prerequisites are satisfied and the called vote obtains the
  required current faction or seat support.
- Includes: Surviving Mars: Relaunched Council and Assembly laws, negotiated
  promises, locked options and repealable multi-choice laws.
- Excludes: Frostpunk's unilateral permanent signing cooldown; research;
  temporary narrative choices.
- Parameters: chamber, preparation, prerequisite, option, faction support,
  seat allocation, promise, vote threshold, upkeep and repeal rule.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## CON-259 — Martian Assembly transition requires a staffed dome spire

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the Earth Council gives way to Martian governance only after the
  unlocked Assembly spire is built in a compatible dome and the new government,
  representation and opposition rules are selected.
- Includes: Surviving Mars: Relaunched Martian Assembly formation.
- Excludes: early Council sessions; one ordinary service building; independence
  payment after the Assembly exists.
- Parameters: technology, dome size, spire slot, materials, staff, government,
  seat rule, Assembly authority and opposition policy.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## CON-260 — Independence requires colony, mission, law and payment gates

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: sponsor control ends only after the colony meets its disclosed
  stability and population conditions, completes required sponsor and people's
  goals, enacts the declaration law and pays the remaining independence price.
- Includes: Surviving Mars: Relaunched patch 1.0.7 purchased-independence route.
- Excludes: declaration alone; optional post-independence goals; military
  victory or full terraforming.
- Parameters: stability, population, comfort, enacted laws, sponsor goals,
  people's goals, declaration, contribution, price and payment.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## CON-261 — Round purchase requires time, location and currency

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a match item can be purchased only while its buy window remains,
  the player is in the permitted spawn area and the current balance covers its price.
- Includes: Counter-Strike 2 Competitive buy-time purchases.
- Excludes: picking up a dropped weapon; a persistent metagame store.
- Parameters: buy time, zone, price, balance, role and refund eligibility.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md).
- Novelty: not assessed.

## CON-262 — Round inventory obeys weapon, grenade and ammunition capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a living player may carry only the permitted weapon-slot classes,
  grenade counts and finite magazine/reserve ammunition for the current life.
- Includes: Counter-Strike 2 primary/secondary slots, grenade limits and finite
  ammunition; Helldivers 2 primary, secondary and support weapons, carried
  grenade limit and finite magazine/reserve ammunition; Rainbow Six Siege
  operator weapon, secondary-gadget and finite ammunition/charge capacity.
- Excludes: unlimited abstract score resources; a crafting-grid stack limit.
- Parameters: slots, item class, grenade type/count, magazine and reserve.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md) and
  [Helldivers 2 decomposition](../games/g-l/helldivers-2.md) and
  [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md), and
  [War Thunder decomposition](../games/s-z/war-thunder.md), and
  [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
- Additional support: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md),
  for typed weapon/support slots and finite magazine/reserve ammunition.
- Additional support: [Destiny 2 decomposition](../games/a-f/destiny-2.md),
  for three typed weapon slots and finite magazine/reserve ammunition.
- Novelty: not assessed.

## CON-263 — Elimination suspends control until the next round

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a defeated participant cannot move, attack or operate the
  objective for the remainder of the current round and returns only at the
  following round boundary.
- Includes: Counter-Strike 2 Competitive one-life round participation and
  Rainbow Six Siege final elimination after any eligible injury/revival window.
- Excludes: the temporary incapacitation before final elimination; permanent run death;
  immediate deathmatch respawn.
- Parameters: defeat state, spectator channel, round boundary and re-entry.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md)
  and [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Novelty: not assessed.

## CON-264 — Planted round-device interaction requires role, site and uninterrupted time

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: planting requires an eligible living attacker with the round
  device inside a valid site, while neutralisation requires an eligible living
  defender at the planted device; interruption prevents channel completion.
- Includes: Counter-Strike 2 C4 plant and kit-sensitive defuse gates; Rainbow
  Six Siege defuser plant and disable gates.
- Excludes: damaging the bomb; instant capture-zone occupancy.
- Parameters: role, device holder, site, range, duration, kit and interruption.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md)
  and [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Novelty: not assessed.

## CON-265 — Planted round-device objective uses an asymmetric two-stage deadline

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: expiry of the unplanted round clock awards the defenders, but a
  completed plant replaces that deadline with a separate live device timer that
  can be beaten only by a completed neutralisation.
- Includes: Counter-Strike 2 Competitive round/C4 timers and Rainbow Six Siege
  action-phase/defuser timers.
- Excludes: one symmetric attempt timer; overtime match scheduling.
- Parameters: round time, plant completion, device timer, neutralisation duration and winner.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md)
  and [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Novelty: not assessed.

## CON-266 — Fixed team role bounds objective authority and friendly interaction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each participant belongs to one current team role that determines
  spawn, equipment access and objective authority while ordinary collision and
  friendly-fire rules still apply among teammates.
- Includes: Counter-Strike 2 Terrorist/Counter-Terrorist roles and Rainbow Six
  Siege attacker/defender roles with configured friendly fire.
- Excludes: hidden traitor roles; individually changing allegiance mid-round.
- Parameters: team, side, spawn, equipment, objective rights and friendly fire.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md)
  and [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Novelty: not assessed.

## CON-267 — Bomb-match score has a bounded regulation and overtime policy

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the match declares finite regulation halves, a role-swap boundary,
  an early clinch threshold and an explicit draw or bounded-overtime policy.
- Includes: Counter-Strike 2 Competitive MR12 regulation and Rainbow Six Siege
  Pro League twelve-round regulation with finite three-round overtime.
- Excludes: tournament series formats; one isolated round; unbounded scheduling.
- Parameters: half length, maximum rounds, clinch score, role swap, draw,
  overtime rounds and score difference.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md)
  and [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Novelty: not assessed.

## CON-268 — Each fixed team slot commits one match hero

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a fixed-size team assigns exactly one available match character
  to each player slot, subject to the current roster conflict rule.
- Includes: Dota 2 five-player All Pick commitment; Apex Legends three-player
  non-duplicate Legend commitment; Rainbow Six Siege five-player non-duplicate
  operator commitment subject to current bans.
- Excludes: swapping controlled heroes during live play; cosmetic loadouts.
- Parameters: team size, slot, hero pool, phase and duplicate/conflict rule.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md),
  [Apex Legends decomposition](../games/a-f/apex-legends.md) and
  [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Novelty: not assessed.

## CON-269 — Ability use requires legal target, range, resource and readiness

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a combatant or item ability resolves only when its cast form, target,
  range, mana or charges, cooldown and disabling-state gates are satisfied.
- Includes: Dota 2 targeted, point, vector, channelled, toggle and no-target
  casts; Cyberpunk 2077 quickhacks and active cyberware gated by target, RAM,
  charge or cooldown; Marvel Rivals hero abilities gated by current target,
  reach, charge, cooldown, control and ultimate-energy state; Battlefield 6
  class gadgets gated by target, range, charge, cooldown and combat state;
  Hollow Knight: Silksong Tools, Silk Skills and Bind gated by equipped state,
  reach, Silk, charge and readiness; Helldivers 2 stratagems gated by selected
  loadout, valid target, charges, cooldown, signal state and destroyer support;
  Rainbow Six Siege gadgets gated by operator loadout, target/surface, charges
  and current disabling state.
- Excludes: passive effects; ordinary basic attacks.
- Parameters: cast form, target class, range, mana, charge, cooldown and disable.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md) and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md), and
  [Battlefield 6 decomposition](../games/a-f/battlefield-6.md), and
  [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md), and
  [Helldivers 2 decomposition](../games/g-l/helldivers-2.md),
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md) and
  [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md), and
  [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
- Additional support: [Destiny 2 decomposition](../games/a-f/destiny-2.md),
  for Titan grenade, melee, barricade and Super readiness gates.
- Novelty: not assessed.

## CON-270 — Character build is bounded by level and branch gates

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: character build points can enter only ability ranks or bounded
  talent and attribute choices currently unlocked by that character's level
  and prerequisite state.
- Includes: Dota 2 skill ranks and talent tiers; Clair Obscur: Expedition 33
  attribute allocation and connected skill trees; Cyberpunk 2077 attribute
  thresholds and prerequisite-linked perk ranks.
- Excludes: item purchases; pre-match facet choice; account-wide unlocks.
- Parameters: persistence, level, available point, rank cap, prerequisite,
  talent tier and branch.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md) and
  [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## CON-271 — Item ownership obeys gold, shop and logistics capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: purchasing, carrying and delivering a match item requires its
  price, eligible shop access and compatible hero, backpack, stash or courier slot.
- Includes: Dota 2 base/secret shop, inventory, backpack, stash and courier.
- Excludes: cosmetic inventory; neutral-item roster details.
- Parameters: gold, shop, stock, item class, slots, stash and courier.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md).
- Novelty: not assessed.

## CON-272 — Death blocks combatant control until return or eligible buyback

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a dead combatant cannot move, attack or use live abilities until
  the current return timer and spawn gates are satisfied, unless its rules
  expose an eligible paid early return.
- Includes: Dota 2 death, level-sensitive respawn and buyback cooldown; Marvel
  Rivals knockout and ordinary timed spawn-room return without buyback;
  Battlefield 6 Conquest death and delayed legal redeployment; Helldivers 2
  death until a teammate's legal Reinforce or depleted-stock recharge return.
- Excludes: one-life match removal; allied units that remain controllable.
- Parameters: death, level, timer, spawn gate, gold, buyback cost, cooldown and
  return point.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md) and
  [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md), and
  [Battlefield 6 decomposition](../games/a-f/battlefield-6.md), and
  [Helldivers 2 decomposition](../games/g-l/helldivers-2.md), and
  [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
- Novelty: not assessed.

## CON-273 — Fog and detection gate actionable hostile state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: current hostile position and ordinary direct targeting require
  allied vision, while invisible entities additionally require eligible detection.
- Includes: Dota 2 fog of war, elevation/trees, invisibility and true sight.
- Excludes: remembered last position; globally revealed objective state.
- Parameters: vision source, occlusion, elevation, invisibility and detection.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md) and
  [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
- Novelty: not assessed.

## CON-274 — Base buildings obey ordered protection and backdoor rules

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: inner structures become legally vulnerable only after their
  current predecessor/protection gates, while unsupported attacks may trigger
  backdoor resistance and recovery.
- Includes: Dota 2 tower, barracks and high-ground protection order.
- Excludes: ordinary hero armour; invulnerability from a hero spell.
- Parameters: tier, predecessor, lane pressure, backdoor state and recovery.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md).
- Novelty: not assessed.

## CON-275 — Terminal loss requires a legally exposed Ancient

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the match-ending structure cannot take terminal legal damage
  until its required base protection is removed; hero or barracks loss alone
  never substitutes for Ancient destruction.
- Includes: Dota 2 standard-map Ancient victory gate.
- Excludes: surrender votes; kill-score thresholds; tournament adjudication.
- Parameters: protection structures, Ancient health, legal damage and winner.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md).
- Novelty: not assessed.

## CON-276 — Capture requires an eligible target and available device

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an ordinary capture attempt can resolve only when a carried
  compatible device reaches a capturable creature, with target health, status
  and device strength determining rather than guaranteeing its chance.
- Includes: Palworld wild-Pal capture with Pal Spheres; Pokémon Legends: Z-A
  wild capture with the selected compatible Poké Ball.
- Excludes: uncapturable trainer bosses; scripted guaranteed quest capture;
  storage transfers.
- Parameters: target class, health, status, device tier, capture power,
  inventory count and probability.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md) and
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Novelty: not assessed.

## CON-277 — Companion rosters have distinct bounded capacities

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: captured companions occupy typed storage, active-party or
  ruleset-specific assignment slots, and a transfer or new capture must resolve
  to an available destination under that roster's capacity.
- Includes: Palworld Palbox storage, five-Pal party and base-Pal capacity;
  Pokémon Legends: Z-A Boxes and six-member party capacity.
- Excludes: carried item stacks; multiplayer Guild membership; cosmetic display slots.
- Parameters: roster, slot count, occupied slots, overflow rule, base level and transfer.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md) and
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Novelty: not assessed.

## CON-278 — Technology purchase requires level, predecessor and points

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a technology node can be bought only after its player-level and
  predecessor gates are met and enough unspent technology points exist.
- Includes: Palworld ordinary and Ancient Technology unlocks.
- Excludes: recipes granted directly by a mission; base work suitability;
  account DLC ownership.
- Parameters: level, predecessor, point type, cost, known node and unlock.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md).
- Novelty: not assessed.

## CON-279 — Base task requires matching suitability and reachable facility

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a base companion may perform a task only when its work
  suitability includes the task type and it can reach the compatible supplied
  facility within the base.
- Includes: Palworld suitability-gated planting, mining, transport and Handiwork.
- Excludes: party combat skills; player hand crafting; priority among tasks
  after eligibility is established.
- Parameters: companion, suitability, task, facility, assignment, path, input and output.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md).
- Novelty: not assessed.

## CON-280 — Base labour depends on food, rest and recoverable condition

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an assigned base companion remains productive only while food,
  rest, sanity and health permit work; starvation, exhaustion, injury or illness
  interrupts or reduces its task execution until supported.
- Includes: Palworld food boxes, beds, hot springs, medicine and Pal work state.
- Excludes: an abstract global workforce count; avatar temperature; cosmetic mood.
- Parameters: hunger, sanity, health, food access, bed, recovery facility,
  illness and treatment.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md).
- Novelty: not assessed.

## CON-281 — Avatar survival depends on climate-compatible equipment and resources

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the avatar's current health and activity remain viable only while
  hunger, temperature exposure, stamina, armour and equipment durability stay
  within recoverable limits for the current region and action.
- Includes: Palworld food, heat/cold protection, stamina, armour and equipment durability.
- Excludes: companion SAN; custom world-setting multipliers; one boss timer.
- Parameters: hunger, temperature, protection, stamina, health, armour,
  durability, food and recovery.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md) and
  [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Novelty: not assessed.

## CON-282 — Main-story encounters require ordered authored gates

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each required main-story encounter starts and advances only after
  its authored prior-mission, discovery, switch, key-item, party, location or
  time-limit conditions are satisfied.
- Includes: Palworld tower access, Sunreach defence modules, Echoing Flute,
  Panthalus party gate and World Tree story sequence; Grand Theft Auto V
  protagonist, setup, location and prior-mission gates on the critical path;
  Cyberpunk 2077 main jobs and their ordered predecessor and choice gates.
- Excludes: optional hard-mode tower rematches; free-roaming Alpha Pals;
  post-story challenge raids.
- Parameters: mission, predecessor, boss, switches, key item, required actor,
  location, timer and completion flag.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md) and
  [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## CON-283 — Aircraft route bounds reachable insertion region

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the participant's initial ground region must be reachable from
  the sampled aircraft line through the finite altitude, fall speed, steering
  and parachute glide available after the chosen exit time.
- Includes: PUBG Normal Match landing choice from the current transport plane.
- Excludes: selecting any map coordinate as a spawn; later vehicle travel;
  teammate Recall insertion.
- Parameters: flight line, exit point, altitude, velocity, canopy, glide range,
  collision and landing surface.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md).
- Novelty: not assessed.

## CON-284 — Backpack capacity and equipment slots bound carried load

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: world-loot transfer succeeds only while its bulk fits current
  carried capacity and its weapon, attachment, armour or backpack class fits an
  available compatible equipment slot.
- Includes: PUBG backpack levels, item capacity values, two primary-weapon
  slots, sidearm, melee, throwable and protection slots; Cyberpunk 2077 carry
  weight and weapon/equipment slot compatibility.
- Excludes: ammunition compatibility inside a weapon; unlimited abstract
  currency; one fixed-grid crafting inventory.
- Parameters: backpack tier, bulk, free capacity, slot class, equipment item,
  replacement and excess quantity.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md) and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## CON-285 — Weapon operation requires compatible live equipment state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: firing, reloading or attaching equipment is legal only when the
  current weapon, ammunition, magazine, attachment slot, fire mode and avatar
  action state satisfy that operation's compatibility rules.
- Includes: PUBG ammunition classes, loaded and reserve rounds, magazines,
  scopes, muzzle, grip and stock restrictions; Cyberpunk 2077 ammunition,
  magazine, weapon-slot and compatible-mod state.
- Excludes: backpack bulk itself; ballistic hit resolution after a legal shot;
  cosmetic weapon skins.
- Parameters: weapon class, ammunition, chamber, magazine, attachment slot,
  fire mode, posture, vehicle lean and action lock.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md) and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## CON-286 — Restorative item requires legal state and uninterrupted cast

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a carried restorative or repair item produces its effect only
  when the matching Health, armour or equipment meter permits use and the
  player completes its live cast without a cancelling movement, weapon or
  damage event.
- Includes: PUBG bandage, First Aid Kit, Med Kit and boost-item restrictions;
  NARAKA: BLADEPOINT Vitalia, Armor Powder and Weapon Repair Kit restrictions.
- Excludes: passive healing; instant armour protection; teammate revival.
- Parameters: item, target meter or equipment, current value, target cap, cast
  duration, allowed movement, cancellation event and environmental interaction.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md)
  and [NARAKA: BLADEPOINT decomposition](../games/m-r/naraka-bladepoint.md).
- Novelty: not assessed.

## CON-287 — Armour protects only covered regions while durable

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: equipped armour reduces incoming damage only for its declared
  body region and tier while positive durability remains; other regions or
  broken equipment receive no such reduction.
- Includes: PUBG helmets protecting head hits and vests protecting torso hits.
- Excludes: cover blocking the projectile before impact; health restoration;
  a permanent character defence statistic.
- Parameters: armour slot, tier, body region, reduction, penetration, durability
  loss and break state.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md).
- Novelty: not assessed.

## CON-288 — Vehicle operation requires viable seat, fuel and geometry

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: direct vehicle control requires an accessible compatible seat and
  remaining operating state; terrain, collision, tyres, speed and any exposed
  fuel reserve bound travel and can make an unsafe moving exit injurious.
- Includes: PUBG Erangel land vehicles, seats, fuel, damaged tyres and exit
  risk; Grand Theft Auto V Story Mode road, water and air vehicle operation;
  Cyberpunk 2077 road vehicles, whose operating state has no exposed fuel gate.
- Excludes: the uncontrolled transport aircraft; route-scheduled autonomous
  vehicles; movement on foot.
- Parameters: seat, entry reach, driver role, fuel, tyre, vehicle health,
  terrain, clearance, speed and exit threshold.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md)
  [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## CON-289 — Phased safe areas impose escalating live deadlines

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: each revealed safe circle becomes the next viable region on a
  forced schedule, and remaining outside its contracting Blue boundary incurs
  health loss that grows with uninterrupted exposure.
- Includes: PUBG Update 42.1 Normal Match Blue Zone pressure.
- Excludes: one static arena wall; Red Zone blast risk; a turn-count move limit.
- Parameters: phase, circle, warning, contraction, travel distance, exposure
  duration, damage curve, healing and terminal phase.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md).
- Novelty: not assessed.

## CON-290 — Solo lethal defeat is permanent for the match

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: once a Solo participant reaches lethal defeat, direct control and
  objective eligibility cannot return during that match through revival,
  Recall, respawn or another round.
- Includes: PUBG Normal Solo elimination.
- Excludes: Duo or Squad DBNO and Recall; Counter-Strike next-round return;
  Minecraft world respawn.
- Parameters: mode, lethal state, self-recovery exception, spectating and match boundary.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md).
- Novelty: not assessed.

## CON-291 — Terrain deformation requires supported surface and source

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: ground volume changes only on a map region and surface marked as
  destructible, when an eligible tool or explosion reaches it, and never beyond
  the system's maximum range or depth.
- Includes: PUBG Update 41.1 Erangel terrain affected by pickaxe, Frag Grenade,
  Mortar, Panzerfaust, C4 or vehicle explosion, with excluded areas.
- Excludes: building destruction; arbitrary digging on unsupported terrain;
  cosmetic impact marks.
- Parameters: map, surface, protected area, source, range, damage, volume and depth.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md).
- Novelty: not assessed.

## CON-292 — Building placement requires legal geometry and stability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a building block may be placed only at a compatible terrain or
  socket pose with clearance, support and stability and outside protected
  monument restrictions.
- Includes: Rust foundation, wall, floor and roof placement previews.
- Excludes: free inventory rearrangement; deployables; terrain excavation.
- Parameters: shape, socket, terrain, overlap, orientation, support, stability,
  monument radius and preview.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## CON-293 — Building grade and repair require material and repair state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a connected block can reach a selected grade or regain health
  only when the player supplies that grade's material and the block is in a
  currently repairable, authorised state.
- Includes: Rust Hammer upgrades and post-damage repairs.
- Excludes: upkeep payment; raid damage; cosmetic skin.
- Parameters: current and target grade, material, cost, privilege, health,
  damage delay and repair amount.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## CON-294 — Building privilege gates protected construction operations

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: within a connected Tool Cupboard's projected region, ordinary
  building and protected pickup require current authorisation, with only
  explicitly allowed hostile-placement exceptions.
- Includes: Rust BUILDING BLOCKED, authorised pickup, twig-floor and ladder exceptions.
- Excludes: locked-door access; damaging an enemy block; unclaimed terrain.
- Parameters: region, identity, authority, operation, exceptions and overlap.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## CON-295 — Upkeep protection requires connected TC material coverage

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a building block avoids grade-specific decay only while connected
  to a Tool Cupboard whose inventory covers that grade's charged upkeep;
  separate buildings require separate connected coverage.
- Includes: Rust wood, stone, metal and armoured upkeep shortages.
- Excludes: direct raid damage; special external-wall coverage; construction cost.
- Parameters: connection, TC, grade, material, rate, stored quantity and duration.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## CON-296 — Secured fixture operation requires matching authority

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a locked door, container or ownership fixture exposes its
  protected interaction only to an identity with its current key, code or
  authority, unless the lock or structure is destroyed.
- Includes: Rust Key Locks, Code Locks and locked Tool Cupboards.
- Excludes: building privilege alone; unlocked storage; administrator bypass.
- Parameters: fixture, lock, identity, key, code, authority and destroyed state.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## CON-297 — Crafting requires ingredients, knowledge and station context

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a personal craft request is legal only when the avatar owns its
  ingredients, knows the recipe, satisfies any required station tier, proximity
  and operating conditions and has capacity for the declared output.
- Includes: Rust hand-crafting, including Workbench-3 C4; Valheim recipes at an
  eligible covered Workbench.
- Excludes: Furnace smelting; Recycler conversion; recipe research.
- Parameters: recipe, ingredients, blueprint/knowledge, station, tier,
  proximity, cover/operating state, queue and output.
- Evidence: [Rust decomposition](../games/m-r/rust.md) and
  [Valheim decomposition](../games/s-z/valheim.md).
- Novelty: not assessed.

## CON-298 — Workbench progression requires ordered tiers and fragments

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: each higher Workbench may be crafted only from its predecessor
  plus the current material and blueprint-fragment recipe, so tier-three
  crafting cannot bypass the ordered workstation chain.
- Includes: Rust 2026 Workbench Level 2 and Level 3 recipes.
- Excludes: item research within a tier; module upgrades; custom recipes.
- Parameters: prior workbench, metal fragments, high-quality metal, basic or
  advanced blueprint fragments and resulting tier.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## CON-299 — Respawn fixture assignment and cooldown bound return

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a player may return at a placed sleeping fixture only while it
  exists, remains assigned to that identity and its shared cooldown has
  expired; otherwise another eligible spawn must be chosen.
- Includes: Rust Sleeping Bag respawn and long cooldown.
- Excludes: teammate revival; one-life elimination; server wipe.
- Parameters: fixture, identity, assignment, cooldown, destruction and alternative spawn.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## CON-300 — Structural breach requires sufficient material-specific damage

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: unauthorised access through a defended route becomes physically
  possible only after eligible accumulated damage exceeds every intervening
  door, lock or building block's current material health.
- Includes: Rust explosive breach through a locked base envelope.
- Excludes: open-door entry; authorised code use; natural upkeep decay.
- Parameters: route, layers, material, health, damage, resistance and charge count.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## CON-301 — Disconnected bodies remain vulnerable in the shared world

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: disconnecting does not remove or protect the avatar's sleeping
  body or owned structures; other participants and server processes may damage,
  loot or destroy them before reconnection.
- Includes: Rust offline killing, looting, raiding and decay.
- Excludes: safe logout; paused private save; spectator mode.
- Parameters: body, inventory, structure, disconnect, hostile participant,
  server tick and reconnect state.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## CON-302 — Scheduled wipe bounds all world persistence

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: every acquired world item, built structure and current island
  position persists for no longer than the server's declared wipe boundary,
  after which a new world cycle supersedes it.
- Includes: Rust default monthly first-Thursday force wipe.
- Excludes: ordinary death; restart without wipe; separately configured account state.
- Parameters: schedule, timezone, next wipe, world state, blueprint reset policy
  and replacement cycle.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## CON-303 — Occupation and traits require a legal point balance

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: character creation may continue only when one occupation and all
  selected traits satisfy their point costs, incompatibilities and required
  remaining balance.
- Includes: Project Zomboid Build 42 survivor creation.
- Excludes: skill experience earned after spawn; custom sandbox settings.
- Parameters: occupation, trait, cost, refund, incompatibility, balance and
  confirmation.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## CON-304 — Body state constrains movement and action performance

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: carried load, exertion, fatigue, pain, wounds, panic, temperature
  and related moodles may slow, weaken, prevent or make noisier the survivor's
  movement, combat and timed work.
- Includes: Project Zomboid encumbrance, endurance and injury penalties.
- Excludes: terrain collision by itself; cosmetic status; skill gates unrelated
  to current body state.
- Parameters: load, stamina, moodle, body region, severity, action, speed,
  accuracy, noise and prohibition threshold.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## CON-305 — Zombie pursuit requires a perceived cue and reachable route

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a zombie may begin or maintain pursuit only from eligible local
  sight, sound or recent target memory and can reach the survivor only through
  a pathable opening or destructible obstruction.
- Includes: Project Zomboid stealth, alarms, gunshots and barricade pathing.
- Excludes: omniscient global tracking; hit resolution after adjacency.
- Parameters: vision, cue volume, occlusion, memory, route, door, window,
  barricade and path failure.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## CON-306 — Weapon use requires viable body, reach and equipment state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a melee strike, shove, firearm shot or reload is legal and
  effective only when facing, reach, footing, exertion, panic, weapon condition,
  ammunition and current action state permit it.
- Includes: Project Zomboid direct combat and Build 42 precise aiming.
- Excludes: damage adjudication after a legal strike; vehicle collision.
- Parameters: target, facing, range, stance, stamina, panic, weapon, condition,
  sharpness, ammunition, jam and action lock.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## CON-307 — Wound care requires a compatible item and body region

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a treatment changes a wound only when the selected body region,
  injury class, carried medical item, accessibility and current treatment state
  admit that operation.
- Includes: Project Zomboid bandaging, disinfecting, splinting and foreign-body
  removal.
- Excludes: eating; passive healing; curing established Knox Infection.
- Parameters: region, wound, bleeding, item, treatment, prior treatment, skill,
  duration and result.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## CON-308 — Established Knox Infection has no ordinary cure path

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: once the hidden zombie-transmitted infection state is established
  under the canonical preset, bandages, disinfectant, food, sleep and ordinary
  medicine cannot restore that survivor to an uninfected state.
- Includes: Project Zomboid Apocalypse Knox Infection.
- Excludes: ordinary wound infection; sandbox transmission changes; preventing
  exposure before the transmission check.
- Parameters: transmission state, wound source, symptoms, treatments,
  mortality and reanimation.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## CON-309 — Barricading requires a compatible opening, tools and material

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: one defensive layer may be attached only to an eligible reachable
  door or window side with matching carried material, fastening tools and legal
  layer capacity; additional layers may progressively obstruct vision.
- Includes: Project Zomboid wooden and metal barricades.
- Excludes: free-standing walls; curtains; furniture placed nearby.
- Parameters: opening, side, layer capacity, material, tools, fasteners, skill,
  visibility and removal eligibility.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## CON-310 — Crafting and construction require learned reachable inputs

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a recipe or construction request can begin only when its recipe
  knowledge, skill level, tools, workstation or reachable ingredients and
  compatible placement state are all satisfied.
- Includes: Project Zomboid Build 42 crafting, workstations and shelter building.
- Excludes: barricade layer capacity; skill experience gain; autonomous work.
- Parameters: recipe, knowledge, skill, tool, workstation, ingredient, reach,
  placement, duration and output.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## CON-311 — Crop viability requires season, water and elapsed growth

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a planted crop reaches harvest only if its species remains within
  a viable seasonal window and receives enough time, water and health; a crop
  planted in a doomed month cannot gain ordinary yield merely by waiting.
- Includes: Project Zomboid Build 42 seasonal farming.
- Excludes: instant recipe crops; wild foraging; cosmetic garden state.
- Parameters: species, planting month, viable months, doomed months, water,
  disease, phase duration, skill and yield.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## CON-312 — Sleep and accelerated time remain vulnerable to danger

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: sleeping, waiting or accelerated timed work requires an eligible
  current state and does not make the survivor safe; detected threat, injury or
  another interruption returns control under the resulting world state.
- Includes: Project Zomboid single-player sleep and fast-forward.
- Excludes: pausing that freezes the world; invulnerable cutscenes; offline
  server progression.
- Parameters: tiredness, resting place, selected rate, threat, interruption,
  wake state and elapsed time.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## CON-313 — One survivor life cannot respawn after death

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: lethal bodily state permanently ends direct control of the
  current survivor; no checkpoint, bed, inventory item or same-character
  respawn can continue that analytical life.
- Includes: the scoped Project Zomboid Apocalypse life.
- Excludes: starting a different survivor in the retained save; temporary
  unconsciousness; multiplayer revival rules.
- Parameters: lethal threshold, character identity, corpse, save persistence,
  later character and statistics boundary.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Additional support: [DayZ decomposition](../games/a-f/dayz.md), where the
  scoped official-server identity cannot continue through the respawn command.
- Novelty: not assessed.

## CON-314 — Long-horizon supplies decay under the canonical calendar

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: inherited water, electricity and perishable food cannot be
  assumed indefinitely available: preset time windows may end utilities, while
  elapsed temperature-dependent aging reduces viable stored food.
- Includes: Project Zomboid Apocalypse utility shutoff and spoilage pressure.
- Excludes: player-configured sandbox dates; one fixed match clock; crops as a
  separate growth eligibility rule.
- Parameters: cutoff window, current service, refrigeration, generator, fuel,
  food age, temperature, freshness and spoilage.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## CON-315 — Raid entry obeys augment-shaped loadout capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a prepared raid loadout is legal only when each weapon, shield,
  ammunition, gadget, utility and carried stack fits slots and capacities
  exposed by the selected compatible augment, or by the smaller Free Loadout.
- Includes: ARC Raiders loadout and augment backpack layouts.
- Excludes: stash capacity outside a raid; cosmetic backpack appearance;
  world-loot transfer after all carried capacity is already free.
- Parameters: augment, weapon slots, shield class, quick-use slots, Safe Pocket,
  backpack capacity, item class and Free Loadout layout.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## CON-316 — Protected-pocket transfer requires eligible item and free slot

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an item can receive protected defeat retention only when its
  current class and use state are eligible for an unoccupied Safe Pocket slot
  exposed by the equipped augment.
- Includes: ARC Raiders Safe Pocket transfers and Safekeeper weapon exception.
- Excludes: ordinary backpack storage; post-raid stash placement; exploit-based
  pocketing of an active Snaphook or ineligible weapon.
- Parameters: item class, active state, augment, pocket count, free slot,
  stack compatibility and exception.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## CON-317 — Extraction requires a live reachable endpoint before closure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: successful return requires the Raider to reach an enabled
  extraction fixture, satisfy its call, key or entry interaction and cross its
  departure boundary before that endpoint or the raid closes.
- Includes: ARC Raiders elevators, metro extraction and Raider Hatches.
- Excludes: menu abandonment; extraction after knockout; reaching an inactive
  fixture without completing its interaction.
- Parameters: endpoint, map state, reach, key, call, arrival, entry zone,
  closure and raid clock.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## CON-318 — Knockout forfeits every unsecured raid item

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when a Raider is knocked out before extraction, every entered or
  scavenged item outside a valid protected pocket leaves persistent ownership,
  regardless of its prior stash origin.
- Includes: ARC Raiders ordinary loadout and backpack loss on Topside knockout.
- Excludes: Safe Pocket contents; automated Fair Play compensation after a
  confirmed cheater; items already banked in Speranza.
- Parameters: terminal state, entered item, scavenged item, secured flag,
  forfeited inventory and compensation exception.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## CON-319 — Search requires reach and uninterrupted interaction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a container, husk or disabled-machine search reveals contents
  only while the Raider remains within legal reach and completes its hold or
  continuous interaction without a cancelling equipment or movement change.
- Includes: ARC Raiders Topside container and ARC-remnant searches.
- Excludes: visible ground-loot pickup; already-open inventory inspection;
  remote search through geometry.
- Parameters: target, reach, duration, posture, equipment change, movement,
  interruption and reveal state.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## CON-320 — Workshop output requires station, recipe and retained ingredients

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a Workshop craft is legal only when its specialised station and
  required tier are unlocked, the recipe is currently known and all declared
  ingredients exist in eligible persistent inventory.
- Includes: ARC Raiders station-specific Speranza crafting and found blueprints.
- Excludes: Field Crafting recipes that need no Workshop station; Trader stock;
  cosmetic purchases.
- Parameters: station, tier, blueprint, recipe, ingredient, quantity, output
  capacity and Expedition reset state.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## CON-321 — Weapon maintenance requires a retained item and repair resources

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a repair or upgrade can change durability only for an owned
  compatible weapon whose current state permits the operation and whose
  declared resource cost is available.
- Includes: ARC Raiders resource-paid repair and upgrade-with-repair.
- Excludes: repairing an item lost Topside; free passive restoration; attaching
  a mod without changing durability.
- Parameters: ownership, weapon, tier, durability, upgrade state, resource,
  cost, repair cap and resulting durability.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## CON-322 — Skill purchase requires a point and predecessor state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a persistent Raider skill node can gain a rank only when an
  unspent skill point exists and all branch, predecessor and rank-cap
  requirements for that node are satisfied.
- Includes: ARC Raiders Conditioning, Mobility and Survival skill trees.
- Excludes: equipment perks; temporary Map Condition effects; automatic level
  benefits that require no choice.
- Parameters: branch, node, predecessor, current rank, cap, point balance and
  purchased modifier.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## CON-323 — Active battle formation is bounded by available expeditioners

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a battle may contain no more than the allowed active party size,
  and only currently recruited, living and story-available expeditioners may
  occupy those slots.
- Includes: the three-member active party in scoped Clair Obscur: Expedition 33.
- Excludes: switching the visible exploration leader; temporary summons;
  assigning passive abilities.
- Parameters: active slots, reserve roster, availability and defeat state.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md).
- Novelty: not assessed.

## CON-324 — Reactive defence requires the matching live timing window

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: dodge, parry or jump negates an incoming attack member only when
  that response is currently unlocked and its input lands inside the attack's
  matching real-time window.
- Includes: Clair Obscur: Expedition 33 defensive timing gates and the wider
  dodge than parry window; Black Myth: Wukong Perfect Dodge timing.
- Excludes: passive evasion chance; an accessibility option that automates a
  prompt; selecting a skill during the character's turn.
- Parameters: response type, unlock, cue, window, difficulty and assist mode.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md)
  and [Black Myth: Wukong decomposition](../games/a-f/black-myth-wukong.md).
- Novelty: not assessed.

## CON-325 — Picto slots and Lumina points bound passive build

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each character may equip only the allowed number of compatible
  Pictos and may activate only learned Luminas whose combined cost fits that
  character's current Lumina-point capacity.
- Includes: Clair Obscur: Expedition 33 Picto and Lumina loadouts.
- Excludes: weapon compatibility; skill-tree prerequisites; temporary combat AP.
- Parameters: slots, compatible Picto, learned state, passive cost and capacity.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md).
- Novelty: not assessed.

## CON-326 — Contextual cover requires reachable protective geometry

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: cover attachment, edge movement and aimed exposure are legal only
  while the controlled protagonist remains beside a compatible surface with a
  supported pose and unobstructed transition.
- Includes: Grand Theft Auto V Story Mode walls, vehicles and low cover.
- Excludes: visual scenery that cannot accept cover; standing behind an object
  without entering contextual cover; invulnerable scripted hiding.
- Parameters: surface, reach, height, edge, posture, clearance and exposure side.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md).
- Novelty: not assessed.

## CON-327 — Protagonist switching requires current authored availability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: direct control may transfer only to a currently unlocked, living
  and mission-permitted protagonist; restricted actions, pursuit or authored
  separation can temporarily block a switch.
- Includes: Grand Theft Auto V Story Mode character-wheel locks and scripted
  multi-protagonist switch windows.
- Excludes: selecting an unavailable online avatar; party-member turn order;
  cosmetic character skins.
- Parameters: unlock, survival, mission state, wanted state, activity, distance
  and scripted permission.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md).
- Novelty: not assessed.

## CON-328 — Wanted clearance requires an unseen search interval

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a non-scripted wanted level clears only after the controlled
  protagonist leaves active police perception and remains undiscovered through
  the complete star-dependent search interval; renewed sight resets pursuit.
- Includes: Grand Theft Auto V Story Mode line-of-sight evasion and flashing-star
  search state; Need for Speed Unbound LPD pursuit-to-search clearance.
- Excludes: GTA Online paid removal; mission scripts that hold a wanted level;
  defeating a fixed enemy encounter.
- Parameters: stars, sight source, search radius, concealment, interval,
  reacquisition and mission override.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md).
- Novelty: not assessed.

## CON-329 — Heist plan requires a legal approach and complete role roster

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a planned heist can advance only after one available approach is
  committed, every role it requires has an unlocked eligible specialist and
  the approach-specific setup conditions are complete.
- Includes: Grand Theft Auto V Story Mode major-heist planning and setup gates.
- Excludes: free-roam robberies; GTA Online lobby readiness; crew skill effects
  after a valid plan begins.
- Parameters: approach, required roles, candidate availability, setup mission,
  vehicle, equipment and completion state.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md).
- Novelty: not assessed.

## CON-330 — Mission-critical actors, assets and area must remain viable

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an active authored mission continues only while its controlled or
  protected actors remain alive and close enough, required vehicles or objects
  remain usable and the player does not abandon its permitted operation area.
- Includes: Grand Theft Auto V Story Mode failure from protagonist or ally death,
  abandoned targets, destroyed vehicles and leaving the mission action.
- Excludes: optional medal conditions that do not fail the attempt; free-roam
  property damage; ordinary hostile defeat.
- Parameters: actor, health, distance, area, asset, damage state, abandonment
  timer and checkpoint.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md).
- Novelty: not assessed.

## CON-331 — Carried weapon classes and ammunition have fixed capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the protagonist can retain only the permitted weapon entry per
  weapon-wheel class and no ammunition type above its current finite cap;
  firing and reloading require compatible remaining rounds.
- Includes: Grand Theft Auto V Story Mode weapon wheel, magazines, reserve
  ammunition and ammunition-capacity statistic.
- Excludes: PUBG backpack bulk; Counter-Strike round inventory; cosmetic weapon
  tints with no capacity effect.
- Parameters: weapon class, owned weapon, ammunition type, magazine, reserve,
  capacity statistic and pickup excess.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md).
- Novelty: not assessed.

## CON-332 — Initial build obeys lifepath and attribute-budget limits

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: campaign entry requires exactly one available lifepath and an
  initial attribute distribution whose values remain within per-attribute
  bounds and the fixed total point budget.
- Includes: Cyberpunk 2077 new-character mechanical setup.
- Excludes: cosmetic appearance; later point spending; difficulty selection.
- Parameters: lifepath count, attribute set, minimum, maximum, budget and
  confirmation.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## CON-333 — Cyberware loadout obeys slot and capacity limits

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an implant may remain installed only in a compatible unlocked
  body slot and while the complete loadout's declared cost stays within current
  cyberware capacity except for an explicitly unlocked over-cap rule.
- Includes: Cyberpunk 2077 Update 2.0+ cyberware slots, capacity and Edgerunner
  exception.
- Excludes: weapon inventory slots; cosmetic wardrobe outfits; RAM spent by a
  quickhack after installation.
- Parameters: slot, compatibility, unlock, implant cost, capacity, exception,
  health trade-off and replacement.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## CON-334 — Quickhack requires access, target, RAM and readiness

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a quickhack upload is legal only with a compatible installed
  cyberdeck and hack, an eligible scanned target within access conditions,
  sufficient RAM or an unlocked substitute, and satisfied cooldown and queue
  gates.
- Includes: Cyberpunk 2077 base-game combat and device quickhacks, including
  Overclock's health-for-RAM exception when unlocked.
- Excludes: ordinary scanner information; weapon attacks; scripted story
  interfaces with no build or resource requirement.
- Parameters: cyberdeck, quickhack, target class, range, access, RAM, health
  substitution, cooldown and queue capacity.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## CON-335 — Stealth neutralisation requires unaware reachable target

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a grapple or stealth takedown remains available only while one
  eligible hostile is within the required relative position and has not
  completed detection or entered a disallowing combat or strength state.
- Includes: Cyberpunk 2077 lethal and non-lethal stealth takedowns.
- Excludes: ordinary melee attacks; remote quickhacks; scripted restrained
  characters.
- Parameters: awareness, position, reach, target class, relative strength,
  combat state and interruption.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## CON-336 — Retained quest state gates later branch availability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a later quest, ally, response or terminal route is offered only
  when its authored prerequisite missions and retained earlier decisions satisfy
  the current branch predicate; incompatible alternatives remain unavailable.
- Includes: Cyberpunk 2077 base-game side-job ending unlocks and the always
  available Arasaka route after the required main jobs.
- Excludes: choosing among already available options; linear prior-mission
  order alone; Phantom Liberty's separate ending path.
- Parameters: prior quest, decision flag, ally state, relationship, offered
  response, terminal route and incompatibility.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## CON-337 — Attribute threshold gates contextual interaction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an authored dialogue response or physical, technical or network
  interaction is selectable only when the controlled character's matching
  current attribute meets the displayed or applied threshold.
- Includes: Cyberpunk 2077 Body, Intelligence, Technical Ability, Reflexes and
  Cool contextual checks.
- Excludes: perk-tree prerequisites; weapon stat requirements; lifepath-only
  options with no attribute threshold.
- Parameters: interaction, attribute, threshold, current value, modifier,
  visibility and alternate route.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## CON-338 — Hero and Team-Up changes require a legal spawn state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: one team slot may control only a currently available hero not
  already occupied by that team, and hero or Team-Up loadout changes take
  effect only through the permitted spawn-room selection state.
- Includes: Marvel Rivals Quick Match team hero uniqueness, initial selection,
  post-knockout swaps and Season 9 Team-Up option changes in spawn.
- Excludes: role queue or a required 2-2-2 composition; a permanent match-long
  draft commitment; cosmetic selection.
- Parameters: team, slot, hero, duplicate state, spawn room, living state,
  partner option and confirmation.
- Evidence: [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md).
- Novelty: not assessed.

## CON-339 — Team-Up enhancement requires the selected allied partner

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a selected Team-Up loadout supplies its hero's base effect, but
  its declared enhanced effect remains inactive unless the corresponding
  designated partner is simultaneously present on the allied team.
- Includes: Marvel Rivals Season 9 two-option Team-Up loadouts and partner-gated
  enhanced hero effects.
- Excludes: ordinary role synergy; a passive that never checks team composition;
  an opponent copying a hero with an ultimate.
- Parameters: selected option, owner, allied partner, base effect, enhanced
  effect, partner arrival, partner departure and spawn change.
- Evidence: [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md).
- Novelty: not assessed.

## CON-340 — Convergence capture and escort obey ordered control gates

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: attackers may escort only after completing the opening mission-area
  capture, and either phase progresses only from eligible objective presence
  without an active opposing contest.
- Includes: Marvel Rivals Convergence capture-before-escort order, vehicle
  checkpoints and contested stops.
- Excludes: free vehicle driving; Domination control percentages; eliminating
  all opponents as an independent terminal win.
- Parameters: phase, objective, eligible side, presence, contest, checkpoint and route.
- Evidence: [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md).
- Novelty: not assessed.

## CON-341 — Overtime requires continuing legal objective pressure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: clock expiry extends an asymmetric objective phase only while
  attackers maintain that ruleset's current capture, escort or touch-renewal
  condition; once legal pressure clears, defence receives the terminal result.
- Includes: Marvel Rivals Convergence capture-point and mission-vehicle
  overtime; Team Fortress 2 Payload pressure and its five-second renewal window.
- Excludes: automatic extra time with no objective presence; competitive
  tournament tie-break maps; a checkpoint's ordinary time award.
- Parameters: clock, phase, attacker presence, contest, decay, clearance and result.
- Evidence: [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md) and
  [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
- Novelty: not assessed.

## CON-342 — Custom character creation obeys compatible build budgets

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a custom campaign character can be confirmed only when lineage,
  class, background, ability point-buy, bonuses and proficiency choices satisfy
  their current compatibility, minimum, maximum and budget rules.
- Includes: Baldur's Gate 3 custom Tav character creation.
- Excludes: cosmetic appearance; later respec services; fixed Origin builds.
- Parameters: choice set, compatibility, point budget, minimum, maximum,
  proficiency source, duplicate rule and confirmation.
- Evidence: [Baldur's Gate 3 decomposition](../games/a-f/baldurs-gate-3.md).
- Novelty: not assessed.

## CON-343 — Combat turns are bounded by movement and action resources

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during one creature's combat turn, movement distance and each
  Action, Bonus Action and Reaction may be spent only by a compatible action
  while that resource remains available, unless a declared feature grants or
  substitutes an additional resource.
- Includes: Baldur's Gate 3 ordinary turn action economy.
- Excludes: initiative ordering; spell-slot cost; real-time exploration input.
- Parameters: creature, turn, movement, Action, Bonus Action, Reaction,
  compatible cost, extra resource, substitution and refresh.
- Evidence: [Baldur's Gate 3 decomposition](../games/a-f/baldurs-gate-3.md).
- Novelty: not assessed.

## CON-344 — Spell use obeys preparation, slot and concentration gates

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a spell may resolve only when learned or prepared and when its
  casting, target, slot and class-resource costs are legal; one caster may
  maintain no more than one concentration spell at a time.
- Includes: Baldur's Gate 3 prepared and known spells, spell slots, upcasting
  and concentration replacement.
- Excludes: weapon attacks; item effects with no spell resource; dialogue checks.
- Parameters: caster, known state, prepared state, action cost, slot level,
  target, range, class resource, upcast and concentration occupant.
- Evidence: [Baldur's Gate 3 decomposition](../games/a-f/baldurs-gate-3.md).
- Novelty: not assessed.

## CON-345 — Rest requires legal safety, remaining use or camp supplies

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: rest is unavailable in disallowing danger or authored areas; a
  short rest requires a remaining charge, while a full long rest requires the
  current difficulty's camp-supply threshold and otherwise resolves only a
  partial rest.
- Includes: Baldur's Gate 3 Balanced short-rest charges and 40-supply full rest.
- Excludes: restoration pods; restorative potions; save loading.
- Parameters: danger state, area permission, rest type, remaining charge,
  difficulty, supply threshold, committed supply and partial-rest fallback.
- Evidence: [Baldur's Gate 3 decomposition](../games/a-f/baldurs-gate-3.md).
- Novelty: not assessed.

## CON-346 — Deployment loadout must fit its selected class

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a legal combat loadout must select one class and use only the
  weapons, capability paths, gadget slots, class tools and throwables permitted
  for that class and playlist.
- Includes: Battlefield 6 Open Weapons Conquest loadouts with class-bound
  gadgets, Training Paths and signature equipment; the controlled Team
  Fortress 2 class's always-available stock weapon set in Casual Payload.
- Excludes: cosmetic customisation; switching the active carried weapon;
  Closed Weapons as the scoped playlist.
- Parameters: class, playlist, unlock state, Training Path, weapon availability,
  attachment points, gadget slots and throwable.
- Evidence: [Battlefield 6 decomposition](../games/a-f/battlefield-6.md) and
  [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
- Novelty: not assessed.

## CON-347 — Redeployment requires a ready and legal team source

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: redeployment is legal only after its current delay and at a team
  headquarters, owned point, eligible non-combat squad source, active beacon
  or compatible vehicle with a free usable seat.
- Includes: Battlefield 6 Conquest deployment-map source eligibility.
- Excludes: revival before death; direct walking; enemy-controlled objectives;
  a full or unsafe vehicle seat.
- Parameters: timer, team, source class, ownership, combat state, beacon state,
  vehicle, seat and entry clearance.
- Evidence: [Battlefield 6 decomposition](../games/a-f/battlefield-6.md).
- Novelty: not assessed.

## CON-348 — Control progress requires uncontested eligible presence

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: control-point progress toward one team requires at least one
  eligible living member of that team inside the authored area and no eligible
  opposing presence contesting it.
- Includes: Battlefield 6 Conquest capture and neutralisation on foot or in an
  eligible vehicle.
- Excludes: ticket drain after ownership; a ranged kill outside the area;
  capture-to-escort phase ordering.
- Parameters: area, team, living state, vehicle eligibility, occupancy,
  opposing presence, contest and progress direction.
- Evidence: [Battlefield 6 decomposition](../games/a-f/battlefield-6.md) and
  [War Thunder decomposition](../games/s-z/war-thunder.md).
- Novelty: not assessed.

## CON-349 — Authored route edges require their acquired capability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an authored movement edge or mechanism is usable only after the
  current save has retained its named traversal or interaction capability and
  the avatar supplies the compatible input at that locus.
- Includes: Hollow Knight: Silksong dash, glide or updraft, wall-cling and
  Needolin gates on the scoped route to the Grand Gate.
- Excludes: an ordinary jump available from the start; a purely narrative flag;
  an optional shortcut that needs no acquired capability.
- Parameters: route edge, mechanism, capability, locus, input and persistence.
- Evidence: [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md).
- Novelty: not assessed.

## CON-350 — Equipped tools must fit the selected Crest's coloured slots

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a tool can become active only in an unlocked slot whose colour
  accepts that tool under the currently selected Crest; changing Crest removes
  assignments that the replacement layout cannot preserve.
- Includes: Hollow Knight: Silksong red, blue and yellow Tool slots, Crest
  layouts and Memory Locket slot unlocks.
- Excludes: unrestricted carried inventory; cosmetic charms; changing only the
  currently held weapon.
- Parameters: Crest, slot colour, unlocked state, tool class, assignment and
  replacement handling.
- Evidence: [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md).
- Novelty: not assessed.

## CON-351 — Bind and Silk Skills require their declared Silk state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the Bind action is legal only when the current Silk spool is full and always
  consumes that spool, while each Silk Skill requires and consumes its own
  declared amount from the same bounded resource.
- Includes: Hollow Knight: Silksong ordinary Bind, Silkspear and Needolin.
- Excludes: a cooldown-only ability; passive Crest effects; ordinary needle
  attacks that generate rather than spend Silk.
- Parameters: current Silk, spool capacity, full predicate, Bind cost, skill
  cost and disabled state.
- Evidence: [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md).
- Novelty: not assessed.

## CON-352 — Only one unrecovered death-currency mark may persist

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the current save may retain only one unrecovered death-currency
  mark; another ordinary death replaces it and permanently loses the currency
  still stored in the earlier mark, including when the new stock is empty.
- Includes: Hollow Knight: Silksong ordinary-mode Cocoon replacement; Elden
  Ring replacement of the previous rune mark on a later death.
- Excludes: several simultaneously recoverable item piles; permanent Steel
  Soul death; currency protected before death in a separate string.
- Parameters: existing mark, new death, old and new currency stocks,
  replacement, protected currency and recovery state.
- Evidence: [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md);
  [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## CON-353 — Field weapon loadout contains one active and one mount-carried weapon

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: away from camp the hunter may retain exactly one active weapon
  and one assigned secondary on the Seikret, and may exchange them only through
  the eligible mounted interaction.
- Includes: Monster Hunter Wilds two-weapon Seikret loadout.
- Excludes: unrestricted access to equipment storage; carried consumables;
  cosmetic weapon layers.
- Parameters: active slot, secondary slot, camp assignment, mounted state,
  exchange and weapon compatibility.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## CON-354 — Weapon actions require stamina, maintenance and recovery state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a weapon move resolves only when its current stamina, sharpness
  or ammunition requirement and previous-animation recovery state permit it.
- Includes: Monster Hunter Wilds melee stamina and sharpness, ranged ammunition
  and committed weapon animations; Black Myth: Wukong staff, dodge and sprint
  stamina plus committed recovery state.
- Excludes: target-body legality after the move begins; inventory capacity;
  long-term smithy upgrade requirements.
- Parameters: weapon, move, stamina, sharpness, ammunition, charge, recovery
  frame and cancel rule.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md),
  [Monster Hunter: World decomposition](../games/m-r/monster-hunter-world.md)
  and [Black Myth: Wukong decomposition](../games/a-f/black-myth-wukong.md).
- Novelty: not assessed.

## CON-355 — Focus Strike requires highlighted reachable body state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a Focus Strike can convert localized body state only when Focus
  Mode exposes a compatible open wound or breakable part within the current
  weapon's legal aim and reach.
- Includes: Monster Hunter Wilds wound and breakable-part Focus Strike gates.
- Excludes: ordinary attacks against intact body regions; passive highlighting;
  a missed finisher outside reach.
- Parameters: focus state, wound, body part, weapon, aim, reach and compatibility.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## CON-356 — Hunt must finish before timer or faint allowance failure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an active quest succeeds only if its declared target condition is
  completed before the quest clock expires or the finite shared faint
  allowance is exhausted.
- Includes: Monster Hunter Wilds early assignment success and failure.
- Excludes: unrestricted expedition play; permanent save deletion; optional
  performance medals after a successful quest.
- Parameters: target, completion form, timer, remaining faints, failure event
  and retry boundary.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md)
  and [Monster Hunter: World decomposition](../games/m-r/monster-hunter-world.md).
- Novelty: not assessed.

## CON-357 — Crafting and smithing require recipe inputs and currency

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: creating a carried item or equipment result requires its known
  recipe, every compatible retained material quantity and any declared zenny
  or facility prerequisite.
- Includes: Monster Hunter Wilds field item crafting and smithy equipment
  creation or upgrades.
- Excludes: gathering raw material; a free quest reward; cosmetic DLC delivery.
- Parameters: recipe, ingredient, material category, quantity, zenny, facility,
  prerequisite and result.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## CON-358 — Gathering and carving require an eligible finite source

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a material extraction resolves only when the addressed source is
  reachable, eligible in the current state and retains at least one yield or
  carve opportunity within its interaction window.
- Includes: Monster Hunter Wilds field gathering and post-hunt large-monster
  carving.
- Excludes: automatic quest rewards; inventory pickup of an already loose item;
  an exhausted or expired carcass.
- Parameters: source, reach, eligibility, remaining yields, carve count,
  interaction window and result table.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md)
  and [Monster Hunter: World decomposition](../games/m-r/monster-hunter-world.md).
- Novelty: not assessed.

## CON-359 — Attribute requirements and equipment load gate combat form

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: effective armament use and dodge form depend on meeting declared
  attributes and remaining within the current equipment-load tier.
- Includes: Elden Ring armament requirements and light, medium or heavy load.
- Excludes: cosmetic weight; temporary slow alone; inventory stack capacity.
- Parameters: requirements, attributes, weight, capacity, ratio and dodge tier.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## CON-360 — Spirit Ash requires one eligible monument-bounded summon state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: spirit Ash use is legal only with its bell and resource inside an
  eligible monument area, outside multiplayer and without another active spirit.
- Includes: Elden Ring early field and boss Spirit Ash restrictions.
- Excludes: NPC summon signs; online co-op; unrestricted companion deployment.
- Parameters: bell, cost, area, multiplayer, concurrent spirit and boss state.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## CON-361 — Only the latest unrecovered death rune mark persists

- Lifecycle: `Merged`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: historical Elden Ring object-specific duplicate of the
  single-unrecovered death-currency-mark constraint represented by `CON-352`.
- Includes: historical references to replacing an unclaimed Elden Ring rune
  mark on a later death.
- Excludes: new game signatures; use `CON-352` with the relevant mark,
  protected-currency and old/new-stock parameters.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Merged into: `CON-352` by
  [`TAXONOMY_CHANGE_011`](../../research/taxonomy-changes/TAXONOMY_CHANGE_011.md).

## CON-362 — Attribute levelling requires its unlocked escalating rune price

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: one attribute increase is legal only after levelling unlock and
  when carried runes meet the displayed price for the next character level.
- Includes: Elden Ring Grace levelling after Melina's accord.
- Excludes: free respec; experience thresholds; weapon reinforcement.
- Parameters: unlock, level, attribute, price curve and carried runes.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## CON-363 — Ash assignment requires compatible armament and affinity unlock

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an Ash of War or affinity may be assigned only to a compatible
  retained armament and within the affinities enabled by owned whetblades.
- Includes: Elden Ring early Whetstone Knife configuration.
- Excludes: using the skill; spell memorisation; reinforcement upgrading.
- Parameters: ash, armament class, affinity, whetblade and existing skill.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## CON-364 — Live combat and destination state gate map travel

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: map access or fast travel is unavailable during live hostile
  engagement and travel requires a discovered eligible destination.
- Includes: Elden Ring map combat lock and discovered-Grace fast travel.
- Excludes: ordinary walking; scripted transfer; unrestricted teleportation.
- Parameters: combat state, map state, destination, discovery and dungeon lock.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## CON-365 — Finite flask charges are allocated between HP and FP recovery

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a bounded total charge stock is divided between Crimson and
  Cerulean flasks, and each use requires one remaining charge of that type.
- Includes: Elden Ring early sacred-flask allocation and use.
- Excludes: Wondrous Physick mixture; passive regeneration; unlimited potions.
- Parameters: total charges, HP charges, FP charges, remaining uses and refill.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## CON-366 — Crafting requires recipe inputs and reachable station context

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a recipe is currently craftable only when every required input
  quantity is available in an eligible carried, opened or nearby inventory and
  the player is within range of every required station or environmental source.
- Includes: Terraria 1.4.5.6 by-hand and station recipes, opened storage and the
  optional craft-from-nearby-chests context.
- Excludes: Minecraft spatial ingredient arrangement; recipe discovery itself;
  an autonomous machine's continuous production state.
- Parameters: recipe, input, quantity, inventory source, source priority,
  station set, environment and reach.
- Evidence: [Terraria decomposition](../games/s-z/terraria.md) and
  [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Novelty: not assessed.

## CON-367 — Town housing requires a safe furnished room and valid home tile

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a town NPC may occupy a room only when its frame and safe
  background walls bound an accepted area, required light, entrance, table and
  comfort categories exist, one standing home tile is legal, the room is
  vacant and nearby world evil remains below the invalidation threshold.
- Includes: Terraria ordinary town-NPC housing validity.
- Excludes: a bed-only player spawn room; enemy-proof construction as such;
  biome happiness and price optimisation after admission.
- Parameters: area, frame, wall holes, safe walls, furniture, home tile,
  occupancy, edge distance and evil score.
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## CON-368 — Town-NPC arrival requires its milestone and vacant valid housing

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a town NPC can arrive or respawn only after its declared world,
  inventory, currency, health or boss condition persists and at least one
  unoccupied valid house is available under the current time and visibility rules.
- Includes: Terraria Merchant, Nurse, Demolitionist and Dryad arrival gates.
- Excludes: the starting Guide; Traveling Merchant visits; hostile spawn tables.
- Parameters: NPC, milestone, world flag, player state, vacancy, daytime,
  offscreen state and arrival delay.
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## CON-369 — Eye encounter requires a legal night summon or natural-spawn state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the Eye of Cthulhu may enter only through one consumed Suspicious
  Looking Eye at night or its unmet-world natural-spawn predicates, cannot be
  duplicated while a boss is active and must be defeated before dawn escape.
- Includes: Terraria 1.4.5.6 manual and natural first-Eye conditions.
- Excludes: later boss summons; keeping the Eye active through daylight;
  Expert-only encounter behaviour.
- Parameters: time, summon item, prior defeat, health, defence, town count,
  active boss, surface presence, countdown and dawn.
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## CON-370 — Healing-item use requires missing health and no Potion Sickness

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an immediate healing item may be consumed only while health is
  below its maximum and the current Potion Sickness timer permits another use;
  successful use starts the item's declared lockout.
- Includes: Terraria mushrooms and Lesser Healing Potions before and during the
  first Eye of Cthulhu fight.
- Excludes: passive regeneration; mana-only items; a flask refilled at a checkpoint.
- Parameters: health, maximum, item, healing amount, sickness duration and timer.
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## CON-371 — Teammate return requires a survivor and an eligible recovery chain

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: a dead squadmate may return only while the squad still has a
  participating survivor and the current deathbox or Banner, crafting, Beacon,
  range, channel and lockout predicates of the chosen source are satisfied.
- Includes: Apex Legends Core teammate recovery from deathbox state or through
  Legend Banner and eligible Respawn Beacon state.
- Excludes: revival from knocked state; return after full squad elimination;
  the unresolved automatic pre-Ring-4 claim.
- Parameters: survivor count, teammate state, object, expiry, crafting, source,
  reach, channel, interruption and lockout.
- Evidence: [Apex Legends decomposition](../games/a-f/apex-legends.md).
- Novelty: not assessed.

## CON-372 — One weapon accepts only compatible attachments and one corrupted slot

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an attachment may enter a weapon only when its class and current
  slot are compatible, while a corrupted attachment additionally occupies the
  weapon's single corrupted-attachment allowance.
- Includes: Apex Legends Marked ammunition and attachment compatibility, locked
  hop-ups and one corrupted attachment per weapon.
- Excludes: backpack capacity; carrying two weapons as such; cosmetic weapon
  skins; account-level weapon unlocks.
- Parameters: weapon, ammunition class, attachment class, slot, compatibility,
  corrupted flag, occupied allowance and replacement.
- Evidence: [Apex Legends decomposition](../games/a-f/apex-legends.md).
- Novelty: not assessed.

## CON-373 — Combat proxy interaction requires a living eligible proxy state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a proxy-commanded attack or interception is legal only while the
  proxy is alive; interception applies only to the declared incoming damage
  class, and damage beyond remaining proxy health continues to the player.
- Includes: living Osty performing Osty Attacks and absorbing otherwise
  unblocked Attack damage, but not most non-Attacks or direct HP loss, in Slay
  the Spire 2.
- Excludes: player Block absorbing any compatible ordinary damage; a dead proxy
  acting before Summon; autonomous target selection by a persistent companion.
- Parameters: alive state, commanding effect, damage source and type, remaining
  proxy health, overflow, immunity and legal restoration.
- Evidence: [Slay the Spire 2 decomposition](../games/s-z/slay-the-spire-2.md).
- Novelty: not assessed.

## CON-374 — Unresolved Quest card is unplayable and ordinarily irremovable

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after acceptance and before its declared completion predicate, a
  Quest card remains a persistent deck member that cannot be played or removed
  through ordinary deck-editing services.
- Includes: Slay the Spire 2 Quest cards occupying draw supply until their
  later event or route predicate resolves.
- Excludes: playable Skills that describe an objective; ordinary removable
  Curses; a journal quest with no card object.
- Parameters: Quest identity, accepted state, playability, removal protection,
  transform protection, completion predicate and automatic removal.
- Evidence: [Slay the Spire 2 decomposition](../games/s-z/slay-the-spire-2.md).
- Novelty: not assessed.

## CON-375 — One persistent card object accepts at most one Enchantment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an eligible persistent deck-card object may hold no more than one
  Enchantment; an existing Enchantment cannot be stacked, removed or replaced
  except when another allowed transformation destroys the affected card object.
- Includes: Slay the Spire 2 run-persistent card Enchantments from Events,
  Ancients and Relics.
- Excludes: ordinary card upgrade level; temporary combat modifiers; several
  independent relics responding to the same played card.
- Parameters: card object, eligibility, Enchantment identity, slot occupancy,
  affected values, removal rule, transformation and copy inheritance.
- Evidence: [Slay the Spire 2 decomposition](../games/s-z/slay-the-spire-2.md).
- Novelty: not assessed.

## CON-376 — Variable-length lexicon membership gate

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a traced ordered-letter proposal is eligible for answer
  classification or assistance credit only when it meets the declared minimum
  length and belongs to the accepted lexicon.
- Includes: Strands accepting recognised words of at least four letters while
  rejecting shorter or unrecognised paths from theme and Hint accounting.
- Excludes: a fixed-length word query; arbitrary symbol paths with no lexical
  gate; whether an eligible word belongs to the authored theme answer set.
- Parameters: minimum length, language, lexicon, inflection policy, proper-name
  policy, duplicate handling and rejection feedback.
- Evidence: [Strands decomposition](../games/s-z/strands.md).
- Novelty: not assessed.

## CON-377 — Spanning answer connects opposite grid boundaries

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: one designated answer path in the hidden partition must touch two
  opposite sides of the finite letter grid while obeying the ordinary path
  topology.
- Includes: a Strands spangram connecting top to bottom or left to right and
  summarising the relationship among the other theme answers.
- Excludes: any word touching adjacent sides; a required route between fixed
  point endpoints; all answer paths having to span the grid.
- Parameters: designated answer, accepted opposite-side pairs, endpoint cells,
  path length and whether corners count for both incident sides.
- Evidence: [Strands decomposition](../games/s-z/strands.md).
- Novelty: not assessed.

## CON-378 — Exactly two independently controlled human actors are required

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the scoped ruleset can begin and continue only with two distinct
  human input owners, each controlling one persistent actor; neither an AI
  substitute nor one actor alone can satisfy the ordinary play contract.
- Includes: Split Fiction assigning Mio and Zoe to two local or online human
  players for its tailored two-player cooperative campaign.
- Excludes: optional multiplayer in a solo-capable campaign; one human
  switching between both actors; autonomous companions; two pieces moved by
  one shared input channel.
- Parameters: required human count, actor ownership, local or network mode,
  reassignment policy, disconnect handling and AI availability.
- Evidence: [Split Fiction decomposition](../games/s-z/split-fiction.md).
- Novelty: not assessed.

## CON-379 — Paired progress gate requires both eligible actor inputs

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an authored progression gate resolves only when each of two
  separately controlled actors supplies its declared eligible interaction,
  occupancy or timed prompt; one actor cannot serially impersonate the pair.
- Includes: Split Fiction's simultaneous lift console, separate floor panels,
  paired handles and doors that Mio and Zoe open together.
- Excludes: a single pressure plate that one actor holds for the other; two
  identical switches that the same actor may toggle in sequence; a dual exit
  checked only at room completion; aggregate damage from several players.
- Parameters: actor identities, interaction loci, simultaneous window, held or
  latched state, eligibility and reset when one input is released.
- Evidence: [Split Fiction decomposition](../games/s-z/split-fiction.md).
- Novelty: not assessed.

## CON-380 — Resident interaction requires a compatible live context

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a directed or autonomous resident interaction is offered and can
  complete only while actor, target, relationship, object, lot and current
  state satisfy that interaction's live eligibility rules.
- Includes: The Sims 4 introductions requiring another Sim, home invitations
  requiring an acquaintance, venue travel requiring a destination and social
  options changing with mood, relationship and target state.
- Excludes: a fixed menu command that always resolves; a spatial collision
  rule alone; hidden authored dialogue branching without simulated eligibility.
- Parameters: actor state, target type, relationship, mood, object affordance,
  lot, route, occupancy, cooldown and cancellation.
- Evidence: [The Sims 4 decomposition](../games/s-z/the-sims-4.md).
- Novelty: not assessed.

## CON-381 — Allied bodies remain valid weapon and deployment targets

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: ordinary combat and deployment resolution does not exempt allied
  controlled bodies from compatible damage, area effect or physical impact;
  positioning must therefore account for teammates as valid casualties.
- Includes: Helldivers 2 firearm, grenade and stratagem friendly fire plus a
  descending Hellpod's collision with another Helldiver.
- Excludes: a deliberate revive interaction; reduced self-damage as a distinct
  parameter; opponents being the only legal damage recipients.
- Parameters: source, allied relation, damage type, area geometry, collision,
  mitigation, self-damage and lethal threshold.
- Evidence: [Helldivers 2 decomposition](../games/g-l/helldivers-2.md).
- Additional support: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md),
  for Normal Campaign friendly-fire damage among Survivors.
- Novelty: not assessed.

## CON-382 — Teammate return requires a live signal and shared stock

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: ordinary return of a dead squad participant is legal only while
  another participant can complete the return signal and the squad-wide return
  resource or its declared depleted-state recharge is available.
- Includes: Helldivers 2 Reinforce requiring a living caller and one shared use,
  with limited timed replenishment after the initial pool is empty.
- Excludes: self-respawn independent of the squad; reviving a living injured
  body; a private life counter that another participant cannot spend.
- Parameters: living caller, dead target, signal validity, shared stock,
  depletion, recharge delay, squad wipe and objective-completion state.
- Evidence: [Helldivers 2 decomposition](../games/g-l/helldivers-2.md).
- Novelty: not assessed.

## CON-383 — Mission horizon removes support and forces final extraction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when the declared mission horizon expires, the remote support
  source withdraws, disabling the ordinary selected support calls and entering
  a bounded automatic departure sequence rather than allowing indefinite play.
- Includes: Helldivers 2's forty-minute scoped mission timer removing Super
  Destroyer stratagem and Reinforce support and automatically calling Pelican.
- Excludes: a soft score penalty; an encounter timer that only spawns enemies;
  manually leaving before the horizon.
- Parameters: horizon, support source, disabled calls, current deployments,
  auto-call, arrival time, landing wait and final departure countdown.
- Evidence: [Helldivers 2 decomposition](../games/g-l/helldivers-2.md).
- Novelty: not assessed.

## CON-384 — Only one eligible party companion is the active commanded battler

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: live battle permits exactly one living eligible party member in
  the commanded active slot; replacement must come from another eligible party
  slot, knockout forces replacement and no eligible member leaves the party
  unable to continue.
- Includes: the single active Pokémon and mid-battle party replacement rules in
  Pokémon Legends: Z-A.
- Excludes: multi-unit simultaneous control; storage capacity; an inactive
  companion merely following the Trainer.
- Parameters: active slot, party slots, eligibility, health, knockout, forced
  switch and terminal all-unable state.
- Evidence: [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Novelty: not assessed.

## CON-385 — Relative awareness gates the battle-opening advantage

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an opening advantage is legal only when the initiator remains
  outside the opponent Trainer's completed awareness, while prior detection can
  instead expose the player's companion to the opposing opening state.
- Includes: concealed or rear approaches granting a critical opening and being
  caught off guard after detection in Pokémon Legends: Z-A.
- Excludes: generic damage from behind with no awareness state; permanent
  invisibility; authored battles that ignore approach.
- Parameters: observer, initiator, sight, cover, facing, detection threshold,
  opening modifier and off-guard recipient.
- Evidence: [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Novelty: not assessed.

## CON-386 — Battle Zone competition requires the eligible night phase

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: current Z-A Royale Trainer competition and its Ticket Point awards are
  eligible only while the current night phase has instantiated the relevant
  Battle Zone.
- Includes: the first Rank Z nighttime Battle Zone in Pokémon Legends: Z-A.
- Excludes: Wild Zone capture; daylight preparation; a permanent arena with no
  world-phase prerequisite.
- Parameters: phase, Battle Zone, entry, Trainer eligibility, victory and point
  award.
- Evidence: [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Novelty: not assessed.

## CON-387 — Promotion requires the current ticket and designated-opponent victory

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the next rank can be recorded only when the current rank's
  Challenger's Ticket exists and the player defeats the opponent designated by
  that ticket.
- Includes: using the Rank Y ticket and defeating Zach in Pokémon Legends: Z-A.
- Excludes: ordinary point-awarding Trainer wins; holding enough points without
  receiving the ticket; later promotion opponents.
- Parameters: current rank, ticket identity, designated opponent, complete-party
  victory and next rank.
- Evidence: [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Novelty: not assessed.

## CON-388 — Standard Trial fixes four Survivor roles against one Killer

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the standard match requires exactly four Survivor participant
  slots and one opposing Killer slot, and each role retains different objective,
  attack, rescue, tracking and escape authority for that Trial.
- Includes: Dead by Daylight standard 1v4 public Trials.
- Excludes: 2v8; a symmetric team contest; hidden allegiance that changes
  during play; Killer-specific Power details.
- Parameters: Survivor count, Killer count, team relation, role authority,
  replacement policy and disconnect handling.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Novelty: not assessed.

## CON-389 — Five completed Generators gate ordinary Exit Gate use

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: neither standard Exit Gate switch is ordinarily actionable until
  Survivors complete five of the seven Trial Generators; completing fewer
  leaves both gates unpowered despite partial progress elsewhere.
- Includes: the standard Dead by Daylight 1v4 Generator quota and paired gates.
- Excludes: the last-Survivor Hatch-closure exception that powers gates; one
  Generator opening a nearby map-specific door; post-match score goals.
- Parameters: available Generators, completion quota, powered switches, gates
  and exception trigger.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Novelty: not assessed.

## CON-390 — Survivor work requires compatible reach, body state and channel

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: repair, healing, recovery, unhooking and gate work may progress
  only while the Survivor, target, distance and interaction state are compatible;
  leaving, being hit, grabbed or otherwise interrupted stops the channel.
- Includes: Dead by Daylight Survivor objective and teammate interactions.
- Excludes: one instantaneous Pallet drop; passive regeneration; the Killer's
  own damage or pickup permissions.
- Parameters: actor state, target class and state, reach, duration, movement,
  interruption, co-worker capacity and saved-progress rule.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Additional support: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md),
  for interruptible first-aid and incapacitated-teammate revival channels.
- Novelty: not assessed.

## CON-391 — Health and Hook state bound Survivor control

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the Survivor's current Healthy, Injured, Dying, carried or Hooked
  state determines available locomotion, work, healing, rescue and escape
  interactions; unavailable states cannot be bypassed by ordinary input.
- Includes: full movement/work while Healthy or Injured, Dying crawl/recovery,
  disabled carried control and Hooked rescue dependence in Dead by Daylight.
- Excludes: Perk or Item exceptions; Hook-stage timing itself; a generic low-
  health speed penalty with no discrete interaction authority.
- Parameters: body state, movement set, interaction catalogue, targetability,
  pickup, rescue and escape permission.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Novelty: not assessed.

## CON-392 — Trial role and obstacle state gate chase traversal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: window and Pallet use depends on participant role, approach and
  current obstacle state: ordinary Survivors may drop and vault Pallets, while
  ordinary Killers cannot vault a dropped Pallet and must destroy it to pass.
- Includes: blank-loadout Dead by Daylight window and Pallet chase rules.
- Excludes: character-specific Killer Power exceptions; arbitrary walls and
  ordinary collision; a one-role platforming jump.
- Parameters: role, obstacle, upright or dropped state, approach speed, side,
  vault class, collision and break authority.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Novelty: not assessed.

## CON-393 — Escape or terminal removal ends one Survivor's Trial

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: crossing an eligible gate or Hatch ends direct control as an
  escape, while sacrifice, killing, cumulative bleed-out or Collapse expiry
  permanently removes that Survivor; no ordinary respawn returns the same
  participant before the Trial ends.
- Includes: Dead by Daylight's independent Survivor terminal results and the
  Endgame Collapse deadline.
- Excludes: post-match spectating; later matchmaking; temporary Dying or Hooked
  state rescued before terminal resolution.
- Parameters: exit boundary, escape, sacrifice, kill, bleed-out, Collapse
  timer, remaining participant and spectating state.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Novelty: not assessed.

## CON-394 — Carried items require compatible rectangular placement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an item can enter carried state only if its rectangular footprint
  fits unoccupied inventory cells, merges into a compatible stack, or enters a
  matching equipment slot.
- Includes: Path of Exile 2 inventory and equipment placement.
- Excludes: weight-only carrying capacity; unlimited lists; stash organisation
  outside the scoped route.
- Parameters: grid dimensions, footprint, occupied cells, stack identity and
  cap, rotation permission and equipment slot.
- Evidence: [Path of Exile 2 decomposition](../games/m-r/path-of-exile-2.md).
- Novelty: not assessed.

## CON-395 — Equipment and skills require compatible character state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an equipment item or active Skill may contribute its declared
  effects only while the character meets its level and attribute requirements
  and has any required compatible weapon state.
- Includes: Path of Exile 2 equipment, Skill and weapon restrictions.
- Excludes: temporary Mana/readiness checks during use; inventory space;
  cosmetic equipment.
- Parameters: level, Strength, Dexterity, Intelligence, weapon class, hand
  state, requirement source and disabled effect.
- Evidence: [Path of Exile 2 decomposition](../games/m-r/path-of-exile-2.md).
- Novelty: not assessed.

## CON-396 — A Support requires a compatible free Skill socket

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a Support Gem may modify an active Skill only when that Skill has
  a free Support socket, their tags and category are compatible and the build
  satisfies the Support's current attribute budget.
- Includes: Path of Exile 2 Support socketing under the current tier/category
  model.
- Excludes: engraving an Uncut Support; passive-tree allocation; free global
  modifiers that affect every Skill.
- Parameters: Skill tags, socket count, Support tags/category, duplicate rule,
  attribute budget and compatibility feedback.
- Evidence: [Path of Exile 2 decomposition](../games/m-r/path-of-exile-2.md).
- Novelty: not assessed.

## CON-397 — Crafting currency requires an eligible item state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each crafting currency can target only items whose base, rarity,
  affix, socket and corruption state satisfies that currency's preconditions,
  and the result cannot exceed the item's legal bounds.
- Includes: ordinary Path of Exile 2 currency crafting eligibility.
- Excludes: item-drop sampling; trade price; a recipe whose ingredients are
  merely exchanged by a vendor.
- Parameters: currency, item class and level, rarity, affix counts, sockets,
  corruption, eligibility and result bounds.
- Evidence: [Path of Exile 2 decomposition](../games/m-r/path-of-exile-2.md).
- Novelty: not assessed.

## CON-398 — One direct-control locus governs an eleven-player side

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each side fields eleven role-bearing players, but one local human
  has at most one direct-control locus and may transfer it only to an eligible
  teammate while the remaining players stay under team AI.
- Includes: one human-controlled home side against a CPU away side in EA SPORTS
  FC 26 Kick Off.
- Excludes: eleven simultaneous local control loci; Clubs avatars; roster and
  transfer-market construction.
- Parameters: roster, formation, active player, switching eligibility, keeper
  state and control side.
- Evidence: [EA SPORTS FC 26 decomposition](../games/a-f/ea-sports-fc-26.md).
- Novelty: first isolated for `GAME-0163`.

## CON-399 — Football play is bounded by field, goal and restart geometry

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: ordinary live play occurs within the marked field; a whole-ball
  crossing of a touchline or goal line stops that phase and determines the
  legal throw-in, goal-kick, corner or goal outcome from crossing location and
  last touch.
- Includes: scoped EA SPORTS FC 26 and Football Manager 26 stadium fields.
- Excludes: a ball merely touching a line; an invisible arena wall that keeps
  every ball live; Rush-specific field geometry.
- Parameters: field dimensions, line, crossing point, last touch, goal frame
  and restart placement.
- Evidence: [EA SPORTS FC 26 decomposition](../games/a-f/ea-sports-fc-26.md)
  and [Football Manager 26 decomposition](../games/a-f/football-manager-26.md).
- Novelty: first isolated for `GAME-0163`.

## CON-400 — Offside restricts eligible attacking involvement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an attacker in an offside position when a teammate plays the ball
  may not become actively involved before the phase is reset by the rules.
- Includes: interfering with play or an opponent in the scoped match.
- Excludes: being level with the second-last opponent; direct receipt from a
  goal kick, throw-in or corner; tactical formation preference.
- Parameters: ball position, second-last opponent, body parts, pass instant,
  active involvement and restart exception.
- Evidence: [EA SPORTS FC 26 decomposition](../games/a-f/ea-sports-fc-26.md)
  and [Football Manager 26 decomposition](../games/a-f/football-manager-26.md).
- Novelty: first isolated for `GAME-0163`.

## CON-401 — Player contact is bounded by football offence rules

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a possession challenge is legal only while its contact and
  manner remain within football law; an offence can surrender a free kick or
  penalty and can add a caution or dismissal.
- Includes: mistimed standing and sliding tackles, handball configuration and
  professional fouls in EA SPORTS FC 26.
- Excludes: health-based combat damage; tactical pressure without illegal
  contact; post-match suspensions outside the scope.
- Parameters: contact, force, ball timing, location, advantage, sanction and
  handball setting.
- Evidence: [EA SPORTS FC 26 decomposition](../games/a-f/ea-sports-fc-26.md)
  and [Football Manager 26 decomposition](../games/a-f/football-manager-26.md).
- Novelty: first isolated for `GAME-0163`.

## CON-402 — Combat-room exits require finite hostile clearance

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after Isaac enters an uncleared ordinary combat room, its normal
  exits remain closed until every required current hostile and declared
  reinforcement is defeated.
- Includes: ordinary combat-room door locks in base The Binding of Isaac: Rebirth.
- Excludes: permanently locked key doors; leaving an already cleared room;
  survival against an endless spawn stream.
- Parameters: room, required set, reinforcement closure, door set, clear state
  and escape exceptions.
- Evidence: [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md).
- Novelty: first isolated for `GAME-0164`.

## CON-428 — Only one current supplied contract may be active

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: accepting a currently offered employer job commits its supplied
  truck and cargo to the single active-job slot; another offer cannot coexist in
  that slot before settlement or abandonment.
- Includes: one Euro Truck Simulator 2 Quick Job.
- Excludes: comparing several unaccepted offers; queued autonomous-driver jobs;
  carrying several unrelated quests without a shared vehicle.
- Parameters: offer eligibility, active-job slot, supplied vehicle, acceptance,
  settlement and abandonment.
- Evidence: [Euro Truck Simulator 2 decomposition](../games/a-f/euro-truck-simulator-2.md).
- Novelty: first isolated for `GAME-0169`; earlier job constraints do not bind
  direct vehicle supply and one active commercial load.

## CON-429 — Road rules constrain legal vehicle movement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the current road's direction, signal state, local regulation and
  posted limit determine which physically possible vehicle movement is legal
  and therefore free of an eligible traffic-offence penalty.
- Includes: Euro Truck Simulator 2 lane direction, traffic lights and speed limits.
- Excludes: collision geometry that makes movement physically impossible;
  informal civilian reactions; a race track boundary with no legal tariff.
- Parameters: jurisdiction, lane direction, signal, stop line, road class,
  posted limit, tolerance, vehicle state and detected offence.
- Evidence: [Euro Truck Simulator 2 decomposition](../games/a-f/euro-truck-simulator-2.md).
- Novelty: first isolated for `GAME-0169`; it distinguishes legal compliance
  from physical traversability inside direct driving.

## CON-430 — Ten driving hours require nine consecutive rest hours

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: with the mandatory-break rule enabled, no more than ten driving
  hours are legal before the driver must complete at least nine consecutive
  rest hours to reset that allowance.
- Includes: Euro Truck Simulator 2 update 1.60 Mandatory Break.
- Excludes: the separately depleting Rest State; an optional short pause; the
  American Truck Simulator fourteen/ten-hour rule.
- Parameters: enabled state, driving limit, remaining allowance, consecutive
  rest minimum, warning, violation and reset.
- Evidence: [Euro Truck Simulator 2 decomposition](../games/a-f/euro-truck-simulator-2.md).
- Novelty: first isolated for `GAME-0169`; prior fatigue rules do not impose
  this separate recoverable legal-hours ratio on a live job.

## CON-431 — Deadline and retained cargo condition bound delivery evaluation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: one delivery is evaluated against its declared completion window
  and the retained truck, trailer and cargo condition rather than merely by
  reaching the destination coordinate.
- Includes: Euro Truck Simulator 2 Quick Job time and damage evaluation.
- Excludes: a traffic fine already debited during travel; owned-truck repair
  after the job; cargo identity with no condition state.
- Parameters: deadline, completion time, overtime, truck damage, trailer damage,
  cargo damage, tolerance and evaluation band.
- Evidence: [Euro Truck Simulator 2 decomposition](../games/a-f/euro-truck-simulator-2.md).
- Novelty: first isolated for `GAME-0169`; earlier delivery constraints do not
  jointly retain articulated load condition and a job deadline.

## CON-432 — Manual trailer delivery requires a valid bay pose

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when a non-skipped parking treatment is chosen, delivery may
  validate only while the declared trailer occupies the assigned bay within its
  tolerated pose and is eligible for detachment.
- Includes: standard and easier Euro Truck Simulator 2 depot drop-off bays.
- Excludes: the automatic-parking/skip treatment; stopping the tractor without
  its trailer; arbitrary free-roam parking.
- Parameters: bay geometry, trailer footprint, position tolerance, orientation
  tolerance, coupling state, detachment and validation feedback.
- Evidence: [Euro Truck Simulator 2 decomposition](../games/a-f/euro-truck-simulator-2.md).
- Novelty: first isolated for `GAME-0169`; prior spatial receivers do not test a
  directly reversed articulated trailer as a contract-closing condition.

## CON-433 — An anomaly route requires a safe phase or accepted exposure

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: crossing an anomalous field safely requires a route outside active
  trigger volumes or movement through the bounded discharged interval produced
  by a probe.
- Includes: bolt-tested hazards in the S.T.A.L.K.E.R. 2 opening.
- Excludes: an impassable wall; a hazard permanently removed after one trigger;
  ordinary hostile line of fire.
- Parameters: field, route, trigger volume, active phase, discharge interval,
  recovery and tolerated exposure.
- Evidence: [S.T.A.L.K.E.R. 2 decomposition](../games/s-z/stalker-2-heart-of-chornobyl.md).
- Novelty: first isolated for `GAME-0170`; legality depends on a temporary
  environmental phase created by an expendable-free probe.

## CON-434 — Artifact acquisition requires detector range and physical reach

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an anomalous-field artifact cannot be taken until a compatible
  active detector brings the player inside manifestation range and the revealed
  object is physically reachable.
- Includes: Echo Detector acquisition of the Mold artifact.
- Excludes: ordinary visible loot; known map coordinates without an active
  detector; equipping an artifact already in inventory.
- Parameters: detector compatibility, active state, signal range, critical
  range, artifact position, manifestation and pickup reach.
- Evidence: [S.T.A.L.K.E.R. 2 decomposition](../games/s-z/stalker-2-heart-of-chornobyl.md).
- Novelty: first isolated for `GAME-0170`; localisation is a mechanical
  prerequisite for object existence in the player's visible pickup state.

## CON-435 — Survival thresholds restrict movement and continued action

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: bleeding, radiation, hunger, depleted stamina or excessive carried
  weight progressively restrict recovery and locomotion, and lethal body state
  ends the current attempt unless a prior save is restored.
- Includes: Lesser Zone survival and inventory-overload thresholds.
- Excludes: a fixed mission timer; weapon ammunition; reputation-gated dialogue.
- Parameters: status, threshold, movement penalty, stamina regeneration, health
  loss, treatment requirement and lethal boundary.
- Evidence: [S.T.A.L.K.E.R. 2 decomposition](../games/s-z/stalker-2-heart-of-chornobyl.md).
- Novelty: first isolated for `GAME-0170`; it makes radiation and inventory load
  co-govern the same live traversal capacity.

## CON-436 — Artifact loadout requires armour slots and radiation tolerance

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an artifact effect is active only while the item occupies an
  available compatible armour container, and its radiation must be tolerated or
  offset by the current protection and other effects.
- Includes: choosing whether to equip a scoped artifact after collection.
- Excludes: carrying an artifact only for sale; ordinary weapon slots; detector
  compatibility during acquisition.
- Parameters: armour, container count, artifact, slot, effect, radiation,
  protection, stacking and removal.
- Evidence: [S.T.A.L.K.E.R. 2 decomposition](../games/s-z/stalker-2-heart-of-chornobyl.md).
- Novelty: first isolated for `GAME-0170`; one item simultaneously consumes a
  wearable slot and creates a persistent risk-benefit budget.

## CON-425 — Mod installation obeys compatibility, capacity and polarity drain

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a Mod may remain installed only on a compatible equipment item,
  in an eligible slot, and while the polarity-adjusted sum of all installed
  drain does not exceed that item's current capacity.
- Includes: starter Warframe and weapon upgrades during Vor's Prize.
- Excludes: acquiring Mods; cosmetic slots; applying an effect without capacity
  cost; account-wide inventory limits.
- Parameters: item class, Mod compatibility, slot, polarities, base drain,
  adjusted drain, total capacity and rejection feedback.
- Evidence: [Warframe decomposition](../games/s-z/warframe.md).
- Novelty: first isolated for `GAME-0168`; earlier slot limits do not combine
  type compatibility with a polarity-adjusted shared budget.

## CON-426 — Mission objective completion gates extraction settlement

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the extraction endpoint may settle the mission only after the
  current mandatory objective has reached its declared completed state and the
  player reaches the active extraction region.
- Includes: mandatory Vor's Prize mission objectives followed by extraction.
- Excludes: leaving through an arbitrary door; optional pickups; returning to
  the Orbiter by aborting without ordinary reward settlement.
- Parameters: mission type, objective state, extraction activation, player
  presence, settlement eligibility and failure state.
- Evidence: [Warframe decomposition](../games/s-z/warframe.md).
- Novelty: first isolated for `GAME-0168`; earlier exits are not uniformly
  coupled to a procedurally assembled mission objective and persistent rewards.

## CON-427 — Self-revival consumes bounded per-mission stock

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after health reaches zero and the downed state is not rescued,
  self-revival may resume play only while a finite mission revive remains;
  using it subtracts one, and the stock restores after returning to the ship.
- Includes: the four ordinary self-revives described by Warframe's official
  quick-start guide.
- Excludes: shield regeneration before health depletion; teammate revival;
  unlimited checkpoint respawns.
- Parameters: health, downed timer, teammate state, revive stock, consumption,
  restored stock and mission boundary.
- Evidence: [Warframe decomposition](../games/s-z/warframe.md).
- Novelty: first isolated for `GAME-0168`; prior life constraints do not reset a
  bounded self-revive stock specifically at the persistent hub boundary.

## CON-405 — Horse authority requires a reachable owned saddle state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: calling, mounting, cargo access and primary-horse replacement are
  legal only for a compatible living horse whose ownership, saddle, proximity,
  bond and current mission state permit that interaction.
- Includes: Arthur's primary and temporary horse rules during scoped Chapter 2.
- Excludes: entering an unowned wagon seat; summoning a spectral mount without
  persistent saddle ownership; remote stable management.
- Parameters: horse identity, ownership, saddle, primary or temporary role,
  distance, bond, health, fear, mission permission and cargo access.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`.

## CON-406 — Field weapon access is split between body and saddle capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: sidearms remain on the protagonist while long guns and selected
  alternate equipment are available only within the current bounded loadout or
  while the saddled horse is close enough for transfer.
- Includes: Chapter 2 weapon-wheel and horse-weapon access in Red Dead
  Redemption 2 Story Mode.
- Excludes: one unlimited weapon catalogue accessible everywhere; magazine
  capacity; cosmetic holster selection.
- Parameters: slot class, body loadout, saddle storage, horse proximity,
  mission lock, equipped weapon and transfer.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`.

## CON-407 — Firearm cleaning requires owned condition and available oil

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: personal field cleaning is legal only for an owned inspectable
  firearm below full condition while at least one unit of gun oil is carried
  and the current interaction state allows maintenance.
- Includes: cleaning an eligible Chapter 2 firearm away from a gunsmith.
- Excludes: buying a gunsmith service; reloading ammunition; passive condition
  recovery; maintaining a weapon not currently owned.
- Parameters: ownership, weapon class, condition, oil count, posture, hostile
  interruption and resulting condition.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`.

## CON-408 — Core and outer-meter state bound sustained performance

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: sustained exertion, Dead Eye duration, damage tolerance and
  recovery remain useful only while their outer meter and supporting core
  permit the requested intensity; depletion applies the declared limit.
- Includes: Arthur and horse health, stamina and Dead Eye resource gates in
  scoped Chapter 2.
- Excludes: a fixed cooldown; ammunition capacity; a health bar with no
  separately maintained core.
- Parameters: resource, core, outer meter, requested action, drain, recovery,
  depleted penalty and consumable modifier.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`.

## CON-409 — Camp ledger spending requires unlocks and shared funds

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a camp restock or upgrade can be purchased only after the ledger
  is unlocked, its authored predecessor conditions are met and the shared camp
  balance covers the displayed price.
- Includes: Horseshoe Overlook supply, lodging, leather-tool and service
  purchases available during Chapter 2.
- Excludes: donating value into the camp; Arthur's personal shop balance;
  cosmetic Red Dead Online camp upgrades.
- Parameters: ledger unlock, predecessor, offer, shared balance, price, stock
  state, purchased state and edition discount.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`.

## CON-410 — Unit commands obey movement, terrain and control budgets

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a unit may enter only passable reachable hexes while its current
  turn movement and action authority cover terrain, river, embarkation and zone
  of control costs.
- Includes: Roman civilian and combat-unit movement in Civilization VI.
- Excludes: trader route assignment; city production; unrestricted teleportation.
- Parameters: unit, movement, action, origin, destination, terrain, river,
  passability, zone of control and remaining budget.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`; it joins hex costs and zone of
  control to a refreshable 4X unit-turn budget.

## CON-411 — Hex stacking permits at most one unit of each broad class

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an occupied hex may not end with two combat units or two civilian
  units belonging to the same side, while one compatible member of each class
  may share it under declared rules.
- Includes: a Warrior and Builder sharing one Roman hex.
- Excludes: district/building occupancy; embarked transport visuals; air-unit capacity.
- Parameters: hex, owner, combat occupant, civilian occupant, support class and transfer.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## CON-412 — City founding requires legal terrain and minimum spacing

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a Settler may found only on an eligible current hex that is not
  occupied or forbidden and lies at least the declared minimum distance from
  every existing City Center.
- Includes: the base-game three-hex city-distance rule in Civilization VI.
- Excludes: capturing a city; placing a district; razing an existing city.
- Parameters: Settler, hex, terrain, occupancy, existing cities, minimum distance and exception.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## CON-413 — Citizens work only eligible tiles or slots assigned to their city

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: each population member can contribute through at most one legal
  owned tile within the city's work radius or one available specialist slot,
  and a tile cannot be worked simultaneously by two cities.
- Includes: reassigning overlapping Roman territory in Civilization VI.
- Excludes: border ownership itself; unit stacking; automated rival decisions.
- Parameters: citizen, city, radius, tile ownership, overlap, slot capacity and assignment.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## CON-414 — District capacity and terrain gate placement

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a city may begin a district only when population permits another
  district and a distinct owned hex satisfies that district's terrain,
  occupancy and feature rules.
- Includes: Campus and Industrial Zone placement and flat-land Spaceports.
- Excludes: buildings inside a completed district; City Center founding;
  neighbourhood Loyalty from expansions.
- Parameters: city population, built districts, district class, hex, terrain,
  feature, ownership, occupancy and exceptions.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## CON-415 — Builder improvements spend finite charges on eligible hexes

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a Builder may create or remove only an unlocked improvement or
  feature valid for its current hex, and a successful build spends one of the
  unit's finite remaining charges.
- Includes: a three-charge base Builder making farms or mines.
- Excludes: city production of a district; military pillaging; reusable worker labour.
- Parameters: Builder, charge count, hex, terrain, feature, resource,
  technology, improvement and remaining charges.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## CON-416 — Technology and Civic choices obey prerequisite graphs

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a Technology or Civic can receive current empire progress only
  after all of its declared mandatory predecessors are complete or the rules
  expose it as otherwise selectable.
- Includes: Rocketry before Satellites and required Space Race civics.
- Excludes: the boost trigger itself; unit promotion prerequisites; random discovery.
- Parameters: tree, target, predecessors, completion, selectable state and stored progress.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## CON-417 — Production and purchases require unlocks, capacity and resources

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a city may produce or buy a target only if its required
  Technology/Civic, district/building, strategic resource, population or
  instance capacity and relevant cost are satisfied.
- Includes: producing resource-gated units and Spaceport projects.
- Excludes: selecting the next Technology; working a tile; free founding effects.
- Parameters: city, target, unlock, district, building, resource, capacity,
  currency, production cost and purchase price.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## CON-418 — Policy cards must fit compatible government slots

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: each active policy card occupies one currently empty slot of its
  matching type or a wildcard slot supplied by the adopted government.
- Includes: military, economic and diplomatic cards in base Civilization VI.
- Excludes: choosing a Civic; equipping a unit; policies not yet unlocked.
- Parameters: government, slot type, card type, wildcard, occupancy and unlock.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## CON-419 — Trade routes require capacity, trader and reachable destination

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a route can begin only while empire route capacity is free, an
  available trader occupies the origin and the destination is within a legal
  path extended by applicable trading posts.
- Includes: domestic and contacted-rival routes in Civilization VI.
- Excludes: diplomatic resource deals; city-state routes disabled by scope;
  manually moving a Builder.
- Parameters: capacity, trader, origin, destination, path range, trading posts and blockage.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## CON-420 — Diplomatic actions obey contact and treaty timing gates

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a civilization-level deal, formal relationship, declaration or
  peace agreement is legal only when contact, current war/peace state, required
  elapsed turns and other declared diplomatic prerequisites permit it.
- Includes: declarations of friendship, war and negotiated peace in base Civilization VI.
- Excludes: tactical attacks after war begins; city-state envoys; chat messages.
- Parameters: parties, contact, relationship, war state, treaty, elapsed turns,
  prerequisite and legal actions.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## CON-421 — Science projects obey Spaceport, technology and launch order

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: each base-game Science Victory project may be produced only in a
  city with a Spaceport after its Technology and all earlier declared launch
  milestones are complete; Mars victory requires all three distinct modules.
- Includes: Satellite, Moon Landing, Mars Reactor, Hydroponics and Habitation.
- Excludes: Gathering Storm's Exoplanet Expedition; arbitrary project order;
  victory merely for researching the technologies.
- Parameters: city, Spaceport, technology, predecessor project, module identity,
  completion and rival terminal state.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## CON-422 — Vertical input eligibility follows avatar mode and support

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the shared vertical control may start a cube jump only when its
  support/buffer rule permits, while ship input remains eligible in flight; no
  mode grants direct horizontal stopping or reversal.
- Includes: supported cube jumps and airborne ship modulation in Stereo Madness.
- Excludes: freely jumping again in mid-air; two-axis flight steering; direct
  selection of a mode portal; horizontal speed as a player choice.
- Parameters: current mode, support contact, buffered hold, airborne state,
  horizontal authority and rejected-input feedback.
- Evidence: [Geometry Dash decomposition](../games/g-l/geometry-dash.md).
- Novelty: first isolated for `GAME-0167`; earlier action gates do not reuse one
  control across support-gated jumping and continuous ship flight.

## CON-423 — Classic Normal Mode has no in-level checkpoint

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a classic Normal Mode completion is valid only as one continuous
  attempt from the authored 0% origin to the finish; no intermediate position
  may become a respawn source inside that attempt.
- Includes: every Stereo Madness Normal Mode retry beginning as the opening cube.
- Excludes: Practice Mode's automatic or manual checkpoints; platformer-mode
  checkpoints; pausing and resuming the same still-live attempt.
- Parameters: mode, origin, finish, checkpoint count, pause policy and retry.
- Evidence: [Geometry Dash decomposition](../games/g-l/geometry-dash.md).
- Novelty: first isolated for `GAME-0167`; existing checkpoint genes restore
  authored or player-made intermediate state rather than forbid it.

## CON-424 — Safe contact depends on current mode and surface normal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the icon may continue only through contacts allowed by its
  current collision regime: the cube can land on authored support but fails on
  spikes or unsafe block faces, while the ship must clear both floor and ceiling
  obstacles with its complete collision envelope.
- Includes: Stereo Madness cube landings, triple-spike jumps and ship corridors.
- Excludes: decorative background shapes; Ignore Damage/editor testing;
  recoverable health loss; collision-free portal crossing.
- Parameters: avatar mode, collision envelope, surface class, contact normal,
  support tolerance, lethal classes and simultaneous contacts.
- Evidence: [Geometry Dash decomposition](../games/g-l/geometry-dash.md).
- Novelty: first isolated for `GAME-0167`; generic visible-hazard failure does
  not distinguish safe cube support from lethal ship or side contact.

## CON-403 — Typed finite pickups gate room interactions

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a typed key, bomb, gem, coin or comparable finite pickup
  interaction is legal only when the current
  run owns enough of that exact pickup type, and successful use subtracts the
  declared amount for locked access, a placed blast or a priced offer.
- Includes: Rebirth locked doors and chests, bomb placement and Shop purchases;
  Blue Prince locks, gem-priced room plans and coin-priced shop offers.
- Excludes: one interchangeable universal currency; health payment; an active
  item charge that replenishes through room clears.
- Parameters: pickup type, current count, interaction class, cost, eligibility
  and remaining count.
- Evidence: [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md)
  and [Blue Prince decomposition](../games/a-f/blue-prince.md).
- Novelty: first isolated for `GAME-0164`; it couples several non-substitutable
  run resources to distinct room-level decisions.

## CON-404 — Special carried items occupy bounded typed slots

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the current character can normally carry at most one active item,
  one trinket and one pocket card, rune or pill; accepting another member of a
  full typed slot requires leaving or replacing the prior occupant.
- Includes: clean-save Isaac's base-Rebirth special-item slots.
- Excludes: unlimited passive collectibles; coin, bomb and key counters; DLC
  items that add or transform slot capacity.
- Parameters: slot type, capacity, occupant, replacement, drop eligibility and
  character modifiers.
- Evidence: [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md).
- Novelty: first isolated for `GAME-0164`.

## CON-437 — Driving-event entry requires an eligible vehicle and class

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a configured driving event may begin only with a vehicle admitted
  by its current theme, type and performance-class restriction.
- Includes: Forza Horizon 6 opening Festival events limited to C-class cars
  until the first Wristband; Need for Speed Unbound `Shopping Spree` accepting
  the fixed A+ Story starter packet; Need for Speed Payback `The Highway Heist`
  accepting an eligible Race car at the displayed `LV180` boundary.
- Excludes: unrestricted free driving; post-completion Race Customizer rules;
  an event whose fixed vehicle is supplied automatically.
- Parameters: event, car theme, vehicle type, performance class, PI range,
  ownership and override state.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md) and
  [Need for Speed Payback decomposition](../games/m-r/need-for-speed-payback.md).
- Novelty: first isolated for `GAME-0171`; earlier vehicle constraints gate
  seats, fuel, cargo or roads rather than race entry by car theme and class.

## CON-438 — Race progress requires ordered checkpoint and lap completion

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a driving-event finish is valid only after the controlled vehicle
  crosses every required checkpoint in sequence and completes the declared lap
  count before the finish line is accepted.
- Includes: Forza Horizon 6 Trail, Circuit, Cross Country, Time Attack and
  Invitational routes; Need for Speed Unbound `Shopping Spree`; Trackmania
  `Summer 2026 - 01` ordered checkpoints and valid Finish trigger; Need for
  Speed Underground's two authored Olympic Square laps before its opening
  Circuit finish settles.
- Excludes: open-world navigation; a single speed-zone measurement; decorative
  gates with no progress authority.
- Parameters: checkpoint order, gate width, direction, lap count, reset policy
  and finish eligibility.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md),
  [Trackmania decomposition](../games/s-z/trackmania.md), and
  [Need for Speed Underground decomposition](../games/m-r/need-for-speed-underground.md).
- Novelty: first isolated for `GAME-0171`; earlier route constraints govern
  networks or escort anchors rather than one directly driven race traversal.

## CON-439 — Driving-event entry requires its current campaign unlock

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an authored driving event can be entered only after the campaign
  has exposed its marker and any required prior introduction, progress band or
  invitation has been retained.
- Includes: Horizon Qualifiers after the Tokyo introduction and the Horizon
  Invitational only after enough Festival Points are earned; Need for Speed
  Payback's Chapter 2 finale after both required predecessor questlines.
- Excludes: choosing among already unlocked events; later Race Customizer
  settings; a hidden future Playlist event.
- Parameters: event, marker, prior gate, progress band, invitation, completion
  and replay state.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md) and
  [Need for Speed Payback decomposition](../games/m-r/need-for-speed-payback.md).
- Novelty: first isolated for `GAME-0171`; generic mission gates do not bind a
  map-visible driving-event catalogue to festival campaign state.

## CON-440 — Horizon Invitational requires the Qualifier progress threshold

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the first Wristband Event remains unavailable until completed
  Qualifier events have accumulated the declared Horizon Festival Point total.
- Includes: the scoped four-event path into the first Horizon Invitational.
- Excludes: later Wristband thresholds; Discover Japan Stamp progression;
  replacing the threshold with one mandatory race win.
- Parameters: eligible events, point values, current total, threshold and
  invitation transition.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md).
- Novelty: first isolated for `GAME-0171`; the gate aggregates alternatives
  before opening one mandatory terminal driving event.

## CON-441 — First Wristband requires Horizon Invitational completion

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: crossing the Qualifier threshold grants access but does not grant
  Festival membership; the scoped player must complete the Horizon
  Invitational before the first Wristband and its unlocks are retained.
- Includes: the fresh-save Forza Horizon 6 first-Wristband boundary.
- Excludes: later Showcase or Horizon Rush Wristband Events; earning a Stamp;
  merely entering or abandoning the Invitational.
- Parameters: invitation, event start, valid completion, Wristband, reward cars
  and Festival feature unlocks.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md).
- Novelty: first isolated for `GAME-0171`; accumulated qualification progress
  and terminal event completion remain two distinct gates.

## CON-442 — Fighting commands require an actionable compatible state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a requested movement, guard, throw or attack can begin only when
  the assigned fighter, control mapping, current pose, recovery and declared
  command prerequisites permit it.
- Includes: Classic-control Ryu commands in the scoped Street Fighter 6 duel.
- Excludes: resource costs handled by Drive or Super constraints; the resulting
  contact; a persistent character-build prerequisite.
- Parameters: fighter, control type, facing, ground/air state, recovery, input
  buffer, command sequence, cancel window and target relation.
- Evidence: [Street Fighter 6 decomposition](../games/s-z/street-fighter-6.md).
- Additional support: [Brawlhalla decomposition](../games/a-f/brawlhalla.md),
  for ground/air, weapon, recovery and dodge state gating one platform-fighter
  command vocabulary.
- Novelty: first isolated for `GAME-0172`; it binds a character-owned fighting
  command vocabulary to transient live pose and recovery state.

## CON-443 — Shared stage bounds and bodies constrain duel spacing

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: both fighters occupy one bounded side-view arena; horizontal
  stage edges, body push contact, airborne crossing and resulting facing limit
  and transform their relative spacing.
- Includes: the fixed Genbu Temple fight plane in Street Fighter 6 Versus.
- Excludes: free three-dimensional arena traversal; ring-out victory; static
  grid occupancy; a projectile's own collision rule.
- Parameters: stage width, body bounds, push interaction, jump arc, corner,
  crossover and facing update.
- Evidence: [Street Fighter 6 decomposition](../games/s-z/street-fighter-6.md).
- Novelty: first isolated for `GAME-0172`; earlier arenas permit broad spatial
  navigation or objective zones rather than a two-body fighting plane whose
  edges create corner pressure without ring-out.

## CON-444 — Drive techniques require stock and non-Burnout state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a Drive technique is legal only when the fighter is outside
  Burnout, its current Drive stock can satisfy the technique's cost and its
  combat-state prerequisites permit activation.
- Includes: Drive Impact, Drive Parry, Drive Rush, Drive Reversal and Overdrive
  attacks in Street Fighter 6.
- Excludes: passive Drive recovery; Super Art costs; ordinary guard or movement.
- Parameters: stock, cost, Burnout, fighter state, cancel source and technique.
- Evidence: [Street Fighter 6 decomposition](../games/s-z/street-fighter-6.md).
- Novelty: first isolated for `GAME-0172`; a single resource gates five shared
  offence, defence and mobility families and becomes wholly unavailable when
  exhausted.

## CON-445 — Super Art level requires sufficient current stock

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a requested Super Art may activate only when the current fighter
  has at least the stock required by that art's level and satisfies its normal
  command-state prerequisites.
- Includes: Level 1, 2 and 3 Super Arts against the three-stock Street Fighter 6
  Super Art Gauge.
- Excludes: Drive costs; passive meter gain; character progression; a cooldown-
  based ultimate with no spendable tiered reserve.
- Parameters: current stock, art level, cost, fighter state, command and spend.
- Evidence: [Street Fighter 6 decomposition](../games/s-z/street-fighter-6.md).
- Novelty: first isolated for `GAME-0172`; the explicit stock tier selects
  progressively priced finishers and persists across ordinary round resets.

## CON-446 — Vitality, timer and round wins bound one fighting match

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each round stops when a fighter reaches zero vitality or the
  declared timer expires and is adjudicated; the match ends only when one side
  accumulates the required round-win count.
- Includes: default `99`-second, first-to-two Street Fighter 6 One on One.
- Excludes: tournament games beyond one in-game match; an elimination-respawn
  objective; infinite Training Mode vitality or timer.
- Parameters: starting vitality, timer, KO, time-over comparison, draw policy,
  round markers and required wins.
- Evidence: [Street Fighter 6 decomposition](../games/s-z/street-fighter-6.md).
- Novelty: first isolated for `GAME-0172`; previous finite-round constraints
  bind team bomb, halftime or score rules rather than repeated resets of one
  fixed fighter pair.

## CON-447 — Drafted room must fit its vacant manor cell and entry edge

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a selected room plan is legal only when its target cell is inside
  the finite manor plan, remains unoccupied and exposes the doorway connection
  required by the addressed entry edge.
- Includes: ordinary Blue Prince room placement on the `5 × 9` manor plan.
- Excludes: judging whether the room is strategically useful; a free-form map
  canvas; movement through an already connected doorway.
- Parameters: grid bounds, target cell, occupancy, entry edge, plan doors,
  position restrictions and eligibility.
- Evidence: [Blue Prince decomposition](../games/a-f/blue-prince.md).
- Novelty: first isolated for `GAME-0173`; prior tile placement genes do not
  constrain a sampled room offer by both vacant cell and addressed doorway.

## CON-448 — Remaining daily steps gate room-to-room traversal

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: traversing from the current room into one connected adjacent room
  is legal only while the player has the required positive daily step amount,
  which the successful traversal reduces.
- Includes: Blue Prince's `50`-step morning and room-transition cost.
- Excludes: real-time movement stamina inside a room; a turn counter that
  advances on every interaction; room-plan gem cost.
- Parameters: current steps, traversal cost, adjacency, current room, target
  room, modifiers and resulting steps.
- Evidence: [Blue Prince decomposition](../games/a-f/blue-prince.md).
- Novelty: first isolated for `GAME-0173`; the resource counts transitions
  across a player-drafted room graph while room inspection remains untimed.

## CON-449 — Preparation and action phases gate role-specific control

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before the action phase, attackers are restricted to supported
  observation control while defenders may move, fortify and deploy; action
  unlocks attacker bodies and the live combat/objective rules for both roles.
- Includes: Rainbow Six Siege Bomb preparation and action phases.
- Excludes: an ordinary pre-round countdown with no asymmetric actions; a
  cosmetic loading screen.
- Parameters: phase, role, body control, observation authority, deployment,
  timer and transition.
- Evidence: [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Novelty: first isolated for `GAME-0174`; one timed phase grants different
  simultaneous control vocabularies to the two opposing roles.

## CON-450 — Fortification and gadget deployment require eligible surface and stock

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a defensive layer or gadget can be deployed only on a compatible,
  reachable and currently available surface while the responsible personal or
  team stock remains.
- Includes: Rainbow Six Siege reinforcements, barricades and surface-bound
  operator gadgets.
- Excludes: free placement through solid geometry; unlimited decorative props;
  selecting the gadget without deploying it.
- Parameters: role, item, stock, surface, reach, occupancy, orientation,
  placement time and conflict.
- Evidence: [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Novelty: first isolated for `GAME-0174`; a shared round fortification reserve
  and personal gadget stock jointly constrain mutable tactical geometry.

## CON-451 — Observation control requires a live feed and exposes the body

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: remote observation is available only through a surviving,
  accessible device feed; while attention controls that feed, the operator's
  body remains in the live world and can be attacked.
- Includes: Rainbow Six Siege drone and camera observation during live rounds.
- Excludes: pausing the world to inspect a map; omniscient spectator mode;
  direct avatar-centred sight.
- Parameters: device life, ownership, access, feed, body state, world time,
  interruption and exit.
- Evidence: [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Novelty: first isolated for `GAME-0174`; information gain explicitly trades
  embodied attention and safety for a destructible remote viewpoint.

## CON-452 — Lineup, bench and roles require eligible available squad members

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a match assignment is legal only when the selected footballer is
  registered and available, occupies one permitted lineup or bench place and
  is not simultaneously assigned to another slot.
- Includes: Football Manager 26 starting eleven, bench and positional roles.
- Excludes: whether a legal choice is tactically strong; transfers; cosmetic
  squad numbers.
- Parameters: competition registration, availability, injury, suspension,
  lineup capacity, bench capacity, position and duplicate assignment.
- Evidence: [Football Manager 26 decomposition](../games/a-f/football-manager-26.md).
- Novelty: first isolated for `GAME-0175`; it constrains a manager-authored
  autonomous match roster rather than direct-control participants.

## CON-453 — Manager influence is limited to declared plans and interventions

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during the fixture the player may alter only the supported
  lineup, role, shape and instruction interfaces; footballers and the ball
  remain under the match engine without direct embodied control.
- Includes: Football Manager 26 match management.
- Excludes: EA SPORTS FC direct player switching; scripted cinematics; a coach
  mode that still permits steering a footballer.
- Parameters: permitted interface, confirmation boundary, autonomous agents,
  direct-control locus and match phase.
- Evidence: [Football Manager 26 decomposition](../games/a-f/football-manager-26.md).
- Novelty: first isolated for `GAME-0175`; absence of body control is the
  operational authority boundary that makes observed football a management
  problem rather than a dexterity problem.

## CON-454 — Live substitutions obey bench, availability and competition limits

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a live substitution may use only an eligible named substitute
  and must remain within the competition's replacement and opportunity limits.
- Includes: the 2025/26 Premier League five-substitute, three-opportunity rule
  with half-time excluded from the opportunity count.
- Excludes: tactical role changes without personnel replacement; emergency
  rules outside the scoped fixture; transfer registration.
- Parameters: named bench, eligibility, substitutions used, opportunities
  used, half-time, outgoing player and incoming player.
- Evidence: [Football Manager 26 decomposition](../games/a-f/football-manager-26.md).
- Novelty: first isolated for `GAME-0175`; it binds a manager's live personnel
  interventions to both roster membership and a separate opportunity budget.

## CON-455 — Soldier commands require Action Points and obey terminal-action closure

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a soldier command is legal only if its movement, target, range,
  ammunition and Action Point requirements are satisfied; a declared
  turn-ending command forfeits that soldier's remaining ordinary authority.
- Includes: XCOM 2 movement bands, firing, reloading, grenades, Overwatch and
  objective interaction in Operation Gatecrasher.
- Excludes: whether a legal shot will hit; shared squad resources; commands
  available only in later classes or campaign systems.
- Parameters: soldier, remaining Action Points, command cost, terminal flag,
  reachable cells, target, range, ammunition and ability readiness.
- Evidence: [XCOM 2 decomposition](../games/s-z/xcom-2.md).
- Novelty: first isolated for `GAME-0176`; it joins per-soldier authority to
  spatial and equipment legality inside one interleavable squad phase.

## CON-456 — Enclosed Soccar geometry keeps ordinary contact live

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the standard arena's floor, curved walls, ceiling, goal frames
  and goal planes bound car and ball motion; ordinary wall or corner contact
  remains live rather than creating a football out-of-bounds restart.
- Includes: Rocket League DFH Stadium standard Soccar geometry.
- Excludes: touchline throw-ins, corners and goal kicks; leaving an open-world
  road; an alternate Dropshot or Hoops arena.
- Parameters: floor, wall, curve, ceiling, goal frame, goal plane, collision
  surface and legal play volume.
- Evidence: [Rocket League decomposition](../games/m-r/rocket-league.md).
- Novelty: first isolated for `GAME-0177`; it is the explicit inverse of
  `CON-399`'s whole-ball boundary stoppage.

## CON-457 — Capped reserve and ready pads gate vehicle boost

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: directed boost thrust is legal only while the controlled car has
  positive stored boost, the reserve cannot exceed its cap and a depleted pad
  cannot replenish another car until recharge completes.
- Includes: Rocket League default finite boost and arena pad availability.
- Excludes: unlimited boost mutators; ordinary throttle; a one-use inventory
  item with no spatial refill source.
- Parameters: reserve, cap, spend rate, pad ready state, pickup amount, recharge
  and crossing eligibility.
- Evidence: [Rocket League decomposition](../games/m-r/rocket-league.md).
- Novelty: first isolated for `GAME-0177`; it couples one personal acceleration
  reserve to contested reusable field locations.

## CON-458 — Airborne dodge requires current reset eligibility

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a second jump or directional dodge is available only while the
  car retains the default airborne eligibility or regains it through a legal
  multi-wheel surface or ball contact; later aerial orientation and boost do
  not themselves restore that action.
- Includes: Rocket League default double-jump/dodge window and flip reset from
  touching the ball with at least three wheels.
- Excludes: unlimited-jump or unlimited-dodge mutators; passive mid-air recharge;
  ordinary ground steering.
- Parameters: jump count, elapsed window, wheel contacts, supporting surface,
  ball contact, reset flag and dodge input.
- Evidence: [Rocket League decomposition](../games/m-r/rocket-league.md).
- Novelty: first isolated for `GAME-0177`; a physical contact condition restores
  a vehicle action token during continuous aerial motion.

## CON-459 — Zero-second ball state gates regulation settlement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: reaching `0:00` does not settle regulation while the live ball
  remains legally airborne; a qualifying ground contact or goal first closes
  that continuation, then score difference ends the match or a tie starts
  sudden-death overtime.
- Includes: Rocket League default Soccar zero-second play.
- Excludes: immediate clock expiry regardless of object state; added-time
  discretion; a fixed overtime duration.
- Parameters: clock, ball height/contact, goal crossing, score, settlement and
  overtime transition.
- Evidence: [Rocket League decomposition](../games/m-r/rocket-league.md).
- Novelty: first isolated for `GAME-0177`; terminal eligibility depends on the
  current physical ball state rather than the clock alone.

## CON-460 — Underwater action is bounded by oxygen and reachable air

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the survivor can continue an underwater excursion only while oxygen remains or a surface, powered habitat or powered vehicle is reachable before suffocation becomes lethal.
- Includes: Subnautica early dives from Lifepod 5 and the return to a powered first habitat.
- Excludes: food and water thresholds; vehicle crush depth; an unlimited breathing mode.
- Parameters: oxygen, capacity, consumption, depth, route distance, air source, travel speed and lethal grace.
- Evidence: [Subnautica decomposition](../games/s-z/subnautica.md).
- Novelty: first isolated for `GAME-0178`; vertical route feasibility depends on a replenishable embodied air budget.

## CON-461 — Blueprint requires its fragment scan threshold

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a fragment-derived recipe remains unavailable until completed scans of its technology class reach the declared required count.
- Includes: three Mobile Vehicle Bay fragments and three Seamoth fragments in Subnautica.
- Excludes: default-known recipes; one data-box unlock; possession of the final item without blueprint knowledge.
- Parameters: blueprint, fragment class, completed scans, required count and unlocked state.
- Evidence: [Subnautica decomposition](../games/s-z/subnautica.md).
- Novelty: first isolated for `GAME-0178`; a recipe gate counts repeated physical observations of matching world technology.

## CON-462 — Crafting requires recipe, ingredients, capacity and station

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: fabrication may begin only when the recipe is known, every required ingredient is available, the compatible station can operate and its output can be collected into eligible carried state.
- Includes: Subnautica Fabricator items and Mobile Vehicle Bay Seamoth fabrication.
- Excludes: Habitat Builder placement; a hidden recipe discovered by attempting arbitrary combinations; output from an autonomous industry line.
- Parameters: recipe state, ingredients, station class, power, output footprint, carried capacity and blocked feedback.
- Evidence: [Subnautica decomposition](../games/s-z/subnautica.md).
- Novelty: first isolated for `GAME-0178`; one legality boundary joins blueprint knowledge, material supply, powered station class and rectangular output fit.

## CON-463 — Habitat placement and use require legal pressure integrity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an underwater module can complete only at a clear supported pose with required materials, and the connected habitat remains safely usable only while its hull integrity is positive or recoverably repaired.
- Includes: placing a Subnautica I Compartment, Hatch and Solar Panel in shallow water with a positive shared hull value.
- Excludes: free-floating deployables; vehicle crush depth; cosmetic interior decoration.
- Parameters: preview, clearance, support, orientation, depth, material, connected base, integrity and breach state.
- Evidence: [Subnautica decomposition](../games/s-z/subnautica.md).
- Novelty: first isolated for `GAME-0178`; legal construction simultaneously respects geometry and a shared underwater pressure budget.

## CON-464 — Habitat oxygen requires connected available power

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a dry habitat supplies breathable oxygen and runs power-dependent fixtures only while connected generation or stored energy remains available.
- Includes: a shallow Solar Panel powering a Subnautica Seabase oxygen supply.
- Excludes: permanent oxygen in Lifepod 5; Seamoth Power Cell; an unpowered decorative module.
- Parameters: connection, generation, stored energy, load, dry state, oxygen and outage behaviour.
- Evidence: [Subnautica decomposition](../games/s-z/subnautica.md).
- Novelty: first isolated for `GAME-0178`; electrical availability is also a life-support legality condition for the interior.

## CON-465 — Seamoth operation obeys energy and current crush depth

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the submersible can provide controlled motion and oxygen only with usable installed energy, and sustained travel below its current maximum depth incurs pressure damage until it returns or is destroyed.
- Includes: an unmodified Subnautica Seamoth with a Power Cell and 200 m crush depth.
- Excludes: the avatar's standalone oxygen tank; an installed depth upgrade; water depth with no vehicle consequence.
- Parameters: charge, enabled systems, oxygen, current depth, crush depth, warning, damage and destruction.
- Evidence: [Subnautica decomposition](../games/s-z/subnautica.md).
- Novelty: first isolated for `GAME-0178`; one vehicle constraint couples stored energy to a vertically bounded breathable operating envelope.

## CON-466 — Building work requires a legal foundation and assigned villager

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a building foundation may be placed and advanced only when its civilization and Age unlock it, its full footprint is legal, its resource cost is available and at least one owned villager can reach and work it.
- Includes: ordinary Age of Empires II economic, military and defensive building construction.
- Excludes: instant editor placement; city-district adjacency; repair of an already completed structure.
- Parameters: building, Age, prerequisite, footprint, terrain, obstruction, stockpile, villager path and ownership.
- Evidence: [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
- Novelty: first isolated for `GAME-0179`; legal placement, prepaid materials and reachable live-builder work are all mandatory.

## CON-467 — Unit and research queues require site, unlock and stockpile

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a unit or technology order can enter only an eligible completed owned building when its civilization/Age prerequisites, resource cost and any population or queue-capacity gates are satisfied.
- Includes: Age of Empires II Town Center, military-building and research orders.
- Excludes: immediate shop purchases; a city's single turn-based production; free scenario reinforcements.
- Parameters: building class, order, civilization, Age, prerequisite, cost, population headroom, queue length and busy state.
- Evidence: [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
- Novelty: first isolated for `GAME-0179`; multiple building-local live queues share one resource and constructed-capacity economy.

## CON-468 — Age advancement requires resources and current-Age buildings

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the next Age can be researched at a Town Center only after the civilization owns the required stockpile and the required count of completed non-economic buildings from its current Age, including the Castle exception.
- Includes: Feudal, Castle and Imperial Age advancement in Age of Empires II: Definitive Edition.
- Excludes: a character level threshold; one technology prerequisite edge; starting directly in a later Age.
- Parameters: current Age, next Age, food, gold, required buildings, Castle exception, Town Center and research availability.
- Evidence: [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
- Novelty: first isolated for `GAME-0179`; spatial construction and shared stockpiles jointly gate the ordered global era transition.

## CON-469 — Resource work requires source access and compatible drop-off

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a villager can continue a resource task only while a compatible source remains reachable and a valid owned drop-off building can accept the carried quantity.
- Includes: food, wood, gold and stone gathering in Age of Empires II: Definitive Edition.
- Excludes: passive global income; inventory pickup with no return journey; trade-cart gold.
- Parameters: villager, source, remaining reserve, reachability, carry amount, drop-off class, ownership and route.
- Evidence: [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
- Novelty: first isolated for `GAME-0179`; extraction legality includes both the outbound worker path and an economic return endpoint.

## CON-470 — Group commands obey terrain, range and formation reachability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: ordered group movement or combat may resolve only through terrain each member can traverse, with legal formation space, target visibility, attack range and minimum-range conditions applied per unit.
- Includes: infantry, archer, cavalry and siege movement and combat in Age of Empires II: Definitive Edition.
- Excludes: hidden opponent strategy; production prerequisites; one direct avatar collision envelope.
- Parameters: terrain, footprint, path, formation, unit class, target, vision, attack range, minimum range and obstruction.
- Evidence: [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
- Novelty: first isolated for `GAME-0179`; heterogeneous group topology and unit-specific firing geometry jointly gate one live command.

## CON-471 — Aircraft operation requires viable powered systems

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: usable propulsion and dependent cockpit functions require a
  compatible fuel path, engine configuration and energised electrical circuits;
  invalid or depleted state removes the corresponding power or information.
- Includes: the scoped Microsoft Flight Simulator 2024 Cessna 172 fuel,
  mixture, magneto/starter, battery, alternator, avionics and shutdown gates.
- Excludes: a road vehicle's generic fuel reserve; cosmetic switch animation;
  Career maintenance or externally injected component failure.
- Parameters: fuel quantity, selector, mixture, ignition, engine state, battery,
  alternator, bus, circuit, load and dependent instrument.
- Evidence: [Microsoft Flight Simulator 2024 decomposition](../games/m-r/microsoft-flight-simulator-2024.md).
- Novelty: first isolated for `GAME-0180`; the aircraft's direct-control and
  information surfaces depend on a player-operated fuel/electrical chain.

## CON-472 — Flight and runway operations obey the aerodynamic envelope

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: taxi, takeoff, stable flight, approach and landing remain viable
  only while speed, attitude, lift, load, configuration, terrain clearance,
  runway alignment and remaining distance permit the intended transition.
- Includes: the scoped Microsoft Flight Simulator 2024 Cessna 172 takeoff,
  hand-flown route, approach, flare, touchdown and rollout.
- Excludes: a road-only collision envelope; a scripted aircraft animation;
  weather variation that does not affect the aircraft state.
- Parameters: airspeed, angle of attack, attitude, load, flap, trim, wind,
  altitude, terrain, runway heading, lateral error, descent rate and distance.
- Evidence: [Microsoft Flight Simulator 2024 decomposition](../games/m-r/microsoft-flight-simulator-2024.md).
- Novelty: first isolated for `GAME-0180`; airborne energy and runway geometry
  jointly gate a reversible ground-to-flight-to-ground chain.

## CON-473 — Logged flight completion requires arrival, parking and shutdown

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the bounded Free Flight terminal is eligible only after the
  selected aircraft reaches the destination on the ground, stops at parking
  and shuts down its propulsion and powered cockpit state without a crash,
  restart or shortcut.
- Includes: the scoped Microsoft Flight Simulator 2024 `KTIW` taxi-in,
  parking-brake stop and engine/electrical/avionics shutdown before logbook
  notification.
- Excludes: a touch-and-go, destination overflight, menu exit, Back on Track,
  teleport, Career mission score or unrelated profile persistence.
- Parameters: selected destination, on-ground state, parking region, speed,
  brake, engine, avionics, electrical power, crash state and entry eligibility.
- Evidence: [Microsoft Flight Simulator 2024 decomposition](../games/m-r/microsoft-flight-simulator-2024.md).
- Novelty: first isolated for `GAME-0180`; a non-competitive simulation terminal
  is made explicit by a complete destination systems reversal and durable record.

## CON-474 — Role Queue fixes a one-two-two team composition

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: each five-player team contains exactly one Tank slot, two Damage
  slots and two Support slots, and a matched player may occupy only the role
  committed before matchmaking.
- Includes: ordinary Overwatch 5v5 Role Queue in Quick Play.
- Excludes: Open Queue; temporary 6v6 Flex or Dynamic Queue; selecting a
  different hero inside the already committed role.
- Parameters: team size, roles, slot counts, player commitment and queue type.
- Evidence: [Overwatch decomposition](../games/m-r/overwatch.md).
- Novelty: first isolated for `GAME-0181`; the exact team topology is enforced
  by pre-match queue authority rather than emergent composition.

## CON-475 — Hero selection requires role, uniqueness and spawn authority

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a player may select or swap only to a hero inside the committed
  role, not currently occupied by an ally, and only while the team's legal
  spawn selection state permits the change.
- Includes: Overwatch Role Queue opening selection and same-role counter-swap
  after a team-spawn return.
- Excludes: Marvel Rivals Team-Up partner requirements; open-role switching;
  cosmetic skin selection.
- Parameters: role, hero, allied occupancy, spawn state, current life and
  effective selection time.
- Evidence: [Overwatch decomposition](../games/m-r/overwatch.md).
- Novelty: first isolated for `GAME-0181`; team uniqueness and reversible hero
  identity remain inside a pre-committed role boundary.

## CON-476 — Control terminal progress requires legal objective pressure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: percentage advances only for the current point owner, and a
  nominal terminal cannot end the round while an eligible opposing hero
  maintains the declared contest or takeover pressure at the active point.
- Includes: ordinary Overwatch Control scoring and overtime contest.
- Excludes: eliminations outside the point; Convergence escort proximity;
  bomb-device overtime or a fixed extension without objective presence.
- Parameters: ownership, percentage, point occupancy, opposing presence,
  contest, takeover, terminal threshold and overtime decay.
- Evidence: [Overwatch decomposition](../games/m-r/overwatch.md).
- Novelty: first isolated for `GAME-0181`; a symmetric ownership score and its
  terminal are both gated by the same live neutral-point pressure.

## CON-477 — One active National Focus obeys its branch gates

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a country may progress only one selected National Focus at a time,
  and the target must satisfy every declared prerequisite, branch exclusion and
  current-country condition.
- Includes: the base-game Italian focus choice in the tutorial.
- Excludes: parallel research slots; a law gated only by political cost; a
  completed focus's passive effect.
- Parameters: focus, active slot, prerequisite set, mutual exclusion, condition,
  cancellation and completion state.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; one national branch channel combines
  graph reachability with exclusive ongoing commitment.

## CON-478 — Research requires a free slot and reachable technology

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a technology can receive national research progress only in an
  available slot after its mandatory prerequisites are complete, with declared
  date and bonus rules modifying rather than bypassing the work.
- Includes: Italian industrial, electronic, land and air research in the scoped
  1936 tutorial.
- Excludes: National Focus selection; building-local research; a technology
  granted outright by an event.
- Parameters: slot, technology, prerequisite, year, ahead-of-time modifier,
  bonus, progress and completion.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; parallel national slots and historical
  timing qualify a persistent technology graph.

## CON-479 — State capacity and civilian factories gate construction

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a national construction entry is legal only in a state with the
  required ownership, building capacity and target-specific conditions, and it
  advances only from currently assignable civilian factory work.
- Includes: infrastructure and factory construction in eligible Italian states.
- Excludes: equipment production; instant event-built structures; worker-based
  foundation construction.
- Parameters: state, ownership, slot or level cap, target, factories, queue,
  modifier, repair and legal progress.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; national mobile work capacity is
  jointly gated by a persistent spatial state container.

## CON-480 — Equipment production requires unlocks, factories and resources

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a military production line can output only an unlocked equipment
  type with assigned operational factories, while missing strategic resources
  reduce its legal effective output.
- Includes: Italian infantry equipment, artillery and aircraft production.
- Excludes: construction of civilian buildings; equipment distribution;
  resources that affect only trade outside the scoped loop.
- Parameters: equipment, technology, factory, assignment cap, resource need,
  satisfaction, efficiency and output penalty.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; portfolio legality, shared factory
  capacity and input shortage jointly bound continuing national output.

## CON-481 — Army plans require legal formation and geography

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a battle plan or manual army order can govern only assigned
  divisions under valid command and must reference reachable provinces, a legal
  hostile border or destination and the current movement/combat state.
- Includes: Italian fronts and offensive lines against Ethiopia.
- Excludes: changing factory allocation; aircraft-region assignment; a purely
  decorative map annotation.
- Parameters: army, commander, division assignment, command limit, frontline,
  destination, adjacency, access, path, control and execution state.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; hierarchical ownership and live
  political geography gate persistent multi-agent instruction fields.

## CON-482 — Rail, hub and local capacity bound division supply

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a division can receive no more supply than the connected capital-
  to-hub route, hub throughput, available transport and local delivery state can
  legally provide against concurrent demand.
- Includes: undersupplied or motorised Italian divisions in East Africa.
- Excludes: equipment stockpile quantity alone; an inventory slot cap; a unit's
  direct movement path.
- Parameters: connected route, bottleneck rail, train, hub, truck, motorisation,
  terrain, weather, demand, delivered supply and penalty.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; nested network and last-mile limits
  directly bound the effectiveness of fielded strategic agents.

## CON-483 — Air missions require viable aircraft, base, range and fuel

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: an air wing can perform a selected mission only with compatible
  operational aircraft at a viable base whose range reaches the region and
  while required fuel and mission conditions remain available.
- Includes: Italian fighter and close-air-support missions over Ethiopia.
- Excludes: aircraft factory output; direct piloting; non-operational stored
  aircraft.
- Parameters: wing, aircraft class, strength, base capacity, region, range,
  coverage, fuel, weather, mission compatibility and efficiency.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; regional agent scheduling is jointly
  bounded by a spatial origin, operational stock and consumable support.

## CON-484 — Surrender threshold gates country capitulation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: ordinary territorial losses do not capitulate a country until
  weighted controlled victory points and modifiers cross its current surrender
  threshold and the war has a legal terminal settlement state.
- Includes: Ethiopian capitulation in the scoped tutorial war.
- Excludes: winning one land battle; occupying an unweighted border province;
  post-war resistance.
- Parameters: country, victory points, controlled share, surrender limit,
  modifiers, progress, remaining belligerents and settlement eligibility.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; spatially distributed losses must
  aggregate past a country-specific threshold before the opponent leaves war.

## CON-485 — Weapon and passive offers obey separate run slot caps

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an ordinary level-up may offer a new item only while its weapon
  or passive class has capacity, and may offer an owned item only below its
  declared maximum level; each offer contains no duplicate option.
- Includes: Vampire Survivors' ordinary six weapon and six passive-item level-up
  capacities under the scoped clean-save run.
- Excludes: stage items that may exceed normal level-up capacity; DLC-specific
  slot exceptions; permanent PowerUp purchases.
- Parameters: weapon slots, passive slots, owned set, item class, item maximum,
  offer uniqueness, eligibility pool and exception.
- Evidence: [Vampire Survivors decomposition](../games/s-z/vampire-survivors.md).
- Novelty: first isolated for `GAME-0183`; two parallel capped build classes
  jointly constrain repeated random drafts during a live survival stage.

## CON-486 — Weapon evolution requires mature base, counterpart and chest

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an ordinary base weapon can evolve only when it has reached its
  required level, its specified passive counterpart is held and the collected
  chest is authorised to award evolutions for the current stage and time.
- Includes: maximum-level Whip plus Hollow Heart and an eligible Mad Forest
  chest producing Bloody Tear.
- Excludes: ordinary weapon levelling; DLC unions and gifts; character-specific
  automatic evolution or all-chest exceptions.
- Parameters: base weapon, required level, passive counterpart, counterpart
  level, chest, stage, minute, eligibility exception and evolved result.
- Evidence: [Vampire Survivors decomposition](../games/s-z/vampire-survivors.md).
- Novelty: first isolated for `GAME-0183`; build maturity and a typed world-drop
  opportunity jointly gate replacement of an automatic weapon.

## CON-487 — Run remains viable only above zero health before the time limit

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the normal survival attempt continues only while the avatar has
  positive health or an eligible revival; reaching zero before the authored
  stage limit fails the attempt, while reaching the limit first satisfies stage
  completion before the terminal Reaper cleanup.
- Includes: a fresh-save Antonio normal Mad Forest run without revival PowerUps.
- Excludes: Endless mode; a multi-node health resource between separate rooms;
  Reaper defeat as a mandatory success condition.
- Parameters: current health, revival count, stage time, time limit, early death,
  completion order and Reaper transition.
- Evidence: [Vampire Survivors decomposition](../games/s-z/vampire-survivors.md).
- Novelty: first isolated for `GAME-0183`; the same health threshold changes
  meaning according to whether the authored survival clock has completed.

## CON-488 — Ground-vehicle fire requires a loaded legal ballistic solution

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a ground-vehicle weapon can release its selected ammunition only
  while ammunition remains, reload has completed and the current gun traverse,
  elevation and line permit that shot; a predicted penetration colour is
  advisory and does not waive the physical impact test.
- Includes: the M2A4 and LVT(A)(1) 37 mm guns and M2A2 heavy machine gun in the
  scoped War Thunder Ground Arcade match; the stock MS-1's finite loaded AP
  fire, gun geometry and uncertain aiming circle in one World of Tanks Standard
  Battle.
- Excludes: temporary aircraft weapons; unlimited abstract attacks; treating a
  green aim indicator as guaranteed penetration.
- Parameters: weapon, ammunition, loaded state, reload time, traverse,
  elevation, line of fire, dispersion, impact prediction and penetration test.
- Evidence: [War Thunder decomposition](../games/s-z/war-thunder.md) and
  [World of Tanks decomposition](../games/s-z/world-of-tanks.md).
- Novelty: first isolated for `GAME-0184`; visible aim assistance predicts a
  later physical armour test while finite ammunition and mechanism state still
  gate release.

## CON-489 — Ground Arcade permits at most three scoped lineup spawns

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player may commit no more than three ground-vehicle spawns in
  one Arcade battle and, with backups excluded, a vehicle already spawned from
  the fixed lineup is not eligible for another scoped spawn.
- Includes: at most one sortie each from M2A4, LVT(A)(1) and M2A2 in the scoped
  USA Rank I lineup.
- Excludes: temporary aircraft events; universal backups; Ground Assault's
  repeated same-vehicle spawns; Realistic spawn-point economy.
- Parameters: ground spawn cap, lineup, prior use, backup ownership, compatible
  vehicle, remaining selections and exhaustion.
- Evidence: [War Thunder decomposition](../games/s-z/war-thunder.md).
- Novelty: first isolated for `GAME-0184`; the tactical life budget is a short
  sequence of distinct preselected vehicles rather than identical respawns or
  one team's freely addressable deployment network.

## CON-490 — Starter Deck Duel admits only one supplied deck

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: entry to the match requires choosing one unedited deck from the
  event's supplied starter set; the game has no construction or sideboard
  revision boundary.
- Includes: selecting the official 60-card Arcane Aerialists list for the
  scoped MTG Arena Starter Deck Duel match.
- Excludes: Standard deck construction; collection ownership or crafting;
  sideboarding between games; every other event or format.
- Parameters: event, supplied deck set, chosen list, card count, edit lock,
  sideboard availability and match count.
- Evidence: [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md).
- Novelty: first isolated for `GAME-0185`; a live player-versus-player card
  match begins from one immutable event-supplied deck rather than a run-built
  or collection-built list.

## CON-491 — Ordinary land play requires the active main phase

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the active player may ordinarily play at most one land during
  their own turn, only in a main phase while the stack is empty and they have
  priority.
- Includes: one ordinary Plains, Island, Tranquil Cove or Temple of
  Enlightenment play per Arcane Aerialists turn.
- Excludes: mana abilities; effects that put lands onto the battlefield;
  casting a spell card; additional land plays created by card text.
- Parameters: active player, turn, land-play count, main phase, stack state,
  priority and rule-modifying effects.
- Evidence: [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md).
- Novelty: first isolated for `GAME-0185`; the resource base grows through a
  once-per-turn special action with stricter timing than its later mana use.

## CON-492 — Spell and ability timing follows priority and object type

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a spell or activated ability may be committed only while its
  controller has priority and its card type, current phase, stack state,
  targets and any text-specific timing restrictions permit that action.
- Includes: Arcane Aerialists instants responding in priority windows and
  ordinary creature or sorcery spells requiring the controller's main phase
  and an empty stack.
- Excludes: whether available mana can pay the cost; post-cast effect
  resolution; mana abilities whose activation can occur during payment.
- Parameters: priority, active player, card type, phase, step, stack state,
  target, timing text and exception.
- Evidence: [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md).
- Novelty: first isolated for `GAME-0185`; the same held resource can be legal
  in one nested response window and illegal in the adjacent one.

## CON-493 — Attacker declaration obeys readiness and attack restrictions

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an attacking creature must be controlled by the active player,
  be untapped, obey every attack restriction and ordinarily have been under
  that player's control continuously since the turn began unless it has haste.
- Includes: selecting ready Arcane Aerialists creatures during the declare-
  attackers step and tapping the declared attackers.
- Excludes: defender block legality; spell targeting; combat-damage assignment.
- Parameters: controller, active player, tapped state, control duration, haste,
  restriction, requirement, cost and defender.
- Evidence: [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md).
- Novelty: first isolated for `GAME-0185`; persistent creature readiness and
  control history jointly bound a simultaneous offensive subset.

## CON-494 — Block assignment obeys readiness and evasion relations

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a blocking creature must be controlled by the defender and
  untapped, and each attacker-blocker relation must satisfy all current evasion,
  restriction, requirement and cost rules.
- Includes: Arcane Aerialists flying creatures blocking attackers with flying,
  while ordinary ground creatures cannot block a flying attacker.
- Excludes: declaring attackers; later damage assignment; destroying a blocker
  after it has legally blocked.
- Parameters: blocker, attacker, controller, tapped state, flying, reach,
  restrictions, requirements, multiplicity and costs.
- Evidence: [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md).
- Novelty: first isolated for `GAME-0185`; defensive assignment is a typed
  relation whose legality depends on both endpoints and current keyword state.

## CON-495 — Cleanup reduces the active hand to its maximum size

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during cleanup, the active player whose hand exceeds the current
  maximum must choose and discard enough cards to reach that limit, normally
  seven.
- Includes: discarding an eighth or later Arcane Aerialists card at the scoped
  turn's cleanup step.
- Excludes: a hard hand capacity that prevents earlier draws; mulligan bottoming;
  discarding as a spell cost.
- Parameters: current hand count, maximum hand size, excess count, chosen cards,
  graveyard destination and modifying effects.
- Evidence: [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md).
- Novelty: first isolated for `GAME-0185`; temporary over-capacity is legal
  until a fixed phase boundary forces a player-selected reduction.

## CON-496 — Harvesting requires compatible reach, target and tool state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a world resource can be harvested only when the survivor is within interaction reach and its current source class accepts the chosen bare-hand action or an equipped compatible tool with remaining durability.
- Includes: picking grass or twigs by hand and chopping trees, mining boulders or digging stumps with the corresponding tool in scoped Don't Starve Together.
- Excludes: whether the source has regrown after depletion; combat-target reach; recipe ingredient requirements.
- Parameters: survivor, target, target state, reach, action class, required tool, equipped tool and durability.
- Evidence: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Novelty: first isolated for `GAME-0186`; spatial reach, source state and typed tool authority jointly gate the recurrent input economy.

## CON-497 — Darkness survival requires a live local light source

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during complete darkness a survivor must remain inside an active compatible illumination field or create one in time; otherwise ordinary interaction is suppressed and the darkness attacker can strike.
- Includes: maintaining a Campfire, Fire Pit, Torch or other ordinary scoped light through night.
- Excludes: winter warmth when ambient light remains; Sanity threshold effects; character-specific night vision.
- Parameters: survivor, world phase, ambient light, source, light radius, fuel state, interaction authority, warning and darkness attack.
- Evidence: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Novelty: first isolated for `GAME-0186`; continuous local illumination is a hard embodied-action precondition rather than only a visibility aid.

## CON-498 — Science-tier recipes require proximity until personally prototyped

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a survivor may craft a science-tier recipe only while near a station that exposes the required tier, unless that same survivor has already completed its first prototype and retained the recipe knowledge.
- Includes: Science Machine and Alchemy Engine recipe access for each scoped Wilson survivor.
- Excludes: ingredient availability; station placement legality; account-level unlocks; recipes that require no science tier.
- Parameters: survivor, recipe, required tier, nearby station, station state, personal prototype flag and knowledge retention.
- Evidence: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Novelty: first isolated for `GAME-0186`; a station gate changes permanently for one actor after successful local use while remaining closed for an uninitiated partner.

## CON-499 — Survival-fixture placement requires compatible clear ground

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a crafted deployable fixture can be committed only when its footprint is positioned on compatible world terrain without a blocking structure, entity or forbidden overlap.
- Includes: finding legal Forest ground for a Fire Pit, Science Machine, Alchemy Engine, Crock Pot or Chest.
- Excludes: paying the recipe ingredients; moving an already placed fixture; arbitrary base-layout optimisation.
- Parameters: fixture, footprint, terrain, obstruction, overlap, range, preview validity and placement position.
- Evidence: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Novelty: first isolated for `GAME-0186`; a crafted output remains unusable until its persistent service footprint passes a world-space compatibility test.

## CON-500 — Telltale revival requires a living giver and compatible ghost target

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: revival with a Telltale Heart requires a living survivor who has paid its material and health cost, carries the completed heart and gives it within reach to another player's ghost, which cannot use it on itself.
- Includes: one scoped Wilson crafting a Telltale Heart from Cut Grass and a Spider Gland at a 40-health cost and reviving the partner ghost with the declared maximum-health penalty.
- Excludes: self-revival; Endless-mode portal revival; Touch Stones or other revival items outside the transition trace.
- Parameters: giver life state, crafting materials, health cost, carried heart, ghost identity, reach, item consumption and revival penalty.
- Evidence: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Novelty: first isolated for `GAME-0186`; the recovery resource is craftable without science but remains unusable unless cooperation spans two different life states.

## CON-501 — Sanity threshold gates hostile shadow physicality

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a shadow creature may become a physically attacking target for a survivor only after that survivor's sanity falls below the applicable threshold, with full aggression below the lowest threshold.
- Includes: shadow-creature visual stages and hostility below fifteen percent sanity in the scoped Forest world.
- Excludes: ordinary hostile creatures; whether darkness changes sanity; visual distortion with no current mechanical target.
- Parameters: survivor, sanity maximum, current percentage, visibility threshold, physicality threshold, aggression threshold and shadow creature.
- Evidence: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Novelty: first isolated for `GAME-0186`; one actor's internal meter determines whether the same perceived entity can enter embodied combat with that actor.

## CON-502 — Class changes require legal team-spawn authority

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: selecting another playable class may change the player's
  controlled body and base kit only through an eligible team-spawn or next-life
  state; the ruleset permits teammates to select duplicate classes.
- Includes: initial and mid-match Team Fortress 2 class selection through the
  current team spawn, including a choice applied on the next legal life.
- Excludes: changing class in open combat; a unique-hero team gate; a required
  role composition; cosmetic or alternate-weapon selection.
- Parameters: player, team, spawn state, living state, current class, next
  class, effect timing and duplicate policy.
- Evidence: [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
- Novelty: first isolated for `GAME-0187`; flexible duplicate composition is
  legal, but embodied class replacement remains bound to spawn authority.

## CON-503 — Duty Support fixes a role-complete preset light party

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: one ordinary Duty Support entry must form a four-member light
  party with exactly one Tank, one Healer and two DPS, while A Realm Reborn
  supplies preset NPCs for every role not occupied by the player.
- Includes: a Gladiator tank entering Sastasha with Eager Conjurer healer,
  Eager Thaumaturge DPS and Eager Lancer DPS.
- Excludes: human Duty Finder composition; Overwatch's one/two/two Role Queue;
  replacing the preset NPCs; an undersized or unrestricted-party run.
- Parameters: party size, player role, required roles, role counts, preset NPCs,
  replacement authority and registration eligibility.
- Evidence: [FINAL FANTASY XIV Online decomposition](../games/a-f/final-fantasy-xiv-online.md).
- Novelty: first isolated for `GAME-0188`; a private instance completes its
  exact cooperative role topology with immutable autonomous participants.

## CON-504 — Duty entry and actions obey minimum level and sync cap

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: registration for Sastasha requires a legal combat class at or above
  the duty minimum, and inside the instance only actions and effective state at
  or below the level-18 sync boundary remain available.
- Includes: a Gladiator at level 18 or above entering Sastasha and using the
  declared level-18-or-lower class and Tank-role kit.
- Excludes: Paladin actions learned at level 30 or above; unrestricted entry;
  permanent removal of learned actions after the instance.
- Parameters: class, actual level, minimum level, sync level, action learn level,
  effective state, admitted action and suppressed action.
- Evidence: [FINAL FANTASY XIV Online decomposition](../games/a-f/final-fantasy-xiv-online.md).
- Novelty: first isolated for `GAME-0188`; entry qualification and temporary
  action legality share a level boundary without rewriting the retained build.

## CON-505 — Sastasha completion must precede the duty limit

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the required final-boss completion can settle the ordinary duty
  successfully only while the instantiated Sastasha 90-minute time allowance
  remains; expiry closes the instance without that completion.
- Includes: one ordinary synced Sastasha Duty Support run.
- Excludes: an individual boss enrage not present in this scope; a survival
  objective satisfied merely by reaching the clock; matchmaking wait time.
- Parameters: instance start, time allowance, remaining time, expiry, final
  objective state, abandon state and duty result.
- Evidence: [FINAL FANTASY XIV Online decomposition](../games/a-f/final-fantasy-xiv-online.md).
- Novelty: first isolated for `GAME-0188`; a generous shared instance horizon
  bounds a recoverable multi-encounter route without itself being the success
  target.

## CON-506 — Focus attacks require accumulated compatible staff state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a Focus-enhanced staff attack resolves only when the current
  stance/input can consume the held point or charge and the attack has not been
  invalidated by insufficient resource, interruption or recovery state.
- Includes: Black Myth: Wukong Chapter 1 Smash-stance heavy and varied attacks
  consuming accumulated Focus.
- Excludes: ordinary light attacks with no Focus cost; spell Mana; hidden enemy
  stagger; experience spent on a skill node.
- Parameters: stance, attack form, Focus stock, point threshold, charge,
  stamina, recovery, interruption and consumed amount.
- Evidence: [Black Myth: Wukong decomposition](../games/a-f/black-myth-wukong.md).
- Novelty: first isolated for `GAME-0189`; a discrete combat meter becomes legal
  only through the matching staff commitment rather than any generic ability.

## CON-507 — Temporary transformation requires acquired ready form state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a temporary replacement combat body may be activated only after
  its form has been acquired, its transformation readiness has recovered and
  the current avatar state permits the transfer.
- Includes: Black Myth: Wukong Red Tides after Guangzhi, subject to its current
  transformation readiness and legal live state.
- Excludes: cosmetic skin selection; an always-available protagonist switch;
  autonomous Spirit use; remaining in the form after its duration expires.
- Parameters: acquisition flag, form, readiness, current body, disabled state,
  duration or Might and return state.
- Evidence: [Black Myth: Wukong decomposition](../games/a-f/black-myth-wukong.md).
- Novelty: first isolated for `GAME-0189`; an earned temporary body is gated by
  both persistent acquisition and renewable live-form readiness.

## CON-508 — Lock torque is bounded by angle tolerance and pick durability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a lock can advance only while the current pick angle lies within
  the lock's concealed tolerance; torque outside that interval is resisted and
  destroys the finite pick after enough strain.
- Includes: the declared novice prison-cell lock and finite lockpicks in Skyrim
  Special Edition's scoped Helgen escape.
- Excludes: guaranteed opening with a matching key; an unlimited reusable probe;
  a single opaque probability check with no angular input.
- Parameters: lock difficulty, sweet-spot interval, pick angle, allowed travel,
  torque, strain, durability, remaining picks and unlock threshold.
- Evidence: [The Elder Scrolls V: Skyrim Special Edition decomposition](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md).
- Novelty: first isolated for `GAME-0190`; one hidden geometric tolerance binds
  both partial mechanical feedback and destruction of the probing resource.

## CON-509 — Campaign army routes require movement allowance and reachability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a campaign army may commit or finish a route only through
  traversable strategic terrain and within its current movement allowance,
  subject to blocking armies, settlement contact and stance restrictions.
- Includes: the Kislev Expedition's scoped movement between Kislev Refuge and
  the Beacon in Total War: WARHAMMER III.
- Excludes: battle-unit pathfinding; unrestricted map teleportation; one fixed
  board step with no replenishing allowance.
- Parameters: army, terrain, route, allowance, stance, obstruction, destination,
  settlement, encounter radius and remaining movement.
- Evidence: [Total War: WARHAMMER III decomposition](../games/s-z/total-war-warhammer-iii.md).
- Novelty: first isolated for `GAME-0191`; strategic reach is paid by a
  per-turn army allowance rather than by per-piece discrete move rules.

## CON-510 — Settlement construction requires a legal chain slot and treasury

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a settlement building may be commissioned only when the
  settlement is owned, a compatible slot and chain tier are available, all
  prerequisites hold and the treasury can pay the declared cost.
- Includes: the Kislev Refuge upgrade and Store House in the scoped Total War:
  WARHAMMER III prologue.
- Excludes: real-time worker access and foundation geometry; city-yield
  production; scripted free upgrades.
- Parameters: owner, settlement tier, slot, chain, prerequisite, treasury,
  cost, queue occupancy and permitted replacement.
- Evidence: [Total War: WARHAMMER III decomposition](../games/s-z/total-war-warhammer-iii.md).
- Novelty: first isolated for `GAME-0191`; a prepaid building-chain choice is
  gated by fixed settlement capacity rather than free spatial placement.

## CON-511 — Pre-battle placement must remain inside the assigned zone

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before battle starts, each controlled unit formation must fit
  entirely within the side's deployment region, on terrain the unit can occupy
  and without illegal overlap with another committed formation.
- Includes: the Kislev Expedition's deployment in the first scoped Beacon
  battle of Total War: WARHAMMER III.
- Excludes: movement orders after battle starts; off-map reinforcements;
  cosmetic formation diagrams.
- Parameters: side, deployment polygon, unit footprint, terrain, overlap,
  facing, formation width, hidden deployment and start commitment.
- Evidence: [Total War: WARHAMMER III decomposition](../games/s-z/total-war-warhammer-iii.md).
- Novelty: first isolated for `GAME-0191`; a temporary side-owned polygon gates
  the initial geometry of a later real-time battle.

## CON-512 — Disabled Survivors depend on a legal teammate intervention

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an incapacitated, ledge-hanging or hostile-held Survivor cannot
  restore ordinary movement and combat authority by standard self-input; a
  living reachable teammate must complete the compatible revive, pull-up or
  captor-release interaction before bleed-out, continuing harm or separation
  reaches defeat.
- Includes: incapacitation and Special Infected holds in Left 4 Dead 2's scoped
  Single Player Hotel chapter, with stock bots or Coach providing the legal
  intervention.
- Excludes: self-revival from a finite stock; ordinary low health with retained
  movement; a stun that expires automatically; post-death rescue closets.
- Parameters: Survivor state, captor, reach, living rescuer, interaction type,
  duration, interruption, bleed-out, continuing damage and defeat threshold.
- Evidence: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md).
- Novelty: first isolated for `GAME-0192`; both health-zero helplessness and an
  enemy-maintained hold impose the same asymmetric teammate authority without
  sharing one resolution rule.

## CON-513 — Chapter transition requires all living Survivors and a closed door

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an ordinary cooperative map transition remains illegal while any
  living Survivor is outside the exit checkpoint or while its terminal door is
  open; only collective occupancy followed by closure can settle the chapter.
- Includes: The Hotel's ground-floor safe room in the scoped Left 4 Dead 2
  Single Player Campaign.
- Excludes: dead Survivors as required occupants; a finale vehicle that may
  depart with fewer survivors; one-player extraction; merely touching the
  checkpoint boundary.
- Parameters: living roster, checkpoint region, per-member occupancy, door
  state, closure authority, completion predicate and next chapter.
- Evidence: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md).
- Novelty: first isolated for `GAME-0192`; a positive map terminal is gated by
  the conjunction of every surviving body and a player-controlled physical seal.

## CON-514 — Recruitment requires an available offer, denars and party space

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a settlement recruit can join the player's party only while that
  body remains in the current offer, the party has free capacity and the
  player's denars cover the displayed hiring price.
- Includes: hiring Tevea's offered tutorial troops in scoped Mount & Blade II:
  Bannerlord Campaign.
- Excludes: production-queue resources and population headroom; prisoner
  resistance; a scripted free companion; reinforcement after battle start.
- Parameters: settlement, recruit, offer quantity, denars, price, party limit,
  current roster, selected quantity and rejection reason.
- Evidence: [Mount & Blade II: Bannerlord decomposition](../games/m-r/mount-and-blade-ii-bannerlord.md).
- Novelty: first isolated for `GAME-0194`; local offer stock, money and mobile
  party capacity jointly gate immediate recruitment.

## CON-515 — Field treatment requires compatible machine, fill and state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a powered field implement can produce accepted treatment only
  when its vehicle supplies sufficient power and a compatible hitch, the tool
  is attached and active with remaining admissible material, and the current
  field/crop state permits that treatment.
- Includes: the tractor and solid-fertilizer spreader used on the assigned
  scoped Farming Simulator 25 field.
- Excludes: merely driving over a field; a hand tool with no coupled vehicle;
  cosmetic attachment; applying the wrong material; an autonomous abstract
  production recipe.
- Parameters: vehicle power, hitch, implement, attachment, activation, fill
  type, fill amount, field, crop/growth state and treatment eligibility.
- Evidence: [Farming Simulator 25 decomposition](../games/a-f/farming-simulator-25.md).
- Novelty: first isolated for `GAME-0196`; productive legality joins vehicle,
  powered attachment, consumable and persistent surface state.

## CON-516 — Field contract requires accepted target coverage

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a field-work contract may become collectable only when its
  accepted treated area reaches the ruleset's threshold on the assigned field;
  passes outside that field, inactive motion and already-counted overlap cannot
  replace the remaining eligible coverage.
- Includes: completion of the scoped Farming Simulator 25 Fertilizing contract.
- Excludes: a fixed route checkpoint order; cargo delivered to a depot; visual
  full coverage without accepted task progress; an owned-field yield bonus with
  no contract.
- Parameters: assigned field mask, eligible area, treated area, overlap policy,
  progress value, completion threshold and collectable state.
- Evidence: [Farming Simulator 25 decomposition](../games/a-f/farming-simulator-25.md).
- Novelty: first isolated for `GAME-0196`; one contract closes through accepted
  continuous surface coverage rather than object count, route or kill quota.

## CON-517 — Active food slots require distinct foods and eligible digestion state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a food can enter the active survival set only if an available
  slot or replaceable digestion state exists and no currently active food has
  the same type; refresh/replacement remains gated by the current food timer.
- Includes: the scoped Valheim three active food slots.
- Excludes: inventory stack capacity; eating any quantity into one hunger bar;
  potion cooldown; choosing an equipment slot.
- Parameters: slot count, food identity, active set, remaining duration,
  flashing/replaceable threshold and refresh rule.
- Evidence: [Valheim decomposition](../games/s-z/valheim.md).
- Novelty: first isolated for `GAME-0197`; capacity and type uniqueness govern
  a temporary stat loadout rather than carried storage.

## CON-518 — Forsaken fixtures require matching trophy state and count

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a Forsaken altar or sacrificial stone accepts an interaction only
  when the carried trophy type, required quantity, addressed boss identity and
  current summon/mount progression state match that fixture.
- Includes: two Deer Trophies at Eikthyr's altar and one Eikthyr Trophy at
  Eikthyr's Sacrificial Stone in the scoped Valheim route.
- Excludes: displaying a trophy at an ordinary item stand; generic held-item
  compatibility without boss/count/progression state; collecting boss loot.
- Parameters: fixture, Forsaken identity, trophy type, quantity, carried state,
  current boss state, mounted state and mismatch feedback.
- Evidence: [Valheim decomposition](../games/s-z/valheim.md).
- Novelty: first isolated for `GAME-0197`; the same trophy vocabulary gates
  both encounter entry and post-defeat power settlement at different fixtures.

## CON-519 — Aerial actions require current recovery eligibility

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an aerial jump, Recovery, Exhausted Recovery or dodge can begin
  only while the fighter retains the corresponding count or cooldown state,
  and only the declared ground, wall, hit or elapsed-time transition can
  restore that eligibility.
- Includes: the scoped Brawlhalla off-stage jump, Recovery and dodge gates.
- Excludes: Rocket League vehicle flip reset; passive flight fuel; ordinary
  grounded walking; an attack's hitbox legality after it begins.
- Parameters: action type, current count, cooldown, ground/wall/hit contact,
  elapsed time, wall-slip state, restored flag and attempted input.
- Evidence: [Brawlhalla decomposition](../games/a-f/brawlhalla.md).
- Novelty: first isolated for `GAME-0198`; several human-scale aerial actions
  use distinct but interacting eligibility gates inside one recoverable
  platform-fighter trajectory.

## CON-520 — Platform and blast zones bound stock survival space

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: fighters may leave and return to the solid platform while inside
  the playable surrounding space, but crossing any declared blast-zone
  boundary converts the current trajectory into a knockout regardless of
  remaining damage tolerance.
- Includes: Small Brawlhaven's platform, walls and surrounding blast zones in
  the scoped Brawlhalla duel.
- Excludes: hard fighting-game corners with no ring-out; a bottomless platform
  hazard that resets one checkpoint; static grid boundaries.
- Parameters: platform geometry, soft/solid surface, wall, playable extent,
  blast zone, fighter position, trajectory and knockout transition.
- Evidence: [Brawlhalla decomposition](../games/a-f/brawlhalla.md).
- Novelty: first isolated for `GAME-0198`; legal off-stage traversal and
  terminal spatial boundaries coexist around the same combat platform.

## CON-521 — Active weapon must belong to the selected Legend's pair

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a fighter may hold at most one active arena weapon, and a claimed
  neutral pickup can resolve only to one of the two weapon classes assigned to
  that fighter's selected Legend; otherwise the fighter remains unarmed.
- Includes: Bödvar's Sword/Hammer pair in the scoped Brawlhalla match.
- Excludes: cosmetic skins; persistent inventory capacity; two simultaneous
  hands; gadgets; selecting one slot from a carried quickbar.
- Parameters: Legend, compatible pair, previous weapon, active weapon, unarmed
  state, pickup alternation, throw/disarm and replacement.
- Evidence: [Brawlhalla decomposition](../games/a-f/brawlhalla.md).
- Novelty: first isolated for `GAME-0198`; shared generic pickups are typed by
  the claimant's fighter identity and produce one active command vocabulary.

## CON-522 — Stocks and clock bound one platform-fighter match

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each participant begins with the declared finite personal stock,
  each blast-zone knockout removes exactly one, and the match must settle at
  stock exhaustion or the configured clock boundary under the current Stock
  rules.
- Includes: three stocks and an eight-minute clock in the scoped Brawlhalla
  Bödvar mirror; the accepted research trace requires final-stock settlement
  before time-over.
- Excludes: health-zero rounds; team-shared reinforcement stock; an unbounded
  Training session; tournament sets beyond one in-game match.
- Parameters: participants, starting stocks, remaining stocks, knockout,
  match clock, time-over adjudication, accepted terminal and restart rule.
- Evidence: [Brawlhalla decomposition](../games/a-f/brawlhalla.md).
- Novelty: first isolated for `GAME-0198`; the same recoverable elimination
  counter both permits repeated returns and becomes the direct duel terminal.

## CON-523 — Garage settlement requires cleared police pursuit

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: exposed street-event earnings cannot become retained while
  police pursuit or search remains active; only escape followed by an eligible
  garage entry permits banking.
- Includes: the mandatory post-`Shopping Spree` LPD escape and Rydell's Rydes
  entry in Need for Speed Unbound.
- Excludes: free garage access with no pursuit; immediate race-result credits;
  paying to remove a wanted level; a loot-extraction zone.
- Parameters: exposed cash, pursuit state, perception, search interval, escape,
  garage, entry eligibility, banked result and bust.
- Evidence: [Need for Speed Unbound decomposition](../games/m-r/need-for-speed-unbound.md).
- Novelty: first isolated for `GAME-0199`; a completed race remains
  economically unsettled until a separate live law-enforcement state is clear.

## CON-524 — Capture and deployment remain inside the active A/D front

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: only objectives and team deployment sources belonging to the
  currently active Attack and Defend sector are legal; completing a sector
  closes its former combat space and requires defenders to fall back before the
  next sector becomes contestable.
- Includes: Coliseum sector objectives, deployment sources and fallback bounds
  in the scoped Delta Force match.
- Excludes: an open Conquest map where every point remains contestable; a
  shrinking survival ring; a payload route with no team redeployment network.
- Parameters: side, active sector, objective, source, legal combat area,
  fallback warning, closed sector and next-sector activation.
- Evidence: [Delta Force decomposition](../games/a-f/delta-force.md).
- Novelty: first isolated for `GAME-0200`; front legality advances only after a
  whole local objective set is secured.

## CON-525 — Casing and mask state gate overt heist actions

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: casing permits observation and ordinary movement but withholds
  weapons, restraints and criminal fixtures until the player commits the mask;
  completed detection or an overt action then commits the alarm boundary.
- Includes: inspecting the scoped PAYDAY 2 bank in casing, masking up and firing
  the declared unsuppressed AMCAR to force loud play.
- Excludes: unrestricted stealth attacks before a stance change; a cosmetic
  mask; concealment that automatically returns after combat.
- Parameters: casing state, mask state, available actions, concealment,
  forbidden input, overt stimulus and alarm commitment.
- Evidence: [PAYDAY 2 decomposition](../games/m-r/payday-2.md).
- Novelty: first isolated for `GAME-0201`; a one-way embodied commitment
  expands the action surface while exposing the remaining contract to alarm.

## CON-526 — Hostage control requires a compliant body and finite restraint

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a civilian can be restrained or redirected only while alive,
  reachable and compliant, each restraint consumes one available cable tie and
  police access can invalidate continued hostage control through rescue.
- Includes: tying and relocating one compliant Bank Heist civilian.
- Excludes: unlimited abstract hostage tokens; restraining an active hostile by
  ordinary civilian input; controlling a body through walls.
- Parameters: body state, compliance, reach, cable-tie stock, restraint,
  follow eligibility, police access and rescued state.
- Evidence: [PAYDAY 2 decomposition](../games/m-r/payday-2.md).
- Novelty: first isolated for `GAME-0201`; coercive control is jointly bounded
  by consumable restraint and the continuing spatial state of a vulnerable NPC.

## CON-527 — Drill work requires the matching vault fixture and live reach

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: placement, assembly and repair resolve only for a live,
  non-custody heister within interaction reach of the matching vault drill
  anchor; interruption prevents the current interaction channel from completing.
- Includes: placing, starting and repairing the Bank Heist thermal drill.
- Excludes: remote repair; a drill on an arbitrary wall; progress while the
  drill remains jammed; opening by a separately excluded preplanning key.
- Parameters: actor state, fixture, anchor, reach, interaction duration,
  interruption, jam state and opened state.
- Evidence: [PAYDAY 2 decomposition](../games/m-r/payday-2.md).
- Novelty: first isolated for `GAME-0201`; a persistent autonomous objective
  process depends on repeated embodied access to one authored machine anchor.

## CON-528 — Heavy loot has exclusive carriage and spatial deposit rules

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: one heavy loot bag may have at most one carrier, modifies that
  carrier's movement while held, becomes a recoverable world object when thrown
  and counts only after crossing a compatible secure-region boundary.
- Includes: the required Bank Heist: Cash money bag and escape van.
- Excludes: weightless inventory stacks; loose cash; credit from merely opening
  the vault; two simultaneous carriers of one bag.
- Parameters: bag, carrier, exclusive state, movement modifier, throw, collision,
  world recovery, secure region and credit.
- Evidence: [PAYDAY 2 decomposition](../games/m-r/payday-2.md).
- Novelty: first isolated for `GAME-0201`; a valuable objective alternates
  between constrained personal movement and shared spatial routing before credit.

## CON-529 — Mandatory secured loot gates the active heist escape

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the declared escape cannot settle before the contract-specific
  minimum secured-loot count holds, and success requires eligible crew presence
  in the currently active escape region rather than mere objective discovery.
- Includes: one secured money bag followed by escape-zone occupancy in Normal
  Bank Heist: Cash.
- Excludes: optional additional-loot maximisation; aborting from the menu;
  career progression after payout; a cash bundle still carried outside the van.
- Parameters: contract variant, required bag count, secured count, escape
  region, living roster, custody state, occupancy and success.
- Evidence: [PAYDAY 2 decomposition](../games/m-r/payday-2.md).
- Novelty: first isolated for `GAME-0201`; transported objective value and
  embodied departure are conjunctive terminal predicates.

## CON-530 — Preparation spawn must use a legal selectable region

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the controlled hero's first live position must belong to a region
  exposed as selectable on the current map during preparation and satisfy its
  current occupancy or conflict rules before the countdown commits it.
- Includes: Viper Ning's selected Wanchu spawn in Solo BOT Mode.
- Excludes: an aircraft-reachable landing envelope; random respawn after death;
  teleporting during live play.
- Parameters: map, selectable region, occupied state, conflict rule, countdown,
  final selection and first live position.
- Evidence: [NARAKA: BLADEPOINT decomposition](../games/m-r/naraka-bladepoint.md).
- Novelty: first isolated for `GAME-0202`; the map interface directly bounds
  the initial ground position before the live Survival loop begins.

## CON-531 — Melee relation requires compatible timing and weapon state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: common attack, Focus Strike, Clash and Counter outcomes occur
  only when the current weapon, charge class, action recovery and relative
  input windows form one of their declared legal relations.
- Includes: NARAKA: BLADEPOINT Blue Focus, Quick Counter, Clash, disarm and
  Counterstrike eligibility.
- Excludes: passive evasion; arbitrary Counter against an ordinary attack;
  ranged weapon reload; hero ability cooldown.
- Parameters: weapon, attack class, charge, recovery, opponent action, timing
  window, relation, disarm and follow-up authority.
- Evidence: [NARAKA: BLADEPOINT decomposition](../games/m-r/naraka-bladepoint.md).
- Novelty: first isolated for `GAME-0202`; the legal response depends on the
  opponent's live attack class and can change weapon ownership.

## CON-532 — Solo Rebirth requires its one available pre-cutoff allowance

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an eliminated Solo participant may return to live control only
  while the match's single Rebirth remains unused and the current phase has not
  crossed the declared Rebirth cutoff; consumption removes later eligibility.
- Includes: the one Rebirth available in NARAKA: BLADEPOINT Solo BOT Mode.
- Excludes: ally revival; indefinite checkpoint return; a fresh later match;
  final spectating after the allowance is unavailable.
- Parameters: mode, eliminated state, available stock, cutoff, consumption,
  return state and later finality.
- Evidence: [NARAKA: BLADEPOINT decomposition](../games/m-r/naraka-bladepoint.md).
- Novelty: first isolated for `GAME-0202`; a one-use Solo return is also bounded
  by the progressing battle-royale phase.

## CON-533 — Grappling requires carried stock and a valid anchor

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: firing a Grappling Hook can start a pull only while one carried hook
  remains and the aimed terrain or combatant is within the current target,
  range, line and action-state rules.
- Includes: NARAKA: BLADEPOINT terrain traversal, pursuit and disengagement by
  Grappling Hook.
- Excludes: unlimited ability charges; grappling through blocked geometry;
  pulling a remote object into inventory.
- Parameters: hook stock, aim mode, target class, range, line, action lock,
  attachment, consumption and rejection feedback.
- Evidence: [NARAKA: BLADEPOINT decomposition](../games/m-r/naraka-bladepoint.md).
- Novelty: first isolated for `GAME-0202`; the same finite item gates both
  traversal anchoring and combatant-targeted approach.

## CON-534 — Climbing grip requires reach, surface and usable stamina

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: continued climbing attachment is legal only while the hand can
  reach compatible surface, body state permits grip and positive usable stamina
  remains to pay the live action cost.
- Includes: PEAK surface grip and ledge transfers.
- Excludes: walkable ground contact; fixed ladder traversal; unlimited wall
  climbing; a rope not within reach.
- Parameters: hand, reach, surface tag, body state, usable stamina, cost,
  attachment and release.
- Evidence: [PEAK decomposition](../games/m-r/peak.md).
- Novelty: first isolated for `GAME-0203`; geometry and a composite survival
  meter jointly gate every free-surface attachment.

## CON-535 — Load and obstruction must leave sufficient climbing capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: carried weight increases activity burden and typed afflictions
  reserve portions of the main stamina bar, so a planned grip sequence is legal
  only within the remaining usable and bonus capacity.
- Includes: PEAK inventory weight, hunger, injury and biome-status obstruction.
- Excludes: a hard inventory slot cap alone; cosmetic encumbrance; fixed health
  damage with no effect on climb capacity.
- Parameters: weight, base stamina, obstruction, bonus stamina, action cost,
  recovery and required route segment.
- Evidence: [PEAK decomposition](../games/m-r/peak.md).
- Novelty: first isolated for `GAME-0203`; what the Scout carries and what has
  harmed them jointly determine whether the next physical route is affordable.

## CON-536 — Climbing-aid deployment requires stock and compatible terrain

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a rope or piton can create support only when its carried use
  remains, the target is reachable and the terrain accepts the aid's attachment
  and clearance rules.
- Includes: PEAK Rope Spool and Piton placement.
- Excludes: arbitrary mid-air creation; deployment through rock; unlimited
  reusable construction; merely dropping the item.
- Parameters: aid, stock, reach, target surface, clearance, attachment,
  consumption and rejection feedback.
- Evidence: [PEAK decomposition](../games/m-r/peak.md).
- Novelty: first isolated for `GAME-0203`; scarce route-editing inventory is
  bounded by the same immediate physical surface problem it is meant to solve.

## CON-537 — Summit rescue requires living presence and an ignitable Flare

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: ordinary rescue settlement may begin only while the controlled
  Scout is alive inside the PEAK region and a Flare can be ignited there after
  traversing the expedition's ordered route.
- Includes: the standard Peak solo helicopter terminal.
- Excludes: reaching the Peak Badge boundary without signalling; Ascent 8's
  Nadir ending; a Flare lit in an earlier biome; a dead Scout's result.
- Parameters: life state, region membership, route progress, Flare possession,
  ignition, signal and rescue eligibility.
- Evidence: [PEAK decomposition](../games/m-r/peak.md).
- Novelty: first isolated for `GAME-0203`; survival, place and a retained
  single-use signal are conjunctive predicates for the run's positive terminal.

## CON-538 — Lifestyle focus must be currently available

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a character can activate only a focus exposed within their
  current lifestyle under the rules governing focus selection or switching.
- Includes: Murchad's available Diplomacy focuses in the Crusader Kings III
  tutorial.
- Excludes: spending a perk point; selecting an unavailable lifestyle branch;
  temporary event modifiers.
- Parameters: character, lifestyle, focus roster, current focus and switch
  eligibility.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; a person-owned development category
  gates one replaceable persistent stance.

## CON-539 — Political marriage requires eligible partners and acceptance

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an ordinary marriage may settle only when both selected
  characters satisfy current kinship, doctrine, existing-relationship and
  availability rules and the receiving side accepts the disclosed arrangement.
- Includes: Murchad's prompted base-game tutorial marriage.
- Excludes: Grand Wedding requirements; childbirth; romance progress;
  succession after a spouse dies.
- Parameters: candidates, age, kinship, doctrine, current partner, marriage
  type, acceptance score and rejection reason.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; a social proposal is jointly gated
  by two character states and a predicted political acceptance result.

## CON-540 — Council office and task require typed eligibility

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a council appointment requires a character eligible for the
  selected office, and its active task must be one that office can perform on a
  legal target.
- Includes: the council and tasks exposed in Murchad's tutorial.
- Excludes: generic court employment; a passive ruler skill; a task outside the
  appointed office's authority.
- Parameters: office, candidate, eligibility, task roster, target, current
  assignment and invalid reason.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; person, office, operation and target
  form a typed four-part assignment gate.

## CON-541 — War declaration requires a valid casus belli

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: war can be declared only against a legal target through an
  available casus belli whose title, claimant, costs, truce and other displayed
  preconditions remain satisfied.
- Includes: the tutorial's Desmond title relation and declaration.
- Excludes: hostile raiding; an army moving without declared war; a fabricated
  claim not admitted by the scoped route.
- Parameters: attacker, defender, casus belli, title, claimant, cost, truce,
  participants and invalid reason.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; military authority begins with an
  inspectable legal relationship rather than spatial reach alone.

## CON-542 — Troop muster and command require available legal state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: troops can gather only from available contributions at a legal
  rally point, and a raised army can accept only reachable map orders permitted
  by current war, terrain, movement and control state.
- Includes: Murchad's levy and men-at-arms muster and Desmond orders.
- Excludes: creating free soldiers; commanding disbanded contributions; direct
  control of individual combatants.
- Parameters: contribution, availability, rally point, gathering, army,
  ownership, war relation, route, terrain and rejection.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; a distributed obligation must first
  become a legal spatial formation before it can receive a hostile route.

## CON-543 — Enforce demands requires a valid war-score settlement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the declared demand may be enforced only while the war remains
  active, the selected settlement is still valid and total war score meets its
  required threshold.
- Includes: enforcing Murchad's won Desmond tutorial war.
- Excludes: white peace at another threshold; surrender by the losing side;
  applying a title transfer without an active war.
- Parameters: active war, war score, required threshold, demand, validity,
  target title and unavailable reason.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; heterogeneous war progress becomes
  authority to apply one predeclared legal state transition.

## CON-544 — Admit only the fixed Tutorial loaner packet

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: entry to the named Solo chapter supplies and locks both declared
  card packets; no personal, edited or collection-owned deck can replace them.
- Includes: Master Duel Tutorial chapter `10003` with fixed player and CPU lists.
- Excludes: Starter Deck choice, later Solo loaners, Ranked construction or Side Decks.
- Parameters: chapter, loaner list, opponent list, edit lock, card counts and Extra Decks.
- Evidence: [Yu-Gi-Oh! Master Duel decomposition](../games/s-z/yu-gi-oh-master-duel.md).
- Novelty: first isolated for `GAME-0206`; one specific authored opponent pair,
  rather than a chosen event deck, is the only legal Duel entry.

## CON-545 — Enforce summon allowance, Tributes and materials

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: one ordinary own-turn allowance is shared by Normal Summon and
  Normal Set; high-Level monsters require their Tributes, while each Special
  Summon procedure requires all declared source and material relations.
- Includes: ordinary, Tribute, Synchro, Xyz and Link procedures reachable in
  chapter `10003`.
- Excludes: card text that explicitly grants an exception; deck construction.
- Parameters: allowance, level, Tribute count, procedure, materials, ratings and source.
- Evidence: [Yu-Gi-Oh! Master Duel decomposition](../games/s-z/yu-gi-oh-master-duel.md).
- Novelty: first isolated for `GAME-0206`; one recurring placement allowance
  coexists with unbounded but relation-gated procedure summons.

## CON-546 — Require a compatible open zone and battle position

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a monster, Spell or Trap may enter the field only in a compatible
  open zone and in a face-up/face-down Attack/Defense state legal for that
  action and card type.
- Includes: Monster and Spell/Trap Zones plus legal Summon, Set and Extra Deck placement.
- Excludes: whether the card's effect may activate; later combat comparison.
- Parameters: card type, source, zone class, occupancy, face, position and procedure.
- Evidence: [Yu-Gi-Oh! Master Duel decomposition](../games/s-z/yu-gi-oh-master-duel.md).
- Novelty: first isolated for `GAME-0206`; typed finite occupancy and
  orientation jointly determine whether a card can become public field state.

## CON-547 — Require activation timing, predicate, cost and targets

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a Spell, Trap or monster effect can activate only in its legal
  phase/window when every stated predicate, cost and target is valid; an
  ordinary Trap remains unavailable during the turn it was Set.
- Includes: fixed-packet Spells, Set Traps and monster effects.
- Excludes: response Spell-Speed compatibility; effect resolution after activation.
- Parameters: effect, phase, event, set turn, predicate, cost, target and availability.
- Evidence: [Yu-Gi-Oh! Master Duel decomposition](../games/s-z/yu-gi-oh-master-duel.md).
- Novelty: first isolated for `GAME-0206`; an event-sensitive activation joins
  card text to deliberately delayed concealed field state.

## CON-548 — Require compatible Spell Speed for each Chain response

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a response may become the next Chain Link only at Spell Speed 2
  or higher and never below the immediately preceding link's speed; no new
  response enters once backward resolution begins.
- Includes: Normal/Continuous Traps, Quick-Play Spells, Quick Effects and Counter Traps.
- Excludes: a first Spell Speed 1 activation; MTG priority; simultaneous combat damage.
- Parameters: prior speed, response speed, link, player, window and resolution state.
- Evidence: [Yu-Gi-Oh! Master Duel decomposition](../games/s-z/yu-gi-oh-master-duel.md).
- Novelty: first isolated for `GAME-0206`; typed response speed constrains a
  growing sequence that later closes completely before new authority returns.

## CON-549 — Require an eligible Battle Phase attack and target

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an ordinary attack requires a legal Battle Phase, a face-up
  Attack Position monster whose attack remains unused and a legal opposing
  monster target unless direct attack is permitted; the first player cannot
  conduct a first-turn Battle Phase.
- Includes: each separate chapter `10003` attack.
- Excludes: effect damage, blocker declaration or a simultaneous attacker set.
- Parameters: phase, first-turn rule, attacker, position, attack count, target and direct state.
- Evidence: [Yu-Gi-Oh! Master Duel decomposition](../games/s-z/yu-gi-oh-master-duel.md).
- Novelty: first isolated for `GAME-0206`; per-monster attack history and
  current opposing occupancy gate each sequential combat commitment.

## CON-550 — Complete the current carrier-heist predicate before advancing

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an authored vehicle-heist stage advances only after its current
  wreck quota, carrier catch-up, rear/side approach or delivery predicate is
  satisfied; unrecovered carrier separation or vehicle loss fails the attempt.
- Includes: the ordered two-Enforcer, rear approach, four-Enforcer, before-city
  catch, side approach and airfield-delivery gates in `The Highway Heist`.
- Excludes: race checkpoints that merely validate course order; an optional
  side bet; a player-selected waypoint; decorative camera positioning.
- Parameters: stage, target, quota, accepted wreck, carrier distance, approach
  region, recovery bound, delivery region, failure and next-stage authority.
- Evidence: [Need for Speed Payback decomposition](../games/m-r/need-for-speed-payback.md).
- Novelty: first isolated for `GAME-0208`; heterogeneous contact and spatial
  predicates gate one continuously moving vehicle set-piece sequence.

## CON-551 — Use an eligible shore and capacity for ferry transfer

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: selected units can enter or leave a ferry only when the vessel
  and passengers can reach a compatible shoreline or ramp, the passenger set
  fits remaining capacity and the destination ground can accept the unload.
- Includes: the river crossing in Cossacks 3 `War Ruse — Peace`.
- Excludes: the ferry's water path; naval attack range; automatic spawn aboard
  a transport; an abstract global transfer with no shoreline.
- Parameters: ferry, unit class, passenger count, remaining capacity, shore,
  ramp, path, destination footprint and obstruction.
- Evidence: [Cossacks 3 decomposition](../games/a-f/cossacks-3.md).
- Novelty: first isolated for `GAME-0209`; transport containment is legal only
  at a shared land-water interface with finite passenger room.

## CON-552 — Assemble the taught infantry regiment from its required members

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the instructed infantry formation becomes available only when
  the selected same-type soldiers meet its declared count and a compatible
  officer and drummer are present and reachable in the group.
- Includes: the 36-pikeman regiment with officer and drummer in Cossacks 3
  `War Ruse — Peace`.
- Excludes: arbitrary multi-type selection; formation movement after assembly;
  a visual group with no membership predicate; every formation count outside
  the taught packet.
- Parameters: infantry type, required count, officer, drummer, proximity,
  ownership, selection and unlocked formation class.
- Evidence: [Cossacks 3 decomposition](../games/a-f/cossacks-3.md).
- Novelty: first isolated for `GAME-0209`; exact rank-and-support composition
  gates conversion of loose RTS units into the instructed regiment.

## CON-553 — Match consumption or treatment to item condition and body state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an intended nutritional, hydration, wound-care or medicinal
  effect is legal and reliable only when the selected item's type, quantity,
  condition, contamination and target body state admit that use; incompatible
  or unsafe inputs may fail or introduce a different harmful state.
- Includes: DayZ clean food and water, disinfected bandages or rags and
  condition-specific medicine during the scoped fresh-spawn life.
- Excludes: generic inventory capacity; an uninterrupted-use duration already
  covered by `CON-286`; exact hidden pathogen progression; blood transfusion
  excluded from the scope.
- Parameters: item, quantity, condition, contamination, target state, wound,
  agent, dose, compatibility, intended effect and harmful alternative.
- Evidence: [DayZ decomposition](../games/a-f/dayz.md).
- Novelty: first isolated for `GAME-0210`; the same apparent resource class can
  help or harm according to retained item safety and the survivor's condition.

## CON-554 — Suspend control while unconscious and exposed

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while the current survivor is unconscious, ordinary movement,
  inventory, communication and combat actions are unavailable, but the body
  remains present and vulnerable in the live world; control returns only if
  shock recovery completes before lethal death.
- Includes: DayZ shock-based unconsciousness on the declared official server.
- Excludes: permanent death; a paused cutscene; voluntary sleep; a protected
  downed state that requires teammate revival; selecting respawn as the same
  analytical identity.
- Parameters: consciousness, shock, recovery rate, body presence, bleeding,
  incoming damage, action prohibition, recovery and death.
- Evidence: [DayZ decomposition](../games/a-f/dayz.md).
- Novelty: first isolated for `GAME-0210`; the player temporarily loses all
  ordinary authority without removing the body from shared hostile resolution.

## CON-555 — One destroyed tank cannot re-enter the current battle

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after the player's single assigned tank is destroyed, that tank
  cannot return during the current battle; direct control ends and only the
  eligible postmortem or spectator view remains until the team result settles.
- Includes: one stock MS-1 life in the scoped World of Tanks Standard Battle.
- Excludes: War Thunder lineup replacement; Battlefield redeployment; a garage
  repair after the battle; leaving before the shared result.
- Parameters: assigned tank, destroyed state, re-entry, spectator access,
  remaining allied vehicles and match boundary.
- Evidence: [World of Tanks decomposition](../games/s-z/world-of-tanks.md).
- Novelty: first isolated for `GAME-0211`; personal combat ends irreversibly
  inside a still-running team match without either a later round return or a
  replacement vehicle.

## CON-556 — Gravity Gun manipulation requires an eligible physics target

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the ordinary Gravity Gun may pull, attach or punt only a target
  accepted by its current trace, distance, movable VPhysics, mass, flesh,
  forbidden-flag, player-support and clearance rules; a rejected target remains
  in world state and no held relation is created.
- Includes: ordinary movable Ravenholm props accepted or rejected by the base
  Half-Life 2 Gravity Gun.
- Excludes: the supercharged Gravity Gun's NPC and mass permissions; Portal
  cube carrying with no physcannon trace; recursive relative-scale eligibility;
  whether an already launched prop later damages a hostile.
- Parameters: trace length, line or hull hit, distance, physics object, maximum
  mass, flesh state, spawn flags, world support, player ground entity,
  attachment clearance and rejection feedback.
- Evidence: [Half-Life 2 decomposition](../games/g-l/half-life-2.md).
- Novelty: first isolated for `GAME-0212`; one remote manipulation attempt is
  jointly gated by physical type, mass, spatial acquisition and explicit
  authoring permissions rather than generic reach or inventory capacity.

## CON-557 — Taxi-fare credit requires the assigned passenger and destination

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: the current taxi fare can settle only while its assigned
  passenger and service vehicle remain mission-valid and that vehicle reaches
  the fare's named destination arrival area; another location or passenger
  cannot advance the authored chain.
- Includes: each of the five scoped Mafia (2002) `The Running Man` passenger
  deliveries.
- Excludes: type-compatible passengers choosing any matching network stop;
  cargo accepted at a generic depot; reaching a destination after abandoning
  the required vehicle; an unbounded taxi score.
- Parameters: fare index, assigned passenger, taxi, viability, destination,
  arrival area, stop state and settlement flag.
- Evidence: [Mafia (2002) decomposition](../games/m-r/mafia-2002.md).
- Novelty: first isolated for `GAME-0214`; identity, vehicle continuity and one
  authored destination jointly gate each service-stage transition.

## CON-558 — Nail deployment requires available stock and a marked target

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a reusable nail may attach only when that named nail is not
  already deployed and its aimed hit reaches a compatible marked surface,
  switch or mechanism; unmarked geometry and exhausted available stock reject
  the request until a deployed nail is recalled.
- Includes: Cody's yellow-target and bounded-nail eligibility during It Takes
  Two's hammer-and-nails packet.
- Excludes: ordinary firearm ammunition; unrestricted building placement;
  inventory capacity with no world-target predicate; May's hammer fixtures.
- Parameters: nail identity, available set, deployed set, mark class, reach,
  line of travel, compatible target, rejection and recall.
- Evidence: [It Takes Two decomposition](../games/g-l/it-takes-two.md).
- Novelty: first isolated for `GAME-0215`; a finite reusable tool is gated by
  both current world assignment and an authored visual-surface predicate.

## CON-559 — First transfer requires level, quest and class compatibility

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a first class transfer is available only when the persistent
  character has the declared starting class/race eligibility, reaches the
  required level, completes the class-transfer quest and selects one compatible
  offered destination.
- Includes: a non-Ertheia Lineage II Live Human Fighter reaching level 20,
  completing `Path of Destiny - Beginning` and selecting Warrior.
- Excludes: level alone; quest completion below threshold; incompatible class;
  skill-point prerequisites; later paid class changes.
- Parameters: race, starting class, level, quest, completion flag, offered
  destinations, selected destination and rejection reason.
- Evidence: [Lineage II decomposition](../games/g-l/lineage-ii.md).
- Novelty: first isolated for `GAME-0219`; persistent level and one authored
  class quest jointly gate an exclusive identity transition.

## CON-560 — Fortification work requires an authored outline and valid channel

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: battlefield construction or repair is legal only at a currently
  exposed compatible authored outline, within tool reach and while the player
  sustains the required interaction without an interrupting state.
- Includes: Battlefield V toolbox work on Arras trenches, barriers and supply
  stations at their fixed Fortification positions.
- Excludes: placing a structure at arbitrary terrain; spending a finite Siege
  reinforcement panel; repairing a tank; merely seeing the outline.
- Parameters: outline, type, team, reach, tool, posture, progress, interruption,
  existing damage and completion.
- Evidence: [Battlefield V decomposition](../games/a-f/battlefield-v.md).
- Novelty: first isolated for `GAME-0220`; placement is not inventory-bounded
  but still constrained by an authored live-world affordance and channel.

## CON-561 — Reinforcement calls require leader authority, points and target

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a squad Reinforcement can be confirmed only by the current squad
  leader when the shared pool covers its cost, the option is currently
  available and every required target satisfies its spatial and state rules.
- Includes: Battlefield V leader-authorised supply, smoke or strike calls after
  the squad earns sufficient points.
- Excludes: any squad member spending the pool; personal gadget charges; a
  targetless request for a spatial call; spending team tickets.
- Parameters: leader identity, squad, points, cost, option, availability,
  target class, range, obstruction, confirmation and rejection.
- Evidence: [Battlefield V decomposition](../games/a-f/battlefield-v.md).
- Novelty: first isolated for `GAME-0220`; a shared resource remains
  deliberately unusable without one role's current authority and a legal call
  geometry.

## CON-562 — Tutorial-dungeon entry requires quest gate and a supported roster

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the required tutorial dungeon becomes a valid continuation only
  after its authored main-chain gate and admits one to five eligible players,
  with the client supplying autonomous followers for missing combat functions
  rather than allowing an empty or unrelated roster.
- Includes: a solo Alliance Human Warrior entering Darkmaul Citadel after
  `To Darkmaul Citadel` on the full Exile's Reach route.
- Excludes: the Housing Skip; a later free-form dungeon group; FFXIV's exact
  four-member 1/1/2 Duty Support composition; human participants above the
  tutorial limit; entering before the required quest state.
- Parameters: quest flag, player count, character eligibility, dungeon,
  follower requirement, admitted roster, rejection and instance lifetime.
- Evidence: [World of Warcraft decomposition](../games/s-z/world-of-warcraft.md).
- Novelty: first isolated for `GAME-0221`; one authored tutorial gate combines
  variable human occupancy with automatic functional completion of the roster.

## CON-563 — Tutorial admission is faction-gated and closes after one exit

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the bounded tutorial can be entered only by an eligible fresh
  character through the City Guard of its faction's major city; selecting the
  Daeva of Time exit permanently removes that character's re-entry permission,
  whether or not every objective and reward was completed.
- Includes: an Elyos Aion Classic character entering `Boundary of Light and
  Darkness` through Sanctum and losing re-entry after leaving.
- Excludes: a repeatable dungeon lockout; a daily entry counter; a quest-gated
  party roster; an exit that can be undone by loading a checkpoint.
- Parameters: character, freshness flag, faction, City Guard, instance,
  completion state, exit confirmation and retained closed flag.
- Evidence: [Aion Classic decomposition](../games/a-f/aion-classic.md).
- Novelty: first isolated for `GAME-0223`; the same warned exit closes both
  successful completion and every incomplete route for that character.

## CON-564 — Gate new-character tutorial admission by account history

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a newly created character is routed directly into the current
  tutorial unless the same account already has a declared non-beginner
  character, in which case the client may offer an authorised skip branch.
- Includes: fixing a fresh Once Human account with no non-beginner character so
  its new Meta-Human must enter the revamped new-player experience.
- Excludes: a per-character one-use exit; a quest level gate; a server queue;
  choosing to skip on a fresh account; inherited inventory or paid access.
- Parameters: account, existing-character history, non-beginner predicate, new
  character, direct admission, skip authority and selected branch.
- Evidence: [Once Human decomposition](../games/m-r/once-human.md).
- Novelty: first isolated for `GAME-0224`; onboarding legality depends on prior
  account-level character history before any scenario or server is selected.

## CON-565 — Share one finite starfighter power budget

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: engines, laser weapons and shields must share one bounded live
  power budget, so emphasizing any channel necessarily withholds some available
  allocation from at least one other channel until the player reallocates it.
- Includes: the fixed T-65B X-wing in `Form the Vanguard`.
- Excludes: three independent cooldown bars; permanent component points;
  front/rear shield-charge transfer; ammunition shared by two weapons.
- Parameters: total budget, engine allocation, laser allocation, shield
  allocation, balanced distribution, emphasized channel and reallocation.
- Evidence: [STAR WARS: Squadrons decomposition](../games/s-z/star-wars-squadrons.md).
- Novelty: first isolated for `GAME-0225`; three simultaneously active cockpit
  subsystems compete through a reversible zero-sum performance allocation.
