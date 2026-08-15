# System Behaviour Genes

## SYS-001 — Directional line compression

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after a direction is chosen, movable elements automatically
  travel as far as permitted along parallel lines.
- Includes: deterministic maximal translation to a boundary or blocker.
- Excludes: the player's directional choice; gravity acting without a
  direction selected each turn.
- Evidence: [2048 decomposition](../games/0-9/2048.md).
- Novelty: not assessed; this is part of the baseline genome.

## SYS-002 — Collision-triggered compatible merge

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: compatible elements that collide during automatic resolution are
  replaced by one transformed element.
- Includes: equality-based numeric doubling in 2048; `1 + 2` base pairing and
  equal-rank doubling from 3 upward in Threes.
- Excludes: a player directly selecting two objects to combine.
- Parameters: compatibility relation, output transform, resolution order.
- Evidence: [2048 decomposition](../games/0-9/2048.md) and
  [Threes decomposition](../games/s-z/threes.md).
- Novelty: not assessed; this is part of the baseline genome.

## SYS-003 — Element spawn after valid action

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: one or more new elements are inserted after a valid action or its
  automatic resolution creates capacity for them.
- Includes: the post-move tile insertion in 2048 and Threes; refilling Royal
  Match board vacancies from above after a clear and collapse.
- Excludes: initial setup; deterministic refill; spawn after an invalid input.
- Parameters: trigger, element type and available positions.
- Evidence: [2048 decomposition](../games/0-9/2048.md) and
  [Royal Match decomposition](../games/m-r/royal-match.md), and
  [Threes decomposition](../games/s-z/threes.md).
- Novelty: not assessed; this is part of the baseline genome.

## SYS-004 — Random outcome selection

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the system selects an outcome from more than one possible result
  according to a probability process.
- Includes: selecting the spawned tile's value and empty position in 2048;
  selecting the successor tetromino in NES Tetris; selecting incoming Royal
  Match item types and a Propeller's target; selecting the eligible entry lane
  and preview-bounded next tile in Threes; selecting Mini Metro station
  locations, passenger demand and eligible weekly offer contents; selecting
  Loop Hero dawn spawns, card rewards and loot.
- Excludes: hidden but predetermined outcomes; player-selected uncertainty.
- Parameters: outcome set and probability distribution.
- Evidence: [2048 decomposition](../games/0-9/2048.md) and
  [Tetris decomposition](../games/s-z/tetris.md), and
  [Royal Match decomposition](../games/m-r/royal-match.md), and
  [Threes decomposition](../games/s-z/threes.md), and
  [Mini Metro decomposition](../games/m-r/mini-metro.md), and
  [Loop Hero decomposition](../games/g-l/loop-hero.md).
- Novelty: not assessed; this is part of the baseline genome.

## SYS-005 — Zero-clue region expansion

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: revealing a safe position with zero adjacent hazards
  automatically reveals its connected zero-valued region and the region's
  numbered boundary before the next player input.
- Includes: classic Minesweeper blank-area expansion.
- Excludes: the player's initially selected reveal; a player-commanded chord;
  random placement of hazards during setup.
- Parameters: neighbourhood topology, connectivity and expansion stopping rule.
- Evidence: [Minesweeper decomposition](../games/m-r/minesweeper.md).
- Novelty: not assessed.

## SYS-006 — Time-driven automatic descent

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while play remains active, the system periodically attempts to
  move the currently controllable element downward without requiring a player
  command.
- Includes: level-dependent gravity applied to the active NES Tetris tetromino.
- Excludes: compression after a direction selected by the player; a one-time
  post-action drop; cosmetic animation without a state change.
- Parameters: descent interval, acceleration schedule and spatial direction.
- Evidence: [Tetris decomposition](../games/s-z/tetris.md).
- Novelty: not assessed.

## SYS-007 — Blocked-descent locking

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when the active element is due to descend but cannot occupy the
  next lower position, the system converts it into fixed board occupancy.
- Includes: an NES Tetris tetromino locking after a blocked gravity or soft-drop
  attempt.
- Excludes: the player explicitly confirming placement; reversible resting that
  can continue indefinitely; collision that only rejects one lateral input.
- Parameters: locking trigger, contact timing and any delay before fixation.
- Evidence: [Tetris decomposition](../games/s-z/tetris.md).
- Novelty: not assessed.

## SYS-008 — Completed-line removal and collapse

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after placement, every completely occupied line is removed and
  the retained occupancy above each removed line shifts toward the vacated
  space before play continues.
- Includes: clearing one to four horizontal rows and shifting higher blocks
  downward in NES Tetris.
- Excludes: deleting selected elements; removing incomplete lines; rigid-body
  gravity that independently settles cells into internal holes.
- Parameters: line orientation, simultaneous-clear limit, collapse direction
  and score schedule.
- Evidence: [Tetris decomposition](../games/s-z/tetris.md).
- Novelty: not assessed.

## SYS-009 — Successor active-element introduction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after the current controllable element becomes fixed and its
  resolution completes, the system introduces a successor as the new active
  element at a designated entry region.
- Includes: spawning the next tetromino after lock and any line clear in NES
  Tetris A-Type.
- Excludes: adding an element after every valid player action; simultaneous
  control of multiple persistent elements; initial setup only.
- Parameters: entry position, orientation, delay and sequence source.
- Evidence: [Tetris decomposition](../games/s-z/tetris.md).
- Novelty: not assessed.

## SYS-010 — Automatic qualifying-match removal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a valid board change, the system detects every qualifying
  same-type pattern in the resolved state and removes its ordinary matched
  elements before the next player input.
- Includes: clearing horizontal or vertical Royal Match groups of three or
  more same-coloured items.
- Excludes: player-selected deletion; completed occupancy-line removal; a
  power-up's triggered area effect; matching that only awards points.
- Parameters: qualifying geometry, minimum group size, simultaneous-resolution
  rule and target-credit rule.
- Evidence: [Royal Match decomposition](../games/m-r/royal-match.md).
- Novelty: not assessed.

## SYS-011 — Vacancy-driven vertical board collapse

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after fixed board elements are removed, retained movable elements
  automatically fall within their columns to occupy reachable vacancies before
  refill or the next player input.
- Includes: Royal Match colour items and power-ups dropping after a clear.
- Excludes: time-driven descent of one controllable active element; compression
  in a direction chosen by the player; shifting whole rows after a completed
  line is removed.
- Parameters: gravity direction, blocked cells, portals and column topology.
- Evidence: [Royal Match decomposition](../games/m-r/royal-match.md).
- Novelty: not assessed.

## SYS-012 — Repeat automatic resolution until stable

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after removal, movement and insertion, the system repeatedly
  checks and resolves newly created qualifying effects until no further effect
  remains, without charging another player action.
- Includes: Royal Match cascades caused by falling or newly inserted items.
- Excludes: one fixed post-action pass; a chain requiring player confirmation
  between steps; indefinite time-driven motion.
- Parameters: stability predicate, effect priority, maximum chain safeguards
  and reward scaling.
- Evidence: [Royal Match decomposition](../games/m-r/royal-match.md).
- Novelty: not assessed.

## SYS-013 — Pattern-conditioned special-element creation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when a resolved match has a declared size or geometry, the system
  replaces part of that match with a persistent special element whose class is
  selected by the pattern.
- Includes: creating Royal Match Rocket, Propeller, TNT and Light Ball
  power-ups from qualifying four- or five-item patterns.
- Excludes: pre-level booster placement; random ordinary refill; combining two
  existing power-ups; a match that only removes its elements.
- Parameters: pattern geometry, special-element class, creation position and
  simultaneous-match priority.
- Evidence: [Royal Match decomposition](../games/m-r/royal-match.md).
- Novelty: not assessed.

## SYS-014 — Activated multi-target clearing effect

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after a board power-up is activated, the system removes or hits
  a rule-selected set of board elements beyond one ordinary qualifying match.
- Includes: Royal Match row or column Rockets, radius-based TNT, target-seeking
  Propellers, colour-wide Light Balls and the larger footprints of power-up
  combinations.
- Excludes: the player's activation gesture; ordinary three-item match removal;
  cosmetic effects that do not change board state.
- Parameters: footprint, target selection, obstacle interaction, repetition and
  combination mapping.
- Evidence: [Royal Match decomposition](../games/m-r/royal-match.md).
- Novelty: not assessed.

## SYS-015 — Maximal compatible top-segment transfer

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after source and destination containers are selected, the system
  transfers the largest possible contiguous top segment of one type, bounded by
  both that segment's size and the destination's remaining capacity.
- Includes: pouring all available same-colour top water into a Water Sort tube,
  or only the part that fits when its remaining capacity is smaller.
- Excludes: player-selected quantity; moving a mixed segment; transferring one
  element when more compatible top units fit; gravity-driven collapse.
- Parameters: unit granularity, segment identity, destination margin and
  animation.
- Evidence: [Water Sort decomposition](../games/s-z/water-sort.md).
- Novelty: not assessed.

## SYS-016 — Overlap-triggered path break

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when an actively traced path attempts to cross or overlap an
  occupied path cell, the system breaks the conflicting pipe instead of
  retaining two paths in that cell.
- Includes: a Flow Free pipe breaking when another traced pipe crosses or
  overlaps it.
- Excludes: rejecting the trace without changing either path; allowing a bridge
  or layered crossing; player-commanded deletion unrelated to overlap.
- Parameters: which conflicting continuation is removed, visual feedback and
  whether the interrupted path may be resumed.
- Evidence: [Flow Free decomposition](../games/a-f/flow-free.md).
- Novelty: not assessed.

## SYS-017 — Spatial text-rule parsing

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after the board changes, the system reads aligned word objects in
  declared directions, recognises grammatically valid sentences and updates
  the active rule set before the next player decision.
- Includes: recognising horizontal or vertical `NOUN IS PROPERTY` sentences in
  Baba Is You and deactivating them when alignment is broken.
- Excludes: player-authored code outside play; decorative text; a static rule
  list that cannot be rearranged.
- Parameters: grammar, reading directions, conjunction support, precedence and
  parsing order.
- Evidence: [Baba Is You decomposition](../games/a-f/baba-is-you.md).
- Novelty: not assessed.

## SYS-018 — Active-rule property rebinding

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when the parsed rule set changes, the system automatically adds
  or removes the declared mechanical properties from every object of the rule's
  subject class.
- Includes: dynamically applying or withdrawing `YOU`, `PUSH`, `STOP` and
  `WIN` properties in Baba Is You.
- Excludes: transforming one noun class into another; a property permanently
  encoded in an object's class; the player's movement of word blocks.
- Parameters: property vocabulary, simultaneous rules, negation, precedence
  and effect timing.
- Evidence: [Baba Is You decomposition](../games/a-f/baba-is-you.md).
- Novelty: not assessed.

## SYS-019 — Ordered execution of committed hostile intents

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after the player phase ends, surviving hostile units
  automatically execute their previously displayed attacks in a disclosed
  order against the board state that exists at each execution step.
- Includes: Into the Breach Vek attacks and Fights in Tight Spaces primed
  attacks resolving after the player has had the opportunity to disrupt their
  targets, positions or ability to act.
- Excludes: an opposing human choosing a move; an undisclosed enemy action;
  the earlier selection and display of the hostile intent.
- Parameters: execution order, cancellation conditions, target persistence and
  friendly-fire rules.
- Evidence: [Into the Breach decomposition](../games/g-l/into-the-breach.md)
  and [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md).
- Novelty: not assessed.

## SYS-020 — Attack-induced displacement and collision resolution

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an ability with a displacement effect automatically shifts its
  target along the declared vector and applies any collision or hazardous-
  terrain consequence created by the destination.
- Includes: pushing a Vek so its telegraphed attack misses, or pushing a unit
  into another unit so both take collision damage in Into the Breach; a Bad
  North targeted ability launching units and resolving contact consequences;
  Fights in Tight Spaces push cards moving enemies into walls, lethal edges or
  another committed attack line.
- Excludes: the player's target selection; ordinary unit relocation; a push
  directly commanded through an adjacent controllable avatar.
- Parameters: vector, distance, stability exceptions, collision damage and
  terrain consequences.
- Evidence: [Into the Breach decomposition](../games/g-l/into-the-breach.md)
  and [Bad North decomposition](../games/a-f/bad-north.md), and
  [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md),
  and [Tactical Breach Wizards decomposition](../games/s-z/tactical-breach-wizards.md).
- Novelty: not assessed.

## SYS-021 — Scheduled battlefield-hazard resolution

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: a battlefield event automatically changes its declared affected
  positions at a fixed point in the round, before the next player decision.
- Includes: scheduled environmental damage or terrain change in an Into the
  Breach mission, whose affected positions may separately be visible in
  advance.
- Excludes: permanent terrain; an enemy unit's committed attack; disclosure of
  future affected positions without the automatic hazard transition itself.
- Parameters: affected positions, effect type, phase order and repetition.
- Evidence: [Into the Breach decomposition](../games/g-l/into-the-breach.md).
- Novelty: not assessed.

## SYS-022 — Marked enemy-emergence cycle

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: hostile reinforcement positions are marked one round before
  arrival; at the scheduled phase an unblocked marker introduces a hostile
  unit, while an occupied marker blocks emergence and applies its declared
  consequence.
- Includes: Into the Breach spawn tiles, where a blocking unit prevents a Vek
  from emerging and takes damage.
- Excludes: unmarked random insertion; initial deployment; a successor element
  introduced immediately after its predecessor locks.
- Parameters: marker placement, reinforcement class, blocking consequence and
  per-round spawn count.
- Evidence: [Into the Breach decomposition](../games/g-l/into-the-breach.md).
- Novelty: not assessed.

## SYS-023 — Single-step coupled directional shift

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a global direction is chosen, every eligible board element
  attempts at most one position of movement along its parallel line, with
  compatible leading collisions resolved during that same step.
- Includes: one Threes swipe moving each movable card by one grid cell rather
  than compressing the row or column to the boundary.
- Excludes: maximal line compression; moving one independently selected piece;
  time-driven repeated motion.
- Parameters: direction set, step distance, synchronous order and blocked-line
  handling.
- Evidence: [Threes decomposition](../games/s-z/threes.md).
- Novelty: not assessed.

## SYS-024 — Visible supplied-sequence advance

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: consuming the first element of a visible ordered supply shifts
  every retained previewed element toward the head and, while underlying
  supply remains, introduces a newly selected or revealed element at the
  preview tail.
- Includes: advancing and replenishing Pipe Dream's pipe dispenser after each
  placement; promoting Dorfromantik's next tile after the current tile is
  committed.
- Excludes: introducing one successor directly as the new active falling
  element; an unordered hand; insertion onto the playfield itself.
- Parameters: preview depth, underlying supply model, refill timing and
  successor generator.
- Evidence: [Pipe Mania decomposition](../games/m-r/pipe-mania.md) and
  [Dorfromantik decomposition](../games/a-f/dorfromantik.md).
- Novelty: not assessed.

## SYS-025 — Time-driven directed flow propagation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after a real-time delay, a system-controlled flow repeatedly
  advances from its current tile through port-compatible placed tiles until no
  valid continuation remains.
- Includes: Pipe Dream Flooz leaving the start piece, filling connected pipe
  sections and ending at an open end, incompatible section or boundary.
- Excludes: a player drawing the route; an instantaneous connectivity check;
  gravity applied to a falling rigid element.
- Parameters: start delay, propagation speed, fill duration and stop condition.
- Evidence: [Pipe Mania decomposition](../games/m-r/pipe-mania.md).
- Novelty: not assessed.

## SYS-026 — Draw-to-hand replacement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after held cards are played or discarded, the system removes
  them from the hand and reveals cards from the top of the existing draw pile
  until the current hand reaches its allowed size or the pile is exhausted.
- Includes: Balatro refilling the visible hand after either commit mode.
- Excludes: player selection of replacement identities; generating a new
  random element after every action; drawing from an unordered infinite pool.
- Parameters: hand size, draw count, deck-exhaustion rule and destination of
  committed cards.
- Evidence: [Balatro decomposition](../games/a-f/balatro.md).
- Novelty: not assessed.

## SYS-027 — Highest-precedence pattern classification

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system tests a committed element subset against a declared
  hierarchy of overlapping patterns and assigns the highest-precedence pattern
  it satisfies.
- Includes: classifying played Balatro cards as Straight Flush, Four of a Kind,
  Full House, Flush, Straight and lower poker hands.
- Excludes: player-declared pattern identity; an unordered set of simultaneous
  matches that all resolve; pattern validity used only to permit an action.
- Parameters: pattern vocabulary, precedence order, subset size and wild-card
  effects.
- Evidence: [Balatro decomposition](../games/a-f/balatro.md).
- Novelty: not assessed.

## SYS-028 — Ordered additive-and-multiplicative score resolution

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a pattern is classified, the system builds base score
  components and applies eligible card and persistent modifier effects in a
  declared order, preserving the distinction between additive and
  multiplicative operations before producing the final score increment.
- Includes: Balatro applying base Chips and Mult, scoring-card effects and the
  ordered `+Chips`, `+Mult` and `XMult` effects of a fixed Joker tableau.
- Excludes: the player's card selection or modifier reordering; one flat score
  table with no order-sensitive effects; mutable rule syntax.
- Parameters: phase order, base hand values, modifier predicates, retriggers
  and arithmetic operations.
- Evidence: [Balatro decomposition](../games/a-f/balatro.md).
- Novelty: not assessed.

## SYS-029 — Time-driven service-node appearance

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: simulation time causes new supply or destination service nodes to appear at
  system-selected positions, expanding the persistent network problem without
  a placement command from the player.
- Includes: new shaped stations opening during a Mini Metro Classic session;
  new colour-coded houses and destinations appearing in Mini Motorways.
- Excludes: player-created Creative-mode stations; refilling a fixed board
  cell; revealing a node that existed in concealed current state.
- Parameters: spawn schedule, spatial distribution, node-type distribution
  and map geography.
- Evidence: [Mini Metro decomposition](../games/m-r/mini-metro.md) and
  [Mini Motorways decomposition](../games/m-r/mini-motorways.md).
- Novelty: not assessed.

## SYS-030 — Time-driven service demand arrival

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: simulation time adds independently generated visible demand
  units to existing service nodes, requiring compatible network service.
- Includes: shaped Mini Metro passengers appearing beside stations and waiting
  for transport to a station of the matching shape; pins appearing at Mini
  Motorways destinations and requesting a compatible house car.
- Excludes: a pre-existing concealed queue; demand directly placed by the
  player; the later movement of a waiting passenger.
- Parameters: arrival rate, origin and destination distributions, bursts and
  map-specific demand rules.
- Evidence: [Mini Metro decomposition](../games/m-r/mini-metro.md) and
  [Mini Motorways decomposition](../games/m-r/mini-motorways.md).
- Novelty: not assessed.

## SYS-031 — Automatic route-based passenger transport

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: assigned vehicles traverse configured routes once or repeatedly
  and automatically load, carry, transfer and unload waiting demand according
  to reachable destinations and available capacity.
- Includes: Mini Metro trains moving along lines while passengers board,
  transfer at intersecting lines and leave at a matching destination station;
  a Cosmic Express train following one committed track while aliens board and
  leave at compatible homes.
- Excludes: player steering of a vehicle; instantaneous connectivity-only
  evaluation; flow that consumes or locks the traversed route.
- Parameters: one-shot versus repeated service, vehicle speed, direction,
  dwell time, routing preference, transfer rule and pickup ordering.
- Evidence: [Mini Metro decomposition](../games/m-r/mini-metro.md) and
  [Cosmic Express decomposition](../games/a-f/cosmic-express.md).
- Novelty: not assessed.

## SYS-032 — Periodic network-capacity award and upgrade offer

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: at a fixed simulation-time boundary, the system grants mandatory
  network capacity and presents a bounded choice of additional
  infrastructure rewards before ordinary progression resumes.
- Includes: Mini Metro's end-of-week locomotive award plus a choice such as a
  line, carriage or tunnels; Mini Motorways granting road tiles and a weekly
  choice between map-eligible infrastructure upgrades.
- Excludes: continuous income; unscheduled random loot; the player's selection
  from the generated offer.
- Parameters: cadence, automatic reward, offer count and eligible reward pool.
- Evidence: [Mini Metro decomposition](../games/m-r/mini-metro.md) and
  [Mini Motorways decomposition](../games/m-r/mini-motorways.md).
- Novelty: not assessed.

## SYS-033 — Jump-triggered intervening removal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after the player commits a legal jump to an empty destination,
  the system removes the occupied element lying between source and destination
  before the next decision.
- Includes: a Peg Solitaire jump changing an `occupied–occupied–empty` triple
  to `empty–empty–occupied`.
- Excludes: capturing an occupant on the destination square; removing a freely
  selected element; clearing every element matched by a pattern.
- Parameters: jump geometry, removed position count and multi-jump grouping.
- Evidence: [Peg Solitaire decomposition](../games/m-r/peg-solitaire.md).
- Novelty: not assessed.

## SYS-034 — Placement-triggered edge and group evaluation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a tile is committed, the system classifies every new
  shared edge, joins compatible adjacent landscape components, evaluates
  affected group conditions and awards the corresponding placement or quest
  score before the next decision.
- Includes: Dorfromantik matching adjacent landscape edges, merging connected
  forests, villages, fields, water or rail groups, recognising completed
  quests and scoring perfect closures.
- Excludes: the player's tile rotation and position choice; time-driven flow
  through printed ports; merely testing whether a placement is legal without
  mutating groups or score.
- Parameters: landscape categories, group-connectivity rules, score table,
  quest predicates and evaluation order.
- Evidence: [Dorfromantik decomposition](../games/a-f/dorfromantik.md).
- Novelty: not assessed.

## SYS-035 — Earned action-supply replenishment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: satisfying a declared in-session performance condition
  automatically adds one or more future action-enabling elements to the current
  bounded supply from which ordinary actions consume.
- Includes: Dorfromantik adding tiles to the stack for completed quests and
  perfect placements; Loop Hero enemies yielding playable world cards to the
  current hand.
- Excludes: refilling a preview queue while total supply strictly decreases;
  awarding reusable infrastructure at a fixed calendar boundary; an unlimited
  creative-mode supply.
- Parameters: reward triggers, awarded quantity, insertion position and
  simultaneous-reward handling.
- Evidence: [Dorfromantik decomposition](../games/a-f/dorfromantik.md) and
  [Loop Hero decomposition](../games/g-l/loop-hero.md).
- Novelty: not assessed.

## SYS-036 — Continuous force-constrained body dynamics

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while simulation time runs, a dynamic body continuously changes
  position and velocity under forces, collisions and any remaining geometric
  constraints, including between player commands.
- Includes: Cut the Rope candy falling under gravity, swinging under intact
  rope-length constraints and continuing by momentum after a rope is cut;
  every World of Goo construction node moving under gravity, elastic links,
  collision, load and Balloon buoyancy while the whole structure deforms; Tin
  Hearts soldiers following airborne arcs, bouncing from drums and gliding
  under force-altering devices; Chell and released cubes falling, colliding and
  retaining velocity through Portal chambers; The Swapper bodies jumping,
  falling and colliding independently under local room geometry; the
  Viewfinder avatar falling, landing and colliding with original or image-
  instantiated geometry; a released Superliminal chess piece falling and
  colliding at its committed physical scale; the Manifold Garden avatar and
  eligible cubes falling, steering, colliding and landing in the selected
  gravity frame; Maquette's released golden key settling as a collidable bridge
  while the avatar walks across it.
- Excludes: grid-stepped gravity; a time-driven path traversal with no force
  integration; one discrete input followed by instantaneous completed motion.
- Parameters: gravity, mass, damping, constraint solver, collision shapes and
  simulation timestep.
- Evidence: [Cut the Rope decomposition](../games/a-f/cut-the-rope.md) and
  [World of Goo decomposition](../games/s-z/world-of-goo.md), and
  [Tin Hearts decomposition](../games/s-z/tin-hearts.md), and
  [Portal decomposition](../games/m-r/portal.md),
  [The Swapper decomposition](../games/s-z/the-swapper.md), and
  [Viewfinder decomposition](../games/s-z/viewfinder.md),
  [Fez decomposition](../games/a-f/fez.md), and
  [Superliminal decomposition](../games/s-z/superliminal.md), and
  [Manifold Garden decomposition](../games/m-r/manifold-garden.md), and
  [Maquette decomposition](../games/m-r/maquette.md).
- Novelty: not assessed.

## SYS-037 — Contact-triggered collectible acquisition

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when the designated moving gameplay body contacts a declared
  collectible, the system removes or marks it acquired and credits its
  evaluation or progression value without immediately ending the attempt.
- Includes: candy contact collecting a gold star in Cut the Rope while motion
  continues toward Om Nom; Tim contacting a required Braid puzzle piece; the
  active The Swapper body collecting a room-progress orb; a Snakebird head
  removing one required fruit before later exit activation; Inertia's ball
  removing every gem crossed without stopping its committed slide; the
  Echochrome Walker crediting an echo on contact while continuing its route.
- Excludes: the player directly selecting a collectible; mandatory destination
  contact that itself completes the level; acquiring a carried key whose later
  barrier interaction is the decision-relevant function; clearing a matched
  board group.
- Parameters: optional versus required status, collectible count, contact
  geometry, score or progression credit and persistence after later failure.
- Evidence: [Cut the Rope decomposition](../games/a-f/cut-the-rope.md) and
  [Braid decomposition](../games/a-f/braid.md), and
  [The Swapper decomposition](../games/s-z/the-swapper.md), and
  [Snakebird decomposition](../games/s-z/snakebird.md), and
  [Inertia decomposition](../games/g-l/inertia.md), and
  [The Talos Principle decomposition](../games/s-z/the-talos-principle.md), and
  [Echochrome decomposition](../games/a-f/echochrome.md).
- Novelty: not assessed.

## SYS-038 — Synchronous cyclic symbolic-program execution

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during a committed run, every programmed controller reads the
  symbol at its current temporal or spatial program position, compatible
  commands advance in one shared discrete cycle, and the programs repeat
  automatically.
- Includes: Opus Magnum arms simultaneously grabbing, dropping, rotating,
  pivoting or traversing track according to their aligned instruction rows;
  SpaceChem's red and blue waldos advancing their routed programs together,
  with sync symbols holding the earlier arrival.
- Excludes: player-issued commands during execution; one automatic response to
  one discrete board action; continuously integrated force motion.
- Parameters: cycle order, program addressing, blank-command semantics, period,
  repeat/reset rules, synchronization and simultaneous-motion rules.
- Evidence: [Opus Magnum decomposition](../games/m-r/opus-magnum.md) and
  [SpaceChem decomposition](../games/s-z/spacechem.md).
- Novelty: not assessed.

## SYS-039 — Geometry-triggered molecular transformation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when atoms with the required identities, bonds and relative
  positions occupy a placed transformation glyph during execution, the system
  deterministically changes their types, bonds, multiplicity or existence.
- Includes: Opus Magnum bonding, unbonding, calcification, duplication,
  purification and disposal glyph effects.
- Excludes: the arm motion that places atoms; equality-based collision merges;
  a player directly selecting the transformation result.
- Parameters: glyph catalogue, activation geometry, input predicate, output
  mapping and within-cycle order.
- Evidence: [Opus Magnum decomposition](../games/m-r/opus-magnum.md).
- Novelty: not assessed.

## SYS-040 — Recurrent input-source and exact-product sink processing

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a source repeatedly makes its declared input assembly available
  according to its release rule, while a sink consumes and credits only a
  delivered assembly matching its declared product schema.
- Includes: Opus Magnum reagent ports supplying molecules and product ports
  accepting successive correctly shaped products during one machine run;
  SpaceChem input instructions requesting reagents and output instructions
  accepting successive bond-graph-equivalent products; Infinifactory hatches
  emitting voxel assemblies and output areas accepting successive exact shapes.
- Excludes: random item spawning; a one-off target location that accepts any
  object; transformation performed by an intermediate glyph.
- Parameters: source timing and blockage rule, input multiplicity, output
  equivalence, required product count and port orientation.
- Evidence: [Opus Magnum decomposition](../games/m-r/opus-magnum.md) and
  [SpaceChem decomposition](../games/s-z/spacechem.md), and
  [Infinifactory decomposition](../games/g-l/infinifactory.md).
- Novelty: not assessed.

## SYS-041 — Corpse-triggered audio and frozen-scene reconstruction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after an eligible death memory is activated, the system plays a
  fixed pre-event audio interval and instantiates a navigable but temporally
  frozen spatial reconstruction of the death moment with its participants and
  geometry preserved.
- Includes: Return of the Obra Dinn's Memento Mortem transition from a corpse
  to final dialogue or sounds and the corresponding death tableau.
- Excludes: an animated replay whose state continues changing; a textual clue
  with no inspectable scene; the player's navigation within the reconstruction.
- Parameters: audio duration, frozen instant, scene bounds, indexed people and
  how newly encountered corpses become eligible.
- Evidence: [Return of the Obra Dinn decomposition](../games/m-r/return-of-the-obra-dinn.md).
- Novelty: not assessed.

## SYS-042 — Thresholded correct-record confirmation and lock-in

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when the number of complete, correct and not-yet-confirmed
  subject records reaches the current batch threshold, the system confirms
  those records together and makes their accepted contents permanent.
- Includes: Return of the Obra Dinn normally validating three correct identity-
  and-fate entries at once, with a smaller endgame threshold.
- Excludes: immediate per-field correctness feedback; confirming a whole board
  only after every entry is complete; manually submitting a chosen batch.
- Parameters: normal and endgame thresholds, correctness equivalence, required
  fields, interruption timing and post-confirmation edit policy.
- Evidence: [Return of the Obra Dinn decomposition](../games/m-r/return-of-the-obra-dinn.md).
- Novelty: not assessed.

## SYS-043 — Selected panel-view substitution

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after the player selects a valid zoom or pan affordance, the
  system replaces that panel's displayed scene with the linked nested,
  surrounding or adjacent illustration while preserving the panel container.
- Includes: a Gorogoa panel zooming through an object, backing out through a
  frame or panning into another illustrated location.
- Excludes: changing the panel's top-level slot; revealing a concealed random
  value; automatic interaction between two composed panels.
- Parameters: directed scene graph, transition duration, return edges and any
  state-dependent destinations.
- Evidence: [Gorogoa decomposition](../games/g-l/gorogoa.md).
- Novelty: not assessed.

## SYS-044 — Compatible panel-composition continuation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when two or more panels are overlaid or placed adjacently in a
  declared compatible visual relation, the system treats their depicted spaces
  or mechanisms as one temporary composition and automatically transfers or
  advances an in-world element across it.
- Includes: a Gorogoa character walking through an overlaid doorway into
  another scene, an apple crossing an aligned seam or light / motion from one
  panel activating another.
- Excludes: visual juxtaposition with no state change; the player's panel drag;
  a persistent route whose nodes were directly connected one by one.
- Parameters: composition relation, transferred element, trigger timing,
  one-way transitions and post-continuation panel state.
- Evidence: [Gorogoa decomposition](../games/g-l/gorogoa.md).
- Novelty: not assessed.

## SYS-045 — Continuous autonomous agent locomotion

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an active agent advances through level geometry on the running
  simulation clock according to fixed locomotion and collision rules, without
  requiring a player command for each movement step.
- Includes: a Walker in Lemmings moving forward, turning at blocking terrain
  and falling when support ends; individual Bad North squad members navigating
  across island geometry toward a squad destination; the Loop Hero protagonist
  advancing around a fixed circuit without movement commands; HUMANITY crowds
  walking forward through trial geometry between persistent commands; Tin
  Hearts soldiers marching until physical contact redirects them; Timelie
  actors and patrol robots traversing multi-step paths as timeline time
  advances; Braid monstars walking under authored ground-collision rules;
  tasked Pikmin travelling and carrying across live terrain; Echochrome's
  Walker advancing and turning without directional movement commands.
- Excludes: a directly navigated avatar; time-driven motion of one currently
  controlled falling piece; execution of a separately assigned specialist
  role.
- Parameters: speed, turning predicate, fall rule, collision priority and
  simultaneous-agent ordering.
- Evidence: [Lemmings decomposition](../games/g-l/lemmings.md) and
  [Bad North decomposition](../games/a-f/bad-north.md), and
  [Loop Hero decomposition](../games/g-l/loop-hero.md), and
  [HUMANITY decomposition](../games/g-l/humanity.md), and
  [Tin Hearts decomposition](../games/s-z/tin-hearts.md), and
  [Timelie decomposition](../games/s-z/timelie.md), and
  [Braid decomposition](../games/a-f/braid.md), and
  [Pikmin 4 decomposition](../games/m-r/pikmin-4.md), and
  [Echochrome decomposition](../games/a-f/echochrome.md).
- Novelty: not assessed.

## SYS-046 — Assigned-role autonomous execution

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after a player commits a behavioural role to an autonomous
  agent, the system advances the role's declared state transition and effects
  without continuous steering of the agent.
- Includes: Lemmings climbing, floating, blocking, counting down and exploding,
  building a finite bridge or excavating horizontally, diagonally or vertically.
- Excludes: the player command that assigns the role; generic walking before a
  role is assigned; automatic execution of a hostile intent committed by the
  game rather than the player.
- Parameters: eligibility, persistence, duration, terrain effect, interruption
  and post-role state.
- Evidence: [Lemmings decomposition](../games/g-l/lemmings.md).
- Novelty: not assessed.

## SYS-047 — Time-scheduled population release

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while an attempt is running, the system automatically introduces
  successive members of a supplied finite or recurring population stream at
  intervals determined by a current release cadence.
- Includes: lemmings emerging one after another from a finite waiting population
  through a trapdoor; the recurring HUMANITY stream emerging from a stage gate;
  a finite Tin Hearts troop marching successively from its opened box.
- Excludes: random enemy emergence; the introduction of one successor active
  piece only after its predecessor locks; a player-commanded unit spawn.
- Parameters: finite versus recurring population extent, population size,
  first-release delay, cadence and entry location.
- Evidence: [Lemmings decomposition](../games/g-l/lemmings.md) and
  [HUMANITY decomposition](../games/g-l/humanity.md), and
  [Tin Hearts decomposition](../games/s-z/tin-hearts.md), and
  [Tactical Breach Wizards decomposition](../games/s-z/tactical-breach-wizards.md).
- Novelty: not assessed.

## SYS-048 — Terminal-zone population accounting

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when an autonomous population member enters a declared terminal
  zone or lethal state, the system removes that agent from active play and
  updates the appropriate rescued or lost count.
- Includes: crediting a lemming that reaches the exit and removing without
  rescue credit one that dies in a hazard or fatal fall; crediting loose World
  of Goo balls extracted by a pipe while lethal spikes destroy affected Goo
  without extraction credit; filling a HUMANITY goal with entrants while falls
  receive no goal credit and may recur as later bodies; crediting Tin Hearts
  soldiers at the exit while destructive falls remain unrescued unless
  rewound; removing Pikmin killed by hazards or left unsafe at sunset while
  updating the surviving field roster without crediting them as payloads.
- Excludes: scoring a reusable passenger delivery while the vehicle continues;
  one payload contacting a receiver to complete the whole attempt; non-terminal
  damage that leaves the agent active.
- Parameters: exit zones, lethal predicates, accounting categories and whether
  removal waits for an animation.
- Evidence: [Lemmings decomposition](../games/g-l/lemmings.md) and
  [World of Goo decomposition](../games/s-z/world-of-goo.md), and
  [HUMANITY decomposition](../games/g-l/humanity.md), and
  [Tin Hearts decomposition](../games/s-z/tin-hearts.md), and
  [Pikmin 4 decomposition](../games/m-r/pikmin-4.md).
- Novelty: not assessed.

## SYS-049 — Placement-triggered elastic-link formation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when a player releases an eligible live structural node at a
  valid position, the system automatically instantiates the permitted elastic
  links between that node and nearby members of the existing force network.
- Includes: World of Goo forming the previewed strands around a placed Goo
  Ball.
- Excludes: the player's drag and release; manually drawing each link; static
  footprint placement with no automatic force-bearing connection.
- Parameters: neighbour selection, link count, rest length, stiffness and
  within-frame creation order.
- Evidence: [World of Goo decomposition](../games/s-z/world-of-goo.md).
- Novelty: not assessed.

## SYS-050 — Autonomous traversal over live structure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: loose members of a population move over the currently connected
  live structure toward a reachable extraction zone without the player
  selecting each route step.
- Includes: unused World of Goo balls roaming over Goo strands and converging
  on a suction pipe once the structure reaches it.
- Excludes: vehicles following a player-authored transit line on a schedule;
  a single payload moving under gravity alone; assigned specialist behaviour
  that transforms terrain.
- Parameters: traversal speed, path choice, attraction radius, congestion and
  extraction handoff.
- Evidence: [World of Goo decomposition](../games/s-z/world-of-goo.md).
- Novelty: not assessed.

## SYS-051 — Context-triggered autonomous combat engagement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: controlled agents automatically select and engage eligible nearby
  hostile targets according to current context and persistent combat class,
  without a player command for each approach, strike or shot.
- Includes: Bad North soldiers forming up, acquiring targets and fighting after
  a squad-level destination order; the Loop Hero protagonist automatically
  fighting enemies encountered on the circuit.
- Excludes: the player selecting an ability and target; execution of a fully
  committed hostile intent; locomotion with no combat target selection.
- Parameters: acquisition radius, class counter, stance, target priority,
  formation, attack cadence and disengagement rule.
- Evidence: [Bad North decomposition](../games/a-f/bad-north.md) and
  [Loop Hero decomposition](../games/g-l/loop-hero.md).
- Novelty: not assessed.

## SYS-052 — Carrier-mediated hostile landing

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a visible hostile carrier advances through the running scene,
  makes contact with a boundary region and automatically releases its
  transported group into active play.
- Includes: Bad North Viking longships approaching an island, landing at shore
  and disembarking their occupants.
- Excludes: a hostile appearing at an abstract marker with no carrier transit;
  initial deployment; one successor replacing a locked active piece.
- Parameters: approach path, speed, landing region, payload, contact effect,
  release order and whether occupants can be affected before landing.
- Evidence: [Bad North decomposition](../games/a-f/bad-north.md).
- Novelty: not assessed.

## SYS-053 — Placed-tile recurring encounter production

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a persistent world tile placed by the player automatically
  introduces encounter actors onto its own or nearby traversal positions
  according to a recurring time, circuit or tile-state trigger.
- Includes: a Loop Hero roadside mausoleum producing skeletons on adjacent road
  tiles and other enemy cards creating later route encounters.
- Excludes: directly placing one enemy as the player's action; releasing a
  finite waiting population; one-round marked emergence blockable by occupancy.
- Parameters: producer tile, eligible destination positions, actor class,
  cadence, occupancy cap and suppression conditions.
- Evidence: [Loop Hero decomposition](../games/g-l/loop-hero.md).
- Novelty: not assessed.

## SYS-054 — Circuit-completion difficulty escalation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when an autonomous actor completes another traversal of a closed
  route, the system increments a progression tier that strengthens or otherwise
  intensifies later encounters on subsequent circuits.
- Includes: Loop Hero enemies becoming stronger after each completed loop.
- Excludes: score increasing for distance alone; time-driven difficulty with no
  circuit boundary; one-use route completion that ends the attempt.
- Parameters: circuit counter, affected actor attributes, scaling function,
  camp-passage timing and difficulty cap.
- Evidence: [Loop Hero decomposition](../games/g-l/loop-hero.md).
- Novelty: not assessed.

## SYS-055 — Contact-triggered persistent command execution

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when an eligible autonomous agent enters a world position bearing
  a persistent instruction, the system applies that instruction's traversal or
  state behaviour to the agent while leaving the marker available for later
  agents.
- Includes: HUMANITY walkers turning, jumping or floating when they cross the
  corresponding placed ground command.
- Excludes: executing a role previously assigned to one selected agent;
  triggering a tile that creates a new actor; a one-use collectible.
- Parameters: command vocabulary, eligibility, entry direction, execution
  duration, stacking priority and marker persistence.
- Evidence: [HUMANITY decomposition](../games/g-l/humanity.md).
- Novelty: not assessed.

## SYS-056 — Geometry-conditioned collision redirection

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when an autonomous ground agent contacts an oriented physical
  routing surface, the system changes its travel direction according to the
  contacted face and then resumes its ordinary locomotion.
- Includes: a Tin Hearts soldier bouncing from an angled prism block into the
  direction determined by that block's orientation.
- Excludes: reading a symbolic command stored on the position; force-driven
  airborne motion after launch; turning at an immovable wall under generic
  locomotion rules.
- Parameters: surface geometry, incoming direction, outgoing mapping, collision
  tolerance, agent spacing and simultaneous-contact order.
- Evidence: [Tin Hearts decomposition](../games/s-z/tin-hearts.md).
- Novelty: not assessed.

## SYS-057 — Perception-triggered hostile pursuit or diversion

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a hostile patrol automatically replaces its current route when
  it perceives an eligible actor or explicit decoy stimulus, pursuing the
  perceived target and applying capture on contact where applicable.
- Includes: a Timelie robot chasing a seen girl or cat and an eligible robot
  diverting toward a deliberately scheduled cat meow.
- Excludes: resolving an already committed attack vector; selecting combat
  targets solely from proximity; scripted route change with no perception
  event.
- Parameters: stimulus classes, sight geometry, pursuit pathfinding, memory,
  distraction priority, abandonment rule and contact consequence.
- Evidence: [Timelie decomposition](../games/s-z/timelie.md).
- Novelty: not assessed.

## SYS-058 — Instruction-triggered geometry-validated molecular transformation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when a programmed controller executes a transformation command,
  the system changes eligible molecular bonds only if the required atoms occupy
  the command's fixed activation geometry.
- Includes: SpaceChem Bond or Unbond executing while eligible atoms occupy the
  reactor's bonder pads.
- Excludes: passive transformation caused solely by occupying a glyph; directly
  selecting two atoms and a result; equality-triggered collision merging.
- Parameters: instruction class, activation cells, atom eligibility, bond-order
  limits, selection priority and within-cycle resolution order.
- Evidence: [SpaceChem decomposition](../games/s-z/spacechem.md).
- Novelty: not assessed.

## SYS-059 — Bidirectional paired-aperture traversal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while two linked apertures exist, a body crossing either one's
  plane is continuously remapped to the corresponding position and orientation
  at the other aperture, which can also be traversed in the reverse direction.
- Includes: Chell or a Weighted Storage Cube entering either active Portal
  aperture and emerging from the other.
- Excludes: one-way teleport destinations; pathfinding between selected nodes;
  physical redirection caused by striking a solid angled surface.
- Parameters: aperture shape, bidirectionality, body eligibility, relative pose
  mapping, partial-body handling and collision continuity.
- Evidence: [Portal decomposition](../games/m-r/portal.md).
- Novelty: not assessed.

## SYS-060 — Portal-relative velocity reorientation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when a moving body crosses a paired portal, the system preserves
  its entry-speed contribution while rotating the velocity into the exit
  aperture's frame, so gravity-built speed can become outward or lateral
  motion.
- Includes: Portal's fling manoeuvre: falling into a floor portal and emerging
  rapidly from a wall portal toward a distant ledge.
- Excludes: ordinary gravity and collision integration; constant-speed network
  travel; a fixed launch impulse unrelated to incoming motion.
- Parameters: speed preservation, orientation transform, minimum exit speed,
  avatar air control and body-class exceptions.
- Evidence: [Portal decomposition](../games/m-r/portal.md).
- Novelty: not assessed.

## SYS-061 — Occupancy-sustained linked mechanism state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an eligible body continuously occupying a pressure region holds
  a linked mechanism in its active state, and vacating the region returns that
  mechanism to its inactive state unless another eligible body remains.
- Includes: Chell or a Weighted Storage Cube holding a Portal floor button down
  so its linked chamber door stays open; a The Swapper body maintaining a
  pressure plate while another body moves elsewhere; Superliminal's dropped
  Induction chess piece holding its linked exit open only while it remains on
  the plate.
- Excludes: a one-shot toggle that remains changed after release; a timed
  pedestal switch; contact that only collects or destroys an object.
- Parameters: eligible body classes, occupancy threshold, linked mechanisms,
  activation delay, multi-body logic and release behaviour.
- Evidence: [Portal decomposition](../games/m-r/portal.md),
  [The Swapper decomposition](../games/s-z/the-swapper.md), and
  [Superliminal decomposition](../games/s-z/superliminal.md).
- Novelty: not assessed.

## SYS-062 — Rewind-exempt forward-time evolution

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while the player restores ordinary world history backward, a
  visibly designated entity retains its current state and continues resolving
  in its own forward-time direction instead of loading an earlier state.
- Includes: Braid's green key remaining carried, green door remaining open, or
  green platform / enemy continuing forward while Tim and ordinary entities
  rewind.
- Excludes: every entity restoring together under generic rewind; an object
  frozen in place while time is paused; permanent meta-progression outside the
  active puzzle world.
- Parameters: immune entity classes, continued-motion rule, interaction with
  rewinding bodies, boundary collisions and state retained across room reset.
- Evidence: [Braid decomposition](../games/a-f/braid.md).
- Novelty: not assessed.

## SYS-063 — Carried-key barrier consumption

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an eligible actor that contacts a free or transferred key gains
  it as carried state, and later contact with a compatible locked barrier
  consumes that key while changing the barrier to its open state.
- Includes: Tim taking a Braid key from the world or a defeated enemy and using
  it to unlock a gate.
- Excludes: collecting an objective token for progression credit; directly
  selecting an inventory item and target; holding a mechanism active only
  while a body occupies a pressure region.
- Parameters: carrier classes, key-door matching, transfer trigger, key count,
  barrier persistence and interaction with rewind immunity.
- Evidence: [Braid decomposition](../games/a-f/braid.md).
- Novelty: not assessed.

## SYS-064 — Direction-sensitive avatar-enemy contact resolution

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: contact between a directly navigated avatar and a hostile ground
  agent resolves differently by relative approach: a qualifying top impact
  removes the hostile and rebounds the avatar, while unsafe side or underside
  contact defeats or disables the avatar.
- Includes: Tim stomping a Braid monstar from above versus being defeated by
  lateral contact.
- Excludes: symmetric collision damage; tactical attacks selected as explicit
  commands; automatic combat based only on nearby target choice.
- Parameters: contact-normal threshold, rebound velocity, hostile eligibility,
  carried-item transfer, avatar failure state and simultaneous contacts.
- Evidence: [Braid decomposition](../games/a-f/braid.md).
- Novelty: not assessed.

## SYS-065 — Switch-directed platform traversal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a linked platform automatically moves through a fixed authored
  trajectory while world time advances, with an activated switch starting,
  stopping or reversing its current traversal state.
- Includes: Braid levers directing moving platforms that carry Tim or enemies
  to otherwise unreachable geometry.
- Excludes: a platform moved directly by the avatar; autonomous pathfinding;
  a pressure plate that only changes a door state while occupied.
- Parameters: trajectory, speed, switch-state mapping, endpoint behaviour,
  rider attachment, collision and rewind affinity.
- Evidence: [Braid decomposition](../games/a-f/braid.md).
- Novelty: not assessed.

## SYS-066 — Context-derived follower task execution

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after followers are dispatched onto a target, the system derives
  their work mode from that target and advances the associated attack, digging,
  construction or transport behaviour without continuous steering.
- Includes: Pikmin 4 followers automatically fighting a creature, breaking or
  building an obstacle, digging, or preparing to carry the assigned object.
- Excludes: executing a separately selected abstract role; generic following
  before task assignment; reading a persistent command from a world cell.
- Parameters: target classes, inferred task, worker type eligibility, work
  rate, interruption, completion state and post-task idling.
- Evidence: [Pikmin 4 decomposition](../games/m-r/pikmin-4.md).
- Novelty: not assessed.

## SYS-067 — Strength-threshold cooperative carrying

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an assigned world object begins autonomous transport only when
  the summed carrying strength of attached eligible followers meets its
  declared weight, after which the carrier group jointly follows a route toward
  its receiver and additional strength may increase speed.
- Includes: several Pikmin or sufficiently trained Oatchi carrying a Pikmin 4
  treasure or castaway back to the S.S. Beagle.
- Excludes: one avatar directly holding an object; fixed-capacity vehicle
  boarding; multiple bodies jointly pushing an object through collision alone.
- Parameters: object weight, per-carrier strength, maximum carriers, speed
  function, route selection, hazard response and carrier replacement.
- Evidence: [Pikmin 4 decomposition](../games/m-r/pikmin-4.md).
- Novelty: not assessed.

## SYS-068 — Base intake of transported world object

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when an eligible carried world object reaches the operational
  base receiver, the system removes it from the field, credits its declared
  rescue or resource value and releases its carriers from the transport task.
- Includes: the S.S. Beagle accepting a Pikmin 4 treasure for Sparklium or a
  castaway for rescue progress.
- Excludes: accounting for the carrier population itself entering an exit;
  one physics payload contact that completes the entire attempt; recurrent
  passenger delivery while the passenger remains reusable.
- Parameters: receiver mobility, target classes, credited value, intake delay,
  carrier release state and whether collection persists across rewind points.
- Evidence: [Pikmin 4 decomposition](../games/m-r/pikmin-4.md).
- Novelty: not assessed.

## SYS-069 — Aligned container-boundary transfer

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when a commanded actor or pushed object legally crosses an open
  container side, the system transfers it between the corresponding aligned
  edge positions of the container's parent and child grids while preserving
  entity identity.
- Includes: Patrick or a pushed box entering an enterable Patrick's Parabox box
  through its centre side cell, and emerging through an interior boundary into
  the corresponding parent-side destination.
- Excludes: changing only a camera view; traversing a fixed paired aperture in
  one continuous space; teleporting to an unrelated authored destination.
- Parameters: entry and exit alignment, coordinate mapping, source and
  destination clearance, traversable entity classes and view-focus update.
- Evidence: [Patrick's Parabox decomposition](../games/m-r/patricks-parabox.md).
- Novelty: not assessed.

## SYS-070 — Recursive containment-graph reparenting

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when one movable container crosses another container's boundary,
  the system changes the moved container's parent relation while preserving its
  identity, internal grid and contained entities, including valid cyclic self-
  containment relations.
- Includes: pushing a Patrick's Parabox box into or out of another box and
  moving a self-containing box under a different outer parent.
- Excludes: nesting a visual panel layer; transferring an ordinary non-container
  object through a boundary; duplicating a container or generating new content
  at every recursively rendered depth.
- Parameters: permitted containment cycles, parent replacement, content
  preservation, rendering depth, reference identity and invalid-cycle handling.
- Evidence: [Patrick's Parabox decomposition](../games/m-r/patricks-parabox.md).
- Novelty: not assessed.

## SYS-071 — Local-resolution divergence under shared body input

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: one movement input is offered to every member of a synchronized
  body set, but each body resolves it against its own local support, collision
  and gravity state, allowing their positions and trajectories to diverge.
- Includes: all The Swapper bodies attempting the same horizontal movement or
  jump while walls, ledges and different supports stop or redirect them
  independently.
- Excludes: autonomous pathfinding; perfectly rigid multi-object translation;
  turn-based movement of one selected actor; merely copying an animation.
- Parameters: synchronized input channels, per-body collision order, grounded
  predicate, gravity frame, simultaneous contacts and update order.
- Evidence: [The Swapper decomposition](../games/s-z/the-swapper.md).
- Novelty: not assessed.

## SYS-072 — Clone-body removal with capacity recovery

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when a non-active created body meets a declared removal trigger,
  the system deletes that body and immediately restores the finite capacity
  consumed by its creation.
- Includes: a The Swapper clone being reclaimed by body contact, destroyed by
  a lethal fall or removed by a white cleansing light, making its clone slot
  available again.
- Excludes: permanent follower death; manually returning a reserve unit;
  merging two valued pieces into a third; resetting the entire puzzle room.
- Parameters: removal triggers, active-body exception, capacity refund timing,
  carried state, simultaneous removals and terminal-body failure.
- Evidence: [The Swapper decomposition](../games/s-z/the-swapper.md).
- Novelty: not assessed.

## SYS-073 — Commit-time panel path validation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when a completed candidate path reaches an eligible terminal and
  is submitted, the system evaluates the path topology and every active panel
  clue conjunctively, accepting and retaining only a solution that satisfies
  the complete rule set.
- Includes: The Witness accepting a start-to-end trace whose simple path and
  black / white square regions are valid, while rejecting a terminal trace
  that violates either requirement.
- Excludes: continuously breaking a path at the moment it overlaps another;
  checking independent cell entries before a complete answer exists; revealing
  or constructing a valid path automatically.
- Parameters: submission trigger, rule catalogue, evaluation order, accepted-
  path persistence, linked output, rejection reset and simultaneous violations.
- Evidence: [The Witness decomposition](../games/s-z/the-witness.md).
- Novelty: not assessed.

## SYS-074 — Authoritative map-to-world topology propagation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a valid map-fragment rearrangement, the system immediately
  rebuilds the traversable world so each fragment's represented region,
  contents and boundary connections occupy the new map topology while
  preserving fragment-relative entity positions.
- Includes: Carto moving or rotating a map piece and causing that land region,
  its paths and occupants to appear in the corresponding new world adjacency.
- Excludes: a map that only reports an independently fixed world; temporary
  visual-panel composition that transfers one depicted element; camera-only
  relocation; loading a separately authored level from a menu.
- Parameters: propagation timing, fragment-local coordinate transform, entity
  anchoring, disconnected components, avatar-bearing fragment and transition
  presentation.
- Evidence: [Carto decomposition](../games/a-f/carto.md).
- Novelty: not assessed.

## SYS-075 — Perspective image-to-world spatial instantiation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: committing a posed two-dimensional source image reconstructs its
  represented contents as solid, interactive three-dimensional world geometry
  transformed by the image plane's current perspective, scale and orientation.
- Includes: Viewfinder turning a placed photograph of a bridge, room, staircase
  or teleporter into geometry that the avatar can enter, walk on and interact
  with at the committed pose.
- Excludes: viewing a passive picture; loading a separately authored level;
  joining two fixed portal endpoints; relocating persistent map regions while
  retaining their identities; temporary depicted-panel continuation.
- Parameters: source depth representation, plane pose, scale transform,
  collision generation, gravity frame, object interactivity and seam handling.
- Evidence: [Viewfinder decomposition](../games/s-z/viewfinder.md).
- Novelty: not assessed.

## SYS-076 — Projection-volume destructive world overwrite

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when a perspective image is committed, pre-existing world
  geometry and objects inside the placement's projected replacement volume are
  removed or cut away rather than merely hidden behind the new image content.
- Includes: Viewfinder deleting walls, floors, batteries or even the level
  teleporter that lie behind a stamped photograph's projected footprint.
- Excludes: non-destructive visual occlusion; moving displaced geometry into
  storage; replacing one same-channel portal endpoint; separating a retained
  illustrated foreground from its underlay.
- Parameters: projection volume, clipping boundary, protected materials,
  partial-object cutting, resolution order and rewind restoration.
- Evidence: [Viewfinder decomposition](../games/s-z/viewfinder.md).
- Novelty: not assessed.

## SYS-077 — Discrete contact-driven conveyor transport

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during an automatic discrete run, persistent oriented conveyor
  components repeatedly apply translation to contacting material assemblies;
  compatible motion advances the assembly while obstruction or unresolved
  opposed transport leaves it stalled.
- Includes: Infinifactory conveyor voxels moving recurring input assemblies
  through a Training Routine 1 factory toward the output area.
- Excludes: a symbolic controller reading commands from a program tape; a
  player directly moving the material; continuously integrated rigid-body
  force motion; an autonomous vehicle following one authored route.
- Parameters: contact faces, cycle order, assembly rigidity, direction
  priority, opposed-force resolution, blockage and input cadence.
- Evidence: [Infinifactory decomposition](../games/g-l/infinifactory.md).
- Novelty: not assessed.

## SYS-078 — Orientation-dependent elongated-body displacement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after one commanded contact with an elongated rigid object, the
  system selects translation without face change for axial contact or one-cell
  rolling with a top / bottom face swap for lateral contact.
- Includes: a Stephen's Sausage Roll sausage sliding when pushed at an end and
  rolling when contacted from either long side.
- Excludes: rotating an object directly in place; uniform one-cell crate
  translation; continuously integrated rigid-body torque; automatic conveyor
  transport independent of object orientation.
- Parameters: object footprint, contact axis, displacement, face permutation,
  destination support and obstruction handling.
- Evidence: [Stephen's Sausage Roll decomposition](../games/s-z/stephens-sausage-roll.md).
- Novelty: not assessed.

## SYS-079 — Contact-triggered per-surface cooking

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when an identified physical face of a multi-face object contacts
  an active processing surface, the system records the processed state only on
  that face and preserves every other face's state.
- Includes: a Stephen's Sausage Roll grill cooking the contacting top-or-bottom
  face of each sausage cell independently.
- Excludes: marking the whole object complete on destination contact;
  processing every face simultaneously; repeated contact that has no state;
  passive visual recolouring.
- Parameters: face identity set, contact geometry, processing surface, update
  timing, visual mark and repeat-contact consequence.
- Evidence: [Stephen's Sausage Roll decomposition](../games/s-z/stephens-sausage-roll.md).
- Novelty: not assessed.

## SYS-080 — Consumable-terrain bounded object growth

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when one movable object enters a consumable terrain state, the
  terrain is depleted and that same object advances one step along a finite
  ordered state ladder, stopping at an absorbing maximum.
- Includes: a small A Good Snowman Is Hard to Build snowball becoming medium,
  or a medium one becoming large, when pushed onto fresh snow while that cell
  becomes bare.
- Excludes: replacing two colliding objects with one output; appending a new
  persistent body segment; unbounded experience progression; cosmetic scaling
  without a decision-relevant state change.
- Parameters: terrain state, object state ladder, maximum state, depletion
  timing, steps advanced per contact and behaviour at maximum.
- Evidence: [A Good Snowman Is Hard to Build decomposition](../games/a-f/a-good-snowman-is-hard-to-build.md).
- Novelty: not assessed.

## SYS-081 — Push-resolved ordered stack transfer

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: resolving a push transfers one exposed movable object between a
  ground position and a vertical stack relation, preserving its identity and
  ordered state while the remaining stack stays in place.
- Includes: placing a smaller A Good Snowman Is Hard to Build snowball atop a
  larger top ball, and knocking the top ball of an incomplete stack into the
  clear cell beyond the pushing agent.
- Excludes: translating every object in a contiguous chain; merging colliding
  objects into one; moving an entire rigid stack; freely transferring a buried
  object.
- Parameters: source stack depth, target compatibility, exposed object,
  knock-off direction, landing-cell clearance and completed-stack lock.
- Evidence: [A Good Snowman Is Hard to Build decomposition](../games/a-f/a-good-snowman-is-hard-to-build.md).
- Novelty: not assessed.

## SYS-082 — Endpoint-led ordered body propagation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a legal displacement of the currently leading endpoint,
  every persistent segment of one articulated controlled body moves into its
  predecessor's immediately prior position while segment order and
  connectivity remain fixed.
- Includes: one Snakebird cardinal input advancing the head one cell and making
  the complete tail follow the preceding body path; forward movement in Can of
  Wormholes propagating the ordered worm from the currently leading endpoint.
- Excludes: translating one rigid multi-cell footprint unchanged; autonomous
  followers pathfinding toward a leader; shifting a contiguous row of
  independently movable objects; continuously integrated flexible-body motion.
- Parameters: segment order, adjacency topology, leading endpoint, endpoint
  step, follower update order, self-collision rule and behaviour under growth.
- Evidence: [Snakebird decomposition](../games/s-z/snakebird.md) and
  [Can of Wormholes decomposition](../games/a-f/can-of-wormholes.md).
- Novelty: not assessed.

## SYS-083 — Consumable-contact persistent segment growth

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: contact with a consumable target removes that target and appends
  one persistent ordered segment to a moving articulated body, increasing its
  future collision, reach and support footprint.
- Includes: a Snakebird eating one fruit and gaining one permanent tail segment.
- Excludes: advancing one object on a bounded size ladder; collision-merging two
  objects; increasing a scalar score without new spatial occupancy; temporary
  visual stretching.
- Parameters: contact locus, segments added, append position, target removal,
  maximum length and interaction with movement resolution.
- Evidence: [Snakebird decomposition](../games/s-z/snakebird.md).
- Novelty: not assessed.

## SYS-084 — Post-input unsupported rigid-shape fall

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after one discrete commanded transition, the system tests whether
  any cell of a multi-cell body has valid external support and, if none does,
  translates its complete retained shape vertically until supported or lost.
- Includes: an unsupported Snakebird falling as one unchanged ordered body
  after head movement and any fruit growth resolve.
- Excludes: continuously integrated gravity and velocity; one active piece
  descending on a real-time clock; autonomous locomotion; falling individual
  segments independently.
- Parameters: gravity direction, valid support classes, body footprint,
  collision during descent, fall distance and terminal boundary.
- Evidence: [Snakebird decomposition](../games/s-z/snakebird.md).
- Novelty: not assessed.

## SYS-085 — Exhaustive-collection exit activation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: removing or crediting the final member of a declared finite
  target set changes one fixed exit from unavailable to eligible before the
  next player decision.
- Includes: the last Snakebird fruit activating the level's rainbow exit.
- Excludes: collecting an item that itself completes the level; opening a gate
  after one specific key; reaching a score threshold; a permanently active exit.
- Parameters: target set, credit predicate, exit identity, activation timing,
  permanence and behaviour for already-overlapping actors.
- Evidence: [Snakebird decomposition](../games/s-z/snakebird.md).
- Novelty: not assessed.

## SYS-086 — Complete-section phrase-assignment validation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when every blank in one structured phrase section is occupied,
  the system compares the complete assignment with an accepted account and
  reports section correctness without disclosing every slot's correct value.
- Includes: The Case of the Golden Idol checking a completed prologue identity,
  location or event Scroll panel and accepting the case when the mandatory
  Scroll is correct.
- Excludes: continuous legality feedback while one slot is edited; validating
  a traced geometric path; waiting until several independently correct subject
  records coexist before confirming and locking them.
- Parameters: completeness trigger, accepted phrase equivalents, coarse close-
  answer indicator, required section, feedback timing and revision after
  rejection.
- Evidence: [The Case of the Golden Idol decomposition](../games/s-z/the-case-of-the-golden-idol.md).
- Novelty: not assessed.

## SYS-087 — Turn-boundary hand turnover

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: at the boundary between successive player phases, the system
  discards the current hand, draws a new bounded hand from the persistent deck
  and recycles the discard pile when the draw pile cannot supply it.
- Includes: Fights in Tight Spaces replacing played and unplayed cards with the
  next turn's hand after hostile resolution.
- Excludes: drawing replacements immediately after every committed card;
  retaining arbitrary unplayed cards across the ordinary turn boundary;
  selecting which card identities enter the new hand.
- Parameters: hand size, discard timing, draw timing, shuffle trigger, retained
  cards and guaranteed-card modifiers.
- Evidence: [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md).
- Novelty: not assessed.

## SYS-088 — Exact draft-state consequence simulation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: on request during an uncommitted tactical turn, the system
  deterministically resolves the current draft's hostile attacks and immediate
  world consequences as a reversible simulation, recomputing them after draft
  revision.
- Includes: Tactical Breach Wizards Foresee resolving current hostile targets,
  damage, displacement and defeat consequences before commit.
- Excludes: irreversible execution of attacks committed before planning; a
  probability estimate; route-only projection; passive target indicators with
  no complete consequence simulation.
- Parameters: simulated phase depth, state fidelity, execution order, failure
  cutoff, recomputation timing and presentation speed.
- Evidence: [Tactical Breach Wizards decomposition](../games/s-z/tactical-breach-wizards.md).
- Novelty: not assessed.

## SYS-089 — Immediate concealed-class truth adjudication

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after the player asserts a class for one concealed position, the
  system immediately compares it with the position's fixed truth, permanently
  accepts a correct assertion or rejects an incorrect one and records an error
  before another assertion is accepted.
- Includes: Hexcells Infinite accepting a correct blue / black classification
  and counting a wrong mouse-button assertion as a mistake.
- Excludes: validating only after a complete assignment is submitted; allowing
  an incorrect tentative value to persist; a reveal command with no asserted
  class; terminal failure from selecting one hazard.
- Parameters: accepted-state rendering, error counter, score penalty, feedback
  detail and whether rejection explicitly exposes the opposite class.
- Evidence: [Hexcells Infinite decomposition](../games/g-l/hexcells-infinite.md).
- Novelty: not assessed.

## SYS-090 — Ordered prepared-attack queue execution

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after queue activation, the system resolves every prepared attack
  tile in its current order as one uninterrupted player action, applying each
  attack to the state produced by its predecessors.
- Includes: Shogun Showdown executing up to three queued tiles from bottom to
  top before hostile response.
- Excludes: the player's queue editing or activation command; hostile intents
  executing after a planning phase; one attack resolving immediately when
  selected.
- Parameters: execution direction, maximum length, retargeting from updated
  state, cancellation, death handling and animation speed.
- Evidence: [Shogun Showdown decomposition](../games/s-z/shogun-showdown.md).
- Novelty: not assessed.

## SYS-091 — Shared turn-clock state advancement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after one turn-costing player action resolves, the system advances
  every surviving hostile unit by one currently declared behavioural step and
  advances each cooldown-governed player ability by one recharge step before
  the next input.
- Includes: Shogun Showdown enemies moving, queueing or attacking after the
  player's turn while used tiles recharge one cooldown pip.
- Excludes: an opposing player choosing a reply; executing a whole set of
  hostile attacks committed before a bounded player phase; continuous real-
  time cooldown progression.
- Parameters: responding units, ordering, zero-time player actions, cooldown
  increment, spawn timing and terminal checks.
- Evidence: [Shogun Showdown decomposition](../games/s-z/shogun-showdown.md).
- Novelty: not assessed.

## SYS-092 — Automatic compatible house-car round trip

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a demand marker automatically dispatches one available vehicle
  attached to a compatible origin, after which that vehicle follows the
  current road graph to the requesting node, clears one demand unit and
  returns to its own origin.
- Includes: a Mini Motorways destination pin causing an available same-colour
  house car to drive to that destination, collect the pin and return home.
- Excludes: passengers boarding a route vehicle; player steering; assigning a
  reusable vehicle among routes; instantaneous connectivity evaluation.
- Parameters: origin choice, route choice, trip reservation, parking capacity,
  dispatch priority and rerouting after edits.
- Evidence: [Mini Motorways decomposition](../games/m-r/mini-motorways.md).
- Novelty: not assessed.

## SYS-093 — Automatic weighted origin-destination road traffic

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system repeatedly introduces vehicles at authored road
  endpoints according to declared destination weights, chooses a currently
  connected directed route and advances each vehicle toward its required exit
  without direct steering.
- Includes: Freeways cars entering from a road sign or building, following the
  player-drawn interchange to one of its declared destinations and leaving the
  level boundary.
- Excludes: one demand marker dispatching a car attached to a compatible house;
  passengers boarding a scheduled route vehicle; directly steered cars.
- Parameters: demand weights, spawn cadence, route-choice rule, destination
  representation and handling of unreachable destinations.
- Evidence: [Freeways decomposition](../games/a-f/freeways.md).
- Novelty: not assessed.

## SYS-094 — Bounded road-traffic congestion evaluation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during a bounded traffic evaluation, multiple automatic vehicles
  occupy finite road space, so close following, intersections and merges reduce
  measured throughput and can form a persistent queue even though the graph
  remains connected.
- Includes: traffic backing up at a Freeways merge during the simulated day and
  reducing the network's speed / efficiency result.
- Excludes: abstract demand accumulating at an unserved node without vehicles
  occupying the connecting graph; one vehicle blocked only by a static wall;
  passenger capacity inside a vehicle.
- Parameters: evaluation horizon, vehicle footprint, following distance, merge
  priority, collision handling, lane count, acceleration and jam threshold.
- Evidence: [Freeways decomposition](../games/a-f/freeways.md).
- Novelty: not assessed.

## SYS-095 — Tail-directed straight reverse propagation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when the player reverses an ordered articulated body, its tail
  becomes the advancing endpoint and moves along its current outward direction,
  after which the remaining segments follow from that end instead of replaying
  the body's historical path.
- Includes: reversing a Can of Wormholes worm so the tail extrudes straight
  from its present orientation and the ordered body follows behind it.
- Excludes: ordinary forward propagation from a fixed head; reversing one
  rigid object's facing; scrubbing recorded movement history; translating an
  unchanged multi-cell footprint.
- Parameters: reverse-input mapping, current tail orientation, endpoint-role
  persistence, segment update order and collision handling.
- Evidence: [Can of Wormholes decomposition](../games/a-f/can-of-wormholes.md).
- Novelty: not assessed.

## SYS-096 — Direction-conditioned maximal log displacement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after one adjacent push on an elongated cylindrical object, the
  system resolves a displacement mode from the contact axis: an end push tips
  the object by one footprint transition, while a side push rolls it along its
  perpendicular axis until the first blocker or accepting boundary.
- Includes: tipping an A Monster's Expedition log from an end and rolling it
  sideways without another input until a rock, stump or water stops it.
- Excludes: a one-cell crate push; one-cell lateral rolling that exposes a
  tracked face; continuously integrated rigid-body physics; direct in-place
  rotation; automatic transport independent of a player's push.
- Parameters: rigid footprint, end and side contact regions, tip displacement,
  rolling axis, stopping objects, accepting boundaries and collision order.
- Evidence: [A Monster's Expedition decomposition](../games/a-f/a-monsters-expedition.md).
- Novelty: not assessed.

## SYS-097 — Water-settled object becomes traversable bridge

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when a required movable rigid object enters an eligible water
  gap in an accepted orientation, the system fixes it in that gap and adds a
  traversable connection between the previously separated land cells.
- Includes: an A Monster's Expedition log settling lengthwise across a one-cell
  water gap so the monster can walk over it to the connected island.
- Excludes: spending an abstract bridge inventory; drawing a road over water;
  editing an authoritative map representation; a floating object that remains
  freely movable; decorative water contact without a new traversal edge.
- Parameters: water-gap width, accepted object orientation and length,
  settlement pose, resulting traversal edges and persistence.
- Evidence: [A Monster's Expedition decomposition](../games/a-f/a-monsters-expedition.md).
- Novelty: not assessed.

## SYS-098 — Required-object fire contact consumes and completes

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when the designated required object enters a fixed fire receiver,
  the system irreversibly consumes that object and immediately credits the
  bounded puzzle rather than preserving it as an ordinary placed object.
- Includes: the belongings crate entering the bonfire in Bonfire Peaks and
  completing `Burn Your Belongings` as the crate burns.
- Excludes: repeatable surface heating; an object destroyed only as failure;
  delivering an intact payload to a receiver; decorative fire contact.
- Parameters: designated object class, receiver cells, entry direction,
  consumption timing, completion timing and treatment of other objects.
- Evidence: [Bonfire Peaks decomposition](../games/a-f/bonfire-peaks.md).
- Novelty: not assessed.

## SYS-099 — Synchronous automatic rail-car traversal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after one explicit run command, every free rail vehicle advances
  automatically on the configured track under one shared movement clock,
  follows the currently selected junction continuation and couples when it
  reaches an eligible receiver approach.
- Includes: all numbered Railbound carriages starting together, following the
  authored rail layout and coupling behind the locomotive when eligible.
- Excludes: recurrent passenger service; individually steered vehicles;
  continuous traffic sampled for throughput; one vehicle traversing one path.
- Parameters: movement cadence, junction selection, start offsets, receiver
  approach, coupling transition and treatment of an already coupled vehicle.
- Evidence: [Railbound decomposition](../games/m-r/railbound.md).
- Novelty: not assessed.

## SYS-100 — Card-parametrised staged ball traversal on heightfield

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after one held movement card and a direction are committed, the
  system advances one ball through the card's declared sequence of grid-step
  travel stages, applying fixed support, barrier and elevation geometry until
  the ball settles, leaves the course or enters its receiver.
- Includes: a Golf Peaks World 1 roll card moving the ball an exact nominal
  distance while authored walls and slopes reject or redirect its route.
- Excludes: continuous force-integrated ball motion; freely commanded avatar
  navigation; a card that only changes a statistic; autonomous rail service.
- Parameters: stage types and distances, direction domain, elevation bands,
  wall response, slope continuation, boundary response and receiver priority.
- Evidence: [Golf Peaks decomposition](../games/g-l/golf-peaks.md).
- Novelty: not assessed.

## SYS-101 — Later footprint overwrites addressed cell contents

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after a legal placement, every non-empty block in the incoming
  typed footprint simultaneously replaces the current visible content of its
  corresponding addressed cell, while all cells outside the footprint retain
  their prior state.
- Includes: a newly placed inbento food piece flattening and replacing earlier
  ingredients in every Chapter 1 bento cell it covers.
- Excludes: rejecting overlap as collision; accumulating two simultaneously
  active layers; merging compatible values; deleting an entire completed line;
  placing only into empty cells.
- Parameters: empty footprint blocks, replacement atomicity, identity domain,
  treatment of covered empty cells and objective-check timing.
- Evidence: [inbento decomposition](../games/g-l/inbento.md).
- Novelty: not assessed.

## SYS-102 — Component-wide class replacement and coalescence

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after a seed-and-class command, the system atomically replaces
  the class of every cell in the seed's maximal connected current-class
  component, then coalesces it with all adjacent components of the replacement
  class for future actions.
- Includes: one KAMI move recolouring a complete orthogonally connected paper
  region and joining it to every touching region of the selected colour.
- Excludes: replacement by an incoming shaped footprint; deletion followed by
  gravity; collision-triggered pair merging; visual recolouring with no change
  to future component selection.
- Parameters: neighbourhood topology, component maximality, merge transitivity,
  replacement atomicity and animation timing.
- Evidence: [KAMI decomposition](../games/g-l/kami.md).
- Novelty: not assessed.

## SYS-103 — Linked hook retraction with swept obstruction adjudication

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a trigger command, the system retracts every currently
  linked line-and-hook mechanism toward that trigger, removes each one that
  completes its swept path, and rejects the attempt when any moving hook or
  line collides with a still-present mechanism.
- Includes: one HOOK button withdrawing one or several attached lines and
  hooks, or producing the visible collision-and-reset response when their
  paths remain obstructed.
- Excludes: player-dragged line removal; route construction; deletion without
  swept motion; simultaneous vehicle travel through reusable infrastructure.
- Parameters: linked set, retraction direction and speed, swept geometry,
  collision classes, removal timing and failure-reset timing.
- Evidence: [HOOK decomposition](../games/g-l/hook.md).
- Novelty: not assessed.

## SYS-104 — Duplicate-aware positional and residual-match scoring

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a complete ordered-symbol hypothesis is committed, the
  system first matches equal symbols at equal positions, removes those matched
  occurrences, then matches equal remaining symbols without position so no
  target occurrence can be credited more than once; the result may be
  aggregated or assigned back to hypothesis positions.
- Includes: Mastermind awarding aggregate exact and misplaced indicators;
  Wordle assigning exact, present-elsewhere or exhausted feedback to guessed
  positions after the same duplicate-safe matching pass.
- Excludes: independent per-position equality without residual occurrence
  accounting; generic similarity scoring that may double-count one target
  symbol; unordered identity overlap that does not prioritise exact positions.
- Parameters: sequence length, symbol multiset, exact-match priority,
  indicator classes, aggregate versus position-addressed disclosure, ordering
  of displayed indicators and terminal all-exact result.
- Evidence: [Mastermind decomposition](../games/m-r/mastermind.md) and
  [Wordle decomposition](../games/s-z/wordle.md).
- Novelty: not assessed.

## SYS-105 — Hidden orthogonal ray interaction resolution

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: from one selected perimeter entry, the system advances a hidden
  ray orthogonally through a fixed concealed occupancy field, giving direct
  forward contact priority, otherwise turning it ninety degrees away from an
  occupied forward diagonal, until it is absorbed or leaves the field.
- Includes: Black Box resolving an immediate or internal hit, pre-entry or
  returned reflection, deflection, and a paired different-edge exit.
- Excludes: player-drawn paths; diagonal ray travel; probabilistic scattering;
  a visible projectile whose continuous trajectory can be steered.
- Parameters: field size, occupied-neighbourhood stencil, hit priority,
  deflection direction, boundary handling and outcome notation.
- Evidence: [Black Box decomposition](../games/a-f/black-box.md).
- Novelty: not assessed.

## SYS-106 — Observational-equivalence adjudication with counterexample

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when a complete hidden-system hypothesis is submitted, the
  system compares its predicted outcome for every legal probe with the fixed
  concealed system, accepts any hypothesis with the same complete outcome
  mapping, and otherwise exposes one probe on which they differ.
- Includes: Black Box accepting a five-ball arrangement observationally
  indistinguishable from the generated arrangement, or firing one omitted
  distinguishing laser after an incorrect check.
- Excludes: literal coordinate equality as the only acceptance rule; checking
  only observations the player already requested; returning a scalar
  similarity score; revealing the complete concealed layout after one error.
- Parameters: probe domain, outcome equivalence, counterexample selection,
  handling of an already visible contradiction and success disclosure.
- Evidence: [Black Box decomposition](../games/a-f/black-box.md).
- Novelty: not assessed.

## SYS-107 — Retained-sequence replay with one-cue extension

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after one complete correct reproduction, the system preserves the
  entire ordered cue sequence, appends exactly one newly selected cue, and
  serially presents the resulting longer sequence from its beginning.
- Includes: Simon replaying every prior light in order and adding one random
  coloured light for the next round.
- Excludes: replacing the target with an unrelated sequence; revealing only the
  new suffix; increasing difficulty without extending the target; a player-
  authored sequence.
- Parameters: initial length, extension count, cue-selection distribution,
  replay tempo and presentation channels.
- Evidence: [Simon decomposition](../games/s-z/simon.md).
- Novelty: not assessed.

## SYS-108 — Ordered-response first-mismatch adjudication

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system compares each response input with the cue at the same
  ordinal position, advances only while they match, recognises a completed
  exact sequence as one successful round, and terminates the attempt on the
  first mismatch.
- Includes: Simon accepting an exact prefix reproduction, increasing the score
  after its final cue, or sounding failure and ending after one wrong pad.
- Excludes: aggregate similarity scoring; edit-before-submit hypotheses;
  accepting a permutation; revealing the remaining answer after an error.
- Parameters: comparison timing, mismatch feedback, round-completion scoring,
  termination policy and whether incomplete input times out.
- Evidence: [Simon decomposition](../games/s-z/simon.md).
- Novelty: not assessed.

## SYS-109 — Simultaneous closed-neighbourhood binary toggle

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after one addressed-cell press, the system atomically inverts
  the binary state of the selected cell and every existing position directly
  adjacent to it in the declared neighbourhood, leaving all other positions
  unchanged.
- Includes: a Lights Out button toggling itself plus its orthogonal neighbours,
  with border and corner presses affecting only neighbours inside the field.
- Excludes: toggling only the selected cell; recolouring a maximal connected
  component; activating linked mechanisms that may be spatially remote;
  revealing concealed contents.
- Parameters: neighbourhood topology, boundary clipping, state vocabulary,
  atomicity, no-op policy and resolution feedback.
- Evidence: [Lights Out decomposition](../games/g-l/lights-out.md).
- Novelty: not assessed.

## SYS-110 — Straight-line travel until declared stop condition

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after a direction is committed, the system advances one
  designated body through successive cells on that unchanged straight heading
  until a declared stopping surface is entered or the next cell is blocked.
- Includes: Inertia's ball continuing through blank, gem and mine cells until
  it enters a stop square, or settling immediately before a wall or board edge.
- Excludes: maximum compression of every movable board element; physics-based
  momentum; pathfinding around obstacles; player steering during travel;
  movement that stops on every collectible.
- Parameters: direction set, stop surfaces, blocking surfaces, diagonal-gap
  policy, traversal speed and intermediate-contact ordering.
- Evidence: [Inertia decomposition](../games/g-l/inertia.md).
- Novelty: not assessed.

## SYS-111 — Wall-bounded orthogonal illumination propagation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: each selected source deterministically activates its own cell
  and every traversable cell on four orthogonal rays up to, but not through,
  the first blocking cell or field boundary.
- Includes: a Light Up bulb illuminating its own white square and unobstructed
  white squares in its row and column until a black square.
- Excludes: hidden ray probing; diagonal propagation; player-drawn paths;
  illumination that turns a corner; flood fill through connected cells.
- Parameters: ray directions, source inclusion, traversable cells, blockers,
  range and overlap presentation.
- Evidence: [Light Up decomposition](../games/g-l/light-up.md).
- Novelty: not assessed.

## SYS-112 — Compatible fixture activation exposes dependent mechanism state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after the player completes an accepted trigger or compatible
  item–fixture operation, the system persistently opens or reveals its authored
  downstream compartment, item, mechanism assembly or final latch.
- Includes: The Room exposing the peculiar key, metal plate, eyepiece lens and
  front rings after their respective accepted operations, then unlatching the
  safe after all three rings match the hidden trace; Machinarium exposing the
  torso and resolving the prepared pole-and-rig operation into arm recovery.
- Excludes: revealing random loot; opening a barrier only while a pressure plate
  remains occupied; merely animating a directly dragged component; validating
  a complete abstract answer with no persistent mechanism state.
- Parameters: activation predicate, revealed state, persistence, reward item,
  animation lockout, repeat policy and reset boundary.
- Evidence: [The Room decomposition](../games/s-z/the-room.md) and
  [Machinarium decomposition](../games/m-r/machinarium.md).
- Novelty: not assessed.

## SYS-113 — Requested item hand-in grants capability component

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after the player gives the currently requested compatible item
  to an addressed character, the system consumes that item and persistently
  grants or attaches one authored component that enables a new avatar
  capability.
- Includes: Machinarium's small scrapyard robot accepting the doll and returning
  Josef's missing leg, after which Josef can walk through the scene.
- Excludes: deterministic fixture activation; buying a statistical upgrade with
  abstract currency; dialogue that changes no mechanical state; random loot
  after defeating an opponent.
- Parameters: recipient, accepted request item, consumed input, granted
  component, enabled capability, persistence and repeat policy.
- Evidence: [Machinarium decomposition](../games/m-r/machinarium.md).
- Novelty: not assessed.

## SYS-114 — Transient constituent decay invalidates composite use

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after the player prepares one temporary material state and may
  incorporate that object into a held composite, the system continuously
  advances the state toward expiry; expiry removes the composite's required
  function while leaving a declared retry path.
- Includes: The Longest Journey's unpatched inflated ducky losing air while it
  holds the fishing instrument's clamp open, after which the clamp closes and
  the constituent assembly must be prepared again.
- Excludes: a permanent held-item configuration; consumption only when a tool
  is successfully used; a visual animation with no compatibility consequence;
  a countdown that merely changes score.
- Parameters: transient state, decay clock, composite propagation, expiry
  effect, constituent recovery, pause behaviour and retry boundary.
- Evidence: [The Longest Journey decomposition](../games/s-z/the-longest-journey.md).
- Novelty: not assessed.

## SYS-115 — Recipient accumulates typed hand-ins and constructs fixed output

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: one addressed recipient persistently retains each accepted
  distinct item from a disclosed required set and, exactly when that set becomes
  complete, automatically replaces the accumulated inputs with one authored
  constructed scene object.
- Includes: Red Edison accepting oil, vinegar and a gold-plated quill in any
  order, then building Day of the Tentacle's uncharged super-battery and
  placing it on the shelf.
- Excludes: the player directly combining inventory items; one hand-in granting
  an avatar component; random reward selection; a recipient that only tracks a
  numeric currency total; incomplete-set progress with no constructed output.
- Parameters: recipient, accepted typed set, partial persistence, order freedom,
  duplicate policy, transformation trigger, output identity and output location.
- Evidence: [Day of the Tentacle decomposition](../games/a-f/day-of-the-tentacle.md).
- Novelty: not assessed.

## SYS-116 — Persistent typed-slot contribution completes collection group

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each accepted typed inventory contribution is consumed and
  retained as a filled requirement; when the collection's declared slot quota
  is filled, the system persistently marks that group complete and exposes its
  authored group reward.
- Includes: Stardew Valley retaining Boiler Room bundle donations across visits
  and completing the Blacksmith's, Geologist's or Adventurer's Bundle after its
  respective three, four or two accepted slots.
- Excludes: one recipient constructing an output from a complete exact set;
  direct item crafting; a reversible inventory transfer; a score counter whose
  past increments have no typed slot identity.
- Parameters: collection identity, slot schema, contribution persistence,
  completion quota, consumed quantities, group reward and repeat policy.
- Evidence: [Stardew Valley decomposition](../games/s-z/stardew-valley.md).
- Novelty: not assessed.

## SYS-117 — Aggregate collection completion schedules world-service restoration

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: once every required subordinate collection group is persistently
  complete, the system marks their enclosing area complete and schedules one
  authored persistent world service to become available at the next declared
  progression boundary.
- Includes: completing all three standard Stardew Valley Boiler Room bundles,
  after which Junimos repair the minecarts overnight and enable their four-stop
  fast-travel service on the following day.
- Excludes: an immediate inventory-item reward for one group; a directly built
  held tool; temporary access while an input remains present; purchasing an
  upgrade with one scalar currency payment.
- Parameters: subordinate group set, aggregate predicate, completion marker,
  scheduled boundary, restored service, persistence and alternate route.
- Evidence: [Stardew Valley decomposition](../games/s-z/stardew-valley.md).
- Novelty: not assessed.

## SYS-118 — Persistent collectible identity populates addressed arranger

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: contact-crediting one authored collectible persistently records
  its distinct rigid footprint and makes exactly that identity available in a
  separately addressed finite arranger whose requirement roster includes it.
- Includes: The Talos Principle crediting each green A1 `L`, `J` or `Z` sigil,
  marking its source progress and exposing that exact piece in the first gate's
  tetromino arranger.
- Excludes: adding fungible currency; automatically opening an exit on the last
  collection; contributing an inventory quantity into a fixed semantic slot;
  generating a random construction piece.
- Parameters: collectible identity, footprint, colour, source marker, arranger
  address, persistence, duplicate policy and cross-gate reuse.
- Evidence: [The Talos Principle decomposition](../games/s-z/the-talos-principle.md).
- Novelty: not assessed.

## SYS-119 — Gapless arranger completion immediately opens persistent gate

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when every cell of one bounded arranger is occupied by exactly
  one required footprint and every required piece has been used, the system
  accepts the arrangement and permanently opens its linked traversal barrier
  before the next world-navigation decision.
- Includes: the first The Talos Principle A1 gate opening immediately after the
  green `L`, `J` and `Z` form a gapless non-overlapping 4 × 3 cover.
- Excludes: automatic exit activation on collecting the last token; delayed
  world repair; temporary door state sustained by occupancy; accepting a typed
  target image whose cells may be overwritten.
- Parameters: completion predicate, linked barrier, activation timing,
  persistence, animation interval and behaviour after reopening the arranger.
- Evidence: [The Talos Principle decomposition](../games/s-z/the-talos-principle.md).
- Novelty: not assessed.

## SYS-120 — View-relative front-layer collision rewrites traversal adjacency

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after a cardinal orthographic view settles, the system resolves
  collision front-to-back in screen space, keeps the nearest eligible solid
  layer active and corrects avatar depth onto visible support; the resulting
  two-dimensional collision slice may connect world positions that were not
  adjacent in the prior view while their underlying geometry remains fixed.
- Includes: Fez rebuilding active trile collision after rotation so Gomez can
  walk across a projection-aligned continuation that another view separates or
  occludes.
- Excludes: moving platforms into new world coordinates; creating or deleting
  geometry from an image; mapping a body through paired portals; cosmetic
  parallax that never changes legal movement.
- Parameters: projection axis, frontmost-layer rule, collision type, depth
  correction, occlusion exceptions, moving-object invalidation and settle time.
- Evidence: [Fez decomposition](../games/a-f/fez.md).
- Novelty: not assessed.

## SYS-121 — Live screen projection governs traversal topology

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while the underlying route geometry remains fixed, the system
  projects it into the current screen frame and treats apparent path contact or
  an occluded discontinuity as authoritative traversal connectivity for an
  agent moving through that projection.
- Includes: Echochrome transferring the Walker between world-separated path
  endpoints that coincide on screen and allowing it across a gap hidden behind
  a nearer route element.
- Excludes: selecting only the nearest solid depth layer; physically moving a
  platform; creating or deleting geometry; paired portal traversal; visual
  overlap that never changes collision or route continuation.
- Parameters: projection model, coincidence tolerance, eligible endpoint
  classes, occluder depth, discontinuity types, update cadence and invalidation
  timing while the camera moves.
- Evidence: [Echochrome decomposition](../games/a-f/echochrome.md).
- Novelty: not assessed.

## SYS-122 — Snap-state projected-node connectivity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after a manipulated architectural component reaches one authored
  settled pose, the system rebuilds its navigation graph by testing visible
  projected node relationships, allowing world-depth-separated route points
  that appear continuous to become connected until the component moves again.
- Includes: Monument Valley connecting the two ends of its Chapter I rotating
  bridge to fixed approach and goal-side nodes only in the aligned snap state.
- Excludes: continuous free-camera topology; four global cardinal collision
  slices; ordinary physical adjacency alone; image-stamped replacement
  geometry; cosmetic alignment with no traversal effect.
- Parameters: component pose set, snap tolerance, projection model, node depth
  ordering, occlusion rule, eligible node types and graph rebuild timing.
- Evidence: [Monument Valley decomposition](../games/m-r/monument-valley.md).
- Novelty: not assessed.

## SYS-123 — Destination-commanded route traversal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after the player selects a reachable world node, the system
  computes a route through the current navigation graph and advances the
  player-controlled avatar along its intervening nodes to the destination
  without requiring step-by-step direction inputs.
- Includes: Ida automatically walking across Monument Valley's settled Chapter
  I bridge and approach path after the player selects the final pedestal.
- Excludes: continuously autonomous walking with no destination command;
  teleportation; direct local steering; a vehicle following a player-drawn
  network; fixed straight-line motion that ignores a route graph.
- Parameters: pathfinder, route tie-break, traversal speed, interruption,
  invalidation during geometry motion, arrival trigger and animation timing.
- Evidence: [Monument Valley decomposition](../games/m-r/monument-valley.md).
- Novelty: not assessed.

## SYS-124 — Perspective-preserving collision-bounded object rescaling

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while a portable object is held, the system continually places
  it at the farthest collision-free depth along the current camera sightline
  and changes its physical world scale in direct proportion to depth so its
  projected screen extent stays constant; release commits that physical pose
  and scale to ordinary world simulation.
- Includes: Superliminal moving a held Induction chess piece toward the
  opposite background, enlarging it as its camera distance grows, and retaining
  the enlarged collidable piece after it is dropped.
- Excludes: camera zoom; scaling only a rendered sprite; image-stamped
  replacement geometry; a global world-scale change; changing scale through a
  fixed portal; freely choosing a numeric object size without a sightline.
- Parameters: pickup projection, camera model, candidate sightline, ray-sample
  density, collision clearance, scale-to-depth ratio, supported object shapes,
  minimum and maximum scale, update cadence and release physics.
- Evidence: [Superliminal decomposition](../games/s-z/superliminal.md).
- Novelty: not assessed.

## SYS-125 — Selected-surface global gravity-frame reorientation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after the player selects an eligible orthogonal surface, the
  system snaps the local world's gravity vector to that surface's inward normal
  and resolves unsupported eligible bodies toward the newly authoritative
  floor while retaining the same physical architecture.
- Includes: Manifold Garden changing from blue floor gravity to the red ceiling
  or a coloured wall gravity so the chosen surface becomes walkable ground.
- Excludes: rotating only the camera; replacing collision with a screen-space
  slice; reorienting velocity only at a portal exit; reversing one body's
  gravity while the world frame stays fixed; visual world rotation with no
  physical force change.
- Parameters: direction domain, affected body classes, transition curve,
  velocity preservation, grounded-state reset, collision recovery and colour
  state.
- Evidence: [Manifold Garden decomposition](../games/m-r/manifold-garden.md).
- Novelty: not assessed.

## SYS-126 — Translationally periodic 3D boundary remapping

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when an eligible dynamic body crosses an authored boundary of a
  three-dimensional repeating world cell, the system translates it by the
  corresponding whole-cell period into the opposite copy while preserving its
  local pose and useful frame-relative trajectory.
- Includes: a Manifold Garden avatar or cube falling through the bottom of the
  central world instance and returning from the corresponding top copy, so a
  lower repeated balcony becomes a reachable landing.
- Excludes: paired placed apertures; a finite board edge whose adjacency wraps
  only logical cells; respawning at a checkpoint; reflection or rotation across
  the seam; visual instancing with no traversable boundary mapping.
- Parameters: period vectors, eligible bodies, boundary threshold, local-pose
  mapping, velocity transform, collision recovery, camera smoothing and
  repeated-instance visibility.
- Evidence: [Manifold Garden decomposition](../games/m-r/manifold-garden.md).
- Novelty: not assessed.

## SYS-127 — Recursive homologous-instance state propagation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: one authoritative world-object pose is exposed through multiple
  scale-transformed representations in recursively nested world instances, and
  manipulating any reachable representation updates every homologous
  representation rather than creating an independently mutable copy.
- Includes: moving Maquette's red block in the central model to clear the
  corresponding normal courtyard gate, or aligning the golden key in the model
  so its larger representation spans the surrounding gap.
- Excludes: visual miniatures with no causal effect; independent clones; a
  periodic body translated into another same-scale cell; changing a container's
  parent in a mutable nested graph; mirroring only an animation.
- Parameters: recursion depth, scale ratio, authoritative identity map, pose
  transform, propagation latency, collision ownership and representation
  culling.
- Evidence: [Maquette decomposition](../games/m-r/maquette.md).
- Novelty: not assessed.

## SYS-128 — Cross-layer carried-object scale reindexing

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when the player carries one reachable recursive object
  representation across an adjacent nested-world boundary, the system retains
  its identity and canonical state but shifts which scale exponent is ordinary
  relative to the avatar, making the object physically smaller or larger after
  release.
- Includes: Maquette turning the same golden key into a giant traversable
  bridge, a tiny house key and then a bridge again by carrying it between the
  central model and surrounding courtyard.
- Excludes: deriving scale from camera depth; global camera zoom; teleporting a
  fixed-size body through a portal; spawning a separate small copy; changing
  only visual size while collision stays fixed.
- Parameters: adjacent-layer rule, scale ratio, identity persistence, held-pose
  transform, collision handoff, minimum and maximum exponent and release
  correction.
- Evidence: [Maquette decomposition](../games/m-r/maquette.md).
- Novelty: not assessed.

## SYS-129 — Observation-gated authored doorway destination remapping

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after an authored trigger is armed and its affected doorway or
  connected region is no longer observed, the system replaces that doorway's
  destination with another fixed room in the authored navigation graph while
  retaining the same local threshold geometry.
- Includes: Antichamber's `Now You See It` doorway continuing to its original
  room while watched, then leading to the changed room after the player takes
  the blue cube and looks through the glass window.
- Excludes: traversing a visible paired portal; translating a body across a
  periodic boundary; propagating one pose across recursive scale instances;
  rotating fixed geometry into a projected connection; procedural room
  generation or cosmetic set dressing.
- Parameters: trigger state, observed region, eligible destination set,
  replacement timing, threshold identity, persistence and reset behaviour.
- Evidence: [Antichamber decomposition](../games/a-f/antichamber.md).
- Novelty: not assessed.

## SYS-130 — Continuous constant-negative-curvature pose integration

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: every locomotion and view update composes the controllable
  body's pose through isometries of one constant-negative-curvature metric, so
  path distance, direction and accumulated orientation follow hyperbolic
  rather than Euclidean translation throughout ordinary traversal.
- Includes: walking through Hyperbolica's Maze of Apeirogon while local steps
  remain continuous but surrounding volume grows exponentially and composed
  translations can produce unexpected orientation.
- Excludes: teleporting between authored rooms; wrapping one Euclidean cell
  periodically; changing only camera projection; paired apertures; a discrete
  hyperbolic adjacency graph with no continuous avatar pose.
- Parameters: curvature magnitude, internal geometry model, translation step,
  rotation representation, numerical renormalisation, collision metric,
  camera coupling and comfort options.
- Evidence: [Hyperbolica decomposition](../games/g-l/hyperbolica.md).
- Novelty: not assessed.

## SYS-131 — Shortest-route hostile step after a player turn

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after one turn-costing player command resolves, each eligible
  hostile automatically takes one cell step chosen to reduce its current
  shortest-path distance to the player's new cell before the next command.
- Includes: standard turn-based HyperRogue pursuers responding after an
  adjacent player move and following a shortest available route.
- Excludes: hostile intents committed before a planning phase; continuous
  steering; an opposing human selecting the response; a full multi-cell path
  resolved at once; mere cooldown advancement.
- Parameters: hostile order, simultaneous-contact policy, tie breaking,
  blocked cells, attack substitution, zero-time player actions and terminal
  check timing.
- Evidence: [HyperRogue decomposition](../games/g-l/hyperrogue.md).
- Novelty: not assessed.

## SYS-132 — Rule-conditioned bomb-module adjudication

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after a live module control is committed, the system compares it
  with the unique action selected by the module's current observable state and
  ordered rule procedure, then either permanently disarms that module or
  records one strike before accepting further play.
- Includes: accepting the one correct Wires cut; accepting the Button's
  required tap or correctly timed held release; striking any other committed
  control.
- Excludes: evaluating a complete concealed sequence hypothesis; accepting a
  freely revisable tentative value; the human communication used to derive the
  instruction; countdown progression by itself.
- Parameters: module state, applicable rule branch, accepted gesture, disarm
  indicator, strike response and post-adjudication input lock.
- Evidence: [Keep Talking and Nobody Explodes decomposition](../games/g-l/keep-talking-and-nobody-explodes.md).
- Novelty: not assessed.

## SYS-133 — Strike-triggered countdown acceleration

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: each accepted mistake increments the persistent strike state and
  immediately increases the rate at which the same terminal countdown loses
  time, so an error reduces both the remaining strike allowance and the real
  time available for later decisions.
- Includes: the Keep Talking and Nobody Explodes timer running faster after a
  recorded first or second strike.
- Excludes: subtracting a fixed score; consuming one move without changing
  clock rate; difficulty increasing only between completed stages; terminal
  expiry at zero without an error-dependent rate change.
- Parameters: strike count, rate multiplier per strike, update instant, audio
  feedback and reset scope.
- Evidence: [Keep Talking and Nobody Explodes decomposition](../games/g-l/keep-talking-and-nobody-explodes.md).
- Novelty: not assessed.

## SYS-134 — Validate and canonicalise complete glyph page

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when every illustrated slot on one bounded notebook page has a
  distinct discovered glyph, the system evaluates the complete mapping as one
  submission; a correct mapping replaces provisional glosses with persistent
  canonical meanings, while an incorrect mapping remains revisable.
- Includes: the forced first three-glyph validation page in Chants of Sennaar.
- Excludes: validating one typed gloss independently; checking a sentence one
  token at a time; scoring a partial mapping; human confirmation outside play.
- Parameters: page size, canonical bijection, submission trigger, incorrect
  feedback, lock persistence and later-display replacement.
- Evidence: [Chants of Sennaar decomposition](../games/a-f/chants-of-sennaar.md).
- Novelty: not assessed.

## SYS-135 — Live revalidation of every revealed answer predicate

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after every edit to one persistent answer, the system
  immediately reevaluates every predicate revealed so far against the complete
  current answer, allowing an earlier passing predicate to become failing.
- Includes: The Password Game continuously rechecking Rules 1-9 after any
  character insertion or deletion.
- Excludes: validating only on submission; checking only the most recently
  revealed rule; preserving a passed rule regardless of later edits; checking
  independent board cells without a shared answer.
- Parameters: evaluation order, update debounce, formatting semantics,
  simultaneous failures and feedback timing.
- Evidence: [The Password Game decomposition](../games/s-z/the-password-game.md).
- Novelty: not assessed.

## SYS-136 — All-valid state reveals the next authored rule

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: whenever every rule currently revealed for one answer passes,
  the system permanently adds the next rule in a fixed authored sequence and
  evaluates it against that same answer.
- Includes: The Password Game revealing Rules 2 through 10 one at a time as
  the current password satisfies the preceding visible set.
- Excludes: displaying the full rule set before play; choosing a random next
  rule; replacing the previous rule; unlocking an unrelated level after a
  submitted answer.
- Parameters: authored order, initial rule count, terminal rule, reveal
  animation and whether multiple already-satisfied rules cascade.
- Evidence: [The Password Game decomposition](../games/s-z/the-password-game.md).
- Novelty: not assessed.

## SYS-137 — Adjudicate a selected fact pair as matching, discrepant or unrelated

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after two visible case facts are selected, the system resolves
  their authored semantic relation as matching data, a formal discrepancy or
  no correlation, and exposes any discrepancy-dependent follow-up action.
- Includes: Papers, Please inspection mode detecting a missing entry permit
  from the empty counter plus the current rule and enabling interrogation.
- Excludes: the player noticing an inconsistency without invoking the check;
  adjudicating the final case verdict; live validation of every predicate in
  one answer; numeric similarity scoring.
- Parameters: relation catalogue, fact typing, asymmetric pairs, feedback,
  interrogation unlock and discrepancy-clearance policy.
- Evidence: [Papers, Please decomposition](../games/m-r/papers-please.md).
- Novelty: not assessed.

## SYS-138 — Audit committed case verdict against the complete active policy

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: once a case leaves after a committed verdict, the system checks
  that verdict against every currently active admissibility predicate for the
  complete case and issues delayed error feedback when any required condition
  was ignored or the valid case was rejected.
- Includes: Papers, Please issuing a citation after an incorrect approval or
  denial while accepting a correct Day 4 decision without one.
- Excludes: checking only the two facts explicitly highlighted; immediate
  truth feedback for one board cell; player-authored review; punishment for a
  slow but correct case.
- Parameters: policy snapshot, case truth, verdict set, feedback delay,
  citation allowance, monetary penalty and special scripted exceptions.
- Evidence: [Papers, Please decomposition](../games/m-r/papers-please.md).
- Novelty: not assessed.

## SYS-139 — Recognise buffered directional code and open addressed seal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an addressed world seal buffers successive cardinal commands,
  compares their ordered identity with its authored code and permanently opens
  only when the complete exact sequence has been recognised.
- Includes: TUNIC's fountain-area patterned door opening after the six-command
  Holy Cross code.
- Excludes: consuming a carried key; validating a freely editable text string;
  moving a character through the same directions; opening after a partial code.
- Parameters: authored code, buffer policy, mismatch recovery, persistence,
  animation and whether the player can know the code before collecting its clue.
- Evidence: [TUNIC decomposition](../games/s-z/tunic.md).
- Novelty: not assessed.

## SYS-140 — Reset embodied world state while preserving learned facts

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: at a repeating-loop boundary, the system restores the controlled
  body and mutable world to one authored origin while transferring the paired
  player's registered learned facts into the next iteration.
- Includes: Outer Wilds returning the Hatchling to the Timber Hearth campfire
  after death or the supernova while retaining the learned launch codes.
- Excludes: rewinding only recent motion; preserving inventory and opened world
  mechanisms; restarting from a save with no cross-attempt information state.
- Parameters: reset trigger, origin state, retained fact classes, cleared state
  classes, pairing prerequisite and loop counter.
- Evidence: [Outer Wilds decomposition](../games/m-r/outer-wilds.md).
- Novelty: not assessed.

## SYS-141 — Authorise mechanism from registered learned fact

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an addressed world mechanism accepts activation when one exact
  fact is registered as learned for the player, without consuming a carried
  token or requiring that fact to be reacquired in the current world iteration.
- Includes: Outer Wilds' launch-tower lift accepting the retained launch codes
  on a later loop without another visit to Hornfels.
- Excludes: manually entering a symbol sequence; consuming a physical key;
  opening from an unrelated story flag; a mechanism available from the start.
- Parameters: learned-fact identifier, mechanism identity, activation gesture,
  consumption policy, iteration scope and unavailable feedback.
- Evidence: [Outer Wilds decomposition](../games/m-r/outer-wilds.md).
- Novelty: not assessed.

## SYS-142 — Retrieve transcript-matching records in fixed chronological order

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a text query is committed, the system identifies every
  fixed evidence record whose indexed transcript satisfies the query and gives
  those matches the same authored chronological order on every repetition.
- Includes: Her Story matching submitted words against interview answers and
  ordering qualifying clips by their fixed recording timestamps.
- Excludes: semantic web search over changing documents; random result rotation;
  player-authored sorting; checking whether one persistent answer is valid.
- Parameters: tokenisation, case handling, phrase semantics, transcript field,
  timestamp key, tie breaking, total-count disclosure and empty-result feedback.
- Evidence: [Her Story decomposition](../games/g-l/her-story.md).
- Novelty: not assessed.

## SYS-143 — Transfer controlled avatar across paired panel ports

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when a directly controlled avatar enters one endpoint of a
  player-created panel link, the system transfers it to the paired endpoint and
  resumes local traversal inside that destination panel.
- Includes: The Pedestrian walking through a linked door or climbing through a
  linked ladder endpoint to emerge in another public-sign panel.
- Excludes: automatic pathfinding across the whole graph; visual composition
  that advances an uncontrolled depicted figure; velocity-transforming portals;
  moving a world region so its physical boundary becomes adjacent.
- Parameters: entry gesture, transfer direction, emergence pose, animation,
  carried-object policy, collision state and link-removal response.
- Evidence: [The Pedestrian decomposition](../games/s-z/the-pedestrian.md).
- Novelty: not assessed.

## SYS-144 — Resolve mounted world orb as reversible contained-world entry

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when one world orb is mounted at an eligible jump pedestal, the
  system exposes that orb's persistent contained world as a local entry surface
  and transfers the directly controlled avatar between the outer pedestal and
  the world's fixed arrival point while the orb retains one identity outside.
- Includes: Cocoon projecting the orange orb's world in the pedestal pool,
  letting the avatar enter it and returning the avatar to the same mounted orb.
- Excludes: crossing an aligned edge of a grid container; traversing a freely
  placed paired aperture; changing a movable container's parent relation;
  replacing the orb with a newly generated world after every entry.
- Parameters: orb identity, outer pedestal, inner arrival point, entry gesture,
  transfer animation, exit mapping, carried-object policy and persistence.
- Evidence: [Cocoon decomposition](../games/a-f/cocoon.md).
- Novelty: not assessed.

## SYS-145 — Manifest orb-specific traversal structure from carried ability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while the avatar carries one unlocked world orb through a
  compatible authored locus, the system instantiates that orb's declared
  traversal structure and removes or disables it when the carried ability is no
  longer available.
- Includes: Cocoon's unlocked orange orb revealing and supporting an otherwise
  absent bridge while the avatar carries it near the matching route.
- Excludes: toggling a permanent switch; constructing a bridge from consumed
  pieces; displaying a cosmetic highlight; granting the effect while the orb
  remains mounted or abandoned elsewhere.
- Parameters: orb identity, unlock flag, receptive-locus class, activation
  radius, structure geometry, persistence, fade timing and collision handoff.
- Evidence: [Cocoon decomposition](../games/a-f/cocoon.md).
- Novelty: not assessed.
