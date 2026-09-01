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
  [Chants of Sennaar decomposition](../games/a-f/chants-of-sennaar.md), and
  [Blue Prince decomposition](../games/a-f/blue-prince.md).
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
  is knocked out, killed or removed through a lethal boundary; defeating every
  enemy in one bounded Slay the Spire combat before player health reaches zero.
- Excludes: surviving a fixed round horizon while hostiles may remain; repelling
  a time-driven multi-wave assault; maximising defeated-enemy score without a
  finite completion set.
- Parameters: required enemy set, incapacitation predicates, reinforcement
  closure, controlled-actor defeat and simultaneous terminal resolution.
- Evidence: [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md)
  and [Tactical Breach Wizards decomposition](../games/s-z/tactical-breach-wizards.md),
  [Shogun Showdown decomposition](../games/s-z/shogun-showdown.md), and
  [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
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

## OBJ-052 — Reach one authored narrative ending

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one run by traversing a sequence of authored branch
  states until the application presents that branch's terminal ending and
  returns or offers return to a replay boundary.
- Includes: reaching any bounded ending route in The Stanley Parable: Ultra
  Deluxe; reaching the first branch-labelled New In Town completion in The
  Sims 4.
- Excludes: completing every ending; merely watching non-terminal dialogue;
  reaching a spatial exit with no branch-dependent conclusion.
- Parameters: branch graph, terminal triggers, reset behaviour, retained
  unlocks and completion presentation.
- Evidence: [The Stanley Parable: Ultra Deluxe decomposition](../games/s-z/the-stanley-parable-ultra-deluxe.md)
  and [The Sims 4 decomposition](../games/s-z/the-sims-4.md).
- Novelty: not assessed.

## OBJ-053 — Sustain and expand an open-ended simulated city

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: maintain fiscal and infrastructural viability while enabling an
  open-ended city population and economy to grow rather than reaching one fixed
  authored terminal solution.
- Includes: ordinary mayor-mode play in SimCity 4 and ordinary new-game city
  development in Cities: Skylines.
- Excludes: completing one disaster mission; maximising a single level score;
  reproducing a prescribed city layout.
- Parameters: population, employment, treasury, service level, mayor rating and player-defined horizon.
- Evidence: [SimCity 4 Deluxe Edition decomposition](../games/s-z/simcity-4-deluxe-edition.md)
  and [Cities: Skylines decomposition](../games/a-f/cities-skylines.md).
- Novelty: not assessed.

## OBJ-054 — Complete and launch a constructed terminal production project

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: finish a finite factory progression by researching and manufacturing the dependent components, constructing or supplying its terminal project and performing the valid launch that marks completion.
- Includes: Factorio and Captain of Industry first-rocket launches and Satisfactory Project Assembly launch.
- Excludes: unlocking one prerequisite; completing one intermediate delivery; open-ended throughput optimisation without the terminal launch.
- Parameters: technology chain, component recipes, delivery phases, terminal structure, payload, launch channel and post-completion continuation.
- Evidence: [Factorio decomposition](../games/a-f/factorio.md), [Captain of Industry decomposition](../games/a-f/captain-of-industry.md) and [Satisfactory decomposition](../games/s-z/satisfactory.md).
- Novelty: not assessed.

## OBJ-055 — Defeat the third-act boss in one continuous climb

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one run by traversing three finite acts and defeating
  each act's terminal boss without the persistent player health reaching its
  failure threshold.
- Includes: ordinary Ascension 0 Slay the Spire victory after the Act 3 boss.
- Excludes: the optional unlocked Act 4; maximising run score; winning only one
  combat encounter.
- Parameters: act count, boss identities, unlock-dependent continuation and
  terminal-health rule.
- Evidence: [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
- Novelty: not assessed.

## OBJ-056 — Complete the finite factory qualification milestone chain

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: advance through the ordinary scenario's ordered milestone chain
  and submit the final exact-shape quota that grants the named qualification.
- Includes: completing shapez 2 Classic/Regular Final Qualification before the
  optional infinite Operator Level becomes the main post-game pursuit.
- Excludes: maximising an endless operator level; completing one intermediate
  shape quota; launching a rocket in a materially finite-resource factory.
- Parameters: scenario, milestone order, final shape schema, delivery quantity,
  difficulty multiplier and post-completion continuation.
- Evidence: [shapez 2 decomposition](../games/s-z/shapez-2.md).
- Novelty: not assessed.

## OBJ-057 — Tip relative combat scale by required damage margin

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: win one bounded card encounter by accumulating a declared net
  direct-damage advantage on a shared two-sided scale before the opponent tips
  that scale by the same margin.
- Includes: winning an Act I Inscryption card battle when the scale reaches a
  five-point advantage on the player's side.
- Excludes: reducing every enemy's Health to zero; reaching a cumulative score
  target with no opposing contribution; surviving a fixed turn count.
- Parameters: winning margin, initial offset, direct-damage contribution,
  opponent contribution, overkill conversion and boss-phase reset.
- Evidence: [Inscryption decomposition](../games/g-l/inscryption.md).
- Novelty: not assessed.

## OBJ-058 — Escape Act I through puzzle-gated final-boss victory

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete a finite multi-run chapter by obtaining one authored
  environment-puzzle item, reaching and defeating the route's final boss, and
  applying that retained item at the resulting exit transition.
- Includes: obtaining the film roll in Leshy's cabin, defeating Leshy and using
  the camera outcome to expose the New Game card at the end of Inscryption Act I.
- Excludes: defeating Leshy without the film roll and returning to another Act
  I run; completing Acts II or III; winning one ordinary card battle.
- Parameters: required item, puzzle chain, route boss, post-boss interaction,
  failed-exit outcome and chapter boundary.
- Evidence: [Inscryption decomposition](../games/g-l/inscryption.md).
- Novelty: not assessed.

## OBJ-059 — Fill settlement reputation before Queen's Impatience

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: win one bounded settlement by filling its Reputation track before
  the opposed Queen's Impatience track reaches its terminal maximum.
- Includes: ordinary Against the Storm settlement victory through Orders, Glade
  Events and sustained high Resolve.
- Excludes: completing an Ancient Seal; maximizing score after victory; merely
  surviving one Storm phase.
- Parameters: reputation target, impatience maximum, difficulty, reputation
  sources, impatience sources and post-settlement reward.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## OBJ-060 — Sustain colony and breach the Temporal Tear

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: keep a base-game colony operational long enough to research,
  construct and supply a space programme that sends a rocket and Duplicant to
  the farthest starmap destination, after which the colony may continue.
- Includes: Oxygen Not Included base-game Great Escape progression through the Temporal Tear.
- Excludes: the Spaced Out! Temporal Tear Opener; indefinite survival alone;
  the separate Monument imperative; DLC asteroid colonisation.
- Parameters: survival, research, discovery, rocket, fuel, crew, destination and continuation.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## OBJ-061 — Sustain and elevate fortress to civilization capital

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: keep an open-ended fortress functioning while population,
  wealth and institutions grow until it becomes an eligible capital and its
  civilization's monarch arrives.
- Includes: ordinary Dwarf Fortress Fortress Mode progression through capital
  status and monarch arrival.
- Excludes: the subsequent seven-symbol Mountainhome quest; Adventure Mode;
  indefinite survival with no institutional growth.
- Parameters: survival, population, created wealth, exported wealth, rank,
  noble rooms, monarch eligibility and continuation.
- Evidence: [Dwarf Fortress decomposition](../games/a-f/dwarf-fortress.md).
- Novelty: not assessed.

## OBJ-062 — Sustain colony, start reactor and launch constructed ship

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: keep a colony viable while researching and constructing a ship,
  survive the reactor's hostile startup interval and launch at least one occupant.
- Includes: RimWorld base-game Crashlanded progression through the constructed-ship credits.
- Excludes: the journey-offer ship; DLC endings; indefinite colony survival without launch.
- Parameters: research, ship resources, reactor startup, defence, occupants and continuation.
- Evidence: [RimWorld decomposition](../games/m-r/rimworld.md).
- Novelty: not assessed.

## OBJ-063 — Complete and launch Project Assembly

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `OBJ-054`.
- Includes: historical references that used `OBJ-063` before registry
  normalisation 006.
- Excludes: new game signatures; use `OBJ-054` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Satisfactory decomposition](../games/s-z/satisfactory.md).
- Merged into: `OBJ-054` by
  [`TAXONOMY_CHANGE_015`](../../research/taxonomy-changes/TAXONOMY_CHANGE_015.md).

## OBJ-064 — Defeat the Ender Dragon and enter the exit portal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete the bounded Survival progression by reaching The End,
  defeating the Ender Dragon and entering the resulting exit portal that
  presents the End Poem and credits.
- Includes: ordinary Minecraft Java Survival first Dragon completion.
- Excludes: merely finding a stronghold; continued post-Dragon exploration;
  permanent one-life completion in Hardcore mode.
- Parameters: portal access chain, Dragon health, crystal state, combat route,
  exit condition and post-credit continuation.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md).
- Novelty: not assessed.

## OBJ-065 — Sustain New London through the Great Storm

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete A New Home by keeping the city and at least part of its
  population alive until the final Great Storm ends and the scenario presents
  its survival and moral-history epilogue.
- Includes: Frostpunk 1.6.2 A New Home completion on Medium difficulty.
- Excludes: merely resolving the Londoners; Endless survival; other scenarios,
  DLC objectives and achievement-specific no-death conditions.
- Parameters: scenario arcs, population, generator state, storm duration,
  survival condition, law history and ending presentation.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## OBJ-066 — Research Mission Completed with Universe Matrices

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: finish the bounded main progression by producing the required
  Universe Matrices from all five coloured matrices and antimatter, then consume
  the declared quantity to complete the Mission Completed technology.
- Includes: Dyson Sphere Program Early Access main mission completion with
  2,000 Universe Matrices.
- Excludes: filling every planned Dyson shell cell; eliminating all Dark Fog;
  post-completion infinite research or megabase optimisation.
- Parameters: prerequisite technologies, matrix recipe, antimatter route,
  required quantity, hash progress and completion presentation.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## OBJ-067 — Complete the campaign and one World’s Fair exhibition

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete the base campaign through its Chapter 4 final naval
  battle, then continue the same city to construct the World’s Fair and finish
  its first selected exhibition.
- Includes: Anno 1800 base-game campaign followed by post-campaign Investor-tier
  monument and exhibition progression.
- Excludes: campaign completion alone; DLC regions or monuments; Creative mode;
  repeating exhibitions indefinitely for a particular reward.
- Parameters: campaign chapters, final battle, continued save, Investors,
  monument phases, exhibition preparation and completion presentation.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## OBJ-068 — Activate the Earth Recultivator for the first map win

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: complete the Folktails map by building, provisioning and
  activating the Earth Recultivator for the first time.
- Includes: congratulations, map badge and flexible-start unlock, regardless of
  optional continued play afterward.
- Excludes: inactive construction; repeated launches; indefinite survival.
- Parameters: faction, map, construction, launch goods and first-win flag.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## OBJ-069 — Complete Soviet Revolution after the introductory campaign

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: complete the first released base campaign, then satisfy every
  mandatory objective branch of Soviet Revolution through its declared finish.
- Includes: the campaign's production, import, export and nuclear-fuel route.
- Excludes: optional sandbox continuation, DLC campaigns or achievements.
- Parameters: predecessor completion, branch states, measured targets and final flag.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## OBJ-070 — Purchase Martian independence from the mission sponsor

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete the scoped Surviving Mars: Relaunched run by meeting the
  colony, people's and sponsor gates, passing the declaration law and paying
  the remaining price so the colony becomes independent from its sponsor.
- Includes: the first achieved purchased-independence state in patch 1.0.7.
- Excludes: declaration without payment; optional post-independence goals and
  monument; full terraforming, mystery completion or exhaustive tech-tree play.
- Parameters: stability, population, comfort, laws, mission goals, declaration,
  contribution, price, payment and independence flag.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## OBJ-071 — Win the regulation bomb-defusal match by round score

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: accumulate the clinching bomb-round score before the opposing
  team under the declared finite regulation and draw or overtime policy.
- Includes: Counter-Strike 2 Competitive victory at thirteen regulation rounds
  and Rainbow Six Siege Pro League regulation/finite-overtime map victory.
- Excludes: maximising kill score; winning a tournament series; Premier rating change.
- Parameters: round wins, clinch threshold, regulation maximum, draw and overtime policy.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md)
  and [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Novelty: not assessed.

## OBJ-072 — Destroy the opposing Ancient before yours falls

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the fixed team wins when legal damage first destroys the enemy
  Ancient while its own Ancient has not already been destroyed.
- Includes: one standard Dota 2 All Pick match.
- Excludes: maximising kills/net worth; ranked rating; surrender procedure.
- Parameters: teams, Ancient health, protection state and terminal winner.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md).
- Novelty: not assessed.

## OBJ-073 — Complete the World Tree main-story finale

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete the released main story by satisfying the ordered tower,
  Sunreach, Panthalus and World Tree mission gates and defeating the terminal
  Sealed Calamity encounter for the first time.
- Includes: one fresh Palworld 1.0 single-player Normal-world story completion.
- Excludes: optional hard-mode towers, exhaustive Pal collection, challenge
  raids, arena ranks and post-story optimisation.
- Parameters: required missions, tower clears, key item, required companion,
  final encounter and completion flag.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md).
- Novelty: not assessed.

## OBJ-074 — Remain the last living Solo participant

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: win one bounded battle-royale match by remaining alive after every
  other independently controlled participant has reached terminal defeat.
- Includes: PUBG Normal Solo `Winner Winner Chicken Dinner`.
- Excludes: maximising kills or placement points; team survival; extraction from
  the map; surviving a fixed clock while opponents remain.
- Parameters: initial participant cap, bot participation, simultaneous defeat
  ordering, self-recovery state, survivor count and terminal winner.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md).
- Novelty: not assessed.

## OBJ-075 — Preserve a recoverable foothold until the world wipe

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: survive one bounded shared-world cycle by retaining or rebuilding
  access to an embodied respawn path and a secured material foothold until the
  scheduled wipe replaces the island.
- Includes: the scoped Rust vanilla monthly-wipe survival objective.
- Excludes: treating a kill, one raid, Workbench 3 or crafted C4 as terminal
  victory; permanent ownership beyond wipe; leaderboard rank.
- Parameters: spawn path, secured storage, recoverable loss, base state, hostile
  pressure, upkeep and wipe boundary.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## OBJ-076 — Extend one survivor life until irreversible death

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: preserve the current survivor's living controllable body for as
  much in-world time as possible; no kill, shelter, crop or elapsed-day
  milestone is a terminal victory, and irreversible character death ends that
  life with its achieved duration.
- Includes: the scoped Project Zomboid Apocalypse `How you died` objective.
- Excludes: respawning the same survivor; treating a thirty-day analytical
  checkpoint as victory; deleting the retained world as part of completion.
- Parameters: survivor identity, elapsed calendar, living state, terminal
  causes, corpse, reanimation and recorded duration.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Additional support: [DayZ decomposition](../games/a-f/dayz.md), for a
  fresh-spawn official-server life with no positive terminal before death.
- Novelty: not assessed.

## OBJ-077 — Complete the main story through the chosen terminal branch

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: advance every required authored mission and setup to a declared
  terminal decision, commit one available branch and complete its resulting
  final mission so the current campaign records a first ending.
- Includes: a fresh Grand Theft Auto V Story Mode critical path from Prologue
  through the first completed The Third Way ending; a fresh Cyberpunk 2077
  critical path through the first completed `Where Is My Mind?` ending.
- Excludes: 100% checklist completion; optional side content or collectibles;
  online progression; replaying an alternate ending after first completion.
- Parameters: required mission graph, heist branches, final option, terminal
  mission, surviving protagonists and completion flag.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md) and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## OBJ-078 — Win one Convergence match by completing or denying the route

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the attacking team wins by capturing the opening mission area and
  escorting its vehicle through the terminal route point before valid time ends;
  the defending team wins by preventing either required completion through the
  final eligible overtime state.
- Includes: one Marvel Rivals Quick Match Convergence result.
- Excludes: maximising eliminations or healing; Competitive rank change;
  winning a multi-map tournament series; Convoy or Domination objectives.
- Parameters: side, capture completion, route checkpoints, terminal point,
  clock, overtime and match result.
- Evidence: [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md).
- Novelty: not assessed.

## OBJ-079 — Deplete the opposing Conquest reinforcement pool first

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the team pursues a match state in which the opposing finite
  reinforcement pool reaches zero before its own pool does, through unrevived
  deaths and sustained ownership of control points.
- Includes: one standard Battlefield 6 Conquest match result.
- Excludes: personal kill-score maximisation; Rush or Breakthrough attacker
  tickets; Domination point-limit scoring; Career XP.
- Parameters: teams, initial tickets, death loss, point ownership, drain,
  zero threshold and result.
- Evidence: [Battlefield 6 decomposition](../games/a-f/battlefield-6.md).
- Novelty: not assessed.

## OBJ-080 — Defeat a route guardian and cross the opened progression threshold

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete a bounded authored route by satisfying its required access state, defeating the mandatory guardian and crossing the newly opened threshold into the next declared progression region or act.
- Includes: Hollow Knight: Silksong Act 1 entry into the Citadel and Elden Ring entry into Stormveil after Margit.
- Excludes: defeating an optional boss; reaching but not crossing the threshold; bypassing the scoped guardian; full-game completion.
- Parameters: required capabilities or gates, guardian, victory state, opened threshold, next region and retained progression.
- Evidence: [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md) and [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## OBJ-081 — Complete ordered prologue hunts and reach the next region boundary

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete the bounded campaign opening by resolving its ordered
  mandatory hunts and retained story gates, then reach the declared transition
  into the next authored region.
- Includes: Monster Hunter Wilds Chatacabra and Quematrice progression through
  completion of `To the Forest` at the Scarlet Forest boundary.
- Excludes: later `Forest Findings`; optional field hunts; High Rank and
  post-game completion.
- Parameters: mandatory hunts, predecessor flags, story interactions, final
  route marker, region boundary and completion flag.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## OBJ-082 — Defeat Margit and cross the first Stormveil threshold

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `OBJ-080`.
- Includes: historical references that used `OBJ-082` before registry
  normalisation 006.
- Excludes: new game signatures; use `OBJ-080` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Merged into: `OBJ-080` by
  [`TAXONOMY_CHANGE_015`](../../research/taxonomy-changes/TAXONOMY_CHANGE_015.md).

## OBJ-083 — Defeat the first Eye and house the eligible Dryad

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: from a new Classic character and world, prepare through mutable
  terrain, equipment, crafting and housing, defeat the world's first Eye of
  Cthulhu before dawn and keep vacant suitable housing until the eligible Dryad arrives.
- Includes: Terraria Desktop 1.4.5.6 first-boss-to-Dryad progression boundary.
- Excludes: stopping after the boss drop without Dryad admission; King Slime or
  later bosses; Hardmode entry and full-game completion.
- Parameters: character, world, preparation route, Eye state, dawn, housing
  vacancy, Dryad eligibility and arrival.
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## OBJ-084 — Remain the last participating squad in Core Battle Royale

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: preserve at least one participating member and eliminate or
  outlast every opposing squad until the match adjudicates this squad as the
  sole remaining participant.
- Includes: Apex Legends Core Unranked Trios Champion objective.
- Excludes: Ranked Point optimisation; individual kill totals; a solo
  last-person objective; winning a round-score or territory match.
- Parameters: squad, active members, recoverable members, opposing squads,
  elimination state and Champion result.
- Evidence: [Apex Legends decomposition](../games/a-f/apex-legends.md).
- Novelty: not assessed.

## OBJ-085 — Reveal the complete hidden word-path partition

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one bounded letter-grid puzzle by identifying every
  authored answer as its exact adjacent-cell path until the accepted disjoint
  paths cover every grid cell exactly once.
- Includes: finding all Strands theme words and the spangram so every letter in
  the daily grid belongs to one accepted answer path.
- Excludes: finding an arbitrary number of valid words; identifying one fixed
  concealed sequence; constructing a freely chosen full-grid path assignment;
  maximising score while unresolved cells remain.
- Parameters: grid size, answer-path count, coverage predicate, designated
  spanning answer, accepted alternate paths and completion feedback.
- Evidence: [Strands decomposition](../games/s-z/strands.md).
- Novelty: not assessed.

## OBJ-086 — Complete a bounded authored cooperative chapter together

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: carry both separately human-controlled protagonists through
  every mandatory segment of one finite authored chapter until their shared
  progression crosses its declared next-chapter boundary.
- Includes: completing Split Fiction's Freedom Fighters and Brave Knights
  opening stories with Mio and Zoe and entering Neon Revenge.
- Excludes: finishing the whole campaign; one actor reaching a room exit while
  the other remains behind; completing optional Side Stories or collectibles;
  maximising a chapter score.
- Parameters: chapter entry, mandatory segment list, required actors, optional
  branches, checkpoint retention and terminal transition.
- Evidence: [Split Fiction decomposition](../games/s-z/split-fiction.md).
- Novelty: not assessed.

## OBJ-087 — Complete the mission objective, then preserve extraction assets

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before a finite mission horizon, satisfy the one required main
  objective that owns mission success, then pursue a separable departure result
  by extracting surviving participants and the shared assets they carry.
- Includes: disabling or destroying the Helldivers 2 illegal broadcast before
  Super Destroyer withdrawal, then extracting Helldivers and carried samples.
- Excludes: extraction as a prerequisite for mission success; optional outpost
  clearance; maximising every reward; winning the complete shared campaign.
- Parameters: main objective, completion predicate, horizon, extraction
  endpoint, survivor, carried asset, post-objective wipe and success retention.
- Evidence: [Helldivers 2 decomposition](../games/g-l/helldivers-2.md).
- Novelty: not assessed.

## OBJ-088 — Earn the first Z-A Royale promotion

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: prepare a legal party, earn the current Challenger's Ticket and
  defeat its designated opponent so the persistent tournament state advances
  from Rank Z to Rank Y.
- Includes: completing Pokémon Legends: Z-A Main Mission 04 by defeating Zach.
- Excludes: later Rank X-to-A progression; exhaustive Pokédex completion; Mega
  Evolution or the base-game finale.
- Parameters: entry rank, party, ticket threshold, designated opponent, victory
  predicate, exit rank and mission completion.
- Evidence: [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Novelty: not assessed.

## OBJ-089 — Escape one standard Trial as a Survivor

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: bring the currently controlled Survivor across one legal powered
  Exit Gate or eligible last-Survivor Hatch boundary before terminal removal.
- Includes: personal escape from the scoped blank-loadout Dead by Daylight 1v4
  Trial, whether or not other Survivors also escape.
- Excludes: merely completing five Generators; maximising Bloodpoints; the
  Killer's sacrifice objective; team-wide all-Survivor evacuation requirement.
- Parameters: controlled Survivor, gate state, Hatch state, boundary crossing,
  terminal removal and individual result.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Novelty: not assessed.

## OBJ-090 — Finish regulation with more goals than the opponent

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: maximise the team's valid goal total relative to one opponent
  until the end of regulation, producing a win when ahead and an accepted draw
  when level under the scoped fixture rules.
- Includes: one EA SPORTS FC 26 Kick Off Classic Match and one managed Football
  Manager 26 league fixture without extra time or a penalty shoot-out.
- Excludes: accumulating an unopposed high score; winning a season table;
  completing Ultimate Team objectives.
- Parameters: goals for, goals against, regulation horizon, draw policy and
  selected side.
- Evidence: [EA SPORTS FC 26 decomposition](../games/a-f/ea-sports-fc-26.md)
  and [Football Manager 26 decomposition](../games/a-f/football-manager-26.md).
- Novelty: first isolated for `GAME-0163`.

## OBJ-091 — Defeat Mom and reach the first clean-save Epilogue

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: carry one ordinary Normal Mode run from clean-save Basement I
  through the boss-gated floor sequence and defeat Mom in Depths II before
  final health depletion so the first Epilogue settles.
- Includes: the first solo Isaac Mom victory in base The Binding of Isaac: Rebirth.
- Excludes: stopping after an earlier floor boss; Mom's Heart, Boss Rush or
  later endings; a manually seeded no-unlock run.
- Parameters: character, difficulty, starting save state, floor sequence, Mom
  defeat, health terminal, Epilogue and unlock eligibility.
- Evidence: [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md).
- Novelty: first isolated for `GAME-0164`; no earlier objective combines this
  generated six-floor run with first-Mom ending and unlock credit.

## OBJ-092 — Complete Horseshoe Overlook and establish the next camp

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete the required Chapter 2 Story Mode mission graph, finish
  `A Strange Kindness` and establish the gang at Clemens Point without leaving
  a required mission in failure state.
- Includes: one clean PC Story Mode route from first free control at Horseshoe
  Overlook after `Eastward Bound` through the Chapter 3 camp transition.
- Excludes: every optional stranger chain, exhaustive Chapter 2 completion,
  later story chapters, either epilogue and Red Dead Online.
- Parameters: required mission set, legal order, optional deferrals, final
  mission, camp transition and checkpoint failure policy.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`; earlier campaign objectives end at
  a complete story, boss or region gate rather than this authored camp era.

## OBJ-093 — Establish the base-game Mars colony before every rival

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: found and develop the selected civilization, construct a
  Spaceport, complete the Satellite and Moon Landing, then launch the Mars
  Reactor, Hydroponics and Habitation modules before another civilization wins.
- Includes: Trajan/Rome under the fixed base-game Science-only setup.
- Excludes: Gathering Storm's Exoplanet Expedition; winning by Religion,
  Culture, Domination or Score; merely researching the required technologies.
- Parameters: civilization, rivals, enabled terminal, Spaceport, five launch
  projects, rival victory state and elimination state.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`; no earlier objective uses this
  ordered base-Civilization-VI Earth-orbit-to-three-Mars-module terminal.

## OBJ-094 — Complete one checkpointless authored auto-run level

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: carry one automatically advancing icon from the authored level
  origin to its finish in a single Normal Mode attempt without terminal contact,
  regardless of how many optional collectibles are credited.
- Includes: first 100% Normal Mode completion of Stereo Madness.
- Excludes: Practice Mode completion; stopping at a best partial percentage;
  completing every official or user-created level; requiring all Secret Coins.
- Parameters: level, mode, origin, finish, attempt validity, optional
  collectibles, reward and prior completion state.
- Evidence: [Geometry Dash decomposition](../games/g-l/geometry-dash.md).
- Novelty: first isolated for `GAME-0167`; earlier spatial exits are reached by
  directly steered or command-routed actors rather than a checkpointless
  one-control auto-run.

## OBJ-095 — Complete Awakening and Vor's Prize and defeat Captain Vor

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: from the first starter selection, complete every mandatory
  Awakening and Vor's Prize step, restore the required Orbiter functions and
  defeat Captain Vor so the opening quest records completion.
- Includes: one fresh-account Solo route using the selected starter Warframe and
  weapons through the final Vor confrontation.
- Excludes: completing the full Star Chart; later quests, Junctions or open
  worlds; collecting every Warframe; multiplayer progression or monetisation.
- Parameters: starter selections, mandatory step set, restored segments, boss
  state, quest completion and retained equipment state.
- Evidence: [Warframe decomposition](../games/s-z/warframe.md).
- Novelty: first isolated for `GAME-0168`; earlier campaign terminals do not end
  at this tutorial-hub restoration and first named-boss boundary.

## OBJ-096 — Complete and settle one employer-supplied cargo delivery

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: accept one supplied loaded vehicle, transport its declared cargo
  from origin to destination under the active job terms and validate drop-off so
  the delivery-results transition closes that contract.
- Includes: one scoped Euro Truck Simulator 2 Quick Job.
- Excludes: accumulating company wealth across multiple jobs; reaching the
  destination without the cargo; an autonomous scheduled transport service.
- Parameters: contract, supplied vehicle, cargo, origin, destination, deadline,
  condition, drop-off, settlement and abandonment.
- Evidence: [Euro Truck Simulator 2 decomposition](../games/a-f/euro-truck-simulator-2.md).
- Novelty: first isolated for `GAME-0169`; earlier delivery objectives terminate
  a passenger route, factory quota or campaign milestone rather than one paid
  directly driven employer load.

## OBJ-097 — Resolve the first Ward Sensors investigation for one recipient

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete the opening and Lesser Zone investigation, obtain the
  Ward Sensors from Squint and hand them to one eligible recipient so `A Needle
  in a Haystack` records its selected terminal branch.
- Includes: the fixed Richter route after exchanging the Mold artifact with
  Squint in S.T.A.L.K.E.R. 2.
- Excludes: completing the whole campaign; handing the sensors to both Richter
  and Zotov; keeping the artifact instead of finishing the declared route.
- Parameters: opening state, investigation route, Squint outcome, artifact
  exchange, sensor possession, recipient, reward and retained quest state.
- Evidence: [S.T.A.L.K.E.R. 2 decomposition](../games/s-z/stalker-2-heart-of-chornobyl.md).
- Novelty: first isolated for `GAME-0170`; the bounded objective closes an
  investigation through a mutually exclusive item hand-in rather than an ending.

## OBJ-098 — Qualify for the Horizon Festival and earn the first Wristband

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: complete the tourist opening, accumulate enough Horizon Festival
  Points through the declared Qualifier route and then complete the Horizon
  Invitational so the first Wristband records Festival membership.
- Includes: the fixed fresh-save Forza Horizon 6 Solo route through the first
  Yellow Wristband and its three granted cars.
- Excludes: becoming a Horizon Legend; obtaining all seven Wristbands or any
  Discover Japan Stamp; multiplayer and Festival Playlist progress.
- Parameters: opening state, Qualifier event set, point threshold,
  Invitational, valid completion, Wristband and retained rewards.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md).
- Novelty: first isolated for `GAME-0171`; the terminal couples alternative
  driving-event progress to one mandatory qualification race and membership gate.

## OBJ-099 — Win two rounds against one fixed opposing fighter

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: in one fixed One on One match, earn the required two round wins
  through KO or favourable time-over before the opposing fighter does.
- Includes: the scoped Ryu-versus-Luke Street Fighter 6 Versus match.
- Excludes: winning a tournament set of several matches; maximising score or
  rank; eliminating a team; merely winning one round.
- Parameters: selected side, opponent, round terminal, required wins, opponent
  wins and final result.
- Evidence: [Street Fighter 6 decomposition](../games/s-z/street-fighter-6.md).
- Novelty: first isolated for `GAME-0172`; earlier match objectives use team
  objectives, round economies, ball score or last-survivor state rather than
  repeated duel rounds for the same fighter pair.

## OBJ-100 — Plant the declared sabotage charge at its mission fixture

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: move an eligible surviving soldier adjacent to the declared
  mission fixture and complete its sabotage interaction so the planted-charge
  condition is recorded before mission settlement.
- Includes: planting X4 at the ADVENT monument in XCOM 2 Operation Gatecrasher.
- Excludes: detonating a carried combat grenade; destroying arbitrary scenery;
  extracting without completing the sabotage interaction.
- Parameters: fixture, eligible soldier, adjacency, interaction, planted flag
  and conjunction with other mission requirements.
- Evidence: [XCOM 2 decomposition](../games/s-z/xcom-2.md).
- Novelty: first isolated for `GAME-0176`; earlier device objectives focus on
  timed competitive activation or neutralisation rather than a squad mission's
  persistent sabotage flag combined with hostile clearance.

## OBJ-101 — Win one Soccar match by decisive goal score

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: finish the bounded match with more valid goals than the opposing
  team, either by retaining a regulation lead through its legal terminal or by
  scoring the first goal of sudden-death overtime after a tie.
- Includes: one default five-minute Rocket League `3v3` Private Match result.
- Excludes: an accepted regulation draw; rank or tournament-series victory;
  maximising personal points, shots or demolitions.
- Parameters: selected team, goals for, goals against, regulation terminal,
  overtime state, deciding goal and final winner.
- Evidence: [Rocket League decomposition](../games/m-r/rocket-league.md).
- Novelty: first isolated for `GAME-0177`; `OBJ-090` accepts a draw, while this
  objective requires a goal-decided terminal after conditional overtime.

## OBJ-102 — Fabricate the first submersible and return to powered refuge

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: convert a fresh breath-limited survival start into one operable player-built submersible, pilot it within its safe envelope to a player-built powered habitat and finish alive inside the dry breathable refuge.
- Includes: Subnautica's scoped first-Seamoth route from Lifepod 5 to a shallow I Compartment, Hatch and Solar Panel habitat.
- Excludes: Moonpool docking; vehicle upgrades; curing infection; launching the Neptune rocket or completing the campaign.
- Parameters: entry save, blueprint, vehicle, safe depth, destination habitat, power, integrity, survivor state and terminal entry.
- Evidence: [Subnautica decomposition](../games/s-z/subnautica.md).
- Novelty: first isolated for `GAME-0178`; the analytical terminal requires knowledge, production, mobile life support and a verified refuge return.

## OBJ-103 — Defeat the opposing civilization under Conquest

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: make the sole opposing civilization resign or remove its Conquest-relevant villagers, military and production buildings before the player's civilization suffers the same terminal state.
- Includes: the scoped Britons-versus-Franks Conquest skirmish in Age of Empires II: Definitive Edition.
- Excludes: Wonder, Relic, Score and campaign victory; winning one battle while the opponent can still rebuild.
- Parameters: player civilization, opponent, alliance, remaining unit and building set, resignation and terminal result.
- Evidence: [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
- Novelty: first isolated for `GAME-0179`; success evaluates the opponent's recoverable civilization-wide economy and army rather than one fixed target.

## OBJ-104 — Complete one planned parking-to-parking logged flight

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: manually take the selected powered-down aircraft from departure
  parking through takeoff and the declared route to a safe destination landing,
  parking stop, shutdown and persistent Free Flight logbook entry.
- Includes: the scoped Microsoft Flight Simulator 2024 Cessna 172 G1000 flight
  from `KBFI` parking to `KTIW` parking.
- Excludes: merely becoming airborne; a touch-and-go; Career score or payment;
  destination overflight; autopilot or teleport completion.
- Parameters: aircraft, origin, destination, route, takeoff, landing, parking,
  shutdown, logbook entry and invalid shortcut.
- Evidence: [Microsoft Flight Simulator 2024 decomposition](../games/m-r/microsoft-flight-simulator-2024.md).
- Novelty: first isolated for `GAME-0180`; the terminal validates a complete
  manual aviation systems cycle through an explicit non-competitive record.

## OBJ-105 — Win two Control rounds before the opposing team

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: in one ordinary Quick Play Control match, earn two round wins by
  taking and holding each active neutral point to its legal percentage terminal
  before the opposing team earns two rounds.
- Includes: the scoped Overwatch 5v5 Role Queue Control result on Busan.
- Excludes: maximising eliminations, damage or healing; Competitive rating;
  winning one submap; Escort, Hybrid, Push, Flashpoint or Clash.
- Parameters: teams, submaps, point ownership, round percentages, overtime,
  round wins, clinch threshold and match result.
- Evidence: [Overwatch decomposition](../games/m-r/overwatch.md).
- Novelty: first isolated for `GAME-0181`; two retained round wins are built
  from separate symmetric point-percentage races.

## OBJ-106 — Conclude the Ethiopian war through capitulation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: as tutorial Italy, coordinate national preparation and the live
  land-air campaign until Ethiopian territorial loss crosses its surrender
  threshold and the immediate war settlement concludes the bounded conflict.
- Includes: the official Hearts of Iron IV Italy tutorial from its first
  controllable 1936 frame through Ethiopian capitulation.
- Excludes: continuing the Italian save after settlement; world conquest;
  winning one battle without country surrender.
- Parameters: country, opponent, tutorial start, national preparation, fronts,
  victory-point control, surrender threshold, capitulation and settlement.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; a country terminal emerges from
  coupled national allocation, logistics and distributed territorial control.

## OBJ-107 — Survive normal Mad Forest until its thirty-minute completion

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: keep the selected character alive through the normal Mad Forest
  wave schedule until the stage clock reaches `30:00` and completion is awarded,
  regardless of the expected Reaper death that settles the completed run.
- Includes: fresh-save solo Antonio in base-game normal Mad Forest.
- Excludes: killing the Reaper; Endless mode; maximising gold, kills or level;
  completing later unlock chains or Adventures.
- Parameters: character, stage, mode, entry clock, health, time limit,
  completion flag, Reaper and settlement.
- Evidence: [Vampire Survivors decomposition](../games/s-z/vampire-survivors.md).
- Novelty: first isolated for `GAME-0183`; the authored success boundary is
  followed by a deliberate lethal system response rather than replacing it.

## OBJ-108 — Exhaust the opposing Ground Domination team first

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: in one ordinary Ground Arcade Domination match, make the opposing
  team's ticket pool reach zero or leave it with no players able to spawn ground
  vehicles before either terminal applies to the allied team.
- Includes: the scoped War Thunder three-point Domination result.
- Excludes: personal kill or capture score; research and Silver Lion rewards;
  Conquest, Battle, Air, Naval, Realistic or Simulator results.
- Parameters: teams, tickets, three point owners, destroyed vehicles, spawnable
  players, zero threshold, exhaustion and result.
- Evidence: [War Thunder decomposition](../games/s-z/war-thunder.md).
- Novelty: first isolated for `GAME-0184`; either a shared ticket resource or
  the remaining distributed vehicle-spawn capacity can establish the same team
  terminal.

## OBJ-109 — Cause the opposing player to lose the single game first

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: win one two-player card game by making the opposing player meet a
  legal loss condition before the controlled player does.
- Includes: reducing the opponent to zero life, making them draw from an empty
  library, accepting their concession or resolving an applicable card-defined
  result in the scoped Starter Deck Duel game.
- Excludes: winning a best-of-three match; ranked-season progress; event rewards;
  maximising damage, creatures or collection value.
- Parameters: players, life, library, concession, card-defined terminal,
  simultaneous loss, draw and Arena result overlay.
- Evidence: [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md)
  and [Yu-Gi-Oh! Master Duel decomposition](../games/s-z/yu-gi-oh-master-duel.md).
- Novelty: first isolated for `GAME-0185`; multiple rules-level loss predicates
  converge on one adversarial single-game result rather than a score threshold.

## OBJ-110 — Survive the first cooperative winter and enter spring together

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: keep both scoped survivors alive and controllable through default Autumn and the complete first Winter, then reach the first transition into Spring beside a viable shared warm base.
- Includes: both Wilson survivors beside a lit Fire Pit at a shared base containing an Alchemy Engine, Crock Pot and Chest when the world clock leaves Winter after day 35.
- Excludes: a game-authored victory claim; defeating a seasonal boss; surviving indefinitely; completing Spring, Summer, caves or a quest arc.
- Parameters: survivors, life state, default season lengths, transition clock, Fire Pit, fuel, warm item, Alchemy Engine, Crock Pot, Chest and shared-base position.
- Evidence: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Novelty: first isolated for `GAME-0186`; an explicit analytical terminal closes one complete cooperative preparation-and-climate cycle in an otherwise open-ended world.

## OBJ-111 — Complete or deny one authored Payload route

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: resolve one asymmetric route match when attackers deliver their
  objective cart through the terminal marker before legal time ends, or
  defenders clear the last eligible overtime pressure before that delivery.
- Includes: one Team Fortress 2 Casual Upward round, where BLU wins by pushing
  the cart into checkpoint D's pit and RED wins by denying that result through
  the final legal overtime state.
- Excludes: personal score or eliminations as a terminal; Payload Race; an
  escort ruleset whose vehicle first requires a separate opening-area capture;
  post-match XP or rematch voting.
- Parameters: attacking team, defending team, route, checkpoints, terminal,
  clock, overtime pressure and declared result.
- Evidence: [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
- Novelty: first isolated for `GAME-0187`; the route begins with an active
  attacker cart and closes through delivery-or-denial without an opening
  capture phase.

## OBJ-112 — Complete one Sastasha Duty Support route

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: satisfy every required authored Sastasha route gate and defeat
  Denn the Orcatoothed before the instance limit so the game issues the
  ordinary duty-complete result.
- Includes: one level-synced Gladiator tank run with the preset Duty Support
  healer and two DPS NPCs.
- Excludes: clearing one intermediate boss; opening every optional coffer or
  side room; Mapping the Realm; levelling or gearing after the duty; Sastasha
  (Hard).
- Parameters: duty, required objectives, switches, keys, bosses, final boss,
  time limit, completion flag and unsuccessful closure.
- Evidence: [FINAL FANTASY XIV Online decomposition](../games/a-f/final-fantasy-xiv-online.md).
- Novelty: first isolated for `GAME-0188`; a fixed autonomous-role party must
  convert clue, key and combat dependencies into one instanced MMO terminal.

## OBJ-113 — Escape one authored captivity tutorial into retained open-world control

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete the mandatory character gate, survive the scripted
  disaster and satisfy one declared escort branch's equipment, combat,
  interaction and traversal gates until the opening quest completes and the
  persistent character first gains controllable exterior-world state.
- Includes: one fresh Skyrim Special Edition `Unbound` (`MQ101`) escape through
  the Hadvar branch to first retained control outside the Helgen cave with
  `Before the Storm` active.
- Excludes: merely entering Helgen Keep; defeating one interior hostile; reaching
  Riverwood; completing a later main quest or the open-world campaign.
- Parameters: character confirmation, disaster, escort branch, required gates,
  opening quest, cave exit, successor quest and retained exterior control.
- Evidence: [The Elder Scrolls V: Skyrim Special Edition decomposition](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md).
- Novelty: first isolated for `GAME-0190`; mandatory identity, one exclusive
  escort path and a tutorial dungeon settle directly into an open-world save.

## OBJ-114 — Complete the first Beacon rescue and regain campaign control

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: follow the declared early prologue campaign gates to the Beacon,
  manually win its first required battle and allow the Rescue mission to settle
  into the first retained campaign-control or recruitment instruction state.
- Includes: one fresh The Lost God run as Prince Yuri's Kislev Expedition in
  the scoped Total War: WARHAMMER III ruleset.
- Excludes: completing the whole prologue; later Dervingard or Chaos-realm
  missions; one custom battle; autoresolve; continuing recruitment after the
  first returned campaign state.
- Parameters: campaign entry, refuge, building instruction, route, Beacon,
  battle, enemy rout, mission completion and retained return state.
- Evidence: [Total War: WARHAMMER III decomposition](../games/s-z/total-war-warhammer-iii.md).
- Novelty: first isolated for `GAME-0191`; an authored tutorial terminal
  requires a turn-based strategic prelude, a manually resolved live battle and
  the resulting return to persistent campaign authority.

## OBJ-115 — Seal The Hotel exit checkpoint with every living Survivor

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: traverse the authored Hotel chapter and bring every currently
  living Survivor into its ground-floor exit checkpoint, then close the door so
  the game issues the ordinary chapter-complete transition.
- Includes: one Normal Single Player Dead Center / The Hotel run controlling
  Coach with Rochelle, Ellis and Nick stock bots.
- Excludes: reaching the elevator; surviving one mob; entering the safe room
  alone; completing the remaining Dead Center campaign; a finale evacuation.
- Parameters: chapter, controlled Survivor, living roster, route gates, panic
  event, checkpoint, occupancy, door closure, completion and next chapter.
- Evidence: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md).
- Novelty: first isolated for `GAME-0192`; a variable Director-populated route
  closes through collective living occupancy and a physical seal rather than a
  kill quota or extraction vehicle.

## OBJ-116 — Complete one solo Normal Devil's Lair Fireteam Op

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: clear the authored mesh-defence and Walker gates, defeat Sepiks
  Prime and reach ordinary activity-complete plus end-chest state in one
  direct-launched solo Normal Fireteam Op.
- Includes: current Destiny 2 `The Devil's Lair: Customize`, one player, Normal,
  no player-selected modifiers and the fixed Titan/loadout packet.
- Excludes: stopping after the mesh or Walker; maximising grade; matchmaking;
  completing another Op; repeating the chest for account progression.
- Parameters: activity hash, participant count, difficulty, modifier set,
  loadout, ordered gates, final boss, completion flag, grade and chest.
- Evidence: [Destiny 2 decomposition](../games/a-f/destiny-2.md).
- Novelty: first isolated for `GAME-0193`; one live-service shooter terminal
  joins a fixed legacy strike route to current Ops scoring and reward state
  without extraction, campaign completion or human-party dependence.

## OBJ-117 — Defeat Radagos and establish the first campaign clan identity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: satisfy the opening Campaign tutorial's recruitment, raider and
  hideout gates, defeat Radagos through the declared troops-assisted choice,
  confirm family name, banner and colours and regain retained campaign-map
  authority with the tutorial closed.
- Includes: one fresh stable v1.4.8 Mount & Blade II: Bannerlord Campaign from
  character packet through the first Radagos hideout and clan identity gate.
- Excludes: merely finding the hideout; the optional solo duel; Rebuild Your
  Clan, Rescue Your Family or any later kingdom/campaign objective; Sandbox.
- Parameters: character packet, recruits, grain, raider parties, hideout,
  Radagos response, victory state, family name, banner, colours and returned
  campaign control.
- Evidence: [Mount & Blade II: Bannerlord decomposition](../games/m-r/mount-and-blade-ii-bannerlord.md).
- Novelty: first isolated for `GAME-0194`; repeated campaign contacts and one
  commanded hideout battle settle through a clan-identity gate rather than at
  the battle result alone.

## OBJ-118 — Complete Road Master and retain one valid elapsed time

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: drive the supplied Ardente 310M through every authored Road
  Master checkpoint in order, cross the valid final gate and reach the mission
  result with one retained elapsed Time Trial entry.
- Includes: one current v0.39.4 unmodded stock Road Master completion.
- Excludes: merely reaching a later gate after missing its predecessor;
  completing another Time Trial; maximising leaderboard rank; Free Roam,
  Career or repeated time optimisation.
- Parameters: mission, supplied vehicle, route, checkpoint order, final gate,
  elapsed time, retained entry and non-completion/retry boundary.
- Evidence: [BeamNG.drive decomposition](../games/a-f/beamng-drive.md).
- Novelty: first isolated for `GAME-0195`; the bounded positive terminal is a
  standalone supplied-car soft-body route evaluation rather than a rival win,
  delivery settlement, logged flight or campaign unlock.

## OBJ-119 — Complete and collect one borrowed-equipment field contract

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: accept one field-work offer with employer machinery, manually
  transform enough of its assigned field into the required accepted state and
  collect the completed contract so its net payment closes the job.
- Includes: one scoped Farming Simulator 25 Riverbend Springs Fertilizing
  contract using `Borrow Items`.
- Excludes: operating an open-ended farm; finishing only one strip; maximising
  yield across a crop season; a cargo delivery; repeating contracts or spending
  the resulting balance.
- Parameters: contract type, field, supplied fleet, required treatment,
  coverage threshold, gross reward, borrowing deduction, collection and net
  account credit.
- Evidence: [Farming Simulator 25 decomposition](../games/a-f/farming-simulator-25.md).
- Novelty: first isolated for `GAME-0196`; one temporary productive vehicle-tool
  system must change a persistent surface before explicit economic settlement.

## OBJ-120 — Mount Eikthyr's trophy and unlock the first Forsaken Power

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: reveal and reach Eikthyr's altar, summon and defeat Eikthyr,
  recover its guaranteed trophy and mount it on the matching Sacrificial Stone
  so the first Forsaken Power becomes available.
- Includes: one current Valheim 0.221.12 solo Normal seed from spawn control to
  mounted Eikthyr Trophy and available power.
- Excludes: boss defeat without mounting; merely collecting Hard Antlers;
  activating the power after unlock; Black Forest or later Forsaken progress.
- Parameters: world seed, wayfinder, altar, offering, boss, guaranteed trophy,
  sacrificial stone, mounted state and power availability.
- Evidence: [Valheim decomposition](../games/s-z/valheim.md).
- Novelty: first isolated for `GAME-0197`; the boss result remains incomplete
  until its carried trophy settles at a separate matching progression fixture.

## OBJ-121 — Be the last fixed participant with a remaining stock

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: in one fixed two-participant Stock match, cause the opposing
  fighter to lose every personal stock before the selected side does and reach
  the resulting winner/loser state.
- Includes: the human Bödvar objective against the Easy CPU Bödvar in the
  scoped Brawlhalla match.
- Excludes: first-to-two health-bar rounds; maximising timed score; team-shared
  lives; winning a tournament set, rank or account reward.
- Parameters: selected side, opponent, starting stocks, knockout condition,
  remaining stocks, clock boundary, winner and result state.
- Evidence: [Brawlhalla decomposition](../games/a-f/brawlhalla.md).
- Novelty: first isolated for `GAME-0198`; repeated same-arena returns consume
  the exact resource whose final exhaustion directly settles the duel.

## OBJ-122 — Classify the street race, escape and retain its result

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one fixed street race through its ordered finish, evade
  the mandatory resulting police pursuit and enter the declared garage so the
  classified event result and earnings become retained.
- Includes: `Shopping Spree`, LPD escape and Rydell's Rydes settlement in the
  scoped Need for Speed Unbound Story prologue.
- Excludes: winning The Grand; merely crossing the race finish; being busted;
  completing a later paid event; Online rank or campaign-wide cash goals.
- Parameters: event, route, classified place, payout, Heat, pursuit, search,
  escape, garage entry, retained result and bust/failure state.
- Evidence: [Need for Speed Unbound decomposition](../games/m-r/need-for-speed-unbound.md).
- Novelty: first isolated for `GAME-0199`; the classified finish is a necessary
  midpoint and only escape plus garage entry closes the bounded objective.

## OBJ-123 — Defend the A/D front until attacker troop force is exhausted

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: as the defending team, prevent the attackers from completing
  every ordered sector until their finite troop-force pool reaches zero and the
  match declares defender victory.
- Includes: the defender-side Luna trace on Coliseum in the scoped Delta Force
  Attack and Defend match.
- Excludes: winning by symmetric Conquest tickets; capturing the final sector as
  attackers; personal kill-score maximisation; post-match rank or rewards.
- Parameters: side, ordered sectors, active objectives, attacker troop force,
  completed sectors, zero-ticket terminal and declared result.
- Evidence: [Delta Force decomposition](../games/a-f/delta-force.md).
- Novelty: first isolated for `GAME-0200`; success is asymmetric attrition
  against a replenishable attacker pool across an advancing objective front.

## OBJ-124 — Open the vault, secure required cash and escape

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one bounded bank contract by opening the declared vault,
  converting at least the contract minimum into secured cash and occupying the
  available escape so the success and payout result settle.
- Includes: one Normal Offline PAYDAY 2 Bank Heist: Cash requiring one secured
  money bag before escape.
- Excludes: securing every optional bag; maximising experience; a stealth-only
  requirement; later Crime.net, skill or Infamy progression.
- Parameters: contract, vault fixture, opening state, loot class, minimum count,
  secured count, escape region, crew state, success and payout.
- Evidence: [PAYDAY 2 decomposition](../games/m-r/payday-2.md).
- Novelty: first isolated for `GAME-0201`; an interruptible access process,
  embodied value transport and spatial departure form one conjunctive terminal.

## OBJ-125 — Ascend one dated island and complete summit rescue

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: in one fixed daily-island expedition, traverse the ordered biomes,
  reach the PEAK alive and ignite an eligible Flare so helicopter rescue and the
  completed expedition result settle.
- Includes: standard Peak solo on the scoped 2026-08-30 daily island interval.
- Excludes: merely reaching the summit; earning Peak Badge without result
  settlement; Nadir; cooperative resurrection; starting another expedition.
- Parameters: daily identity, difficulty, biome progress, life state, summit
  region, Flare, rescue sequence, report and success result.
- Evidence: [PEAK decomposition](../games/m-r/peak.md).
- Novelty: first isolated for `GAME-0203`; a generated vertical route must
  preserve one explicit signal action beyond arrival to turn survival into rescue.

## OBJ-126 — Win and settle Murchad's guided Desmond war

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: follow the fixed Murchad teaching sequence far enough to declare,
  win and enforce the instructed Desmond war, then reach the explicit tutorial
  completion state with retained campaign control.
- Includes: the current base-game Learning the Game tutorial through its
  Desmond settlement.
- Excludes: creating the Kingdom of Ireland; surviving until Murchad dies;
  succession; later generations; any player-declared calendar checkpoint.
- Parameters: tutorial, ruler, target title, declared war, war score, enforced
  demand, completion state and retained control.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; an open-ended dynasty simulation
  supplies one system-authored completion immediately after a legal title war.

## OBJ-127 — Complete the White Orchard griffin investigation and hand-in

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: satisfy the required informant, clue and material gates of The
  Beast of White Orchard, defeat the royal griffin, loot and hand in its trophy,
  settle the declared reward response and reach retained quest-complete control.
- Includes: the fresh base-game quest through `Take the coin` and resumed Lilac
  and Gooseberries control.
- Excludes: stopping at the kill; leaving the trophy unreported; the White
  Orchard tavern incident, Vizima, expansions or the broader search for Ciri.
- Parameters: quest, clue gates, Buckthorn, preparation, target, defeat,
  trophy, captain, response, reward, completion flag and retained control.
- Evidence: [The Witcher 3: Wild Hunt decomposition](../games/s-z/the-witcher-3-wild-hunt.md).
- Novelty: first isolated for `GAME-0205`; forensic preparation and a boss
  defeat remain incomplete until a physical proof is handed to an author.

## OBJ-128 — Complete and retain the first Great Jagras assignment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: post assigned quest `00103`, satisfy its Great Jagras hunt
  condition before time or faint failure, accept the quest result and rewards,
  and regain Astera control with the completion flag retained.
- Includes: the fixed no-capture `The Great Jagras Hunt` slay route in Monster
  Hunter: World through result-screen settlement and hub return.
- Excludes: the lethal hit alone; optional smithy spending; another weapon or
  capture packet; later assigned quests; an expedition defeat with no quest.
- Parameters: predecessor, quest, target, completion form, clock, faints,
  result, materials, zenny, completion flag and returned control.
- Evidence: [Monster Hunter: World decomposition](../games/m-r/monster-hunter-world.md).
- Novelty: first isolated for `GAME-0207`; one evidence-led migrating hunt
  closes only after its discrete result economy and authored assignment flag
  persist at hub control.

## OBJ-129 — Complete and retain The Highway Heist delivery

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete the ordered carrier catch-up, House Enforcer wreck and
  approach stages, take fixed direct control of the stolen Regera, deliver it
  to Airfield 73 and reach retained mission and Chapter 2 success.
- Includes: the fixed Easy, automatic, `LV180` Story replay of `The Highway
  Heist` in Need for Speed Payback.
- Excludes: reaching the truck alone; entering the Regera without delivery;
  another Race or police event; all-campaign completion; Online results.
- Parameters: mission, entry car, carrier, wreck stages, approach gates,
  target vehicle, destination, failure, completion, chapter flag and return.
- Evidence: [Need for Speed Payback decomposition](../games/m-r/need-for-speed-payback.md).
- Novelty: first isolated for `GAME-0208`; counted vehicle combat and authored
  control handoff remain intermediate to a later retained stolen-car delivery.

## OBJ-130 — Complete War Ruse — Peace and return to the campaign

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: satisfy the ordered Peace instructions for settlement economy,
  regiment, repair, ferry colony, guarded ownership, mercenary breach, Academy
  and final Town Hall interaction, then reach mission-complete settlement and
  retained return to the campaign screen.
- Includes: Cossacks 3 Tutorial campaign mission `War Ruse — Peace` on Normal.
- Excludes: destroying the enemy barracks without the final instruction; the
  combat-only `War` tutorial; a historical campaign mission; Random Map victory.
- Parameters: build, difficulty, mission, objective flags, settlement state,
  regiment, ferry, capture lesson, barracks, Academy, Town Hall and return state.
- Evidence: [Cossacks 3 decomposition](../games/a-f/cossacks-3.md).
- Novelty: first isolated for `GAME-0209`; one authored RTS tutorial requires
  economy, transport and breach lessons to settle before campaign return.

## OBJ-131 — Win one Standard Battle for the allied tank team

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: make the allied team complete enemy-base capture or destroy every
  opposing vehicle before the enemy team does either and before the battle
  limit settles a draw.
- Includes: one ordinary World of Tanks Standard Battle in the scoped MS-1.
- Excludes: personal damage, kills, experience or credits; surviving one's own
  tank as a mandatory condition; other Random Battle types or event modes.
- Parameters: teams, bases, capture, surviving vehicles, battle limit, victory,
  defeat and draw.
- Evidence: [World of Tanks decomposition](../games/s-z/world-of-tanks.md).
- Novelty: first isolated for `GAME-0211`; the same symmetric tank-team contest
  admits either full vehicle elimination or opposing-base capture, with a
  non-winning timed draw as the third result.

## OBJ-132 — Complete five taxi fares and survive the resulting escape

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: settle every fare in the fixed five-passenger Story chain, then
  survive the authored vehicle-to-foot attack and enter the designated safe
  location so the mission-complete transition persists.
- Includes: Mafia (2002) Chapter 2 `The Running Man` through entry into
  Salieri's Bar and Story advancement.
- Excludes: one successful fare; Free Ride taxi income; reaching the final
  street without entering the bar; defeating the attackers; completing the
  whole campaign.
- Parameters: fare set, settlement count, transition, attackers, escape route,
  protagonist health, safe location, mission completion and retained Story flag.
- Evidence: [Mafia (2002) decomposition](../games/m-r/mafia-2002.md).
- Novelty: first isolated for `GAME-0214`; a finite service sequence is a
  prerequisite for a compulsory real-time survival phase whose safe-location
  settlement supplies the only positive terminal.

## OBJ-133 — Finish one official track and retain its timed medal evaluation

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: drive the dedicated car through every required waypoint of one
  identified official track in order, cross its valid finish and reach one
  retained elapsed result with the corresponding fixed medal evaluation.
- Includes: the first valid Starter Access Solo finish of Trackmania official
  `Summer 2026 - 01`, UID `buNzfsVlp2NF2oWtHM3729dEylg`.
- Excludes: merely crossing one checkpoint; earning a particular medal as a
  mandatory completion gate; maximising leaderboard rank; repeating the track
  to optimise a personal best; completing the full seasonal campaign.
- Parameters: official track identity, vehicle, ordered waypoints, valid
  finish, elapsed result, fixed medal thresholds, retained evaluation and
  first-result boundary.
- Evidence: [Trackmania decomposition](../games/s-z/trackmania.md).
- Novelty: first isolated for `GAME-0216`; unlike Road Master's soft-body
  mission terminal, this exact positive boundary ends at one official map's
  retained result plus a fixed medal class while a no-medal valid finish still
  counts as completion.
