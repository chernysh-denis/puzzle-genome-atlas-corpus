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
  player and hostile state advancement.
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
  [Shogun Showdown decomposition](../games/s-z/shogun-showdown.md).
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
  inspecting, extracting terms and revising the event Scroll in The Case of the
  Golden Idol.
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
  [Return of the Obra Dinn decomposition](../games/m-r/return-of-the-obra-dinn.md),
  [Gorogoa decomposition](../games/g-l/gorogoa.md), and
  [Patrick's Parabox decomposition](../games/m-r/patricks-parabox.md), and
  [The Witness decomposition](../games/s-z/the-witness.md),
  [Carto decomposition](../games/a-f/carto.md), and
  [The Case of the Golden Idol decomposition](../games/s-z/the-case-of-the-golden-idol.md).
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
  live.
- Excludes: a discrete input followed by completed automatic resolution;
  self-paced actions with no time-driven state change; an external timer that
  only measures performance.
- Parameters: update frequency, input-repeat timing, pause rule and speed
  progression. A pause command may provide unbounded planning time without
  changing the fact that running simulation time independently mutates state.
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
  [The Swapper decomposition](../games/s-z/the-swapper.md), and
  [Viewfinder decomposition](../games/s-z/viewfinder.md).
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
  primed hostile attacks and the next hand.
- Excludes: one player input followed immediately by full resolution;
  alternating moves selected by two human decision-makers; simultaneous hidden
  planning.
- Parameters: commands per phase, intra-phase order, resolution order and undo
  availability.
- Evidence: [Into the Breach decomposition](../games/g-l/into-the-breach.md)
  and [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md).
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
  and continuing with a different pose.
- Excludes: restarting a level from its initial state; undoing one discrete
  move in a self-paced puzzle; watching a non-interactive replay.
- Parameters: history horizon, rewind rate, restoration granularity, editable
  paused state and branch-commit rule.
- Evidence: [Tin Hearts decomposition](../games/s-z/tin-hearts.md) and
  [Timelie decomposition](../games/s-z/timelie.md), and
  [Braid decomposition](../games/a-f/braid.md),
  [Pikmin 4 decomposition](../games/m-r/pikmin-4.md), and
  [Viewfinder decomposition](../games/s-z/viewfinder.md).
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

## TIM-009 — Self-paced route design before locked one-shot traversal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player authors one complete spatial route without time
  pressure, then starts one deterministic traversal during which route edits
  remain unavailable until the vehicle succeeds, fails, stops or is reset.
- Includes: drawing a Cosmic Express entrance-to-exit track, starting the train
  and revising the route only after the run finishes or is reset.
- Excludes: editing a network while vehicles continue running; a cyclic machine
  repeatedly executing an instruction schedule; one discrete input followed by
  one immediate automatic response.
- Parameters: route-completion requirement, start control, execution speed,
  pause / stop permission, reset state and success / failure boundary.
- Evidence: [Cosmic Express decomposition](../games/a-f/cosmic-express.md).
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
