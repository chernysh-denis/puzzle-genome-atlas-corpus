# Action Genes

## ACT-001 — Global directional slide

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects a direction and attempts to translate every
  movable element along that direction.
- Includes: one input globally coupled across multiple rows or columns.
- Excludes: selecting one element and moving it independently; automatic
  compression after the direction has been chosen.
- Parameters: direction set, affected topology, movement distance.
- Evidence: [2048 decomposition](../games/0-9/2048.md) and
  [Threes decomposition](../games/s-z/threes.md).
- Novelty: not assessed; this is part of the baseline genome.

## ACT-002 — Direct layer rotation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player directly selects a coupled layer of elements and
  rotates that layer as one rigid action.
- Includes: an outer face-layer turn of a standard 3 × 3 Rubik's Cube.
- Excludes: rotating the whole object only to change viewpoint; rotating one
  element independently; an automatic rotation caused by another action.
- Parameters: available axes, selectable layers, permitted turn angles and move
  metric.
- Evidence: [Rubik's Cube decomposition](../games/m-r/rubiks-cube.md).
- Novelty: not assessed.

## ACT-003 — Select concealed cell for reveal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one concealed position and commands its fixed
  underlying content to be exposed.
- Includes: uncovering one covered Minesweeper cell.
- Excludes: automatically exposed neighbouring cells; selecting already visible
  information; generating new random content after the selection.
- Parameters: input method, target geometry and first-selection protection.
- Evidence: [Minesweeper decomposition](../games/m-r/minesweeper.md).
- Novelty: not assessed.

## ACT-004 — Toggle protective hypothesis marker

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player marks or unmarks a concealed position as a suspected
  hazard without verifying its content, and the marker blocks ordinary reveal
  while present.
- Includes: flagging and unflagging a covered Minesweeper cell.
- Excludes: a system-confirmed hazard; a cosmetic note with no input effect;
  automatically revealing unmarked neighbours.
- Parameters: marker cycle, question-mark state, reveal protection and whether
  markers enable a bulk-reveal command.
- Evidence: [Minesweeper decomposition](../games/m-r/minesweeper.md).
- Novelty: not assessed.

## ACT-005 — Reposition active falling element

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while one element is descending under system control, the player
  directly changes its permitted horizontal position or orientation before it
  becomes fixed.
- Includes: moving or rotating the active tetromino in NES Tetris A-Type.
- Excludes: automatic descent; translating already fixed elements; rotating a
  coupled layer of a persistent object.
- Parameters: translation directions, rotation states, repeat timing and
  rotation model.
- Evidence: [Tetris decomposition](../games/s-z/tetris.md).
- Novelty: not assessed.

## ACT-006 — Accelerate automatic progression

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player temporarily increases the rate of an automatic
  time-driven state change without replacing its direction or terminal rule.
- Includes: holding down to make the active NES Tetris tetromino descend
  faster; selecting FAST mode to accelerate Pipe Dream's Flooz after pipe
  placement; selecting Mini Metro's faster simulation clock while automatic
  demand and transport continue; fast-forwarding a HUMANITY crowd simulation
  after its command field is ready; fast-forwarding Tin Hearts soldiers through
  an unchanged physical route; holding the Echochrome speed control while the
  Walker follows the same projection-governed route.
- Excludes: an instantaneous hard drop; selecting the direction of movement;
  changing a persistent difficulty setting outside play.
- Parameters: activation delay, accelerated rate and any score reward.
- Evidence: [Tetris decomposition](../games/s-z/tetris.md),
  [Pipe Mania decomposition](../games/m-r/pipe-mania.md), and
  [Mini Metro decomposition](../games/m-r/mini-metro.md), and
  [HUMANITY decomposition](../games/g-l/humanity.md), and
  [Tin Hearts decomposition](../games/s-z/tin-hearts.md), and
  [Echochrome decomposition](../games/a-f/echochrome.md).
- Novelty: not assessed.

## ACT-007 — Assign symbol to open position

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one currently assignable position and records
  one symbol from the permitted domain as that position's proposed value.
- Includes: placing a digit from 1 to 9 in an empty Sudoku cell; assigning a
  Nonogram cell as filled or confirmed empty; tapping an editable Hexologic
  cell to assign or replace its proposed value among one, two and three pips;
  assigning `/` or `\` to one Slant cell; assigning or removing a bulb in one
  white Light Up cell; assigning one of four palette colours to one editable
  Map region; assigning a digit from 1 through 9 to one editable Filling cell;
  assigning a digit from 1 through 6 to one Keen cell.
- Excludes: revealing a pre-existing concealed value; annotating several
  possible candidates without assigning one; changing an immutable given.
- Parameters: symbol domain, input medium and whether tentative assignments may
  be erased or replaced.
- Additional support: assigning a tent or an explicit non-tent mark to one
  editable Tents cell.
- Evidence: [Sudoku decomposition](../games/s-z/sudoku.md),
  [Nonogram decomposition](../games/m-r/nonogram.md), and
  [Hexologic decomposition](../games/g-l/hexologic.md), and
  [Slant decomposition](../games/s-z/slant.md), and
  [Tents decomposition](../games/s-z/tents.md), and
  [Light Up decomposition](../games/g-l/light-up.md), and
  [Map decomposition](../games/m-r/map.md), and
  [Filling decomposition](../games/a-f/filling.md), and
  [Keen decomposition](../games/g-l/keen.md).
- Novelty: not assessed.

## ACT-008 — Navigate controllable agent

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player directly advances one persistent controllable agent
  through traversable level geometry according to local movement inputs rather
  than selecting a remote destination for automatic pathfinding.
- Includes: moving the warehouse keeper one orthogonal floor cell in Sokoban
  without moving a crate; running and jumping the HUMANITY Shiba Inu through a
  trial to reach command positions; walking and jumping Chell through a Portal
  chamber; running and jumping Tim through a Braid stage; navigating the active
  Rescue Officer or Oatchi through a Pikmin 4 surface area; moving Patrick one
  cardinal local cell through a Patrick's Parabox nested space; walking and
  jumping the active The Swapper body through a puzzle room; walking Carto
  through the currently connected map-fragment landscape; walking and jumping
  through Viewfinder's current three-dimensional puzzle geometry; moving the
  A Good Snowman Is Hard to Build monster one cardinal garden cell; advancing
  a Snakebird head one cardinal grid cell while its body follows automatically;
  advancing either current Can of Wormholes endpoint one cardinal grid cell;
  walking an A Monster's Expedition monster across land or a completed log
  bridge; walking and jumping the Superliminal dreamer through the Induction
  room and its opened exit; walking, jumping and steering a fall through
  Manifold Garden's periodic Part 1 architecture; walking between Maquette's
  central model, scale-linked courtyards, key bridges and fixed house exit.
- Excludes: changing viewpoint; moving an adjacent object; teleporting or
  pathfinding that resolves several steps automatically.
- Parameters: adjacency or continuous topology, step distance, jump rules and
  input repetition.
- Evidence: [Sokoban decomposition](../games/s-z/sokoban.md),
  [HUMANITY decomposition](../games/g-l/humanity.md),
  [Portal decomposition](../games/m-r/portal.md), and
  [Braid decomposition](../games/a-f/braid.md), and
  [Pikmin 4 decomposition](../games/m-r/pikmin-4.md), and
  [Patrick's Parabox decomposition](../games/m-r/patricks-parabox.md), and
  [The Swapper decomposition](../games/s-z/the-swapper.md),
  [Carto decomposition](../games/a-f/carto.md), and
  [Viewfinder decomposition](../games/s-z/viewfinder.md), and
  [A Good Snowman Is Hard to Build decomposition](../games/a-f/a-good-snowman-is-hard-to-build.md),
  [Snakebird decomposition](../games/s-z/snakebird.md), and
  [Can of Wormholes decomposition](../games/a-f/can-of-wormholes.md), and
  [A Monster's Expedition decomposition](../games/a-f/a-monsters-expedition.md), and
  [Shogun Showdown decomposition](../games/s-z/shogun-showdown.md), and
  [The Talos Principle decomposition](../games/s-z/the-talos-principle.md), and
  [Fez decomposition](../games/a-f/fez.md), and
  [Superliminal decomposition](../games/s-z/superliminal.md), and
  [Manifold Garden decomposition](../games/m-r/manifold-garden.md), and
  [Maquette decomposition](../games/m-r/maquette.md), and
  [Antichamber decomposition](../games/a-f/antichamber.md).
- Novelty: not assessed.

## ACT-009 — Push adjacent movable object

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: by commanding the controllable agent toward one adjacent movable
  object with its body or attached tool, the player shifts that one object one
  logical position away; the agent or tool occupies the vacated contact side.
- Includes: pushing one Sokoban crate one orthogonal cell; pushing one
  `PUSH`-assigned object in Baba Is You; pushing one adjacent Patrick's Parabox
  box into a valid local or cross-boundary destination; displacing one
  Stephen's Sausage Roll sausage with the attached fork; pushing one A Good
  Snowman Is Hard to Build snowball into an empty cell or compatible stack
  destination; pushing one A Monster's Expedition tree or log from an adjacent
  reachable side before its direction-conditioned resolution.
- Excludes: pulling an object; selecting and moving an object independently of
  the agent; an automatic collision response.
- Parameters: object class, body-versus-attached-tool contact, adjacency
  topology, displacement distance and whether automatic resolution changes
  object orientation.
- Evidence: [Sokoban decomposition](../games/s-z/sokoban.md) and
  [Baba Is You decomposition](../games/a-f/baba-is-you.md), and
  [Patrick's Parabox decomposition](../games/m-r/patricks-parabox.md), and
  [Stephen's Sausage Roll decomposition](../games/s-z/stephens-sausage-roll.md),
  [A Good Snowman Is Hard to Build decomposition](../games/a-f/a-good-snowman-is-hard-to-build.md),
  and [A Monster's Expedition decomposition](../games/a-f/a-monsters-expedition.md).
- Novelty: not assessed.

## ACT-010 — Transfer accessible card between zones

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one currently accessible card and moves it to
  a destination zone whose placement rule accepts that card.
- Includes: moving an exposed FreeCell tableau card to another cascade, an
  empty free cell, an empty cascade or a legal foundation; moving a card from a
  free cell to a legal cascade or foundation.
- Excludes: revealing a concealed card; dealing a successor card; moving an
  inaccessible card from within a stack; an implementation shortcut that only
  compresses several otherwise legal single-card transfers.
- Parameters: source and destination zone classes, access position and
  destination acceptance rule.
- Evidence: [FreeCell decomposition](../games/a-f/freecell.md).
- Novelty: not assessed.

## ACT-011 — Swap orthogonally adjacent board elements

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player directly exchanges the positions of two selected
  elements occupying orthogonally adjacent addressed cells.
- Includes: swapping two neighbouring colour items to form a match in Royal
  Match.
- Excludes: moving one element into an empty cell; swapping non-adjacent
  elements; automatic falling or board shuffling.
- Parameters: adjacency topology, swappable element classes and invalid-swap
  handling.
- Evidence: [Royal Match decomposition](../games/m-r/royal-match.md).
- Novelty: not assessed.

## ACT-012 — Activate or combine board power-up

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player directly triggers one persistent special board
  element, or swaps two compatible special elements to trigger a combined
  effect.
- Includes: tapping or swapping a Royal Match Rocket, TNT, Propeller or Light
  Ball and swapping two power-ups together.
- Excludes: automatic creation of a power-up from a match; pre-level booster
  selection; the system-resolved clearing footprint after activation.
- Parameters: activation gesture, combinable classes and whether activation
  consumes a move.
- Evidence: [Royal Match decomposition](../games/m-r/royal-match.md).
- Novelty: not assessed.

## ACT-013 — Select source and destination containers

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player directly selects one non-empty source container and a
  distinct destination container, commanding the system to attempt one
  transfer between them.
- Includes: selecting two Water Sort tubes to attempt a pour from the first
  into the second.
- Excludes: choosing the transferred quantity; moving one independently
  selected internal layer; automatic transfer without a destination command.
- Parameters: selection order, input medium and cancellation behaviour.
- Evidence: [Water Sort decomposition](../games/s-z/water-sort.md).
- Novelty: not assessed.

## ACT-014 — Relocate selected controlled board piece

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player selects one board piece they currently control and a
  destination allowed by that piece's movement rules, directly changing its
  position and completing any capture specified by the destination.
- Includes: ordinary chess moves and captures; castling as a declared compound
  exception initiated by moving the king; relocating one available mech in an
  Into the Breach player phase; selecting a Peg Solitaire peg and the empty
  hole two orthogonal positions away for one jump; relocating one commander-led
  squad to a legal island destination in Bad North; sliding one selected Rush
  Hour car or truck to a reachable position on its fixed axis.
- Excludes: moving an opponent-controlled piece; automatic opponent response;
  choosing the replacement type for a promoting pawn; adjacency-only
  directional navigation of one permanently controlled agent (`ACT-008`).
- Parameters: piece classes, destination geometry, capture convention and
  compound-move exceptions.
- Evidence: [Chess decomposition](../games/a-f/chess.md),
  [Into the Breach decomposition](../games/g-l/into-the-breach.md), and
  [Peg Solitaire decomposition](../games/m-r/peg-solitaire.md), and
  [Bad North decomposition](../games/a-f/bad-north.md), and
  [Tactical Breach Wizards decomposition](../games/s-z/tactical-breach-wizards.md), and
  [Rush Hour decomposition](../games/m-r/rush-hour.md).
- Novelty: not assessed.

## ACT-015 — Choose promotion replacement type

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: when an eligible unit reaches its terminal region, the player
  directly chooses one type from a declared set to replace that unit as part
  of the same move.
- Includes: choosing a queen, rook, bishop or knight for a chess pawn reaching
  its furthest rank.
- Excludes: a system-selected upgrade; a replacement restricted to previously
  removed pieces; movement to the terminal region itself.
- Parameters: eligible unit, terminal region, replacement set and effect
  timing.
- Evidence: [Chess decomposition](../games/a-f/chess.md).
- Novelty: not assessed.

## ACT-016 — Trace path from fixed endpoint

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player starts at one fixed endpoint and directly traces a
  variable-length ordered route through successively adjacent board positions
  toward its declared terminal endpoint as one compound gesture.
- Includes: dragging a Flow Free pipe from either coloured dot through grid
  squares to the matching dot; drawing one Cosmic Express track from a fixed
  entrance stub to the selected exit; tracing a The Witness panel line from a
  start circle to its end cap; drawing one LYNE route from a hollow endpoint
  through same-family markers to the other hollow endpoint.
- Excludes: assigning unrelated cells independently; selecting only two
  endpoints while the system finds a route; rotating pre-existing pipe tiles.
- Parameters: adjacency topology, terminal identity, gesture sampling,
  permitted diagonal steps, backtracking and whether a trace may be resumed.
- Evidence: [Flow Free decomposition](../games/a-f/flow-free.md) and
  [Cosmic Express decomposition](../games/a-f/cosmic-express.md), and
  [The Witness decomposition](../games/s-z/the-witness.md), and
  [LYNE decomposition](../games/g-l/lyne.md).
- Novelty: not assessed.

## ACT-017 — Directionally step all rule-controlled objects

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: one directional input commands every object currently selected
  by an active control rule to attempt the same one-position orthogonal step.
- Includes: moving all objects whose noun currently has the `YOU` property in
  Baba Is You.
- Excludes: moving one permanently designated agent; a global maximal slide;
  movement produced automatically without player input.
- Parameters: direction set, controlled object count, simultaneous-resolution
  rule and blocked-object handling.
- Evidence: [Baba Is You decomposition](../games/a-f/baba-is-you.md).
- Novelty: not assessed.

## ACT-018 — Push contiguous movable chain

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: by commanding a controlled object toward an adjacent sequence of
  pushable objects, the player attempts to shift the entire contiguous chain
  one logical position in that direction under the destination topology.
- Includes: pushing a row of text or `PUSH`-assigned objects in Baba Is You;
  pushing an aligned row of boxes in Patrick's Parabox, including when the
  distal member crosses an eligible container boundary.
- Excludes: the single-object-only push boundary of `ACT-009`; pulling a chain;
  selecting remote objects directly; automatic conveyor movement.
- Parameters: chain length, adjacency and destination topology, participating
  object classes and simultaneous controlled movers.
- Evidence: [Baba Is You decomposition](../games/a-f/baba-is-you.md) and
  [Patrick's Parabox decomposition](../games/m-r/patricks-parabox.md).
- Novelty: not assessed.

## ACT-019 — Select unit ability and target

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one currently available controlled unit,
  chooses one of its declared abilities and specifies the target position or
  area on which that ability will resolve.
- Includes: firing a mech weapon or selecting that mech's repair action in
  Into the Breach; targeting an available squad class ability in Bad North.
- Excludes: relocating the acting unit; an enemy executing an already committed
  attack; the automatic damage, push or collision produced by the ability.
- Parameters: unit and ability classes, target geometry, range, damage and
  secondary effects.
- Evidence: [Into the Breach decomposition](../games/g-l/into-the-breach.md)
  and [Bad North decomposition](../games/a-f/bad-north.md), and
  [Tactical Breach Wizards decomposition](../games/s-z/tactical-breach-wizards.md).
- Novelty: not assessed.

## ACT-020 — Place queue-head tile at selected board position

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player selects one eligible board position and places the
  currently mandatory first element of a visible queue there in its supplied
  orientation, optionally replacing a declared replaceable occupant.
- Includes: placing the bottom Pipe Dream dispenser piece on an empty cell or
  blasting an unfilled ordinary pipe by placing that same queue-head piece over
  it.
- Excludes: choosing a different queued element; rotating the element; tracing
  a path; assigning an arbitrary symbol from a domain.
- Parameters: eligible positions, replacement rule, placement delay and input
  method.
- Evidence: [Pipe Mania decomposition](../games/m-r/pipe-mania.md).
- Novelty: not assessed.

## ACT-021 — Commit selected visible-card subset

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects a bounded non-empty subset of cards from one
  currently visible card zone and commits that subset for rule evaluation or
  discard-and-replacement.
- Includes: playing one to five Balatro cards for scoring or discarding up to
  five selected cards to draw replacements; selecting exactly three face-up
  SET cards for relational evaluation.
- Excludes: selecting a card outside the eligible visible zone; choosing the
  identities of replacement draws; moving one exposed card between tableau
  zones; assigning a value to a blank position.
- Parameters: card zone, subset-size limit, commit modes and whether unscored
  extra cards may accompany a qualifying pattern.
- Evidence: [Balatro decomposition](../games/a-f/balatro.md) and
  [SET decomposition](../games/s-z/set.md).
- Novelty: not assessed.

## ACT-022 — Reorder persistent effect sequence

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player rearranges persistent effect-bearing elements within
  an ordered zone so their effects resolve in the new sequence during a later
  automatic evaluation.
- Includes: moving Balatro Jokers so additive Mult resolves before a later
  multiplicative XMult effect.
- Excludes: buying or selling an effect; reordering elements when order has no
  mechanical consequence; choosing cards for the one scoring hand.
- Parameters: reorderable zones, effect classes and latest legal reorder time.
- Evidence: [Balatro decomposition](../games/a-f/balatro.md).
- Novelty: not assessed.

## ACT-023 — Edit ordered transit line

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player creates, extends, shortens, reroutes or removes a
  persistent named route by editing its ordered sequence of service nodes.
- Includes: drawing a Mini Metro line through stations, dragging an endpoint
  to a new station, changing an intermediate connection and reclaiming a
  removed line for reuse.
- Excludes: tracing a one-use path from a fixed endpoint; placing immutable
  queue-head tiles; commanding a vehicle's next stop directly.
- Parameters: allowed edit gestures, loop permission, node-revisit rule and
  whether edits may occur while simulation time is paused.
- Evidence: [Mini Metro decomposition](../games/m-r/mini-metro.md).
- Novelty: not assessed.

## ACT-024 — Reassign transport capacity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player assigns or relocates a reusable vehicle or capacity
  attachment among eligible persistent service routes.
- Includes: placing a Mini Metro locomotive on a line, moving it to another
  line and attaching or reassigning a carriage.
- Excludes: steering the vehicle along the route; creating new inventory;
  editing the ordered station sequence itself.
- Parameters: asset classes, attachment compatibility, transition delay and
  maximum vehicles per route.
- Evidence: [Mini Metro decomposition](../games/m-r/mini-metro.md).
- Novelty: not assessed.

## ACT-025 — Choose periodic network upgrade

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: at a scheduled progression boundary, the player selects one of
  the offered infrastructure or capacity rewards to add to finite inventory.
- Includes: choosing between a new Mini Metro line, carriage, tunnel or other
  map-eligible weekly upgrade alongside the automatically awarded locomotive;
  choosing one of the weekly road-network upgrades offered in Mini Motorways.
- Excludes: purchasing arbitrary items at any time; assigning the chosen asset
  to a route; generating the offered options.
- Parameters: offer size, reward families, cadence and map-specific options.
- Evidence: [Mini Metro decomposition](../games/m-r/mini-metro.md) and
  [Mini Motorways decomposition](../games/m-r/mini-motorways.md).
- Novelty: not assessed.

## ACT-026 — Orient and place mandatory supply-head tile

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player chooses an eligible empty position and a permitted
  orientation, then commits the currently mandatory first tile from a supplied
  sequence to that position.
- Includes: rotating the current Dorfromantik hex tile and placing it beside
  the existing landscape.
- Excludes: selecting a later supplied tile; placing a fixed-orientation queue
  head (`ACT-020`); tracing a route; rotating a persistent coupled layer.
- Parameters: orientation count, eligible-position topology, preview depth and
  input method.
- Evidence: [Dorfromantik decomposition](../games/a-f/dorfromantik.md).
- Novelty: not assessed.

## ACT-027 — Swipe-sever selected support link

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player traces a short gesture across one or more currently
  cuttable links and commands every intersected link to be severed at that
  moment.
- Includes: swiping across one or several ropes supporting the candy in Cut
  the Rope.
- Excludes: dragging the supported body; choosing its post-release trajectory;
  automatically breaking a link under load; tracing a persistent route.
- Parameters: gesture sampling, simultaneously intersected link count, link
  eligibility and input device.
- Evidence: [Cut the Rope decomposition](../games/a-f/cut-the-rope.md).
- Novelty: not assessed.

## ACT-028 — Configure spatial machine layout

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during an editable design phase, the player places, removes and
  orients persistent machine components whose relative geometry determines
  what a later execution can reach, route or transform.
- Includes: arranging Opus Magnum arms, tracks, glyphs and movable reagent or
  product ports on the transmutation-engine workspace; placing and orienting
  Infinifactory conveyor / support voxels for a later factory run; placing and
  orienting finite rail pieces and junctions before a Railbound carriage run.
- Excludes: placing a consumable gameplay tile; moving material while the
  machine runs; editing the commands that control a placed mechanism.
- Parameters: component catalogue, placement topology, orientation set,
  movable fixed ports and deletion policy.
- Evidence: [Opus Magnum decomposition](../games/m-r/opus-magnum.md),
  [Infinifactory decomposition](../games/g-l/infinifactory.md), and
  [Railbound decomposition](../games/m-r/railbound.md).
- Novelty: not assessed.

## ACT-029 — Edit per-mechanism symbolic instruction tape

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player assigns, removes or repositions command symbols at
  addressed cycle positions on one persistent mechanism's execution row.
- Includes: programming each Opus Magnum arm with grab, drop, rotate, pivot,
  extend, retract, track-move, repeat, reset or wait positions.
- Excludes: issuing one command directly to a currently moving piece; changing
  component geometry; reordering passive effects that resolve after a later
  hand evaluation.
- Parameters: command vocabulary, tape length, blank semantics, macros and
  whether several rows may be edited independently.
- Evidence: [Opus Magnum decomposition](../games/m-r/opus-magnum.md).
- Novelty: not assessed.

## ACT-030 — Navigate and focus within static evidence scene

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player directs an observation viewpoint or pointer focus
  through a bounded, immutable scene and selects people or details for closer
  inspection without changing the represented event.
- Includes: walking around and zooming within a frozen Return of the Obra Dinn
  death memory to inspect faces, objects, poses and sight lines; selecting
  people, possessions, documents or map details in a fixed The Case of the
  Golden Idol scene to open evidence overlays.
- Excludes: navigating a controllable gameplay agent whose position changes
  puzzle state; manipulating evidence objects; selecting a scene to enter.
- Parameters: viewpoint freedom, pointer versus camera access, focus range,
  scene boundary, overlays, bookmarks and permitted camera clipping.
- Evidence: [Return of the Obra Dinn decomposition](../games/m-r/return-of-the-obra-dinn.md)
  and [The Case of the Golden Idol decomposition](../games/s-z/the-case-of-the-golden-idol.md).
- Novelty: not assessed.

## ACT-031 — Activate corpse-linked evidence memory

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects an eligible discovered corpse or indexed
  death record and commands entry into its fixed evidence reconstruction.
- Includes: using Memento Mortem beside a corpse in Return of the Obra Dinn and
  revisiting an already indexed death memory.
- Excludes: revealing an unknown random outcome; directly assigning the
  deceased person's identity; navigating inside the resulting scene.
- Parameters: eligibility, physical-corpse requirement, nested-memory access,
  revisit interface and exit rule.
- Evidence: [Return of the Obra Dinn decomposition](../games/m-r/return-of-the-obra-dinn.md).
- Novelty: not assessed.

## ACT-032 — Assign structured identity-fate hypothesis

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player edits a subject's provisional dossier by selecting a
  candidate identity and a structured fate expression, including a responsible
  party or location when the chosen fate requires one.
- Includes: filling an Obra Dinn book sentence with one manifest identity,
  cause of death and killer, creature or escape destination.
- Excludes: recording free-form notes; exposing a pre-existing hidden value;
  receiving confirmation that the hypothesis is correct.
- Parameters: field vocabulary, partial-entry policy, accepted synonyms,
  revision availability and compound-field dependencies.
- Evidence: [Return of the Obra Dinn decomposition](../games/m-r/return-of-the-obra-dinn.md).
- Novelty: not assessed.

## ACT-033 — Rearrange intact panel among fixed slots

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player drags one intact framed scene from its current
  top-level slot to another eligible slot without changing that panel's current
  internal viewpoint.
- Includes: moving a Gorogoa illustration panel among the four positions of its
  two-by-two playfield to place it beside or over another scene.
- Excludes: zooming within the panel; detaching its foreground layer; placing a
  supplied consumable tile.
- Parameters: slot topology, swap or displacement behaviour, empty-slot rule
  and whether stacking is allowed at the destination.
- Evidence: [Gorogoa decomposition](../games/g-l/gorogoa.md).
- Novelty: not assessed.

## ACT-034 — Traverse illustrated panel viewpoint

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects a visible focus, back control or directional
  affordance to zoom or pan one panel to a linked illustrated viewpoint while
  leaving its top-level slot unchanged.
- Includes: zooming into a Gorogoa picture, zooming back out or panning to an
  adjacent room or scene within the same panel.
- Excludes: moving the whole panel between slots; directly manipulating an
  object depicted in the scene; moving a camera through one immutable 3D
  evidence tableau.
- Parameters: scene graph, focus hotspots, pan directions, backtracking and
  transition animation.
- Evidence: [Gorogoa decomposition](../games/g-l/gorogoa.md).
- Novelty: not assessed.

## ACT-035 — Detach and relocate illustrated panel layer

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: when a panel exposes a separable framed layer, the player lifts
  that layer away from its underlay and moves it to another slot or onto
  another panel while both illustrated layers persist.
- Includes: removing a Gorogoa window, doorway, frame or foreground overlay to
  reveal the scene beneath and superimposing the detached layer elsewhere.
- Excludes: moving an indivisible intact panel; erasing a layer; selecting a
  nested viewpoint without changing layer ownership.
- Parameters: detachable regions, retained underlay, destination eligibility,
  stack order and recombination policy.
- Evidence: [Gorogoa decomposition](../games/g-l/gorogoa.md).
- Novelty: not assessed.

## ACT-036 — Assign selected role to autonomous agent

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player selects one available behavioural role and commits it
  to one currently present autonomous agent without directly specifying the
  agent's subsequent path or continuously steering its execution.
- Includes: assigning one of the eight classic Lemmings skills to a selected
  lemming.
- Excludes: selecting an ability owned by a directly controlled tactical unit
  and targeting a separate board area; navigating an agent step by step; an
  automatic state change that requires no player assignment.
- Parameters: role set, recipient eligibility, selection priority and whether
  the assignment is immediate, delayed or persistent.
- Evidence: [Lemmings decomposition](../games/g-l/lemmings.md).
- Novelty: not assessed.

## ACT-037 — Adjust automatic population-release rate

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during an attempt, the player persistently raises or lowers the
  cadence at which a finite waiting population automatically enters the active
  playfield, without changing the speed of agents already active.
- Includes: using the minus and plus controls to change the Lemmings trapdoor
  release rate.
- Excludes: temporarily accelerating the entire running simulation; manually
  spawning one chosen unit; changing a difficulty setting outside play.
- Parameters: minimum and maximum rate, step size, initial rate and whether a
  later decrease is permitted.
- Evidence: [Lemmings decomposition](../games/g-l/lemmings.md).
- Novelty: not assessed.

## ACT-038 — Attach selected live node to force-bearing structure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while a force-resolved construction remains live, the player
  selects one loose or currently detachable material agent, drags it to a
  continuous-space position near eligible structural nodes and releases it to
  request attachment.
- Includes: grabbing a loose or reusable Goo Ball and placing it against a
  World of Goo structure.
- Excludes: configuring static machine footprints before a separate run;
  assigning a behavioural role to an autonomous agent; placing a discrete tile
  from a mandatory queue.
- Parameters: selectable types, detachable state, pointer sampling, release
  position and cancellation rule.
- Evidence: [World of Goo decomposition](../games/s-z/world-of-goo.md).
- Novelty: not assessed.

## ACT-039 — Place selected held world card

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player selects one currently held world card and commits it
  to one map position allowed by that card's spatial category, creating or
  replacing a persistent world tile that affects later simulation states.
- Includes: placing a Loop Hero road, roadside or landscape card to modify the
  current expedition map.
- Excludes: committing a mandatory queue head; playing a card only for immediate
  score resolution; configuring a whole world before a separate run.
- Parameters: card category, target position, replacement rule, adjacency
  requirements and immediate placement effects.
- Evidence: [Loop Hero decomposition](../games/g-l/loop-hero.md).
- Novelty: not assessed.

## ACT-040 — Replace equipped item from current loot

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player selects one acquired inventory item and assigns it to
  its compatible equipment slot, replacing the currently equipped item and
  updating the autonomous agent's combat statistics.
- Includes: equipping a newly dropped Loop Hero weapon or armour piece during
  the expedition.
- Excludes: choosing a pre-run character class; automatically accepting a stat
  increase; moving a generic card between tableau zones.
- Parameters: equipment slots, compatibility, replaced-item disposition,
  stat update timing and combat-lock restrictions.
- Evidence: [Loop Hero decomposition](../games/g-l/loop-hero.md).
- Novelty: not assessed.

## ACT-041 — Commit voluntary expedition retreat

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player deliberately terminates an active expedition and
  transfers the currently permitted share of its accumulated resources into
  persistent storage.
- Includes: leaving a Loop Hero expedition at campfire passage or accepting the
  lower retained share of a mid-loop retreat.
- Excludes: involuntary defeat; pausing without ending the attempt; moving a
  squad to an escape carrier while the battle continues.
- Parameters: eligible states, retained share, confirmation, combat restriction
  and destination storage.
- Evidence: [Loop Hero decomposition](../games/g-l/loop-hero.md).
- Novelty: not assessed.

## ACT-042 — Place persistent traversal command

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player writes an oriented behavioural instruction into an
  eligible world position so that it remains there and affects autonomous
  agents that later enter that position, until edited, moved with its support
  or cleared.
- Includes: placing HUMANITY Turn or Jump commands on the stage grid.
- Excludes: assigning a role directly to one selected agent; placing a card
  whose tile later generates encounters; drawing a route segment.
- Parameters: command vocabulary, orientation, eligible support, edit / removal
  rule, persistence across retry and attachment to movable support.
- Evidence: [HUMANITY decomposition](../games/g-l/humanity.md).
- Novelty: not assessed.

## ACT-043 — Reposition and orient live routing device

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during an active simulation, the player selects one reusable
  physical routing object, moves it to a valid support position and chooses its
  orientation so later autonomous agents physically contact it.
- Includes: moving and rotating a Tin Hearts prism block or aiming a trampoline
  drum within the current level.
- Excludes: placing a symbolic instruction marker; attaching a live node to a
  force-bearing structure; configuring a machine only before a separate run.
- Parameters: device class, support validity, position, orientation, paused /
  live placement and whether agents may occupy the object during movement.
- Evidence: [Tin Hearts decomposition](../games/s-z/tin-hearts.md).
- Novelty: not assessed.

## ACT-044 — Rewind recent simulation history

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player continuously or incrementally restores retained prior
  states of an active simulation, then may stop at an earlier moment and resume
  after making a different intervention.
- Includes: rewinding Tin Hearts soldiers and routing objects to before a fatal
  fall, repositioning a device and resuming a safer outcome; scrubbing Timelie
  to before capture, revising a character command and seeking a new future;
  rewinding Tim and ordinary Braid entities before resuming different local
  movement; selecting an earlier Pikmin 4 automatic checkpoint and replaying a
  replacement command sequence; scrubbing Viewfinder to before a fall or image
  placement and committing a different spatial continuation.
- Excludes: restarting the entire attempt from initial state; undoing only the
  most recent discrete edit; reversing cosmetic animation without game state.
- Parameters: history horizon, scrub speed, restored entity classes, resource
  cost, continuous versus checkpoint restoration granularity, stop precision
  and branch replacement policy.
- Evidence: [Tin Hearts decomposition](../games/s-z/tin-hearts.md) and
  [Timelie decomposition](../games/s-z/timelie.md), and
  [Braid decomposition](../games/a-f/braid.md),
  [Pikmin 4 decomposition](../games/m-r/pikmin-4.md), and
  [Viewfinder decomposition](../games/s-z/viewfinder.md).
- Novelty: not assessed.

## ACT-045 — Edit timestamped agent command

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: at a selected simulation time, the player assigns, replaces or
  clears a destination or contextual interaction for one persistent actor, and
  the command remains in the temporal plan until revised or resolved.
- Includes: selecting the Timelie girl or cat at the current cursor time and
  scheduling a destination, keypad, vent, meow or related interaction.
- Excludes: local step-by-step avatar movement; writing a reusable instruction
  into a world cell; editing cycle symbols on a machine mechanism.
- Parameters: actor count, cursor precision, command vocabulary, path choice,
  replacement semantics and whether future commands survive earlier revision.
- Evidence: [Timelie decomposition](../games/s-z/timelie.md).
- Novelty: not assessed.

## ACT-046 — Edit spatial controller route and instruction field

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: on a fixed machine grid, the player draws one controller's
  directed traversal route and assigns colour- or controller-specific command
  symbols to route cells, making spatial address determine execution order.
- Includes: authoring the red and blue SpaceChem waldo paths and placing their
  input, grab, rotate, bond, sync, drop and output instructions.
- Excludes: editing commands in separate addressed time columns; placing
  physical machine components; scheduling a situated actor command at an
  arbitrary simulation time.
- Parameters: controller count, grid topology, route branching, symbol
  vocabulary, colour ownership, crossing rules and loop closure.
- Evidence: [SpaceChem decomposition](../games/s-z/spacechem.md).
- Novelty: not assessed.

## ACT-047 — Place replaceable paired-portal endpoint

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player aims at an eligible world surface and creates one
  colour- or channel-specific endpoint of a persistent spatial portal pair,
  replacing the previous endpoint of that same channel.
- Includes: firing Portal's blue or orange portal onto a valid flat chamber
  surface after the fully powered handheld portal device is acquired.
- Excludes: tracing every intermediate position of a route; editing an ordered
  transit line; moving a solid routing device that agents later collide with.
- Parameters: channel count, aim model, placement range, replacement rule,
  projectile travel and whether firing through an existing portal is allowed.
- Evidence: [Portal decomposition](../games/m-r/portal.md).
- Novelty: not assessed.

## ACT-048 — Pick up and release portable rigid object

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player directly acquires one reachable free rigid object,
  keeps it at a controlled offset while navigating and releases, drops or
  throws it back into the active world state.
- Includes: lifting, carrying and dropping a Weighted Storage Cube in Portal;
  grabbing, carrying and releasing the belongings crate in Bonfire Peaks;
  taking, sightline-positioning and dropping an Induction chess piece in
  Superliminal; lifting, carrying and placing an eligible coloured cube in
  Manifold Garden; lifting, carrying and placing the currently manageable
  representation of Maquette's persistent golden key.
- Excludes: pushing an adjacent object one board position; relocating a board
  piece directly to a legal destination; attaching a node to a structure.
- Parameters: reach, held-object count, carry offset, collision handling,
  release impulse, discrete versus continuous motion and portal-traversal
  permission.
- Evidence: [Portal decomposition](../games/m-r/portal.md),
  [Bonfire Peaks decomposition](../games/a-f/bonfire-peaks.md), and
  [Superliminal decomposition](../games/s-z/superliminal.md), and
  [Manifold Garden decomposition](../games/m-r/manifold-garden.md), and
  [Maquette decomposition](../games/m-r/maquette.md).
- Novelty: not assessed.

## ACT-049 — Toggle reachable world switch

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player makes the locally navigated avatar activate a
  reachable persistent switch, changing the commanded state or travel direction
  of a linked world mechanism.
- Includes: operating a Braid lever to start or reverse its linked platform;
  pressing Manifold Garden's reachable blue switch after the periodic gap
  crossing to open its linked door; setting each reachable valve in Chants of
  Sennaar's first water instruction to its commanded open or closed state.
- Excludes: sustaining a pressure plate by occupancy; editing a remote
  timestamped interaction; placing a reusable instruction marker.
- Parameters: reach, activation gesture, binary or multi-state switch,
  retrigger delay, linked mechanism set and whether avatar motion pauses.
- Evidence: [Braid decomposition](../games/a-f/braid.md),
  [Manifold Garden decomposition](../games/m-r/manifold-garden.md), and
  [Chants of Sennaar decomposition](../games/a-f/chants-of-sennaar.md).
- Novelty: not assessed.

## ACT-050 — Commit selected follower to contextual target task

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player selects a follower type and dispatches one or more
  currently available followers onto a world target, causing the target class
  to determine the autonomous task they begin.
- Includes: throwing Pikmin at a treasure, castaway, enemy, obstacle or
  construction target in Pikmin 4.
- Excludes: selecting an abstract behavioural role before choosing its agent;
  directly relocating a squad to a destination; picking up and holding the
  target object beside the avatar.
- Parameters: dispatch gesture, follower type, per-input count, target lock,
  accepted target classes and automatic stop at sufficient assignment.
- Evidence: [Pikmin 4 decomposition](../games/m-r/pikmin-4.md).
- Novelty: not assessed.

## ACT-051 — Recall nearby followers from autonomous tasks

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player emits a spatially bounded recall command that cancels
  or interrupts eligible nearby followers' current idle or autonomous task
  state and makes them rejoin the active leader's squad.
- Includes: blowing the whistle to gather Pikmin back to the Rescue Officer or
  Oatchi in Pikmin 4.
- Excludes: globally selecting every unit regardless of distance; rewinding
  task history; changing a persistent world instruction.
- Parameters: radius, duration, task interruption threshold, affected follower
  classes, current leader and response delay.
- Evidence: [Pikmin 4 decomposition](../games/m-r/pikmin-4.md).
- Novelty: not assessed.

## ACT-052 — Transfer direct control among persistent bodies

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while multiple eligible persistent bodies remain active in the
  same world state, the player transfers the unique locus of direct navigation
  or command authority from its current body to another, leaving the former
  body present under its declared non-locus rules.
- Includes: switching from the Rescue Officer to Oatchi after separating their
  Pikmin groups in Pikmin 4; swapping consciousness from the current The
  Swapper body into a visible existing clone while the former body remains.
- Excludes: selecting an actor only to schedule a remote destination; creating
  a new body without transferring control; teleporting one unchanged body;
  alternating adversarial turns.
- Parameters: eligible body classes, target-selection method, separation
  requirement, retained follower groups, former-body behaviour, transfer delay,
  unavailable states and camera transfer.
- Evidence: [Pikmin 4 decomposition](../games/m-r/pikmin-4.md) and
  [The Swapper decomposition](../games/s-z/the-swapper.md).
- Novelty: not assessed.

## ACT-053 — Push contiguous movable-object chain

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: historical Patrick's Parabox-specific duplicate of the
  contiguous-chain command represented by `ACT-018`.
- Includes: historical references to Patrick pushing an aligned row of boxes.
- Excludes: new game signatures; use `ACT-018` for the command and the relevant
  System / Constraint genes for destination resolution.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Patrick's Parabox decomposition](../games/m-r/patricks-parabox.md).
- Merged into: `ACT-018` by
  [`TAXONOMY_CHANGE_003`](../../research/taxonomy-changes/TAXONOMY_CHANGE_003.md).
- Novelty: not assessed.

## ACT-054 — Instantiate body at aimed reachable position

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player aims at a currently eligible world position and
  commands a new controllable body to be instantiated there without moving an
  existing body along the intervening path.
- Includes: creating a The Swapper clone at an unobstructed valid point within
  the device's range.
- Excludes: summoning an autonomous unit from reserve; placing an inert object;
  teleporting the current body; generating a body automatically on a timer.
- Parameters: range, aim geometry, support requirement, creation delay,
  initial velocity, population cost and invalid-target feedback.
- Evidence: [The Swapper decomposition](../games/s-z/the-swapper.md).
- Novelty: not assessed.

## ACT-055 — Transfer direct-control locus to targeted body

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player targets one existing eligible body and transfers the
  unique direct-control locus to it while the former body persists in the
  world under the non-locus rules of the same body set.
- Includes: swapping consciousness from the current The Swapper body into a
  visible clone, leaving the former body as another synchronized clone.
- Excludes: switching between persistent leaders with different follower
  groups; teleporting one unchanged body; selecting an actor only to schedule
  a future action; alternating turns between opponents.
- Parameters: eligible body set, target acquisition, transfer delay, former-
  body state, camera transfer and failure conditions.
- Evidence: [The Swapper decomposition](../games/s-z/the-swapper.md).
- Replaced by: `ACT-052`.
- Novelty: not assessed.

## ACT-056 — Reposition and rotate persistent map fragment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: in a map-editing view, the player selects one already acquired
  persistent world fragment, translates it to a new map position and may rotate
  its orientation before committing the new adjacency arrangement.
- Includes: picking up, moving and quarter-turning a Carto square map piece,
  including the fragment currently containing the avatar.
- Excludes: consuming the mandatory head of a supplied tile queue; moving an
  intact illustration only among fixed display slots; rotating one coupled
  layer of a persistent mechanical object; drawing a route.
- Parameters: fragment shape, rotation set, position lattice, displacement /
  swap behaviour, occupied-fragment permission and commit gesture.
- Evidence: [Carto decomposition](../games/a-f/carto.md).
- Novelty: not assessed.

## ACT-057 — Position and commit held perspective image

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while holding one available two-dimensional source image, the
  player positions its plane in the current three-dimensional view, chooses its
  orientation and commits that projected pose as a world-edit request.
- Includes: picking up a supplied Viewfinder photograph, holding it against the
  scene, translating or rotating it in perspective and stamping it into place.
- Excludes: capturing the source image; rearranging a persistent map fragment;
  moving an intact panel among fixed interface slots; placing one endpoint of a
  linked aperture pair; carrying and dropping a rigid world object.
- Parameters: source medium, plane translation, rotation set, perspective-
  determined scale, aim distance, preview opacity and commit gesture.
- Evidence: [Viewfinder decomposition](../games/s-z/viewfinder.md).
- Novelty: not assessed.

## ACT-058 — Rotate agent with body-attached tool sweep

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player commands a persistent agent to rotate in place while
  its body-attached tool sweeps from one adjacent orientation cell to another,
  potentially contacting an object along that sweep.
- Includes: quarter-turning the Stephen's Sausage Roll character so the fixed
  fork changes facing and can laterally displace a sausage.
- Excludes: rotating a remotely selected object; changing viewpoint; rotating
  an active falling piece; turning without a decision-relevant attached
  footprint.
- Parameters: angle set, pivot cell, tool length, swept cells, contact rule and
  turn-clearance geometry.
- Evidence: [Stephen's Sausage Roll decomposition](../games/s-z/stephens-sausage-roll.md).
- Novelty: not assessed.

## ACT-059 — Extract highlighted term from evidence detail

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one explicitly eligible word or phrase inside
  an opened evidence detail and copies that exact term into a persistent case-
  local hypothesis vocabulary.
- Includes: clicking highlighted names and place terms in The Case of the
  Golden Idol's prologue documents and map so they enter the word bank.
- Excludes: merely reading unhighlighted evidence; revealing a concealed truth
  value; assigning the extracted term to an answer field.
- Parameters: eligibility marking, phrase length, duplicate handling, source
  detail classes and extraction-completion indicator.
- Evidence: [The Case of the Golden Idol decomposition](../games/s-z/the-case-of-the-golden-idol.md).
- Novelty: not assessed.

## ACT-060 — Assign phrase token to structured answer slot

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one available phrase token and places it into
  a typed blank within a structured proposition, with later removal or
  replacement permitted before acceptance.
- Includes: dragging collected The Case of the Golden Idol terms into the
  prologue Thinking-screen identity, location and event Scroll blanks.
- Excludes: entering unrestricted prose; extracting the phrase from evidence;
  assigning a complete identity-and-fate dossier to one roster subject.
- Parameters: drag or selection input, slot type, token reuse, replacement,
  partial-entry policy and grammatical scaffold.
- Evidence: [The Case of the Golden Idol decomposition](../games/s-z/the-case-of-the-golden-idol.md).
- Novelty: not assessed.

## ACT-061 — Play held spatial action card

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one currently held action card and a legal
  spatial target parameter, consuming that card to apply its declared movement,
  attack, defence or repositioning transition.
- Includes: playing a Fights in Tight Spaces movement card on a legal cell or
  an attack / push card on a legal enemy or adjacent target; playing a Golf
  Peaks movement card with one cardinal direction as its spatial target.
- Excludes: selecting an ability from a persistent unit menu; committing a
  held subset for pattern evaluation; placing a card as a persistent world
  object; choosing a target for an enemy's already committed attack.
- Parameters: card type, entity / cell / direction target, target geometry,
  cost, compound effects, facing and target eligibility.
- Evidence: [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md)
  and [Golf Peaks decomposition](../games/g-l/golf-peaks.md).
- Novelty: not assessed.

## ACT-062 — Rewind uncommitted tactical draft

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before committing the current bounded tactical turn, the player
  restores any earlier discrete draft step and may replace the subsequent
  commands while completed earlier turns remain inaccessible.
- Includes: rewinding Tactical Breach Wizards movement, ability and resource
  choices after Foresee exposes an unwanted current-turn consequence.
- Excludes: continuous rewind of already lived simulation history; random-
  access editing of timestamped commands; ordinary one-step puzzle undo without
  an explicit tactical forecast / commit loop.
- Parameters: draft horizon, step granularity, resource restoration, selection
  interface, cost and whether partial rewinds are allowed.
- Evidence: [Tactical Breach Wizards decomposition](../games/s-z/tactical-breach-wizards.md).
- Novelty: not assessed.

## ACT-063 — Assert concealed binary cell class

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one unresolved position and asserts which of
  two fixed concealed classes it already belongs to.
- Includes: left-clicking an orange Hexcells Infinite cell to assert blue or
  right-clicking it to assert black.
- Excludes: commanding the system merely to reveal an unknown value; recording
  a tentative value that remains editable before validation; choosing a value
  that did not exist before the action.
- Parameters: class domain, input mapping, target topology, validation timing
  and whether a rejected assertion leaves the position unresolved.
- Evidence: [Hexcells Infinite decomposition](../games/g-l/hexcells-infinite.md).
- Novelty: not assessed.

## ACT-064 — Reverse controlled-agent facing

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player commands a persistent controlled agent to reverse its
  facing while remaining in the same addressed position.
- Includes: turning the Shogun Showdown Wanderer around as one turn-costing
  combat action.
- Excludes: rotating a body-attached tool with a decision-relevant swept
  footprint; changing camera viewpoint; moving into another position.
- Parameters: orientation set, turn cost, blocked-state rule and effects tied
  to facing.
- Evidence: [Shogun Showdown decomposition](../games/s-z/shogun-showdown.md).
- Novelty: not assessed.

## ACT-065 — Edit bounded attack-execution queue

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player inserts one currently ready attack tile into a bounded
  ordered queue or revises the membership / order of tiles already waiting
  there before activation.
- Includes: adding a Shogun Showdown tile to the three-slot attack queue and
  freely reordering or removing queued tiles before release.
- Excludes: immediately resolving the selected attack; selecting a mandatory
  queue head supplied by the system; editing timestamped future commands.
- Parameters: capacity, insertion position, reorder / removal controls, turn
  cost by edit operation and permitted tile classes.
- Evidence: [Shogun Showdown decomposition](../games/s-z/shogun-showdown.md).
- Novelty: not assessed.

## ACT-066 — Activate prepared attack queue

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player commits the currently prepared ordered attack queue
  for immediate automatic execution as one action.
- Includes: releasing one to three queued Shogun Showdown attack tiles.
- Excludes: inserting or reordering a queued tile; selecting a target separately
  for each attack; ending a planning phase whose hostile intents then execute.
- Parameters: minimum queue size, activation input, turn cost, interruptibility
  and empty-queue handling.
- Evidence: [Shogun Showdown decomposition](../games/s-z/shogun-showdown.md).
- Novelty: not assessed.

## ACT-067 — Swap controlled agent with faced adjacent unit

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: by commanding forward movement into an occupied adjacent
  position, the player exchanges the controlled agent's position with the
  faced unit instead of rejecting movement or pushing it.
- Includes: the Shogun Showdown Wanderer swapping with an enemy directly in
  front of her.
- Excludes: selecting any two board elements to swap; pushing the adjacent
  unit away; teleporting without exchanging positions.
- Parameters: faced-unit classes, cooldown, turn cost, orientation after swap
  and edge cases with immovable units.
- Evidence: [Shogun Showdown decomposition](../games/s-z/shogun-showdown.md).
- Novelty: not assessed.

## ACT-068 — Edit persistent branching road network

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player draws, extends, reroutes, undoes or marks for removal
  a persistent spatial road graph whose intersections may branch and whose
  connected segments are used automatically by multiple vehicles.
- Includes: drawing and redrawing ordinary roads in a Mini Motorways Classic
  city while traffic continues to use the connected network; freehand drawing
  and revising a Freeways interchange between traffic evaluations.
- Excludes: editing one named ordered service line; steering an individual
  vehicle; tracing one unbranched route whose geometry is consumed or becomes
  permanently locked after a run begins.
- Parameters: tile or continuous geometry, edge direction, intersection
  degree, undo / deletion policy, obstacle rules and when edits are permitted.
- Evidence: [Mini Motorways decomposition](../games/m-r/mini-motorways.md) and
  [Freeways decomposition](../games/a-f/freeways.md).
- Novelty: not assessed.

## ACT-069 — Adjust active road-stroke elevation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while authoring one road stroke, the player raises or lowers its
  active segment so a geometric crossing becomes a grade-separated overpass or
  underpass rather than a same-level junction.
- Includes: using the raise and lower controls while drawing a Freeways ramp so
  it crosses another road without connecting to it.
- Excludes: changing camera height; placing a fixed bridge token that merely
  consumes inventory; automatically selecting a crossing layer from geometry.
- Parameters: available elevation bands, slope limit, control granularity,
  crossing connection rule and scoring cost.
- Evidence: [Freeways decomposition](../games/a-f/freeways.md).
- Novelty: not assessed.

## ACT-070 — Select, orient and place finite footprint piece

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player selects any one remaining piece from a finite visible
  construction inventory, chooses one of its permitted rigid orientations and
  commits its complete typed footprint at an addressed offset in a fixed
  container.
- Includes: choosing, quarter-turning and placing one available multi-block
  food piece in a Chapter 1 inbento box; selecting, rotating and placing one
  collected tetromino in The Talos Principle's first A1 gate arranger.
- Excludes: placing the mandatory head of a supplied queue; editing a persistent
  machine component; assigning independent values to each covered cell;
  playing a card that commands another moving entity.
- Parameters: piece multiset, typed footprint, orientation set, anchor,
  placement lattice, selection method and consumption timing.
- Evidence: [inbento decomposition](../games/g-l/inbento.md) and
  [The Talos Principle decomposition](../games/s-z/the-talos-principle.md).
- Novelty: not assessed.

## ACT-071 — Select connected-region seed and replacement class

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player selects one replacement class and one addressed cell,
  thereby commanding a class change for the complete current connected
  component containing that seed.
- Includes: choosing a palette colour and tapping one differently coloured
  paper cell in KAMI.
- Excludes: assigning only the addressed cell; selecting a fixed geometric
  footprint; deleting a matching group; expanding from one permanently fixed
  origin.
- Parameters: class vocabulary, selection order, seed-cell topology, valid
  no-op policy and input method.
- Evidence: [KAMI decomposition](../games/g-l/kami.md).
- Novelty: not assessed.

## ACT-072 — Activate addressed mechanism trigger

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one visible trigger and commands every
  mechanism currently linked to that trigger to begin its declared automatic
  operation.
- Includes: pressing one circular HOOK trigger to retract its one or several
  attached line-and-hook mechanisms; pressing The Room's addressed fire symbol
  to open its linked key compartment.
- Excludes: navigating an avatar to a world switch; holding a pressure region;
  editing a connection graph; directly dragging the linked mechanisms.
- Parameters: input gesture, trigger identity, linked-mechanism multiplicity,
  activation availability and repeat policy.
- Evidence: [HOOK decomposition](../games/g-l/hook.md) and
  [The Room decomposition](../games/s-z/the-room.md).
- Novelty: not assessed.

## ACT-073 — Commit complete ordered-symbol hypothesis

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player fills every position of one fixed-length ordered
  proposal from a bounded symbol vocabulary and commits the complete sequence
  for comparison with one concealed target sequence.
- Includes: placing four colour pegs, with repeated colours permitted, and
  submitting the complete row as one Mastermind guess; entering and submitting
  one recognised five-letter Wordle guess.
- Excludes: editing an unsubmitted partial assignment; asserting one concealed
  cell independently; selecting an unordered subset; entering a free-form
  answer whose positions have no identity.
- Parameters: sequence length, symbol vocabulary, duplicate policy, partial-row
  edit controls, submission trigger and whether earlier proposals remain
  visible.
- Evidence: [Mastermind decomposition](../games/m-r/mastermind.md) and
  [Wordle decomposition](../games/s-z/wordle.md).
- Novelty: not assessed.

## ACT-074 — Fire probe from perimeter entry

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player selects one unused entry on the boundary of a
  concealed spatial field and commits one probe whose internal route and
  eventual categorical outcome are resolved by the system.
- Includes: firing one Black Box laser from an unfired edge position to obtain
  a hit, reflection or paired exit observation.
- Excludes: revealing the addressed boundary cell; drawing a route through the
  field; submitting a complete hidden-layout hypothesis; repeating an already
  resolved entry as a new observation.
- Parameters: boundary topology, entry count, reuse policy, input gesture and
  whether opposite-side exits become independently unavailable.
- Evidence: [Black Box decomposition](../games/a-f/black-box.md).
- Novelty: not assessed.

## ACT-075 — Submit fixed-cardinality spatial hypothesis

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after marking a declared exact number of positions in a bounded
  field, the player commits that complete occupancy proposal for global
  comparison with a concealed spatial system.
- Includes: pressing Check in default Black Box after marking exactly five
  cells as balls.
- Excludes: committing an ordered symbol sequence; asserting one cell without
  global evaluation; revealing a marked position; selecting an unordered
  subset from already visible objects.
- Parameters: required mark count, position topology, submission control,
  incomplete-submission policy and whether an accepted equivalent layout may
  differ from the generated truth.
- Evidence: [Black Box decomposition](../games/a-f/black-box.md).
- Novelty: not assessed.

## ACT-076 — Reproduce presented ordered cue sequence

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during a response phase, the player presses one member of a
  bounded control set for each ordinal position of a sequence that the system
  has just presented, preserving both cue identity and order.
- Includes: pressing Simon's four coloured pads to echo the complete current
  light sequence from its first cue to its last.
- Excludes: committing a fully editable proposal as one query; selecting an
  unordered subset; reacting only to the most recent cue; entering inputs while
  the system is still presenting the target.
- Parameters: control vocabulary, target length, repeated-cue policy, response
  editability, per-symbol feedback and input modality.
- Evidence: [Simon decomposition](../games/s-z/simon.md).
- Novelty: not assessed.

## ACT-077 — Press addressed binary-state cell

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player selects one individually addressed cell in a fixed
  field and commits one press whose declared effect is resolved from that
  position, regardless of the cell's current one-of-two state.
- Includes: pressing any lit or unlit button of the original `5 × 5` Lights
  Out field.
- Excludes: assigning a proposed value to the selected cell; revealing a
  concealed value; selecting a remote mechanism trigger; choosing a global
  direction rather than a position.
- Parameters: field topology, address scheme, binary state labels, input
  gesture, repeat policy and whether current state affects press legality.
- Evidence: [Lights Out decomposition](../games/g-l/lights-out.md).
- Novelty: not assessed.

## ACT-078 — Launch designated slider in chosen direction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while one designated body is stationary, the player chooses one
  permitted direction and commits the body to automatic straight-line travel
  without choosing an intermediate or final cell.
- Includes: sending Inertia's green ball horizontally, vertically or diagonally
  from its current stopping position.
- Excludes: moving every board element with one global direction; directly
  choosing a destination; steering or changing direction during unresolved
  travel; entering one adjacent grid step that remains under player control.
- Parameters: direction vocabulary, stationary-input requirement, blocked-input
  policy, controlled-body count and input modality.
- Evidence: [Inertia decomposition](../games/g-l/inertia.md).
- Novelty: not assessed.

## ACT-079 — Toggle orthogonal adjacent-cell pairing

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player selects the shared boundary of two orthogonally
  adjacent fixed cells to place or remove one proposed 1 × 2 pairing relation.
- Includes: joining two neighbouring numbered cells as one domino in Dominosa.
- Excludes: moving a physical domino from an inventory; assigning independent
  symbols to two cells; drawing an arbitrary-length path; pairing diagonal or
  non-spatial identities.
- Parameters: cell topology, allowed adjacency, place / remove gesture,
  overlap-editing policy and optional forbidden-boundary notation.
- Evidence: [Dominosa decomposition](../games/a-f/dominosa.md).
- Novelty: not assessed.

## ACT-080 — Cycle bounded nearest-vertex linkage multiplicity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player chooses one direction from a fixed vertex, targets the
  nearest visible vertex on that ray and cycles the multiplicity of their
  linkage through a finite ordered domain.
- Includes: dragging from one Bridges island toward its nearest orthogonal
  neighbour to cycle zero, one and two bridges.
- Excludes: choosing an arbitrary non-nearest endpoint; freehand path drawing;
  moving a physical bridge piece; toggling one independent binary edge.
- Parameters: direction vocabulary, visibility rule, multiplicity domain,
  wraparound policy and input gesture.
- Evidence: [Bridges decomposition](../games/a-f/bridges.md).
- Novelty: not assessed.

## ACT-081 — Toggle independently addressed binary edge

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player selects one fixed permitted edge and independently
  changes whether that edge belongs to the proposed solution subgraph.
- Includes: left-clicking one yellow Loopy grid segment to mark it as part of
  the loop, then clicking again to return it to unknown; drawing or clearing
  one fixed internal cell boundary in Galaxies; selecting or clearing one
  permitted orthogonal link between adjacent Pearl cell centres.
- Excludes: tracing a continuous route in one gesture; choosing an endpoint
  pair and a multiplicity; assigning a symbol to a face; automatically
  propagating the same state to neighbouring edges.
- Parameters: edge topology, binary selected state, optional unknown and
  explicit-excluded notation, input gesture and independent-editing policy.
- Evidence: [Loopy decomposition](../games/g-l/loopy.md),
  [Galaxies decomposition](../games/g-l/galaxies.md) and
  [Pearl decomposition](../games/m-r/pearl.md).
- Novelty: not assessed.

## ACT-082 — Link directed-ray successor

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player selects one addressed source and one eligible target
  at any positive distance on the source's fixed directed ray, declaring the
  target to be the source's immediate successor in an ordered chain.
- Includes: dragging from one Signpost cell to any still-eligible cell lying
  along its displayed orthogonal or diagonal arrow direction.
- Excludes: linking only the nearest visible target; tracing every intervening
  position; moving an actor along the ray; choosing a direction when the source
  already fixes it; linking two arbitrary cells without an ordered relation.
- Parameters: direction vocabulary, ray geometry, maximum distance, target
  eligibility, forward or reciprocal gesture and link-replacement policy.
- Evidence: [Signpost decomposition](../games/s-z/signpost.md).
- Novelty: not assessed.

## ACT-083 — Rotate addressed tile in place

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player selects one persistent addressed tile and changes
  only its rigid orientation within that same position, preserving its shape,
  ports and identity.
- Includes: rotating one Net endpoint, straight, corner or T-junction tile
  clockwise, anticlockwise or by 180 degrees without moving it to another cell.
- Excludes: rotating a moving active element before it locks; rotating a whole
  coupled layer; repositioning and then rotating a map fragment; selecting an
  orientation while placing a new piece; changing the tile's port degree.
- Parameters: orientation cycle, available turn increments, tile topology,
  lock state and whether invalid intermediate orientations are permitted.
- Evidence: [Net decomposition](../games/m-r/net.md).
- Novelty: not assessed.

## ACT-084 — Cyclically shift addressed line

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player selects one eligible addressed row or column and
  translates every persistent element in that line by the same fixed number of
  positions, cyclically returning the displaced end element at the opposite
  end while preserving every element's orientation.
- Includes: shifting one non-central Netslide row left or right, or one
  non-central column up or down, by one tile.
- Excludes: applying one direction to every movable element across the whole
  board; shifting a line into an empty buffer; rotating a rigid layer; moving
  only one selected element; automatically compressing or merging a line.
- Parameters: line family, eligible indices, shift distance, direction,
  wraparound rule and whether element orientation is preserved.
- Evidence: [Netslide decomposition](../games/m-r/netslide.md).
- Novelty: not assessed.

## ACT-085 — Manipulate constrained diegetic component

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player directly drags or turns one persistent visible
  mechanism component through only its authored local path or orientation
  range, committing the component's resulting physical state.
- Includes: sliding The Room's keyhole covers, turning an inserted key or
  wrench, rotating one front ring and pulling the unlatched safe door; removing
  Machinarium's covering tub, dropping the exposed torso and bending the fixed
  scrapyard pole into its usable state; turning Monument Valley's marked
  central bridge through its authored local arc until it settles at a route-
  bearing orientation.
- Excludes: rotating an addressed grid tile by an abstract step; changing only
  camera viewpoint; moving a free rigid body through world space; pressing a
  trigger whose linked mechanism moves automatically.
- Parameters: component identity, motion path, orientation range, continuous
  gesture sampling, snap states, prerequisite state and completion effect.
- Evidence: [The Room decomposition](../games/s-z/the-room.md),
  [Machinarium decomposition](../games/m-r/machinarium.md), and
  [Monument Valley decomposition](../games/m-r/monument-valley.md).
- Novelty: not assessed.

## ACT-086 — Reconfigure articulated held item

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while inspecting one acquired inventory object, the player
  rotates or folds its articulated parts to commit one of several persistent
  functional configurations without consuming or placing the object.
- Includes: changing The Room's peculiar key between its spiral and crown
  shapes before using it on different locks.
- Excludes: rotating a board tile; choosing a fixed orientation while placing a
  new piece; merely viewing a held object from another angle; swapping one
  equipped item for another.
- Parameters: articulated parts, configuration domain, intermediate states,
  inspection controls, persistence after closing inventory and reset rule.
- Evidence: [The Room decomposition](../games/s-z/the-room.md).
- Novelty: not assessed.

## ACT-087 — Apply held item to compatible fixture

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one acquired inventory object and commits it
  to a persistent addressed fixture whose current type and state permit that
  object's declared mechanical use.
- Includes: inserting The Room's configured key into a matching keyhole,
  placing the metal plate over its matching screw and fitting the recovered
  lens into the eyepiece assembly; applying Machinarium's combined
  magnet-and-string rig to the prepared scrapyard pole; applying The Longest
  Journey's completed fishing instrument to the track-key hotspot.
- Excludes: equipping statistical loot; placing a construction piece on a
  board; collecting an item by contact; a carried key automatically opening a
  barrier when an avatar touches it.
- Parameters: item identity and state, fixture identity and state, consumption
  or retention, attachment persistence and follow-up manipulation.
- Evidence: [The Room decomposition](../games/s-z/the-room.md),
  [Machinarium decomposition](../games/m-r/machinarium.md), and
  [The Longest Journey decomposition](../games/s-z/the-longest-journey.md).
- Novelty: not assessed.

## ACT-088 — Reconfigure articulated avatar reach

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player directly commits one controlled articulated avatar
  between declared body configurations whose different geometry changes which
  current scene affordances the avatar can reach.
- Includes: extending Josef's telescoping torso in Machinarium to collect the
  high doll, then contracting it before ordinary walking and item exchange.
- Excludes: changing camera zoom; crouching with no rule-relevant reach change;
  moving an independent mechanism component; equipping an item that changes a
  numeric range statistic.
- Parameters: configuration domain, transition control, collision envelope,
  reachable affordance set, movement compatibility and persistence.
- Evidence: [Machinarium decomposition](../games/m-r/machinarium.md).
- Novelty: not assessed.

## ACT-089 — Collect addressed scene item into inventory

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one currently reachable addressed scene item,
  removing it from that scene position and adding its persistent identity to a
  discrete held inventory.
- Includes: collecting Machinarium's high doll, loose magnet and string spool
  after their respective reach and locomotion prerequisites are satisfied;
  taking Day of the Tentacle's completed super-battery from Red's shelf.
- Excludes: carrying a free rigid object continuously in world space; receiving
  an item automatically from a character; collecting a score token on contact;
  revealing an item without acquiring it.
- Parameters: item identity, reach predicate, scene removal, inventory capacity,
  duplicate policy, acquisition animation and reset boundary.
- Evidence: [Machinarium decomposition](../games/m-r/machinarium.md) and
  [Day of the Tentacle decomposition](../games/a-f/day-of-the-tentacle.md).
- Novelty: not assessed.

## ACT-090 — Combine two held inventory items

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player directly selects two compatible held item identities
  and commits their replacement by one persistent composite inventory item
  whose fixture use differs from either constituent alone.
- Includes: combining Machinarium's magnet and string into one fishing rig;
  The Longest Journey first combining clamp and clothesline, then combining
  that composite with the inflated ducky.
- Excludes: reshaping one articulated item without changing its identity;
  activating two adjacent board power-ups; crafting from an abstract resource
  count; applying an already complete item to a world fixture.
- Parameters: constituent identities, order sensitivity, compatibility table,
  consumption, composite identity, reversibility and inventory capacity.
- Evidence: [Machinarium decomposition](../games/m-r/machinarium.md) and
  [The Longest Journey decomposition](../games/s-z/the-longest-journey.md).
- Novelty: not assessed.

## ACT-091 — Give held item to addressed character

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one held inventory item and commits its
  transfer to one addressed non-player character whose current request accepts
  that item, removing it from the player's inventory.
- Includes: giving Machinarium's doll to the small scrapyard robot that showed
  the doll in its request bubble; giving Day of the Tentacle's patent and three
  requested battery ingredients to Red Edison.
- Excludes: applying a tool to an inanimate fixture; equipping an item;
  surrendering an abstract currency amount; an automatic collision pickup or
  exchange with no selected recipient.
- Parameters: item identity, recipient identity and state, request predicate,
  transfer persistence, rejection feedback and repeat policy.
- Evidence: [Machinarium decomposition](../games/m-r/machinarium.md) and
  [Day of the Tentacle decomposition](../games/a-f/day-of-the-tentacle.md).
- Novelty: not assessed.

## ACT-092 — Alter one held item's functional state

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player directly operates one acquired inventory object to
  commit a rule-relevant material or component state while retaining that
  object's identity and without selecting a second inventory item.
- Includes: removing the Band-Aid from The Longest Journey's rubber ducky in
  close-up and inflating the now-leaky ducky through the mouth interaction.
- Excludes: rotating or folding articulated parts into a persistent shape;
  combining two item identities into a new composite; merely inspecting an
  item; applying an already prepared item to a scene fixture.
- Parameters: object identity, exposed subpart, operation mode, state domain,
  persistence or decay, reversibility and inventory identity retention.
- Evidence: [The Longest Journey decomposition](../games/s-z/the-longest-journey.md).
- Novelty: not assessed.

## ACT-093 — Contribute inventory quantity to displayed collection slot

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player addresses one visible collection requirement and
  irreversibly transfers the displayed quantity of a compatible held inventory
  type into that requirement's persistent filled state.
- Includes: placing one copper, iron or gold bar into its Stardew Valley
  Blacksmith's Bundle slot; placing 99 Slime or 10 Bat Wings into one eligible
  Adventurer's Bundle slot.
- Excludes: giving an item to an addressed character; combining held items into
  a new identity; paying abstract currency; moving an item between reversible
  inventory containers.
- Parameters: collection, slot, accepted identities, quantity, minimum quality,
  inventory-stack consumption, reversibility and rejection feedback.
- Evidence: [Stardew Valley decomposition](../games/s-z/stardew-valley.md).
- Novelty: not assessed.

## ACT-094 — Rotate world to adjacent orthographic view

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player commands one clockwise or counterclockwise horizontal
  quarter-turn from the current settled cardinal view, making the adjacent
  orthographic projection authoritative for subsequent traversal without
  selecting or relocating individual world objects.
- Includes: rotating a Fez area left or right between its four classic 2D
  perspectives so previously depth-separated platforms can acquire different
  screen-space adjacency.
- Excludes: freely orbiting an inspection camera; rotating one held or selected
  object; turning an articulated world mechanism; moving a map fragment;
  committing a perspective image that creates replacement geometry.
- Parameters: direction, cardinal view count, angular increment, transition
  duration, unavailable avatar actions and whether chained turns are buffered.
- Evidence: [Fez decomposition](../games/a-f/fez.md).
- Novelty: not assessed.

## ACT-095 — Orbit rule-bearing perspective camera

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player continuously tilts or turns the viewing frame around
  fixed three-dimensional route geometry, and the resulting screen projection
  is used by the rules to determine an indirectly controlled agent's legal
  continuation.
- Includes: orbiting an Echochrome maze until separated path endpoints coincide
  on screen or a discontinuity is hidden, allowing the autonomous Walker to
  continue under the current perspective law.
- Excludes: four fixed cardinal quarter-turns; freely inspecting a scene whose
  camera never changes gameplay; rotating one physical object; changing world
  gravity; committing a perspective image that creates geometry.
- Parameters: yaw and pitch freedom, zoom policy, alignment tolerance, orbit
  rate, pause availability, input device and whether an alignment snap exists.
- Evidence: [Echochrome decomposition](../games/a-f/echochrome.md).
- Novelty: not assessed.

## ACT-096 — Select reachable world destination

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player selects one visible currently reachable navigation
  point, delegating the intervening multi-node route to the system rather than
  supplying each locomotion step.
- Includes: tapping Monument Valley's Chapter I pedestal after the rotating
  bridge settles into a connected state so Ida walks the complete route to it.
- Excludes: directional avatar steering; drawing the route itself; selecting
  an unreachable point as a speculative command; assigning a task to an
  autonomous population; teleporting immediately to the selected point.
- Parameters: selection tolerance, eligible surface, reachability gate, route
  recomputation, command buffering, cancellation and arrival radius.
- Evidence: [Monument Valley decomposition](../games/m-r/monument-valley.md).
- Novelty: not assessed.

## ACT-097 — Select orthogonal surface as gravity down

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player aims at one visible eligible axis-aligned world
  surface and commits its inward normal as the global down direction for the
  local physical scene, without rotating an individual body or merely changing
  the camera.
- Includes: using Manifold Garden's Gravity Shift on a wall or ceiling so that
  surface becomes the floor in its corresponding coloured gravity frame.
- Excludes: orbiting a camera; rotating a four-view projection; walking through
  a portal that reorients velocity; toggling an authored reverse-gravity field;
  choosing a diagonal or freely numeric gravity vector.
- Parameters: eligible surface class, normal quantisation, aim tolerance,
  transition duration, input lock, unavailable targets and repeat policy.
- Evidence: [Manifold Garden decomposition](../games/m-r/manifold-garden.md).
- Novelty: not assessed.

## ACT-098 — Direct free-look toward or away from rule-bearing geometry

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while retaining direct control of a first-person avatar, the
  player deliberately reorients the viewing direction toward or away from an
  identified world surface whose visibility state changes a spatial rule,
  without that camera turn itself translating the avatar.
- Includes: keeping Antichamber's `Now You See It` doorway in view so its
  destination remains stable, or turning to look through the glass window so
  the doorway leaves view and its authored replacement becomes eligible.
- Excludes: orbiting an immutable stage to make screen-space alignment
  authoritative; inspecting a frozen evidence scene; rotating the whole world;
  aiming a carried object or weapon; ordinary cosmetic camera movement with no
  rule consequence.
- Parameters: view freedom, rule-bearing surface, visibility test, look-away
  threshold, dwell requirement, avatar-motion coupling and input device.
- Evidence: [Antichamber decomposition](../games/a-f/antichamber.md).
- Novelty: not assessed.

## ACT-099 — Communicate role-exclusive observation or instruction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: one human role deliberately transmits a decision-relevant
  observation, query or instruction to another role because neither role can
  independently access both the current problem state and the rule procedure
  needed to choose the next committed control.
- Includes: the Keep Talking and Nobody Explodes Defuser verbally describing
  wire order, button appearance or bomb-edge identifiers, and an Expert
  returning the selected cut or timed button instruction.
- Excludes: optional tactical discussion when every player can inspect the
  complete state and rules; flavour dialogue; an automated hint; assigning a
  behavioural role to a simulated agent.
- Parameters: communication medium, vocabulary, direction, confirmation
  protocol, number of Experts and whether notes are permitted.
- Evidence: [Keep Talking and Nobody Explodes decomposition](../games/g-l/keep-talking-and-nobody-explodes.md).
- Novelty: not assessed.

## ACT-100 — Commit addressed bomb-module control

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the acting role commits one irreversible or time-sensitive
  physical control on an addressed live bomb module, after which the module
  immediately accepts the control or records a strike.
- Includes: cutting one selected wire; pressing and immediately releasing the
  Button; holding it to reveal a strip and releasing at a chosen timer digit.
- Excludes: communicating which control to use; inspecting the casing; editing
  a tentative assignment; pressing a resettable mechanism with no error state.
- Parameters: module type, addressed element, press/hold threshold, release
  instant, input device and whether the successful control ends the module.
- Evidence: [Keep Talking and Nobody Explodes decomposition](../games/g-l/keep-talking-and-nobody-explodes.md).
- Novelty: not assessed.

## ACT-101 — Record editable provisional glyph gloss

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player attaches or revises a free provisional semantic gloss
  for one recurring unknown glyph while its canonical meaning remains
  unconfirmed, preserving the hypothesis for later occurrences.
- Includes: writing and revising a tentative meaning beneath a Devotee glyph in
  Chants of Sennaar's notebook before its first validation page is solved.
- Excludes: assigning a value to a board cell; filling a fixed answer slot;
  selecting a supplied canonical label; editing text after validation locks it.
- Parameters: glyph identity, free-text vocabulary, edit permission, recurrence
  propagation, character limit and validation state.
- Evidence: [Chants of Sennaar decomposition](../games/a-f/chants-of-sennaar.md).
- Novelty: not assessed.

## ACT-102 — Match discovered glyph to illustrated meaning slot

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player assigns one already encountered unknown glyph to one
  authored illustrated semantic slot on a bounded validation page, building a
  revisable one-to-one interpretation before submitting the complete page.
- Includes: placing the three first Devotee glyphs beside the notebook pictures
  for open, closed and door in Chants of Sennaar.
- Excludes: typing a provisional gloss; assigning a numeral to a grid cell;
  arranging words into a sentence; choosing a world switch state.
- Parameters: discovered-glyph pool, illustrated slots, assignment gesture,
  reassignment policy, submission control and page size.
- Evidence: [Chants of Sennaar decomposition](../games/a-f/chants-of-sennaar.md).
- Novelty: not assessed.

## ACT-103 — Edit one persistent free-form answer string

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player inserts, removes or replaces characters anywhere in
  one persistent free-form string whose entire current content remains the
  answer under evaluation.
- Includes: revising the single password field in The Password Game while
  previously entered characters and already revealed rules remain in play.
- Excludes: assigning a symbol to one bounded board cell; filling typed phrase
  slots from a supplied vocabulary; submitting an immutable whole guess;
  editing source code outside play.
- Parameters: character repertoire, formatting support, cursor operations,
  length boundary, paste policy and whether edits are reversible.
- Evidence: [The Password Game decomposition](../games/s-z/the-password-game.md).
- Novelty: not assessed.

## ACT-104 — Cross-reference two visible case facts

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects two currently exposed facts from case
  materials, reference rules, speech or an explicitly empty required-document
  area and asks the system to test their declared relationship.
- Includes: highlighting an entrant's passport expiry and the booth date, or
  the empty document counter and the current entry-permit rule, in Papers,
  Please inspection mode.
- Excludes: passively reading two fields; submitting a complete case verdict;
  comparing two hidden values; filling answer slots from extracted evidence.
- Parameters: selectable fact classes, ordered or unordered selection,
  relation vocabulary, empty-area representation and reset gesture.
- Evidence: [Papers, Please decomposition](../games/m-r/papers-please.md).
- Novelty: not assessed.

## ACT-105 — Stamp one case with a terminal binary verdict

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after inspecting one presented case, the player commits exactly
  one of two mutually exclusive terminal classifications by applying its
  addressed physical or diegetic mark to the case record.
- Includes: aligning an entrant's passport beneath and applying the `APPROVED`
  or `DENIED` stamp in Papers, Please before returning the documents.
- Excludes: marking a revisable hypothesis; asserting one concealed board-cell
  class; selecting among several nonterminal dialogue responses; scoring a
  case automatically without player commitment.
- Parameters: verdict labels, stamp alignment, correction policy, required
  target document, post-stamp return and alternative terminal actions.
- Evidence: [Papers, Please decomposition](../games/m-r/papers-please.md).
- Novelty: not assessed.

## ACT-106 — Enter ordered directional code without locomotion

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while addressing one receptive world object, the player enters a
  finite ordered sequence of cardinal directions as symbolic commands rather
  than moving the controlled character through those directions.
- Includes: entering `Down, Right, Up, Left, Up, Right` at TUNIC's patterned
  door near the Overworld fountain.
- Excludes: walking an avatar along a route; tracing a continuous pointer path;
  choosing a dialogue direction; editing a complete code before submission.
- Parameters: direction alphabet, target-address condition, input device,
  sequence length, movement suppression and feedback per symbol.
- Evidence: [TUNIC decomposition](../games/s-z/tunic.md).
- Novelty: not assessed.

## ACT-107 — Acquire operational fact through authored dialogue

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player completes an authored dialogue exchange that registers
  one exact fact as learned and makes that fact available to later rule-bearing
  interactions, rather than receiving a carried object or a new physical verb.
- Includes: asking Hornfels for Outer Wilds' launch codes and completing the
  exchange that records the fixed code as known.
- Excludes: reading optional flavour text; taking a key item; entering the code
  at its target; selecting dialogue whose only consequence is narrative tone.
- Parameters: speaker, dialogue prerequisite, learned fact identity, exact
  representation, interruption policy and repeat acknowledgement.
- Evidence: [Outer Wilds decomposition](../games/m-r/outer-wilds.md).
- Novelty: not assessed.

## ACT-108 — Submit free-text term query against evidence archive

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player enters one or more freely chosen words and commits
  them as an independent retrieval request against a fixed evidence archive.
- Includes: typing a word or phrase into Her Story's L.O.G.I.C. database and
  submitting it to retrieve interview clips containing those spoken terms.
- Excludes: editing one persistent answer; selecting supplied tags; filling
  structured evidence slots; searching application source code outside play.
- Parameters: character vocabulary, phrase syntax, normalisation, submit
  gesture, query history, edit-before-submit policy and empty-query response.
- Evidence: [Her Story decomposition](../games/g-l/her-story.md).
- Novelty: not assessed.

## ACT-109 — Play selected immutable evidence record

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one available indexed audiovisual record and
  commands playback of its fixed evidence content without changing the event.
- Includes: opening and replaying a returned Her Story interview clip to inspect
  its spoken words, performance and timestamp context.
- Excludes: entering a spatial memory through a corpse; moving inside a frozen
  scene; playing a mutable simulation; passively receiving an automatic cutscene.
- Parameters: record selector, playback position, pause, replay, transcript
  display, bookmark state and whether previous discovery is required.
- Evidence: [Her Story decomposition](../games/g-l/her-story.md).
- Novelty: not assessed.

## ACT-110 — Reposition intact traversal panel in edit plane

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: in an external layout-editing mode, the player translates one
  intact panel containing fixed traversable geometry and ports while preserving
  its interior, orientation and occupants.
- Includes: dragging one early The Pedestrian public-sign panel to a new place
  in the overview before constructing the pedestrian's route.
- Excludes: moving an authoritative world-map region; swapping an illustrated
  scene among fixed slots; rotating a panel; directly creating a traversal edge.
- Parameters: edit-plane bounds, overlap policy, snap behaviour, orientation,
  retained contents and whether existing links survive repositioning.
- Evidence: [The Pedestrian decomposition](../games/s-z/the-pedestrian.md).
- Novelty: not assessed.

## ACT-112 — Mount or retrieve portable world orb at jump pedestal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while carrying a persistent orb that contains a world, the player
  places it into an eligible world-jump pedestal or retrieves that same orb from
  the pedestal, transferring the orb between carried and mounted states without
  changing its identity or contained world.
- Includes: setting Cocoon's orange world orb into a compatible jump mechanism
  to expose its world, then taking the same orb back after returning outside.
- Excludes: dropping a generic rigid object anywhere; consuming an inventory
  key in a fixture; placing a portal endpoint on a surface; changing which
  object or world the orb represents.
- Parameters: orb identity, pedestal compatibility, insertion gesture, mounted
  pose, retrieval side, occupancy capacity and rejection feedback.
- Evidence: [Cocoon decomposition](../games/a-f/cocoon.md).
- Novelty: not assessed.

## ACT-111 — Pair compatible traversal-panel ports

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects two exposed ports on different traversal
  panels and commits one explicit bidirectional graph edge between them.
- Includes: drawing a connection between compatible door endpoints or between
  complementary ladder endpoints in an early The Pedestrian sign packet.
- Excludes: merely placing panels near each other; tracing every intermediate
  route position; placing a portal on world geometry; toggling a fixed board edge.
- Parameters: endpoint-selection gesture, visible connector line, deletion,
  port type, polarity, capacity and cross-panel requirement.
- Evidence: [The Pedestrian decomposition](../games/s-z/the-pedestrian.md).
- Novelty: not assessed.
