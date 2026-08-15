---
game_id: GAME-0093
slug: monument-valley
game_title: Monument Valley
analysis_status: reviewed
reviewed: 2026-08-14
combination_ids:
  - COMB-0093
gene_ids:
  action:
    - ACT-085
    - ACT-096
  system:
    - SYS-122
    - SYS-123
  constraint:
    - CON-144
  information:
    - INF-001
    - INF-043
  objective:
    - OBJ-026
  time:
    - TIM-002
---

# Game: Monument Valley

## Analysis scope

- Version / ruleset: original 2014 Monument Valley core rules, bounded to
  Chapter I, Prelude. The authored packet begins with Ida separated from the
  final pedestal by the central marked bridge and ends after the bridge is
  rotated into its route-bearing snap state and the pedestal is selected. A
  separate four-node executable control isolates the same component-to-
  projection-to-destination sequence.
- Included: one fixed orthographic camera; one visibly marked rotating bridge;
  authored snap poses; depth-separated navigation nodes; screen-space node
  connection after settle; current reachability marking; selection of a remote
  reachable destination; automatic multi-node walking; arrival at the chapter
  pedestal; self-paced sequencing.
- Excluded: Chapters II–X; floor buttons, Crow People, ladders, doors, movable
  blocks, Totem, gravity reorientation and later transformations; Forgotten
  Shores and Ida's Dream; story text, achievements, hints, soundtrack,
  platform-specific pointer labels and Panoramic Edition framing.
- Direct-play status: not conducted. Ustwo's official records establish Ida,
  impossible architecture, optical illusions and hidden paths. The current
  developer-authored product description establishes monument manipulation and
  evolving routes. Technical director Peter Pashley's account directly
  establishes projected node connection, depth ordering, snap-only decisions
  and reachable-node highlights. Two independent walkthroughs corroborate the
  exact Chapter I rotate-then-select boundary. The local control proves only a
  normalised four-node route, not the retail scene geometry.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MON-001` | Monument Valley is Ustwo's 2014 impossible-architecture puzzle about guiding Ida through monuments | Confirmed | Direct | High | P1, P2 |
| `MON-002` | The player manipulates monument components to reveal paths through optical illusions | Confirmed | Direct | High | P1, P3 |
| `MON-003` | Walkable navigation nodes are attached to visible geometry and automatic connections are resolved in camera depth order | Confirmed | Direct | High | P4 |
| `MON-004` | Traversal decision points are evaluated only when manipulated geometry occupies a snap position | Confirmed | Direct | High | P4 |
| `MON-005` | Nodes reachable in the current configuration are highlighted, and the highlighted set shifts with geometry | Confirmed | Direct | High | P4 |
| `MON-006` | Selecting a reachable point makes Ida traverse the intervening current route without step-level direction commands | Confirmed | Corroborated | High | P4, S1, S2 |
| `MON-007` | Chapter I completes by rotating the central beam into a connection and selecting the final patterned pedestal | Confirmed | Corroborated | High | S1, S2 |
| `MON-008` | The control's aligned bridge creates two projected joins across retained world depth and one four-node route | Observation | Direct | High | V1, MON-003–MON-007 |
| `MON-009` | Monument Valley differs from Fez because one physical component moves while the camera remains fixed, and from Echochrome because the route is evaluated only after snap and Ida moves by destination command | Observation | Corroborated | High | P4, GAME-0091, GAME-0092 |
| `MON-010` | The scoped packet has no random transition, resource consumption, direct locomotion or continuously authoritative moving-camera state | Observation | Corroborated | High | P3, P4, S1, V1 |

## Basic data

- Release / origin: developed and published by Ustwo Games; the original game
  launched on iOS in 2014, with later Android and Panoramic editions.
- Platform or physical form: single-player touch-first spatial puzzle shown as
  a self-contained isometric monument under a fixed orthographic view.
- Puzzle family: discrete architectural manipulation followed by projected-
  node destination traversal.
- Primary and creator sources:
  - **[P1]** [Ustwo Games — Monument Valley](https://ustwogames.co.uk/our-games/monument-valley/),
    for Ida, mysterious monuments, hidden paths, optical illusions and
    impossible geometry.
  - **[P2]** [Ustwo Games — ten years of Monument Valley](https://ustwogames.co.uk/mv10/),
    for the original 2014 launch and the studio's impossible-architecture
    framing.
  - **[P3]** [Monument Valley on Steam](https://store.steampowered.com/app/1927720/Monument_Valley__Panoramic_Edition/),
    an Ustwo-authored product record for manipulating monuments, creating
    evolving paths and transforming landscapes by pushing, pulling, clicking,
    raising and lowering.
  - **[P4]** [Game Developer — Making the impossible possible in Monument Valley](https://www.gamedeveloper.com/design/making-the-impossible-possible-in-i-monument-valley-i-),
    with technical director Peter Pashley, for walkable nodes, automatic
    projected connections, depth ordering, dual floor/ladder nodes, snap-only
    decision points and current reachable-node highlights.
- Reproducible corroboration:
  - **[S1]** [Pocket Gamer — complete Monument Valley walkthrough](https://www.pocketgamer.com/monument-valley/how-to-finish-monument-valley-the-complete-walkthrough-to-ustwos-escher-like-adv/),
    published at launch, for rotating the Chapter I middle beam and tapping the
    patterned panel at the stair top.
  - **[S2]** [Into Indie Games — Monument Valley Chapters 1 & 2](https://intoindiegames.com/walkthroughs/monument-valley-walkthrough-chapters-1-2/),
    for holding and rotating the Chapter I valve until the path appears, then
    selecting the large square exit.
  - **[A1]** [GDC Vault — The Art of Monument Valley](https://www.gdcvault.com/play/1022476/The-Art-of-Monument),
    by lead designer Ken Wong, for optical-illusion puzzles, impossible
    geometry and visuals integrated with gameplay.
  - **[V1]**
    [`verify_monument_valley_control.py`](../../../scripts/verify_monument_valley_control.py),
    an executable two-snap model of physical bridge rotation, projected node
    connection, reachable marking, destination pathfinding and six rejected
    invalid transitions.

## Mechanical decomposition

### Action Genes

- `ACT-085` — manipulate constrained diegetic component. The player drags the
  marked central bridge around its authored local pivot and releases it into a
  supported settled orientation; the camera and fixed banks do not move.
- `ACT-096` — select reachable world destination. After the aligned route is
  visible, the player selects the patterned pedestal rather than supplying
  each step of Ida's walk.
- `ACT-008`, `ACT-094` and `ACT-095` are absent. Ida is not driven by local
  directional inputs, the world is not globally rotated through four views,
  and no rule-bearing camera is freely orbited.

### System Behaviour Genes

- `SYS-122` — snap-state projected-node connectivity. Once the bridge settles,
  the navigation system orders its visible nodes in camera depth and connects
  eligible apparent neighbours. World-depth-separated nodes can therefore
  form the route the fixed screen image presents.
- `SYS-123` — destination-commanded route traversal. Selecting the reachable
  pedestal finds the current path and advances Ida through its bridge nodes to
  arrival without further locomotion commands.
- `SYS-120` is absent because no global front-layer collision slice is rebuilt
  after camera rotation. `SYS-121` is absent because fixed geometry under a
  continuously changing projection is not live-authoritative: the bridge
  itself moves and traversal decisions wait for snap.
- Resolution order: accept bridge gesture; rotate the addressed component;
  settle at an authored pose; rebuild projected navigation-node connections;
  update reachable markings; accept one reachable destination; compute the
  path; animate Ida through it; evaluate pedestal arrival.

### Constraint Genes

- `CON-144` — traversal decisions require settled architecture. An intermediate
  bridge angle supplies neither a selectable route nor a stable graph; only an
  authored snap state can be queried for reachability.
- The destination command is also reachability-gated. The disconnected
  pedestal cannot be used speculatively and decoration is not a navigation
  target.
- Scarce strategic resources: none consumed. The bounded chapter has no move
  cap, deadline or failure-producing random event.

### Information Genes

- `INF-001` — fully visible current state. Ida, the bridge, its marked control,
  the fixed approach, the goal-side path and the pedestal are all visible in
  the bounded screen.
- `INF-043` — current reachable destinations are visibly marked. The game
  exposes which nodes accept a destination command in the settled pose and
  shifts that reachable set after the bridge changes configuration.
- This is not a complete route forecast. The interface exposes current
  destination eligibility, while the system owns the exact intervening path.

### Objective Genes

- `OBJ-026` — reach designated traversable world location. Chapter I ends when
  the bridge has made the final pedestal reachable and Ida arrives there.
- No collectible or inventory token is acquired inside the bounded control;
  the ceremonial chapter transition follows arrival and is not a separate
  mechanical objective.

### Time Genes

- `TIM-002` — self-paced sequential action. The player may inspect indefinitely
  before rotating or selecting, and the world does not independently advance
  the decision state between completed commands.
- Ida's walking animation resolves a destination command but introduces no
  concurrent adversary, timer or forced-progression decision window.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Ida is at the Chapter I approach and the central bridge is crosswise | inspect the screen | only the current start-side node is reachable; the pedestal cannot accept the route command | visible current reachability | `MON-005`, `MON-007` |
| The bridge is settled at 90 degrees | begin dragging its marked control | the component rotates physically while route decisions are suspended | diegetic manipulation and settle gate | `MON-002`, `MON-004` |
| The bridge passes through an intermediate angle | release before an authored pose | the control rejects that angle as a traversal-decision state | snap-only topology | `MON-004`, `MON-008` |
| Bridge endpoints occupy `(1,0,2)` and `(2,0,2)` while fixed nodes occupy `(1,0,0)` and `(2,0,0)` | settle at 0 degrees | each depth-separated pair shares one screen position and becomes a navigation edge | projected-node connection | `MON-003`, `MON-008` |
| The aligned graph contains start, two bridge nodes and goal | inspect selectable surfaces | all four nodes are marked reachable from Ida's position | dynamic destination disclosure | `MON-005`, `MON-008` |
| The pedestal is marked reachable | select the goal node once | the system finds `start → bridge-left → bridge-right → goal` and walks Ida through it | destination pathfinding without step inputs | `MON-006`, `MON-008` |
| Ida arrives at the patterned pedestal | evaluate the bounded chapter | the destination is credited and Chapter I completes | location-reaching objective | `MON-007`, `MON-008` |

The executable control separately rejects direct step steering, the
disconnected goal, a decorative non-node, destination selection during bridge
motion, an unsupported 45-degree decision state and editing after completion.
It also proves that the connected bridge still occupies different world depth
from both fixed banks: the accepted joins are projected, not Euclidean.

## Strategic and experiential structure

- Local decision: identify the marked manipulable component and determine
  which settled orientation makes the visible route continuous.
- Medium-term planning: separate world-reconfiguration commands from later
  destination commands; Ida cannot be sent across until the graph settles.
- Long-term structure: later chapters repeat this grammar with more components,
  switches and orientation-dependent surfaces, but those additions are outside
  this minimal packet.
- Common heuristics: follow circular handle markings; wait for a clean snap;
  read screen continuity rather than world depth; select the farthest confirmed
  reachable surface; let Ida clear a movable component before changing it.
- Failure attribution: a rejected destination is explained by current
  reachability, component pose or input target rather than randomness.
- Player-trust factors: snap timing, projected node matching, reachable
  highlighting, path selection and arrival must agree with the same screen.

## Replay and variation

- What changes between chapters: monument layout, manipulator class, snap
  poses, switches, doors, character orientation, Crow People and destination.
- Randomness or procedural generation: none in the scoped authored chapter.
- Multiple viable strategies: Chapter I has one short intended relation;
  later scenes may allow harmless exploratory component states or different
  intermediate stopping points.
- Typical replay motive: revisit the visual transformation, take screenshots,
  complete later included content or replay the short narrative sequence.

## Adjacent systems and history

- Carto is the nearest complete genome because both are self-paced, show the
  current world, make a destination traversably connected and then move the
  player-controlled character there. Carto relocates persistent map fragments
  and uses direct local walking; Monument Valley rotates a local monument
  component, rebuilds projected nodes and accepts a remote destination.
- Machinarium shares constrained diegetic manipulation, visibility and
  self-paced interaction. Its scrapyard sequence changes item and avatar
  configuration rather than projected route connectivity.
- Fez keeps every trile fixed and rotates the global camera/world frame through
  four cardinal slices before directly controlled platforming. Monument Valley
  keeps the camera fixed and rotates one physical component before pathfinding.
- Echochrome keeps every path fixed, allows continuous camera orbit and guides
  an already autonomous Walker. Monument Valley waits for discrete physical
  settle and moves Ida only after a destination command.
- The Room also uses visibly constrained mechanisms, but their persistent lock
  state exposes nested evidence and parts rather than an impossible route.

## Normalised genome

| Type | IDs | Key parameters |
|---|---|---|
| Action | `ACT-085`, `ACT-096` | rotate marked bridge; select reachable pedestal |
| System | `SYS-122`, `SYS-123` | snap-state projected graph; automatic destination route |
| Constraint | `CON-144` | route decisions only at authored settled poses |
| Information | `INF-001`, `INF-043` | visible monument; marked current reachability |
| Objective | `OBJ-026` | bring Ida to the final pedestal |
| Time | `TIM-002` | untimed sequential manipulation and selection |

Compact signature:

`ACT-085,ACT-096; SYS-122,SYS-123; CON-144; INF-001,INF-043; OBJ-026; TIM-002`

## Corpus comparison

The comparison scanned every complete `GAME-0001`–`GAME-0092` signature with
canonical Jaccard intersection over union.

- Near match: `GAME-0040` Carto is uniquely nearest at
  `3 / 14 = 0.214286`.

| Prior game | Shared genes | Boundary | Jaccard |
|---|---|---|---:|
| `GAME-0040` — Carto | `INF-001`, `OBJ-026`, `TIM-002` | relocates map fragments, then uses direct local walking; no projected-node graph | nearest, `3 / 14 = 0.214286` |
| `GAME-0064` — SET | `INF-001`, `TIM-002` | selects a simultaneous visual triple, not a world destination | control, `2 / 12 = 0.166667` |
| `GAME-0086` — Machinarium | `ACT-085`, `INF-001`, `TIM-002` | manipulates scene mechanisms for avatar reconstruction | control, `3 / 19 = 0.157895` |
| `GAME-0091` — Fez | `INF-001`, `OBJ-026` | rotates a global cardinal view and directly steers Gomez | falsification control, `2 / 16 = 0.125000` |
| `GAME-0092` — Echochrome | `INF-001` | continuously orbits fixed paths around an autonomous Walker | falsification control, `1 / 18 = 0.055556` |

No prior full signature is exact, no prior combination equals the candidate and
no prior combination is a supported subset of the complete genome. The result
falsifies merging the three adjacent perspective systems: Fez moves the global
frame, Echochrome moves only the camera, and Monument Valley moves one
addressed component before a destination command.

- Full numeric scan (`intersection / union = Jaccard`):
  - `GAME-0001`: `1 / 22 = 0.045455`; `GAME-0002`: `2 / 14 = 0.142857`; `GAME-0003`: `0 / 18 = 0.000000`; `GAME-0004`: `1 / 23 = 0.043478`; `GAME-0005`: `2 / 14 = 0.142857`; `GAME-0006`: `2 / 16 = 0.125000`; `GAME-0007`: `2 / 15 = 0.133333`; `GAME-0008`: `2 / 14 = 0.142857`.
  - `GAME-0009`: `1 / 24 = 0.041667`; `GAME-0010`: `1 / 17 = 0.058824`; `GAME-0011`: `2 / 20 = 0.100000`; `GAME-0012`: `2 / 16 = 0.125000`; `GAME-0013`: `1 / 21 = 0.047619`; `GAME-0014`: `1 / 23 = 0.043478`; `GAME-0015`: `1 / 22 = 0.045455`; `GAME-0016`: `1 / 23 = 0.043478`.
  - `GAME-0017`: `0 / 22 = 0.000000`; `GAME-0018`: `1 / 27 = 0.037037`; `GAME-0019`: `1 / 18 = 0.055556`; `GAME-0020`: `1 / 22 = 0.045455`; `GAME-0021`: `1 / 17 = 0.058824`; `GAME-0022`: `1 / 20 = 0.050000`; `GAME-0023`: `1 / 18 = 0.055556`; `GAME-0024`: `1 / 20 = 0.050000`.
  - `GAME-0025`: `1 / 19 = 0.052632`; `GAME-0026`: `1 / 20 = 0.050000`; `GAME-0027`: `1 / 20 = 0.050000`; `GAME-0028`: `1 / 25 = 0.040000`; `GAME-0029`: `1 / 20 = 0.050000`; `GAME-0030`: `1 / 22 = 0.045455`; `GAME-0031`: `1 / 19 = 0.052632`; `GAME-0032`: `1 / 19 = 0.052632`.
  - `GAME-0033`: `1 / 21 = 0.047619`; `GAME-0034`: `1 / 22 = 0.045455`; `GAME-0035`: `1 / 26 = 0.038462`; `GAME-0036`: `2 / 19 = 0.105263`; `GAME-0037`: `1 / 17 = 0.058824`; `GAME-0038`: `1 / 24 = 0.041667`; `GAME-0039`: `2 / 16 = 0.125000`; `GAME-0040`: `3 / 14 = 0.214286`.
  - `GAME-0041`: `1 / 19 = 0.052632`; `GAME-0042`: `1 / 17 = 0.058824`; `GAME-0043`: `1 / 22 = 0.045455`; `GAME-0044`: `1 / 18 = 0.055556`; `GAME-0045`: `1 / 22 = 0.045455`; `GAME-0046`: `2 / 17 = 0.117647`; `GAME-0047`: `1 / 22 = 0.045455`; `GAME-0048`: `1 / 22 = 0.045455`.
  - `GAME-0049`: `0 / 18 = 0.000000`; `GAME-0050`: `1 / 23 = 0.043478`; `GAME-0051`: `1 / 24 = 0.041667`; `GAME-0052`: `1 / 18 = 0.055556`; `GAME-0053`: `1 / 17 = 0.058824`; `GAME-0054`: `2 / 18 = 0.111111`; `GAME-0055`: `1 / 18 = 0.055556`; `GAME-0056`: `1 / 16 = 0.062500`.
  - `GAME-0057`: `1 / 16 = 0.062500`; `GAME-0058`: `1 / 17 = 0.058824`; `GAME-0059`: `1 / 15 = 0.066667`; `GAME-0060`: `1 / 15 = 0.066667`; `GAME-0061`: `2 / 17 = 0.117647`; `GAME-0062`: `2 / 15 = 0.133333`; `GAME-0063`: `2 / 14 = 0.142857`; `GAME-0064`: `2 / 12 = 0.166667`.
  - `GAME-0065`: `1 / 15 = 0.066667`; `GAME-0066`: `1 / 18 = 0.055556`; `GAME-0067`: `0 / 17 = 0.000000`; `GAME-0068`: `1 / 16 = 0.062500`; `GAME-0069`: `2 / 15 = 0.133333`; `GAME-0070`: `1 / 16 = 0.062500`; `GAME-0071`: `2 / 14 = 0.142857`; `GAME-0072`: `2 / 15 = 0.133333`.
  - `GAME-0073`: `2 / 14 = 0.142857`; `GAME-0074`: `2 / 16 = 0.125000`; `GAME-0075`: `2 / 16 = 0.125000`; `GAME-0076`: `2 / 14 = 0.142857`; `GAME-0077`: `2 / 14 = 0.142857`; `GAME-0078`: `2 / 14 = 0.142857`; `GAME-0079`: `2 / 14 = 0.142857`; `GAME-0080`: `2 / 14 = 0.142857`.
  - `GAME-0081`: `2 / 15 = 0.133333`; `GAME-0082`: `2 / 15 = 0.133333`; `GAME-0083`: `2 / 15 = 0.133333`; `GAME-0084`: `2 / 17 = 0.117647`; `GAME-0085`: `2 / 18 = 0.111111`; `GAME-0086`: `3 / 19 = 0.157895`; `GAME-0087`: `1 / 18 = 0.055556`; `GAME-0088`: `2 / 16 = 0.125000`.
  - `GAME-0089`: `1 / 17 = 0.058824`; `GAME-0090`: `2 / 22 = 0.090909`; `GAME-0091`: `2 / 16 = 0.125000`; `GAME-0092`: `1 / 18 = 0.055556`.

## Coverage decision

- Reuse constrained diegetic manipulation, complete current visibility,
  designated-location completion and self-paced sequencing.
- Add only the missing boundaries: remote destination selection, snap-state
  projected connectivity, destination route traversal, settle-only decisions
  and visible current destination eligibility.
- Keep direct locomotion, global camera rotation, continuous perspective law,
  image-created geometry and switch systems outside this minimal chapter.

## Confidence and open questions

### Assumptions

- The local coordinates normalise the Chapter I decision structure and do not
  reconstruct its art, exact navigation mesh or proprietary node tolerances.
- The original touch release and later Panoramic release preserve the scoped
  rotate-then-select rule despite different pointer hardware.

### Unknowns

- Exact production snap tolerance, node highlight shader and pathfinder tie-
  breaking were not measured.
- Whether any input is buffered during Ida's short Chapter I walk is outside
  the control and does not affect the bounded causal chain.

### Confidence

- High for component manipulation, snap-only graph decisions, visible current
  reachability, destination selection and Chapter I completion order.
- Medium-high for the exact original touch presentation of every highlight,
  because the technical account describes the production system across levels
  while the walkthroughs document the authored Chapter I sequence.

## Combination candidate

- Candidate ID: `COMB-0093`.
- Gene set: `ACT-085`, `ACT-096`, `SYS-122`, `SYS-123`, `CON-144`, `INF-043`,
  `OBJ-026`.
- Supporting game: `GAME-0093`.
- Proper-subset rationale: `INF-001` and `TIM-002` support general visibility
  and scheduling but do not define the architecture-to-destination interaction.
- Novelty claim: not assessed.

## Outcome

- Reused genes: `ACT-085`, `INF-001`, `OBJ-026`, `TIM-002`.
- Added genes: `ACT-096`, `SYS-122`, `SYS-123`, `CON-144`, `INF-043`.
- Added combination: `COMB-0093`.
- Evidence gate: passed with three Ustwo-authored records, one developer
  technical account, one creator GDC record, two independent walkthroughs and
  one executable verifier.
- Nearest prior genome: Carto at `3 / 14 = 0.214286`.
- Next falsification target: a perspective route where the player rotates the
  entire fixed frame, directly steers the avatar or manipulates a component
  continuously while traversal remains live.

## Taxonomy impact

- Local physical component rotation is separated from camera or world-frame
  rotation.
- Projected-node connectivity at snap is separated from both ordinary physical
  adjacency and continuously authoritative perspective.
- Player ownership of an avatar is separated from locomotion input granularity:
  selecting Ida's destination is direct control without direct route steps.

## Negative results

- The camera does not rotate in the scoped chapter.
- The crosswise bridge does not make the pedestal reachable.
- A 45-degree intermediate gesture pose is not a traversal decision state.
- The player does not steer Ida across each individual node.
- The verifier does not claim exact retail coordinates or later chapter rules.

## Delta summary

- Added one reviewed game record and one verified combination.
- Added one Action, two System Behaviour, one Constraint and one Information
  gene.
- Extended four reused genes with Monument Valley evidence.
- Added an executable two-snap four-node route control.

## Нові факти

- Monument Valley фізично повертає позначений елемент, а не камеру.
- Навігаційні зв'язки перебудовуються лише після фіксації у snap-стані.
- Досяжні точки видно, а один вибір цілі запускає повний маршрут Іди.
- Контроль довів два проєкційні стики, чотиривузловий маршрут і шість
  відхилених невалідних переходів.

## Нові гени

- `ACT-096` — вибрати досяжну світову ціль замість покрокового руху.
- `SYS-122` — перебудувати проєкційні вузлові зв'язки після snap.
- `SYS-123` — автоматично пройти маршрут до вибраної цілі.
- `CON-144` — рішення про рух можливі лише після фіксації архітектури.
- `INF-043` — поточні досяжні цілі позначені візуально.

## Нові комбінації

- `COMB-0093` — snap-архітектура, що відкриває вибір і автоматичний прохід до
  віддаленої цілі.

## Зміни таксономії

- Фізичне обертання одного мосту відокремлено від глобального повороту Fez.
- Дискретну вузлову проєкцію відокремлено від живого закону Echochrome.
- Вибір цілі відокремлено від прямого керування кожним кроком аватара.

## Український підсумок

У першому розділі Monument Valley гравець не повертає камеру і не керує кожним
кроком Іди. Він обертає позначений міст до одного з дозволених положень. Після
фіксації гра заново визначає, які видимі вузли з'єднані, і позначає доступні
цілі. Натискання на фінальний п'єдестал запускає весь маршрут Іди автоматично.
Це ближче до Carto за послідовністю «зміни світ — дійди до місця», але Carto
пересуває частини карти й використовує локальну ходу: `3 / 14 = 0.214286`.

## Research log

- 2026-08-14: selected as `GAME-0093` to separate discrete local
  architecture, remote destination control and snap-state projection from Fez
  and Echochrome.
- Bounded Chapter I Prelude from the crosswise bridge to pedestal arrival.
- Used Ustwo and developer technical evidence to establish projected node
  connection, snap-only decisions and dynamic reachable marking.
- Added an executable four-node control with six rejected invalid transitions.
- Classified nine genes and confirmed `COMB-0093` as a proper subset.
- Exhaustively compared the signature with all 92 prior genomes; Carto is
  uniquely nearest at `3 / 14 = 0.214286`.
