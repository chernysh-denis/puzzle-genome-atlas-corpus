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
  Loop Hero dawn spawns, card rewards and loot; generating Slay the Spire act
  maps, encounter contents and bounded reward offers from run-seeded pools.
- Excludes: hidden but predetermined outcomes; player-selected uncertainty.
- Parameters: outcome set and probability distribution.
- Evidence: [2048 decomposition](../games/0-9/2048.md) and
  [Tetris decomposition](../games/s-z/tetris.md), and
  [Royal Match decomposition](../games/m-r/royal-match.md), and
  [Threes decomposition](../games/s-z/threes.md), and
  [Mini Metro decomposition](../games/m-r/mini-metro.md),
  [Loop Hero decomposition](../games/g-l/loop-hero.md), and
  [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
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
  leave at compatible homes; Cities: Skylines vehicles repeatedly serving
  player-authored public-transport stops.
- Excludes: player steering of a vehicle; instantaneous connectivity-only
  evaluation; flow that consumes or locks the traversed route.
- Parameters: one-shot versus repeated service, vehicle speed, direction,
  dwell time, routing preference, transfer rule and pickup ordering.
- Evidence: [Mini Metro decomposition](../games/m-r/mini-metro.md),
  [Cosmic Express decomposition](../games/a-f/cosmic-express.md) and
  [Cities: Skylines decomposition](../games/a-f/cities-skylines.md).
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
  Walker advancing and turning without directional movement commands; Factorio
  attack groups pathing from their rally point toward a pollution source; and
  Dota 2 lane creeps and courier following live paths.
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
  [Dota 2 decomposition](../games/a-f/dota-2.md), and
  [Timelie decomposition](../games/s-z/timelie.md), and
  [Braid decomposition](../games/a-f/braid.md), and
  [Pikmin 4 decomposition](../games/m-r/pikmin-4.md),
  [Echochrome decomposition](../games/a-f/echochrome.md), and
  [Factorio decomposition](../games/a-f/factorio.md).
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
- Includes: Bad North soldiers forming up and fighting after a squad order; the
  Loop Hero protagonist automatically fighting circuit enemies; Factorio
  turrets selecting targets; and Dota 2 creeps/towers acquiring nearby hostiles.
- Excludes: the player selecting an ability and target; execution of a fully
  committed hostile intent; locomotion with no combat target selection.
- Parameters: acquisition radius, class counter, stance, target priority,
  formation, attack cadence and disengagement rule.
- Evidence: [Bad North decomposition](../games/a-f/bad-north.md),
  [Loop Hero decomposition](../games/g-l/loop-hero.md),
  [Factorio decomposition](../games/a-f/factorio.md), and
  [Dota 2 decomposition](../games/a-f/dota-2.md).
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
  next turn's hand after hostile resolution; Slay the Spire discarding
  ordinary unretained cards at End Turn, recycling the discard pile when
  necessary and drawing the next bounded hand.
- Excludes: drawing replacements immediately after every committed card;
  retaining arbitrary unplayed cards across the ordinary turn boundary;
  selecting which card identities enter the new hand.
- Parameters: hand size, discard timing, draw timing, shuffle trigger, retained
  cards and guaranteed-card modifiers.
- Evidence: [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md)
  and [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
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
  controlled avatar or travelling team along its intervening nodes without
  requiring step-by-step direction inputs.
- Includes: Ida automatically walking across Monument Valley's settled Chapter
  I route, and Frostpunk scouts travelling between known Frostland locations.
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

## SYS-146 — Resolve launched body through ballistic collisions

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after launcher release, the system advances one body under
  gravity and collision, transferring momentum through contacted bodies until
  the projectile leaves play or settles.
- Includes: bird, block and pig collisions in Angry Birds Classic; ball, peg,
  wall and bucket collisions in Peggle Deluxe.
- Excludes: deterministic grid travel; a projectile whose entire result is
  resolved without intermediate physical contacts; player-steered flight.
- Parameters: gravity, restitution, friction, collision layers, settle test and
  out-of-bounds rule.
- Evidence: [Angry Birds Classic decomposition](../games/a-f/angry-birds-classic.md)
  and [Peggle Deluxe decomposition](../games/m-r/peggle-deluxe.md).
- Novelty: not assessed.

## SYS-147 — Damage removes supports and cascades rigid structure collapse

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: collision damage can break a finite structural element; lost
  support then causes still-intact bodies to fall, collide and produce further
  damage in the same live resolution.
- Includes: breaking glass or wood in Angry Birds Classic so blocks above fall
  onto pigs or other supports.
- Excludes: deleting a matched tile and vertically refilling a board; moving a
  rigid structure without damage; purely cosmetic debris.
- Parameters: material strength, impact threshold, support graph, damage
  accumulation and debris collision policy.
- Evidence: [Angry Birds Classic decomposition](../games/a-f/angry-birds-classic.md).
- Novelty: not assessed.

## SYS-148 — Validate household-object placement against room affordances

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after all boxes are emptied, the system marks each object whose
  current support, room or containment class is not one of its accepted authored
  placements and withholds completion until every object is valid.
- Includes: Unpacking accepting clothes in drawers or wardrobes while rejecting
  contextually inappropriate room placements.
- Excludes: free decoration with no validation; exact target-coordinate
  reconstruction; collision rejection during dragging before release.
- Parameters: object class, accepted rooms, support classes, containment,
  overlap, invalid marker and completion timing.
- Evidence: [Unpacking decomposition](../games/s-z/unpacking.md).
- Novelty: not assessed.

## SYS-149 — Narrator response follows authored traversal branch

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: crossing an authored route threshold commits a narrative branch
  whose pre-recorded narrator response and downstream world state depend on the
  chosen path and prior branch history.
- Includes: The Stanley Parable narrator acknowledging whether Stanley follows
  or contradicts the announced left-door instruction.
- Excludes: non-interactive narration; random dialogue unrelated to player
  state; a dialogue menu that does not change traversable space.
- Parameters: trigger volumes, history flags, branch priority, interruption and
  reset boundary.
- Evidence: [The Stanley Parable: Ultra Deluxe decomposition](../games/s-z/the-stanley-parable-ultra-deluxe.md).
- Novelty: not assessed.

## SYS-150 — Publish puzzle clue through external interface state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: reaching a declared in-game state causes the application to
  create or update a decision-relevant clue outside the ordinary world view,
  while preserving that clue for independent inspection.
- Includes: OneShot exposing a clue through the host filesystem or the World
  Machine Edition mock operating system.
- Excludes: an in-world notebook; a platform achievement; a crash dump or save
  file whose contents are not intended as a puzzle channel.
- Parameters: trigger, external surface, persistence, refresh timing, clue
  encoding and platform-equivalent presentation.
- Evidence: [OneShot decomposition](../games/m-r/oneshot.md).
- Novelty: not assessed.

## SYS-151 — Develop zoned lots from demand and desirability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the simulation autonomously constructs, upgrades, abandons or
  replaces private buildings on authorised zones according to current sector
  demand, density, access and local desirability.
- Includes: residential, commercial and industrial growth in SimCity 4 and
  residential, commercial, industrial and office growth in Cities: Skylines.
- Excludes: direct player placement of a civic building; a fixed authored level
  transition; cosmetic growth without occupancy or budget consequences.
- Parameters: demand sector, stage, density, wealth, occupancy, abandonment and redevelopment.
- Evidence: [SimCity 4 Deluxe Edition decomposition](../games/s-z/simcity-4-deluxe-edition.md)
  and [Cities: Skylines decomposition](../games/a-f/cities-skylines.md).
- Novelty: not assessed.

## SYS-152 — Recompute sector demand from population and policy

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the simulation continuously recalculates residential,
  commercial and industrial demand from population, jobs, taxes, regional
  links and other declared city conditions.
- Includes: the SimCity 4 and Cities: Skylines RCI demand models responding to
  population, employment, tax and city conditions.
- Excludes: a fixed level quota; one visible passenger queue; random building
  selection independent of city state.
- Parameters: demand sectors, wealth classes, tax sensitivity, caps, regional
  contribution and update cadence.
- Evidence: [SimCity 4 Deluxe Edition decomposition](../games/s-z/simcity-4-deluxe-edition.md)
  and [Cities: Skylines decomposition](../games/a-f/cities-skylines.md).
- Novelty: not assessed.

## SYS-153 — Propagate utility and civic-service coverage

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: operating infrastructure distributes capacity through a network
  or service radius, changing which lots are supplied and how desirable or
  viable their locations are.
- Includes: SimCity 4 and Cities: Skylines power, water, education, health,
  police, fire and waste capacity or coverage.
- Excludes: a decorative range overlay; direct private-building placement;
  pathfinding that carries one discrete agent to a goal.
- Parameters: capacity, radius or network, funding, distance decay, demand and outage.
- Evidence: [SimCity 4 Deluxe Edition decomposition](../games/s-z/simcity-4-deluxe-edition.md)
  and [Cities: Skylines decomposition](../games/a-f/cities-skylines.md).
- Novelty: not assessed.

## SYS-154 — Settle recurring municipal budget

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: at recurring simulation intervals, the system credits taxes and
  deals, debits maintenance and service expenditure, and updates the treasury
  and solvency state.
- Includes: recurring income and expenditure settlement in SimCity 4 and
  Cities: Skylines.
- Excludes: a one-time purchase only; score awarded at a level ending; a
  household budget outside the managed city.
- Parameters: interval, revenue categories, maintenance, deals, debt and deficit response.
- Evidence: [SimCity 4 Deluxe Edition decomposition](../games/s-z/simcity-4-deluxe-edition.md)
  and [Cities: Skylines decomposition](../games/a-f/cities-skylines.md).
- Novelty: not assessed.

## SYS-155 — Generate trips and congestion from urban activity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: occupied lots create origin-to-destination travel demand whose
  routed use of the transport network produces commute access, congestion and
  local externalities.
- Includes: SimCity 4 and Cities: Skylines citizens and goods using roads and
  transit while congestion affects travel, pollution, services and development.
- Excludes: player-authored fixed vehicle endpoints; one scripted convoy;
  decorative traffic without network load.
- Parameters: trip purpose, mode, capacity, route cost, congestion, commute time and pollution.
- Evidence: [SimCity 4 Deluxe Edition decomposition](../games/s-z/simcity-4-deluxe-edition.md)
  and [Cities: Skylines decomposition](../games/a-f/cities-skylines.md).
- Novelty: not assessed.

## SYS-156 — Continuously execute supplied production recipe

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an operating production entity repeatedly consumes its declared
  recipe inputs and energy over simulation time, then emits the declared output
  while supply, power and output space remain available.
- Includes: Factorio furnaces smelting ore, assembling machines crafting their
  selected item, refineries and chemical plants transforming fluids, and labs
  consuming science packs through their active research recipe.
- Excludes: one hand-crafted inventory item; a stopped deterministic test run;
  item transport that does not transform item identity.
- Parameters: recipe, craft duration, ingredient quantities, result quantities,
  machine category, energy source, modules, productivity and blocked output.
- Evidence: [Factorio decomposition](../games/a-f/factorio.md).
- Novelty: not assessed.

## SYS-157 — Transport items and fluids through live factory logistics

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: persistent logistics entities repeatedly move eligible item or
  fluid quantities between world positions and inventories while the player
  may continue editing the running network.
- Includes: Factorio belts advancing lane items, inserters transferring between
  belts and inventories, pipes equalising fluid networks, scheduled trains
  carrying cargo and logistic robots satisfying chest requests.
- Excludes: transport that runs only after an editor is locked; direct avatar
  carrying; urban trips generated from simulated population rather than
  discrete stored items.
- Parameters: transport class, direction, lane, speed, stack size, inventory,
  route, schedule, request priority, fluid volume and blockage.
- Evidence: [Factorio decomposition](../games/a-f/factorio.md).
- Novelty: not assessed.

## SYS-158 — Distribute network power and throttle consumers

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each connected power network continuously pools current
  generation and storage, distributes available energy among active consumers
  and slows or stops them when demand exceeds supply.
- Includes: Factorio pole-connected generators, accumulators, assembling
  machines, inserters, mining drills and laser turrets sharing electricity.
- Excludes: binary service-radius coverage with no energy flow; fuel consumed
  independently inside an unconnected burner; a fixed level power switch.
- Parameters: network membership, production priorities, storage charge,
  satisfaction ratio, consumer drain and outage behaviour.
- Evidence: [Factorio decomposition](../games/a-f/factorio.md).
- Novelty: not assessed.

## SYS-159 — Consume science toward queued technology unlock

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: supplied laboratories consume the required science-pack set over
  time to advance the front queued technology, then persistently unlock its
  recipes or bonuses and advance to the next eligible queue entry.
- Includes: Factorio research units supplied to one or more powered labs and
  the automatic research queue.
- Excludes: crafting the science packs; an experience level granted directly
  by combat; exposing a recipe that was already available.
- Parameters: science-pack types, units, unit duration, lab count and speed,
  partial progress, prerequisites, unlocks and queue advance.
- Evidence: [Factorio decomposition](../games/a-f/factorio.md).
- Novelty: not assessed.

## SYS-160 — Diffuse production pollution into hostile attack pressure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: operating entities emit pollution into spatial chunks; the cloud
  spreads and is absorbed, and enemy spawners that absorb enough of it assemble
  attack groups whose size and cadence depend on accumulated pressure.
- Includes: Factorio mining, power and production pollution attracting biter
  and spitter attacks toward the factory.
- Excludes: cosmetic smoke; a fixed authored enemy wave; enemy evolution with
  no spatial pollution link.
- Parameters: emission rate, chunk cadence, diffusion, terrain absorption,
  spawner threshold, group size, rally delay and attack target.
- Evidence: [Factorio decomposition](../games/a-f/factorio.md).
- Novelty: not assessed.

## SYS-161 — Deplete spatial resource reserve on extraction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each non-productivity extraction result reduces the finite
  reserve of its addressed world resource position until the reserve reaches
  zero and further extraction there stops.
- Includes: Factorio ore tiles losing one unit per ordinary drill or hand-mined
  ore result and a drill shutting down after its covered patch is exhausted.
- Excludes: consuming an already stored ingredient; an infinite source port;
  depletion represented only by a global level counter.
- Parameters: reserve per tile, extraction result, resource drain probability,
  productivity bonus, mixed-resource coverage and exhaustion signal.
- Evidence: [Factorio decomposition](../games/a-f/factorio.md).
- Novelty: not assessed.

## SYS-162 — Construction agents fulfil supplied world-placement requests

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: available construction agents with access to a compatible owned
  item supply claim construction, repair, upgrade or deconstruction requests,
  travel to them and materialise or remove the affected world entities.
- Includes: Factorio robots building a stamped blueprint from network storage,
  and Dyson Sphere Program Icarus drones building supplied placements or
  blueprints from ordinary mecha inventory.
- Excludes: direct placement by the player; logistic robots moving inventory
  between chests without changing world structure; an instantaneous editor fill.
- Parameters: control or network coverage, agent availability, accessible item
  supply, request priority, charging, travel, repair and destination validity.
- Evidence: [Factorio decomposition](../games/a-f/factorio.md) and
  [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## SYS-163 — Resolve played card text in declared effect order

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a legal card play, the system executes the card's declared
  damage, block, draw, status and persistent-effect clauses in their rules-
  defined order before accepting the next command.
- Includes: resolving one Slay the Spire Attack, Skill or Power card and moving
  it to its declared discard, exhaust or persistent-power destination.
- Excludes: choosing the card or its target; evaluating a multi-card poker
  pattern; executing a spatial route encoded by a card.
- Parameters: effect clauses, trigger order, target count, generated effects,
  destination zone and interruption on terminal combat state.
- Evidence: [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
- Novelty: not assessed.

## SYS-164 — Execute telegraphed hostile combat intents

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after the player ends the combat phase, surviving enemies carry
  out their currently telegraphed attacks, defence, buffs or debuffs in the
  system's fixed actor order, then prepare their next intents.
- Includes: Slay the Spire enemies acting left to right after End Turn.
- Excludes: exact spatial attacks whose target cells may be redirected before
  resolution; a human opponent selecting a move; an untelegraphed real-time
  attack.
- Parameters: actor order, intent-selection policy, multi-hit count, target,
  cancellation conditions and post-action intent timing.
- Evidence: [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
- Novelty: not assessed.

## SYS-165 — Apply block before persistent health loss

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: incoming ordinary damage first consumes the target's current
  temporary Block and only the uncovered remainder reduces persistent health;
  ordinary Block then clears at its declared turn boundary.
- Includes: Slay the Spire player and enemy Block absorbing attack damage,
  with ordinary player Block removed at the start of the next player turn.
- Excludes: permanent armour; a one-use shield that cancels an entire attack
  regardless of magnitude; healing lost health.
- Parameters: damage type, block-loss timing, bypass effects, retention effects
  and health floor.
- Evidence: [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
- Novelty: not assessed.

## SYS-166 — Trigger persistent run modifiers at matching events

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: persistent acquired modifiers automatically apply their declared
  effects whenever a matching combat, reward, node or turn event occurs.
- Includes: Slay the Spire relics granting start-of-combat resources, modifying
  rewards or reacting to card and damage events.
- Excludes: a card effect that lasts only until one combat ends; an item that
  requires a separate consume command; equipment whose only effect is a static
  cosmetic change.
- Parameters: modifier identity, trigger event, ordering, once-per-event limit
  and run duration.
- Evidence: [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
- Novelty: not assessed.

## SYS-167 — Carry mutable run state across resolved nodes

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after one node resolves, the system carries the player's current
  health, deck, currency, persistent modifiers and consumable inventory into
  the next reachable node until victory or terminal defeat resets the run.
- Includes: Slay the Spire preserving damage, card additions and removals,
  gold, relics and potions across fights, shops, events and rest sites.
- Excludes: temporary combat-only powers and status cards; profile unlocks
  retained after the run; a level that fully restores all state on completion.
- Parameters: retained fields, healing, node reward timing, act transition and
  terminal reset.
- Evidence: [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
- Novelty: not assessed.

## SYS-168 — Generate a finite branching act route from a run seed

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: at act entry, the system constructs a finite directed acyclic
  route of disclosed node categories and connections from the run seed, ending
  at that act's boss node.
- Includes: Slay the Spire generating different connected maps for Acts 1–3.
- Excludes: a player-drawn network; an unbounded overworld; selecting the
  contents of a node only after the player chooses it.
- Parameters: floors, branch degree, forced node rows, category distribution,
  boss identity and seed.
- Evidence: [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
- Novelty: not assessed.

## SYS-169 — Unlock municipal capabilities at population milestones

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when the current city population first crosses a declared
  threshold, the simulation persistently adds its associated municipal tools,
  services, zones, policies, finance options or purchasable land areas to the
  available action catalogue.
- Includes: Cities: Skylines population milestones unlocking services,
  buildings, zones, loans, policies and additional map areas.
- Excludes: spending produced science on a queued technology; receiving a
  random weekly upgrade; a purely cosmetic achievement with no available
  action change.
- Parameters: population thresholds, unlock bundle, cash award, notification,
  map scaling and whether population decline can revoke access.
- Evidence: [Cities: Skylines decomposition](../games/a-f/cities-skylines.md).
- Novelty: not assessed.

## SYS-170 — Continuously apply fixed geometric-shape machine operation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while compatible shape or fluid inputs arrive and output space
  remains available, a placed factory machine repeatedly applies its fixed
  geometric operation and emits the resulting structured shape.
- Includes: shapez 2 cutting, rotating, stacking, swapping, painting, colour
  mixing, pin pushing and crystal-processing machines.
- Excludes: a selected inventory recipe that consumes item quantities; a
  stopped puzzle-program test; transport that preserves the carried shape.
- Parameters: machine class, accepted inputs, quadrant or layer mapping,
  colour, processing rate, output order and blockage.
- Evidence: [shapez 2 decomposition](../games/s-z/shapez-2.md).
- Novelty: not assessed.

## SYS-171 — Convert exact-shape delivery quota into milestone unlocks

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the central receiver counts delivered assemblies matching the
  current milestone schema and, when its required quantity is reached,
  persistently exposes the milestone's machines, mechanics, jobs and rewards.
- Includes: shapez 2 Vortex delivery completing a Classic milestone and
  unlocking later shape operations, floors, platforms, trains or progression.
- Excludes: purchasing an optional shop upgrade with research points; merely
  scoring an irrelevant shape; population growth unlocking city services.
- Parameters: accepted shape equivalence, quota, simultaneous goal lines,
  reward set, next milestone and difficulty multiplier.
- Evidence: [shapez 2 decomposition](../games/s-z/shapez-2.md).
- Novelty: not assessed.

## SYS-172 — Resolve paired-lane creature attacks into cards or damage scale

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after combat is committed, active creatures attack in fixed lane
  order; an opposed creature loses Health, while an unopposed attack adds its
  Power to the attacker's side of one shared relative-damage scale.
- Includes: Act I Inscryption creatures attacking from left to right, damaging
  the opposing card in the same lane or tipping the scale when that lane is
  open, subject to declared Sigils.
- Excludes: selecting targets freely; reducing one persistent player-health
  total; resolving a poker hand into an aggregate score.
- Parameters: lane order, attack count, Power, Health, direct-damage direction,
  Sigil overrides, overflow and scale threshold.
- Evidence: [Inscryption decomposition](../games/g-l/inscryption.md).
- Novelty: not assessed.

## SYS-173 — Convert friendly creature death into Bone currency

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: whenever an eligible friendly creature dies or is consumed by a
  sacrifice, the system increments a persistent encounter-local numeric pool
  that can pay the costs of later cards.
- Includes: Act I Inscryption granting one Bone for an ordinary friendly
  creature killed in combat or removed as Blood payment.
- Excludes: the Blood value used by the same sacrifice; post-battle Teeth;
  currency awarded only by completing a map node.
- Parameters: eligible death causes, amount, encounter reset, starting boons,
  multipliers and cards that do not die when sacrificed.
- Evidence: [Inscryption decomposition](../games/g-l/inscryption.md).
- Novelty: not assessed.

## SYS-174 — Advance disclosed opponent cards into combat lanes

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during the hostile phase, already disclosed opponent cards move
  from their queued back positions into the corresponding open active lanes,
  preserving the previewed lane assignment before later attacks resolve.
- Includes: Leshy's queued Act I Inscryption cards entering the front row after
  the player rings the bell and space permits.
- Excludes: an unseen enemy action sampled only after commitment; free target
  selection by a human opponent; a preview that never becomes active state.
- Parameters: preview horizon, lane, blocked-lane behaviour, entry order,
  exceptional boss rules and attack timing.
- Evidence: [Inscryption decomposition](../games/g-l/inscryption.md).
- Novelty: not assessed.

## SYS-175 — Reset failed run while preserving authored metaprogression

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: terminal run failure rebuilds the route and ordinary run state
  from its authored start while retaining declared cross-run unlocks, solved
  environment mechanisms and player-composed future-run content.
- Includes: Act I Inscryption clearing the current map deck and items after the
  last candle is lost while retaining opened cabin puzzles, staged rule
  unlocks and eligible Deathcards for later attempts.
- Excludes: a clean restart with no retained state; preserving only learned
  facts while every mechanism resets; carrying the failed run's complete deck
  unchanged into the next attempt.
- Parameters: reset trigger, cleared fields, retained unlocks, puzzle state,
  inherited content pool and mandatory early-run progression gates.
- Evidence: [Inscryption decomposition](../games/g-l/inscryption.md).
- Novelty: not assessed.

## SYS-176 — Generate seeded settlement map with concealed resource glades

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a run seed creates a finite spatial resource map partitioned by
  initially opaque regions whose contents become concrete only when opened.
- Includes: an Against the Storm settlement surrounded by concealed glades with
  resources, events and hazards determined by the map seed.
- Excludes: a fully visible random board; fixed authored levels; hidden entities
  moving independently through already explored space.
- Parameters: seed, biome, map size, glade classes, resource distribution and
  reveal trigger.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## SYS-177 — Advance repeating Drizzle-Clearance-Storm phases

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: live settlement time repeats a fixed three-phase cycle in which
  phase identity changes production conditions, active mysteries and population
  pressure.
- Includes: the Drizzle, Clearance and Storm cycle in Against the Storm.
- Excludes: a cosmetic day-night cycle; one non-repeating countdown; weather
  sampled independently without an ordered phase cycle.
- Parameters: phase order, duration, difficulty modifiers, pause and speed.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## SYS-178 — Convert expansion and exploitation into tiered hostility effects

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: settlement growth and forest exploitation accumulate an explicit
  pressure measure whose crossed tiers activate additional adverse effects,
  especially during the hostile phase.
- Includes: Against the Storm Hostility rising from years, population,
  woodcutters and opened glades, then activating mysteries and Resolve penalties.
- Excludes: hidden enemy aggression; pollution directly spawning attack groups;
  a difficulty setting fixed before play.
- Parameters: contributing sources, reductions, tier thresholds, phase gating
  and mystery set.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## SYS-179 — Aggregate group Resolve and trigger departures

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: current needs, services, work conditions and global effects are
  aggregated into one live welfare value per population group; sustained values
  below its threshold cause individual members to leave.
- Includes: species Resolve and departure checks in Against the Storm.
- Excludes: one shared city happiness score; combat morale causing temporary
  retreat; scripted population loss with no welfare state.
- Parameters: group, needs, job modifiers, favouring, threshold, grace period
  and departure cadence.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## SYS-180 — Convert sustained high group Resolve into reputation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while a population group's live welfare remains above its current
  threshold, the system continuously converts the surplus state into progress
  on the settlement's success track.
- Includes: high species Resolve generating Reputation in Against the Storm.
- Excludes: a one-time quest reward; passive score from population count; low
  welfare merely ceasing production.
- Parameters: group threshold, population scaling, rate, difficulty and current
  reputation.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## SYS-181 — Couple reputation gains and Queen's Impatience

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: time and declared failures increase a visible failure track while
  every gain on the success track reduces it, creating coupled opposed progress
  rather than independent counters.
- Includes: Against the Storm Reputation gains lowering Queen's Impatience
  while time and failed or declined Orders can raise it.
- Excludes: a fixed time limit; two scores with no causal link; health restored
  only by consumable items.
- Parameters: passive rate, event penalties, reduction per reputation point,
  difficulty and terminal thresholds.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## SYS-182 — Present bounded reward offers at settlement milestones

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: declared settlement milestones trigger finite random or seeded
  option sets from which a persistent reward or task may be committed.
- Includes: blueprint offers from Reputation and cornerstone offers by year in
  Against the Storm.
- Excludes: an always-open shop; deterministic technology unlocks; an offer
  whose selection has no later mechanical effect.
- Parameters: trigger, pool, option count, rerolls, rarity and exclusions.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## SYS-183 — Resolve staffed timed world event or trigger its threat

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: once a world event is activated, supplied workers and compatible
  goods advance one selected resolution over live time; completion grants its
  declared result, whereas deadline expiry activates the declared threat.
- Includes: dangerous and forbidden Glade Events in Against the Storm.
- Excludes: an instantaneous dialogue choice; production with no deadline or
  threat; an event resolved only by winning combat.
- Parameters: worker slots, goods, work duration, deadline, resolution options,
  reward and threat.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## SYS-184 — Award meta resources and cycle-map foothold for completed settlement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: completing a bounded settlement converts its difficulty and map
  conditions into persistent resources and leaves a temporary world-map origin
  from which later destinations become reachable during the current cycle.
- Includes: Against the Storm settlement rewards and its completed-settlement
  embarkation foothold before the next Blightstorm.
- Excludes: run-local loot; permanent free travel from every historical run;
  a sequel level unlocked without persistent resources or spatial reach.
- Parameters: reward formula, difficulty, modifiers, map range, cycle reset and
  retained Citadel resources.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## SYS-185 — Generate concealed material-cell asteroid

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a colony seed creates a bounded asteroid whose cells contain
  typed solid, liquid, gas or vacuum mass and concealed features revealed by excavation.
- Includes: Oxygen Not Included base-game terrain, biomes, resources, geysers and ruins.
- Excludes: a node-only resource graph; later random offers; hidden traps with no material simulation.
- Parameters: seed, asteroid type, element, mass, temperature, biome, feature and reveal radius.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## SYS-186 — Route eligible agent to highest-ranked errand

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an available agent filters errands by permissions, skills and
  reachability, ranks them by agent and task priority, then claims and completes one.
- Includes: Oxygen Not Included dig, build, supply, operate, research, tidy and life-support errands.
- Excludes: a permanently staffed role; direct step-by-step control; an unstaffed machine task.
- Parameters: errand pool, permissions, skill, path, personal priority,
  sub-priority, proximity and interruption.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## SYS-187 — Redistribute gas and liquid cell mass

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live simulation transfers gas and liquid mass among connected
  cells according to element, available space, pressure and gravity.
- Includes: oxygen rising over carbon dioxide, liquids falling and spreading,
  pressure equalisation and pumps changing local atmosphere.
- Excludes: conduit packets; cosmetic particles; water with no conserved cell mass.
- Parameters: element, mass, capacity, density, gravity, pressure and update cadence.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## SYS-188 — Transfer heat and resolve material phase change

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: neighbouring materials and entities exchange heat; crossing an
  element threshold replaces it with the declared solid, liquid or gas product.
- Includes: water freezing or boiling, steam condensing, machines heating rooms
  and conduit contents changing phase in Oxygen Not Included.
- Excludes: scripted melting; heat damage without temperature; machine recipes.
- Parameters: temperature, mass, specific heat, conductivity, transition, product and overheat.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## SYS-189 — Advance agent metabolism and personal needs

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each living agent consumes breathable gas and calories,
  accumulates bladder and fatigue needs, and seeks the scheduled response before failure.
- Includes: Oxygen Not Included breathing, carbon-dioxide output, eating, toilets and sleep.
- Excludes: one global population statistic; cosmetic idles; morale-only departure.
- Parameters: oxygen, calories, breath, bladder, stamina, schedule, waste, incapacitation and death.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## SYS-190 — Convert morale and environment into stress response

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: morale relative to trained-skill expectation plus environmental
  modifiers changes stress over time; maximum stress triggers the agent's declared response.
- Includes: Oxygen Not Included morale, oxygen, heat, wetness, rooms, food,
  recreation, stress responses and overjoyed responses.
- Excludes: one shared happiness score; lethal need depletion; cosmetic mood.
- Parameters: morale, expectation, modifiers, stress rate, threshold, response and relief.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## SYS-191 — Propagate germs through material and contact

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: germs reproduce or decay on compatible elements and transfer by
  inhalation, ingestion or contact until exposure can apply disease.
- Includes: base-game Oxygen Not Included food poisoning, slimelung and environmental carriers.
- Excludes: a carrierless health debuff; cosmetic dirt; DLC-only radiation.
- Parameters: germ, carrier, count, growth, decay, route, threshold, resistance and disease.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## SYS-192 — Propagate automation signal to building state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: sensors and logic evaluate visible state, propagate binary signals
  through an authored network and control connected buildings without workers.
- Includes: Oxygen Not Included smart batteries, atmo sensors, pumps and logic gates.
- Excludes: direct toggles; recipe filters; electric power flow itself.
- Parameters: sensor, threshold, truth function, topology, signal, delay and controlled port.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## SYS-193 — Refresh bounded Printing Pod offer

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after an offer is accepted or rejected and its cycle cooldown
  expires, the system samples new candidate agents or care packages with visible properties.
- Includes: Oxygen Not Included Printing Pod choices and cooldown.
- Excludes: starting Duplicants; unrestricted shops; alternatives retained after selection.
- Parameters: cooldown, count, traits, package quantity, unlock, acceptance and rejection.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## SYS-194 — Complete staffed research from typed points

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible agents operate supplied stations to consume material and
  power, produce required research-point types and unlock the target when costs are met.
- Includes: Oxygen Not Included Research Station, Super Computer, Telescope and Virtual Planetarium.
- Excludes: unstaffed laboratory research; passive experience; ordinary recipes.
- Parameters: station, skill, material, power, point type, target cost, progress and unlocks.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## SYS-195 — Generate persistent historical world and concealed fortress site

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a seed simulates a persistent world's geography, civilizations
  and history, then instantiates the selected multi-level site with concealed
  geology, creatures and structures.
- Includes: Dwarf Fortress world generation and Fortress Mode embark sites.
- Excludes: a rerolled encounter with no persistent world; cosmetic lore.
- Parameters: seed, world age, geography, civilizations, history, site, strata,
  caverns, aquifers and reveal radius.
- Evidence: [Dwarf Fortress decomposition](../games/a-f/dwarf-fortress.md).
- Novelty: not assessed.

## SYS-196 — Route hauling through filtered stockpiles and links

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: available agents claim hauling jobs that move matching items
  toward accepted storage, workshops or explicitly linked destinations.
- Includes: Dwarf Fortress stockpile hauling, containers and give/take links.
- Excludes: conveyor transport without agents; direct item teleportation.
- Parameters: item filter, source, destination, links, containers, path,
  hauling labour and job priority.
- Evidence: [Dwarf Fortress decomposition](../games/a-f/dwarf-fortress.md).
- Novelty: not assessed.

## SYS-197 — Convert worker skill and material into duration, quality and value

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: completing compatible work transforms supplied material while
  worker skill and material properties determine speed, quality and value.
- Includes: Dwarf Fortress workshop products, constructions and crafted goods.
- Excludes: a fixed recipe independent of worker and material; combat injury.
- Parameters: labour, skill, workshop, material, recipe, duration, quality and value.
- Evidence: [Dwarf Fortress decomposition](../games/a-f/dwarf-fortress.md).
- Novelty: not assessed.

## SYS-198 — Accumulate personal needs, memories and stress outcomes

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each resident's bodily and social needs, experienced events,
  personality and remembered emotions update focus and stress, which can
  produce changed behaviour or breakdown.
- Includes: Dwarf Fortress hunger, thirst, sleep, relationships, thoughts,
  memories, unmet needs, stress and tantrums.
- Excludes: one global happiness score; combat morale only.
- Parameters: resident, need, experience, emotion, personality, memory,
  focus, stress threshold and response.
- Evidence: [Dwarf Fortress decomposition](../games/a-f/dwarf-fortress.md).
- Novelty: not assessed.

## SYS-199 — Attract migrants and promote fortress rank

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: population, created and exported wealth, civilization state and
  prior reports determine incoming population and promotion through named
  settlement ranks toward a capital.
- Includes: Dwarf Fortress migration waves, settlement ranks and monarch arrival.
- Excludes: buying one recruit; the post-arrival Mountainhome quest.
- Parameters: population, wealth, exports, civilization, rank thresholds,
  migration size and monarch eligibility.
- Evidence: [Dwarf Fortress decomposition](../games/a-f/dwarf-fortress.md).
- Novelty: not assessed.

## SYS-200 — Resolve strange mood into artifact or collapse

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an eligible resident may claim a workshop, demand a generated
  material list and, if supplied in time, create an artifact and master skill;
  failure produces a declared destructive or fatal outcome.
- Includes: Dwarf Fortress strange moods.
- Excludes: an ordinary work order; random loot with no worker dependency.
- Parameters: eligibility, mood type, workshop, demanded materials, timeout,
  artifact, skill change and failure outcome.
- Evidence: [Dwarf Fortress decomposition](../games/a-f/dwarf-fortress.md).
- Novelty: not assessed.

## SYS-201 — Schedule civilization caravan and resolve barter

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a world-connected civilization sends a timed caravan and liaison;
  at a reachable depot, offered lots exchange according to value, relations and
  trader skill.
- Includes: Dwarf Fortress caravans, trade depots, brokers and agreements.
- Excludes: an always-open shop; off-map trade with no arriving entities.
- Parameters: civilization, season, route, depot, goods, value, broker,
  relations, requests and departure.
- Evidence: [Dwarf Fortress decomposition](../games/a-f/dwarf-fortress.md).
- Novelty: not assessed.

## SYS-202 — Execute world-connected hostile siege and breach plan

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a hostile world faction arrives with generated forces whose
  autonomous plan may path, attack, destroy, dig or build to reach fortress targets.
- Includes: current Dwarf Fortress sieges and invasion planning.
- Excludes: wildlife attacking only by proximity; player-controlled movement.
- Parameters: faction, force, equipment, target, route, breach capability,
  morale, retreat and world consequence.
- Evidence: [Dwarf Fortress decomposition](../games/a-f/dwarf-fortress.md).
- Novelty: not assessed.

## SYS-203 — Schedule storyteller incident from colony pressure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a selected storyteller schedules beneficial, neutral or hostile
  incidents from current time, colony wealth, population, adaptation and difficulty.
- Includes: RimWorld Cassandra Classic raids, traders, disasters and recovery intervals.
- Excludes: a fixed scripted encounter; nearby autonomous combat; pure uniform randomness.
- Parameters: storyteller, cadence, wealth, population, adaptation, threat scale and incident.
- Evidence: [RimWorld decomposition](../games/m-r/rimworld.md).
- Novelty: not assessed.

## SYS-204 — Propagate body-part condition into pawn capacities

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: injuries, disease, missing parts, treatment and replacement parts
  update local body-part state, pain and derived capacities that govern work and survival.
- Includes: RimWorld wounds, bleeding, infection, prostheses and consciousness.
- Excludes: one undifferentiated health total; mood without bodily impairment.
- Parameters: part, condition, severity, bleeding, treatment, capacity and fatal threshold.
- Evidence: [RimWorld decomposition](../games/m-r/rimworld.md).
- Novelty: not assessed.

## SYS-205 — Evolve interpersonal opinion and relationship

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: proximity, traits, kinship, social interactions and remembered
  events update directed opinions and may create or end persistent relationships.
- Includes: RimWorld friendships, rivalries, romances, marriages, breakups and social fights.
- Excludes: one global happiness value; a fixed biography with no causal effect.
- Parameters: pair, compatibility, interaction, memory, opinion and relationship transition.
- Evidence: [RimWorld decomposition](../games/m-r/rimworld.md).
- Novelty: not assessed.

## SYS-206 — Reduce prisoner resistance and resolve recruitment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible social work repeatedly changes a captive's resistance
  and recruitment state until a probabilistic attempt converts them or they remain captive.
- Includes: RimWorld warden recruitment of captured pawns.
- Excludes: an instant purchased recruit; scripted joining without custody.
- Parameters: resistance, will, mood, warden skill, attempt chance and outcome.
- Evidence: [RimWorld decomposition](../games/m-r/rimworld.md).
- Novelty: not assessed.

## SYS-207 — Complete staffed research and unlock colony technology

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible researchers operate suitable benches to add persistent
  progress to the selected prerequisite-valid project and unlock it at its cost.
- Includes: RimWorld base-game research from simple and hi-tech benches.
- Excludes: unstaffed laboratory packs; passive personal experience; ordinary crafting.
- Parameters: project, prerequisites, bench, facilities, researcher, speed, cost and unlocks.
- Evidence: [RimWorld decomposition](../games/m-r/rimworld.md).
- Novelty: not assessed.

## SYS-208 — Resolve drafted ranged attack through cover and body hit

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a commanded ranged attack resolves aim, range, intervening cover,
  armour and hit location into a miss or a wound on a specific body part.
- Includes: RimWorld drafted firearm combat and cover-dependent injury;
  Counter-Strike 2 firearm resolution through range, material, armour and hit
  group; Cyberpunk 2077 ranged attacks through cover, armour and body regions.
- Excludes: abstract card damage; automatic engagement with no tactical target order.
- Parameters: shooter, weapon, range, cover, accuracy, armour, body part and damage.
- Evidence: [RimWorld decomposition](../games/m-r/rimworld.md) and
  [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## SYS-209 — Generate seeded planet and landing map

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a seed creates a persistent planet of biomes, factions and sites,
  then instantiates the chosen landing tile with terrain, resources and inhabitants.
- Includes: RimWorld planet generation and Crashlanded map creation.
- Excludes: simulated deep civilization history; a fixed authored level.
- Parameters: seed, coverage, temperature, rainfall, factions, biome, terrain and map size.
- Evidence: [RimWorld decomposition](../games/m-r/rimworld.md).
- Novelty: not assessed.

## SYS-210 — Complete a selected material delivery into a persistent capability unlock

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when the player supplies every declared material quantity for the
  currently selected progression requirement, the system irreversibly completes
  that requirement and adds its disclosed buildings, recipes, equipment, tiers
  or other capability bundle to the current save.
- Includes: Satisfactory HUB Milestones and Space Elevator Project Assembly
  phase deliveries unlocking their listed rewards and later tiers.
- Excludes: a laboratory consuming science packs over time; a Vortex checking
  an exact geometric-shape schema; purchasing one optional research upgrade
  with accumulated points.
- Parameters: selected requirement, item identities and quantities, submission
  channel, optional completion delay, reward set, next requirement and whether
  delivery is manual or conveyor-fed.
- Evidence: [Satisfactory decomposition](../games/s-z/satisfactory.md).
- Novelty: not assessed.

## SYS-211 — Trip a connected power grid on uncovered demand deficit

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when the current demand of one connected electrical grid exceeds
  its generation plus available storage, the grid enters a tripped state and
  its consumers cease normal operation until the player restores a viable
  supply and resets it.
- Includes: Satisfactory's power-trip response after a grid exceeds production
  and has no storage coverage.
- Excludes: proportionally sharing insufficient supply by slowing consumers;
  one machine lacking a local fuel or input item; an authored fail-state timer.
- Parameters: graph topology, generation, demand, stored energy, trip warning,
  reset action, priority switching and recovery condition.
- Evidence: [Satisfactory decomposition](../games/s-z/satisfactory.md).
- Novelty: not assessed.

## SYS-212 — Resolve a targeted terrain-cell break and its eligible drop

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a completed valid break removes the addressed mutable terrain
  tile, wall or placed object and emits its eligible world-item result,
  persistently changing local geometry.
- Includes: Minecraft Survival block breaking and tool-dependent drops;
  Terraria tool-dependent mining, wall removal and recovered furniture.
- Excludes: moving a rigid free object; terrain changes made by an autonomous
  worker; placing a non-voxel factory building.
- Parameters: projection, layer, tile state, tool, harvest rule, drop, gravity
  and neighbour update.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md) and
  [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## SYS-213 — Generate a seed-determined mutable tile world

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a world seed determines mutable tile terrain, resources, biomes
  and discoverable geography, whether the finite world is generated before play
  or later reached regions instantiate from the same seed.
- Includes: Minecraft Java Survival chunked Overworld generation; Terraria
  finite world generation with seeded layers, caves, ores, biomes and structures.
- Excludes: a fixed level; a fully simulated historical civilization planet;
  random outcomes independent of a persistent world seed.
- Parameters: seed, generator version, projection, finite extent, generation
  timing, biome, terrain, structure placement and chunk horizon.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md) and
  [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## SYS-214 — Update hunger, health and regeneration

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: real-time activity, food and damage update an avatar's hunger and
  health, while sufficiently high hunger permits automatic health regeneration.
- Includes: Minecraft Survival hunger, food, starvation damage and regeneration.
- Excludes: a permanently ending one-life mode; one global colony need score;
  an encounter-local health bar restored automatically after each fight.
- Parameters: hunger, saturation, health, food value, regeneration threshold
  and damage source.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md).
- Novelty: not assessed.

## SYS-215 — Resolve direct real-time hostile combat

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: direct avatar and hostile attacks apply range, cooldown, damage,
  armour, knockback and defeat effects while the world continues in real time.
- Includes: Minecraft Survival hostile-mob fights and Ender Dragon attacks;
  Counter-Strike 2 firefights; Dota 2 hero attacks and ability combat; and
  Cyberpunk 2077 firearm, melee and offensive quickhack combat; Marvel Rivals
  simultaneous hero attacks and damaging abilities; Hollow Knight: Silksong
  needle, Tool and Silk Skill combat against live hostiles.
- Excludes: autonomous squad engagement; a telegraphed turn queue; a boss with
  no linked destructible healing condition.
- Parameters: target, attack, armour, cooldown, projectile, damage, knockback
  and defeat drop.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md),
  [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md), and
  [Dota 2 decomposition](../games/a-f/dota-2.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md),
  [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md), and
  [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## SYS-216 — Drop carried inventory on death and respawn the avatar

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when ordinary Survival health reaches zero, carried inventory is
  emitted at the death position and the avatar returns at its active spawn
  point while the same persistent world continues.
- Includes: Minecraft Java Survival death, dropped inventory and respawn.
- Excludes: Hardcore world termination; an encounter restart that restores a
  checkpoint inventory; damage without death.
- Parameters: death position, dropped stacks, loaded-item lifetime, spawn point
  and retained world state.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md).
- Novelty: not assessed.

## SYS-217 — Resolve held-tile placement and neighbour updates

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a valid placement consumes one held tile item, writes its block,
  wall or placed-object state into the addressed compatible world cell or
  footprint and applies resulting neighbour updates.
- Includes: Minecraft Survival construction and local traversability changes;
  Terraria block, wall, platform, torch and furniture placement.
- Excludes: breaking a block; moving a free rigid body; placing an abstract tile.
- Parameters: projection, layer, held stack, cell, footprint, tile state,
  orientation, support and neighbour update.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md) and
  [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## SYS-218 — Fly a thrown locator toward the nearest target then drop or shatter

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a thrown locator travels along the bearing toward the nearest
  eligible hidden target, then either becomes recoverable or is destroyed by a
  fixed random outcome.
- Includes: Minecraft Eye of Ender stronghold locating and its shatter chance.
- Excludes: a compass with continuous display; a projectile that damages its target.
- Parameters: nearest target, bearing, flight duration, drop and shatter chance.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md).
- Novelty: not assessed.

## SYS-219 — Activate a dimension portal from a completed frame state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when a portal frame reaches its required geometry and activation
  state, the system replaces its interior with an active traversal surface.
- Includes: igniting a valid Minecraft Nether frame and filling every End portal
  frame slot with an Eye of Ender.
- Excludes: travelling through an already active portal; a door opened by one key.
- Parameters: frame type, geometry, filled slots, ignition and active surface.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md).
- Novelty: not assessed.

## SYS-220 — Transfer the avatar through an active dimension portal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: sustained contact with an active portal transfers the avatar and
  carried state to the corresponding destination dimension and arrival region.
- Includes: Minecraft Nether portal transfer and End portal entry.
- Excludes: portal activation; free teleportation to any chosen coordinate.
- Parameters: portal type, contact duration, destination dimension and arrival.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md).
- Novelty: not assessed.

## SYS-221 — Heal the Ender Dragon from active linked crystals

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an intact End crystal can periodically restore health to the
  linked Ender Dragon; destroying that crystal removes only that healing source.
- Includes: Minecraft Ender Dragon crystal healing.
- Excludes: making the Dragon immune to all damage until every crystal is gone;
  ordinary hostile regeneration with no linked world object.
- Parameters: crystal state, link, healing rate and Dragon health.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md).
- Novelty: not assessed.

## SYS-222 — Pick up an eligible world item into carried inventory on contact

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: avatar contact with an eligible dropped world item transfers as
  much of its stack as compatible carried inventory capacity accepts.
- Includes: Minecraft collecting block drops and recovering death drops;
  Counter-Strike 2 collecting a compatible dropped weapon, grenade or C4.
- Excludes: crediting an abstract score collectible; opening a container UI.
- Parameters: item entity, pickup delay, stack type, capacity and remainder.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md) and
  [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md).
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## SYS-223 — Reduce tool durability on eligible use and remove it at exhaustion

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an eligible use subtracts durability from the active tool, and a
  tool reaching zero durability breaks and leaves its carried slot.
- Includes: Minecraft Survival tools, weapons and flint-and-steel wear.
- Excludes: consuming a stacked ingredient; permanent tools with no wear state.
- Parameters: tool, use class, durability cost, remaining durability and break.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md).
- Novelty: not assessed.

## SYS-224 — Consume coal to sustain configured city heat sources

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while the generator and connected local heat sources are enabled,
  they continuously debit coal at rates determined by their configured output
  and cease supplying ordinary heat when fuel is unavailable.
- Includes: Frostpunk generator, Steam Hub and heater coal consumption.
- Excludes: Overdrive stress; building temperature aggregation; a power grid.
- Parameters: source, output, range, efficiency, hourly coal rate, reserve and
  fuel-exhaustion response.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## SYS-225 — Compute occupied-building heat from weather, insulation and sources

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: each occupied home or workplace receives a discrete heat state
  from current ambient temperature plus its insulation, active heat-zone and
  local-heater modifiers.
- Includes: Frostpunk Comfortable through Freezing building conditions.
- Excludes: coal consumption; illness resolution; material phase change.
- Parameters: ambient level, insulation, generator zone, Steam Hub, heater,
  special modifier and resulting heat category.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## SYS-226 — Convert cold exposure into staged citizen sickness

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: time spent by citizens in homes or workplaces at each heat
  category contributes a bounded risk of becoming sick or gravely ill.
- Includes: Frostpunk cold-related sickness and frostbite risk.
- Excludes: a scripted accident independent of temperature; medical treatment;
  one undifferentiated health total.
- Parameters: citizen, exposure duration, heat category, difficulty, illness
  stage and random check.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## SYS-227 — Admit and treat eligible illness in staffed medical capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: sick citizens seek compatible free medical beds, where eligible
  staff and facility rules accumulate treatment until recovery; untreated
  illness worsens and may become fatal.
- Includes: Frostpunk Medical Posts, Infirmaries, Houses of Healing and Care Houses.
- Excludes: preventing sickness through heat; instant healing; body-part surgery.
- Parameters: illness stage, bed capacity, facility, staff, heat, efficiency,
  treatment rule, duration, worsening and death.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## SYS-228 — Accumulate and release generator stress from Overdrive

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: enabled Overdrive raises generator stress over live time while
  disabled Overdrive releases it; reaching critical state triggers an available
  emergency response or generator destruction.
- Includes: Frostpunk Overdrive heat bonus, stress gauge and explosion risk.
- Excludes: ordinary coal depletion; The Fall of Winterhome maintenance failure.
- Parameters: overdrive state, stress rate, cooling rate, warning threshold,
  critical threshold, rescue availability and explosion.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## SYS-229 — Advance authored scenario weather and temperature forecast

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: scenario time advances through an authored weather schedule whose
  forecast temperature changes modify every city's ambient heat condition.
- Includes: A New Home cold snaps, temporary rises and the final Great Storm.
- Excludes: a repeating three-season cycle; cell-based thermal diffusion;
  independently sampled cosmetic weather.
- Parameters: scenario time, forecast horizon, temperature step, storm phase
  and active modifiers.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## SYS-230 — Trigger authored city event arc and resolve chosen consequence

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: matching time, city state or prior-arc conditions present an
  authored dilemma, promise or objective whose committed response applies its
  declared persistent and timed consequences.
- Includes: A New Home shelter and food promises, Winterhome, Londoners,
  refugees, storm preparation and moral law events.
- Excludes: a uniformly random incident generator; recipe completion; flavour dialogue.
- Parameters: trigger, prior arc, options, promise, deadline, completion state,
  population, resource and welfare consequence.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## SYS-231 — Consume population food rations and advance hunger state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each citizen periodically consumes one eligible prepared ration;
  insufficient supply advances hunger and then starvation toward death.
- Includes: Frostpunk normal, Soup or Food Additives rations and daily feeding.
- Excludes: raw-food production; directly controlled avatar eating; food preferences.
- Parameters: population, ration type, interval, reserve, hunger, starvation and death.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## SYS-232 — Aggregate city conditions into Hope and Discontent

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: laws, events, promises, deaths, shortages, work rules and active
  social facilities apply declared changes or modifiers to the city's paired
  Hope and Discontent tracks.
- Includes: Frostpunk Hope and Discontent trends, Londoner pressure and crises.
- Excludes: group production Resolve; individual mood; an opaque approval score.
- Parameters: hope, discontent, modifier source, permanence, trend, threshold,
  purpose replacement and crisis grace period.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## SYS-233 — Apply signed law rule and lock exclusive alternatives

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: signing a law persistently changes its declared city rule,
  unlocks listed facilities or abilities and removes any mutually exclusive
  alternative from later selection.
- Includes: Frostpunk work, food, medical, child, Order and Faith laws.
- Excludes: research progress; reversible local policy; one event response.
- Parameters: law, rule effect, unlocked content, alternative, welfare change,
  follow-up event and ending judgement.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## SYS-234 — Resolve Frostland exploration into cargo, people and revealed nodes

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when a travelling team reaches and explores a world-map location,
  the selected resolution can add carried resources or survivors, remove the
  team, and reveal declared successor destinations.
- Includes: A New Home scout exploration, risk dilemmas and returning cargo.
- Excludes: city hauling; passive camera reveal; direct-control combat.
- Parameters: location, option, outcome, cargo, survivors, revealed nodes,
  team survival and return.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## SYS-235 — Route available citizens to construction tasks and complete plans

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: available eligible citizens autonomously travel to prioritised
  placed construction or demolition tasks and accumulate labour until the
  planned structure changes state.
- Includes: Frostpunk building, road construction, upgrades and dismantling.
- Excludes: a staffed production job; instantly placed player-held entity;
  user-steered builder movement.
- Parameters: task, priority, free labour, route, build time, pause, completion and refund.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## SYS-236 — Generate a deterministic star cluster from setup seed

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: new-game setup resolves a declared seed and cluster parameters
  into a repeatable spatial set of stars, orbiting planets, resource deposits
  and hostile presences that persists for the run.
- Includes: Dyson Sphere Program seeded 32–64-star clusters with different
  planet and resource distributions.
- Excludes: expanding voxel terrain only when visited; one fixed authored
  star map; random production output after setup.
- Parameters: seed, star count, resource multiplier, star and planet types,
  orbit layout, deposits and combat setting.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## SYS-237 — Consume and replenish a mecha core-energy reserve

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: construction drones, movement regimes, replicator work and combat
  debit a shared mecha-core energy reserve while the fuel chamber and compatible
  external charging restore it over live time.
- Includes: Dyson Sphere Program Icarus core capacity, fuel generation,
  wireless charging and high-energy sail or warp travel.
- Excludes: a factory's connected power-grid satisfaction; character health;
  consuming one Space Warper to activate warp.
- Parameters: core capacity, current energy, action drain, fuel, generation
  rate, fuel bonus, charging input and insufficient-energy slowdown.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## SYS-238 — Integrate controlled mecha travel across planetary and stellar frames

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: continuous steering and velocity move the controlled mecha across
  a planet, into orbital or interplanetary space and through accelerated warp,
  with takeoff, gravity capture and landing changing its current spatial frame.
- Includes: Dyson Sphere Program Icarus walking, flying, sailing between planets
  and warping between star systems.
- Excludes: autonomous logistics-vessel delivery; a menu-selected fast-travel
  transition; scout travel resolved without direct steering.
- Parameters: position, heading, speed, acceleration, frame, gravity, drive
  level, energy drain, target indicator and landing.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## SYS-239 — Match logistics-station requests and dispatch cargo carriers

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the logistics network pairs compatible supply and demand slots,
  then an eligible charged station dispatches a drone or vessel to transfer a
  bounded cargo load and return.
- Includes: Dyson Sphere Program local drones, interplanetary vessels and
  warper-enabled interstellar station routes.
- Excludes: directional belt transport; manually carrying inventory; a train
  following a player-authored stop schedule.
- Parameters: item, local or remote mode, supply, demand, storage, carrier,
  load threshold, range, energy charge, warper and trip state.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## SYS-240 — Insert launched solar sails into a configured orbit and age them

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an eligible EM-Rail Ejector consumes supplied solar sails and
  inserts them into the selected swarm orbit, where free sails contribute
  luminosity until their finite lifetime expires or a shell absorbs them.
- Includes: Dyson Sphere Program Dyson Swarm orbit insertion and sail expiry.
- Excludes: rockets constructing solid nodes and frames; surface logistics;
  permanent sails already incorporated into a shell.
- Parameters: ejector, sail, target orbit, pitch window, launch cadence,
  sail lifetime, luminosity and absorption availability.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## SYS-241 — Apply launched rockets and sails to a planned Dyson structure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: supplied launch silos consume Small Carrier Rockets whose payload
  incrementally materialises planned nodes and frames; completed frame regions
  then absorb available solar sails until their planned shell is filled.
- Includes: Dyson Sphere Program persistent Dyson Sphere construction.
- Excludes: free-orbit sail lifetime; editing the plan; one scripted completed
  megastructure granted without material launches.
- Parameters: plan element, rocket payload, node and frame points, shell cell,
  required structure, absorbed sails and completion state.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## SYS-242 — Convert swarm or sphere output into receiver power or photons

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: active swarm and sphere components generate star-scaled output;
  a continuously receiving Ray Receiver converts its allocated share into
  connected-grid power or, in unlocked photon mode, Critical Photons.
- Includes: Dyson Sphere Program Ray Receiver energy generation and photon
  production for antimatter.
- Excludes: burning an Antimatter Fuel Rod locally; solar-panel generation;
  producing Universe Matrix directly.
- Parameters: star luminosity, swarm and shell output, requested power,
  continuous receiving, efficiency, receiver mode, lens and photon cadence.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## SYS-243 — Accumulate industrial threat and dispatch hostile attack waves

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: configured hostile bases accumulate threat from the player's
  industrial energy use or aggression; reaching the current threshold launches
  a bounded wave toward the mecha or factory and resets or advances pressure.
- Includes: default Regular Dark Fog planetary attacks in Dyson Sphere Program.
- Excludes: Factorio's spatially diffusing pollution cloud; a fixed authored
  wave timer; enemies that only retaliate when directly struck.
- Parameters: base, power-threat factor, aggression, current threat, threshold,
  wave size, target, level and reset state.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## SYS-244 — Resolve residence needs into occupancy, income and happiness

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each residence compares its population tier's current basic and
  luxury supplies with demand, then updates occupancy, tax income and happiness.
- Includes: Anno 1800 residences gaining residents from basic needs and
  happiness or income from luxury needs.
- Excludes: the player's explicit tier-upgrade command; workforce allocation to
  production buildings; a one-time quest reward.
- Parameters: tier, residence count, need, supply, consumption, occupancy,
  income, happiness and shortage response.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## SYS-245 — Apply tiered island workforce balance to workplace productivity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an island totals residents and jobs separately by population
  tier, then reduces operation when a workplace's required tier lacks labour.
- Includes: Anno 1800 Farmer, Worker, Artisan, Engineer and Investor workforce
  balances affecting production and services on their island.
- Excludes: assigning named workers to individual job slots; goods shortage;
  an unlimited abstract labour bonus.
- Parameters: island, tier, available workforce, job demand, commuter transfer,
  shortage and productivity multiplier.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## SYS-246 — Execute scheduled trade route by cargo slots and port orders

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: assigned ships repeatedly traverse their ordered ports and apply
  each cargo slot's valid load or unload instruction against island storage.
- Includes: Anno 1800 trade-route cycles between Old and New World islands.
- Excludes: local cart delivery; manual harbour transfer; automatically matched
  station demand without a player-authored schedule.
- Parameters: route, ship, stop, travel time, cargo slot, order, island stock,
  minimum reserve, capacity and waiting rule.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## SYS-247 — Allocate and release influence across strategic investments

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: population and Investors expand a finite influence pool while
  owned islands, ships, defences, propaganda and other investments commit
  portions that return when the associated investment is removed or expires.
- Includes: Anno 1800 influence categories and temporary newspaper spending.
- Excludes: treasury purchase costs; workforce; a permanent technology point.
- Parameters: population tier, pool, category, investment, committed amount,
  refund condition and temporary duration.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## SYS-248 — Generate newspaper issue and apply published propaganda

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: at recurring publication intervals the system selects articles
  from recent settlement conditions, accepts eligible replacements, and applies
  the published issue's effects until the next issue.
- Includes: Anno 1800 newspaper reports and propaganda with accumulating riot risk.
- Excludes: fixed campaign narration; a permanent law; hidden random modifiers.
- Parameters: interval, observed condition, article, propaganda slot, effect,
  influence, duration and repeated-use penalty.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## SYS-249 — Trigger and resolve city incidents through emergency services

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: density, working conditions and local risk can initiate fire,
  illness or riot states that spread or damage buildings while reachable staffed
  emergency services dispatch units to contain them.
- Includes: Anno 1800 fire stations, police stations and hospitals responding
  through the road network.
- Excludes: naval combat; a scripted quest explosion with no civic response;
  passive service coverage without an incident.
- Parameters: incident type, risk, trigger, spread, damage, service range,
  mobilised units, response time and containment.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## SYS-250 — Resolve expedition skills and morale through event sequence

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an expedition advances through bounded events whose visible
  options test carried skills or consume supplies, changing morale and either
  continuing, returning or completing the voyage.
- Includes: Anno 1800's New World discovery expedition and its region unlock.
- Excludes: direct ship steering; a cyclic trade route; one fixed quest payment.
- Parameters: event, option, skill chance, cargo consumption, morale, reward,
  return threshold and completion unlock.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## SYS-251 — Advance authored cross-region campaign quest sequence

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: completing declared construction, delivery, expedition and combat
  requirements advances a persistent authored campaign through its chapters,
  changing available regions, characters and follow-up objectives.
- Includes: Anno 1800's prologue and four campaign chapters through the final battle.
- Excludes: optional sandbox play after the story; generic population unlocks;
  one independent timed task.
- Parameters: chapter, quest, prerequisites, delivery, region flag, authored
  world change, failure policy and successor.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md) and
  [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## SYS-252 — Resolve directly commanded real-time naval combat

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: mobile ships acquire commanded targets, move within navigable
  water and exchange range-, facing-, cadence- and armour-dependent damage until
  retreat, surrender or destruction.
- Includes: Anno 1800 warships and command ships in the campaign's final battle.
- Excludes: land combat; harbour weapons firing without a target command;
  expedition events resolved as choices.
- Parameters: ship, target, range, broadside arc, attack speed, damage, armour,
  hit points, movement, stance and destruction.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## SYS-253 — Advance World’s Fair construction and supplied exhibition

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the monument progresses through ordered construction phases after
  receiving each phase's materials, workforce and utilities; a completed venue
  then runs a selected exhibition whose supplied goods determine its reward tier.
- Includes: constructing Anno 1800's World’s Fair and completing one exhibition.
- Excludes: an ordinary repeatable factory recipe; a cosmetic monument granted
  complete; DLC monuments.
- Parameters: investor threshold, phase, materials, workforce, electricity,
  exhibition type and size, preparation time, supplied goods and reward tier.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## SYS-254 — Generate seeded multi-region archipelago

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a declared setup seed and settings instantiate persistent island
  layouts, fertilities, resource deposits and navigable water across linked
  regional sessions, while authored campaign islands may remain fixed.
- Includes: Anno 1800 Old World and New World campaign sessions.
- Excludes: a wholly fixed single map; generating a new island during play;
  DLC regions outside the scoped base game.
- Parameters: seed, region, island, fertility, deposit, coastline, session link
  and fixed campaign exception.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## SYS-255 — Redistribute terrain water and badwater in three dimensions

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: source output and conserved surface volumes flow, mix, equalise
  and evaporate through 3D terrain while barriers, openings and pumps alter them.
- Includes: Timberborn reservoirs, dams, levees, floodgates, pumps and valves.
- Excludes: pipe-only packets; binary irrigation radius; multi-element gases.
- Parameters: elevation, volume, flow, contamination, evaporation and opening.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## SYS-256 — Alternate escalating temperate, drought and badtide weather

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: cycles alternate temperate periods with forecast drought or
  badtide events drawn within progressively harsher mode-specific bounds.
- Includes: Timberborn Normal weather and initial handicaps.
- Excludes: fixed authored weather; cosmetic seasons.
- Parameters: cycle, event, forecast, duration, chance and source substitution.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## SYS-257 — Update plant growth from local water and contamination

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: plants grow only under compatible soil-water or aquatic-depth
  state; dryness, submersion or contamination arrests growth or kills them.
- Includes: Timberborn crops and trees.
- Excludes: abstract farm yield independent of terrain water.
- Parameters: species, growth, irrigation, depth, contamination and death.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## SYS-258 — Advance beaver needs, well-being, ageing and lifespan

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each beaver consumes food and water, seeks sleep and well-being
  effects, ages and receives threshold-dependent performance and life modifiers.
- Includes: Timberborn hunger, thirst, shelter, nutrition and attractions.
- Excludes: one aggregate happiness score; oxygen/bladder metabolism.
- Parameters: needs, effects, productivity, movement, growth, age and lifespan.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## SYS-259 — Reproduce Folktails toward available housing capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible adult Folktails produce children over time while lodge
  capacity remains; children mature and deaths reopen capacity with delay.
- Includes: Timberborn natural Folktail reproduction.
- Excludes: Iron Teeth breeding pods; immigration; instant residents.
- Parameters: adults, children, beds, reproduction, maturation and death.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## SYS-260 — Balance mechanical power across connected shafts and storage

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: connected generators supply variable output through shafts,
  consumers draw demand, and storage absorbs surplus or releases deficits.
- Includes: Timberborn wheels, windmills, engines, clutches and Gravity Batteries.
- Excludes: road-radius electricity; isolated fuel recipes.
- Parameters: topology, generation, demand, clutch, storage and discharge.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## SYS-261 — Propagate automation signals and apply target state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: sensors sample simulation values, logic transforms their signals,
  and connected targets adopt the resulting operating state.
- Includes: Timberborn water, weather and power automation.
- Excludes: manual toggles; hidden AI; missing-input recipe stops.
- Parameters: value, threshold, logic, graph, signal and target response.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## SYS-262 — Accumulate staffed Science Points for map unlocks

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: staffed science workplaces add points over live time to an
  uncapped map-local balance that funds persistent construction unlocks.
- Includes: Timberborn Inventors and later science workplaces.
- Excludes: queued multi-item technologies; profile metacurrency.
- Parameters: workplace, staffing, rate, power, balance and unlock cost.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## SYS-263 — Construct, provision and activate Earth Recultivator

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after its science gate, the faction wonder accepts its large
  construction set, then consumes separate launch supplies for the first win.
- Includes: Timberborn Folktails Earth Recultivator.
- Excludes: ordinary recipes; Iron Teeth's wonder; repeated launches.
- Parameters: science, build materials, progress, launch goods and win flag.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## SYS-264 — Advance citizen life, needs and capability state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: individual citizens age, learn, consume services and goods, work,
  reproduce and change health, happiness and loyalty over simulation time.
- Includes: Workers & Resources residents, education tiers, needs and births.
- Excludes: one aggregate city-demand bar or instant purchased population.
- Parameters: age, education, need, health, happiness, loyalty, housing and time.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## SYS-265 — Route citizens to jobs and services through public transport

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: citizens search reachable walking and enabled transport paths for
  an eligible free workplace or needed service, wait, ride and abandon trips at
  declared time limits.
- Includes: Workers & Resources workers and passengers using stops and lines.
- Excludes: player-authored cargo only or abstract traffic without people.
- Parameters: purpose, reach, stop types, job slots, wait, ride and total travel time.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## SYS-266 — Execute scheduled multi-modal vehicle service

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an assigned road, rail, ship or aircraft vehicle repeatedly
  follows ordered stops, loads and unloads allowed passengers or cargo, refuels
  and is delayed by network traffic and facility throughput.
- Includes: Workers & Resources lines and their vehicles.
- Excludes: distribution-office request matching or direct steering.
- Parameters: mode, stops, load rules, capacity, speed, fuel, traffic and wait conditions.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## SYS-267 — Dispatch construction inputs by site phase

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a construction office selects assigned sites by priority and
  sends compatible vehicles to fetch the materials, mechanisms and workers
  required by each current construction phase.
- Includes: Workers & Resources groundworks and later building phases.
- Excludes: instant money construction or generic agent-carried building.
- Parameters: site, phase, source, vehicle, material, workers, priority and progress.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## SYS-268 — Dispatch office cargo from storage thresholds

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a distribution office compares configured source and destination
  storage percentages, then sends an eligible vehicle to transfer the selected
  resource when a rule is triggered.
- Includes: Workers & Resources road and railway distribution offices.
- Excludes: an ordered vehicle line or drone station pair.
- Parameters: resource, thresholds, source, destination, vehicle, load and reach.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## SYS-269 — Settle physical border trade in two responsive markets

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: goods or vehicles physically crossing a Soviet or NATO border
  debit or credit its currency, while sustained traded volume and world factors
  update later market prices.
- Includes: Workers & Resources customs houses and foreign power connections.
- Excludes: municipal taxation or a fixed shop price.
- Parameters: bloc, currency, commodity, volume, direction, price and threshold.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## SYS-270 — Propagate capacity and loss through republic utilities

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: generated or imported electricity, heat, water and sewage move
  through compatible networks, with capacity, pressure, temperature, loss and
  outage changing building operation and citizen welfare.
- Includes: Workers & Resources power grids, heating, water and sewage.
- Excludes: decorative pipes or one building's isolated fuel inventory.
- Parameters: utility, topology, capacity, voltage, pressure, temperature, loss and demand.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## SYS-271 — Apply seasons, pollution, fire and deterioration

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: live weather and industry change temperature, pollution and fire
  risk while enabled vehicles and structures wear and create waste, producing
  maintenance, health and emergency pressure.
- Includes: advanced systems exercised by the second base campaign.
- Excludes: authored campaign objectives or nuclear radiation alone.
- Parameters: season, temperature, pollution, ignition, wear, waste and response.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## SYS-272 — Convert staffed university workdays into research unlocks

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: qualified university staff accumulate workdays on the selected
  reachable project until it unlocks its declared capability.
- Includes: Workers & Resources technical and medical research.
- Excludes: buying a technology with abstract global points.
- Parameters: project, prerequisites, faculty, workers, professors, workdays and unlock.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## SYS-273 — Run the nuclear fuel, reactor and waste cycle

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: uranium processing and staffed fabrication produce fuel; a
  staffed, fuelled and cooled reactor generates power and radioactive waste,
  with blocked waste or failed safety systems stopping or endangering operation.
- Includes: the Workers & Resources nuclear chain used by Campaign 2.
- Excludes: generic coal power or a scripted counter without production.
- Parameters: uranium, chemicals, fuel, staff, cooling, output, waste and radiation.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## SYS-274 — Advance campaign branches from measured republic objectives

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the campaign script observes declared construction, production,
  import and export totals, completes objectives and releases their next branch
  until the current campaign is complete.
- Includes: the two released base-game Workers & Resources campaigns.
- Excludes: sandbox play without objectives or platform achievements.
- Parameters: campaign, branch, objective, measured total, prerequisite and completion.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## SYS-275 — Excavate and dump conserved terrain material

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: excavators remove typed material from designated terrain volume,
  vehicles carry that loose quantity, and dumping adds it to another terrain
  volume whose surface settles according to material slope.
- Includes: Captain of Industry mines, cut ramps, spoil piles, land reclamation
  and material-specific dumping zones.
- Excludes: an extractor reducing only a numeric deposit; decorative terrain
  painting; water-cell flow without vehicle-carried loose material.
- Parameters: designation height, material, density, excavator bucket, vehicle
  load, dump filter, surface elevation, angle of repose and avalanche.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## SYS-276 — Dispatch paired mine excavator and haul-truck jobs

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a mine control tower assigns its available excavators to
  reachable designations and pairs trucks to receive each bucket and deliver
  the resulting load to a compatible destination or dumping zone.
- Includes: Captain of Industry tower-assigned excavators and trucks returning
  to idle when no reachable dig or unload exists.
- Excludes: generic factory belts; a manually driven vehicle; construction
  offices dispatching phase-specific crews and mechanisms.
- Parameters: tower area, designation, excavator, truck, material preference,
  reachability, receiver capacity, fuel and idle state.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## SYS-277 — Match island vehicle jobs across configured buffers

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the island logistics dispatcher matches available compatible
  vehicles to producer, storage and consumer pickup or delivery requests using
  import, export, assignment and buffer rules.
- Includes: Captain of Industry trucks hauling construction parts, fuel and
  products among machines and storages, including dedicated routes.
- Excludes: belt or pipe flow; mine-tower excavator pairing; a fixed rail
  schedule or distribution office with authored percentage endpoints.
- Parameters: product state, source, destination, buffer, import/export mode,
  dedicated assignment, vehicle class, reservation, route and priority.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## SYS-278 — Convert settlement supply and pollution into Unity and population state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: settlements consume population-scaled food and services while
  fulfilled variety and services generate Unity or health and pollution and
  shortages reduce health, growth or population.
- Includes: Captain of Industry housing, food markets, water, waste, household
  goods, clinics, air pollution and water pollution.
- Excludes: individual citizens choosing destinations; a fixed happiness score
  with no supplied services; factory recipes outside settlement demand.
- Parameters: population, housing tier, food categories, service demand,
  fulfilment, Unity, health, pollution, growth and mortality.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## SYS-279 — Consume pooled maintenance and break down uncovered entities

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: operating machines and vehicles drain tiered island-wide
  maintenance pools; insufficient coverage accumulates failure pressure and
  temporarily breaks entities until ordinary or Unity repair resolves them.
- Includes: Captain of Industry Maintenance I–III production, global
  distribution and shortage breakdowns.
- Excludes: manually delivered repair parts to one site; permanent vehicle
  wear; a recurring monetary building upkeep fee.
- Parameters: maintenance tier, production, pool, consumption, shortage,
  breakdown probability, downtime and Unity repair.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## SYS-280 — Resolve industrial ship exploration and world-node operation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the repaired main ship spends fuel to travel between revealed
  world nodes, resolves strength-gated encounters and returns loot or unlocks
  villages, cargo ships and staffed resource locations.
- Includes: Captain of Industry world-map exploration, ship upgrades, battles,
  outpost repair and later resource pickup.
- Excludes: home-island truck routing; recurring trade contracts; a freely
  navigated real-time ocean vessel.
- Parameters: node graph, distance, fuel, ship strength, enemy strength,
  damage, repair cargo, loot, manpower, Unity and resource stock.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## SYS-281 — Settle quick trades and recurring cargo contracts

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an accepted village offer exchanges its specified goods, while
  an active contract repeatedly loads exports and returns imports through its
  dedicated cargo ship and debits establishment, voyage and recurring Unity.
- Includes: Captain of Industry trading dock exchanges and cargo-depot contracts.
- Excludes: domestic vehicle delivery; world-node resource outposts; border
  markets with responsive prices and two currencies.
- Parameters: offer, product ratio, reputation, Unity costs, depot module,
  cargo-ship capacity, load, voyage and cancellation.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## SYS-282 — Assemble, transfer, fuel and launch an industrial rocket

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a supplied assembly depot consumes the declared components to
  construct a rocket, a specialised transporter moves it over level terrain to
  a free pad, and connected propellant and water permit the launch sequence.
- Includes: Captain of Industry's first completed base-game rocket launch.
- Excludes: ordinary factory recipes; repeated orbital-station supply after
  the first launch; Factorio silo part assembly inside one entity.
- Parameters: rocket tier, components, workforce, power, transporter path,
  pad availability, propellant, water, payload and first-launch flag.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## SYS-283 — Scan a Mars sector and resolve revealed anomalies

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: sector scanning progressively reveals deposits, anomalies and
  entrances in the selected map area; an eligible explorer resolving a
  revealed anomaly grants its disclosed research, technology or event result.
- Includes: Surviving Mars: Relaunched surface sector scanning and RC Explorer
  anomaly analysis.
- Excludes: ordinary camera reveal; mining an already known deposit; optional
  mystery-story completion.
- Parameters: sector, scan progress, queue, deposit, anomaly, explorer,
  analysis duration, research reward and revealed technology.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## SYS-284 — Balance stored Martian life-support networks

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: connected producers, consumers and tanks continuously balance
  water and oxygen supply, demand and stored reserve, with deficits disabling
  dependent buildings and endangering occupied domes.
- Includes: Surviving Mars: Relaunched water and oxygen grids, tanks, MOXIEs,
  extractors, vaporators and dome demand.
- Excludes: electric power distribution; item hauling; unconstrained cosmetic
  pipes.
- Parameters: network topology, resource, production, demand, storage,
  pressure, leak, reserve duration, priority and outage.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## SYS-285 — Accumulate dust maintenance and dispatch local repair

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: exposed operating infrastructure accumulates maintenance demand,
  consumes its declared local repair resource when serviced by a reachable
  drone and malfunctions while overdue until repair completes.
- Includes: Surviving Mars: Relaunched building maintenance, dust accumulation,
  drone-delivered parts and temporary malfunction.
- Excludes: an island-wide abstract maintenance pool; permanent vehicle wear;
  recurring monetary upkeep without physical repair.
- Parameters: building, dust source, maintenance threshold, resource type,
  quantity, commander range, drone, malfunction and repair duration.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## SYS-286 — Cycle universal rockets among Earth, Mars and projects

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a dispatched universal rocket autonomously travels between its
  declared destinations, lands at a valid site, unloads or boards its manifest,
  receives fuel and may return resources, colonists or expedition rewards.
- Includes: Surviving Mars: Relaunched patch 1.0.7 cargo, passenger, automated
  Earth-import, rare-metal export and planetary-project flights.
- Excludes: direct spacecraft steering; an industrial rocket that ends at its
  first launch; a fixed local shuttle trip.
- Parameters: rocket, destination, travel time, landing site, manifest, fuel,
  unload, passengers, export value, automation and return state.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## SYS-287 — Spend mixed research points through a shuffled queue

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: sponsor income, staffed laboratories, anomalies, expeditions and
  outsourcing add research points that advance the front revealed technology
  in a bounded queue until its cost is paid and its capability unlocks.
- Includes: Surviving Mars: Relaunched seven shuffled technology fields and
  queue of up to five technologies in patch 1.0.7.
- Excludes: laboratories consuming typed science packs; one staffed workday
  project with no passive sources; instant point-store purchases.
- Parameters: field, shuffled position, reveal state, prerequisite, queue,
  cost, sponsor rate, lab output, anomaly reward, outsourcing and unlock.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## SYS-288 — Apply typed Martian disaster pressure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an active dust storm, cold wave or meteor event applies its
  declared modifiers to exposed production, travel, power, life support and
  structures until the event ends, with damage or deficits persisting afterward.
- Includes: Surviving Mars: Relaunched surface disasters on ordinary maps.
- Excludes: optional mystery arcs; underground marsquakes; cosmetic weather
  without mechanical effects.
- Parameters: disaster type, warning, duration, map exposure, disabled system,
  demand multiplier, leak, impact, damage and recovery.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## SYS-289 — Prepare, vote and apply Martian laws

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: political sessions prepare eligible laws, current seats and
  negotiated support resolve a called vote, and an enacted option changes the
  colony rule while charging any disclosed upkeep until repeal or replacement.
- Includes: Surviving Mars: Relaunched Earth Council and Martian Assembly law
  categories, multi-choice laws and governance rules.
- Excludes: a permanently signed binary law with no vote; research-tree
  progression; one event consequence.
- Parameters: session cadence, preparation, law option, faction seats, promise,
  support, threshold, effect, upkeep, repeal and replacement.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## SYS-290 — Update Martian factions, tension and political crisis

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: colony conditions, enacted laws, completed promises and faction
  goals update faction support and seats; sustained dissatisfaction can cause
  radicalisation, renegades, rising tension or a crisis that revokes laws.
- Includes: Surviving Mars: Relaunched sponsor and Martian factions, Assembly
  representation and nonterminal political crises.
- Excludes: hostile military factions; one aggregate city-happiness meter;
  election flavour with no rule consequences.
- Parameters: faction, agenda, membership, seats, satisfaction, promise,
  radicalisation, renegades, tension, crisis and revoked laws.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## SYS-291 — Resolve sponsor separation into purchased independence

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a stable colony completes its people's and sponsor's gates,
  an enacted declaration triggers sponsor penalties and a sponsor colony; sent
  resources reduce the disclosed price, whose payment ends sponsor control.
- Includes: Surviving Mars: Relaunched declaration, import/research/applicant
  penalties, sponsor-colony contributions and bought independence.
- Excludes: military conquest; post-independence technology and monument goals;
  terraforming completion.
- Parameters: stability gate, mission goals, declaration, penalty, sponsor
  colony, resource contribution, base price, reduction, payment and free state.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## SYS-292 — Resolve tactical grenade flight and field effect

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a thrown tactical grenade follows world collision and timing,
  then creates its typed transient blast, flash, smoke or fire effect over the
  affected space.
- Includes: Counter-Strike 2 HE damage, line-sensitive flash, volumetric smoke
  and spreading incendiary fire, including smoke/fire interaction; Cyberpunk
  2077 thrown grenade trajectories and typed explosions or fields.
- Excludes: ordinary firearm shots; decorative particles; a permanent terrain edit.
- Parameters: type, trajectory, bounce, fuse, line of sight, radius, duration
  and interaction rules.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md) and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## SYS-293 — Remove a defeated player for the round and drop equipment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: lethal damage ends the player's control for the current round,
  emits eligible carried equipment at the death position and restores a fresh
  role loadout only when the next round begins.
- Includes: Counter-Strike 2 Competitive death, dropped weapon/C4 and next-round spawn.
- Excludes: immediate same-round respawn; permanent campaign death; a reversible stun.
- Parameters: lethal threshold, drops, spectator access, round boundary and spawn state.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md).
- Novelty: not assessed.

## SYS-294 — Adjudicate an asymmetric bomb-defusal round

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system awards one round from the ordered interaction among
  team elimination, unplanted round timeout, C4 planting, defusal and explosion,
  preserving an already planted bomb beyond elimination or the original clock.
- Includes: Counter-Strike 2 Competitive bomb-defusal round resolution.
- Excludes: score-only deathmatch; hostage rescue; a symmetric last-player-standing round.
- Parameters: roles, living players, clock, plant state, fuse, defuse and winner.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md).
- Novelty: not assessed.

## SYS-295 — Award and carry round economy

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: kills, objective actions and the team round result produce typed
  currency awards, while surviving equipment and unspent currency carry into
  the next round subject to caps and loss-streak state.
- Includes: Counter-Strike 2 Competitive personal awards, team rewards, loss
  bonus and saved equipment.
- Excludes: persistent account currency; a shop price with no cross-round state.
- Parameters: award event, weapon, side, loss count, balance cap and survival.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md).
- Novelty: not assessed.

## SYS-296 — Swap team sides and reset half economy

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after the declared regulation half, the two fixed teams exchange
  attacker and defender roles and begin the second half from the configured
  starting economy while retaining the match round score.
- Includes: Counter-Strike 2 Competitive halftime after twelve rounds.
- Excludes: changing teams by choice; shuffling players; overtime side changes.
- Parameters: half length, roles, retained score and restart money.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md).
- Novelty: not assessed.

## SYS-297 — Resolve commanded pathing and attack acquisition

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a controlled unit follows the committed navigable path, acquires
  the ordered eligible target and repeats basic attacks at its current cadence.
- Includes: Dota 2 hero move, attack and attack-move execution.
- Excludes: autonomous lane-creep routing; player-selected spell resolution.
- Parameters: path, collision, target, range, turn rate and attack interval.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md).
- Novelty: not assessed.

## SYS-298 — Award match gold and experience from live events

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible last hits, nearby defeats, hero kills, structures and
  timed income add their declared personal or shared gold and experience awards.
- Includes: Dota 2 lane/neutral last hits, assists, towers and passive gold.
- Excludes: account currency; item refunds; experience with no event/source rule.
- Parameters: event, last hitter, proximity, team share, gold type and experience.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md).
- Novelty: not assessed.

## SYS-299 — Convert experience into character levels and build points

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: accumulated character experience crosses level thresholds,
  updates attributes and grants bounded points for eligible skills or talents.
- Includes: Dota 2 match hero levels and build points; persistent Clair Obscur:
  Expedition 33 character levels, Attribute Points and Skill Points; Cyberpunk
  2077 character levels, Attribute Points and Perk Points.
- Excludes: account levels; item-derived attributes alone; reward acquisition
  before experience conversion.
- Parameters: experience threshold, persistence, level cap, attributes, point
  types and talent tier.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md) and
  [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## SYS-300 — Combine compatible carried item components

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when all required components and any recipe are co-located in
  eligible hero, stash or courier slots, they are replaced by the completed item.
- Includes: Dota 2 shop item assembly across inventory logistics.
- Excludes: crafting at a workstation; temporary neutral-item selection.
- Parameters: recipe, components, location, ownership and resulting item.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md).
- Novelty: not assessed.

## SYS-301 — Resolve hero death, respawn and paid early return

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: lethal damage removes a hero from control, settles kill rewards
  and starts a level-sensitive respawn; eligible buyback pays to return early.
- Includes: Dota 2 ordinary death, respawn and buyback.
- Excludes: one-life round elimination; permanent campaign death.
- Parameters: killer, streak, rewards, level, respawn time, buyback cost/cooldown.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md).
- Novelty: not assessed.

## SYS-302 — Spawn and route opposing lane-creep waves

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the match periodically creates typed opposing unit waves at both
  bases and routes them along fixed lanes into autonomous combat.
- Includes: Dota 2 melee, ranged and scheduled siege lane creeps.
- Excludes: player-summoned units; neutral camp respawn; hero draft.
- Parameters: cadence, lane, composition, path, upgrade state and spawn side.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md).
- Novelty: not assessed.

## SYS-303 — Resolve defensive building protection and target priority

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an active defensive building acquires eligible nearby hostiles,
  attacks by priority and applies its current protection/backdoor state.
- Includes: Dota 2 lane/base towers and protected high-ground structures.
- Excludes: a player-aimed turret; the Ancient victory check itself.
- Parameters: range, priority, aggro, armour, protection and backdoor recovery.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md).
- Novelty: not assessed.

## SYS-304 — Propagate barracks loss into stronger enemy lane waves

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: destroying one enemy barracks persistently upgrades the matching
  allied lane-creep class; losing all enemy barracks produces the full upgrade.
- Includes: Dota 2 melee/ranged barracks and mega-creep pressure.
- Excludes: temporary aura buffs; tower destruction with no wave mutation.
- Parameters: lane, barracks class, surviving set and creep upgrade.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md).
- Novelty: not assessed.

## SYS-305 — Propagate allied vision, fog and detection

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: allied units, structures and wards reveal bounded current space
  to the team while terrain, day/night and invisibility remove or qualify sightings.
- Includes: Dota 2 shared vision, fog of war, wards and true sight.
- Excludes: post-match replay omniscience; voluntary teammate messages.
- Parameters: source, radius, elevation, time of day, invisibility and detection.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md).
- Novelty: not assessed.

## SYS-306 — Respawn neutral camps and award Roshan control

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible neutral sites repopulate on their schedule; defeating
  the major neutral boss emits its current bounded team advantage.
- Includes: Dota 2 neutral camps and Roshan's Aegis-centred reward cycle.
- Excludes: lane waves; player summons; cosmetic event bosses.
- Parameters: camp, blocked state, schedule, boss state, killer and reward set.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md).
- Novelty: not assessed.

## SYS-307 — Resolve probabilistic creature capture into owned storage

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an eligible capture-device hit computes the current target and
  device probability, performs the disclosed capture checks and on success
  removes the wild creature into the player's owned companion storage.
- Includes: ordinary Pal Sphere capture of wild Pals in Palworld.
- Excludes: a guaranteed quest capture after a boss is reduced to one health;
  defeating the target; hatching an egg.
- Parameters: target health, status, level, capture power, probability, checks,
  success, experience award and storage destination.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md).
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## SYS-308 — Execute deployed companion follow and combat behaviour

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: one deployed party companion follows the avatar, acquires
  eligible hostiles, chooses ready active skills and returns or incapacitates
  according to recall, distance and health state.
- Includes: Palworld party-Pal field AI and player-designated attack target.
- Excludes: base production work; directly steering the player avatar; a fixed
  lane-creep route.
- Parameters: companion, follow radius, target, active skills, cooldowns,
  health, incapacitation and recall.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md).
- Novelty: not assessed.

## SYS-309 — Award persistent player and companion experience levels

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible capture, combat and world events add persistent
  experience to the player and qualifying companions; crossed thresholds raise
  levels and expose their declared stats or unlock opportunities.
- Includes: Palworld player and party-Pal levelling, including capture bonuses.
- Excludes: match-local hero levels; account battle-pass progression; spending
  technology points itself.
- Parameters: event, recipient, experience, threshold, level, stats and cap.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md).
- Novelty: not assessed.

## SYS-310 — Dispatch base companions by work suitability and priority

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each available base companion selects reachable pending work
  whose type its suitability permits, using fixed assignment and configured
  priority before performing and repeating the task.
- Includes: Palworld planting, watering, gathering, handiwork, mining,
  lumbering, transport and related base jobs.
- Excludes: party combat AI; player hand crafting; a machine running with no worker.
- Parameters: companion, suitability type and level, fixed assignment,
  category priority, task, path, work speed and interruption.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md).
- Novelty: not assessed.

## SYS-311 — Update companion hunger, sanity and work condition

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: time, work and damage change a companion's hunger, sanity and
  health; available food, rest and care restore eligible values while poor
  state slows work or produces injury and illness.
- Includes: Palworld base-Pal food-box use, beds, hot springs, SAN and ailments.
- Excludes: the directly controlled avatar's hunger bar; cosmetic affection;
  instant roster transfer.
- Parameters: hunger, sanity, health, workload, food, rest, treatment, illness
  and work modifier.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md).
- Novelty: not assessed.

## SYS-312 — Advance material-backed crafting and construction workload

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: supplied player or companion work accumulates against a selected
  recipe or construction workload and, when complete, consumes its reserved
  materials and emits the declared item or persistent structure.
- Includes: Palworld workbench crafting and structure construction by the
  player or a Handiwork-capable Pal.
- Excludes: spatial-grid crafting; a continuously operating automated recipe;
  free placement with no material/work cost.
- Parameters: recipe or plan, ingredients, workload, contributor, work speed,
  completion and output.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md).
- Novelty: not assessed.

## SYS-313 — Generate and preserve an explorable survival world

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a new save instantiates a persistent open world with discoverable
  terrain, resources, creatures, weather regions and authored facilities whose
  local player changes and base structures persist.
- Includes: a new ordinary Palworld single-player world and its Palpagos regions.
- Excludes: a block-addressable voxel generator; a fixed match map reset after
  each round; custom world-setting parameters.
- Parameters: seed, terrain, biome, spawn, resource, creature, facility,
  persistence and respawn rules.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md).
- Novelty: not assessed.

## SYS-314 — Resolve avatar defeat, inventory loss and world respawn

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: lethal damage incapacitates the avatar, applies the current
  world-setting loss rule to carried state and returns the avatar at an
  available respawn point while the same world persists.
- Includes: Palworld Normal single-player defeat and respawn under default
  version-1.0 world settings.
- Excludes: permanent save deletion; one-life round elimination; companion
  incapacitation alone.
- Parameters: death position, retained and dropped classes, respawn point,
  world persistence and recovery marker.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md).
- Novelty: not assessed.

## SYS-315 — Advance authored missions through tower and raid gates

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: completing the current mission's declared discovery, crafting,
  capture or boss condition marks it complete and exposes the next authored
  location, interaction or World Tree gate.
- Includes: Palworld 1.0 main missions, tower bosses, Sunreach defence modules,
  Echoing Flute, Panthalus capture and World Tree finale.
- Excludes: optional hard-mode rematches, platform achievements and post-story raids.
- Parameters: mission, prerequisite, marker, tower timer, boss, key item,
  companion requirement and next state.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md).
- Novelty: not assessed.

## SYS-316 — Initialise stochastic battle-royale match state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before ground play, the system fills the current participant
  roster and samples an insertion-aircraft line plus match-local world-loot and
  vehicle placements from the scoped map's eligible distributions.
- Includes: PUBG Normal Match players or substitute bots, variable Erangel
  aircraft route and distributed weapons, supplies and vehicles.
- Excludes: a persistent generated survival world; fixed authored item
  placement; later care-package or safe-area sampling.
- Parameters: player cap, bot substitution, aircraft line, map, item tables,
  spawn loci, vehicle set and random seed.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md).
- Novelty: not assessed.

## SYS-317 — Resolve freefall and parachute landing

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after aircraft exit, the system integrates gravity, drag, avatar
  steering, canopy deployment and collision until the participant reaches a
  valid ground or structure landing state.
- Includes: PUBG freefall, parachute opening, glide and landing.
- Excludes: ordinary jumping; vehicle motion; an uncontrolled cinematic spawn.
- Parameters: altitude, velocity, posture, steering, canopy threshold, drag,
  collision surface, landing speed and damage.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md).
- Novelty: not assessed.

## SYS-318 — Apply attachments and regional armour durability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: compatible equipped attachments modify the current weapon's
  handling or capacity, while a hit to a protected body region applies the
  matching armour reduction and decreases that equipment's durability.
- Includes: PUBG sights, magazines, muzzle, grip and stock effects together
  with helmet and vest protection by hit region.
- Excludes: deciding to equip an item; ballistic hit testing itself; a permanent
  character-stat upgrade.
- Parameters: weapon, attachment slot and modifier, body region, armour tier,
  reduction, durability loss and break state.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md).
- Novelty: not assessed.

## SYS-319 — Resolve restorative cast and boost-over-time

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an uninterrupted medical or boost cast consumes its item,
  applies the allowed immediate health change and, where declared, advances a
  temporary boost reserve into gradual healing and movement effects.
- Includes: PUBG bandage, First Aid Kit and Med Kit completion plus Energy
  Drink, Painkiller and Adrenaline boost decay.
- Excludes: teammate revival; passive health regeneration without a consumed
  item; armour damage reduction.
- Parameters: cast, interruption, item, health cap, boost amount, decay,
  healing cadence and movement modifier.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md).
- Novelty: not assessed.

## SYS-320 — Simulate occupied vehicle motion and damage

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system integrates a directly operated vehicle's steering,
  acceleration and terrain contact while resolving collision, projectile and
  explosive damage to vehicle parts and occupants; an operating fuel reserve
  may additionally constrain vehicles whose rules expose one.
- Includes: PUBG Erangel land-vehicle rotation, fuel, tyre damage, collision
  injury, delayed explosion and speed-sensitive passenger fire; Grand Theft
  Auto V Story Mode road, water and air vehicle handling, deformation and loss.
  Cyberpunk 2077 road vehicles likewise resolve steering, traction, collision
  and combat damage without exposing a player-managed fuel reserve.
- Excludes: autonomous route service; the starting aircraft; movement on foot.
- Parameters: vehicle, seat, speed, traction, terrain, fuel, tyre, health,
  damage region, collision, explosion delay and occupant exposure.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md)
  and [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## SYS-321 — Contract phased safe area and apply Blue Zone exposure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the system reveals a new safe circle inside the current playable
  region, waits for its warning interval, contracts the damaging Blue boundary
  toward it and increases damage with uninterrupted time spent outside safety.
- Includes: PUBG Update 42.1 Normal Match Blue Zone phases and exposure-duration
  damage model.
- Excludes: a static lethal border; a player-authored arena; Red Zone bombing.
- Parameters: phase, centre distribution, radius, warning, contraction speed,
  exposure duration, damage curve and final area.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md).
- Novelty: not assessed.

## SYS-322 — Fly and signal a random care package

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: at an eligible match time, the system routes a supply aircraft,
  releases a crate containing high-level sampled loot and emits persistent red
  smoke that publicly marks its landed position.
- Includes: ordinary PUBG Erangel care-package flights and supply crates.
- Excludes: ground loot created at match start; player-called flare packages;
  cosmetic aircraft passes.
- Parameters: schedule, flight line, drop locus, descent, loot table, smoke,
  collision and availability.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md).
- Novelty: not assessed.

## SYS-323 — Warn and bombard a stochastic hazard zone

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system samples an eligible map region, marks it as a warning
  area and, after a delay, schedules multiple damaging explosions within its
  boundary before removing the hazard.
- Includes: PUBG Erangel Red Zone warning and bombardment.
- Excludes: player-thrown explosives; Blue Zone contraction; a deterministic
  authored artillery strike.
- Parameters: eligible region, centre, radius, warning, duration, explosion
  count, sampled impacts, cover interaction and damage.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md).
- Novelty: not assessed.

## SYS-324 — Deform eligible combat terrain

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an eligible tool strike or explosion removes bounded volume from
  supported terrain, updates collision and leaves the altered ground available
  as movement space or cover for the remainder of the match.
- Includes: PUBG Update 41.1 destructible terrain on Erangel.
- Excludes: building destruction; visual-only craters; persistent saved-world
  voxel edits.
- Parameters: surface, excluded region, damage source, volume, maximum depth,
  collision mesh, persistence and replication.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md).
- Novelty: not assessed.

## SYS-325 — Convert lethal defeat into death crate and terminal survivor

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: lethal damage permanently removes one Solo participant from the
  live match, exposes eligible carried state in a lootable death container,
  decrements the surviving population and awards victory when one remains.
- Includes: PUBG Normal Solo death crate, alive-count update and `Winner Winner
  Chicken Dinner` resolution.
- Excludes: temporary DBNO; team revival or Recall; round-boundary respawn.
- Parameters: lethal threshold, dropped inventory, spectating, survivor count,
  simultaneous defeat ordering and terminal participant.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md).
- Novelty: not assessed.

## SYS-326 — Generate and populate a shared procedural survival island

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: at a server-world boundary, the system generates a seeded island
  with terrain, biomes and monuments and populates sampled resource, wildlife
  and loot states for concurrent participants.
- Includes: a default Rust procedural-map wipe initialisation.
- Excludes: one authored match map; loading an unchanged save; custom-map authoring.
- Parameters: seed, world size, terrain, biome, monuments, protected radii,
  spawn tables and participant cap.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## SYS-327 — Advance metabolism and environmental exposure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system continuously updates health, calories, hydration,
  temperature and radiation from activity, consumed resources, equipment and
  the avatar's current environment.
- Includes: Rust hunger, thirst, wetness, heat, cold and radiation survival.
- Excludes: building decay; equipment durability; direct hostile damage.
- Parameters: health, calories, hydration, temperature, wetness, radiation,
  protection, activity and recovery.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## SYS-328 — Resolve the personal crafting queue

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system orders legal personal craft requests, consumes their
  ingredients and emits each output when its live duration completes, returning
  eligible inputs when a request is cancelled.
- Includes: Rust inventory crafting from known recipes near any required Workbench.
- Excludes: Furnace smelting; Recycler conversion; industrial automation.
- Parameters: recipe, quantity, queue, ingredients, workbench, duration,
  cancellation and output capacity.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## SYS-329 — Convert fixture inputs through live processing cycles

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an active material fixture repeatedly consumes compatible input
  and fuel where required, advances a live cycle and places typed products or
  by-products into bounded output slots.
- Includes: Rust Furnace smelting and monument Recycler conversion.
- Excludes: hand-crafting; unchanged storage; autonomous conveyor routing.
- Parameters: fixture, recipe, input, fuel, duration, yield, by-product, slots
  and active state.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## SYS-330 — Resolve connected building grade, health and stability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a legal block placement joins a building entity, while material
  upgrades, repairs, support changes and damage update its grade, health,
  stability and traversable collision.
- Includes: Rust twig-to-armoured building blocks and Hammer repairs.
- Excludes: deployable fixtures; terrain voxels; cosmetic building skins.
- Parameters: block, connection, grade, material, support, stability, health,
  repair state and collision.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## SYS-331 — Project building privilege and credentialled access

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: each connected claimed building projects an authority region from
  its foundations, and its Tool Cupboard and locks resolve whether an identity
  may build, pick up protected deployables or operate secured openings.
- Includes: Rust TC authorisation, BUILDING PRIVILEGE/BLOCKED and lock access.
- Excludes: upkeep consumption; physical durability; server administrator roles.
- Parameters: foundations, projection, TC, identity, authority, lock,
  credential and protected operation.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## SYS-332 — Consume upkeep and decay unprotected building material

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the server charges each connected Tool Cupboard for protected
  material grades and, when a required material is absent, damages exposed
  blocks of that grade from outer layers toward the core.
- Includes: Rust 24-hour upkeep display, grade-specific shortages and decay.
- Excludes: raid damage; tool durability; world wipe deletion.
- Parameters: building, grades, upkeep rate, TC inventory, protected duration,
  exposed layer, interval and damage.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## SYS-333 — Preserve authoritative world and sleepers while players are absent

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the server retains buildings, inventories and participant bodies
  as authoritative shared state and continues eligible simulation and hostile
  interaction while an owner is disconnected.
- Includes: Rust sleeping bodies, offline raiding, upkeep and decay.
- Excludes: pausing a private world; bounded match state deleted at round end.
- Parameters: disconnect, sleeper, persistence, tick, ownership, hostile access
  and reconnect position.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## SYS-334 — Destroy defended structure and expose secured contents

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: accumulated valid damage reduces a door, building block, fixture
  or lock through zero health, removes its collision or authority contribution
  and makes previously enclosed storage or ownership fixtures reachable.
- Includes: Rust explosive raiding into a locked base and destroying its TC.
- Excludes: authorised opening; natural decay; complete scheduled wipe.
- Parameters: target, material, health, damage, blast, destroyed state,
  collision, lock, TC and reachable contents.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## SYS-335 — Persist learned blueprints and gate personal recipes

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: research adds one recipe to an identity's blueprint knowledge,
  Workbench tech trees expose ordered unlock paths, and crafting consults that
  knowledge plus the current tier.
- Includes: Rust Research Table and Workbench tech-tree progression.
- Excludes: possessing an item without learning it; default recipes; crafting completion.
- Parameters: identity, blueprint, item, scrap, prerequisite, tier, learned
  state and reset policy.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## SYS-336 — Execute the scheduled shared-world wipe boundary

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when the configured wipe time arrives, the server ends the
  current island cycle and replaces its world, buildings and world inventories
  with a newly initialised cycle under the declared reset policy.
- Includes: Rust default monthly force-wipe boundary.
- Excludes: avatar death; local base destruction; ordinary server restart.
- Parameters: schedule, timezone, timestamp, seed, cleared state, blueprint
  reset policy and next cycle.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## SYS-337 — Initialise seeded Knox Country survival state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a new life combines the authored Knox Country map with a saved
  world seed that determines eligible generated basements, wilderness, zombie
  distribution and randomized starting states under the selected game mode.
- Includes: Project Zomboid Build 42.20.3 Apocalypse world creation.
- Excludes: an unbounded voxel generator; competitive match reset; custom
  sandbox parameter editing.
- Parameters: build, seed, mode, start town, authored map, generated locations,
  interiors, loot and zombie distribution.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## SYS-338 — Advance embodied needs into graded moodles

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: activity, environment, intake, rest, fear and injury continuously
  update personal hunger, thirst, fatigue, temperature, exertion, panic, stress,
  boredom, unhappiness, pain and sickness, then convert their ranges into
  graded action-relevant status effects.
- Includes: Project Zomboid survivor moodles and performance pressure.
- Excludes: one global colony need score; cosmetic emotion; body-part wound
  progression itself.
- Parameters: need, hidden value, grade, threshold, modifier, activity,
  environment, relief and lethal boundary.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## SYS-339 — Route zombies from local sight and emitted sound

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: nearby zombies detect eligible visual or acoustic cues, retain a
  bounded recent target, path toward its perceived location and may attract or
  join other local zombies without receiving omniscient survivor state.
- Includes: Project Zomboid zombies reacting to movement, voices, alarms,
  impacts, broken windows and gunfire.
- Excludes: a scripted horde that knows the avatar's exact location; direct hit
  resolution after contact; purely ambient sound.
- Parameters: cue source, volume, occlusion, sight, range, memory, path,
  grouping, loss of contact and investigation state.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## SYS-340 — Resolve interruptible embodied timed actions

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a valid looting, crafting, treatment, barricading, farming or
  resting request occupies the survivor for an in-world duration, advances
  progress under the selected time rate and either commits its state change or
  preserves the declared partial consequences when interrupted.
- Includes: Project Zomboid timed-action queue and danger-sensitive fast-forward.
- Excludes: an instant discrete command; autonomous worker jobs; server time
  while disconnected.
- Parameters: action, queue order, duration, time rate, movement lock,
  interruption, partial result, completion and refund.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## SYS-341 — Progress Knox infection into irreversible death and reanimation

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an eligible zombie-transmitted wound may establish the concealed
  Knox Infection; once established, time advances systemic sickness toward
  irreversible survivor death and later zombie reanimation rather than a
  curable ordinary wound state.
- Includes: Project Zomboid Apocalypse scratches, lacerations and bites.
- Excludes: ordinary bacterial wound infection; immediate lethal damage;
  sandbox transmission overrides.
- Parameters: wound class, transmission check, concealed infection, symptoms,
  mortality, reanimation delay and corpse state.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## SYS-342 — Accumulate activity-specific skill experience and modifiers

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: eligible performed activity adds progress to its matching personal
  skill; authored traits or learning multipliers may alter gain, while thresholds
  change the declared performance or eligibility of that activity.
- Includes: Project Zomboid Build 42 occupations, traits and skill progression;
  Grand Theft Auto V Story Mode stamina, shooting, strength, stealth, flying,
  driving and lung-capacity development through corresponding use; Cyberpunk
  2077 skill progression through matching activities.
- Excludes: team-wide research; purchased technology nodes; cosmetic level.
- Parameters: skill, activity, progress, multiplier, threshold, level, speed,
  quality, accuracy, capacity and retained character.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md) and
  [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## SYS-343 — Persist and damage barricaded or constructed geometry

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: completed barricades and player constructions alter local
  traversal, sight and protection in the persistent save, retain material- and
  skill-dependent health, and lose it under zombie or player damage until the
  affected layer or structure breaks.
- Includes: Project Zomboid barricades, fences and basic shelter geometry.
- Excludes: closing an authored door; abstract base defence; Rust privilege,
  upkeep and connected stability.
- Parameters: structure, material, layer, skill, health, collision, sight,
  attack count, break result and salvage.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## SYS-344 — Advance apocalypse calendar, utilities, spoilage and crops

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the calendar advances weather and seasons, may end inherited
  water or electrical service under the preset schedule, ages food toward
  spoilage and advances crops according to time, season, water and condition.
- Includes: Project Zomboid Apocalypse long-horizon resource decay and Build 42
  seasonal farming.
- Excludes: a fixed terminal countdown; shared-server offline time; crop yield
  independent of elapsed calendar state.
- Parameters: date, weather, utility cutoff window, refrigeration, food age,
  crop, season, water, disease, growth phase and yield.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## SYS-345 — End one survivor life at permanent death

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when the controlled survivor reaches lethal bodily state, that
  character permanently loses direct control and cannot resume the same life;
  the save may retain the body, zombie and world, but any later character is a
  different analytical life.
- Includes: the scoped Project Zomboid Apocalypse death boundary.
- Excludes: same-avatar respawn; temporary incapacitation; deleting the entire
  world save as part of death.
- Parameters: lethal condition, death instant, corpse, reanimation, retained
  world, later-character option and life statistics.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## SYS-346 — Instantiate a condition-bound shared extraction raid

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: matchmaking creates one bounded shared session on the selected
  authored map, applies its current regional Map Condition and samples legal
  Raider insertions, ARC presence and world-loot states.
- Includes: ARC Raiders solo matchmaking into a normal Dam Battlegrounds raid.
- Excludes: a persistent survival server; a private authored level; Expedition
  metaprogression reset.
- Parameters: party-size queue, playstyle estimate, region, map, condition,
  participant roster, insertion, ARC table, loot table and session seed.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## SYS-347 — Route ARC machines from perception into typed attack behaviour

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an ARC machine detects eligible visual or acoustic evidence,
  selects or changes a reachable target and executes its type-specific movement,
  telegraph, armour, weak-point and attack cycle.
- Includes: ARC Raiders Wasps, Snitches, Leapers, Bastions and other Topside ARC.
- Excludes: another human Raider's choices; scripted ambient flyovers; direct
  projectile damage after no legal attack was emitted.
- Parameters: machine type, sight, sound, cover, target, path, telegraph,
  attack, armour, weak point, stagger and destroyed state.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## SYS-348 — Resolve shield, health and downed Raider state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: incoming damage is applied through the compatible equipped shield
  and health state, may trigger injury or downed-but-not-out state, and reaches
  knockout when recovery or revival no longer prevents terminal raid defeat.
- Includes: ARC Raiders shield damage, health, DBNO, revival and knockout.
- Excludes: weapon durability loss; successful extraction; post-raid inventory
  settlement itself.
- Parameters: damage, shield capacity, shield charge, health, augment effect,
  downed state, bleedout, revive, self-recovery and knockout.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## SYS-349 — Settle a raid into extracted or forfeited inventory

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the raid's terminal extraction or knockout state partitions the
  entered and scavenged inventory into items returned to Speranza and items
  forfeited Topside, then closes that session for the Raider.
- Includes: ARC Raiders successful extraction with carried loot and knockout
  loss of ordinary loadout and scavenged items.
- Excludes: moving one item into the Safe Pocket; later selling or crafting;
  cosmetic unlocks with no inventory stake.
- Parameters: terminal state, entered loadout, scavenged inventory, protected
  contents, retained items, lost items and session closure.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## SYS-350 — Preserve protected-pocket contents through raid defeat

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when knockout would otherwise forfeit carried raid inventory,
  eligible items occupying protected-pocket slots are returned to persistent
  ownership unchanged by the ordinary unsecured-loss partition.
- Includes: ARC Raiders Safe Pocket retention after a Topside knockout.
- Excludes: weapons illegally pocketed through an exploit; successful
  extraction, which retains ordinary carried loot too; Fair Play compensation.
- Parameters: protected slots, item eligibility, contents at knockout,
  retained state and exception source.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## SYS-351 — Convert raid activity into persistent Raider levels

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: eligible Topside actions and completed objectives award persistent
  experience; threshold crossings increase Raider level and grant spendable
  skill points for the current progression.
- Includes: ARC Raiders raid XP, levels and skill-point awards.
- Excludes: match-local hero levels; Cred from daily Feats; paid Raider Tokens.
- Parameters: event, experience award, accumulated XP, threshold, Raider level,
  skill point and Expedition reset boundary.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## SYS-352 — Persist stash, workshop and learned recipes between raids

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: extracted items, coins, workshop-station state and learned
  blueprints remain available across ordinary raid boundaries and become the
  supply from which later loadouts and crafts are assembled.
- Includes: ARC Raiders Speranza stash, personal Workshop and blueprint state.
- Excludes: unsecured items lost in a knockout; match-local container contents;
  the optional Expedition reset and its carry-over exceptions.
- Parameters: stash slots, item stacks, coin, station tier, known recipe,
  ordinary raid boundary and reset boundary.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## SYS-353 — Resolve station-gated workshop conversion

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a legal Workshop request consumes retained ingredients at the
  required unlocked station and emits its known weapon, gear, medical, utility
  or refined-part output into persistent inventory.
- Includes: ARC Raiders Gunsmith, Gear Bench, Medical Lab, Utility Station,
  Explosives Station and Refiner crafting.
- Excludes: improvised Field Crafting during a raid; Trader purchase; arbitrary
  combination without a known recipe.
- Parameters: station, station tier, recipe, blueprint state, ingredients,
  duration, output and stash capacity.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## SYS-354 — Distribute loot value by danger and changing map condition

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the current map region, access state, container class and Map
  Condition alter eligible item tables and rarity so higher-danger or gated
  opportunities can yield more valuable extraction stakes.
- Includes: ARC Raiders risky locations, locked rooms, event caches and
  condition-specific loot distributions.
- Excludes: a fixed authored pickup; the player's decision to keep an item;
  post-extraction sale value conversion.
- Parameters: map, region, danger, access, container, condition, item table,
  rarity, durability and sampled contents.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## SYS-355 — Instantiate authored field encounter with initiative advantage

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: contacting or striking a roaming authored hostile transfers the
  current party and enemy group into a bounded battle, with a legal pre-emptive
  strike granting the declared opening advantage.
- Includes: Clair Obscur: Expedition 33 field encounters and First Strike.
- Excludes: seamless real-time combat; a random encounter with no visible world
  actor; choosing the first combat command after ordinary entry.
- Parameters: encounter group, contact side, pre-emptive hit and initial queue.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md).
- Novelty: not assessed.

## SYS-356 — Advance a stat-ordered visible combat turn queue

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system orders living combatants by their current initiative
  state, exposes the upcoming sequence and advances control after each
  completed turn or extra-turn effect.
- Includes: Clair Obscur: Expedition 33 visible party-and-enemy turn order.
- Excludes: alternating human turns; one player phase followed by a committed
  enemy phase; live simultaneous combat.
- Parameters: initiative attribute, ties, extra turns, delays and defeat removal.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md).
- Novelty: not assessed.

## SYS-357 — Generate and spend per-character Action Points within a turn

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: basic attacks, successful defence and declared passives add
  Action Points to one character, while skills and free-aim shots spend that
  balance according to their costs before the turn ends.
- Includes: Clair Obscur: Expedition 33 AP economy.
- Excludes: cooldown-only abilities; shared deck energy; permanent skill points.
- Parameters: starting AP, gain source, skill cost, shot cost, cap and carryover.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md).
- Novelty: not assessed.

## SYS-358 — Modify a selected combat effect from timed execution

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system grades the prompted real-time input embedded in a
  chosen turn command and applies its declared damage, healing, hit-count or
  secondary-effect modifier.
- Includes: Clair Obscur: Expedition 33 timed skill and basic-attack outcomes.
- Excludes: choosing the command; random critical hits; enemy-attack defence.
- Parameters: input grade, base effect, multiplier, extra hit and bonus clause.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md).
- Novelty: not assessed.

## SYS-359 — Resolve telegraphed enemy sequence through timed defence

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each hit in an enemy sequence checks the chosen live defensive
  input, negates or applies damage accordingly and awards the declared counter
  only when the required complete parry condition is met.
- Includes: Clair Obscur: Expedition 33 dodge, parry, jump and full-combo
  counter resolution.
- Excludes: passive evasion; preselected block values; untimed enemy intent.
- Parameters: cue, hit count, response window, damage, AP reward and counter gate.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md).
- Novelty: not assessed.

## SYS-360 — Update character-specific combat resource or stance

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a character's chosen skills and resolved effects create, consume
  or switch a persistent-in-battle resource whose current state changes later
  skill effects.
- Includes: Gustave Overcharge, Lune Stains and Maelle stances in the scoped
  Clair Obscur: Expedition 33 party.
- Excludes: universal AP; ordinary status effects; equipment changed outside
  battle.
- Parameters: character, resource states, generation, consumption, stance and
  effect modifier.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md).
- Novelty: not assessed.

## SYS-361 — Resolve party health, Break, statuses and battle retry

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: combat effects update health, shields or statuses and enemy Break
  gauges; crossing the Break threshold stuns the enemy, while loss of every
  active expeditioner ends the attempt and permits checkpoint retry.
- Includes: Clair Obscur: Expedition 33 damage, Burn, Break, defeat and Battle
  Retry in version 1.5.6.
- Excludes: world-map falling; permanent character deletion; timed-input grading
  before its damage is applied.
- Parameters: health, Break damage, threshold, stun duration, status, defeat and
  retry destination.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md).
- Novelty: not assessed.

## SYS-362 — Award bounded battle loot, experience and mastery credit

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: defeating the finite encounter grants its eligible items,
  Chroma, experience and one completed-battle credit to equipped Pictos before
  returning the party to exploration.
- Includes: Clair Obscur: Expedition 33 post-battle rewards and Picto progress.
- Excludes: converting accumulated experience into a level; random world pickup;
  mastering a Picto before its battle threshold.
- Parameters: encounter table, reward quantities, recipients and mastery credit.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md).
- Novelty: not assessed.

## SYS-363 — Convert mastered Picto passive into reusable Lumina

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a character wins the required number of battles with one
  Picto equipped, its passive becomes permanently available as a Lumina that
  eligible party members may activate without equipping that Picto.
- Includes: Clair Obscur: Expedition 33 four-battle Picto mastery.
- Excludes: the Picto's immediate equipped stat bonuses; selecting active
  Luminas; ordinary character levelling.
- Parameters: Picto, required victories, mastering character, passive and
  campaign persistence.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md).
- Novelty: not assessed.

## SYS-364 — Refill expedition resources and respawn field enemies on rest

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: resting at an activated checkpoint restores the party and
  replenishable Tints, revives eligible expeditioners and repopulates defeated
  ordinary field encounters in the linked area.
- Includes: Clair Obscur: Expedition 33 Expedition Flag and campsite rest;
  Hollow Knight: Silksong Bench recovery and ordinary-enemy reset.
- Excludes: a combat heal; a full new-game reset; enemies returning merely
  because real time elapsed.
- Parameters: recovery set, item maxima, respawn scope and checkpoint state.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md)
  and [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md).
- Novelty: not assessed.

## SYS-365 — Simulate ambient traffic and reactive civilians

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the populated authored world continuously routes civilian
  vehicles and pedestrians, resolves their collisions and makes nearby agents
  flee, resist or report eligible danger while the player travels or fights.
- Includes: Grand Theft Auto V Story Mode traffic, pedestrians, witnesses and
  ordinary world reactions in Los Santos and Blaine County; Cyberpunk 2077
  traffic and civilian reactions across Night City.
- Excludes: authored mission allies; police wanted escalation after dispatch;
  decorative crowds with no collision or response state.
- Parameters: population density, route, signal, collision, witness radius,
  reaction, vehicle availability and despawn horizon.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md) and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## SYS-366 — Escalate crime into wanted pursuit and timed search

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: reported or observed crimes raise a bounded wanted level, spawn
  and coordinate matching law-enforcement pressure, then replace direct pursuit
  with a timed spatial search that clears only while the protagonist stays
  outside police perception.
- Includes: Grand Theft Auto V Story Mode one-to-five-star wanted escalation,
  patrol pursuit, search cones and eventual clearance; Cyberpunk 2077 NCPD
  Heat escalation, pursuit and loss after evasion.
- Excludes: fixed mission enemies with no wanted state; GTA Online paid removal;
  a scripted chase whose pressure cannot clear through evasion.
- Parameters: crime, witness, stars, unit set, search radius, line of sight,
  concealment, cooldown and mission override.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md) and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## SYS-367 — Preserve concurrent protagonists across control transfer

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each unlocked protagonist retains authored position, resources
  and activity while not directly controlled; a legal switch advances the
  shared world and transfers camera and authority into the selected character's
  current state.
- Includes: Grand Theft Auto V Story Mode free-roam and mission character
  switches among Michael, Franklin and Trevor.
- Excludes: loading an independent save; turn-based party selection; creating a
  duplicate body with shared inventory.
- Parameters: protagonist, location, activity, elapsed simulation, mission
  staging, transition camera and retained state.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md).
- Novelty: not assessed.

## SYS-368 — Drain and restore protagonist special ability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: active special use continuously consumes the current character's
  finite meter and applies that character's temporary combat or driving
  modifiers until cancellation or exhaustion; eligible play restores readiness.
- Includes: Michael's shooting slowdown, Franklin's driving focus and Trevor's
  rage in Grand Theft Auto V Story Mode.
- Excludes: permanent skill statistics; passive armour; cheat-enabled slow time.
- Parameters: protagonist, meter, activation, drain, recharge events, duration,
  damage, accuracy, handling and cancellation.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md).
- Novelty: not assessed.

## SYS-369 — Restore an authored mission checkpoint after failure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when the controlled protagonist dies, is arrested or violates a
  declared mission-critical condition, the current attempt ends and a chosen
  retry restores the latest authored checkpoint state rather than preserving
  the failed world's transient damage and positions.
- Includes: Grand Theft Auto V Story Mode mission `Wasted`, `Busted`, abandoned
  target, destroyed asset and restart-from-checkpoint outcomes; Cyberpunk 2077
  critical-job death or failure followed by retry from an authored checkpoint.
- Excludes: free-roam hospital recovery outside the scoped mission route;
  permanent save deletion; replaying a completed mission for a medal.
- Parameters: failure reason, checkpoint, restored actors, vehicles, inventory,
  mission variables and retry choice.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md) and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## SYS-370 — Resolve heist plan and crew proficiency into take

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the committed approach determines preparation and execution
  structure, while assigned specialist skill and scripted performance affect
  mistakes, retained haul, survival, improvement and each crew member's cut
  before the remaining take reaches the protagonists.
- Includes: Grand Theft Auto V Story Mode major heists from The Jewel Store Job
  through The Big Score.
- Excludes: ordinary mission rewards; GTA Online cooperative heists; cosmetic
  crew identity with no mechanical consequence.
- Parameters: approach, role, specialist, skill, cut, mistake, survival,
  improvement, gross haul and protagonist shares.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md).
- Novelty: not assessed.

## SYS-371 — Resolve terminal story choice into roster state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the committed final option selects its authored last mission and,
  on completion, persists the corresponding protagonist survival and control
  availability in the current Story Mode save.
- Includes: Grand Theft Auto V's Something Sensible, The Time's Come and The
  Third Way branches; the scoped route completes The Third Way first.
- Excludes: replaying a completed ending from the mission menu; heist approach
  selection; temporary dialogue with no roster consequence.
- Parameters: option, final mission, required protagonists, survival, unlocks,
  completion flag and replay treatment.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md).
- Novelty: not assessed.

## SYS-372 — Apply lifepath to prologue and contextual options

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the committed character origin selects its authored opening route
  and remains available as a prerequisite for later origin-specific dialogue,
  information and quest interactions without replacing the shared campaign.
- Includes: Cyberpunk 2077 Nomad, Streetkid and Corpo prologues and lifepath
  dialogue options; the scoped route selects Nomad.
- Excludes: cosmetic biography; class-exclusive combat abilities; a completely
  separate campaign save with no shared main story.
- Parameters: lifepath, prologue, later option, quest context, information and
  shared-story convergence.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## SYS-373 — Escalate local suspicion into detection and combat

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: hostile perception of visible movement, bodies, sound or harmful
  effects fills a local suspicion state; completed detection alerts eligible
  nearby actors and changes them from search to active combat until they lose or
  neutralise the protagonist.
- Includes: Cyberpunk 2077 base-game guarded-area stealth and combat alerts.
- Excludes: NCPD wanted escalation after a public crime; a permanently
  omniscient enemy; scripted combat that begins without perception.
- Parameters: observer, sight, sound, suspicion, detection threshold, shared
  alert, search, reacquisition and combat exit.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## SYS-374 — Resolve quickhack upload, queue and hostile trace

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a committed quickhack reserves its RAM, advances through upload
  and any unlocked queue, applies its target effect, then observes cooldown and
  RAM recovery while eligible hostile tracing may progress toward revealing the
  netrunner.
- Includes: Cyberpunk 2077 Update 2.0+ base-game netrunning.
- Excludes: ordinary weapon damage; passive scanner disclosure; Breach Protocol
  removed from enemies in Update 2.0.
- Parameters: quickhack, RAM, upload, queue, effect, duration, cooldown, trace,
  interruption and reveal.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## SYS-375 — Derive protection and abilities from installed cyberware

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the current compatible implant loadout supplies armour, active or
  passive abilities and attribute-attuned modifiers, with each installed item
  consuming its declared cyberware capacity.
- Includes: Cyberpunk 2077 Update 2.0+ cyberware armour, operating systems,
  capacity and attribute attunement.
- Excludes: cosmetic clothing; perk effects with no implant; the player's
  decision to install or replace an implant.
- Parameters: slot, implant, tier, capacity cost, armour, ability, attunement,
  attribute and modifier.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## SYS-376 — Recharge spent health-item and grenade charges

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: using an equipped health item or grenade decreases its currently
  ready charge count, applies the typed effect and schedules automatic recovery
  of spent charges after their declared cooldown.
- Includes: Cyberpunk 2077 Update 2.0+ rechargeable healing and grenade items.
- Excludes: consuming a finite ammunition stack; passive health regeneration;
  permanent item destruction after one use.
- Parameters: item, maximum charges, spent charge, effect, recharge delay,
  simultaneous timers and readiness.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## SYS-377 — Convert Street Cred into offered-world unlocks

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: completed mercenary work and eligible world activity add
  persistent Street Cred; crossed thresholds expand declared fixer work,
  vehicle and equipment offers without replacing character level.
- Includes: Cyberpunk 2077 base-game Street Cred progression and offer gates.
- Excludes: ordinary experience levels; spendable eurodollars; cosmetic account
  reputation.
- Parameters: event, cred award, threshold, level, fixer, job, vehicle,
  equipment and availability.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## SYS-378 — Scale enemy, loot and vendor tiers to character level

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the current character level determines ordinary enemy scaling,
  generated loot tier and the tier range exposed by vendor stocks, so campaign
  route order changes encountered values without changing authored locations.
- Includes: Cyberpunk 2077 Update 2.0+ base-game enemies, loot and vendors.
- Excludes: fixed quest identity; player-selected difficulty; unique Iconic
  effects and concealed future drops.
- Parameters: level, difficulty, enemy tier, item tier, vendor threshold, stock
  and scaling curve.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## SYS-379 — Advance authored quest state from retained choices

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: completing mission objectives and committed conversation or quest
  responses updates persistent flags that open, alter or close later objectives,
  allies and terminal routes in the same campaign save.
- Includes: Cyberpunk 2077 base-game main jobs, optional outcome changes and the
  Nocturne Op55N1 choice into Last Caress, Totalimmortal and Where Is My Mind?.
- Excludes: flavour dialogue with no state mutation; Phantom Liberty branches;
  selecting a destination without completing its quest.
- Parameters: quest, objective, response, retained flag, ally, branch, failure,
  terminal route and completion state.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## SYS-380 — Resolve a hero ability into its typed live effect

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a legal hero ability applies its authored combination of damage,
  healing, protection, displacement, movement or control to eligible live targets.
- Includes: Luna Snow's Season 9.5 attack-healing projectile, Absolute Zero,
  Share the Stage and Fate of Both Worlds effects in Marvel Rivals.
- Excludes: primary attack selection itself; passive role labels; match-objective
  capture from merely standing in a zone.
- Parameters: hero, ability, target class, projectile or field, effect, duration,
  cooldown, interruption and stacking.
- Evidence: [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md).
- Novelty: not assessed.

## SYS-381 — Convert live contribution into ultimate readiness and spend it

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible damage and healing add role-scaled ultimate energy until
  the hero reaches its declared cost; activation consumes that readiness and
  resolves the hero's bounded ultimate effect.
- Includes: Marvel Rivals Season 9 Vanguard, Duelist and Strategist
  damage/healing-to-energy conversion and Luna Snow's Fate of Both Worlds.
- Excludes: a real-time cooldown with no earned meter; permanent account XP;
  spending a character-build point.
- Parameters: role, contribution type, conversion rate, energy cost, retained
  energy after hero swap, activation and reset.
- Evidence: [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md).
- Novelty: not assessed.

## SYS-382 — Resolve knockout and timed team-spawn return

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: committed lethal defeat removes the current combatant from live
  control, records the loss and starts a finite wait before the player may
  return through the team's currently legal spawn system.
- Includes: ordinary Marvel Rivals Quick Match knockout, respawn countdown and
  spawn-room return or hero change; Battlefield 6 Conquest post-death wait and
  legal team redeployment.
- Excludes: one-life round elimination; an allied resurrection that prevents
  the ordinary spawn timer; paid buyback.
- Parameters: lethal source, defeat credit, timer, spawn system, combatant
  selection and retained match state.
- Evidence: [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md) and
  [Battlefield 6 decomposition](../games/a-f/battlefield-6.md).
- Novelty: not assessed.

## SYS-383 — Convert mission-area control into the escort phase

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible attackers occupying an uncontested mission area add
  capture progress; completed capture fixes that checkpoint and activates the
  mode's mission vehicle and escort route.
- Includes: the opening capture phase of Marvel Rivals Convergence.
- Excludes: Domination percentage scoring; escort progress after the vehicle
  already exists; personal kill score.
- Parameters: area, eligible side, occupancy, contest, capture rate, completion,
  time award and vehicle activation.
- Evidence: [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md).
- Novelty: not assessed.

## SYS-384 — Advance or reverse an objective vehicle from team proximity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an active mission vehicle advances along its fixed route while
  eligible attackers accompany it without defender contest, stops when
  contested and may reverse toward the latest secured checkpoint under defender control.
- Includes: Marvel Rivals Convergence escort, up-to-three-attacker speed
  increase, checkpoint locking and defender reversal.
- Excludes: a player-driven transport; a fixed receiver that accepts one
  independently moved payload; Convoy's omitted opening boundary.
- Parameters: route, checkpoint, nearby attackers, nearby defenders, contest,
  forward speed, reverse speed and locked minimum.
- Evidence: [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md).
- Novelty: not assessed.

## SYS-385 — Extend contested objective time and adjudicate Convergence

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when the active Convergence objective remains legally contested
  at clock expiry, overtime preserves the attempt while its contest condition
  holds; cleared contest then awards defence, while route completion awards attack.
- Includes: Marvel Rivals capture and escort overtime plus Quick Match terminal
  win/loss adjudication.
- Excludes: regulation round-score accumulation; tournament tie-break series;
  overtime generated while no eligible attacker contests the objective.
- Parameters: phase, clock, contest, overtime decay, route completion, side and result.
- Evidence: [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md).
- Novelty: not assessed.

## SYS-386 — Destroy eligible arena geometry while preserving route anchors

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: sufficient attack impact removes or fractures map elements marked
  destructible, changing local sightlines, cover or paths while essential
  objective and traversal anchors remain indestructible.
- Includes: Marvel Rivals destructible walls, floors and cover with protected
  core route geometry and themed reconstruction effects; Battlefield 6
  tactical destruction that changes cover, routes and sightlines.
- Excludes: voxel harvesting into inventory; cosmetic debris with no changed
  traversal or cover; fully deleting the mission route.
- Parameters: element, durability, impact, fracture, debris, path, cover,
  essential flag and reconstruction.
- Evidence: [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md) and
  [Battlefield 6 decomposition](../games/a-f/battlefield-6.md).
- Novelty: not assessed.

## SYS-387 — Resolve a visible d20 check against authored difficulty

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an eligible task rolls one d20, selects the effective die under
  advantage or disadvantage, adds ability, proficiency and declared bonuses,
  compares the result with the authored difficulty and may spend shared
  Inspiration to repeat an eligible failed roll.
- Includes: Baldur's Gate 3 dialogue ability checks, Add Bonus effects and
  Inspiration rerolls.
- Excludes: combat damage dice; concealed automatic exploration checks that
  cannot spend Inspiration; a response with no check.
- Parameters: ability, skill, d20, advantage, disadvantage, modifier, bonus die,
  difficulty class, result, Inspiration and reroll.
- Evidence: [Baldur's Gate 3 decomposition](../games/a-f/baldurs-gate-3.md).
- Novelty: not assessed.

## SYS-388 — Schedule initiative turns and refresh action resources

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: entering combat rolls and orders initiative, activates one legal
  participant or tied allied group at a time and refreshes that creature's
  ordinary movement, Action, Bonus Action and Reaction resources on schedule.
- Includes: Baldur's Gate 3 single-player combat initiative and turn cycling.
- Excludes: continuous real-time combat; pre-authored enemy intent queues;
  selecting the action or resolving its effect.
- Parameters: participant, initiative die, modifier, tie group, round, active
  turn, movement, Action, Bonus Action, Reaction and refresh.
- Evidence: [Baldur's Gate 3 decomposition](../games/a-f/baldurs-gate-3.md).
- Novelty: not assessed.

## SYS-389 — Resolve typed attacks, spells and environmental interaction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a legal attack or spell resolves its attack roll or saving throw,
  damage, healing and conditions, consumes declared turn and casting resources,
  updates one maintained concentration effect and transforms compatible
  surfaces or sight conditions.
- Includes: Baldur's Gate 3 weapon attacks, spell slots, concentration,
  elevation modifiers, line of sight and elemental surface interactions.
- Excludes: dialogue ability checks; initiative scheduling; resting restoration.
- Parameters: action, target, roll, armour class, save, damage, condition,
  spell slot, concentration, elevation, sight, surface and elemental reaction.
- Evidence: [Baldur's Gate 3 decomposition](../games/a-f/baldurs-gate-3.md).
- Novelty: not assessed.

## SYS-390 — Resolve downing, death saves and party-member revival

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an eligible party member at zero hit points becomes Downed and
  rolls one death save per turn until three successes stabilise them, three
  failures kill them, or Help or healing restores consciousness; a dead
  companion requires an eligible resurrection effect or service.
- Includes: Baldur's Gate 3 player characters and companions, Help, healing,
  Revivify and Withers' resurrection service.
- Excludes: ordinary hostile death; non-lethal knockouts; loading an earlier save.
- Parameters: hit points, Downed, d20, success, failure, damage, Stable, Help,
  healing, death, resurrection resource and returned state.
- Evidence: [Baldur's Gate 3 decomposition](../games/a-f/baldurs-gate-3.md).
- Novelty: not assessed.

## SYS-391 — Restore party resources and advance camp state through rest

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a committed short or long rest restores its declared health and
  class-resource subset; a full long rest consumes difficulty-scaled camp
  supplies, restores broader resources and advances the camp night and any
  eligible rest-sensitive scenes or quests.
- Includes: Baldur's Gate 3 Balanced Short Rest and 40-supply Long Rest.
- Excludes: a healing consumable; passive regeneration; a checkpoint retry.
- Parameters: rest type, remaining short rests, camp, supplies, health, spell
  slots, class resources, partial rest, night, scene and quest advancement.
- Evidence: [Baldur's Gate 3 decomposition](../games/a-f/baldurs-gate-3.md).
- Novelty: not assessed.

## SYS-392 — Update companion approval and campaign participation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible dialogue, quest and combat decisions adjust each
  recruited companion's retained approval toward the player character, which
  can alter later dialogue, personal-quest outcomes, persuasion difficulty or
  continued party participation.
- Includes: Baldur's Gate 3 single-player companion approval and departure at
  sufficiently low approval.
- Excludes: romance completion as an independent objective; multiplayer-specific
  approval per human avatar; ordinary vendor attitude.
- Parameters: companion, proximity, decision, approval delta, current rating,
  threshold, dialogue, quest outcome, warning and departure.
- Evidence: [Baldur's Gate 3 decomposition](../games/a-f/baldurs-gate-3.md).
- Novelty: not assessed.

## SYS-393 — Resolve a class gadget into its typed team effect

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a legally activated class gadget applies its authored healing,
  ammunition, repair, spotting, protection, mobility or deployment effect to
  eligible live targets or space.
- Includes: Battlefield 6 Supply Bag, Repair Tool, Motion Sensor, Deploy Beacon
  and other scoped class-gadget effects in Conquest.
- Excludes: ordinary firearm fire; passive class identity by itself; capturing
  a point merely by standing inside it.
- Parameters: class, gadget, target class, placement, radius, charge, cooldown,
  duration, interruption and effect.
- Evidence: [Battlefield 6 decomposition](../games/a-f/battlefield-6.md).
- Novelty: not assessed.

## SYS-394 — Resolve downing, revival and ticketed death

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: lethal infantry damage enters a bounded downed state; a legal
  completed revive restores live control without team-ticket loss, while
  bleedout, give-up or disallowed revival commits death and debits one ticket.
- Includes: Battlefield 6 Conquest downing, drag-revive completion, reduced-
  health return, bleedout and unrevived-death reinforcement loss.
- Excludes: one-life round removal; instant knockout with no revive stage;
  campaign death saves or resurrection.
- Parameters: damage, downed duration, revive authority, channel, interruption,
  returned health, bleedout, give-up and ticket debit.
- Evidence: [Battlefield 6 decomposition](../games/a-f/battlefield-6.md).
- Novelty: not assessed.

## SYS-395 — Convert control-point occupancy into contested ownership

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible living team presence inside one control area advances
  neutralisation or capture toward that team, while simultaneous opposing
  presence marks the point contested and halts progress until the contest clears.
- Includes: Battlefield 6 Conquest lettered control points captured on foot or
  from eligible vehicles.
- Excludes: an escort vehicle moving from proximity; a bomb plant; scoring one
  point immediately from a touch.
- Parameters: point, owner, team occupancy, vehicle eligibility, contest,
  neutralisation, capture rate and completed ownership.
- Evidence: [Battlefield 6 decomposition](../games/a-f/battlefield-6.md).
- Novelty: not assessed.

## SYS-396 — Aggregate Conquest pressure into reinforcement tickets

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system debits a team's finite reinforcement pool for each
  committed unrevived death and repeatedly debits the opposing pool for every
  currently owned control point, ending the match when either pool reaches zero.
- Includes: Battlefield 6 standard Conquest death loss, point-driven ticket
  bleed and zero-ticket victory or defeat.
- Excludes: personal kill score as the terminal objective; a round win counter;
  an attacker-only ticket pool that resets after sectors.
- Parameters: initial tickets, death debit, owned points, drain cadence,
  simultaneous updates, zero threshold and result.
- Evidence: [Battlefield 6 decomposition](../games/a-f/battlefield-6.md).
- Novelty: not assessed.

## SYS-397 — Convert needle strikes into Silk-funded Bind and skills

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible direct strikes add Silk to a bounded spool, while Bind
  consumes a full spool for immediate healing and learned Silk Skills consume
  their declared Silk cost for an authored effect.
- Includes: Hollow Knight: Silksong needle-generated Silk, full-spool Bind and
  Silk-powered Silkspear or Needolin use.
- Excludes: passive health regeneration; an unrelated mana pool; healing from a
  finite carried consumable; a resource that resets after every enemy.
- Parameters: strike, Silk gain, spool capacity, Bind cost, healing, skill cost
  and skill effect.
- Evidence: [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md).
- Novelty: not assessed.

## SYS-398 — Retain an acquired traversal or world-interaction capability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: completing an authored acquisition permanently adds one named
  movement or world-interaction capability to the current save, making every
  compatible later route edge or mechanism usable without carrying its source.
- Includes: Hollow Knight: Silksong Swift Step, Drifter's Cloak, Cling Grip and
  Needolin acquisitions in the scoped Act 1 route.
- Excludes: a temporary buff; a carried key consumed by one lock; a technology
  unlocked only after accumulating abstract research points.
- Parameters: acquisition, capability, save persistence, compatible edge,
  mechanism and revocation rule.
- Evidence: [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md).
- Novelty: not assessed.

## SYS-399 — Convert death into checkpoint return and one recoverable currency mark

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: ordinary death returns the avatar to an eligible checkpoint while
  storing carried spendable currency in one recoverable world mark at the death
  region; game-specific parameters may select the return point or attach a
  reversible capacity penalty until recovery.
- Includes: Hollow Knight: Silksong Bench return, Rosary Cocoon and temporary
  nine-Silk cap; Elden Ring Grace-or-Stake return and recoverable rune mark.
- Excludes: dropping every carried inventory item; permanent one-life defeat;
  reloading a snapshot that erases the intervening world state.
- Parameters: death position, checkpoint options, currency, mark object,
  optional capacity penalty, recovery interaction and retained world state.
- Evidence: [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md);
  [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## SYS-400 — Apply the selected Crest to moveset, Bind and tool topology

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the currently selected Crest replaces the avatar's basic attack
  geometry, declares its coloured Tool-slot layout and may modify the effect
  that follows Bind while leaving acquired traversal capabilities intact.
- Includes: Hollow Knight: Silksong Hunter or Reaper Crest moveset, slot layout
  and Reaper post-Bind Silk-generation effect.
- Excludes: cosmetic armour; one weapon's numeric damage bonus; a character
  class fixed before the campaign starts.
- Parameters: Crest, attack geometry, slot layout, Bind modifier, equipped tools
  and traversal invariants.
- Evidence: [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md).
- Novelty: not assessed.

## SYS-401 — Route the called mount toward a tracked field target

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a mounted target selection produces autonomous pathing toward the
  tracked field position, pauses for manual deviation and resumes while that
  target remains selected.
- Includes: Monster Hunter Wilds Seikret automatic travel and manual steering.
- Excludes: teleportation; direct avatar input alone; an immutable cutscene path.
- Parameters: target, known terrain, route, obstacle, deviation, resume and
  target invalidation.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## SYS-402 — Accumulate localized monster wounds and resolve Focus destruction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: attacks update wound and break state on the struck monster body
  region; an open wound takes increased pressure and a legal Focus Strike
  destroys it for a stronger damage, control and material transition.
- Includes: Monster Hunter Wilds wounds, part pressure and Focus Strike wound
  destruction.
- Excludes: one undifferentiated health bar; cosmetic hit decals; a generic
  critical hit without retained localized state.
- Parameters: body region, attack type, wound threshold, open state, break
  threshold, Focus Strike, damage, control and bonus material.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## SYS-403 — Migrate and reacquire a hunted monster across field zones

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an engaged large monster may disengage and move through connected
  locale zones while the retained hunt target and tracking layer update its
  current or last known position for pursuit.
- Includes: Monster Hunter Wilds large-monster pursuit on the Windward Plains.
- Excludes: a boss fixed to one arena; a scripted disappearance that terminates
  the quest; random enemy spawning with no retained target identity.
- Parameters: monster, zone graph, retreat trigger, route, target identity,
  current position and tracking confidence.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## SYS-404 — Convert hunter defeat into camp return and a consumed faint

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: lethal hunter damage ends the current field life, returns the
  hunter to camp and reduces the active quest's remaining faint allowance
  without deleting retained campaign equipment or materials.
- Includes: Monster Hunter Wilds assignment faint and camp return.
- Excludes: permanent character death; ordinary knockdown; checkpoint rollback
  that restores all transient monster state.
- Parameters: lethal state, camp, faint allowance, reward penalty, retained
  equipment, monster continuity and failure threshold.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## SYS-405 — Settle a completed hunt into rewards and authored unlocks

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: defeating the declared hunt target before failure closes the
  quest, awards its material and currency results and retains the completion
  flag that exposes eligible follow-up assignments or facilities.
- Includes: Monster Hunter Wilds early assignment rewards and prologue
  progression after Chatacabra or Quematrice.
- Excludes: manual carving before settlement; free-roam defeat with no quest;
  account achievements.
- Parameters: target, completion method, reward table, zenny, material,
  completion flag, unlocked quest and facility.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## SYS-406 — Forge or upgrade equipment from retained hunt materials

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a legal smithy recipe consumes its declared retained materials
  and currency to create one persistent equipment piece or advance an eligible
  weapon along its upgrade path.
- Includes: Monster Hunter Wilds early weapon and armour smithing.
- Excludes: hand-crafting a carried consumable; repairing temporary sharpness;
  cosmetic layered equipment.
- Parameters: recipe, equipment, path, materials, zenny, prerequisite, output
  tier and retained inventory.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## SYS-407 — Run an autonomous Palico beside direct hunter control

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a persistent allied companion follows the directly controlled
  hunter and independently selects legal movement, attack or support actions
  against current local state.
- Includes: Monster Hunter Wilds Palico field and hunt assistance.
- Excludes: a second human-controlled hunter; a directly queued tactical squad;
  a cosmetic follower with no causal actions.
- Parameters: companion, follow range, target selection, support action,
  cooldown, incapacitation and return.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## SYS-408 — Change locale conditions and active ecology in real time

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the running locale transitions among authored environmental
  conditions that alter hazards, creature activity and available resources
  without ending the current field session.
- Includes: Monster Hunter Wilds Windward Plains weather and ecosystem changes.
- Excludes: a visual skybox change with no causal state; loading a different
  fixed level; a forecast that never resolves during the scope.
- Parameters: locale, condition, transition, hazard, creature set, resource set
  and duration.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## SYS-409 — Convert guard or stance depletion into a critical opening

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: qualifying attacks reduce a hidden or guarded stability state;
  crossing its threshold interrupts the target and exposes a critical window.
- Includes: Elden Ring guard breaks, stance breaks and critical follow-ups.
- Excludes: health-only stagger; scripted boss phase change; turn-based Break.
- Parameters: attack, stance damage, guard stamina, threshold and critical window.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## SYS-410 — Replace death with checkpoint return and one rune mark

- Lifecycle: `Merged`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: historical Elden Ring object-specific duplicate of checkpoint
  return with one recoverable death-currency mark, now represented by
  parameterised `SYS-399`.
- Includes: historical references to Elden Ring Grace-or-Stake return and its
  recoverable rune mark.
- Excludes: new game signatures; use `SYS-399` with the relevant checkpoint,
  currency, recovery and optional capacity-penalty parameters.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Merged into: `SYS-399` by
  [`TAXONOMY_CHANGE_011`](../../research/taxonomy-changes/TAXONOMY_CHANGE_011.md).

## SYS-411 — Convert runes into a chosen attribute level

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a legal level purchase consumes its escalating rune cost,
  increments character level and updates the selected attribute and derivatives.
- Includes: Elden Ring levelling after accepting Melina's accord.
- Excludes: experience-threshold levels; skill points; armament reinforcement.
- Parameters: level, attribute, cost curve, rune stock and derived statistics.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## SYS-412 — Derive combat performance from armament and equipment load

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: equipped armaments, armour, attributes and total load jointly
  determine usable moves, damage, defence, stamina burden and dodge tier.
- Includes: Elden Ring requirement penalties, scaling and load tiers.
- Excludes: cosmetic outfits; fixed class kits; temporary status effects alone.
- Parameters: attributes, requirements, scaling, weight, capacity and load tier.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## SYS-413 — Integrate spectral-steed traversal and mounted combat

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while mounted the system integrates direct steering, double jump,
  mounted attacks and mount health, with legal resummon after defeat.
- Includes: Torrent traversal and mounted combat in Elden Ring Limgrave.
- Excludes: target autopilot; vehicle fuel simulation; indoor fast travel.
- Parameters: velocity, terrain, jumps, attack side, mount health and resummon cost.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## SYS-414 — Execute and dismiss one autonomous Spirit Ash group

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a legal summon instantiates its declared spirit actors, runs their
  autonomous follow and combat behaviour and dismisses them on defeat or boundary.
- Includes: early Elden Ring Spirit Ash assistance and boss-area dismissal.
- Excludes: online players; NPC signs; permanent pet progression.
- Parameters: ash, actor count, AI, health, arena, boss state and dismissal.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## SYS-415 — Resolve immediate station-gated recipe crafting

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a legal craft consumes the required quantities from eligible
  inventory sources and immediately emits the declared item, including any
  permitted random modifier, without advancing a work queue.
- Includes: Terraria 1.4.5.6 by-hand, Work Bench, Furnace, Anvil and
  multi-station crafting, including craft-from-nearby-chests.
- Excludes: Minecraft spatial-grid matching; Rust timed personal queues;
  autonomous machine processing.
- Parameters: recipe, inputs, station set, source priority, output, stack and
  modifier distribution.
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## SYS-416 — Advance day-night ecology and local world spawns

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the running world clock changes day or night state and the system
  selects, spawns, routes or removes eligible local creatures according to
  time, biome, depth, weather, town suppression and player position.
- Includes: Terraria surface slimes by day, zombies and Demon Eyes by night,
  layer-specific encounters and dawn removal of nocturnal enemies.
- Excludes: one authored encounter trigger; a fixed match spawn wave; cosmetic
  lighting with no mechanical population change.
- Parameters: clock, phase, biome, layer, weather, spawn rate, spawn cap,
  offscreen region, town count and despawn rule.
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## SYS-417 — Apply a permanent character-capacity booster

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: consuming an eligible bounded booster permanently raises one
  character resource maximum by its declared increment and restores that
  increment without changing the world's terrain state.
- Includes: Terraria Life Crystals raising maximum health by 20 up to 400 and
  Mana Crystals raising maximum mana within their cap.
- Excludes: temporary potion buffs; equipment-derived statistics; purchased
  attribute levels.
- Parameters: booster, resource, current maximum, increment, cap and restored amount.
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## SYS-418 — Validate a constructed room as town-NPC housing

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system evaluates an addressed player-built room against its
  enclosure, safe-wall, size, furniture, home-tile, occupancy and local-biome
  predicates and records whether it is suitable housing.
- Includes: Terraria housing-query validation for a furnished safe-walled room.
- Excludes: cosmetic room scoring; unrestricted spawn shelters; automatic
  construction of a house.
- Parameters: frame, area, wall holes, safe walls, furniture categories, home
  tile, occupancy, evil score and validity message.
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## SYS-419 — Admit an eligible town NPC into vacant housing

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when a town character's persistent world milestone is satisfied,
  the system assigns an available valid house and instantiates or restores that
  NPC under the current arrival-time and visibility rules.
- Includes: Terraria Merchant, Nurse, Demolitionist and post-boss Dryad arrival
  into vacant suitable housing.
- Excludes: random hostile spawning; hiring a controllable unit; an NPC remaining
  available without any valid house after death.
- Parameters: NPC, milestone, inventory or boss flag, vacancy, time, visibility,
  assigned home and respawn delay.
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## SYS-420 — Resolve the night-bound two-phase Eye encounter

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the Eye of Cthulhu alternates servant summoning, hovering and
  charge sequences until its health threshold transforms it into a faster
  second phase, then yields defeat drops or escapes when the legal night ends.
- Includes: Terraria 1.4.5.6 Classic first Eye of Cthulhu fight.
- Excludes: generic direct-hit arithmetic; later bosses; Expert or Master-only
  attack additions.
- Parameters: health, phase threshold, servant count, charge cadence, target,
  dawn, escape and drops.
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.
