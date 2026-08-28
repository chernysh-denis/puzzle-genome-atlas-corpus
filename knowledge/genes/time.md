# Time Genes

## TIM-001 — Discrete turn with automatic resolution

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player supplies one discrete input, after which the system
  completes all resulting state changes before accepting the next input.
- Includes: one 2048 direction followed by movement, merges, scoring and spawn;
  one Minesweeper reveal followed by zero-region expansion; one Royal Match
  move followed by all match, power-up, collapse, refill and cascade effects;
  one Water Sort source-destination choice followed by maximal pouring; one
  Baba Is You direction followed by movement and rule recalculation; one
  Threes swipe followed by one-step shift, merging and successor insertion; one
  Balatro play or discard followed by evaluation and hand refill; one Peg
  Solitaire jump followed by removal of the intervening peg; one Dorfromantik
  tile placement followed by edge, group, quest, score and supply resolution;
  one Stephen's Sausage Roll move or turn followed by fork contact, sausage
  slide / roll, cooking and failure / completion checks; one A Good Snowman Is
  Hard to Build movement followed by snow depletion, growth, stack transfer
  and completion checks; one Snakebird head step followed by body propagation,
  fruit growth, exit activation, unsupported falling and death / completion;
  one Hexcells Infinite binary assertion followed by immediate truth
  adjudication, mistake handling and completion checking; one turn-costing
  Shogun Showdown movement, queue edit or queue activation followed by all
  player and hostile state advancement; one A Monster's Expedition push
  followed by the complete log tip or maximal roll, bridge settlement and
  arrival check; one Bonfire Peaks input followed by the complete carried-
  footprint movement, fire consumption and completion check; one Golf Peaks
  card-direction commitment followed by complete staged ball travel, terrain
  response, settlement and hole-entry evaluation; one inbento placement
  followed by footprint validation, inventory consumption, covered-cell
  overwrite and exact-recipe evaluation; one KAMI seed-and-colour commitment
  followed by complete component recolouring, same-class coalescence, move
  accounting and whole-field evaluation; one HOOK trigger press followed by
  complete linked retraction, removal or collision-and-reset adjudication; one
  Inertia direction followed by the complete straight slide, transit
  collection, stopping and mine / completion checks.
- Excludes: real-time input and simultaneous unresolved planning.
- Evidence: [2048 decomposition](../games/0-9/2048.md) and
  [Minesweeper decomposition](../games/m-r/minesweeper.md), and
  [Royal Match decomposition](../games/m-r/royal-match.md), and
  [Water Sort decomposition](../games/s-z/water-sort.md), and
  [Baba Is You decomposition](../games/a-f/baba-is-you.md), and
  [Threes decomposition](../games/s-z/threes.md), and
  [Balatro decomposition](../games/a-f/balatro.md), and
  [Peg Solitaire decomposition](../games/m-r/peg-solitaire.md), and
  [Dorfromantik decomposition](../games/a-f/dorfromantik.md), and
  [Stephen's Sausage Roll decomposition](../games/s-z/stephens-sausage-roll.md),
  [A Good Snowman Is Hard to Build decomposition](../games/a-f/a-good-snowman-is-hard-to-build.md),
  [Snakebird decomposition](../games/s-z/snakebird.md), and
  [Hexcells Infinite decomposition](../games/g-l/hexcells-infinite.md), and
  [Shogun Showdown decomposition](../games/s-z/shogun-showdown.md), and
  [Can of Wormholes decomposition](../games/a-f/can-of-wormholes.md), and
  [A Monster's Expedition decomposition](../games/a-f/a-monsters-expedition.md), and
  [Bonfire Peaks decomposition](../games/a-f/bonfire-peaks.md), and
  [Golf Peaks decomposition](../games/g-l/golf-peaks.md), and
  [inbento decomposition](../games/g-l/inbento.md), and
  [KAMI decomposition](../games/g-l/kami.md), and
  [HOOK decomposition](../games/g-l/hook.md), and
  [Inertia decomposition](../games/g-l/inertia.md).
- Novelty: not assessed.

## TIM-002 — Self-paced sequential action

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player may pause between discrete actions, and each completed
  action changes state without a time-driven system step.
- Includes: an untimed physical Rubik's Cube solve; a printed Sudoku solved
  without an external competition timer; a classic Sokoban level without a
  timer or automatic motion; classic FreeCell with manual card transfers; a
  printed Nonogram solved without an external timer; Return of the Obra Dinn
  ship exploration, frozen-memory inspection and book revision; Gorogoa's
  ordinary view exploration, layer separation and panel composition; Patrick's
  Parabox movement, pushes and containment transitions; tracing and revising
  an untimed foundational The Witness panel path; rearranging Carto map
  fragments and walking through the resulting world without a forced clock;
  drafting, inspecting and traversing Blue Prince rooms without a real-time
  deadline inside the room;
  inspecting, extracting terms and revising the event Scroll in The Case of the
  Golden Idol; drawing, retracting and redrawing LYNE routes without a forced
  clock or time-driven board step; assigning and revising Hexologic pip values
  without a forced clock or automatic world step; inspecting and selecting a
  valid triple from a fixed SET solitaire field without a deadline; completing
  Mastermind proposals against one fixed code without a deadline; entering
  Wordle guesses without a per-row deadline; pressing Lights Out buttons
  without a forced clock or autonomous board change between presses; assigning
  and revising Slant diagonals without a deadline; placing and revising Tents
  occupancy marks without a forced clock; placing and revising Dominosa pairs;
  cycling and revising Bridges link multiplicities; assigning and revising
  Light Up bulbs without autonomous change or a deadline; selecting and
  revising Loopy edges without a forced clock or time-driven board step;
  assigning and revising Map region colours without autonomous progression;
  drawing and revising Galaxies region boundaries without a forced clock;
  assigning and revising Filling digits without a deadline; assigning and
  revising Keen digits without a deadline; rotating, locking and revising Net
  tiles without a forced clock or autonomous network change; shifting and
  revising Netslide lines without automatic progression between moves;
  inspecting and manipulating The Room's first safe without a forced clock;
  reassembling Josef in Machinarium's scrapyard without autonomous progression
  between committed interactions; handing Day of the Tentacle's battery
  ingredients to Red Edison without partial-set decay or a deadline; rotating
  Monument Valley's Chapter I bridge and selecting Ida's destination without a
  deadline or independent world progression between commands; annotating,
  matching and revising Chants of Sennaar glyph hypotheses while the world
  waits for the next discrete input.
- Excludes: competition timing as an external scoring condition; automatic
  post-action resolution; continuous real-time state change.
- Parameters: action granularity and any externally imposed solve timer.
- Evidence: [Rubik's Cube decomposition](../games/m-r/rubiks-cube.md) and
  [Sudoku decomposition](../games/s-z/sudoku.md), and
  [Sokoban decomposition](../games/s-z/sokoban.md), and
  [FreeCell decomposition](../games/a-f/freecell.md), and
  [Nonogram decomposition](../games/m-r/nonogram.md), and
  [Chess decomposition](../games/a-f/chess.md), and
  [Flow Free decomposition](../games/a-f/flow-free.md), and
  [LYNE decomposition](../games/g-l/lyne.md), and
  [Return of the Obra Dinn decomposition](../games/m-r/return-of-the-obra-dinn.md),
  [Gorogoa decomposition](../games/g-l/gorogoa.md), and
  [Patrick's Parabox decomposition](../games/m-r/patricks-parabox.md), and
  [The Witness decomposition](../games/s-z/the-witness.md),
  [Carto decomposition](../games/a-f/carto.md),
  [The Case of the Golden Idol decomposition](../games/s-z/the-case-of-the-golden-idol.md), and
  [Hexologic decomposition](../games/g-l/hexologic.md), and
  [Rush Hour decomposition](../games/m-r/rush-hour.md), and
  [SET decomposition](../games/s-z/set.md), and
  [Mastermind decomposition](../games/m-r/mastermind.md), and
  [Wordle decomposition](../games/s-z/wordle.md), and
  [Lights Out decomposition](../games/g-l/lights-out.md), and
  [Slant decomposition](../games/s-z/slant.md), and
  [Tents decomposition](../games/s-z/tents.md), and
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
  [Netslide decomposition](../games/m-r/netslide.md), and
  [The Room decomposition](../games/s-z/the-room.md), and
  [Machinarium decomposition](../games/m-r/machinarium.md), and
  [Day of the Tentacle decomposition](../games/a-f/day-of-the-tentacle.md),
  [The Talos Principle decomposition](../games/s-z/the-talos-principle.md), and
  [Monument Valley decomposition](../games/m-r/monument-valley.md), and
  [Chants of Sennaar decomposition](../games/a-f/chants-of-sennaar.md).
- Novelty: not assessed.

## TIM-003 — Real-time input during forced progression

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system advances the decision state on a real-time schedule
  while accepting player inputs during the bounded interval before the current
  state becomes fixed.
- Includes: moving, rotating or accelerating an NES Tetris tetromino while
  gravity continues to schedule descent and eventual lock; placing Pipe Dream
  pieces while Flooz advances through the constructed pipeline; editing a Mini
  Metro network while stations, demand and vehicles progress on the running
  simulation clock; cutting Cut the Rope supports while the candy continues to
  swing, fall and collide under live physics; composing a Gorogoa panel during
  its single developer-identified moving timing puzzle; attaching World of Goo
  nodes while gravity, elasticity, buoyancy and loose-ball traversal continue;
  issuing Bad North squad orders while carriers, soldiers and combat advance,
  with selection slowdown as a parameter; placing Loop Hero cards and replacing
  equipment while the hero, day clock and encounters progress, with pause as a
  planning control; navigating and editing a HUMANITY trial while gates release
  people and the crowd advances, with stop-time and fast-forward controls;
  repositioning Tin Hearts routing devices while soldiers walk and collide,
  with pause and fast-forward as rate controls; moving and firing portals while
  Portal body physics continues; running, jumping or operating switches while
  Braid enemies and platforms advance; dispatching and recalling Pikmin while
  surface tasks, transport, combat and the day clock advance; creating and
  swapping The Swapper bodies while slowed gravity and collision continue;
  moving, jumping and stamping images while Viewfinder body physics remains
  live; combining and applying The Longest Journey's fishing instrument while
  its unpatched inflated ducky continues to lose air toward clamp closure;
  moving, aiming and releasing a Superliminal chess piece while held-pose
  updates and released-body gravity remain live; changing Manifold Garden's
  gravity frame or steering a periodic fall while body physics continues;
  carrying, dropping and crossing Maquette's recursive key while held pose,
  collision and avatar motion remain live; placing, configuring or removing
  Factorio factory entities while mining, transport, crafting, research,
  electricity, pollution and hostile agents continue to advance on the live
  simulation clock; editing SimCity 4 or Cities: Skylines roads, zones,
  services and policy while development, traffic and finances continue on the
  running clock; navigating, aiming, fighting, hacking and driving while
  Cyberpunk 2077 world agents and combat continue in real time; moving,
  attacking, healing, casting and contesting while Marvel Rivals combat and
  objective clocks remain live; navigating, striking, casting, binding and
  evading while Hollow Knight: Silksong enemies and hazards continue in real
  time; moving, grappling, operating switches, piloting and firing while Split
  Fiction Chapter 1 hazards, vehicles and hostiles continue in real time;
  directing Farrah while motives, mood, autonomy and social activity continue
  in The Sims 4 Live Mode; moving, passing, shooting, switching and tackling
  while the EA SPORTS FC 26 ball, players, referee and match clock continue;
  pressing or holding Geometry Dash's one vertical control while Stereo
  Madness continues its automatic travel, physics and authored level clock;
  moving, attacking, guarding, throwing or spending Drive while both Street
  Fighter 6 combatants, projectiles, recovery states and the round clock remain
  live; moving, observing, breaching, shooting, using gadgets and planting or
  disabling the defuser while Rainbow Six Siege phase clocks and opponents
  advance; revising Football Manager 26 roles, instructions and substitutions
  while the autonomous match, player condition and clock continue; steering,
  jumping, boosting and contacting the ball while all Rocket League cars, ball
  physics, pad opportunities and the match clock continue.
- Excludes: a discrete input followed by completed automatic resolution;
  self-paced actions with no time-driven state change; an external timer that
  only measures performance.
- Parameters: update frequency, input-repeat timing, pause rule and speed
  progression. A pause command may provide unbounded planning time without
  changing the fact that running simulation time independently mutates state.
- Evidence: [Factorio decomposition](../games/a-f/factorio.md).
- Evidence: [Tetris decomposition](../games/s-z/tetris.md),
  [Pipe Mania decomposition](../games/m-r/pipe-mania.md), and
  [Mini Metro decomposition](../games/m-r/mini-metro.md), and
  [Cut the Rope decomposition](../games/a-f/cut-the-rope.md), and
  [Gorogoa decomposition](../games/g-l/gorogoa.md), and
  [Lemmings decomposition](../games/g-l/lemmings.md), and
  [World of Goo decomposition](../games/s-z/world-of-goo.md), and
  [Bad North decomposition](../games/a-f/bad-north.md), and
  [Loop Hero decomposition](../games/g-l/loop-hero.md), and
  [HUMANITY decomposition](../games/g-l/humanity.md), and
  [Tin Hearts decomposition](../games/s-z/tin-hearts.md),
  [Portal decomposition](../games/m-r/portal.md), and
  [Braid decomposition](../games/a-f/braid.md), and
  [Pikmin 4 decomposition](../games/m-r/pikmin-4.md),
  [The Swapper decomposition](../games/s-z/the-swapper.md),
  [Viewfinder decomposition](../games/s-z/viewfinder.md),
  [The Longest Journey decomposition](../games/s-z/the-longest-journey.md),
  [Fez decomposition](../games/a-f/fez.md), and
  [Echochrome decomposition](../games/a-f/echochrome.md), and
  [Superliminal decomposition](../games/s-z/superliminal.md), and
  [Manifold Garden decomposition](../games/m-r/manifold-garden.md), and
  [Maquette decomposition](../games/m-r/maquette.md), and
  [Antichamber decomposition](../games/a-f/antichamber.md),
  [SimCity 4 Deluxe Edition decomposition](../games/s-z/simcity-4-deluxe-edition.md)
  [Cities: Skylines decomposition](../games/a-f/cities-skylines.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md), and
  [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md), and
  [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md), and
  [Split Fiction decomposition](../games/s-z/split-fiction.md),
  [The Sims 4 decomposition](../games/s-z/the-sims-4.md) and
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md), and
  [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md), and
  [EA SPORTS FC 26 decomposition](../games/a-f/ea-sports-fc-26.md), and
  [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md), and
  [Geometry Dash decomposition](../games/g-l/geometry-dash.md), and
  [Street Fighter 6 decomposition](../games/s-z/street-fighter-6.md), and
  [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md),
  [Football Manager 26 decomposition](../games/a-f/football-manager-26.md), and
  [Rocket League decomposition](../games/m-r/rocket-league.md), and
  [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## TIM-004 — Alternating adversarial turns

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: two opposing decision-makers take exclusive turns in a fixed
  order, and each completed action hands control of the next decision to the
  other side.
- Includes: White moving first and White and Black then alternating in chess.
- Excludes: automatic system response; simultaneous planning; one player taking
  every turn; real-time action without exclusive turns.
- Parameters: side count, starting side, turn order and extra-turn exceptions.
- Evidence: [Chess decomposition](../games/a-f/chess.md).
- Novelty: not assessed.

## TIM-005 — Planning phase before committed hostile resolution

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player may issue a bounded set of unit commands in flexible
  order during one planning phase, then ends that phase and observes already
  committed hostile and scheduled system events resolve before planning again.
- Includes: the Into the Breach player phase followed by environment and Vek
  attack phases; a Fights in Tight Spaces card-play phase followed by ordered
  primed hostile attacks and the next hand; a Slay the Spire player phase with
  flexible card and potion use followed by End Turn, hostile intents and the
  next hand.
- Excludes: one player input followed immediately by full resolution;
  alternating moves selected by two human decision-makers; simultaneous hidden
  planning.
- Parameters: commands per phase, intra-phase order, resolution order and undo
  availability.
- Evidence: [Into the Breach decomposition](../games/g-l/into-the-breach.md),
  [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md),
  and [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
- Novelty: not assessed.

## TIM-006 — Editable design before resettable automatic run

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player edits a persistent machine design and any authored
  command schedule without time pressure, then starts a deterministic multi-
  cycle run in which design edits are unavailable until execution stops,
  fails, completes or is reset.
- Includes: Opus Magnum's repeated build-program-test-revise loop; SpaceChem's
  self-paced route / symbol editing followed by committed cyclic reactor tests;
  Infinifactory's self-paced conveyor layout followed by a committed factory
  simulation with pause, stop and reset.
- Excludes: editing while a live simulation continues; one input followed by
  one completed automatic response; a bounded tactical planning phase followed
  by hostile resolution and another in-mission planning phase.
- Parameters: stepping and speed controls, pause semantics, reset state,
  success horizon and whether execution can be stopped manually.
- Evidence: [Opus Magnum decomposition](../games/m-r/opus-magnum.md) and
  [SpaceChem decomposition](../games/s-z/spacechem.md), and
  [Infinifactory decomposition](../games/g-l/infinifactory.md).
- Novelty: not assessed.

## TIM-007 — Branchable player-reversible simulation history

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system retains prior world states across continuous
  progression, lets the player restore one and permits a new intervention whose
  continuation replaces the previously observed future.
- Includes: rewinding Tin Hearts to before a soldier falls, moving a routing
  block and resuming along a different path; rewinding Timelie to before
  capture, changing a timestamped command and seeking the replacement future;
  rewinding already lived Braid states and resuming different local movement,
  with marked entity exceptions as a parameter; restoring a retained Pikmin 4
  autosave from minutes earlier and replaying different task assignments;
  rewinding Viewfinder to before a fall or destructive photograph placement
  and continuing with a different pose; restoring a Cyberpunk 2077 manual or
  autosave and making different combat, dialogue or route choices.
- Excludes: restarting a level from its initial state; undoing one discrete
  move in a self-paced puzzle; watching a non-interactive replay.
- Parameters: history horizon, rewind rate, restoration granularity, editable
  paused state and branch-commit rule.
- Evidence: [Tin Hearts decomposition](../games/s-z/tin-hearts.md) and
  [Timelie decomposition](../games/s-z/timelie.md), and
  [Braid decomposition](../games/a-f/braid.md),
  [Pikmin 4 decomposition](../games/m-r/pikmin-4.md), and
  [Viewfinder decomposition](../games/s-z/viewfinder.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## TIM-008 — Random-access editable deterministic action timeline

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: one cursor addresses past, current and prospective simulation
  times; the player may inspect deterministic resolution and edit actor commands
  at the selected time without entering a separate locked execution phase.
- Includes: Timelie's media-player timeline, where commands for the girl and cat
  can be inserted or cleared after seeking backward or forward.
- Excludes: a machine design edited only before a locked run; live real-time
  intervention with pause; replay controls that cannot alter the plan.
- Parameters: timeline horizon, seek direction and speed, command persistence,
  edit granularity, recomputation boundary and playback mode.
- Evidence: [Timelie decomposition](../games/s-z/timelie.md).
- Novelty: not assessed.

## TIM-009 — Self-paced transport-layout design before locked one-shot traversal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player authors one complete spatial transport layout without
  time pressure, then starts one deterministic traversal during which layout
  edits remain unavailable until the vehicle set succeeds, fails, stops or is
  reset.
- Includes: drawing a Cosmic Express entrance-to-exit track, starting the train
  and revising the route only after the run finishes or is reset; arranging a
  Railbound rail layout before starting all numbered carriages together.
- Excludes: editing a network while vehicles continue running; a cyclic machine
  repeatedly executing an instruction schedule; one discrete input followed by
  one immediate automatic response.
- Parameters: layout-completion requirement, vehicle count, start control,
  execution speed, pause / stop permission, reset state and success / failure
  boundary.
- Evidence: [Cosmic Express decomposition](../games/a-f/cosmic-express.md) and
  [Railbound decomposition](../games/m-r/railbound.md).
- Novelty: not assessed.

## TIM-010 — Editable tactical draft with forecast before commit

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player flexibly sequences a bounded tactical turn, invokes
  exact automatic consequence simulation, may restore and revise earlier draft
  steps, then commits one accepted outcome before the next turn begins.
- Includes: Tactical Breach Wizards action / Foresee / rewind / commit timing,
  with hostile movement creating the next turn's circumstances afterward.
- Excludes: hostile attacks committed before planning and executed after it;
  random-access editing across several simulated times; machine design before a
  locked run; ordinary discrete undo without a forecast phase.
- Parameters: commands per draft, forecast depth, rewind horizon, commit
  gesture, post-commit hostile movement and allowance refresh.
- Evidence: [Tactical Breach Wizards decomposition](../games/s-z/tactical-breach-wizards.md).
- Novelty: not assessed.

## TIM-011 — Editable network with repeatable bounded traffic evaluation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player edits a persistent network without a forced planning
  deadline, then runs a bounded automatic traffic evaluation; after the result
  or a jam, the same retained design can be revised and evaluated again.
- Includes: completing a Freeways network, running its accelerated simulated
  day, then undoing or adding roads and rerunning the evaluation.
- Excludes: editing continuously while an endless score simulation advances;
  a deterministic cyclic production machine locked during its test; one fixed
  route consumed by a single traversal.
- Parameters: whether light traffic appears during construction, evaluation
  horizon, speed control, edit lock during evaluation, reset scope and retained
  best design.
- Evidence: [Freeways decomposition](../games/a-f/freeways.md).
- Novelty: not assessed.

## TIM-012 — Alternating automatic presentation and player reproduction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: play alternates between an automatic phase that serially presents
  the complete current target with no player choice and a response phase in
  which the system stops adding cues and accepts ordered player inputs; exact
  completion returns control to automatic presentation.
- Includes: Simon presenting a light sequence, waiting for its reproduction,
  then presenting the retained sequence plus one new cue.
- Excludes: simultaneous real-time intervention in an advancing world; an
  editable planning phase followed by a locked run; one ordinary discrete
  input with immediate consequence resolution; a required response deadline.
- Parameters: phase boundary, input gating, cue tempo, transition delay and
  response-time policy.
- Evidence: [Simon decomposition](../games/s-z/simon.md).
- Novelty: not assessed.

## TIM-013 — Completed progression schedules next-day world update

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: satisfying the current progression predicate records completion
  immediately, but its persistent world-state consequence resolves only across
  the end-of-day boundary and is available on the following play day.
- Includes: Stardew Valley marking the Boiler Room complete when its last bundle
  is filled, showing the Junimo minecart repair overnight and enabling minecart
  travel the next day.
- Excludes: an immediate automatic consequence before the next input; a real-
  time deadline; a fixed number of tactical turns; cosmetic day-night change
  with no new capability.
- Parameters: completion instant, scheduled boundary, intervening cutscene,
  skipped-scene behaviour, activation day and persistence after activation.
- Evidence: [Stardew Valley decomposition](../games/s-z/stardew-valley.md).
- Novelty: not assessed.

## TIM-014 — Real-time shift gates admission of new cases

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a work clock advances while the player inspects sequential cases;
  reaching the shift cutoff normally prevents another case from entering but
  permits the currently open case, or a required scripted minimum, to finish.
- Includes: Papers, Please running from 6am to 6pm, allowing the current
  entrant to be completed after the clock darkens and extending the day when a
  minimum scripted entrant has not yet been processed.
- Excludes: a terminal attempt deadline; a live world simulation that mutates
  the current case; an external speedrun timer; a fixed action count.
- Parameters: shift duration, clock scale, new-case gate, open-case completion,
  scripted minimum, paid-after-cutoff policy and pauses.
- Evidence: [Papers, Please decomposition](../games/m-r/papers-please.md).
- Novelty: not assessed.

## TIM-015 — Short inactivity terminates buffered code entry without world penalty

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: once a symbolic input sequence has begun, too much real-time
  inactivity clears its unfinished buffer, but leaves the world target and
  player state intact so the complete sequence can be attempted again.
- Includes: pausing too long between Holy Cross directions in TUNIC and then
  restarting the fountain-door code; Sequence Assist removes this timing demand.
- Excludes: a terminal attempt countdown; a world that advances while idle; a
  fixed turn budget; an exact duration claim not established by evidence.
- Parameters: inactivity threshold, reset feedback, assist override, target
  scope, buffer-prefix policy and whether wrong symbols also restart the buffer.
- Evidence: [TUNIC decomposition](../games/s-z/tunic.md).
- Novelty: not assessed.

## TIM-016 — Fixed real-time world cycle terminates in loop reset

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after the repeating simulation begins, its world continues to
  evolve while player input remains available until an authored fixed-duration
  terminal event ends the current iteration and starts the next one.
- Includes: Outer Wilds' approximately 22-minute post-pairing solar-system cycle
  ending in the supernova and a new campfire awakening.
- Excludes: a timer that merely scores performance; a work-shift cutoff that
  leaves the current case open; a resettable automatic run locked against input.
- Parameters: cycle start, duration, pause policy, terminal event, alternate
  early-death trigger and next-iteration delay.
- Evidence: [Outer Wilds decomposition](../games/m-r/outer-wilds.md).
- Novelty: not assessed.

## TIM-017 — Advance authoritative time while the player is absent

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the shared world continues under server time while one player is
  disconnected, so upkeep, decay, sleepers and adversarial actions may change
  that player's recoverable state before return.
- Includes: Rust offline persistence and raiding within a wipe cycle.
- Excludes: a paused single-player world; active real-time choice while logged
  in; deletion at the scheduled wipe itself.
- Parameters: disconnect interval, server tick, sleeper, upkeep, decay, hostile
  action and reconnect state.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## TIM-018 — Alternate sequential multi-command civilization turns

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: one civilization at a time receives an open decision interval in
  which it may issue any legal subset of unit, city, economy, research and
  diplomacy commands; End Turn commits settlement and passes authority to the
  next civilization in sequence.
- Includes: Rome followed by the three fixed AI rivals in scoped Civilization VI.
- Excludes: one-action alternating turns; simultaneous hidden orders; a live
  world that advances while the player deliberates.
- Parameters: participant order, turn number, command set, optional omissions,
  settlement, refresh and next participant.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`; earlier turn genes bound one action,
  one phase or simultaneous commitment rather than a whole empire command set.
