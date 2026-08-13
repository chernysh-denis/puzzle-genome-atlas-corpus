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
  stack at any legal ground location.
- Excludes: reaching a scalar value; maximising score; merely keeping another
  action available.
- Parameters: target equivalence, permitted whole-object orientations and
  alignment tolerance, whether target positions distinguish occupant class and
  whether the target's ground location is fixed or flexible.
- Evidence: [Rubik's Cube decomposition](../games/m-r/rubiks-cube.md) and
  [Sokoban decomposition](../games/s-z/sokoban.md), and
  [FreeCell decomposition](../games/a-f/freecell.md), and
  [Peg Solitaire decomposition](../games/m-r/peg-solitaire.md), and
  [Patrick's Parabox decomposition](../games/m-r/patricks-parabox.md), and
  [A Good Snowman Is Hard to Build decomposition](../games/a-f/a-good-snowman-is-hard-to-build.md).
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
  all valid.
- Excludes: reconstructing a separately specified arrangement; revealing
  pre-existing hidden contents; maximising the number of valid partial entries.
- Parameters: position set, symbol domain, accepted completion test and whether
  the instance is guaranteed to have one solution.
- Evidence: [Sudoku decomposition](../games/s-z/sudoku.md) and
  [Nonogram decomposition](../games/m-r/nonogram.md), and
  [Flow Free decomposition](../games/a-f/flow-free.md), and
  [The Witness decomposition](../games/s-z/the-witness.md).
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
  Match level; eating every visible fruit in one Snakebird level before exit.
- Excludes: maximising score; clearing every non-hazard position; reconstructing
  a specified arrangement; meta-progression rewards after the level.
- Parameters: target classes, required quantities, credit triggers and whether
  several target conditions are conjunctive.
- Evidence: [Royal Match decomposition](../games/m-r/royal-match.md) and
  [Snakebird decomposition](../games/s-z/snakebird.md).
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

## OBJ-014 — Deliver indirectly controlled payload to fixed receiver

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete the attempt by causing one required dynamic payload,
  whose trajectory is influenced through environmental interventions rather
  than direct position commands, to contact a fixed receiving object or zone.
- Includes: feeding Cut the Rope candy to Om Nom by timing rope cuts around
  gravity and momentum.
- Excludes: directly navigating the delivered object; overlapping a directly
  controlled object with a mutable rule-defined goal (`OBJ-010`); transporting
  repeated demand units for unbounded score.
- Parameters: payload count, receiver geometry, accepted contact velocity and
  completion timing.
- Evidence: [Cut the Rope decomposition](../games/a-f/cut-the-rope.md).
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

## OBJ-017 — Complete exact identity-and-fate ledger

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: complete an investigation by assigning every subject in a fixed
  roster to the accepted identity and compound fate record supported by the
  evidence.
- Includes: identifying all Obra Dinn souls and recording each death cause and
  responsible party, or the required survival / destination fate.
- Excludes: revealing every safe board position; reconstructing one spatial
  arrangement; understanding a narrative without entering structured answers.
- Parameters: subject count, fate grammar, required dependent fields, accepted
  equivalent causes and completion exceptions.
- Evidence: [Return of the Obra Dinn decomposition](../games/m-r/return-of-the-obra-dinn.md).
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
  activating the fixed level teleporter.
  It also includes moving the sole required Snakebird head-first through the
  activated fixed exit after every fruit is cleared.
- Excludes: rescuing only a minimum share of a supplied autonomous population;
  delivering one indirectly controlled payload; voluntarily withdrawing a
  surviving squad without completing a fixed exit set.
- Parameters: required actor count, shared or actor-specific exits, simultaneous
  arrival rule, capture failure and whether exited actors remain in simulation.
- Evidence: [Timelie decomposition](../games/s-z/timelie.md),
  [Portal decomposition](../games/m-r/portal.md), and
  [Viewfinder decomposition](../games/s-z/viewfinder.md), and
  [Snakebird decomposition](../games/s-z/snakebird.md).
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
  Swapper puzzle-room arrangement.
- Excludes: collecting every member of a finite campaign set; optional rating
  collectibles; reaching a fixed exit without acquiring a token; maximising an
  unbounded token score.
- Parameters: token count per room, eligible collector, credit persistence,
  room-reset behaviour and later gate threshold.
- Evidence: [The Swapper decomposition](../games/s-z/the-swapper.md).
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
  land region, then walking Carto to its declared person or place.
- Excludes: evacuating every controlled actor through fixed exits; delivering
  an indirectly controlled payload; collecting a token on contact; merely
  reconstructing a target map shape with no avatar traversal requirement.
- Parameters: target identity, arrival radius, required interaction, topology-
  edit requirement, intermediate targets and persistence after arrival.
- Evidence: [Carto decomposition](../games/a-f/carto.md).
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

- Lifecycle: `Active`
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
