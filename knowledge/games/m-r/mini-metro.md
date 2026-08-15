---
game_id: GAME-0018
slug: mini-metro
game_title: Mini Metro
analysis_status: reviewed
reviewed: 2026-08-11
combination_ids:
  - COMB-0018
  - COMB-0037
  - COMB-0051
gene_ids:
  action:
    - ACT-006
    - ACT-023
    - ACT-024
    - ACT-025
  system:
    - SYS-004
    - SYS-029
    - SYS-030
    - SYS-031
    - SYS-032
  constraint:
    - CON-047
    - CON-048
    - CON-049
    - CON-050
    - CON-051
    - CON-052
  information:
    - INF-001
    - INF-002
  objective:
    - OBJ-002
  time:
    - TIM-003
---

# Game: Mini Metro

## Analysis scope

- Version / ruleset: one single-player Classic-mode session on an ordinary
  official city map under the current cross-platform core rules.
- Included: shaped stations and passengers; drawing, extending, rerouting and
  removing coloured lines; assigning locomotives and carriages; automatic
  train movement, boarding, transfers and delivery; map water and limited
  tunnels or bridges; weekly locomotives and upgrade choices; pause, normal and
  accelerated simulation speed; delivered-passenger score; overcrowding
  countdown and terminal failure.
- Excluded: Endless, Expert and Creative modes, daily and weekly challenges,
  multiplayer, achievements, unlock requirements, leaderboards, Workshop and
  custom maps, map-specific special rolling stock and presentation-only audio
  or colour options.
- Direct-play status: not conducted for this record. Developer and publisher
  descriptions establish the core loop; detailed capacity, destination and
  overload rules are corroborated by secondary and community references.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MET-001` | The player draws persistent coloured lines through stations and may extend, reroute or remove them in Classic mode | Confirmed | Direct | High | F1, F3, F4 |
| `MET-002` | Each line is an ordered unbranched station route; shared stations connect separate lines for passenger transfers | Observation | Corroborated | High | F3, F5 |
| `MET-003` | Assigned trains traverse lines automatically, and passengers board, transfer and leave without stop-by-stop player commands | Confirmed | Direct | High | F3, F4, F5 |
| `MET-004` | New stations appear at system-selected locations as simulation time passes | Confirmed | Direct | High | F1, F2, F3 |
| `MET-005` | Destination-marked passengers appear at stations over time, and their shape identifies the station class they seek | Confirmed | Corroborated | High | F3, F5 |
| `MET-006` | Lines, locomotives, carriages and crossings form finite reusable inventories that must be allocated among competing routes | Confirmed | Direct | High | F1, F3 |
| `MET-007` | A segment crossing map water requires an available tunnel or bridge resource | Confirmed | Corroborated | High | F3, F5 |
| `MET-008` | Vehicle capacity bounds automatic pickup, so unboarded passengers remain in the station queue | Confirmed | Corroborated | High | F4, F5 |
| `MET-009` | At each in-game week's end the system grants a locomotive and offers a choice of an additional upgrade | Confirmed | Direct | High | F3 |
| `MET-010` | Sustained excess waiting demand starts a visible station countdown; relieving demand can recover it, while a filled countdown ends Classic mode | Confirmed | Corroborated | High | F3, F5, F6 |
| `MET-011` | Each completed passenger trip increases the session's score, which Classic mode maximises until failure | Confirmed | Corroborated | High | F4, F5 |
| `MET-012` | Current stations, lines, vehicles, waiting passengers, inventory and overload state are visible, but future station and passenger arrivals are not previewed | Observation | Corroborated | High | F1, F3–F5 |
| `MET-013` | The player may pause for network edits or run the simulation at an accelerated clock rate | Confirmed | Corroborated | High | F3, F7 |
| `MET-014` | Random station layouts make repeated sessions on the same city mechanically different | Confirmed | Direct | High | F2, F3 |
| `MET-015` | A route remains reusable infrastructure after transport; train traversal neither consumes nor locks its serviced stations | Observation | Corroborated | High | MET-001–MET-003 |

## Basic data

- Origin: created as *Mind the Gap* during Ludum Dare 26 in 2013; released
  commercially by Dinosaur Polo Club, with the desktop version leaving Early
  Access in November 2015.
- Platform scope: cross-platform core Classic rules; control gestures and map-
  specific content are parameters.
- Puzzle family: stochastic real-time transport-network management.
- Sources:
  - **[F1]** [Official Mini Metro game page](https://dinopoloclub.com/games/mini-metro/),
    primary description of drawing and redrawing lines, new stations and
    limited-resource allocation.
  - **[F2]** [Dinosaur Polo Club press kit](https://dinopoloclub.com/press/mini-metro/),
    primary history, Classic-mode distinction, dynamic-city variation and
    upgrades.
  - **[F3]** [Robert Curry's official gameplay guide](https://blog.playstation.com/archive/2019/09/09/5-gameplay-tips-for-subway-puzzle-sim-mini-metro-out-on-ps4-tomorrow/),
    designer-authored evidence for automatic service, editable lines, weekly
    rewards, resource reassignment, pause, randomness and overload failure.
  - **[F4]** [Official Steam product page](https://store.steampowered.com/app/287980/Mini_Metro/),
    publisher description of routes, commuters, station queues, score mode and
    release metadata.
  - **[F5]** [Mini Metro gameplay summary](https://en.wikipedia.org/wiki/Mini_Metro_(video_game)),
    secondary corroboration of shape destinations, transfers, vehicle
    capacity, water crossings and Classic failure.
  - **[F6]** [Mini Metro Wiki — Normal mode](https://mini-metro.fandom.com/wiki/Normal),
    community documentation of the overload grace indicator, recovery and
    weekly budgets; used only where primary descriptions are less granular.
  - **[F7]** [Mini Metro Wiki — Beta 12](https://mini-metro.fandom.com/wiki/Beta_12),
    community release-history record for the pause, fast-forward and keyboard
    simulation-speed controls.
- Claim IDs: `MET-001`–`MET-015`.

## Mechanical decomposition

### Action Genes

- `ACT-023` — edit ordered transit line. The player draws a named line through
  stations and may extend, reroute, shorten or remove it; the action changes
  service topology rather than directly moving a passenger.
- `ACT-024` — reassign transport capacity. Locomotives and carriages are
  deployed or moved among eligible lines to change frequency and carrying
  capacity.
- `ACT-025` — choose periodic network upgrade. At a weekly boundary the player
  selects one offered infrastructure reward after the automatic locomotive
  award.
- `ACT-006` — accelerate automatic progression. The player may run the city at
  a faster simulation rate; pause is recorded as a `TIM-003` parameter rather
  than a separate mechanical gene.
- Claim IDs: `MET-001`, `MET-006`, `MET-009`, `MET-013`.

### System Behaviour Genes

- `SYS-004` — random outcome selection. Station positions and types, passenger
  arrivals and eligible reward offers are selected by the system.
- `SYS-029` — time-driven station appearance. New destination nodes expand the
  spatial problem without a player placement command.
- `SYS-030` — time-driven destination demand arrival. Shaped waiting
  passengers accumulate at existing stations as the clock advances.
- `SYS-031` — automatic route-based passenger transport. Trains traverse their
  assigned lines and resolve boarding, transfer and delivery subject to
  topology, destination and capacity.
- `SYS-032` — periodic capacity award and upgrade offer. Each weekly boundary
  grants the locomotive and constructs the additional bounded choice.
- Claim IDs: `MET-003`–`MET-005`, `MET-008`, `MET-009`, `MET-014`, `MET-015`.

### Constraint Genes

- `CON-047` — finite reassignable network inventory. A deployed line,
  locomotive, carriage or crossing is unavailable elsewhere until reclaimed.
- `CON-048` — unbranched ordered route topology. One coloured line is an
  ordered open route or permitted loop; branching service is represented by
  separate lines meeting at transfer stations.
- `CON-049` — geography-gated crossing consumption. Crossing map water ties up
  a limited tunnel or bridge until the relevant segment is removed.
- `CON-050` — capacity-bounded passenger pickup. A full vehicle leaves further
  eligible passengers waiting even when it serves the correct route.
- `CON-051` — shape-coded destination completion. A passenger completes only
  at a station matching its displayed destination shape.
- `CON-052` — sustained station-overload termination. Excess waiting demand is
  recoverable during a grace interval, but any completed overload indicator
  ends the session.
- `CON-001` is absent: official stations expand dynamically and are not a fixed
  set of persistent addressed cells. `CON-029` and `CON-030` are also absent:
  separate lines may share stations for transfers, and routes remain editable
  reusable infrastructure rather than exclusive puzzle paths.
- Claim IDs: `MET-002`, `MET-005`–`MET-010`.

### Information Genes

- `INF-001` — fully visible current state. Current topology, station types,
  passenger queues, moving vehicles, asset inventory, score, clock and
  overload indicators are public.
- `INF-002` — unpreviewed random future event. The exact next station opening,
  passenger arrival and their timing or location are not displayed in advance.
- `INF-003` is absent because future stations and demand have not been encoded
  as a concealed fixed board awaiting reveal; they are generated progression
  events.
- Claim IDs: `MET-004`, `MET-005`, `MET-012`, `MET-014`.

### Objective Genes

- `OBJ-002` — maximise accumulated score. Each completed trip raises the
  delivered-passenger count, and Classic play continues to improve that score
  until terminal overload.
- Overcrowding remains `CON-052`, not a second Objective: it is a failure
  predicate the player manages while pursuing the scored measurement.
- Claim IDs: `MET-010`, `MET-011`.

### Time Genes

- `TIM-003` — real-time input during forced progression. While the clock runs,
  stations, passenger queues and vehicles change independently as the player
  edits and reallocates the network.
- Pausing supplies unbounded planning time and fast-forward changes the rate;
  both are timing parameters. They do not turn the running simulation into
  discrete post-command resolution.
- Claim IDs: `MET-003`–`MET-005`, `MET-009`, `MET-013`.

## Reproducible transitions

| Before | Player action or elapsed event | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Three initial stations are unconnected | Draw one coloured line through them | A persistent ordered route appears and its assigned train begins service | Topology edit and automatic movement are separate | `MET-001`, `MET-003` |
| A new station opens beyond a line endpoint | Drag the endpoint to that station | Route sequence grows; serving vehicles include the added stop | Dynamic nodes are integrated by line editing | `MET-004` |
| Two lines share a station | Allow a passenger whose destination is on the other line to travel | Passenger may leave one train, wait and board through the shared transfer | Shared nodes connect otherwise separate sequences | `MET-002`, `MET-003` |
| A locomotive is full at a station with eligible demand | Let it stop | Capacity-limited riders board and the remainder stay queued | Connectivity alone does not guarantee immediate service | `MET-008` |
| A proposed segment crosses water with no free crossing | Attempt the edit | Segment cannot remain deployed until a tunnel or bridge is reclaimed | Geography consumes finite infrastructure | `MET-006`, `MET-007` |
| The weekly boundary arrives | No route command | System grants a locomotive and presents an additional upgrade choice | Reward generation precedes player selection | `MET-009` |
| A station exceeds waiting capacity | Let time continue without sufficient pickup | Its overload indicator advances toward failure | Excess demand has a grace interval | `MET-010` |
| The overloaded station is serviced in time | Reduce its waiting queue | Indicator stops or recedes and the session continues | Overload is recoverable before the terminal boundary | `MET-010` |
| Any overload indicator fills | Let time advance | Classic session ends and delivered-passenger score is finalised | Failure is local in cause but global in effect | `MET-010`, `MET-011` |

## Strategic and experiential structure

- Local decision: extend a nearby line, create a transfer, or move rolling
  stock to the queue most likely to overflow first.
- Medium-term planning: balance route length, repeated station shapes,
  transfer load, vehicle frequency and crossing scarcity instead of merely
  connecting every node.
- Long-term structure: preserve spare routes and capacity for random city
  growth while using weekly choices to relieve the limiting bottleneck.
- Common heuristic: alternate common station shapes on lines and avoid forcing
  too much demand through one transfer; these are strategies, not rules.
- Failure attribution: the next growth event is uncertain, but visible queues,
  capacities, routes and overload clocks expose why the present system is
  failing.
- Player-trust factor: edits must predictably change automatic routing and
  asset reclamation, because the player does not command individual riders.
- Claim IDs: `MET-001`–`MET-015`.

## Replay and variation

- What changes: generated station positions and shapes, passenger demand,
  weekly offers, resulting bottlenecks and the player's evolving network.
- What remains stable: line editing, automatic transport, finite inventory,
  shaped destinations, weekly cadence and sustained-overload termination.
- Randomness: new city nodes and demand are generated beyond the current
  visible state rather than exposed from a fixed concealed layout.
- Multiple viable strategies: short shuttle lines, loops and transfer-centred
  layouts trade directness, frequency and load concentration differently.
- Typical replay motive: increase score on one city and adapt a network to a
  new generated layout.
- Claim IDs: `MET-004`–`MET-014`.

## Adjacent systems and history

- Flow Free's gesture creates terminal, cell-exclusive endpoint paths on a
  fixed board. Mini Metro repeatedly edits named routes on expanding geometry,
  permits transfer-node sharing and delegates traversal to autonomous agents.
- Pipe Dream also runs a network-like system in real time, but a visible forced
  tile queue constructs one consumptive flow route. Mini Metro has no forced
  piece queue; its infrastructure remains reusable and transport is cyclic.
- Tetris shares unpreviewed random inputs, speed control and forced real-time
  progression, but operates one gravity-driven active element in a fixed
  capacity rather than a persistent multi-route service system.
- The original *Mind the Gap* prototype and later map-specific variants are
  historically adjacent but require their own scope if their rules change
  route or capacity boundaries.
- Claim IDs: `MET-001`–`MET-015`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-006`, `ACT-023`, `ACT-024`, `ACT-025` | pause / speed control, edit gestures and asset transition delay |
| System Behaviour | `SYS-004`, `SYS-029`, `SYS-030`, `SYS-031`, `SYS-032` | distributions, cadence, routing and service speed |
| Constraint | `CON-047`, `CON-048`, `CON-049`, `CON-050`, `CON-051`, `CON-052` | inventory counts, map geometry, capacities and grace time |
| Information | `INF-001`, `INF-002` | display conventions and undisclosed event distributions |
| Objective | `OBJ-002` | passengers delivered before failure |
| Time | `TIM-003` | pause availability and simulation speeds |

Canonical signature:

`ACT-006,ACT-023,ACT-024,ACT-025; SYS-004,SYS-029,SYS-030,SYS-031,SYS-032; CON-047,CON-048,CON-049,CON-050,CON-051,CON-052; INF-001,INF-002; OBJ-002; TIM-003`

## Corpus comparison

- Indexed games scanned: `GAME-0001`–`GAME-0017`.
- Indexed combinations scanned: `COMB-0001`–`COMB-0017`.
- Exact genome matches: none.
- Existing combination subsets: none.
- Jaccard scores against complete genomes:
  - `GAME-0001`: shared `SYS-004`, `INF-001`, `INF-002`, `OBJ-002`; `4 / 29 = 0.137931`.
  - `GAME-0002`: shared `INF-001`; `1 / 25 = 0.040000`.
  - `GAME-0003`: no shared genes; `0 / 28 = 0.000000`.
  - `GAME-0004`: shared `ACT-006`, `SYS-004`, `INF-001`, `OBJ-002`, `TIM-003`; `5 / 29 = 0.172414`.
  - `GAME-0005`: shared `INF-001`; `1 / 25 = 0.040000`.
  - `GAME-0006`: shared `INF-001`; `1 / 27 = 0.037037`.
  - `GAME-0007`: shared `INF-001`; `1 / 26 = 0.038462`.
  - `GAME-0008`: shared `INF-001`; `1 / 25 = 0.040000`.
  - `GAME-0009`: shared `SYS-004`, `INF-001`, `INF-002`; `3 / 32 = 0.093750`.
  - `GAME-0010`: shared `INF-001`; `1 / 27 = 0.037037`.
  - `GAME-0011`: shared `INF-001`; `1 / 31 = 0.032258`.
  - `GAME-0012`: shared `INF-001`; `1 / 27 = 0.037037`.
  - `GAME-0013`: shared `INF-001`; `1 / 31 = 0.032258`.
  - `GAME-0014`: shared `INF-001`; `1 / 33 = 0.030303`.
  - `GAME-0015`: shared `SYS-004`, `INF-001`, `OBJ-002`; `3 / 30 = 0.100000`.
  - `GAME-0016`: shared `ACT-006`, `SYS-004`, `INF-001`, `OBJ-002`, `TIM-003`; `5 / 29 = 0.172414`.
  - `GAME-0017`: no shared genes; `0 / 32 = 0.000000`.
- Mathematically selected near matches: `GAME-0004` — Tetris and `GAME-0016`
  — Pipe Mania / Pipe Dream, tied at `0.172414`.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0004` — Tetris | `ACT-006`, `SYS-004`, `INF-001`, `OBJ-002`, `TIM-003` | Tetris controls one active falling element inside fixed capacity; Mini Metro edits persistent routes and reallocates autonomous multi-vehicle service as nodes and demand grow | Near match only |
| `GAME-0016` — Pipe Mania / Pipe Dream | `ACT-006`, `SYS-004`, `INF-001`, `OBJ-002`, `TIM-003` | Pipe Dream consumes a forced preview queue to build ahead of one locking flow; Mini Metro has random unpreviewed growth, reversible route edits and cyclic capacity-bounded transport | Near match only |

- New genes: `ACT-023`–`ACT-025`, `SYS-029`–`SYS-032`, `CON-047`–`CON-052`.
- Classification result: `New gene` and a new verified combination.
- Evidence and reasoning: direct sources establish player-owned topology and
  allocation decisions separately from automatic growth and service. The new
  boundaries keep route form, inventory, vehicle capacity, destination
  compatibility and terminal overload from collapsing into a generic
  “network” label.
- Scan date: 2026-08-11.

## Taxonomy impact

- Registry changes: thirteen new bounded IDs; reused genes `ACT-006`,
  `SYS-004`, `INF-001`, `INF-002`, `OBJ-002` and `TIM-003` gain a Mini Metro
  example.
- Taxonomy-change record: none. Existing definitions were expanded only with
  in-boundary examples and parameters.
- Candidate terms affected: route editing, network allocation, timed growth,
  autonomous transport, bounded capacity and overload are promoted to the
  stable IDs listed above.

## Negative results

- No structured negative-result file was required. `ACT-016`, `CON-029` and
  `CON-030` were explicitly rejected because Mini Metro routes are editable,
  reusable and may share transfer stations; `SYS-025` and `CON-041` were
  rejected because train traversal neither consumes nor locks the network.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Player line edits and transport allocation remain
  distinct from automatic city growth and service (`MET-001`–`MET-009`).
- [Confirmed | Corroborated | High] Station overload is recoverable during a
  grace countdown but terminal if the countdown fills (`MET-010`).

## Нові гени

- [Observation | Direct / Corroborated | High] Added `ACT-023`–`ACT-025`,
  `SYS-029`–`SYS-032` and `CON-047`–`CON-052`.

## Нові комбінації

- [Observation | Direct / Corroborated | High] `COMB-0018` captures editable
  finite transit infrastructure under unpreviewed real-time demand and
  sustained-overload failure.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає.

## Нові питання

- Does a later transport game reuse automatic route-based passenger transport
  while replacing random growth with a fixed demand schedule?
- Should periodic upgrade offers remain one behaviour when a future game grants
  resources without presenting a player choice?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] `GAME-0019` — Peg Solitaire, traditional
  English 33-hole central-vacancy problem.
- Optimisation criterion: restore deterministic mechanical distance after a
  stochastic real-time network system.
- Expected information gain: test jump-and-remove action boundaries, monotonic
  material reduction, dead-end reachability and exact final occupancy.
- Backlog impact: Peg Solitaire leaves the pool; Dorfromantik remains.

## Чому саме вона

- [Hypothesis | Limited | High] Peg Solitaire should share visibility,
  self-paced time and fixed capacity with deterministic board puzzles while
  testing a capture-by-jump reduction mechanic absent from the corpus.
