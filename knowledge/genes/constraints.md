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
  sequence visiting distinct cells under directed arrow-ray adjacency.
- Excludes: adjacency not declared by the instance; branched networks;
  disconnected cells of one route; paths that leave and re-enter the board.
- Parameters: adjacency topology, turn count, route length and board boundary.
- Evidence: [Flow Free decomposition](../games/a-f/flow-free.md) and
  [Cosmic Express decomposition](../games/a-f/cosmic-express.md), and
  [The Witness decomposition](../games/s-z/the-witness.md), and
  [LYNE decomposition](../games/g-l/lyne.md), and
  [Signpost decomposition](../games/s-z/signpost.md).
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
- Excludes: unrestricted crossing; bridge cells carrying two routes on separate
  layers; ordinary piece occupancy without route continuity.
- Parameters: position capacity, permitted bridge classes and endpoint sharing.
- Evidence: [Flow Free decomposition](../games/a-f/flow-free.md), and
  [LYNE decomposition](../games/g-l/lyne.md), and
  [Bridges decomposition](../games/a-f/bridges.md).
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
  after collecting the final remaining gem earlier in the same move.
- Excludes: exposing a previously concealed hazard; falling beyond a supported
  boundary; recoverable damage; a blocked command that never enters a hazard;
  a hazard that merely removes optional score.
- Parameters: hazard class, contact geometry, completion-versus-failure
  precedence, feedback and recovery interface.
- Evidence: [Inertia decomposition](../games/g-l/inertia.md).
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
  [The Talos Principle decomposition](../games/s-z/the-talos-principle.md).
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
