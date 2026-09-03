---
game_id: GAME-0040
slug: carto
game_title: Carto
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0040
gene_ids:
  action:
    - ACT-008
    - ACT-056
  system:
    - SYS-074
  constraint:
    - CON-058
    - CON-088
  information:
    - INF-001
  objective:
    - OBJ-026
  time:
    - TIM-002
---

# Game: Carto

## Analysis scope

- Version / ruleset: Sunhead Games' 2020 base game, scoped to one ordinary
  early acquired-map-fragment task with square pieces and no chapter-specific
  transformation rule.
- Included: direct avatar walking; opening the map; selecting an acquired
  fragment; translating and quarter-turning it; moving the avatar-bearing
  fragment; matching terrain patterns on every touching edge; preserving one
  instance of each fragment; immediate map-to-world topology propagation;
  returning to exploration; walking across a newly connected boundary to the
  designated person or place; self-paced revision.
- Excluded: dialogue interpretation, inventory riddles, pattern-triggered new
  fragment manifestation, forest-loop and desert cycling variants, underground
  map coupling, chapter-wide collection, secrets, achievements and platform
  presentation.
- Direct-play status: not conducted. Humble Games' PlayStation developer /
  publisher account establishes map rearrangement and immediate world change.
  Game Informer, Nintendo Life, Film Stories and Nintendo World Report
  independently corroborate square-fragment translation / rotation, typed-edge
  legality, fragment-relative geography, avatar-bearing tile movement and
  traversal into newly connected areas.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CAR-001` | The scoped world consists of persistent square map fragments whose terrain and contents correspond to traversable world regions | Confirmed | Corroborated | High | P1, S1–S4 |
| `CAR-002` | The player directly walks Carto within and across currently connected world regions | Confirmed | Corroborated | High | S1–S4 |
| `CAR-003` | In map view the player can pick up an acquired fragment, move it and rotate it in quarter turns before placing it | Confirmed | Corroborated | High | S1–S4 |
| `CAR-004` | A fragment containing Carto may itself be relocated, carrying the avatar to the corresponding new world position | Confirmed | Corroborated | High | S1, S3 |
| `CAR-005` | Touching fragment edges are legal only when their displayed terrain patterns are compatible, such as forest-to-forest or road-to-road | Confirmed | Corroborated | High | S1–S4 |
| `CAR-006` | Each acquired fragment remains one unique reusable object rather than being consumed or copied on placement | Confirmed | Corroborated | High | P1, S1–S4 |
| `CAR-007` | A valid map rearrangement immediately changes the traversed world's region positions and boundary connections | Confirmed | Direct | High | P1, S1, S3, S4 |
| `CAR-008` | Terrain, structures and occupants remain attached to their fragments when the world topology changes | Confirmed | Corroborated | High | S1, S3, S4 |
| `CAR-009` | Connecting a formerly distant fragment creates a traversable border that Carto can cross after leaving map view | Confirmed | Corroborated | High | P1, S1, S2, S4 |
| `CAR-010` | The scoped task progresses when Carto reaches the declared newly connected person or place, not merely when a map shape is displayed | Confirmed | Corroborated | High | P1, S2, S4 |
| `CAR-011` | Acquired fragments, typed edges, current arrangement, avatar location and resulting world are inspectable; no random transition changes them | Observation | Corroborated | High | CAR-001–CAR-010 |
| `CAR-012` | Map editing and walking have no forced clock or autonomous world progression in the scoped task | Observation | Corroborated | High | P1, S1–S4 |
| `CAR-013` | Carto's map is authoritative state, not a passive representation or a temporary visual composition | Observation | Corroborated | High | CAR-004, CAR-007–CAR-009 |

## Basic data

- Release / origin: Sunhead Games developed Carto; Humble Games published it
  for PC, PlayStation 4, Xbox One and Nintendo Switch on 27 October 2020.
- Platform or physical form: single-player top-down puzzle adventure alternating
  direct avatar exploration with a manipulable overview map.
- Puzzle family: authoritative map-fragment topology editing.
- Primary / publisher source:
  - **[P1]** [Humble Games / Sunhead announcement on PlayStation Blog](https://blog.playstation.com/2020/07/01/introducing-carto-a-charming-innovative-puzzle-adventure-coming-to-ps4/),
    stating that rearranging map pieces visibly changes the world and connecting
    missing pieces reveals new lands.
- Contemporary corroboration:
  - **[S1]** [Game Informer review](https://gameinformer.com/review/carto/carto-review-putting-the-pieces-together),
    documenting square pieces, matching road / river / forest borders,
    rotation, real-time world alteration and relocation of the occupied tile.
  - **[S2]** [Nintendo Life review](https://www.nintendolife.com/reviews/switch-eshop/carto),
    documenting side-pattern matching, fragment acquisition, exploration and
    route-building through arranged tiles.
  - **[S3]** [Film Stories review](https://filmstories.co.uk/reviews/carto-review-mapping-all-over-the-world/),
    distinguishing a map that defines the world from one that merely depicts it
    and confirming immediate world reflection and matching scenery.
  - **[S4]** [Nintendo World Report review](https://www.nintendoworldreport.com/review/55335/carto-switch-review),
    corroborating that moved fragments restructure the world, open paths and
    expose new areas.
- Claim IDs: `CAR-001`–`CAR-013`.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. Outside map view, the player walks
  Carto directly through each region and across currently connected boundaries.
- `ACT-056` — reposition and rotate persistent map fragment. The player picks
  one acquired square piece, translates it to a new map coordinate and chooses
  among quarter-turn orientations, including for the occupied fragment.
- `ACT-026` is absent: there is no mandatory supply head consumed once into an
  expanding landscape. `ACT-033` is absent because fragments are not fixed-slot
  framed illustrations; they are persistent authoritative world regions with
  rotation and open reconfiguration.
- Claim IDs: `CAR-002`–`CAR-004`, `CAR-006`.

### System Behaviour Genes

- `SYS-074` — authoritative map-to-world topology propagation. A legal map
  edit relocates and rotates each corresponding world region, preserves its
  attached terrain / occupants and rebuilds cross-fragment traversal edges.
- `SYS-044` is absent: Carto does not temporarily align depicted scenes so one
  element advances across a composition. The entire navigable world topology
  persistently adopts the edited map arrangement.
- Resolution order: select fragment and proposed transform; test every new
  touching edge for terrain compatibility; commit the unique fragment to the
  new arrangement; transform its world-region coordinates and attached
  contents; rebuild matching boundary traversal; expose the updated map and
  world for the next action.
- Claim IDs: `CAR-001`, `CAR-004`, `CAR-007`–`CAR-009`, `CAR-013`.

### Constraint Genes

- `CON-058` — typed shared-edge compatibility. Any two touching square edges
  must display compatible continuation types: forest meets forest, river meets
  river, road meets road and ordinary land / water patterns meet their accepted
  counterparts.
- `CON-088` — unique persistent map-fragment inventory. Only the map pieces
  acquired so far are available; each exists once, retains its content and can
  occupy only one position at a time despite unlimited rearrangement.
- `CON-001` is absent: the editable map does not expose a fixed persistent set
  of addressable board positions. `CON-056` is absent because edits can detach,
  relocate and reconnect existing fragments rather than monotonically add one
  tile along a single frontier.
- Scarce strategic resources: unique fragment identities, compatible boundary
  segments, orientations and the cross-fragment corridors needed to connect
  Carto's current region with the target.
- Claim IDs: `CAR-001`, `CAR-003`–`CAR-006`, `CAR-009`.

### Information Genes

- `INF-001` — fully visible current state. The map view exposes all currently
  acquired fragments, terrain patterns, their arrangement and Carto's fragment;
  exploration exposes the corresponding current world without hidden random
  topology changes.
- The map-to-world relationship is causal system state (`SYS-074`), not a
  separate future preview: the overview shows the topology that the world has
  already adopted.
- Claim IDs: `CAR-001`, `CAR-007`, `CAR-011`, `CAR-013`.

### Objective Genes

- `OBJ-026` — reach designated traversable world location. The bounded task
  requires connecting the target fragment or resident to Carto's current
  component and then walking the avatar there.
- `OBJ-004` is absent because displaying one specific map arrangement is not by
  itself completion; several layouts may create the required traversal.
  `OBJ-022` is absent because there is one required avatar and no fixed exit /
  all-actor evacuation condition.
- Claim IDs: `CAR-009`, `CAR-010`.

### Time Genes

- `TIM-002` — self-paced sequential action. The player can pause indefinitely
  in exploration or map view, revise fragments repeatedly and traverse only
  when ready; no system clock mutates the scoped state.
- Immediate topology propagation is deterministic post-action resolution, not
  `TIM-003` forced real-time progression.
- Claim IDs: `CAR-007`, `CAR-012`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Two acquired fragments are separated | Move one so matching plain edges touch | Placement commits and a traversable world boundary appears | map edit plus topology propagation | `CAR-003`, `CAR-005`, `CAR-007`, `CAR-009` |
| Proposed touching edges show forest versus incompatible water | Place fragments adjacent | The adjacency cannot be committed as a connected join | typed edge legality | `CAR-005` |
| One river fragment faces the wrong direction | Rotate it one quarter turn and place | Its world region rotates and the river boundary now aligns | persistent orientation affects world | `CAR-003`, `CAR-007` |
| Carto stands inside a movable fragment | Relocate that fragment beside the target piece | Carto and fragment-local contents retain their local positions in the relocated region | entity anchoring and occupied-piece permission | `CAR-004`, `CAR-008` |
| Target fragment becomes adjacent through matching edges | Exit map view and walk across seam | Direct traversal reaches the formerly disconnected region | topology is authoritative, not visual | `CAR-002`, `CAR-009`, `CAR-013` |
| Same fragment is moved again | Commit a different legal placement | Prior instance is removed from its old coordinate; no duplicate remains | unique persistent inventory | `CAR-006` |
| Target is connected but Carto remains elsewhere | Leave map view without walking there | Task remains incomplete until avatar arrival / interaction | objective is embodied reachability | `CAR-010` |

## Strategic and experiential structure

- Local decision: choose one fragment, its quarter-turn orientation and a legal
  compatible neighbour without losing a useful existing boundary.
- Medium-term planning: preserve or rebuild a connected component between
  Carto and the target while transporting useful terrain junctions to the
  required sides.
- Long-term structure: treat the overview as the actual topology, repeatedly
  reshaping it so direct avatar traversal can realize the requested sequence of
  places rather than searching a fixed world.
- Common heuristics: work backward from the target's needed entry edge; rotate
  constrained river / road pieces first; move the occupied fragment when it
  avoids long walking; distinguish fragment content from absolute coordinates.
- Failure attribution: rejected edge joins and visible disconnected components
  expose whether the obstacle is compatibility, orientation or insufficient
  fragment inventory rather than hidden randomness.
- Player-trust factors: edge classification, fragment-local entity anchoring,
  occupied-piece relocation, coordinate rotation and cross-seam walkability
  must remain consistent.
- Claim IDs: `CAR-001`–`CAR-013`.

## Replay and variation

- What changes between tasks: acquired fragment set, terrain-edge patterns,
  target location and excluded chapter-specific map rules.
- Randomness or procedural generation: none in the scoped authored task.
- Multiple viable strategies: several legal layouts or sequences may connect
  the same regions, and the player may relocate Carto's current fragment or
  walk through intermediate fragments.
- Typical replay motive: revise an inefficient configuration, discover a
  different legal route or complete optional fragments / secrets outside scope.
- Claim IDs: `CAR-001`, `CAR-003`–`CAR-012`.

## Adjacent systems and history

- Dorfromantik shares typed edge comparison, visible landscapes and rotatable
  tiles. It consumes a mandatory supply head into a growing scored landscape;
  Carto repeatedly rearranges unique persistent fragments and propagates their
  arrangement into an embodied traversable world.
- Gorogoa moves intact illustrated panels among four slots and temporarily
  composes their depicted spaces. Carto uses an open map layout whose fragments
  are authoritative persistent world regions rather than scene windows.
- Patrick's Parabox changes a recursive containment graph through local pushes.
  Carto directly edits a flat region-adjacency graph in overview and then walks
  the resulting world.
- Sokoban shares direct avatar navigation, visible state and self-paced spatial
  planning but treats one immutable floor plan as the arena.
- Claim IDs: `CAR-001`–`CAR-013`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-056` | direct walking plus fragment translation / rotation |
| System Behaviour | `SYS-074` | authoritative map-to-world topology propagation |
| Constraint | `CON-058`, `CON-088` | matching terrain edges and unique fragments |
| Information | `INF-001` | visible current map and world state |
| Objective | `OBJ-026` | reach newly connected person or place |
| Time | `TIM-002` | self-paced editing and traversal |

Canonical signature:

`ACT-008,ACT-056; SYS-074; CON-058,CON-088; INF-001; OBJ-026; TIM-002`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `39` (`GAME-0001`–`GAME-0039`).
- Exact genome matches: none.
- Tied near matches: `GAME-0006` — Sokoban (`3 / 14 = 0.214286`).
- Supported combination subsets: `COMB-0040`.
- Scan date: 2026-08-12.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0006`.

## Combination record

- Registered `COMB-0040` — authoritative persistent map-fragment traversal.
- Its five-gene proper subset isolates the edit / propagate / traverse target
  loop without requiring generic visibility, self-paced timing or the particular
  direct-navigation implementation.

## Taxonomy impact

- Registry changes: four stable genes added: `ACT-056`, `SYS-074`, `CON-088`
  and `OBJ-026`; four existing genes reused.
- `CON-058` now recurs and receives representation-neutral wording across
  Dorfromantik's scored hex-edge matching and Carto's mandatory square-edge
  legality.
- `ACT-026`, `ACT-033` and `SYS-044` remain bounded; no merge, split or earlier
  signature rewrite is justified.

## Negative results

- `ACT-026` is rejected because fragments persist and can be moved again rather
  than consuming a mandatory supply head. `ACT-033` is rejected because the
  map has no fixed display slots and rotations change world orientation.
- `SYS-044` is rejected because the edit persistently rebuilds the entire
  traversable topology instead of creating a temporary depicted continuation.
- `CON-001` and `CON-056` are rejected because map positions are not fixed and
  editing is not monotonic adjacent-frontier growth.
- `OBJ-004` is rejected because avatar arrival, not one exact map arrangement,
  completes the scoped task.
