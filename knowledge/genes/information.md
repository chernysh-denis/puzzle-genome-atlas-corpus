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
  house state; Factorio's explored terrain, placed entities, inventories,
  moving items, active recipes, power state and visible hostile units; each
  Split Fiction player's local Chapter 1 geometry, hazards and prompts.
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
  [Maquette decomposition](../games/m-r/maquette.md),
  [Antichamber decomposition](../games/a-f/antichamber.md), and
  [Factorio decomposition](../games/a-f/factorio.md), and
  [Split Fiction decomposition](../games/s-z/split-fiction.md).
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
  Hero's next random dawn spawn, card reward opportunity and loot identity;
  Slay the Spire's unrevealed encounter identity, card offer and relic or
  potion result before the run seed resolves that future node.
- Excludes: a preview queue or deterministic future state.
- Evidence: [2048 decomposition](../games/0-9/2048.md) and
  [Royal Match decomposition](../games/m-r/royal-match.md), and
  [Mini Metro decomposition](../games/m-r/mini-metro.md),
  [Loop Hero decomposition](../games/g-l/loop-hero.md), and
  [Slay the Spire decomposition](../games/s-z/slay-the-spire.md), and
  [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md).
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
  covers, plates and locks; the concealed order of a Slay the Spire combat
  draw pile while the deck list and visible hand remain inspectable.
- Excludes: a future random event not yet selected; an inspectable element that
  is merely offscreen; information the player once saw and forgot.
- Parameters: setup distribution, known global content count, first-action
  conditioning and reveal permanence.
- Evidence: [Minesweeper decomposition](../games/m-r/minesweeper.md),
  [Mastermind decomposition](../games/m-r/mastermind.md),
  [Wordle decomposition](../games/s-z/wordle.md), and
  [Balatro decomposition](../games/a-f/balatro.md), and
  [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md),
  [The Room decomposition](../games/s-z/the-room.md), and
  [Slay the Spire decomposition](../games/s-z/slay-the-spire.md), and
  [Strands decomposition](../games/s-z/strands.md).
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

## INF-057 — RCI demand and spatial diagnostic overlays are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes current sector demand plus selectable maps
  for coverage, traffic, pollution, desirability and other spatial city conditions.
- Includes: SimCity 4 and Cities: Skylines RCI bars, information views and
  building or location query inspection.
- Excludes: a fully revealed internal demand formula; decorative map colouring;
  post-hoc score only.
- Parameters: demand sectors, overlay layers, spatial resolution, refresh cadence and query detail.
- Evidence: [SimCity 4 Deluxe Edition decomposition](../games/s-z/simcity-4-deluxe-edition.md)
  and [Cities: Skylines decomposition](../games/a-f/cities-skylines.md).
- Novelty: not assessed.

## INF-058 — Itemised municipal budget ledger is visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface itemises recurring income, expenditure, tax rates,
  deals and treasury balance before the player commits further fiscal changes.
- Includes: SimCity 4 and Cities: Skylines economy, budget and tax panels.
- Excludes: one undifferentiated currency total; hidden future random expenses;
  private household accounts outside the managed city.
- Parameters: categories, period, projected versus realised totals, tax groups and deal terms.
- Evidence: [SimCity 4 Deluxe Edition decomposition](../games/s-z/simcity-4-deluxe-edition.md)
  and [Cities: Skylines decomposition](../games/a-f/cities-skylines.md).
- Novelty: not assessed.

## INF-059 — Recipe and technology dependency reference is visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes known production recipes and the reachable
  technology prerequisite graph, including required inputs, products and
  unlock relationships, before the player commits the next factory expansion.
- Includes: Factorio recipe tooltips, crafting menus and technology screen with
  science-pack costs, prerequisites and unlock effects.
- Excludes: a hidden recipe inferred only by experiment; one current inventory
  count; a static external manual with no in-game reference.
- Parameters: known recipe set, ingredient quantities, machine category,
  technology prerequisites, science costs, queue state and search filters.
- Evidence: [Factorio decomposition](../games/a-f/factorio.md).
- Novelty: not assessed.

## INF-060 — Live factory-network diagnostics are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: inspectable panels and overlays expose current production flow,
  network satisfaction and spatial externalities so the player can locate a
  running factory's bottleneck or risk without seeing every future event.
- Includes: Factorio production and consumption statistics, electric-network
  satisfaction, logistic-network contents, train state, machine status icons
  and the pollution map overlay.
- Excludes: the recipe dependency reference itself; a post-level score only;
  full disclosure of future enemy attack timing or unexplored terrain.
- Parameters: metric, interval, network scope, spatial layer, update cadence,
  historical window, status icon and aggregation.
- Evidence: [Factorio decomposition](../games/a-f/factorio.md).
- Novelty: not assessed.

## INF-061 — Category-and-magnitude hostile intent preview

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before the player commits a combat phase, each hostile actor
  discloses its next action category and any declared attack magnitude while
  some buff, debuff or special-effect details may remain categorical.
- Includes: Slay the Spire intent icons showing attack damage and whether an
  enemy plans to attack, defend, buff, debuff, sleep or use an unknown action.
- Excludes: an exact spatial target-and-effect preview; no forecast of the next
  hostile action; a probability distribution over uncommitted actions.
- Parameters: category vocabulary, damage count, multi-hit display, hidden
  special details and intent-suppression effects.
- Evidence: [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
- Novelty: not assessed.

## INF-062 — Revealed branching route categories and connections

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player can inspect the current act's directed route,
  successor connections and node categories before choosing the next node,
  while encounter-specific contents may remain unknown.
- Includes: Slay the Spire maps exposing combat, elite, unknown, rest, shop,
  treasure and boss icons plus their connecting paths.
- Excludes: a hidden map revealed only after travel; exact contents of an
  unknown event; a route authored directly by the player.
- Parameters: visible horizon, node categories, boss disclosure, connection
  graph and hidden encounter identity.
- Evidence: [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
- Novelty: not assessed.

## INF-063 — Visible exact delivery shape, quota and progression reward

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the progression interface discloses the exact structured shape
  currently accepted, the remaining delivery quantity and the mechanics or
  resources awarded when that quota completes.
- Includes: shapez 2 milestone diagrams, live Vortex progress and listed
  machine, floor, platform, blueprint-point or research-point rewards.
- Excludes: the full hidden algorithm of later random Operator shapes; a recipe
  list with no current quota; a receiver whose required object must be inferred.
- Parameters: shape code or diagram, delivered count, target quantity, reward
  list, locked-successor visibility and difficulty scaling.
- Evidence: [shapez 2 decomposition](../games/s-z/shapez-2.md).
- Novelty: not assessed.

## INF-064 — Visible season, hostility and mystery activation forecast

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes the current and next ordered weather phase,
  the settlement's hostility tier and which declared phase effects are active or
  will activate at the current tier.
- Includes: Against the Storm's season timeline, Hostility meter and forest
  mystery thresholds.
- Excludes: hidden weather; an unlabeled difficulty number; exact future random
  offers.
- Parameters: phase horizon, time remaining, hostility sources, tier thresholds
  and mystery descriptions.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## INF-065 — Visible population-group resolve trajectory and need state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: for each population group the interface exposes current Resolve,
  its direction of change, threshold relations and the satisfied or unsatisfied
  contributors that explain the value.
- Includes: Against the Storm species portraits and need panels.
- Excludes: one opaque happiness icon; exact hidden future newcomers; individual
  cosmetic mood animation.
- Parameters: group, value, trend, departure threshold, reputation threshold,
  needs and modifiers.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## INF-066 — Visible paired reputation and impatience progress

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface simultaneously exposes the settlement success track
  and opposed failure track, their terminal thresholds and current progress.
- Includes: Against the Storm Reputation and Queen's Impatience bars.
- Excludes: one hidden failure timer; a final score shown only after play; two
  unrelated currencies.
- Parameters: current values, maxima, passive rate, milestone markers and active
  modifiers.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## INF-067 — Visible task requirements, deadline and rewards

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before or during commitment, the interface discloses a task's
  required state or payment, remaining time where applicable, promised reward
  and declared failure or threat consequence.
- Includes: Against the Storm Orders and Glade Event resolution panels; The
  Sims 4 scenario stage checklist and declared branch rewards.
- Excludes: hidden quest requirements; a generic recipe with no task reward; a
  surprise failure effect disclosed only after expiry.
- Parameters: requirements, alternatives, deadline, progress, reward and threat.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md)
  and [The Sims 4 decomposition](../games/s-z/the-sims-4.md).
- Novelty: not assessed.

## INF-068 — Visible world-map range, biome and modifier state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before embarking, the persistent map exposes which tiles are
  reachable and the known biome, difficulty or modifier properties attached to
  candidate destinations.
- Includes: the Against the Storm world-map embarkation preview.
- Excludes: concealed settlement glade contents; an unrestricted level-select
  list; a destination whose rules appear only after starting the run.
- Parameters: origin, range, biome, difficulty, map modifier, reward and cycle.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## INF-069 — Material and infrastructure overlays are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: selectable spatial overlays expose elements, oxygen, temperature,
  germs, rooms, power, plumbing, ventilation, shipping and automation.
- Includes: Oxygen Not Included overlays and inspectable cell values.
- Excludes: unexplored contents; one nonspatial tooltip; future random offers.
- Parameters: layer, legend, resolution, topology, colouring, cadence and detail.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## INF-070 — Agent needs, errands and stress causes are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes each agent's needs, traits, skills, morale,
  stress modifiers, schedule and ranked eligible errands.
- Includes: Oxygen Not Included Duplicant details and building Errands tabs.
- Excludes: hidden final tie-break logic; aggregate totals only; cosmetic animation.
- Parameters: agent, need, trait, skill, morale, stress, schedule, errand and eligibility reason.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## INF-071 — Colony production and survival reports are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: current and historical panels expose colony-wide oxygen, food,
  power, material, labour and population changes plus actionable shortage warnings.
- Includes: Oxygen Not Included cycle reports, resource lists, diagnostics and notifications.
- Excludes: exact future outcomes; a single score; hidden asteroid resources.
- Parameters: metric, cycle, production, consumption, reserve, warning, population and labour.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## INF-072 — Resident profile exposes work, needs, thoughts and relationships

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes one autonomous resident's current job,
  skills, labour permissions, bodily needs, recent thoughts, relationships and
  stress state for causal inspection.
- Includes: Dwarf Fortress creature, labour, thoughts and preferences panels;
  The Sims 4 active-Sim needs, skills, work and relationship panels.
- Excludes: hidden future events; one aggregate settlement happiness number.
- Parameters: resident, job, skills, work details, needs, thoughts, memories,
  relationships, stress and health.
- Evidence: [Dwarf Fortress decomposition](../games/a-f/dwarf-fortress.md) and
  [The Sims 4 decomposition](../games/s-z/the-sims-4.md).
- Novelty: not assessed.

## INF-073 — Carried hotbar and active equipment state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes carried quick slots, their stack contents
  and the currently active hand or equipped item before a local world action.
- Includes: Minecraft Survival hotbar and selected held item; Counter-Strike 2
  carried weapon/utility icons, active item and ammunition state; Cyberpunk
  2077 weapon slots, active weapon and ammunition HUD; Hollow Knight: Silksong
  equipped Crest, Tool slots and Tool charge state; Helldivers 2 current
  firearm, magazine/reserve ammunition, grenade and support-weapon state.
- Excludes: a complete future terrain map; a hidden recipe discovered only by
  external knowledge; a colony-wide production report.
- Parameters: slots, stacks, selected item, hand and equipment state.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md) and
  [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md), and
  [Helldivers 2 decomposition](../games/g-l/helldivers-2.md) and
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Additional support: [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md),
  for the visible active, trinket and pocket slots plus pickup counters.
- Novelty: not assessed.

## INF-074 — Crafting grid and available recipe state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the crafting interface exposes the current grid contents,
  matching output and recipe-book entries currently available to the player.
- Includes: Minecraft 2×2 and 3×3 crafting UI with recipe-book autofill.
- Excludes: hidden future recipes; an autonomous machine production report.
- Parameters: grid, cells, ingredients, matched output and recipe-book entries.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md).
- Novelty: not assessed.

## INF-075 — Health, hunger, armour and durability state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes the avatar's current survival meters and
  carried tool wear sufficiently to judge food, combat and replacement needs.
- Includes: Minecraft hearts, hunger drumsticks, armour icons and durability bars.
- Excludes: exact hidden saturation; a predicted future damage outcome.
- Parameters: health, hunger, armour, breath, status and durability.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md).
- Novelty: not assessed.

## INF-076 — A thrown locator reveals a temporary bearing to a hidden target

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the visible flight path of a used locator discloses a temporary
  directional observation toward an otherwise undisclosed world target.
- Includes: watching a thrown Minecraft Eye of Ender point toward a stronghold.
- Excludes: revealing exact coordinates; a permanently updating compass needle.
- Parameters: bearing, flight path, observation position and target class.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md).
- Novelty: not assessed.

## INF-077 — Weather timeline and city heat conditions are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the interface exposes current and forecast ambient temperature
  changes together with inspectable heat categories for occupied buildings.
- Includes: Frostpunk weather bar, temperature forecast and heat view.
- Excludes: exact future dilemmas; material-cell thermal simulation; decorative snow.
- Parameters: current temperature, forecast horizon, change time, building heat,
  category legend and illness risk.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## INF-078 — Hope, Discontent and promise causes are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the interface exposes current Hope and Discontent, active positive
  and negative causes, crisis thresholds and timed promises affecting them.
- Includes: Frostpunk welfare bars, modifier lists and promise deadlines.
- Excludes: one citizen mood; hidden event outcomes; resource stockpiles.
- Parameters: track values, trends, modifiers, promise, deadline, recovery target
  and purpose replacement.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## INF-079 — Generator fuel, heat-output and stress diagnostics are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: generator controls expose current coal reserve and consumption,
  configured power and range, heat output, Overdrive state and stress.
- Includes: Frostpunk generator panel and coal-depletion forecast.
- Excludes: city-wide production history; hidden explosion chance; technology tree.
- Parameters: coal, burn rate, remaining duration, power, range, overdrive,
  stress and warning threshold.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## INF-080 — Frostland destinations, travel time and scout cargo are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the world map exposes revealed scout destinations and route-time
  estimates together with each team's current position, status and carried
  resources or escorted people.
- Includes: A New Home Frostland map and approaching Great Storm coverage.
- Excludes: concealed successors before exploration; street routing; fast travel.
- Parameters: node, route, estimated time, team, cargo, survivors, storm reach
  and destination state.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## INF-081 — Star map, planet properties and known resource reserves are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the navigation views expose discovered stars, planetary orbits,
  distances and available planet properties, with researched exploration levels
  revealing aggregate resource types and remaining reserves.
- Includes: Dyson Sphere Program planet view, star map and universe-exploration
  resource summaries.
- Excludes: deposits on unscanned distant systems; factory production rates;
  hidden future Dark Fog wave composition.
- Parameters: exploration level, star, planet, orbit, distance, resource type,
  reserve estimate, rare resource and hostile presence.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## INF-082 — Mecha energy, flight state and navigation target are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes current mecha-core energy and fuel state,
  active movement regime, speed, target bearing and distance needed to judge a
  surface, sail or warp journey.
- Includes: Dyson Sphere Program Icarus core meter and space-navigation HUD.
- Excludes: factory electric-grid satisfaction; autonomous vessel cargo;
  exact undiscovered planet resources.
- Parameters: core energy, generation, fuel, mode, speed, heading, target,
  distance and estimated approach.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## INF-083 — Logistics-station slot and carrier state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: each logistics station exposes its typed stored quantities, local
  and remote slot modes, carrier inventory, charge, range, load thresholds,
  warper policy and active trips.
- Includes: Dyson Sphere Program Planetary and Interstellar Logistics Station panels.
- Excludes: belt-lane contents outside the station; hidden route-selection
  internals; general recipe reference.
- Parameters: item slot, storage, supply, demand, current quantity, carrier,
  energy, range, minimum load, warper and trip.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## INF-084 — Dyson plan, construction progress and stellar output are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the orbital editor and receiver panels expose configured orbits
  and sphere layers, planned and built elements, sail and rocket progress,
  generated output, receiver demand and continuous-receiving state.
- Includes: Dyson Sphere Program Dyson editor, swarm/sphere statistics and Ray
  Receiver diagnostics.
- Excludes: ordinary factory production statistics; unexplored star resources;
  future shell elements not placed by the player.
- Parameters: orbit, layer, node, frame, shell cell, sail count, rocket points,
  generation, requested power, efficiency and receiver mode.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## INF-085 — Dark Fog threat, wave and combat state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: combat overlays expose known hostile bases and units, current
  planetary threat progress, incoming-wave warning and the mecha or defence
  state needed to respond.
- Includes: default Regular Dark Fog threat meter, attack warning and targeting.
- Excludes: exact future wave composition before dispatch; ordinary factory
  bottlenecks; a hidden random event.
- Parameters: base, level, threat value, threshold, wave warning, target,
  hostile health, ammunition, shield and defence coverage.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## INF-086 — Settlement population, needs and workforce state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: inspectable settlement panels expose population groups, housing, needs or well-being, employment, vacancies and available versus required workforce.
- Includes: Anno 1800 residence/workforce, Timberborn population/well-being, Workers & Resources citizen/labour and Surviving Mars population/work-allocation interfaces.
- Excludes: hidden future births or exact death time; production throughput without population state; aggregate score alone.
- Parameters: species or citizen groups, age, tier, housing, need schema, education, health, happiness, loyalty and work priorities.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md), [Timberborn decomposition](../games/s-z/timberborn.md), [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md) and [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## INF-087 — Island storage and trade-route orders are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: storage and route interfaces expose island quantities, capacity,
  selected ports, assigned ships, cargo-slot orders and current route progress.
- Includes: Anno 1800 trading post, warehouse and trade-route panels.
- Excludes: local cart paths in transit; unknown competitor cargo; recipe reference.
- Parameters: island, good, quantity, capacity, port, ship, slot, order,
  minimum stock and route state.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## INF-088 — Influence allocation and current newspaper issue are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes available and committed influence by
  category together with the current newspaper's articles, replacement costs
  and published effects.
- Includes: Anno 1800 influence overview and newspaper editor.
- Excludes: hidden future issue composition; treasury budget; AI reputation.
- Parameters: influence pool, category, investment, article, propaganda,
  replacement cost, effect and publication time.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## INF-089 — Regional map exposes islands, fertilities and expedition state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: discovered regional and expedition views expose island locations,
  known crop fertilities and deposits, ship positions, voyage morale and the
  declared skill or supply consequences of current expedition choices.
- Includes: Anno 1800 Old/New World maps and discovery expedition interface.
- Excludes: undiscovered island details; exact hidden event rolls; local factory flow.
- Parameters: region, island, fertility, deposit, ship, destination, morale,
  skill chance, cargo and event option.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## INF-090 — World’s Fair phase and exhibition supply are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the monument interface exposes its current construction or
  exhibition phase, required and delivered inputs, remaining preparation time,
  achieved supply tier and associated reward pool.
- Includes: Anno 1800 World’s Fair construction and exhibition panels.
- Excludes: hidden reward identity where only a pool is declared; ordinary
  factory diagnostics; campaign quest text outside the monument.
- Parameters: phase, input, delivered quantity, workforce, electricity, time,
  supply tier, exhibition and reward pool.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## INF-091 — Current and forecast weather event is visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface identifies the current weather, remaining duration
  and next forecast when advance warning is available.
- Includes: Timberborn temperate, drought and badtide displays.
- Excludes: hidden future draws; cosmetic seasons.
- Parameters: event, remaining days, forecast, lead time and cycle.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## INF-092 — Water, irrigation and contamination state is inspectable

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: rendering, overlays and panels expose depth, flow, contamination
  and affected irrigation or plant state at relevant locations.
- Includes: Timberborn water, badwater, pumps, barriers and soil effects.
- Excludes: exact future source output; world visibility alone.
- Parameters: location, depth, flow, contamination, irrigation and opening.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## INF-093 — Population, well-being and work allocation are visible

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `INF-086`.
- Includes: historical references that used `INF-093` before registry
  normalisation 006.
- Excludes: new game signatures; use `INF-086` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Merged into: `INF-086` by
  [`TAXONOMY_CHANGE_014`](../../research/taxonomy-changes/TAXONOMY_CHANGE_014.md).

## INF-094 — Goods, production and power-network state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: panels disclose stored goods, recipe flow, operating reason and
  connected power generation, demand, satisfaction and storage.
- Includes: Timberborn stock, workplace and mechanical-power interfaces.
- Excludes: recipe reference without live quantities; future wind output.
- Parameters: goods, capacity, inputs, outputs, status, generation and demand.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## INF-095 — Automation measurement, logic and target state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: automation interfaces disclose connections, sampled values,
  thresholds or logic, current signals and resulting target state.
- Includes: Timberborn 1.0 sensors, relays, logic and controlled buildings.
- Excludes: hidden scripts; manual state without a signal rule.
- Parameters: connection, measurement, predicate, signal and target response.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## INF-096 — Wonder unlock, build and activation progress is visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the interface itemises the wonder's science gate, build
  deliveries and progress, then separate activation supplies and eligibility.
- Includes: Timberborn Earth Recultivator panel and first-launch state.
- Excludes: one-step ordinary building costs; hidden victory rules.
- Parameters: science, delivered goods, progress, launch supply and win state.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## INF-097 — Citizen welfare, education and labour state is visible

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `INF-086`.
- Includes: historical references that used `INF-097` before registry
  normalisation 006.
- Excludes: new game signatures; use `INF-086` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Merged into: `INF-086` by
  [`TAXONOMY_CHANGE_014`](../../research/taxonomy-changes/TAXONOMY_CHANGE_014.md).

## INF-098 — Lines, passengers, vehicles and traffic state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: transport panels expose stops, line orders, waiting passengers,
  vehicle cargo, fuel, delay, reachability and network traffic.
- Includes: Workers & Resources passenger and cargo transport.
- Excludes: hidden future pathfinder choices.
- Parameters: line, stop, passenger, vehicle, cargo, fuel, route and delay.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## INF-099 — Construction assignments and phase progress are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: site and office panels itemise sources, vehicles, current phase,
  required and delivered materials, workers, mechanisms and work progress.
- Includes: Workers & Resources realistic construction UI.
- Excludes: hidden delivery timing or instant-money completion.
- Parameters: site, source, phase, material, vehicle, labour and progress.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## INF-100 — Dual-currency trade prices and flows are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: economy panels expose ruble and dollar balances, current import
  and export prices, traded volumes and income or expenditure by commodity.
- Includes: Workers & Resources economy and customs panels.
- Excludes: fully disclosed future world-event price changes.
- Parameters: bloc, currency, resource, direction, price, volume and period.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## INF-101 — Utility and environmental diagnostics are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: overlays expose connected power, heat, water and sewage capacity
  plus temperature, pollution, fire, waste and maintenance state.
- Includes: Workers & Resources infrastructure overlays.
- Excludes: exact future failures or cosmetic network rendering only.
- Parameters: network, supply, demand, loss, environment, risk and outage.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## INF-102 — Research and nuclear-chain state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: panels expose research prerequisites and workdays, uranium and
  fuel inventories, reactor staff, cooling, output, waste and radiation.
- Includes: Workers & Resources nuclear route.
- Excludes: hidden future accidents.
- Parameters: project, progress, material, staff, cooling, output, waste and risk.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## INF-103 — Campaign branches and measured objectives are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: campaign UI exposes active and completed branches, required
  construction or traded totals and the next available task.
- Includes: both released Workers & Resources base campaigns.
- Excludes: platform achievements or hidden sandbox goals.
- Parameters: campaign, branch, objective, target, current total and completion.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## INF-104 — Terrain layers, designations and mine remit are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: overlays expose typed underground material, surface height,
  mining and dumping target volumes and the selected tower's operating area.
- Includes: Captain of Industry resource layers, terrain grid, designations and
  Mine Control Tower area display.
- Excludes: concealed ore with no preview; factory recipe diagnostics; a
  decorative contour map.
- Parameters: material, depth, height, designation type, target plane, tower
  area, vehicle access and mixed-load warning.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## INF-105 — Vehicle jobs, buffers and reachability state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: entity and vehicle panels expose current cargo requests,
  reservations, import or export rules, assignments, fuel, maintenance and
  unreachable destinations.
- Includes: Captain of Industry truck statistics, storage sliders, dedicated
  routes, mine assignments and navigation warnings.
- Excludes: hidden future jobs; belt-only throughput graphs; world-map trade offers.
- Parameters: vehicle, product, source, destination, request, reservation,
  buffer, assignment, route, fuel and maintenance.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## INF-106 — Settlement, Unity, health and maintenance state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: population and statistics panels expose housing, workers, food
  and service fulfilment, Unity income and expenses, health modifiers,
  pollution and maintenance supply and demand.
- Includes: Captain of Industry population overview and product statistics.
- Excludes: individual citizen routes; undisclosed future disease timing;
  municipal cash in multiple currencies.
- Parameters: population, jobs, housing, service, Unity, health, pollution,
  maintenance tier, production and consumption.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## INF-107 — World nodes, ship state and island offers are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the world map and trading interface expose revealed routes,
  destinations, enemy strength, ship fuel and damage, outpost requirements,
  village reputation and available exchange terms.
- Includes: Captain of Industry exploration map, villages, contracts and resource nodes.
- Excludes: unrevealed node identity; home-island terrain layers; train schedules.
- Parameters: node, edge, distance, fuel, strength, damage, loot, reputation,
  offer ratio, Unity cost and cargo capacity.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## INF-108 — Rocket assembly, transfer and launch readiness are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: assembly and launch panels expose rocket component progress,
  transporter or pad availability, connected propellant and water and the
  first-launch state.
- Includes: Captain of Industry Rocket Assembly Depot and Rocket Launch Pad.
- Excludes: hidden launch prerequisites; space-station upkeep after the first
  launch; generic factory output statistics alone.
- Parameters: rocket tier, components, assembly progress, transporter route,
  pad, fuel, oxidiser, water, payload and launch status.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## INF-109 — Mars sectors, deposits and anomaly progress are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: map overlays expose sector scan progress and revealed deposits,
  anomalies, entrances and explorer-analysis state while unrevealed contents
  remain unknown.
- Includes: Surviving Mars: Relaunched surface scanning and RC Explorer pins.
- Excludes: exact contents of unscanned sectors; production diagnostics;
  cosmetic terrain rendering.
- Parameters: sector, progress, queue, deposit, grade, anomaly, explorer and
  analysis status.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## INF-110 — Drone command areas, errands and resource access are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: commander and work panels expose service-area coverage, assigned
  drones, pending construction, hauling or repair errands, required resources
  and unreachable or unpowered causes.
- Includes: Surviving Mars: Relaunched rockets, RC Commanders, Drone Hubs and
  controlled drones.
- Excludes: hidden pathfinder tie-breaks; human workplace staffing; shuttle-only
  global transport.
- Parameters: commander, range, drone, errand, priority, resource, route,
  power and failure reason.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## INF-111 — Mars rocket manifests, flights and landing state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: resupply and rocket panels expose cargo or passenger capacity,
  selected manifest, fuel, origin, destination, travel progress, landing-site
  compatibility, automation and expected export or project result.
- Includes: Surviving Mars: Relaunched patch 1.0.7 universal rockets.
- Excludes: hidden future expedition events; local shuttle routes; generic
  inventory lists with no flight state.
- Parameters: rocket, capacity, manifest, passenger, fuel, route, travel time,
  landing site, automation, export and reward.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## INF-112 — Dome life support and local maintenance are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: network and building panels expose each dome's current power,
  water, oxygen, food and storage coverage plus leaks, dust, required repair
  resources, malfunction and estimated reserve duration.
- Includes: Surviving Mars: Relaunched dome, pipe, tank, grid and maintenance
  diagnostics.
- Excludes: undisclosed disaster timing; colonist comfort causes unrelated to
  survival; one aggregate resource total without topology.
- Parameters: dome, network, supply, demand, storage, reserve duration, leak,
  dust, maintenance threshold, repair resource and malfunction.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## INF-113 — Martian laws, factions, seats and tension are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: political panels expose prepared and locked laws, option effects
  and upkeep, faction agendas and support, Assembly seats, promises, vote state,
  global tension and crisis causes.
- Includes: Surviving Mars: Relaunched Earth Council and Martian Assembly UI.
- Excludes: hidden future faction events; flavour biographies; research costs
  unrelated to law upkeep.
- Parameters: law, option, prerequisite, preparation, effect, upkeep, faction,
  agenda, seats, support, promise, vote, tension and crisis.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## INF-114 — Independence gates, penalties, contributions and price are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the independence interface exposes required colony and mission
  goals, declaration state, sponsor penalties, sponsor-colony contributions,
  current price reduction, remaining payment and achieved free status.
- Includes: Surviving Mars: Relaunched purchased-independence sequence.
- Excludes: optional post-independence mission goals; platform achievements;
  hidden future sponsor events.
- Parameters: goal, progress, declaration, penalty, sponsor colony, resource,
  contribution, base price, reduction, balance and completion.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## INF-115 — Local sight and sound expose partial opponent state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a player directly learns opponents and their actions only through
  current avatar-centred visibility, spatial sound or effects that penetrate the
  local occlusion state.
- Includes: Counter-Strike 2 sightlines, footsteps, shots, reloads, utility and
  bomb interaction audio; Cyberpunk 2077 local sight, footsteps, speech,
  gunfire and scanner-assisted currently exposed hostile state; Marvel Rivals
  third-person sightlines, effects, silhouettes and spatial combat audio;
  Helldivers 2 local patrol silhouettes, movement, calls, shots and effects.
- Excludes: omniscient enemy positions; an authored hidden solution inferred
  from static clues; teammate-transmitted knowledge itself.
- Parameters: view, occlusion, distance, material, sound event and effect state.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md) and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md), and
  [Helldivers 2 decomposition](../games/g-l/helldivers-2.md) and
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md) and
  [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md), and
  [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md).
- Novelty: not assessed.

## INF-116 — Live team, score and shared-objective state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live team interface exposes eligible allied status, match clock or score and current shared-objective ownership, progress or phase state.
- Includes: Counter-Strike 2, Dota 2, Marvel Rivals, Battlefield 6 and
  Helldivers 2 team HUD, radar or minimap and objective state, including
  Reinforce stock and mission time where applicable; EA SPORTS FC 26 match
  score, clock, side identity and restart state.
- Excludes: permanent omniscient enemy tracking; post-match analytics; account rank.
- Parameters: team frames, allied state, radar or minimap, shared sightings, clock, score, objective schema, phase and respawn notice.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md),
  [Dota 2 decomposition](../games/a-f/dota-2.md),
  [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md),
  [Battlefield 6 decomposition](../games/a-f/battlefield-6.md) and
  [Helldivers 2 decomposition](../games/g-l/helldivers-2.md) and
  [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md), and
  [EA SPORTS FC 26 decomposition](../games/a-f/ea-sports-fc-26.md).
- Novelty: not assessed.

## INF-117 — Personal economy and purchase state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player can inspect current money, offered prices, owned
  equipment and purchase availability before committing a buy or save decision.
- Includes: Counter-Strike 2 Competitive money display and buy menu; Grand Theft
  Auto V Story Mode character balances and shop offers; Cyberpunk 2077 eurodollar
  balance, vendor prices and purchase eligibility.
- Excludes: opponents' exact hidden balances; cosmetic marketplace prices.
- Parameters: balance, price, role, inventory, buy state and refund state.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md)
  [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## INF-118 — Team-shared fog-limited world and minimap state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player sees current terrain, allied entities and hostiles
  revealed by any eligible allied vision source, with the same bounded state
  summarised on a team minimap.
- Includes: Dota 2 shared unit/ward vision, fog and minimap sightings.
- Excludes: omniscient spectator view; voluntary team chat content.
- Parameters: allied source, radius, terrain, hostile visibility and minimap marker.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md).
- Novelty: not assessed.

## INF-119 — Personal character resources and build are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes a controlled character's health, action or
  casting resources, experience, attributes, learned build, status effects and
  ability readiness.
- Includes: Dota 2 hero HUD and ability/talent panels; Clair Obscur: Expedition
  33 character menus and combat resources; Grand Theft Auto V Story Mode health,
  armour, special meter and character-stat panels; Cyberpunk 2077 health, RAM,
  level, attributes, perks, skills and cooldown displays; Marvel Rivals hero
  health, ultimate meter, ability readiness, status and selected Team-Up state;
  Hollow Knight: Silksong health, Silk, equipped Crest and Tool state.
  Helldivers 2 health, injury/status and selected stratagem charge or cooldown
  state.
- Excludes: hidden enemy cooldowns; account statistics; exact future turn order.
- Parameters: health, resource, experience, level, attributes, skill, status,
  cooldown and persistence.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md),
  [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md),
  [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md), and
  [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md), and
  [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Evidence: [Helldivers 2 decomposition](../games/g-l/helldivers-2.md) and
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md) and
  [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Novelty: not assessed.

## INF-120 — Match economy, item logistics and buyback are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player can inspect current gold, shop prices and access,
  hero/backpack/stash/courier items, recipe dependencies and buyback state.
- Includes: Dota 2 shop, inventory, courier and buyback panels.
- Excludes: opponents' hidden gold; cosmetic inventory value.
- Parameters: gold, price, shop, recipe, slot, courier, cost and cooldown.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md).
- Novelty: not assessed.

## INF-121 — Team clock, score, structures and objectives are visible

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `INF-116`.
- Includes: historical references that used `INF-121` before registry
  normalisation 006.
- Excludes: new game signatures; use `INF-116` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md).
- Merged into: `INF-116` by
  [`TAXONOMY_CHANGE_014`](../../research/taxonomy-changes/TAXONOMY_CHANGE_014.md).

## INF-122 — Capture probability and attempt state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before and during an eligible capture, the interface exposes the
  target and device's current success estimate plus the progress or failure of
  the committed checks.
- Includes: Palworld capture percentage and Sphere attempt feedback; Pokémon
  Legends: Z-A capture arrows and committed throw feedback.
- Excludes: a guaranteed hidden recruitment roll; exact future random sample;
  creature combat damage alone.
- Parameters: target, device, estimated chance, check progress, success and failure.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md) and
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Novelty: not assessed.

## INF-123 — Companion profile exposes combat and assignment capabilities

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player can inspect a captured companion's level, stats,
  type or element, active skills, passives and ruleset-specific assignment
  capabilities before assigning it to a bounded roster.
- Includes: Palworld Pal detail and Palbox management panels; Pokémon Legends:
  Z-A Pokémon summaries exposing level, stats, type and learned moves.
- Excludes: undiscovered wild-creature identity; cosmetic-only appearance;
  hidden random future mutation.
- Parameters: identity, level, stats, type or element, skills, passives,
  partner interaction and assignment capability.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md) and
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Novelty: not assessed.

## INF-124 — Avatar and active-party survival state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the HUD exposes the avatar's health, hunger, stamina, temperature
  and equipped state together with active-party companion health and readiness.
- Includes: Palworld exploration and combat HUD.
- Excludes: base-wide task detail; hidden wild-creature stats; post-run analytics.
- Parameters: health, hunger, stamina, temperature, armour, durability, party,
  active companion and cooldown.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md).
- Novelty: not assessed.

## INF-125 — Explored map and authored mission gates are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: discovered terrain, travel points, mission markers and current
  main-mission requirements are inspectable before route choice.
- Includes: Palworld map, Watchtower reveal, mission list and World Tree markers;
  Grand Theft Auto V Story Mode map icons and critical-path mission prompts;
  Cyberpunk 2077 map, journal, tracked job and fast-travel points; Hollow
  Knight: Silksong explored map, pins and current route gates.
- Excludes: undiscovered map contents; optional external interactive maps;
  custom server navigation aids.
- Parameters: discovered region, marker, fast travel, objective, prerequisite
  and completion.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md) and
  [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md), and
  [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md) and
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## INF-126 — Base assignments, resources and worker condition are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: base interfaces expose assigned companions, fixed jobs and
  priorities, available shared materials, facility task state and worker
  hunger, sanity, health or illness.
- Includes: Palworld Palbox, Monitoring Stand, storage and base status displays.
- Excludes: remote multiplayer guild administration; hidden future production;
  active-party combat HUD.
- Parameters: base, worker, assignment, priority, inventory, facility, task,
  hunger, sanity and ailment.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md).
- Novelty: not assessed.

## INF-127 — Match map exposes current insertion and zone timing

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the world map and HUD expose the participant's current position,
  visible aircraft state, present safe-area and Blue/Red Zone boundaries, and
  the warning or contraction timing needed for the next route decision.
- Includes: PUBG Normal Match map, minimap, plane, white circle, Blue Zone,
  Red Zone and phase countdowns.
- Excludes: exact future safe-circle centres; hidden opponents; external map tools.
- Parameters: player, aircraft, safe circle, damaging boundary, hazard region,
  phase, warning and contraction timer.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md).
- Novelty: not assessed.

## INF-130 — Map exposes self, landmarks and wipe horizon

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the map and server interface expose the player's current island
  position, visible biomes or monuments and the declared next wipe horizon
  without revealing ordinary opponent positions or unopened loot.
- Includes: Rust world map, monument labels and server wipe timer.
- Excludes: omniscient player tracking; future loot contents; hidden base
  interiors.
- Parameters: player position, terrain, biome, monument, safe zone, marker,
  server and wipe time.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## INF-131 — Building interface exposes legality, privilege and upkeep

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: placement previews and building HUD expose whether the current
  operation is geometrically legal and authorised, while connected Tool
  Cupboard inspection exposes charged materials and protected decay duration.
- Includes: Rust placement colour, BUILDING PRIVILEGE/BLOCKED, stability and
  TC cost per 24 hours.
- Excludes: hidden enemy TC inventory; future raid damage; exact remote base
  layout.
- Parameters: preview, socket, stability, privilege, blocked reason, upkeep,
  stored material and protected duration.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## INF-132 — Research and crafting dependencies are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the crafting, Research Table and Workbench interfaces expose
  known status, prerequisites, ingredients, scrap or fragment costs, required
  tier, queue progress and declared output before commitment.
- Includes: Rust blueprint, tech-tree, Workbench and crafting-queue panels.
  Cyberpunk 2077 crafting specifications expose components and output tier.
- Excludes: unrevealed world-loot rolls; other players' blueprint knowledge;
  hidden future server balance changes.
- Parameters: recipe, learned state, prerequisite, cost, ingredient, workbench,
  duration, queue and output.
- Evidence: [Rust decomposition](../games/m-r/rust.md) and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## INF-128 — Ground loot and inventory compatibility are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: reachable world items and the inventory interface expose item
  identity, quantity, equipment or attachment compatibility and remaining
  carrying state before the player transfers or replaces loot.
- Includes: PUBG ground labels, inventory stacks, weapon and attachment slots,
  backpack load and equipment comparison; Cyberpunk 2077 loot labels,
  inventory comparisons, weapon slots and carry weight.
- Excludes: contents of unopened remote death crates; future loot spawns;
  opponents' carried inventories.
- Parameters: item, quantity, slot, weapon compatibility, capacity, equipped
  state, replacement and reach.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md) and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## INF-129 — Survivor count and elimination feed are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface exposes the current number of living participants,
  public elimination events and the terminal placement or victory result
  without revealing every survivor's location or loadout.
- Includes: PUBG alive counter, kill feed, death result and chicken-dinner state.
- Excludes: omniscient spectator positions; hidden player inventory; post-match
  progression rewards.
- Parameters: alive count, event participants, event cause, placement, personal
  kills and terminal result.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md).
- Novelty: not assessed.

## INF-133 — Graded moodles expose embodied pressure categories

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface names current hunger, thirst, fatigue, exertion,
  panic, stress, pain, sickness, temperature, encumbrance and related categories
  at graded severity while leaving complete internal numeric state hidden.
- Includes: Project Zomboid moodle stack and tooltips.
- Excludes: exact health-panel wounds; cosmetic facial emotion; one visible
  undifferentiated health bar.
- Parameters: category, grade, icon, tooltip, threshold, modifier and hidden value.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## INF-134 — Body health panel exposes wounds and applied treatments

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an inspectable body diagram identifies affected regions, visible
  wound classes, bleeding and current treatment so the player can select a
  compatible care action, without revealing a concealed Knox Infection flag.
- Includes: Project Zomboid Health panel.
- Excludes: exact future recovery time; omniscient infection diagnosis; moodle
  summaries without body location.
- Parameters: region, wound, bleeding, treatment, bandage state, pain, visible
  infection and concealed transmission state.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## INF-135 — Isometric cutaway reveals only locally perceived space

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the world view cuts away obstructing architecture around the
  survivor and renders only terrain, interiors, items and creatures currently
  available through local vision, hearing or remembered exploration.
- Includes: Project Zomboid's Sims-style cutaway vision and local sound cues.
- Excludes: an omniscient top-down map; hidden container contents; exact zombie
  positions beyond perception.
- Parameters: camera, floor, wall cutaway, line of sight, lighting, hearing,
  explored memory and occlusion.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## INF-136 — Calendar and survival infrastructure state are inspectable

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: clocks, weather cues, container and appliance state, crop panels
  and item tooltips expose the current date, accessible reserves, power or water
  availability, freshness and crop condition without revealing every future
  cutoff or weather sample.
- Includes: Project Zomboid long-horizon shelter and farming inspection.
- Excludes: exact hidden utility shutoff date; undiscovered loot; a global
  forecast of all future seasons.
- Parameters: date, time, weather, service state, container, reserve, item age,
  crop phase, water and disease.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## INF-137 — Raid map exposes condition, extraction and remaining time

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the mission or raid interface identifies the current map and
  condition, shows known objectives, points of interest and eligible extraction
  fixtures, and exposes remaining session or departure timing needed to route risk.
- Includes: ARC Raiders Topside map, regional condition and extraction state;
  Helldivers 2 mission map, main objective, extraction location and mission time.
- Excludes: exact hidden loot rolls; omniscient Raider positions; future Map
  Condition schedules outside the current raid.
- Parameters: map, condition, point of interest, endpoint, endpoint state,
  Raider position, route marker and clock.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md) and
  [Helldivers 2 decomposition](../games/g-l/helldivers-2.md).
- Novelty: not assessed.

## INF-138 — Inventory marks value, compatibility and defeat protection

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: item and inventory panels expose identity, rarity, stack,
  durability, compatible slot, sale or recycle value and whether current
  placement protects the item from knockout loss.
- Includes: ARC Raiders backpack, loadout, Safe Pocket and stash tooltips.
- Excludes: unopened-container contents; hidden future market rotation;
  another Raider's complete inventory.
- Parameters: item, rarity, quantity, durability, slot, compatibility, value,
  protected state and capacity.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## INF-139 — ARC cues disclose type, attention and vulnerable components

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: visible form, lights, movement, emitted sound and attack windups
  let the player identify an ARC machine's type, current attention, imminent
  attack and externally vulnerable or destructible components without exposing
  its complete hidden controller state.
- Includes: ARC Raiders machine audio, target-switch cues, telegraphs, armour
  and weak-point feedback.
- Excludes: exact internal AI probabilities; other Raiders' intentions; a
  permanent omniscient target marker through cover.
- Parameters: machine type, cue, alert, target switch, windup, attack, armour,
  component, hit feedback and destroyed state.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## INF-140 — Raid settlement exposes retained loss and persistent rewards

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after the raid ends, the result presentation distinguishes
  extraction from knockout, item retention from forfeiture and awarded
  experience, level or quest progress before the next loadout is prepared.
- Includes: ARC Raiders End of Round and return-to-Speranza result state.
- Excludes: hidden loot that was never searched; future Expedition rewards;
  another squad's private progression.
- Parameters: terminal result, extracted items, protected items, lost items,
  XP, level, skill point, quest progress and next hub state.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## INF-141 — Combat HUD exposes turn order, AP, party and target state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during battle the interface exposes upcoming combatant order,
  current character AP, party health and status plus the selected enemy's
  health, Break and condition state before command commitment.
- Includes: Clair Obscur: Expedition 33 reactive turn-based combat HUD.
- Excludes: exact future enemy move contents; offscreen exploration secrets;
  post-battle statistics alone.
- Parameters: queue horizon, AP, health, status, target and Break gauge.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md).
- Novelty: not assessed.

## INF-142 — Attack motion, sound and prompts cue reactive timing

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: animation, sound and optional prompt elements disclose enough of
  an executing attack's rhythm for the player to time its offensive or
  defensive real-time input without revealing the exact timing numerically.
- Includes: Clair Obscur: Expedition 33 skill prompts and Nevron attack cues.
- Excludes: a static turn-order preview; hidden untelegraphed damage; a
  persistent countdown that reveals an exact future event time.
- Parameters: cue channel, attack member, rhythm, prompt visibility and assist.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md).
- Novelty: not assessed.

## INF-143 — Build interface exposes Picto mastery and Lumina cost

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the party build interface exposes acquired Pictos, equipped stat
  effects, battle-mastery progress, learned Luminas, their costs and each
  character's remaining activation capacity before configuration.
- Includes: Clair Obscur: Expedition 33 Pictos and Lumina menus in version 1.5.6.
- Excludes: concealed future loot; skill timing prompts; exact enemy build state.
- Parameters: Picto, mastery count, passive, cost, capacity and equipped state.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md).
- Novelty: not assessed.

## INF-144 — Navigation view exposes GPS route and wanted search

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the map and minimap expose the controlled protagonist, chosen or
  authored destination, calculated road route and current police search state
  needed to choose travel and evasion paths.
- Includes: Grand Theft Auto V Story Mode GPS line, waypoint, wanted stars,
  police markers and search cones; Cyberpunk 2077 route guidance, waypoint,
  minimap and NCPD Heat/search state.
- Excludes: undiscovered optional content; exact future traffic positions;
  omniscient hostile tracking outside the wanted search.
- Parameters: protagonist, destination, route, recalculation, stars, police
  marker, cone and minimap scale.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md) and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## INF-145 — Character wheel exposes protagonist availability and context

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before a control transfer, the character interface identifies
  unlocked protagonists, marks unavailable choices and previews the selected
  character whose current world activity will receive control.
- Includes: Grand Theft Auto V Story Mode character wheel and switch transition.
- Excludes: hidden off-screen future missions; turn-order panels; multiplayer
  player lists.
- Parameters: protagonist, availability, portrait, current activity, mission
  restriction and transition.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md).
- Novelty: not assessed.

## INF-146 — Heist board exposes approach, roles, skill and cut

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the planning interface discloses available approaches, required
  specialist roles and each unlocked candidate's competence and percentage cut
  before the player commits the operation plan.
- Includes: Grand Theft Auto V Story Mode major-heist planning boards.
- Excludes: exact concealed future mistakes; GTA Online lobby readiness;
  post-heist payout only.
- Parameters: approach, preparation, role, candidate, skill, cut, availability
  and confirmed plan.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md).
- Novelty: not assessed.

## INF-147 — Scanner exposes target state and available quickhacks

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: scanner focus reveals an eligible actor or device's disclosed
  identity, affiliation, vulnerabilities and current hackable functions, plus
  each installed quickhack's RAM cost, upload state and availability.
- Includes: Cyberpunk 2077 base-game Kiroshi scanning and quickhack selection.
- Excludes: future patrol paths; concealed loot; information available only
  after an unselected dialogue branch.
- Parameters: target, identity, affiliation, level, vulnerability, device
  function, quickhack, RAM cost, upload, cooldown and trace.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## INF-148 — Dialogue interface exposes contextual response gates

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the conversation interface presents currently available
  responses and marks their timing, lifepath or attribute context before the
  player commits, without disclosing all downstream quest consequences.
- Includes: Cyberpunk 2077 dialogue, timed response, lifepath and attribute
  options.
- Excludes: hidden future branch flags; subtitles with no choice; an external
  walkthrough revealing consequences.
- Parameters: option, speaker, timer, lifepath, attribute, threshold,
  availability, styling and concealed consequence.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## INF-149 — Cyberware interface exposes capacity and implant effects

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the ripperdoc and character interfaces expose current cyberware
  capacity, compatible body slots, installed and offered implants, armour,
  attunement, tier, price and declared ability effects before configuration.
- Includes: Cyberpunk 2077 Update 2.0+ cyberware menus.
- Excludes: concealed vendor-stock changes at future levels; cosmetic body
  appearance; hidden enemy implants outside scanner disclosure.
- Parameters: capacity, slot, implant, tier, armour, attunement, effect, price,
  components and compatibility.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## INF-150 — Character roster exposes roles, kits and composition alternatives

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the match selection interface exposes currently available
  characters, their role or class, ability kit, allied occupancy and any
  offered composition alternatives before confirmation.
- Includes: Marvel Rivals Season 9.5 hero and Team-Up selection state; Apex
  Legends Legend classes, kits and current squad occupancy.
- Excludes: hidden opponent selection before disclosure; cosmetic skin details;
  external tier-list recommendations.
- Parameters: character, role or class, team occupancy, ability, composition
  option, base effect, enhanced effect and selection state.
- Evidence: [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md) and
  [Apex Legends decomposition](../games/a-f/apex-legends.md).
- Novelty: not assessed.

## INF-151 — Match HUD exposes team, phase and live objective state

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `INF-116`.
- Includes: historical references that used `INF-151` before registry
  normalisation 006.
- Excludes: new game signatures; use `INF-116` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md).
- Merged into: `INF-116` by
  [`TAXONOMY_CHANGE_014`](../../research/taxonomy-changes/TAXONOMY_CHANGE_014.md).

## INF-152 — Dice interface exposes difficulty, modifiers and reroll state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before and during an eligible explicit check, the interface
  exposes its difficulty, governing skill, current modifiers, available bonus
  sources, advantage or disadvantage and remaining Inspiration rerolls without
  revealing every downstream narrative consequence.
- Includes: Baldur's Gate 3 dialogue and explicit ability-check dice interface.
- Excludes: automatic passive checks; hidden future quest branches; damage dice.
- Parameters: difficulty, skill, modifier, proficiency, bonus, advantage,
  disadvantage, rolled total, success, failure and Inspiration.
- Evidence: [Baldur's Gate 3 decomposition](../games/a-f/baldurs-gate-3.md).
- Novelty: not assessed.

## INF-153 — Party interface exposes active members, condition and approval

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: party frames and character sheets identify the current active
  members and expose their health, conditions, concentration, equipment and
  inspectable approval state before control, treatment or formation changes.
- Includes: Baldur's Gate 3 single-player party HUD and companion sheets.
- Excludes: exact concealed approval triggers; inactive strangers; romance state.
- Parameters: member, active slot, health, condition, concentration, equipment,
  approval value or category and selected control.
- Evidence: [Baldur's Gate 3 decomposition](../games/a-f/baldurs-gate-3.md).
- Novelty: not assessed.

## INF-154 — Rest interface exposes recovery and camp-supply commitment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before committing a short or long rest, the interface identifies
  the rest type, remaining short-rest opportunities, required and selected camp
  supplies and whether the resulting long rest will be full or partial.
- Includes: Baldur's Gate 3 Balanced rest and camp-supply interfaces.
- Excludes: concealed future camp scenes; external inventory calculators;
  restoration from a spell or potion.
- Parameters: rest type, remaining uses, required supplies, selected supplies,
  full-rest state, partial-rest state and declared recovery.
- Evidence: [Baldur's Gate 3 decomposition](../games/a-f/baldurs-gate-3.md).
- Novelty: not assessed.

## INF-155 — Deployment map exposes objectives and legal team sources

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before redeployment, the team map identifies current objective
  ownership, squad positions, active beacons, available vehicles and whether
  each candidate source can presently accept the configured combatant.
- Includes: Battlefield 6 Conquest deployment interface and source icons.
- Excludes: omniscient enemy positions; ordinary first-person minimap use after
  deployment; external voice coordination.
- Parameters: objective, owner, squad source, combat state, beacon, vehicle,
  seat, timer, availability and selection focus.
- Evidence: [Battlefield 6 decomposition](../games/a-f/battlefield-6.md).
- Novelty: not assessed.

## INF-156 — Focus Mode highlights wounds and breakable monster parts

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while Focus Mode is held, the view marks open localized wounds
  and compatible breakable body regions before the player aims a Focus Strike.
- Includes: Monster Hunter Wilds Focus Mode wound and weak-part highlights.
- Excludes: exact hidden monster health; a damage number alone; an external
  weakness guide.
- Parameters: focus state, body region, wound state, breakable state, highlight
  and occlusion.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## INF-157 — Hunt HUD exposes target, clock, faint allowance and monster condition

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the quest interface identifies the active target, remaining
  attempt conditions and observable monster status needed to judge pursuit,
  success or failure without exposing exact hidden health.
- Includes: Monster Hunter Wilds assignment target, timer, faint state and
  visible monster condition or minimap state.
- Excludes: exact internal health values; future drop rolls; external overlays.
- Parameters: target, timer, faint allowance, engagement, condition, zone and
  completion state.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## INF-158 — Scoutflies expose a selected target route or last known position

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the navigation layer marks the current route toward a selected
  objective, resource or tracked monster and updates to its current or last
  known field position as evidence changes.
- Includes: Monster Hunter Wilds scoutflies and target map route.
- Excludes: omniscient disclosure of every monster; direct automatic movement;
  an external map guide.
- Parameters: selected target, evidence, current position, last known position,
  route segment, update and lost state.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## INF-159 — Combat HUD exposes resources, equipment and carried runes

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the live HUD discloses HP, FP, stamina, statuses, equipped
  armaments, selected actions and the current carried-rune count.
- Includes: Elden Ring base combat HUD and compass.
- Excludes: hidden stance values; undiscovered loot; future boss phases.
- Parameters: gauges, status, slots, skill, item, runes and target health.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## INF-160 — Map exposes fragments, Grace, guidance and the rune mark

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the world map reveals acquired regional detail, discovered Grace,
  advisory guidance, placed markers and the active dropped-rune location.
- Includes: scoped Elden Ring Limgrave map information.
- Excludes: undiscovered exact terrain; forced routing; enemy omniscience.
- Parameters: fragment, region, Grace, guidance, marker and rune mark.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## INF-161 — Equipment panels expose requirements, scaling and load tier

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: equipment interfaces disclose armament requirements and scaling,
  attack or defence values, weight, capacity and resulting load tier.
- Includes: Elden Ring early equipment and status panels.
- Excludes: hidden enemy stance; undiscovered upgrade results; cosmetic preview.
- Parameters: item, requirements, scaling, values, weight, capacity and tier.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## INF-162 — Grace menus expose level price, flask split and reset choices

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an eligible Grace menu shows available rest functions, next level
  cost, attribute preview and current flask allocation before commitment.
- Includes: Elden Ring early Grace levelling and flask menus.
- Excludes: concealed later menu unlocks; live combat HUD; merchant stock.
- Parameters: menu unlock, level price, preview, charges, allocation and time.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## INF-163 — Explored minimap retains lit terrain and world-state icons

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the character-bound minimap retains the brightest explored tile
  state, updates later visible terrain mutations and marks known spawn points,
  town NPCs, bosses and the most recent death location.
- Includes: Terraria 1.4.5.6 portrait, overlay and full-screen minimap modes.
- Excludes: unreached dark terrain; another character's map history; exact
  future spawns or hidden chest contents.
- Parameters: explored brightness, tile update, character map, icon class,
  zoom, mode and death position.
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## INF-164 — Housing query exposes room validity and NPC assignment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the housing interface identifies available town NPCs and assigned
  rooms, and an addressed-room query reports suitability or a prioritised
  missing frame, wall, furniture, occupancy or home-tile condition.
- Includes: Terraria housing menu, NPC flags and question-mark validation tool.
- Excludes: hidden exact arrival time; biome-happiness optimisation not shown by
  the query; visual decoration with no housing consequence.
- Parameters: NPC flag, room, assignment, validity, failed category and message.
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## INF-165 — World and boss cues expose night risk and Eye state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: environmental light and celestial motion, status messages, enemy
  appearance, boss bar, sprite transformation and minimap icon disclose the
  current day-night risk and live Eye encounter state without revealing its AI rolls.
- Includes: Terraria dusk/night cues, evil-presence warning and first Eye fight.
- Excludes: exact hidden natural-spawn roll; future attack coordinates; external clocks.
- Parameters: phase of day, warning, boss health, phase cue, target icon and dawn.
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## INF-166 — Progressive themed-path discovery and earned route disclosure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the interface begins with one broad semantic clue and a visible
  letter field, retains every accepted answer as an addressed path, reports
  assistance progress, and can progressively disclose an unresolved answer's
  cell set and then its traversal order after earned requests.
- Includes: Strands' Today's Theme clue, retained theme-word and spangram paths,
  Hint meter, highlighted answer letters and subsequent ordered-letter hint.
- Excludes: exposing the complete hidden answer partition at entry; feedback
  about only positional similarity to a guessed word; an unearned walkthrough;
  a clue whose text itself is the answer.
- Parameters: clue specificity, path colours or labels, retained word list,
  progress display, hinted target choice, cell highlight and order notation.
- Evidence: [Strands decomposition](../games/s-z/strands.md).
- Novelty: not assessed.

## INF-167 — Concurrent partner viewport exposes live cooperative state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while each human controls one actor, the interface concurrently
  renders the partner's live viewpoint alongside the local viewpoint so that
  both positions, hazards, prompts and interaction progress can inform current
  coordination without changing control ownership.
- Includes: Split Fiction's persistent split-screen presentation in local and
  online cooperative play.
- Excludes: a minimap icon without the partner's view; switching a single
  camera between actors; an external streamed screen; hidden role-exclusive
  information that must be communicated verbally.
- Parameters: pane count, layout, local-player emphasis, online rendering,
  shared overlays, prompt duplication and cutscene behaviour.
- Evidence: [Split Fiction decomposition](../games/s-z/split-fiction.md).
- Novelty: not assessed.

## INF-168 — Active-resident panel exposes motives, mood and action queue

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live interface exposes the active resident's current motive
  levels, dominant emotion and ordered or executing interactions so the player
  can attribute behaviour and revise near-term direction.
- Includes: The Sims 4 Live Mode needs panel, emotional state and visible
  interaction queue for Farrah Nouvel.
- Excludes: a colony aggregate; a biography-only profile; hidden exact future
  autonomy choices or relationship outcomes.
- Parameters: motive categories, value resolution, mood label, contributing
  modifiers, queue order, cancellation affordance and failed-action feedback.
- Evidence: [The Sims 4 decomposition](../games/s-z/the-sims-4.md).
- Novelty: not assessed.

## INF-169 — Debrief separates mission, extraction and shared-war results

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the post-mission presentation separately exposes whether the
  required objective succeeded, which participants and carried shared assets
  departed, and what operation-level contribution entered the shared campaign.
- Includes: Helldivers 2 mission debrief separating objective success,
  extracted Helldivers, recovered samples and Galactic War impact.
- Excludes: a single undifferentiated score; live tactical HUD; private account
  experience without any operation or shared-campaign result.
- Parameters: mission result, survivor count, asset types/counts, operation
  status, contribution components, planet and campaign progress.
- Evidence: [Helldivers 2 decomposition](../games/g-l/helldivers-2.md).
- Novelty: not assessed.

## INF-170 — Battle HUD exposes partner, target, health, moves and cooldowns

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live battle interface identifies the sole active companion
  and current target while exposing health plus the bounded assigned move set
  and each move's current readiness.
- Includes: Pokémon Legends: Z-A partner/target health and four move-button
  cooldown displays.
- Excludes: a storage-only profile; hidden opponent future decisions; an
  unlabelled animation with no readiness feedback.
- Parameters: active partner, target, health, move slots, input mapping,
  cooldown, range feedback and status.
- Evidence: [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Novelty: not assessed.

## INF-171 — Royale interface exposes rank, points, ticket and promotion target

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the progression interface exposes the current tournament rank,
  accumulated qualification points and threshold, ticket possession and the
  designated opponent for the next promotion.
- Includes: Rank Z, 1,000 Ticket Point threshold, Challenger's Ticket and Zach
  promotion state in Pokémon Legends: Z-A.
- Excludes: hidden matchmaking rating; battle experience; a generic quest title
  without qualification state.
- Parameters: rank, points, threshold, ticket, opponent and promotion status.
- Evidence: [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Novelty: not assessed.

## INF-172 — Terror Radius encodes approximate Killer proximity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: survivor audio layers intensify as the Killer enters nearer bands
  and change for an active chase, communicating approximate threat proximity
  without revealing the Killer's exact coordinate or route.
- Includes: Dead by Daylight heartbeat, Terror Radius music and chase layer in
  the blank-loadout standard Trial.
- Excludes: Killer-specific Undetectable or Lullaby exceptions; exact aura
  reading; ordinary spatial footsteps already covered by local sound.
- Parameters: source, radius, proximity bands, audio layers, chase state,
  listener role and suppression exceptions.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Novelty: not assessed.

## INF-173 — Killer-only transient tracks expose recent Survivor routes

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: recent running and injury leave spatial track cues visible to the
  Killer role but ordinarily hidden from Survivors, disclosing a fading route
  rather than the tracked Survivor's current exact position.
- Includes: Dead by Daylight Scratch Marks and Pools of Blood.
- Excludes: audible footsteps; public teammate HUD state; exact temporary aura
  revelation from a Perk.
- Parameters: cue class, source state, location, direction quality, role
  visibility, intensity, duration and decay.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Novelty: not assessed.

## INF-174 — Work progress and Skill Check window are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while a Survivor performs eligible work, the interface exposes
  current progress and, when sampled, a moving timing pointer with graded
  response zones plus immediate success or failure feedback.
- Includes: Dead by Daylight repair, healing, recovery, unhook and gate progress
  bars together with Good/Great Skill Check intervals.
- Excludes: hidden future prompt location; post-match score events; attack-
  timing cues without a continuing work bar.
- Parameters: interaction, progress, efficiency colour, pointer, success zones,
  warning, response grade and failure feedback.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Novelty: not assessed.

## INF-175 — Item panels expose rarity, affixes, requirements and comparison

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: inspecting ground, carried or equipped gear exposes its base and
  rarity, explicit modifiers, sockets and unmet requirements, with the relevant
  equipped alternative available for comparison.
- Includes: Path of Exile 2 equipment tooltips and comparison panels.
- Excludes: hidden future affix rolls; external trade valuation; an unlabelled
  item model with no statistics.
- Parameters: item identity, rarity, modifiers, sockets, requirements,
  comparison slot, deltas and unusable warning.
- Evidence: [Path of Exile 2 decomposition](../games/m-r/path-of-exile-2.md).
- Novelty: not assessed.

## INF-176 — Skill panels expose sockets, compatibility, cost and effect

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the Skills interface exposes each active Skill's assigned input,
  Support sockets and occupants, compatibility feedback, resource cost and the
  effect produced by the current composed Gem state.
- Includes: Path of Exile 2 active Skill and Support management.
- Excludes: hidden exact future damage outcomes; passive-tree topology; item
  affixes unrelated to the selected Skill.
- Parameters: Skill, input, sockets, Supports, tags, cost, damage or utility
  summary, warnings and resulting changes.
- Evidence: [Path of Exile 2 decomposition](../games/m-r/path-of-exile-2.md).
- Novelty: not assessed.

## INF-177 — Passive tree exposes connections, effects and available points

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the character-development view exposes current allocated nodes,
  adjacent reachable nodes, each inspected node's effect, unspent points and
  the declared refund cost so the next connected allocation is attributable.
- Includes: Path of Exile 2 Passive Skill Tree in the scoped campaign.
- Excludes: hidden optimal builds; the active Skill socket panel; account-wide
  Atlas progression.
- Parameters: root, allocated and adjacent nodes, effect text, point count,
  refund currency and confirmation.
- Evidence: [Path of Exile 2 decomposition](../games/m-r/path-of-exile-2.md).
- Novelty: not assessed.

## INF-178 — Broadcast view identifies ball, control and local team shape

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live match view exposes the shared ball, nearby players,
  pitch markings, the current direct-control marker and context for the next
  eligible control or ball action.
- Includes: broadcast camera, player indicator and local formation shape in EA
  SPORTS FC 26.
- Excludes: permanent omniscient player attributes; post-match heat maps; a
  manager-only tactical board.
- Parameters: camera, zoom, indicator, radar availability, player labels,
  pitch markings and suggested-switch cue.
- Evidence: [EA SPORTS FC 26 decomposition](../games/a-f/ea-sports-fc-26.md).
- Novelty: first isolated for `GAME-0163`.

## INF-179 — Current room exposes threats, trajectories, pickups and exits

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the room camera simultaneously exposes Isaac, visible enemies,
  projectiles, hazards, obstacles, pickups and door states needed to choose the
  next movement, attack or resource action.
- Includes: ordinary base-Rebirth room play and boss encounters.
- Excludes: concealed adjacent-room contents; exact hidden drop rolls; an
  external item-description overlay.
- Parameters: room bounds, actor, projectile, hazard, obstacle, pickup, door,
  boss bar and visual effect.
- Evidence: [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md).
- Novelty: first isolated for `GAME-0164`; existing partial-opponent sight genes
  do not expose a complete bounded room's shared projectile field and exits.

## INF-180 — Explored map retains room graph and disclosed room roles

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the minimap retains every discovered room cell and connection on
  the current floor and marks the identity of eligible disclosed special rooms
  without revealing all unexplored contents.
- Includes: base-Rebirth explored ordinary, Treasure, Shop and boss room map state.
- Excludes: a fully revealed future floor; a non-spatial branching act-node
  chart; secret rooms not yet disclosed by an eligible effect or entry.
- Parameters: cell, adjacency, explored state, current room, room-role icon,
  concealment and map-reveal effect.
- Evidence: [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md).
- Novelty: first isolated for `GAME-0164`.

## INF-181 — Horse interface exposes bond, condition and saddle cargo

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: horse HUD, wheel and management views expose the current horse's
  identity, health, stamina, bond, active saddle and accessible weapon, outfit
  or carcass cargo before a riding or transfer decision.
- Includes: Arthur's current horse during the scoped Chapter 2 route.
- Excludes: hidden wild-horse traits before inspection; motor-vehicle state;
  cosmetic horse appearance with no mechanical value.
- Parameters: horse, health, stamina, core, bond, saddle, cargo slot, carried
  weapon, outfit and call state.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`.

## INF-182 — Legal and honour interface exposes report and consequence state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: contextual prompts, minimap marks and status displays disclose
  an active witness and identification state, reported crime, law search,
  regional bounty and current honour movement or band before the next response.
- Includes: scoped Chapter 2 witness, wanted, bounty and honour feedback.
- Excludes: exact hidden future witness compliance; undisclosed law spawns;
  companion-specific affinity.
- Parameters: witness marker, identity, report phase, search area, bounty,
  jurisdiction, honour change, band and contextual prompt.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`.

## INF-183 — Camp ledger exposes shared funds, supplies and upgrades

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the donation ledger and camp status icons expose recent
  contributions, shared balance, medicine, ammunition and food supply state,
  offered restocks, upgrade prerequisites, prices and purchased effects.
- Includes: the unlocked Horseshoe Overlook camp ledger during Chapter 2.
- Excludes: Arthur's private wallet alone; hidden future gang donations;
  flavour-only camp decoration with no registered effect.
- Parameters: contribution, balance, category, stock band, offer, predecessor,
  price, purchase and service effect.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`.

## INF-184 — Explored hex map retains terrain, resources and borders

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the world view retains every explored hex's known terrain,
  features, disclosed resources, improvements, districts, roads and borders
  while distinguishing current visibility from remembered fog.
- Includes: the scoped seeded Pangaea map in Civilization VI.
- Excludes: exact contents of never-seen fog; hidden rival orders; a room minimap.
- Parameters: hex, exploration, visibility, terrain, feature, resource,
  improvement, road, district and owner.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## INF-198 — Quick-job market exposes supplied contract terms

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before acceptance, the market exposes each current offer's cargo,
  origin, destination, route distance, deadline, advertised income and supplied
  vehicle needed to compare one employer job with another.
- Includes: Euro Truck Simulator 2 Quick Jobs.
- Excludes: owned-truck Freight Market costs; undisclosed future offers; an
  autonomous employee's completed-job log.
- Parameters: offer, cargo, weight, origin, destination, distance, deadline,
  income, truck, trailer and expiration.
- Evidence: [Euro Truck Simulator 2 decomposition](../games/a-f/euro-truck-simulator-2.md).
- Novelty: first isolated for `GAME-0169`; earlier job displays do not expose a
  complete supplied direct-drive cargo contract.

## INF-199 — Driving widgets expose vehicle, damage and rest state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the live driving interface exposes current speed, selected gear,
  fuel, Rest State, time until Mandatory Break and separate truck, trailer and
  cargo damage needed to decide whether and how to continue the haul.
- Includes: Euro Truck Simulator 2 update 1.60 widgets and Quick Info.
- Excludes: exact future traffic; hidden internal component values below the
  interface boundary; post-delivery reward settlement.
- Parameters: speed, gear, fuel, rest state, break time, truck damage, trailer
  damage, cargo damage, malfunction and widget visibility.
- Evidence: [Euro Truck Simulator 2 decomposition](../games/a-f/euro-truck-simulator-2.md).
- Novelty: first isolated for `GAME-0169`; earlier vehicle HUD genes do not join
  articulated cargo condition to separate physiological and legal rest clocks.

## INF-200 — Job and GPS widgets expose delivery progress

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during an active delivery, the interface exposes cargo type and
  weight, destination, advertised income, remaining completion time, estimated
  arrival, remaining travel time and route distance.
- Includes: Euro Truck Simulator 2 update 1.60 Job Details and GPS widgets.
- Excludes: exact future traffic delay; a job-market offer not yet accepted;
  final deductions and experience after delivery.
- Parameters: cargo, weight, destination, income, deadline remainder, arrival
  day and time, travel time, distance and route recalculation.
- Evidence: [Euro Truck Simulator 2 decomposition](../games/a-f/euro-truck-simulator-2.md).
- Novelty: first isolated for `GAME-0169`; earlier route views do not combine a
  live cargo contract's economic terms with ETA and deadline slack.

## INF-201 — Delivery results expose one-job settlement

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `Medium`
- Definition: after delivery, the results interface exposes the completed job's
  evaluation, settled income, eligible time or damage adjustments, parking
  experience and resulting profile credit.
- Includes: Euro Truck Simulator 2 Quick Job result screen.
- Excludes: live GPS state before drop-off; recurring company profit; a traffic
  fine notification already applied on the road.
- Parameters: evaluation, base income, adjustments, paid income, base
  experience, parking experience and profile totals.
- Evidence: [Euro Truck Simulator 2 decomposition](../games/a-f/euro-truck-simulator-2.md).
- Novelty: first isolated for `GAME-0169`; earlier summaries do not expose the
  economic and experience settlement of one directly driven cargo contract.

## INF-202 — HUD exposes survival pressure and quick-use state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the live interface exposes health, stamina, bleeding, hunger,
  overload and radiation pressure together with selected weapon ammunition and
  four assigned quick-use slots.
- Includes: the scoped S.T.A.L.K.E.R. 2 HUD and inventory weight indication.
- Excludes: hidden future damage; undiscovered loot; all downstream consequences
  of a dialogue choice.
- Parameters: health, stamina, effect icon, radiation meter, load colour,
  quick slot, weapon, magazine, reserve and fire mode.
- Evidence: [S.T.A.L.K.E.R. 2 decomposition](../games/s-z/stalker-2-heart-of-chornobyl.md).
- Novelty: first isolated for `GAME-0170`; it joins radiation and overload with
  the immediate first-person treatment and ammunition interface.

## INF-203 — Detector signal exposes artifact proximity

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: an active detector communicates changing direction or distance to
  a nearby hidden artifact and marks the critical range at which it can appear.
- Includes: Echo Detector signal cadence during both scoped artifact searches.
- Excludes: revealing the artifact's future sampled identity; showing ordinary
  ground loot; an external walkthrough coordinate.
- Parameters: detector model, direction, distance, signal cadence, critical
  range, artifact class and manifestation state.
- Evidence: [S.T.A.L.K.E.R. 2 decomposition](../games/s-z/stalker-2-heart-of-chornobyl.md).
- Novelty: first isolated for `GAME-0170`; the signal is a continuous local
  measurement that precedes visual access to its target.

## INF-195 — Expose the partial mission route through map and markers

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the live HUD shows the locally revealed portion of the assembled
  mission map, the player, nearby contacts and the current objective or
  extraction marker without revealing every unopened branch.
- Includes: minimap and white/yellow objective guidance in Awakening and Vor's
  Prize.
- Excludes: the full future tile graph; Navigation's planetary node selection;
  an external walkthrough route.
- Parameters: revealed tiles, player position, contacts, objective, extraction,
  marker colour, distance and occlusion.
- Evidence: [Warframe decomposition](../games/s-z/warframe.md).
- Novelty: first isolated for `GAME-0168`; existing maps do not expose a
  progressively revealed generated route plus its current mission endpoint.

## INF-196 — Expose equipment ranks, Mod slots and resulting statistics

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the Arsenal and upgrade interface show selected equipment,
  separate ranks, compatible Mod slots, capacity, polarities, drain and the
  resulting statistic changes before live play resumes.
- Includes: starter Warframe and weapon configuration in Vor's Prize.
- Excludes: hidden damage formulas; unidentified future drops; cosmetic-only
  appearance editing.
- Parameters: item, rank, statistics, slots, compatibility, capacity, polarity,
  drain, preview and validation feedback.
- Evidence: [Warframe decomposition](../games/s-z/warframe.md).
- Novelty: first isolated for `GAME-0168`; earlier equipment views do not expose
  this capacity-and-polarity modifier calculation.

## INF-197 — Expose mission rewards, Affinity changes and next quest state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: mission completion and the returning Orbiter state show retained
  rewards, equipment Affinity/rank changes, restored functions and the next
  available opening-quest step.
- Includes: the Vor's Prize settlement loop from extraction back to Navigation,
  Arsenal, Foundry or Mod Station.
- Excludes: temporary ammunition; later quest spoilers; undisclosed random
  reward outcomes before extraction.
- Parameters: mission, pickups, reward, Affinity, ranks, segment, quest step,
  next mission and presentation timing.
- Evidence: [Warframe decomposition](../games/s-z/warframe.md).
- Novelty: first isolated for `GAME-0168`; earlier result screens do not combine
  retained equipment growth with restoration of a persistent tutorial hub.

## INF-192 — Side-scrolling viewport exposes local obstacle lookahead

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the running side view exposes the icon, current support and a
  bounded forward slice of blocks, gaps, spikes, portals and optional routes,
  while later authored geometry remains outside the viewport.
- Includes: the moving Stereo Madness playfield in cube and ship sections.
- Excludes: simultaneous disclosure of the full level; editor view; hidden
  collision objects; a minimap that reveals the entire future route.
- Parameters: camera anchor, forward margin, viewport width, scroll speed,
  object classes, occlusion and visual-effect contrast.
- Evidence: [Geometry Dash decomposition](../games/g-l/geometry-dash.md).
- Novelty: first isolated for `GAME-0167`; `INF-001` requires every
  decision-relevant current-board element to be inspectable, whereas this
  auto-run deliberately reveals only a live local horizon.

## INF-193 — Attempt, progress and Secret Coin state are visible

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the level interface identifies the current attempt, exposes
  proportional route progress and reports contacted or persistently credited
  Secret Coins and completion feedback without revealing future geometry.
- Includes: Stereo Madness attempt counter, progress percentage/bar, coin
  feedback and 100% completion presentation under the scoped UI settings.
- Excludes: an external speedrun overlay; user-level leaderboards; exact future
  obstacle timing; account-wide achievement statistics.
- Parameters: attempt number, percentage precision, bar visibility, coin slots,
  pending versus credited state and completion banner.
- Evidence: [Geometry Dash decomposition](../games/g-l/geometry-dash.md).
- Novelty: first isolated for `GAME-0167`; earlier progress interfaces report
  work, mission or tournament state rather than clean-retry route execution.

## INF-194 — Soundtrack and pulses cue the authored obstacle cadence

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the fixed soundtrack and synchronised visual pulses provide
  recurring temporal cues for the authored obstacle sequence, letting learned
  input timing be aligned before the corresponding geometry reaches the icon.
- Includes: Stereo Madness's fixed music, colour pulses and repeated route timing.
- Excludes: a song selected independently of level geometry; metronome scoring
  that grades presses against beats; music muted as a parameter.
- Parameters: song, offset, cue events, obstacle positions, audio latency,
  visual pulse, mute state and learned timing.
- Evidence: [Geometry Dash decomposition](../games/g-l/geometry-dash.md).
- Novelty: first isolated for `GAME-0167`; earlier audio-timing genes telegraph
  hostile attacks rather than one replayed platform route.

## INF-185 — City panel exposes yields, growth, production and citizens

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the city interface shows population, worked tiles and specialists,
  Food and growth, Housing, Amenities, current Production target/progress and
  the city's other yield contributions before reassignment.
- Includes: each Roman city in the scoped Civilization VI route.
- Excludes: hidden rival city values; empire diplomacy; district placement preview.
- Parameters: city, population, assignments, yields, food, growth, Housing,
  Amenities, production target and progress.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## INF-186 — District lens exposes legal hexes and adjacency preview

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before placement, the map marks district-eligible and ineligible
  city hexes and exposes the adjacency yield predicted for each legal choice.
- Includes: Campus, Industrial Zone and Spaceport placement in Civilization VI.
- Excludes: hidden future resource spawns; citizen tile assignment; wonder animation.
- Parameters: city, district, hex, legality, terrain, occupancy, neighbours and adjacency.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## INF-187 — Government view exposes typed slots and policy effects

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the government interface exposes available governments, their
  inherent effects and typed slot frames, plus unlocked policy cards, card
  effects, current assignments and incompatibility feedback.
- Includes: base-game policy configuration in Civilization VI.
- Excludes: hidden AI policies; expansion Governor promotions; civic-tree progress.
- Parameters: government, effects, slot types, cards, assignments, unlocks and warnings.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## INF-188 — Diplomacy view exposes relationships, agreements and war state

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: contacted-civilization views expose current relationship cues,
  available deal terms, active agreements, war/peace state, treaty gates and
  disclosed warmonger consequences before a diplomatic action.
- Includes: Greece, Egypt and Germany in the scoped game.
- Excludes: exact hidden future acceptance calculations; city-state envoy state;
  multiplayer chat.
- Parameters: rival, relationship, agenda feedback, deal terms, agreement,
  war, peace, timer and warmonger value.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## INF-189 — Trade view exposes capacity, destinations and route yields

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: trader selection shows used and available route capacity,
  eligible origin/destination pairs, predicted yields, duration and route state
  before the player commits a destination.
- Includes: domestic and international base-game trade routes.
- Excludes: diplomatic lump-sum trades; hidden hostile routes; manual road planning.
- Parameters: capacity, trader, origin, destination, path, yields, duration and trading post.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## INF-190 — Unit interface exposes movement, actions and combat forecast

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: selecting a unit exposes remaining movement, health, strength,
  available commands, reachable hexes and the declared forecast for an eligible
  attack before commitment.
- Includes: Roman civilian, melee and ranged units in Civilization VI.
- Excludes: exact hidden random damage; city production choices; rival future orders.
- Parameters: unit, movement, health, strength, commands, range, target and forecast.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## INF-191 — Victory view exposes science milestones and rival progress

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the victory interface shows Rome's completed and outstanding
  Science milestones and disclosed progress by each rival toward the enabled
  terminal, allowing the remaining launch race to be compared.
- Includes: Satellite, Moon Landing and three Mars modules in the scoped route.
- Excludes: disabled victory conditions; exact future completion turns;
  Gathering Storm exoplanet speed.
- Parameters: civilization, enabled victory, milestone, completion, rival
  comparison and terminal state.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`.

## INF-204 — Driving HUD exposes speed, gear and route guidance

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the live driving view exposes current speed and gear together
  with the authored or waypoint route cues needed to judge braking and steering.
- Includes: Forza Horizon 6 speedometer, gear, minimap/GPS and configurable
  driving line in the scoped opening.
- Excludes: event eligibility before entry; hidden future traffic; post-event
  settlement.
- Parameters: speed, gear, route, minimap, driving line, braking cue, waypoint
  and camera.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md).
- Novelty: first isolated for `GAME-0171`; cargo-driving widgets join speed to
  fuel, rest and damage rather than a race-oriented guidance layer.

## INF-205 — Race HUD exposes position, course progress and nearby rivals

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during a driving event, the interface exposes current place or
  timed target, lap/checkpoint progress, elapsed or remaining time and locally
  sensed rival vehicles needed to revise the racing line.
- Includes: Forza Horizon 6 Festival races and Time Attack in the scoped route,
  including configurable Proximity Radar.
- Excludes: omniscient future rival paths; free-roam traffic with no event
  result; the final reward panel.
- Parameters: position, participant count, lap, checkpoint, time, split,
  proximity direction, distance and audio cue.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md).
- Novelty: first isolated for `GAME-0171`; prior opponent HUD genes do not join
  course progress to vehicle proximity and race position.

## INF-206 — Map and event card expose driving-event terms

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the world map and selected event panel disclose its location,
  type, route form, current unlock, vehicle eligibility and available reward or
  campaign contribution before entry.
- Includes: the six exposed Horizon Qualifiers and first Horizon Invitational.
- Excludes: undiscovered optional content; live race position; post-completion
  Race Customizer options unavailable on first play.
- Parameters: marker, location, event type, route, car theme, class, unlock,
  progress value and reward.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md).
- Novelty: first isolated for `GAME-0171`; generic mission maps do not expose
  one driving event's course and car-entry contract.

## INF-207 — Festival meter exposes progress and the next Wristband gate

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the campaign interface shows retained Horizon Festival Points,
  the required next threshold and whether the corresponding Wristband Event is
  still locked or available.
- Includes: the upper-right Qualifier meter and first Invitational status in
  Forza Horizon 6.
- Excludes: Discover Japan Stamp progress; live Festival Playlist points;
  hidden future reward rolls.
- Parameters: current points, threshold, remaining points, gate, invitation and
  Wristband identity.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md).
- Novelty: first isolated for `GAME-0171`; earlier progression interfaces do
  not expose a heterogeneous driving-activity total and its terminal event gate.

## INF-208 — Driving-event results expose performance and retained rewards

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a valid finish, the results transition exposes place, time
  or rating, earned Festival progress and any credits, experience, vehicles or
  campaign unlocks retained from that event.
- Includes: Forza Horizon 6 Qualifier and first-Wristband settlement panels.
- Excludes: live HUD values before the finish; an unclaimed Playlist reward;
  hidden future Wheelspin outcomes.
- Parameters: event, position, time, stars, points, credits, experience, vehicle
  and unlock.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md).
- Novelty: first isolated for `GAME-0171`; delivery results expose contract
  damage and pay, not competitive driving performance and festival progress.
