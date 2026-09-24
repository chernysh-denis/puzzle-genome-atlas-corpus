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
- Additional support: [Duck Hunt decomposition](../games/a-f/duck-hunt.md),
  for target-class points and the first-round no-miss PERFECT bonus alongside
  the separate minimum-hit qualification objective.
- Additional support: [Space Invaders decomposition](../games/s-z/space-invaders.md),
  for optional score maximisation through row values and a mystery-value UFO
  alongside mandatory rack clearance.
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
- Additional support: [DEATH STRANDING DIRECTOR'S CUT decomposition](../games/a-f/death-stranding-directors-cut.md),
  for committing required Smart Drugs to Capital Knot City's fixed terminal.
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
- Additional support: [Resident Evil 2 (2019 remake) decomposition](../games/m-r/resident-evil-2-2019.md),
  for the key-gated street route walked to the police station, whose arrival settles the authored objective and is retained through a reload-verified Main Hall save.
- Additional support: [Resident Evil: Director's Cut decomposition](../games/m-r/resident-evil-directors-cut.md),
  for carrying one key through three locks, crossing the newly connected L Passage and verifying the route through a typewriter save and reload.
- Additional support: [Dead Cells decomposition](../games/a-f/dead-cells.md),
  for reaching the generated biome's Promenade exit, whose interaction settles the biome and whose arrival is the documented retained successor.
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
  enemy in one bounded Slay the Spire combat before player health reaches zero;
  defeating Hollow Knight's one declared opening-route guardian.
- Excludes: surviving a fixed round horizon while hostiles may remain; repelling
  a time-driven multi-wave assault; maximising defeated-enemy score without a
  finite completion set.
- Parameters: required enemy set, incapacitation predicates, reinforcement
  closure, controlled-actor defeat and simultaneous terminal resolution.
- Evidence: [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md)
  and [Tactical Breach Wizards decomposition](../games/s-z/tactical-breach-wizards.md),
  [Shogun Showdown decomposition](../games/s-z/shogun-showdown.md),
  [Slay the Spire decomposition](../games/s-z/slay-the-spire.md), and
  [Hollow Knight decomposition](../games/g-l/hollow-knight.md), and
  [Cuphead decomposition](../games/a-f/cuphead.md).
- Additional support: [Darkest Dungeon decomposition](../games/a-f/darkest-dungeon.md),
  for the corridor Brigand Cutthroat battle and the room battle against the Bloodletter and Fusilier, each cleared before both heroes are lost.
- Additional support: [Space Invaders decomposition](../games/s-z/space-invaders.md),
  for removing every member of the finite 55-invader rack before stock
  exhaustion or overrun.
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
- Additional support: [Battletoads decomposition](../games/a-f/battletoads.md),
  for clearing Ragnarok's Canyon, defeating Tall Walker and crossing into
  Wookie Hole with eligible run state retained.
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
- Includes: Terraria Desktop 1.4.5.8 first-boss-to-Dryad progression boundary.
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

## OBJ-099 — Win the required round count against one fixed opposing fighter

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: in one fixed one-on-one match, earn the declared required
  number of round wins through KO or favourable time-over before the
  opposing fighter does.
- Includes: the scoped Ryu-versus-Luke Street Fighter 6 Versus match at two
  required wins; the scoped Jin-versus-Kazuya TEKKEN 8 offline Versus match
  at the default three required wins.
- Excludes: winning a tournament set of several matches; maximising score or
  rank; eliminating a team; merely winning one round.
- Parameters: selected side, opponent, round terminal, required wins, opponent
  wins and final result.
- Evidence: [Street Fighter 6 decomposition](../games/s-z/street-fighter-6.md).
- Additional support: [TEKKEN 8 decomposition](../games/s-z/tekken-8.md),
  for the third round win by KO or favourable time-over against the fixed
  CPU Kazuya.
- Novelty: first isolated for `GAME-0172`; generalised by
  [`TAXONOMY_CHANGE_047`](../../research/taxonomy-changes/TAXONOMY_CHANGE_047.md)
  so that the required count is a parameter; earlier match objectives use team
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
  disaster and satisfy the declared opening route's equipment, combat,
  interaction and traversal gates until the opening quest completes and the
  persistent character first gains controllable exterior-world state.
- Includes: one fresh Skyrim Special Edition `Unbound` (`MQ101`) escape through
  the Hadvar branch to first retained control outside the Helgen cave with
  `Before the Storm` active; one fresh Fallout 4 base-game escape through Vault
  111 to retained Commonwealth control with `Out of Time` active.
- Excludes: merely entering Helgen Keep; defeating one interior hostile; reaching
  Riverwood; completing a later main quest or the open-world campaign.
- Parameters: character confirmation, disaster, optional escort branch, required gates,
  opening quest, cave exit, successor quest and retained exterior control.
- Evidence: [The Elder Scrolls V: Skyrim Special Edition decomposition](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md).
- Additional support: [Fallout 4 decomposition](../games/a-f/fallout-4.md), for
  the attribute-budget gate, Vault 111 route and reloaded exterior state.
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

## OBJ-120 — Complete a staged progression-key route to a retained capability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: satisfy every required stage of one bounded progression route
  whose accepted terminal is persistent availability of its first capability
  after a separately earned progression key has reached the matching fixture.
- Includes: one current Valheim 0.221.12 solo Normal seed from spawn control to
  mounted Eikthyr Trophy and available power.
- Excludes: settling the guarded encounter while its resulting key remains
  undelivered; receiving other encounter drops; activating an already
  available capability; continuing into later progression stages.
- Parameters: route, wayfinder, entry offering, guarded encounter, guaranteed
  progression key, matching fixture, first retained capability and accepted
  terminal state.
- Evidence: [Valheim decomposition](../games/s-z/valheim.md).
- Novelty: first isolated for `GAME-0197`; encounter settlement and possession
  of its guaranteed key remain intermediate states, while the first retained
  capability is the portable terminal.

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

## OBJ-124 — Breach secured storage, secure required valuables and escape

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one bounded heist contract by breaching the declared
  secured storage, converting at least the contract minimum into spatially
  secured valuables and occupying the available escape so success and payout
  settle.
- Includes: one Normal Offline PAYDAY 2 Bank Heist: Cash requiring one secured
  money bag before escape; one Normal Solo PAYDAY 3 Road Rage requiring five
  secured rare-earth bags before escape.
- Excludes: securing every optional bag; maximising experience; a stealth-only
  requirement; later Crime.net, skill or Infamy progression.
- Parameters: contract, secured-storage fixture, breach state, loot class,
  minimum count, secured count, escape region, crew state, success and payout.
- Evidence: [PAYDAY 2 decomposition](../games/m-r/payday-2.md) and
  [PAYDAY 3 decomposition](../games/m-r/payday-3.md).
- Novelty: first isolated for `GAME-0201`; an interruptible access process,
  embodied value transport and spatial departure form one conjunctive terminal.

## OBJ-125 — Complete a bounded survival route through a location-bound signal

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: traverse the required bounded survival route, obtain or preserve
  a usable carried signal item and activate it while alive in the declared
  terminal region so the authored positive result settles.
- Includes: standard PEAK solo on the scoped 2026-08-30 daily island interval;
  The Long Dark's standard `Hopeless Rescue` summit-to-Lighthouse Challenge.
- Excludes: merely reaching an intermediate or terminal location; signalling in
  the wrong region; a different alternate ending; starting another attempt.
- Parameters: ruleset identity, difficulty, route progress, life state, terminal
  region, signal item, activation, response, report and success result.
- Evidence: [PEAK decomposition](../games/m-r/peak.md) and
  [The Long Dark decomposition](../games/s-z/the-long-dark.md).
- Novelty: first isolated for `GAME-0203`; a generated vertical route must
  preserve one explicit signal action beyond arrival to turn survival into
  rescue. The route-neutral generalisation was accepted in
  [`TAXONOMY_CHANGE_051`](../../research/taxonomy-changes/TAXONOMY_CHANGE_051.md).

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

## OBJ-134 — Win one rival race and retain its reward

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete the required ordered course of one finite race against
  autonomous rivals, cross its valid finish in first place and reach a
  persistent event result with the disclosed completion reward retained.
- Includes: the stock Honda Civic Si packet for Need for Speed Underground
  Race 1 at Olympic Square, Easy, automatic transmission and `375` Bank; the
  stock Supra packet for Forza Horizon 5's Horizon Mexico Circuit, Average
  Drivatars and retained first-place result.
- Excludes: a valid solo time-trial finish without a rival-victory predicate;
  a race where any classified place satisfies the packet; a championship or
  multi-event progression gate; a race whose result remains unsettled until a
  later pursuit, escape or garage gate; a delivery mission that merely uses a
  car; the full career.
- Parameters: event, route, lap count, rivals, finish place, difficulty,
  reward, completion flag, career state and returned control.
- Evidence: [Need for Speed Underground decomposition](../games/m-r/need-for-speed-underground.md)
  and [Forza Horizon 5 decomposition](../games/a-f/forza-horizon-5.md).
- Novelty: first isolated for `GAME-0217` and generalised under
  `TAXONOMY_CHANGE_017`; the reusable boundary is the finite rival-race win
  plus retained result/reward, while event identity, vehicle, laps,
  difficulty and reward amount remain parameters.

## OBJ-135 — Reach stock map-time settlement with the team-round score

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: complete the ordinary server packet when its shipped finite map
  time invokes the map-cycle boundary and evaluate the retained team-round
  score as one side's lead or a tie.
- Includes: Counter-Strike 1.6 on stock `de_dust2` with the shipped dedicated
  `mp_timelimit 20`, no win/max-round limit and its final T/CT round score.
- Excludes: winning a fixed regulation match by a clinching round threshold;
  personal kill score; an invented tournament configuration; an unbounded
  community server session; a tie-breaking overtime not present in the packet.
- Parameters: map, time limit, teams, round scores, cycle trigger, lead/tie
  classification and result visibility.
- Evidence: [Counter-Strike decomposition](../games/a-f/counter-strike.md).
- Novelty: first isolated for `GAME-0218`; unlike `OBJ-071`, this terminal is
  the current package's time-driven map cycle, not a fixed round regulation,
  halftime, clinch or overtime policy.

## OBJ-136 — Complete the first class quest and retain Warrior

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete `Path of Destiny - Beginning`, reach level 20, confirm
  Warrior and regain control with the quest and first class transfer retained
  on the same fixed Lineage II Live server character.
- Includes: the fresh Human Fighter-to-Warrior Chronos packet.
- Excludes: reaching level 20 without transfer; another destination class; a
  later transfer; completing all levelling or the whole MMO history.
- Parameters: server, character, quest, level threshold, selected first class,
  completion flag and returned controllable state.
- Evidence: [Lineage II decomposition](../games/g-l/lineage-ii.md).
- Novelty: first isolated for `GAME-0219`; the terminal requires both authored
  quest settlement and the resulting retained class identity.

## OBJ-137 — Complete Exile's Reach and retain the Dragon Isles hand-in

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete the full current Alliance Exile's Reach main chain and
  Darkmaul Citadel, reach the Dragon Isles docks and hand `An End to Beginnings`
  to Kalecgos with the same fresh Human Warrior's level, abilities, quest state
  and equipment retained.
- Includes: the current US Retail `12.1.0.69587` full-tutorial packet without
  Housing Skip.
- Excludes: reaching level 10 alone; skipping the island; defeating only the
  first dungeon boss; arriving at the docks without hand-in; subsequent
  Dragonflight quests or the complete live service.
- Parameters: branch, faction, race, class, required quests, dungeon bosses,
  destination, final quest, recipient, completion flag and retained state.
- Evidence: [World of Warcraft decomposition](../games/s-z/world-of-warcraft.md).
- Novelty: first isolated for `GAME-0221`; an assisted fresh-character
  tutorial dungeon is only the penultimate gate before a current cross-region
  quest hand-in writes the persistent terminal.

## OBJ-138 — Complete the corrected first Gunslinger episode

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: survive the ordered first Story episode, resolve its apparent
  stable duel, continue through the compulsory narrator correction and enter
  the stable again so the corrected recognition scene settles episode
  completion.
- Includes: `Once Upon a Time in Stinking Springs` on Normal from clean Story
  entry through the second stable entry after `Get the horses... this time for
  real`.
- Excludes: the first apparent duel win; farmhouse clearance; a combo target;
  every later episode; whole-Story completion; Arcade or Duel mode result.
- Parameters: episode, difficulty, ordered gates, apparent outcome, correction,
  replacement objective, repeated stable entry and completion transition.
- Evidence: [Call of Juarez: Gunslinger decomposition](../games/a-f/call-of-juarez-gunslinger.md).
- Novelty: first isolated for `GAME-0222`; success explicitly requires playing
  beyond a revoked outcome into the narrator's mechanically corrected account.

## OBJ-139 — Clear, claim and close one Aion Classic tutorial

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: in the character's only admitted tutorial run, complete all three
  typed defeat counts, claim every spawned Mystic Cube and both objective reward
  boxes, then leave through the Daeva of Time and retain the rewards outside.
- Includes: 20 Invading Balaurs, five Special Forces, Fiery Rantak, Roaring
  Dahakar and Abyssal Karmatan in `Boundary of Light and Darkness`.
- Excludes: leaving early; one complete counter; an unclaimed cube or reward
  box; later open-world progression; repeating on another character.
- Parameters: three target classes, required counts, three cubes, two reward
  boxes, exit actor, retained items and closed tutorial flag.
- Evidence: [Aion Classic decomposition](../games/a-f/aion-classic.md).
- Novelty: first isolated for `GAME-0223`; success joins typed combat quotas and
  a complete reward envelope before an irreversible personal exit.

## OBJ-140 — Complete onboarding and stop at scenario selection

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: complete the current mandatory new-player experience on the
  fixed fresh account, retain its `Distant Memory` grant and regain control at
  the scenario/server selection surface without entering a scenario.
- Includes: one new Once Human Meta-Human completing the Version `3.0.4`
  pre-scenario tutorial packet.
- Excludes: partial instruction completion; veteran skip; the veteran mail
  route; selecting Manibus; wilderness entry; one Monolith; full service play.
- Parameters: account branch, character, tutorial predicates, completion flag,
  retained grant, selection surface and excluded scenario entry.
- Evidence: [Once Human decomposition](../games/m-r/once-human.md).
- Novelty: first isolated for `GAME-0224`; the exact success state is authority
  to choose a later world ruleset, not entry into or completion of that world.

## OBJ-141 — Complete Form the Vanguard and retain its mission medal

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: satisfy every required authored objective in the fixed first
  Rebel story mission, destroy its final required Imperial formation, reach the
  debrief and retain the unconditional `Mission Complete` medal.
- Includes: one Pilot-difficulty run of `Form the Vanguard` in the fixed X-wing.
- Excludes: optional performance medals; Mission 2; campaign completion;
  multiplayer victory; replay optimisation; cosmetic or rank rewards.
- Parameters: mission, ordered objectives, final formation, completion state,
  debrief, mission-complete medal, retained record and optional medals.
- Evidence: [STAR WARS: Squadrons decomposition](../games/s-z/star-wars-squadrons.md).
- Novelty: first isolated for `GAME-0225`; success is one bounded authored
  cockpit mission and its guaranteed retained medal, not the wider campaign.

## OBJ-142 — Complete a forced-loss driving prologue into retained campaign control

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: enter one authored rival-driving event, allow its unavoidable
  mechanical failure and loss to settle, acquire the declared replacement
  vehicle and reach the first retained ordinary campaign-control checkpoint.
- Includes: Need for Speed: Most Wanted (2005)'s Razor prologue from the fixed
  story-race start through Lexus IS300 purchase and safe-house autosave.
- Excludes: beating the rival; stopping at the breakdown or arrest; an ordinary
  lower-place finish; later Blacklist progress; the complete campaign.
- Parameters: event, rival, failure trigger, removed vehicle, cash grant,
  replacement vehicle, destination, autosave and retained campaign state.
- Evidence: [Need for Speed: Most Wanted (2005) decomposition](../games/m-r/need-for-speed-most-wanted-2005.md).
- Novelty: first isolated for `GAME-0226`; the accepted terminal lies beyond a
  mandatory competitive loss and requires a replacement-vehicle checkpoint.

## OBJ-143 — Repair disabled transport and retain the first guided destination

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: satisfy taught survival, gathering, production and technology
  dependencies that restore disabled personal transport, directly travel to
  the first newly guided destination, complete its required interaction and
  retain progress through an explicit save/reload boundary.
- Includes: No Man's Sky Awakenings from fresh Normal start through repaired
  starter-starship flight, first abandoned-building terminal and verified
  post-terminal ship-exit save.
- Excludes: stopping at repair, launch or arrival; an arbitrary sandbox save;
  base construction; later main-story progress; completing an open world.
- Parameters: tutorial, survival requirements, transport, repair chain,
  destination, interaction, save trigger, reload and successor mission state.
- Evidence: [No Man's Sky decomposition](../games/m-r/no-mans-sky.md).
- Novelty: first isolated for `GAME-0229`; restored transport changes traversal
  scale, but completion requires a remote interaction and verified retention.

## OBJ-144 — Purge mission-critical data and escape into a retained successor

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: satisfy an ordered infiltration's access gates, delete the
  required hostile data, survive the authored escape and retain access to the
  named successor mission after a clean exit and relaunch.
- Includes: The Cleaner from directly controlled ID10 through Iden's message
  purge and airlock escape to retained The Battle of Endor access.
- Excludes: reaching the data terminal without deleting its target; one
  transient checkpoint; later campaign completion; multiplayer match victory.
- Parameters: infiltration, access gates, data target, purge interaction,
  escape route, completion transition, successor, save state and relaunch check.
- Evidence: [STAR WARS Battlefront II (2017) decomposition](../games/s-z/star-wars-battlefront-ii-2017.md).
- Novelty: first isolated for `GAME-0230`; a role-changing infiltration closes
  only when purge and escape become retained authority for the next mission.

## OBJ-145 — Redeem survival onboarding and retain its service-route reward

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: satisfy and redeem every requirement in one bounded survival
  onboarding group, follow the destination quest created by its group reward,
  settle the marked service location and retain the explicit route reward.
- Includes: the current 7 Days to Die `Basics of Survival` group through
  `Journey to Settlement`, Stone Shovel credit and verification reload.
- Excludes: green but unredeemed rows; stopping when the trader marker appears;
  trading or accepting a first job; surviving an arbitrary number of days;
  completing the wider open world.
- Parameters: challenge group, mandatory rows, row claims, issued route,
  service destination, spatial objective, credited reward, save and reload.
- Evidence: [7 Days to Die decomposition](../games/0-9/7-days-to-die.md).
- Novelty: first isolated for `GAME-0233`; a claimed tutorial checklist creates
  a world-space service route whose own reward supplies the positive terminal.

## OBJ-146 — Complete one multi-event driving stage into retained route rank

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: satisfy every required rival-passing and ordered-route result in
  one authored driving stage, retain the resulting cumulative route rank and
  expose its named successor stage after a persistence check.
- Includes: Need for Speed: The Run Stage 1 West Coast from rank 211 through
  three required events to retained rank 195 and Stage 2 access.
- Excludes: winning the complete cross-country campaign; one isolated race
  victory; stopping after a checkpoint or intermediate event; leaderboard rank;
  a later replay for improved stage time.
- Parameters: stage, ordered event set, event targets, initial rank, passed
  rivals, terminal rank, settlement, successor unlock and retained state.
- Evidence: [Need for Speed: The Run decomposition](../games/m-r/need-for-speed-the-run.md).
- Novelty: first isolated for `GAME-0235`; several driving-event results reduce
  one campaign rank before a stage-level successor becomes the terminal.

## OBJ-147 — Clear one occupied site and retain its converted local services

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: defeat every member of one closed required hostile set, complete
  the site's immediate authored terminal and preserve its converted allied
  ownership plus declared local services or successor access after relaunch.
- Includes: clearing Far Cry 3's scoped first outpost, entering its main
  building and retaining Rakyat control, fast travel, vendor access and the
  next story mission.
- Excludes: one kill while hostiles remain; clearing a room with no persistent
  world change; temporary match-zone control; optional loot collection; winning
  every site or completing the whole campaign.
- Parameters: site, hostile set, required local interaction, owner, service set,
  successor, persistence check and failure state.
- Evidence: [Far Cry 3 decomposition](../games/a-f/far-cry-3.md).
- Novelty: first isolated for `GAME-0236`; the positive terminal combines
  closed hostile clearance with retained local ownership and operational access.

## OBJ-148 — Complete one recovery quest and retain its successor

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: restore required actors' immediate condition, complete one
  bounded authored recovery quest's field, dialogue and production sequence,
  and retain its named successor objective after a persistence check.
- Includes: Kingdom Come: Deliverance II's scoped `Fortuna` route through
  treatment, herb collection, manual brew, hand-in, sleep and load-verified
  `Laboratores` successor.
- Excludes: treating one condition without quest settlement; arbitrary open-
  world survival; whole-campaign completion; a transient successor cutscene.
- Parameters: actors, condition, quest, sequence, product, hand-in, completion,
  successor, save and verification load.
- Evidence: [Kingdom Come: Deliverance II decomposition](../games/g-l/kingdom-come-deliverance-ii.md).
- Novelty: first isolated for `GAME-0240`; recovery and a manually produced
  quest item jointly close one packet into retained successor authority.

## OBJ-149 — Finish one exhibition with more points than the opponent

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete every required period of one bounded head-to-head
  exhibition and finish its final unequal score with the controlled side
  holding more legally awarded points than the opposing side.
- Includes: winning the scoped NBA 2K26 Play Now match after regulation or any
  required overtime.
- Excludes: winning a season or series; accumulating account rewards; ending
  regulation tied; stopping after one possession or quarter; a named matchup or
  exact score as a gene.
- Parameters: controlled side, opponent, periods, points, regulation terminal,
  overtime predicate, final score, win and loss.
- Evidence: [NBA 2K26 decomposition](../games/m-r/nba-2k26.md).
- Novelty: first isolated for `GAME-0241`; multiple point values accumulate
  across four periods and a tie obligatorily extends the same exhibition.

## OBJ-150 — Meet one disclosed race-place threshold and retain progression

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one finite ordered race against autonomous rivals,
  finish within its disclosed accepted set of places and reach a persistent
  result with the event's progression marker and disclosed rewards retained.
- Includes: finishing third or better in the scoped Asphalt Legends Career
  Classic race and retaining its Career Flag and displayed rewards.
- Excludes: a first-place-only race; a solo medal time; finishing outside the
  accepted set; a result not retained until a later escape; the full Career.
- Parameters: event, route, rivals, disclosed place threshold, final place,
  progression marker, rewards, completion state and returned control.
- Evidence: [Asphalt Legends decomposition](../games/a-f/asphalt-legends.md).
- Novelty: first isolated for `GAME-0242`; success is an explicitly disclosed
  set of classified places rather than only overall victory or mere finish.

## OBJ-151 — Complete one investigative episode into retained successor access

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: satisfy one authored investigative episode's required evidence,
  custody or combat and protected-actor gates, reach its discrete evaluated
  settlement and retain both recorded progress and successor access.
- Includes: completing Battlefield Hardline Episode 1 after its mandatory
  evidence, suspect, school and partner-defence sequence.
- Excludes: stopping at one arrest or clue; maximising every optional record;
  finishing the entire campaign; a multiplayer result without episode state.
- Parameters: episode, ordered gates, evidence, custody outcome, combat,
  protected actor, evaluation, completion flag, successor and retention.
- Evidence: [Battlefield Hardline decomposition](../games/a-f/battlefield-hardline.md).
- Novelty: first isolated for `GAME-0243`; investigative evaluation and living
  custody remain part of the required authored episode before successor access.

## OBJ-152 — Classify a night race and voluntarily bank its session reputation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one fixed night race through its valid classified
  finish and reach an eligible refuge with its session reputation retained,
  avoiding or resolving any acquired pursuit before voluntary settlement.
- Includes: the first Hard Stop sprint in Make a Name followed by successful
  safe-house banking in the scoped Need for Speed Heat packet.
- Excludes: requiring first place; requiring a pursuit that did not occur;
  stopping at the finish; capture or wreck as a positive terminal; another race
  or full-career reputation goal.
- Parameters: event, route, classified place, session reputation, notoriety,
  conditional pursuit, evasion, payment, refuge, retained progress and failure.
- Evidence: [Need for Speed Heat decomposition](../games/m-r/need-for-speed-heat.md).
- Novelty: first isolated for `GAME-0244`; a valid race result requires a later
  voluntary reputation settlement without imposing a mandatory chase.

## OBJ-153 — Resolve one authored target and retain post-mission successor control

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete the required information objective and resolve one
  designated mission target through an admitted lethal or non-lethal method,
  return to the mission exit, accept its finite settlement and retain ordinary
  control in the authored successor state.
- Includes: resolving Campbell non-lethally, obtaining the required journal,
  returning to Samuel, accepting Stats and retaining Hound Pits control in
  Dishonored's scoped mission.
- Excludes: reaching the target without resolving it; stopping immediately
  after one target interaction; an optional side objective; completing the
  entire campaign; requiring one branded method in the portable gene boundary.
- Parameters: mission, designated target, admitted methods, required
  information objective, exit, settlement, successor state and persistence.
- Evidence: [Dishonored (2012) decomposition](../games/a-f/dishonored-2012.md).
- Novelty: first isolated for `GAME-0247`; target disposition and required
  information must survive a separate return and evaluated mission boundary
  before the positive terminal is reached.

## OBJ-154 — Resolve a closed target set and retain scored mission settlement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: resolve every member of one declared finite designated-target
  set through admitted mission methods, use an enabled exit and retain a
  terminal report that exposes completion and the attempt's aggregate score or
  rating before another attempt begins.
- Includes: resolving both targets, exiting Paris and accepting Debriefing in
  HITMAN World of Assassination's scoped story mission.
- Excludes: resolving one target while another remains; optional hostile
  clearance; maximising every challenge; an unscored successor transition;
  completing an entire campaign or rotating target series.
- Parameters: mission, target set, accepted resolution methods, member states,
  exit, completion, score, rating, report and retained result.
- Evidence: [HITMAN World of Assassination decomposition](../games/g-l/hitman-world-of-assassination.md).
- Novelty: first isolated for `GAME-0248`; a finite conjunctive target roster
  gates the exit that produces one explicit scored mission terminal.

## OBJ-155 — Complete one authored survival-action segment into retained successor control

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: survive and satisfy the ordered mandatory interactions of one
  bounded authored action chapter or mission, accept its explicit completion
  and save boundary and retain ordinary control in the immediate successor
  segment.
- Includes: completing Chapter 1 and retaining first Chapter 2 control in a
  fresh Standard game of Resident Evil 4; completing Mission 5 and restoring
  first Mission 6 control in Alien: Isolation's scoped Story Mode packet.
- Excludes: stopping at an intermediate autosave; clearing every optional
  hostile or collectible; requiring a particular combat route; completing the
  whole campaign; replaying the chapter for rank.
- Parameters: chapter, ordered mandatory interactions, survival state, final
  interaction, completion display, save boundary, successor and retention.
- Evidence: [Resident Evil 4 decomposition](../games/m-r/resident-evil-4-2023.md)
  and [Alien: Isolation decomposition](../games/a-f/alien-isolation.md).
- Additional support: [Warcraft III: Reign of Chaos decomposition](../games/s-z/warcraft-iii-reign-of-chaos.md),
  for satisfying the ordered mandatory command tutorial, reaching the Prophet
  beacon and exposing `Departures` without entering the successor chapter.
- Novelty: first isolated for `GAME-0249`; the positive terminal requires an
  authored chapter boundary and retained successor control without importing a
  boss sequence, mission-conduct score or full-campaign ending.

## OBJ-156 — Escape a boss-gated region chain before terminal health loss

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: carry one continuous multi-region attempt through its mandatory
  guardians and final escape settlement before persistent health reaches its
  terminal threshold, then accept the rules-defined return to the persistent hub.
- Includes: one first-save Hades escape attempt, with first retained House
  control after the surface visit as success and retained House control after
  ordinary death as the bounded failure settlement.
- Excludes: clearing one chamber or regional guardian; stopping at an autosave;
  repeated attempts; completing the full story; arbitrary survival duration.
- Parameters: attempt entry, region sequence, guardians, health threshold,
  revival state, final escape, success transition, failure transition and hub.
- Evidence: [Hades decomposition](../games/g-l/hades.md).
- Novelty: first isolated for `GAME-0251`; prior run objectives end at a named
  boss, clock or voluntary retreat rather than sharing one progression-retaining
  hub locus after both final escape and terminal defeat.

## OBJ-157 — Resolve one investigated live incident into a retained branch endpoint

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: investigate one bounded authored incident, commit its admitted
  live responses or interventions, reach a discrete endpoint for the protected
  and controlled actors and retain the traversed result for later inspection.
- Includes: resolving Detroit: Become Human's opening hostage incident and
  retaining its completed flowchart endpoint; the reproducible positive trace
  releases the protected actor and preserves the negotiator.
- Excludes: collecting every branch; completing a whole campaign; stopping at
  rooftop entry; a generic dialogue scene with no protected-actor result;
  replaying the chapter until every endpoint is visible.
- Parameters: incident, evidence threshold, controlled actor, protected actor,
  response path, intervention, endpoint, success predicate and retained record.
- Evidence: [Detroit: Become Human decomposition](../games/a-f/detroit-become-human.md).
- Novelty: first isolated for `GAME-0252`; the objective binds authored
  investigation and live negotiation to one retained branch result without
  extending to the complete narrative.

## OBJ-158 — Settle one authored dialogue-gated episode into retained successor access

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete the required interactions of one bounded authored
  episode whose gates are satisfied through conversation, examination and
  attribute checks rather than through physical resolution, then retain its
  recorded progress and successor access across a persistence check.
- Includes: completing the opening episode and reaching the first retained
  partner encounter in Disco Elysium - The Final Cut.
- Excludes: defeating a mandatory guardian; clearing a designated target set;
  reaching an authored narrative ending; filling every slot of a structured
  evidence account.
- Parameters: episode boundary, required interactions, gate types, recorded
  progress and the successor state that must survive reloading.
- Evidence: [Disco Elysium - The Final Cut decomposition](../games/a-f/disco-elysium-the-final-cut.md).
- Novelty: first isolated for `GAME-0264`; the settlement is produced entirely
  by talking, looking and rolling, so no physical resolution appears anywhere
  in the completion condition.

## OBJ-159 — Survive a fixed wave schedule with the defence stock above zero

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete the attempt by carrying a shared defence stock through
  every round of a finite authored wave schedule to its declared final round;
  hostiles that escape debit that stock without ending the attempt, and the
  attempt fails only when the stock is exhausted before the schedule ends.
- Includes: clearing the declared final round of the Easy standard schedule on
  a beginner map with lives remaining in Bloons TD 6.
- Excludes: neutralising every member of a finite assault force as the
  completion predicate; surviving until a clock reaches a stated time; escaping
  a chain of regions before health is lost; defeating a mandatory guardian.
- Parameters: schedule length, final round index, starting stock, per-escape
  debit and the stock value that ends the attempt.
- Evidence: [Bloons TD 6 decomposition](../games/a-f/bloons-td-6.md).
- Novelty: first isolated for `GAME-0265`; completion is measured by outlasting
  a known finite schedule rather than by destroying everything, so a
  deliberately conceded escape can be a legitimate cost of surviving it.

## OBJ-160 — Fill the declared quota, then board the departing transport

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete the attempt by filling the mission's declared collection
  quota, which alone enables the departure call, and then reaching and boarding
  the arriving transport before its declared waiting interval expires; failing
  to board leaves the attempt unsuccessful even though the quota was filled.
- Includes: depositing the required Morkite, pressing the extraction button and
  boarding the drop pod before it departs in Deep Rock Galactic's bounded solo
  Mining Expedition.
- Excludes: a mission whose success is owned by the main objective alone, with
  extraction only a separable departure bonus; surviving a fixed wave schedule;
  clearing a designated target set; reaching an authored narrative ending.
- Parameters: quota identity and size, departure trigger, transport arrival,
  waiting interval, boarding zone and the survivors required for success.
- Evidence: [Deep Rock Galactic decomposition](../games/a-f/deep-rock-galactic.md).
- Novelty: first isolated for `GAME-0266`; the collected objective is worthless
  unless it is physically carried out, so the run's last decision is when to
  stop gathering and start leaving.

## OBJ-161 — Reach and retain a closed orbit about the declared body

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Limited`
- Confidence: `Medium`
- Definition: complete the attempt by manoeuvring a craft the player assembled
  until its projected path closes into a repeating orbit about the declared
  attracting body with its lowest point above that body's atmospheric
  boundary, then retain that state through a persistence check.
- Includes: reaching a stable closed orbit about the home body and confirming
  it survives a save and reload during Kerbal Space Program's bounded Sandbox
  orbit task.
- Excludes: reaching a named location on a surface; completing a delivery
  quota; surviving a wave schedule; defeating a mandatory guardian; landing on
  a runway.
- Parameters: body, atmospheric boundary, closure test, lowest-point margin and
  the state that must survive the persistence check.
- Evidence: [Kerbal Space Program decomposition](../games/g-l/kerbal-space-program.md).
- Novelty: first isolated for `GAME-0267`; success is a property of a
  trajectory rather than of a place or an opponent, so the attempt ends when
  the craft's own motion has been made self-sustaining.

## OBJ-162 — Settle one encounter without defeating anyone and retain it

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Limited`
- Confidence: `Medium`
- Definition: complete the attempt by bringing one bounded encounter to its
  close entirely through non-damaging interactions and a release, with no
  opponent defeated at any point in the run, then retain that state through a
  persistence check that shows the defeat count still at zero.
- Includes: closing one ordinary monster encounter through interaction and
  release, then saving and reloading with nothing defeated, in Undertale's
  bounded opening route.
- Excludes: incapacitating every member of a finite hostile set; resolving a
  designated target through an admitted lethal or non-lethal method; surviving
  a wave schedule; reaching an authored narrative ending.
- Parameters: encounter identity, permitted interactions, release condition,
  the count that must stay at zero and the state that must survive the check.
- Evidence: [Undertale decomposition](../games/s-z/undertale.md).
- Novelty: first isolated for `GAME-0268`; success is defined by a
  capability deliberately not used, so the objective is satisfied by what the
  run's record does not contain.

## OBJ-163 — Return a voyage's catch to market before the day's night boundary

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete the attempt by taking material from the field, stowing it
  legally in the carried grid, bringing it back to the fixed buyer and selling it
  in its undegraded condition, with the whole round trip finished before the
  world clock crosses its declared night boundary; the objective is the
  round trip rather than the quantity taken.
- Includes: catching, stowing and selling a fresh catch at Greater Marrow and
  meeting the declared dockside characters before nightfall in DREDGE's bounded
  first-day route.
- Excludes: filling a declared delivery quota; reaching a named location;
  surviving a wave schedule; maximising an accumulated score; completing one
  employer-supplied cargo contract.
- Parameters: field material, buyer, condition bands, the declared boundary hour
  and the characters the commission names.
- Evidence: [DREDGE decomposition](../games/a-f/dredge.md).
- Novelty: first isolated for `GAME-0269`; success is a completed circuit rather
  than an amount, so the run's decisive moment is choosing when to stop taking.

## OBJ-164 — Clear one region's exit event and carry the run into the next

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete the attempt by satisfying the current region's declared
  exit event, taking its closeout and arriving in the next region with eligible
  accumulated run state carried forward; the objective is the transition
  itself rather than any amount collected, defeated or survived before it.
- Includes: charging the Teleporter, defeating its boss and taking the opened
  exit into the second environment with the run's item set and rising
  coefficient retained, in Risk of Rain 2's bounded first-environment route;
  contacting the World 1-1 flagpole, entering the castle and reaching World
  1-2 with eligible run state retained in original Super Mario Bros.
- Excludes: surviving a declared duration; clearing every hostile in the region;
  reaching a named location that needs no event; completing a delivery quota;
  reaching an authored narrative ending.
- Parameters: region, exit event, closeout, successor, state carried forward,
  reset state and any escalation the transition itself applies.
- Evidence: [Risk of Rain 2 decomposition](../games/m-r/risk-of-rain-2.md) and
  [Super Mario Bros. decomposition](../games/s-z/super-mario-bros.md).
- Novelty: first isolated for `GAME-0270`; leaving is the goal and staying is the
  temptation, so the objective is defined against the enrichment the player wants
  to keep doing.

## OBJ-165 — Fill one region's progress measure and retain the opened succession

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: raise one bounded region's retained progress measure to its
  declared threshold through any mix of qualifying activities, and reach the
  persistent state in which the region counts as resolved and its authored
  successors are selectable.
- Includes: liberating Far Cry 5's tutorial island by filling its resistance
  measure and retaining the three offered successor regions.
- Excludes: clearing one occupied site and retaining its own services;
  completing one event or wave schedule; reaching a region boundary through an
  ordered mission list; a personal level threshold.
- Parameters: the required total, the qualifying activity classes, the region's
  identity and the number of successors.
- Evidence: [Far Cry 5 decomposition](../games/a-f/far-cry-5.md).
- Novelty: first isolated for `GAME-0271`.

## OBJ-166 — Eliminate the declared hostile set and retain the next mission

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one bounded mission by removing every member of the
  hostile set the mission declares, then reach the persistent state in which the
  mission is settled and the campaign's next mission is retained as selectable.
- Includes: destroying the opposing force in the opening GDI mission of Command
  & Conquer Remastered Collection's bounded route and continuing the campaign.
- Excludes: repelling an assault that a defence must survive; clearing an
  occupied site and retaining its local services; reaching a designated
  location; surviving a declared duration; defeating one named guardian.
- Parameters: the hostile set's composition, the map, the debrief content and
  how many successors open.
- Evidence: [Command & Conquer Remastered Collection decomposition](../games/a-f/command-and-conquer-remastered-collection.md).
- Novelty: first isolated for `GAME-0275`.

## OBJ-167 — Complete one cycle from excursion stock to its service settlement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Limited`
- Confidence: `Medium`
- Definition: complete one bounded cycle by taking a single excursion's stock
  into a second, different activity that consumes it, settling that activity's
  own bounded result, and reaching the persistent state in which the cycle is
  recorded and the next one is available.
- Includes: completing DAVE THE DIVER's required second tutorial dive with the
  declared catch, using that stock through the first evening service, accepting
  its sales report and grade, and reaching the following play day.
- Excludes: returning a catch to a market for coin; securing gathered resources
  at a base; completing one activity whose result is only a score; a day
  boundary with no second activity consuming the first's output; requiring a
  longer campaign mission that the scoped cycle does not complete.
- Parameters: the two activities, excursion quota, what the stock maps to, the
  second activity's bound, terminal report and what the settlement retains.
- Evidence: [DAVE THE DIVER decomposition](../games/a-f/dave-the-diver.md).
- Novelty: first isolated for `GAME-0278`.

## OBJ-168 — Reach the declared state on every eligible surface and settle

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one bounded task by bringing every eligible surface to
  its declared target state, then reach the persistent settlement in which the
  task's payment or credit is recorded and the surrounding progression returns.
- Includes: completing PowerWash Simulator's bounded first Career job and
  retaining its settled payment.
- Excludes: completing an authored room task set; revealing every non-hazard
  position; surviving a declared duration; clearing a hostile set; a partial
  coverage contract.
- Parameters: the task subject, accepted per-surface tolerance, settlement
  value, successor availability and persistence check.
- Evidence: [PowerWash Simulator decomposition](../games/m-r/powerwash-simulator.md).
- Novelty: first isolated for `GAME-0279`; the objective is measured
  completeness itself, with no clock, failure state or consumable beside it.

## OBJ-169 — Cross the first of a continuing subject's declared progression thresholds

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Limited`
- Confidence: `Medium`
- Definition: raise one continuing subject's retained progression measure to
  the first of its declared thresholds and reach the persistent state in which
  that threshold has settled and the capabilities it releases stay available,
  while the subject itself is not completed and its same measure keeps
  accumulating toward the later thresholds that remain outside the packet.
- Includes: reaching the first progression milestone of a new Cities:
  Skylines II city and keeping what that milestone releases.
- Excludes: a bounded region that counts as resolved once its measure is
  filled, with authored successors then selectable (`OBJ-165`); an open-ended
  subject with no declared threshold (`OBJ-053`); the final qualification of an
  ordered milestone chain (`OBJ-056`); one finite ordered event judged by
  finishing place (`OBJ-150`); a measure filled against an opposed failure
  track (`OBJ-059`); producing one element that meets a target value
  (`OBJ-001`); a rank or membership earned by named designated events
  (`OBJ-088`, `OBJ-098`).
- Parameters: the subject, the measure and its first threshold, the qualifying
  sources, the released capabilities, any one-time award, the number of later
  thresholds and whether a failure terminal exists beside it.
- Evidence: [Cities: Skylines II decomposition](../games/a-f/cities-skylines-ii.md);
  the publisher establishes that a milestone is reached with the progression
  measure and releases further capability, while the first milestone's exact
  threshold and award remain run-time parameters recorded in that record.
- Novelty: first isolated for `GAME-0284`; the subject is neither completed nor
  resolved at the terminal, and the same measure continues past it, which
  separates this boundary from every retained-successor objective whose subject
  finishes when its measure fills.

## OBJ-170 — Establish one off-origin colony and regain continuing polity control

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete the required knowledge, territorial and transport chain
  for one eligible habitat away from the polity's origin and reach the retained
  successor in which its first new settlement is established while the larger
  polity remains available for continued control.
- Includes: Stellaris from fresh United Nations of Earth control through one
  surveyed and claimed system to its first established colony.
- Excludes: winning a whole campaign; reaching a later colony-count threshold;
  founding an instant territory-claiming city; improving the new settlement
  after establishment.
- Parameters: polity, origin, target habitat, prerequisite chain, establishment
  threshold, retained successor, calendar date and later campaign state.
- Evidence: [Stellaris decomposition](../games/s-z/stellaris.md).
- Novelty: first isolated for `GAME-0287`; the terminal completes one
  off-origin settlement dependency chain but deliberately leaves the polity
  and wider campaign continuing.

## OBJ-171 — Build one survival shelter and retain its saved world state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: gather and commit the required local materials to one freely
  positioned survival-shelter plan, complete it as a usable world fixture and
  accept a manual save there so the current survivor and altered world become a
  retained continuation state.
- Includes: The Forest's bounded fresh Normal start through one completed
  Temporary Shelter and its accepted save interaction.
- Excludes: merely placing an unfinished outline; sleeping without saving;
  requiring the shelter to remain after its one allowed sleep; building a
  permanent base; completing the story or surviving a declared duration.
- Parameters: world start, shelter design, position, material requirements,
  survivor state, completed fixture, save slot, retained snapshot and excluded
  post-save branch.
- Evidence: [The Forest decomposition](../games/s-z/the-forest.md).
- Novelty: first isolated for `GAME-0292`; the constructed object is both the
  bounded material objective and the fixture that creates the retained
  terminal, while its optional one-use sleep remains a destructive branch.

## OBJ-172 — Reach and retain the first restorative route checkpoint

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one fresh authored opening through its required finite
  access items, mandatory guardian and first retained capability, then activate
  the first declared restorative save point so the completed route becomes the
  retained continuation state.
- Includes: Ori and the Will of the Wisps from its unskipped Swallow's Nest
  prologue through the two-Keystone Spirit Gate, repelled Howl and retained
  Spirit Edge to the first used Inkwater Marsh Spirit Well.
- Excludes: stopping at an automatic checkpoint; reaching but not using the
  save point; acquiring the capability without the later retained checkpoint;
  taking optional Double Jump, Regenerate or Shard detours; completing the
  whole campaign.
- Parameters: entry, access-item type and count, barrier, guardian, retained
  capability, direct route, save point, restored resources, saved state and
  verification reload.
- Evidence: [Ori and the Will of the Wisps decomposition](../games/m-r/ori-and-the-will-of-the-wisps.md).
- Novelty: first isolated for `GAME-0293`; the terminal deliberately separates
  dense automatic failure checkpoints from the first player-triggered
  restorative save after the key, guardian and capability chain.

## OBJ-173 — Establish and retain one powered claimed early shelter

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete the opening survival and construction dependency chain,
  claim one eligible territory with a powered ownership core, close an early
  defensive enclosure around its required shelter fixtures and retain that
  altered world as the next continuation state.
- Includes: V Rising's fresh normal private-world opening through one positive-
  Blood-Essence Castle Heart, a shut palisade enclosure, Wooden Coffin, Small
  Chest and active bone-fuelled Mist Brazier, followed by the intended autosave
  and same-world reload.
- Excludes: an unpowered Heart; an open perimeter; a brazier without fuel;
  assuming an unavailable early roof; upgrading to stone construction;
  defeating a V Blood boss; completing the campaign.
- Parameters: opening prerequisites, territory, ownership core, power reserve,
  connected enclosure, closed opening, shelter fixtures, protection source,
  saved world and verification reload.
- Evidence: [V Rising decomposition](../games/s-z/v-rising.md).
- Novelty: first isolated for `GAME-0294`; the terminal joins a predefined
  territorial claim and continuously powered core to a closed early shelter,
  unlike free-positioned shelters or later whole-campaign base objectives.

## OBJ-174 — Complete and retain the first solo large-monster Village hunt

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one fresh authored Village opening through its required
  training and Key Quest predecessors, defeat and carve the first urgent
  large-monster target, accept the hunt rewards and save the returned Village
  state as the retained continuation point.
- Includes: MONSTER HUNTER RISE from `Back to Basics` through the two fixed ★1
  Key Quests and `Great Izuchi, Great Pain`, ending after `900 z` settlement
  and an accepted Kamura manual save.
- Excludes: stopping on the lethal hit; capture; Hub or multiplayer quests;
  completing all Village ranks; claiming an unperformed verification reload;
  Sunbreak progression.
- Parameters: training, required Key count, chosen predecessors, urgent quest,
  target, completion method, carve, reward, return hub, save and verification
  reload.
- Evidence: [MONSTER HUNTER RISE decomposition](../games/m-r/monster-hunter-rise.md),
  using Capcom's official quest rules and corroborated opening quest records.
- Novelty: first isolated for `GAME-0297`; the retained objective joins an
  authored solo-only predecessor chain to the first large-monster quest
  settlement rather than one isolated assignment or a later campaign hunt.

## OBJ-175 — Earn the first Goodwin House Career Bronze award

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Limited`
- Confidence: `Medium`
- Definition: from a fresh Goodwin House Career tutorial, satisfy the authored
  exploration, adoption and habitat-setup predicates for its first award and
  end when Bronze becomes visibly registered, before any Silver-stage work.
- Includes: the written-source route through Warthog care and the gated,
  path-connected Ostrich habitat with four adopted Ostriches in Planet Zoo:
  Console Edition's base-product analysis.
- Excludes: stopping at an unregistered checklist item; earning Silver or
  Gold; a Timed Scenario; free-form Sandbox success; a claimed directly earned
  Xbox medal without a performed run.
- Parameters: scenario version, objective text, required species and counts,
  completed predicates, visible Bronze award and successor availability.
- Evidence: [Planet Zoo: Console Edition decomposition](../games/m-r/planet-zoo-console-edition.md),
  using Frontier's Career guide and two older written objective checklists;
  exact current Xbox objective parity remains unverified.
- Novelty: first isolated for `GAME-0298`; the finite authored management
  award is distinct from generic accumulation or endless zoo operation.

## OBJ-176 — Earn the first ordinary kitchen progression star

- Lifecycle: `Active`
- Claim status: `Hypothesis`
- Evidence quality: `Limited`
- Confidence: `Low`
- Definition: complete a first scored Story kitchen with a final service
  score meeting its minimum one-star threshold and thereby reach the next
  map node, without requiring higher-star replay.
- Includes: Overcooked! 2's reported solo 1-1 one-star result and access to
  1-2 in the original Switch base-game packet, pending direct Switch check.
- Excludes: the mandatory tutorial alone; maximising score without a
  progression boundary; New Game+ fourth star; claiming a reload was observed.
- Parameters: kitchen identity, player count, score threshold, awarded star,
  successor node and persistence after return to map.
- Evidence: [Overcooked! 2 decomposition](../games/m-r/overcooked-2.md),
  using the level-specific written star chart; installed Switch parity is
  unverified.
- Novelty: first isolated for `GAME-0300`; a bounded scored kitchen award
  governs immediate Story progression rather than endless service score.

## OBJ-177 — Win the terminal wall-score comparison

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after a legal round-completion terminal, have the highest score
  after placement, floor and end-game bonus settlement; tied scores compare
  complete horizontal rows, then remain a shared win if still tied.
- Includes: the two-player original Azul base game's final ranking.
- Excludes: maximising provisional score without a terminal comparison;
  ending on a vertical-column completion alone; inventing a further tie-break.
- Parameters: final scores, complete rows, winner and unresolved tie.
- Evidence: [Azul decomposition](../games/a-f/azul.md), official rules.
- Novelty: first isolated for `GAME-0304`; a spatial row threshold ends
  drafting, but score and row-count ranking determine the winner.

## OBJ-178 — Extract a designated living subject and depart with them

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: locate the declared living mission subject, keep that subject
  viable, transport or escort them into a currently usable evacuation vehicle,
  then board or depart as the controlled rescuer so the mission's required
  rescue result can settle.
- Includes: loading injured Kazuhira Miller into the second available
  helicopter and boarding it to complete the first `Phantom Limbs` mission
  in METAL GEAR SOLID V: THE PHANTOM PAIN.
- Excludes: finding the subject but leaving them behind; reaching a blocked
  pickup marker; rescuing an optional extra prisoner; autonomous Pikmin
  carriers delivering a castaway; collecting a quota of mineral payloads;
  treating extraction as an optional bonus after an already-settled objective.
- Parameters: target identity, viable state, rescue route, transport mode,
  usable vehicle, subject loading, rescuer boarding and mission settlement.
- Evidence: [METAL GEAR SOLID V: THE PHANTOM PAIN decomposition](../games/m-r/metal-gear-solid-v-the-phantom-pain.md),
  official Xbox One carry/board controls and independent Mission 1 route.
- Novelty: first isolated for `GAME-0306`; a protected living subject and
  rescuer have distinct required departure states at the same active vehicle.

## OBJ-179 — Buy a first enclosure upgrade through a care-and-sale cycle

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: contain and feed a compatible creature, recover its produced
  output, sell enough output to make a declared enclosure improvement
  affordable, and purchase that improvement so its ownership is registered.
- Includes: selling at least enough Pink Plorts to raise a fresh Slime Rancher
  Adventure balance from its initial 250 Newbucks to the 350 needed for High
  Walls, then buying High Walls for the starter corral.
- Excludes: treating the starting 250 as earned output; merely reaching the
  displayed price; buying a Garden instead; later automated collection;
  maximising market income or completing the wider open-ended campaign.
- Parameters: creature, enclosure, food, produced item, sale value, starting
  balance, target price, purchased improvement and registration state.
- Evidence: [Slime Rancher decomposition](../games/s-z/slime-rancher.md),
  official product description plus original-game beginner routes that state
  the starting ranch loop and High Walls price.
- Novelty: first isolated for `GAME-0307`; one finite terminal joins creature
  care, recoverable output, sale income and a concrete containment purchase.

## OBJ-180 — Win a fixed multi-race cup by cumulative points

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete every race in one fixed ordered cup, accumulate the
  highest total of place-derived points across those results and retain the
  corresponding gold trophy after final settlement.
- Includes: winning Mario Kart 8 Deluxe's four-race 150 cc Mushroom Cup and
  retaining its gold trophy, without requiring a perfect sixty-point result or
  three-star rating.
- Excludes: winning one isolated race; completing the last race first while
  losing the cup total; a campaign stage whose progress is rivals passed rather
  than place points; maximising an unbounded score; winning every cup.
- Parameters: cup, ordered race set, valid results, point table, cumulative
  totals, rank, trophy, optional rating and retained result.
- Evidence: [Mario Kart 8 Deluxe decomposition](../games/m-r/mario-kart-8-deluxe.md),
  using Nintendo's Grand Prix manual and corroborating Deluxe cup records.
- Novelty: first isolated for `GAME-0309`; several complete competitive race
  results are necessary inputs to one aggregate trophy objective.

## OBJ-181 — Clear one authored level and retain credited optional progress

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: reach one authored level's ordinary exit, accept its closeout and
  return to a selectable map state where level completion and every optional
  collectible already credited are retained, without requiring the complete
  optional set for the exit itself.
- Includes: breaking Sky Garden's final glass in ASTRO BOT and returning to its
  galaxy-map state with the level complete and acquired Bots and Puzzle Pieces
  still credited.
- Excludes: a fixed exit that retains no level result; requiring every
  collectible before the exit activates; advancing directly into a successor
  stage with continuous run state; completing a whole campaign.
- Parameters: level, exit event, closeout, map state, completion mark, optional
  roster, retained subset, replay availability and successor nodes.
- Evidence: [ASTRO BOT decomposition](../games/a-f/astro-bot.md), using the
  official map/level structure and independent written Sky Garden route,
  replayability and persistence evidence.
- Novelty: first isolated for `GAME-0312`; ordinary completion and incomplete
  optional collection settle together into a replayable map record rather than
  one being a prerequisite of the other.

## OBJ-182 — Analyse, build and retain one assigned first shelter

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one fresh survival opening by analysing the materials
  needed to learn its tool and shelter dependencies, crafting the harvesting
  capability, gathering and committing the shelter bill, completing the first
  shelter tutorial, assigning the finished fixture as the respawn point and
  accepting the resulting world in retained save history.
- Includes: Grounded from first Kid Case control through `Build Shelter`, one
  assigned Lean-To, completed `Settling In` and an accepted manual save.
- Excludes: placing only the unfinished plan; building without respawn
  assignment; sleeping; executing death and respawn; requiring a save command
  at the shelter itself; completing the wider story.
- Parameters: fresh world, material samples, recipe unlocks, harvesting tool,
  shelter design and bill, tutorial states, assigned respawn fixture, save
  slot, retained world and unverified reload state.
- Evidence: [Grounded decomposition](../games/g-l/grounded.md), official
  new-game/save notes and current tutorial, analyzer and Lean-To references.
- Novelty: first isolated for `GAME-0314`; the constructed shelter is preceded
  by charged material analysis and followed by a separate respawn assignment,
  while retention belongs to playthrough save history rather than a
  fixture-bound save command.

## OBJ-183 — Rescue the captive ally and extract into the named successor mission

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one authored campaign mission by reaching and releasing
  its captive allied leader, settling the required hostile response, boarding
  the admitted extraction transport and retaining the named successor mission
  as the ordinary campaign continuation.
- Includes: releasing Sergeant Johnson, defeating the required dam
  counterattack, boarding the Pelican and advancing from Halo 3 `Sierra 117`
  toward `Crow's Nest` in the scoped original Xbox 360 campaign.
- Excludes: reaching the captive without releasing them; rescue without the
  required counterattack; seeing transport without boarding; player-controlled
  vehicle traversal; completing the whole campaign; optional skulls, scoring
  or collectibles.
- Parameters: mission, captive, release interaction, hostile response,
  settlement predicate, extraction transport, boarding region, mission result,
  successor and retention boundary.
- Evidence: [Halo 3 decomposition](../games/g-l/halo-3.md), using the licensed
  mission guide and corroborating Sierra 117 route references.
- Novelty: first isolated for `GAME-0315`; captive release and mandatory
  response are necessary predecessors to an interaction-gated extraction that
  names the next retained campaign mission.

## OBJ-184 — Pass one bounded acceleration-and-braking licence test

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one assigned driving-skill test by accelerating its
  supplied vehicle across the fixed approach, bringing the complete vehicle to
  rest inside the declared goal area before the deadline and reaching the
  accepted test result.
- Includes: the first passed attempt of Gran Turismo `SCUS-94194` licence B-1
  with the supplied Mazda Demio.
- Excludes: earning the complete B licence; winning a rival race; crossing a
  track finish while moving; obtaining a particular optional grade; repeating
  the test to optimise time.
- Parameters: test, supplied vehicle, approach, stopping area, deadline,
  accepted result, disqualification and broader-licence exclusion.
- Evidence: [Gran Turismo decomposition](../games/g-l/gran-turismo.md), using
  original-product and contemporary licence-test evidence.
- Novelty: first isolated for `GAME-0316`; the positive terminal is one passed
  acceleration/braking examination rather than a race, route or full licence.

## OBJ-185 — Destroy one designated mission structure and retain the successor

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one bounded command mission by destroying its single
  designated hostile structure while every declared mission-critical actor
  remains viable, accept mission completion and retain access to the named
  campaign successor.
- Includes: destroying the Logistics Headquarters while Raynor survives in
  StarCraft II's `Liberation Day`, then advancing to `The Outlaws`.
- Excludes: eliminating every hostile on the map; destroying optional
  structures; resolving a character target and returning to a separate exit;
  building a structure; completing the whole campaign.
- Parameters: designated structure, controlled force, critical actors,
  destruction predicate, optional targets, mission settlement and successor.
- Evidence: [StarCraft II decomposition](../games/s-z/starcraft-ii.md), using
  Blizzard's command documentation and corroborated written mission records.
- Novelty: first isolated for `GAME-0317`; a single structure directly owns the
  campaign terminal while critical-actor survival remains conjunctive and
  ordinary hostile clearance is unnecessary.

## OBJ-186 — Recover and settle one mapped shared-world treasure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one named tutorial voyage by locating its mapped buried
  object, exposing and retaining that physical object through a shared-world
  return journey, then handing it to the designated receiver so reward and
  voyage completion settle.
- Includes: `An Introduction to the Gold Hoarders` from Quest Table acceptance
  through Sailor's Chest sale to Gold Hoarders in Sea of Thieves 3.9.0.
- Excludes: stopping when the chest is dug up; selling arbitrary treasure;
  completing an ordinary multi-chest Voyage; maximising gold or reputation;
  winning combat against another crew.
- Parameters: voyage, map, buried object, destination, shared world, return
  receiver, recoverability, reward, completion flag and retained control.
- Evidence: [Sea of Thieves decomposition](../games/s-z/sea-of-thieves.md),
  using current official release notes, Gold Hoarders guidance and the
  corroborated tutorial route.
- Novelty: first isolated for `GAME-0319`; the same stealable world object must
  survive both outbound inference and inbound custody before the terminal sale.

## OBJ-187 — Establish the first invited island service through natural-history evidence

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: from the first ordinary island day, craft the required capture
  tools, hand one addressed resident five distinct eligible wildlife species,
  place the resulting service-site marker and return after the next-day world
  update to receive the invited specialist's declared capability recipes.
- Includes: Animal Crossing: New Horizons from Tom Nook's DIY workshop through
  Blathers' occupied tent and the shovel/vaulting-pole DIY recipe handoff.
- Excludes: stopping after five catches; carrying the marker without placing it;
  building the later museum; completing Critterpedia; paying the first house debt.
- Parameters: starting day, tool recipes, species quota, recipient, marker,
  site, next-day boundary, specialist and terminal recipes.
- Evidence: [Animal Crossing: New Horizons decomposition](../games/a-f/animal-crossing-new-horizons.md),
  using Nintendo's current product/beginner guidance and three route sources.
- Novelty: first isolated for `GAME-0320`; open-category observation evidence
  becomes player-placed service infrastructure across an external day boundary.

## OBJ-188 — Complete one prison-training breakout into the named successor

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: from first control in confinement, choose the authored training
  branch, cross its required interaction, traversal and combat gates, settle the
  final hostile group and enter the extraction trigger that completes the
  chapter and advances to its named campaign successor.
- Includes: Gears of War's `14 Years After E-Day` right-hand Training route from
  Marcus's opened cell through the King Raven transition to `Trial By Fire`.
- Excludes: taking the left Combat route; stopping after the movement lessons;
  seeing the Raven without entering the transition; optional collectibles;
  completing all of Act 1 or the campaign.
- Parameters: confinement, branch, lessons, interaction gates, combat groups,
  companion, extraction event, trigger, chapter result and successor.
- Evidence: [Gears of War decomposition](../games/g-l/gears-of-war.md), using
  three corroborating original-game written routes.
- Novelty: first isolated for `GAME-0321`; a chosen tutorial branch itself
  remains part of the required breakout terminal before a named combat chapter.

## OBJ-189 — Clear one sampled first den and commit its skill reward

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one first quest by accepting it, locating its sampled
  dungeon, defeating every required living or reanimated hostile, returning to
  the designated quest giver, retaining the fixed point/reset reward and
  spending one available point on a currently eligible character skill.
- Includes: fresh offline Normal Barbarian `Den of Evil` through Akara's reward
  and one legal level-one skill allocation in Diablo II: Resurrected.
- Excludes: stopping when the cave first brightens; hand-in without the declared
  skill commitment; activating a waypoint; deliberately dying for corpse
  recovery; completing Act I or the campaign.
- Parameters: quest giver, sampled area, required hostile set, reanimation,
  clearance signal, hand-in, point reward, retained reset permission, eligible
  skill and post-allocation character state.
- Evidence: [Diablo II: Resurrected decomposition](../games/a-f/diablo-ii-resurrected.md).
- Novelty: first isolated for `GAME-0322`; sampled geography and a re-openable
  hostile set feed an invariant full-clear hand-in whose reward becomes a
  committed persistent build choice.

## OBJ-190 — Complete one dual-protagonist opening boss mission into retained campaign progress

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: carry one opening campaign mission through its ordered traversal,
  civilian-rescue, finite-minion and multi-phase boss gates while accepting
  every authored protagonist handoff, then defeat the designated boss and
  retain the mission-completion reward and successor campaign state.
- Includes: Marvel's Spider-Man 2 `Surface Tension` from first Peter control
  through Sandman's final contextual defeat, 1,900 XP settlement and the
  post-mission successor state.
- Excludes: stopping at one control handoff or boss phase; clearing only the
  sand minions; requiring optional collectibles; free-roam hero switching;
  completing the full campaign.
- Parameters: mission, protagonist roster, handoffs, ordered gates, protected
  civilians, minion groups, boss phases, final contextual strike, reward,
  completion flag and successor state.
- Evidence: [Marvel's Spider-Man 2 decomposition](../games/m-r/marvels-spider-man-2.md),
  using PlayStation's opening-sequence description and two corroborating
  written walkthroughs.
- Novelty: first isolated for `GAME-0323`; the terminal requires two authored
  direct-control perspectives to settle one shared opening boss mission before
  its fixed reward and successor state become retained.

## OBJ-191 — Defeat the first dungeon guardian and claim its Triforce fragment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one authored first dungeon by traversing its required
  carried-key and hostile-clearance gates, defeating its mandatory guardian
  and collecting the exposed Triforce fragment so the dungeon settles and
  retained overworld progression resumes.
- Includes: The Legend of Zelda Quest 1 Level-1 Eagle from entry through
  Aquamentus and collection of the first Triforce fragment.
- Excludes: stopping at boss defeat without taking the fragment; requiring the
  optional heart-container pickup; completing later dungeons; assembling the
  full Triforce or rescuing Princess Zelda; Second Quest.
- Parameters: dungeon, required route gates, guardian, defeat state, optional
  local reward, fragment, credit transition and retained successor state.
- Evidence: [The Legend of Zelda decomposition](../games/s-z/the-legend-of-zelda.md),
  using Nintendo's original manual and three corroborating written Level-1
  references.
- Novelty: first isolated for `GAME-0325`; a guardian defeat exposes a required
  persistent campaign fragment whose contact, rather than crossing a newly
  opened spatial threshold, owns the bounded dungeon terminal.

## OBJ-192 — Clear every counted crate, claim its gem and cross the level portal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one authored platform level by destroying its entire
  qualifying counted-crate set under the declared gem-eligibility rule,
  accepting the resulting clear gem and entering the exit portal so the
  successor map state becomes available.
- Includes: all 49 qualifying crates, clear-gem settlement and portal exit in
  original Crash Bandicoot's scoped `N. Sanity Beach` route.
- Excludes: ordinary exit without the optional gem; collecting a coloured gem
  in a later level; every fruit, mask or enemy being mandatory; completing the
  full game; a score maximum.
- Parameters: level, qualifying count, eligibility state, gem, settlement,
  exit portal, successor map and retained credit.
- Evidence: [Crash Bandicoot decomposition](../games/a-f/crash-bandicoot.md),
  using the original manual and corroborating written first-level route.
- Novelty: first isolated for `GAME-0326`; one optional perfect-clear predicate
  must settle before the ordinary spatial exit carries that credit onward.

## OBJ-193 — Graduate a retained character through a staged life curriculum

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete a character's authored childhood prerequisite, every
  mandatory discipline lesson and the final multi-discipline test, then accept
  the graduation settlement so ordinary control continues with the same
  persistent character and the wider profession-specific task system becomes
  available.
- Includes: original Xbox Fable's good-deed birthday route, childhood and
  adolescent Heroes' Guild lessons, adult sword/bow/Lightning test and Chamber
  of Fate graduation before accepting Wasp Menace.
- Excludes: completing only one lesson; reaching the adult body without the
  final test; an ordinary level-up; accepting or completing the first later
  quest; finishing the campaign.
- Parameters: character, prologue prerequisite, discipline set, life-stage
  gates, final test, graduation event, retained capabilities and successor task
  access.
- Evidence: [Fable decomposition](../games/a-f/fable.md), using Microsoft's
  preserved original-Xbox manual and corroborating original-game walkthroughs.
- Novelty: first isolated for `GAME-0327`; the terminal is neither escape nor
  one combat victory, but the completed curriculum and retained professional
  transition that unlocks the game's ordinary quest layer.

## OBJ-194 — Find every local bonus detour and cross the retained stage exit

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one authored traversal stage by discovering and
  settling every declared hidden bonus detour, then cross its ordinary exit so
  the parent map records full local completion and exposes the immediate
  successor stage.
- Includes: both hidden bonus rooms, exit cave, completed `Jungle Hijinxs!`
  exclamation marker and unlocked `Ropey Rampage` in original Donkey Kong
  Country.
- Excludes: ordinary stage exit with a bonus still undiscovered; requiring all
  route collectibles or enemies; completing an animal-token bonus stage;
  clearing the next stage, world or full game; maximising score or speed.
- Parameters: stage, declared hidden-detour set, discovery credit, detour
  settlement, ordinary exit, map marker, successor access and retained state.
- Evidence: [Donkey Kong Country decomposition](../games/a-f/donkey-kong-country.md),
  using Nintendo's original bonus-room framing and three corroborating written
  first-stage references.
- Novelty: first isolated for `GAME-0329`; the terminal combines an optional
  exhaustive hidden-room predicate with an otherwise ordinary stage exit whose
  parent-map settlement records completeness separately from progression.

## OBJ-195 — Capture Terraneus and preserve the declared successor heroes

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: capture the named underground town Terraneus before simultaneously
  losing every town and hero, settle `Homecoming` and preserve the declared
  four strongest eligible heroes for the unstarted successor scenario.
- Includes: Heroes of Might and Magic III: Complete `Long Live the Queen` first
  scenario on fixed Easy difficulty with the 14 Pikemen bonus.
- Excludes: clearing every enemy or site; starting the next scenario; completing
  the campaign; retaining every troop unchanged.
- Parameters: target town, ownership, surviving town/hero predicate, victory,
  hero ranking, carryover count, level cap and successor boundary.
- Evidence: [Heroes of Might and Magic III: Complete decomposition](../games/g-l/heroes-of-might-and-magic-iii-complete.md).
- Novelty: first isolated for `GAME-0332`; one named-territory capture closes a
  map and selects a ranked subset of agents for later play.

## OBJ-196 — Meet attendance and park-rating thresholds at the fixed deadline

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when the authored scenario date arrives, retain success only if
  the managed park simultaneously contains at least the required number of
  guests and its current Park Rating meets the declared minimum.
- Includes: Forest Frontiers requiring 250 guests and Park Rating 600 at the
  end of October, Year 1 in RollerCoaster Tycoon Deluxe.
- Excludes: reaching either threshold early without retaining both at the
  deadline; a pure cash or Park Value objective; an open-ended sandbox park;
  continuing after the recorded scenario result.
- Parameters: scenario, deadline, minimum guests, minimum rating, simultaneous
  evaluation, success/failure record and optional post-result continuation.
- Evidence: [RollerCoaster Tycoon Deluxe decomposition](../games/m-r/rollercoaster-tycoon-deluxe.md),
  using the official Steam-hosted 2003 manual's Forest Frontiers tutorial.
- Novelty: first isolated for `GAME-0335`; the terminal couples a live
  population count and aggregate quality measure at one fixed calendar check.

## OBJ-197 — Defeat the first Gym Leader and retain its badge

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: defeat the declared first Gym Leader's complete party and finish
  the authored post-battle reward script so its badge is retained before
  ordinary Gym control returns.
- Includes: defeating Brock's level-12 Geodude and level-14 Onix and retaining
  the BoulderBadge in the scoped original Pokémon Red Version route.
- Excludes: reaching Pewter Gym; defeating only the preceding Gym Trainer;
  showing reward dialogue without the retained badge flag; later badges.
- Parameters: Gym, leader, declared party, defeat predicate, reward script,
  badge, retained flag and return-to-control boundary.
- Evidence: [Pokémon Red Version decomposition](../games/m-r/pokemon-red-version.md),
  using the pinned Pewter Gym script and Trainer-party data.
- Novelty: first isolated for `GAME-0336`; a named multi-opponent battle and
  authored reward settlement jointly define the first retained progression gate.

## OBJ-198 — Acquire a retained capability chain and reopen its authored route

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: complete a bounded authored opening by acquiring its declared
  persistent traversal and interaction capabilities in dependency order,
  clearing the required guardian and using the final retained capability to
  reopen the declared route back into the parent traversal network.
- Includes: obtaining Morphing Ball, the first Missile Tank and Bombs; opening
  the five-missile red door; defeating Bomb Torizo; and bombing the exit blocks
  to return to Super Metroid's main Crateria vertical shaft.
- Excludes: merely collecting the first capability; defeating the guardian
  without using the retained exit capability; later bosses, areas or full-game
  completion; sequence breaks or glitch routes.
- Parameters: ordered acquisition chain, capacity gate, guardian, retained
  final capability, reopened edge, parent network and return-to-control state.
- Evidence: [Super Metroid decomposition](../games/s-z/super-metroid.md), using
  Nintendo's original manual and pinned exact-ROM disassembly room, item, door,
  encounter and bomb-block records.
- Novelty: first isolated for `GAME-0337`; earlier route-guardian objectives
  cross into a new region, while this terminal proves that a retained
  capability reopens an earlier authored topology and reconnects the route.

## OBJ-199 — Arm a mission device, clear its response and evacuate before detonation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one bounded sabotage mission by reaching and arming its
  designated device, clearing the mandatory security response and satisfying
  every authored return-route gate before the detonation countdown expires, so
  ordinary control resumes in the declared post-mission field.
- Includes: planting the Reactor No. 1 bomb, defeating Guard Scorpion, freeing
  Jessie, reopening the return doors and escaping before the ten-minute timer
  to reach Sector 8 in original Final Fantasy VII.
- Excludes: arming the device without surviving its response; leaving a
  required ally or route gate unresolved; reaching the exit after timer expiry;
  the later train return, Sector 7 settlement or complete campaign.
- Parameters: device, arming interaction, mandatory response, return gates,
  required actors, countdown, exit, post-detonation transition and successor
  control state.
- Evidence: [Final Fantasy VII decomposition](../games/a-f/final-fantasy-vii.md),
  using the original PlayStation manual and corroborated original-release route.
- Novelty: first isolated for `GAME-0338`; earlier sabotage and mission-exit
  objectives stop at the planted flag, separate target settlement or persistent
  successor, rather than joining an armed device, mandatory security battle,
  timed authored return and post-detonation field control.

## OBJ-200 — Complete one authored qualification trial and retain its proof token

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one named qualification trial's full authored
  dependency chain and acquire its designated retained proof object, without
  requiring the other parallel trials or their combined settlement.
- Includes: finding Mêlée Island's buried treasure and retaining the Treasure
  Huntery T-shirt in the original EGA The Secret of Monkey Island.
- Excludes: merely reaching the trial destination; obtaining an optional
  collectible; completing all parallel trials; receiving a score-only result;
  acquiring a generic puzzle-room token with no qualification role.
- Parameters: qualification, parallel trials, dependency chain, proof object,
  acquisition condition, retained state and combined-settlement exclusion.
- Evidence: [The Secret of Monkey Island decomposition](../games/s-z/the-secret-of-monkey-island.md),
  using the original manual's Three Trials boundary and two corroborated routes.
- Novelty: first isolated for `GAME-0343`; the retained object proves one
  separately completable qualification while the larger multi-trial objective
  remains explicitly outside the packet.

## OBJ-201 — Acquire one unique artefact and retain its first capability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one bounded authored opening by reaching its designated
  unique artefact, accepting the acquisition settlement and regaining ordinary
  control with that artefact and its first granted capability retained.
- Includes: reaching the Dagger of Time through the opening palace and treasure
  vault, accepting its falling-rock Power of Revival demonstration and
  returning to control with the Dagger and rewind capability in Prince of
  Persia: The Sands of Time.
- Excludes: merely seeing or reaching the artefact; a generic puzzle-room token;
  a consumed key; stopping inside the acquisition cinematic; requiring the
  subsequent escape route, later powers or complete campaign.
- Parameters: opening route, unique artefact, acquisition trigger,
  demonstration, first capability, retained state, return-to-control boundary
  and excluded successor route.
- Evidence: [Prince of Persia: The Sands of Time decomposition](../games/m-r/prince-of-persia-the-sands-of-time.md),
  using the official PC manual and three corroborating written route sources.
- Novelty: first isolated for `GAME-0344`; earlier capability objectives require
  a guardian, fixture delivery, multi-capability chain, route reopening or
  later checkpoint, while this terminal is the settled unique-artefact
  acquisition itself.

## OBJ-202 — Meet the minimum hit quota across a fixed target round

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: complete one fixed-length sequence of separately settling target
  opportunities with at least the declared number credited as hits, advancing
  only when the final count reaches the displayed qualification boundary and
  otherwise ending the session.
- Includes: hitting at least six of the ten ducks in round one of original Duck
  Hunt Game A to advance to round two.
- Excludes: clearing every target; maximising score; reaching one numeric-value
  object; a delivery or rescue quota; later Duck Hunt rounds with higher PASS
  LINE values.
- Parameters: target schedule size, credited-hit predicate, qualifying count,
  result check, advance state and failure state.
- Evidence: [Duck Hunt decomposition](../games/a-f/duck-hunt.md), using the
  preserved original English NES manual and corroborating round-one table.
- Novelty: first isolated for `GAME-0345`; success is a minimum count across
  expiring independent target opportunities rather than exhaustive clearance,
  score threshold or transported population.

## OBJ-203 — Complete a festival challenge and enter another era

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one bounded authored festival opening by forming its
  initial party, settling the declared optional challenge and event-currency
  transaction, then resolving the key-item mechanism incident and regaining
  ordinary control at the declared corresponding location in another era.
- Includes: Chrono Trigger's fresh opening through Marle's party join, Gato
  victory, one Silver Point exchange, the Pendant-reactive Telepod incident and
  first ordinary Crono control in 600 A.D. Truce Canyon.
- Excludes: stopping at challenge victory, currency exchange, companion
  disappearance or gate creation; traversing Truce Canyon; rescuing Marle;
  reaching an ending or restoring the complete timeline.
- Parameters: festival, party join, challenge, reward, transaction, mechanism,
  key item, origin era, destination era and successor control state.
- Evidence: [Chrono Trigger decomposition](../games/a-f/chrono-trigger.md),
  using the original English SNES manual and three corroborated written route
  references.
- Novelty: first isolated for `GAME-0346`; earlier opening objectives retain an
  artefact, proof token, capability, checkpoint or mission successor but do not
  join a recoverable event challenge and currency transaction to a
  prerequisite-created cross-era relocation.

## OBJ-204 — Replace every required graffiti point and expose successor stages

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one bounded authored street stage by replacing every
  point marked as required before its failure boundary, accept the settled
  result and end with the declared successor-stage set available for selection.
- Includes: all four small, five large and one x-large red Shibuya GG points,
  result settlement and the three next choices in the bounded Xbox 360 Jet Set
  Radio opening.
- Excludes: optional green tags; reaching a score or Jet-rank threshold;
  defeating all police; campaign completion; stopping after the last surface
  before the result; entering or clearing a successor stage.
- Parameters: stage, required point set, replacement predicate, deadline and
  survival boundary, result, rank display, successor set and availability.
- Evidence: [Jet Set Radio decomposition](../games/g-l/jet-set-radio.md), using
  the inherited original rules and corroborated Xbox 360 Shibuya route.
- Novelty: first isolated for `GAME-0350`; the terminal is exhaustive authored
  surface replacement under live pressure followed by a multi-stage unlock,
  not collectible pickup, hostile clearance or a score threshold.

## OBJ-205 — Escape a prologue and retain its reduced-capability landing

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: clear the authored prologue guardian, reach the declared exit
  before its evacuation deadline, survive the unavoidable capability-removal
  event and regain ordinary control at the successor landing with the reduced
  base capability set retained.
- Includes: Metroid Prime from Parasite Queen clearance through Frigate
  Orpheon escape, equipment malfunction and first Tallon Overworld control.
- Excludes: stopping at guardian defeat, air-lock exit or a cinematic; later
  capability reacquisition; reaching the successor with the original full
  loadout; a voluntary equipment change.
- Parameters: guardian, evacuation trigger, deadline, exit, forced event,
  removed set, retained base set, travel transition, landing and successor
  control.
- Evidence: [Metroid Prime decomposition](../games/m-r/metroid-prime.md), using
  Nintendo product/rule sources and the bounded independent route.
- Novelty: first isolated for `GAME-0355`; prior escape and forced-loss
  objectives do not require both a nonterminal capability reset and a later
  reduced-loadout successor-control state.

## OBJ-206 — Find, climb and defeat one guardian before automatic shrine return

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one bounded hunt by using the authored world bearing to
  reach a mandatory giant guardian, changing and traversing its body topology,
  depleting its required major sigil and accepting the automatic return that
  restores ordinary control at the declared hub.
- Includes: finding and defeating the first colossus on original Shadow of the
  Colossus Normal difficulty and regaining control at the Shrine of Worship.
- Excludes: stopping at discovery, kneeling, first mount or guardian death;
  starting the second hunt; defeating every colossus; Hard-mode extra sigils;
  optional exploration or time attack.
- Parameters: hub, bearing target, guardian, topology trigger, required sigils,
  health terminal, automatic return and successor-control state.
- Evidence: [Shadow of the Colossus decomposition](../games/s-z/shadow-of-the-colossus.md),
  using the original North American PlayStation 2 manual and corroborated
  first-colossus routes.
- Novelty: first isolated for `GAME-0356`; the objective binds optical world
  search and traversal across the living target to a non-voluntary hub return,
  rather than crossing a guardian-opened threshold or continuing in the arena.

## OBJ-207 — Follow two moving leaders by bicycle and unlock the first home

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete one bounded authored opening by mounting the supplied
  bicycle, following a first and then a second named moving leader through
  consecutive route stages, reaching the final home marker and retaining the
  declared reputation, safehouse and successor-mission unlocks.
- Includes: original PlayStation 2 Grand Theft Auto: San Andreas `Sweet & Kendl`
  from the cemetery bicycle mount through Sweet, Ryder and settled Grove Street
  control with Respect, Johnson House and `Ryder` available.
- Excludes: reaching only one leader; arriving home before the cemetery;
  completing the prior cutscene-only `Big Smoke` transition; saving inside the
  house; beginning the successor mission; completing the wider campaign.
- Parameters: supplied bicycle, first leader, handoff, second leader, route
  markers, home, reputation reward, safehouse, successor and settled control.
- Evidence: [Grand Theft Auto: San Andreas decomposition](../games/g-l/grand-theft-auto-san-andreas.md),
  using the original PlayStation 2 booklet and three corroborating written
  opening routes.
- Novelty: first isolated for `GAME-0357`; existing route, escort and race
  objectives do not join a two-leader moving-reference handoff to the first
  retained home and next-story unlock.

## OBJ-208 — Complete one mental training course and retain its successor invitation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: enter one named training mind, complete its authored physical,
  combat and class-sensitive qualification gates, cross its closing mental
  sequence and regain ordinary real-world control with course completion and
  the declared next-training invitation retained.
- Includes: completing Coach Oleander's `Basic Braining` in Psychonauts and
  returning to the Kid's Cabins with Sasha Nein's advanced-training button.
- Excludes: entering the mind; clearing only the target gallery; collecting
  every optional figment, baggage pair, vault or cobweb; beginning the next
  training; completing the full camp or campaign.
- Parameters: training mind, ordered course gates, qualification result,
  closing sequence, real-world return, completion flag, invitation object and
  successor activity.
- Evidence: [Psychonauts decomposition](../games/m-r/psychonauts.md), using
  the original Xbox manual and two corroborating written routes.
- Novelty: first isolated for `GAME-0358`; the terminal joins completion of an
  entered mental curriculum to a real-world return and a retained invitation
  for a different instructor's successor training.

## OBJ-209 — Recapture the airborne base and retain the sortie token

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete every required flight-training and hostile predicate of
  one fixed opening sortie, accept the declared airborne-base return marker and
  regain ordinary post-mission control inside the recaptured base with its
  completion token retained.
- Includes: completing `The Morning After`, recapturing Pandora and retaining
  its Upgrade Token in original-Xbox Crimson Skies: High Road to Revenge.
- Excludes: stopping at the final fighter defeat or return marker; finding a
  hidden token; beginning Mission 2; upgrading an aircraft; completing the
  wider campaign.
- Parameters: sortie, ordered predicates, final hostile set, base marker,
  return interaction, recaptured state, completion token and successor control.
- Evidence: [Crimson Skies: High Road to Revenge decomposition](../games/a-f/crimson-skies-high-road-to-revenge.md),
  using Prima's first-mission guide and two corroborating written routes.
- Novelty: first isolated for `GAME-0359`; existing mission terminals settle a
  medal, region or invitation, not an interacted airborne-home recapture with a
  retained upgrade currency token and interior-control handoff.

## OBJ-210 — Defeat the first dungeon guardian and retain its story token

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete a bounded first authored dungeon by opening its boss
  route, defeating its mandatory guardian, exiting the settled encounter and
  receiving a unique persistent story token from a separate quest-giving
  actor before entering the next region.
- Includes: defeating Queen Gohma, using the boss-room exit and receiving the
  Kokiri's Emerald from the Great Deku Tree in Ocarina of Time before leaving
  Kokiri Forest.
- Excludes: stopping when the boss falls without receiving the token; a
  fragment awarded by direct contact in the boss dungeon (`OBJ-191`);
  crossing into the next region before the declared terminal (`OBJ-080`);
  collecting every optional dungeon treasure or completing the campaign.
- Parameters: dungeon, access sequence, guardian, encounter settlement,
  exit, giver, token, persistent quest state and next-region boundary.
- Evidence: [Ocarina of Time decomposition](../games/s-z/the-legend-of-zelda-ocarina-of-time.md),
  using Nintendo's original N64 manual and independent written routes.
- Novelty: first isolated for `GAME-0363`; guardian defeat enables a distinct
  post-dungeon giver to award the retained token while next-region entry
  remains outside the packet.

## OBJ-211 — Earn and retain at least one goal in a timed park run

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: in one fixed-duration goal-based park attempt, satisfy one or
  more independently declared local goal predicates and finish the run with
  that Tour credit retained, even if other park goals remain incomplete.
- Includes: a fresh Tony Hawk's Pro Skater 1 + 2 Warehouse Tour run ending
  with a credited score, single-combo, collection, object or gap goal.
- Excludes: requiring every Warehouse goal in one run; Free Skate without
  goals; a Single Session leaderboard submission; treating a high score
  without a crossed goal threshold as the only success condition.
- Parameters: park, run window, available goal set, completed subset,
  retained Tour progress and subsequent-run eligibility.
- Evidence: [Tony Hawk's Pro Skater 1 + 2 decomposition](../games/s-z/tony-hawks-pro-skater-1-plus-2.md),
  using Activision's Tours rules and a corroborating Warehouse guide.
- Novelty: first isolated for `GAME-0365`; the objective is partial retained
  credit from one timed multi-goal park attempt, not full park clearance.

## OBJ-212 — Clear every CPU duel in a fixed-fighter Arcade ladder

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: retain one selected fighter through the required sequence of
  one-player CPU matches and win the final match, with any admitted Continue
  retry returning to its lost stage rather than counting as ladder progress.
- Includes: Jin Kazama clearing original PlayStation Tekken 3 Arcade Mode.
- Excludes: winning only one duel (`OBJ-099`); a two-player tournament set;
  switching selected fighters during a Continue; earning an unlock or viewing
  the ending movie after Arcade completion.
- Parameters: selected fighter, current CPU opponent, completed stages,
  final-stage condition, continue decision and cleared result.
- Evidence: [Tekken 3 decomposition](../games/s-z/tekken-3.md), from Namco's
  original PlayStation instruction manual.
- Novelty: first isolated for `GAME-0366`; completing a full opponent ladder
  is a different terminal from the required round wins of any one duel.

## OBJ-213 — Meet five hospital criteria together at quarterly appraisal

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: at a financial quarter's evaluation, satisfy the briefing's
  Reputation, Money, Cures, Happiness and Hospital Value thresholds together
  without having reached any declared losing criterion, earning an offer to
  proceed to the next hospital.
- Includes: the first Theme Hospital level's first successful quarterly
  appraisal, whether or not the player accepts immediate transfer.
- Excludes: winning solely by cash or cure count; treating an unsuccessful
  but non-losing quarter as a final defeat; completing all later hospitals.
- Parameters: quarter, five target values, five observed values, loss
  thresholds, appraisal timing and next-hospital offer.
- Evidence: [Theme Hospital decomposition](../games/s-z/theme-hospital.md),
  using the original PC manual's Mission Briefing, Status and Yearly
  Appraisal descriptions; exact first-level numbers were not inferred.
- Novelty: first isolated for `GAME-0370`; five managed-service outcomes
  must coincide at one recurring appraisal while separate loss bars remain
  below threshold.

## OBJ-214 — Finish a photo course and submit one subject for appraisal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: carry one bounded moving photographic excursion through its
  goal gate and submit a selected image of the declared subject for the
  post-course expert check, producing an observable scored Report result.
- Includes: original Pokémon Snap's Beach goal gate followed by Oak's
  appraisal of one marked Pikachu frame during the scoped excursion.
- Excludes: merely reaching the gate without a usable marked subject;
  completing every island course or the full PKMN Report; guaranteeing that
  a new submission improves the previous best.
- Parameters: course, target subject, captured frame, goal gate, selection,
  evaluation result and retained Report state.
- Evidence: [Pokémon Snap decomposition](../games/m-r/pokemon-snap.md), using
  Nintendo's original instruction booklet, pp. 12–17.
- Novelty: first isolated for `GAME-0371`; the course gate and later
  evidence appraisal together form the declared bounded research terminal,
  not a global game-over.

## OBJ-215 — Survive one authored song to its results screen

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: play the selected chart to its authored end without the live
  performance gauge reaching failure, then receive its score, note-hit rate,
  longest streak and star grade on the song-results screen.
- Includes: one single-player Guitar Hero III Quick Play song on Easy.
- Excludes: completing Career, earning a five-star result, unlocking songs,
  defeating a guitar-battle rival or judging success from score alone.
- Parameters: selected song, difficulty, chart endpoint, Rock Meter survival,
  score, notes hit, streak and grade.
- Evidence: [Guitar Hero III decomposition](../games/g-l/guitar-hero-iii-legends-of-rock.md),
  Activision's PlayStation 3 instruction booklet, pp. 8–9.
- Novelty: first isolated for `GAME-0372`; song completion and live survival
  are distinct from optional score optimisation.

## OBJ-216 — Fill cell-stage progress and enter the successor stage

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: complete a cell-stage feeding-and-growth path until the stage
  Progress Bar is full, choose to advance, finish the required transition and
  retain the evolved lineage at the first controllable successor-stage state.
- Includes: moving a Spore cell through the water's growth progression and
  entering the Creature stage on land.
- Excludes: filling the bar without choosing the offered advance; finishing
  every later evolutionary stage; requiring one specific cell-part loadout.
- Parameters: stage progress, advance choice, transition, retained lineage
  and successor entry state.
- Evidence: [Spore decomposition](../games/s-z/spore.md), original EA manual,
  pp. 6–8 and 30–31.
- Novelty: first isolated for `GAME-0373`.

## OBJ-217 — Obtain one coloured resident through garden conditions

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: alter a starting garden so a named wild species appears, visits and satisfies its residence conditions, ending when one individual has visibly changed into a coloured garden resident.
- Includes: the bounded first-Whirlm residency path in the original Viva Piñata tutorial.
- Excludes: first appearance alone; a black-and-white visit alone; obtaining two residents, a home or a romance result; guaranteeing permanent retention after neglect.
- Parameters: starting garden, target species, staged conditions, resident individual and visible terminal.
- Evidence: [Viva Piñata decomposition](../games/s-z/viva-pinata.md), original Xbox 360 booklet pp. 8–9, 16–17.
- Novelty: first isolated for `GAME-0375`; the scoped endpoint is residency, not a wildlife capture or a bought zoo specimen.

## OBJ-218 — Meet a rolling-body size target before stage settlement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: grow the controlled katamari by attaching eligible world
  objects until it reaches the stage's declared diameter before the
  authoritative deadline, then accept the successful stage result that
  converts the collected mass into a star.
- Includes: replaying Katamari Damacy REROLL Make a Star 1 until its size
  target is met and the King settles that timed attempt.
- Excludes: merely touching a destination marker; collecting every object;
  a shooting-star speed bonus as a required condition; the larger campaign
  or Moon stage; assuming the stage must end immediately on first reaching
  the minimum size.
- Parameters: target diameter, current diameter, deadline, accepted result
  and created star.
- Evidence: [Katamari Damacy REROLL decomposition](../games/g-l/katamari-damacy-reroll.md),
  Bandai Namco's REROLL star-making premise, its original timed-size game
  description and a first-hand REROLL stage report.
- Novelty: first isolated for `GAME-0376`; completion evaluates a physically
  accumulated moving body at a timed size threshold.

## OBJ-219 — Claim the victory-point threshold on one's own turn

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: be the first participant with at least the declared total of
  points during one's own active turn and substantiate any concealed point
  cards needed for that total, immediately ending the contest.
- Includes: CATAN's ten-point base-game win from settlements, cities,
  Longest Road, Largest Army and revealed victory-point cards.
- Excludes: merely leading a final-score table; reaching the threshold on
  another player's turn and claiming victory immediately; a resource-count
  target rather than points.
- Parameters: point threshold, active player, public structure and bonus
  points, concealed point cards and declaration state.
- Evidence: [CATAN decomposition](../games/a-f/catan.md), official base rules.
- Novelty: first isolated for `GAME-0377`; a race threshold is gated by the
  claimant's own turn and can include privately held score evidence.

## OBJ-220 — Guide a rolling avatar ball into a fixed goal before expiry

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: clear one bounded stage by steering an avatar-containing ball
  into its fixed goal while the attempt clock still permits success, without
  requiring every optional collectible or a score threshold.
- Includes: entering the goal with the monkey ball in Super Monkey Ball 2's
  first Jungle Island Story stage before time reaches zero.
- Excludes: `OBJ-014`'s delivery of a separate payload; `OBJ-026`'s directly
  navigated avatar reaching a place; collecting all bananas; merely remaining
  on the course until the clock expires.
- Parameters: fixed goal geometry, ball-goal contact, time remaining,
  optional pickups, accepted clear and score settlement.
- Evidence: [Super Monkey Ball 2 decomposition](../games/s-z/super-monkey-ball-2.md),
  original GameCube manual p. 9 and publisher-supplied Nintendo description.
- Novelty: first isolated for `GAME-0378`; indirect field control and a live
  clock gate the avatar-containing ball's entry into one stage receiver.

## OBJ-221 — Be the last team with a living worm

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: win the declared one-round match by eliminating all opposing
  worms through zero energy or drowning while at least one own worm survives.
- Includes: the scoped two-team Worms Armageddon offline match with one round
  victory required.
- Excludes: maximising damage without elimination; a fixed score threshold;
  winning a multiround series; inventing a tie-breaker for simultaneous
  last-worm death.
- Parameters: team roster, living worms, elimination event and round result.
- Evidence: [Worms Armageddon decomposition](../games/s-z/worms-armageddon.md),
  Team17 manual pp. 2 and 33.
- Novelty: first isolated for `GAME-0379`; the terminal counts surviving
  team members after physical artillery and water resolution.

## OBJ-222 — Solve one authored map question to open the story route

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: submit the one accepted region of an authored visual question
  so its puzzle is recorded solved and its linked narrative route becomes
  available, regardless of whether the maximum picarat reward was preserved.
- Includes: identifying the village in the opening Professor Layton map
  question to continue toward St. Mystere.
- Excludes: maximizing picarats without solving; completing every later
  riddle; selecting any reachable map node without validating a puzzle.
- Parameters: target question, accepted region, solved flag, story successor
  and reward-independent completion test.
- Evidence: [Professor Layton and the Curious Village
  decomposition](../games/m-r/professor-layton-and-the-curious-village.md),
  Nintendo manual pp. 9–10 and corroborated puzzle 001 walkthroughs.
- Novelty: first isolated for `GAME-0380`; a singular pictured answer
  resolves a narrative access gate, not a whole-grid or score objective.

## OBJ-223 — Neutralise a declared alarm set and depart from the mission platform

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: resolve every member of a finite declared security-alarm set,
  then use a separately reachable departure point so the bounded mission
  settles with all required objective flags complete.
- Includes: destroying the four Dam alarms and then making the bungee-platform
  departure on GoldenEye 007's Secret Agent difficulty.
- Excludes: jumping before the alarms are resolved; destroying all guards;
  00 Agent modem/data tasks; a generic spatial exit with no mission checklist
  (`OBJ-026`).
- Parameters: alarm set, member destruction states, departure point,
  difficulty-specific checklist and mission settlement.
- Evidence: [GoldenEye 007 decomposition](../games/g-l/goldeneye-007.md),
  two independent original-N64 Dam guides.
- Novelty: first isolated for `GAME-0381`; a fixed dispersed sabotage set and
  an independently accessible exit form one conjunctive mission objective.

## OBJ-224 — Restore the cursed village by cutting its suspended fruit

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: acquire the brush capabilities needed to reach the cursed
  village's suspended restorative fruit, then sever its stalk so the fruit
  falls and the village changes from ruined to restored within the bounded
  opening route.
- Includes: the Rejuvenation river and Nagi sword, Power Slash access through
  the blocked cave return, and the final fruit cut at Kamiki Village in Ōkami
  HD's scoped opening.
- Excludes: merely reaching the fruit without cutting it; restoring every
  villager's later personal state; Hana Valley's Guardian Sapling; defeating
  Orochi or completing the whole campaign.
- Parameters: required acquired powers, route gates, fruit stalk, accepted
  slash, restoration event and terminal village state.
- Evidence: [Ōkami HD decomposition](../games/m-r/okami-hd.md), two independent
  PS4 opening routes and Capcom's original manual restorative premise.
- Novelty: first isolated for `GAME-0382`; a culminating world-restoration
  object is gated by acquiring and applying two brush techniques along one
  authored route.

## OBJ-225 — Fulfil one offered Want within a bounded household day

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during an explicitly bounded household observation, realise at
  least one Want currently displayed for a resident and retain its aspiration
  and reward-point effect as the local positive result.
- Includes: one eligible displayed Want completed before the next 08:00 in the
  scoped two-adult The Sims 2: Legacy Collection study.
- Excludes: claiming the day boundary is an in-game victory; a staged scenario
  ending (`OBJ-052`); fulfilling an undisplayed preference or merely avoiding
  a Fear without a positive Want event.
- Parameters: resident, displayed Want, matching event, aspiration update,
  reward points, observation entry and end time.
- Evidence: [The Sims 2: Legacy Collection decomposition](../games/s-z/the-sims-2-legacy-collection.md), EA's original PC manual and Maxis' design diary.
- Novelty: first isolated for `GAME-0383`; the local objective is a chosen
  repeatable desire in an open household, not a product-level game ending.

## OBJ-226 — Win one race and carry points into an unfinished Cup

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: finish an ordered Cup course ahead of its rival field, receive
  the classified race points and stop while the multi-race championship is
  still unresolved; this local success is not a Cup trophy.
- Includes: first place and credited points after the first Novice Ruby Cup
  Twist Road race in F-Zero GX.
- Excludes: winning all five Ruby Cup courses by cumulative points
  (`OBJ-180`); a self-contained race event with a final retained career reward
  (`OBJ-134`); lower place without the local first-place target.
- Parameters: Cup, race index, ordered laps, finish order, awarded points,
  carried championship total and later unresolved races.
- Evidence: [F-Zero GX decomposition](../games/a-f/f-zero-gx.md), Nintendo's
  original instruction booklet, official Cup rules and result display.
- Novelty: first isolated for `GAME-0384`; the packet's positive result is
  one scored race within, not the terminal of, the larger championship.

## OBJ-227 — Secure first-case acquittal through supported objections

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: in one authored courtroom case, resolve the required witness
  contradictions and prompted explanations with available case evidence
  until the judge declares the defendant not guilty.
- Includes: defending Larry Butz through Frank Sahwit's changing testimony
  to the acquittal at the end of The First Turnabout.
- Excludes: the player personally choosing a binary verdict (`ACT-105`);
  guessing the culprit shown in the introduction; solving a later case;
  treating an unsupported objection as progress.
- Parameters: case, defendant, required contradiction sequence, case-record
  availability, prompted explanations and terminal verdict.
- Evidence: [Phoenix Wright: Ace Attorney decomposition](../games/m-r/phoenix-wright-ace-attorney.md),
  Nintendo's DS description, Capcom's creator interview, contemporary
  GameSpot review and first-case written route.
- Novelty: first isolated for `GAME-0385`; the local terminal is a
  judge-issued acquittal earned by evidence-to-testimony challenges.

## OBJ-228 — Complete one world packet and open its next collection-gated world

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete a declared bounded world's collection and capability
  checkpoints, return to the parent hub, satisfy separate retained-collection
  and allocated-piece access gates, then reach the newly opened successor
  world entrance without entering or completing that successor.
- Includes: a full first Mumbo's Mountain visit with ten world Jiggies and
  100 Notes, then the first 50-Note Door and two-piece Treasure Trove Cove
  picture in original N64 Banjo-Kazooie.
- Excludes: claiming that the full-world checkpoints are the game's minimum
  next-world admission cost; collecting the entire campaign; entering or
  completing Treasure Trove Cove; opening only one of the two hub gates.
- Parameters: world, bounded collection controls, learned capabilities,
  retained Note threshold, addressed picture, allocated piece quota and
  reachable successor entrance.
- Evidence: [Banjo-Kazooie decomposition](../games/a-f/banjo-kazooie.md),
  original Nintendo 64 manual and original-N64 first-world written route.
- Novelty: first isolated for `GAME-0386`; the route ends at successor
  availability after two differently accounted collection gates.
