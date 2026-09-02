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
  [Echochrome decomposition](../games/a-f/echochrome.md),
  [SimCity 4 Deluxe Edition decomposition](../games/s-z/simcity-4-deluxe-edition.md)
  and [Cities: Skylines decomposition](../games/a-f/cities-skylines.md), and
  [Football Manager 26 decomposition](../games/a-f/football-manager-26.md).
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
  Rescue Officer or Oatchi through a Pikmin 4 surface area; walking between
  connected drafted rooms in Blue Prince's current manor; moving Patrick one
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
  central model, scale-linked courtyards, key bridges and fixed house exit;
  running, jogging and dribbling the currently controlled footballer across an
  EA SPORTS FC 26 pitch; walking, crouching, jumping and dashing Ryu through
  the bounded Street Fighter 6 Versus arena;
  walking, sprinting, jumping and crouching V through Night City and authored
  Cyberpunk 2077 mission spaces; directly moving and jumping a selected Marvel
  Rivals hero through a live arena; running and jumping Hornet through
  Pharloom's connected rooms in Hollow Knight: Silksong; running, jumping,
  dashing, swimming and grappling Mio or Zoe through Split Fiction's Rader
  Publishing chapter.
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
  [EA SPORTS FC 26 decomposition](../games/a-f/ea-sports-fc-26.md), and
  [Antichamber decomposition](../games/a-f/antichamber.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md),
  [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md), and
  [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md), and
  [Split Fiction decomposition](../games/s-z/split-fiction.md), and
  [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Additional support: [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md),
  for direct room navigation.
- Additional support: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md),
  for direct survivor movement through the generated Forest world.
- Additional support: [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md),
  for direct class movement through the authored Upward combat route.
- Additional support: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md),
  for direct Survivor traversal through the authored Hotel route.
- Additional support: [Destiny 2 decomposition](../games/a-f/destiny-2.md),
  for direct Titan traversal through the authored Devil's Lair route.
- Additional support: [Brawlhalla decomposition](../games/a-f/brawlhalla.md),
  for ground, air and wall movement through one bounded fighting arena.
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
  and [Bad North decomposition](../games/a-f/bad-north.md),
  [Tactical Breach Wizards decomposition](../games/s-z/tactical-breach-wizards.md)
  and [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
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
  removed line for reuse; drawing and revising a Cities: Skylines public-
  transport line through its ordered stops.
- Excludes: tracing a one-use path from a fixed endpoint; placing immutable
  queue-head tiles; commanding a vehicle's next stop directly.
- Parameters: allowed edit gestures, loop permission, node-revisit rule and
  whether edits may occur while simulation time is paused.
- Evidence: [Mini Metro decomposition](../games/m-r/mini-metro.md) and
  [Cities: Skylines decomposition](../games/a-f/cities-skylines.md).
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
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
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
  Sennaar's first water instruction to its commanded open or closed state;
  activating reachable Split Fiction Chapter 1 consoles that change a linked
  barrier or platform independently of paired co-op gates.
- Excludes: sustaining a pressure plate by occupancy; editing a remote
  timestamped interaction; placing a reusable instruction marker.
- Parameters: reach, activation gesture, binary or multi-state switch,
  retrigger delay, linked mechanism set and whether avatar motion pauses.
- Evidence: [Braid decomposition](../games/a-f/braid.md),
  [Manifold Garden decomposition](../games/m-r/manifold-garden.md), and
  [Chants of Sennaar decomposition](../games/a-f/chants-of-sennaar.md), and
  [Split Fiction decomposition](../games/s-z/split-fiction.md).
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
  Swapper body into a visible existing clone while the former body remains;
  switching direct control to an eligible teammate while the former footballer
  remains on the pitch under team AI in EA SPORTS FC 26.
- Excludes: selecting an actor only to schedule a remote destination; creating
  a new body without transferring control; teleporting one unchanged body;
  alternating adversarial turns.
- Parameters: eligible body classes, target-selection method, separation
  requirement, retained follower groups, former-body behaviour, transfer delay,
  unavailable states and camera transfer.
- Evidence: [Pikmin 4 decomposition](../games/m-r/pikmin-4.md) and
  [The Swapper decomposition](../games/s-z/the-swapper.md), and
  [EA SPORTS FC 26 decomposition](../games/a-f/ea-sports-fc-26.md).
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
  and revising a Freeways interchange between traffic evaluations; constructing
  and upgrading persistent roads in SimCity 4 and Cities: Skylines.
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
  [The Longest Journey decomposition](../games/s-z/the-longest-journey.md), and
  [Blue Prince decomposition](../games/a-f/blue-prince.md), and
  [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
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
  [Day of the Tentacle decomposition](../games/a-f/day-of-the-tentacle.md), and
  [Blue Prince decomposition](../games/a-f/blue-prince.md).
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
- Evidence: [Monument Valley decomposition](../games/m-r/monument-valley.md)
  and [The Sims 4 decomposition](../games/s-z/the-sims-4.md).
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
- Definition: while addressing one receptive world object or command
  interface, the player enters a
  finite ordered sequence of cardinal directions as symbolic commands rather
  than moving the controlled character through those directions.
- Includes: entering `Down, Right, Up, Left, Up, Right` at TUNIC's patterned
  door near the Overworld fountain; entering a selected Helldivers 2
  stratagem's directional command sequence.
- Excludes: walking an avatar along a route; tracing a continuous pointer path;
  choosing a dialogue direction; editing a complete code before submission.
- Parameters: direction alphabet, target-address condition, input device,
  sequence length, movement suppression and feedback per symbol.
- Evidence: [TUNIC decomposition](../games/s-z/tunic.md) and
  [Helldivers 2 decomposition](../games/g-l/helldivers-2.md).
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
  exchange that records the fixed code as known; completing Cyberpunk 2077
  mission conversations that register actionable people, places or access.
- Excludes: reading optional flavour text; taking a key item; entering the code
  at its target; selecting dialogue whose only consequence is narrative tone.
- Parameters: speaker, dialogue prerequisite, learned fact identity, exact
  representation, interruption policy and repeat acknowledgement.
- Evidence: [Outer Wilds decomposition](../games/m-r/outer-wilds.md) and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
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

## ACT-113 — Aim and release projectile from fixed launcher

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player adjusts the direction and launch strength of one
  projectile at a fixed launcher, then commits its release into live physics.
- Includes: pulling and releasing a bird from the Angry Birds slingshot; aiming
  and firing one Peggle ball from the top launcher.
- Excludes: steering a projectile after launch; placing a portal endpoint;
  selecting a discrete destination without a continuous launch trajectory.
- Parameters: angular range, strength control, aim guide, projectile type and
  whether a character ability may be triggered after release.
- Evidence: [Angry Birds Classic decomposition](../games/a-f/angry-birds-classic.md)
  and [Peggle Deluxe decomposition](../games/m-r/peggle-deluxe.md).
- Novelty: not assessed.

## ACT-114 — Grip world geometry with independently controlled hands

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player raises and steers each articulated hand independently
  and holds contact to create a temporary physical grip on reachable geometry.
- Includes: gripping a ledge with one or both hands in Human: Fall Flat, then
  pulling the ragdoll body upward or suspending it while repositioning.
- Excludes: picking up one rigid object into a centred carry pose; attaching an
  autonomous agent to a structure; an animation-only climb command.
- Parameters: hand channels, reach, grip strength, release control, body mass
  and collision response.
- Evidence: [Human: Fall Flat decomposition](../games/g-l/human-fall-flat.md).
- Novelty: not assessed.

## ACT-115 — Inspect game-authored external interface artefact

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player leaves or shifts focus from the game world to inspect
  a file, desktop layer or mock operating-system artefact created by the game
  and uses its content as puzzle information.
- Includes: opening the authored document or desktop clue used by OneShot's PC
  release; inspecting the corresponding mock-OS artefact in World Machine
  Edition.
- Excludes: reading an in-world manual; searching an unauthorised walkthrough;
  opening a purely diagnostic log with no puzzle consequence.
- Parameters: host interface, artefact path, update trigger, accessibility
  alternative and whether the game remains visible simultaneously.
- Evidence: [OneShot decomposition](../games/m-r/oneshot.md).
- Novelty: not assessed.

## ACT-116 — Zone land by use class and density

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player paints bounded land parcels with an allowed urban use
  and density, authorising rather than directly placing the buildings that may
  later develop there.
- Includes: drawing low-, medium- or high-density residential, commercial or
  industrial zones in SimCity 4; painting residential, commercial, industrial
  or office zones by available density in Cities: Skylines.
- Excludes: placing a specific building footprint; changing tax policy; drawing
  a road or utility line.
- Parameters: use class, density, parcel depth, frontage, de-zoning and cost.
- Evidence: [SimCity 4 Deluxe Edition decomposition](../games/s-z/simcity-4-deluxe-edition.md)
  and [Cities: Skylines decomposition](../games/a-f/cities-skylines.md).
- Novelty: not assessed.

## ACT-117 — Place priced civic or utility infrastructure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player commits a priced facility or drawn distribution
  segment whose position and operating state alter municipal coverage.
- Includes: placing power plants, water facilities, schools, hospitals, police,
  fire and waste facilities, and drawing power or water distribution in
  SimCity 4 and Cities: Skylines.
- Excludes: zoning land for autonomous private development; drawing a road;
  changing a department's funding slider.
- Parameters: footprint, construction cost, upkeep, capacity, radius, network
  attachment and demolition refund.
- Evidence: [SimCity 4 Deluxe Edition decomposition](../games/s-z/simcity-4-deluxe-edition.md)
  and [Cities: Skylines decomposition](../games/a-f/cities-skylines.md).
- Novelty: not assessed.

## ACT-118 — Adjust municipal tax rate or service funding

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player changes a persistent fiscal parameter that governs a
  sector's tax burden or a public facility's recurring funding and capacity.
- Includes: editing SimCity 4 or Cities: Skylines tax rates by zone category
  and changing the funding of transport, utility or civic services.
- Excludes: paying a one-time construction cost; accepting a neighbour deal;
  selecting simulation speed.
- Parameters: affected category, percentage, effective capacity, upkeep and
  demand or approval response.
- Evidence: [SimCity 4 Deluxe Edition decomposition](../games/s-z/simcity-4-deluxe-edition.md)
  and [Cities: Skylines decomposition](../games/a-f/cities-skylines.md).
- Novelty: not assessed.

## ACT-119 — Place, rotate or deconstruct live factory entity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while a production world continues running, the player places,
  rotates, removes or replaces a persistent machine, transport, power or
  defence entity whose footprint immediately joins or alters the live system.
- Includes: placing and rotating Factorio mining drills, belts, inserters,
  assemblers, pipes, power poles, rails, chests, walls and turrets, or mining
  those entities back into inventory while the rest of the factory advances.
- Excludes: editing a machine only in a separate stopped design phase; zoning
  land for autonomous development; stamping a non-materialised construction
  plan without supplying its entities.
- Parameters: entity catalogue, footprint, orientation, placement reach,
  inventory cost, fast replacement and deconstruction return.
- Evidence: [Factorio decomposition](../games/a-f/factorio.md) and
  [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Novelty: not assessed.

## ACT-120 — Configure local factory-entity operating rule

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player assigns or revises a persistent local rule that tells
  one placed factory entity what to make, accept, dispatch or do when a visible
  signal condition is satisfied.
- Includes: selecting a Factorio assembling-machine recipe; setting inserter,
  splitter, chest or train filters; editing a train schedule; or connecting a
  machine to a circuit-network threshold.
- Excludes: physically placing the entity; selecting a global technology to
  research; directly moving the item that the rule later handles.
- Parameters: entity class, recipe, filter, schedule, signal expression,
  comparison operator and enable/disable state.
- Evidence: [Factorio decomposition](../games/a-f/factorio.md).
- Novelty: not assessed.

## ACT-121 — Queue technology research

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one or more currently reachable technologies
  and commits their order in a persistent queue whose front entry receives
  subsequent research progress.
- Includes: choosing Factorio technologies, queueing their prerequisites and
  reordering or replacing the current research target.
- Excludes: producing science packs; choosing a machine recipe; receiving an
  automatic upgrade with no player-selected research order.
- Parameters: prerequisite graph, queue length, reorder policy, saved partial
  progress and unavailable-node feedback.
- Evidence: [Factorio decomposition](../games/a-f/factorio.md) and
  [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
- Novelty: not assessed.

## ACT-122 — Manually extract or dismantle world entity

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player holds an extraction command on a reachable resource
  or removable entity until its progress completes and the resulting material
  or recoverable entity enters inventory.
- Includes: hand-mining Factorio ore, rock or tree resources and manually
  dismantling a placed entity before automated deconstruction is available.
- Excludes: an operating mining drill producing ore automatically; destroying
  an enemy with a weapon; instant selection of an item already in storage.
- Parameters: target class, extraction time, tool or character modifier,
  yielded items, placement recovery and cancellation progress.
- Evidence: [Factorio decomposition](../games/a-f/factorio.md).
- Novelty: not assessed.

## ACT-123 — Craft a selected known inventory recipe

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one currently known and legal personal recipe and commits one or more copies of its declared output.
- Includes: Factorio and Cyberpunk 2077 personal crafting, Monster Hunter Wilds field crafting and Terraria inventory or nearby-station crafting.
- Excludes: assigning a recipe to an autonomous production entity; arbitrary object combination; research selection; system-owned resolution duration.
- Parameters: recipe, quantity, ingredient source, station context, immediate or queued resolution and output.
- Evidence: [Factorio decomposition](../games/a-f/factorio.md), [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md), [Terraria decomposition](../games/s-z/terraria.md) and [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Novelty: not assessed.

## ACT-124 — Stamp reusable construction or deconstruction plan

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player places a reusable multi-entity plan or marked removal
  region into the live world, creating persistent ghost requests rather than
  immediately materialising or removing every affected entity by hand.
- Includes: stamping, rotating and flipping a Factorio blueprint, placing a
  copied factory section and marking an area for construction-robot removal.
- Excludes: direct placement of one supplied entity; a decorative overlay with
  no fulfilment request; loading an authored level layout.
- Parameters: blueprint contents, anchor, rotation, mirroring, overlap policy,
  upgrade planner, deconstruction filters and ghost lifetime.
- Evidence: [Factorio decomposition](../games/a-f/factorio.md).
- Novelty: not assessed.

## ACT-125 — Play one held effect card

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one currently held card, supplies any legal
  declared target and pays its current cost so the card's immediate and
  persistent effects resolve.
- Includes: playing one Slay the Spire Attack, Skill or Power card during the
  player phase, with an enemy target when the card requires one.
- Excludes: committing several held cards together for pattern evaluation;
  placing a card as a persistent world object; playing a card whose defining
  parameter is a spatial cell, direction or displacement geometry.
- Parameters: card identity, target requirement, current cost, generated-card
  status, exhaust or retain keywords and effect text.
- Evidence: [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
- Novelty: not assessed.

## ACT-126 — End the current player combat phase

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player explicitly commits the current combat phase, giving
  up any remaining ordinary card plays so end-of-turn and hostile effects can
  resolve.
- Includes: pressing End Turn in Slay the Spire after any number of legal card
  and potion uses.
- Excludes: the automatic resolution after every individual command; ending a
  real-time shift; activating a prepared spatial attack queue.
- Parameters: remaining-resource treatment, confirmation behaviour, end-turn
  triggers and whether the command can be reversed before resolution.
- Evidence: [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
- Novelty: not assessed.

## ACT-127 — Choose a reachable node on a revealed branching route

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: from the current route position, the player selects one visibly
  connected successor node whose disclosed category determines the next
  encounter or service.
- Includes: choosing a connected Slay the Spire map node marked as combat,
  elite, unknown, rest site, shop or treasure.
- Excludes: drawing or editing the route; selecting an arbitrary remote
  destination; choosing among rewards after the node has resolved.
- Parameters: route depth, branch degree, node categories, revealed horizon
  and exceptional reach modifiers.
- Evidence: [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
- Novelty: not assessed.

## ACT-128 — Accept or skip one offered persistent-deck card

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after an encounter or event presents a bounded card offer, the
  player either adds exactly one offered card to the run's persistent deck or
  declines the complete offer.
- Includes: choosing one of the ordinary post-combat Slay the Spire card
  rewards or pressing Skip.
- Excludes: drawing a temporary combat hand; buying a priced card; replacing a
  card through transformation; choosing several cards from one offer.
- Parameters: offer size, eligible pool, rarity, upgrade state, skip reward and
  mandatory-choice exceptions.
- Evidence: [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
- Novelty: not assessed.

## ACT-129 — Apply one persistent modification to a deck card

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one eligible card already in the persistent
  run deck and applies a declared lasting upgrade, removal or transformation.
- Includes: Smithing one Slay the Spire card at a rest site, paying a merchant
  to remove one card, or accepting an event option that transforms one card.
- Excludes: adding a reward card; changing a card only for the current combat;
  sorting or viewing the deck without mutation.
- Parameters: modification type, eligible card set, price, upgrade ceiling,
  replacement pool and event restrictions.
- Evidence: [Slay the Spire decomposition](../games/s-z/slay-the-spire.md).
- Novelty: not assessed.

## ACT-130 — Purchase one offered scoped asset or service

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player spends current scoped currency to acquire one currently offered asset or execute one priced service.
- Includes: run merchants, Blue Prince room shops, Dota 2 match shops, Grand Theft Auto V and Cyberpunk 2077 stores, Hollow Knight: Silksong wares, and Counter-Strike 2 freeze/buy-time equipment purchases.
- Excludes: a free reward; recurring operating cost; unavailable offer; cosmetic marketplace trade.
- Parameters: currency, offer, asset or service, purchase window, location, inventory lifetime and persistence horizon.
- Evidence: [Slay the Spire decomposition](../games/s-z/slay-the-spire.md), [Dota 2 decomposition](../games/a-f/dota-2.md), [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md), [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md), [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md), [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md) and [Blue Prince decomposition](../games/a-f/blue-prince.md).
- Novelty: not assessed.

## ACT-131 — Consume one held immediate-effect item

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player activates one item from a bounded carried consumable
  inventory, optionally supplies a legal target and permanently empties that
  slot after the item's immediate effect resolves.
- Includes: drinking or throwing a held Slay the Spire potion during a legal
  combat timing window.
- Excludes: playing a deck card; equipping a persistent relic; applying a held
  world object to a spatial fixture.
- Parameters: item identity, target requirement, use timing, slot count and
  discard-without-use rule.
- Evidence: [Slay the Spire decomposition](../games/s-z/slay-the-spire.md),
  [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md)
  and [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Additional support: [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md),
  for one held card, rune or pill consumed into an immediate effect; and
  [Blue Prince decomposition](../games/a-f/blue-prince.md), for one held
  immediate-effect manor item.
- Novelty: not assessed.

## ACT-132 — Paint administrative district and assign local policy

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player delineates a persistent spatial district and applies,
  removes or changes a declared policy or land-use specialisation whose
  mechanical effects are scoped to that boundary.
- Includes: painting a Cities: Skylines district and assigning a base-game
  local policy or industrial specialisation to it.
- Excludes: changing a city-wide tax rate; zoning private land by use and
  density; placing one civic facility; a decorative district name with no
  rule effect.
- Parameters: boundary-edit gesture, policy catalogue, specialisation,
  eligibility, upkeep, overlap rule and removal behaviour.
- Evidence: [Cities: Skylines decomposition](../games/a-f/cities-skylines.md).
- Novelty: not assessed.

## ACT-133 — Duplicate a built factory region from a reusable blueprint

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player captures a selected multi-entity factory region as a
  reusable plan and pastes, rotates or mirrors that plan so its compatible
  entities immediately become part of the running factory.
- Includes: shapez 2 blueprints that copy machine, belt, lift, pipe or platform
  layouts and place another working instance by spending any configured
  blueprint-point cost.
- Excludes: a Factorio blueprint that creates unfulfilled ghost requests;
  manually rebuilding each entity; exporting an image with no world effect.
- Parameters: captured region, anchor, rotation, mirroring, compatible
  footprint, blueprint-point cost and unavailable-content handling.
- Evidence: [shapez 2 decomposition](../games/s-z/shapez-2.md).
- Novelty: not assessed.

## ACT-134 — Purchase one persistent factory research upgrade

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player spends accumulated research points on one currently
  eligible shop node, persistently adding its building, mechanic, capacity or
  throughput modifier to the current save.
- Includes: buying shapez 2 machine levels, belt or train speed, platform
  capacity, Vortex inputs, wires or other unlocked shop upgrades.
- Excludes: automatically receiving a milestone reward; queueing research that
  laboratories advance over time; changing a machine's local operating rule.
- Parameters: node, prerequisite milestone, point cost, level, unlocked
  catalogue and persistent effect.
- Evidence: [shapez 2 decomposition](../games/s-z/shapez-2.md).
- Novelty: not assessed.

## ACT-135 — Play held creature card into open combat lane

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one creature card from the visible hand, pays
  its current legal cost and places it as a persistent combatant in one chosen
  unoccupied friendly lane.
- Includes: placing an Act I Inscryption Beast card into one of the player's
  four open card spaces after satisfying its Blood, Bone or free cost.
- Excludes: playing a card whose effects resolve without occupying a lane;
  transferring an exposed tableau card between storage zones; placing a card
  as a persistent overworld tile.
- Parameters: lane count, card identity, cost class, placement timing, occupied-
  lane rejection and on-play effects.
- Evidence: [Inscryption decomposition](../games/g-l/inscryption.md).
- Novelty: not assessed.

## ACT-136 — Sacrifice selected controlled creatures as Blood payment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while paying one pending creature-card cost, the player selects
  a sufficient subset of eligible friendly combatants and commits their
  declared sacrifice value, normally removing them from their lanes.
- Includes: sacrificing one or more ordinary Act I Inscryption creatures to
  pay the Blood pips of the creature currently being played.
- Excludes: removing a persistent deck card at a map event; losing a creature
  to hostile damage; spending an already accumulated numeric currency.
- Parameters: pending cost, eligible creatures, sacrifice value, survival
  exceptions, overpayment and cancellation before placement.
- Evidence: [Inscryption decomposition](../games/g-l/inscryption.md).
- Novelty: not assessed.

## ACT-137 — Draw one card from a chosen combat deck

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: at the ordinary draw step, the player selects one of several
  currently available ordered draw piles and takes its concealed top card into
  the visible hand.
- Includes: choosing between the persistent main deck and the Squirrel side
  deck at the start of an Act I Inscryption player turn.
- Excludes: selecting a known card from an open catalogue; automatically
  replacing a complete hand; choosing which card enters a shuffled deck.
- Parameters: deck identities, availability, known composition, concealed
  order, forced opening draw and exhaustion behaviour.
- Evidence: [Inscryption decomposition](../games/g-l/inscryption.md).
- Novelty: not assessed.

## ACT-138 — Compose future-run card from sampled source traits

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a failed run, the player makes successive choices from
  bounded sampled source cards so one new card inherits the selected cost,
  statistics and ability set for possible appearance in later runs.
- Includes: choosing the cost, Power and Health, and Sigils of an Act I
  Inscryption Deathcard from three separately sampled groups, then naming it.
- Excludes: freely assigning arbitrary card values; upgrading an existing run
  card; combining duplicate cards during the same run.
- Parameters: sampled group size, trait order, excluded source cards, inherited
  fields, naming and future-offer eligibility.
- Evidence: [Inscryption decomposition](../games/g-l/inscryption.md).
- Novelty: not assessed.

## ACT-139 — Place, move or demolish staffed settlement building

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player places a settlement building on compatible terrain,
  may reassign its position where the rules permit, or marks it for demolition,
  changing the live set of workplaces, housing or services.
- Includes: constructing, moving or demolishing ordinary buildings in an
  Against the Storm settlement.
- Excludes: selecting a recipe inside an already placed building; stamping a
  reusable multi-entity plan; placing a card into a combat lane.
- Parameters: footprint, terrain, orientation, construction cost, move cost,
  refund, building category and maximum copies.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md) and
  [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
- Novelty: not assessed.

## ACT-140 — Commit one option from bounded persistent offer

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the system presents a finite set of mutually exclusive options
  and the player commits one whose selected rule, task or asset persists beyond
  the choice interface.
- Includes: choosing one blueprint, cornerstone, Order, newcomer group or glade
  event resolution in Against the Storm; choosing Grand Theft Auto V's terminal
  Story Mode option; choosing Cyberpunk 2077's base-game terminal route and
  final contract response.
- Excludes: purchasing any number of catalogue items; choosing a temporary
  dialogue line with no mechanical persistence; selecting a known route node.
- Parameters: offer type, option count, rerolls, selection count, duration,
  prerequisite and whether deferral is allowed.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md)
  [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md) and
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Novelty: not assessed.

## ACT-141 — Favour one population group at others' expense

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player designates one population group to receive a declared
  asymmetric welfare modifier while the competing groups receive the paired
  penalty.
- Includes: favouring one species in Against the Storm, increasing its Resolve
  while lowering the Resolve of every other species.
- Excludes: assigning workers to jobs; supplying one need to all eligible
  residents; selecting a global difficulty modifier.
- Parameters: favoured group, bonus, non-favoured penalty, duration and
  cancellation.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## ACT-142 — Choose reachable metaworld destination and embark package

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before starting a bounded run, the player selects one currently
  reachable destination on a persistent world map and commits a limited package
  of starting people, resources or bonuses.
- Includes: choosing an embarkation tile and embarkation bonuses before an
  Against the Storm settlement.
- Excludes: ordinary movement inside a settlement; choosing a node on a
  self-contained run map; freely editing the starting inventory.
- Parameters: range, terrain, modifiers, cost budget, population, goods and
  persistent foothold used as the origin.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## ACT-143 — Purchase persistent metaprogression upgrade

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: between bounded runs, the player spends persistent resources on
  one prerequisite-valid upgrade whose rules or starting benefits apply to
  later runs.
- Includes: buying a Citadel upgrade in Against the Storm.
- Excludes: buying a run-local trader item; unlocking content automatically at
  a level threshold; selecting a temporary cornerstone.
- Parameters: resource costs, predecessor level, branch, unlock effect and
  maximum rank.
- Evidence: [Against the Storm decomposition](../games/a-f/against-the-storm.md).
- Novelty: not assessed.

## ACT-144 — Mark spatial colony work order

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player marks world cells or objects for a typed autonomous
  work errand without directly steering the worker who later claims it.
- Includes: painting Oxygen Not Included dig, harvest, mop, sweep, disinfect,
  attack, wrangle, repair or deconstruction orders.
- Excludes: directly moving a Duplicant; placing a building plan; changing an
  already generated errand's priority.
- Parameters: errand type, brush footprint, eligibility, cancellation and default priority.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## ACT-150 — Author conditional fortress production order

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player creates a repeatable production order whose recipe,
  quantity, frequency and stock conditions persist for autonomous execution.
- Includes: Dwarf Fortress manager work orders with material, amount, repeat
  cadence and checked conditions.
- Excludes: ordering one immediate workshop job; directly crafting an item;
  configuring transport filters.
- Parameters: recipe, amount, workshop scope, frequency, conditions, material
  masks and cancellation.
- Evidence: [Dwarf Fortress decomposition](../games/a-f/dwarf-fortress.md).
- Novelty: not assessed.

## ACT-151 — Configure filtered stockpile and supply links

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player declares which item categories a spatial store may
  accept and optionally directs its giving or taking relationships.
- Includes: Dwarf Fortress custom stockpile filters and workshop or stockpile links.
- Excludes: moving one item by hand; choosing a production recipe; drawing a vehicle route.
- Parameters: footprint, categories, qualities, materials, containers,
  give-to links, take-from links and priority.
- Evidence: [Dwarf Fortress decomposition](../games/a-f/dwarf-fortress.md).
- Novelty: not assessed.

## ACT-152 — Define functional zone or owned room

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player marks a spatial area, selects its institutional
  function and may assign it to a resident or service.
- Includes: Dwarf Fortress bedrooms, offices, dining rooms, hospitals,
  meeting areas, pastures and other zones.
- Excludes: placing qualifying furniture; selecting a work detail; merely naming an area.
- Parameters: footprint, function, owner, accepted creatures, service flags
  and overlapping-zone rules.
- Evidence: [Dwarf Fortress decomposition](../games/a-f/dwarf-fortress.md).
- Novelty: not assessed.

## ACT-153 — Configure squad equipment, schedule and order

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player persistently assigns residents to a military group,
  specifies its equipment and training schedule, then activates a group order.
- Includes: Dwarf Fortress squads, uniforms, monthly schedules, training,
  station, patrol, kill and defend orders.
- Excludes: directly steering one combatant; civilian work details; automatic targeting.
- Parameters: members, leader, uniform, ammunition, month, minimum attendance,
  alert and active order.
- Evidence: [Dwarf Fortress decomposition](../games/a-f/dwarf-fortress.md).
- Novelty: not assessed.

## ACT-154 — Appoint resident to administrative or noble office

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player assigns an eligible resident to a persistent office
  that unlocks administrative work or creates declared institutional demands.
- Includes: appointing a manager, broker, bookkeeper or militia commander in
  Dwarf Fortress and assigning rooms required by the office.
- Excludes: assigning one workshop job; hereditary simulation-only appointment;
  choosing a labour preference.
- Parameters: office, candidate, requirements, rooms, mandates and replacement.
- Evidence: [Dwarf Fortress decomposition](../games/a-f/dwarf-fortress.md).
- Novelty: not assessed.

## ACT-145 — Configure per-agent and per-errand priority

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player persistently changes how one autonomous agent ranks
  work categories or how the colony ranks one generated errand against peers.
- Includes: Oxygen Not Included Duplicant priorities, disabled categories,
  building sub-priorities and yellow-alert escalation.
- Excludes: selecting a worker for one immediate action; setting a machine
  recipe; editing the daily schedule.
- Parameters: agent, category, relative tier, sub-priority, proximity rule and alert state.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## ACT-146 — Train one agent in prerequisite skill

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player spends one earned skill point on an eligible node in
  one agent's prerequisite tree, persistently granting its permission or bonus
  while raising that agent's expectation cost.
- Includes: assigning Oxygen Not Included digging, researching, operating,
  carrying, farming, ranching or rocketry skills to one Duplicant.
- Excludes: passive attribute experience; researching colony technology;
  selecting a starting trait.
- Parameters: agent, skill point, prerequisite, permission, bonus, interest and morale expectation.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## ACT-147 — Edit agent activity schedule

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player assigns agents to a repeating timetable and edits its
  blocks so autonomous behaviour switches among work, downtime, hygiene and sleep.
- Includes: Oxygen Not Included schedules, membership and cycle blocks.
- Excludes: prioritising one work errand; pausing the whole simulation; a fixed
  authored day/night change.
- Parameters: membership, block type, cycle position, duration and emergency override.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## ACT-148 — Place material-backed construction plan

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects a known structure and commits a compatible
  footprint plus construction material as a plan that autonomous workers must supply and build.
- Includes: Oxygen Not Included buildings, tiles, wires, pipes, automation
  wire, ladders and rocket modules.
- Excludes: instantly materialising an entity from inventory; marking natural
  terrain for digging; stamping a reusable multi-entity blueprint.
- Parameters: structure, footprint, orientation, material, mass cost, priority and supply state.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## ACT-149 — Select colony research target

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one reachable technology as the colony-wide
  target whose required research-point types will be produced by staffed stations.
- Includes: choosing an Oxygen Not Included research-tree node after its prerequisites are complete.
- Excludes: assigning a Duplicant to research work; supplying station material;
  buying a metaprogression upgrade.
- Parameters: prerequisite graph, point types, costs, cancellation, partial progress and unlocks.
- Evidence: [Oxygen Not Included decomposition](../games/m-r/oxygen-not-included.md).
- Novelty: not assessed.

## ACT-155 — Assign allowed area and personal colony policy

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player persistently assigns one autonomous resident a spatial
  allowed area and one or more declared consumption, treatment or equipment policies.
- Includes: RimWorld allowed areas plus food, drug, outfit and medicine policies.
- Excludes: one immediate movement order; work-category priority; a temporary draft order.
- Parameters: resident, area, food, drugs, apparel, medicine and emergency override.
- Evidence: [RimWorld decomposition](../games/m-r/rimworld.md).
- Novelty: not assessed.

## ACT-156 — Draft resident and issue exact tactical order

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player temporarily suspends one autonomous resident's ordinary
  work and directly orders exact movement, target or combat actions in live time.
- Includes: drafting RimWorld colonists, positioning them and ordering attacks,
  rescue, arrest or field tending.
- Excludes: persistent work priorities; autonomous nearby engagement; squad policy.
- Parameters: resident set, destination, queue, target, ability and undraft state.
- Evidence: [RimWorld decomposition](../games/m-r/rimworld.md).
- Novelty: not assessed.

## ACT-157 — Form and route loaded world caravan

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects people, animals and cargo for a travelling
  group, commits its formation, then chooses reachable world-map destinations.
- Includes: RimWorld caravan membership, supplies, pack animals and route orders.
- Excludes: a local hauling job; an arriving trader; unrestricted teleportation.
- Parameters: members, cargo, capacity, supplies, destination, route and split or merge.
- Evidence: [RimWorld decomposition](../games/m-r/rimworld.md).
- Novelty: not assessed.

## ACT-158 — Configure prisoner interaction policy

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player assigns a captive's persistent handling goal and care
  settings so eligible wardens attempt release, resistance reduction or recruitment.
- Includes: RimWorld prisoner interaction modes and medicine policy.
- Excludes: one combat arrest; buying a recruit; automatic population growth.
- Parameters: prisoner, interaction mode, medicine, warden and recruitment threshold.
- Evidence: [RimWorld decomposition](../games/m-r/rimworld.md).
- Novelty: not assessed.

## ACT-159 — Target a reachable terrain cell to break it

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player aims at one reachable mutable terrain cell and holds
  the break command to remove its block, wall or placed object with the current
  hand or tool.
- Includes: Minecraft Survival breaking a tree or stone block; Terraria mining
  a foreground block, breaking a background wall or freeing placed furniture.
- Excludes: placing a factory entity; moving a free object; painting an
  abstract board cell with no embodied reach requirement.
- Parameters: projection, layer, target cell, reach, held tool, break duration
  and block class.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md) and
  [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## ACT-160 — Arrange inventory materials in a spatial crafting grid

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player places carried material quantities into named cells of
  an available crafting grid, then collects the recipe result when the full
  identity, quantity and spatial arrangement match one declared recipe.
- Includes: Minecraft's 2×2 inventory crafting and 3×3 crafting-table recipes.
- Excludes: selecting a queued hand-craft recipe; combining two arbitrary held
  inventory objects; assigning an autonomous machine recipe.
- Parameters: grid size, cell arrangement, item identity, stack quantity,
  recipe-book autofill, result and remainder items.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md).
- Novelty: not assessed.

## ACT-161 — Aim and strike a reachable hostile with the current tool

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player aims an equipped melee or ranged combat tool at one
  reachable hostile and commits a direct strike or shot rather than assigning
  an autonomous squad or selecting an abstract card target.
- Includes: Minecraft Survival attacks against hostile mobs and the Ender Dragon;
  Counter-Strike 2 aimed firearm, knife and utility attacks; Cyberpunk 2077
  aimed firearm and melee attacks against reachable hostiles; Marvel Rivals
  hero primary attacks against visible opponents; Hornet's aimed needle
  strikes against reachable hostiles in Hollow Knight: Silksong; Split Fiction
  Chapter 1 gunner shots and direct attacks against authored hostiles.
- Excludes: automatic turret fire; a turn-based ability card; a group waypoint
  that causes agents to acquire targets on their own.
- Parameters: target, reach, weapon, cooldown, projectile, damage, armour and
  hit condition.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md) and
  [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md),
  [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md), and
  [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md), and
  [Split Fiction decomposition](../games/s-z/split-fiction.md).
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Additional support: [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md),
  for directly aimed tear shots.
- Additional support: [War Thunder decomposition](../games/s-z/war-thunder.md),
  for direct ground-vehicle gun aiming and fire.
- Additional support: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md),
  for directly commanded melee attacks against Forest hostiles.
- Additional support: [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md),
  for directly aimed stock-weapon attacks against opposing classes.
- Additional support: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md),
  for aimed firearm/melee attacks and the close-range shove.
- Additional support: [Destiny 2 decomposition](../games/a-f/destiny-2.md),
  for directly aimed firearm, melee and boss attacks.
- Novelty: not assessed.

## ACT-162 — Place a held tile into a reachable world cell

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player aims at a reachable placement anchor and uses one held
  block, wall or placed object to request occupation of a compatible tile-world
  cell or supported footprint.
- Includes: Minecraft Survival placing blocks for shelter, bridges or stairs;
  Terraria placing blocks, background walls, platforms, torches or furniture.
- Excludes: breaking a block; placing a footprint-based factory building;
  unrestricted Creative editing.
- Parameters: projection, layer, target, reach, held tile, support, footprint
  and orientation.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md) and
  [Terraria decomposition](../games/s-z/terraria.md).
- Novelty: not assessed.

## ACT-163 — Throw a held locator item to request a world bearing

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player uses one held consumable locator so it leaves the hand
  and travels in the direction of its current hidden-world target.
- Includes: Minecraft throwing an Eye of Ender to locate the nearest stronghold.
- Excludes: reading a static map; firing a damaging projectile; teleporting to
  the target.
- Parameters: locator item, origin, target class, bearing and recovery chance.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md).
- Novelty: not assessed.

## ACT-164 — Select a carried quick-slot item as the active hand

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one occupied carried quick slot so its item or
  tool becomes the active hand input for the next compatible world action.
- Includes: Minecraft selecting a pickaxe, food, block, Eye or flint and steel
  from the hotbar; Counter-Strike 2 switching among carried weapons, grenades,
  knife and C4; Cyberpunk 2077 weapon-slot switching.
- Excludes: rearranging a crafting recipe; assigning an autonomous worker tool.
- Parameters: slot, item, stack, hand and equipment state.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md) and
  [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Additional support: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md),
  for selecting carried tools, food and fuel from inventory slots.
- Additional support: [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md),
  for switching among the selected class's carried stock weapon slots.
- Additional support: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md),
  for switching among weapon, throwable and medical slots.
- Additional support: [Destiny 2 decomposition](../games/a-f/destiny-2.md),
  for switching among the first, second and Power weapon slots.
- Novelty: not assessed.

## ACT-165 — Consume held food to restore hunger

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player holds the use command on eligible carried food to
  consume one unit and increase the avatar's hunger and saturation state.
- Includes: Minecraft Survival eating food when sufficiently hungry.
- Excludes: using a healing potion; automatically feeding an autonomous agent;
  crafting a food item.
- Parameters: food, use duration, hunger, saturation and status effects.
- Evidence: [Minecraft decomposition](../games/m-r/minecraft.md) and
  [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Novelty: not assessed.

## ACT-166 — Configure a workplace's active shift and unlocked ability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player changes one staffed facility's enabled state, declared
  work-shift mode or law- and technology-unlocked operating ability.
- Includes: Frostpunk turning a workplace on or off, selecting a normal,
  extended or emergency shift, and toggling its heater or Foreman ability.
- Excludes: assigning the workers; selecting a production recipe; changing the
  city-wide simulation speed.
- Parameters: facility, enabled state, shift length, ability, cooldown, resource
  cost and welfare consequence.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## ACT-167 — Sign one available irreversible civic law

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player commits one currently available node in a civic law
  tree, permanently applying its declared rule and branch consequences.
- Includes: Frostpunk Adaptation laws and the mutually exclusive Order or Faith
  Purpose paths.
- Excludes: a reversible district policy; selecting colony research; choosing
  one temporary event response.
- Parameters: law tree, node, prerequisite, exclusive alternative, cooldown,
  immediate modifier, unlocked building or ability and ending judgement.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## ACT-168 — Configure generator and local heat-source operating mode

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player sets the enabled state or output mode of the central
  generator or one local heat source, including a temporary higher-risk mode.
- Includes: Frostpunk generator on/off, power and range, Overdrive, Steam Hub
  schedule and workplace heater controls.
- Excludes: researching a heat upgrade; placing the facility; assigning staff.
- Parameters: source, enabled state, heat level, range, schedule, overdrive and
  transition delay.
- Evidence: [Frostpunk decomposition](../games/a-f/frostpunk.md).
- Novelty: not assessed.

## ACT-169 — Edit a star-orbit swarm or megastructure plan

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player creates or revises a persistent orbital construction
  plan by selecting its star, layer or orbit and placing typed structural
  elements that later launch systems attempt to fulfil.
- Includes: Dyson Sphere Program configuring Dyson Swarm orbits and drawing
  Dyson Sphere layers, nodes, frames and shell regions.
- Excludes: placing one planetary factory building; launching one supplied
  rocket; stamping a surface-factory blueprint.
- Parameters: star, layer radius, orbit inclination and longitude, node, frame,
  shell region, latitude research and plan deletion.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## ACT-170 — Activate mecha flight, sail or warp mode

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player changes the directly controlled mecha from surface
  movement into an unlocked flight regime, or activates consumable warp while
  steering through space.
- Includes: Dyson Sphere Program Icarus takeoff, planetary cruise, interplanetary
  sail and Space-Warper activation.
- Excludes: choosing the destination of an autonomous logistics vessel;
  teleporting between maps; ordinary ground walking.
- Parameters: movement regime, drive level, heading, throttle, core energy,
  warper, cruise altitude and landing state.
- Evidence: [Dyson Sphere Program decomposition](../games/a-f/dyson-sphere-program.md).
- Novelty: not assessed.

## ACT-171 — Author cyclic ship trade route with per-port cargo orders

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player creates or revises a persistent ordered cycle of island
  ports for one or more ships and assigns typed load or unload quantities to
  individual cargo slots at each stop.
- Includes: Anno 1800 trade routes with ordered stations and slot-specific
  loading, unloading and minimum-stock-aware collection.
- Excludes: manually transferring one stack in port; local carts choosing a
  warehouse; drawing a road; a station pair matched automatically by demand.
- Parameters: ships, stop order, cargo slot, good, load or unload quantity,
  minimum stock, wait rule and route activation.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## ACT-172 — Upgrade eligible residence to next population tier

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects a fully eligible residence and pays its
  declared construction materials to convert it into the next population tier.
- Includes: upgrading Anno 1800 Farmers through Workers, Artisans, Engineers
  and Investors when the residence's basic needs and occupancy allow it.
- Excludes: automatically growing occupancy within one tier; placing a new
  house; unlocking the tier's buildings after the population threshold.
- Parameters: source and destination tier, occupancy, fulfilled needs,
  materials, workforce change and multi-upgrade selection.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## ACT-173 — Replace newspaper article with propaganda

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before publication, the player selects a generated newspaper
  article and spends influence to replace it with one available propaganda item.
- Includes: editing an Anno 1800 newspaper issue to change consumption,
  happiness or income until the following issue.
- Excludes: choosing a permanent civic law; changing an article after
  publication; a story dialogue response with no simulation effect.
- Parameters: article slot, replacement tier, influence cost, effect,
  publication time and repeated-propaganda consequence.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## ACT-174 — Provision expedition ship and depart

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player assigns an eligible ship and fills its finite cargo
  slots with goods or specialists whose skills and supplies will be used during
  a declared expedition, then commits departure.
- Includes: preparing Anno 1800's mandatory New World discovery expedition.
- Excludes: authoring a repeating trade route; manually sailing the ship;
  resolving a later expedition event choice.
- Parameters: expedition, ship, cargo slots, item or specialist, skill values,
  rations, morale contribution and departure gate.
- Evidence: [Anno 1800 decomposition](../games/a-f/anno-1800.md).
- Novelty: not assessed.

## ACT-175 — Purchase construction unlock with Science Points

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player spends accumulated settlement Science Points on one
  eligible catalogue entry, making it persistently available in the current map.
- Includes: Timberborn buildings and Earth Recultivator unlocks.
- Excludes: selecting a research target produced afterward; population gates;
  metaprogression retained across fresh maps.
- Parameters: construction, point cost, prerequisite, balance and map scope.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## ACT-176 — Connect and configure local automation signal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player connects a sensor, logic or relay output to a
  compatible target and sets persistent thresholds or Boolean rules.
- Includes: Timberborn sensors controlling pumps, floodgates or valves.
- Excludes: manual toggling; recipe selection; hidden scripts.
- Parameters: source, target, threshold, logic, inversion and signal state.
- Evidence: [Timberborn decomposition](../games/s-z/timberborn.md).
- Novelty: not assessed.

## ACT-177 — Configure an operating office's transport remit

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player assigns sources, destinations, cargo classes,
  thresholds, vehicles or work sites to a persistent office that will dispatch
  eligible vehicles automatically.
- Includes: Workers & Resources construction-office sources and sites, and
  distribution-office supply, demand, resource and storage-percentage rules.
- Excludes: editing one vehicle's ordered line; placing the office; directly
  driving a delivery.
- Parameters: office, source, destination, resource, threshold, fleet, radius,
  priority and assignment mode.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## ACT-178 — Commit a foreign purchase or border trade rule

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player spends the selected foreign currency on an imported
  vehicle or configures an eligible connection to buy or sell a declared flow.
- Includes: purchasing vehicles at Soviet or NATO customs and setting a foreign
  power connection to import or export electricity.
- Excludes: a domestic recipe; cargo crossing customs under an already authored
  vehicle line; an automatic tax settlement.
- Parameters: market bloc, currency, item or power, quantity or limit, price,
  connection and delivery state.
- Evidence: [Workers & Resources: Soviet Republic decomposition](../games/s-z/workers-resources-soviet-republic.md).
- Novelty: not assessed.

## ACT-179 — Commit an island trade or supply contract

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects a disclosed island offer and commits either
  one immediate exchange or a persistent export-for-import contract whose
  later cargo cycles consume the declared institutional resource.
- Includes: Captain of Industry quick trades and village contracts that spend
  Unity and use compatible cargo-depot modules and ships for recurring flows.
- Excludes: domestic production recipes; automatically dispatched island
  trucks; foreign trade settled by a vehicle crossing a land border.
- Parameters: village, reputation, exported product, imported product, ratio,
  establishment cost, recurring Unity cost, module and cargo ship.
- Evidence: [Captain of Industry decomposition](../games/a-f/captain-of-industry.md).
- Novelty: not assessed.

## ACT-180 — Configure and dispatch a Mars rocket manifest

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player assigns an eligible rocket a destination and finite
  payload of resources, prefabs, vehicles or colonists, then commits its launch
  or landing while the resulting flight resolves autonomously.
- Includes: Surviving Mars: Relaunched cargo, passenger, Earth-return and
  planetary-project manifests in patch 1.0.7.
- Excludes: editing a cyclic trade route; directly steering a spacecraft;
  launching one fixed-payload factory rocket.
- Parameters: rocket, origin, destination, cargo capacity, resource, prefab,
  vehicle, passenger, fuel, landing site and automation mode.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## ACT-181 — Prepare, negotiate and vote on a Martian law

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects an eligible law or one of its bounded rule
  options, prepares it, may exchange disclosed promises for faction support,
  and calls the vote that accepts or rejects the proposed colony rule.
- Includes: Surviving Mars: Relaunched Earth Council and Martian Assembly laws,
  including the declaration of independence.
- Excludes: permanently signing a no-vote law branch; selecting research;
  choosing a one-off narrative response.
- Parameters: chamber, law, option, preparation, faction, promise, seats,
  support, vote, upkeep, enactment and repeal eligibility.
- Evidence: [Surviving Mars: Relaunched decomposition](../games/s-z/surviving-mars.md).
- Novelty: not assessed.

## ACT-182 — Purchase one offered round item

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `ACT-130`.
- Includes: historical references that used `ACT-182` before registry
  normalisation 006.
- Excludes: new game signatures; use `ACT-130` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md).
- Merged into: `ACT-130` by
  [`TAXONOMY_CHANGE_012`](../../research/taxonomy-changes/TAXONOMY_CHANGE_012.md).

## ACT-183 — Reload the active magazine-fed weapon

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player commits a timed transfer of reserve ammunition into
  the active weapon, temporarily giving up fire readiness to restore its magazine.
- Includes: Counter-Strike 2 and Cyberpunk 2077 manual firearm reloads.
- Excludes: automatically replenishing ammunition between attempts; changing
  weapons; firing a chambered shot.
- Parameters: weapon, magazine, reserve, reload duration and cancellation rule.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md) and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
- Additional support: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md),
  for reloading carried firearms during the Hotel route.
- Additional support: [Destiny 2 decomposition](../games/a-f/destiny-2.md),
  for reloading magazine-fed weapons during the Fireteam Op.
- Novelty: not assessed.

## ACT-184 — Prime and throw one carried tactical grenade

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects a carried single-use grenade, chooses its
  release direction and strength, and commits it to a ballistic world path.
- Includes: Counter-Strike 2 smoke, flashbang, explosive and incendiary throws.
- Excludes: a fixed launcher shot; placing a persistent trap; ordinary firearm fire.
- Parameters: grenade type, throw mode, aim, velocity, fuse and retained count.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md).
- Additional support: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md),
  for throwing an eligible pipe bomb, Molotov or bile jar.
- Novelty: not assessed.

## ACT-185 — Commit a planted round-device activation or neutralisation channel

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: an eligible player holds the objective interaction continuously
  for its declared duration to activate a carried round device at a valid site
  or neutralise the active planted device.
- Includes: Counter-Strike 2 C4 planting/defusing and Rainbow Six Siege defuser
  planting/disabling.
- Excludes: an instantaneous switch; damaging the device; a scripted cutscene.
- Parameters: role, device, device state, site, duration, kit and interruption.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md)
  and [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Novelty: not assessed.

## ACT-186 — Drop one carried round item into the world

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player removes one eligible carried weapon or objective item
  from personal inventory and emits it at the current world position for
  possible teammate or opponent pickup.
- Includes: Counter-Strike 2 weapon and C4 drops used for team redistribution.
- Excludes: discarding spent magazines; consuming a grenade; selling an item.
- Parameters: item class, throw impulse, ownership, pickup delay and capacity.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md).
- Novelty: not assessed.

## ACT-187 — Communicate a live tactical cue to teammates

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a player deliberately transmits a current position, observation,
  warning or plan through the bounded team communication channel while the
  shared real-time contest continues.
- Includes: Counter-Strike 2 team voice, text and radio cues, and Dota 2 team
  chat, pings and drawings about enemies, cooldowns, movement and objectives;
  Marvel Rivals team voice, text, ping and quick-wheel cues.
- Excludes: the complementary rule/live-state split of `ACT-099`; communication
  outside the game with no bounded team channel; automatic system callouts.
- Parameters: channel, living/dead state, cue form, recipients and delay.
- Evidence: [Counter-Strike 2 decomposition](../games/a-f/counter-strike-2.md)
  [Dota 2 decomposition](../games/a-f/dota-2.md), and
  [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md), and
  [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
- Novelty: not assessed.

## ACT-188 — Commit one match hero and build option

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during bounded team selection, the player commits one available
  match character and any disclosed pre-match or later gated build branch to
  the current slot.
- Includes: Dota 2 All Pick hero and facet selection; Apex Legends Legend
  selection followed by match-local perk choices; Rainbow Six Siege operator
  selection and round loadout commitment.
- Excludes: cosmetic loadout; changing to another hero during live play.
- Parameters: roster, team slot, pick phase, character, build branch, timing and
  conflict rule.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md),
  [Apex Legends decomposition](../games/a-f/apex-legends.md) and
  [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Novelty: not assessed.

## ACT-189 — Issue a contextual destination or attack command

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player addresses a controlled agent and commits a world
  destination, target or attack-move order that autonomous pathing then executes.
- Includes: Dota 2 hero move, attack, attack-move, stop and hold commands.
- Excludes: direct per-step avatar locomotion; an ability cast; lane-creep AI.
- Parameters: selected unit, order, point, target, path and queue modifier.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md) and
  [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
- Novelty: not assessed.

## ACT-190 — Cast one hero or item ability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player activates one learned hero skill or carried item
  active and supplies its legal unit, point, vector or no-target input.
- Includes: Dota 2 spells, toggles and active items; Marvel Rivals hero
  abilities and ultimate activations; Battlefield 6 targeted, placed and
  no-target class gadgets; Hollow Knight: Silksong Silk Skills and equipped
  Tools activated with their legal directional or no-target input; throwing a
  keyed Helldivers 2 stratagem beacon at its legal world target.
- Excludes: automatic attack acquisition; passive effects; cosmetic emotes.
- Parameters: ability, cast form, target, range, mana, cooldown and channel.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md) and
  [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md), and
  [Battlefield 6 decomposition](../games/a-f/battlefield-6.md), and
  [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md), and
  [Helldivers 2 decomposition](../games/g-l/helldivers-2.md), and
  [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md), and
  [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
- Additional support: [Destiny 2 decomposition](../games/a-f/destiny-2.md),
  for fixed Titan grenade, melee, class and Super ability activations.
- Novelty: not assessed.

## ACT-191 — Spend one character-development point

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player spends one currently available match-local or persistent character-development point on an eligible ability rank, attribute, talent or skill-tree node.
- Includes: Dota 2 ability and talent choices; Clair Obscur, Cyberpunk 2077 and Baldur's Gate 3 build allocation; ARC Raiders skill-tree allocation; Black Myth: Wukong Spark allocation.
- Excludes: purchasing an item; automatic level rewards; account-wide cosmetic progression.
- Parameters: point source, persistence horizon, tree, prerequisite, node, rank and resulting modifier.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md), [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md), [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), [Baldur's Gate 3 decomposition](../games/a-f/baldurs-gate-3.md), [ARC Raiders decomposition](../games/a-f/arc-raiders.md) and [Black Myth: Wukong decomposition](../games/a-f/black-myth-wukong.md).
- Novelty: not assessed.

## ACT-192 — Configure a stash or courier delivery

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player transfers eligible match items among hero, stash and
  team courier or commands the courier to collect and deliver them.
- Includes: Dota 2 stash retrieval and courier delivery.
- Excludes: buying the item; dropping it for ground pickup; direct hero movement.
- Parameters: item, source, destination, courier, route and capacity.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md).
- Novelty: not assessed.

## ACT-193 — Purchase immediate hero buyback

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while the controlled hero is dead, the player spends the
  disclosed match cost to replace the remaining respawn wait with immediate return.
- Includes: Dota 2 buyback when cost and cooldown gates are satisfied.
- Excludes: ordinary free respawn; revival by an allied effect; account purchase.
- Parameters: cost, current gold, cooldown, death state and return location.
- Evidence: [Dota 2 decomposition](../games/a-f/dota-2.md).
- Novelty: not assessed.

## ACT-194 — Throw a capture device at one eligible world creature

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player aims and spends one carried capture device on an
  eligible world creature, committing its current probability check rather
  than dealing an ordinary weapon hit.
- Includes: throwing a Pal Sphere at a weakened wild Pal in Palworld; throwing
  a Poké Ball directly or after weakening an eligible wild Pokémon in Pokémon
  Legends: Z-A.
- Excludes: defeating the creature; a guaranteed scripted recruitment; moving
  an already captured companion between rosters.
- Parameters: target, device tier, range, target health, capture power,
  displayed probability and consumed count.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md) and
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Novelty: not assessed.

## ACT-195 — Deploy or recall one carried companion

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one member of the active companion party and
  throws it into a reachable world position or recalls the currently deployed
  companion to carried state.
- Includes: Palworld party-Pal deployment and recall during exploration or
  combat; selecting and deploying the current party partner in Pokémon
  Legends: Z-A.
- Excludes: transferring a Pal into base labour; issuing direct avatar movement;
  capturing a new creature.
- Parameters: party slot, world position, active companion, recall state and
  deployment cooldown.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md) and
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Novelty: not assessed.

## ACT-196 — Transfer a captured companion among bounded rosters

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: through a persistent management fixture, the player moves one
  captured companion between reserve storage, the bounded active party and
  any available ruleset-specific assignment roster.
- Includes: Palbox transfers among Pal storage, party and base assignments;
  Pokémon Legends: Z-A transfers between Boxes and the six-member party.
- Excludes: capturing a wild creature; temporary field deployment; breeding
  two stored creatures.
- Parameters: companion, source roster, destination roster, slot capacity and
  base ownership.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md) and
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Novelty: not assessed.

## ACT-197 — Activate one companion partner skill

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while the required companion and equipment state are available,
  the player invokes its declared partner interaction, mount form or active
  field ability.
- Includes: riding an eligible Pal, using its traversal form or triggering its
  active Partner Skill in Palworld.
- Excludes: the companion's autonomous ordinary attacks; a passive work
  suitability; direct player weapon use.
- Parameters: companion, key item, mount state, stamina, cooldown, target and effect.
- Evidence: [Palworld decomposition](../games/m-r/palworld.md).
- Novelty: not assessed.

## ACT-198 — Commit aircraft exit and steer aerial insertion

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player chooses when to leave a moving insertion aircraft,
  steers the avatar through freefall and canopy flight, and thereby commits to
  one reachable starting region before ordinary ground control begins.
- Includes: PUBG Normal Match aircraft exit, freefall and parachute steering.
- Excludes: choosing a static spawn point; jumping during ground locomotion;
  entering a vehicle after landing.
- Parameters: aircraft line and speed, exit time, fall vector, canopy opening,
  glide, steering, collision and landing region.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md).
- Novelty: not assessed.

## ACT-215 — Configure one bounded compatible combat loadout

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: at an eligible preparation state, the player fills or revises bounded equipment and capability slots for the next controlled deployment or live segment.
- Includes: ARC Raiders raid loadouts, Battlefield 6 class-bound deployment
  loadouts, Hollow Knight: Silksong Crest-and-Tool Bench loadouts,
  Helldivers 2 weapon, armour, booster and four-stratagem deployment choices and
  Rainbow Six Siege operator weapon and secondary-gadget preparation.
- Excludes: cosmetic-only changes; looting after deployment; changing only the active carried slot; selecting a playable hero identity.
- Parameters: preparation state, class or chassis, slot schema, capacity, retained or free inventory, persistence horizon and replacement timing.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md),
  [Battlefield 6 decomposition](../games/a-f/battlefield-6.md),
  [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md) and
  [Helldivers 2 decomposition](../games/g-l/helldivers-2.md),
  [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md) and
  [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Additional support: [Destiny 2 decomposition](../games/a-f/destiny-2.md),
  for the bounded Titan, subclass and three-weapon activity loadout.
- Novelty: not assessed.

## ACT-216 — Search a reachable container or disabled machine

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player commits a proximity-bounded search interaction whose
  completion reveals the eligible contents of one container, wreck or disabled
  machine for subsequent transfer.
- Includes: ARC Raiders lockers, drawers, crates, husks and destroyed ARC
  salvage interactions.
- Excludes: picking up already visible ground loot; remote map revelation;
  automatic resource collection after a kill.
- Parameters: target, reach, interaction duration, interruption, contents,
  prior search state and concurrent access.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## ACT-217 — Move one carried item into or out of a protected pocket

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during a live raid, the player transfers an eligible carried item
  between ordinary backpack storage and a bounded protected pocket whose
  contents use a different defeat-retention rule.
- Includes: ARC Raiders Safe Pocket inventory transfers.
- Excludes: ordinary backpack reordering; banking at successful extraction;
  exploit-based transfer of an ineligible weapon or active gadget.
- Parameters: item, eligibility, source, destination, protected slots, stack,
  active-use state and displacement.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## ACT-218 — Activate and enter a live extraction endpoint

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player reaches an available extraction fixture, starts any
  required call or unlock interaction and enters its bounded departure zone
  before the endpoint closes.
- Includes: ARC Raiders extraction elevators, metro exits and Raider Hatches;
  Helldivers 2 extraction-terminal call and entry into the landed Pelican.
- Excludes: leaving a match through a menu; dying Topside; completing a quest
  without returning to Speranza.
- Parameters: endpoint, availability, key or call, interaction, arrival delay,
  entry zone, closure and damage immunity boundary.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md) and
  [Helldivers 2 decomposition](../games/g-l/helldivers-2.md).
- Novelty: not assessed.

## ACT-219 — Sell or recycle one retained or carried item

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one owned item and irreversibly converts it
  through an available sale or recycling operation into the disclosed coin or
  component return.
- Includes: ARC Raiders Speranza sales and recycling plus Topside Field
  Recycling.
- Excludes: dropping loot for another Raider; consuming a medical item;
  cancelling a craft for a refund.
- Parameters: item, quantity, location, sale value, recycle output, durability,
  confirmation and destination capacity.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Novelty: not assessed.

## ACT-220 — Spend a persistent Raider skill point

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `ACT-191`.
- Includes: historical references that used `ACT-220` before registry
  normalisation 006.
- Excludes: new game signatures; use `ACT-191` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md).
- Merged into: `ACT-191` by
  [`TAXONOMY_CHANGE_012`](../../research/taxonomy-changes/TAXONOMY_CHANGE_012.md).

## ACT-221 — Repair or upgrade one retained weapon

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: in the safe hub, the player selects one retained weapon and pays
  the declared compatible resources to restore durability or advance its
  current upgrade state.
- Includes: ARC Raiders workshop weapon repair and upgrade-with-repair.
- Excludes: field healing; attaching a weapon mod; replacing a broken weapon
  with another stored copy.
- Parameters: weapon, tier, durability, upgrade level, resources, repair amount
  and resulting state.
- Evidence: [ARC Raiders decomposition](../games/a-f/arc-raiders.md) and
  [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## ACT-210 — Configure one survivor's occupation and traits

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before world entry, the player selects one occupation and a
  legal set of positive and negative traits whose combined point balance
  defines the survivor's starting skills and persistent modifiers.
- Includes: Project Zomboid Build 42 occupation and trait creation.
- Excludes: gaining skill experience after spawn; cosmetic appearance; changing
  a world preset.
- Parameters: occupation, traits, point costs, incompatibilities, starting
  skills and persistent modifiers.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## ACT-211 — Apply or remove treatment on a selected body wound

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects a disclosed wound on one body region and uses
  a compatible carried medical item to clean, cover, splint, remove an embedded
  object or otherwise change that wound's treatment state.
- Includes: Project Zomboid Health-panel bandaging and wound care.
- Excludes: consuming food; passive recovery; treating an abstract shared
  health bar with no body location.
- Parameters: body region, wound, item, treatment, duration, skill, pain,
  bleeding and resulting state.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## ACT-212 — Attach or remove defensive material from an opening or surface

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player targets a reachable eligible opening or surface and
  uses compatible material to add one defensive layer or remove one legally
  removable layer from that same target.
- Includes: Project Zomboid plank, metal-sheet and metal-bar barricades; Rainbow
  Six Siege door/window barricades and wall/hatch reinforcements.
- Excludes: constructing a free-standing wall; closing an ordinary curtain;
  damaging an opening in combat.
- Parameters: opening or surface, side, material, layer count, tools, fasteners, skill,
  health, visibility and removal return.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md)
  and [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Novelty: not assessed.

## ACT-213 — Plant, tend or harvest one world crop

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player targets a compatible world plot and commits a carried
  seed, water, treatment or harvesting interaction to one persistent crop.
- Includes: Project Zomboid Build 42 seasonal crop farming.
- Excludes: autonomous colony farming; gathering wild plants; selecting a
  recipe whose output is food.
- Parameters: plot, crop, seed, water, treatment, growth phase, season, skill,
  yield and harvest state.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## ACT-214 — Commit the survivor to sleep

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player uses an eligible resting place to relinquish ordinary
  direct control while personal fatigue and world time advance until waking or
  an allowed interruption.
- Includes: sleeping during a Project Zomboid single-player life.
- Excludes: placing a respawn fixture; pausing the simulation; cosmetic resting
  with no time or fatigue consequence.
- Parameters: resting place, tiredness, safety, sleep duration, time rate,
  interruption, fatigue recovery and wake state.
- Evidence: [Project Zomboid decomposition](../games/m-r/project-zomboid.md).
- Novelty: not assessed.

## ACT-204 — Place, upgrade or repair a connected building block

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player targets a legal socket or existing connected building
  block and spends the selected material to place its initial form, raise its
  construction grade or restore lost structural health.
- Includes: Rust foundations, walls, floors, ceilings and door frames placed
  with the Building Plan and upgraded or repaired with the Hammer.
- Excludes: deploying a free-standing item; blueprint planning for autonomous
  workers; terrain excavation.
- Parameters: block shape, socket, orientation, grade, material cost, stability,
  privilege, repair delay and restored health.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## ACT-205 — Configure authority on a claimed world fixture

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player interacts with a reachable ownership fixture or lock
  to authorise or deauthorise an identity, set or enter an access credential,
  or clear the fixture's current authority list.
- Includes: Rust Tool Cupboard authorisation and Code Lock code entry or change.
- Excludes: opening an already authorised door; transferring stored items;
  server administrator permissions.
- Parameters: fixture, identity, authority list, credential, lock state,
  interaction reach and privilege region.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## ACT-206 — Load and operate a material-processing fixture

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player transfers compatible inputs and any required fuel into
  a reachable processing fixture, starts or stops it where applicable, and
  later removes its produced or residual stacks.
- Includes: loading and lighting a Rust Furnace and transferring components
  through a monument Recycler.
- Excludes: hand-crafting; assigning an autonomous industrial recipe; merely
  storing unchanged items.
- Parameters: fixture, input slots, fuel, active state, cycle, output slots,
  capacity and transfer quantity.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## ACT-207 — Spend research currency to learn one item recipe

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player selects an eligible item at a Research Table or an
  available Workbench tech-tree node and spends the declared research currency
  to add that recipe to personal blueprint knowledge.
- Includes: Rust scrap research and Workbench technology-tree unlocks.
- Excludes: crafting the learned item; discovering a free default recipe;
  upgrading the Workbench itself.
- Parameters: item or node, prerequisite path, workbench tier, scrap cost,
  research item and persistent blueprint state.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## ACT-208 — Place and assign a persistent respawn fixture

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player deploys a legal sleeping fixture in the shared world
  and assigns its future respawn destination to an eligible identity.
- Includes: placing and assigning a Rust Sleeping Bag.
- Excludes: choosing a random beach spawn after death; checkpoint autosave;
  temporary team revival.
- Parameters: fixture, placement, assigned identity, ownership, cooldown group
  and destruction state.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## ACT-209 — Attach a timed explosive to a structure

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player throws or places one carried timed charge onto a
  reachable world surface, committing the charge to its fuse and structural
  blast rather than retaining direct control.
- Includes: deploying a Rust Timed Explosive Charge against a door or building
  block during a raid.
- Excludes: firearm attack; terrain-only excavation; remote administrative
  destruction.
- Parameters: charge, target surface, trajectory, attachment, fuse, blast,
  structural damage and consumed item.
- Evidence: [Rust decomposition](../games/m-r/rust.md).
- Novelty: not assessed.

## ACT-199 — Transfer and equip compatible world loot

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects reachable world loot and transfers it into a
  compatible carried stack, weapon, attachment, protection or storage slot,
  optionally replacing the currently equipped item.
- Includes: PUBG ground-loot interaction and inventory drag/equip actions for
  firearms, ammunition, attachments, armour, backpacks and consumables;
  Cyberpunk 2077 world-loot and inventory equipment transfers.
- Excludes: automatic contact pickup; purchasing a round item; crafting an
  item; collecting an abstract score token.
- Parameters: item, reach, stack, slot, compatibility, capacity, replacement
  disposition and auto-equip setting.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md)
  and [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Additional support: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md),
  for collecting or replacing compatible weapons, ammunition and support items.
- Novelty: not assessed.

## ACT-200 — Use one interruptible restorative consumable

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player begins a timed use of one carried restorative or
  repair item and receives its declared immediate or gradual effect only
  if no cancelling action interrupts the channel.
- Includes: PUBG bandages, First Aid Kits, Med Kits, Energy Drinks, Painkillers
  and Adrenaline Syringes; Black Myth: Wukong finite Gourd sips; NARAKA:
  BLADEPOINT Vitalia, Armor Powder and Weapon Repair Kits.
- Excludes: instant turn-based potion use; passive regeneration without an item;
  reviving another participant.
- Parameters: item, eligible meter or equipment, legal target range, cast time,
  allowed movement, cancelling actions, consumed quantity and effect.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md)
  and [Black Myth: Wukong decomposition](../games/a-f/black-myth-wukong.md).
- Additional support: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md),
  for self-administering first aid and temporary-health items, and
  [NARAKA: BLADEPOINT decomposition](../games/m-r/naraka-bladepoint.md), for
  interruptible Health, armour and weapon-Durability recovery.
- Novelty: not assessed.

## ACT-201 — Enter and directly operate a world vehicle

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player enters an available vehicle seat, directly controls
  its acceleration and steering when occupying the driver position, may switch
  seats, and chooses when to exit into the world.
- Includes: driving or riding Erangel land vehicles in PUBG Normal Match;
  entering, stealing and operating road, water or air vehicles in Grand Theft
  Auto V Story Mode; driving owned or available vehicles in Cyberpunk 2077;
  directly piloting Split Fiction's Chapter 1 escape vehicle while the partner
  occupies the separate turret role.
- Excludes: assigning an autonomous transport route; an insertion aircraft the
  player cannot steer; avatar locomotion on foot.
- Parameters: vehicle, seat, entry reach, driver authority, steering, throttle,
  brake, boost, seat change and exit speed.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md)
  [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md), and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md), and
  [Split Fiction decomposition](../games/s-z/split-fiction.md).
- Novelty: not assessed.

## ACT-202 — Change direct-combat posture or lean

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player changes the controlled avatar among standing,
  crouched, prone or lateral-lean states, altering visible body exposure,
  movement and weapon handling without leaving the current local position.
- Includes: PUBG stance changes and left/right peeking around cover; Cyberpunk
  2077 standing and crouched stealth/combat posture.
- Excludes: ordinary translation through terrain; changing camera perspective;
  an automatic knockback pose.
- Parameters: posture, lean side, transition duration, collision clearance,
  movement rate, exposed hit regions and weapon spread.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md)
  and [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## ACT-203 — Excavate eligible terrain for tactical cover

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player targets supported world terrain with an eligible tool
  or explosive and commits an attack intended to remove bounded ground volume
  and create a traversable depression or cover edge.
- Includes: PUBG Update 41.1 Erangel pickaxe digging and terrain destruction by
  grenades, mortar, Panzerfaust, C4 or vehicle explosion.
- Excludes: damaging a hostile; destroying a building; unlimited voxel mining;
  cosmetic decals with no collision change.
- Parameters: map, surface, tool, strike or blast, range, removed volume, depth,
  collision update and excluded area.
- Evidence: [PUBG: BATTLEGROUNDS decomposition](../games/m-r/pubg-battlegrounds.md).
- Novelty: not assessed.

## ACT-222 — Execute the prompted timing input during a chosen combat action

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after choosing a turn-based attack, skill, heal or buff, the
  player presses or sequences the displayed real-time input while its animation
  is running to modify the declared effect.
- Includes: Clair Obscur: Expedition 33 timed offensive and support prompts.
- Excludes: selecting the command or target; reacting to an enemy attack;
  passive critical-hit probability.
- Parameters: prompt sequence, timing window, success grade and modified clause.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md).
- Novelty: not assessed.

## ACT-223 — Choose a timed dodge, parry or jump response

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during a telegraphed enemy attack, the player commits the
  currently eligible defensive response at a chosen instant inside the live
  attack sequence.
- Includes: Clair Obscur: Expedition 33 dodge, parry and unlocked jump inputs;
  Black Myth: Wukong ordinary and Perfect Dodge timing.
- Excludes: selecting a turn command; passive evasion chance; blocking with a
  persistent armour statistic.
- Parameters: response type, attack member, timing window, affected character
  or party and accessibility assist.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md)
  and [Black Myth: Wukong decomposition](../games/a-f/black-myth-wukong.md).
- Novelty: not assessed.

## ACT-224 — Rest at an expedition checkpoint

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player deliberately rests at an activated campaign
  checkpoint to accept its linked recovery and world-reset consequences.
- Includes: resting at Clair Obscur: Expedition 33 Expedition Flags; resting at
  activated Benches in Hollow Knight: Silksong; resting at an activated Keeper's
  Shrine in Black Myth: Wukong.
- Excludes: touching a checkpoint without resting; using a combat healing item;
  sleeping while an open-world simulation continues.
- Parameters: checkpoint, refill set, revival state, respawn set and save timing.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md),
  [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md) and
  [Black Myth: Wukong decomposition](../games/a-f/black-myth-wukong.md).
- Novelty: not assessed.

## ACT-225 — Configure equipped Pictos and active Luminas

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: outside a locked combat resolution, the player assigns acquired
  Pictos to compatible character slots and activates learned Lumina passives
  within that character's point capacity.
- Includes: Clair Obscur: Expedition 33 per-character Picto and Lumina builds.
- Excludes: equipping a weapon; spending a skill point; the automatic mastery
  that makes a Picto passive available as Lumina.
- Parameters: character, Picto slots, passive identity, Lumina cost, capacity
  and combat-lock state.
- Evidence: [Clair Obscur: Expedition 33 decomposition](../games/a-f/clair-obscur-expedition-33.md).
- Novelty: not assessed.

## ACT-226 — Enter or leave contextual combat cover

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player attaches the controlled protagonist to a reachable
  protective surface, shifts along or around its supported edge and deliberately
  leaves that cover state while direct combat continues.
- Includes: Grand Theft Auto V Story Mode wall, vehicle and low-object cover.
- Excludes: merely crouching in open space; passive armour; cover used only by
  autonomous allies.
- Parameters: surface, reach, edge, posture, blind fire, aimed exposure and exit.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md).
- Novelty: not assessed.

## ACT-227 — Set a personal world-map waypoint

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one reachable map position or known marker as
  a personal destination so the navigation interface can calculate and display
  a road route without moving the protagonist automatically.
- Includes: Grand Theft Auto V Story Mode and Cyberpunk 2077 map waypoints and
  calculated road routes.
- Excludes: directly commanding autonomous traversal; authored mission markers
  the system fixes without player selection; drawing a transport network.
- Parameters: map position, marker, route mode, recalculation and removal.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md) and
  [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## ACT-228 — Switch direct control to an available protagonist

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects another currently available authored
  protagonist and transfers direct movement, combat and interaction authority
  to that character without beginning a separate save or multiplayer session.
- Includes: Grand Theft Auto V Story Mode switching among Michael, Franklin and
  Trevor in free roam and at eligible mission moments.
- Excludes: changing cosmetic avatars; ordering an autonomous squad member;
  selecting a turn-based party member's command.
- Parameters: protagonist, availability, mission permission, transition and
  current world activity.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md).
- Novelty: not assessed.

## ACT-229 — Activate the controlled protagonist's special ability

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player deliberately commits the controlled protagonist's
  ready special resource to enter that character's authored temporary combat
  form or driving modifier.
- Includes: Michael's shooting focus, Franklin's driving focus and Trevor's
  rage ability in Grand Theft Auto V Story Mode; the acquired Red Tides
  transformation in Black Myth: Wukong.
- Excludes: passive statistics; cheat codes; GTA Online Quickplay actions.
- Parameters: protagonist, resource or readiness, context, form, duration,
  drain, cancellation, moveset and mechanical modifiers.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md)
  and [Black Myth: Wukong decomposition](../games/a-f/black-myth-wukong.md).
- Novelty: not assessed.

## ACT-230 — Configure a heist approach and specialist crew

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: at an authored planning board, the player selects one available
  operation approach and assigns eligible specialists to every required crew
  role before preparation or execution begins.
- Includes: Grand Theft Auto V Story Mode approach, gunman, driver and hacker
  choices for its major heists.
- Excludes: moment-to-moment protagonist switching during execution; an online
  lobby; cosmetic crew selection.
- Parameters: heist, approach, required roles, candidate, skill, cut, prior
  survival and commitment point.
- Evidence: [Grand Theft Auto V decomposition](../games/g-l/grand-theft-auto-v.md).
- Novelty: not assessed.

## ACT-231 — Commit lifepath and initial attribute allocation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before entering the persistent campaign, the player selects one
  authored origin and distributes a fixed initial point budget among mechanical
  character attributes that persist into play.
- Includes: Cyberpunk 2077's Nomad, Streetkid or Corpo lifepath selection and
  initial Body, Intelligence, Reflexes, Technical Ability and Cool allocation.
- Excludes: cosmetic appearance; later attribute-point spending; selecting a
  temporary dialogue response.
- Parameters: origin roster, attribute set, base values, point budget, minimum,
  maximum and confirmation boundary.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## ACT-232 — Commit one authored dialogue or quest response

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during an authored conversation or quest decision, the player
  selects one currently offered response whose declared or concealed result may
  update information, relationships, mission state or a later branch.
- Includes: Cyberpunk 2077 dialogue choices, timed responses and the base-game
  decision to accept Hanako's route during Nocturne Op55N1.
- Excludes: optional flavour lines with no state change; buying a catalogue
  item; allocating a character point.
- Parameters: speaker, option set, timer, prerequisite, response, state change,
  reversibility and later branch.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## ACT-233 — Scan a world target and upload one quickhack

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player holds scanner focus on an eligible person, device or
  vehicle, selects one available quickhack and commits its timed upload from the
  installed cyberdeck.
- Includes: Cyberpunk 2077 base-game combat, covert and device quickhacks.
- Excludes: firing a weapon; passively revealing a target; selecting a dialogue
  response; hacking without an installed compatible operating system.
- Parameters: target, scanner range, cyberdeck, quickhack, RAM cost, upload
  time, queue position, cooldown and trace exposure.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## ACT-234 — Configure installed cyberware at a ripperdoc

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: at an eligible specialist interface, the player buys, installs,
  removes, replaces or upgrades one implant in a compatible body slot while
  preserving the resulting capacity-bound loadout.
- Includes: Cyberpunk 2077 Update 2.0+ ripperdoc cyberware configuration.
- Excludes: equipping a carried weapon; cosmetic-only wardrobe changes;
  allocating an attribute or perk point.
- Parameters: slot, implant, tier, price, components, capacity cost, armour,
  attunement, replacement and upgrade result.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## ACT-235 — Grapple and neutralise an unaware reachable target

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: from valid close range outside active detection, the player grabs
  one eligible hostile and commits a lethal or non-lethal neutralisation or
  body movement instead of an ordinary weapon attack.
- Includes: Cyberpunk 2077 stealth grabs, takedowns and short body carries.
- Excludes: melee strikes against an alerted enemy; scripted dialogue custody;
  remotely uploading a quickhack.
- Parameters: target awareness, reach, relative level, grab state, outcome,
  body destination and interruption.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## ACT-236 — Activate one rechargeable combat-item charge

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player activates one currently ready charge of an equipped
  health item or grenade, supplying aim where required, without permanently
  consuming the underlying reusable item.
- Includes: Cyberpunk 2077 Update 2.0+ health-item and grenade charges.
- Excludes: consuming a finite inventory stack; firing a weapon; passive health
  regeneration; using an unavailable recharging charge.
- Parameters: item, charge count, aim, activation duration, effect, recharge
  delay and interruption.
- Evidence: [Cyberpunk 2077 decomposition](../games/a-f/cyberpunk-2077.md).
- Novelty: not assessed.

## ACT-237 — Select a match hero and Team-Up loadout in spawn

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before leaving an active team spawn room, the player selects one
  currently available hero and one offered Team-Up partner loadout, transferring
  direct control and the resulting base ability configuration to that hero.
- Includes: Marvel Rivals Quick Match hero selection, legal mid-match hero
  swaps in spawn and Season 9 Team-Up partner selection.
- Excludes: a draft that permanently commits one hero for the whole match;
  cosmetic skin selection; copying another hero with an ultimate ability.
- Parameters: team slot, hero, role, uniqueness, spawn state, partner option,
  base effect, enhanced effect and confirmation.
- Evidence: [Marvel Rivals decomposition](../games/m-r/marvel-rivals.md).
- Novelty: not assessed.

## ACT-238 — Configure a persistent custom campaign character

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before entering a persistent authored campaign, the player
  commits one compatible set of lineage, class, background, ability allocation
  and proficiencies that determines the new character's starting capabilities.
- Includes: Baldur's Gate 3 custom Tav race or subrace, class, background,
  27-point ability allocation, skill proficiencies and starting choices.
- Excludes: cosmetic appearance; selecting a fixed Origin character; later
  levelling, multiclassing or equipment changes.
- Parameters: lineage, class, background, ability budget, proficiency, cantrip,
  spell, compatibility and confirmation boundary.
- Evidence: [Baldur's Gate 3 decomposition](../games/a-f/baldurs-gate-3.md).
- Novelty: not assessed.

## ACT-239 — Configure one class-bound deployment loadout

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `ACT-215`.
- Includes: historical references that used `ACT-239` before registry
  normalisation 006.
- Excludes: new game signatures; use `ACT-215` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Battlefield 6 decomposition](../games/a-f/battlefield-6.md).
- Merged into: `ACT-215` by
  [`TAXONOMY_CHANGE_012`](../../research/taxonomy-changes/TAXONOMY_CHANGE_012.md).

## ACT-240 — Select a legal team deployment source and redeploy

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while direct combatant control is unavailable, the player
  selects one currently legal team source on the deployment interface and
  commits the configured combatant to enter the live match there.
- Includes: Battlefield 6 Conquest deployment at headquarters, a held point,
  eligible squadmate, Deploy Beacon or compatible vehicle seat.
- Excludes: walking from an existing position; automatic checkpoint respawn;
  placing the spawn source itself.
- Parameters: source class, ownership, safety, combat state, seat, timer,
  loadout and entry position.
- Evidence: [Battlefield 6 decomposition](../games/a-f/battlefield-6.md).
- Novelty: not assessed.

## ACT-241 — Revive or reposition one eligible downed ally

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player addresses one reachable downed ally, optionally
  repositions that body where the rules allow it and commits the required
  revival channel or instant tool before the downed opportunity expires.
- Includes: Battlefield 6 squad revival, drag-to-cover and Defibrillator
  completion; Apex Legends teammate revival from knocked state; Rainbow Six
  Siege teammate revival from an eligible injured state.
- Excludes: self-healing; ordinary post-death redeployment; carrying an
  objective item; resurrecting a character after a campaign death.
- Parameters: ally relation, reach, posture, movement, revive authority,
  duration, interruption, tool and returned health.
- Evidence: [Battlefield 6 decomposition](../games/a-f/battlefield-6.md),
  [Apex Legends decomposition](../games/a-f/apex-legends.md) and
  [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Additional support: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md),
  for reviving a reachable incapacitated Survivor before bleed-out.
- Novelty: not assessed.

## ACT-242 — Configure a Crest-bound tool loadout at a bench

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `ACT-215`.
- Includes: historical references that used `ACT-242` before registry
  normalisation 006.
- Excludes: new game signatures; use `ACT-215` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Hollow Knight: Silksong decomposition](../games/g-l/hollow-knight-silksong.md).
- Merged into: `ACT-215` by
  [`TAXONOMY_CHANGE_012`](../../research/taxonomy-changes/TAXONOMY_CHANGE_012.md).

## ACT-243 — Call and ride a target-routed field mount

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player calls, mounts or dismounts a persistent field mount
  and may commit one currently tracked destination for its autonomous travel
  while retaining manual steering.
- Includes: calling and riding the Monster Hunter Wilds Seikret toward an
  assignment target, map marker or tracked monster.
- Excludes: direct hunter locomotion; a non-interactive fast-travel jump; an
  autonomous companion with no ride state.
- Parameters: mount, call range, mount state, selected target, automatic route,
  manual deviation and dismount.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## ACT-244 — Exchange active and mount-carried weapons

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while riding the eligible mount, the player swaps the currently
  active weapon with exactly one secondary weapon assigned to the mount.
- Includes: Monster Hunter Wilds Seikret weapon switching.
- Excludes: selecting any weapon from camp storage; reloading ammunition;
  changing a cosmetic weapon layer.
- Parameters: active weapon, secondary weapon, mounted state, compatibility,
  exchange animation and resulting equipment state.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## ACT-245 — Gather or carve one reachable material yield

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player interacts with one reachable eligible field source or
  defeated body to extract one finite material yield into carried inventory.
- Includes: gathering a Monster Hunter Wilds plant, ore or bone source and
  carving a defeated large monster during its eligible window.
- Excludes: automatic contact pickup; quest rewards delivered without a world
  interaction; destroying terrain for a drop.
- Parameters: source, body point, reach, remaining yields, result table,
  inventory capacity and interaction window.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md)
  and [Monster Hunter: World decomposition](../games/m-r/monster-hunter-world.md).
- Novelty: not assessed.

## ACT-246 — Aim and commit a weapon-specific Focus Strike

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: in Focus Mode, the player aligns the current weapon with one
  highlighted compatible body state and commits that weapon's Focus Strike.
- Includes: Monster Hunter Wilds Focus Strikes aimed at an open wound or
  compatible breakable monster part.
- Excludes: ordinary repeated attacks; passive wound highlighting; a Focus
  Strike that lacks a legal reachable body state.
- Parameters: weapon, focus state, body part, wound, reach, aim, attack form and
  animation commitment.
- Evidence: [Monster Hunter Wilds decomposition](../games/m-r/monster-hunter-wilds.md).
- Novelty: not assessed.

## ACT-247 — Call and directly steer a spectral field mount

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player calls an unlocked personal mount, enters or leaves its
  saddle and directly steers its ground movement, jumps and mounted attacks.
- Includes: calling and riding Torrent in scoped Elden Ring Limgrave.
- Excludes: target-routed Seikret travel; autonomous vehicles; fast travel.
- Parameters: mount availability, call state, direction, jump, attack and health.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## ACT-248 — Purchase one chosen attribute level with runes

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: at an eligible checkpoint the player selects one character
  attribute and commits the displayed rune price to raise it by one level.
- Includes: levelling Vigor, Mind or another attribute at Elden Ring Grace.
- Excludes: automatic experience levelling; perk purchase; weapon upgrading.
- Parameters: attribute, current value, character level, price and rune stock.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## ACT-249 — Recover the active dropped-rune mark

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player reaches and touches the currently active death mark to
  transfer its retained rune stock back to the living character.
- Includes: reclaiming Elden Ring runes before another death replaces the mark.
- Excludes: ordinary loot pickup; corpse inventory; Cocoon resource recovery.
- Parameters: mark position, retained runes, current life and replacement state.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## ACT-250 — Summon one equipped Spirit Ash group

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player spends the declared resource in an eligible monument
  zone to instantiate one equipped autonomous spirit group.
- Includes: Elden Ring early Spirit Ash use in eligible field and boss areas.
- Excludes: online allies; NPC summon signs; directly commanded companions.
- Parameters: ash, FP or HP cost, monument range, concurrent summon and arena.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## ACT-251 — Assign an Ash of War and affinity to an armament

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: from an eligible menu the player selects a compatible acquired
  Ash of War and one available affinity for a retained armament.
- Includes: early Elden Ring Whetstone Knife armament configuration.
- Excludes: executing the skill; upgrading reinforcement level; equipping magic.
- Parameters: armament class, ash compatibility, affinity unlock and replacement.
- Evidence: [Elden Ring decomposition](../games/a-f/elden-ring.md).
- Novelty: not assessed.

## ACT-252 — Craft one currently offered station recipe

- Lifecycle: `Merged`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: historical game-specific duplicate now represented by the
  parameterised active boundary `ACT-123`.
- Includes: historical references that used `ACT-252` before registry
  normalisation 006.
- Excludes: new game signatures; use `ACT-123` with the scoped parameters and
  any retained companion Constraints or System behaviours.
- Parameters: none; preserved as a lifecycle alias.
- Evidence: [Terraria decomposition](../games/s-z/terraria.md).
- Merged into: `ACT-123` by
  [`TAXONOMY_CHANGE_012`](../../research/taxonomy-changes/TAXONOMY_CHANGE_012.md).

## ACT-253 — Commit a surviving squadmate to one teammate-return source

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while at least one squadmate remains active, the player commits
  an eligible dead teammate's current recovery object or state to one legal
  return source that can restore that teammate to the live match.
- Includes: using an Apex Legends deathbox return or carrying or crafting a
  Legend Banner and activating an eligible Respawn Beacon; a surviving
  Helldivers 2 squadmate keying and throwing Reinforce for a dead teammate.
- Excludes: reviving a merely downed ally; automatic round respawn; selecting a
  fresh class after ordinary death; account-level resurrection.
- Parameters: teammate state, recovery object, carrier, source, reach, channel,
  interruption, lockout and returned equipment state.
- Evidence: [Apex Legends decomposition](../games/a-f/apex-legends.md) and
  [Helldivers 2 decomposition](../games/g-l/helldivers-2.md).
- Novelty: not assessed.

## ACT-254 — Choose one mandatory Ancient boon at act entry

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before an act route begins, the player selects exactly one item
  from the current Ancient's bounded offered set, committing its persistent
  run effect before progression may continue.
- Includes: choosing one of three offered Ancient Relics at the beginning of a
  Slay the Spire 2 act.
- Excludes: optional post-combat card rewards; buying a priced item; a passive
  automatic milestone unlock; the random selection of which Ancient appears.
- Parameters: act, Ancient, unlocked pool, offered items, eligibility, selected
  boon, skip permission and persistent effect.
- Evidence: [Slay the Spire 2 decomposition](../games/s-z/slay-the-spire-2.md).
- Novelty: not assessed.

## ACT-255 — Trace and submit an adjacent letter-cell word

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player begins on any eligible letter cell, traces one
  variable-length ordered sequence through successively adjacent distinct
  letter cells and submits the resulting word as one compound proposal.
- Includes: tracing and submitting a Strands theme word, spangram or eligible
  non-theme word through horizontal, vertical or diagonal neighbours.
- Excludes: typing a word without selecting its spatial route; tracing from a
  fixed endpoint; selecting disconnected letters; merely highlighting a
  system-revealed route.
- Parameters: adjacency topology, minimum length, gesture sampling, direction
  changes, backtracking, submission trigger and already-claimed-cell policy.
- Evidence: [Strands decomposition](../games/s-z/strands.md).
- Novelty: not assessed.

## ACT-256 — Commit one half of a paired cooperative interaction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: one human-controlled actor commits its locally eligible input to
  a world interaction whose progress depends on a separately controlled
  partner committing the complementary input rather than on one actor
  repeating both steps.
- Includes: one Split Fiction player operating one side of a simultaneous
  console, paired handle, dual plate or joint door interaction while the other
  player supplies the other required input.
- Excludes: one avatar toggling an ordinary switch; an autonomous follower
  satisfying the second input; two players independently attacking one target;
  holding a mechanism that has already opened a solo route.
- Parameters: actor identities, input prompts, simultaneity tolerance,
  eligibility, persistence before the second input and cancellation rule.
- Evidence: [Split Fiction decomposition](../games/s-z/split-fiction.md).
- Novelty: not assessed.

## ACT-257 — Direct an active resident to a contextual interaction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects an active persistent resident, addresses an
  eligible resident, object or ground context and commits one offered social,
  self-care or world interaction for autonomous execution.
- Includes: directing Farrah Nouvel to introduce herself, chat, invite a Sim,
  use a household object or perform another offered base-game interaction in
  The Sims 4.
- Excludes: directly steering every locomotion step; setting a colony-wide job
  priority; choosing an authored dialogue line with no simulated actor state.
- Parameters: active resident, target, interaction category, queue position,
  cancellation, autonomy rule and execution prerequisites.
- Evidence: [The Sims 4 decomposition](../games/s-z/the-sims-4.md).
- Novelty: not assessed.

## ACT-258 — Switch the active battle companion from the bounded party

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during live battle, the player selects one other eligible living
  party member so it replaces the current sole commanded companion while both
  retain their own persistent health, status, level and learned moves.
- Includes: voluntary or knockout-forced partner replacement in Pokémon
  Legends: Z-A.
- Excludes: moving a companion between storage and party; recalling without a
  replacement; switching direct control between human protagonists.
- Parameters: party slots, current and replacement companion, health, status,
  switch delay and voluntary or forced trigger.
- Evidence: [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Novelty: not assessed.

## ACT-259 — Choose one persistent starting companion

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: at campaign entry, the player accepts exactly one member of a
  bounded offered roster so that identity and its initial kit become a
  persistent owned party member.
- Includes: choosing Chikorita, Tepig or Totodile as the first partner in
  Pokémon Legends: Z-A.
- Excludes: selecting a match-only hero; choosing a cosmetic; capturing a later
  world creature.
- Parameters: offered roster, selected identity, initial level, initial moves,
  ownership persistence and decline permission.
- Evidence: [Pokémon Legends: Z-A decomposition](../games/m-r/pokemon-legends-z-a.md).
- Novelty: not assessed.

## ACT-260 — Commit one reachable Survivor interaction channel

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a directly controlled Survivor holds one contextual interaction
  against a reachable objective or teammate so progress accumulates only while
  the actor remains eligible and the channel continues.
- Includes: Dead by Daylight Generator repair, altruistic healing, Dying-state
  recovery by another Survivor, teammate unhooking and powered Exit Gate switch
  work in the scoped blank-loadout Trial.
- Excludes: walking or vaulting; one instantaneous switch press; the Killer's
  pickup, carry or damage interactions; an autonomous worker order.
- Parameters: target class, reach, actor state, duration, saved or reset
  progress, co-worker count, interruption and completion effect.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Additional support: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md),
  for channelled first-aid-kit use on a living teammate.
- Novelty: not assessed.

## ACT-261 — Execute one prompted skilful timing input

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during an eligible continuing world interaction, the player
  commits one response while a moving pointer overlaps a disclosed success
  interval, producing a graded timing result without selecting a new target.
- Includes: Dead by Daylight Good, Great and failed Skill Check responses during
  Generator repair or altruistic healing.
- Excludes: timed defence inside a chosen combat action; rhythm sequences whose
  notes are the complete objective; passive random resolution with no input.
- Parameters: trigger chance, warning, pointer direction and speed, zone
  position, good and great intervals, response input and missed-input rule.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Novelty: not assessed.

## ACT-262 — Drop one upright chase pallet

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: a directly controlled fleeing actor commits one reachable
  upright Pallet into its dropped state, creating a persistent local obstacle
  and an impact interval rather than merely vaulting existing geometry.
- Includes: a Survivor dropping an upright Pallet during a Dead by Daylight
  chase, with or without stunning the Killer.
- Excludes: vaulting a dropped Pallet; the Killer breaking it; placing a carried
  construction piece; toggling a reusable door switch.
- Parameters: pallet, reach, facing, drop animation, impact volume, stun target,
  resulting collision and later destruction.
- Evidence: [Dead by Daylight decomposition](../games/a-f/dead-by-daylight.md).
- Novelty: not assessed.

## ACT-263 — Engrave one Uncut Gem into a selected skill or support

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player commits one carried Uncut Gem to one eligible offered
  active Skill or Support identity, consuming the uncut item and creating the
  selected usable Gem.
- Includes: Path of Exile 2 Uncut Skill Gem and Uncut Support Gem engraving.
- Excludes: socketing an already created Support; random item identification;
  learning a skill automatically at level-up.
- Parameters: uncut kind and level, offered catalogue, selected identity,
  requirement preview, created Gem and cancellation.
- Evidence: [Path of Exile 2 decomposition](../games/m-r/path-of-exile-2.md).
- Novelty: not assessed.

## ACT-264 — Socket or remove one compatible support from an active skill

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player transfers one carried Support Gem into a free legal
  socket of one selected active Skill, or removes it, changing that Skill's
  composed behaviour while preserving both Gem identities.
- Includes: Path of Exile 2 Skill-panel Support socket management.
- Excludes: engraving the Support; equipping armour; permanently upgrading a
  skill node.
- Parameters: Skill, Support, socket, compatibility, category, attributes,
  insertion, removal and resulting cost/effect.
- Evidence: [Path of Exile 2 decomposition](../games/m-r/path-of-exile-2.md).
- Novelty: not assessed.

## ACT-265 — Apply one crafting currency item to an eligible item

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one carried crafting currency and commits it
  to one eligible target item, consuming the currency to request its declared
  rarity, affix or socket transformation.
- Includes: one ordinary Path of Exile 2 currency-item craft.
- Excludes: vendor purchase; equipment swapping; a multi-step external crafting
  calculator.
- Parameters: currency class, target item and state, eligibility preview,
  consumption, mutation class and resulting item.
- Evidence: [Path of Exile 2 decomposition](../games/m-r/path-of-exile-2.md).
- Novelty: not assessed.

## ACT-266 — Activate one charged recovery flask

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during eligible direct control, the player activates an equipped
  Life or Mana Flask, immediately consuming its declared charges and beginning
  the recovery effect without consuming the flask item itself.
- Includes: Path of Exile 2 Life and Mana Flask use in campaign combat.
- Excludes: an interruptible carried-food channel; passive regeneration; a
  single-use potion removed from inventory.
- Parameters: flask slot, resource class, charges, recovery amount and duration,
  modifiers and use restrictions.
- Evidence: [Path of Exile 2 decomposition](../games/m-r/path-of-exile-2.md).
- Novelty: not assessed.

## ACT-267 — Direct a ball delivery toward an eligible teammate

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while directly controlling the current ball carrier, the player
  commits a grounded, lofted or crossed delivery whose intended receiver and
  trajectory are resolved from directional, power and contextual input.
- Includes: short and driven passes, through balls, lofted passes and crosses
  in an EA SPORTS FC 26 association-football match.
- Excludes: striking primarily at the opponent's goal; an AI teammate's
  uncommanded clearance; selecting a remote movement destination.
- Parameters: delivery family, direction, power, assistance, intended receiver,
  body orientation, dominant foot and contextual animation.
- Evidence: [EA SPORTS FC 26 decomposition](../games/a-f/ea-sports-fc-26.md).
- Novelty: first isolated for `GAME-0163`; no earlier active action boundary
  expresses teammate-targeted transfer of one live shared ball.

## ACT-268 — Direct an attempt at the opponent's goal

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while controlling an eligible attacker, the player commits a
  shot intended to send the live ball across the opponent's goal line.
- Includes: ordinary, finesse, chipped and headed attempts in the scoped EA
  SPORTS FC 26 match.
- Excludes: teammate-targeted passing; a penalty shoot-out selection; an
  autonomous goalkeeper clearance.
- Parameters: direction, power, shot family, assistance, body orientation,
  contact type and player attributes.
- Evidence: [EA SPORTS FC 26 decomposition](../games/a-f/ea-sports-fc-26.md).
- Novelty: first isolated for `GAME-0163`.

## ACT-269 — Commit a legal possession challenge

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while directly controlling an eligible defender, the player
  commits a standing, shoulder or sliding challenge intended to dislodge or
  intercept the opponent's live ball without first taking direct control of it.
- Includes: timing a standing tackle or slide against the current ball carrier
  in EA SPORTS FC 26.
- Excludes: automatic off-ball marking; simply running into space; hostile
  combat whose outcome is health depletion.
- Parameters: challenge family, direction, timing, contact geometry, defender
  attributes and foul risk.
- Evidence: [EA SPORTS FC 26 decomposition](../games/a-f/ea-sports-fc-26.md).
- Novelty: first isolated for `GAME-0163`.

## ACT-270 — Place one carried bomb with a timed fuse

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player spends one bomb from the current run supply and places
  a live explosive at Isaac's position, starting its fuse before blast resolution.
- Includes: placing a standard bomb for hostile damage, rock destruction or an
  eligible secret-room wall in base The Binding of Isaac: Rebirth.
- Excludes: throwing a tactical grenade; firing an explosive projectile; an
  automatic item-triggered explosion that spends no carried bomb.
- Parameters: carried count, placement point, fuse, kick or displacement,
  blast radius and modifiers.
- Evidence: [The Binding of Isaac: Rebirth decomposition](../games/s-z/the-binding-of-isaac-rebirth.md).
- Novelty: first isolated for `GAME-0164`; no earlier action boundary couples
  finite carried supply to a freely placed room-scale timed blast.

## ACT-271 — Call, mount and directly ride a persistent horse

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player calls an owned horse, mounts or dismounts it and
  directly controls its pace, steering, jump and stop while the same horse
  retains its condition and carried saddle state.
- Includes: calling and riding Arthur Morgan's current saddled horse during the
  scoped Red Dead Redemption 2 Chapter 2 route.
- Excludes: steering a road vehicle; target-routed automatic mount travel; a
  spectral mount freely resummoned after defeat; fast travel.
- Parameters: horse identity, call range, saddle, gait, direction, jump,
  dismount, health, stamina and temporary-horse state.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`; earlier mount actions either route
  automatically or concern a resummonable supernatural steed.

## ACT-272 — Clean one owned firearm with gun oil

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player inspects one owned firearm and consumes one available
  unit of gun oil to restore its current condition before returning it to use.
- Includes: field-cleaning a dirty Chapter 2 firearm from the Red Dead
  Redemption 2 weapon interface.
- Excludes: reloading ammunition; buying a gunsmith cleaning service; repairing
  a retained weapon at a safe-hub workbench; attaching a cosmetic component.
- Parameters: weapon, current condition, oil count, cleaning duration,
  interruption and restored condition.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`; `ACT-221` is a hub repair or upgrade,
  not carried-consumable maintenance in the field.

## ACT-273 — Donate eligible value to the shared gang camp

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects personal money or an eligible carried valuable,
  provision or carcass and commits it to the gang camp's shared funds or supply
  state, permanently removing the donated value from personal possession.
- Includes: the Horseshoe Overlook donation box and eligible meat or carcasses
  given to Pearson during Chapter 2.
- Excludes: purchasing a ledger upgrade from shared funds; selling to a merchant
  for personal cash; a cosmetic gift with no camp state change.
- Parameters: recipient, item or money class, amount, personal source, shared
  destination, camp supply category and honour effect.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`; earlier contribution genes fill
  fixed authored collection slots rather than an open operating reserve.

## ACT-274 — Choose one contextual ambient social response

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while focused on a live nearby person, the player chooses one
  currently offered contextual response such as greet, antagonise, calm,
  threaten or surrender, allowing that person's state to determine the reply.
- Includes: greeting or antagonising civilians, trying to stop a witness and
  surrendering to lawmen in scoped Red Dead Redemption 2 Story Mode.
- Excludes: selecting a fixed authored quest branch; attacking with the current
  weapon; passive dialogue heard without a player response.
- Parameters: target, awareness, distance, role, response set, repetition,
  weapon posture and resulting disposition.
- Evidence: [Red Dead Redemption 2 decomposition](../games/m-r/red-dead-redemption-2.md).
- Novelty: first isolated for `GAME-0165`; earlier dialogue actions commit
  authored narrative options rather than a live systemic social verb.

## ACT-275 — Choose one city's production target

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player selects one currently legal unit, building, district,
  wonder or project as the single target that a city will advance with its
  accumulated production until completion or replacement.
- Includes: choosing a Settler, Campus or Spaceport project in the scoped
  Civilization VI game.
- Excludes: buying the target immediately with Gold; assigning a worked tile;
  an unrestricted multi-item automation queue.
- Parameters: city, target class, cost, progress, prerequisites, replacement
  and completion effect.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`; earlier construction actions place
  footprints or order work but do not select a city's one accumulating output.

## ACT-276 — Choose the active civic research target

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player chooses one unlocked Civic as the current destination
  for empire Culture, replacing or continuing the prior target while retaining
  its stored progress.
- Includes: selecting Political Philosophy or Space Race in base Civilization VI.
- Excludes: selecting a Technology funded by Science; equipping a policy card;
  accepting a narrative dialogue branch.
- Parameters: civic, prerequisites, stored progress, culture cost, boost and unlocks.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`; it is the Culture-funded parallel
  dependency choice beside existing Technology selection.

## ACT-277 — Assign one citizen to a worked tile or specialist slot

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player moves one available city citizen between eligible
  worked territory, a district specialist slot or unemployment, changing which
  yields that finite population member contributes.
- Includes: prioritising a farm, mine or Campus specialist in Civilization VI.
- Excludes: placing a district; moving a military unit; changing a whole city's
  cosmetic population model.
- Parameters: city, citizen, source, destination, ownership, work eligibility
  and resulting yields.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`; earlier worker allocation concerns
  abstract jobs rather than individually reassigned map tiles and specialists.

## ACT-278 — Select a government and fill its policy slots

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player adopts an unlocked government and assigns compatible
  policy cards to its typed military, economic, diplomatic and wildcard slots.
- Includes: adopting Classical Republic and configuring available base-game cards.
- Excludes: choosing the active Civic; appointing an expansion Governor;
  setting a purely cosmetic national label.
- Parameters: government, unlocked cards, slot types, assignments, change cost
  and active effects.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`; earlier loadouts do not combine a
  regime-defined typed slot frame with swappable empire rules.

## ACT-279 — Establish a trade route to an eligible destination

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player assigns an available trader to one eligible origin and
  destination, committing the unit to the displayed route and per-turn yields.
- Includes: a domestic route between the two scoped Roman cities or an
  international route to a contacted rival.
- Excludes: a one-off diplomatic resource deal; manually steering a unit one
  hex at a time; passively receiving city income.
- Parameters: trader, origin, destination, capacity, reach, duration, yields,
  road and trading-post effects.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`; existing logistics actions route
  cargo directly rather than commit an autonomous yield-and-road mission.

## ACT-280 — Commit a civilization-level diplomatic action

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after contact, the player proposes, accepts, rejects or counters
  an eligible deal, relationship, declaration of war or peace agreement with
  one civilization.
- Includes: exchanging Gold/resources, declaring war and negotiating peace in
  the scoped Civilization VI game.
- Excludes: tactical unit attack; a city-state envoy; fixed campaign dialogue.
- Parameters: counterpart, contact, action, terms, duration, relationship,
  treaty gate and acceptance.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`; it binds negotiated bilateral terms
  and formal war state at sovereign-player scale.

## ACT-281 — End the current civilization's multi-command turn

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player commits the current civilization turn after any legal
  subset of available commands, allowing settlement and the next rival's turn
  to begin while unspent optional unit authority expires for that turn.
- Includes: the End Turn control in single-player Civilization VI.
- Excludes: spending one unit action; pausing real time; submitting one
  simultaneous hidden order.
- Parameters: civilization, turn number, mandatory-choice checks, unresolved
  alerts, unspent movement and next participant.
- Evidence: [Sid Meier's Civilization VI decomposition](../games/s-z/sid-meiers-civilization-vi.md).
- Novelty: first isolated for `GAME-0166`; earlier commit actions close one
  order or simultaneous phase rather than a whole empire's multi-command turn.

## ACT-282 — Modulate one context-sensitive vertical control

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while horizontal travel remains automatic, the player presses,
  holds or releases one control whose current avatar mode determines the
  requested vertical response without supplying a horizontal direction.
- Includes: pressing or holding to jump as the Stereo Madness cube and holding
  or releasing the same control to raise or lower the ship's flight path.
- Excludes: steering freely in two axes; selecting a destination; changing
  avatar mode directly; a decorative input with no collision consequence.
- Parameters: input device, press, hold, release, current mode, buffering and
  requested vertical response.
- Evidence: [Geometry Dash decomposition](../games/g-l/geometry-dash.md).
- Novelty: first isolated for `GAME-0167`; earlier locomotion actions directly
  steer an avatar or issue separate abilities rather than reuse one vertical
  control across an automatically advancing mode sequence.

## ACT-283 — Install or remove one compatible equipment Mod

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: in equipment configuration, place one owned compatible Mod into
  an eligible slot or remove it before returning to live play.
- Includes: configuring the chosen Warframe or starter weapon in the Arsenal
  during Awakening and Vor's Prize.
- Excludes: acquiring a Mod drop; levelling equipment; changing a weapon in the
  broader loadout; using an ability during a mission.
- Parameters: equipment, Mod, ownership, compatibility, slot, rank, drain,
  polarity and resulting configuration.
- Evidence: [Warframe decomposition](../games/s-z/warframe.md).
- Novelty: first isolated for `GAME-0168`; earlier loadout genes select whole
  equipment pieces rather than socketing one capacity-bearing modifier.

## ACT-284 — Rotate terminal nodes into a connected cipher

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while a terminal timer runs, rotate the displayed nodes until
  their paths form the accepted connected pattern, then submit or let the
  terminal validate it.
- Includes: the Grineer-style terminal hacking taught in Warframe's opening
  route.
- Excludes: entering a remembered password; consuming a Cipher item to bypass
  the puzzle; arbitrary movement or combat around the console.
- Parameters: node set, orientations, required connectivity, timer, retries,
  input device and validation state.
- Evidence: [Warframe decomposition](../games/s-z/warframe.md).
- Novelty: first isolated for `GAME-0168`; existing rotation actions transform
  world pieces rather than solve a timed terminal network.

## ACT-285 — Accept one employer-supplied cargo job

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: from a current job market, the player accepts one offer that fixes
  its cargo, origin, destination, deadline and payment and supplies the declared
  loaded vehicle for the duration of that job.
- Includes: accepting the scoped Euro Truck Simulator 2 Quick Job.
- Excludes: collecting freight with an owned truck; buying a vehicle; assigning
  a job to an autonomous employee; merely previewing an offer.
- Parameters: offer set, cargo, origin, destination, deadline, income, supplied
  truck, trailer and replacement policy.
- Evidence: [Euro Truck Simulator 2 decomposition](../games/a-f/euro-truck-simulator-2.md).
- Novelty: first isolated for `GAME-0169`; prior contracts dispatch autonomous
  carriers or retain player-owned equipment rather than instantiate one loaded
  employer vehicle for direct operation.

## ACT-286 — Choose a duration of rest at an eligible stop

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while stopped in an eligible rest location, the player selects a
  permitted sleep duration and commits the live job and world clock to advance
  through that interval while driver-rest state is restored.
- Includes: choosing when to wake under Euro Truck Simulator 2 update 1.60.
- Excludes: pausing simulation time; sleeping for a fixed system-chosen period;
  resting at a checkpoint that respawns enemies or heals combat resources.
- Parameters: location, current rest state, chosen duration, minimum break,
  world time, job deadline and wake time.
- Evidence: [Euro Truck Simulator 2 decomposition](../games/a-f/euro-truck-simulator-2.md).
- Novelty: first isolated for `GAME-0169`; earlier rest genes use a fixed
  checkpoint or survival sleep transition rather than schedule a player-sized
  break against an active delivery deadline.

## ACT-287 — Choose one delivery drop-off treatment

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: at the cargo destination, the player chooses one currently
  offered trailer treatment whose bay geometry or skip rule determines the
  required parking manoeuvre and eligible experience credit.
- Includes: selecting a standard or easier Euro Truck Simulator 2 trailer bay,
  or accepting the available automatic-parking/skip treatment.
- Excludes: steering and reversing the vehicle itself; accepting the cargo job;
  choosing an arbitrary world parking space with no delivery consequence.
- Parameters: offered treatments, bay, difficulty, skip, validation pose,
  detachment and experience credit.
- Evidence: [Euro Truck Simulator 2 decomposition](../games/a-f/euro-truck-simulator-2.md).
- Novelty: first isolated for `GAME-0169`; prior spatial actions do not select a
  contract-closing parking obligation with difficulty-sensitive experience.

## ACT-288 — Throw a bolt to probe an anomaly path

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player throws one carried bolt into a reachable direction to
  trigger an anomaly and observe whether a short traversal window opens.
- Includes: testing and crossing Lesser Zone anomalies after the prologue in
  S.T.A.L.K.E.R. 2.
- Excludes: damaging an enemy with a grenade; permanently disabling a hazard;
  revealing an artifact with a detector.
- Parameters: bolt, trajectory, anomaly class, trigger radius, discharge window,
  recovery time and observed route.
- Evidence: [S.T.A.L.K.E.R. 2 decomposition](../games/s-z/stalker-2-heart-of-chornobyl.md).
- Novelty: first isolated for `GAME-0170`; earlier thrown probes reveal a remote
  bearing or deal damage rather than briefly cycle a local environmental hazard.

## ACT-289 — Sweep with a detector and collect a manifested artifact

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player equips an artifact detector, follows its changing
  signal inside an anomalous field and takes the artifact after proximity makes
  it visible and reachable.
- Includes: the prologue artifact and the Mold artifact in `Piece of Cake`.
- Excludes: seeing ordinary ground loot; reading an external map; equipping an
  already owned artifact in a suit container.
- Parameters: detector, signal cadence, bearing, critical range, field, artifact,
  manifestation position and pickup reach.
- Evidence: [S.T.A.L.K.E.R. 2 decomposition](../games/s-z/stalker-2-heart-of-chornobyl.md).
- Novelty: first isolated for `GAME-0170`; ordinary loot is visible before
  transfer, while this action actively localises an initially invisible object.

## ACT-290 — Directly control a dedicated driving vehicle

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while assigned to one driving vehicle, the player directly
  controls steering, throttle, braking, gear selection and any declared
  handbrake without first entering or later leaving an embodied seat.
- Includes: controlling each assigned road, dirt, cross-country and Time Attack
  car in the scoped Forza Horizon 6 opening; steering, accelerating, reversing,
  braking and powersliding one dedicated Rocket League car; driving the fixed
  Story starter through Need for Speed Unbound's `Shopping Spree` packet; and
  driving the fixed Mustang then authored Regera handoff through Need for Speed
  Payback's `The Highway Heist`; and steering, accelerating and braking the
  dedicated CarSport vehicle on Trackmania `Summer 2026 - 01`; and steering,
  accelerating, braking and handbraking the fixed stock starter through Need
  for Speed Underground's opening Circuit.
- Excludes: entering and exiting a persistent world vehicle; assigning an
  autonomous transport route; selecting which owned car will become active.
- Parameters: vehicle, steering, throttle, brake, handbrake, transmission,
  camera, input device and control assistance.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md) and
  [Rocket League decomposition](../games/m-r/rocket-league.md), and
  [War Thunder decomposition](../games/s-z/war-thunder.md), and
  [Need for Speed Payback decomposition](../games/m-r/need-for-speed-payback.md),
  [Trackmania decomposition](../games/s-z/trackmania.md), and
  [Need for Speed Underground decomposition](../games/m-r/need-for-speed-underground.md).
- Novelty: first isolated for `GAME-0171`; `ACT-201` requires an embodied
  enter/seat/exit loop that a dedicated racing-car assignment does not expose.

## ACT-291 — Select the active vehicle from an eligible collection

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: outside a locked event, the player chooses one currently owned
  and eligible vehicle so it becomes the active directly controlled car.
- Includes: choosing one of the three Forza Horizon 6 starter cars and later
  switching among owned cars through Car Collection before an event.
- Excludes: purchasing a vehicle; accepting a supplied cargo job; changing cars
  after an event has locked its grid.
- Parameters: owned collection, current vehicle, eligibility, location,
  delivery transition and event lock.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md).
- Novelty: first isolated for `GAME-0171`; inventory-equipment actions do not
  replace a complete directly driven world vehicle from an owned garage.

## ACT-292 — Configure driving assists and opponent difficulty

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player commits a compatible driving-assistance and opponent-
  difficulty profile that changes how direct inputs, guidance and autonomous
  rivals resolve during eligible driving events.
- Includes: Forza Horizon 6 steering, braking, transmission, traction,
  stability, driving-line, Rewind and Drivatar difficulty settings; Need for
  Speed Unbound's Relaxed Story rival/police profile and automatic gearbox;
  Need for Speed Payback's Easy opponent profile and automatic gearbox; Need
  for Speed Underground's per-event Easy rivals and automatic transmission.
- Excludes: changing only rendering quality; tuning a car's mechanical parts;
  selecting a different event or owned vehicle.
- Parameters: steering, braking, transmission, traction, stability, driving
  line, Rewind, damage, game speed and opponent difficulty.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md),
  [Need for Speed Payback decomposition](../games/m-r/need-for-speed-payback.md),
  and [Need for Speed Underground decomposition](../games/m-r/need-for-speed-underground.md).
- Novelty: first isolated for `GAME-0171`; earlier difficulty parameters do not
  expose one coupled driving-control, guidance and autonomous-rival profile.

## ACT-293 — Commit one available mapped driving event

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player selects one currently unlocked driving-event marker
  and commits to its authored route, vehicle eligibility and result rules.
- Includes: entering the scoped Trail, Circuit, Cross Country, Time Attack and
  Horizon Invitational events in Forza Horizon 6; committing Need for Speed
  Unbound's available Story `Shopping Spree` marker; committing Need for Speed
  Payback's available `The Highway Heist` Story marker; committing Need for
  Speed Underground's first available `Jose's Got Your Back` event.
- Excludes: placing a navigation waypoint without starting the event; creating
  a custom route; selecting a multiplayer playlist.
- Parameters: marker, event type, route, eligibility, solo field, result rule,
  reward and first-completion state.
- Evidence: [Forza Horizon 6 decomposition](../games/a-f/forza-horizon-6.md),
  [Need for Speed Payback decomposition](../games/m-r/need-for-speed-payback.md),
  and [Need for Speed Underground decomposition](../games/m-r/need-for-speed-underground.md).
- Novelty: first isolated for `GAME-0171`; earlier world-node selections launch
  expeditions or narrative tasks rather than one bounded driving ruleset.

## ACT-294 — Commit fighter, side and control type for one duel

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before a fixed fighting match begins, the player assigns one
  available fighter, participant side and supported input mapping to each
  declared participant.
- Includes: assigning base-roster Ryu to P1, base-roster Luke to CPU and Classic
  controls to both in Street Fighter 6 Fighting Ground Versus.
- Excludes: changing fighter during an active round; configuring a persistent
  campaign avatar; selecting a multi-member team or online rank queue.
- Parameters: roster, participant, side, human or CPU authority, control type,
  costume, stage and Advantage setting.
- Evidence: [Street Fighter 6 decomposition](../games/s-z/street-fighter-6.md).
- Additional support: [Brawlhalla decomposition](../games/a-f/brawlhalla.md),
  for assigning one fixed human fighter and one fixed CPU mirror before an
  offline Stock duel.
- Novelty: first isolated for `GAME-0172`; earlier hero selections bind team
  compositions, deployment kits or persistent builds rather than two sides of
  one short offline duel.

## ACT-295 — Enter one character-command fighting attack

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while the controlled fighter is actionable, the player commits
  one legal normal, command, special, projectile or Super attack through its
  declared directional and button sequence.
- Includes: Ryu's ordinary Classic-control attacks, Hadoken and a stocked Super
  Art in the scoped Street Fighter 6 duel.
- Excludes: moving without an attack; automatically resolving the resulting
  contact; an equipped firearm or tool; a tactical turn command.
- Parameters: fighter, control mapping, directional sequence, button, strength,
  attack member, cancel source, buffer, resource and facing.
- Evidence: [Street Fighter 6 decomposition](../games/s-z/street-fighter-6.md).
- Additional support: [Brawlhalla decomposition](../games/a-f/brawlhalla.md),
  for unarmed and selected-Legend weapon commands in a platform-fighter duel.
- Novelty: first isolated for `GAME-0172`; the corpus previously addressed
  equipped tools, cooldown abilities and queued attacks rather than a
  character-owned fighting command vocabulary.

## ACT-296 — Hold or release directional fighting guard

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player holds the direction away from the current opponent to
  request standing or crouching guard, or releases that direction to leave the
  guard request as live combat continues.
- Includes: ordinary high and low blocking in the scoped Street Fighter 6 duel.
- Excludes: Drive Parry; armour granted by an attack; a turn-based defend
  command; cover attachment in a world shooter.
- Parameters: facing, away direction, standing or crouching posture, incoming
  attack class, cross-up, block contact and release timing.
- Evidence: [Street Fighter 6 decomposition](../games/s-z/street-fighter-6.md).
- Novelty: first isolated for `GAME-0172`; earlier defence actions use cover,
  timed prompts or equipment rather than a continuous opponent-relative input.

## ACT-297 — Attempt a close throw or matching throw escape

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: at close range the player commits the throw input either to seize
  a throwable opponent or, during the declared response window, to escape the
  opponent's ordinary throw.
- Includes: ordinary throw and Throw Escape in Street Fighter 6 Versus.
- Excludes: command-grab attacks as roster parameters; carrying an incapacitated
  body; grappling a world target from stealth; automatic collision displacement.
- Parameters: range, target state, input, start-up, escape window, damage,
  displacement, side switch and recovery.
- Evidence: [Street Fighter 6 decomposition](../games/s-z/street-fighter-6.md).
- Novelty: first isolated for `GAME-0172`; it couples the same live input to
  offensive seizure or a simultaneous close-range escape contest.

## ACT-298 — Commit one legal Drive technique

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player requests one of the shared Drive System techniques
  from an eligible fighting state, accepting its current stock cost and combat
  transition.
- Includes: Drive Impact, Drive Parry, Drive Rush, Drive Reversal and Overdrive
  attacks in Street Fighter 6.
- Excludes: ordinary guard; spending Super Art stock; passive Drive regeneration;
  a character-specific attack with no Drive cost.
- Parameters: technique, input, fighter state, stock cost, cancel source,
  contact, recovery and Burnout eligibility.
- Evidence: [Street Fighter 6 decomposition](../games/s-z/street-fighter-6.md).
- Novelty: first isolated for `GAME-0172`; one shared meter explicitly funds
  several offensive, defensive and mobility commitments rather than one
  cooldown or single-purpose stamina action.

## ACT-299 — Draft one offered floorplan behind an addressed door

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: at one unopened doorway, the player selects exactly one exposed
  room plan from the bounded offer and commits it as the candidate room behind
  that door.
- Includes: selecting one of three room plans in Blue Prince.
- Excludes: drawing a room without choosing it; rearranging an already owned
  map tile; buying a shop item; free-form building.
- Parameters: doorway, offer size, plan, room type, orientation, cost, effect
  and selection state.
- Evidence: [Blue Prince decomposition](../games/a-f/blue-prince.md).
- Novelty: first isolated for `GAME-0173`; earlier bounded offers choose
  upgrades, story outcomes or assets rather than the next traversable room.

## ACT-300 — End the current manor day and request a fresh layout

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player explicitly ends the current manor attempt, accepting
  its declared daily-state loss and starting the next morning's fresh layout.
- Includes: Call it a Day in Blue Prince.
- Excludes: an automatic timeout; death-triggered restart; loading a prior save;
  leaving one room while preserving the current floorplan.
- Parameters: current day, confirmation, daily state, retained state, next
  morning and reset seed.
- Evidence: [Blue Prince decomposition](../games/a-f/blue-prince.md).
- Novelty: first isolated for `GAME-0173`; prior resets are system terminals or
  consequence loops rather than an ordinary player-called route decision.

## ACT-301 — Ban one eligible opposing-role operator

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during a scheduled roster-denial phase, one team commits an
  eligible operator from the opposing role to the shared unavailable pool.
- Includes: Rainbow Six Siege Pro League attacker and defender operator bans.
- Excludes: selecting one's own operator; disabling a cosmetic; a tournament
  map veto outside the in-game match.
- Parameters: team, role, phase, eligible roster, operator, prior bans and
  resulting unavailable pool.
- Evidence: [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Novelty: first isolated for `GAME-0174`; earlier roster commitments choose a
  playable identity but do not spend an in-game team choice to deny the
  opposing role across scheduled round blocks.

## ACT-302 — Direct one live observation device or feed

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player enters one surviving remote observation feed and,
  where supported, moves or rotates its device and requests a scan or ping.
- Includes: Rainbow Six Siege attacker drones, defender cameras and compatible
  observation tools.
- Excludes: avatar-centred sight; a static minimap; reviewing a post-match
  replay; automatic detection with no device control.
- Parameters: owner, device, feed, field of view, movement, rotation, scan,
  ping, team sharing and destruction state.
- Evidence: [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Novelty: first isolated for `GAME-0174`; it transfers live attention and
  control from an exposed body to a destructible team observation node.

## ACT-303 — Breach one eligible constructed surface

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player targets an eligible wall, floor, ceiling, door or
  window and commits a compatible impact, explosive or hard-breach tool to
  open or enlarge traversable, visible or penetrable geometry.
- Includes: Rainbow Six Siege soft breach and compatible reinforced-wall hard
  breach.
- Excludes: ordinary bullet penetration with no useful opening; placing the
  reinforcement; cosmetic debris; free-form terrain mining into inventory.
- Parameters: surface, material, fortification, tool, placement, charge,
  countermeasure, opening geometry and completion.
- Evidence: [Rainbow Six Siege decomposition](../games/s-z/tom-clancys-rainbow-six-siege.md).
- Novelty: first isolated for `GAME-0174`; existing destruction genes resolve
  system damage, while this action commits a player-controlled structural route
  intervention against constructed defence.

## ACT-304 — Configure one autonomous football lineup and dual tactical plan

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before or during a managed fixture, the player assigns eligible
  squad members to legal lineup positions and configures distinct in-possession
  and out-of-possession shapes, roles and team instructions for autonomous play.
- Includes: Football Manager 26 team selection and dual tactical formations.
- Excludes: directly moving a footballer; signing a player; choosing only a
  cosmetic formation graphic.
- Parameters: available squad, starting eleven, substitutes, position, role,
  duty, possession phase, formation and team instructions.
- Evidence: [Football Manager 26 decomposition](../games/a-f/football-manager-26.md).
- Novelty: first isolated for `GAME-0175`; earlier football genes coordinate
  an already declared team but do not expose the manager's two-phase plan as a
  player-authored control surface.

## ACT-305 — Commit a live managerial substitution or tactical revision

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while an autonomous football fixture remains live, the player
  commits one legal personnel, role, shape or instruction change that the team
  applies from the next eligible match state.
- Includes: Football Manager 26 substitutions and live tactical changes.
- Excludes: directly steering a player or ball; editing the squad after the
  fixture; uncommitted analysis-screen experimentation.
- Parameters: match state, outgoing player, incoming player, position, role,
  phase shape, instruction, confirmation and application point.
- Evidence: [Football Manager 26 decomposition](../games/a-f/football-manager-26.md).
- Novelty: first isolated for `GAME-0175`; the intervention changes the policy
  of autonomous agents rather than issuing their next embodied action.

## ACT-306 — Arm one soldier's movement-triggered reaction fire

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player spends a controlled soldier's remaining authority to
  prepare one ranged attack that may trigger when an eligible hostile moves
  through that soldier's visible firing conditions during the hostile phase.
- Includes: XCOM 2 Overwatch in the scoped Operation Gatecrasher mission.
- Excludes: firing immediately at a selected target; an always-on zone attack;
  a hostile reaction that was not armed by the player.
- Parameters: soldier, weapon, remaining Action Points, sight line, hostile
  movement, trigger eligibility, accuracy modifier and ammunition.
- Evidence: [XCOM 2 decomposition](../games/s-z/xcom-2.md).
- Novelty: first isolated for `GAME-0176`; existing reaction systems resolve a
  trigger, while this action explicitly commits a soldier's remaining turn to
  prepare it across the squad-to-hostile phase boundary.

## ACT-307 — Commit one adjacent tactical mission interaction

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player commands an adjacent controlled soldier to perform a
  declared mission interaction at an eligible fixture, consuming the required
  action authority and changing objective state.
- Includes: planting the X4 charge at the ADVENT monument in XCOM 2 Operation
  Gatecrasher.
- Excludes: ordinary movement; picking up cosmetic scenery; automatic mission
  completion merely from entering an area.
- Parameters: soldier, fixture, adjacency, interaction type, Action Point cost,
  eligibility and resulting objective flag.
- Evidence: [XCOM 2 decomposition](../games/s-z/xcom-2.md).
- Novelty: first isolated for `GAME-0176`; it separates a spatially gated
  mission-state command from attacks, movement and generic item collection.

## ACT-308 — Commit a vehicle jump, dodge or aerial orientation

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while directly controlling the current vehicle, the player
  commits an eligible jump, directional dodge or continuous aerial-orientation
  input that changes its position and facing beyond ground steering alone.
- Includes: Rocket League jump, double jump, directional flip, air roll and
  aerial pitch or yaw control.
- Excludes: ordinary ground steering; boost thrust without jump authority; an
  automatic stunt animation.
- Parameters: vehicle, grounded state, jump count, dodge direction, input
  timing, pitch, yaw, roll, contact reset and resulting orientation.
- Evidence: [Rocket League decomposition](../games/m-r/rocket-league.md).
- Novelty: first isolated for `GAME-0177`; earlier avatar jumps and racing-car
  steering do not expose a dedicated vehicle's resettable aerial dodge budget.

## ACT-309 — Spend stored boost for directed vehicle thrust

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player holds or releases boost while directly controlling a
  vehicle, consuming its current finite reserve to add thrust along the
  vehicle's facing in ground or aerial motion.
- Includes: Rocket League ground acceleration, aerial ascent and recovery using
  stored boost; Need for Speed Payback conventional nitrous acceleration during
  the scoped carrier chase.
- Excludes: passive engine throttle; a permanent unlimited speed modifier;
  consuming a carried medical booster.
- Parameters: vehicle, reserve, input duration, thrust, facing, velocity,
  supersonic state and release.
- Evidence: [Rocket League decomposition](../games/m-r/rocket-league.md) and
  [Need for Speed Payback decomposition](../games/m-r/need-for-speed-payback.md).
- Novelty: first isolated for `GAME-0177`; the finite, spatially replenished
  reserve converts current vehicle orientation into optional directed thrust.

## ACT-310 — Choose a side-relative post-demolition respawn

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during the brief post-demolition window, the removed player
  selects one currently offered spawn position relative to the team's own goal
  before the vehicle returns to live control.
- Includes: Rocket League v2.72 online-match post-demolition respawn choice.
- Excludes: selecting the opening kickoff slot; a permanent spawn fixture;
  returning an eliminated player only in the next round.
- Parameters: team, own goal, offered positions, input window, selection,
  timeout fallback and restored vehicle.
- Evidence: [Rocket League decomposition](../games/m-r/rocket-league.md).
- Novelty: first isolated for `GAME-0177`; earlier respawn actions choose
  persistent beacons or allies rather than one immediate team-side field slot.

## ACT-311 — Consume a carried drink to restore hydration

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player consumes one eligible carried drink so its declared water value increases the avatar's current hydration state.
- Includes: drinking Filtered Water or another scoped water item in Subnautica Survival.
- Excludes: eating food for calories; automatically drinking from the environment; fabricating the drink.
- Parameters: drink, quantity, hydration value, current hydration and status effects.
- Evidence: [Subnautica decomposition](../games/s-z/subnautica.md).
- Novelty: first isolated for `GAME-0178`; earlier food-consumption actions do not spend an item into a separate hydration reserve.

## ACT-312 — Catch one reachable free-swimming organism

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player reaches toward one eligible freely moving small organism and takes it directly into carried inventory before it escapes range.
- Includes: hand-catching a reachable Peeper or Bladderfish in Subnautica.
- Excludes: gathering a stationary material yield; defeating a creature with a weapon; automatic trap collection.
- Parameters: organism, movement, reach, interaction window, inventory footprint and resulting carried state.
- Evidence: [Subnautica decomposition](../games/s-z/subnautica.md).
- Novelty: first isolated for `GAME-0178`; the collectible target remains an independently moving world organism until the successful interaction.

## ACT-313 — Hold a scanner on one reachable world target

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player equips a powered scanner, keeps one eligible world target within range and holds the scan command to advance its persistent analysis progress.
- Includes: scanning Subnautica technology fragments and organisms with the handheld Scanner.
- Excludes: selecting a completed blueprint in a crafting interface; an autonomous room-wide resource search; instant pickup of the target.
- Parameters: scanner, target, range, aim, battery, progress, interruption and completion.
- Evidence: [Subnautica decomposition](../games/s-z/subnautica.md).
- Novelty: first isolated for `GAME-0178`; unlike earlier target scans, the held observation itself accumulates resumable blueprint evidence.

## ACT-314 — Construct or deconstruct one habitat module

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player uses a powered building tool on one legal underwater module pose or existing module and holds construction or deconstruction until its material-backed progress completes.
- Includes: building or removing a Subnautica I Compartment, Hatch or Solar Panel with the Habitat Builder.
- Excludes: placing a carried block instantly; repairing a breach; deploying a free-floating fabrication fixture.
- Parameters: tool charge, module, pose, orientation, material, progress, cancellation, refund and connected habitat.
- Evidence: [Subnautica decomposition](../games/s-z/subnautica.md).
- Novelty: first isolated for `GAME-0178`; underwater module progress changes a connected pressure hull and may be fully reversed into materials.

## ACT-315 — Deploy or pack a floating vehicle-fabrication fixture

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player releases one eligible carried fabrication fixture so it reaches its operating water state, or packs the idle fixture back into carried inventory.
- Includes: deploying, boarding and later packing a Subnautica Mobile Vehicle Bay.
- Excludes: constructing a connected habitat module; entering the fabricated vehicle; selecting the vehicle recipe itself.
- Parameters: fixture, carried footprint, water state, surface movement, unfold state, boarding reach and packing legality.
- Evidence: [Subnautica decomposition](../games/s-z/subnautica.md).
- Novelty: first isolated for `GAME-0178`; a bulky carried station transforms into a reusable floating fabrication platform rather than a fixed building.

## ACT-316 — Queue one unit at an eligible production building

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player selects an owned production building and appends one currently available unit type to its finite training queue.
- Includes: queuing Villagers at a Town Center and military units at Barracks, Archery Ranges, Stables, Castles or Siege Workshops in Age of Empires II: Definitive Edition.
- Excludes: choosing one city's turn-settled production target; spawning a free scripted unit; selecting a technology rather than a unit.
- Parameters: building, unit type, queue position, cost, training time, prerequisites, queue capacity and population headroom.
- Evidence: [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
- Novelty: first isolated for `GAME-0179`; existing production choices either own one accumulating target or configure an automatic recipe.

## ACT-317 — Set formation and stance for a selected unit group

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player assigns one available spatial formation and combat stance to a selected group, changing how its members arrange, acquire targets and preserve or abandon position during later commands.
- Includes: line, box, staggered or flank formations and aggressive, defensive, stand-ground or no-attack stances in Age of Empires II: Definitive Edition.
- Excludes: drawing a cosmetic formation; assigning football roles; directly specifying every member's path independently.
- Parameters: selected group, formation, stance, facing, spacing, acquisition policy and regroup condition.
- Evidence: [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
- Novelty: first isolated for `GAME-0179`; the setting persists on a directly commanded multi-unit group rather than configuring an autonomous squad plan.

## ACT-318 — Assign a villager to a reachable economic task

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player orders one or more selected villagers to gather from a reachable resource source, construct a placed foundation or repair an eligible damaged owned entity.
- Includes: tasking villagers to food, wood, gold or stone and to building or repair work in Age of Empires II: Definitive Edition.
- Excludes: the automatic work ticks after assignment; configuring a global worker-priority policy; direct military attack orders.
- Parameters: villagers, task class, target, path, drop-off building, foundation, repair target and queue modifier.
- Evidence: [Age of Empires II: Definitive Edition decomposition](../games/a-f/age-of-empires-ii-definitive-edition.md).
- Novelty: first isolated for `GAME-0179`; earlier worker assignment genes allocate abstract jobs or autonomous errands rather than a selected live RTS worker to a world target.

## ACT-319 — Configure and launch a bounded Free Flight plan

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before taking control, the player selects one aircraft, departure,
  arrival, route and environmental/assistance settings, then launches that
  declared Free Flight instance.
- Includes: the scoped Microsoft Flight Simulator 2024 Cessna 172 G1000 flight
  from `KBFI` parking to `KTIW` parking under fixed daytime Clear Skies.
- Excludes: accepting a Career mission; changing live weather after launch;
  filing an autonomous transport schedule; selecting only a road waypoint.
- Parameters: aircraft, livery, departure, parking, arrival, route rules, time,
  weather, traffic, assistance preset and launch command.
- Evidence: [Microsoft Flight Simulator 2024 decomposition](../games/m-r/microsoft-flight-simulator-2024.md).
- Novelty: first isolated for `GAME-0180`; one pre-control commitment joins
  aircraft, aeronautical endpoints, route and conditions into a reproducible
  manual-flight instance.

## ACT-320 — Operate aircraft power, engine and configuration controls

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player manipulates cockpit switches and levers that establish
  or change the aircraft's fuel feed, electrical power, engine operation,
  lighting and aerodynamic configuration without delegating flight control.
- Includes: Cessna 172 fuel selector, battery/alternator, avionics, mixture,
  magnetos/starter, throttle, lights, trim and flap controls in the scoped
  Microsoft Flight Simulator 2024 Free Flight.
- Excludes: moving the yoke or rudder for attitude control; one-key automatic
  startup; configuring an aircraft before the simulation instance exists.
- Parameters: control, position, dependency, engine state, circuit, power,
  mixture, RPM, light, trim and flap setting.
- Evidence: [Microsoft Flight Simulator 2024 decomposition](../games/m-r/microsoft-flight-simulator-2024.md).
- Novelty: first isolated for `GAME-0180`; direct cockpit configuration is a
  persistent causal control surface rather than a vehicle-selection parameter.

## ACT-321 — Directly pilot a fixed-wing aircraft

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player continuously commands a fixed-wing aircraft's pitch,
  roll, yaw, thrust and wheel braking to taxi, take off, fly, land and stop
  rather than selecting a destination for autonomous movement.
- Includes: hand-flying and ground handling the scoped Microsoft Flight
  Simulator 2024 Cessna 172 G1000 without autopilot.
- Excludes: mecha regime switching; parachute steering; autonomous AI piloting;
  road driving whose lift and airborne envelope are not causal.
- Parameters: elevator, aileron, rudder, throttle, brake, trim, attitude,
  airspeed, ground speed, contact state and control device.
- Evidence: [Microsoft Flight Simulator 2024 decomposition](../games/m-r/microsoft-flight-simulator-2024.md).
- Novelty: first isolated for `GAME-0180`; the same direct control authority
  spans runway contact and a continuously integrated aerodynamic flight regime.

## ACT-322 — Commit one role-queue slot before matchmaking

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before matchmaking, the player commits one offered combat role,
  reserving only that role's team slot and character roster for the resulting
  match.
- Includes: ordinary Overwatch 5v5 Role Queue selection of Tank, Damage or
  Support before entering Quick Play matchmaking.
- Excludes: selecting a hero after the lobby forms; an open-queue preference;
  an autonomous party role; account profile labels.
- Parameters: queue, role, team composition, reserved slot, eligible roster and
  cancellation boundary.
- Evidence: [Overwatch decomposition](../games/m-r/overwatch.md).
- Novelty: first isolated for `GAME-0181`; role authority is committed before
  the match exists rather than assigned by a later hero pick.

## ACT-323 — Vote for one offered map or random alternative

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during the pre-match ballot, the player commits one vote to an
  exposed map candidate or the explicit random-map alternative before the
  ruleset settles the lobby's arena.
- Includes: Overwatch Quick Play's three visible map choices and fourth Random
  Map option.
- Excludes: selecting a map with unilateral authority; banning a character;
  external survey voting; a hidden matchmaking preference.
- Parameters: lobby, offered maps, modes, random option, vote, pass, deadline
  and side marker.
- Evidence: [Overwatch decomposition](../games/m-r/overwatch.md).
- Novelty: first isolated for `GAME-0181`; the player's input changes selection
  weight but usually does not determine the arena alone.

## ACT-324 — Select one eligible National Focus

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player commits one currently eligible national-development
  branch as the country's active focus so subsequent calendar progress accrues
  toward its declared persistent effects.
- Includes: choosing one base-game Italian National Focus during the scoped
  Hearts of Iron IV tutorial war.
- Excludes: selecting a technology in a research slot; changing a law; receiving
  an automatic national event.
- Parameters: country, focus tree, target, prerequisite, exclusion, duration,
  progress, cancellation rule and completion effects.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; one country-level authored branch
  occupies an exclusive continuous-progress channel.

## ACT-325 — Prioritise national state construction

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player places a legal state building or infrastructure target
  into the national construction queue and sets its priority for shared civilian
  factory work.
- Includes: queueing or reprioritising base-game Italian construction in an
  eligible state during the tutorial.
- Excludes: placing an independently simulated worker; configuring an equipment
  production line; instantly buying a finished structure.
- Parameters: country, state, building, level, slot, queue position, priority,
  civilian-factory allocation and cancellation.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; national capacity is allocated through
  one ordered cross-state work list rather than a city-local build choice.

## ACT-326 — Configure a national equipment production line

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player creates or edits an unlocked equipment line and assigns
  a chosen number of national military factories to its continuing output.
- Includes: allocating Italian military factories to infantry equipment,
  artillery or support aircraft in the scoped Hearts of Iron IV rules.
- Excludes: selecting a construction project; manually crafting one item;
  changing a division template outside the tutorial packet.
- Parameters: equipment type, variant, factory count, priority, resources,
  efficiency, output, retention and line replacement.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; national factories share a persistent
  equipment portfolio whose allocation and retained efficiency are causal.

## ACT-327 — Organise divisions under an army commander

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player assigns selected divisions to one army and selects or
  changes the commander who provides that formation's shared command authority.
- Includes: grouping the tutorial's Italian divisions into northern and southern
  armies under eligible generals.
- Excludes: drawing the army's spatial plan; directly moving one division;
  changing a division's equipment template.
- Parameters: division set, army, theatre, commander, command limit, traits,
  reassignment and removal.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; many persistent strategic units are
  explicitly collected beneath a shared command object before plan execution.

## ACT-328 — Draw and execute an army front plan

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player draws a legal frontline and destination-oriented
  offensive line for an army, then activates, pauses or deletes the resulting
  persistent multi-division plan.
- Includes: defining and executing Italian fronts from Eritrea or Somaliland
  into Ethiopia.
- Excludes: issuing one division a manual destination; selecting a commander;
  choosing a diplomatic war goal.
- Parameters: army, frontline geometry, opposing border, offensive line,
  assignment, execution state, aggressiveness, planning progress and deletion.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; player-authored geographic fields
  persist as autonomous instructions for a selected strategic formation.

## ACT-329 — Assign an air wing to a region and mission

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player commits one available air wing to an eligible air
  region and enables or disables one of its currently supported missions.
- Includes: assigning fighters or close air support to the East African theatre
  and enabling air superiority or close-air-support work.
- Excludes: directly piloting an aircraft; configuring its production line;
  ordering a naval task force.
- Parameters: wing, aircraft type, base, region, mission, day/night operation,
  intensity, range, fuel and reassignment.
- Evidence: [Hearts of Iron IV decomposition](../games/g-l/hearts-of-iron-iv.md).
- Novelty: first isolated for `GAME-0182`; aircraft are scheduled as a regional
  operational pool rather than directly routed as individual combat agents.

## ACT-330 — Select one spawnable lineup vehicle for the next ground sortie

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: at a pre-spawn or post-loss selection state, the player chooses
  one currently eligible vehicle from the match-locked lineup and commits it as
  the next directly controlled ground vehicle.
- Includes: choosing the M2A4, LVT(A)(1) or M2A2 for one of the scoped War
  Thunder Ground Arcade spawns while backups are disabled.
- Excludes: buying or researching a vehicle; switching an owned car outside a
  match; entering an already present world vehicle; temporary aircraft sorties.
- Parameters: lineup, crew slot, vehicle, eligibility, prior use, backup,
  remaining ground spawns, spawn point and commitment.
- Evidence: [War Thunder decomposition](../games/s-z/war-thunder.md).
- Novelty: first isolated for `GAME-0184`; the chosen member of a fixed
  pre-match vehicle roster becomes the next expendable combat body after each
  loss rather than replacing one persistent world vehicle.

## ACT-331 — Keep or mulligan the presented opening hand

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: before the first turn, the player either accepts the currently presented opening hand or requests a replacement hand and later returns the required number of cards to the bottom of the library.
- Includes: keeping or taking a London mulligan in the scoped MTG Arena Starter Deck Duel game.
- Excludes: discarding during a live turn; selecting cards while constructing a deck; redrawing a complete hand as a repeatable combat action.
- Parameters: starting hand size, mulligan count, replacement draw, cards put on bottom, ordering and final keep.
- Evidence: [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md).
- Novelty: first isolated for `GAME-0185`; opening-hand replacement is a pre-turn commitment whose retained size falls with each repeated request.

## ACT-332 — Play one land from hand

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during an eligible main phase, the active player places one land card from their hand onto the battlefield without casting it as a spell.
- Includes: playing a Plains, Island, Tranquil Cove or Temple of Enlightenment from Arcane Aerialists.
- Excludes: casting a permanent spell; activating a land's mana ability; putting a land onto the battlefield because another card instructs it.
- Parameters: land, controller, turn allowance, main phase, stack state, replacement effects and battlefield entry state.
- Evidence: [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md).
- Novelty: first isolated for `GAME-0185`; the primary renewable resource source enters through a special once-per-turn action rather than the stack.

## ACT-333 — Cast one spell from a visible hand

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player selects one castable card in their visible hand, declares any required modes, targets and variable values, then commits its payable cost so the resulting spell enters the stack.
- Includes: casting an Arcane Aerialists creature, instant, sorcery, artifact or enchantment under its current timing and target rules.
- Excludes: playing a land; activating text on a permanent already on the battlefield; resolving the spell immediately without priority.
- Parameters: card, spell type, timing, modes, targets, division, additional or alternative costs, mana payment and stack object.
- Evidence: [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md).
- Novelty: first isolated for `GAME-0185`; a held card becomes an interruptible stack object before its type-specific destination is known.

## ACT-334 — Activate one card ability

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player chooses one activated ability on a card they control, declares required choices and targets and pays its activation cost so the ability enters the stack unless it is a mana ability.
- Includes: activating Goldvein Pick or another legal activated ability present in the scoped supplied-deck match.
- Excludes: casting the source card; automatic triggered abilities; ordinary land play; system resolution of the activated text.
- Parameters: source, ability, priority, target, tap or mana cost, timing restriction, mana-ability exception and stack placement.
- Evidence: [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md).
- Novelty: first isolated for `GAME-0185`; an already present card can create a separate stack object by paying its own declared activation cost.

## ACT-335 — Pass priority without adding an object

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player who currently has priority declines to cast, activate or take another special action and transfers the response opportunity to the opponent.
- Includes: Arena's explicit or automated pass while a spell, ability, phase or step awaits both players.
- Excludes: ending the whole turn unilaterally; conceding; resolving an object before the opponent receives a response window.
- Parameters: priority holder, stack state, stop settings, consecutive passes, next player and phase or object awaiting settlement.
- Evidence: [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md).
- Novelty: first isolated for `GAME-0185`; choosing not to act is itself the handoff that permits stack resolution or phase advancement.

## ACT-336 — Declare an eligible attacking creature set

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: at the declare-attackers step, the active player chooses any legal subset of controlled creatures and commits each chosen creature as an attacker against the opponent or another legal defender.
- Includes: attacking with untapped Arcane Aerialists creatures that have been controlled since the turn began or have haste.
- Excludes: dealing combat damage; choosing blockers; casting a spell during a combat priority window.
- Parameters: creature subset, defender, tapped state, control duration, haste, attack restrictions, requirements and attack costs.
- Evidence: [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md).
- Novelty: first isolated for `GAME-0185`; one simultaneous legal subset begins combat before the opponent assigns any blockers.

## ACT-337 — Declare legal creature blockers

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: at the declare-blockers step, the defending player assigns any legal untapped controlled creatures to attacking creatures under current evasion, restriction and requirement rules.
- Includes: assigning eligible Arcane Aerialists creatures to block, including flying creatures blocking attackers with flying.
- Excludes: selecting attackers; assigning combat damage; casting an instant after blockers have been declared.
- Parameters: blocker, attacker, multiplicity, tapped state, flying or other evasion, restrictions, requirements and block costs.
- Evidence: [Magic: The Gathering Arena decomposition](../games/m-r/magic-the-gathering-arena.md).
- Novelty: first isolated for `GAME-0185`; the defender constructs a legal many-to-one interception relation after seeing the attacking set.

## ACT-338 — Place one crafted survival fixture

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player positions one already crafted deployable fixture on compatible clear world ground and commits it as a persistent usable structure.
- Includes: placing a Campfire, Fire Pit, Science Machine, Alchemy Engine, Crock Pot or Chest in the scoped Don't Starve Together Forest world.
- Excludes: crafting the fixture item; feeding fuel to an existing fire; constructing a multi-part blueprint; dropping an ordinary carried item.
- Parameters: fixture, carried deployment state, position, footprint, clear ground, collision, orientation and resulting structure.
- Evidence: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Novelty: first isolated for `GAME-0186`; a personally crafted survival output becomes an addressed persistent world service through a separate spatial commitment.

## ACT-339 — Give a crafted revival item to a ghost partner

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: one living player targets a nearby dead partner's ghost with a carried revival item and commits that item to return the partner to embodied play.
- Includes: giving a Telltale Heart to the other scoped Wilson survivor's ghost.
- Excludes: a ghost reviving itself; touching the Florid Postern in Endless mode; automatic respawn; healing a living partner.
- Parameters: living giver, ghost target, revival item, reach, item consumption, restored health, maximum-health penalty and revived position.
- Evidence: [Don't Starve Together decomposition](../games/a-f/dont-starve-together.md).
- Novelty: first isolated for `GAME-0186`; cooperative recovery requires asymmetric authority between an embodied giver and a non-corporeal partner state.

## ACT-340 — Select or change one playable class in team spawn

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while the player's team-spawn selection state is legal, the
  player chooses one playable class and transfers the current or next-life
  controlled body and its base stock kit to that class.
- Includes: selecting or changing among the nine ordinary Team Fortress 2
  classes in a Casual Payload team spawn, with teammate duplicates permitted.
- Excludes: a match-long hero draft; a role-queue commitment; selecting a
  Team-Up partner; configuring alternate weapons; cosmetic appearance.
- Parameters: team, spawn state, living state, class roster, selected class,
  stock kit, duplicate policy and effect timing.
- Evidence: [Team Fortress 2 decomposition](../games/s-z/team-fortress-2.md).
- Novelty: first isolated for `GAME-0187`; the live selection changes embodied
  class function through spawn without either uniqueness or a permanent draft.

## ACT-341 — Commit one contextual authored-object interaction

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player addresses one reachable authored world object and
  commits its currently legal read, activate, collect, install, repair, unlock
  or open interaction, changing local objective, fixture, inventory or route
  state.
- Includes: reading Sastasha's Bloody Memo, activating the matching coral and
  revealed switch, collecting and using the Captain's Quarters and Waverider
  Gate keys, opening their gates and opening an admitted treasure coffer.
- Excludes: an ordinary weapon attack; free-form crafting; dialogue choice;
  an interaction outside the current bounded route or objective.
- Parameters: actor, object, reach, interaction, prerequisite, carried key,
  consumed or retained item, resulting flag, route state and reward source.
- Evidence: [FINAL FANTASY XIV Online decomposition](../games/a-f/final-fantasy-xiv-online.md).
- Additional support: [Left 4 Dead 2 decomposition](../games/g-l/left-4-dead-2.md),
  for opening authored route doors and activating the Hotel elevator control.
- Additional support: [Destiny 2 decomposition](../games/a-f/destiny-2.md),
  for activating the mesh terminal and opening the admitted end chest.
- Additional support: [PAYDAY 2 decomposition](../games/m-r/payday-2.md), for
  installing, assembling and repairing the authored Bank Heist thermal drill.
- Novelty: first isolated for `GAME-0188`; one generic command boundary joins
  readable clues, stateful switches, typed route keys and optional dungeon
  reward objects without treating their different resolutions as one system.

## ACT-342 — Reclaim allocated character-development points at a checkpoint

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: at an eligible campaign checkpoint, the player selects one or
  more previously allocated character-development nodes and commits their
  permitted reclamation so those points return to the unspent pool.
- Includes: Black Myth: Wukong Reignite the Sparks for one node, a branch or
  all currently allocated Sparks at a Keeper's Shrine without a Will fee.
- Excludes: spending an available point; purchasing a paid attribute reset;
  refunding an item or account-wide progression.
- Parameters: checkpoint, allocation set, branch, current rank, reclaimed
  points, fee, retained unlock and resulting unspent pool.
- Evidence: [Black Myth: Wukong decomposition](../games/a-f/black-myth-wukong.md).
- Novelty: first isolated for `GAME-0189`; a campaign checkpoint exposes
  granular cost-free recovery of already committed build authority.

## ACT-343 — Confirm one persistent ancestry and bodily presentation

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: at a mandatory new-character gate, the player selects one
  available ancestry and commits the permitted body, face, sex and name values
  as the persistent identity that enters the authored campaign.
- Includes: choosing a Nord and confirming the body, face and name at Helgen in
  the scoped Skyrim Special Edition fresh start.
- Excludes: choosing a class, background or point-buy build; changing equipment;
  a cosmetic editor that has no campaign-entry authority.
- Parameters: ancestry, body preset, sex, appearance controls, name, confirmation
  gate, starting traits and persistent identity.
- Evidence: [The Elder Scrolls V: Skyrim Special Edition decomposition](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md).
- Novelty: first isolated for `GAME-0190`; mandatory ancestry and presentation
  are committed without a class, occupation, background or build-point budget.

## ACT-344 — Probe and turn one keyed lock with a fragile pick

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while a keyed lock is addressed, the player changes the angular
  position of one consumable pick and applies rotational torque to test whether
  the current offset can turn the cylinder far enough to unlock it.
- Includes: opening one declared novice prison-cell lock during Skyrim Special
  Edition's scoped Hadvar route through Helgen Keep.
- Excludes: using the correct carried key; entering a numeric code; automatically
  resolving a skill check; forcing a door with an attack.
- Parameters: lock, difficulty, hidden sweet spot, pick angle, torque, cylinder
  rotation, resistance feedback, pick durability and unlocked state.
- Evidence: [The Elder Scrolls V: Skyrim Special Edition decomposition](../games/s-z/the-elder-scrolls-v-skyrim-special-edition.md).
- Novelty: first isolated for `GAME-0190`; continuous angular probing consumes
  a fragile tool while progressively exposing one hidden opening interval.

## ACT-345 — Commission one building in an owned settlement slot

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one currently legal building or chain upgrade
  for a vacant or compatible slot in an owned settlement and commits its stated
  treasury cost and turn duration to the campaign queue.
- Includes: upgrading Kislev Refuge and commissioning its declared Store House
  during the scoped Total War: WARHAMMER III prologue route.
- Excludes: placing a freely positioned real-time building; choosing a city's
  yield-funded production target; recruiting a unit; instant scripted scenery.
- Parameters: settlement, slot, building chain, tier, prerequisite, treasury
  cost, build duration, cancellation and completed effect.
- Evidence: [Total War: WARHAMMER III decomposition](../games/s-z/total-war-warhammer-iii.md).
- Novelty: first isolated for `GAME-0191`; a fixed settlement slot accepts a
  prepaid chain entry whose effect arrives after campaign-turn settlement.

## ACT-346 — Arrange units inside a pre-battle deployment zone

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before a real-time battle begins, the player selects controlled
  units and commits their positions, facing, width and grouping within the
  side's currently legal deployment region.
- Includes: arranging the Kislev Expedition's admitted formations before the
  first Beacon battle in the scoped Total War: WARHAMMER III prologue.
- Excludes: issuing movement after battle starts; choosing a reinforcement
  spawn; placing units outside the deployment boundary; cosmetic army display.
- Parameters: unit set, deployment region, position, facing, frontage, depth,
  group, overlap, terrain and battle-start commitment.
- Evidence: [Total War: WARHAMMER III decomposition](../games/s-z/total-war-warhammer-iii.md).
- Novelty: first isolated for `GAME-0191`; the editable formation is spatially
  legal only before the live battle clock and becomes its initial combat state.

## ACT-347 — Hire available settlement recruits into a persistent party

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: at an entered settlement the player selects one or more currently
  offered recruit bodies and pays their displayed hiring cost so they leave the
  local offer and occupy available slots in the player's persistent campaign
  party.
- Includes: hiring the maximum offered tutorial troops at Tevea in scoped Mount
  & Blade II: Bannerlord Campaign.
- Excludes: training a queued RTS unit; persuading a prisoner over time;
  recruiting a named companion through a quest; automatic population growth.
- Parameters: settlement, offer source, troop type, available count, cost,
  denars, party capacity, selected quantity and resulting roster.
- Evidence: [Mount & Blade II: Bannerlord decomposition](../games/m-r/mount-and-blade-ii-bannerlord.md).
- Novelty: first isolated for `GAME-0194`; immediate paid transfer from a local
  recruit offer into a mobile persistent party is absent from lower-ID actions.

## ACT-348 — Mount and directly ride an available battle horse

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player approaches an eligible horse in a live battle, mounts
  or dismounts it and directly controls its pace, steering and jump while
  retaining personal weapon and attack authority.
- Includes: using the fixed starting horse in scoped Mount & Blade II:
  Bannerlord tutorial field battles.
- Excludes: calling a persistent bonded horse with saddle cargo; target-routed
  automatic mount travel; a resummonable spectral steed; campaign-map movement.
- Parameters: horse, reach, rider, mount state, pace, direction, jump, weapon,
  mounted attack and dismount.
- Evidence: [Mount & Blade II: Bannerlord decomposition](../games/m-r/mount-and-blade-ii-bannerlord.md).
- Novelty: first isolated for `GAME-0194`; the horse is an embodied available
  battle agent without the identity, bond, cargo or summon rules of prior mounts.

## ACT-349 — Hold a weapon block toward one incoming attack direction

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during live melee the player aims and holds the equipped weapon or
  shield guard toward one current attack direction, or releases it, so the
  chosen guard geometry can oppose the incoming strike.
- Includes: directional weapon and shield blocking in scoped Mount & Blade II:
  Bannerlord tutorial combat.
- Excludes: Street Fighter opponent-relative high/low guard; a timed parry
  prompt with no chosen direction; passive armour; turn-based Defend.
- Parameters: equipment, attack direction, block direction, aim mapping, hold,
  release, contact instant and recovery.
- Evidence: [Mount & Blade II: Bannerlord decomposition](../games/m-r/mount-and-blade-ii-bannerlord.md).
- Novelty: first isolated for `GAME-0194`; an aimed spatial guard must match a
  weapon strike direction rather than only height, timing or armour value.

## ACT-350 — Request mission-authorised recovery of an assigned vehicle

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while directly controlling a mission-assigned vehicle, the
  player requests the current ruleset's recover/repair or recovery-position
  transition so a damaged, spun or stranded vehicle can resume the attempt
  without the input itself granting omitted route progress.
- Includes: ordinary Recover Vehicle use during scoped BeamNG.drive Road
  Master; its clean current-mission restart remains the declared retry boundary.
- Excludes: player-scrubbed branchable rewind; loading a campaign save; free
  camera teleport; manually saving and loading an arbitrary home position.
- Parameters: vehicle, mission, recovery command, authorised recovery state,
  repair/rewind behaviour, retained checkpoint, elapsed-time treatment and
  full-restart alternative.
- Evidence: [BeamNG.drive decomposition](../games/a-f/beamng-drive.md).
- Novelty: first isolated for `GAME-0195`; prior recovery actions restore an
  avatar, checkpoint or editable history rather than one assigned soft-body
  vehicle under a still-unfinished driving mission.

## ACT-351 — Accept one field-work contract with borrowed machinery

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: from a current field-contract list, the player accepts one offer
  that fixes its task, assigned field, displayed reward and progress boundary,
  while electing to pay the declared deduction for employer-supplied compatible
  machines during that contract.
- Includes: accepting the scoped Farming Simulator 25 Fertilizing contract with
  `Borrow Items`.
- Excludes: accepting a preloaded road-cargo job; leasing a machine for general
  farm use; buying equipment; assigning an autonomous worker; previewing an
  offer without commitment.
- Parameters: offer set, task type, field, owner, reward, borrowing deduction,
  supplied fleet, active-contract slot, cancellation and settlement.
- Evidence: [Farming Simulator 25 decomposition](../games/a-f/farming-simulator-25.md).
- Novelty: first isolated for `GAME-0196`; the temporary supplied asset set is
  a compatible field-working fleet that must still be coupled and operated,
  not one already loaded delivery vehicle.

## ACT-352 — Couple and operate a powered vehicle implement

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player aligns a directly operated vehicle with a compatible
  implement, attaches or detaches its declared hitch and controls the coupled
  tool's raised/lowered and active/inactive working state while moving.
- Includes: coupling, lowering and activating the borrowed fertilizer spreader
  behind the supplied tractor in scoped Farming Simulator 25.
- Excludes: a permanently articulated cargo trailer; equipping a carried hand
  tool; attaching a weapon modification; cosmetic vehicle customisation;
  assigning an AI helper to operate the machinery.
- Parameters: vehicle, implement, hitch class, alignment, attachment state,
  power requirement, raise/lower state, activation, working width and input.
- Evidence: [Farming Simulator 25 decomposition](../games/a-f/farming-simulator-25.md).
- Novelty: first isolated for `GAME-0196`; attachment grants a controllable
  productive footprint whose state changes the traversed field rather than
  only making a trailer follow the tractor.

## ACT-353 — Consume a distinct food into a timed survival slot

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: consume one carried food whose type is distinct from the current
  active set, placing or refreshing its timed contribution in an eligible food
  slot so it can modify personal survival bounds.
- Includes: one scoped Valheim Meadows food entering one of three active slots.
- Excludes: eating to prevent starvation; drinking a healing potion; passive
  nutrition from inventory; replacing a food before digestion permits it.
- Parameters: food, slot, distinctness, remaining duration, replacement state,
  health, stamina and regeneration contribution.
- Evidence: [Valheim decomposition](../games/s-z/valheim.md).
- Novelty: first isolated for `GAME-0197`; unlike generic hunger restoration,
  the chosen set is a temporary three-part personal stat configuration.

## ACT-354 — Read a world wayfinder to reveal a boss altar

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: interact with an addressed world wayfinder so its registered
  boss class reveals the nearest matching generated altar on the personal map.
- Includes: the scoped spawn-stone Eikthyr Vegvisir interaction in Valheim.
- Excludes: following an existing map marker; throwing a consumable bearing
  locator; discovering a landmark only by entering its local radius.
- Parameters: wayfinder, boss class, world seed, candidate altars, nearest
  eligible altar, player map and retained marker.
- Evidence: [Valheim decomposition](../games/s-z/valheim.md).
- Novelty: first isolated for `GAME-0197`; an authored fixed interaction maps
  one semantic target onto the nearest seed-generated destination.

## ACT-355 — Claim, throw or discard a spawned arena weapon

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during a live arena match, the player interacts with a reachable
  neutral weapon pickup to make it the fighter's active weapon, or commits a
  throw/drop input that returns the fighter to the unarmed command state.
- Includes: claiming and throwing Bödvar's spawned Sword or Hammer in the
  scoped Brawlhalla Stock match.
- Excludes: selecting a carried quickbar slot; looting a persistent inventory
  item; firing a throwable gadget; cosmetic weapon skins.
- Parameters: fighter, pickup, reach, compatible weapon, prior weapon, claim,
  throw direction, collision, expiry and resulting unarmed/armed state.
- Evidence: [Brawlhalla decomposition](../games/a-f/brawlhalla.md).
- Novelty: first isolated for `GAME-0198`; the arena object changes a
  character-owned fighting vocabulary but is not retained as inventory or a
  multi-slot loadout.

## ACT-356 — Commit a spot or directional fighting dodge

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while the live fighter is eligible, the player commits the dodge
  input in place or with one direction to request its protected movement and
  accept the resulting cooldown/reset state.
- Includes: grounded spot dodge and aerial spot/directional dodge in the scoped
  Brawlhalla Stock match.
- Excludes: passive evasion chance; holding opponent-relative guard; a
  prompted turn-based defence; a vehicle flip without invulnerability.
- Parameters: fighter, ground/air state, direction, startup, protection,
  displacement, cooldown, reset contact and follow-up action.
- Evidence: [Brawlhalla decomposition](../games/a-f/brawlhalla.md).
- Novelty: first isolated for `GAME-0198`; unlike a telegraphed prompt response,
  the dodge is a freely timed neutral, pressure or recovery commitment in a
  continuously repositionable duel.

## ACT-357 — Spend an earned driving burst

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while a directly controlled vehicle has accumulated an eligible
  temporary burst reserve, the player activates some or all of it to request a
  short tactical acceleration increase.
- Includes: spending Burst Nitrous during the scoped Need for Speed Unbound
  race or mandatory pursuit.
- Excludes: collecting a spatial boost pad; passive top-speed tuning; a fixed
  launch-control start; cosmetic exhaust effects.
- Parameters: vehicle, reserve, activation, consumed amount, acceleration,
  duration, grip/drift state and cancellation.
- Evidence: [Need for Speed Unbound decomposition](../games/m-r/need-for-speed-unbound.md).
- Novelty: first isolated for `GAME-0199`; the reserve is earned by live
  driving technique rather than collected as a fixed world object.

## ACT-358 — Intimidate, restrain or reposition one reachable civilian

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player addresses one reachable civilian with the currently
  legal heist command, ordering compliance, applying one finite restraint or
  directing an already compliant hostage to follow or stop.
- Includes: shouting a PAYDAY 2 Bank Heist civilian to the floor, tying that
  civilian with a cable tie and issuing follow or stay commands.
- Excludes: shooting a hostile; communicating a plan to a human teammate;
  automatic civilian panic; trading a hostage after custody.
- Parameters: civilian, distance, visibility, command, compliance, cable-tie
  stock, restraint, follow state and interruption.
- Evidence: [PAYDAY 2 decomposition](../games/m-r/payday-2.md).
- Novelty: first isolated for `GAME-0201`; one contextual authority channel
  changes a neutral witness into a spatially managed, finitely restrained
  hostage whose later state affects the police-response loop.

## ACT-359 — Lift, carry, throw or secure one heavy loot bag

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player takes one eligible bagged objective payload into the
  dedicated carry state, moves or throws it through the world and deposits it
  inside a compatible secure region.
- Includes: bagging a PAYDAY 2 Bank Heist cash bundle, carrying or throwing its
  money bag and loading it into the escape van.
- Excludes: collecting loose instant cash; equipping a weapon; moving an
  unconstrained physics prop; the later payout calculation.
- Parameters: loot source, bag identity, carrier, carry state, movement
  modifier, throw impulse, world position, secure region and credited state.
- Evidence: [PAYDAY 2 decomposition](../games/m-r/payday-2.md).
- Novelty: first isolated for `GAME-0201`; an objective object alternates
  between exclusive embodied carriage and recoverable world trajectory before
  a spatial deposit makes its value count.

## ACT-360 — Commit one legal pre-match spawn region

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: during a bounded match-preparation phase, the player selects one
  currently legal map region as the controlled participant's initial live
  position and accepts that commitment when the preparation countdown ends.
- Includes: Viper Ning's spawn-point selection before the scoped Wanchu Solo
  BOT Mode match.
- Excludes: exiting an aircraft in motion; choosing a later respawn; random
  insertion with no player selection; an account-level home location.
- Parameters: map, selectable region, current occupancy, selection, revision
  window, countdown and instantiated position.
- Evidence: [NARAKA: BLADEPOINT decomposition](../games/m-r/naraka-bladepoint.md).
- Novelty: first isolated for `GAME-0202`; an explicit preparation choice owns
  the first live position without an intervening flight or route traversal.

## ACT-361 — Fire one consumable grappling hook

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player aims one carried grappling charge at eligible terrain
  or a live combatant and fires it to request a tethered approach toward the
  selected target.
- Includes: NARAKA: BLADEPOINT Grappling Hook traversal, pursuit and escape.
- Excludes: a permanent unlimited grappling ability; pulling an object toward
  the player; grappling and silently neutralising an unaware target.
- Parameters: carried stock, aim mode, target, anchor, range, hit, pull,
  collision, cancellation and consumed charge.
- Evidence: [NARAKA: BLADEPOINT decomposition](../games/m-r/naraka-bladepoint.md).
- Novelty: first isolated for `GAME-0202`; a finite loot item creates a direct
  terrain- or opponent-targeted movement commitment inside the same match.

## ACT-362 — Engage or release one reachable climbing grip

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while a directly controlled body can reach compatible world
  surface and has usable stamina, the player holds the grip input to request
  continued attachment and aimed body movement, or releases it to detach.
- Includes: PEAK surface grabbing, climbing, ledge transfer and deliberate release.
- Excludes: ordinary walking; an animation-only ladder; unlimited automatic
  wall climbing; independently mapping two hands to separate buttons.
- Parameters: body, hand reach, surface, contact, aim, hold, stamina, pose,
  attachment, movement and release.
- Evidence: [PEAK decomposition](../games/m-r/peak.md).
- Novelty: first isolated for `GAME-0203`; freely targeted geometry becomes a
  continuously stamina-priced attachment rather than a fixed traversal link.

## ACT-363 — Deploy one carried climbing aid onto terrain

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one finite carried climbing aid and commits it
  against compatible reachable terrain to request a persistent anchor, line or
  rest point in the current expedition.
- Includes: placing a PEAK Rope Spool line or Piton for later climbing support.
- Excludes: firing a grappling hook that moves the user immediately; permanent
  construction; dropping an inert item; a pre-authored ladder.
- Parameters: item, carried stock, target surface, reach, placement, anchor,
  line, support, persistence and rejection.
- Evidence: [PEAK decomposition](../games/m-r/peak.md).
- Novelty: first isolated for `GAME-0203`; a disposable inventory object edits
  the current physics route without becoming a general building system.

## ACT-364 — Ignite a carried signal flare in an eligible region

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while carrying an ignitable signal item inside its declared
  activation region, the player lights it to request the associated rescue or
  terminal response and consumes its ordinary future use.
- Includes: lighting a PEAK Flare inside the PEAK region to call the helicopter.
- Excludes: firing a combat flare; entering an already open exit; a purely
  cosmetic emote; rescue triggered automatically by arrival.
- Parameters: item, carried state, region, ignition legality, signal, response,
  consumption and terminal eligibility.
- Evidence: [PEAK decomposition](../games/m-r/peak.md).
- Novelty: first isolated for `GAME-0203`; the run's retained signal supply is
  also the explicit final command that asks the rescue system to settle.

## ACT-365 — Select one eligible lifestyle focus

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player chooses one currently available focus inside the
  controlled character's lifestyle, replacing its focus-level passive effects
  while preserving the broader character state.
- Includes: selecting one Diplomacy focus for Petty King Murchad in the scoped
  Crusader Kings III tutorial.
- Excludes: spending a perk point; changing culture; choosing a game mode.
- Parameters: character, lifestyle, available focus, current focus, passive
  effects and switch condition.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; a character-owned development track
  exposes one replaceable passive stance before campaign time advances.

## ACT-366 — Propose one eligible political marriage

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects two eligible characters and submits one
  ordinary marriage arrangement whose disclosed acceptance and relationship
  rules determine whether it can settle.
- Includes: arranging Murchad's prompted base-game tutorial marriage.
- Excludes: Grand Weddings; automatic romance; births or succession; cosmetic
  partner selection.
- Parameters: proposer, candidates, marriage type, doctrine, kinship,
  acceptance, alliance expectation and confirmation.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; a roster comparison directly submits
  a persistent family-and-diplomacy state transition.

## ACT-367 — Appoint a councillor and assign a council task

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player fills one legal council office with an eligible
  character or selects one task and target that the appointed office can pursue.
- Includes: the base-game offices and instructed tasks exposed in Murchad's
  tutorial.
- Excludes: changing a feudal contract; hiring a court position from DLC;
  directly resolving the task's effect.
- Parameters: office, candidate, skill, appointment, task, target and current
  assignment.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; one person is bound to a typed realm
  office and a separately chosen time-driven operation.

## ACT-368 — Declare war with an available casus belli

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects one legal target and available casus belli,
  reviews its objective, costs and settlement effects, then commits both realms
  to the resulting war.
- Includes: declaring the instructed Desmond war in the Crusader Kings III
  Murchad tutorial.
- Excludes: an unbounded attack with no legal cause; choosing battle tactics;
  enforcing demands after the war is won.
- Parameters: attacker, defender, casus belli, target title, objective, cost,
  truce, allies and declared effects.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; a title relation and explicit legal
  predicate configure the later military contest and its possible transfer.

## ACT-369 — Raise or disband realm troops at a rally point

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player orders currently available levies and men-at-arms to
  gather at a legal rally point, or releases an eligible raised army back into
  its realm contributions.
- Includes: raising Murchad's available tutorial army for the Desmond war.
- Excludes: recruiting a new regiment; moving the gathered army; a fixed
  scenario army that exists without realm obligations.
- Parameters: realm, contribution, troop class, rally point, gathering time,
  raised army, maintenance and disband eligibility.
- Evidence: [Crusader Kings III decomposition](../games/a-f/crusader-kings-iii.md).
- Novelty: first isolated for `GAME-0204`; dispersed feudal obligations become
  one temporary controllable map formation through a player-selected muster.

## ACT-370 — Focus a sensory mode and inspect highlighted evidence

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player sustains a character-centred investigative sense,
  follows its locally exposed trace and inspects one reachable highlighted clue
  to submit that evidence to the current authored investigation.
- Includes: using Witcher Senses to inspect the attacked camp, footprints,
  griffin nest and corpse evidence in The Beast of White Orchard.
- Excludes: automatically revealing every future clue; reading an external
  walkthrough; a detector whose signal identifies only physical proximity.
- Parameters: sense state, search area, highlight, clue, trace, reach,
  inspection, retained fact and next objective.
- Evidence: [The Witcher 3: Wild Hunt decomposition](../games/s-z/the-witcher-3-wild-hunt.md).
- Novelty: first isolated for `GAME-0205`; an embodied focus exposes an
  authored evidence trail whose individual inspections advance a quest.

## ACT-371 — Normal Summon or Normal Set one monster

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during an eligible own Main Phase, the player places one legal
  monster from hand face-up in Attack Position as a Normal Summon or face-down
  in Defense Position as a Normal Set and spends the shared turn allowance.
- Includes: an ordinary Level 4 or lower monster in Tutorial chapter `10003`.
- Excludes: a Special, Flip or effect-directed Summon; resolving an attack.
- Parameters: card, level, Tribute, zone, position, turn allowance and effect.
- Evidence: [Yu-Gi-Oh! Master Duel decomposition](../games/s-z/yu-gi-oh-master-duel.md).
- Novelty: first isolated for `GAME-0206`; two distinct visible/concealed field
  entries compete for one recurrent own-turn placement allowance.

## ACT-372 — Commit one procedure-based Special Summon

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player declares one currently legal Special Summon procedure,
  selects every required material or source and commits those objects so the
  matching monster can enter its legal field zone and position.
- Includes: reachable Synchro, Xyz or Link Summons from the chapter `10003`
  five-card Extra Deck.
- Excludes: a Normal/Tribute Summon; an automatic card-effect Summon with no
  player-selected procedure; deck construction.
- Parameters: procedure, monster, materials, levels, ratings, source, zone and position.
- Evidence: [Yu-Gi-Oh! Master Duel decomposition](../games/s-z/yu-gi-oh-master-duel.md).
- Novelty: first isolated for `GAME-0206`; public field objects are consumed
  under a typed relation to admit one matching Extra Deck object.

## ACT-373 — Set one Spell or Trap from hand

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during an eligible Main Phase, the player places one Spell or
  Trap from hand face-down into an open compatible zone without resolving its
  text.
- Includes: setting `Ballista Squad`, `Call of the Haunted` or `Skill Successor`
  in the fixed Tutorial packet.
- Excludes: activating a card; Normal Setting a monster; placing a public
  continuous object directly face-up.
- Parameters: card type, zone, concealed state, set turn and later eligibility.
- Evidence: [Yu-Gi-Oh! Master Duel decomposition](../games/s-z/yu-gi-oh-master-duel.md).
- Novelty: first isolated for `GAME-0206`; one visible hand card becomes
  concealed board occupancy whose response authority is deliberately delayed.

## ACT-374 — Activate one eligible card or effect

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player declares one currently activatable Spell, Trap or
  monster effect, pays its stated costs and selects required targets so the
  activation becomes the first unresolved Chain Link.
- Includes: activating a fixed-packet Normal Spell, a previously Set Trap or an
  eligible monster effect.
- Excludes: resolving the text immediately; responding as a later Chain Link;
  passive continuous text without an activation.
- Parameters: source, effect, timing, cost, target, Spell Speed and Chain Link.
- Evidence: [Yu-Gi-Oh! Master Duel decomposition](../games/s-z/yu-gi-oh-master-duel.md).
- Novelty: first isolated for `GAME-0206`; activation commits card-specific
  predicates before either side knows the completed response chain.

## ACT-375 — Add one eligible response as the next Chain Link

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after another effect is activated, the responding player chooses
  one legal equal-or-faster response, pays its costs and appends it as the next
  numbered Chain Link before any linked effect resolves.
- Includes: chaining an eligible Trap, Quick-Play Spell or Quick Effect in the
  scoped Duel.
- Excludes: activating Spell Speed 1 in response; adding a link while a
  completed Chain is resolving; an MTG priority pass.
- Parameters: responder, prior link, response, speed, cost, target and link number.
- Evidence: [Yu-Gi-Oh! Master Duel decomposition](../games/s-z/yu-gi-oh-master-duel.md).
- Novelty: first isolated for `GAME-0206`; response legality depends on the
  immediately preceding link's typed speed before whole-chain settlement.

## ACT-376 — Declare one eligible monster attack

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during a legal Battle Phase, the player selects one eligible
  face-up Attack Position monster and commits its ordinary attack against one
  legal opposing monster or directly when the field permits.
- Includes: each separate chapter `10003` attack declaration.
- Excludes: selecting a simultaneous attacker subset; choosing a blocker;
  resolving battle damage.
- Parameters: attacker, used-attack flag, target, direct eligibility, phase and responses.
- Evidence: [Yu-Gi-Oh! Master Duel decomposition](../games/s-z/yu-gi-oh-master-duel.md).
- Novelty: first isolated for `GAME-0206`; combat begins as one sequential
  attacker-target commitment rather than a simultaneous army declaration.

## ACT-377 — Change one eligible monster's battle position

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during an eligible own Main Phase, the player changes one monster
  between face-up Attack and Defense Position or Flip Summons an eligible
  face-down Defense Position monster.
- Includes: a legal manual position change or Flip Summon in chapter `10003`.
- Excludes: a position change caused by card text; Normal Setting from hand;
  declaring an attack.
- Parameters: monster, current position, destination, set turn, attack history and prior change.
- Evidence: [Yu-Gi-Oh! Master Duel decomposition](../games/s-z/yu-gi-oh-master-duel.md).
- Novelty: first isolated for `GAME-0206`; one retained field object changes
  its offence/defence and disclosure role under per-turn history rules.

## ACT-378 — Sharpen the equipped close-range weapon

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player commits an exposed whetstone interaction on the
  equipped close-range weapon so a completed maintenance animation restores
  its current sharpness gauge while live combat and quest time continue.
- Includes: sharpening `Hunter's Knife I` during the scoped Monster Hunter:
  World Great Jagras assignment.
- Excludes: consuming a finite healing item; smithy upgrading; automatically
  restoring sharpness after combat; repairing a weapon's persistent durability.
- Parameters: weapon, whetstone, current sharpness, restored sharpness,
  animation, interruption, combat state and quest clock.
- Evidence: [Monster Hunter: World decomposition](../games/m-r/monster-hunter-world.md).
- Novelty: first isolated for `GAME-0207`; field maintenance restores a
  repeatedly degraded combat resource through a live interruptible commitment
  without consuming the maintenance tool.

## ACT-379 — Ram one reachable hostile vehicle

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: while directly driving, the player commits the controlled
  vehicle's trajectory into one reachable hostile vehicle to request a
  damaging contact and accept the resulting loss of speed, position and
  vehicle condition.
- Includes: ramming a House Enforcer during the scoped Need for Speed Payback
  `The Highway Heist` wreck stages.
- Excludes: accidental traffic contact; firing a mounted weapon; a Rocket
  League bump whose target returns after a timed demolition respawn; a
  cinematic crash with no player-authored approach.
- Parameters: controlled vehicle, hostile target, relative speed, contact
  angle, road edge, damage, knockback, recovery line and objective credit.
- Evidence: [Need for Speed Payback decomposition](../games/m-r/need-for-speed-payback.md).
- Novelty: first isolated for `GAME-0208`; direct vehicle control becomes a
  deliberate contact attack whose positional cost competes with a moving
  mission target.

## ACT-380 — Load or unload selected units through a transport

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player selects eligible ground units and commits them to
  enter one reachable transport, or selects the occupied transport and orders
  its retained passengers to return to traversable ground at an eligible
  destination.
- Includes: loading Swedish peasants and soldiers into the ferry and unloading
  them on the opposite river shore in Cossacks 3 `War Ruse — Peace`.
- Excludes: moving the ferry itself; an automatic reinforcement landing; a
  vehicle entered by one directly controlled avatar; units teleported between
  fixed endpoints.
- Parameters: selected units, transport, shore, ramp, reachability, capacity,
  embark interval, passenger state, destination and unload interval.
- Evidence: [Cossacks 3 decomposition](../games/a-f/cossacks-3.md).
- Novelty: first isolated for `GAME-0209`; one command moves a selected RTS
  group between ground authority and retained transport containment.

## ACT-381 — Apply one contextual held-item operation to another item

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player selects one carried item in hands and one compatible
  inventory or world item, chooses an exposed contextual operation and commits
  their combination, division, loading, repair or simple crafting action.
- Includes: DayZ inventory `Combine`, split, load-ammunition, repair and
  two-item hand-crafting interactions within one fresh-spawn Chernarus life.
- Excludes: selecting an abstract recipe from a detached crafting queue;
  equipping unchanged loot; consuming an item directly; automatic contact
  pickup; arbitrary combinations the current item pair does not expose.
- Parameters: item in hands, second item, operation, quantity, compatibility,
  duration, interruption, consumption, condition and output.
- Evidence: [DayZ decomposition](../games/a-f/dayz.md).
- Novelty: first isolated for `GAME-0210`; DayZ makes the currently held item
  and a second concrete item define the available transformation before the
  system resolves its result.

## ACT-382 — Address nearby survivors through local voice or gesture

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the player deliberately emits speech through the current
  proximity channel or performs a visible body gesture toward nearby human
  survivors while shared-world control continues.
- Includes: DayZ proximity voice and emotes used to greet, warn, negotiate,
  surrender or misdirect a locally perceived stranger.
- Excludes: a bounded teammate-only tactical channel; an external voice
  service; automatic pain or illness vocalisation; communication that
  guarantees truth, alliance or response.
- Parameters: voice level, spatial range, occlusion, gesture, body state,
  visible hands, recipients, delay and response.
- Evidence: [DayZ decomposition](../games/a-f/dayz.md).
- Novelty: first isolated for `GAME-0210`; communication is a local embodied
  signal to potentially hostile strangers rather than a trusted team channel.

## ACT-383 — Hold or release a sustained melee guard

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: during live melee, the player holds the equipped weapon in a
  persistent guard or releases that request, accepting continuing guard-meter
  loss and a possible exposed state when incoming strikes exhaust it.
- Includes: holding and releasing Cal Kestis's lightsaber block during the
  scoped Bogano visit in STAR WARS Jedi: Fallen Order.
- Excludes: an opponent-relative high/low fighting-game guard; choosing an
  attack direction for a directional block; a single timed parry input; passive
  armour or a turn-based Defend command.
- Parameters: weapon, hold, release, incoming strike, guard meter, depletion,
  exposed state and difficulty.
- Evidence: [STAR WARS Jedi: Fallen Order decomposition](../games/s-z/star-wars-jedi-fallen-order.md).
- Novelty: first isolated for `GAME-0213`; an undirected sustained weapon guard
  remains a player-held request whose finite stability can fail, rather than a
  direction-matching block or a single reactive timing window.

## ACT-384 — Toggle a vehicle speed limiter

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while directly operating a road vehicle, the player toggles a
  bounded maximum-speed controller that limits further acceleration above its
  configured cap without taking away steering, braking or route choice.
- Includes: toggling the `F5` speed limiter in the scoped Mafia (2002) Chapter
  2 taxi packet to reduce observed speeding risk.
- Excludes: autonomous route following; a permanent engine upgrade; an event
  difficulty setting; ordinary braking; a cruise-control target that actively
  maintains an arbitrary selected speed.
- Parameters: controlled vehicle, limiter state, configured cap, current speed,
  throttle request, road limit, transmission and control binding.
- Evidence: [Mafia (2002) decomposition](../games/m-r/mafia-2002.md).
- Novelty: first isolated for `GAME-0214`; the player accepts a reversible
  acceleration ceiling as a live compliance tool while retaining complete
  spatial control of the taxi.

## ACT-385 — Throw or recall one role-bound reusable nail

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the assigned player aims one currently available reusable nail
  at a reachable compatible world target and throws it, or commands one already
  deployed nail to detach and return to the available hand-held set.
- Includes: Cody throwing and instantly recalling his bounded nail set during
  the hammer-and-nails packet of It Takes Two's `The Shed`.
- Excludes: firing expendable ammunition at a hostile; placing an inventory
  building part; recalling an autonomous companion; picking up generic loot.
- Parameters: role, nail identity, available set, aim, target, travel, hit,
  deployed state, recall input, return delay and rejection.
- Evidence: [It Takes Two decomposition](../games/g-l/it-takes-two.md).
- Novelty: first isolated for `GAME-0215`; one direct input reversibly moves a
  named reusable tool between hand availability and several persistent world
  roles.

## ACT-386 — Strike a reachable fixture with a role-bound hammer

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: the assigned player commits a close hammer swing against one
  compatible reachable world fixture to request its local impact operation.
- Includes: May striking marked buttons, route locks, Toolbox locks and the
  authored launch fixture in It Takes Two's bounded `The Shed` packet.
- Excludes: an aimed attack against a hostile body; ordinary unarmed
  interaction; construction repair; a cosmetic swing with no fixture response.
- Parameters: role, hammer, reach, fixture class, swing timing, contact,
  impulse, accepted operation and rejection.
- Evidence: [It Takes Two decomposition](../games/g-l/it-takes-two.md).
- Novelty: first isolated for `GAME-0215`; a permanent role tool owns typed
  traversal and boss-fixture impacts without becoming general melee combat.

## ACT-387 — Confirm one eligible persistent first class transfer

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: after a persistent character satisfies the declared first-class
  prerequisites, the player selects one compatible destination class and
  confirms the exclusive transfer for that character.
- Includes: a level-20 Lineage II Live Human Fighter with completed `Path of
  Destiny - Beginning` confirming Warrior on Chronos.
- Excludes: choosing the starting race/class at creation; changing a temporary
  team-spawn role; allocating a skill point; later paid class change.
- Parameters: character, current class, level, quest flag, offered classes,
  selected class, confirmation and reversibility.
- Evidence: [Lineage II decomposition](../games/g-l/lineage-ii.md).
- Novelty: first isolated for `GAME-0219`; an earned quest-and-level-gated
  choice permanently replaces the starting class rather than configuring it.

## ACT-388 — Build or repair one authored battlefield Fortification

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the player addresses one visible authored construction outline,
  equips the compatible field tool and sustains the build or repair interaction
  until the outline becomes its declared usable defensive or supply structure.
- Includes: a Battlefield V soldier using the toolbox to build or repair an
  Arras trench, sandbag, barrier, tank stopper or resupply station.
- Excludes: unrestricted free-form building; Siege wall reinforcement from
  finite team stock; repairing a vehicle; destroying existing geometry.
- Parameters: outline, structure type, tool, reach, progress, interruption,
  repair state, completion and resulting world entity.
- Evidence: [Battlefield V decomposition](../games/a-f/battlefield-v.md).
- Novelty: first isolated for `GAME-0220`; a live combatant converts an
  authored empty silhouette into route, cover or sustain state without
  spending a carried construction inventory.

## ACT-389 — Spend squad authority on one typed Reinforcement call

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: the current squad leader selects one available Reinforcement,
  chooses its required battlefield target and confirms expenditure of the
  squad's shared earned points to request its delivery.
- Includes: Battlefield V squad-leader calls for a supply drop, smoke barrage
  or eligible strike after the squad earns sufficient requisition points.
- Excludes: throwing a carried grenade; using an equipped personal gadget;
  spending private account currency; an automatic scripted air strike.
- Parameters: squad, leader, shared points, option, cost, target, confirmation,
  delivery request and rejection.
- Evidence: [Battlefield V decomposition](../games/a-f/battlefield-v.md).
- Novelty: first isolated for `GAME-0220`; several players earn one live
  tactical budget but only their current leader may commit its typed spend.

## ACT-390 — Prepare focus and draw hand, then commit one duel draw

- Lifecycle: `Active`
- Claim status: `Observation`
- Evidence quality: `Corroborated`
- Confidence: `High`
- Definition: before a fixed-opponent firearm duel, the player concurrently
  keeps one focus reticle on the opponent and one represented hand near the
  holstered weapon, then commits the draw either before or in response to the
  opponent's visible draw.
- Includes: Silas preparing focus and hand speed against Pat Garrett in the
  first `Call of Juarez: Gunslinger` Story duel.
- Excludes: ordinary free aim with an already drawn weapon; selecting a fighter
  before a versus match; one-button quick-time prompt; automatic cutscene draw.
- Parameters: opponent, focus reticle, hand position, focus value, speed value,
  opponent cue, draw input, draw order and post-draw control.
- Evidence: [Call of Juarez: Gunslinger decomposition](../games/a-f/call-of-juarez-gunslinger.md).
- Novelty: first isolated for `GAME-0222`; one live preparation state requires
  two independently maintained pointing relations before a reaction-timed draw.

## ACT-391 — Strike an upgradeable reward object before claiming it

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: after a bounded encounter spawns a non-hostile reward object, the
  player aims ordinary attacks at that object to request changes to its reward
  level before committing the separate interaction that claims it.
- Includes: striking a Mystic Cube of Light and Darkness in Aion Classic before
  interacting to receive its enhanced-equipment reward.
- Excludes: attacking a hostile; opening an unchanged chest; damaging a fixture
  to clear a route; spending currency on a deterministic upgrade.
- Parameters: spawned object, attack, hit, current level, cap, interaction
  readiness, claim and resulting reward.
- Evidence: [Aion Classic decomposition](../games/a-f/aion-classic.md).
- Novelty: first isolated for `GAME-0223`; the combat input prepares a
  non-hostile reward source rather than dealing damage or opening it directly.

## ACT-392 — Directly pilot a cockpit starfighter

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: continuously command a first-person starfighter's throttle,
  pitch, yaw and roll to change its position and orientation through open
  three-dimensional space while retaining direct cockpit control.
- Includes: flying the fixed T-65B X-wing during `Form the Vanguard`.
- Excludes: choosing a destination on a map; commanding an autonomous squad;
  runway take-off; third-person ground driving; a non-interactive flight scene.
- Parameters: craft, throttle, pitch, yaw, roll, position, orientation,
  velocity, collision and control state.
- Evidence: [STAR WARS: Squadrons decomposition](../games/s-z/star-wars-squadrons.md).
- Novelty: first isolated for `GAME-0225`; continuous cockpit input directly
  composes four flight controls in unrestricted three-dimensional space.

## ACT-393 — Allocate starfighter power among three systems

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: while flying, redirect one shared starfighter power allocation
  among engines, laser weapons and shields, or restore the balanced allocation.
- Includes: the X-wing power controls taught in `Form the Vanguard`.
- Excludes: spending upgrade currency; selecting a permanent component;
  transferring shield charge between facings; activating one cooldown ability.
- Parameters: power budget, engines, lasers, shields, selected emphasis,
  balanced state, overcharge state and resulting subsystem performance.
- Evidence: [STAR WARS: Squadrons decomposition](../games/s-z/star-wars-squadrons.md).
- Novelty: first isolated for `GAME-0225`; one reversible live allocation
  changes three simultaneously relevant flight-combat subsystems.

## ACT-394 — Focus charged shields toward one starfighter facing

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: transfer existing deflector charge toward the front or rear
  facing of a shielded starfighter, or rebalance it, during direct flight.
- Includes: focusing the X-wing's shields front or rear in `Form the Vanguard`.
- Excludes: allocating reactor power to shields; rotating the craft to face an
  attack; repairing hull; raising a single undirected temporary barrier.
- Parameters: front charge, rear charge, total charge, selected facing,
  balance command, transfer rate and incoming hit direction.
- Evidence: [STAR WARS: Squadrons decomposition](../games/s-z/star-wars-squadrons.md).
- Novelty: first isolated for `GAME-0225`; the player redistributes one live
  defensive reserve between two spatially opposed damage interceptors.

## ACT-395 — Deploy one ready starfighter countermeasure

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: respond to an incoming guided-missile warning by releasing one
  available countermeasure charge at a chosen time to attempt to break the
  threat's lock or interception path.
- Includes: using Seeker Warheads from the fixed Mission 1 X-wing loadout.
- Excludes: dodging by steering alone; firing a missile at a target; a passive
  shield interception; changing the equipped countermeasure outside the mission.
- Parameters: warning, incoming missile, timing window, countermeasure type,
  ready state, finite charge, release and interception result.
- Evidence: [STAR WARS: Squadrons decomposition](../games/s-z/star-wars-squadrons.md).
- Novelty: first isolated for `GAME-0225`; a finite defensive projectile is
  committed against a specifically signalled homing threat during direct flight.

## ACT-396 — Request repair and resupply from an AI wingmate

- Lifecycle: `Active`
- Claim status: `Confirmed`
- Evidence quality: `Direct`
- Confidence: `High`
- Definition: issue the contextual single-player support request that directs
  an AI wingmate to deliver a repair-and-resupply payload to the player's
  current starfighter during the mission.
- Includes: requesting support from Gunny's U-wing in `Form the Vanguard`.
- Excludes: docking at a station; consuming a carried repair kit; a human
  teammate choosing support independently; automatic regeneration.
- Parameters: player craft, AI wingmate, request availability, delivery route,
  payload, hull restoration, ordnance replenishment and completion feedback.
- Evidence: [STAR WARS: Squadrons decomposition](../games/s-z/star-wars-squadrons.md).
- Novelty: first isolated for `GAME-0225`; a direct contextual command invokes
  mobile AI logistics without leaving the active starfighter encounter.
