# Objective Genes

## OBJ-001 — Reach target value

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: produce an element whose value meets a declared threshold.
- Includes: creating the 2048 tile in the original 2048 ruleset.
- Excludes: maximising an unbounded score without a target-state threshold.
- Parameters: target value.
- Evidence: [2048 decomposition](../games/0-9/2048.md).
- Novelty: not assessed; this is part of the baseline genome.

## OBJ-002 — Maximise accumulated score

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: increase an unbounded or session-bounded numerical evaluation.
- Includes: increasing 2048's accumulated merge score; increasing the NES
  Tetris A-Type score through line clears and soft drops; increasing the
  rank-weighted board score in Threes; increasing Mini Metro's delivered-
  passenger total before network failure; increasing a Dorfromantik Classic
  session score; increasing a Cut the Rope level score through star collection
  and efficient completion; preserving the maximum Hexcells Infinite hex score
  by completing an authored puzzle with fewer classification mistakes.
- Excludes: reaching one fixed threshold as the only objective.
- Evidence: [2048 decomposition](../games/0-9/2048.md) and
  [Tetris decomposition](../games/s-z/tetris.md), and
  [Threes decomposition](../games/s-z/threes.md), and
  [Mini Metro decomposition](../games/m-r/mini-metro.md), and
  [Dorfromantik decomposition](../games/a-f/dorfromantik.md), and
  [Cut the Rope decomposition](../games/a-f/cut-the-rope.md), and
  [Hexcells Infinite decomposition](../games/g-l/hexcells-infinite.md).
- Novelty: not assessed; this is part of the baseline genome.

## OBJ-003 — Preserve move availability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: avoid a state in which no legal state-changing action remains.
- Includes: survival as an implicit continuing objective in 2048 and Threes,
  and avoiding terminal stack obstruction in NES Tetris A-Type.
- Excludes: maximising score independently of terminal mobility.
- Evidence: [2048 decomposition](../games/0-9/2048.md) and
  [Tetris decomposition](../games/s-z/tetris.md), and
  [Threes decomposition](../games/s-z/threes.md).
- Novelty: not assessed; this is part of the baseline genome.

## OBJ-004 — Reconstruct specified configuration

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: transform the existing components into a declared target
  arrangement.
- Includes: restoring a Rubik's Cube so that each face has one colour relative
  to its fixed centres; placing every Sokoban crate onto a goal position;
  arranging the complete FreeCell deck into four suit foundations from ace
  through king; reducing the English Peg Solitaire central game to the exact
  occupancy with one surviving peg in the centre hole; placing Patrick's
  Parabox boxes and the player onto their respective marked goal classes;
  arranging three A Good Snowman Is Hard to Build balls as one decreasing-size
  stack at any legal ground location; fitting the complete ordered Can of
  Wormholes body into a matching fixed worm-shaped hole; making every final
  inbento cell equal the ingredient identity in the visible recipe; restoring
  every button of a Lights Out field to the declared all-off configuration.
- Excludes: reaching a scalar value; maximising score; merely keeping another
  action available.
- Parameters: component count, target equivalence, permitted whole-object
  orientations and alignment tolerance, whether target positions distinguish
  occupant class and whether the target's ground location is fixed or flexible.
- Evidence: [Rubik's Cube decomposition](../games/m-r/rubiks-cube.md) and
  [Sokoban decomposition](../games/s-z/sokoban.md), and
  [FreeCell decomposition](../games/a-f/freecell.md), and
  [Peg Solitaire decomposition](../games/m-r/peg-solitaire.md), and
  [Patrick's Parabox decomposition](../games/m-r/patricks-parabox.md), and
  [A Good Snowman Is Hard to Build decomposition](../games/a-f/a-good-snowman-is-hard-to-build.md), and
  [Can of Wormholes decomposition](../games/a-f/can-of-wormholes.md), and
  [inbento decomposition](../games/g-l/inbento.md), and
  [Lights Out decomposition](../games/g-l/lights-out.md).
- Novelty: not assessed.

## OBJ-005 — Reveal every non-hazard position

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: expose every safe position while leaving all hazardous positions
  unexposed.
- Includes: completing a classic Minesweeper board without detonating a mine.
- Excludes: merely placing markers on every suspected hazard; clearing all
  pieces from a board; maximising score without completing the safe set.
- Parameters: whether correct markers are also required and the number of safe
  positions.
- Evidence: [Minesweeper decomposition](../games/m-r/minesweeper.md).
- Novelty: not assessed.

## OBJ-006 — Complete constraint-satisfying assignment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one finite answer assignment or traced answer object so
  its implied selected and unselected positions satisfy every declared
  constraint simultaneously.
- Includes: filling every empty Sudoku cell while satisfying all row, column
  and block rules; assigning every Nonogram cell as filled or empty so every
  row and column realises its ordered run clues; covering every Flow Free cell
  with non-overlapping paths that connect all matching endpoint pairs; tracing
  a The Witness start-to-end path whose topology and clue-induced regions are
  all valid; completing every LYNE family path through all typed markers while
  satisfying every shared-junction count; assigning every Hexologic cell one
  to three pips while satisfying every overlapping exact line sum; assigning
  every Slant cell one diagonal while satisfying vertex degrees and acyclicity;
  completing a Tents field under exact quotas, non-touching and perfect
  tree-to-tent matching; pairing every Dominosa cell while using every
  unordered domino type exactly once; completing a Bridges network whose
  weighted degrees, crossings, multiplicity bounds and connectivity all pass;
  completing a Light Up field whose clues, source exclusion and illumination
  coverage all pass; completing a Loopy edge assignment whose face counts and
  single-cycle topology both pass; colouring every Map region while preserving
  immutable givens and separating every boundary-adjacent pair; partitioning a
  Galaxies field into connected one-centre half-turn-symmetric regions;
  assigning every Filling cell so each equal-digit component has exact area;
  assigning every Keen cell so all Latin units and arithmetic cages pass;
  linking every Signpost cell into one arrow-compatible ordinal path; rotating
  every Net tile so reciprocal ports form one connected acyclic network;
  permuting Netslide tiles until their fixed ports form the same accepted
  spanning-tree structure against stationary barriers.
- Excludes: reconstructing a separately specified arrangement; revealing
  pre-existing hidden contents; maximising the number of valid partial entries.
- Parameters: position set, symbol domain, accepted completion test and whether
  the instance is guaranteed to have one solution.
- Evidence: [Sudoku decomposition](../games/s-z/sudoku.md) and
  [Nonogram decomposition](../games/m-r/nonogram.md), and
  [Flow Free decomposition](../games/a-f/flow-free.md), and
  [The Witness decomposition](../games/s-z/the-witness.md),
  [LYNE decomposition](../games/g-l/lyne.md), and
  [Hexologic decomposition](../games/g-l/hexologic.md), and
  [Slant decomposition](../games/s-z/slant.md), and
  [Tents decomposition](../games/s-z/tents.md), and
  [Dominosa decomposition](../games/a-f/dominosa.md), and
  [Bridges decomposition](../games/a-f/bridges.md), and
  [Light Up decomposition](../games/g-l/light-up.md), and
  [Loopy decomposition](../games/g-l/loopy.md), and
  [Map decomposition](../games/m-r/map.md), and
  [Galaxies decomposition](../games/g-l/galaxies.md), and
  [Filling decomposition](../games/a-f/filling.md), and
  [Keen decomposition](../games/g-l/keen.md), and
  [Pearl decomposition](../games/m-r/pearl.md), and
  [Signpost decomposition](../games/s-z/signpost.md), and
  [Net decomposition](../games/m-r/net.md), and
  [Netslide decomposition](../games/m-r/netslide.md).
- Novelty: not assessed.

## OBJ-007 — Clear declared board-element targets

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before a bounded attempt ends, remove or hit every declared
  quantity or visible instance of specified target elements from the active
  board.
- Includes: completing the displayed colour-item collection targets of a Royal
  Match level; eating every visible fruit in one Snakebird level before exit;
  removing every visible hook-and-line mechanism in one HOOK level; collecting
  every displayed gem on one Inertia board.
- Excludes: maximising score; clearing every non-hazard position; reconstructing
  a specified arrangement; meta-progression rewards after the level.
- Parameters: target classes, required quantities, credit triggers and whether
  several target conditions are conjunctive.
- Evidence: [Royal Match decomposition](../games/m-r/royal-match.md) and
  [Snakebird decomposition](../games/s-z/snakebird.md), and
  [HOOK decomposition](../games/g-l/hook.md), and
  [Inertia decomposition](../games/g-l/inertia.md).
- Novelty: not assessed.

## OBJ-008 — Segregate types into homogeneous containers

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: rearrange a conserved multiset of typed units so every occupied
  container is filled exclusively by one type and every other container is
  empty.
- Includes: sorting all Water Sort colours into full monochromatic tubes while
  leaving spare tubes empty.
- Excludes: reconstructing a separately specified container-to-type mapping;
  merely reducing mixed boundaries; grouping without container capacity.
- Parameters: type counts, container count, capacity, whether occupied
  containers must be full and target equivalence under container permutation.
- Evidence: [Water Sort decomposition](../games/s-z/water-sort.md).
- Novelty: not assessed.

## OBJ-009 — Checkmate opposing royal piece

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: create a legal position in which the opposing designated royal
  piece is attacked and the opponent has no legal move that removes the attack.
- Includes: checkmating the opponent's king in chess.
- Excludes: physically capturing the royal piece; winning by resignation or
  external penalty; merely gaining material or giving a recoverable check.
- Parameters: royal piece, attack relation and available defensive move set.
- Evidence: [Chess decomposition](../games/a-f/chess.md).
- Novelty: not assessed.

## OBJ-010 — Overlap controlled and rule-defined goal objects

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete the level by placing an object currently controlled by
  the player in the same position as an object currently bearing the declared
  goal property.
- Includes: a `YOU` object sharing a cell with a `WIN` object in Baba Is You.
- Excludes: reaching a permanently designated geometric exit; merely creating
  a `WIN` rule without the required overlap; collecting or removing the goal.
- Parameters: control property, goal property, overlap layer and evaluation
  timing.
- Evidence: [Baba Is You decomposition](../games/a-f/baba-is-you.md).
- Novelty: not assessed.

## OBJ-011 — Preserve protected infrastructure through horizon

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: complete a bounded mission while keeping a declared protected
  infrastructure resource above its terminal failure threshold.
- Includes: defending civilian buildings and retaining non-zero Power Grid
  until an Into the Breach battle's final round completes.
- Excludes: eliminating every hostile unit; maximising score; preserving each
  controlled unit as an independently mandatory target.
- Parameters: protected objects, shared resource, failure threshold, horizon
  and optional secondary objectives.
- Evidence: [Into the Breach decomposition](../games/g-l/into-the-breach.md).
- Novelty: not assessed.

## OBJ-012 — Sustain flow through minimum connected distance

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before the advancing flow terminates, make it traverse at least
  the declared number of connected placed tiles from its fixed start.
- Includes: reducing Pipe Dream's remaining DIST counter to zero by extending
  the Flooz pipeline through enough sections.
- Excludes: connecting fixed paired endpoints; covering every board cell;
  maximising path length without a completion threshold.
- Parameters: required distance, counted tile classes, loop counting and
  success evaluation timing.
- Evidence: [Pipe Mania decomposition](../games/m-r/pipe-mania.md).
- Novelty: not assessed.

## OBJ-013 — Reach target score within action budget

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: accumulate at least a declared score threshold before the finite
  supply of score-producing actions is exhausted.
- Includes: defeating one Balatro Blind by reaching its required Chips before
  all scoring Hands are spent.
- Excludes: maximising an unbounded score with no success threshold; producing
  one element with a target face value; clearing board targets.
- Parameters: score threshold, producing-action allowance, carry-over rule and
  early-success timing.
- Evidence: [Balatro decomposition](../games/a-f/balatro.md).
- Novelty: not assessed.

## OBJ-014 — Deliver designated payload to fixed receiver

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete a bounded attempt by causing one required portable or
  dynamic payload to contact, enter or be committed to one fixed receiving
  object or zone, independently of how the payload's trajectory is controlled.
- Includes: feeding Cut the Rope candy to Om Nom through rope and physics
  interventions; carrying the Bonfire Peaks belongings crate into the bonfire;
  commanding the Golf Peaks ball into the authored hole.
- Excludes: reaching the receiver with the avatar alone; overlapping a directly
  controlled object with a mutable rule-defined goal (`OBJ-010`); extracting a
  full rigid footprint through a boundary opening; transporting repeated demand
  units for unbounded score.
- Parameters: payload identity and count, receiver geometry, accepted contact
  or entry, control pathway, preservation or consumption, overshoot treatment
  and completion timing.
- Evidence: [Cut the Rope decomposition](../games/a-f/cut-the-rope.md),
  [Bonfire Peaks decomposition](../games/a-f/bonfire-peaks.md) and
  [Golf Peaks decomposition](../games/g-l/golf-peaks.md).
- Novelty: not assessed.

## OBJ-015 — Repeatedly produce exact target assembly

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete a production puzzle by automatically constructing and
  submitting the declared structured output the required number of times in
  one uninterrupted valid run.
- Includes: an Opus Magnum machine producing six accepted copies of the target
  molecule in an ordinary campaign puzzle; a SpaceChem reactor repeatedly
  submitting the required molecular product until its shipment quota is met;
  an Infinifactory Training Routine 1 layout delivering ten accepted voxel
  assemblies.
- Excludes: manually reconstructing one static arrangement; reaching a scalar
  value; delivering one unchanged payload to a receiver.
- Parameters: product schema, required count, orientation equivalence and
  uninterrupted-run policy.
- Evidence: [Opus Magnum decomposition](../games/m-r/opus-magnum.md) and
  [SpaceChem decomposition](../games/s-z/spacechem.md), and
  [Infinifactory decomposition](../games/g-l/infinifactory.md).
- Novelty: not assessed.

## OBJ-016 — Minimise independent solution resource metrics

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after functional success, improve a persistent solution by
  independently reducing two or more reported resource-use measurements
  without one mandatory aggregate score replacing them.
- Includes: revising an Opus Magnum machine to reduce cost, completion cycles
  or occupied area, each shown on its own histogram; revising a SpaceChem
  program to reduce cycles or placed symbols as separate measurements;
  revising an Infinifactory layout to reduce cycles, horizontal footprint or
  placed factory blocks independently.
- Excludes: maximising accumulated play score; meeting only one fixed move
  limit; a single lexicographic ranking imposed as the sole objective.
- Parameters: metric set, measurement formulas, comparison population and
  whether trade-offs are player-selected.
- Evidence: [Opus Magnum decomposition](../games/m-r/opus-magnum.md) and
  [SpaceChem decomposition](../games/s-z/spacechem.md), and
  [Infinifactory decomposition](../games/g-l/infinifactory.md).
- Novelty: not assessed.

## OBJ-017 — Complete exact structured evidence account

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete an investigation by filling every mandatory slot of one
  declared structured evidence account with the accepted identities, actions,
  causes, objects, locations or dependent fates supported by fixed evidence.
- Includes: assigning every Obra Dinn soul an identity and compound fate;
  completing The Case of the Golden Idol prologue Scroll with the accepted
  actors, action, object and location.
- Excludes: revealing every safe board position; reconstructing one spatial
  arrangement; understanding a narrative without entering structured answers;
  satisfying a board-wide system of non-semantic variables.
- Parameters: account topology, subject or event count, required semantic
  fields, dependency grammar, accepted synonyms or equivalent causes,
  auxiliary-panel requirements and completion exceptions.
- Evidence: [Return of the Obra Dinn decomposition](../games/m-r/return-of-the-obra-dinn.md)
  and [The Case of the Golden Idol decomposition](../games/s-z/the-case-of-the-golden-idol.md).
- Novelty: not assessed.

## OBJ-018 — Complete finite staged token collection

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: progress through a fixed sequence of puzzle stages by causing a
  represented character to acquire every required member of a declared finite
  token set.
- Includes: Gorogoa's boy obtaining the five coloured fruits or offerings that
  structure the panel-puzzle journey; Tim acquiring Braid's declared finite
  jigsaw-piece set across authored stages.
- Excludes: maximising an unbounded collectible score; collecting optional
  contact rewards; producing repeated copies of one target assembly.
- Parameters: token count, stage order, acquisition carrier and final
  completion presentation.
- Evidence: [Gorogoa decomposition](../games/g-l/gorogoa.md) and
  [Braid decomposition](../games/a-f/braid.md).
- Novelty: not assessed.

## OBJ-019 — Rescue minimum population quota through fixed exit

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: complete an attempt by causing at least a declared share or count
  of a supplied autonomous population to enter a fixed rescue exit, while
  allowing non-credited exits or losses so long as enough entrants remain or
  recur to satisfy the quota.
- Includes: achieving the required rescued percentage in a Lemmings level;
  extracting the displayed minimum number of loose Goo Balls through a World
  of Goo suction pipe; filling a HUMANITY goal with the required recurring
  human flow; guiding enough of a finite Tin Hearts troop through its fixed
  exit.
- Excludes: delivering one required payload to one receiver; maximising an
  unbounded transport score; preserving every unit through a fixed horizon.
- Parameters: finite or recurring supplied population, required count or
  percentage, exit count and whether early completion waits for remaining agents.
- Evidence: [Lemmings decomposition](../games/g-l/lemmings.md) and
  [World of Goo decomposition](../games/s-z/world-of-goo.md), and
  [HUMANITY decomposition](../games/g-l/humanity.md), and
  [Tin Hearts decomposition](../games/s-z/tin-hearts.md).
- Novelty: not assessed.

## OBJ-020 — Repel finite hostile assault

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete a bounded battle by neutralising the finite hostile
  force introduced through its assault sequence before the defence is defeated
  or fully withdrawn.
- Includes: defeating the Viking groups arriving across the complete wave
  sequence of one Bad North island battle.
- Excludes: preserving a shared infrastructure meter through a fixed number of
  rounds; checkmating one royal piece; maximising defeated-enemy score without
  a bounded terminal assault.
- Parameters: force size, wave schedule, neutralisation predicate, defender
  defeat predicate and optional protected-object outcomes.
- Evidence: [Bad North decomposition](../games/a-f/bad-north.md).
- Novelty: not assessed.

## OBJ-021 — Secure accumulated expedition resources

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: gather transferable resources during a repeatable-risk expedition
  and deliberately end the attempt in a state that banks a strategically
  acceptable share before defeat destroys a larger share.
- Includes: returning from a Loop Hero resource expedition, preferably at the
  campfire boundary, with accumulated materials retained for the camp.
- Excludes: maximising abstract score; collecting a fixed required token set;
  reaching an exit with a minimum population quota.
- Parameters: resource classes, retention schedule, safe exit state, voluntary
  threshold and whether the attempt may continue indefinitely.
- Evidence: [Loop Hero decomposition](../games/g-l/loop-hero.md).
- Novelty: not assessed.

## OBJ-022 — Evacuate every required controlled actor through fixed exits

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete a bounded level by bringing every member of a declared
  controlled actor set to its required fixed exit, with no permitted loss or
  below-total completion quota.
- Includes: coordinating Timelie's girl and cat until both satisfy the scoped
  puzzle's escape endpoints; bringing Portal's sole required test subject
  through the chamber exit; navigating the sole Viewfinder avatar to and
  activating the fixed level teleporter; walking Superliminal's sole dreamer
  through the fixed Induction exit after its linked plate opens the door;
  moving Manifold Garden's sole avatar through periodic space to the blue
  switch and then through its linked fixed door; unlocking Maquette's spawned
  house, spanning its approach gap with the key and entering its fixed doorway.
  It also includes moving the sole required Snakebird head-first through the
  activated fixed exit after every fruit is cleared.
- Excludes: rescuing only a minimum share of a supplied autonomous population;
  delivering one indirectly controlled payload; voluntarily withdrawing a
  surviving squad without completing a fixed exit set.
- Parameters: required actor count, shared or actor-specific exits, simultaneous
  arrival rule, capture failure and whether exited actors remain in simulation.
- Evidence: [Timelie decomposition](../games/s-z/timelie.md),
  [Portal decomposition](../games/m-r/portal.md), and
  [Viewfinder decomposition](../games/s-z/viewfinder.md),
  [Snakebird decomposition](../games/s-z/snakebird.md), and
  [Superliminal decomposition](../games/s-z/superliminal.md), and
  [Manifold Garden decomposition](../games/m-r/manifold-garden.md), and
  [Maquette decomposition](../games/m-r/maquette.md).
- Novelty: not assessed.

## OBJ-023 — Extract designated world objects to operational base

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: progress by assigning autonomous carriers to bring declared
  finite world objects or immobile rescue subjects to an operational base that
  accepts and credits each arrival.
- Includes: recovering Pikmin 4 treasures for Sparklium and transporting
  castaways to the S.S. Beagle for rescue.
- Excludes: rescuing a quota of the carrier population itself; directly
  navigating the delivered object; delivering one force-driven payload whose
  receiver contact completes the entire attempt.
- Parameters: target classes, required set or value threshold, base mobility,
  carrier survival requirement, intake credit and campaign persistence.
- Evidence: [Pikmin 4 decomposition](../games/m-r/pikmin-4.md).
- Novelty: not assessed.

## OBJ-024 — Complete finite passenger-service route

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one bounded service run by transporting every required
  waiting passenger to a compatible distributed destination and then bringing
  the service vehicle to its declared route exit.
- Includes: delivering every scoped Cosmic Express alien to a compatible home
  before the train reaches the exit.
- Excludes: maximising an unbounded delivery score; rescuing a minimum quota of
  autonomous agents through one shared exit; transporting world objects to one
  operational base.
- Parameters: passenger set, destination compatibility, vehicle count, route
  exit, tolerated undelivered count and simultaneous final delivery.
- Evidence: [Cosmic Express decomposition](../games/a-f/cosmic-express.md).
- Novelty: not assessed.

## OBJ-025 — Acquire fixed puzzle-gated progress token

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: solve one bounded authored puzzle by bringing the privileged
  controlled body into contact with its fixed progress token, whose acquisition
  credits that room and contributes to later route access.
- Includes: reaching and collecting an orb at the end of an ordinary The
  Swapper puzzle-room arrangement; contacting one already-exposed green sigil
  after solving its authored The Talos Principle A1 challenge.
- Excludes: collecting every member of a finite campaign set; optional rating
  collectibles; reaching a fixed exit without acquiring a token; maximising an
  unbounded token score.
- Parameters: token count per room, eligible collector, credit persistence,
  room-reset behaviour and later gate threshold.
- Evidence: [The Swapper decomposition](../games/s-z/the-swapper.md) and
  [The Talos Principle decomposition](../games/s-z/the-talos-principle.md).
- Novelty: not assessed.

## OBJ-026 — Reach designated traversable world location

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete a bounded spatial task by navigating the directly
  controlled avatar to one designated world location or resident after making
  that target traversably connected.
- Includes: rearranging Carto map fragments to connect a previously unreachable
  land region, then walking Carto to its declared person or place; settling an
  A Monster's Expedition log as a bridge and walking the monster to the
  connected target shore; rotating a fixed Fez room until its hidden rear
  continuation is traversable, then walking Gomez into that compartment;
  rotating Monument Valley's Chapter I bridge into a projected connection and
  sending Ida to the final pedestal; interpreting Chants of Sennaar's first
  instruction, setting its six valves and passing the newly traversable gate.
- Excludes: evacuating every controlled actor through fixed exits; delivering
  an indirectly controlled payload; collecting a token on contact; merely
  reconstructing a target map shape with no avatar traversal requirement.
- Parameters: target identity, arrival radius, required interaction, topology-
  edit requirement, intermediate targets and persistence after arrival.
- Evidence: [Carto decomposition](../games/a-f/carto.md) and
  [A Monster's Expedition decomposition](../games/a-f/a-monsters-expedition.md),
  [Fez decomposition](../games/a-f/fez.md), and
  [Monument Valley decomposition](../games/m-r/monument-valley.md), and
  [Antichamber decomposition](../games/a-f/antichamber.md), and
  [Chants of Sennaar decomposition](../games/a-f/chants-of-sennaar.md).
- Novelty: not assessed.

## OBJ-027 — Exact-once surface processing plus return pose

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete a bounded puzzle by processing every identified surface
  of each required object exactly once and then restoring the controllable
  agent / tool assembly to its declared initial position and orientation.
- Includes: cooking all four faces of the Maiden's Walk sausage once and
  returning Stephen and the fork to the exact start pose.
- Excludes: reconstructing only a final component arrangement; merely touching
  one receiver; processing the whole object without face identity; returning
  to start without completing every surface.
- Parameters: object and face count, processing predicate, allowed repetitions,
  start-pose equality and evaluation order.
- Evidence: [Stephen's Sausage Roll decomposition](../games/s-z/stephens-sausage-roll.md).
- Novelty: not assessed.

## OBJ-028 — Complete exact structured event account

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one investigation case by filling every mandatory slot
  of a structured causal statement with the accepted actors, actions, objects
  or locations supported by fixed evidence.
- Includes: completing The Case of the Golden Idol prologue Scroll describing
  who acted against whom and where the event occurred.
- Excludes: assigning every member of a fixed roster an identity and compound
  fate; understanding a narrative without entering an answer; satisfying every
  variable of a board-wide constraint system.
- Parameters: required semantic fields, event count, accepted synonyms,
  auxiliary-panel requirement and completion feedback.
- Evidence: [The Case of the Golden Idol decomposition](../games/s-z/the-case-of-the-golden-idol.md).
- Replaced by: `OBJ-017`.
- Novelty: not assessed.

## OBJ-029 — Incapacitate finite hostile encounter set

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one bounded combat encounter by incapacitating every
  required member of its finite hostile set before the controlled combatant is
  defeated.
- Includes: clearing a Fights in Tight Spaces room after every required enemy
  is knocked out, killed or removed through a lethal boundary.
- Excludes: surviving a fixed round horizon while hostiles may remain; repelling
  a time-driven multi-wave assault; maximising defeated-enemy score without a
  finite completion set.
- Parameters: required enemy set, incapacitation predicates, reinforcement
  closure, controlled-actor defeat and simultaneous terminal resolution.
- Evidence: [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md)
  and [Tactical Breach Wizards decomposition](../games/s-z/tactical-breach-wizards.md),
  and [Shogun Showdown decomposition](../games/s-z/shogun-showdown.md).
- Novelty: not assessed.

## OBJ-030 — Preserve designated vulnerable actor during clearance

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Conflicting`
- Confidence: `Medium`
- Definition: while completing a finite hostile-clearance encounter, keep one
  designated non-hostile actor alive until the required hostile set is cleared,
  with reward-only versus terminal failure determined by the declared mode.
- Includes: preserving the Ambassador in a Fights in Tight Spaces protect
  encounter; higher difficulty may make Ambassador death terminal.
- Excludes: retaining one shared infrastructure meter through a fixed horizon;
  protecting a hostile Informant who continues to attack; preserving every
  controlled squad member as an implicit preference.
- Parameters: protected actor, health, displacement immunity, reward, terminal
  mode, hostile-clearance predicate and simultaneous death handling.
- Evidence: [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md).
- Novelty: not assessed.

## OBJ-031 — Complete authored room task set

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one bounded authored encounter by satisfying every
  currently declared mandatory predicate in its finite task set, where no one
  task class alone is sufficient.
- Includes: Tactical Breach Wizards rooms requiring a conjunction drawn from
  hostile clearance, rescue, redeployment, laptop use, door sealing or a named
  displacement outcome.
- Excludes: one invariant clearance predicate; optional style/score challenges;
  completing a fixed identity ledger; preserving one shared resource through a
  time horizon.
- Parameters: task count, task vocabulary, ordering, simultaneous credit,
  optional-task separation and room-transition timing.
- Evidence: [Tactical Breach Wizards decomposition](../games/s-z/tactical-breach-wizards.md).
- Novelty: not assessed.

## OBJ-032 — Correctly classify every concealed cell

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete a bounded field by truthfully resolving every initially
  concealed position into its fixed class.
- Includes: completing one Hexcells Infinite puzzle by correctly identifying
  every orange cell as blue or black.
- Excludes: revealing only every non-hazard cell while hazards remain covered;
  constructing values that did not pre-exist the player's assignment; merely
  minimising mistakes without completing the field.
- Parameters: class domain, concealed-position set, completion timing and
  treatment of already visible givens.
- Evidence: [Hexcells Infinite decomposition](../games/g-l/hexcells-infinite.md).
- Novelty: not assessed.

## OBJ-033 — Establish every declared directed network connection

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: construct a network in which every explicitly required directed
  origin-destination pair has at least one traversable route before the system
  accepts the design as functionally complete.
- Includes: reaching `Network Complete` in Freeways only after every road sign
  and building can send traffic to each of its declared destinations.
- Excludes: connecting one undirected pair; maximising throughput after basic
  connectivity; serving randomly arriving requests until failure.
- Parameters: endpoint set, directionality, requirement weights, reachability
  test and whether every endpoint must also receive traffic.
- Evidence: [Freeways decomposition](../games/a-f/freeways.md).
- Novelty: not assessed.

## OBJ-034 — Sacrifice designated carried object to fixed receiver

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete a bounded spatial puzzle by transporting one designated
  portable object with the avatar and releasing or moving it into a fixed
  destructive receiver that consumes it.
- Includes: carrying the belongings crate up the first Bonfire Peaks staircase
  and putting it into the bonfire.
- Excludes: indirectly steering a free payload (`OBJ-014`); preserving the
  delivered object in a target arrangement; reaching the receiver with the
  avatar alone; destroying any interchangeable object as an optional tactic.
- Parameters: required object identity, receiver geometry, accepted entry,
  whether release is explicit and completion timing.
- Evidence: [Bonfire Peaks decomposition](../games/a-f/bonfire-peaks.md).
- Replaced by: `OBJ-014`.
- Novelty: not assessed.

## OBJ-035 — Assemble numbered vehicles at receiver in declared order

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete a bounded routing puzzle by bringing every required
  independently moving vehicle to one fixed receiver and attaching them in the
  exact order declared by their visible ordinal labels.
- Includes: coupling every Railbound carriage behind the locomotive with
  carriage 1 arriving first, then 2 and each remaining successor.
- Excludes: delivering typed passengers to distributed destinations; connecting
  endpoints without moving vehicles; maximising the number of arrivals.
- Parameters: vehicle set, ordinal domain, receiver approach, attachment timing,
  invalid-arrival handling and final completion predicate.
- Evidence: [Railbound decomposition](../games/m-r/railbound.md).
- Novelty: not assessed.

## OBJ-036 — Deliver directly commanded ball into fixed hole

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete a bounded spatial puzzle by issuing declared trajectory
  commands to one required ball until its automatically resolved motion enters
  one fixed authored hole.
- Includes: sequencing Golf Peaks cards and directions so the golf ball enters
  the level's hole exactly.
- Excludes: steering a payload only through indirect environmental intervention;
  navigating an avatar to a location; repeated scoring shots; merely passing
  adjacent to or beyond the receiver.
- Parameters: ball count, receiver geometry, command grammar, accepted entry,
  overshoot treatment and completion timing.
- Evidence: [Golf Peaks decomposition](../games/g-l/golf-peaks.md).
- Replaced by: `OBJ-014`.
- Novelty: not assessed.

## OBJ-037 — Make fixed field monochromatic

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: complete a fixed field by making every position carry one common
  class, while permitting the player to determine which available class
  survives.
- Includes: finishing a KAMI puzzle with the complete paper field in any one
  selected palette colour.
- Excludes: reconstructing one specified per-position pattern; segregating
  several classes into separate containers; clearing all elements; matching
  only adjacent pairs.
- Parameters: field topology, allowed terminal classes and whether every cell
  must belong to one connected component or merely share a class.
- Evidence: [KAMI decomposition](../games/g-l/kami.md).
- Novelty: not assessed.

## OBJ-038 — Match authored optimal action count

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after satisfying the functional completion predicate, earn the
  declared optimal result by using no more than one authored target count of
  chargeable actions.
- Includes: earning Perfect in KAMI by making the field monochromatic within
  the displayed target number of recolours.
- Excludes: a finite allowance whose exhaustion terminates play; reducing two
  or more independently reported machine metrics; maximising an accumulated
  score; an unreported theoretical minimum with no authored target.
- Parameters: counted action classes, equality-versus-upper-bound acceptance,
  target disclosure and non-optimal completion ratings.
- Evidence: [KAMI decomposition](../games/g-l/kami.md).
- Novelty: not assessed.

## OBJ-039 — Extract designated sliding block through fixed boundary gap

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete a bounded sliding-block puzzle by directly relocating
  one designated persistent rigid block until its complete footprint passes
  through one fixed opening in the playfield boundary.
- Includes: clearing the invariant row of the red Rush Hour car and sliding
  that car through the traffic grid's right-side exit.
- Excludes: navigating a continuously controlled avatar through a level exit;
  pushing a crate onto an internal target; reconstructing prescribed final
  positions for every block; ejecting any non-designated blocker.
- Parameters: designated block, footprint, movement axis, gap geometry,
  complete-versus-partial exit test and terminal removal timing.
- Evidence: [Rush Hour decomposition](../games/m-r/rush-hour.md).
- Novelty: not assessed.

## OBJ-040 — Identify one valid relational subset

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete a bounded visible-field puzzle by selecting one existing
  fixed-size subset whose members jointly satisfy a declared relation without
  changing their values or completing an assignment over the whole field.
- Includes: finding and retaining one exactly-three SET from a fixed visible
  12-card solitaire field.
- Excludes: maximising the number or score of subsets across a session;
  reconstructing a specified configuration; assigning values to every field
  position; merely identifying one equal pair.
- Parameters: subset size, acceptance relation, field size, removal policy and
  whether more than one accepted subset may exist.
- Evidence: [SET decomposition](../games/s-z/set.md).
- Novelty: not assessed.

## OBJ-041 — Identify fixed concealed ordered sequence

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete a bounded deduction attempt by submitting an ordered
  sequence whose symbol at every position exactly equals one fixed concealed
  target sequence.
- Includes: breaking a four-position Mastermind code by receiving four exact-
  position indicators for one submitted guess; submitting the exact five-letter
  Wordle answer.
- Excludes: revealing every concealed cell separately; reconstructing a fully
  visible target arrangement; identifying an unordered multiset; maximising a
  similarity score without exact completion.
- Parameters: sequence length, symbol domain, duplicate policy, attempt limit,
  success disclosure and whether successful guess count is scored.
- Evidence: [Mastermind decomposition](../games/m-r/mastermind.md) and
  [Wordle decomposition](../games/s-z/wordle.md).
- Novelty: not assessed.

## OBJ-042 — Reconstruct observationally equivalent concealed layout

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete a deduction puzzle by submitting one fixed-cardinality
  spatial layout whose response to every legal external probe is identical to
  that of the fixed concealed layout, even if its occupied coordinates are not
  literally the same.
- Includes: solving Black Box with any five-ball arrangement that produces the
  same hits, reflections and paired exits for all perimeter lasers.
- Excludes: revealing every concealed cell separately; reconstructing a
  visible target configuration; matching only the probes already fired;
  identifying an ordered sequence.
- Parameters: field topology, occupancy count, complete probe domain, outcome
  equivalence and whether the original layout is revealed after acceptance.
- Evidence: [Black Box decomposition](../games/a-f/black-box.md).
- Novelty: not assessed.

## OBJ-043 — Open bounded staged mechanism enclosure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one authored mechanism puzzle by satisfying its finite
  persistent prerequisite chain, releasing the final enclosure latch and
  physically opening that enclosure.
- Includes: acquiring and applying The Room's Chapter 1 tools, matching all
  three front rings through the eyepiece and opening the unlatched safe door.
- Excludes: reconstructing an exposed target arrangement without opening an
  enclosure; reaching a spatial exit; collecting every campaign token; opening
  one generic lock with a key and no staged dependency chain.
- Parameters: enclosure identity, prerequisite graph, final latch predicate,
  required opening action, completion boundary and restart behaviour.
- Evidence: [The Room decomposition](../games/s-z/the-room.md).
- Novelty: not assessed.

## OBJ-044 — Restore required avatar components and leave bounded scene

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one bounded authored scene by recovering every missing
  avatar component required for its declared capabilities and then traversing
  the newly available exit into the next scene.
- Includes: restoring Josef's missing leg and arm in Machinarium's scrapyard,
  using the recovered arm to cross the oil pool and leaving to the right.
- Excludes: collecting optional avatar upgrades; repairing an inanimate machine;
  merely reaching a visible exit with the starting capability set; opening a
  staged enclosure without avatar restoration.
- Parameters: required component set, enabled capabilities, exit traversal,
  completion boundary, alternate recovery order and reset behaviour.
- Evidence: [Machinarium decomposition](../games/m-r/machinarium.md).
- Novelty: not assessed.

## OBJ-045 — Retrieve inaccessible scene item with constructed reach tool

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one bounded authored inventory puzzle by assembling the
  required reach tool and applying it to move one otherwise inaccessible
  addressed scene object into the player's inventory.
- Includes: using The Longest Journey's clamp, clothesline and inflated-ducky
  fishing instrument to retrieve the iron key beside the electrified track.
- Excludes: opening an enclosure with an ordinary key; restoring avatar parts;
  collecting a reachable item directly; moving a target only for score; using
  a starting permanent ability rather than a constructed tool.
- Parameters: target object, access hazard or distance, constituent set,
  construction sequence, application hotspot, acquisition and completion edge.
- Evidence: [The Longest Journey decomposition](../games/s-z/the-longest-journey.md).
- Novelty: not assessed.

## OBJ-046 — Obtain specified device through intermediary construction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one bounded authored commission by supplying its
  disclosed exact item set to an addressed intermediary, allowing that
  recipient to construct one specified device, and acquiring the resulting
  device into player inventory.
- Includes: supplying Red Edison with oil, vinegar and gold and collecting Day
  of the Tentacle's uncharged super-battery from his shelf.
- Excludes: directly combining held items; buying a pre-existing object with
  currency; receiving an avatar body component for one hand-in; constructing a
  world fixture in place; collecting random output.
- Parameters: intermediary, required input set, output device, construction
  trigger, output location, acquisition action and completion boundary.
- Evidence: [Day of the Tentacle decomposition](../games/a-f/day-of-the-tentacle.md).
- Novelty: not assessed.

## OBJ-047 — Restore persistent world service through collection groups

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete every required persistent collection group in one
  authored area so the system permanently restores a declared world service
  rather than granting the completion object into player inventory.
- Includes: completing Stardew Valley's three standard Boiler Room bundles so
  the minecart network is repaired and becomes available for fast travel.
- Excludes: collecting one immediate bundle reward; constructing a held device;
  paying for the same upgrade through an alternate commercial route; reaching
  one location with an already available transport service.
- Parameters: required group set, restored service, activation boundary,
  persistent access scope, alternate route and completion marker.
- Evidence: [Stardew Valley decomposition](../games/s-z/stardew-valley.md).
- Novelty: not assessed.

## OBJ-048 — Unlock persistent traversal gate through collected exact cover

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one bounded progression packet by collecting every
  gate-addressed rigid piece and arranging those exact footprints into a
  gapless non-overlapping cover that permanently makes the linked passage
  traversable.
- Includes: collecting and arranging The Talos Principle A1's green `L`, `J`
  and `Z` sigils so the first 4 × 3 tetromino gate opens.
- Excludes: automatically activating an exit after exhaustive collection;
  paying a scalar key price; reconstructing a recipe with no world-access
  consequence; restoring a service at a later calendar boundary.
- Parameters: gate identity, collectible roster, arranger board, exact-cover
  predicate, access persistence and completion boundary.
- Evidence: [The Talos Principle decomposition](../games/s-z/the-talos-principle.md).
- Novelty: not assessed.

## OBJ-049 — Collect every required target with indirectly guided walker

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: complete one bounded spatial stage by changing the environment
  or its authoritative interpretation so an autonomous represented walker
  contacts every member of the stage's fixed required target set.
- Includes: guiding Echochrome's Walker through perspective-law routes until it
  collects all echoes in the maze.
- Excludes: directly navigating an avatar to one token; rescuing only a quota
  of a population through an exit; collecting optional score items; completing
  a whole campaign-wide token set across separately bounded stages.
- Parameters: target count, contact radius, collection order, target motion,
  persistence after failure, walker count and completion timing.
- Evidence: [Echochrome decomposition](../games/a-f/echochrome.md).
- Novelty: not assessed.

## OBJ-050 — Maximise correctly processed cases within a work shift

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during one bounded real-time work interval, correctly classify
  as many sequential independent cases as possible because each completed
  correct case contributes to the shift's earned resources while errors incur
  separate penalties.
- Includes: processing more Papers, Please entrants before 6pm to earn more
  credits while avoiding protocol citations.
- Excludes: maximising an abstract score with no case-correctness gate;
  completing a fixed case count; transporting demand continuously; solving one
  case as accurately as possible with no throughput consequence.
- Parameters: pay per correct case, error allowance and penalties, unpaid
  scripted minimum, queue availability and end-of-day resource use.
- Evidence: [Papers, Please decomposition](../games/m-r/papers-please.md).
- Novelty: not assessed.

## OBJ-051 — Expand reviewed evidence coverage through semantic retrieval

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: progress consists of using inferred semantic keys to surface and
  inspect additional fixed evidence records that have not yet been reviewed,
  increasing the player's accessible basis for an interpretation.
- Includes: refining Her Story transcript queries until a later unseen clip
  hidden behind a broad result cap can be watched.
- Excludes: completing a validated structured account; revealing every safe
  board cell; retrieving one specified physical object; merely replaying an
  already reviewed record with no new evidence coverage.
- Parameters: evidence corpus size, watched-state definition, target coverage,
  completion prompt threshold, optional exhaustive target and revisit policy.
- Evidence: [Her Story decomposition](../games/g-l/her-story.md).
- Novelty: not assessed.
