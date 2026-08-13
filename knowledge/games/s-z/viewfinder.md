---
game_id: GAME-0041
slug: viewfinder
game_title: Viewfinder
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0041
gene_ids:
  action:
    - ACT-008
    - ACT-044
    - ACT-057
  system:
    - SYS-036
    - SYS-075
    - SYS-076
  constraint:
    - CON-089
  information:
    - INF-001
  objective:
    - OBJ-022
  time:
    - TIM-003
    - TIM-007
---

# Game: Viewfinder

## Analysis scope

- Version / ruleset: Sad Owl Studios' 2023 base game, scoped to one ordinary
  early supplied-photograph puzzle after rewind is available and before the
  player receives a camera.
- Included: first-person walking and jumping; picking up one found photograph;
  holding, positioning and rotating its plane in perspective; committing the
  image; converting represented content into solid interactive 3D geometry;
  deleting intersected world geometry behind the placement; walking into or on
  the result; falling; rewinding to before the placement; choosing a replacement
  pose; reaching and activating the fixed teleporter.
- Excluded: taking new photographs, stationary or portable cameras,
  photocopiers, image duplication, batteries, multiple-image recursion,
  protected purple geometry, paintings and other media variants, timed final
  content, optional puzzles, narrative, collectibles, achievements and
  platform presentation.
- Direct-play status: not conducted. Two Sad Owl / Thunderful creator-publisher
  accounts establish image placement, destruction, rewind and release context.
  Game Informer, PC Gamer, The Guardian, Push Square and GamesRadar independently
  corroborate perspective placement, 3D instantiation, overwrite, traversal,
  finite supplied images, body motion and teleporter completion.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `VWF-001` | The player directly walks and jumps a first-person avatar through the current three-dimensional level | Confirmed | Corroborated | High | P1–P3, S1–S5 |
| `VWF-002` | Early puzzles provide a finite set of found source photographs before camera capture is introduced | Confirmed | Corroborated | High | S1, S4, S5, R1 |
| `VWF-003` | The player picks up a supplied image, holds its plane in the world, changes its position and orientation and commits the chosen pose | Confirmed | Corroborated | High | P1, S2–S5, R1 |
| `VWF-004` | The held image's apparent perspective and rotation determine the scale and orientation of the committed spatial result | Confirmed | Corroborated | High | P2, S2–S5 |
| `VWF-005` | Committing the image makes its depicted contents solid, interactive 3D geometry that the avatar can enter or walk on | Confirmed | Corroborated | High | P3, S1–S5, R1 |
| `VWF-006` | The committed image removes or cuts away existing world geometry and objects inside the projected volume behind it | Confirmed | Direct | High | P1, P2, S3, S4 |
| `VWF-007` | A misplaced image can erase a required teleporter or other essential object and create a dead-end current branch | Confirmed | Direct | High | P1, S3 |
| `VWF-008` | Rewind restores a retained state before a fall or image placement, including erased geometry and source availability, after which a different continuation can be played | Confirmed | Corroborated | High | P1, S3–S5, R1 |
| `VWF-009` | Falling, landing and collision resolve continuously against both original and image-instantiated geometry | Confirmed | Corroborated | High | S2, S3, S5, R1 |
| `VWF-010` | The scoped level completes when the sole avatar reaches and activates its fixed teleporter | Confirmed | Corroborated | High | P1, S2–S5, R1 |
| `VWF-011` | Current geometry, held image, image plane, avatar and teleporter are visible; the scoped transitions contain no random state change | Observation | Corroborated | High | VWF-001–VWF-010 |
| `VWF-012` | Ordinary navigation and body physics advance in real time, while rewind directly drives retained history backward | Observation | Corroborated | High | P1, S3–S5, R1 |
| `VWF-013` | The image is not a persistent world fragment, fixed interface panel or portal endpoint: commitment consumes its held source and creates replacement geometry | Observation | Corroborated | High | VWF-002–VWF-008 |
| `VWF-014` | The scoped supplied-image task does not require camera capture, duplication, battery transport or protected-surface rules | Observation | Corroborated | High | S1, S4, R1 |

## Basic data

- Release / origin: Sad Owl Studios developed Viewfinder; Thunderful Publishing
  released it for PlayStation 5 and Windows on 18 July 2023. Later platform
  ports are outside the scoped release record.
- Platform or physical form: single-player first-person spatial puzzle with a
  held 2D image serving as a perspective-dependent world-edit instrument.
- Puzzle family: perspective-image geometry instantiation with destructive
  overwrite and branchable rewind.
- Creator / publisher sources:
  - **[P1]** [Sad Owl director Gwen Foster on PlayStation Blog](https://blog.playstation.com/2023/06/08/create-destroy-and-rewind-in-viewfinder-out-july-18-play-the-demo-today/),
    establishing placed photographs, destruction of prior space, teleporter
    deletion, dead ends and rewind as the recovery mechanism.
  - **[P2]** [Sad Owl release account on PlayStation Blog](https://blog.playstation.com/2023/07/18/reshape-reality-with-your-perspective-in-viewfinder-out-today/),
    corroborating camera / perspective / rewind and the design principle that
    creation destroys.
  - **[P3]** [Thunderful publisher page](https://thunderfulgames.com/games/viewfinder/),
    identifying the developer, release date, first-person format and pictures
    brought to life by placing them into the world.
- Contemporary corroboration:
  - **[S1]** [Game Informer review](https://www.gameinformer.com/review/viewfinder/short-and-smart),
    documenting early found photographs, later camera progression, bridge
    creation and walkable paths.
  - **[S2]** [PC Gamer review](https://www.pcgamer.com/viewfinder-review/),
    documenting held-image placement, perspective-relative 3D conversion,
    rotation, bridges and teleporter objectives.
  - **[S3]** [The Guardian review](https://www.theguardian.com/games/2023/jul/17/viewfinder-review-sad-owl-thunderful),
    documenting solid explorable photo spaces, landscape obliteration, limited
    image resources, falling and scrubbed rewind.
  - **[S4]** [Push Square review](https://www.pushsquare.com/reviews/ps5/viewfinder),
    distinguishing initial supplied pictures from later camera capture and
    corroborating perspective insertion, replacement and rewind.
  - **[S5]** [GamesRadar review](https://www.gamesradar.com/viewfinder-review/),
    documenting found-photo pickup, bridge / ramp construction, teleporter
    endpoints and alternate placement after rewind.
- Transition reference:
  - **[R1]** [GamesRadar walkthrough](https://www.gamesradar.com/viewfinder-walkthrough-solutions/),
    used only to bound the early supplied-image / rewind / teleporter sequence.
- Claim IDs: `VWF-001`–`VWF-014`.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. The player directly walks and jumps
  the sole avatar through the current original and instantiated geometry.
- `ACT-044` — rewind recent simulation history. The player scrubs back before
  a fall or committed image, then releases rewind and tries a different pose or
  route.
- `ACT-057` — position and commit held perspective image. The player picks up
  the supplied picture, translates its plane through the current view, rotates
  it and stamps the selected perspective into the world.
- `ACT-033` and `ACT-035` are absent: the picture is neither moved among fixed
  UI slots nor detached as one retained layer above another. `ACT-047` is
  absent because the player does not place one channel of a paired aperture.
  `ACT-048` is absent because the image is not released as a rigid physics body.
  `ACT-056` is absent because no persistent map-region identity is relocated.
- Claim IDs: `VWF-001`–`VWF-004`, `VWF-008`, `VWF-013`.

### System Behaviour Genes

- `SYS-036` — continuous force-constrained body dynamics. The avatar falls,
  lands and collides against whichever original and newly instantiated surfaces
  exist in the current history.
- `SYS-075` — perspective image-to-world spatial instantiation. The committed
  image's represented bridge, room, platform or teleporter becomes solid 3D
  geometry at the pose and scale implied by the held plane.
- `SYS-076` — projection-volume destructive world overwrite. Existing geometry
  and objects behind the committed image are removed inside its replacement
  volume before the new geometry becomes authoritative.
- Resolution order: read held source and plane pose; derive the perspective-
  relative spatial transform; identify and delete intersected replaceable world
  content; instantiate the image's solid / interactive contents; rebuild
  collision; consume the held source in the current branch; continue live body
  dynamics. Rewind restores the earlier complete state rather than applying an
  inverse image operation.
- `SYS-044` is absent because no two retained panels compose a temporary
  depicted continuation. `SYS-059` is absent because traversal does not map a
  body between paired apertures. `SYS-074` is absent because no persistent map
  fragments retain identity while their adjacency graph changes.
- Claim IDs: `VWF-004`–`VWF-009`, `VWF-013`.

### Constraint Genes

- `CON-089` — finite branch-local source-image stock. The scoped puzzle offers
  one found source; once it is stamped into the world, no second placement of
  that source is available in the current branch. Rewinding restores the
  pre-commit stock.
- `CON-065` is absent: placement does not require authored visual compatibility
  with another image or seam. `CON-066` is absent because the player directly
  changes the traversed world with one image rather than requiring cross-panel
  causation. `CON-088` is absent because the source does not remain a freely
  rearrangeable persistent fragment after commitment.
- Scarce strategic resources: the single source image, unobstructed projected
  space that does not delete the required exit, usable walking surfaces and
  retained rewind history.
- Later camera film, duplicators and protected geometry are excluded rather
  than silently folded into this constraint.
- Claim IDs: `VWF-002`, `VWF-003`, `VWF-007`, `VWF-008`, `VWF-013`, `VWF-014`.

### Information Genes

- `INF-001` — fully visible current state. The player can inspect the current
  geometry, the held image and its on-screen plane, the avatar's immediate
  route and the teleporter; no hidden random transition alters the scoped task.
- The held plane previews image alignment, but it does not disclose every
  post-commit collision and overwrite consequence as an exact future state.
  No separate exact-preview gene is admitted.
- A picture may contain spatial depth not readable from one flat view; that is
  source content resolved by `SYS-075`, not concealed current world state.
- Claim IDs: `VWF-002`–`VWF-011`.

### Objective Genes

- `OBJ-022` — evacuate every required controlled actor through fixed exits.
  The sole required avatar must reach and activate the level's fixed teleporter
  after the image edit makes it accessible.
- `OBJ-026` is absent. Unlike Carto's declared remote person or land region,
  the target is the level's fixed exit apparatus and the one-actor case already
  lies inside `OBJ-022`.
- Merely creating a bridge, preserving the image or displaying a target shape
  does not complete the level.
- Claim IDs: `VWF-007`, `VWF-010`.

### Time Genes

- `TIM-003` — real-time input during forced progression. Navigation, falling,
  collision and image stamping occur in a continuously simulated first-person
  world even though the ordinary puzzle has no deadline.
- `TIM-007` — branchable player-reversible simulation history. Rewind restores
  already lived states, and releasing it permits a different placement or route
  that replaces the abandoned continuation.
- `TIM-002` is absent because live body state can change continuously while the
  player falls. Rewind is more than one-step undo and exposes no editable
  prospective future, so `TIM-008` is absent.
- Claim IDs: `VWF-008`, `VWF-009`, `VWF-012`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| One found image is available in the level | Pick it up and hold it against empty space | Its plane follows the player's chosen view pose without yet changing the world | direct perspective-image action | `VWF-002`, `VWF-003` |
| The image depicts a horizontal bridge | Rotate and position it across a gap, then commit | The depicted bridge becomes solid at the projected pose and spans the gap | perspective instantiation | `VWF-004`, `VWF-005` |
| A required wall blocks the route | Stamp an image whose open passage overlaps the wall | The overlapped wall volume is cut away and replaced by image geometry | destructive overwrite | `VWF-006` |
| The teleporter lies behind the proposed image plane | Commit the image across it | The teleporter is deleted from the current branch, so completion is impossible there | overwrite affects essential objects | `VWF-006`, `VWF-007` |
| The wrong placement consumed the only supplied source | Rewind to immediately before commitment | Original geometry, teleporter and held-image stock are restored | full-state reversible history | `VWF-002`, `VWF-008` |
| An earlier state has been restored | Release rewind and stamp the image elsewhere | A new spatial continuation replaces the abandoned dead-end branch | branchability | `VWF-008` |
| Instantiated geometry forms a usable route | Walk or jump onto and through it | Collision and gravity treat the image result as ordinary solid world space | authoritative interactive geometry | `VWF-001`, `VWF-005`, `VWF-009` |
| The image route reaches the exit | Enter and activate the fixed teleporter | The sole required avatar completes the bounded level | fixed-exit objective | `VWF-010` |

## Strategic and experiential structure

- Local decision: choose the image plane's position and rotation so useful
  depicted surfaces align with the current world while the replacement volume
  avoids the teleporter and necessary supports.
- Medium-term planning: reason simultaneously about what the image creates and
  what its frustum deletes, then reserve a walkable approach and landing path.
- Long-term structure: use rewind as an experimental branch tool rather than a
  failure reset, comparing alternative world edits from the same source state.
- Common heuristics: work backward from the fixed teleporter; identify the
  picture's usable floors and openings; rotate vertical structures into ramps;
  inspect the entire projected volume, not only the visible frame; rewind as
  soon as a unique source or critical object is lost.
- Failure attribution: a visible misalignment, deleted exit, missing support or
  unsafe landing explains failure without random state.
- Player-trust factors: perspective scale, clipping volume, source consumption,
  generated collision, gravity orientation and rewind restoration must be
  consistent across repeated placements.
- Claim IDs: `VWF-001`–`VWF-014`.

## Replay and variation

- What changes between tasks: supplied image content, existing geometry, gap /
  obstacle arrangement, allowed placement space and teleporter position.
- Randomness or procedural generation: none in the scoped authored puzzle.
- Multiple viable strategies: a source image can often be placed at different
  scales, rotations and positions that still create a viable route.
- Typical replay motive: test a more direct placement, discover geometry hidden
  within the image or recover from destructive overwrite through rewind.
- Claim IDs: `VWF-002`–`VWF-012`.

## Adjacent systems and history

- Portal is the mathematical near match through first-person navigation, live
  body physics, current-state visibility, a fixed exit and real-time play.
  Portal preserves chamber geometry and links two apertures; Viewfinder creates
  and deletes geometry through a single perspective image.
- Braid and Tin Hearts share branchable rewind. Braid rewinds a platform world
  with affinity exceptions; Tin Hearts revises physical routing around
  autonomous soldiers; Viewfinder rewinds direct avatar history and destructive
  world-image commits.
- Pikmin 4 shares the direct-navigation branchable-rewind core at a much coarser
  autosave granularity. Its follower work and day cycle remain absent here.
- Gorogoa retains illustrated panels and layers in four slots and composes
  depicted spaces. Viewfinder consumes one held source into solid world
  geometry and may erase the prior scene.
- Carto moves unique persistent map fragments and propagates their flat
  adjacency. Viewfinder does not preserve a moved fragment identity or map
  topology; it stamps new spatial content into one projection volume.
- Claim IDs: `VWF-001`–`VWF-014`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-044`, `ACT-057` | direct navigation, rewind and image-plane commitment |
| System Behaviour | `SYS-036`, `SYS-075`, `SYS-076` | body physics, image instantiation and overwrite |
| Constraint | `CON-089` | one finite supplied image in the current branch |
| Information | `INF-001` | visible current world and held placement plane |
| Objective | `OBJ-022` | sole avatar reaches fixed teleporter exit |
| Time | `TIM-003`, `TIM-007` | live world with branchable rewind |

Canonical signature:

`ACT-008,ACT-044,ACT-057; SYS-036,SYS-075,SYS-076; CON-089; INF-001; OBJ-022; TIM-003,TIM-007`

## Corpus comparison

- Indexed games scanned: `GAME-0001`–`GAME-0040`.
- Indexed combinations scanned: `COMB-0001`–`COMB-0040`.
- Exact genome matches: none.
- Existing combination subsets: none before registering `COMB-0041`.
- Full Jaccard scan (intersection / union = score):
  `GAME-0001` `1 / 24 = 0.041667`; `GAME-0002` `1 / 17 = 0.058824`;
  `GAME-0003` `0 / 20 = 0.000000`; `GAME-0004` `2 / 24 = 0.083333`;
  `GAME-0005` `1 / 17 = 0.058824`; `GAME-0006` `2 / 18 = 0.111111`;
  `GAME-0007` `1 / 18 = 0.055556`; `GAME-0008` `1 / 17 = 0.058824`;
  `GAME-0009` `1 / 26 = 0.038462`; `GAME-0010` `1 / 19 = 0.052632`;
  `GAME-0011` `1 / 23 = 0.043478`; `GAME-0012` `1 / 19 = 0.052632`;
  `GAME-0013` `1 / 23 = 0.043478`; `GAME-0014` `1 / 25 = 0.040000`;
  `GAME-0015` `1 / 24 = 0.041667`; `GAME-0016` `2 / 24 = 0.083333`;
  `GAME-0017` `0 / 24 = 0.000000`; `GAME-0018` `2 / 28 = 0.071429`;
  `GAME-0019` `1 / 20 = 0.050000`; `GAME-0020` `1 / 24 = 0.041667`;
  `GAME-0021` `3 / 17 = 0.176471`; `GAME-0022` `1 / 22 = 0.045455`;
  `GAME-0023` `0 / 21 = 0.000000`; `GAME-0024` `1 / 22 = 0.045455`;
  `GAME-0025` `2 / 20 = 0.100000`; `GAME-0026` `3 / 20 = 0.150000`;
  `GAME-0027` `2 / 21 = 0.095238`; `GAME-0028` `2 / 26 = 0.076923`;
  `GAME-0029` `3 / 20 = 0.150000`; `GAME-0030` `5 / 20 = 0.250000`;
  `GAME-0031` `4 / 18 = 0.222222`; `GAME-0032` `1 / 21 = 0.047619`;
  `GAME-0033` `5 / 19 = 0.263158`; `GAME-0034` `5 / 20 = 0.250000`;
  `GAME-0035` `5 / 24 = 0.208333`; `GAME-0036` `2 / 21 = 0.095238`;
  `GAME-0037` `1 / 19 = 0.052632`; `GAME-0038` `4 / 23 = 0.173913`;
  `GAME-0039` `1 / 19 = 0.052632`; `GAME-0040` `2 / 17 = 0.117647`.
- Mathematical near match: `GAME-0033` — Portal at `5 / 19 = 0.263158`.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0033` — Portal | `ACT-008`, `SYS-036`, `INF-001`, `OBJ-022`, `TIM-003` | Portal places two replaceable endpoints on eligible surfaces, preserves chamber geometry, remaps crossing bodies and velocity, supports portable cubes and has no rewind. Viewfinder poses one consumable image, instantiates its contents, destructively replaces a projection volume and branches history. | Near only; no exact genome or inherited combination match |

## Combination record

- Registered recurring `COMB-0041` — live navigable branchable-rewind core.
- Its five-gene proper subset is supported by Braid, Pikmin 4 and Viewfinder.
  It requires direct avatar navigation inside the same live world whose retained
  history can be restored and branched; it omits each game's distinct puzzle
  object, objective and rewind granularity.
- The record complements `COMB-0034`: that core requires continuously
  autonomous agents, while `COMB-0041` requires direct avatar navigation.

## Taxonomy impact

- Registry changes: added `ACT-057`, `SYS-075`, `SYS-076` and `CON-089`;
  reused seven existing genes.
- `OBJ-022` gains a third supporter and remains the correct fixed-exit boundary.
  `ACT-044` / `TIM-007` absorb Viewfinder without wording changes because their
  existing restoration and branch tests already include this granularity.
- No merge, split, deprecation, type move or earlier game-signature rewrite is
  justified.

## Negative results

- `ACT-033`, `ACT-035`, `SYS-044`, `CON-065` and `CON-066` are rejected: no
  persistent fixed-slot panel pair or cross-panel-only causal relation exists.
- `ACT-047` and `SYS-059` are rejected: one placed image does not create paired
  apertures or map crossing coordinates to a remote endpoint.
- `ACT-056`, `SYS-074` and `CON-088` are rejected: image placement does not
  relocate a unique persistent map region or preserve fragment identity.
- `ACT-048` is rejected because the held photograph becomes a world-edit
  request rather than a released rigid body. `OBJ-026` is rejected because the
  teleporter is the fixed level exit already covered by `OBJ-022`.
- `TIM-002` is rejected because falling and collision continue in real time;
  `TIM-008` is rejected because rewind exposes lived history, not an editable
  prospective command timeline.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] A committed image both creates solid traversable
  geometry and destructively deletes world content inside its projected volume
  (`VWF-005`–`VWF-007`).
- [Confirmed | Corroborated | High] Rewind restores the pre-placement source,
  geometry and avatar state, enabling a replacement spatial branch
  (`VWF-008`).

## Нові гени

- [Observation | Corroborated | High] Added `ACT-057`, `SYS-075`, `SYS-076`
  and `CON-089`; reused `ACT-008`, `ACT-044`, `SYS-036`, `INF-001`, `OBJ-022`,
  `TIM-003` and `TIM-007`.

## Нові комбінації

- [Confirmed | Corroborated | High] Registered recurring `COMB-0041`, supported
  by Braid, Pikmin 4 and Viewfinder.

## Зміни таксономії

- [Observation | Corroborated | High] No lifecycle or signature rewrite;
  image instantiation and overwrite remain distinct from panels, portals and
  map fragments.

## Нові питання

- Which independent game best tests finite consumable representation sources
  without repeating the current geometry / rewind cluster?
- Does a future camera-capture scope require a separate capture Action and
  exposure Constraint, or reuse broader image-source boundaries?

## Наступна рекомендована гра

- [Hypothesis | Corroborated | High] `TARGETED_REUSE_SELECTION_005`.
- Required baseline: 41 games, 278 active genes and 489 usages.
- Optimisation criterion: source at least five mechanically independent
  candidates, favour Action / Constraint singleton falsification and a
  plausible recurring combination, and avoid another immediate perspective-
  geometry or rewind subject.
- Stop condition: selection and scope only; do not begin `GAME-0042` inside
  that unit.

## Sources consulted

- Sad Owl Studios' two PlayStation developer accounts and Thunderful's
  publisher page.
- Contemporary Game Informer, PC Gamer, The Guardian, Push Square and
  GamesRadar mechanical accounts plus one bounded GamesRadar walkthrough.
