---
game_id: GAME-0095
slug: manifold-garden
game_title: Manifold Garden
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0095
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-049
    - ACT-097
  system:
    - SYS-036
    - SYS-125
    - SYS-126
  constraint:
    - CON-146
  information:
    - INF-001
    - INF-045
  objective:
    - OBJ-022
  time:
    - TIM-003
---

# Game: Manifold Garden

## Analysis scope

- Version / ruleset: William Chyr Studio's original 2019 base game, bounded to
  the opening Part 1 gravity tutorial and the first exterior periodic-space
  crossing. The packet begins on the blue floor, establishes the six coloured
  orthogonal gravity frames and matching-cube rule, then follows the blue-tree
  balcony route: fall while moving forward through one repeated world boundary,
  land on the corresponding lower tower copy, repeat the gap-crossing lesson,
  press the blue switch and leave through its linked fixed door. A compact
  executable control joins those two tutorial lessons without reproducing the
  production level geometry.
- Included: first-person walking and jumping; choosing a visible surface as
  down; six axis-aligned gravity directions; live body gravity and collision;
  colour-coded current frame; one portable matching-colour cube; frame-gated
  pickup and placement; reachable door switches; translational three-axis
  world repetition; boundary remapping that preserves local pose; deliberate
  falling as traversal; fixed exit; real-time simulation.
- Excluded: later shrines and monuments; trees as renewable cube sources;
  planting; water, water loops and redirection; balls and tubes; lasers; Dark
  and God Cubes; portals between levels; staggered, reflected or rotated wrap
  variants; toxic ooze, ending, photo mode, achievements, speedrun routes and
  platform-specific control assistance.
- Direct-play status: not conducted. The official product records establish
  gravity manipulation, walkable surfaces and infinitely repeating geometry.
  William Chyr's technical and design accounts directly establish six-direction
  traversal, falling-to-return, grid repetition and gap crossing. The studio's
  official walkthrough fixes the exact colour, cube, switch and balcony order.
  The local control proves one normalised lattice mapping, not production
  coordinates, collision meshes or animation timing.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MFG-001` | Manifold Garden launched in 2019 as William Chyr Studio's first-person exploration puzzle about gravity and impossible geometry | Confirmed | Direct | High | P1, P2 |
| `MFG-002` | The player can select a visible wall or ceiling as the new down direction and walk on that surface | Confirmed | Direct | High | P2, P3, S1 |
| `MFG-003` | The ordinary gravity domain contains six colour-coded orthogonal directions | Confirmed | Direct | High | S1 |
| `MFG-004` | A coloured cube is movable only while the current gravity matches its colour | Confirmed | Direct | High | S1, S2 |
| `MFG-005` | World geometry repeats translationally in every direction, so crossing one boundary returns a body through the corresponding opposite side | Confirmed | Direct | High | P2–P5 |
| `MFG-006` | Production renders repeated instances in a grid and teleports the player at the centre-instance boundary | Confirmed | Direct | High | P5 |
| `MFG-007` | Deliberately falling through a repeated boundary is required to cross otherwise unreachable gaps | Confirmed | Direct | High | P3, P4, S1 |
| `MFG-008` | In the scoped balcony sequence the player carries a blue cube, falls forward to a lower repeated tower balcony and places it in the receiver | Confirmed | Direct | High | S1 |
| `MFG-009` | The following gap is crossed by another deliberate fall, after which the blue switch opens the next fixed door | Confirmed | Direct | High | S1 |
| `MFG-010` | The control preserves local coordinates modulo one period while recording a one-cell lattice displacement | Observation | Direct | High | V1, MFG-005–MFG-007 |
| `MFG-011` | The control rejects diagonal gravity, wrong-colour cube pickup, premature wrap traversal, remote switch activation, closed-exit entry and wrong-frame reuse | Observation | Direct | High | V1 |
| `MFG-012` | Neither gravity selection nor world wrapping changes object scale or derives topology from the camera projection | Observation | Corroborated | High | P3–P5, GAME-0091–0094 |

## Basic data

- Release / origin: William Chyr Studio launched Manifold Garden on Apple
  Arcade and Epic Games Store on 18 October 2019; later platform releases do
  not change the bounded rule packet.
- Platform or physical form: single-player first-person three-dimensional
  traversal puzzle with live rigid-body physics and a translationally repeating
  world.
- Puzzle family: gravity-frame traversal through periodic three-dimensional
  space.
- Primary and creator sources:
  - **[P1]** [William Chyr Studio — Manifold Garden available now](https://manifold.garden/news/2019/10/18/manifold-garden-available-now/),
    for the original 2019 launch and gravity / impossible-geometry premise.
  - **[P2]** [Manifold Garden on Steam](https://store.steampowered.com/app/473950/Manifold_Garden/),
    for first-person play, walking on visible surfaces, gravity manipulation,
    infinitely repeating architecture and falling back to the start.
  - **[P3]** [PlayStation Blog — Cultivate an Infinite World in Manifold Garden](https://blog.playstation.com/?p=162218),
    by developer William Chyr, for gravity changes, three-dimensional wrap,
    travel returning to the origin and falling cubes reappearing above.
  - **[P4]** [Game Developer — How Manifold Garden makes reality fold back on itself](https://www.gamedeveloper.com/design/how-i-manifold-garden-i-makes-reality-fold-back-on-itself),
    reporting Chyr's toroidal / stacked wrap explanation and the deliberate
    fall used to cross gaps that cannot be walked.
  - **[P5]** [SIGGRAPH 2020 — That's a wrap: Manifold Garden rendering retrospective](https://doi.org/10.1145/3388767.3407385),
    by Arthur Brussee, Andrew Saraev and William Chyr, for grid-instanced
    repeated geometry and centre-instance boundary teleportation.
- Reproducible corroboration:
  - **[S1]** [William Chyr Studio — official Manifold Garden walkthrough](https://manifold.garden/walkthrough),
    for six coloured directions, wall-selected gravity, colour-locked cubes,
    the blue-tree balcony fall, receiver, second gap, blue switch and door.
  - **[S2]** [PC Gamer review](https://www.pcgamer.com/manifold-garden-review/),
    for gravity-matching cube manipulation as an independent summary.
  - **[V1]**
    [`verify_manifold_garden_control.py`](../../../scripts/verify_manifold_garden_control.py),
    an executable six-frame, colour-gated, periodic-lattice route with six
    rejected invalid transitions.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. The player directly walks, jumps
  and steers during a fall rather than selecting a remote pathfinding target.
- `ACT-048` — pick up and release portable rigid object. A matching-colour cube
  can be lifted, carried while moving and placed on its receiver or support.
- `ACT-049` — toggle reachable world switch. After the repeated-space crossing,
  the avatar presses the locally reachable blue switch to change its linked
  door state.
- `ACT-097` — select orthogonal surface as gravity down. The player aims at a
  visible eligible wall, floor or ceiling and commits its inward normal as the
  new gravity direction without rotating an individual object.

### System Behaviour Genes

- `SYS-036` — continuous force-constrained body dynamics. The avatar and
  eligible cube accelerate, fall, collide and land while live time advances.
- `SYS-125` — selected-surface global gravity-frame reorientation. A valid
  gravity-shift command snaps the whole local physics frame to one of six
  orthogonal directions, making the selected surface the floor and resolving
  unsupported bodies toward it.
- `SYS-126` — translationally periodic three-dimensional boundary remapping.
  Crossing a world-period boundary maps the body to the corresponding local
  pose in the opposite repeated instance while preserving its frame-relative
  trajectory, making downward travel return from above.
- Resolution order: select a legal surface normal; update current gravity and
  frame colour; continue body dynamics; enforce cube-colour eligibility;
  accept carry or switch actions; integrate a deliberate fall; detect the
  centre-instance boundary; add the opposite lattice translation; retain local
  motion; resolve landing; activate the reachable switch; traverse the door.

### Constraint Genes

- `CON-146` — portable cube manipulation requires matching gravity colour. A
  red cube can be picked up or deliberately placed only in red gravity, a blue
  cube only in blue gravity, and so on. Changing away leaves the nonmatching
  cube as world geometry rather than a freely draggable object.
- The six gravity states are orthogonal surface normals. A diagonal vector,
  free numeric direction or camera roll without an eligible surface is not a
  legal gravity choice.
- Crossing a rendered repeated view is not enough: the dynamic body must reach
  the active periodic boundary and retain a landing-compatible trajectory.
- Scarce strategic resources: none consumed in the bounded packet. Cubes are
  retained physical objects, and retrying a fall does not spend a life counter.

### Information Genes

- `INF-001` — fully visible current state. Relevant surfaces, gaps, repeated
  copies, cube, receiver, switch, door and present avatar relation are visible
  before each scoped action.
- `INF-045` — gravity-frame colour and eligible-surface encoding. The floor,
  world tint, crosshair-facing surface, cubes and matching fixtures expose the
  currently selected directional frame and which objects can be manipulated.
- Infinite visual repetition is decision-bearing rather than decorative: the
  aligned copies disclose that a lower target is the translated counterpart of
  the upper structure, though they do not draw the exact future trajectory.

### Objective Genes

- `OBJ-022` — evacuate every required controlled actor through fixed exits.
  The sole avatar must use the repeated fall to reach the switch and then pass
  through the linked fixed door into the next Part 1 area.
- The cube receiver and blue switch are prerequisites. Neither is a terminal
  score, optional collectible or campaign-wide completion objective.

### Time Genes

- `TIM-003` — real-time input during forced progression. Gravity, velocity and
  collision continue while the player walks, carries, aims, shifts frame and
  steers during a fall.
- There is no authored deadline in the packet; live physics rather than time
  pressure is what separates it from self-paced atomic board turns.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Blue floor is current down; green wall is visible | use gravity shift on green wall | green wall becomes the floor and unsupported bodies resolve toward it | selected surface defines gravity | `MFG-002`, `MFG-003` |
| Blue gravity is active; red cube is reachable | try to pick up red cube | interaction is rejected and cube remains fixed | cube eligibility is frame-colour gated | `MFG-004`, `MFG-011` |
| Red gravity is active; red cube and red switch align | carry and place red cube | cube becomes supported on the red target and the linked route opens | frame selection enables object handling | `MFG-004` |
| Avatar stands above an unreachable repeated tower in blue gravity | step off and hold forward | body falls one period, crosses the lower boundary and reappears through the corresponding upper side | downward motion wraps rather than kills | `MFG-005`–`MFG-008` |
| Unwrapped position changes from `(2,1,2)` by one blue period plus `(3,0,0)` | normalise modulo period `12` | local position becomes `(5,1,2)` and lattice offset becomes `(0,-1,0)` | local pose and copy displacement are distinct | `MFG-010` |
| Avatar has landed on the translated balcony | place blue cube in receiver | linked access to the next interior gap becomes available | carried body survives useful traversal | `MFG-008` |
| Second platform cannot be reached by walking | leap through the repeated boundary | avatar lands on the corresponding opposite-side platform | periodic fall is a route operation | `MFG-007`, `MFG-009` |
| Blue switch is locally reachable | press switch and enter linked door | door opens and the sole required actor leaves the bounded packet | fixed-exit completion | `MFG-009` |

The executable control separately rejects a diagonal gravity vector, moving a
red cube under blue gravity, crossing before the tutorial door is opened,
pressing the remote blue switch, entering its closed exit and reusing the red
cube after returning to blue gravity. Its integer lattice deliberately omits
production acceleration, collision meshes and visual duplicate rendering.

## Strategic and experiential structure

- Local decision: choose which visible surface becomes down, then distinguish
  the reachable architectural copy from a merely distant-looking repetition.
- Medium-term planning: put colour-matched objects in useful states before
  changing frame; preserve enough lateral drift during a fall to land on the
  target copy and reach the switch.
- Long-term structure: later areas compose gravity and wrap with renewable
  cubes, water, planting, balls, lasers and modified repetition, all excluded
  so the baseline topology remains falsifiable.
- Common heuristics: read colour before grabbing; inspect above and below as
  one periodic neighbourhood; when a gap has no bridge, search for its
  translated landing copy; steer during the full fall; confirm the local switch
  before treating a visible repeated switch as reachable.
- Failure attribution: rejected manipulation follows current frame colour;
  missed landing follows visible geometry and trajectory, not randomness.
- Player-trust factors: frame tint, crosshair colour, gravity animation,
  repeated instance alignment, boundary transfer and landing must agree.

## Replay and variation

- The bounded route is deterministic. Variation comes from gravity-frame order,
  approach angle and fall steering rather than random layouts or hidden state.
- Repeated copies provide several visually plausible approaches, but the scoped
  receiver and switch order keeps the required causal packet finite.
- Accessibility-relevant variance includes instant versus animated gravity
  motion and input platform, neither of which changes the selected direction or
  periodic mapping classified here.

## Adjacent systems and history

- Portal maps bodies between two player-created paired apertures and rotates
  velocity relative to the exit. Manifold Garden maps every periodic world
  boundary by an authored lattice translation and does not require apertures.
- Fez rotates one of four horizontal orthographic views while world gravity
  remains down; Manifold Garden selects one of six physical down directions in
  a fully navigable three-dimensional scene.
- Superliminal changes one held object's physical scale from camera depth;
  Manifold Garden preserves scale and instead changes gravity and world copy.
- Snakebird applies discrete post-input gravity to a grid body; Manifold Garden
  integrates live physics and permits the player to change the gravity frame.
- Wraparound board variants in Net or Netslide alter finite graph adjacency.
  Here a continuous body crosses a three-dimensional world-period boundary.

## Normalised genome

| Gene type | IDs | Scope meaning |
|---|---|---|
| Action | `ACT-008`, `ACT-048`, `ACT-049`, `ACT-097` | steer avatar, carry cube, press switch, select gravity surface |
| System Behaviour | `SYS-036`, `SYS-125`, `SYS-126` | live bodies, gravity-frame snap, periodic boundary mapping |
| Constraint | `CON-146` | cube manipulation requires matching frame colour |
| Information | `INF-001`, `INF-045` | visible world and colour-coded gravity eligibility |
| Objective | `OBJ-022` | take the sole avatar through the linked fixed door |
| Time | `TIM-003` | live steering and physics during falls |

Full signature:
`ACT-008,ACT-048,ACT-049,ACT-097; SYS-036,SYS-125,SYS-126; CON-146; INF-001,INF-045; OBJ-022; TIM-003`.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `94` (`GAME-0001`–`GAME-0094`).
- Exact genome matches: none.
- Tied near matches: `GAME-0094` — Superliminal (`6 / 16 = 0.375000`).
- Supported combination subsets: `COMB-0095`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0094`.

## Coverage decision

- Reuse direct navigation, rigid-object carry, reachable switches, continuous
  body physics, visible state, fixed-exit completion and live scheduling.
- Add only the absent causal boundaries: selecting a surface as down, applying
  the selected global gravity frame, translational periodic remapping, matching
  gravity-colour object eligibility and visible frame encoding.
- Keep portals, camera-authoritative topology, object scaling, water loops,
  planting and later nontrivial wrap variants outside this packet.

## Confidence and open questions

### Assumptions

- The control represents the ordinary early world as a cubic period with equal
  axis lengths; production levels can use different cell extents and offsets.
- The two tutorial modules are combined because the official Part 1 sequence
  teaches one stable causal system: selected gravity determines both object
  eligibility and which periodic boundary is downward.

### Unknowns

- Exact production period vectors, teleport threshold, velocity correction,
  collision skin width and cross-boundary camera smoothing were not measured.
- Whether every early receiver is strictly occupancy-sustained is not claimed;
  `SYS-061` is therefore absent from the signature.

### Confidence

- High for six surface-selected gravity frames, colour-gated cubes, global
  repetition, downward-return mapping and the official balcony order.
- Medium-high for frame-relative velocity preservation at the exact production
  seam because the technical paper confirms boundary teleportation while the
  walkthrough and creator accounts establish useful continuous falling.

## Combination candidate

- Candidate ID: `COMB-0095`.
- Gene set: `ACT-008`, `ACT-097`, `SYS-125`, `SYS-126`, `INF-045`, `OBJ-022`.
- Supporting game: `GAME-0095`.
- Proper-subset rationale: cube carrying, switch interaction, generic body
  physics, the cube-colour constraint, full visibility and live scheduling
  support the tutorial but do not define fall-through-periodic-space traversal.
- Novelty claim: not assessed.

## Outcome

- Reused genes: `ACT-008`, `ACT-048`, `ACT-049`, `SYS-036`, `INF-001`,
  `OBJ-022`, `TIM-003`.
- Added genes: `ACT-097`, `SYS-125`, `SYS-126`, `CON-146`, `INF-045`.
- Added combination: `COMB-0095`.
- Evidence gate: passed with two official product records, three creator or
  studio technical accounts, the official walkthrough, one independent rules
  summary and one executable verifier.
- Nearest prior genome: Superliminal; see `Corpus comparison` for the current
  result.
- Next falsification target: Maquette, to distinguish recursive cross-scale
  state propagation from both periodic translation and camera-derived scale.

## Taxonomy impact

- Physical gravity-frame selection is separated from Fez camera rotation and
  Rubik's Cube reference-frame inspection.
- Periodic world remapping is separated from Portal's paired apertures and
  cyclic finite-board adjacency.
- Colour is classified as information and interaction eligibility, not as an
  objective or cosmetic theme.

## Negative results

- `SYS-061` was rejected: the evidence does not prove that every scoped cube
  receiver and door reverses immediately when vacated.
- No generic “non-Euclidean geometry” gene was added; the record names the
  exact translational quotient behaviour that changes transitions.
- No separate falling action was added; stepping and steering remain ordinary
  direct navigation, while gravity and seam mapping are system behaviours.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Вибір поверхні фіксує один із шести
  ортогональних напрямів гравітації, позначених кольором (`MFG-002`, `MFG-003`).
- [Confirmed | Direct | High] Перетин межі періоду переносить тіло в
  відповідну копію світу, тому падіння стає способом перейти розрив
  (`MFG-005`–`MFG-009`).

## Нові гени

- [Observation | Direct | High] `ACT-097` — вибрати ортогональну поверхню як
  новий напрям униз.
- [Observation | Direct | High] `SYS-125` — перебудувати глобальний
  гравітаційний кадр за вибраною поверхнею.
- [Observation | Direct | High] `SYS-126` — трансляційно періодично перенести
  тіло крізь межу тривимірного світу.
- [Observation | Direct | High] `CON-146` — куб можна переносити лише у
  гравітації відповідного кольору.
- [Observation | Direct | High] `INF-045` — колір показує поточний кадр і
  придатні поверхні, куби та цілі.

## Нові комбінації

- [Observation | Direct | High] `COMB-0095` — вибрати напрям униз і пройти
  фіксований вихід через трансляційно повторюваний світ.

## Зміни таксономії

- [Observation | Direct | High] Глобальну зміну гравітації відділено від
  повороту камери; періодичну трансляцію — від парних порталів.

## Нові питання

- Які production-корекції швидкості й камери приховують момент перенесення на
  межі центральної копії?
- Чи потребують staggered і rotated wrap-варіанти окремого системного гена,
  коли їх буде проаналізовано як причинний puzzle packet?

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] Maquette.
- Optimisation criterion: test recursive same-state propagation across nested
  world scales after perspective scaling and periodic translation have been
  separated.
- Expected information gain: distinguish simultaneous cross-scale object
  correspondence from Superliminal's held-object resize, Patrick's Parabox
  containment and Manifold Garden's translated copies.
- Backlog impact: move Maquette to `GAME-0096`; retain Antichamber as a later
  discontinuous-topology falsification target.

## Чому саме вона

- [Hypothesis | Limited | Medium] Maquette should reuse direct first-person
  navigation and object handling while introducing a materially different
  recursive-scale causal link, giving the next iteration a narrow comparison
  against three already separated spatial transformations.
