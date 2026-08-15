---
game_id: GAME-0091
slug: fez
game_title: Fez
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0091
gene_ids:
  action:
    - ACT-008
    - ACT-094
  system:
    - SYS-036
    - SYS-120
  constraint:
    - CON-142
  information:
    - INF-001
    - INF-041
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Fez

## Analysis scope

- Version / ruleset: original Fez traversal rules, bounded to the first Village
  fireplace tutorial after Gomez receives the fez and world rotation becomes
  available. The authored packet begins inside the front room before the
  fireplace transition and ends after two legal quarter-turns expose the rear
  continuation and Gomez walks through it. A separate three-support executable
  control isolates one equivalent single-quarter-turn adjacency rewrite.
- Included: walking and jumping; clockwise or counterclockwise 90-degree view
  rotation; four settled horizontal orthographic views; transition-time action
  suspension; front-to-back visible collision; avatar depth correction;
  projection-relative adjacency; fixed underlying world geometry; reaching the
  previously hidden rear compartment.
- Excluded: the chest and key after traversal, cube bits, cube-count doors,
  codes, language and number systems, anti-cubes, treasure maps, first-person
  New Game Plus view, movable objects, ladders, bombs, switches, hazards,
  narrative, achievements, later areas and platform-specific button labels.
- Direct-play status: not conducted. Polytron's official fact sheet and Steam
  record establish the four-view traversal premise. Programmer Renaud Bédard's
  collision article and GDC postmortem directly document orthographic frames,
  front-layer collision, depth correction and rotation suspension. Two
  walkthrough records identify the first Village fireplace boundary. The local
  control proves only the normalised fixed-platform transition.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FEZ-001` | Fez is Polytron's 2D/3D exploration puzzle platformer, first released on Xbox 360 on 13 April 2012 | Confirmed | Direct | High | P2, P4 |
| `FEZ-002` | The player navigates 3D structures from four distinct classic 2D perspectives | Confirmed | Direct | High | P1, P2, P4 |
| `FEZ-003` | One input rotates to the adjacent cardinal view by 90 degrees rather than freely orbiting the camera | Confirmed | Corroborated | High | P2, P4, S3 |
| `FEZ-004` | Settled collision is resolved from the current 2D view front-to-back, keeping the first eligible solid layer | Confirmed | Direct | High | P3, P4 |
| `FEZ-005` | Gomez's hidden depth is corrected to remain visible and supported, while otherwise avoiding arbitrary depth changes | Confirmed | Direct | High | P3, P4 |
| `FEZ-006` | Movement and simulation time are suspended during a view rotation | Confirmed | Direct | High | P4 |
| `FEZ-007` | Rotation can change the legal traversal continuation without relocating fixed triles in world coordinates | Confirmed | Corroborated | High | P2–P4, A1 |
| `FEZ-008` | The first Village fireplace tutorial is traversed by standing before the empty fireplace, rotating 180 degrees and walking out the other side | Confirmed | Corroborated | High | S1, S2 |
| `FEZ-009` | The control's north view exposes A–B while its east view exposes B–C, producing one route over three unchanged supports | Observation | Direct | High | V1, FEZ-003–FEZ-007 |
| `FEZ-010` | Viewfinder is not the same system: Fez recomputes active collision over retained geometry instead of instantiating and deleting geometry | Observation | Corroborated | High | P3, P4, GAME-0041 |
| `FEZ-011` | The bounded packet has no random transition, inventory payment or permanent world edit | Observation | Corroborated | High | P2–P4, S1 |

## Basic data

- Release / origin: developed by Polytron; Xbox Live Arcade release on 13 April
  2012, followed by Windows on 1 May 2013.
- Platform or physical form: single-player platform exploration through a
  three-dimensional trile world presented as four rule-bearing orthographic
  side views.
- Puzzle family: fixed-world orthographic projection that rewrites traversable
  adjacency.
- Primary and creator sources:
  - **[P1]** [Fez on Steam](https://store.steampowered.com/app/224760/FEZ/),
    for the four distinct 2D perspectives, open-ended exploration and product
    framing.
  - **[P2]** [Polytron press-kit fact sheet](https://upload.wikimedia.org/wikipedia/commons/0/04/Fez_%28video_game%29_press_kit_fact_sheet.pdf),
    for developer, publisher, releases, 2D platforming in a 3D world and
    environment rotation that changes the landscape.
  - **[P3]** [Renaud Bédard — Behind Fez: Collision and Physics](https://theinstructionlimit.com/behind-fez-collision-and-physics),
    for front-to-back visible collision, first-solid-layer selection and the
    three avatar-depth correction rules.
  - **[P4]** [Renaud Bédard — Cubes All The Way Down](https://theinstructionlimit.com/wp-content/uploads/2012/03/fez_tech_postmort_pdf_no_notes.pdf),
    for four orthographic views, view-plane motion, collision peeling, depth
    correction and suspended movement/time during rotations.
- Reproducible corroboration:
  - **[S1]** [XBLAFans — Fez Cube Guide: The Village](https://xblafans.com/fez-cube-guide-the-village-45460.html),
    for the empty-fireplace instruction, 180-degree rotation and walking out
    the other side.
  - **[S2]** [GameFAQs — Fez guide and walkthrough](https://gamefaqs.gamespot.com/pc/945079-fez/faqs/66903),
    for rotation becoming available after the reboot and the initial Village
    traversal boundary.
  - **[S3]** [Save or Quit — Fez review](https://saveorquit.com/?p=61585),
    for left/right 90-degree rotation controls and ordinary platforming.
  - **[A1]** [Ferland and Kher — NP-Hardness of a 2D, a 2.5D, and a 3D Puzzle Game](https://arxiv.org/abs/2202.10529),
    for the independent formal framing of Fez as switching among four 2D views
    of one position.
  - **[V1]**
    [`verify_fez_control.py`](../../../scripts/verify_fez_control.py), an
    executable three-support model of cardinal projection, front-layer
    activation, adjacency rewrite and six rejected invalid transitions.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate controllable agent. Gomez walks and jumps along the
  currently active two-dimensional collision slice.
- `ACT-094` — rotate world to adjacent orthographic view. One left or right
  input requests a cardinal quarter-turn; individual triles are not selected,
  dragged or given new coordinates.
- `ACT-056` is absent because no persistent map fragment changes adjacency by
  relocation. `ACT-057` is absent because the player holds and commits no
  image. A free inspection camera is access, not this rule-bearing action.

### System Behaviour Genes

- `SYS-036` — continuous force-constrained body dynamics. In each settled
  frame Gomez runs, jumps, falls, lands and collides in real time.
- `SYS-120` — view-relative front-layer collision rewrites traversal adjacency.
  The settled view peels collision candidates front-to-back, activates the
  first solid layer at a screen position and corrects Gomez onto visible,
  supported depth. A different view can therefore expose another legal edge
  between unchanged world supports.
- `SYS-075` and `SYS-076` are absent: Fez neither stamps projected content into
  the world nor destroys geometry behind it. `SYS-074` is absent because no
  map-piece identity is moved. The visual turn changes the authoritative
  traversal projection, not the stored trile coordinates.
- Resolution order: accept one legal quarter-turn; lock movement and time;
  animate relative depth; settle the adjacent cardinal frame; rebuild visible
  front-layer collision; correct avatar depth only as required for visibility
  and support; resume real-time traversal.

### Constraint Genes

- `CON-142` — four cardinal orthographic traversal frames. Only the four
  horizontal axis-aligned views are ordinary traversal states, each command
  advances one step around that cycle, and movement is unavailable mid-turn.
- The two-turn 180-degree fireplace solution is two legal atomic quarter-turns,
  not a separate half-turn action. Some later rooms restrict rotation, but
  those authored exceptions are outside this packet.
- Scarce strategic resources: none consumed. The decision resource is which
  projection to make authoritative before walking or jumping.

### Information Genes

- `INF-001` — fully visible current state. Within the current frame, Gomez,
  visible triles, ledges and the immediate continuation are inspectable, with
  no concealed random mutation.
- `INF-041` — rotation reveals depth between flattened traversal views. The
  transition temporarily displays side/depth relations that a settled
  orthographic endpoint collapses, then shows the new active front layer.
- This does not promise an exact future-route overlay. Occluded world depth may
  require rotation to inspect, but the transition itself supplies the relevant
  spatial evidence rather than revealing a hidden symbolic answer.

### Objective Genes

- `OBJ-026` — reach designated traversable world location. The bounded task
  ends when projection changes make the fireplace's rear continuation
  traversable and Gomez walks into that compartment.
- The later chest key is excluded, so neither contact collection nor a
  progress-token objective enters this signature.

### Time Genes

- `TIM-003` — real-time input during forced progression. In settled views,
  gravity and avatar motion continue between commands. The view transition is
  a documented local suspension inside that real-time system, not a separate
  turn-based ruleset.
- `TIM-002` is rejected because Gomez may fall without another input while a
  settled frame runs. The scoped task has no deadline, rewind or random clock.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Gomez has received the fez and a Village room is settled | request one left or right turn | the adjacent 90-degree view animates while movement and time are suspended | cardinal action and transition lock | `FEZ-003`, `FEZ-006` |
| Two triles occupy one screen position at different depths | allow the turn to settle | collision searches front-to-back and retains the first eligible solid layer | view-relative collision | `FEZ-004` |
| Gomez would be hidden or unsupported at retained depth | settle the new frame | depth is corrected onto a visible supported layer, but otherwise remains unchanged | bounded depth correction | `FEZ-005` |
| Fixed supports A `(0,0,0)`, B `(1,0,0)`, C `(1,0,1)` are viewed from north | walk A to B | A and B are adjacent; C is hidden behind B in the same projected column | first edge of control route | `FEZ-009` |
| Gomez stands on B and the supports retain their coordinates | rotate once east and settle | B remains active, A is occluded behind it and C now occupies the adjacent projected column | adjacency changes without geometry motion | `FEZ-007`, `FEZ-009` |
| East view exposes B–C | walk B to C | the target is reached through the newly authoritative collision slice | projection-relinked traversal | `FEZ-009` |
| Gomez stands before the Village room's empty fireplace | issue two legal quarter-turns, then walk | the rear continuation becomes the visible traversable side and Gomez exits through it | authored boundary control | `FEZ-008` |

The executable control separately rejects a hidden destination, an atomic
half-turn, physical support relocation, movement during transition, a second
turn before settling and traversal onto an occluded far support. It also proves
that four quarter-turns close the cardinal view cycle.

## Strategic and experiential structure

- Local decision: recognise whether the current projection contains the next
  usable edge; if not, rotate one step and reassess visible support.
- Medium-term planning: route through a three-dimensional structure as a
  sequence of locally two-dimensional walks and projection changes, preserving
  safe support at every settle.
- Long-term structure: build a mental model of which apparently continuous
  surfaces are depth-separated and which separated silhouettes can become
  adjacent from another side.
- Common heuristics: rotate before attempting a long jump; watch the depth
  revealed during transition; keep Gomez on an unambiguous frontmost support;
  test both neighbouring views; distinguish background decoration from solid
  front-layer triles.
- Failure attribution: a failed continuation is explained by the current view,
  occlusion, support or landing rather than random state.
- Player-trust factors: cardinal orientation, frontmost selection, depth snap,
  rotation lock and post-turn collision must remain deterministic.

## Replay and variation

- What changes between tasks: fixed 3D trile geometry, heights, occlusion,
  ladders, moving elements, available view directions and target location.
- Randomness or procedural generation: none in the scoped authored packet.
- Multiple viable strategies: the fireplace requires a net 180-degree change,
  which may be composed clockwise or counterclockwise; larger areas can permit
  several view sequences and platform routes.
- Typical replay motive: take a shorter rotation sequence, collect an omitted
  item or reinterpret a familiar flat silhouette from another side.

## Adjacent systems and history

- Viewfinder is the nearest complete genome because both have avatar
  navigation, live body dynamics, visible current geometry and real-time play.
  Viewfinder consumes a perspective image to instantiate and delete geometry;
  Fez keeps fixed world coordinates and swaps the collision projection.
- Portal also preserves world geometry and changes traversal connectivity, but
  it does so through two player-placed apertures and continuous body mapping,
  not a global cardinal view slice.
- Carto also changes reachability before avatar traversal, but the player
  explicitly relocates persistent map fragments. Fez changes neither platform
  identity nor coordinates.
- A Monster's Expedition physically moves logs into bridges. Fez's platforms
  are already present; a new view changes whether their projections connect.

## Normalised genome

| Type | IDs | Key parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-094` | direct platform traversal; left/right quarter-turn |
| System | `SYS-036`, `SYS-120` | live body dynamics; front-layer collision and depth correction |
| Constraint | `CON-142` | four cardinal settled frames; transition movement lock |
| Information | `INF-001`, `INF-041` | visible current slice; transient depth disclosure |
| Objective | `OBJ-026` | reach hidden rear compartment after relinking route |
| Time | `TIM-003` | real-time settled traversal with local rotation suspension |

Compact signature:

`ACT-008,ACT-094; SYS-036,SYS-120; CON-142; INF-001,INF-041; OBJ-026; TIM-003`

## Corpus comparison

The comparison scanned every complete `GAME-0001`–`GAME-0090` signature with
canonical Jaccard intersection over union.

- Near match: `GAME-0041` Viewfinder is uniquely nearest at
  `4 / 16 = 0.250000`.

| Prior game | Shared genes | Boundary | Jaccard |
|---|---|---|---:|
| `GAME-0041` — Viewfinder | `ACT-008`, `SYS-036`, `INF-001`, `TIM-003` | commits finite perspective images that instantiate and erase world geometry; no cardinal global collision slice | nearest, `4 / 16 = 0.250000` |
| `GAME-0033` — Portal | `ACT-008`, `SYS-036`, `INF-001`, `TIM-003` | places paired apertures and preserves continuous momentum through them | second, `4 / 18 = 0.222222` |
| `GAME-0040` — Carto | `ACT-008`, `INF-001`, `OBJ-026` | relocates persistent map fragments to alter world topology | third, `3 / 14 = 0.214286` |
| `GAME-0021` — Cut the Rope | `SYS-036`, `INF-001`, `TIM-003` | cuts supports around one continuously simulated payload; no avatar or view-state topology | control, `3 / 15 = 0.200000` |

No prior full signature is exact, no prior combination equals the candidate and
no prior combination is a supported subset of the complete genome. The result
falsifies reuse of Viewfinder's perspective-instantiation combination: four
generic real-time spatial genes survive, but source-image stock, world
overwrite and rewind do not.

- Full numeric scan (`intersection / union = Jaccard`):
  - `GAME-0001`: `1 / 22 = 0.045455`; `GAME-0002`: `1 / 15 = 0.066667`; `GAME-0003`: `0 / 18 = 0.000000`; `GAME-0004`: `2 / 22 = 0.090909`; `GAME-0005`: `1 / 15 = 0.066667`; `GAME-0006`: `2 / 16 = 0.125000`; `GAME-0007`: `1 / 16 = 0.062500`; `GAME-0008`: `1 / 15 = 0.066667`.
  - `GAME-0009`: `1 / 24 = 0.041667`; `GAME-0010`: `1 / 17 = 0.058824`; `GAME-0011`: `1 / 21 = 0.047619`; `GAME-0012`: `1 / 17 = 0.058824`; `GAME-0013`: `1 / 21 = 0.047619`; `GAME-0014`: `1 / 23 = 0.043478`; `GAME-0015`: `1 / 22 = 0.045455`; `GAME-0016`: `2 / 22 = 0.090909`.
  - `GAME-0017`: `0 / 22 = 0.000000`; `GAME-0018`: `2 / 26 = 0.076923`; `GAME-0019`: `1 / 18 = 0.055556`; `GAME-0020`: `1 / 22 = 0.045455`; `GAME-0021`: `3 / 15 = 0.200000`; `GAME-0022`: `1 / 20 = 0.050000`; `GAME-0023`: `0 / 19 = 0.000000`; `GAME-0024`: `1 / 20 = 0.050000`.
  - `GAME-0025`: `2 / 18 = 0.111111`; `GAME-0026`: `3 / 18 = 0.166667`; `GAME-0027`: `2 / 19 = 0.105263`; `GAME-0028`: `2 / 24 = 0.083333`; `GAME-0029`: `3 / 18 = 0.166667`; `GAME-0030`: `3 / 20 = 0.150000`; `GAME-0031`: `1 / 19 = 0.052632`; `GAME-0032`: `1 / 19 = 0.052632`.
  - `GAME-0033`: `4 / 18 = 0.222222`; `GAME-0034`: `3 / 20 = 0.150000`; `GAME-0035`: `3 / 24 = 0.125000`; `GAME-0036`: `2 / 19 = 0.105263`; `GAME-0037`: `1 / 17 = 0.058824`; `GAME-0038`: `4 / 21 = 0.190476`; `GAME-0039`: `1 / 17 = 0.058824`; `GAME-0040`: `3 / 14 = 0.214286`.
  - `GAME-0041`: `4 / 16 = 0.250000`; `GAME-0042`: `1 / 17 = 0.058824`; `GAME-0043`: `2 / 21 = 0.095238`; `GAME-0044`: `2 / 17 = 0.117647`; `GAME-0045`: `2 / 21 = 0.095238`; `GAME-0046`: `1 / 18 = 0.055556`; `GAME-0047`: `1 / 22 = 0.045455`; `GAME-0048`: `1 / 22 = 0.045455`.
  - `GAME-0049`: `0 / 18 = 0.000000`; `GAME-0050`: `2 / 22 = 0.090909`; `GAME-0051`: `2 / 23 = 0.086957`; `GAME-0052`: `1 / 18 = 0.055556`; `GAME-0053`: `2 / 16 = 0.125000`; `GAME-0054`: `3 / 17 = 0.176471`; `GAME-0055`: `2 / 17 = 0.117647`; `GAME-0056`: `1 / 16 = 0.062500`.
  - `GAME-0057`: `1 / 16 = 0.062500`; `GAME-0058`: `1 / 17 = 0.058824`; `GAME-0059`: `1 / 15 = 0.066667`; `GAME-0060`: `1 / 15 = 0.066667`; `GAME-0061`: `1 / 18 = 0.055556`; `GAME-0062`: `1 / 16 = 0.062500`; `GAME-0063`: `1 / 15 = 0.066667`; `GAME-0064`: `1 / 13 = 0.076923`.
  - `GAME-0065`: `0 / 16 = 0.000000`; `GAME-0066`: `0 / 19 = 0.000000`; `GAME-0067`: `0 / 17 = 0.000000`; `GAME-0068`: `0 / 17 = 0.000000`; `GAME-0069`: `1 / 16 = 0.062500`; `GAME-0070`: `1 / 16 = 0.062500`; `GAME-0071`: `1 / 15 = 0.066667`; `GAME-0072`: `1 / 16 = 0.062500`.
  - `GAME-0073`: `1 / 15 = 0.066667`; `GAME-0074`: `1 / 17 = 0.058824`; `GAME-0075`: `1 / 17 = 0.058824`; `GAME-0076`: `1 / 15 = 0.066667`; `GAME-0077`: `1 / 15 = 0.066667`; `GAME-0078`: `1 / 15 = 0.066667`; `GAME-0079`: `1 / 15 = 0.066667`; `GAME-0080`: `1 / 15 = 0.066667`.
  - `GAME-0081`: `1 / 16 = 0.062500`; `GAME-0082`: `1 / 16 = 0.062500`; `GAME-0083`: `1 / 16 = 0.062500`; `GAME-0084`: `1 / 18 = 0.055556`; `GAME-0085`: `0 / 20 = 0.000000`; `GAME-0086`: `1 / 21 = 0.047619`; `GAME-0087`: `2 / 17 = 0.117647`; `GAME-0088`: `1 / 17 = 0.058824`.
  - `GAME-0089`: `1 / 17 = 0.058824`; `GAME-0090`: `2 / 22 = 0.090909`.

## Coverage decision

- Reuse navigation, live body physics, current visibility, location-reaching
  and real-time genes shared with existing spatial games.
- Add only the four missing boundaries: cardinal world-view action,
  front-layer collision rewrite, four-frame restriction and rotational depth
  disclosure.
- Keep physical world edits, portal topology, map relocation and image
  instantiation excluded even though each can also create a new route.

## Confidence and open questions

### Assumptions

- The local three-support model is a minimal mechanical control, not a claim
  that the fireplace room uses those exact coordinates.
- The press-kit and GDC descriptions apply to the released core traversal
  rules; the detailed collision article describes the evolving production
  engine but agrees with the later postmortem on the admitted rules.

### Unknowns

- Platform-specific buffering of chained rotation inputs was not tested.
- Reduced-motion presentation and every later moving-object depth exception are
  outside the bounded packet.

### Confidence

- High for four cardinal views, 90-degree commands, front-layer collision,
  depth correction, transition lock and unchanged underlying geometry.
- Medium-high for the exact visual sequence of the fireplace tutorial because
  direct play was not conducted.

## Combination candidate

- Candidate ID: `COMB-0091`.
- Gene set: `ACT-008`, `ACT-094`, `SYS-120`, `CON-142`, `INF-041`, `OBJ-026`.
- Supporting game: `GAME-0091`.
- Proper-subset rationale: `SYS-036`, `INF-001` and `TIM-003` support ordinary
  live platforming but do not define the projection-relinked route.
- Novelty claim: not assessed.

## Outcome

- Reused genes: `ACT-008`, `SYS-036`, `INF-001`, `OBJ-026`, `TIM-003`.
- Added genes: `ACT-094`, `SYS-120`, `CON-142`, `INF-041`.
- Added combination: `COMB-0091`.
- Evidence gate: passed with two official product records, two creator
  technical records, two walkthrough controls, one independent formal source
  and one executable verifier.
- Nearest prior genome: Viewfinder at `4 / 16 = 0.250000`.
- Next falsification target: a fixed-world game whose camera rotation changes
  visible alignment but not collision or legal traversal.

## Taxonomy impact

- A rule-bearing view rotation is separated from camera inspection because it
  selects the collision plane used by subsequent avatar actions.
- Apparent adjacency is separated from physical geometry mutation: the same
  world coordinates support different legal edges under different projections.
- Rotational animation earns an Information gene only because it exposes the
  depth relation needed to interpret the next collision slice.

## Negative results

- The environment does not rotate as a rigid gravity puzzle; down remains down
  and the horizontal view frame changes.
- A settled 2D overlap is not a portal and does not pair persistent endpoints.
- No platform is dragged into place, no image source is consumed and no world
  geometry is overwritten in the scoped transition.
- The verifier establishes one minimal route, not every production collision
  exception or the exact Village mesh.

## Delta summary

- Added one reviewed game record and one verified combination.
- Added one Action, one System Behaviour, one Constraint and one Information
  gene.
- Extended five reused genes with Fez evidence.
- Added an executable four-view fixed-support control.

## Нові факти

- Fez має чотири горизонтальні ортографічні стани огляду.
- Один крок повороту дорівнює 90 градусам, а рух і час під час переходу
  призупиняються.
- Після повороту система заново обирає передній шар зіткнень і коригує глибину
  Гомеса, не пересуваючи платформи у світових координатах.
- Контроль довів маршрут A–B–C через дві різні проєкції та шість відхилень.

## Нові гени

- `ACT-094` — повернути світ до сусіднього ортографічного виду.
- `SYS-120` — залежні від виду передній шар зіткнень і суміжність маршруту.
- `CON-142` — чотири кардинальні ортографічні рамки пересування.
- `INF-041` — поворот показує глибину між сплощеними видами.

## Нові комбінації

- `COMB-0091` — поворот незмінного світу у проєкційно з'єднаний маршрут.

## Зміни таксономії

- Правило повороту світу відокремлено від вільної камери й фізичного руху
  об'єктів.
- Зміну активної суміжності відокремлено від створення, видалення чи
  телепортації геометрії.

## Український підсумок

Fez не пересуває платформу, щоб побудувати міст, і не створює її з картинки.
Гравець повертає весь спосіб читання незмінного 3D-світу на один із чотирьох
плоских боків. Після переходу передній видимий шар стає активним для зіткнень,
а глибина Гомеса коригується до опори. Через це дві точки, розділені в одному
виді, можуть стати сусідніми в іншому. Найближчий Viewfinder поділяє чотири
загальні гени, але фізично створює та стирає геометрію: `4 / 16 = 0.250000`.

## Research log

- 2026-08-14: selected as `GAME-0091` to test traversal through a
  representation-changing orthographic rotation.
- Bounded the first Village fireplace tutorial and excluded its later chest,
  codes, collectibles and campaign systems.
- Used Polytron's product records and Renaud Bédard's collision/postmortem
  documentation to separate projection from geometry motion.
- Added an executable three-support, four-view control with six rejections.
- Classified nine genes and confirmed `COMB-0091` as a proper subset.
- Exhaustively compared the signature with all 90 prior genomes; Viewfinder is
  uniquely nearest at `4 / 16 = 0.250000`.
