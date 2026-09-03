---
game_id: GAME-0030
slug: tin-hearts
game_title: Tin Hearts
analysis_status: reviewed
reviewed: 2026-08-12
combination_ids:
  - COMB-0030
  - COMB-0034
gene_ids:
  action:
    - ACT-006
    - ACT-043
    - ACT-044
  system:
    - SYS-036
    - SYS-045
    - SYS-047
    - SYS-048
    - SYS-056
  constraint:
    - CON-047
  information:
    - INF-001
    - INF-017
  objective:
    - OBJ-019
  time:
    - TIM-003
    - TIM-007
---

# Game: Tin Hearts

## Analysis scope

- Version / ruleset: the 2023 full release, scoped to one ordinary post-tutorial
  single-player level after freely placeable prism blocks and remote pause /
  rewind / fast-forward have been unlocked.
- Included: opening the trinket box; finite successive soldier release;
  autonomous forward walking; collision redirection by moved / rotated prism
  blocks; drums and simple ballistic / bounce routing; hazards; finite reusable
  routing objects; paused path projection; live object repositioning;
  fast-forward; rewind and alternate continuation; fixed exit; rescue threshold.
- Excluded: story interpretation, memories and collectibles, Mr Soldier direct-
  control stages, later power glove / combat, complex machines not required by
  the scoped routing grammar, hints, VR-specific input and cosmetics.
- Direct-play status: not conducted. Two publisher briefing documents and the
  platform-holder product description are combined with contemporary hands-on
  reviews that describe exact block, preview and rewind transitions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TH-001` | Opening the level box releases a supplied group of soldiers that know only forward walking and collision response | Confirmed | Direct | High | P1, P2, S1 |
| `TH-002` | The player moves and orients a finite set of prism blocks and other contraptions to construct a safe route rather than assigning skills to soldiers | Confirmed | Direct | High | P1–P3, S1 |
| `TH-003` | A soldier colliding with an oriented routing face changes direction according to contact geometry and continues autonomously | Confirmed | Corroborated | High | P1, S1, S3 |
| `TH-004` | Drums, cannons and balloon devices apply physical launch, bounce or glide transitions that can bridge vertical or horizontal gaps | Confirmed | Direct | High | P2, P3 |
| `TH-005` | Pausing stops simulation progression and displays a projected route based on the current arrangement | Confirmed | Corroborated | High | S2, S3 |
| `TH-006` | Fast-forward accelerates the unchanged running soldier simulation | Confirmed | Direct | High | P2, P3 |
| `TH-007` | Rewind restores earlier soldier and object states, after which the player can change the arrangement and resume along a different future | Confirmed | Corroborated | High | P2, P3, S1–S3 |
| `TH-008` | Soldiers reaching the exit are credited and enough rescues complete the level; falls or hazards destroy unrescued soldiers | Confirmed | Direct | High | P1, P2, S1 |
| `TH-009` | Routing devices are finite reusable inventory: a block committed at one location must be moved away before serving elsewhere | Confirmed | Corroborated | High | P2, S2, S3 |
| `TH-010` | Current geometry, soldiers, contraptions, exit and rescued progress are visible; projected path is additional prospective information rather than hidden-state disclosure | Confirmed | Corroborated | High | P3, S2 |
| `TH-011` | Tin Hearts shares the Lemmings / HUMANITY release-and-rescue motif but routes through physical world objects and a reversible timeline | Confirmed | Corroborated | High | TH-001–TH-010 |

## Basic data

- Release / origin: Rogue Sun developed Tin Hearts and Wired Productions
  published the full release in 2023.
- Platform or physical form: real-time three-dimensional puzzle adventure with
  physical object manipulation, autonomous toy soldiers and reversible history.
- Puzzle family: reusable physical-device population routing with temporal
  experimentation.
- Publisher primary material:
  - **[P1]** [Wired Productions Demo Guide](https://media.wiredproductions.com/wp-content/uploads/2022/05/Tin-Hearts-DEMO-guide-PDF.pdf),
    describing contraptions that bounce, shoot and glide soldiers toward the
    goal across time-bending routing levels.
  - **[P2]** [Wired Productions Product Deck](https://media.wiredproductions.com/wp-content/uploads/2023/01/Tin_Hearts_Product_Deck-December-2022.pdf),
    stating that soldiers walk forward, bounce from the environment, require a
    player-created path, must be rescued in sufficient number and support pause,
    fast-forward and rewind.
- Platform-holder description:
  - **[P3]** [PlayStation — Tin Hearts](https://www.playstation.com/en-us/games/tin-hearts/),
    documenting repositionable blocks, cannons, trampoline drums, balloon
    machines, route building, goal routing and time controls.
- Contemporary corroboration:
  - **[S1]** [Push Square review](https://www.pushsquare.com/reviews/ps5/tin-hearts),
    describing box-triggered walking, object possession / placement, exit
    routing and rewind that restores a fallen soldier.
  - **[S2]** [VGC review](https://www.videogameschronicle.com/review/tin-hearts/),
    documenting freely placed blocks, freeze-time route preview and reversible
    experimentation.
  - **[S3]** [Nintendo World Report review](https://www.nintendoworldreport.com/review/63557/tin-hearts-switch-review),
    distinguishing peg-bounded early blocks from later freely rotated prism
    blocks and corroborating drums, cannons and time controls.
- Claim IDs: `TH-001`–`TH-011`.

## Mechanical decomposition

### Action Genes

- `ACT-043` — reposition and orient live routing device. The player grabs one
  available prism block or eligible contraption, moves it to a valid physical
  support position and chooses its orientation while the same level state is
  paused or live.
- `ACT-044` — rewind recent simulation history. The player scrubs backward to a
  retained earlier state, restoring soldiers and moved objects, then may stop
  rewinding, edit and resume a divergent outcome.
- `ACT-006` — accelerate automatic progression. Fast-forward increases soldier
  walking and system resolution rate without changing routes or rules.
- `ACT-036` and `ACT-042` are absent: no skill is assigned to one soldier and
  no abstract executable command marker is written into a cell.
- Claim IDs: `TH-002`, `TH-006`, `TH-007`, `TH-009`.

### System Behaviour Genes

- `SYS-045` — continuous autonomous agent locomotion. Released soldiers walk
  forward under the live simulation clock without player step commands.
- `SYS-047` — time-scheduled population release. Opening the box starts
  successive release from a finite supplied troop.
- `SYS-056` — geometry-conditioned collision redirection. Contact with an
  oriented prism or other routing face changes the soldier's travel direction
  according to surface geometry.
- `SYS-036` — continuous force-constrained body dynamics. Drums, cannons,
  balloons, falls and airborne arcs update motion through forces and collision.
- `SYS-048` — terminal-zone population accounting. Exit entry credits rescue;
  destructive falls or hazards remove a soldier without rescue credit.
- `SYS-055` is absent: a block has no stored symbolic Turn / Jump instruction;
  its physical surface and collision determine the response.
- Claim IDs: `TH-001`, `TH-003`, `TH-004`, `TH-008`.

### Constraint Genes

- `CON-047` — finite reassignable network inventory. The scoped level supplies
  a finite set of prism blocks / contraptions; an object already supporting one
  route position cannot be used elsewhere until physically moved and may need
  to be reused after earlier soldiers pass.
- Continuous support, collision clearance and orientation validity are
  parameters of `ACT-043`; they do not instantiate `CON-001` fixed cells.
- Scarce strategic resources: routing-device count, safe support surfaces,
  time window before the next soldier arrives and remaining recoverable troop.
- Claim IDs: `TH-002`, `TH-009`.

### Information Genes

- `INF-001` — fully visible current state. Current soldiers, room geometry,
  devices, hazards, exit and progress are inspectable.
- `INF-017` — prospective autonomous-route projection. While time is frozen,
  the interface draws the path soldiers are predicted to follow under the
  current device arrangement before the player resumes; it does not guarantee
  later edits or all multi-body collision outcomes.
- Claim IDs: `TH-005`, `TH-010`.

### Objective Genes

- `OBJ-019` — rescue minimum population quota through fixed exit. The level
  completes after enough of the finite released troop reaches its destination,
  while rewind can recover otherwise lost soldiers before that history is
  accepted.
- Claim IDs: `TH-008`.

### Time Genes

- `TIM-003` — real-time input during forced progression. While running,
  soldiers walk, collide, fall and enter devices as player interventions remain
  possible; pause and fast-forward alter rate.
- `TIM-007` — branchable player-reversible simulation history. Rewind restores
  a prior authoritative world state, and stopping rewind permits a new edit and
  future that replaces the previously observed outcome.
- Rewind is not only undoing the last discrete placement: it reverses ongoing
  agents and physical consequences across simulation time.
- Claim IDs: `TH-005`–`TH-007`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Closed trinket box contains the level troop | Open the box | Soldiers emerge successively and begin forward walking | release and locomotion are automatic after one start trigger | `TH-001` |
| Prism block faces an approaching soldier at an angle | Give no soldier command | Collision redirects travel according to the block face and walking continues | route response is physical, not symbolic role execution | `TH-003` |
| Soldier approaches a gap below an aimed drum | Give no further input | Drum contact launches the soldier along the current projected arc | continuous dynamics can extend the collision route | `TH-004` |
| Simulation is paused with devices arranged | Move or rotate one prism | Projected soldier route updates before time resumes | action, prediction and later physical resolution remain distinct | `TH-002`, `TH-005` |
| A soldier falls from the table and breaks | Hold rewind | Simulation restores the soldier to an earlier safe state along with relevant object history | rewind restores world state rather than merely restarting the level | `TH-007`, `TH-008` |
| Rewind reaches the moment before the bad collision | Stop, reposition block, resume | Soldier follows a different future route | restored history is branchable through new intervention | `TH-007` |
| A block is needed after earlier soldiers pass it | Move that same block forward | Former routing support disappears and the finite object becomes available at the new location | device scarcity is reusable inventory | `TH-009` |
| Required number of soldiers enters the exit | Give no further input | Rescue accounting reaches threshold and completes the puzzle | reuses fixed-exit quota rescue | `TH-008` |

## Strategic and experiential structure

- Local decision: choose one physical device position / orientation whose
  contact normal, bounce or launch arc sends the next soldier safely onward.
- Medium-term planning: chain collision surfaces and ballistic devices, then
  recycle scarce blocks after earlier soldiers clear them.
- Long-term structure: preserve enough of the finite troop to reach the exit,
  using path projection and rewind to test uncertain three-dimensional timing.
- Common heuristics: pause before moving a device, inspect the projected line,
  separate direction changes from height changes, fast-forward only stable
  spans and rewind immediately after a destructive deviation.
- Failure attribution: prospective paths expose intended routing, while actual
  physical contact and timing reveal whether placement clearance and device
  sequence were robust.
- Player-trust factors: full reversible history makes experimentation forgiving;
  the preview reduces camera / geometry ambiguity without replacing live
  collision verification.
- Claim IDs: `TH-001`–`TH-011`.

## Replay and variation

- What changes between sessions: selected authored room, troop size, device
  inventory, support geometry, hazards and destination.
- Randomness or procedural generation: none in the scoped level grammar.
- Multiple viable strategies: publisher material claims multiple paths;
  continuous placement, orientation, device order and reuse timing can differ.
- Typical replay motive: find a cleaner route, rescue more soldiers, avoid
  rewind or solve later rooms with additional contraptions.
- Claim IDs: `TH-002`, `TH-007`–`TH-011`.

## Adjacent systems and history

- Lemmings shares finite scheduled release, autonomous walking, terminal
  accounting and rescue quota. Tin Hearts changes world objects and simulation
  history instead of spending roles on selected agents.
- HUMANITY shares fast-forward plus the complete release / locomotion /
  accounting / rescue motif. Its abstract persistent commands execute on
  contact for a recurring stream; Tin Hearts uses finite physical devices,
  collision geometry and a finite troop.
- World of Goo shares live physical dynamics, reusable finite structural
  inventory, terminal accounting and rescue quota. World of Goo builds a
  force-bearing structure out of the rescue population itself; Tin Hearts moves
  separate rigid routing devices around the population.
- Claim IDs: `TH-001`–`TH-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-006`, `ACT-043`, `ACT-044` | fast-forward, device manipulation and rewind |
| System Behaviour | `SYS-036`, `SYS-045`, `SYS-047`, `SYS-048`, `SYS-056` | physics, walking, release, accounting and collision routing |
| Constraint | `CON-047` | finite reusable routing devices |
| Information | `INF-001`, `INF-017` | current state and paused path projection |
| Objective | `OBJ-019` | minimum troop rescue through exit |
| Time | `TIM-003`, `TIM-007` | live progression plus branchable reversible history |

Canonical signature:

`ACT-006,ACT-043,ACT-044; SYS-036,SYS-045,SYS-047,SYS-048,SYS-056; CON-047; INF-001,INF-017; OBJ-019; TIM-003,TIM-007`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `29` (`GAME-0001`–`GAME-0029`).
- Exact genome matches: none.
- Tied near matches: `GAME-0029` — HUMANITY (`7 / 19 = 0.368421`).
- Supported combination subsets: `COMB-0030`, `COMB-0034`.
- Scan date: 2026-08-12.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0029` — HUMANITY | `ACT-006`, `SYS-045`, `SYS-047`, `SYS-048`, `INF-001`, `OBJ-019`, `TIM-003` | persistent symbolic world commands and recurring people versus rigid physical routing objects, finite troop and rewind | Near, `0.368421` |

### Preserved research notes

- New genes: `ACT-043`, `ACT-044`, `SYS-056`, `INF-017`, `TIM-007`.
- Classification result: `New gene` and a new verified combination.
- Evidence and reasoning: acceleration, live physics, autonomous locomotion,
  scheduled release, terminal accounting, reusable inventory, visible state,
  rescue quota and real-time progression reuse cleanly. Physical device
  manipulation, collision routing, path projection and branchable rewind do not.

## Combination record

- Registered [`COMB-0030`](../../combinations/COMB-0030.md), an eleven-gene
  proper subset for reversible physical-device routing of a rescue troop.
- Generic visibility, fast-forward and the underlying live-time gene remain in
  the full genome but are not all required to identify the interaction; rewind
  and `TIM-007` remain central.
- No previous complete combination gains a second supporting game. Tin Hearts
  further confirms the shared six-gene Lemmings / HUMANITY rescue motif while
  adding the World of Goo physics / reusable-inventory motif.

## Taxonomy impact

- Registry changes: five stable genes added; nine existing genes reused.
- Taxonomy-change record: none. `ACT-044` captures the chosen input, while
  `TIM-007` captures the branchable temporal affordance; neither replaces
  `TIM-003` live progression.
- Candidate terms affected: live routing-device manipulation, simulation rewind,
  geometry-conditioned collision routing, prospective route projection and
  branchable reversible history are promoted.

## Negative results

- `ACT-036`, `SYS-046` and `CON-067` are absent because soldiers receive no
  selected consumable behavioural role.
- `ACT-042`, `SYS-055` and `CON-075` are absent because the player moves
  physical devices remotely rather than writing symbolic commands through a
  local avatar.
- `SYS-050` is absent because soldiers traverse ordinary surfaces and devices,
  not one connected live force-bearing structure.
- `INF-015` is absent because the preview shows a future route, not the exact
  structural links one held node would create.
- The working hypothesis that a closer Lemmings-like game might support
  `COMB-0025` is rejected; only its six-gene rescue motif recurs.
