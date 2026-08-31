---
game_id: GAME-0195
slug: beamng-drive
game_title: BeamNG.drive
analysis_status: reviewed
reviewed: 2026-08-29
combination_ids:
  - COMB-0193
gene_ids:
  action:
    - ACT-290
    - ACT-350
  system:
    - SYS-320
    - SYS-516
    - SYS-627
    - SYS-628
  constraint:
    - CON-438
  information:
    - INF-204
    - INF-205
    - INF-250
    - INF-251
  objective:
    - OBJ-118
  time:
    - TIM-003
---

# Game: BeamNG.drive

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodded Windows Steam Early Access client
  `v0.39.4`, public build `24617469`, checked 2026-08-29; one stock
  single-player `Time Trial` mission, **Road Master**, on East Coast USA in the
  supplied Cherrier Ardente 310M, with the mission's ordinary defaults and
  automatic gearbox mode. The reviewed official product title remains
  **BeamNG.drive**.
- Reproducible start packet: launch Road Master through the current Gameplay
  Selector rather than Free Roam, do not replace or configure its supplied
  vehicle, accept the mission start/countdown and begin at the first retained
  controllable state. Use the ordinary keyboard driving bindings; no traffic,
  AI rivals, custom parts, tuning, mods or player-created content is admitted.
- Primary decision loop: read speed, gear, elapsed time, the next coloured-post
  gate and vehicle shape/response; steer, accelerate, brake or use the declared
  recovery action; let node-beam chassis, suspension and pressure-tyre contact,
  traction, collision and permanent damage resolve; preserve a viable line
  through every checkpoint in order; then cross the final gate and retain the
  completed time in the mission result/high-score state.
- Entry and exit: begins after Road Master's countdown releases the supplied
  Ardente 310M. It succeeds only when every authored checkpoint has been
  triggered in order, the final gate accepts the finish and the mission end
  screen records the elapsed time. A missed gate cannot advance the route;
  voluntary restart, abort or an immobilised vehicle is non-completion and may
  lead to retry, not an evidence-backed separate classified-loss result.
- Included: the supplied Ardente 310M; steering, throttle, brake, reverse,
  handbrake and automatic transmission as declared input parameters; the
  authored rural East Coast USA point-to-point route; ordered gateways;
  mission countdown, current checkpoint, elapsed time, finish and retained
  high-score entry; road and terrain contact; pressure-tyre load, flex and
  sliding transition; node-beam chassis/suspension motion; permanent beam
  deformation or breakage; visible damage and resulting control change; one
  ordinary vehicle recovery request when needed; full mission restart as the
  clean retry boundary.
- Excluded: Free Roam, Career, campaigns and every other mission; Ardente
  Experience, Guttered, rally, chase, delivery, drag, drift, parking and AI
  races; traffic, police and multiplayer/BeamMP; vehicle/parts selector,
  custom configurations, tuning, paint and debug tools; other maps or cars;
  slow motion, node grabber, manual home positions, free camera teleport,
  replays, photo mode, World Editor and custom race paths; Repository mods,
  Workshop/user content, Automation imports; achievements, aggregate stats,
  repeated leaderboard optimisation and version history.
- Potential scoped modules: one scenario-like mission with a binary result;
  one AI Race; one Career contract; one Free Roam vehicle experiment; one rally
  stage; vehicle construction/debug tooling. Each needs its own current packet,
  causal loop and terminal rather than inheritance from Road Master.
- Direct-play status: no authenticated Windows Steam run was conducted. The
  current official patch notes name Road Master, its map, supplied Ardente 310M
  and Time Trial type; official mission/race-path, JBeam, tyre and input
  documentation establishes route, finish, recovery and physical transitions.
  Public-branch metadata pins only the build identifier. Repository transitions
  are evidence-based rules reasoning, not captured direct play.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BEAMNG-001` | v0.39.4 / public build 24617469 is the current reviewed Windows Steam client | Confirmed | Corroborated | High | P1, P2, S1 |
| `BEAMNG-002` | v0.39 adds stock Time Trial Road Master as a high-speed technical rural East Coast USA route in the Ardente 310M | Confirmed | Direct | High | P2 |
| `BEAMNG-003` | A Time Trial presents a predefined route through coloured-post gateways and records the finish time on that mission's high-score board | Confirmed | Direct | High | P3 |
| `BEAMNG-004` | Race pathnodes must trigger in order and the route declares start, recovery and final path positions | Confirmed | Direct | High | P4 |
| `BEAMNG-005` | The supplied vehicle is controlled continuously through steering, throttle, braking and the fixed automatic gearbox profile | Confirmed | Direct | High | P2, P5 |
| `BEAMNG-006` | Vehicle chassis, suspension, wheels and other components are represented through node-beam structures whose springs, damping, deformation and breakage change physical response | Confirmed | Direct | High | P6 |
| `BEAMNG-007` | Pressure tyres resolve load-sensitive static-to-sliding friction, tread deformation and sidewall flex against ground surfaces | Confirmed | Direct | High | P7, P8 |
| `BEAMNG-008` | Visible vehicle form and changed motion expose persistent beam deformation or broken connections after contact | Confirmed | Direct | High | P6, P9 |
| `BEAMNG-009` | Current bindings distinguish vehicle recovery from restarting the current mission or vehicle | Confirmed | Direct | High | P5 |
| `BEAMNG-010` | Road Master's positive terminal is ordered-course completion plus a retained timed evaluation; abort, restart or immobilisation is non-completion, not an asserted binary failure grade | Observation | Direct | High | P2–P5 |
| `BEAMNG-011` | Free Roam, Career, other missions, custom cars and user content are separable from the selected stock Time Trial | Confirmed | Direct | High | P2, P10 |
| `BEAMNG-012` | The repository trace reproduces the complete selected loop without generalising Road Master's evaluation to all BeamNG.drive modes | Observation | Direct | High | P1–P10, S1, V1 |

## Basic data

- Release / origin: developed and published by BeamNG; first released to Steam
  Early Access in 2015 and maintained through the official 2026 v0.39 line.
- Platform or physical form: single-player Windows Steam soft-body vehicle
  simulation; only one stock v0.39 Road Master Time Trial is asserted.
- Puzzle family: physics and object manipulation; real-time system pressure;
  route planning and optimisation.
- Primary and official sources:
  - **[P1]** [official v0.39.3/v0.39.4 release notes](https://www.beamng.com/game/news/patch/beamng-drive-v0-39-3/),
    dated 2026-08-07, for the latest public v0.39 hotfix boundary.
  - **[P2]** [official BeamNG.drive v0.39 release notes](https://www.beamng.com/game/news/patch/beamng-drive-v0-39/),
    for Road Master as a stock Time Trial, rural East Coast USA, the Ardente
    310M, current selector flow, gearbox-state handling and mission restart
    fixes.
  - **[P3]** [official predefined mission types](https://documentation.beamng.com/modding/gamemodes/missions/premadetypes/),
    for the Time Trial route, coloured-post checkpoints, final time and
    mission high-score entry.
  - **[P4]** [official Race/Path Editor documentation](https://documentation.beamng.com/world_editor/windows/race_path_editor/),
    for ordered pathnodes, start/recovery positions and the declared final
    point of a point-to-point route.
  - **[P5]** [official default keyboard bindings](https://documentation.beamng.com/modding/input/default-keyboard-bindings/),
    for steering, throttle, brake, gear, handbrake, recover and mission-restart
    actions in the current client.
  - **[P6]** [official Introduction to JBeam](https://documentation.beamng.com/modding/vehicle/intro_jbeam/),
    for soft-body nodes/beams, chassis/suspension/wheel structures, springs,
    damping, permanent deformation and breakage.
  - **[P7]** [official pressure-wheel documentation](https://documentation.beamng.com/modding/vehicle/sections/wheels/),
    for real-time node-beam tyres, tread and sidewall deformation, load and
    static/sliding ground friction.
  - **[P8]** [official node documentation](https://documentation.beamng.com/modding/vehicle/sections/nodes/),
    for collision and advanced tyre-friction parameters.
  - **[P9]** [official flexbody documentation](https://documentation.beamng.com/modding/vehicle/sections/flexbodies/),
    for mesh-to-node deformation and damage-material response.
  - **[P10]** [official product page](https://store.steampowered.com/app/284160/BeamNGdrive/),
    for the current product title, developer/publisher, Early Access status and
    separable product-level modes/features.
- Secondary build metadata:
  - **[S1]** [public Steam app-info metadata](https://api.steamcmd.net/v1/info/284160),
    for public build `24617469` and its 2026-08-07 publication timestamp only.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P10` and `S1`; rules reasoning, not a direct-play claim.
- Claim IDs: `BEAMNG-001`–`BEAMNG-012`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-290`: directly steer, accelerate, reverse, brake and use the
  declared handbrake of the mission-assigned Ardente 310M without an embodied
  enter/seat/exit loop.
- New `ACT-350`: request the current mission-authorised recovery of the assigned
  damaged, spun or stranded vehicle; clean full-mission restart remains the
  separate retry boundary rather than a route shortcut.
- Parameters: vehicle, steering, throttle, brake, reverse, handbrake, automatic
  gearbox, camera, input device, recovery command and retry choice.
- Claim IDs: `BEAMNG-005`, `BEAMNG-009`, `BEAMNG-010`.

### System Behaviour Genes

- Existing `SYS-320`: integrate the directly controlled car's acceleration,
  steering, terrain contact, collision and broad part-damage envelope.
- Existing `SYS-516`: accept only ordered course progress, measure elapsed time
  and settle the finish after the final valid gate.
- New `SYS-627`: resolve chassis, suspension and pressure tyres as coupled
  node-beam structures, converting contact forces into elastic response,
  load-sensitive traction, permanent deformation, beam breakage and changed
  vehicle authority.
- New `SYS-628`: retain a valid completed Time Trial elapsed result in Road
  Master's mission high-score state without treating an unfinished attempt as
  a classified result.
- Resolution order: accept direct input; resolve engine/drivetrain and tyre
  contact; integrate node-beam motion; resolve collision, deformation and
  breakage; update visible/control state; validate the next ordered gate; on
  recovery restore the permitted vehicle state without granting a gate; on the
  final valid gate settle elapsed time and retain its mission result.
- Parameters: node mass, beam spring/damping/deformation/strength, tyre load and
  friction curve, ground surface, collision impulse, vehicle state, checkpoint
  index, recovery state, elapsed time and retained result.
- Claim IDs: `BEAMNG-003`–`BEAMNG-010`.

### Constraint Genes

- Existing `CON-438`: the finish is valid only after the supplied car crosses
  every Road Master checkpoint in order before the final gate is accepted.
- Scarce strategic resources: tyre grip, braking distance, vehicle alignment,
  viable steering/suspension geometry, collision-free road space and elapsed
  time. Vehicle recovery can preserve attempt viability but cannot fabricate
  an omitted checkpoint or completed result.
- Claim IDs: `BEAMNG-003`, `BEAMNG-004`, `BEAMNG-010`.

### Information Genes

- Existing `INF-204`: the driving view exposes current speed, gear and authored
  route/gate cues needed for line and braking decisions.
- Existing `INF-205`: the mission HUD exposes elapsed time and current ordered
  course progress; no rival-position parameter exists in this solo Time Trial.
- New `INF-250`: world-visible deformation, detached/damaged parts, tyre state
  and changed steering/traction response expose the current distributed vehicle
  condition without reducing it to one abstract health bar.
- New `INF-251`: the end transition exposes the completed elapsed time and its
  retained Road Master high-score entry separately from live HUD progress.
- Claim IDs: `BEAMNG-003`, `BEAMNG-006`–`BEAMNG-010`.

### Objective Genes

- New `OBJ-118`: complete the supplied-car Road Master point-to-point course
  through all ordered checkpoints and retain one valid elapsed Time Trial
  result.
- Success, evaluation and failure: the positive evaluated terminal is a valid
  final gate followed by the saved time/result screen. A slower result remains
  a completion. A missed gate, restart, abort or immobilisation before that
  transition is non-completion and may be retried; the evidence does not support
  inventing a separate binary failure grade.
- Claim IDs: `BEAMNG-002`–`BEAMNG-004`, `BEAMNG-010`, `BEAMNG-012`.

### Time Genes

- Existing `TIM-003`: vehicle physics, tyre contact, deformation and the mission
  timer advance continuously while driving input remains available; pause and
  retry parameters do not convert the route into turns.
- Claim IDs: `BEAMNG-003`, `BEAMNG-005`–`BEAMNG-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Current v0.39.4 client is at the Gameplay Selector | Choose stock Road Master with no mods or vehicle substitution | East Coast USA loads the mission-supplied Ardente 310M and its authored route | exact versioned entry | `BEAMNG-001`, `BEAMNG-002` |
| Mission start screen is active | Accept start and countdown | Countdown releases the assigned vehicle at the authored start while elapsed timing begins under mission rules | retained first control | `BEAMNG-002`, `BEAMNG-003` |
| First coloured-post gateway is ahead | Steer, accelerate and brake toward it | Pressure tyres transfer load and force through the node-beam vehicle while speed, gear, time and route cues update | input, information and physics couple | `BEAMNG-005`–`BEAMNG-007` |
| Vehicle crosses the next gate in sequence | Give no additional command during crossing | That pathnode advances current course progress and exposes the following gate | route authority is ordered | `BEAMNG-003`, `BEAMNG-004` |
| Vehicle bypasses the current gate and reaches a later one | Cross the later gateway geometry | The later pathnode cannot become valid before its predecessor, so finish eligibility does not advance | shortcuts cannot fabricate completion | `BEAMNG-004`, `BEAMNG-010` |
| Car contacts a barrier or terrain edge | Continue or correct steering after impact | Nodes move, beams elastically respond or permanently deform/break, visible shape changes and the altered wheel/suspension state changes control | damage is physical state | `BEAMNG-006`–`BEAMNG-008` |
| Damaged or spun vehicle remains recoverable | Request ordinary Recover Vehicle | The authorised recovery returns a usable vehicle state under the mission/race-path recovery boundary but does not credit an omitted checkpoint | recovery preserves viability, not progress fraud | `BEAMNG-004`, `BEAMNG-009` |
| Attempt is no longer worth continuing | Restart the current mission | Transient attempt state returns to the authored start/countdown and no completed time is recorded | retry differs from positive terminal | `BEAMNG-009`, `BEAMNG-010` |
| Every preceding checkpoint is valid and the final gate is ahead | Cross the final gate | Ordered progress settles, elapsed time stops and the end transition records that time in Road Master's mission result/high-score state | bounded evaluated terminal | `BEAMNG-003`, `BEAMNG-004`, `BEAMNG-010` |

## Strategic and experiential structure

- Local decision: choose braking point, steering angle, throttle and recovery
  response from visible gate geometry, speed, tyre grip and accumulated damage.
- Medium-term planning: preserve the Ardente's alignment and functional tyre,
  suspension and body state across the technical rural route; decide whether a
  compromised line is faster to correct or safer to recover/restart.
- Long-term structure: link one continuous supplied-car attempt through every
  ordered gate into a retained elapsed result; subsequent optimisation is
  possible but outside the one-result terminal.
- Common heuristics: brake before weight transfer overwhelms available grip;
  turn smoothly through gateway centres; avoid cutting beyond the current gate;
  treat visible deformation and changed pull as functional information; recover
  only when continuing under current shape/contact is worse.
- Failure attribution: missed-gate state, route cues, speed/gear, elapsed time,
  visible deformation and control response separate route error, excess entry
  speed, lost traction, damaging contact and voluntary retry.
- Player-trust factors: ordered gates visibly declare progress; node-beam and
  tyre response makes consequences spatially legible; the final saved time is
  distinct from an arbitrary free-driving stop.
- Claim IDs: `BEAMNG-003`–`BEAMNG-012`.

## Replay and variation

- What changes between attempts: steering/braking trace, exact speed, contact,
  deformation, recovery use and elapsed result. Vehicle, route, gate order and
  positive terminal remain fixed.
- Randomness or procedural generation: the map, car and checkpoints are
  authored; small numerical/contact variation can change damage and time, but
  no procedural route or AI opponent is admitted.
- Multiple viable strategies: conservative no-contact completion, later
  braking, wider stable lines or selective recovery can reach the same valid
  result with different times and damage states.
- Typical replay motive: improve line, braking, damage avoidance and retained
  time. The canonical packet stops after the first valid result.
- Claim IDs: `BEAMNG-002`–`BEAMNG-010`.

## Adjacent systems and history

- Direct predecessors: BeamNG's earlier builds established node-beam vehicle
  physics and campaigns, but no prior patch supplies evidence for current
  Road Master availability or v0.39.4 selector behaviour.
- Variants: Free Roam has no required positive terminal; Career adds economy
  and progression; AI Race adds opponents/order; scenarios can add binary
  failure; rally can add pacenotes; mods and custom paths are user content.
- Similar games: Forza Horizon 6 shares dedicated car control, ordered gates,
  timed driving and race result; Euro Truck Simulator 2 shares road-vehicle
  handling and live terrain/traffic contact; War Thunder shares broad vehicle
  motion/damage but adds combat modules and team objectives.
- Important differences: Road Master removes campaign unlocks, rivals, traffic,
  cargo, fuel economy, combat and rewards. Its decision surface is one fixed
  timed route where continuously deformable structure and pressure-tyre contact
  can change the same car before the retained finish.
- Claim IDs: `BEAMNG-002`–`BEAMNG-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-290`, `ACT-350` | direct assigned-car input and mission-authorised recovery |
| System Behaviour | `SYS-320`, `SYS-516`, `SYS-627`, `SYS-628` | broad vehicle motion, ordered finish, node-beam/tyre resolution and retained time |
| Constraint | `CON-438` | authored checkpoint order and valid final gate |
| Information | `INF-204`, `INF-205`, `INF-250`, `INF-251` | driving cues, live progress, distributed damage and final result |
| Objective | `OBJ-118` | first valid retained Road Master time |
| Time | `TIM-003` | continuous driving physics and elapsed attempt time |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `194` (`GAME-0001`–`GAME-0194`).
- Exact genome matches: none.
- Tied near matches: `GAME-0171` — Forza Horizon 6 (`7 / 32 = 0.218750`).
- Supported combination subsets: `COMB-0193`.
- Scan date: 2026-08-29.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0171` — Forza Horizon 6 | `ACT-290`, `SYS-320`, `SYS-516`, `CON-438`, `INF-204`, `INF-205`, `TIM-003` | both directly drive an assigned car in live time through an authored ordered course with route, speed, gear and timed-progress feedback; Forza's scoped opening adds car selection, assists, Drivatars, traffic, Rewind, campaign unlocks, Festival Points and reward settlement under cosmetic damage, while Road Master fixes one supplied car and standalone route whose node-beam/pressure-tyre deformation changes control, permits mission recovery and retains only the elapsed result | Near, `0.218750` |

### Preserved research notes

- New genes: `ACT-350`, `SYS-627`, `SYS-628`, `INF-250`, `INF-251` and
  `OBJ-118`.
- Classification result: `New gene`, supported reuse and a new verified
  interaction combination.
- Evidence and reasoning: dedicated car control, generic occupied-vehicle
  motion/damage, ordered race validation, checkpoint order, driving/course HUD
  and real time reuse lower-ID boundaries. Mission-authorised vehicle recovery,
  decision-relevant node-beam/pressure-tyre coupling, retained standalone Time
  Trial result, distributed-damage feedback and the exact Road Master terminal
  do not.

## Combination status

- `COMB-0193` is a verified strict subset of this genome, coupling assigned-car
  control and recoverability to node-beam/tyre consequences, ordered route
  validation and one retained timed result.
- Every earlier verified combination is tested deterministically after
  registration; no earlier combination is assumed from product similarity.

## Taxonomy impact

- Registry changes: six new Active genes, `COMB-0193` and relevant existing
  family memberships.
- Taxonomy-change record: none; no prior lifecycle or reviewed-game signature
  changes. Reused definitions retain their existing boundaries.
- Candidate terms affected: recover vehicle, node-beam deformation, pressure
  tyre, distributed visible damage and retained Time Trial result.

## Negative results

- `ACT-044` is rejected: Recover Vehicle is mission-authorised repair/rewind or
  repositioning, not player-scrubbed branchable recent-state history.
- `ACT-201` and `CON-288` are rejected: Road Master's car is supplied directly
  and has no admitted on-foot seat/exit or fuel loop.
- `SYS-365` is rejected because traffic is excluded; `SYS-515` is rejected
  because Road Master has no Drivatar or other rival field.
- `INF-208` is rejected because its existing definition joins event performance
  to Festival progress/rewards, while this scope retains only a mission time.
- Road Master does not establish an evidence-backed binary loss grade. A
  restart, abort or immobilisation is recorded only as non-completion under the
  named selection amendment and ADR-007's completion/evaluation terminal test.
- Free Roam, Career, AI Race, rally, other missions, custom cars and mods are
  product inventory outside the causal packet.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Current v0.39 adds Road Master as a stock Ardente
  310M Time Trial through rural East Coast USA (`BEAMNG-002`).
- [Confirmed | Direct | High] Ordered gateways settle a saved timed result,
  while node-beam and pressure-tyre state changes the same car before that
  terminal (`BEAMNG-003`–`BEAMNG-008`).

## Нові гени

- [Observation | Direct | High] Six records isolate authorised vehicle
  recovery, distributed soft-body/tyre resolution, retained Time Trial result,
  physical damage feedback and the exact bounded objective.

## Нові комбінації

- [Observation | Direct | High] `COMB-0193` captures the fixed-car soft-body
  route from live control through ordered gates into one retained time.

## Зміни таксономії

- [Observation | Direct | High] Змін таксономії немає; жодна раніше reviewed
  signature не змінена.

## Нові питання

- Will an independently analysed fixed-route vehicle game reuse distributed
  structural-damage feedback, or is BeamNG's node-beam decision boundary unique?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0196` — Farming Simulator 25, the next
  authorised unit in `SEARCH_DEMAND_GAME_SELECTION_007`.
- Optimisation criterion: test machine/attachment, land-state, time and money
  recurrence inside one settled guided task or contract.
- Expected information gain: distinguish route-bound soft-body vehicle
  optimisation from productive vehicle/tool coupling and persistent field state.
