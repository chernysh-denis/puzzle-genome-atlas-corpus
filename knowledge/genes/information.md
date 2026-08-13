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
  terms and current Thinking-panel assignments.
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
  and [Tactical Breach Wizards decomposition](../games/s-z/tactical-breach-wizards.md).
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
- Includes: fixed mine locations under covered Minesweeper cells; the current
  concealed order of Balatro's remaining draw pile while the hand and remaining
  deck composition are inspectable; the current concealed order of Fights in
  Tight Spaces' draw pile while the visible hand and deck contents constrain
  future card availability.
- Excludes: a future random event not yet selected; an inspectable element that
  is merely offscreen; information the player once saw and forgot.
- Parameters: setup distribution, known global content count, first-action
  conditioning and reveal permanence.
- Evidence: [Minesweeper decomposition](../games/m-r/minesweeper.md) and
  [Balatro decomposition](../games/a-f/balatro.md), and
  [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md).
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
  input assembly and required output product.
- Includes: Opus Magnum's visible input and output molecular diagrams;
  SpaceChem's visible reagent and required product bond structures, with screen
  orientation ignored where acceptance uses graph equivalence; Infinifactory's
  visible input and target voxel arrangements with required output orientation.
- Excludes: revealing only a target score or category; hidden transformation
  rules; visibility of material currently moving through the machine.
- Parameters: input and output count, identity vocabulary, relation or bond
  representation, spatial geometry, orientation and equivalence rule.
- Evidence: [Opus Magnum decomposition](../games/m-r/opus-magnum.md) and
  [SpaceChem decomposition](../games/s-z/spacechem.md), and
  [Infinifactory decomposition](../games/g-l/infinifactory.md).
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
