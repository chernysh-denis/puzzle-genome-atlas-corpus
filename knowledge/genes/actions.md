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
  an unchanged physical route.
- Excludes: an instantaneous hard drop; selecting the direction of movement;
  changing a persistent difficulty setting outside play.
- Parameters: activation delay, accelerated rate and any score reward.
- Evidence: [Tetris decomposition](../games/s-z/tetris.md),
  [Pipe Mania decomposition](../games/m-r/pipe-mania.md), and
  [Mini Metro decomposition](../games/m-r/mini-metro.md), and
  [HUMANITY decomposition](../games/g-l/humanity.md), and
  [Tin Hearts decomposition](../games/s-z/tin-hearts.md).
- Novelty: not assessed.

## ACT-007 — Assign symbol to open position

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one currently assignable position and records
  one symbol from the permitted domain as that position's proposed value.
- Includes: placing a digit from 1 to 9 in an empty Sudoku cell; assigning a
  Nonogram cell as filled or confirmed empty.
- Excludes: revealing a pre-existing concealed value; annotating several
  possible candidates without assigning one; changing an immutable given.
- Parameters: symbol domain, input medium and whether tentative assignments may
  be erased or replaced.
- Evidence: [Sudoku decomposition](../games/s-z/sudoku.md) and
  [Nonogram decomposition](../games/m-r/nonogram.md).
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
  a Snakebird head one cardinal grid cell while its body follows automatically.
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
  [Shogun Showdown decomposition](../games/s-z/shogun-showdown.md).
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
  destination.
- Excludes: pulling an object; selecting and moving an object independently of
  the agent; an automatic collision response.
- Parameters: object class, body-versus-attached-tool contact, adjacency
  topology, displacement distance and whether automatic resolution changes
  object orientation.
- Evidence: [Sokoban decomposition](../games/s-z/sokoban.md) and
  [Baba Is You decomposition](../games/a-f/baba-is-you.md), and
  [Patrick's Parabox decomposition](../games/m-r/patricks-parabox.md), and
  [Stephen's Sausage Roll decomposition](../games/s-z/stephens-sausage-roll.md),
  and [A Good Snowman Is Hard to Build decomposition](../games/a-f/a-good-snowman-is-hard-to-build.md).
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
  squad to a legal island destination in Bad North.
- Excludes: moving an opponent-controlled piece; automatic opponent response;
  choosing the replacement type for a promoting pawn; adjacency-only
  directional navigation of one permanently controlled agent (`ACT-008`).
- Parameters: piece classes, destination geometry, capture convention and
  compound-move exceptions.
- Evidence: [Chess decomposition](../games/a-f/chess.md),
  [Into the Breach decomposition](../games/g-l/into-the-breach.md), and
  [Peg Solitaire decomposition](../games/m-r/peg-solitaire.md), and
  [Bad North decomposition](../games/a-f/bad-north.md), and
  [Tactical Breach Wizards decomposition](../games/s-z/tactical-breach-wizards.md).
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
  variable-length ordered route through adjacent board positions toward its
  declared terminal endpoint as one compound gesture.
- Includes: dragging a Flow Free pipe from either coloured dot through grid
  squares to the matching dot; drawing one Cosmic Express track from a fixed
  entrance stub to the selected exit; tracing a The Witness panel line from a
  start circle to its end cap.
- Excludes: assigning unrelated cells independently; selecting only two
  endpoints while the system finds a route; rotating pre-existing pipe tiles.
- Parameters: adjacency topology, terminal identity, gesture sampling,
  permitted backtracking and whether a trace may be resumed.
- Evidence: [Flow Free decomposition](../games/a-f/flow-free.md) and
  [Cosmic Express decomposition](../games/a-f/cosmic-express.md), and
  [The Witness decomposition](../games/s-z/the-witness.md).
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

## ACT-021 — Commit selected held-card subset

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects a bounded non-empty subset of cards from the
  visible hand and commits that subset either for rule evaluation or for
  discard-and-replacement.
- Includes: playing one to five Balatro cards for scoring or discarding up to
  five selected cards to draw replacements.
- Excludes: selecting a card not currently held; choosing the identities of
  replacement draws; moving one exposed card between tableau zones.
- Parameters: subset-size limit, commit modes and whether unscored extra cards
  may accompany a qualifying pattern.
- Evidence: [Balatro decomposition](../games/a-f/balatro.md).
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
  map-eligible weekly upgrade alongside the automatically awarded locomotive.
- Excludes: purchasing arbitrary items at any time; assigning the chosen asset
  to a route; generating the offered options.
- Parameters: offer size, reward families, cadence and map-specific options.
- Evidence: [Mini Metro decomposition](../games/m-r/mini-metro.md).
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
  what a later execution can reach and transform.
- Includes: arranging Opus Magnum arms, tracks, glyphs and movable reagent or
  product ports on the transmutation-engine workspace; placing and orienting
  Infinifactory conveyor / support voxels for a later factory run.
- Excludes: placing a consumable gameplay tile; moving material while the
  machine runs; editing the commands that control a placed mechanism.
- Parameters: component catalogue, placement topology, orientation set,
  movable fixed ports and deletion policy.
- Evidence: [Opus Magnum decomposition](../games/m-r/opus-magnum.md) and
  [Infinifactory decomposition](../games/g-l/infinifactory.md).
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
  keeps it at a controlled offset while navigating and releases or throws it
  back into live world physics.
- Includes: lifting, carrying and dropping a Weighted Storage Cube in Portal.
- Excludes: pushing an adjacent object one board position; relocating a board
  piece directly to a legal destination; attaching a node to a structure.
- Parameters: reach, held-object count, carry offset, collision handling,
  release impulse and portal-traversal permission.
- Evidence: [Portal decomposition](../games/m-r/portal.md).
- Novelty: not assessed.

## ACT-049 — Toggle reachable world switch

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player makes the locally navigated avatar activate a
  reachable persistent switch, changing the commanded state or travel direction
  of a linked world mechanism.
- Includes: operating a Braid lever to start or reverse its linked platform.
- Excludes: sustaining a pressure plate by occupancy; editing a remote
  timestamped interaction; placing a reusable instruction marker.
- Parameters: reach, activation gesture, binary or multi-state switch,
  retrigger delay, linked mechanism set and whether avatar motion pauses.
- Evidence: [Braid decomposition](../games/a-f/braid.md).
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

## ACT-052 — Switch direct control between field leaders

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while multiple persistent leaders remain active in the same
  field, the player transfers local navigation and follower-command authority
  from the current leader to another, leaving the former at its world state.
- Includes: switching from the Rescue Officer to Oatchi after disbanding them
  into separate Pikmin groups in Pikmin 4.
- Excludes: selecting an actor only to schedule a remote destination; swapping
  a consciousness into a newly created body; alternating adversarial turns.
- Parameters: leader classes, separation requirement, retained squads,
  switch delay, unavailable states and camera transfer.
- Evidence: [Pikmin 4 decomposition](../games/m-r/pikmin-4.md).
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

- Lifecycle: `Active`
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
  entity or board-position target, consuming that card to apply its declared
  movement, attack, defence or repositioning transition.
- Includes: playing a Fights in Tight Spaces movement card on a legal cell or
  an attack / push card on a legal enemy or adjacent target.
- Excludes: selecting an ability from a persistent unit menu; committing a
  held subset for pattern evaluation; placing a card as a persistent world
  object; choosing a target for an enemy's already committed attack.
- Parameters: card type, target geometry, cost, compound effects, facing and
  target eligibility.
- Evidence: [Fights in Tight Spaces decomposition](../games/a-f/fights-in-tight-spaces.md).
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
