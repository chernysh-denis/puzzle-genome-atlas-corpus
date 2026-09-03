---
game_id: GAME-0092
slug: echochrome
game_title: Echochrome
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0092
gene_ids:
  action:
    - ACT-006
    - ACT-095
  system:
    - SYS-037
    - SYS-045
    - SYS-121
  constraint:
    - CON-143
  information:
    - INF-001
    - INF-042
  objective:
    - OBJ-049
  time:
    - TIM-003
---

# Game: Echochrome

## Analysis scope

- Version / ruleset: original 2008 Echochrome PSP/PS3 core Solo-stage rules,
  bounded to the Law of Perspective Travelling and Law of Perspective
  Existence plus collection of the stage's required echoes. The evidence
  packet begins with a Walker approaching separated fixed paths and ends after
  apparent endpoint contact and a hidden gap let it contact all required
  echoes. A separate two-echo executable control supplies exact coordinates.
- Included: autonomous forward walking and dead-end response; thinking-mode
  pause; optional speed-up; continuously variable stage orbit; fixed 3D path
  coordinates; screen-space endpoint coincidence; nearer-geometry occlusion of
  a gap; contact collection; visible current projection; real-time scheduling.
- Excluded: Perspective Landing, Perspective Absence and Perspective Jumping;
  black holes and jump circles; other Solo stages; Pair and Others modes;
  Canvas editor and sharing; timers, clear-time scoring, hints, soundtrack,
  narrative, platform-specific input labels and later releases.
- Direct-play status: not conducted. Sony's official product page directly
  defines the Walker, all-echo objective and five laws. Two PlayStation producer
  posts establish free camera control, live autonomous guidance and separate
  perspective transformation. The official trailer corroborates the laws. The
  local control proves only a normalised two-relation route, not an authored
  retail-stage layout.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `ECH-001` | Echochrome is a Sony-published perspective puzzle released for PSP and PS3 in 2008 | Confirmed | Direct | High | P1, P2 |
| `ECH-002` | The player tilts and turns the camera while the Walker moves through fixed 3D mazes | Confirmed | Direct | High | P1, P2 |
| `ECH-003` | The Walker is guided indirectly and advances without a directional locomotion command for each step | Confirmed | Corroborated | High | P1, P2, S1 |
| `ECH-004` | Perspective Travelling connects world-separated paths when their current screen projections appear to touch | Confirmed | Direct | High | P1, P3, A1 |
| `ECH-005` | Perspective Existence treats a gap hidden by nearer geometry as a continuous path | Confirmed | Direct | High | P1, P3, A1 |
| `ECH-006` | Completing the scoped stage requires the Walker to collect all required echoes | Confirmed | Direct | High | P1 |
| `ECH-007` | Camera transformation and perspective-law calculation are distinct from ordinary image rendering | Confirmed | Direct | High | P3 |
| `ECH-008` | The control aligns two endpoints at 45 degrees, hides one later gap at 0 degrees and collects two echoes without moving any path | Observation | Direct | High | V1, ECH-004–ECH-007 |
| `ECH-009` | Echochrome differs from Fez because it admits continuously varying projections and an autonomous Walker rather than four cardinal collision slices and a directly controlled avatar | Observation | Corroborated | High | P1–P3, GAME-0091 |
| `ECH-010` | The scoped route has no random transition, inventory state or persistent world-geometry edit | Observation | Corroborated | High | P1–P3, V1 |

## Basic data

- Release / origin: developed by SCE Japan Studio with Game Yarouze!/Will and
  published by Sony Computer Entertainment; released for PSP and PS3 in 2008.
- Platform or physical form: single-player perspective puzzle on floating
  three-dimensional line mazes, presented through a continuously rotatable
  screen projection.
- Puzzle family: indirect autonomous traversal under authoritative visual
  coincidence and occlusion.
- Primary and creator sources:
  - **[P1]** [Sony — Echochrome product and feature page](https://www.sony.co.in/microsite/playstation/product/echochrome/game.html),
    for the Walker, all-echo goal, fixed maze, view manipulation and exact five
    perspective laws.
  - **[P2]** [PlayStation Blog — echochrome arrives tomorrow!](https://blog.playstation.com/2008/04/30/echochrome-arrives-tomorrow/),
    by producer Kumi Yuasa, for camera/perspective control, tilting and turning,
    continual-path creation and safe autonomous guidance.
  - **[P3]** [PlayStation Blog — 71% More echochrome PSP](https://blog.playstation.com/?p=2497),
    with producer Tatsuya Suzuki, for clarity as a decision requirement and the
    separation of graphics rendering from perspective-transformation
    calculation.
  - **[P4]** [PlayStation — Echochrome official trailer](https://www.youtube.com/watch?v=GybxIwfU4rI),
    for the five laws, joining walkways, hiding dangers and reaching echoes.
- Reproducible corroboration:
  - **[S1]** [GameSpot — GDC 2008 Echochrome hands-on](https://www.gamespot.com/articles/gdc-08-echochrome-hands-on-impressions-what-you-see-is-what-you-get/1100-6186366/),
    for the real-time Walker/camera relationship and tutorial presentation of
    the five laws.
  - **[A1]** [Boluk and LeMieux — Metagaming, chapter 2](https://manifold.umn.edu/read/metagaming/section/fb4e77c9-5347-42a4-9149-dfd009bd864f),
    for the independent account of Echochrome's five laws and the screen image
    taking precedence over mimetic 3D space.
  - **[A2]** [DBLP — Jun Fujiki, OLE coordinate system](https://dblp.org/rec/conf/siggraph/Fujiki07.html),
    for bibliographic confirmation of the creator's SIGGRAPH 2007 OLE system.
  - **[V1]**
    [`verify_echochrome_control.py`](../../../scripts/verify_echochrome_control.py),
    an executable fixed-geometry model of continuous projection, apparent
    endpoint transfer, foreground occlusion, contact collection and six
    rejected invalid transitions.

## Mechanical decomposition

### Action Genes

- `ACT-006` — accelerate automatic progression. Holding the speed control
  increases Walker rate without selecting a direction or changing its route.
- `ACT-095` — orbit rule-bearing perspective camera. The player continuously
  tilts and turns the viewing frame until separated world paths coincide or a
  gap is hidden in the screen projection.
- `ACT-008` is absent because the player never directly commands the Walker's
  left/right route steps. `ACT-094` is absent because views are not limited to
  four atomic cardinal quarter-turns.

### System Behaviour Genes

- `SYS-037` — contact-triggered collectible acquisition. When the Walker
  reaches an echo, that required target is credited while the stage continues
  until all required echoes are collected.
- `SYS-045` — continuous autonomous agent locomotion. The Walker advances on
  the running clock and follows its current eligible route without per-step
  player direction commands.
- `SYS-121` — live screen projection governs traversal topology. Fixed
  world-separated endpoints transfer the Walker when their projected positions
  coincide; a nearer occluder can make a projected discontinuity traversable by
  hiding it.
- `SYS-120` is absent: the system does not settle one of four views, peel to a
  nearest collision layer and correct avatar depth as Fez does. `SYS-075` and
  `SYS-076` are absent because the perspective neither instantiates nor deletes
  world geometry.
- Resolution order: update camera transform; project route geometry; identify
  apparent endpoint contact and eligible hidden discontinuities; advance the
  Walker under that temporary topology; credit contacted echoes; complete only
  when the required set is exhausted.

### Constraint Genes

- `CON-143` — camera-only route control over autonomous walker. The player may
  orbit, pause or accelerate, but cannot choose Walker direction directly or
  relocate a path.
- A useful projected relation is ephemeral: if the player moves the camera so
  contact or occlusion no longer holds before traversal, the ordinary 3D
  discontinuity again blocks the route.
- Scarce strategic resources: none consumed. The limiting resource is the
  interval before the Walker reaches the next junction, softened by thinking
  mode rather than converted into turn-based movement.

### Information Genes

- `INF-001` — fully visible current state. The current line geometry, Walker,
  echoes and decision-relevant screen projection are visible; other angles can
  be inspected by orbiting without random hidden mutation.
- `INF-042` — live projected path authority is visually disclosed. A current
  screen join looks joined, and an occluded gap is absent from the same view
  that governs the Walker's next traversal.
- The display is not a route forecast. It shows the present authoritative
  relation, not a guaranteed multi-step future after further camera movement.

### Objective Genes

- `OBJ-049` — collect every required target with indirectly guided walker. The
  bounded stage completes only after the autonomous Walker contacts the full
  fixed echo set.
- `OBJ-026` is rejected because the success state is not simply arrival at a
  location by a directly controlled avatar. `OBJ-019` is rejected because all
  targets, not a tolerated population quota, are required.

### Time Genes

- `TIM-003` — real-time input during forced progression. The Walker advances
  while the player changes perspective; a thinking control may suspend that
  clock and speed-up may increase its rate.
- `TIM-002` is absent because the unpaused Walker changes the decision state
  without another player action. `TIM-006` is absent because perspective edits
  occur during the live run rather than only before committed execution.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fixed route endpoints are separated in world space and in the current projection | orbit the stage continuously | every intermediate camera angle produces a distinct screen projection without moving either path | free rule-bearing camera, not four frames | `ECH-002`, `ECH-007` |
| Start end `(1,0,0)` and remote start `(3,0,2)` remain fixed | settle at yaw 45 degrees | both project to the same horizontal/vertical screen position | apparent endpoint contact | `ECH-004`, `ECH-008` |
| The Walker reaches the aligned start endpoint | let automatic motion continue | it transfers onto the remote path and contacts `E1` | autonomous traversal and contact credit | `ECH-003`, `ECH-006`, `ECH-008` |
| Remote path has a world gap from `(4,0,2)` to `(5,0,2)` | leave the gap visible | the Walker cannot cross the discontinuity | visual relation is required | `ECH-005`, `ECH-008` |
| A nearer occluder occupies `(4.5,0,0)` | orbit to yaw 0 degrees | the occluder projects inside the gap and lies in front of the path | perspective existence condition | `ECH-005`, `ECH-008` |
| The gap is hidden and the Walker is before it | resume automatic motion | the projected route continues across the hidden gap and contacts `E2` | occlusion-governed topology | `ECH-005`, `ECH-008` |
| Both fixed echoes are credited | evaluate the stage | the two-echo requirement completes; one echo alone does not | all-target objective | `ECH-006`, `ECH-008` |

The executable control separately rejects direct Walker steering, camera-driven
path relocation, remote echo credit, motion while paused, transfer across
misaligned endpoints and traversal across a visible gap. It also proves that
five sampled angles yield five distinct projections and that an occluder behind
the path cannot hide its gap.

## Strategic and experiential structure

- Local decision: determine which camera motion will make the next path
  relation true in screen space before the Walker reaches it.
- Medium-term planning: sequence several temporary visual joins so automatic
  forward motion encounters the required echoes in a safe order.
- Long-term structure: alternate between reading the maze as fixed 3D geometry
  and treating its current 2D image as the operative collision graph.
- Common heuristics: pause before a junction; align endpoint tips precisely;
  use foreground rails to cover gaps; confirm the intended target is next on
  the autonomous route; accelerate only after a stable relation is prepared.
- Failure attribution: a missed route is explained by alignment, occluder depth,
  timing or Walker approach direction rather than randomness.
- Player-trust factors: projected coincidence tolerance, occlusion ordering,
  Walker turn rules and collection credit must remain deterministic and legible.

## Replay and variation

- What changes between stages: fixed line-maze geometry, echo count and
  placement, Walker count, gaps, holes, jump points and useful camera angles.
- Randomness or procedural generation: none in the scoped authored packet.
- Multiple viable strategies: continuous camera freedom can admit several
  alignments or orders, but each accepted relation must satisfy the same five
  declared laws.
- Typical replay motive: reduce clear time, discover a cleaner perspective
  sequence, solve alternate modes or explore user-authored Canvas levels.

## Adjacent systems and history

- HUMANITY is the nearest complete genome because both combine speed control,
  autonomous walking, current-state visibility and live intervention. HUMANITY
  places persistent direction commands for a crowd; Echochrome changes the
  projection that makes fixed geometry temporarily traversable.
- Tin Hearts also pauses, accelerates and redirects autonomous walkers, but the
  player repositions physical routing devices and receives a prospective path
  overlay rather than making screen coincidence authoritative.
- Braid shares autonomous locomotion, contact collection, visibility and live
  time, but its player directly controls Tim and rewinds history; projection
  never rewrites route topology.
- Fez is the key falsification control: its directly controlled avatar traverses
  one of four settled cardinal collision slices. Echochrome's Walker is
  autonomous and its useful projection may occur at continuously varying angles.
- Viewfinder turns a held image into physical geometry and overwrites part of
  the world. Echochrome retains all path coordinates and only changes the
  route interpretation of their current screen projection.

## Normalised genome

| Type | IDs | Key parameters |
|---|---|---|
| Action | `ACT-006`, `ACT-095` | Walker speed multiplier; continuous camera orbit |
| System | `SYS-037`, `SYS-045`, `SYS-121` | contact credit; autonomous walk; projection-authoritative topology |
| Constraint | `CON-143` | no direct locomotion; camera/pause/speed only |
| Information | `INF-001`, `INF-042` | visible current maze; live authoritative screen relation |
| Objective | `OBJ-049` | collect every required echo in the bounded stage |
| Time | `TIM-003` | live camera intervention with optional thinking pause |

Compact signature:

`ACT-006,ACT-095; SYS-037,SYS-045,SYS-121; CON-143; INF-001,INF-042; OBJ-049; TIM-003`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `91` (`GAME-0001`–`GAME-0091`).
- Exact genome matches: none.
- Tied near matches: `GAME-0029` — HUMANITY (`4 / 18 = 0.222222`).
- Supported combination subsets: `COMB-0092`.
- Scan date: 2026-08-14.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0029`.

## Coverage decision

- Reuse speed control, contact collection, autonomous locomotion, general
  current visibility and live time from established real-time route systems.
- Add only the five missing boundaries: continuous rule-bearing camera orbit,
  screen-projection topology, camera-only Walker control, live visual authority
  and the all-echo indirectly guided objective.
- Keep Fez collision slicing, Viewfinder world overwrite, physical device
  routing and direct avatar movement outside despite surface similarities.

## Confidence and open questions

### Assumptions

- The local coordinates are a minimal control, not a reconstruction of any
  retail Echochrome stage.
- The PSP/PS3 core rules share the two scoped perspective laws even though
  their authored stage sets and some platform controls differ.

### Unknowns

- Exact production tolerances for endpoint snapping and occluder coverage were
  not measured.
- Pair/Others mode ordering, multiple-Walker collision and every later law
  interaction remain outside the bounded packet.

### Confidence

- High for autonomous guidance, continuous perspective control, apparent
  endpoint connection, hidden-gap continuity and the all-echo objective.
- Medium-high for pause/speed details across both release platforms because
  the primary product descriptions emphasise the shared rules more than every
  button mapping.

## Combination candidate

- Candidate ID: `COMB-0092`.
- Gene set: `ACT-095`, `SYS-045`, `SYS-121`, `CON-143`, `INF-042`, `OBJ-049`.
- Supporting game: `GAME-0092`.
- Proper-subset rationale: `ACT-006`, `SYS-037`, `INF-001` and `TIM-003`
  support rate, collection, visibility and scheduling but do not define the
  perspective-governed indirect route.
- Novelty claim: not assessed.

## Outcome

- Reused genes: `ACT-006`, `SYS-037`, `SYS-045`, `INF-001`, `TIM-003`.
- Added genes: `ACT-095`, `SYS-121`, `CON-143`, `INF-042`, `OBJ-049`.
- Added combination: `COMB-0092`.
- Evidence gate: passed with three official Sony/PlayStation records, one
  official trailer, one independent hands-on source, one academic account and
  one executable verifier.
- Nearest prior genome: HUMANITY; see `Corpus comparison` for the current
  result.
- Next falsification target: a perspective puzzle where apparent alignment
  changes traversal for a directly controlled object or under a discrete
  camera set rather than continuous autonomous guidance.

## Taxonomy impact

- Rule-bearing camera orbit is separated from both free inspection and Fez's
  four-state world rotation.
- Screen-space route authority is separated from physical geometry mutation,
  front-layer selection and portal linkage.
- Indirect control is made explicit: pause and speed affect the Walker's clock,
  while perspective is the only route-shaping player channel.

## Negative results

- No path endpoint or occluder changes world coordinates in the scoped route.
- A visually close but non-coincident endpoint does not become connected.
- A gap remains a gap when visible or when the supposed occluder lies behind it.
- The player cannot steer the Walker as a conventional avatar.
- The verifier does not claim exact retail-stage geometry or cover the other
  three perspective laws.
