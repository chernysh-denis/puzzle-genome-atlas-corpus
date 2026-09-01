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
  [Slay the Spire decomposition](../games/s-z/slay-the-spire.md) and
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md) and
  [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Additional support: [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md),
  for seed- and pool-bounded room, enemy, pickup and item selection.
- Additional support: [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md),
  for declared-seed Random Map generation.
- Additional support: [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md),
  for shuffled library order inside one supplied-deck duel.
- Additional support: [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md),
  for eligible stock-weapon random critical-hit selection.
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
  while the avatar walks across it; Split Fiction's Mio and Zoe falling,
  jumping, grappling and colliding with live Chapter 1 geometry and hazards;
  Geometry Dash's cube and ship following gravity, impulses and continuous
  collision geometry while Stereo Madness advances.
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
  [Maquette decomposition](../games/m-r/maquette.md), and
  [Split Fiction decomposition](../games/s-z/split-fiction.md), and
  [Geometry Dash decomposition](../games/g-l/geometry-dash.md).
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
  Echochrome Walker crediting an echo on contact while continuing its route;
  the Stereo Madness icon marking an optional Secret Coin collected while the
  attempt continues toward the level finish.
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
  [Echochrome decomposition](../games/a-f/echochrome.md), and
  [Geometry Dash decomposition](../games/g-l/geometry-dash.md).
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
  Dota 2 lane creeps and courier following live paths; the Geometry Dash icon
  advancing horizontally through Stereo Madness while the player controls only
  its vertical response.
- Excludes: horizontal locomotion supplied directly by the player; time-driven
  motion of one currently controlled falling piece; execution of a separately
  assigned specialist role.
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
  [Factorio decomposition](../games/a-f/factorio.md), and
  [Geometry Dash decomposition](../games/g-l/geometry-dash.md).
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
- Evidence: [Braid decomposition](../games/a-f/braid.md) and
  [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md).
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
  to otherwise unreachable geometry; Split Fiction Chapter 1 switches holding
  or directing authored moving platforms and passage mechanisms.
- Excludes: a platform moved directly by the avatar; autonomous pathfinding;
  a pressure plate that only changes a door state while occupied.
- Parameters: trajectory, speed, switch-state mapping, endpoint behaviour,
  rider attachment, collision and rewind affinity.
- Evidence: [Braid decomposition](../games/a-f/braid.md), and
  [Split Fiction decomposition](../games/s-z/split-fiction.md).
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
- Evidence: [Factorio decomposition](../games/a-f/factorio.md) and
  [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
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

## SYS-192 — Propagate automation signals into target operating state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: sensors sample visible simulation values, authored logic propagates or transforms signals, and connected targets adopt the resulting operating state without another player command.
- Includes: Oxygen Not Included automation networks and Timberborn water, weather and power automation.
- Excludes: direct toggles; recipe filters without signal evaluation; electric power flow itself; hidden AI decisions.
- Parameters: sensor, signal domain, logic graph, target, state and update cadence.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md) and [Timberborn decomposition](../games/s-z/timberborn.md).
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

## SYS-194 — Complete staffed research into a technology unlock

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible staff operate suitable supplied research facilities to accumulate the selected project's required typed progress and unlock it when its cost is met.
- Includes: Oxygen Not Included research stations, RimWorld benches, Frostpunk workshops and Workers & Resources staffed universities.
- Excludes: unstaffed laboratory packs; instant catalogue purchase; passive personal experience; ordinary crafting.
- Parameters: staff eligibility, facility, supply, progress type, project prerequisites, cost and unlock.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md), [RimWorld decomposition](../games/m-r/rimworld.md), [Frostpunk decomposition](../games/a-f/frostpunk.md) and [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
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
- Includes: RimWorld friendships, rivalries, romances, marriages, breakups and
  social fights; The Sims 4 friendship and romance relationship transitions.
- Excludes: one global happiness value; a fixed biography with no causal effect.
- Parameters: pair, compatibility, interaction, memory, opinion and relationship transition.
- Evidence: [RimWorld decomposition](../games/m-r/rimworld.md) and
  [The Sims 4 decomposition](../games/s-z/the-sims-4.md).
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

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `SYS-194`.
- Includes: historical references that used `SYS-207` before registry
  normalisation 006.
- Excludes: new game signatures; use `SYS-194` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [RimWorld decomposition](../games/m-r/rimworld.md).
- Merged into: `SYS-194` by
  [`TAXONOMY_CHANGE_013`](../../research/taxonomy-changes/TAXONOMY_CHANGE_013.md).

## SYS-208 — Resolve drafted ranged attack through cover and body hit

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a commanded ranged attack resolves aim, range, intervening cover,
  armour and hit location into a miss or a wound on a specific body part.
- Includes: RimWorld drafted firearm combat and cover-dependent injury;
  Counter-Strike 2 firearm resolution through range, material, armour and hit
  group; Cyberpunk 2077 ranged attacks through cover, armour and body regions;
  Helldivers 2 aimed firearm hits against armoured body regions; Rainbow Six
  Siege firearm resolution through penetrable materials and operator bodies.
- Excludes: abstract card damage; automatic engagement with no tactical target order.
- Parameters: shooter, weapon, range, cover, accuracy, armour, body part and damage.
- Evidence: [RimWorld decomposition](../games/m-r/rimworld.md) and
  [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [Helldivers 2 decomposition](../games/g-l/helldivers-2.md) and
  [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md), and
  [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
- Additional support: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md),
  for firearm aim, obstruction and body-hit resolution against Infected.
- Additional support: [Destiny 2 decomposition](../games/a-f/destiny-2.md),
  for firearm aim, defence and hostile hit-region resolution.
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

## SYS-215 — Resolve directly commanded real-time hostile combat

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: directly controlled combatants acquire or receive legal targets and exchange range-, cadence-, damage-, defence- and defeat-dependent effects while the world continues in real time.
- Includes: embodied avatar combat, team firefights, Anno 1800 directly
  commanded naval combat and the fixed-opponent Street Fighter 6 Versus duel.
- Excludes: autonomous squad engagement; a telegraphed turn queue; non-combat collision damage; harbour fire with no relevant command.
- Parameters: combatant body, locomotion domain, target command, range, facing, cooldown, damage, armour, knockback and retreat.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md),
  [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md),
  [Dota 2 decomposition](../games/a-f/dota-2.md),
  [Anno 1800 decomposition](../games/a-f/anno-1800.md),
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md),
  [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md),
  [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md),
  [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md),
  [Helldivers 2 decomposition](../games/g-l/helldivers-2.md) and
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md) and
  [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md), and
  [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md) and
  [Street Fighter 6 decomposition](../games/s-z/street-fighter-6.md), and
  [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md), and
  [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md), and
  [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
- Additional support: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md),
  for continuous directly controlled Survivor combat against Infected.
- Additional support: [Destiny 2 decomposition](../games/a-f/destiny-2.md),
  for continuous directly controlled Titan combat through one Fireteam Op.
- Additional support: [Brawlhalla decomposition](../games/a-f/brawlhalla.md),
  for simultaneous two-fighter contact, damage, force and knockout resolution.
- Novelty: not assessed.

## SYS-216 — Apply carried-state loss and respawn in the persistent world

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when ordinary avatar health reaches its defeat threshold, the system applies the scoped loss rule to carried state and returns the avatar at an eligible respawn point while the same persistent world continues.
- Includes: Minecraft, Rust, Palworld and Terraria ordinary persistent-world defeat and respawn.
- Excludes: permanent save deletion; one-life round elimination; recoverable single-currency marks; checkpoint reload that restores inventory.
- Parameters: loss rule, dropped or destroyed state, respawn source, delay, world persistence and recovery opportunity.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md), [Rust decomposition](../games/m-r/rust.md), [Palworld decomposition](../games/m-r/palworld.md) and [Terraria decomposition](../games/s-z/terraria.md).
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
- Additional support: [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md),
  for contact pickup of eligible run resources and pocket items.
- Additional support: [Destiny 2 decomposition](../games/a-f/destiny-2.md),
  for contact pickup of compatible ammunition bricks.
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
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md) and
  [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
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

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `SYS-215`.
- Includes: historical references that used `SYS-252` before registry
  normalisation 006.
- Excludes: new game signatures; use `SYS-215` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Merged into: `SYS-215` by
  [`TAXONOMY_CHANGE_013`](../../research/taxonomy-changes/TAXONOMY_CHANGE_013.md).

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

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `SYS-192`.
- Includes: historical references that used `SYS-261` before registry
  normalisation 006.
- Excludes: new game signatures; use `SYS-192` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Merged into: `SYS-192` by
  [`TAXONOMY_CHANGE_013`](../../research/taxonomy-changes/TAXONOMY_CHANGE_013.md).

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

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `SYS-194`.
- Includes: historical references that used `SYS-272` before registry
  normalisation 006.
- Excludes: new game signatures; use `SYS-194` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Merged into: `SYS-194` by
  [`TAXONOMY_CHANGE_013`](../../research/taxonomy-changes/TAXONOMY_CHANGE_013.md).

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
  2077 thrown grenade trajectories and typed explosions or fields; Helldivers
  2 frag, incendiary, smoke and other carried grenade trajectories and fields.
- Excludes: ordinary firearm shots; decorative particles; a permanent terrain edit.
- Parameters: type, trajectory, bounce, fuse, line of sight, radius, duration
  and interaction rules.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md) and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [Helldivers 2 decomposition](../games/g-l/helldivers-2.md).
- Additional support: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md),
  for pipe-bomb, Molotov and bile-jar trajectories and fields.
- Novelty: not assessed.

## SYS-293 — Remove a defeated player for the round and drop equipment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: lethal damage ends the player's control for the current round,
  emits eligible carried equipment at the death position and restores a fresh
  role loadout only when the next round begins.
- Includes: Counter-Strike 2 Competitive death and eligible dropped weapon/C4;
  Rainbow Six Siege final elimination and eligible dropped defuser, each with
  next-round return.
- Excludes: immediate same-round respawn; permanent campaign death; a reversible stun.
- Parameters: lethal threshold, drops, spectator access, round boundary and spawn state.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md)
  and [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Novelty: not assessed.

## SYS-294 — Adjudicate an asymmetric bomb-defusal round

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system awards one round from the ordered interaction among
  team elimination, unplanted round timeout, device planting, neutralisation
  and planted-device completion, preserving the live objective beyond relevant
  elimination or the original clock.
- Includes: Counter-Strike 2 Competitive C4 resolution and Rainbow Six Siege
  Bomb defuser plant/disable resolution.
- Excludes: score-only deathmatch; hostage rescue; a symmetric last-player-standing round.
- Parameters: roles, living players, clock, device, plant state, fuse,
  neutralisation and winner.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md)
  and [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
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

## SYS-296 — Swap team roles under retained match score

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: at the declared match boundary, the two fixed teams exchange
  attacker and defender roles, retain the round score and apply the next
  role-local starting-state policy.
- Includes: Counter-Strike 2 Competitive halftime with starting economy and
  Rainbow Six Siege role swap with rebuilt round state and retained bans.
- Excludes: changing teams by choice; shuffling players; overtime side changes.
- Parameters: boundary, roles, retained score, economy, bans and round state.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md)
  and [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
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
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md) and
  [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
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

## SYS-299 — Convert experience thresholds into character progression

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible activity awards scoped character experience; crossed thresholds raise one or more character levels and expose their declared stats, unlock opportunities or spendable build points.
- Includes: Dota 2 match hero levels; persistent Clair Obscur, Cyberpunk 2077, Baldur's Gate 3, Palworld and ARC Raiders progression.
- Excludes: account battle-pass levels; item-derived attributes alone; spending a granted point; reward acquisition with no experience threshold.
- Parameters: recipient set, experience source, threshold curve, persistence horizon, level cap, stat update and point award.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md), [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md), [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), [Baldur's Gate 3 decomposition](../games/a-f/baldurs-gate-3.md), [Palworld decomposition](../games/m-r/palworld.md), [ARC Raiders decomposition](../games/a-f/arc-raiders.md) and [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
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
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md) and
  [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
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
- Includes: ordinary Pal Sphere capture of wild Pals in Palworld and eligible
  Poké Ball capture in Pokémon Legends: Z-A.
- Excludes: a guaranteed quest capture after a boss is reduced to one health;
  defeating the target; hatching an egg.
- Parameters: target health, status, level, capture power, probability, checks,
  success, experience award and storage destination.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md) and
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
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

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `SYS-299`.
- Includes: historical references that used `SYS-309` before registry
  normalisation 006.
- Excludes: new game signatures; use `SYS-299` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md).
- Merged into: `SYS-299` by
  [`TAXONOMY_CHANGE_013`](../../research/taxonomy-changes/TAXONOMY_CHANGE_013.md).

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

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `SYS-216`.
- Includes: historical references that used `SYS-314` before registry
  normalisation 006.
- Excludes: new game signatures; use `SYS-216` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md).
- Merged into: `SYS-216` by
  [`TAXONOMY_CHANGE_013`](../../research/taxonomy-changes/TAXONOMY_CHANGE_013.md).

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
  Auto V Story Mode road, water and air vehicle handling, deformation and loss;
  the fixed Need for Speed Unbound Story starter's road/off-road motion,
  collision and health response.
  Cyberpunk 2077 road vehicles likewise resolve steering, traction, collision
  and combat damage without exposing a player-managed fuel reserve.
- Excludes: autonomous route service; the starting aircraft; movement on foot.
- Parameters: vehicle, seat, speed, traction, terrain, fuel, tyre, health,
  damage region, collision, explosion delay and occupant exposure.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md)
  and [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [War Thunder decomposition](../games/s-z/war-thunder.md).
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

## SYS-326 — Generate and populate a procedural survival world

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: at a world boundary, the system generates a seeded survival
  landscape with terrain, biomes and landmarks and populates sampled resource,
  wildlife and loot states for the scoped participant count.
- Includes: a default Rust procedural-map wipe initialisation; Don't Starve
  Together world generation; one Valheim solo seed.
- Excludes: one authored match map; loading an unchanged save; custom-map authoring.
- Parameters: seed, version, world size, terrain, biome, landmarks, protected
  radii, spawn tables and participant count/cap.
- Evidence: [Rust decomposition](../games/m-r/rust.md) and
  [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md),
  and [Valheim decomposition](../games/s-z/valheim.md).
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
- Evidence: [Rust decomposition](../games/m-r/rust.md) and
  [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
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
- Evidence: [Rust decomposition](../games/m-r/rust.md) and
  [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
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

## SYS-348 — Resolve layered shield, health and downed combatant state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: incoming damage is applied through compatible shield and health
  layers, may trigger injury or downed-but-not-out state, and reaches knockout
  when recovery or revival no longer prevents terminal combatant defeat.
- Includes: ARC Raiders shield damage, health, DBNO, revival and knockout; Apex
  Legends Legend Armor, health, knockdown shield, knocked state and revival.
- Excludes: weapon durability loss; successful extraction; post-raid inventory
  settlement itself.
- Parameters: damage, shield capacity, shield charge, health, augment effect,
  downed state, bleedout, revive, self-recovery and knockout.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md) and
  [Apex Legends decomposition](../games/a-f/apex-legends.md).
- Additional support: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md),
  for permanent/temporary health, incapacitation, bleed-out, revival and death
  without requiring a shield layer.
- Additional support: [Destiny 2 decomposition](../games/a-f/destiny-2.md),
  for Guardian shield, health and defeated Ghost-marker state.
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

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `SYS-299`.
- Includes: historical references that used `SYS-351` before registry
  normalisation 006.
- Excludes: new game signatures; use `SYS-299` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Merged into: `SYS-299` by
  [`TAXONOMY_CHANGE_013`](../../research/taxonomy-changes/TAXONOMY_CHANGE_013.md).

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

## SYS-353 — Resolve station-gated retained-input crafting

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a legal personal station recipe consumes retained eligible ingredients and emits its known item or material output into persistent inventory.
- Includes: ARC Raiders Workshop conversions and Terraria immediate station-gated recipes.
- Excludes: spatial crafting-grid matching; autonomous continuous production; arbitrary combination without a known recipe; timed personal queues owned by another System gene.
- Parameters: station set, ingredient sources, recipe, quantity, duration, random modifier and output inventory.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md), [Terraria decomposition](../games/s-z/terraria.md) and [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
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

## SYS-362 — Award bounded encounter loot and progression credit

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: resolving a bounded encounter or opening its authorised reward
  source selects and grants eligible items, currency, experience or declared
  encounter-progress credit before play returns to traversal.
- Includes: Clair Obscur: Expedition 33 post-battle rewards and Picto progress;
  Sastasha boss rewards and admitted treasure coffers entering the controlled
  player's inventory during the scoped Duty Support run.
- Excludes: converting accumulated experience into a level; unauthorised random
  world pickup; hidden collection or market progression after the bounded unit.
- Parameters: encounter or source, reward table, sampled item, quantities,
  recipients, experience, currency and bounded progress credit.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md)
  and [FINAL FANTASY XIV Online decomposition](../games/a-f/final-fantasy-xiv-online.md).
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
- Definition: resting at an activated checkpoint restores its declared player
  resources and replenishable items, revives eligible party members where
  applicable and repopulates defeated ordinary field encounters in the linked area.
- Includes: Clair Obscur: Expedition 33 Expedition Flag and campsite rest;
  Hollow Knight: Silksong Bench recovery and ordinary-enemy reset; Black Myth:
  Wukong Keeper's Shrine recovery, Gourd refill and ordinary-enemy reset.
- Excludes: a combat heal; a full new-game reset; enemies returning merely
  because real time elapsed.
- Parameters: recovery set, item maxima, respawn scope and checkpoint state.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md),
  [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md) and
  [Black Myth: Wukong decomposition](../games/a-f/black-myth-wukong.md).
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
  traffic and civilian reactions across Night City; live Lakeshore road
  traffic during Need for Speed Unbound racing and pursuit.
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
- Definition: eligible reported/observed danger or event-built Heat raises a
  bounded wanted level, spawns and coordinates matching law-enforcement
  pressure, then replaces direct pursuit with a timed spatial search that
  clears only while the protagonist stays outside police perception.
- Includes: Grand Theft Auto V Story Mode one-to-five-star wanted escalation,
  patrol pursuit, search cones and eventual clearance; Cyberpunk 2077 NCPD
  Heat escalation; Need for Speed Unbound event Heat, LPD pursuit and loss
  after evasion.
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
- Includes: Cyberpunk 2077 base-game guarded-area stealth and combat alerts;
  Pokémon Legends: Z-A Trainer awareness and battle-opening state.
- Excludes: NCPD wanted escalation after a public crime; a permanently
  omniscient enemy; scripted combat that begins without perception.
- Parameters: observer, sight, sound, suspicion, detection threshold, shared
  alert, search, reacquisition and combat exit.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md) and
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
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

- Lifecycle: `Deprecated`
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
- Deprecation: the stable ID is retained for historical compatibility after
  `TAXONOMY_CHANGE_016`; no reviewed scoped game currently carries it.

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

## SYS-380 — Resolve a selected ability into its typed live effect

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a legal selected ability or equipped gadget applies its authored combination of damage, healing, supply, repair, spotting, protection, displacement, movement, control or deployment to eligible live targets or space.
- Includes: Marvel Rivals hero abilities, Battlefield 6 class gadgets and
  Helldivers 2 orbital, Eagle, support-weapon, emplacement and supply stratagems;
  Rainbow Six Siege operator gadgets.
- Excludes: ordinary basic attacks; passive identity labels; objective capture caused only by presence.
- Parameters: source, effect types, target schema, geometry, duration, cooldown, charges and team relation.
- Evidence: [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md),
  [Battlefield 6 decomposition](../games/a-f/battlefield-6.md) and
  [Helldivers 2 decomposition](../games/g-l/helldivers-2.md) and
  [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md), and
  [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
- Additional support: [Destiny 2 decomposition](../games/a-f/destiny-2.md),
  for typed Void grenade, melee, barricade and Super effects.
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
  [Battlefield 6 decomposition](../games/a-f/battlefield-6.md), and
  [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
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
- Definition: an active objective vehicle advances along its fixed route while
  eligible attackers accompany it without defender contest, stops when
  contested and may reverse toward the latest secured checkpoint under its
  ruleset's unattended or defender-control condition.
- Includes: Marvel Rivals Convergence escort, up-to-three-attacker speed
  increase, checkpoint locking and defender reversal; Team Fortress 2 Payload
  attacker proximity, defender blocking, capped pusher speed and unattended
  rollback to the latest secured checkpoint.
- Excludes: a player-driven transport; a fixed receiver that accepts one
  independently moved payload; Convoy's omitted opening boundary.
- Parameters: route, checkpoint, nearby attackers, nearby defenders, contest,
  forward speed, reverse speed and locked minimum.
- Evidence: [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md) and
  [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
- Novelty: not assessed.

## SYS-385 — Extend contested objective time and adjudicate its route

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when an active asymmetric objective retains its ruleset's legal
  pressure at clock expiry, overtime preserves the attempt while that pressure
  condition holds; cleared pressure awards defence, while route completion
  awards attack.
- Includes: Marvel Rivals capture and escort overtime plus Quick Match terminal
  adjudication; Team Fortress 2 Payload's five-second touch-renewed overtime,
  final delivery and defensive expiry.
- Excludes: regulation round-score accumulation; tournament tie-break series;
  overtime generated while no eligible attacker contests the objective.
- Parameters: phase, clock, contest, overtime decay, route completion, side and result.
- Evidence: [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md) and
  [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
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
  tactical destruction that changes cover, routes and sightlines; Rainbow Six
  Siege soft-wall, floor, hatch, barricade and cover destruction.
- Excludes: voxel harvesting into inventory; cosmetic debris with no changed
  traversal or cover; fully deleting the mission route.
- Parameters: element, durability, impact, fracture, debris, path, cover,
  essential flag and reconstruction.
- Evidence: [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md),
  [Battlefield 6 decomposition](../games/a-f/battlefield-6.md) and
  [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
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

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `SYS-380`.
- Includes: historical references that used `SYS-393` before registry
  normalisation 006.
- Excludes: new game signatures; use `SYS-380` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Battlefield 6 decomposition](../games/a-f/battlefield-6.md).
- Merged into: `SYS-380` by
  [`TAXONOMY_CHANGE_013`](../../research/taxonomy-changes/TAXONOMY_CHANGE_013.md).

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
- Evidence: [Battlefield 6 decomposition](../games/a-f/battlefield-6.md) and
  [War Thunder decomposition](../games/s-z/war-thunder.md).
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
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md)
  and [Monster Hunter: World decomposition](../games/m-r/monster-hunter-world.md).
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
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md)
  and [Monster Hunter: World decomposition](../games/m-r/monster-hunter-world.md).
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
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md)
  and [Monster Hunter: World decomposition](../games/m-r/monster-hunter-world.md).
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
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md)
  and [Monster Hunter: World decomposition](../games/m-r/monster-hunter-world.md).
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

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `SYS-353`.
- Includes: historical references that used `SYS-415` before registry
  normalisation 006.
- Excludes: new game signatures; use `SYS-353` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Merged into: `SYS-353` by
  [`TAXONOMY_CHANGE_013`](../../research/taxonomy-changes/TAXONOMY_CHANGE_013.md).

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
- Evidence: [Terraria decomposition](../games/s-z/terraria.md) and
  [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
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

## SYS-421 — Resolve Core teammate return through a legal recovery source

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: after a Core squad member dies, the system preserves the current
  recovery state and, when a surviving teammate completes a legal deathbox or
  Banner-and-Beacon process, restores that member to live play under the
  source's current equipment, timing and lockout rules.
- Includes: Apex Legends Core deathbox return and Legend Banner return through
  a Replicator and Respawn Beacon where required by the current source.
- Excludes: revival before death; the conflicting automatic pre-Ring-4 claim;
  Wildcard and other mode-specific automatic return rules.
- Parameters: deathbox, Banner, crafting state, Beacon, channel, interruption,
  lockout, return position, equipment retention and squad state.
- Evidence: [Apex Legends decomposition](../games/a-f/apex-legends.md).
- Novelty: not assessed.

## SYS-422 — Advance one locked hop-up on its current weapon object

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible weapon activity or an eligible upgrade source adds
  progress to the locked hop-up bound to that weapon object; crossing the
  threshold activates its declared effect and the progress follows the weapon
  when ownership changes.
- Includes: Apex Legends Marked locked hop-ups advanced by damage and eligible
  upgrade sources on the attached weapon.
- Excludes: character-wide experience; ordinary attachment pickup; permanent
  account weapon mastery and cosmetic unlocks.
- Parameters: weapon object, hop-up, progress source, threshold, active state,
  owner transfer and effect.
- Evidence: [Apex Legends decomposition](../games/a-f/apex-legends.md).
- Novelty: not assessed.

## SYS-423 — Adjudicate squad elimination and last-squad victory

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the match continuously evaluates every squad's active, downed,
  dead and legally recoverable members, removes a squad when no member can
  preserve its participation and awards victory when exactly one squad remains.
- Includes: Apex Legends Core Trios squad elimination and Champion result.
- Excludes: individual kill credit; Ranked Point settlement; round-score or
  ticket victory; solo permanent-defeat adjudication.
- Parameters: squad roster, member state, recovery eligibility, remaining
  squads, elimination event and winning squad.
- Evidence: [Apex Legends decomposition](../games/a-f/apex-legends.md).
- Novelty: not assessed.

## SYS-424 — Resolve a card-commanded combat proxy's health and attacks

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a separate combat proxy tracks its own current and maximum
  health, intercepts eligible damage that would reach the player and executes
  attacks only when a resolving card commands it while the proxy is alive.
- Includes: Osty absorbing otherwise unblocked attack damage and performing
  Necrobinder card-commanded attacks in Slay the Spire 2.
- Excludes: ordinary temporary Block; an autonomous follower choosing actions;
  a lane creature that attacks every round; a second human-controlled player.
- Parameters: proxy, current and maximum health, eligible damage class,
  overflow, alive state, summon amount, commanding card and attack effect.
- Evidence: [Slay the Spire 2 decomposition](../games/s-z/slay-the-spire-2.md).
- Novelty: not assessed.

## SYS-425 — Settle a persistent Quest card into its deferred route reward

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while a declared Quest card remains in the persistent deck, the
  system watches its later route predicate and, when satisfied, resolves the
  specified reward or event and removes that Quest card from the deck.
- Includes: Slay the Spire 2 Byrdonis Egg, Lantern Key, Dowsing and Spoils Map
  resolving at their declared later act, room or encounter state.
- Excludes: an immediately playable objective card; a journal-only quest with
  no deck membership; a card reward chosen after the same combat.
- Parameters: Quest card, predicate, route horizon, marked node or event,
  reward, duplicate handling and removal timing.
- Evidence: [Slay the Spire 2 decomposition](../games/s-z/slay-the-spire-2.md).
- Novelty: not assessed.

## SYS-426 — Reveal milestone Epoch and expand future-run content pools

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after run settlement, the system compares retained profile
  milestones with concealed or visible Epoch predicates, reveals each newly
  satisfied Epoch and adds its declared cards, relics, potions, character,
  Ancient, act or mode to eligible future-run pools.
- Includes: the Slay the Spire 2 Timeline revealing `Spireborn` after a
  Necrobinder Act 3 victory and unlocking three Necrobinder potions.
- Excludes: temporary run-local relic acquisition; purchasing a metaprogression
  upgrade; cosmetic-only account levels; a future mode merely announced.
- Parameters: profile, milestone, Epoch, reveal graph, story panel, unlocked
  content class, future pool and settlement order.
- Evidence: [Slay the Spire 2 decomposition](../games/s-z/slay-the-spire-2.md).
- Novelty: not assessed.

## SYS-427 — Classify a submitted word path against the authored answer set

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after one eligible letter-cell path is submitted, the system
  compares its ordered word and addressed cells with the fixed authored answer
  set, permanently claims a matching theme path, marks the designated spanning
  answer distinctly, or credits an accepted non-answer word toward assistance.
- Includes: Strands accepting theme words and its spangram into the solved
  partition while counting valid non-theme words toward the Hint meter.
- Excludes: scoring a fixed-position hypothesis by per-letter similarity;
  accepting any geometrically valid path into the final partition; generating
  the authored answers during play; the later assistance reveal itself.
- Parameters: answer set, lexicon, duplicate handling, claimed-cell state,
  spangram identity, non-answer credit and feedback rendering.
- Evidence: [Strands decomposition](../games/s-z/strands.md).
- Novelty: not assessed.

## SYS-428 — Convert non-answer words into staged answer-path hints

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: accepted distinct non-answer words accumulate toward a fixed
  threshold; reaching it grants one assistance use that first identifies the
  cells of an unresolved answer and, when invoked again for that same answer,
  discloses their traversal order.
- Includes: Strands granting a Hint after three non-theme words, highlighting
  one theme word's letters and allowing a following Hint to show their order.
- Excludes: revealing a complete answer without earned progress; a static
  visible clue; counting rejected strings; changing the concealed partition.
- Parameters: threshold, duplicate policy, stored credit, target selection,
  first-stage cell reveal, second-stage ordering reveal and consumption timing.
- Evidence: [Strands decomposition](../games/s-z/strands.md).
- Novelty: not assessed.

## SYS-429 — Return one failed partner while the cooperative segment stays live

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when exactly one member of a required human-controlled pair
  fails, the surviving partner keeps the current real-time segment active and
  the system restores the failed actor into that continuing segment after its
  declared return condition.
- Includes: Split Fiction returning Mio or Zoe after a brief recovery input or
  delay while the other remains alive in the current traversal, chase or
  encounter.
- Excludes: a teammate manually reviving a downed body; a fixed team-spawn
  wave; restoring the whole encounter immediately after any one death; joining
  a persistent world from a remote spawn fixture.
- Parameters: pair size, failed-state trigger, survivor requirement, return
  input or delay, re-entry position, invulnerability and segment continuity.
- Evidence: [Split Fiction decomposition](../games/s-z/split-fiction.md).
- Novelty: not assessed.

## SYS-430 — Restore an authored segment after simultaneous partner failure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the current cooperative attempt continues through individual
  actor failures but restores the latest authored segment checkpoint when no
  member of the required pair remains active.
- Includes: Split Fiction resetting the current Chapter 1 segment when Mio and
  Zoe fail together while preserving later chapter progression outside the
  failed transient attempt.
- Excludes: restoring after every individual death; ending a finite-life run;
  round elimination with a later team spawn; freely selecting an earlier
  checkpoint as an accessibility skip.
- Parameters: required active count, simultaneous or overlapping failure
  window, checkpoint granularity, transient state reset and retained progress.
- Evidence: [Split Fiction decomposition](../games/s-z/split-fiction.md).
- Novelty: not assessed.

## SYS-431 — Advance personal motives into mood and interaction pressure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each resident's bodily and social motive values change with
  simulation time and activity; their current balance contributes to a visible
  emotional state that modifies available or effective interactions.
- Includes: The Sims 4 base-game hunger, energy, bladder, hygiene, fun and
  social motives, their replenishing activities and mood-dependent socials.
- Excludes: one settlement-wide happiness total; lethal survival metabolism;
  cosmetic facial expression with no interaction consequence.
- Parameters: motive set, decay rate, activity effect, emotion contributors,
  dominant mood, interaction modifier and extreme threshold.
- Evidence: [The Sims 4 decomposition](../games/s-z/the-sims-4.md).
- Novelty: not assessed.

## SYS-432 — Execute directed actions beside resident autonomy

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a resident paths to and executes queued player-directed
  interactions while the autonomy system may select eligible activity when no
  blocking direction owns the actor; cancellation or changed context can
  interrupt either activity.
- Includes: Farrah autonomously moving between household activities and
  executing queued social, travel-preparation and self-care commands in The
  Sims 4 Live Mode.
- Excludes: an agent following only one assigned profession; direct avatar
  locomotion; a pre-authored non-interactive cutscene.
- Parameters: queue length, priority, pathing, autonomy level, interruption,
  cancellation, target reservation and failure feedback.
- Evidence: [The Sims 4 decomposition](../games/s-z/the-sims-4.md).
- Novelty: not assessed.

## SYS-433 — Advance staged scenario goals into a branch reward

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: completing the currently exposed required predicates advances an
  authored scenario to its next stage, retains route-dependent choices and,
  after the terminal predicate, assigns one branch ending and its declared
  persistent rewards.
- Includes: New In Town advancing from introductions and socialising through a
  venue visit, friendship gates and a house or dinner party, then awarding an
  ending, Inspired Explorer, a bonus trait and satisfaction points.
- Excludes: one independent quest reward; an endless aspiration checklist;
  selecting every branch ending at once.
- Parameters: stage graph, required and optional predicates, branch memory,
  terminal trigger, ending label, trait reward and satisfaction award.
- Evidence: [The Sims 4 decomposition](../games/s-z/the-sims-4.md).
- Novelty: not assessed.

## SYS-434 — Escalate patrol detection into faction reinforcement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a roaming hostile group that detects eligible player activity
  enters alert state and can issue a faction-specific alarm that introduces
  additional hostile units into the same continuous encounter.
- Includes: Helldivers 2 patrol aggro followed by a Terminid breach or Automaton
  reinforcement call in the scoped Easy mission.
- Excludes: authored enemies already occupying the objective; a scheduled wave
  unrelated to detection; an opposing player respawn.
- Parameters: patrol composition, vision, sound, alert delay, caller, interrupt,
  reinforcement type, arrival locus and escalation cap.
- Evidence: [Helldivers 2 decomposition](../games/g-l/helldivers-2.md).
- Novelty: not assessed.

## SYS-435 — Spend shared reinforcement stock and return a squadmate by drop pod

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a valid teammate-return signal consumes one use from a squad-wide
  stock and instantiates an eligible dead participant above the addressed area
  in a steerable descent body that restores live control on landing.
- Includes: Helldivers 2 Reinforce returning one dead Helldiver in a Hellpod
  from the squad's twenty-use four-player stock.
- Excludes: reviving an injured body in place; private per-player lives;
  automatic round respawn; returning without a living caller.
- Parameters: dead teammate, caller, shared stock, signal target, drop altitude,
  steering, pod collision, landing, equipment and depleted-stock recharge.
- Evidence: [Helldivers 2 decomposition](../games/g-l/helldivers-2.md).
- Novelty: not assessed.

## SYS-436 — Settle main-objective success separately from extraction assets

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after the required mission predicate resolves, the system retains
  mission success independently while later departure resolves each controlled
  survivor and the shared retention of assets carried aboard.
- Includes: Helldivers 2 mission success after the main objective, with
  Pelican boarding separately determining extracted Helldivers and samples.
- Excludes: extraction as the only success predicate; loot retained on death;
  a score bonus that cannot lose a carried asset.
- Parameters: main objective, completion time, survivor, departure endpoint,
  boarded state, carried assets, shared retention and post-objective wipe.
- Evidence: [Helldivers 2 decomposition](../games/g-l/helldivers-2.md).
- Novelty: not assessed.

## SYS-437 — Convert successful operation settlement into shared war impact

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system converts a completed local mission sequence and its
  operation bonus into an aggregate contribution that changes the selected
  planet's shared campaign progress for the broader player population.
- Includes: one successful Helldivers 2 Easy mission completing its one-mission
  operation and contributing Galactic War impact.
- Excludes: private experience or currency awards; a campaign ending caused by
  one run alone; live tactical control of the planet map.
- Parameters: mission result, operation length, difficulty, operation bonus,
  planet, liberation or defence state, aggregation and server settlement.
- Evidence: [Helldivers 2 decomposition](../games/g-l/helldivers-2.md).
- Novelty: not assessed.

## SYS-438 — Alternate wild preparation with nighttime battle-zone competition

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the persistent world advances between a daytime preparation
  phase and a night phase that additionally instantiates eligible Battle Zone
  opponents and competition without ending the current save.
- Includes: daytime catching, training and shopping followed by nighttime Z-A
  Royale Battle Zones in Pokémon Legends: Z-A.
- Excludes: a hard match reset; claiming that Wild Zones cease to exist at
  night; a cosmetic lighting cycle with no eligibility change.
- Parameters: phase, transition schedule, preparation activities, Battle Zone,
  opponent availability and retained world state.
- Evidence: [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Novelty: not assessed.

## SYS-439 — Convert Trainer victories into a Challenger's Ticket

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible Battle Zone Trainer victories add their declared Ticket
  Points, and reaching the current rank threshold issues the corresponding
  Challenger's Ticket.
- Includes: accumulating 1,000 points at Rank Z for the first ticket in Pokémon
  Legends: Z-A.
- Excludes: ordinary battle experience; direct promotion without the ticket;
  a leaderboard score with no qualification object.
- Parameters: current rank, eligible victory, point award, threshold, ticket
  identity and duplicate-award rule.
- Evidence: [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Novelty: not assessed.

## SYS-440 — Settle a designated promotion battle into the next rank

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: defeating the current ticket's designated opponent and complete
  party records the declared persistent next rank and unlocks the next authored
  stage, while a loss leaves promotion unsatisfied.
- Includes: defeating Zach to move from Rank Z to Rank Y in Pokémon Legends:
  Z-A.
- Excludes: earning the ticket itself; an ordinary Trainer victory; account
  matchmaking rating with no designated opponent.
- Parameters: ticket, opponent, opposing party, victory predicate, old rank,
  new rank and unlocked stage.
- Evidence: [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Novelty: not assessed.

## SYS-441 — Instantiate one fixed-role asymmetric Trial

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a match start assigns one Killer and four Survivor slots, samples
  one eligible Trial Ground plus its match-local prop layout, and grants each
  participant the state and authority of the committed role.
- Includes: standard Dead by Daylight 1v4 Trial initialisation with sampled
  spawns, Generators, Hooks, Pallets, windows, Exit Gates and concealed Hatch.
- Excludes: 2v8; a persistent generated survival world; character-specific
  Killer Power resolution after the Trial begins.
- Parameters: role counts, map pool, spawn loci, prop budgets, layout rules,
  loadouts, random seed and network participants.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Novelty: not assessed.

## SYS-442 — Accumulate and regress shared Generator work into gate power

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible Survivor repair channels add persistent progress to one
  Generator with concurrent-worker efficiency, while Killer damage can enter
  bounded regression; reaching the Trial quota completes remaining Generator
  work and powers both Exit Gates.
- Includes: Dead by Daylight's seven standard Generators, five completions,
  saved partial repair, cooperative efficiency penalty, Killer kick regression
  and powered gates.
- Excludes: a fuel-powered world generator; instant switch activation; score
  accumulation that does not unlock an escape mechanism.
- Parameters: generator count, quota, capacity, repair rate, worker count,
  efficiency, saved progress, damage, regression rate and event cap.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Novelty: not assessed.

## SYS-443 — Convert Skill Check timing into progress and noise

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system samples an eligible Skill Check during continuing
  skilful work, classifies the player's response against graded zones and
  applies the declared progress bonus, continuation or failure penalty plus
  any opposing-role notification.
- Includes: Good, Great and failed Generator or healing Skill Checks in Dead by
  Daylight, including failed-repair explosion and Loud Noise Notification.
- Excludes: a telegraphed attack parry; ordinary hit accuracy; a fully authored
  rhythm chart.
- Parameters: interaction, trigger chance, zone, response time, grade, progress
  delta, pause and notification recipient.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Novelty: not assessed.

## SYS-444 — Advance and restore Survivor health states

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: compatible damage advances one Survivor through Healthy, Injured
  and Dying states, while completed recovery or healing restores only the
  eligible next state and Dying bleed-out can reach terminal death.
- Includes: ordinary Dead by Daylight Survivor damage, altruistic healing,
  Dying recovery completion and cumulative bleed-out.
- Excludes: Hook-stage advancement; layered armour or shield depletion;
  checkpoint respawn; a persistent body-part wound simulation.
- Parameters: health state, damage class, invulnerability window, healing
  charges, recovery cap, bleed-out duration and terminal threshold.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Novelty: not assessed.

## SYS-445 — Emit and decay role-exclusive Survivor tracks

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible Survivor movement or injury emits transient spatial
  evidence along the recent route that is hidden from ordinary Survivors but
  available to the Killer until it decays.
- Includes: running-created Scratch Marks and injury-created Pools of Blood in
  Dead by Daylight's blank-loadout Trial.
- Excludes: audible footsteps visible to both roles; exact aura revelation;
  an NPC automatically changing its route after sight.
- Parameters: source state, movement threshold, spawn surface, visibility role,
  brightness, blood interval, duration and decay.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Novelty: not assessed.

## SYS-446 — Resolve asymmetric vault and Pallet chase geometry

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a window or Pallet interaction resolves role, approach speed,
  collision and current obstacle state into a slow or rushed vault, a Pallet
  block or stun, or Killer destruction that permanently reopens the route.
- Includes: ordinary Survivor window/Pallet vaults, Killer window vault,
  Survivor Pallet drop, Killer stun and Killer destruction in Dead by Daylight.
- Excludes: character-specific Powers that vault or break differently;
  arbitrary destructible buildings; ordinary unobstructed movement.
- Parameters: role, obstacle, state, approach vector, vault class, duration,
  noise, impact volume, stun and break time.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Novelty: not assessed.

## SYS-447 — Advance carry and Hook state into rescue or sacrifice

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a Killer pickup converts an eligible Dying Survivor into carried
  state, a completed Hook placement begins or advances the persistent Hook
  Stage, and elapsed stage progress or another Hook reaches sacrifice unless a
  teammate completes the eligible rescue first.
- Includes: Dead by Daylight pickup, carry, Hook Stages, teammate unhook and
  terminal sacrifice in the scoped Trial.
- Excludes: self-unhook exceptions; anti-camp mechanics; campaign imprisonment;
  an immediate revive from ordinary downed state.
- Parameters: pickup eligibility, carry, wiggle exception, Hook reach, current
  stage, stage duration, rescue, returned health and sacrifice trigger.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Novelty: not assessed.

## SYS-448 — Resolve gates, Hatch and Collapse into terminal Trial state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: powered Exit Gate work can open a fixed escape boundary; one
  remaining Survivor exposes an alternate Hatch; opening a gate or closing
  that Hatch starts a bounded Collapse whose expiry sacrifices every remaining
  Survivor, while crossing a legal boundary records individual escape.
- Includes: Dead by Daylight Exit Gates, last-Survivor Hatch, Killer Hatch
  closure, Endgame Collapse and independent Survivor escape/death settlement.
- Excludes: Key reopening, Perk exceptions, post-match score and account
  progression; extraction with retained inventory stakes.
- Parameters: gate power, switch progress, gate state, living Survivor count,
  Hatch state, Collapse trigger, timer rate, incapacitated slowdown and exit.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Novelty: not assessed.

## SYS-449 — Instantiate an authored campaign area with sampled local contents

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: entering one authored campaign-area identity creates a traversable
  local instance by sampling compatible layout, encounter and interactable
  placements while preserving its declared exits and quest gates.
- Includes: Path of Exile 2 Act 1 area instances.
- Excludes: a fixed authored room; a match-only arena; generating a persistent
  editable survival world.
- Parameters: area identity and level, layout grammar, exits, checkpoints,
  encounter tables, seed, reset and persistence.
- Evidence: [Path of Exile 2 decomposition](../games/m-r/path-of-exile-2.md).
- Novelty: not assessed.

## SYS-450 — Sample eligible item bases, rarity and affixes from a source

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a defeated source or opened container samples eligible item
  bases and then applies allowed rarity, item level, socket and affix outcomes
  before placing the resulting items in the world.
- Includes: Path of Exile 2 campaign equipment and currency drops.
- Excludes: deterministic quest rewards; player-authored currency crafting;
  post-match score rewards.
- Parameters: source, area/item level, base table, rarity, affix pool and count,
  sockets, quantity and ground placement.
- Evidence: [Path of Exile 2 decomposition](../games/m-r/path-of-exile-2.md).
- Novelty: not assessed.

## SYS-451 — Compose an active skill from its Gem and socketed Supports

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an active Skill Gem grants its declared action and every legal
  socketed Support modifies that action's cost, damage, timing, targets or
  secondary behaviour as one composed usable skill.
- Includes: Path of Exile 2 active Skill and Support Gem composition.
- Excludes: passive-tree statistics with no active skill; equipment affixes;
  an independently triggered second hotbar action.
- Parameters: active Gem, level and quality, sockets, Supports, tags, cost,
  timing and composed effect.
- Evidence: [Path of Exile 2 decomposition](../games/m-r/path-of-exile-2.md).
- Novelty: not assessed.

## SYS-452 — Transform an item under one crafting currency rule

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: applying an eligible crafting currency consumes it and resolves
  the currency's declared operation against the target item's current rarity,
  affix and socket state, producing a legal new item state.
- Includes: ordinary Path of Exile 2 currency crafting.
- Excludes: random loot generation before pickup; vendor exchange; external
  player trade.
- Parameters: currency, target, precondition, protected state, mutation pool,
  deterministic or sampled result and corruption.
- Evidence: [Path of Exile 2 decomposition](../games/m-r/path-of-exile-2.md).
- Novelty: not assessed.

## SYS-453 — Derive usable combat state from equipment, attributes and passives

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system combines equipped item properties, current attributes,
  allocated passives and Gem requirements to derive legal skills and current
  offensive, defensive and resource statistics.
- Includes: Path of Exile 2 requirement-sensitive Warrior builds.
- Excludes: temporary attack resolution; one isolated equipment comparison;
  cosmetic loadout changes.
- Parameters: equipment, attributes, passive modifiers, Gems, requirements,
  derived statistics and disabled effects.
- Evidence: [Path of Exile 2 decomposition](../games/m-r/path-of-exile-2.md).
- Novelty: not assessed.

## SYS-454 — Consume and replenish flask charges

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each Flask activation removes its use cost from a persistent
  charge pool, while eligible monster deaths, wells or checkpoint activation
  add charges up to capacity without replacing the equipped flask.
- Includes: Path of Exile 2 campaign Life and Mana Flask economy.
- Excludes: single-use inventory potions; unconditional cooldown refresh;
  healing that consumes Mana instead of flask charges.
- Parameters: flask, capacity, use cost, recovery effect, monster gain, well or
  checkpoint refill and modifiers.
- Evidence: [Path of Exile 2 decomposition](../games/m-r/path-of-exile-2.md).
- Novelty: not assessed.

## SYS-455 — Reset a campaign area and boss after Softcore death

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: softcore campaign death returns the character to town or an
  activated checkpoint while rebuilding the current area's ordinary monsters,
  removing its ground items and restoring the current boss to its initial state.
- Includes: Path of Exile 2 campaign death before the Act 1 boundary.
- Excludes: Hardcore character transfer; a recoverable currency marker; an
  unchanged world with only player health restored.
- Parameters: respawn choice, checkpoint, retained character state, area seed,
  monsters, ground items, boss state and experience penalty.
- Evidence: [Path of Exile 2 decomposition](../games/m-r/path-of-exile-2.md).
- Novelty: not assessed.

## SYS-456 — Resolve committed dodge start against attack overlap

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: starting an eligible spot or directional dodge moves or holds the
  character, cancels compatible current actions and ignores eligible attack
  overlap during its protected opening interval, while later overlap and
  blocking geometry still resolve normally.
- Includes: Path of Exile 2 dodge roll and its hold-to-sprint continuation;
  Brawlhalla spot and directional dodges.
- Excludes: a universal invulnerable teleport; passive evasion rolls; an
  authored quick-time event.
- Parameters: direction, distance, opening protection, collision, cancellation,
  recovery, repeated hold and sprint transition.
- Evidence: [Path of Exile 2 decomposition](../games/m-r/path-of-exile-2.md)
  and [Brawlhalla decomposition](../games/a-f/brawlhalla.md).
- Novelty: not assessed.

## SYS-457 — Resolve one live football through contact and free motion

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system continuously resolves one shared ball through player
  contact, momentum, spin, deflection, collision and free motion without
  replacing it by a turn-owned token.
- Includes: dribbles, ricochets, loose balls, posts, blocks and deflections in
  EA SPORTS FC 26 and Football Manager 26 matches; Rocket League car contacts,
  arena rebounds and free ball motion.
- Excludes: inventory ownership; a projectile destroyed on impact; abstract
  possession without a spatial ball.
- Parameters: contact point, velocity, spin, friction, restitution, surface,
  player animation and assistance.
- Evidence: [EA SPORTS FC 26 decomposition](../games/a-f/ea-sports-fc-26.md),
  [Football Manager 26 decomposition](../games/a-f/football-manager-26.md) and
  [Rocket League decomposition](../games/m-r/rocket-league.md).
- Novelty: first isolated for `GAME-0163`.

## SYS-458 — Resolve assisted football targeting and contact

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system combines the player's directional, power and action
  choice with eligible receivers, goal geometry, body pose and attributes to
  select a contact animation and resulting ball trajectory.
- Includes: default-assisted passes, crosses and shots in EA SPORTS FC 26.
- Excludes: a fully authored cinematic result; automatic team positioning;
  the referee's legality decision.
- Parameters: assistance setting, input vector, power, eligible targets,
  pressure, body orientation, attributes and contact animation.
- Evidence: [EA SPORTS FC 26 decomposition](../games/a-f/ea-sports-fc-26.md).
- Novelty: first isolated for `GAME-0163`.

## SYS-459 — Coordinate off-ball football roles under team AI

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the system continuously positions and moves non-controlled
  teammates and opponents according to formation, role, possession, ball
  location, marking and available space.
- Includes: support runs, defensive shape, midfield positioning, marking and
  autonomous team decisions in EA SPORTS FC 26 and Football Manager 26.
- Excludes: the currently controlled player's direct movement; a scripted set
  of fixed routes; account-level squad construction.
- Parameters: formation, role, tactical instruction, possession, pressure,
  score state, fatigue and difficulty.
- Evidence: [EA SPORTS FC 26 decomposition](../games/a-f/ea-sports-fc-26.md)
  and [Football Manager 26 decomposition](../games/a-f/football-manager-26.md).
- Novelty: first isolated for `GAME-0163`.

## SYS-460 — Adjudicate football offences and select the restart

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system evaluates ball boundaries, last touch, offside and
  player contact, stops or continues play, applies any sanction and places the
  ball into the corresponding restart state.
- Includes: throw-ins, goal kicks, corners, kick-offs, free kicks, advantage,
  cautions, dismissals and penalties in the scoped match.
- Excludes: manual tactical menus; post-match disciplinary progression; a
  shoot-out after a tied knockout fixture.
- Parameters: boundary crossed, last touch, attacker positions, contact,
  advantage, sanction, restart point and defending distance.
- Evidence: [EA SPORTS FC 26 decomposition](../games/a-f/ea-sports-fc-26.md)
  and [Football Manager 26 decomposition](../games/a-f/football-manager-26.md).
- Novelty: first isolated for `GAME-0163`.

## SYS-461 — Resolve autonomous goalkeeper intervention

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an eligible goalkeeper autonomously positions, catches, parries
  or blocks the live ball according to goal threat, handling privileges and
  assistance settings while remaining a field participant.
- Includes: autonomous or assisted saves and claims in EA SPORTS FC 26 and
  Football Manager 26.
- Excludes: an outfield player's commanded tackle; a penalty shoot-out minigame;
  guaranteed prevention of a valid goal.
- Parameters: shot trajectory, positioning, reaction, reach, handling area,
  assistance and goalkeeper attributes.
- Evidence: [EA SPORTS FC 26 decomposition](../games/a-f/ea-sports-fc-26.md)
  and [Football Manager 26 decomposition](../games/a-f/football-manager-26.md).
- Novelty: first isolated for `GAME-0163`.

## SYS-462 — Register a valid goal and update the match score

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when the whole legal ball crosses the defended goal line between
  the posts and under the crossbar without an overriding offence, the system
  increments the scoring team and resets play to the opponent's kick-off.
- Includes: ordinary goals and own goals in scoped EA SPORTS FC 26, Football
  Manager 26 and Rocket League matches.
- Excludes: shots that touch the line without wholly crossing it; offside or
  foul-invalidated finishes; shoot-out tallies.
- Parameters: line-crossing geometry, scoring team, prior offence, score and
  kick-off side.
- Evidence: [EA SPORTS FC 26 decomposition](../games/a-f/ea-sports-fc-26.md),
  [Football Manager 26 decomposition](../games/a-f/football-manager-26.md) and
  [Rocket League decomposition](../games/m-r/rocket-league.md).
- Novelty: first isolated for `GAME-0163`.

## SYS-463 — Advance football halves and settle regulation result

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the match clock advances during live play, permits bounded added
  time, transitions through half-time and ends after the second half by
  comparing the regulation score while allowing a draw.
- Includes: two regulation halves, half-time continuation and a win, loss or
  draw in EA SPORTS FC 26 and Football Manager 26.
- Excludes: extra time, penalty shoot-outs, tournament tables and career-season
  progression.
- Parameters: half length, clock rate, stoppage allowance, score and draw policy.
- Evidence: [EA SPORTS FC 26 decomposition](../games/a-f/ea-sports-fc-26.md)
  and [Football Manager 26 decomposition](../games/a-f/football-manager-26.md).
- Novelty: first isolated for `GAME-0163`.

## SYS-464 — Generate a seed-determined floor graph from authored rooms

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: at floor entry, the system uses the run seed and current depth to
  assemble a connected graph from compatible authored room layouts, assign its
  mandatory and eligible special-room roles and populate concealed contents.
- Includes: Basement, Caves and Depths floor generation in base The Binding of
  Isaac: Rebirth.
- Excludes: a disclosed branching node map; a persistent open world; one fixed
  authored room sequence.
- Parameters: seed, floor depth, room count, dead ends, layout pool, room role,
  difficulty, adjacency and concealed contents.
- Evidence: [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md).
- Novelty: first isolated for `GAME-0164`; earlier generators do not create a
  locally explored spatial graph from authored combat-room layouts and roles.

## SYS-465 — Settle combat-room clearance and sample its award

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when the final required hostile in the current combat room is
  defeated, the system changes the room to cleared, opens its ordinary exits
  and samples any eligible room-clear pickup or charge award.
- Includes: ordinary hostile-room settlement in base The Binding of Isaac: Rebirth.
- Excludes: defeating only one member of a remaining wave; boss-floor descent;
  a score-only kill reward that leaves exits locked.
- Parameters: required hostile set, reinforcement closure, clear trigger, door
  state, award eligibility, pool and active-item charge gain.
- Evidence: [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md).
- Novelty: first isolated for `GAME-0164`.

## SYS-505 — Instantiate an accepted employer-supplied vehicle job

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: accepting one eligible contract creates its active job state and
  places the player in the declared employer-provided vehicle with cargo already
  loaded, retaining its destination, deadline and advertised income until the
  job settles or is abandoned.
- Includes: the scoped Euro Truck Simulator 2 Quick Job.
- Excludes: spawning a free-roam vehicle with no contract; loading cargo into an
  owned truck; dispatching an autonomous employee.
- Parameters: offer, truck, trailer, cargo, origin, destination, deadline,
  income, active-job slot and abandonment result.
- Evidence: [Euro Truck Simulator 2 decomposition](../games/a-f/euro-truck-simulator-2.md).
- Novelty: first isolated for `GAME-0169`; prior mission instantiation does not
  bind a supplied loaded commercial vehicle to one direct paid delivery.

## SYS-506 — Resolve articulated trailer tracking and cargo damage

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system constrains a coupled trailer through its hitch behind
  the directly operated tractor, lets cargo mass affect the moving combination
  and updates separate trailer and cargo damage from eligible contacts.
- Includes: Euro Truck Simulator 2 single-trailer hauling, reversing and depot
  parking in the scoped Quick Job.
- Excludes: one rigid road vehicle; an autonomously routed cargo carrier; a
  trailer represented only as cosmetic geometry.
- Parameters: tractor, hitch, trailer, articulation angle, cargo mass, wheel
  contact, collision, trailer damage, cargo damage and detachment.
- Evidence: [Euro Truck Simulator 2 decomposition](../games/a-f/euro-truck-simulator-2.md).
- Novelty: first isolated for `GAME-0169`; generic occupied-vehicle damage does
  not preserve a separately damaged articulated load across the haul.

## SYS-507 — Detect regulated-road violations and debit fines

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while the vehicle remains physically controllable, the system
  compares observed movement with the current road direction, signal, posted
  limit and driver-hours rule and immediately debits the configured fine for a
  detected eligible violation.
- Includes: Euro Truck Simulator 2 speeding, red-light, wrong-way and exceeded
  mandatory-break offences under enabled traffic offences.
- Excludes: an impassable road barrier; police wanted pursuit; a post-match
  referee sanction; collision repair cost.
- Parameters: jurisdiction, offence, observation, tolerance, signal, limit,
  driving hours, fine, notification and account balance.
- Evidence: [Euro Truck Simulator 2 decomposition](../games/a-f/euro-truck-simulator-2.md).
- Novelty: first isolated for `GAME-0169`; earlier crime systems escalate
  pursuit, whereas this rule leaves the delivery live and applies a tariff.

## SYS-508 — Advance driver rest and mandatory-break clocks

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: driving depletes a comfort-like Rest State and a separate legal
  driving allowance; exhausted Rest State produces warnings and microsleep
  pressure, while a sufficiently long consecutive rest restores state and
  resets the mandatory-break allowance.
- Includes: Euro Truck Simulator 2 update 1.60 Rest State and ten-hour driving
  limit cleared by nine consecutive rest hours.
- Excludes: one undifferentiated survival-fatigue meter; fixed checkpoint rest;
  a timer that fails immediately without a recoverable rest action.
- Parameters: rest state, depletion, exhaustion, microsleep, driving allowance,
  warning threshold, violation, rest rate, consecutive minimum and reset.
- Evidence: [Euro Truck Simulator 2 decomposition](../games/a-f/euro-truck-simulator-2.md).
- Novelty: first isolated for `GAME-0169`; it preserves separate physiological
  and legal clocks whose recovery rates and terminal consequences differ.

## SYS-509 — Settle delivery time, damage and parking into job rewards

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: after a valid cargo drop-off, the system compares completion time
  and retained vehicle/cargo condition with the job terms, applies eligible
  adjustments to advertised income and awards experience including the selected
  parking treatment before closing the active contract.
- Includes: the Euro Truck Simulator 2 delivery-results settlement for the
  scoped Quick Job.
- Excludes: a traffic fine applied during travel; recurring company income;
  merely arriving near the destination without validating delivery.
- Parameters: advertised income, completion time, deadline, truck damage,
  trailer damage, cargo damage, parking difficulty, adjustments, experience,
  evaluation and contract closure.
- Evidence: [Euro Truck Simulator 2 decomposition](../games/a-f/euro-truck-simulator-2.md).
- Novelty: first isolated for `GAME-0169`; earlier settlements do not price one
  directly driven articulated haul through time, retained cargo and parking.

## SYS-510 — Recalculate a waypoint-constrained road route

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the navigation system calculates a traversable road route from
  the controlled vehicle through the ordered active waypoints to the job
  destination and updates route geometry, ETA, travel time and distance when
  position or waypoint state changes.
- Includes: Euro Truck Simulator 2 map route customisation and update 1.60 GPS.
- Excludes: automatically steering the vehicle; authoring the road network;
  showing one fixed compass bearing without a road path.
- Parameters: road graph, vehicle position, destination, waypoint order, route
  preference, recalculation, ETA, travel time and distance.
- Evidence: [Euro Truck Simulator 2 decomposition](../games/a-f/euro-truck-simulator-2.md).
- Novelty: first isolated for `GAME-0169`; earlier GPS information exposes a
  route but does not isolate multi-waypoint recalculation and delivery ETA.

## SYS-511 — Cycle an anomaly through trigger and recovery

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an eligible nearby body or thrown probe activates the anomaly's
  typed effect, after which the hazard may remain discharged briefly before
  recovering its trigger state.
- Includes: bolt-probed anomalous hazards in the S.T.A.L.K.E.R. 2 opening route.
- Excludes: permanent environmental destruction; ordinary projectile damage;
  an artifact's equipped passive effect.
- Parameters: anomaly class, trigger volume, activator, effect, damage or force,
  discharge duration and recovery.
- Evidence: [S.T.A.L.K.E.R. 2 decomposition](../games/s-z/stalker-2-heart-of-chornobyl.md).
- Novelty: first isolated for `GAME-0170`; it creates a repeatable temporary
  safe interval in a persistent field hazard.

## SYS-512 — Manifest an artifact from detector proximity

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an artifact remains visually absent while the detector converts
  decreasing distance into a stronger signal, then materialises the artifact
  once the player reaches its critical range.
- Includes: Echo Detector searches in the prologue and `Piece of Cake` cave.
- Excludes: revealing ordinary loot labels; generating a future random reward;
  equipping an artifact after collection.
- Parameters: artifact, field, detector model, distance, signal cadence,
  critical range, manifestation and reachability.
- Evidence: [S.T.A.L.K.E.R. 2 decomposition](../games/s-z/stalker-2-heart-of-chornobyl.md).
- Novelty: first isolated for `GAME-0170`; prior locators disclose bearings but
  do not turn proximity into the hidden object's in-world manifestation.

## SYS-513 — Integrate survival statuses into live capacity

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: damage, bleeding, radiation, hunger, stamina and carried weight
  update continuously and modify the avatar's movement, recovery or survival
  until the responsible state is treated, reduced or becomes lethal.
- Includes: Skif's scoped Lesser Zone health, bleed, radiation, hunger, stamina
  and overload loop.
- Excludes: a decorative status icon; long-term character attributes; vehicle
  fatigue or damage.
- Parameters: health, bleeding, radiation, hunger, stamina, load, thresholds,
  treatment, recovery and lethal state.
- Evidence: [S.T.A.L.K.E.R. 2 decomposition](../games/s-z/stalker-2-heart-of-chornobyl.md).
- Novelty: first isolated for `GAME-0170`; existing survival systems cover
  subsets, while this boundary couples radiation and carried overload to the
  same live first-person action capacity.

## SYS-514 — Compose equipped artifact effects and radiation

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: every artifact placed in an eligible armour container contributes
  its declared beneficial effects and radiation burden to the current body
  state while it remains equipped.
- Includes: artifacts found and optionally equipped during the scoped opening.
- Excludes: selling an artifact; detector manifestation; armour protection that
  does not come from an artifact slot.
- Parameters: artifact, container slot, positive effects, radiation, protection,
  stacking order and unequip transition.
- Evidence: [S.T.A.L.K.E.R. 2 decomposition](../games/s-z/stalker-2-heart-of-chornobyl.md).
- Novelty: first isolated for `GAME-0170`; it binds an equippable benefit and a
  continuous harmful output inside one slot-limited object.

## SYS-500 — Assemble a mission route from authored tile-set pieces

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: at mission creation, connect reusable authored rooms into one
  traversable route containing an entry, the required objective region and a
  legal extraction region, with optional branches and dead ends.
- Includes: Earth and Grineer mission interiors traversed during Awakening and
  Vor's Prize.
- Excludes: one fixed authored level; an overworld road network; player-built
  room placement.
- Parameters: tile set, seed, entry, objective tiles, extraction tile, doors,
  branches, dead ends and traversal legality.
- Evidence: [Warframe decomposition](../games/s-z/warframe.md).
- Novelty: first isolated for `GAME-0168`; existing procedural maps do not bind
  reusable action rooms to Warframe's entry-objective-extraction mission route.

## SYS-501 — Apply equipped Mods through capacity and polarity

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: recompute an equipment item's live statistics and effects from
  every installed compatible Mod whose rank-adjusted drain fits capacity, with
  slot polarity modifying that drain.
- Includes: starter Warframe and weapon Mod configuration during Vor's Prize.
- Excludes: the player's placement action; equipment rank gain; cosmetic
  attachments; an effect granted without an installed Mod.
- Parameters: base item, rank, capacity, slot polarity, Mod polarity, drain,
  Mod rank, effect and resulting statistics.
- Evidence: [Warframe decomposition](../games/s-z/warframe.md).
- Novelty: first isolated for `GAME-0168`; earlier build systems do not couple
  socket polarity to a shared per-item modifier budget.

## SYS-502 — Distribute Affinity into separate equipment ranks

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: eligible mission actions award Affinity to the used Warframe and
  weapons under the current distribution rule, and each recipient converts its
  accumulated share into its own rank and Mod capacity.
- Includes: starter Warframe, primary, secondary and melee progression during
  Awakening and Vor's Prize.
- Excludes: account Mastery Rank tests; Mod fusion; mission reward inventory;
  one undifferentiated character level.
- Parameters: Affinity source, eligible recipients, distribution, prior
  Affinity, threshold, rank, capacity and rank cap.
- Evidence: [Warframe decomposition](../games/s-z/warframe.md).
- Novelty: first isolated for `GAME-0168`; earlier experience genes advance a
  character rather than several equipped progression tracks in parallel.

## SYS-503 — Settle extraction into retained mission progress

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: valid extraction closes the current mission and commits eligible
  pickups, rewards, Affinity and rank changes to persistent account and Arsenal
  state before the Orbiter view resumes.
- Includes: successfully extracted Vor's Prize missions and their retained
  resources, Mods and equipment progress.
- Excludes: temporary ammunition or Energy; aborting before settlement;
  retaining the generated tile route itself.
- Parameters: objective state, extraction state, pickups, rewards, Affinity,
  ranks, inventory capacity, prior account state and next Orbiter state.
- Evidence: [Warframe decomposition](../games/s-z/warframe.md).
- Novelty: first isolated for `GAME-0168`; earlier extraction systems either
  forfeit carried gear or settle one run rather than persistent equipment growth.

## SYS-504 — Restore Orbiter segments through the opening quest chain

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: completing each mandatory opening quest step restores its
  declared Orbiter segment or function and unlocks the next legal Vor's Prize
  mission until Captain Vor is defeated and the quest closes.
- Includes: Arsenal, Foundry, Mod Station and Navigation restoration in the
  official opening route.
- Excludes: later Junctions and quests; optional market purchases; arbitrary
  access to every Orbiter function at the first mission.
- Parameters: quest step, completion, segment, installed state, newly available
  function, next mission and terminal boss state.
- Evidence: [Warframe decomposition](../games/s-z/warframe.md).
- Novelty: first isolated for `GAME-0168`; it binds tutorial mission settlement
  to progressive restoration of the player's persistent operations hub.

## SYS-471 — Integrate persistent horse traversal, condition and saddle cargo

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while the current horse is called or mounted, the system resolves
  gait, terrain, collision, health, stamina, fear and rider input while keeping
  saddle-borne weapons, outfits and carcass cargo attached to that horse.
- Includes: Arthur's current saddled horse during the scoped Red Dead Redemption
  2 Chapter 2 route.
- Excludes: motor-vehicle physics; target autopilot; a mount with no persistent
  care or cargo state; stable menus outside the active route.
- Parameters: horse, saddle, gait, acceleration, terrain, jump, collision,
  health, stamina, fear, cargo and separation distance.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`; earlier mount behaviours omit the
  jointly retained animal condition and saddle cargo boundary.

## SYS-472 — Convert horse care and shared travel into bonding levels

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible riding, feeding, grooming, calming and leading add bond
  progress to the current owned horse, and reached levels improve declared
  handling, resource and response capabilities for that horse.
- Includes: Chapter 2 horse bonding in Red Dead Redemption 2 Story Mode.
- Excludes: ordinary vehicle skill; cosmetic affection with no mechanical
  state; account-wide mount unlocks.
- Parameters: horse, care event, bond progress, level, handling, health,
  stamina, whistle range and unlocked manoeuvre.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`.

## SYS-473 — Couple character and horse cores to recoverable outer meters

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: health, stamina and Dead Eye, plus horse health and stamina, each
  use a recoverable outer meter whose refill and performance depend on its
  slower-draining core; exertion, damage, time, food, rest and tonics update the
  paired states.
- Includes: Arthur and horse core-and-bar resources during Chapter 2.
- Excludes: one ordinary health bar; a temporary armour layer; hunger with no
  linked action meter.
- Parameters: resource, core value, outer value, drain, refill rate, exertion,
  damage, consumable, rest and depleted-core penalty.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`; no earlier active system couples five
  visible core reservoirs to their corresponding action meters.

## SYS-474 — Degrade firearm condition and scale its live performance

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: firing and eligible environmental exposure reduce an owned
  firearm's retained condition, which lowers declared weapon performance until
  cleaning restores the condition state.
- Includes: soot, water, mud and cleaning effects on scoped Chapter 2 firearms.
- Excludes: consuming magazine ammunition; permanent item destruction at zero
  durability; cosmetic wear with no mechanical consequence.
- Parameters: weapon, use, environment, condition loss, damage, range, fire
  rate, reload or accuracy modifier and cleaning restoration.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`; existing durability genes do not
  represent degradable firearm performance plus carried field oil.

## SYS-475 — Resolve a witnessed offence before its law report

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an eligible observed offence creates one or more live witnesses
  who attempt to reach reporting state; escape, intimidation, calming or
  further violence can prevent, redirect or multiply the report before law
  enforcement receives it.
- Includes: the Story Mode witness phase in scoped Red Dead Redemption 2.
- Excludes: an immediately scripted wanted level; police search after a report;
  an invisible reputation penalty with no reporting agent.
- Parameters: offence, observer, identification, route, report delay, response,
  success chance, additional witnesses and transmitted crime.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`; `SYS-366` does not model a
  preventable reporting agent before escalation.

## SYS-476 — Preserve and settle jurisdictional bounty after active pursuit

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: once identified, eligible crimes add money to a
  jurisdiction-specific bounty that persists after immediate wanted search
  clears, changes later pressure and is removed by payment or surrender.
- Includes: New Hanover and West Elizabeth bounty state reached during the
  scoped Chapter 2 route.
- Excludes: the active search timer itself; a one-mission scripted price with
  no persistent jurisdiction; multiplayer wanted removal.
- Parameters: jurisdiction, identity, offence, added value, pursuit state,
  hunter pressure, payment, arrest, gang rescue and cleared amount.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`; earlier wanted systems retain no
  separately payable regional debt after active search.

## SYS-477 — Aggregate contextual conduct into persistent honour consequences

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible helpful, restrained, exploitative or violent actions
  change one persistent honour value whose current band modifies disclosed
  prices, ambient responses and authored presentation without replacing wanted.
- Includes: Chapter 2 greetings, mercy, camp donations, theft and violence in
  Red Dead Redemption 2 Story Mode.
- Excludes: immediate witness reporting; one fixed narrative choice; hidden
  affinity with a single companion.
- Parameters: conduct event, signed change, cap, band, price modifier, ambient
  response and authored presentation consequence.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`.

## SYS-478 — Convert shared camp value into supplies and ledger upgrades

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: accepted donations increase shared camp value or provisions;
  ledger spending consumes shared funds to restock medicine, ammunition or food
  and to persist eligible camp upgrades and services.
- Includes: the unlocked Horseshoe Overlook donation box, supply wagons and
  ledger during Chapter 2.
- Excludes: Arthur's personal shop purchase; flavour-only camp dialogue; Red
  Dead Online camp businesses.
- Parameters: donation class, fund balance, supply category, stock level,
  upgrade, price, prerequisite and persistent camp effect.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`; earlier pooled-resource genes do not
  join voluntary personal transfer to a shared authored camp service ledger.

## SYS-479 — Slow live action and resolve Dead Eye target marks

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: activating available Dead Eye slows surrounding live action,
  allows the current Chapter 2 targeting tier to place eligible marks, then
  resolves committed shots against those marks while spending the Dead Eye bar.
- Includes: automatic early marking and the manual-mark upgrade unlocked during
  `Pouring Forth Oil IV` in the scoped route.
- Excludes: pausing for menu planning; ordinary free aim; a turn-based attack
  queue whose enemies wait by rule.
- Parameters: tier, time scale, meter drain, target, mark order, weapon,
  ammunition, exit condition and shot resolution.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`.

## SYS-480 — Settle an animal kill into a harvestable carcass state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: animal species, prior quality, weapon and hit outcome resolve a
  defeated animal into a carcass whose remaining meat, pelt and whole-carcass
  yields can be harvested, carried, sold or donated.
- Includes: rabbit skinning and ordinary Chapter 2 hunting around Horseshoe
  Overlook in Red Dead Redemption 2 Story Mode.
- Excludes: a monster quest's fixed reward screen; defeating a human hostile;
  cosmetic wildlife with no recoverable yield.
- Parameters: species, quality, weapon, hit region, damage, carcass size,
  spoilage horizon, meat, pelt and carry state.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`; earlier carving genes do not preserve
  a portable whole carcass with weapon-sensitive yield quality.

## SYS-481 — Convert a Settler into a founded city and initial territory

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a legal Found City command consumes the Settler, creates a City
  Center and ownership state on that hex, claims the declared initial territory
  and applies eligible civilization/leader founding effects.
- Includes: founding Rome under Trajan in the scoped Civilization VI setup.
- Excludes: capturing an existing city; placing a district; expansion loyalty.
- Parameters: Settler, hex, owner, city name, initial tiles, population,
  buildings and civilization effects.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## SYS-482 — Aggregate worked-tile and specialist yields into city totals

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: each worked tile, specialist, building and applicable modifier
  contributes its declared Food, Production, Gold, Science, Culture or Faith to
  the owning city's next settlement and empire totals.
- Includes: farm Food, mine Production and Campus Science in Civilization VI.
- Excludes: hidden rival yields; one immediate Gold purchase; combat damage.
- Parameters: source, yield type, base value, modifier, city and settlement turn.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`; it joins spatial citizen assignment
  to the multi-currency 4X settlement ledger.

## SYS-483 — Resolve city growth through food, Housing and Amenities

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: net Food accumulates toward population growth while current
  Housing and Amenities apply disclosed growth and yield modifiers, starvation
  or discontent consequences to that city.
- Includes: base-game Roman city growth in Civilization VI.
- Excludes: expansion Loyalty; a fixed scripted population increase; unit health.
- Parameters: food income, consumption, stored food, population, Housing,
  Amenities, thresholds, modifiers and starvation.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## SYS-484 — Accumulate city production and complete its current target

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a city's net Production advances its single selected target each
  settlement; reaching cost creates the unit, building, district, wonder or
  project result and returns the city to a new production choice.
- Includes: completing a Campus, Settler or Mars project in Civilization VI.
- Excludes: immediate Gold purchase; builder improvement charges; research.
- Parameters: city, target, cost, stored production, modifiers, completion and overflow.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## SYS-485 — Expand city borders through accumulated culture

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: local Culture progress periodically claims an eligible adjacent
  hex for a city, expanding owned work and placement space without moving the
  City Center.
- Includes: ordinary base-game border growth in Civilization VI.
- Excludes: purchasing a specific tile with Gold; capturing territory in war;
  expansion Loyalty pressure.
- Parameters: city, culture, threshold, candidate hexes, selection and ownership.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## SYS-486 — Advance parallel Technology and Civic trees with boosts

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: empire Science and Culture separately advance their active
  prerequisite-valid targets; a satisfied Eureka or Inspiration adds its
  declared progress, and completion unlocks dependent content.
- Includes: the base-game Technology and Civic trees in Civilization VI.
- Excludes: unit experience trees; random research discovery; future-tech loops.
- Parameters: tree, target, cost, income, boost trigger, boost value,
  prerequisites, completion and unlocks.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`; prior research genes do not pair two
  concurrent currencies with action-triggered partial completion.

## SYS-487 — Resolve district geometry, adjacency and building yields

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a completed district reserves its separate city hex, calculates
  bonuses from neighbouring terrain and structures, and hosts only its eligible
  buildings and specialists for later yields.
- Includes: a Campus beside mountains and an Industrial Zone beside mines.
- Excludes: the City Center sharing the same hex; arbitrary building placement;
  one cosmetic neighbourhood model.
- Parameters: district, city, hex, neighbours, adjacency rules, buildings,
  specialists and yields.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## SYS-488 — Convert improvements and connected resources into empire effects

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a legal builder improvement changes tile yields and, when it
  connects a strategic or luxury resource, grants the declared unit-production
  access or distributed Amenity effect to the empire.
- Includes: farms, mines, Iron access and luxury Amenities in Civilization VI.
- Excludes: constructing a district; merely revealing a resource; city-state gifts.
- Parameters: improvement, tile, resource, yields, connection, strategic access
  and Amenity distribution.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## SYS-489 — Apply government and slotted policy effects

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the adopted government supplies typed slots and inherent effects;
  every valid slotted policy contributes its declared modifiers until the next
  legal reconfiguration.
- Includes: military, economic, diplomatic and wildcard cards in base Civilization VI.
- Excludes: expansion Governors; unit equipment; one temporary event bonus.
- Parameters: government, slot frame, cards, compatibility, modifiers and replacement.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## SYS-490 — Settle trade-route yields, roads and trading posts

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an active trader repeatedly grants its declared origin yields,
  creates a road along traversed land and leaves eligible trading-post state at
  a completed destination.
- Includes: domestic and international base-game routes in Civilization VI.
- Excludes: a one-time diplomatic resource exchange; manually laid railways;
  city-state quest rewards.
- Parameters: origin, destination, path, duration, yields, road state,
  trading post and interruption.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## SYS-491 — Resolve civilization relationships, deals, war and peace

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: contact, declared conduct and negotiated terms change persistent
  relationship, agreement, war, peace and warmonger state, which in turn alters
  later offers, access and hostility.
- Includes: base-game civilization diplomacy in the scoped four-rival game.
- Excludes: city-state envoy influence; multiplayer chat; scripted quest affinity.
- Parameters: civilizations, contact, relationship, agenda response, deal,
  duration, war cause, peace gate and warmonger value.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## SYS-492 — Resolve unit and city combat, promotion and capture

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: attacker and defender strength, health, terrain, support and
  ranged or melee mode settle reciprocal damage; threshold outcomes defeat or
  promote units and allow eligible melee capture of a city.
- Includes: base-game land combat and Roman conquest during the scoped route.
- Excludes: theological combat; automated battle simulation outside the map;
  expansion loyalty after capture.
- Parameters: attacker, defender, strength, health, terrain, support, range,
  damage, promotion, defeat and ownership.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`; it preserves 4X unit and city
  ownership consequences rather than only actor health depletion.

## SYS-493 — Advance the ordered launch chain and settle Science Victory

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: completed Spaceport projects advance the base-game Science track
  from Satellite to Moon Landing and then the Mars Reactor, Hydroponics and
  Habitation modules; launching all three Mars modules first settles victory.
- Includes: the official launch-rule Science Victory sequence in Civilization VI.
- Excludes: Gathering Storm's Exoplanet Expedition; score comparison; domination.
- Parameters: Spaceport, technology gates, project costs, completed milestones,
  three Mars modules, rival progress and terminal result.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## SYS-494 — Transform avatar mode at an authored portal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: crossing one fixed authored mode portal replaces the active
  avatar form, control interpretation and collision envelope while preserving
  the same attempt, forward progress and level clock.
- Includes: Stereo Madness changing cube to ship at 29%, back to cube after the
  first flight, and into ship again for the final section.
- Excludes: player-selected character loadouts; teleporting to a remote scene;
  gravity-only portals; cosmetic icon changes with unchanged control rules.
- Parameters: portal position, source mode, destination mode, carried velocity,
  collision envelope, control mapping and transition feedback.
- Evidence: [Geometry Dash decomposition](../games/g-l/geometry-dash.md).
- Novelty: first isolated for `GAME-0167`; earlier portals relocate bodies or
  rotate velocity rather than replace the same auto-runner's control regime.

## SYS-495 — Resolve the single control under the current movement mode

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the current avatar mode maps the one vertical-control stream to
  its declared force response: an eligible cube press starts a jump arc, while
  ship hold and release respectively bias flight upward and downward.
- Includes: the cube and ship sections of Stereo Madness under default classic
  gameplay options.
- Excludes: the player's input gesture itself; automatic horizontal travel;
  mode transition; click-between/on-steps precision as a separate mechanic.
- Parameters: mode, support state, press buffering, impulse, hold duration,
  vertical acceleration, release and update step.
- Evidence: [Geometry Dash decomposition](../games/g-l/geometry-dash.md).
- Novelty: first isolated for `GAME-0167`; it binds one input stream to two
  authored force laws without granting horizontal steering.

## SYS-496 — Advance obstacles and soundtrack on one authored level clock

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: starting the level advances its fixed obstacle sequence,
  background pulses and soundtrack from one authored time origin so the same
  route features recur at the same progress positions on every clean attempt.
- Includes: Stereo Madness geometry, transitions and ForeverBound soundtrack
  progressing together from 0% toward 100%.
- Excludes: procedural obstacle generation; tempo selected by player input;
  music that is decorative and unsynchronised with the level sequence.
- Parameters: level clock, song offset, obstacle positions, visual events,
  progress mapping, pause policy and restart origin.
- Evidence: [Geometry Dash decomposition](../games/g-l/geometry-dash.md).
- Novelty: first isolated for `GAME-0167`; earlier live clocks advance dynamic
  systems but do not replay one authored audiovisual obstacle timeline.

## SYS-497 — Restart a failed classic attempt from its fixed origin

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: lethal contact ends the current classic Normal Mode attempt,
  clears its transient position, mode and uncredited collectible state and
  immediately creates a fresh attempt at the level's authored 0% origin.
- Includes: crashing the Stereo Madness cube or ship and returning to its
  opening cube state without an in-level checkpoint.
- Excludes: Practice Mode checkpoint respawn; loading an authored campaign save;
  preserving failed-attempt position; deleting persistent prior completions.
- Parameters: lethal trigger, restart delay, origin state, cleared attempt
  fields, retained best progress and prior persistent rewards.
- Evidence: [Geometry Dash decomposition](../games/g-l/geometry-dash.md).
- Novelty: first isolated for `GAME-0167`; earlier reset genes restore a
  checkpoint, persistent world or metaprogression-bearing generated route.

## SYS-498 — Retain best progress across repeated level attempts

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after each failed classic attempt, the level record preserves the
  farthest reached percentage while the next attempt restarts at 0%, allowing
  repeated execution to expose improvement without preserving world position.
- Includes: Stereo Madness Normal Mode best-percentage feedback across retries.
- Excludes: Practice checkpoint placement; an external speedrun timer; carrying
  the avatar's transient mode or location into the next attempt.
- Parameters: attempt number, reached percentage, previous best, update rule,
  persistent display and completion value.
- Evidence: [Geometry Dash decomposition](../games/g-l/geometry-dash.md).
- Novelty: first isolated for `GAME-0167`; it separates persistent performance
  feedback from the otherwise clean full-level restart.

## SYS-499 — Settle level completion and contacted Secret Coins

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: reaching the authored finish without prior lethal contact records
  100% Normal Mode completion, grants the level reward and persistently credits
  each optional Secret Coin contacted during that successful attempt.
- Includes: first Stereo Madness completion with zero through three coins.
- Excludes: awarding a contacted coin after dying before the finish; Practice
  Mode completion; requiring all three coins for ordinary level completion.
- Parameters: finish boundary, attempt validity, pending coin set, star/orb
  reward, prior completion, persistent coin set and completion presentation.
- Evidence: [Geometry Dash decomposition](../games/g-l/geometry-dash.md).
- Novelty: first isolated for `GAME-0167`; earlier completion systems do not
  settle a checkpointless auto-run and optional route coins together.

## SYS-466 — Apply damage and healing through ordered heart layers

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: valid damage removes health from the eligible outer heart layer
  in declared order, while a heart pickup restores only compatible missing
  capacity or adds its allowed temporary layer.
- Includes: red, soul and black hearts encountered by clean-save Isaac in base
  The Binding of Isaac: Rebirth.
- Excludes: one undifferentiated health bar; armour that regenerates after a
  firefight; healing another party member.
- Parameters: heart type, order, half-heart value, container capacity, damage,
  invulnerability interval, pickup type and legal restoration.
- Evidence: [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md).
- Novelty: first isolated for `GAME-0164`; earlier health systems do not use
  Isaac's ordered coexisting heart layers and pickup compatibility.

## SYS-467 — Compose collected item effects into the current run build

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: accepting a pedestal collectible adds its passive effect or
  replaces the active slot, and the system composes all retained compatible
  effects into movement, tears, bombs, health, pickups and triggered behaviour
  until the run terminates.
- Includes: cumulative base-Rebirth collectible effects and tear transformations.
- Excludes: permanent account equipment; a card consumed for one immediate
  effect; external mod descriptions.
- Parameters: item identity, passive or active class, replacement, statistics,
  tear form, trigger, interaction order and run lifetime.
- Evidence: [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md).
- Novelty: first isolated for `GAME-0164`; it preserves cumulative rule-changing
  item interactions inside one disposable live-action run.

## SYS-468 — Advance a boss-gated floor sequence toward the scoped ending

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: clearing the current floor boss opens its legal descent, and
  entering that transition advances the same run build to the next generated
  floor until the scoped final boss settles the ending.
- Includes: Basement I through Depths II and first Mom defeat in base Rebirth.
- Excludes: choosing a visible Slay the Spire node edge; a checkpoint inside
  one persistent area; optional post-Mom chapters outside the clean-save route.
- Parameters: floor, boss, clear state, descent, next depth, retained run state,
  final boss and ending.
- Evidence: [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md).
- Novelty: first isolated for `GAME-0164`.

## SYS-469 — Clear terminal run state while retaining eligible save unlocks

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: death or the scoped ending closes the current run and removes its
  floor graph, pickups, health and item build from the next run, while any
  already earned eligible secret, ending or unlock remains in the save file.
- Includes: clean-save base Rebirth death reset and first-Mom Epilogue unlock.
- Excludes: Softcore checkpoint return with the same character build; complete
  save deletion; a manually seeded run that cannot award ordinary unlocks.
- Parameters: terminal cause, transient run state, prior save state, unlock
  condition, achievement eligibility and next-run pool.
- Evidence: [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md).
- Novelty: first isolated for `GAME-0164`; earlier reset genes retain a world or
  character build rather than discarding the whole transient build around save unlocks.

## SYS-470 — Resolve one timed bomb blast against room state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when a placed bomb's fuse expires, the system applies one bounded
  blast to overlapping actors, destructible rocks and eligible secret-room
  walls, then removes the bomb object.
- Includes: ordinary bomb damage, rock destruction and secret-room opening in
  base The Binding of Isaac: Rebirth.
- Excludes: a grenade field persisting after detonation; terrain mining by a
  reusable tool; an item effect with no placed fuse.
- Parameters: fuse, centre, radius, damage, knockback, rock class, wall
  eligibility and item modifiers.
- Evidence: [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md).
- Novelty: first isolated for `GAME-0164`.

## SYS-515 — Run a difficulty-scaled autonomous racing field

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after an authored race starts, the system continuously drives the
  eligible rival field along the same course and scales its pace and behaviour
  through the selected opponent-difficulty profile.
- Includes: Solo Forza Horizon 6 Festival races against Drivatars; the seven
  Relaxed AI rivals in Need for Speed Unbound `Shopping Spree`.
- Excludes: ambient open-world traffic; a human multiplayer field; one fixed
  scripted convoy with no competitive result.
- Parameters: field size, car theme, difficulty, aggression, course, start grid,
  contact and finish state.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md).
- Novelty: first isolated for `GAME-0171`; earlier autonomous agents pursue
  combat, logistics or team roles rather than a shared-course race ranking.

## SYS-516 — Validate ordered race progress and finish result

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system accepts course progress only through the event's
  ordered checkpoints and required laps, then settles elapsed time and, when a
  rival field exists, the complete finish order.
- Includes: Forza Horizon 6 Trail, Circuit, Cross Country, Time Attack and
  Horizon Invitational course completion; Need for Speed Unbound's ordered
  `Shopping Spree` route and eight-place result.
- Excludes: free driving through unvalidated map space; a speed trap with no
  ordered course; points awarded after the validated result.
- Parameters: checkpoint sequence, checkpoint width, lap count, elapsed time,
  participant order, missed-checkpoint recovery and finish line.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md).
- Novelty: first isolated for `GAME-0171`; no prior system jointly validates
  directly driven course order, lap progress and race finish classification.

## SYS-517 — Convert driving-event results into Festival progress

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a first eligible event result or rated driving activity adds its
  declared Horizon Festival Points to retained campaign progress, which can
  cross the threshold for the next Wristband Event.
- Includes: the fixed Horizon Qualifier route that unlocks the first Horizon
  Invitational in Forza Horizon 6.
- Excludes: Discover Japan Stamp progress; live Festival Playlist points;
  credits or experience that do not advance the Wristband meter.
- Parameters: event, first-completion state, rating, points, prior total,
  threshold and overflow.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md).
- Novelty: first isolated for `GAME-0171`; earlier score systems do not convert
  heterogeneous driving-event results into a persistent festival gate.

## SYS-518 — Advance the tourist opening through festival unlock gates

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: completing each mandatory opening gate retains its campaign state
  and exposes the next authored feature set: the Tokyo introduction opens the
  map and Qualifiers, the points threshold exposes the Invitational, and its
  completion grants the first Wristband and Festival access.
- Includes: the scoped Forza Horizon 6 fresh-save opening through first
  Wristband settlement.
- Excludes: later Wristbands, Gold status and Legend Island; Discover Japan
  Stamps; multiplayer progression.
- Parameters: prologue completion, introductory race, qualifier state, point
  threshold, Invitational state, Wristband and feature unlocks.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md).
- Novelty: first isolated for `GAME-0171`; prior authored quest chains do not
  stage one open-world driving campaign through a points-gated race invitation.

## SYS-519 — Settle a completed driving event into retained rewards

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after a valid driving-event result and any declared post-result
  settlement gate, the system records completion and transfers the declared
  credits, experience, cars or feature unlocks into persistent campaign or
  garage state.
- Includes: qualifier results and the three cars granted with the first Forza
  Horizon 6 Wristband; the scoped Need for Speed Unbound result and cash after
  pursuit clearance plus Rydell's Rydes entry.
- Excludes: temporary race position; live Festival Playlist rewards outside the
  scoped opening; buying an Aftermarket Car.
- Parameters: event, completion, position, time, credits, experience, vehicle,
  unlock and retained save state.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md).
- Novelty: first isolated for `GAME-0171`; delivery and combat settlements do
  not retain a curated driving-event result into garage and festival state.

## SYS-520 — Update Drive stock, Burnout and corner Stun

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: drive techniques spend a shared six-stock reserve while eligible
  defence and elapsed live combat can change it; exhaustion enters Burnout,
  recovery eventually restores access, and an eligible corner Drive Impact in
  Burnout can produce Stun.
- Includes: the ordinary Street Fighter 6 Drive Gauge lifecycle.
- Excludes: Super Art stock; one move cooldown; ordinary vitality damage; a
  guard-only stamina break with no offensive uses.
- Parameters: six-stock capacity, technique costs, passive recovery, block and
  punish loss, Burnout entry/recovery, corner state and Stun.
- Evidence: [Street Fighter 6 decomposition](../games/s-z/street-fighter-6.md).
- Novelty: first isolated for `GAME-0172`; the same reserve changes offence,
  defence, mobility and the rules of vulnerability when exhausted.

## SYS-521 — Earn, carry and spend tiered Super Art stock

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: eligible live combat activity increases a bounded three-stock
  meter; a legal tiered Super Art consumes its declared level cost, while
  unspent stock persists across an ordinary round reset.
- Includes: Street Fighter 6's three-level Super Art Gauge in Fighting Ground.
- Excludes: Drive stocks; one-round economy; permanent character experience;
  an ability that merely recovers on a cooldown.
- Parameters: capacity, gain sources, carried amount, Super level, cost,
  activation and round carry-over.
- Evidence: [Street Fighter 6 decomposition](../games/s-z/street-fighter-6.md).
- Novelty: first isolated for `GAME-0172`; earlier live combat resources do not
  combine tiered attack costs with explicit inter-round retention.

## SYS-522 — Adjudicate and reset finite fighting rounds

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: vitality depletion or expiry of the declared round timer
  determines one round result; the system records its marker, resets eligible
  fighter state and begins another round until one side reaches the required
  win count and the match settles.
- Includes: default `99`-second, first-to-two One on One rounds in Street Fighter
  6 Versus.
- Excludes: a team-elimination round with equipment economy; respawning during
  one continuous objective phase; tournament games beyond the in-game match.
- Parameters: vitality comparison, timer, KO, draw policy, round markers, reset
  state, carried resources, required wins and result screen.
- Evidence: [Street Fighter 6 decomposition](../games/s-z/street-fighter-6.md).
- Novelty: first isolated for `GAME-0172`; Counter-Strike's round gene binds
  asymmetric bomb and team-elimination rules, while this boundary resets one
  fixed fighting pair and carries eligible Super stock.

## SYS-523 — Sample a position-conditioned room offer from an authored pool

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when an eligible unopened door is addressed, the system filters
  an authored room pool by current position and estate state, then exposes a
  bounded offer of three candidate plans.
- Includes: ordinary Blue Prince room-plan offers.
- Excludes: unconstrained procedural geometry; drawing one hidden random room;
  a shop inventory unrelated to spatial construction.
- Parameters: day, cell, edge, authored pool, rarity, eligibility, weights,
  offer size and candidate plans.
- Evidence: [Blue Prince decomposition](../games/a-f/blue-prince.md).
- Novelty: first isolated for `GAME-0173`; the sampled alternatives directly
  determine the next room in a player-built traversal graph.

## SYS-524 — Instantiate a drafted room and propagate its graph effects

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a legal plan choice, the system occupies the target manor
  cell, joins compatible doorway edges and applies the room's declared local or
  manor-wide effects.
- Includes: placing one selected Blue Prince room behind the addressed door.
- Excludes: previewing an offer; moving a previously placed tile; rendering a
  cosmetic room with no topology or rule state.
- Parameters: cell, room, orientation, entry edge, exits, role, effect,
  occupancy and graph update.
- Evidence: [Blue Prince decomposition](../games/a-f/blue-prince.md).
- Novelty: first isolated for `GAME-0173`; it couples offer resolution to a
  persistent within-day room graph and authored room effects.

## SYS-525 — Update day-local manor resources and held items

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: traversal, room entry, pickup, purchase, consumption and fixture
  use add or subtract the current day's steps, keys, gems, coins and eligible
  held items according to their typed rules.
- Includes: Blue Prince's ordinary daily resource economy.
- Excludes: permanent estate upgrades; knowledge retained by the player; a
  single universal score with no typed uses.
- Parameters: event, resource type, prior amount, delta, capacity, item,
  persistence horizon and resulting amount.
- Evidence: [Blue Prince decomposition](../games/a-f/blue-prince.md).
- Novelty: first isolated for `GAME-0173`; it binds several typed resources to
  a changing drafted route and explicit daily reset boundary.

## SYS-526 — Rebuild daily manor state while retaining declared progress

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: on a declared day end, the system discards the current drafted
  layout and day-local economy, begins a fresh manor morning and restores only
  explicitly persistent estate changes, records and knowledge state.
- Includes: ordinary between-day Blue Prince rebuilding.
- Excludes: deleting the whole profile; preserving every drafted room; an
  automatic fixed-duration time loop.
- Parameters: day, layout, daily resources, retained upgrades, retained clues,
  next seed, starting room and starting steps.
- Evidence: [Blue Prince decomposition](../games/a-f/blue-prince.md).
- Novelty: first isolated for `GAME-0173`; it separates a drafted spatial graph
  from declared persistent estate progress under a player-called reset.

## SYS-527 — Resolve observation-device movement, feed, scan and loss

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a surviving remote device resolves its supported movement,
  orientation and local field into a live team feed or marked observation, and
  removes that access when the device is disabled or destroyed.
- Includes: Rainbow Six Siege attacker drones, defender cameras and compatible
  observation tools.
- Excludes: direct avatar sight; permanent omniscient tracking; a post-match
  replay camera.
- Parameters: device, owner, position, orientation, field, visibility, scan,
  ping, recipients, health and loss.
- Evidence: [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Novelty: first isolated for `GAME-0174`; information is produced by a
  destructible, controllable spatial node rather than a fixed HUD sensor.

## SYS-528 — Apply defensive fortification layers to eligible surfaces

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a legal defender placement converts an eligible opening or soft
  surface into its declared barricaded or reinforced layer, changing access,
  penetration, sight and compatible breach requirements.
- Includes: Rainbow Six Siege door/window barricades and team-stock wall or
  hatch reinforcements.
- Excludes: indestructible authored geometry; a purely cosmetic skin; damage
  that removes the layer.
- Parameters: surface, material, side, placement duration, team stock, layer,
  durability, access and compatible counters.
- Evidence: [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Novelty: first isolated for `GAME-0174`; it resolves a replenished round-local
  defensive construction layer that explicitly changes opposing breach rules.

## SYS-529 — Resolve injury, team revival and final round elimination

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: qualifying damage may place a living participant into a bounded
  injured state; a legal ally revival returns control with configured health,
  while further or disqualifying damage finalises removal for the round.
- Includes: Rainbow Six Siege down-but-not-out injury, ally revival and final
  elimination.
- Excludes: guaranteed injury from every lethal hit; immediate same-round
  respawn; permanent campaign resurrection.
- Parameters: damage, injury eligibility, bleed state, crawl, revive authority,
  duration, returned health, final damage and round boundary.
- Evidence: [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Novelty: first isolated for `GAME-0174`; it joins one-life round removal to a
  conditional, interruptible teammate recovery window.

## SYS-530 — Rebuild and rotate round-local siege state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after a settled round, the system restores operators and the
  authored map, clears round-local destruction, construction, devices and
  injuries, retains the match score and applies the next site, role and ban
  schedule state.
- Includes: Rainbow Six Siege Pro League round reset, role swap after six
  regulation rounds and scheduled ban-pool changes.
- Excludes: restoring a saved mid-round position; retaining breached geometry;
  resetting the whole match score.
- Parameters: round, score, role, site, operator pool, bans, geometry, devices,
  health, loadout and overtime state.
- Evidence: [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Novelty: first isolated for `GAME-0174`; it rebuilds player-modified tactical
  geometry and devices while rotating declared role and roster state.

## SYS-531 — Resolve autonomous football choices from player state and tactical plan

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each footballer autonomously selects movement, positioning and
  ball actions from the live match state, attributes, assigned role and the
  manager's current in-possession or out-of-possession plan.
- Includes: Football Manager 26 match-engine player and team decisions.
- Excludes: direct avatar control; a fixed authored highlight; formation
  editing before confirmation.
- Parameters: player attributes, condition, role, possession phase, formation,
  instruction, teammates, opponents, ball, score and match time.
- Evidence: [Football Manager 26 decomposition](../games/a-f/football-manager-26.md).
- Novelty: first isolated for `GAME-0175`; it makes the declared managerial
  policy, rather than moment-to-moment body input, the source of team action.

## SYS-532 — Update player condition, performance and injury through the fixture

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: live participation and incidents update each footballer's
  condition, performance assessment and injury availability, changing the
  evidence and legal options for later managerial interventions.
- Includes: Football Manager 26 match condition, ratings and injuries.
- Excludes: long-term training development; contract morale; cosmetic sweat.
- Parameters: minutes, workload, fatigue, incident, injury, rating, position,
  role and substitution status.
- Evidence: [Football Manager 26 decomposition](../games/a-f/football-manager-26.md).
- Novelty: first isolated for `GAME-0175`; it binds evolving per-agent
  performance evidence to a manager-only substitution decision loop.

## SYS-533 — Record a managed fixture result in persistent competition state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after regulation settles, the career records the fixture score
  and outcome and applies the declared competition consequences to its results
  and table state.
- Includes: a Football Manager 26 Premier League result and updated table.
- Excludes: a temporary Kick Off score; an unplayed fixture prediction; an
  entire season's final classification.
- Parameters: fixture, score, outcome, points policy, table rows, played count,
  goals and career save.
- Evidence: [Football Manager 26 decomposition](../games/a-f/football-manager-26.md).
- Novelty: first isolated for `GAME-0175`; earlier match settlement terminates
  one play session without committing its result to a persistent league state.

## SYS-534 — Refresh and spend per-soldier Action Points inside a squad phase

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: at the player phase boundary each available soldier receives a
  small personal Action Point allowance; legal commands spend that allowance,
  with declared terminal actions consuming all remaining authority.
- Includes: XCOM 2's two-action soldier turns, blue first move and yellow final
  move in Operation Gatecrasher.
- Excludes: one shared team energy pool; initiative-ordered individual turns;
  real-time cooldowns.
- Parameters: soldier, refreshed points, command cost, movement band, terminal
  action, free action and remaining authority.
- Evidence: [XCOM 2 decomposition](../games/s-z/xcom-2.md).
- Novelty: first isolated for `GAME-0176`; unlike a single-character turn
  economy, several soldiers retain independently spendable authority inside
  one freely interleaved squad phase.

## SYS-535 — Break squad concealment and activate a revealed hostile pod

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: detection or a concealment-breaking action reveals the squad,
  while newly exposed inactive hostiles enter alerted tactical behaviour and
  take their activation movement before later phase decisions.
- Includes: XCOM 2 concealment, detection tiles and ADVENT pod activation.
- Excludes: ordinary fog-of-war reveal without behavioural activation;
  permanent invisibility; a scripted cutscene with no tactical consequence.
- Parameters: concealed side, detector, detection radius, sight, breaking
  action, pod membership, activation movement and alert state.
- Evidence: [XCOM 2 decomposition](../games/s-z/xcom-2.md).
- Novelty: first isolated for `GAME-0176`; it couples information exposure to
  a coordinated hostile-state transition rather than revealing units alone.

## SYS-536 — Resolve prepared reaction fire on eligible hostile movement

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when a hostile moves through the legal sight and weapon state of
  a soldier with prepared reaction fire, the system interrupts movement to
  resolve one modified ranged attack and consumes the preparation.
- Includes: XCOM 2 Overwatch fire during the enemy phase.
- Excludes: an immediate selected shot; unlimited automatic turret fire;
  reaction against a target that never moved through eligible sight.
- Parameters: prepared soldier, hostile movement segment, sight, ammunition,
  trigger, accuracy modifier, attack result and consumption.
- Evidence: [XCOM 2 decomposition](../games/s-z/xcom-2.md).
- Novelty: first isolated for `GAME-0176`; the resolution crosses a faction
  phase boundary and is conditional on a later opponent movement event.

## SYS-537 — Select and resolve hostile commands during the enemy squad phase

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after the player commits the squad phase, each surviving alerted
  hostile selects legal movement, cover and attack behaviour from the visible
  tactical state and the system resolves those commands before player refresh.
- Includes: XCOM 2 ADVENT and Sectoid behaviour in Operation Gatecrasher.
- Excludes: a human-controlled opponent; pre-disclosed deterministic intent;
  simultaneous real-time combat.
- Parameters: hostile, alert state, reachable cells, targets, cover, ability,
  attack probability, resolution order and surviving state.
- Evidence: [XCOM 2 decomposition](../games/s-z/xcom-2.md).
- Novelty: first isolated for `GAME-0176`; it is an autonomous faction phase
  operating against a freely interleaved multi-soldier player phase.

## SYS-538 — Settle soldier health into recovery, wounds or permanent loss

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: tactical damage updates a soldier's health and death state; at
  mission settlement a survivor returns for immediate use or wound recovery,
  while a killed soldier is permanently absent from the campaign roster.
- Includes: XCOM 2 mission health, wounds and permanent soldier death.
- Excludes: same-turn respawn; cosmetic injury; guaranteed recovery of a killed
  soldier.
- Parameters: health, damage, lethal threshold, survival, wound severity,
  recovery duration and roster state.
- Evidence: [XCOM 2 decomposition](../games/s-z/xcom-2.md).
- Novelty: first isolated for `GAME-0176`; it connects bounded tactical health
  to persistent post-mission availability without modelling the full campaign.

## SYS-539 — Integrate rocket-car motion across surfaces and air

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system continuously integrates one dedicated car's steering,
  throttle, braking, powerslide, jump, dodge, aerial orientation, gravity and
  collision into ground, wall, ceiling and airborne motion.
- Includes: Rocket League standard-arena car movement and recovery.
- Excludes: occupant health or vehicle-part damage; an autonomous racing line;
  entering and leaving a world vehicle.
- Parameters: hitbox, mass, velocity, angular velocity, traction, surface,
  gravity, steering, jump, dodge, orientation and contact impulse.
- Evidence: [Rocket League decomposition](../games/m-r/rocket-league.md).
- Novelty: first isolated for `GAME-0177`; `SYS-320` joins vehicle motion to
  damage and occupants, while this boundary centres surface-to-air car control.

## SYS-540 — Refill and spend spatial vehicle boost

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: crossing a ready arena boost pad transfers its declared amount
  into the vehicle's capped reserve and makes that pad unavailable until its
  recharge completes; active boost then consumes reserve as directed thrust.
- Includes: Rocket League small and large boost pads, the ten-second large-pad
  recharge and ground or aerial boost use.
- Excludes: passive throttle; a carried consumable; unlimited boost mutators.
- Parameters: pad class, position, ready state, recharge, pickup amount,
  reserve cap, current reserve, thrust and spend rate.
- Evidence: [Rocket League decomposition](../games/m-r/rocket-league.md).
- Novelty: first isolated for `GAME-0177`; the same spatial nodes repeatedly
  replenish a shared movement resource during continuous competitive play.

## SYS-541 — Resolve vehicle bump, demolition and timed respawn

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: car-car contact transfers a physical bump unless a legal
  demolition-speed contact temporarily removes the struck car; after the
  declared delay, an eligible own-side spawn restores that car to live play.
- Includes: Rocket League bumps, supersonic demolitions and same-match respawn.
- Excludes: persistent vehicle damage; round-long elimination; scoring a point
  merely for demolition under default mutators.
- Parameters: attacker velocity, contact direction, demolition eligibility,
  removed car, delay, offered spawn, fallback selection and returned state.
- Evidence: [Rocket League decomposition](../games/m-r/rocket-league.md).
- Novelty: first isolated for `GAME-0177`; removal is a short positional cost
  inside uninterrupted team play, not health depletion or round elimination.

## SYS-542 — Advance zero-second regulation into sudden-death overtime

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the five-minute match clock counts down during live Soccar; at
  zero the current ball remains live until a valid grounding or goal, after
  which a tied score starts unlimited sudden-death overtime and the first legal
  goal settles the winner.
- Includes: Rocket League default Soccar regulation and overtime settlement.
- Excludes: a draw accepted at regulation; fixed extra-time periods; penalty
  shoot-outs; account rank updates.
- Parameters: regulation length, score, zero-second ball state, grounding,
  overtime state, deciding goal and winner.
- Evidence: [Rocket League decomposition](../games/m-r/rocket-league.md).
- Novelty: first isolated for `GAME-0177`; clock expiry is conditionally delayed
  by live-ball state before a goal-only sudden-death phase.

## SYS-543 — Deplete and replenish the survivor oxygen reserve

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while the avatar lacks a breathable source the system reduces carried oxygen over real time, warns at low reserve and applies suffocation at exhaustion, while a surface or powered breathable interior refills it.
- Includes: Subnautica diving, surface breathing, Lifepod, powered Seabase and powered Seamoth oxygen.
- Excludes: calories or hydration; a one-shot air consumable without a live reserve; vehicle crush damage.
- Parameters: capacity, depletion rate, warning thresholds, breathable source, refill rate, exhaustion grace and lethal damage.
- Evidence: [Subnautica decomposition](../games/s-z/subnautica.md).
- Novelty: first isolated for `GAME-0178`; reachable spatial air nodes govern a continuously depleting excursion reserve.

## SYS-544 — Accumulate scan progress and unlock fragment blueprint

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: valid held scanning accumulates resumable target progress; a completed technology fragment increments its blueprint counter and the required count turns that recipe into persistent known state.
- Includes: Subnautica Mobile Vehicle Bay and Seamoth fragment scanning.
- Excludes: consuming research currency; opening a single data box; merely reading an already known recipe.
- Parameters: target, progress, range, interruption, fragment class, current count, required count, duplicate conversion and blueprint state.
- Evidence: [Subnautica decomposition](../games/s-z/subnautica.md).
- Novelty: first isolated for `GAME-0178`; physical observations are counted toward a class-specific fabrication unlock.

## SYS-545 — Resolve one powered fabricator recipe

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an available powered fabricator accepts one legal known recipe, consumes its declared ingredients and energy where applicable, runs its fabrication interval and presents the output for inventory transfer.
- Includes: Subnautica Lifepod or Seabase Fabricator conversion and Mobile Vehicle Bay Seamoth fabrication.
- Excludes: a persistent multi-item personal crafting queue; autonomous factory production; Habitat Builder module placement.
- Parameters: station, power source, recipe, ingredients, energy cost, duration, output and uncollected-output blocking.
- Evidence: [Subnautica decomposition](../games/s-z/subnautica.md).
- Novelty: first isolated for `GAME-0178`; one powered station transformation owns its output until the player can collect it.

## SYS-546 — Resolve connected habitat integrity, breaches and flooding

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: completed modules join a connected underwater habitat and change its depth-sensitive hull integrity; non-positive integrity creates breaches and propagating water until integrity and leaks are repaired.
- Includes: a Subnautica I Compartment and Hatch retaining positive integrity, or an overextended Seabase flooding after integrity reaches zero.
- Excludes: vehicle crush damage; visual water outside a sealed base; ordinary building health without a shared pressure-hull value.
- Parameters: connected module, base integrity, module modifier, depth, breach, flooded volume, compartment boundary, repair and dry state.
- Evidence: [Subnautica decomposition](../games/s-z/subnautica.md).
- Novelty: first isolated for `GAME-0178`; connected construction shares one pressure budget whose failure changes the interior medium.

## SYS-547 — Generate and distribute habitat power and oxygen

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an eligible generator converts its environmental input into stored habitat energy, connected systems consume that reserve, and a powered dry habitat maintains breathable interior oxygen.
- Includes: a shallow Subnautica Solar Panel charging a connected Seabase and enabling its oxygen supply.
- Excludes: vehicle Power Cell discharge; daylight as visual ambience only; oxygen inside an unpowered flooded module.
- Parameters: generator, light or fuel input, generation rate, storage cap, connected load, power priority, dry state and oxygen availability.
- Evidence: [Subnautica decomposition](../games/s-z/subnautica.md).
- Novelty: first isolated for `GAME-0178`; one stored network resource gates both habitat fixtures and the breathable interior state.

## SYS-548 — Consume submersible energy and apply collision or crush damage

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: operating a piloted submersible consumes installed energy while contact damage and time below its current crush depth reduce vehicle health, potentially destroying it while the world continues.
- Includes: an unmodified Subnautica Seamoth using its Power Cell, taking collision damage and becoming unsafe below 200 m.
- Excludes: avatar oxygen depletion; land-vehicle fuel only; a depth marker with no damage consequence.
- Parameters: Power Cell charge, movement load, lights, health, collision, depth, crush threshold, warning, damage cadence and destruction.
- Evidence: [Subnautica decomposition](../games/s-z/subnautica.md).
- Novelty: first isolated for `GAME-0178`; vehicle range and vertical operating envelope share energy, health and pressure limits.

## SYS-549 — Gather and deposit a finite map resource

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an assigned worker repeatedly extracts a carried quantity from its reachable world source, returns it to a compatible drop-off building and adds it to the owner's shared stockpile until interrupted or exhausted.
- Includes: Age of Empires II villagers gathering Food, Wood, Gold or Stone.
- Excludes: instantaneous hand collection into personal inventory; city-turn yield aggregation; automated mining with no worker return route.
- Parameters: worker, resource class, source reserve, carry capacity, gather rate, drop-off class, path and stockpile.
- Evidence: [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
- Novelty: first isolated for `GAME-0179`; it couples finite spatial extraction, worker carrying and a required return trip into one live economy loop.

## SYS-550 — Advance villager construction and repair work

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: each eligible assigned villager contributes timed work to an owned foundation or damaged entity, completing construction or restoring hit points while the task and target remain legal.
- Includes: Age of Empires II building construction and villager repair.
- Excludes: instant player placement; autonomous construction robots supplied from a logistics network; passive regeneration.
- Parameters: target, builder count, build or repair time, work-rate scaling, resource cost, cancellation, hit points and completion state.
- Evidence: [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
- Novelty: first isolated for `GAME-0179`; the live selected workers themselves supply construction or repair progress.

## SYS-551 — Advance a building-local unit training queue

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an owned production building advances the front paid unit order over real time, creates the unit when training completes and then advances the next queued order if its release remains legal.
- Includes: Villager and military production queues in Age of Empires II: Definitive Edition.
- Excludes: a city's per-turn production target; scheduled free wave spawning; an item recipe that repeatedly runs without discrete queued orders.
- Parameters: building, queue, unit, training time, owner, completion, spawn cell, rally point and blocked release.
- Evidence: [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
- Novelty: first isolated for `GAME-0179`; it preserves simultaneous finite queues across multiple player-built RTS production structures.

## SYS-552 — Complete building-bound technology or Age research

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a paid research order occupies its eligible building for a declared live duration, then persistently applies the technology, unit, building or next-Age unlocks to the owning civilization.
- Includes: economic and military technologies and Feudal, Castle and Imperial Age advancement in Age of Empires II: Definitive Edition.
- Excludes: science-point accumulation across laboratories; turn-settled technology income; character experience levels.
- Parameters: building, research, cost, duration, prerequisites, current Age, civilization tree, completion and unlocked effects.
- Evidence: [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
- Novelty: first isolated for `GAME-0179`; progress is a paid building-local real-time order, not a global research currency stream.

## SYS-553 — Apply housing capacity to live unit production

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: completed capacity-providing buildings raise the owner's current population ceiling up to the match maximum, while unit creation occupies population space and stalls when no legal headroom remains.
- Includes: Houses, Town Centers and Castles supporting Age of Empires II unit production under the scoped population-200 limit.
- Excludes: residential happiness; abstract labour slots; a fixed team roster with no constructed capacity.
- Parameters: used population, current capacity, match maximum, provider, unit cost, destruction and blocked queue.
- Evidence: [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
- Novelty: first isolated for `GAME-0179`; constructed world buildings directly gate release from concurrent military and economic queues.

## SYS-554 — Resolve ordered group movement through formation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a selected group maps its members into the active formation, paths toward the ordered destination at a group-compatible pace and then applies its stance while acquiring or refusing eligible targets.
- Includes: formation movement and stance-governed engagement in Age of Empires II: Definitive Edition.
- Excludes: one unit's ordinary path; a manager's abstract team shape; a scripted autonomous lane wave.
- Parameters: group, member classes, formation slots, path, speed, facing, stance, regroup and target acquisition.
- Evidence: [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
- Novelty: first isolated for `GAME-0179`; group topology and engagement policy remain coupled throughout command execution.

## SYS-555 — Settle Conquest elimination or resignation

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the match awards victory when every opposing civilization has resigned or lost the unit and production-building set required by Conquest, and applies defeat symmetrically to the player's civilization.
- Includes: one-versus-one Conquest victory or resignation in Age of Empires II: Definitive Edition.
- Excludes: Wonder and Relic countdowns; score-at-time-limit victory; campaign triggers; destruction of one designated Ancient.
- Parameters: civilizations, alliance, surviving villagers, military units, production buildings, resignation and terminal result.
- Evidence: [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
- Novelty: first isolated for `GAME-0179`; the terminal evaluates an entire civilization's recoverable production capacity rather than one structure.

## SYS-556 — Integrate fixed-wing aerodynamics and ground contact

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the system continuously combines aircraft configuration, control
  deflection, propulsion, atmosphere, gravity and surface contact into attitude,
  airspeed, altitude, trajectory, taxi motion, takeoff, landing and unsafe
  envelope consequences.
- Includes: the scoped Microsoft Flight Simulator 2024 Cessna 172 G1000 ground
  run, climb, cruise, descent, flare, touchdown and rollout.
- Excludes: generic occupied road-vehicle traction; autonomous scripted flight;
  purely cosmetic turbulence or scenery streaming.
- Parameters: mass, centre of gravity, lift, drag, thrust, control surface,
  flap, trim, wind, density, attitude, speed, terrain, runway and contact force.
- Evidence: [Microsoft Flight Simulator 2024 decomposition](../games/m-r/microsoft-flight-simulator-2024.md).
- Novelty: first isolated for `GAME-0180`; runway contact and airborne energy
  remain one causally continuous manually controlled fixed-wing model.

## SYS-557 — Resolve piston-engine, fuel and electrical state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: connected fuel and electrical components determine whether the
  piston engine can start and continue producing power and whether dependent
  avionics, instruments, lights and circuits remain energised.
- Includes: the scoped Microsoft Flight Simulator 2024 Cessna 172 cold start,
  fuel consumption, powered flight and destination shutdown.
- Excludes: abstract vehicle fuel with no operable system graph; unlimited
  arcade boost; aircraft selection before the flight loads.
- Parameters: tank, selector, line, valve, mixture, magneto, starter, engine,
  RPM, battery, alternator, bus, circuit, load, fuel quantity and shutdown.
- Evidence: [Microsoft Flight Simulator 2024 decomposition](../games/m-r/microsoft-flight-simulator-2024.md).
- Novelty: first isolated for `GAME-0180`; propulsion and cockpit availability
  share an operable component dependency chain that the player starts and stops.

## SYS-558 — Load and advance an active avionics flight plan

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the system loads the declared aeronautical plan into compatible
  navigation surfaces and updates aircraft position, active leg, track,
  deviation, distance and waypoint progression as the manual flight moves.
- Includes: the scoped VFR direct plan shared by Microsoft Flight Simulator
  2024 Free Flight, EFB and Cessna 172 G1000 avionics.
- Excludes: road-route recalculation; autopilot control; ATC clearance authority;
  an authored mission marker with no player-selected plan.
- Parameters: origin, destination, procedure, waypoint, leg, aircraft position,
  desired track, cross-track deviation, distance, activation and completion.
- Evidence: [Microsoft Flight Simulator 2024 decomposition](../games/m-r/microsoft-flight-simulator-2024.md).
- Novelty: first isolated for `GAME-0180`; an aeronautical route persists across
  planning and cockpit surfaces while remaining advisory to direct control.

## SYS-559 — Record a completed Free Flight in the logbook

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after the bounded Free Flight reaches an eligible destination
  ground terminal, the system adds the flight to the persistent logbook and
  emits the current in-flight entry notification.
- Includes: Sim Update 6 Microsoft Flight Simulator 2024 Free Flight logbook
  settlement after the scoped destination parking and shutdown.
- Excludes: Career reward scoring; an unrecorded touch-and-go; a user-authored
  note; exiting before the flight qualifies for a logbook entry.
- Parameters: flight identity, origin, destination, departure, arrival, duration,
  ground state, shutdown state, entry identifier and notification.
- Evidence: [Microsoft Flight Simulator 2024 decomposition](../games/m-r/microsoft-flight-simulator-2024.md).
- Novelty: first isolated for `GAME-0180`; the terminal converts one continuous
  manual simulation into an explicit persistent non-career flight record.

## SYS-560 — Settle a map ballot through landslide or weighted selection

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after the pre-match vote closes, a qualifying vote margin picks
  its choice directly; otherwise valid votes define the declared selection
  weights, with Random Map resolving outside the visible candidate set.
- Includes: current Overwatch Quick Play map voting, six-vote landslide margin,
  weighted ballot and Random Map option.
- Excludes: deterministic host map selection; competitive character bans;
  background matchmaking that exposes no player ballot.
- Parameters: candidates, votes, margin, landslide threshold, weights, random
  pool, recency and selected map.
- Evidence: [Overwatch decomposition](../games/m-r/overwatch.md).
- Novelty: first isolated for `GAME-0181`; collective influence combines a
  direct majority override with otherwise probabilistic settlement.

## SYS-561 — Convert Control ownership into percentage and a round win

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while one team owns the active neutral point, its retained round
  percentage rises toward the terminal value; reaching that value after any
  legal contest awards the round to that team.
- Includes: ordinary Overwatch Quick Play Control ownership, percentage and
  100-percent round settlement.
- Excludes: capturing an escort vehicle; draining reinforcement tickets from
  several simultaneously owned points; personal kill-score accumulation.
- Parameters: point, owner, team percentages, score rate, terminal percentage,
  contest, overtime and round winner.
- Evidence: [Overwatch decomposition](../games/m-r/overwatch.md).
- Novelty: first isolated for `GAME-0181`; retained percentage is produced by
  exclusive point ownership rather than by independent kills or ticket drain.

## SYS-562 — Reset Control point state and settle the first two rounds

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after each Control round, the next authored submap begins with a
  fresh neutral point and zero local percentages while team round wins persist;
  the first team to two round wins receives the match result.
- Includes: ordinary Overwatch Quick Play Control best-of-three settlement.
- Excludes: regulation bomb rounds with side swaps; a single continuous ticket
  pool; tournament series across separately queued matches.
- Parameters: submap order, point state, percentages, retained round score,
  clinch threshold and match winner.
- Evidence: [Overwatch decomposition](../games/m-r/overwatch.md).
- Novelty: first isolated for `GAME-0181`; local spatial-score state resets
  between authored arenas while only the two-round match score persists.

## SYS-563 — Advance and complete the active National Focus

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while national time advances, the active eligible focus gains
  progress; completion applies its declared persistent country effects and
  releases the focus channel for another choice.
- Includes: base-game Italian focus progress during the scoped tutorial war.
- Excludes: research-slot progress; a random event with no selected focus;
  player selection of the next focus.
- Parameters: country, focus, daily progress, duration, completion, effects,
  cancellation and retained state.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; country development occupies a single
  selected calendar-progress channel distinct from parallel technology work.

## SYS-564 — Advance parallel national research slots

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each occupied national research slot independently accumulates
  calendar progress toward its selected reachable technology and applies that
  technology's unlocks or modifiers on completion.
- Includes: simultaneous industrial, electronic, land or air research in the
  scoped Italian tutorial.
- Excludes: a building-local research queue; National Focus progress; hidden
  automatic invention.
- Parameters: slot count, target, prerequisite, base duration, ahead-of-time
  modifier, research bonus, completion and effects.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; several national calendar channels
  progress independently without belonging to physical production sites.

## SYS-565 — Distribute civilian factories through the construction queue

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: available civilian factories contribute continuing construction
  work to eligible national queue entries by priority and complete each target
  into its persistent state level.
- Includes: Italian civilian factories building infrastructure or factories in
  eligible states.
- Excludes: military equipment output; individual worker travel; purchasing a
  completed building.
- Parameters: available factories, queue order, per-project cap, modifiers,
  state slot, progress, damage, repair and completion.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; a mobile national capacity pool flows
  across an ordered set of spatial projects.

## SYS-566 — Convert factory allocation and resources into equipment

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: each active military production line combines its allocated
  factories, resource satisfaction and retained efficiency into continuing
  equipment output deposited in the national stockpile.
- Includes: infantry equipment, artillery and aircraft production in the
  scoped Italian tutorial.
- Excludes: civilian state construction; equipment distribution to divisions;
  instantaneous inventory crafting.
- Parameters: line, factory count, resource need and satisfaction, efficiency,
  cap, output rate, variant, stockpile and conversion loss.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; national portfolio allocation and
  line history jointly determine continuous material output.

## SYS-567 — Reinforce divisions from manpower and equipment stockpiles

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible national manpower and compatible stockpiled equipment
  are distributed over time to divisions according to need, access and priority,
  restoring or completing their fielded strength.
- Includes: replacing Italian infantry losses and filling equipment shortages
  during the tutorial war.
- Excludes: producing the equipment; healing one directly controlled avatar;
  spawning a free full-strength unit.
- Parameters: recipient, template need, manpower, equipment type, stockpile,
  reinforcement priority, delivery, attrition and resulting strength.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; nation-scale inventory becomes
  combat-body readiness through delayed typed distribution.

## SYS-568 — Execute battle plans and resolve division combat

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: assigned divisions distribute and advance under an active army
  plan or manual override, then resolve province-scale combat through current
  strength, organisation, width, terrain, weather and support until movement,
  retreat or defeat changes control.
- Includes: Italian northern and southern front operations against Ethiopia.
- Excludes: embodied weapon aiming; selecting or drawing the plan; strategic
  supply propagation itself.
- Parameters: plan, division, path, province, frontage, organisation, strength,
  planning, entrenchment, terrain, weather, tactics, damage, retreat and control.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; persistent authored front geometry
  drives many abstract divisions through continuous territorial combat.

## SYS-569 — Propagate theatre supply through rails and hubs

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the system routes available supply from the national capital over
  railway capacity to hubs, then distributes it across local terrain and
  motorised reach to eligible divisions, applying deficits where demand exceeds
  delivered capacity.
- Includes: East African rail, hub and last-mile supply for Italian armies.
- Excludes: military equipment production; direct inventory transfer by the
  player; naval convoy logistics outside the scoped route.
- Parameters: capital, rail path and level, train availability, hub throughput,
  motorisation, trucks, terrain, weather, local supply, demand and deficit.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; a hierarchical spatial network
  continuously converts national capacity into local army viability.

## SYS-570 — Resolve regional air missions and land support

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: eligible assigned air wings generate sorties in their selected
  region and mission, applying coverage-, range-, detection- and opposition-
  dependent effects to regional air state and supported land combat.
- Includes: fighter air superiority and close air support over the scoped
  Ethiopian theatre.
- Excludes: direct aircraft piloting; aircraft factory output; strategic bombing
  outside the tutorial route.
- Parameters: region, mission, aircraft, base, range, coverage, weather, fuel,
  efficiency, detection, opposition, sortie and land-support effect.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; a regional scheduled agent pool
  modifies a separate land-resolution system without direct unit steering.

## SYS-571 — Convert territorial loss into capitulation and war settlement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: controlled provinces and weighted victory points update a
  country's surrender progress; crossing its legal threshold causes
  capitulation and permits the immediate terminal war settlement.
- Includes: Ethiopian capitulation and conclusion of the scoped tutorial war.
- Excludes: destruction of one fixed base; a battle win with the country still
  fighting; occupation and resistance after settlement.
- Parameters: country, controlled territory, victory-point weight, surrender
  limit, progress, capitulation, remaining belligerents and settlement outcome.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; distributed territorial control is
  aggregated into a country-level terminal rather than a single-target defeat.

## SYS-572 — Spawn time-indexed hostile waves around a surviving avatar

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while a bounded survival-stage clock advances, the system creates
  authored enemy types and bosses at their scheduled minutes around the current
  avatar and directs them into the live field.
- Includes: ordinary normal-mode Mad Forest waves and minute bosses in
  Vampire Survivors.
- Excludes: enemies generated by a player-placed world tile; one finite carrier
  landing; random encounter selection between rooms.
- Parameters: stage, minute, enemy type, quantity, spawn region, frequency,
  boss, movement rule and stage modifier.
- Evidence: [Vampire Survivors decomposition](../games/s-z/vampire-survivors.md).
- Novelty: first isolated for `GAME-0183`; authored clock-indexed population
  pressure continuously surrounds one freely steered survivor.

## SYS-573 — Resolve cooldown-driven weapons without attack commands

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: every equipped run weapon activates from its own cooldown and
  targeting or attack geometry without a player-issued strike, then resolves
  its projectiles or areas, damage, knockback and enemy defeat.
- Includes: Antonio's directional Whip and other ordinary base-game Vampire
  Survivors weapons obtained during the scoped run.
- Excludes: directly aimed real-time attacks; autonomous squad members that
  first acquire a contextual combat target; one passive contact hazard.
- Parameters: weapon, level, cooldown, targeting, facing, projectile count,
  area, duration, damage, knockback and defeat.
- Evidence: [Vampire Survivors decomposition](../games/s-z/vampire-survivors.md).
- Novelty: first isolated for `GAME-0183`; the player shapes coverage by moving
  while several build-owned attack clocks execute independently.

## SYS-574 — Convert defeated enemies into magnet-collected experience

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an eligible defeated enemy leaves an experience gem, and avatar
  proximity pulls that gem into the character and credits its run-local
  experience value rather than placing an item in carried inventory.
- Includes: blue, green and red Experience Gems in Vampire Survivors.
- Excludes: manually looting a container; contact pickup into a bounded
  inventory slot; experience awarded directly with no world pickup.
- Parameters: enemy, gem value, drop position, magnet radius, attraction,
  contact, experience counter and ground consolidation.
- Evidence: [Vampire Survivors decomposition](../games/s-z/vampire-survivors.md).
- Novelty: first isolated for `GAME-0183`; spatial risk determines when defeated
  enemies become threshold progression through a non-inventory pickup field.

## SYS-575 — Present an eligible random level-up offer

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when run-local experience crosses the next level threshold, the
  live stage pauses and the system samples a non-duplicated finite offer from
  currently eligible weapons, passive items and owned upgrades.
- Includes: ordinary three- or four-option Vampire Survivors level-up screens
  under a clean save with no Reroll, Skip, Banish or Random LevelUp.
- Excludes: an always-open shop; a deterministic technology unlock; automatic
  random selection when the player has enabled Random LevelUp.
- Parameters: threshold, level, pool, rarity weight, option count, duplicate
  rule, owned item, maximum level, slot capacity and pause.
- Evidence: [Vampire Survivors decomposition](../games/s-z/vampire-survivors.md).
- Novelty: first isolated for `GAME-0183`; live spatial XP collection repeatedly
  interrupts one fixed-duration stage with a constrained build draft.

## SYS-576 — Apply the selected weapon or passive level to the run build

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: committing one level-up option adds its new weapon or passive to
  the current run or advances an owned item's declared level, immediately
  recomputing the compatible cumulative build before live play resumes.
- Includes: adding or upgrading base-game weapons and passive items during one
  normal Mad Forest run.
- Excludes: persistent account PowerUps; replacing an inventory object with a
  separately carried item; the later chest evolution transition.
- Parameters: item, item class, prior level, next level, slot, stat changes,
  weapon activation reset, cumulative modifiers and run lifetime.
- Evidence: [Vampire Survivors decomposition](../games/s-z/vampire-survivors.md).
- Novelty: first isolated for `GAME-0183`; a paused draft directly rewrites the
  independently ticking automatic weapon portfolio of the same live run.

## SYS-577 — Resolve an eligible boss chest into upgrade or evolution

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: collecting a chest dropped by a defeated boss samples its legal
  reward; if that chest can evolve and a maximum-level base weapon has its
  required counterpart, the system replaces the base weapon with its evolved
  form, otherwise it grants an eligible item level or ordinary reward.
- Includes: replacing maximum-level Whip with Bloody Tear when Hollow Heart and
  an evolution-capable Mad Forest chest are present.
- Excludes: selecting an ordinary level-up option; crafting two inventory
  components; DLC unions, gifts and character-specific bypasses.
- Parameters: boss, chest configuration, reward count, eligible items, maximum
  level, counterpart, evolution permission, replacement and fallback reward.
- Evidence: [Vampire Survivors decomposition](../games/s-z/vampire-survivors.md).
- Novelty: first isolated for `GAME-0183`; a world-drop reward conditionally
  substitutes one mature automatic weapon using a separately acquired passive.

## SYS-578 — Apply damage and healing to one continuous run health pool

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: hostile contact or attacks reduce the avatar's single current
  health pool, compatible effects restore missing health, and reaching zero
  closes the current run unless a scoped revival prevents the terminal.
- Includes: Antonio's ordinary Max Health, enemy damage, Floor Chicken healing
  and Bloody Tear critical-hit healing in normal Mad Forest.
- Excludes: ordered coexisting heart layers; a shield/downed/revive stack;
  health restored automatically between separate encounters.
- Parameters: maximum health, current health, armour, incoming damage, recovery,
  healing cap, invulnerability interval, revival and death.
- Evidence: [Vampire Survivors decomposition](../games/s-z/vampire-survivors.md).
- Novelty: first isolated for `GAME-0183`; one uninterrupted survival field
  couples contact avoidance, optional healing and the disposable run terminal.

## SYS-579 — Complete the stage clock and dispatch the terminal Reaper

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when a non-Endless stage reaches its authored time limit, the
  system marks the stage complete, spawns a Reaper each following minute and
  settles the completed run after death, including the declared completion
  reward.
- Includes: normal Mad Forest reaching `30:00`, its first Reaper and subsequent
  run result in Vampire Survivors.
- Excludes: Endless wave cycling; treating Reaper defeat as necessary for stage
  completion; an external timer that only scores performance.
- Parameters: stage clock, time limit, completion flag, Reaper cadence, damage,
  completion reward, revival and result screen.
- Evidence: [Vampire Survivors decomposition](../games/s-z/vampire-survivors.md).
- Novelty: first isolated for `GAME-0183`; success precedes an intentionally
  overwhelming hostile cleanup transition rather than immediate quiet victory.

## SYS-580 — Resolve a ground-vehicle shot through armour and internal components

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the system projects a fired round along its current ballistic
  path, tests impact angle and penetration against layered armour, then applies
  any surviving path and effect to spatially located crew, ammunition and
  vehicle modules rather than subtracting one undifferentiated health value.
- Includes: cannon and heavy-machine-gun impacts among the scoped War Thunder
  Rank I Ground Arcade vehicles.
- Excludes: hitscan damage to a single character health pool; abstract unit
  strength loss; aircraft, naval and later guided-weapon damage models.
- Parameters: ammunition, trajectory, distance, impact angle, armour layer,
  penetration, ricochet, post-penetration effect, crew, module and ammunition
  rack.
- Evidence: [War Thunder decomposition](../games/s-z/war-thunder.md).
- Novelty: first isolated for `GAME-0184`; armour geometry and the projectile's
  continuing internal path determine which separate functions or crew roles are
  lost, not only whether an external target was hit.

## SYS-581 — Apply Arcade partial-function damage and vehicle loss

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: damage to ground-vehicle crew and modules reduces their specific
  effectiveness under Arcade rules, preserves declared partial module function
  where applicable and marks the vehicle lost when its surviving combat state
  no longer satisfies the mode's vehicle-loss predicate.
- Includes: impaired engine, gun, aiming drive or crew state after a penetrating
  hit in the scoped War Thunder Ground Arcade match.
- Excludes: one generic hit-point depletion; Realistic-mode fully disabled
  modules; hangar repair cost or modification research.
- Parameters: module, damage state, effectiveness penalty, crew role, crew
  count, mobility, firing capability, ammunition detonation and loss predicate.
- Evidence: [War Thunder decomposition](../games/s-z/war-thunder.md).
- Novelty: first isolated for `GAME-0184`; internal damage changes several
  causal vehicle functions before the same vehicle reaches its terminal state.

## SYS-582 — Return a lost ground vehicle to bounded lineup selection

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after the active ground vehicle is lost, the system removes it
  from live control, records the consumed ground spawn and presents another
  currently eligible lineup vehicle while any scoped spawn remains.
- Includes: returning from a destroyed M2A4 to the fixed USA lineup and spawning
  an unused LVT(A)(1) or M2A2 in Ground Arcade without backups.
- Excludes: revival of the destroyed vehicle; aircraft airstrike events;
  Realistic spawn-point purchasing; returning to the hangar early.
- Parameters: lost vehicle, lineup, consumed spawn, eligible vehicles, backup,
  spawn cap, selection state and exhausted state.
- Evidence: [War Thunder decomposition](../games/s-z/war-thunder.md).
- Novelty: first isolated for `GAME-0184`; repeated combat lives are different
  selected vehicles drawn from one locked lineup rather than copies of one
  character or a free spawn-point network.

## SYS-583 — Convert Domination control and vehicle losses into team tickets

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: destroying an enemy ground vehicle debits its team's tickets,
  while ownership of more of the three Domination points repeatedly drains the
  opposing pool in proportion to the ownership difference; zero tickets or no
  players able to spawn ground vehicles settles the match.
- Includes: one ordinary War Thunder Ground Arcade Domination match.
- Excludes: Battlefield Conquest's one-ticket unrevived infantry deaths;
  one-point Conquest missions; two-base Battle missions; personal score or
  research rewards.
- Parameters: teams, initial tickets, destroyed vehicle debit, three point
  owners, ownership difference, drain cadence, spawnable players, zero
  threshold and result.
- Evidence: [War Thunder decomposition](../games/s-z/war-thunder.md).
- Novelty: first isolated for `GAME-0184`; a three-point majority and bounded
  vehicle lineups jointly pressure one shared terminal resource.

## SYS-584 — Administer opening hand and London mulligan

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the system presents an opening hand of the declared size and, after each requested mulligan, returns that hand, presents a replacement and requires the player to put one additional card on the library bottom before the game begins.
- Includes: the scoped MTG Arena seven-card opening hand and repeated London mulligan settlement.
- Excludes: live-turn card draw; sideboarding; assuming an unpublished exact Arena Best-of-One hand-selection probability.
- Parameters: deck order, presented hand, mulligan count, replacement hand, bottom-card count, player order and opaque client selection layer.
- Evidence: [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md).
- Novelty: first isolated for `GAME-0185`; the client couples a full replacement draw to a progressively smaller retained hand before turn one.

## SYS-585 — Generate, spend and clear typed mana

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: mana abilities add typed or unrestricted mana to the current pool, costs consume compatible quantities, and ordinary unspent mana empties as steps and phases end.
- Includes: tapping Plains, Island, Tranquil Cove or Temple of Enlightenment for the white or blue payments used by Arcane Aerialists spells.
- Excludes: playing the land itself; a persistent energy budget that refreshes only once per turn; non-mana additional costs.
- Parameters: source, mana type, quantity, pool, generic and coloured payment, autotap choice, residual mana and clearing boundary.
- Evidence: [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md).
- Novelty: first isolated for `GAME-0185`; renewable sources generate typed step-local payment units rather than one undifferentiated turn allowance.

## SYS-586 — Advance the ordered turn phases and refresh permanents

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the system advances each turn through beginning, precombat main, combat, postcombat main and ending phases, performing untap, upkeep, draw and cleanup actions at their declared steps before passing the next turn.
- Includes: alternating turns in the scoped two-player Arcane Aerialists game.
- Excludes: priority decisions within a step; stack-object resolution; a planning phase followed by one autonomous enemy phase.
- Parameters: active player, phase, step, untap, upkeep triggers, draw, combat, cleanup, maximum hand and next active player.
- Evidence: [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md).
- Novelty: first isolated for `GAME-0185`; an alternating player turn contains several fixed subphases in which both players may still receive priority.

## SYS-587 — Resolve the top stack object after consecutive passes

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: spells and non-mana abilities remain ordered on a last-in, first-out stack while players receive priority; when all players pass in succession, only the top object resolves before priority is offered again.
- Includes: responding to an Arcane Aerialists spell or triggered ability with an eligible instant before the newest object resolves first.
- Excludes: mana abilities that resolve without the stack; combat damage as a turn-based action; immediately executing a card when cast.
- Parameters: stack order, active player, priority order, consecutive passes, top object, resolution, countering and next priority holder.
- Evidence: [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md).
- Novelty: first isolated for `GAME-0185`; response opportunities build a LIFO rule queue whose newest unresolved effect settles first.

## SYS-588 — Apply card text and route the object between zones

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when a spell or ability resolves, the system performs its card text in rules order and places the represented card in its type- and effect-defined destination while creating any resulting triggers.
- Includes: creatures, artifacts and enchantments entering the battlefield; resolved instants and sorceries entering the graveyard; Arcane Aerialists draw, removal, life-gain and token effects.
- Excludes: choosing the spell or target; LIFO stack scheduling; construction or collection changes outside the game.
- Parameters: object, controller, text clauses, targets, replacement effects, destination zone, created object and trigger event.
- Evidence: [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md).
- Novelty: first isolated for `GAME-0185`; one resolved rule object can update several public and private zones and enqueue further abilities.

## SYS-589 — Resolve declared combat through blockers and damage

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after attacker and blocker declarations and their response windows, each creature assigns damage under the current block relation and the system deals the assigned combat damage simultaneously at that step.
- Includes: unblocked Arcane Aerialists flyers damaging the opponent and blocked creatures exchanging power-based damage.
- Excludes: selecting attackers or blockers; noncombat spell damage; removing a creature only after the later state-based-action check.
- Parameters: attackers, blockers, power, damage assignment, unblocked target, first or double strike, simultaneous damage and marked damage.
- Evidence: [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md).
- Novelty: first isolated for `GAME-0185`; a defender-authored relation redirects attacker damage before simultaneous combat settlement.

## SYS-590 — Apply state-based actions and settle the game terminal

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before priority is granted, the system repeatedly checks current state, destroys creatures with lethal marked damage and immediately settles a player loss caused by zero life, an empty-library draw, concession or an applicable card-defined condition.
- Includes: destroying an Arcane Aerialists creature whose marked damage meets toughness and opening the victory or defeat result overlay when one player loses the scoped game.
- Excludes: strategic evaluation before a legal terminal exists; post-match reward or rank progression; best-of-three game sequencing.
- Parameters: state check, lethal damage, toughness, life, draw attempt, concession, card-defined win or loss, simultaneous loss and result.
- Evidence: [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md).
- Novelty: first isolated for `GAME-0185`; continuous rules validation removes illegal surviving states and shares that check boundary with the game result.

## SYS-591 — Resolve manual harvesting and renewable resource return

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a completed manual gather, pick, chop, mine or dig interaction yields the target's typed materials and updates, removes or schedules regrowth of its world source.
- Includes: collecting grass, twigs, berries, logs, rocks, flint, gold and other ordinary Forest materials in the scoped Don't Starve Together world.
- Excludes: autonomous harvesting; Crock Pot conversion; creature loot produced by combat; generation of the original world source.
- Parameters: source, action or tool, work amount, yield, source depletion, stump or replacement state, regrowth rule, season and fertilisation.
- Evidence: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Novelty: first isolated for `GAME-0186`; renewable survival inputs remain spatial world entities whose collection changes their local availability across days and seasons.

## SYS-592 — Advance sanity and hostile shadow manifestation

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: environmental, creature, food, clothing and activity effects continuously change personal sanity, while low thresholds alter perception and make shadow creatures present and eventually physically hostile.
- Includes: darkness, rain and monsters reducing sanity and below-fifteen-percent shadow creatures becoming aggressive in the scoped Forest world.
- Excludes: health or hunger loss by itself; purely cosmetic screen treatment with no hostile-state consequence; character-specific sanity abilities.
- Parameters: survivor, sanity, rate modifier, source, threshold, audiovisual distortion, shadow creature, corporeality and aggression.
- Evidence: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Novelty: first isolated for `GAME-0186`; a visible mental-state meter changes both presentation and the legal hostility of entities perceived by that survivor.

## SYS-593 — Consume fuel into local light and heat and enforce darkness threat

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an active fire or portable light consumes its compatible fuel over live time, emits a bounded light-and-heat field, and leaves survivors in complete darkness vulnerable to sanity loss and lethal darkness attacks when illumination expires.
- Includes: Campfires and Fire Pits consuming fuel, warming nearby survivors and protecting them from Charlie during night.
- Excludes: seasonal ambient temperature by itself; cooking-recipe conversion; decorative lighting without survival authority.
- Parameters: source, fuel type, fuel reserve, burn rate, light radius, heat radius, rain modifier, darkness exposure, sanity rate and attack response.
- Evidence: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Novelty: first isolated for `GAME-0186`; one depleting local field jointly grants visibility, winter warmth and immunity from an otherwise unavoidable darkness attacker.

## SYS-594 — Persist science prototyping from nearby stations

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: proximity to a compatible science station makes its recipe tier available, and the first completed prototype permanently records that recipe for the individual survivor so later copies can be crafted away from the station.
- Includes: prototyping Science Machine and Alchemy Engine recipes for each scoped Wilson survivor.
- Excludes: consuming recipe ingredients; placing the crafted fixture; account-wide unlocks; character-specific skill trees.
- Parameters: survivor, station, station tier, proximity, recipe, known state, first-prototype sanity reward and retained personal knowledge.
- Evidence: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Novelty: first isolated for `GAME-0186`; a temporary spatial station relation writes permanent recipe knowledge separately for each cooperating survivor.

## SYS-595 — Advance seasonal climate, resources and ecology

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the world calendar advances through configured seasons and changes temperature, daylight proportions, weather, resource availability and eligible creature behaviour at their boundaries.
- Includes: default Autumn days 1–20, Winter days 21–35 and the first transition into Spring in the scoped Don't Starve Together Forest.
- Excludes: day-night phase resolution alone; event calendars; a full multi-year world; Caves or Ruins seasonal differences.
- Parameters: world day, season, configured length, temperature, precipitation, day-dusk-night mix, resource rule, creature rule and next-season boundary.
- Evidence: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Novelty: first isolated for `GAME-0186`; a fixed shared calendar changes several coupled survival and ecology systems before returning to a distinct new season.

## SYS-596 — Convert death to ghost and resolve cooperative revival or world reset

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when a survivor dies, the system drops eligible inventory and keeps that player as a roaming ghost; an authorised revival returns embodiment with its declared penalty, while simultaneous team death starts the Survival reset countdown.
- Includes: Telltale Heart revival and the 120-second all-player-dead reset rule in scoped Survival mode.
- Excludes: Endless-mode Florid Postern revival; Wilderness respawn; rollback commands; resurrection items or structures outside the bounded packet.
- Parameters: survivor, lethal state, dropped inventory, ghost position, team ghosts, sanity aura, revival source, restored health, maximum-health penalty, countdown and reset.
- Evidence: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Novelty: first isolated for `GAME-0186`; individual death preserves limited cooperative presence, but collective death escalates the same state into a timed world terminal.

## SYS-597 — Age and transform perishable food

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: carried, stored or prepared food loses freshness over live time at environment- and container-dependent rates and crosses freshness states that alter its value or transform it into spoilage.
- Includes: ordinary raw, cooked and Crock Pot foods aging during the scoped first-Autumn and first-Winter interval.
- Excludes: consuming the food; Crock Pot recipe selection; non-perishable materials; an exhaustive farm or preservation module.
- Parameters: item, freshness, elapsed time, temperature, wetness, container modifier, cooked state, stale threshold and spoilage output.
- Evidence: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Novelty: first isolated for `GAME-0186`; the same survival resource remains useful only within a continuously shrinking time window that preparation and storage can change.

## SYS-598 — Secure a Payload checkpoint and transform route state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when the attacking cart crosses one authored intermediate route
  marker, the system secures that checkpoint, awards its fixed time, locks the
  cart's rollback floor and applies its authored team-spawn or route changes.
- Includes: Team Fortress 2 Upward checkpoints A, B and C, which add three,
  five and four minutes and change BLU or RED spawn access as authored.
- Excludes: final route completion; a generic lap split; score awarded without
  changing objective state; an opening area capture that activates the vehicle.
- Parameters: checkpoint, crossing, time award, rollback floor, team spawns,
  doors, route access and resulting segment.
- Evidence: [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
- Novelty: first isolated for `GAME-0187`; one route crossing atomically changes
  remaining time, reversible progress and where teams re-enter the fight.

## SYS-599 — Batch eligible dead players into team respawn waves

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system assigns eligible dead teammates to a shared periodic
  return boundary and respawns that batch together, deferring a player to a
  later wave when the current wave's timing or capacity gate is missed.
- Includes: ordinary Team Fortress 2 team respawn waves, with a default
  ten-second wave and possible next-wave wait under high server population.
- Excludes: independent fixed personal countdowns; one-life elimination;
  player-triggered resurrection; autonomous enemy wave spawning.
- Parameters: team, dead players, deathcam, wave interval, eligibility,
  capacity, current spawn and return batch.
- Evidence: [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
- Novelty: first isolated for `GAME-0187`; death timing couples several players'
  next controllable state through one shared team cadence.

## SYS-600 — Project an attacker-only supply field from the Payload cart

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the active route cart continuously restores declared combat
  resources to eligible nearby attackers while it remains an objective object,
  making escort proximity also a moving sustain position.
- Includes: the Team Fortress 2 Payload cart acting like a Level 1 Dispenser for
  nearby BLU players by restoring health, ammunition and Engineer metal.
- Excludes: map health/ammo pickups; a player-built Dispenser; spawn lockers;
  supply granted to defenders; progress caused by the supply effect itself.
- Parameters: cart, eligible team, radius, health rate, ammunition, metal,
  disguise exception and objective state.
- Evidence: [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
- Novelty: first isolated for `GAME-0187`; the same contested moving objective
  is also an asymmetric replenishment source for the team that advances it.

## SYS-601 — Apply a duty level-sync boundary at entry

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: entering a synced duty caps the controlled character at the
  declared duty level, derives effective combat state within that cap and makes
  actions above it unavailable until the instance boundary ends.
- Includes: a level-18-or-higher Gladiator entering ordinary Sastasha and being
  synced to level 18 with only the admitted level-18-or-lower kit.
- Excludes: permanent level loss; item-level progression outside the duty;
  unrestricted-party entry; changing the selected class or job.
- Parameters: actual level, duty minimum, sync cap, effective attributes,
  equipment treatment, admitted actions, suppressed actions and exit restore.
- Evidence: [FINAL FANTASY XIV Online decomposition](../games/a-f/final-fantasy-xiv-online.md).
- Novelty: first isolated for `GAME-0188`; one instance temporarily projects a
  persistent character into a lower rules envelope without changing retained
  progression.

## SYS-602 — Run a preset role-complete NPC light party

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after Duty Support fills the missing light-party roles with
  preset NPCs, those allies autonomously follow, acquire targets and execute
  their healer or damage behaviour around the directly controlled player.
- Includes: Eager Conjurer, Eager Thaumaturge and Eager Lancer accompanying a
  controlled Gladiator tank through Sastasha.
- Excludes: directly commanding each NPC action; a single cosmetic follower;
  human matchmaking; changing the preset A Realm Reborn roster.
- Parameters: player role, NPC roster, role, follow state, combat target,
  healing priority, damage behaviour, pathing and encounter state.
- Evidence: [FINAL FANTASY XIV Online decomposition](../games/a-f/final-fantasy-xiv-online.md).
- Novelty: first isolated for `GAME-0188`; autonomous agents complete every
  missing tactical role around one directly controlled party member inside a
  bounded authored duty.

## SYS-603 — Accumulate enmity and redirect hostile targets

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: eligible attacks, healing and high-enmity effects add actor-
  specific threat toward each hostile, which selects or changes its preferred
  target according to the resulting enmity relation.
- Includes: Iron Will, Shield Lob, Total Eclipse and Provoke helping a Sastasha
  Gladiator remain above healer and DPS allies on enemy enmity lists.
- Excludes: human opponent choice; a scripted boss target that ignores enmity;
  damage resolution after a target has already been selected.
- Parameters: hostile, party member, action, stance, enmity amount, rank,
  forced placement, target selection and target-change cue.
- Evidence: [FINAL FANTASY XIV Online decomposition](../games/a-f/final-fantasy-xiv-online.md).
- Novelty: first isolated for `GAME-0188`; party offence and healing are coupled
  through a continuously ranked targeting authority that the tank deliberately
  manipulates.

## SYS-604 — Schedule shared global and independent action recasts

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a committed weaponskill or spell starts its shared global recast
  group, while eligible abilities use independent recast timers and can be
  sequenced between global-ready action commitments.
- Includes: level-synced Gladiator weaponskills such as Fast Blade, Riot Blade
  and Total Eclipse sharing the weaponskill cadence while Fight or Flight,
  Rampart, Low Blow, Provoke and Interject retain their own readiness.
- Excludes: turn-based action points; automatic weapon firing; one universal
  cooldown that blocks every input; animation detail not exposed as legality.
- Parameters: action category, global group, base recast, independent recast,
  charge, readiness, sequence, target and interruption.
- Evidence: [FINAL FANTASY XIV Online decomposition](../games/a-f/final-fantasy-xiv-online.md).
- Novelty: first isolated for `GAME-0188`; two concurrent readiness layers let
  the player interleave role utility with a shared offensive cadence.

## SYS-605 — Advance an authored dungeon through switches, keys and boss gates

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: required observations, object interactions, carried keys and
  encounter clears update ordered route flags that reveal, unlock or admit the
  next authored dungeon segment.
- Includes: Sastasha's Bloody Memo and coral, Inconspicuous Switch, Chopper
  passage, Captain's Quarters Key, Waverider Gate Key, Captain Madison gates
  and final access to Denn.
- Excludes: optional side-room exploration; a persistent open-world quest tree;
  free-form lockpicking; defeating an unrelated enemy with no route effect.
- Parameters: segment, observed clue, switch, key, door, boss, completion flag,
  prerequisite relation and next admitted segment.
- Evidence: [FINAL FANTASY XIV Online decomposition](../games/a-f/final-fantasy-xiv-online.md).
- Additional support: [Destiny 2 decomposition](../games/a-f/destiny-2.md),
  for terminal-, defence-, miniboss- and boss-gated authored activity progress.
- Novelty: first isolated for `GAME-0188`; readable clue state, typed carried
  access and mandatory combat checkpoints all update one finite instance route.

## SYS-606 — Convert boss wipes into consumable Willful protection

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after the controlled player is incapacitated by a Duty Support
  boss and rechallenges the reset encounter, prior failures grant capped
  Willful stacks; each stack prevents one later lethal event, restores full
  health through Will to Live and is cleared with the remaining stack set when
  that boss is defeated.
- Includes: current Patch 7.55 Sastasha Duty Support boss rechallenges under
  the Patch 7.4 Willful rule, up to five stacks.
- Excludes: ordinary healer resurrection; an unconditional extra life at first
  entry; retaining stacks after boss victory; open-world Echo effects.
- Parameters: boss, player KO count, rechallenge, stack cap, lethal event,
  consumed stack, one-HP survival, immobilisation, full heal and victory reset.
- Evidence: [FINAL FANTASY XIV Online decomposition](../games/a-f/final-fantasy-xiv-online.md).
- Novelty: first isolated for `GAME-0188`; repeated local failure writes a
  capped consumable safety budget into the next attempt and erases it at the
  same boss's success boundary.

## SYS-607 — Convert combat timing and staff pressure into Focus attacks

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible staff hits, held charging and correctly timed Perfect
  Dodges add progress toward bounded Focus points, while compatible heavy or
  varied attacks consume that retained Focus for their authored stronger form.
- Includes: Black Myth: Wukong Chapter 1 Smash-stance Focus generation and
  Focus-enhanced staff commitments.
- Excludes: experience toward a character level; Mana spent on a spell; a
  passive critical-hit chance; damage that never changes a spendable meter.
- Parameters: source, Focus gain, point threshold, capacity, charge, attack
  form, consumed points, damage, stagger and interruption.
- Evidence: [Black Myth: Wukong decomposition](../games/a-f/black-myth-wukong.md).
- Novelty: first isolated for `GAME-0189`; precisely timed defence and ordinary
  weapon pressure feed the same discrete player-spent offensive authority.

## SYS-608 — Replace the base combat body with one temporary transformation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: activating an acquired transformation transfers direct control
  from the persistent avatar to a temporary combat body with its own health,
  readiness and moveset, then restores the surviving base body when the form
  expires or is dismissed.
- Includes: Black Myth: Wukong Red Tides after defeating Guangzhi.
- Excludes: cosmetic appearance; a numeric buff that retains the same body and
  moveset; switching to another persistent protagonist; an autonomous summon.
- Parameters: acquired form, base body, temporary health, Might or duration,
  moveset, readiness, damage, expiry, dismissal and return state.
- Evidence: [Black Myth: Wukong decomposition](../games/a-f/black-myth-wukong.md).
- Novelty: first isolated for `GAME-0189`; a retained ability supplies a
  replaceable second combat body without creating a party member or death.

## SYS-609 — Convert experience into freely reallocatable Spark modifiers

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: crossing an experience threshold increments character level and
  awards a Spark; legal allocation applies the selected tree-node modifier,
  while checkpoint reclamation removes selected modifiers and returns their
  Sparks without a spendable-currency fee.
- Includes: Black Myth: Wukong Foundation, Stamina, Martial Arts, Survival and
  Smash-stance Spark allocation and Reignite the Sparks at Keeper's Shrines.
- Excludes: purchased item upgrades; fixed automatic level bonuses alone;
  account-wide progression; a paid full character rebuild.
- Parameters: experience, threshold, level, Spark stock, node, rank,
  prerequisite, modifier, reclaimed set, fee and resulting build.
- Evidence: [Black Myth: Wukong decomposition](../games/a-f/black-myth-wukong.md).
- Novelty: first isolated for `GAME-0189`; earned persistent build authority is
  both granularly applied and freely recoverable at the same checkpoint layer.

## SYS-610 — Return death to a Shrine without dropping retained resources

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: ordinary lethal damage returns the controlled avatar to the
  latest eligible checkpoint while retaining spendable currency, experience,
  development points, inventory and completed authored progress and creating
  no recoverable death-world mark.
- Includes: Black Myth: Wukong return to the latest eligible Keeper's Shrine
  with Will, experience, Sparks, items, spells and boss flags retained.
- Excludes: one recoverable rune/Cocoon mark; quest faint allowance; loading a
  manually selected older save; permanent one-life deletion.
- Parameters: lethal state, checkpoint, retained sets, ordinary-enemy reset,
  boss state, mark absence and resumed control.
- Evidence: [Black Myth: Wukong decomposition](../games/a-f/black-myth-wukong.md).
- Novelty: first isolated for `GAME-0189`; checkpoint return preserves both
  spendable progression and authored victories without a corpse-recovery debt.

## SYS-611 — Settle retained chapter boss gates into the next region

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: defeating each admitted mandatory or deliberately selected boss
  persists its reward and route flag; satisfying the final chapter guardian
  then resolves the chapter-ending sequence and admits retained control in the
  next authored region.
- Includes: the bounded Black Myth: Wukong Chapter 1 sequence through Bullguard,
  Guangzhi, Lingxuzi, Guangmou, Whiteclad Noble, Black Wind King and Black Bear
  Guai into first Chapter 2 control.
- Excludes: every optional Chapter 1 boss; a single isolated arena replay;
  defeating the guardian without settling the chapter transition.
- Parameters: boss, optional-admitted flag, reward, route prerequisite,
  completion flag, chapter guardian, settlement sequence and next-region state.
- Evidence: [Black Myth: Wukong decomposition](../games/a-f/black-myth-wukong.md).
- Novelty: first isolated for `GAME-0189`; retained boss states and one selected
  ability branch compose into a chapter boundary rather than a quest result.

## SYS-612 — Apply chosen ancestry to the starting character state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: confirming one available ancestry writes its authored starting
  skill bonuses, passive trait and active power into the persistent character
  while the remaining appearance values alter presentation only.
- Includes: the selected Nord's starting bonuses, frost resistance and Battle
  Cry entering the scoped Skyrim Special Edition save, even though Battle Cry
  is not required by the Helgen escape trace.
- Excludes: a later level-up allocation; equipment statistics; a class or
  occupation budget; treating purely cosmetic sliders as separate mechanics.
- Parameters: ancestry, skill bonuses, passive, active power, appearance,
  persistent save and later eligibility.
- Evidence: [The Elder Scrolls V: Skyrim Special Edition decomposition](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md).
- Novelty: first isolated for `GAME-0190`; ancestry changes the persistent
  starting state without also committing a class, background or point budget.

## SYS-613 — Resolve angular lock probing into breakage or access

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the addressed lock compares pick angle with its concealed valid
  interval; applied torque converts proximity into cylinder travel and feedback,
  while excess torque outside tolerance breaks the pick and sufficient legal
  travel permanently opens the lock.
- Includes: one novice prison-cell lock in the scoped Skyrim Special Edition
  Helgen route.
- Excludes: an exact key check; a dice-only lock skill roll; reusable code entry;
  breaking a door with combat damage.
- Parameters: hidden interval, angle error, tolerance, torque, cylinder travel,
  feedback, pick loss, unlock threshold and retained door state.
- Evidence: [The Elder Scrolls V: Skyrim Special Edition decomposition](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md).
- Novelty: first isolated for `GAME-0190`; analog error simultaneously controls
  information gain, disposable-tool risk and persistent spatial access.

## SYS-614 — Spend campaign movement through an army route

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a selected campaign army follows its committed world-map route,
  consuming movement allowance according to terrain and stopping at the legal
  destination, settlement or encounter that the remaining allowance reaches.
- Includes: Prince Yuri's Kislev Expedition moving from Kislev Refuge toward
  the Beacon in the scoped Total War: WARHAMMER III prologue.
- Excludes: formation movement during battle; direct avatar locomotion; an
  instantaneous board move with no route cost; automatic scout travel.
- Parameters: army, origin, route, terrain, stance, movement allowance,
  destination, obstruction, encounter and retained position.
- Evidence: [Total War: WARHAMMER III decomposition](../games/s-z/total-war-warhammer-iii.md).
- Novelty: first isolated for `GAME-0191`; one persistent army token spends a
  replenishing turn allowance on a continuous strategic-map route.

## SYS-615 — Advance prepaid settlement construction at turn settlement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each eligible campaign-turn settlement reduces the remaining
  duration of a commissioned settlement building and, at zero, installs its
  chain tier and persistent local effects without further placement input.
- Includes: the Kislev Refuge upgrade and Store House construction required by
  the scoped Total War: WARHAMMER III prologue instructions.
- Excludes: worker-driven live construction; yield accumulation toward one city
  target; national factory allocation; an immediate shop purchase.
- Parameters: settlement, slot, building, remaining turns, interruption,
  completion, effect and retained campaign state.
- Evidence: [Total War: WARHAMMER III decomposition](../games/s-z/total-war-warhammer-iii.md).
- Novelty: first isolated for `GAME-0191`; treasury commitment precedes a fixed
  turn countdown in a bounded building-chain slot.

## SYS-616 — Transfer an army encounter through battle and back to campaign

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: campaign contact instantiates a separate battle from the involved
  armies and terrain; resolving that battle then returns surviving unit counts,
  casualties, experience, rewards and encounter outcome to the persistent
  campaign state.
- Includes: entering, manually resolving and returning from the first Beacon
  battle in the scoped Total War: WARHAMMER III prologue.
- Excludes: autoresolve without the live battle; a disconnected custom battle;
  combat that never returns state to a strategic layer.
- Parameters: campaign armies, terrain, deployment, battle instance, casualty,
  survivor, experience, reward, result and restored campaign control.
- Evidence: [Total War: WARHAMMER III decomposition](../games/s-z/total-war-warhammer-iii.md).
- Novelty: first isolated for `GAME-0191`; one persistent strategic encounter
  expands into a distinct command timescale and contracts back with losses.

## SYS-617 — Convert unit leadership into routing and rally state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: live casualties, threats, flanking, nearby leadership and other
  declared modifiers update a unit's morale; crossing its break condition
  removes ordinary command compliance and sends it routing until defeat,
  withdrawal or an eligible rally restores control.
- Includes: unit morale, routing and possible rally during the scoped Total War:
  WARHAMMER III Beacon battle.
- Excludes: permanent unit death alone; a global team surrender meter; fear as
  presentation with no control consequence.
- Parameters: unit, leadership, casualty, flank, threat, commander, modifier,
  break threshold, route direction, rally condition and destroyed state.
- Evidence: [Total War: WARHAMMER III decomposition](../games/s-z/total-war-warhammer-iii.md).
- Novelty: first isolated for `GAME-0191`; a formation may become temporarily
  uncontrollable and flee while individual models remain alive.

## SYS-618 — Run stock autonomous teammates around one controlled cooperator

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: vacant members of a fixed cooperative party are filled by stock
  agents that autonomously follow the controlled member, acquire and attack
  local hostiles, collect compatible supplies and perform eligible healing,
  release or revival support without receiving individual action commands.
- Includes: Rochelle, Ellis and Nick bots accompanying a controlled Coach
  through Left 4 Dead 2's scoped Single Player Hotel chapter; three stock AI
  heisters supporting Dallas in the scoped PAYDAY 2 Offline Bank Heist.
- Excludes: directly commanded party members; human matchmaking; one role-
  complete Tank/Healer/DPS Duty Support roster; an ambient escort NPC whose
  survival is not part of the shared checkpoint state.
- Parameters: party slots, controlled member, bot identities, follow distance,
  target acquisition, carried item, support priority, release, revival, pathing
  and living state.
- Evidence: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md).
- Additional support: [PAYDAY 2 decomposition](../games/m-r/payday-2.md), for
  the fixed Offline heister slots, follow/combat support and legal bot revival
  or hostage-trade behaviour around Dallas.
- Novelty: first isolated for `GAME-0192`; same-authority cooperative slots are
  substituted by autonomous partners whose combat and rescue keep the shared
  route viable around one directly controlled cooperator.

## SYS-619 — Modulate encounter population from Survivor intensity

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the encounter controller estimates current team intensity from
  combat, damage, incapacitation and nearby threats, then alternates build-up,
  peak and relaxation by selecting constrained populations and supplies in
  unseen reachable space rather than replaying one fixed encounter script.
- Includes: Left 4 Dead 2's AI Director varying wanderers, mobs, Special or Boss
  Infected, weapons and scavenge items around the Hotel party while retaining
  the authored chapter route and terminal.
- Excludes: one clock-indexed fixed wave schedule; a player-triggered one-shot
  panic event; uniformly random spawning without team-state modulation;
  changing the chapter's positive terminal.
- Parameters: Survivor intensity, team maximum, build-up threshold, peak,
  relaxation, active area, population class, supply class, visibility,
  reachability and sample.
- Evidence: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md).
- Novelty: first isolated for `GAME-0192`; observed team pressure regulates both
  when encounter density rises and which bounded hostile/supply population is
  instantiated around an authored route.

## SYS-620 — Resolve a hostile isolating hold until teammate release

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an eligible hostile attack transfers one Survivor into a pinned,
  dragged, carried or otherwise disabled state, continues its typed harm or
  displacement and returns ordinary control only when a teammate breaks the
  hold or the victim reaches defeat.
- Includes: Special Infected disabling attacks against the Left 4 Dead 2 Hotel
  party and another Survivor shooting or shoving the attacker free.
- Excludes: ordinary damage that leaves full self-control; voluntary teammate
  carrying; a turn-based stun with automatic expiry and no ally counteraction;
  health-zero incapacitation without a continuing captor.
- Parameters: attacker type, victim, acquisition, hold state, movement,
  continuing damage, release action, rescuer, attacker defeat, victim defeat
  and restored authority.
- Evidence: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md).
- Novelty: first isolated for `GAME-0192`; one hostile temporarily monopolises
  a living player's authority and makes another party body the decisive
  counteractor.

## SYS-621 — Launch an authored panic population from a route trigger

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: completing a declared world interaction fires a one-shot authored
  event request that dispatches a mass hostile population through eligible
  navigation space while the route transition continues.
- Includes: the scoped Left 4 Dead 2 Hotel elevator control initiating its
  bounded mass attack before the party traverses the burning lobby.
- Excludes: an ambient Director peak chosen only from current intensity; a
  clock-indexed survival wave; infinitely repeatable farming from the same
  trigger; presentation-only alarms.
- Parameters: trigger object, prerequisite, one-shot flag, event request,
  population class, navigation space, start cue, route transition and settled
  flag.
- Evidence: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md).
- Novelty: first isolated for `GAME-0192`; authored route commitment requests a
  discrete mass encounter without replacing the surrounding adaptive Director.

## SYS-622 — Settle a Survivor chapter through safe-room closure

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when every currently living Survivor occupies the exit checkpoint
  and its door reaches closed state, the system marks the current map complete,
  retains eligible Survivor and carried-item state and loads the next authored
  chapter boundary.
- Includes: closing The Hotel's ground-floor safe room and settling into The
  Streets in the scoped Left 4 Dead 2 Campaign.
- Excludes: one player crossing an extraction radius; a finale rescue vehicle;
  closing the opening checkpoint door; entering a shelter with living party
  members still outside.
- Parameters: chapter, living roster, checkpoint region, occupancy, door,
  closure, completion flag, retained health, retained items and next map.
- Evidence: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md).
- Novelty: first isolated for `GAME-0192`; collective living-body occupancy and
  a physical door state jointly commit a persistent authored map transition.

## SYS-623 — Settle an Ops boss into score, grade and reward chest

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after the final mandatory activity objective and boss defeat,
  the system closes live objective scoring, calculates the eligible activity
  score and grade, maps that grade to its reward tier and admits the bounded
  end chest or reward package.
- Includes: Sepiks Prime defeat completing the scoped Normal Devil's Lair
  Fireteam Op, with Normal's `B` grade, Tier-1 reward boundary and end chest.
- Excludes: extracting through a separate departure region; opening an
  intermediate world chest; account-wide Power or vendor progression; farming
  another run.
- Parameters: activity, final boss, objective state, score, time contribution,
  difficulty, grade, reward tier, completion flag and chest admission.
- Evidence: [Destiny 2 decomposition](../games/a-f/destiny-2.md).
- Novelty: first isolated for `GAME-0193`; a final encounter simultaneously
  closes authored objectives and converts one live score into a declared grade,
  tier and separately admitted chest without an extraction phase.

## SYS-624 — Restore an authored activity checkpoint after a solo wipe

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: when no eligible Guardian remains active inside a Restricted
  Zone, the unfinished activity attempt restores its most recent authored
  checkpoint, resetting transient encounter state without issuing the positive
  activity-complete result.
- Includes: one-player Normal Devil's Lair defeat in its Restricted Zone.
- Excludes: free self-respawn while the encounter continues; teammate revival;
  consuming limited revive tokens; returning to orbit or erasing the character.
- Parameters: active roster, lethal state, zone, checkpoint, transient enemies,
  objective state, retained route flag and resumed control.
- Evidence: [Destiny 2 decomposition](../games/a-f/destiny-2.md).
- Novelty: first isolated for `GAME-0193`; collective-failure checkpoint logic
  is applied to a one-participant live-service activity without pair recovery,
  world reset or persistent-resource loss.

## SYS-625 — Resolve attack and block directions into deflection or damage

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when an eligible melee strike contacts a guarding combatant, the
  system compares attack direction, current weapon or shield guard direction,
  timing and reach; compatible opposition deflects the strike, while a mismatch
  permits ordinary damage resolution.
- Includes: skill-based directional melee and blocking in scoped Mount & Blade
  II: Bannerlord tutorial battles.
- Excludes: passive armour mitigation; a turn-based accuracy roll; high/low
  guard with no aimed weapon direction; a universal invulnerable parry window.
- Parameters: attacker, defender, weapon, attack direction, guard direction,
  timing, reach, contact, deflection and health damage.
- Evidence: [Mount & Blade II: Bannerlord decomposition](../games/m-r/mount-and-blade-ii-bannerlord.md).
- Novelty: first isolated for `GAME-0194`; opposed weapon directions mediate
  contact before ordinary live-combat damage rather than merely modifying odds.

## SYS-626 — Consume party provisions and recover health through campaign time

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while campaign time advances, the travelling party consumes its
  carried food under the current roster state and eligible wounded characters
  recover health over time, so waiting for recovery spends part of the same
  persistent provision horizon.
- Includes: grain consumption and pre-hideout health recovery in scoped Mount &
  Blade II: Bannerlord Campaign tutorial.
- Excludes: one avatar hunger meter; an instant healing potion; a turn-based
  camp rest that spends a selected supply bundle; battle-local regeneration.
- Parameters: campaign time, party size, food stock, consumption rate, wound,
  health, recovery rate, starvation state and retained party.
- Evidence: [Mount & Blade II: Bannerlord decomposition](../games/m-r/mount-and-blade-ii-bannerlord.md).
- Novelty: first isolated for `GAME-0194`; continuous campaign waiting couples
  roster-wide provisions to recovery of persistent battle injuries.

## SYS-627 — Couple node-beam structure and pressure tyres to vehicle response

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the system resolves a vehicle's chassis, suspension, wheels and
  tyres as coupled mass nodes, spring-like beams and pressure-tyre structures,
  converting load and contact into elastic motion, traction, permanent
  deformation, beam breakage and changed driving authority.
- Includes: the supplied Ardente 310M's route-driving, collision and damage
  response in scoped BeamNG.drive Road Master.
- Excludes: one aggregate vehicle health value; cosmetic mesh deformation that
  cannot change motion; rigid-body car handling without distributed structure;
  projectile-specific armour penetration.
- Parameters: node mass, beam spring, damping, deform force, break strength,
  tyre pressure, load sensitivity, static/sliding friction, tread, surface,
  contact force, resulting geometry and available control.
- Evidence: [BeamNG.drive decomposition](../games/a-f/beamng-drive.md).
- Novelty: first isolated for `GAME-0195`; `SYS-320` retains the generic
  vehicle-motion/damage envelope, while this boundary requires distributed
  soft-body and pressure-tyre state to alter the next driving decision.

## SYS-628 — Retain one valid Time Trial elapsed result

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after a valid ordered Time Trial finish, the system stops the
  attempt clock and records its elapsed result in that mission's retained
  high-score state; an unfinished or restarted attempt creates no completion.
- Includes: the first valid scoped BeamNG.drive Road Master finish and saved
  mission time.
- Excludes: live checkpoint timing before the finish; Festival points, credits
  or unlock rewards; external online leaderboard submission; an arbitrary
  free-driving stop.
- Parameters: mission, ordered-finish validity, elapsed time, prior entries,
  insertion rule, retained record and retry state.
- Evidence: [BeamNG.drive decomposition](../games/a-f/beamng-drive.md).
- Novelty: first isolated for `GAME-0195`; prior driving settlement combines
  finish data with campaign rewards, while this standalone mission retains the
  timed evaluation itself.

## SYS-629 — Instantiate a borrowed-machinery field contract

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: accepting an eligible field-work offer creates one active
  contract that retains its assigned field, task, reward, borrowing deduction
  and progress while placing the compatible employer-supplied machines at the
  declared collection location.
- Includes: the scoped Farming Simulator 25 Fertilizing contract and its
  borrowed tractor/spreader spawn at the local shop.
- Excludes: one preloaded delivery vehicle that starts with cargo; general
  equipment leasing; owned-machine persistence after the contract; spawning an
  unrestricted free-roam vehicle.
- Parameters: offer, field, task, owner, reward, deduction, vehicle set,
  collection location, active slot, progress and cancellation.
- Evidence: [Farming Simulator 25 decomposition](../games/a-f/farming-simulator-25.md).
- Novelty: first isolated for `GAME-0196`; the contract supplies a multi-part
  productive fleet whose coupling and field operation remain player work.

## SYS-630 — Convert implement coverage into persistent field treatment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while a compatible filled vehicle implement is active, the
  system intersects its moving working-width footprint with eligible field
  state, consumes the declared material and persists newly accepted treatment
  into both the field layer and current task progress.
- Includes: solid-fertilizer application and Fertilized-state progress during
  the scoped Farming Simulator 25 contract.
- Excludes: harvesting a discrete world crop by hand; autonomous factory
  conversion; cosmetic tyre tracks; movement of an inactive or empty tool;
  treatment outside the assigned field counting toward contract completion.
- Parameters: implement, footprint, application rate, fill type, fill amount,
  field, crop/growth state, eligible cells, prior treatment, overlap, resulting
  treatment and progress.
- Evidence: [Farming Simulator 25 decomposition](../games/a-f/farming-simulator-25.md).
- Novelty: first isolated for `GAME-0196`; a continuously swept powered
  footprint consumes material and writes a persistent productive surface layer.

## SYS-631 — Settle a completed borrowed-equipment field contract

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: after the assigned field reaches the accepted task threshold,
  the system exposes a collectable completed contract and, on collection,
  closes its active state, releases or removes its borrowed equipment and
  credits the displayed reward net of the declared borrowing deduction.
- Includes: collecting the scoped Farming Simulator 25 Fertilizing contract.
- Excludes: passive farm income; selling a harvest; paying for an owned-machine
  lease; automatically settling partial coverage; spending the resulting money.
- Parameters: contract, coverage threshold, completed flag, collection action,
  gross reward, borrowing deduction, net credit, account and asset disposition.
- Evidence: [Farming Simulator 25 decomposition](../games/a-f/farming-simulator-25.md).
- Novelty: first isolated for `GAME-0196`; surface-treatment progress closes a
  temporary supplied-fleet job into one net payment rather than a cargo depot,
  quest reward bundle or retained high-score result.

## SYS-632 — Convert an active food set into decaying survival bounds

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: aggregate each distinct active food's remaining contribution into
  the avatar's current maximum health, stamina and regeneration parameters,
  then decay those contributions through their timed digestion states.
- Includes: the scoped Valheim three-food set during Meadows preparation and Eikthyr.
- Excludes: a hunger meter whose depletion causes starvation; permanent stat
  upgrades; one immediate healing potion; equipment-only maximum health.
- Parameters: active foods, remaining duration, decay curve, health, stamina,
  regeneration, flashing/replacement state and base values.
- Evidence: [Valheim decomposition](../games/s-z/valheim.md).
- Novelty: first isolated for `GAME-0197`; temporary food composition defines
  the capacity envelope rather than merely replenishing a survival meter.

## SYS-633 — Convert shelter, fire and comfort into rest and station state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: evaluate local roof/cover, heat and comfort around the avatar and
  nearby stations; qualifying shelter permits Resting, converts sustained rest
  into a comfort-scaled Rested effect and enables station operations that need cover.
- Includes: the scoped Valheim covered Workbench, campfire, Resting and Rested state.
- Excludes: sleeping to skip night; passive base ownership; a generic safe
  zone; structural stability without shelter or station consequences.
- Parameters: roof, cover percentage, shelter, fire/heat, comfort, rest interval,
  Rested duration, recovery modifiers, station and operation availability.
- Evidence: [Valheim decomposition](../games/s-z/valheim.md).
- Novelty: first isolated for `GAME-0197`; one spatial microclimate jointly
  changes personal recovery and local production-fixture legality.

## SYS-634 — Reveal the nearest matching Forsaken altar from a wayfinder

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when an eligible Vegvisir is read, choose the nearest matching
  generated Forsaken altar in the current world and persist its marker on the
  interacting player's explored map.
- Includes: the scoped Valheim Eikthyr Vegvisir at the Sacrificial Stones.
- Excludes: random compass drift; a thrown locator; revealing every boss altar;
  changing the seed-generated altar position.
- Parameters: wayfinder, Forsaken class, generated candidates, distance rule,
  chosen altar, player identity and map marker.
- Evidence: [Valheim decomposition](../games/s-z/valheim.md).
- Novelty: first isolated for `GAME-0197`; it deterministically binds authored
  semantic guidance to the nearest instance in procedural geography.

## SYS-635 — Convert a boss offering into encounter and guaranteed defeat drops

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: consume the exact matching offering at its eligible altar,
  instantiate the registered boss and, if direct combat defeats it, emit the
  boss's guaranteed progression drops before ordinary world continuation.
- Includes: two Deer Trophies summoning Eikthyr and its guaranteed Eikthyr
  Trophy plus three Hard Antlers.
- Excludes: a naturally spawning ordinary enemy; random loot without an exact
  offering; mounting the resulting trophy; later Forsaken outside the scope.
- Parameters: altar, offering type/count, boss, combat state, defeat predicate,
  guaranteed drops, optional drops and pickup capacity.
- Evidence: [Valheim decomposition](../games/s-z/valheim.md).
- Novelty: first isolated for `GAME-0197`; one exact sacrificial input opens a
  live encounter whose guaranteed output is a separate progression key.

## SYS-636 — Mount a matching Forsaken trophy and unlock its power

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: applying a carried Forsaken trophy to its matching sacrificial
  stone persists the mounted state and makes that Forsaken Power available for
  the character's selection and later activation.
- Includes: mounting the scoped Eikthyr Trophy to unlock Eikthyr's power.
- Excludes: collecting the trophy; summoning or defeating the boss; activating
  a power already unlocked; cosmetic display at an ordinary item stand.
- Parameters: trophy, stone, Forsaken identity, mounted state, character,
  selectable power and activation rules.
- Evidence: [Valheim decomposition](../games/s-z/valheim.md).
- Novelty: first isolated for `GAME-0197`; a post-boss carried key must settle
  at a matching central fixture before its persistent capability exists.

## SYS-637 — Convert accumulated damage and attack force into launch state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible attack contact increases the target's accumulated damage
  and combines the attack's force, current defence and damage state into
  hitstun, launch speed and trajectory rather than subtracting from a terminal
  health pool.
- Includes: unarmed, Sword and Hammer contact in the scoped Brawlhalla Stock
  match, including greater knockout potential at higher damage colours.
- Excludes: vitality reaching zero; fixed knockback independent of damage;
  vehicle collision; a turn-based displacement effect.
- Parameters: attack, damage, fixed/variable force, defence, contact point,
  facing, stun, launch vector, gravity and surface collision.
- Evidence: [Brawlhalla decomposition](../games/a-f/brawlhalla.md).
- Novelty: first isolated for `GAME-0198`; the retained damage value changes
  the spatial consequence of later hits and therefore the probability of a
  boundary elimination without itself being the defeat threshold.

## SYS-638 — Convert blast-zone knockout into stock reset or match result

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when a fighter crosses an arena blast zone, the system records a
  knockout and removes one personal stock; if stock remains it returns the
  same fighter with reset damage and weapon state, otherwise it settles the
  opposing participant as winner and opens the match result.
- Includes: each of three possible Bödvar stock losses and the final result in
  the scoped Brawlhalla duel.
- Excludes: health-zero round resets; timed team respawn waves; persistent-world
  death with inventory loss; manual pause-menu restart.
- Parameters: fighter, blast zone, knockout attribution, remaining stocks,
  damage reset, weapon reset, respawn position/protection and final result.
- Evidence: [Brawlhalla decomposition](../games/a-f/brawlhalla.md).
- Novelty: first isolated for `GAME-0198`; recoverable same-match eliminations
  become the match terminal only when a participant's personal stock reaches
  zero.

## SYS-639 — Spawn and assign a compatible arena weapon

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live arena schedules a neutral pickup at an eligible spawn
  region and, when a fighter claims it, transforms the generic object into the
  next compatible weapon from that fighter's declared pair, changing available
  attacks until throw, disarm, replacement or knockout.
- Includes: normal-spawn Sword/Hammer assignment for Bödvar in the scoped
  Brawlhalla 1v1 Stock match.
- Excludes: gadget spawns; persistent random loot; selecting a pre-equipped
  quick slot; a cosmetic weapon skin with no command change.
- Parameters: arena, spawn region, delay, pickup count, fighter, weapon pair,
  alternation, active weapon, expiry, disarm and replacement.
- Evidence: [Brawlhalla decomposition](../games/a-f/brawlhalla.md).
- Novelty: first isolated for `GAME-0198`; a shared spatial pickup becomes one
  of the claimant's character-specific command kits rather than preserving a
  globally fixed item identity.

## SYS-640 — Consume and restore aerial recovery opportunities

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: aerial jumps, Recovery and later Exhausted Recovery consume the
  fighter's current off-ground opportunities, while declared ground, wall or
  hit transitions restore only their corresponding eligibility for continued
  movement.
- Includes: Brawlhalla's two aerial jumps, Recovery/Exhausted Recovery and
  reset behaviour during the scoped Stock match.
- Excludes: unlimited flight; passive stamina regeneration; vehicle flip reset;
  checkpoint respawn; the separate dodge cooldown itself.
- Parameters: ground/air/wall state, aerial-jump count, Recovery use, Exhausted
  Recovery, hit-granted opportunity, wall slip and reset transition.
- Evidence: [Brawlhalla decomposition](../games/a-f/brawlhalla.md).
- Novelty: first isolated for `GAME-0198`; several substitutable movement and
  attack forms share one contact-resettable survival budget during a live
  off-stage trajectory.

## SYS-641 — Accumulate and resolve technique-earned driving burst

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: eligible live driving events add to a temporary acceleration
  reserve, and player activation consumes that reserve into a bounded burst of
  increased vehicle acceleration.
- Includes: Need for Speed Unbound grip/drift driving and drafting that fill
  Burst Nitrous, followed by tactical Burst activation.
- Excludes: ordinary refillable nitrous not tied to driving technique; spatial
  arena boost pads; permanent engine upgrades; cinematic acceleration.
- Parameters: eligible event, gain, reserve cap, current reserve, activation,
  consumption, acceleration, duration and reset.
- Evidence: [Need for Speed Unbound decomposition](../games/m-r/need-for-speed-unbound.md).
- Novelty: first isolated for `GAME-0199`; manoeuvre quality becomes a
  spendable near-term acceleration resource inside the same race or pursuit.

## SYS-642 — Keep race earnings exposed until pursuit settlement

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a classified street-race payout enters an exposed cash state
  that persists through required police pressure; eligible garage entry banks
  it, while a completed bust removes it before durable settlement.
- Includes: `Shopping Spree` earnings carried through its mandatory LPD pursuit
  to Rydell's Rydes in the scoped Need for Speed Unbound trace.
- Excludes: credits retained immediately at a race result; paid event entry;
  side bets; inventory loot extraction; account purchases after banking.
- Parameters: event, classified place, payout, exposed cash, Heat, pursuit,
  escape, garage eligibility, banked amount and bust loss.
- Evidence: [Need for Speed Unbound decomposition](../games/m-r/need-for-speed-unbound.md).
- Novelty: first isolated for `GAME-0199`; the race result creates value but a
  distinct live pursuit must be survived before that value becomes durable.

## SYS-643 — Advance an attack-and-defend front by completed sectors

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when the attacking team owns every required objective in the
  currently active sector, the system locks that sector as completed, moves the
  legal combat front to the next authored sector and exposes its objective set.
- Includes: the ordered sector progression of the scoped Delta Force Coliseum
  Attack and Defend match.
- Excludes: simultaneous control of every point on an open Conquest map; a
  single Control point that resets between rounds; payload checkpoints.
- Parameters: map, active sector, objective set, capture state, completed
  sector, retreat boundary, next sector and final sector.
- Evidence: [Delta Force decomposition](../games/a-f/delta-force.md).
- Novelty: first isolated for `GAME-0200`; objective ownership changes the
  playable front itself instead of only contributing continuous score or
  ticket pressure.

## SYS-644 — Resolve asymmetric attacker tickets and sector replenishment

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: committed attacker deaths debit one finite shared troop-force
  pool while defenders may redeploy without debiting an equivalent pool;
  completed sectors replenish the attacking pool, attacker exhaustion settles
  defender victory and completion of the final sector settles attacker victory.
- Includes: the scoped Delta Force Coliseum Attack and Defend ticket loop and
  its defender Victory result after attacker troop-force exhaustion.
- Excludes: symmetric Conquest reinforcement pools; personal Stock lives; a
  shared cooperative reinforcement reserve; score-only eliminations.
- Parameters: side, attacker troop force, defender redeploy authority, downed
  state, revive, committed death, sector replenishment, zero-ticket terminal,
  final-sector terminal and result.
- Evidence: [Delta Force decomposition](../games/a-f/delta-force.md).
- Novelty: first isolated for `GAME-0200`; the same front progression that
  rewards the attacking team also refreshes the only finite team-life pool.

## SYS-645 — Commit heist detection into an irreversible loud response

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: completed guard, camera or civilian detection, a panic trigger or
  an overt criminal action commits the current heist from casing or stealth to
  a shared alarm state, starts law-enforcement response and prevents return to
  the unalerted route.
- Includes: intentionally firing the unsuppressed AMCAR after masking in the
  scoped PAYDAY 2 Bank Heist and thereby forcing the loud branch.
- Excludes: local suspicion that clears before detection; a scripted combat
  encounter with no prior concealment; losing police sight during a chase.
- Parameters: entry phase, observer, stimulus, detection threshold, panic
  trigger, alarm flag, response delay, shared alert and reversibility.
- Evidence: [PAYDAY 2 decomposition](../games/m-r/payday-2.md).
- Novelty: first isolated for `GAME-0201`; a local perception or deliberate
  reveal permanently changes the remaining objective's global response rules.

## SYS-646 — Maintain compliant civilians as hostages

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: intimidation, restraint, criminal proximity and police rescue
  pressure update each civilian between unalerted, panicked, compliant,
  restrained, following, escaped and rescued states; eligible restrained or
  dominated bodies count as hostages for the heist response.
- Includes: controlling and tying a Bank Heist civilian, moving that hostage
  away from police access and retaining the hostage through control and assault
  phases.
- Excludes: decorative crowds; a friendly escort with no coercion state;
  hostage trade settlement after a player has entered custody.
- Parameters: civilian, awareness, intimidation, compliance, restraint,
  criminal proximity, follow target, police rescuer, escape and hostage count.
- Evidence: [PAYDAY 2 decomposition](../games/m-r/payday-2.md).
- Novelty: first isolated for `GAME-0201`; a neutral autonomous body becomes a
  reversible controlled resource whose physical rescue state changes pressure.

## SYS-647 — Advance a placed objective drill through jams and repair

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: once assembled on its compatible vault fixture, the drill
  advances a visible opening timer while operating, may enter a stopped jammed
  state and resumes only after a legal player repair until the vault gate opens.
- Includes: the ordinary thermal drill on the scoped PAYDAY 2 Bank Heist vault.
- Excludes: an instantaneous key unlock; passive crafting; mining terrain for
  resources; a drill whose breakdown has no player response.
- Parameters: fixture, placement, assembly, duration, operating state, jam
  sample, repair reach, repair channel, progress retention and opened gate.
- Evidence: [PAYDAY 2 decomposition](../games/m-r/payday-2.md).
- Novelty: first isolated for `GAME-0201`; a long objective channel retains
  progress across stochastic stoppages that demand renewed spatial attention.

## SYS-648 — Cycle police response through control and assault pressure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after alarm, law enforcement alternates bounded control,
  anticipation, build, sustain and fade intervals, changing reinforcement
  density and aggression while surviving hostages and difficulty modify
  eligible timing without ending the objective clock.
- Includes: repeated Normal-difficulty police assault waves during the scoped
  PAYDAY 2 Bank Heist drill and cash transfer.
- Excludes: one authored panic population; intensity-adaptive Director pacing;
  a fixed wave-survival terminal that requires killing a finite enemy set.
- Parameters: difficulty, response phase, phase duration, hostage modifier,
  spawn and active limits, enemy classes, aggression, fade condition and cycle.
- Evidence: [PAYDAY 2 decomposition](../games/m-r/payday-2.md).
- Novelty: first isolated for `GAME-0201`; an irreversible alarm starts a
  repeating multi-phase pressure schedule whose low-pressure intervals remain
  tactically usable rather than ending combat permanently.

## SYS-649 — Convert repeated incapacitation into custody and hostage return

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: health loss can down and bleed out a heister, teammate revival
  restores control while eligibility remains, and exhausting the declared down
  allowance transfers the human heister to custody until an eligible hostage
  trade or stock-AI trade restores that slot.
- Includes: Normal Offline PAYDAY 2 downing, bot revival, custody and a stock-AI
  hostage trade when a living bot and hostage make return legal.
- Excludes: immediate one-life elimination; ticketed battlefield respawn;
  self-revival with no teammate or hostage state.
- Parameters: health, down count, bleed-out, rescuer, revival, custody timer,
  hostage, assault phase, trader and returned state.
- Evidence: [PAYDAY 2 decomposition](../games/m-r/payday-2.md).
- Novelty: first isolated for `GAME-0201`; repeated recoverable failure crosses
  into loss of player authority that can be reversed by exchanging a separately
  controlled civilian resource.

## SYS-650 — Convert vault cash into spatially secured loot credit

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an eligible vault cash source becomes one bagged payload; pickup
  binds it to one carrier, a throw restores it as a recoverable world object and
  entry into the declared secure region permanently increments secured loot.
- Includes: one required Bank Heist: Cash money bag deposited in the escape van.
- Excludes: loose cash credited on contact; an inventory item retained merely
  by surviving; final contract and spending-cash settlement.
- Parameters: source, bagging, carrier, carry modifier, throw trajectory,
  recoverability, secure region, required count and secured value.
- Evidence: [PAYDAY 2 decomposition](../games/m-r/payday-2.md).
- Novelty: first isolated for `GAME-0201`; value becomes objective credit only
  after a reversible carrier/world-state object crosses a fixed deposit border.

## SYS-651 — Settle a heist escape into retained payout

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: once the contract's mandatory secured-loot predicate holds,
  eligible crew occupancy of the active escape region closes the heist,
  combines contract and secured-loot value into the disclosed payout and
  retains the result beyond the session.
- Includes: escaping the scoped Normal Bank Heist: Cash after securing at least
  one money bag and reaching its success/payout screen.
- Excludes: career-level optimisation after the result; optional additional
  bags; a failed restart; extraction that does not retain objective value.
- Parameters: secured requirement, escape availability, living or custody
  roster, occupancy, success flag, contract value, loot value, payout partitions
  and retained result.
- Evidence: [PAYDAY 2 decomposition](../games/m-r/payday-2.md).
- Novelty: first isolated for `GAME-0201`; a spatial departure gate settles a
  preceding transported-value chain into a persistent economic result.

## SYS-652 — Initialise a spawn-selected bot survival match

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after hero, map, difficulty and mode are fixed, the system fills
  one bounded Survival session with the controlled participant and AI opponents,
  samples its Easy modifier and match-local loot, then instantiates each side at
  a legal committed or system-assigned spawn.
- Includes: Easy Solo BOT Mode on single-selected Wanchu with Viper Ning.
- Excludes: a persistent survival server; human Ranked matchmaking; combining
  several maps or difficulties; account progression after settlement.
- Parameters: hero, mode, difficulty, map, participants, AI policy, modifier,
  spawn regions, loot tables, seed and countdown.
- Evidence: [NARAKA: BLADEPOINT decomposition](../games/m-r/naraka-bladepoint.md).
- Novelty: first isolated for `GAME-0202`; a player-selected ground spawn is
  resolved inside a fully bot-filled last-survivor session.

## SYS-653 — Resolve grappling-hook attachment and approach

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a fired grappling charge tests its aimed terrain or combatant,
  consumes the item and, on a legal hit, moves the user along the tether toward
  that target until arrival, collision, release or another cancelling state.
- Includes: NARAKA: BLADEPOINT Grappling Hook climb, gap close and escape.
- Excludes: ordinary jumping or wall running; a permanent cooldown-only hook;
  dragging the target back to a stationary user.
- Parameters: projectile, anchor class, hit, tether, pull path, velocity,
  collision, impact response, release and charge consumption.
- Evidence: [NARAKA: BLADEPOINT decomposition](../games/m-r/naraka-bladepoint.md).
- Novelty: first isolated for `GAME-0202`; the same finite carried charge
  resolves against both authored geometry and an independently moving opponent.

## SYS-654 — Resolve common, Focus, Clash and Counter relations

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: simultaneous or reactive melee inputs are classified as common
  attacks, charged Focus Strikes, compatible Clashes or Counters, then resolve
  their priority, stagger, disarm and eligible Counterstrike consequences.
- Includes: NARAKA: BLADEPOINT ordinary melee, Blue Focus, Clash, Quick Counter,
  weapon drop and Counterstrike Combo outcomes.
- Excludes: passive armour reduction; a turn-based parry prompt; ranged
  projectile collision; hero-specific control abilities.
- Parameters: attack class, charge, Focus colour, timing window, collision,
  priority, Clash, Counter, disarm, stagger and follow-up.
- Evidence: [NARAKA: BLADEPOINT decomposition](../games/m-r/naraka-bladepoint.md).
- Novelty: first isolated for `GAME-0202`; the live relation can defeat an
  attack, force its weapon into world state and grant a distinct riposte.

## SYS-655 — Apply damage through armour before Health

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible incoming damage first depletes the controlled hero's
  current match armour capacity, then crosses into Health once that protection
  is exhausted, while restoration may refill either layer separately.
- Includes: NARAKA: BLADEPOINT Survival armour, Health, Armor Powder and Healing
  Berries.
- Excludes: body-region-specific helmets and vests; a downed teammate state;
  passive damage immunity; weapon Durability.
- Parameters: damage, armour quality, armour capacity, penetration, Health,
  restoration, zero state and elimination threshold.
- Evidence: [NARAKA: BLADEPOINT decomposition](../games/m-r/naraka-bladepoint.md).
- Novelty: first isolated for `GAME-0202`; a replaceable match-loot armour layer
  and its dedicated consumable precede one Solo Health pool without DBNO.

## SYS-656 — Consume, zero and restore weapon Durability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible weapon use or combat interaction subtracts from the
  active weapon's match-local Durability; zero changes its declared combat
  effectiveness without deleting the weapon, and a completed Weapon Repair Kit
  restores Durability up to the allowed maximum.
- Includes: NARAKA: BLADEPOINT melee/ranged Durability, zero-Durability Rage
  consequence and Weapon Repair Kit use.
- Excludes: weapon rarity; armour capacity; a tool that disappears at zero;
  permanent account equipment wear.
- Parameters: weapon, use or interaction, cost, current and maximum Durability,
  zero-state modifier, repair cast and restored amount.
- Evidence: [NARAKA: BLADEPOINT decomposition](../games/m-r/naraka-bladepoint.md).
- Novelty: first isolated for `GAME-0202`; exhaustion changes a live combat
  feedback economy while preserving the repairable weapon object.

## SYS-657 — Resolve interruptible survival-item recovery

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a legal uninterrupted recovery-item cast consumes its carried
  item and restores the matching Health, armour or weapon-Durability meter;
  sprint, attack, damage or another declared cancelling state prevents the
  current cast from completing.
- Includes: NARAKA: BLADEPOINT Healing Berries, Armor Powder and Weapon Repair
  Kit use in the scoped Survival match.
- Excludes: passive regeneration; instant armour from looting; teammate healing;
  out-of-match item storage.
- Parameters: item, target meter, missing capacity, cast, allowed movement,
  cancellation, consumption and restored amount.
- Evidence: [NARAKA: BLADEPOINT decomposition](../games/m-r/naraka-bladepoint.md).
- Novelty: first isolated for `GAME-0202`; one interruptible item grammar
  repairs three independently pressured survival/equipment meters.

## SYS-658 — Contract Shadow Corruption and damage exposed participants

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: successive match phases disclose a smaller safe region, contract
  Shadow Corruption toward it on the live schedule and apply damage to
  participants who remain beyond the safe boundary.
- Includes: Shadow Corruption in the scoped NARAKA: BLADEPOINT Solo BOT match.
- Excludes: PUBG's exposure-duration-specific Blue Zone model; one static lethal
  wall; a random bombardment area; a cosmetic map tint.
- Parameters: phase, safe region, boundary, warning, contraction, schedule,
  damage, recovery and final region.
- Evidence: [NARAKA: BLADEPOINT decomposition](../games/m-r/naraka-bladepoint.md).
- Novelty: first isolated for `GAME-0202`; it preserves the NARAKA phase and
  damage contract without importing PUBG-specific exposure escalation.

## SYS-659 — Route Solo elimination through Rebirth or final settlement

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when the Solo hero is eliminated, the system consumes one legal
  Rebirth and returns control if that allowance remains before its cutoff;
  otherwise it finalises removal, updates survivor count and placement, and
  awards the complete Victory result when one participant remains.
- Includes: one Rebirth, later final elimination, placement and first-place
  Victory in the scoped NARAKA: BLADEPOINT Solo BOT match.
- Excludes: teammate revival; unlimited respawn; PUBG's terminal first death;
  post-match rank, quest or account-reward progression.
- Parameters: elimination, Rebirth stock, cutoff, return location and state,
  survivor count, placement, final participant and result.
- Evidence: [NARAKA: BLADEPOINT decomposition](../games/m-r/naraka-bladepoint.md).
- Novelty: first isolated for `GAME-0202`; one recoverable Solo elimination
  precedes the same placement-owning last-survivor settlement.

## SYS-660 — Initialise one dated daily-island expedition

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after date interval, difficulty and participant mode are fixed,
  the system selects the matching generated island from the current map batch,
  samples expedition-local supplies and instantiates control at the Crash Site.
- Includes: standard Peak solo on the island interval beginning 2026-08-30
  17:00 UTC under patch 2.03.a.
- Excludes: joining several daily maps; selecting a user-authored seed; a
  persistent survival server; account state after the expedition.
- Parameters: build, patch, interval, map batch, biome sequence, difficulty,
  player count, loot sample, crash transition and control point.
- Evidence: [PEAK decomposition](../games/m-r/peak.md).
- Novelty: first isolated for `GAME-0203`; civil time identifies a disposable
  shared generated route while supplies are still sampled per expedition.

## SYS-661 — Resolve stamina-bounded surface grip and climb

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: reachable hand contact, aimed body motion, gravity, surface
  geometry and current usable stamina continuously determine attachment,
  upward progress, sliding, resting or release into a fall.
- Includes: PEAK free-surface climbing and ledge transfer.
- Excludes: a fixed ladder animation; unlimited parkour; a grappling projectile;
  stamina use that does not affect attachment.
- Parameters: hand, reach, surface, friction, body pose, input, gravity,
  stamina drain/recovery, attachment and fall.
- Evidence: [PEAK decomposition](../games/m-r/peak.md).
- Novelty: first isolated for `GAME-0203`; arbitrary visible geometry is a
  real-time grip field whose continuity is paid from survival capacity.

## SYS-662 — Convert falls and hazards into ragdoll injury

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: lost support, gravity, velocity, collision and local hazard type
  resolve the body's ragdoll trajectory and apply the resulting injury or other
  affliction that obstructs later survival capacity.
- Includes: PEAK missed grips, damaging landings, rolling falls and biome contact hazards.
- Excludes: authored cutscene falls; direct hostile combat; a stock lost only
  by leaving a fixed arena; cosmetic stumble.
- Parameters: support, height, velocity, collision, ragdoll, hazard, protection,
  injury, status and final rest position.
- Evidence: [PEAK decomposition](../games/m-r/peak.md).
- Novelty: first isolated for `GAME-0203`; physical route error persists as
  obstruction of the same capacity required to recover the climb.

## SYS-663 — Compose hunger, afflictions and weight into climbing capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: current hunger, injury and typed biome afflictions obstruct the
  main stamina bar while carried weight changes activity cost and active food
  may add temporary bonus stamina, yielding the capacity available to climb.
- Includes: PEAK hunger, injury, poison/cold/heat/drowsy-style obstruction,
  item weight and food-derived bonus stamina.
- Excludes: one ordinary health bar; equipment-only durability; a permanent
  character upgrade; team-shared stamina.
- Parameters: base stamina, obstruction types/amounts, weight, activity cost,
  food bonus, recovery and usable capacity.
- Evidence: [PEAK decomposition](../games/m-r/peak.md).
- Novelty: first isolated for `GAME-0203`; heterogeneous harm and inventory
  load are normalised into the exact resource that sustains physical grip.

## SYS-664 — Resolve typed expedition supply effects

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: completed use of one compatible carried food, medical item or
  hazard remedy consumes or advances that item and changes only its declared
  hunger, injury, affliction, bonus-stamina or protection state.
- Includes: PEAK food, Bandages and biome-specific remedies in the scoped ascent.
- Excludes: passive campfire morale; a climbing aid; account inventory;
  untyped generic healing that clears every status.
- Parameters: item, uses, channel, compatibility, target status, amount,
  duration, protection, consumption and cancellation.
- Evidence: [PEAK decomposition](../games/m-r/peak.md).
- Novelty: first isolated for `GAME-0203`; supplies repair distinct portions
  of one composite climbing-capacity problem rather than a single health meter.

## SYS-665 — Resolve persistent rope and piton support

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a legal climbing-aid deployment consumes its carried item,
  attaches it to compatible terrain and exposes a persistent physical line or
  support that later body movement and grip may use.
- Includes: PEAK Rope Spool and Piton route support.
- Excludes: immediate grappling-hook pull; a permanent crafted building;
  ordinary surface grip with no placed item.
- Parameters: aid, target, attachment, line/support geometry, collision, use,
  persistence, detachment and consumed stock.
- Evidence: [PEAK decomposition](../games/m-r/peak.md).
- Novelty: first isolated for `GAME-0203`; finite expedition loot leaves a
  persistent reusable affordance in an otherwise fixed daily surface field.

## SYS-666 — Advance ordered biome hazards and rising pressure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the active biome and standard Peak clock advance their declared
  weather, creatures, traps, fog or rising hazard, applying typed afflictions
  and removing safe lower space until the Scout moves or counters them.
- Includes: the scoped island's rain/wind or cold/heat sample, Gloom hazards,
  Citadel traps/rising pressure and standard Peak fog pressure.
- Excludes: combining mutually exclusive biomes; higher-Ascent-only modifiers;
  random enemies unrelated to traversal; cosmetic weather.
- Parameters: biome, hazard set, clock, trigger, affected region, affliction,
  obstacle, rise, avoidance and reset.
- Evidence: [PEAK decomposition](../games/m-r/peak.md).
- Novelty: first isolated for `GAME-0203`; successive traversal ecologies share
  one ascent clock and attack the capacity needed to stay attached.

## SYS-667 — Settle a lit campfire into biome passage and morale

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: lighting the reached biome campfire records the local passage,
  grants its eligible morale/resource response and clears or opens the authored
  gate into the next ordered region where that gate exists.
- Includes: PEAK biome campfires and the Gloom entrance fire that opens The Citadel.
- Excludes: arbitrary player-built fires; sleeping to skip time; a checkpoint
  respawn not selected in scope; summit Flare ignition.
- Parameters: biome, campfire, reach, lit state, morale, gate, next region and persistence.
- Evidence: [PEAK decomposition](../games/m-r/peak.md).
- Novelty: first isolated for `GAME-0203`; one world fixture both marks ascent
  progress and changes the capacity or topology of the continuing run.

## SYS-668 — Advance zero usable stamina to unconsciousness and solo death

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when obstruction removes all usable stamina, the Scout becomes
  unconscious and a recovery/death interval advances; without restored capacity
  or an eligible external rescue, expiration produces death and ends solo control.
- Includes: unrecovered unconsciousness and terminal death in scoped PEAK solo.
- Excludes: cooperative item revival; Ancient Statue resurrection; checkpoint
  respawn; immediate elimination with no unconscious interval.
- Parameters: usable stamina, unconscious state, temporary-status decay,
  recovery source, timer, external rescuer, death and control terminal.
- Evidence: [PEAK decomposition](../games/m-r/peak.md).
- Novelty: first isolated for `GAME-0203`; the same composite capacity that
  sustains grip also controls a timed, potentially recoverable loss-of-control state.

## SYS-669 — Convert summit Flare into helicopter rescue settlement

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an ignited Flare inside the PEAK region calls the rescue
  helicopter, advances its arrival and boarding countdown, then emits the
  rescue sequence, Scouting Report and completed expedition result.
- Includes: the standard Peak solo positive terminal.
- Excludes: reaching the summit without signalling; Nadir's alternate ending;
  touching the helicopter rope as a separate requirement; post-result replay.
- Parameters: living Scout, region, Flare, signal, helicopter, arrival,
  countdown, rescue sequence, report and result.
- Evidence: [PEAK decomposition](../games/m-r/peak.md).
- Novelty: first isolated for `GAME-0203`; a supply preserved across the full
  route becomes the explicit system request for a bounded rescue settlement.

## SYS-670 — Instantiate a fixed historical character tutorial

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: starting the declared tutorial creates one authored historical
  date, controlled ruler, character network, title graph, realm state and
  ordered guidance layer before returning retained control.
- Includes: Petty King Murchad of Munster in Crusader Kings III's 1066 Learning
  the Game tutorial.
- Excludes: a custom ruler; another bookmark; a later DLC tutorial; post-
  terminal campaign generation.
- Parameters: date, ruler, characters, titles, realm, rules, guidance stage and
  initial control state.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; a live grand-strategy state remains
  historical and persistent while an authored teaching sequence bounds it.

## SYS-671 — Derive effects from character qualities and opinion

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a character's skills, traits, relationships and directed opinion
  modify eligibility, acceptance, task effectiveness and other disclosed realm
  or interaction outcomes.
- Includes: Murchad, marriage candidates, councillors, vassals and commanders
  in the scoped Crusader Kings III tutorial.
- Excludes: one cosmetic biography; a unit class with no person-specific state;
  hidden narrative flavour with no rule effect.
- Parameters: character, skill, trait, relation, opinion, modifier, eligibility,
  acceptance and derived effect.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; the same named actor modifies social,
  administrative and military decisions through inspectable qualities.

## SYS-672 — Settle an accepted political marriage

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an accepted eligible proposal creates the declared spouse and
  family relation, moves characters where rules require and creates any
  resulting alliance or opinion effects.
- Includes: the ordinary marriage taught in Murchad's base-game tutorial.
- Excludes: Grand Wedding activities; childbirth; inheritance after death;
  romance without a submitted marriage.
- Parameters: spouses, marriage type, courts, houses, alliance, opinion and
  settled relationship.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; one accepted social arrangement can
  change both personal and inter-realm network edges.

## SYS-673 — Advance an assigned council task

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while campaign time runs, an appointed councillor applies their
  office, skill and selected target to progress or periodically resolve the
  declared realm task.
- Includes: council work exposed by the scoped Crusader Kings III tutorial.
- Excludes: instant player-authored construction; an unassigned passive trait;
  a court position outside the council.
- Parameters: office, councillor, skill, task, target, progress, periodic effect
  and completion.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; office placement and a separate task
  turn character skill into a persistent time-driven operation.

## SYS-674 — Propagate title hierarchy and vassal obligations

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: direct title ownership, de jure hierarchy, liege-vassal relations
  and current obligations determine realm/domain membership and the taxes and
  levies contributed upward.
- Includes: Murchad's Thomond domain, Ormond vassal relation and Munster realm.
- Excludes: free unit generation unrelated to holdings; post-terminal
  succession; a flat national income with no title graph.
- Parameters: title, rank, holder, de jure parent, domain, liege, vassal,
  obligation, tax and levy contribution.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; nested legal ownership continuously
  produces both administrative scope and military capacity.

## SYS-675 — Instantiate a claim-bounded war and objective

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an accepted declaration binds attacker, defender, legal cause,
  target title, war objective, eligible participants and enforceable outcomes
  into one active war state.
- Includes: the instructed Desmond war in Murchad's tutorial.
- Excludes: hostile combat without a war; choosing the casus belli itself;
  applying the final demand before the score gate.
- Parameters: attacker, defender, casus belli, target title, objective,
  participants, score components and settlement effects.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; a legal title predicate authors the
  contest's geography, score logic and possible ownership result.

## SYS-676 — Gather feudal contributions into a raised army

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a valid muster draws available direct and vassal levies plus
  eligible men-at-arms toward the selected rally point over time, forming a
  controllable army and applying raised maintenance.
- Includes: Murchad's tutorial muster for Desmond.
- Excludes: buying mercenaries; recruiting new men-at-arms; movement after
  gathering; an army permanently present at scenario start.
- Parameters: contribution source, available levy, regiment, rally point,
  distance, gathering interval, army and maintenance.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; a social ownership graph is sampled
  into temporary spatial command capacity.

## SYS-677 — Resolve commander-led battle, retreat and siege

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: raised armies path on the strategic map; contact resolves
  commander, troop, terrain and phase effects into casualties and retreat,
  while an eligible stationary hostile holding advances siege to occupation.
- Includes: Murchad's army, the Desmond field encounter and capital siege.
- Excludes: direct control of individual soldiers; a separate tactical battle
  scene; naval warfare; merely selecting the army destination.
- Parameters: army, commander, route, terrain, supply, advantage, troop class,
  casualty, retreat, fort, besieger count, siege progress and occupation.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; one high-level formation alternates
  between live pursuit/combat and strength-gated fort occupation.

## SYS-678 — Convert war events into war score

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: relevant battles, occupied holdings, captured important
  characters and control of the declared objective update bounded war-score
  components whose total determines available settlements.
- Includes: the Desmond tutorial war score.
- Excludes: generic prestige; campaign score across several wars; title
  transfer before a demand is accepted.
- Parameters: battle result, occupation, prisoner, objective control, ticking
  component, cap, total score and settlement threshold.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; heterogeneous political and military
  events accumulate toward one legally constrained negotiation gate.

## SYS-679 — Enforce war demands and settle tutorial completion

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when the active war permits enforcement, the selected demand
  applies its declared title, vassal, prestige and peace effects, closes the
  war and advances the authored tutorial to its explicit completion state.
- Includes: enforcing the won Desmond war and completing Murchad's guided
  tutorial.
- Excludes: forming Ireland; post-tutorial campaign play; succession after
  Murchad's death; a player-declared analytical stop.
- Parameters: score, demand, target title, holder, liege relation, prestige,
  truce, closed war, tutorial stage and retained control.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; a legal war settlement is also the
  system-authored boundary between guided instruction and an open campaign.

## SYS-680 — Convert examined evidence into authored investigation progress

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system records the ordered inspection of eligible local
  clues, derives the corresponding fact or trail and advances the current
  search area, journal knowledge, preparation information or quest objective.
- Includes: the camp, footprint, nest and corpse evidence that identifies and
  prepares the royal-griffin route in The Beast of White Orchard.
- Excludes: free-form player notes; automatic omniscient target revelation;
  proximity detection without authored interpretation.
- Parameters: investigation, prerequisite fact, clue, order, trace, inference,
  journal entry, bestiary information, objective and completion flag.
- Evidence: [The Witcher 3: Wild Hunt decomposition](../games/s-z/the-witcher-3-wild-hunt.md).
- Novelty: first isolated for `GAME-0205`; several embodied inspections become
  retained authored knowledge that changes the legal quest route.

## SYS-681 — Instantiate one fixed loaner duel packet

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system loads two immutable Main Deck lists, declared Extra
  Decks, fixed concealed order and opening hands, Life Points and empty public
  zones for one named loaner-versus-CPU chapter.
- Includes: Master Duel Tutorial chapter `10003` with two 40-card Main Decks,
  player Extra Deck of five, five-card hands and 4,000 LP each.
- Excludes: personal deck selection, shuffling, matchmaking or collection state.
- Parameters: chapter, decks, order, hands, Extra Decks, LP, CPU and zones.
- Evidence: [Yu-Gi-Oh! Master Duel decomposition](../games/s-z/yu-gi-oh-master-duel.md).
- Novelty: first isolated for `GAME-0206`; one authored duel fixture preserves
  hidden information without randomising or accepting player-built contents.

## SYS-682 — Advance ordered duel phases and active turns

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the system advances Draw, Standby, Main 1, optional Battle,
  optional Main 2 and End phases, performs phase-bound actions, refreshes turn
  allowances and transfers the active turn to the opponent.
- Includes: the chapter `10003` alternating duel, including first-turn draw and
  Battle restrictions.
- Excludes: response ordering inside a Chain; battle calculation; unrestricted
  real-time progression.
- Parameters: active player, turn, phase, draw, allowances, optional phases and next player.
- Evidence: [Yu-Gi-Oh! Master Duel decomposition](../games/s-z/yu-gi-oh-master-duel.md).
- Novelty: first isolated for `GAME-0206`; one active turn has fixed subphases
  but can repeatedly yield short card-response windows to either player.

## SYS-683 — Build and resolve a Spell-Speed Chain backward

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the system alternates legal response opportunities, numbers each
  appended Chain Link and, once neither side adds another, resolves every link
  from newest to oldest without accepting a new link during that resolution.
- Includes: Spell, Trap and effect Chains in the scoped Tutorial duel.
- Excludes: MTG priority where only one top stack object resolves before a new
  priority round; simultaneous effect selection outside this packet.
- Parameters: links, players, Spell Speeds, response window, closure, reverse order and negation.
- Evidence: [Yu-Gi-Oh! Master Duel decomposition](../games/s-z/yu-gi-oh-master-duel.md).
- Novelty: first isolated for `GAME-0206`; the entire closed response sequence
  settles backward as one uninterrupted resolution interval.

## SYS-684 — Apply card text and route cards among duel zones

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: a resolving card or effect applies its clauses in rules order and
  moves affected cards among hand, Deck, field, Graveyard, banished state and
  Extra Deck while retaining current face and position state.
- Includes: fixed-packet draw, destruction, revival, stat change and material movement.
- Excludes: choosing the activation or target; Chain scheduling; collection mutation.
- Parameters: effect, target, clauses, origin, destination, face, position and retained modifier.
- Evidence: [Yu-Gi-Oh! Master Duel decomposition](../games/s-z/yu-gi-oh-master-duel.md).
- Novelty: first isolated for `GAME-0206`; one digital card rule can jointly
  change typed zones, disclosure and battle state inside a fixed Duel.

## SYS-685 — Resolve one attack through position and ATK/DEF

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after attack responses settle, the system compares the attacker's
  ATK with the target's position-appropriate ATK or DEF, destroys the required
  monster and applies the corresponding battle damage, or debits a direct
  attack from opposing Life Points.
- Includes: ordinary chapter `10003` Attack- and Defense-Position battles.
- Excludes: declaring the attack; non-battle effect damage; blocker assignment.
- Parameters: attacker, target, positions, ATK, DEF, destruction, damage and LP.
- Evidence: [Yu-Gi-Oh! Master Duel decomposition](../games/s-z/yu-gi-oh-master-duel.md).
- Novelty: first isolated for `GAME-0206`; one target's orientation switches
  both the comparison statistic and which player can receive battle damage.

## SYS-686 — Settle the Duel result and Solo clear state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when a legal player-loss predicate occurs, the system stops the
  Duel, presents Victory or Defeat and, on the required victory, records the
  chapter and gate clear before returning retained Solo control.
- Includes: opponent zero LP, failed draw or applicable card-defined loss in
  Tutorial chapter `10003`, and controlled-player loss or surrender.
- Excludes: starter-deck selection, Gem rewards, mission progress or a PvP match series.
- Parameters: losing player, predicate, result, chapter clear, gate clear and return state.
- Evidence: [Yu-Gi-Oh! Master Duel decomposition](../games/s-z/yu-gi-oh-master-duel.md).
- Novelty: first isolated for `GAME-0206`; a rules-level card-game terminal also
  closes one authored Solo gate without admitting its reward economy.

## SYS-687 — Update monster exhaustion and feeding recovery

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: eligible combat actions spend a large monster's stamina until
  observable exhaustion changes its attack pressure; the monster may then
  attempt to feed, and completed feeding restores stamina while a timely
  interruption prevents that recovery.
- Includes: Great Jagras exhaustion, prey swallowing and visible swollen-belly
  state during the scoped Monster Hunter: World assignment.
- Excludes: the hunter's stamina gauge; an arbitrary rage phase; health
  regeneration with no feeding action; exact hidden stamina values.
- Parameters: monster, stamina, spend event, exhaustion cue, attack modifier,
  food source, feeding interval, interruption, recovery and visible body state.
- Evidence: [Monster Hunter: World decomposition](../games/m-r/monster-hunter-world.md).
- Novelty: first isolated for `GAME-0207`; an autonomous hostile's live
  resource becomes observable through behaviour and recoverable through an
  interruptible world interaction.

## SYS-688 — Degrade and restore close-range sharpness

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: repeated eligible close-range attacks reduce the equipped
  weapon's sharpness and increase deflection exposure; completing the legal
  whetstone action restores the gauge without replacing or upgrading the
  weapon.
- Includes: `Hunter's Knife I` sharpness loss and whetstone restoration in the
  scoped Monster Hunter: World assignment.
- Excludes: ammunition consumption; permanent weapon durability; smithy
  improvement; a cosmetic blade-colour change.
- Parameters: weapon, attack, sharpness tier, decrement, deflection, whetstone,
  maintenance completion and restored gauge.
- Evidence: [Monster Hunter: World decomposition](../games/m-r/monster-hunter-world.md).
- Novelty: first isolated for `GAME-0207`; one retained weapon cycles between
  attack-driven degradation and live field restoration inside the same hunt.
