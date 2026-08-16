# Information Genes

## INF-001 — Fully visible current state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: every decision-relevant element of the current board is visible
  before the player acts.
- Includes: the complete tile layout and values on the standard 2048 board; all
  Rubik's Cube stickers, inspectable by changing viewpoint before a move; the
  settled field and active tetromino in NES Tetris; every given, empty cell and
  player assignment in a printed Sudoku; all walls, goals, crates and the
  keeper in a Sokoban level; every card and its current zone in FreeCell; every
  Nonogram clue and current cell assignment; the current Royal Match board,
  level targets and remaining move count; every visible Water Sort layer and
  empty tube slot; current Into the Breach units, terrain, health and markers;
  every current card and empty cell on the Threes board; Dorfromantik's placed
  landscape, current tile, visible preview and remaining stack count; every
  rope, anchor, star, the candy and Om Nom in a Cut the Rope level; Opus
  Magnum's placed components, instruction rows, atoms, bonds and mechanism
  poses during editing and testing; World of Goo's terrain, hazards, pipe,
  loose population, connected structure and extraction count; Bad North's
  current island terrain, squads, enemies, houses and incoming longships; Loop
  Hero's current route, hero state, known enemies, held cards, equipment
  inventory and accumulated resources; HUMANITY's trial geometry, crowd,
  placed commands, enabled commands and goal fill; Tin Hearts' room geometry,
  soldiers, routing devices, hazards, exit and rescued progress; Timelie's
  current maze, actors, robots, doors and scheduled command state; SpaceChem's
  routes, symbols, waldos, atoms, bonds, ports and current fault state;
  Portal's chamber, cubes, buttons, hazards and apertures; Braid's current Tim,
  enemy, platform, key, gate, switch and puzzle-piece state; Pikmin 4's current
  leaders, followers, targets, routes, tasks and day clock; Patrick's Parabox's
  inspectable current grids, occupants, goals and containment relations;
  Cosmic Express's fixed grid, route, passengers, homes and carriage capacity;
  The Swapper's room geometry, bodies, coloured fields, mechanisms and orb;
  Carto's acquired map fragments, terrain edges, current arrangement, avatar
  location and corresponding traversable world regions; Viewfinder's current
  world geometry, held source image, placement plane, avatar and teleporter;
  Fights in Tight Spaces' current arena, occupants, health, hand, momentum and
  primed hostile indicators; A
  Good Snowman Is Hard to Build's monster, walls, remaining snow, ball sizes
  and ordered stacks; Snakebird's fixed terrain, fruit, exit state and ordered
  body segments; The Case of the Golden Idol's inspectable tableau, extracted
  terms and current Thinking-panel assignments; every platform, barrier, target
  cell and ordered body segment in a scoped Can of Wormholes stage; the local
  A Monster's Expedition land, water, stopper, log pose and target shore; every
  current trigger, line, hook, crossing and linkage in scoped HOOK levels; all
  LYNE endpoints, typed waypoints, nexus capacities and current route segments;
  all 25 current lit or unlit states on a Lights Out field; every Slant clue,
  empty cell and assigned diagonal; every Tents tree, side quota and current
  tent or non-tent assignment; every Dominosa digit and current selected or
  rejected pair; every Bridges island clue and current single or double bridge;
  every Light Up wall, clue, bulb and currently illuminated white cell; every
  Loopy dot, face clue and current edge mark; every Map boundary, immutable
  colour and current editable-region assignment; every Galaxies cell, centre
  dot and current boundary mark; every Filling cell, immutable digit and
  current editable-cell assignment; every Keen cage, operation, target and
  current digit; every Pearl clue and selected link; every Signpost arrow,
  immutable number, current successor link and derived chain label; every Net
  tile shape, orientation, lock and centre-connected component highlight; every
  Netslide tile mask, current position, fixed barrier and connected highlight;
  Machinarium's currently exposed scrapyard objects, Josef configuration,
  acquired inventory and prepared pole state; The Longest Journey's current
  constituent or composite inventory identities, exposed ducky subpart and
  visible track-key target; Day of the Tentacle's current held ingredients and
  constructed battery on Red Edison's shelf; Monument Valley's current Ida
  position, fixed route surfaces, rotating bridge pose and final pedestal;
  Maquette's current model, corresponding courtyards, key pose, gaps, doors and
  house state.
- Excludes: knowledge of future random events.
- Parameters: simultaneous display versus sequential inspection.
- Evidence: [2048 decomposition](../games/0-9/2048.md) and
  [Rubik's Cube decomposition](../games/m-r/rubiks-cube.md), and
  [Tetris decomposition](../games/s-z/tetris.md), and
  [Sudoku decomposition](../games/s-z/sudoku.md), and
  [Sokoban decomposition](../games/s-z/sokoban.md), and
  [FreeCell decomposition](../games/a-f/freecell.md), and
  [Nonogram decomposition](../games/m-r/nonogram.md), and
  [Royal Match decomposition](../games/m-r/royal-match.md), and
  [Water Sort decomposition](../games/s-z/water-sort.md), and
  [Chess decomposition](../games/a-f/chess.md), and
  [Flow Free decomposition](../games/a-f/flow-free.md), and
  [Baba Is You decomposition](../games/a-f/baba-is-you.md), and
  [Lights Out decomposition](../games/g-l/lights-out.md), and
  [Into the Breach decomposition](../games/g-l/into-the-breach.md), and
  [Threes decomposition](../games/s-z/threes.md), and
  [Mini Metro decomposition](../games/m-r/mini-metro.md), and
  [Peg Solitaire decomposition](../games/m-r/peg-solitaire.md), and
  [Dorfromantik decomposition](../games/a-f/dorfromantik.md), and
  [Cut the Rope decomposition](../games/a-f/cut-the-rope.md), and
  [Opus Magnum decomposition](../games/m-r/opus-magnum.md), and
  [Lemmings decomposition](../games/g-l/lemmings.md), and
  [World of Goo decomposition](../games/s-z/world-of-goo.md), and
  [Bad North decomposition](../games/a-f/bad-north.md), and
  [Loop Hero decomposition](../games/g-l/loop-hero.md), and
  [HUMANITY decomposition](../games/g-l/humanity.md), and
  [Tin Hearts decomposition](../games/s-z/tin-hearts.md), and
  [Timelie decomposition](../games/s-z/timelie.md), and
  [SpaceChem decomposition](../games/s-z/spacechem.md),
  [Portal decomposition](../games/m-r/portal.md), and
  [Braid decomposition](../games/a-f/braid.md), and
  [Pikmin 4 decomposition](../games/m-r/pikmin-4.md), and
  [Patrick's Parabox decomposition](../games/m-r/patricks-parabox.md), and
  [Cosmic Express decomposition](../games/a-f/cosmic-express.md), and
  [The Swapper decomposition](../games/s-z/the-swapper.md),
  [Carto decomposition](../games/a-f/carto.md), and
  [Viewfinder decomposition](../games/s-z/viewfinder.md), and
  [A Good Snowman Is Hard to Build decomposition](../games/a-f/a-good-snowman-is-hard-to-build.md),
  [Snakebird decomposition](../games/s-z/snakebird.md), and
  [The Case of the Golden Idol decomposition](../games/s-z/the-case-of-the-golden-idol.md),
  [Can of Wormholes decomposition](../games/a-f/can-of-wormholes.md), and
  [A Monster's Expedition decomposition](../games/a-f/a-monsters-expedition.md),
  and [Tactical Breach Wizards decomposition](../games/s-z/tactical-breach-wizards.md),
  and [KAMI decomposition](../games/g-l/kami.md), and
  [HOOK decomposition](../games/g-l/hook.md),
  [LYNE decomposition](../games/g-l/lyne.md), and
  [Hexologic decomposition](../games/g-l/hexologic.md), and
  [Rush Hour decomposition](../games/m-r/rush-hour.md), and
  [SET decomposition](../games/s-z/set.md), and
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
  [Netslide decomposition](../games/m-r/netslide.md),
  [Machinarium decomposition](../games/m-r/machinarium.md), and
  [The Longest Journey decomposition](../games/s-z/the-longest-journey.md), and
  [Day of the Tentacle decomposition](../games/a-f/day-of-the-tentacle.md), and
  [Stardew Valley decomposition](../games/s-z/stardew-valley.md), and
  [The Talos Principle decomposition](../games/s-z/the-talos-principle.md),
  [Fez decomposition](../games/a-f/fez.md),
  [Echochrome decomposition](../games/a-f/echochrome.md),
  [Monument Valley decomposition](../games/m-r/monument-valley.md), and
  [Superliminal decomposition](../games/s-z/superliminal.md), and
  [Manifold Garden decomposition](../games/m-r/manifold-garden.md), and
  [Maquette decomposition](../games/m-r/maquette.md), and
  [Antichamber decomposition](../games/a-f/antichamber.md).
- Novelty: not assessed.

## INF-002 — Unpreviewed random future event

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the next random state change is not revealed before the action
  that triggers it.
- Includes: both the value and position of the next 2048 tile; the types of
  Royal Match items that will refill vacated board cells; Mini Metro's next
  station opening and passenger arrival before the system selects them; Loop
  Hero's next random dawn spawn, card reward opportunity and loot identity.
- Excludes: a preview queue or deterministic future state.
- Evidence: [2048 decomposition](../games/0-9/2048.md) and
  [Royal Match decomposition](../games/m-r/royal-match.md), and
  [Mini Metro decomposition](../games/m-r/mini-metro.md), and
  [Loop Hero decomposition](../games/g-l/loop-hero.md).
- Novelty: not assessed; this is part of the baseline genome.

## INF-003 — Fixed concealed current state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: decision-relevant contents already exist in the current state but
  remain inaccessible until an information-revealing action occurs.
- Includes: fixed mine locations under covered Minesweeper cells; a fixed
  concealed Mastermind code or Wordle answer tested by successive guesses; the current concealed
  order of Balatro's remaining draw pile while the hand and remaining deck
  composition are inspectable; the current concealed order of Fights in Tight
  Spaces' draw pile while the visible hand and deck contents constrain future
  card availability; The Room's authored items and mechanisms behind unopened
  covers, plates and locks.
- Excludes: a future random event not yet selected; an inspectable element that
  is merely offscreen; information the player once saw and forgot.
- Parameters: setup distribution, known global content count, first-action
  conditioning and reveal permanence.
- Evidence: [Minesweeper decomposition](../games/m-r/minesweeper.md),
  [Mastermind decomposition](../games/m-r/mastermind.md),
  [Wordle decomposition](../games/s-z/wordle.md), and
  [Balatro decomposition](../games/a-f/balatro.md), and
  [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md),
  and [The Room decomposition](../games/s-z/the-room.md).
- Novelty: not assessed.

## INF-004 — Exact local aggregate clue

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a visible clue position reports the exact aggregate count of
  positions belonging to one fixed concealed target class in its declared
  local neighbourhood.
- Includes: Minesweeper mine clues from 0 through 8 on a square grid; Hexcells
  Infinite black clues counting adjacent blue cells on a hex grid.
- Excludes: approximate hints; the global remaining-hazard count alone; direct
  identification of which neighbouring position belongs to the target class;
  a whole-line ordered run description.
- Parameters: target class, neighbourhood topology, clue range and display
  convention.
- Evidence: [Minesweeper decomposition](../games/m-r/minesweeper.md) and
  [Hexcells Infinite decomposition](../games/g-l/hexcells-infinite.md).
- Novelty: not assessed.

## INF-005 — Exact ordered successor preview

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player is shown the exact identities and order of one or more
  elements already scheduled to become available next.
- Includes: the enabled-by-default one-piece `NEXT` tetromino display in NES
  Tetris; the ordered five-piece pipe dispenser in Pipe Dream; Dorfromantik's
  visible current tile and ordered successor preview.
- Excludes: showing only a probability distribution or category; revealing no
  future element; an unordered set that does not identify which element is
  next.
- Parameters: preview depth, visibility control and displayed attributes.
- Evidence: [Tetris decomposition](../games/s-z/tetris.md) and
  [Pipe Mania decomposition](../games/m-r/pipe-mania.md), and
  [Dorfromantik decomposition](../games/a-f/dorfromantik.md).
- Novelty: not assessed.

## INF-006 — Visible ordered run-length description

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each declared line exposes the exact ordered sequence of lengths
  of its filled contiguous runs while withholding the runs' absolute positions.
- Includes: a Nonogram row clue `3 1 2`, meaning a run of three, then one, then
  two in that order with separation.
- Excludes: an unordered total of filled cells; exact local hazard counts; a
  fully specified target image; clues concealed until later play.
- Parameters: line orientation, run count, run lengths and whether colours are
  encoded.
- Evidence: [Nonogram decomposition](../games/m-r/nonogram.md).
- Novelty: not assessed.

## INF-007 — Public action-history state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: every participant observes the action sequence, and retained
  facts from that public history remain decision-relevant even when the current
  spatial arrangement does not encode them.
- Includes: knowing chess castling and en-passant rights, repetition history and
  the sequence relevant to automatic draw counters.
- Excludes: concealed actions; private hands; future random events; information
  derivable entirely from the visible current arrangement.
- Parameters: record persistence, remembered event classes and whether a formal
  move record is available.
- Evidence: [Chess decomposition](../games/a-f/chess.md).
- Novelty: not assessed.

## INF-008 — Visible executable rule syntax

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the current mechanical rules are disclosed through visible,
  spatially arranged symbols whose syntactic configuration determines which
  rules are active.
- Includes: visible noun, `IS` and property word blocks in Baba Is You.
- Excludes: static instructional prose; hidden rules learned only by trial;
  visible objects whose arrangement changes state but not rule syntax.
- Parameters: symbol language, reading directions, grammar and separate active
  rule display.
- Evidence: [Baba Is You decomposition](../games/a-f/baba-is-you.md).
- Novelty: not assessed.

## INF-009 — Exact committed hostile-intent preview

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before the player acts, every hostile unit's already committed
  action exposes its acting unit, target positions, effect and relative
  execution order.
- Includes: Into the Breach attack arrows, damage indicators and attack-order
  display; Fights in Tight Spaces primed-attack ranges, effects and displayed
  enemy order.
- Excludes: predicting an opponent's not-yet-chosen move; a probability
  distribution over possible attacks; previewing only the next falling piece.
- Parameters: preview horizon, displayed effect attributes, order display and
  cancellation visibility.
- Evidence: [Into the Breach decomposition](../games/g-l/into-the-breach.md)
  and [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md).
- Novelty: not assessed.

## INF-010 — Category-bounded next-element preview

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before the next action, the player sees a category that contains
  the successor element but may withhold its exact identity and insertion
  position.
- Includes: Threes showing an exact coloured base card or a white / `+`
  high-card category while leaving the eligible entry lane unresolved.
- Excludes: an exact successor identity (`INF-005`); no preview of the next
  random event (`INF-002`); a probability distribution with no guaranteed
  category.
- Parameters: category vocabulary, exact base-card exceptions, candidate value
  range and whether position is disclosed.
- Evidence: [Threes decomposition](../games/s-z/threes.md).
- Novelty: not assessed.

## INF-011 — Exact visible input-output assembly schema

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before construction begins, the puzzle discloses the exact
  identities, relations and acceptance-relevant geometry of every supplied
  input assembly and required output product, whether the transformation is
  performed directly or through an executing machine.
- Includes: Opus Magnum's visible input and output molecular diagrams;
  SpaceChem's visible reagent and required product bond structures, with screen
  orientation ignored where acceptance uses graph equivalence; Infinifactory's
  visible input and target voxel arrangements with required output orientation;
  inbento's complete typed piece footprints and per-cell recipe.
- Excludes: revealing only a target score or category; hidden transformation
  rules; visibility of material currently moving through the machine.
- Parameters: input and output count, identity vocabulary, relation or bond
  representation, spatial geometry, orientation and equivalence rule.
- Evidence: [Opus Magnum decomposition](../games/m-r/opus-magnum.md) and
  [SpaceChem decomposition](../games/s-z/spacechem.md), and
  [Infinifactory decomposition](../games/g-l/infinifactory.md), and
  [inbento decomposition](../games/g-l/inbento.md).
- Novelty: not assessed.

## INF-012 — Scene-indexed revisitable fixed evidence

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: decision-relevant facts are distributed across a finite set of
  named, immutable scenes that become selectively accessible, remain stable
  across visits and can be cross-referenced after discovery.
- Includes: Return of the Obra Dinn death memories, their transcripts, depicted
  participants and book links between a person and scenes where they appear.
- Excludes: concealed contents revealed permanently by one action; a random
  future event; every relevant fact being simultaneously visible in the
  current scene.
- Parameters: scene-discovery order, indexing metadata, transcript availability,
  bookmarks and revisit path.
- Evidence: [Return of the Obra Dinn decomposition](../games/m-r/return-of-the-obra-dinn.md).
- Novelty: not assessed.

## INF-013 — Finite identity roster with disclosed role metadata

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the puzzle exposes a complete finite list of candidate identities
  and structured attributes while withholding the mapping from those labels to
  the subjects observed in evidence.
- Includes: the Obra Dinn manifest listing names, occupations and nationalities
  alongside an illustration containing the sixty faces.
- Excludes: an unknown population whose candidate names emerge gradually; a
  complete disclosed identity-to-face mapping; an unlabelled set of hazards.
- Parameters: roster size, metadata fields, portrait grouping and whether
  confirmed identities are eliminated from unresolved choices.
- Evidence: [Return of the Obra Dinn decomposition](../games/m-r/return-of-the-obra-dinn.md).
- Novelty: not assessed.

## INF-014 — Navigable nested panel scene graph

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each visible panel is one node in a deterministic illustrated
  scene graph; visible focus or navigation affordances disclose routes to other
  views, but only the current node per panel is displayed at once.
- Includes: Gorogoa hiding deeper pictures, rooms, frames and alternate crops
  behind zoom-in, zoom-out and pan transitions in each of four panels.
- Excludes: a finite set of separately indexed evidence scenes; exact successor
  preview; concealed content exposed permanently by one reveal.
- Parameters: graph depth, branching, affordance visibility, backtracking and
  simultaneous panel count.
- Evidence: [Gorogoa decomposition](../games/g-l/gorogoa.md).
- Novelty: not assessed.

## INF-015 — Prospective structural-link preview

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before a held live structural node is committed, the interface
  shows the exact connection topology that the current position would create
  while leaving later force response or operational load unresolved.
- Includes: World of Goo guidelines displaying prospective strands from a held
  Goo Ball to nearby structural nodes.
- Excludes: previewing a supplied successor element; displaying only generic
  placement validity; predicting the complete physical deformation after
  commitment.
- Parameters: previewed neighbour set, link count, validity colour and whether
  geometry updates continuously during drag.
- Evidence: [World of Goo decomposition](../games/s-z/world-of-goo.md).
- Novelty: not assessed.

## INF-016 — Visible carrier-arrival telegraph

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a currently visible in-world carrier and its approach disclose a
  future boundary region where a transported group will enter active play,
  while leaving those occupants' later targets and effects unresolved.
- Includes: an approaching Bad North Viking longship giving advance warning of
  the shore region at which its group will land.
- Excludes: an exact committed action for every hostile unit; an abstract spawn
  marker with no carrier transit; an unpreviewed random insertion.
- Parameters: visible approach horizon, landing-region precision, payload
  visibility, speed readability and route variability.
- Evidence: [Bad North decomposition](../games/a-f/bad-north.md).
- Novelty: not assessed.

## INF-017 — Prospective autonomous-route projection

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before paused autonomous traversal resumes, the interface draws
  the predicted route through the current routing surfaces or devices.
- Includes: Tin Hearts' projected soldier path updating after a prism block is
  repositioned or rotated while time is frozen.
- Excludes: prospective structural links alone; a carrier-arrival region; a
  guarantee of the complete future state of multiple colliding bodies.
- Parameters: projection horizon, device classes represented, collision detail,
  update latency and whether uncertainty is displayed.
- Evidence: [Tin Hearts decomposition](../games/s-z/tin-hearts.md).
- Novelty: not assessed.

## INF-018 — Exact scrubbed future-state preview

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: moving a time cursor forward exposes the complete deterministic
  world states that the current command schedule would produce, including
  actor, hostile and interactive-object consequences up to a terminal boundary.
- Includes: seeking forward in Timelie to observe patrol positions, character
  paths, door states, pursuit and capture under the current plan.
- Excludes: a drawn route without resolved world consequences; one committed
  hostile action preview; a prerecorded replay that cannot inform revision.
- Parameters: preview horizon, state fidelity, seek granularity, failure cutoff,
  hidden variables and update behaviour after plan edits.
- Evidence: [Timelie decomposition](../games/s-z/timelie.md).
- Novelty: not assessed.

## INF-019 — Live cross-portal scene view

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an active portal surface continuously displays the scene visible
  from its paired endpoint under the corresponding transformed viewpoint,
  before the player or an object crosses it.
- Includes: looking through a Portal aperture to inspect its exit side, hazards
  or the player character from the remote viewpoint.
- Excludes: a symbolic destination label; a route-only future projection; a
  prerecorded camera view that does not update with the current world.
- Parameters: recursion depth, field of view, occlusion, update latency,
  displayed body classes and incomplete-pair presentation.
- Evidence: [Portal decomposition](../games/m-r/portal.md).
- Novelty: not assessed.

## INF-020 — Visible rewind-affinity marking

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before temporal manipulation, a persistent visual treatment
  identifies which current entities will not restore with ordinary world state
  when the player rewinds.
- Includes: Braid's green glow on time-immune keys, doors, switches, platforms
  or enemies.
- Excludes: discovering immunity only after testing; an exact preview of every
  future state; colour that has no rule consequence.
- Parameters: marked affinity classes, animation, visibility range, inheritance
  by carried objects and mixed-affinity composite mechanisms.
- Evidence: [Braid decomposition](../games/a-f/braid.md).
- Novelty: not assessed.

## INF-021 — Visible cooperative-work capacity state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before and during cooperative work, the interface exposes the
  target's required capacity and the currently committed workers or strength,
  making the threshold for starting and accelerating the task inspectable.
- Includes: Pikmin 4 showing a treasure's carrying requirement and the current
  Pikmin / Oatchi carrying strength assigned to it.
- Excludes: an undisclosed capacity learned only by failed assignment; generic
  follower headcount; a prospective route projection after work begins.
- Parameters: unit count versus weighted strength, maximum assignment, speed
  indication, target lock display and mixed-worker contribution.
- Evidence: [Pikmin 4 decomposition](../games/m-r/pikmin-4.md).
- Novelty: not assessed.

## INF-022 — Nested-space view with parent-boundary context

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while one contained space is expanded as the active local view,
  the interface simultaneously retains the relevant surrounding parent
  geometry and boundary correspondence needed to judge whether outward transfer
  is currently possible.
- Includes: Patrick's Parabox enlarging a box interior while leaving its parent
  context visible around the box, including walls that block a proposed exit.
- Excludes: a view showing only the active interior; selectable hidden nodes of
  an illustrated scene graph; a live view through a paired portal endpoint.
- Parameters: parent depth shown, scale, occlusion, boundary highlights,
  recursive rendering depth and focus transition.
- Evidence: [Patrick's Parabox decomposition](../games/m-r/patricks-parabox.md).
- Novelty: not assessed.

## INF-023 — Post-commit violated-clue indication

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a submitted complete answer is rejected, the interface
  identifies at least one currently violated clue instance or rule location
  without displaying a corrected answer.
- Includes: an invalid The Witness panel submission blinking implicated square
  clues red while leaving the player to infer a valid partition.
- Excludes: a generic failure sound with no located cause; highlighting illegal
  geometry continuously before submission; revealing the complete solution;
  merely keeping all current clues visible.
- Parameters: indicated violation subset, delay, duration, ordering, ambiguous
  responsibility, repeated submissions and accessibility channel.
- Evidence: [The Witness decomposition](../games/s-z/the-witness.md).
- Novelty: not assessed.

## INF-024 — Persistent extracted phrase bank with answer scaffold

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: terms explicitly collected from distributed case evidence remain
  visible as a reusable hypothesis vocabulary alongside a partially written
  structured answer whose fixed text signals possible semantic roles.
- Includes: The Case of the Golden Idol retaining names and place words at the
  bottom of its Thinking screen while the event Scroll supplies grammatical
  context around blank slots.
- Excludes: a complete candidate identity roster disclosed before exploration;
  unstructured personal notes; clues that remain only at their original scene
  locations; feedback identifying a violated answer slot.
- Parameters: bank grouping, found / missing indicator, fixed scaffold text,
  phrase categories, sorting and cross-panel availability.
- Evidence: [The Case of the Golden Idol decomposition](../games/s-z/the-case-of-the-golden-idol.md).
- Novelty: not assessed.

## INF-025 — Exact reactive hostile-consequence preview

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before tactical commit, the interface exposes the exact hostile
  attacks and immediate resulting state computed from the player's current
  tentative actions, and updates that disclosure when the draft changes.
- Includes: Tactical Breach Wizards Foresee showing who current enemies will
  attack and the damage / displacement outcome of the current turn draft.
- Excludes: hostile actions already committed before the player acts; a
  probability distribution; a route-only projection; random-access scrubbing
  across a multi-time deterministic world trajectory.
- Parameters: displayed actors, targets and effects, simulation depth, target-
  update timing, order display and failure-state detail.
- Evidence: [Tactical Breach Wizards decomposition](../games/s-z/tactical-breach-wizards.md).
- Novelty: not assessed.

## INF-026 — Visible local target-contiguity qualifier

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a visible qualifier on an exact local target-count clue states
  that all counted target-class neighbours form one contiguous run in the
  clue's declared neighbourhood order.
- Includes: braces around a Hexcells Infinite black clue stating that its
  counted adjacent blue cells are consecutive around the hexagonal ring.
- Excludes: an unqualified exact local count; ordered run lengths spanning a
  complete row or column; a qualifier stating that target neighbours are
  separated rather than contiguous.
- Parameters: neighbourhood order, cyclic-versus-linear adjacency, target
  class, run count and notation.
- Evidence: [Hexcells Infinite decomposition](../games/g-l/hexcells-infinite.md).
- Novelty: not assessed.

## INF-027 — Exact next hostile-step preview

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before the next player action, the interface identifies each
  hostile unit's exact next automatic behavioural step and the attack geometry
  when that step is an attack.
- Includes: Shogun Showdown showing whether an enemy will move, prepare an
  attack or execute its currently queued attack after the player's turn.
- Excludes: a complete hostile attack committed before a multi-action planning
  phase; a learned but undisplayed later behaviour pattern; a probability over
  possible responses.
- Parameters: preview horizon, displayed movement direction, attack footprint,
  damage, response order and update timing after displacement.
- Evidence: [Shogun Showdown decomposition](../games/s-z/shogun-showdown.md).
- Novelty: not assessed.

## INF-028 — Visible weighted origin-destination demand

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before network construction or evaluation, the interface exposes
  which authored entrances require routes to which exits and visibly encodes
  their relative traffic frequencies.
- Includes: selecting a Freeways road sign or building to inspect its required
  destination arrows and their relative sizes.
- Excludes: unpreviewed demand generated during play; destination identity
  inferred only after a vehicle moves; exact future vehicle spawn times.
- Parameters: endpoint classes, direction convention, weight granularity and
  whether reciprocal demand is shown separately.
- Evidence: [Freeways decomposition](../games/a-f/freeways.md).
- Novelty: not assessed.

## INF-029 — Visible exact directional line-sum clue

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a visible clue identifies one fixed directional line of
  assignable positions and discloses the exact arithmetic sum their completed
  numeric values must equal without disclosing each individual value.
- Includes: a Hexologic edge number and arrow identifying one horizontal or
  diagonal line whose one-to-three-pip cells must add to that number.
- Excludes: an exact count of concealed members of one class in a local
  neighbourhood; ordered run lengths; a fully specified per-position target;
  an inequality or approximate total; score accumulated from past actions.
- Parameters: line orientation, member positions, target range, arrow notation,
  clue visibility and whether every geometric line is clued.
- Evidence: [Hexologic decomposition](../games/g-l/hexologic.md).
- Novelty: not assessed.

## INF-031 — Persistent partitioned hypothesis-match counts

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after each complete ordered hypothesis, the interface retains
  that proposal with two exact aggregate counts: symbols matched at the same
  position and additional symbols matched only by identity, without revealing
  which positions produced the second count.
- Includes: Mastermind retaining every four-peg guess beside unordered exact-
  position and wrong-position indicator totals.
- Excludes: revealing the target symbols or their positions; one undivided
  similarity score; identifying a specific violated clue; feedback that
  disappears before the next hypothesis can be compared with it.
- Parameters: history depth, count notation, exact / residual labels, indicator
  ordering, accessibility channel and whether zero counts use blanks.
- Evidence: [Mastermind decomposition](../games/m-r/mastermind.md).
- Novelty: not assessed.

## INF-032 — Persistent indirect probe outcome

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after a probe into a concealed spatial system, the interface
  permanently labels its boundary entry with the exact categorical result and,
  when the probe exits elsewhere, links both boundary positions as one paired
  observation without exposing the internal route.
- Includes: Black Box retaining `H`, `R` or a matching numbered entry / exit
  pair around the arena.
- Excludes: revealing the concealed cells traversed; a local count attached to
  one interior cell; feedback that disappears before the next query; a score
  with no identified probe origin.
- Parameters: outcome vocabulary, pair notation, persistence, accessibility
  channel and whether already used exits may be selected.
- Evidence: [Black Box decomposition](../games/a-f/black-box.md).
- Novelty: not assessed.

## INF-030 — Live exact-subconstraint satisfaction indication

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before full answer submission, the interface continuously marks
  one declared local constraint as currently satisfied exactly while making no
  claim that its internal assignments are compatible with all other
  constraints or belong to the final solution.
- Includes: Hexologic turning one arrow-line border green when its current pip
  total equals the displayed target even though an intersecting line may force
  those values to be rearranged.
- Excludes: marking a violated clue only after a rejected complete submission;
  revealing corrected values; generic success feedback; highlighting a legal
  action whose local completion predicate is still false.
- Parameters: predicate type, update timing, satisfied-state notation,
  persistence, animation and accessibility channel.
- Evidence: [Hexologic decomposition](../games/g-l/hexologic.md).
- Novelty: not assessed.

## INF-033 — Transient ordered-cue presentation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the system exposes a complete target sequence one cue at a time
  in ordinal order, but does not leave a persistent symbolic record of earlier
  cues available during the subsequent reproduction decision.
- Includes: Simon flashing the current light sequence serially before the
  player echoes it from memory; sound may redundantly identify the same pads.
- Excludes: a persistent preview queue; simultaneously visible target symbols;
  a concealed sequence known only through aggregate query feedback; an
  unpreviewed future event.
- Parameters: cue channels, presentation duration, inter-cue interval,
  persistence, replay count and accessibility redundancy.
- Evidence: [Simon decomposition](../games/s-z/simon.md).
- Novelty: not assessed.

## INF-034 — Persistent position-addressed ternary hypothesis feedback

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after each accepted complete sequence query, the interface
  retains the proposal and labels every guessed position as an exact-position
  match, a duplicate-limited identity match elsewhere, or absent after all
  target occurrences have been consumed.
- Includes: Wordle keeping every guessed word as green, yellow and grey tiles,
  including grey excess copies of a letter that has already received all
  available exact or residual credit.
- Excludes: two aggregate exact / misplaced counts; a transient correctness
  signal; per-position equality only with no present-elsewhere category; full
  target reveal.
- Parameters: category labels, colour-independent accessibility channel,
  history depth, duplicate notation and whether absent and exhausted share one
  visible class.
- Evidence: [Wordle decomposition](../games/s-z/wordle.md).
- Novelty: not assessed.

## INF-035 — Instrument-gated alternate visual layer

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: decision-relevant markings over one persistent mechanism state
  are unavailable in ordinary view and become visible only while an acquired
  inspection instrument is active, without that viewing mode itself changing
  the underlying mechanism.
- Includes: The Room's completed eyepiece revealing the hidden alignment trace
  over the exposed front rings.
- Excludes: an inspectable object merely being offscreen; permanent compartment
  opening; random information generated by inspection; cosmetic colour grading
  with no rule consequence; a preview of future system motion.
- Parameters: required instrument and assembly state, target region, overlay
  persistence, toggle behaviour, simultaneous manipulation and reset scope.
- Evidence: [The Room decomposition](../games/s-z/the-room.md).
- Novelty: not assessed.

## INF-036 — Pictorial requested-item disclosure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: interacting with one addressed character exposes a persistent or
  repeatable non-verbal depiction of the exact item identity that character
  currently accepts, without revealing the full downstream solution chain.
- Includes: Machinarium's small scrapyard robot showing the high doll in its
  request bubble before the player retrieves and gives that item.
- Excludes: spoken flavour dialogue; a generic interaction icon; a complete
  walkthrough hint; an item–fixture match inferred only from shape; a reward
  shown only after the exchange.
- Parameters: requester, depicted item identity, display duration, repeatability,
  accessibility channel, request-state changes and ambiguity.
- Evidence: [Machinarium decomposition](../games/m-r/machinarium.md).
- Novelty: not assessed.

## INF-037 — Close inspection exposes manipulable held-item subpart

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: opening a dedicated close-up view of one acquired item reveals a
  previously unavailable addressed component whose direct manipulation changes
  that item's later mechanical compatibility.
- Includes: close inspection of The Longest Journey's rubber ducky exposing
  the removable Band-Aid that covers its leak.
- Excludes: enlarging artwork with no new action; viewing an already available
  mechanism from another angle; an inspection instrument revealing a separate
  world overlay; receiving a complete text hint.
- Parameters: item identity, inspection mode, exposed hotspot, manipulation,
  resulting state, persistence and accessibility alternative.
- Evidence: [The Longest Journey decomposition](../games/s-z/the-longest-journey.md).
- Novelty: not assessed.

## INF-038 — Addressed recipient discloses exact multi-item commission

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after one initiating interaction with an addressed recipient,
  the game explicitly names every distinct item type in the finite set that the
  recipient will accept to produce the declared result.
- Includes: Red Edison responding to Day of the Tentacle's patent application
  by requesting oil, vinegar and gold for the super-battery.
- Excludes: a picture of one requested item; an undisclosed recipe inferred by
  trial and error; vague flavour dialogue; a full walkthrough of how to acquire
  each ingredient; a numeric currency price.
- Parameters: recipient, initiating state, item labels, set cardinality,
  persistence or repeatability, accepted synonyms and accessibility channel.
- Evidence: [Day of the Tentacle decomposition](../games/a-f/day-of-the-tentacle.md).
- Novelty: not assessed.

## INF-039 — Visible typed collection schema and retained slot progress

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before each contribution, the interface displays the collection's
  eligible item identities, required quantities, quality thresholds, slot quota
  and which requirements have already been persistently filled.
- Includes: Stardew Valley's readable Boiler Room scrolls showing three bar
  slots, four mineral slots and two slots chosen from four monster-drop options,
  together with retained bundle progress.
- Excludes: a character verbally requesting one exact set; a crafting recipe
  with no persistent partial contribution state; acquisition-route guidance;
  an undisclosed target inferred only from rejected items.
- Parameters: collection hierarchy, item labels, quantities, quality markers,
  alternative quota, filled-state marker, remote progress access and
  accessibility representation.
- Evidence: [Stardew Valley decomposition](../games/s-z/stardew-valley.md).
- Novelty: not assessed.

## INF-040 — Visible gate-specific shape roster and arranger occupancy

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an addressed access barrier displays the exact coloured rigid
  piece identities it still requires, and its arranger exposes the complete
  finite piece inventory, board boundary, current orientations, occupied cells
  and remaining gaps before each placement decision.
- Includes: The Talos Principle's first A1 lock showing its green `L`, `J` and
  `Z` requirements and the 4 × 3 arranger showing every live placement.
- Excludes: a scalar key count with no identities; hidden target geometry;
  acquisition-route hints; a crafting recipe with no addressed spatial board.
- Parameters: roster identity, missing-state marker, board topology, footprint
  preview, occupancy display, invalid-placement feedback and accessibility form.
- Evidence: [The Talos Principle decomposition](../games/s-z/the-talos-principle.md).
- Novelty: not assessed.

## INF-041 — Rotation reveals depth between flattened traversal views

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the animated transition between two settled orthographic views
  temporarily exposes the relative depth and side arrangement that each flat
  endpoint collapses, then presents the new front-layer collision slice as the
  visible basis for the next movement decision.
- Includes: a Fez quarter-turn showing that two apparently aligned platforms
  occupy different world depths before the adjacent settled view exposes a new
  continuation.
- Excludes: free-camera inspection with no rule consequence; a static cutaway;
  hidden-state revelation unrelated to projection; an exact preview of every
  future movement outcome.
- Parameters: transition duration, intermediate layers, occlusion, silhouette,
  depth cues, reduced-motion alternative and settled-state indicator.
- Evidence: [Fez decomposition](../games/a-f/fez.md).
- Novelty: not assessed.

## INF-042 — Live projected path authority is visually disclosed

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the continuously updated screen image itself exposes the
  currently authoritative path joins and occlusions: apparent contact is shown
  as contact, while a discontinuity hidden by nearer geometry is absent from
  the traversal image used for the next decision.
- Includes: Echochrome showing when remote walkway ends line up and when a
  nearer element covers a gap before the Walker reaches that relation.
- Excludes: a hidden numeric topology table; a route forecast drawn ahead of
  an autonomous agent; a four-state transition animation; cosmetic perspective
  whose apparent joins have no rule consequence.
- Parameters: line clarity, depth cues, silhouette contrast, occlusion edge,
  alignment snap, reduced-motion presentation and update latency.
- Evidence: [Echochrome decomposition](../games/a-f/echochrome.md).
- Novelty: not assessed.

## INF-043 — Current reachable destinations are visibly marked

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the current settled navigation state visibly distinguishes the
  nodes or surfaces that can accept a destination command, and that reachable
  marking changes when architectural connectivity changes.
- Includes: Monument Valley highlighting nodes that Ida can reach in the
  current snap configuration and shifting those highlights after geometry
  moves.
- Excludes: a complete future-route overlay; decoration with no input meaning;
  hidden reachability discovered only after rejection; showing the current
  avatar location without marking selectable destinations.
- Parameters: marker form, contrast, focus state, path-versus-node scope,
  update latency, invalid-target feedback and reduced-motion presentation.
- Evidence: [Monument Valley decomposition](../games/m-r/monument-valley.md).
- Novelty: not assessed.

## INF-044 — Live perspective-held physical placement preview

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before release, the rendered held object continuously shows the
  exact current collision-bounded world position, orientation and scale that
  will become physical if committed, even though its projected screen extent
  remains stable while camera depth changes.
- Includes: Superliminal showing the Induction chess piece grow in world scale
  as it is aimed toward a distant wall and showing its current plate-relative
  pose before it is dropped.
- Excludes: a cursor with no object pose; a numeric size label; an image plane
  that will create different geometry; a route forecast; discovering scale or
  collision only after release.
- Parameters: silhouette, depth cues, contact shadow, target overlap, update
  latency, invalid-placement feedback, rotation preview and accessibility form.
- Evidence: [Superliminal decomposition](../games/s-z/superliminal.md).
- Novelty: not assessed.

## INF-045 — Gravity-frame colour and eligibility encoding

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the scene continuously uses one stable colour mapping to expose
  the currently selected orthogonal gravity frame, the colour a faced surface
  would acquire as floor, and which coloured portable bodies and fixtures are
  eligible in that frame.
- Includes: Manifold Garden tinting the current floor by gravity direction,
  showing the aimed wall's colour at the crosshair and matching red, blue or
  other cubes and switches to those directional frames.
- Excludes: colour used only for decoration; a hidden gravity vector; a numeric
  direction label with no object eligibility; colour identifying teams or
  score; a portal surface class unrelated to global down.
- Parameters: six-direction palette, current-frame indicator, aimed-surface
  preview, object and fixture marking, colour-blind alternative, contrast and
  transition timing.
- Evidence: [Manifold Garden decomposition](../games/m-r/manifold-garden.md).
- Novelty: not assessed.

## INF-046 — Simultaneous nested-scale correspondence display

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the current view exposes at least two recognisable nested scale
  instances of one world together, using homologous architecture and object
  silhouettes so the player can identify which locations and bodies share
  authoritative state across scale.
- Includes: Maquette showing the central model inside the normal courtyard and
  distinctive matching buildings, gaps, red block and golden key
  representations at different sizes.
- Excludes: a minimap whose symbols do not physically exist; sequential views
  with no retained parent context; identical decoration without causal linkage;
  a numeric scale label; periodic same-scale copies.
- Parameters: visible recursion depth, landmark distinctiveness, scale ratio,
  occlusion, correspondence highlight, update latency and reduced-detail
  rendering.
- Evidence: [Maquette decomposition](../games/m-r/maquette.md).
- Novelty: not assessed.

## INF-047 — Stable local threshold with concealed remote destination

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the current doorway, window or corridor mouth is visibly stable,
  but the identity of the remote room presently connected beyond it is not
  disclosed as a persistent map relation and must be revealed by a viewpoint
  change or traversal.
- Includes: Antichamber showing the same local `Now You See It` doorway before
  and after the off-screen change while withholding which authored room it now
  reaches until the player returns to inspect or cross it.
- Excludes: a live cross-portal view; a simultaneously visible recursive
  counterpart; a periodic copy whose translation is already legible; a hidden
  random outcome; a locked door whose fixed destination is known.
- Parameters: local threshold cues, destination disclosure moment, map support,
  preview depth, persistence, change feedback and accessibility alternative.
- Evidence: [Antichamber decomposition](../games/a-f/antichamber.md).
- Novelty: not assessed.

## INF-048 — Continuous curvature-rendered distance and direction cues

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live first-person scene renders landmarks, horizons and
  route directions through the same curved metric that resolves traversal, so
  apparent spacing, angular spread and accumulated orientation continuously
  expose consequences of curvature rather than a hidden graph label.
- Includes: Hyperbolica showing curved horizons, rapidly multiplying visible
  surroundings and route directions that shift while the avatar walks through
  the Maze of Apeirogon.
- Excludes: a flat minimap alone; cosmetic lens distortion over Euclidean
  collision; a live portal endpoint; an off-screen room remap; a static
  diagram of hyperbolic tiling outside play.
- Parameters: projection model, field of view, landmark density, horizon form,
  depth cue, distortion strength, motion smoothing and accessibility overlay.
- Evidence: [Hyperbolica decomposition](../games/g-l/hyperbolica.md).
- Novelty: not assessed.

## INF-049 — Player-centred finite projection of an unbounded tiling

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: play displays a finite projected neighbourhood around the
  player's current cell, shrinking more distant tiles toward the view boundary
  and allowing the view to recenter on the player while the underlying world
  continues beyond the generated radius.
- Includes: HyperRogue's standard Poincare-disc presentation and explicit view
  recentering over a lazily generated hyperbolic cell field.
- Excludes: a finite minimap; continuous first-person curved collision cues; a
  camera zoom over a flat finite board; decorative radial distortion; complete
  disclosure of an unbounded graph.
- Parameters: projection model, generated radius, visible radius, view centre,
  cell scaling, rotation, pan limit, recenter control and edge highlighting.
- Evidence: [HyperRogue decomposition](../games/g-l/hyperrogue.md).
- Novelty: not assessed.

## INF-050 — Complementary role-partitioned rules and live state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the complete decision procedure is split between human roles:
  one role can inspect the changing live object but lacks the authoritative
  rule reference, while another can inspect that reference but cannot see the
  object's current instance; only communicated descriptions combine them.
- Includes: Keep Talking and Nobody Explodes Defusers seeing bomb modules,
  timer, strikes and casing facts while Experts read the separate Bomb Defusal
  Manual without seeing the bomb.
- Excludes: one player switching between board and help screen; concealed state
  unknown to every role; optional secret information in an adversarial game;
  all collaborators seeing the same interface.
- Parameters: role count, state fields, rule pages, communication channel,
  persistent shared notes and whether any role may change between attempts.
- Evidence: [Keep Talking and Nobody Explodes decomposition](../games/g-l/keep-talking-and-nobody-explodes.md).
- Novelty: not assessed.

## INF-051 — Stable unknown glyph identity across contextual occurrences

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the same visually distinct but initially untranslated glyph
  recurs across world labels, dialogue or instructions with one stable semantic
  identity, letting separate contexts constrain a shared hypothesis.
- Includes: recurring Devotee signs for open, closed and door across the first
  lever, doorway and six-valve instruction in Chants of Sennaar.
- Excludes: a fresh random cipher each occurrence; translated text; ornamental
  marks with no stable meaning; information split between human roles.
- Parameters: glyph inventory, occurrence contexts, visual variants, language,
  morphology and when canonical translation becomes visible.
- Evidence: [Chants of Sennaar decomposition](../games/a-f/chants-of-sennaar.md).
- Novelty: not assessed.

## INF-052 — Persistent provisional glossary with illustrated validation cues

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a persistent player-facing notebook stores editable hypotheses
  beside discovered glyphs and later presents authored nonverbal illustrations
  that disclose the candidate semantic slots used to verify a bounded group.
- Includes: Chants of Sennaar's first journal page retaining notes and showing
  pictures for opening, closing and a door before the three-glyph match.
- Excludes: an external manual; a second player's private interface; automatic
  translation with no hypothesis state; a static glossary already solved.
- Parameters: retained annotations, illustration set, discovery threshold,
  page grouping, reveal timing, incorrect feedback and solved-state display.
- Evidence: [Chants of Sennaar decomposition](../games/a-f/chants-of-sennaar.md).
- Novelty: not assessed.

## INF-053 — Visible current-day policy with persistent reference detail

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before timed case processing begins, the interface explicitly
  discloses the current workday's new or repealed rules and keeps an inspectable
  authoritative reference for document requirements and validation details.
- Includes: Papers, Please showing the daily official bulletin alongside the
  rulebook's basic rules, issuing cities and valid document seals.
- Excludes: a second human's private manual; rules inferred only from penalties;
  one static clue sheet that never changes across days; automatic pass/fail
  feedback without the governing reference.
- Parameters: amendment source, persistent reference sections, rule hierarchy,
  bookmark upgrades, setup-time pause and whether old rules remain listed.
- Evidence: [Papers, Please decomposition](../games/m-r/papers-please.md).
- Novelty: not assessed.

## INF-054 — Collectible diegetic manual progressively expands persistent reference

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: individually collected page pairs permanently expand one
  inspectable in-world manual whose authored diagrams, maps and annotations can
  communicate controls or secrets that were mechanically possible beforehand.
- Includes: collecting TUNIC pages 42–43 at the fountain, then reading page 43
  to identify the Holy Cross as directional input and infer a nearby door code.
- Excludes: an editable player glossary; an external second-role manual; a
  tutorial that grants the control it describes; transient pickup flavour text.
- Parameters: page-pair locations, collection prerequisites, page order,
  inspect-anywhere access, zoom, encoded language and knowledge-only secrets.
- Evidence: [TUNIC decomposition](../games/s-z/tunic.md).
- Novelty: not assessed.

## INF-055 — Retained fact is explicitly available after world reset

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a world-reset boundary, the interface or authored dialogue
  exposes that one previously acquired operational fact remains available to
  the player even though the source encounter and surrounding world state reset.
- Includes: Outer Wilds continuing to display the launch-code marks and offering
  a reply to Slate that the Hatchling already obtained them from the observatory.
- Excludes: the human player remembering an undisplayed solution; a retained
  inventory object; a complete public action history; a fact reacquired anew.
- Parameters: fact identity, display channel, dialogue acknowledgement, reset
  boundary, persistence duration and accessibility alternative.
- Evidence: [Outer Wilds decomposition](../games/m-r/outer-wilds.md).
- Novelty: not assessed.

## INF-056 — Game-authored clue is visible in an external interface

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a decision-relevant clue is fully observable in a file, desktop
  layer or mock operating-system surface outside the ordinary game-world view.
- Includes: the intended external clue channel in OneShot and its World Machine
  Edition equivalent.
- Excludes: information hidden in executable code; a normal pause menu; an
  in-world computer terminal rendered inside the same scene.
- Parameters: interface surface, file format, persistence, update signal and
  accessibility equivalent.
- Evidence: [OneShot decomposition](../games/m-r/oneshot.md).
- Novelty: not assessed.
