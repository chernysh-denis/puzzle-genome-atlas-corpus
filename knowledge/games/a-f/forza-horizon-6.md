---
game_id: GAME-0171
slug: forza-horizon-6
game_title: Forza Horizon 6
analysis_status: reviewed
reviewed: 2026-08-27
combination_ids:
  - COMB-0169
gene_ids:
  action:
    - ACT-044
    - ACT-227
    - ACT-290
    - ACT-291
    - ACT-292
    - ACT-293
  system:
    - SYS-320
    - SYS-365
    - SYS-515
    - SYS-516
    - SYS-517
    - SYS-518
    - SYS-519
  constraint:
    - CON-437
    - CON-438
    - CON-439
    - CON-440
    - CON-441
  information:
    - INF-125
    - INF-204
    - INF-205
    - INF-206
    - INF-207
    - INF-208
  objective:
    - OBJ-098
  time:
    - TIM-003
---

# Game: Forza Horizon 6

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: official PC Standard Edition with the Series 4 `Horizon
  Mascot Party` update available on `2026-08-27`; fresh Solo campaign save;
  assisted opening profile with Novice Drivatars, full driving line, assisted
  braking and steering, automatic transmission, traction and stability control,
  cosmetic damage, Rewind enabled, AutoDrive disabled and Offline Game Speed at
  `100%`.
- Primary decision loop: read the route, driving line, vehicle state, nearby
  rivals and event progress; steer, accelerate, brake, shift or rewind; let
  continuous car physics, surface contact, collisions and Drivatar motion
  resolve; complete the ordered course; retain its Festival Points and rewards;
  then choose the next available Qualifier until the Invitational opens.
- Entry and exit: begins on a clean save before the four-car prologue; continues
  through the tourist introduction, the 1989 Nissan Silvia K's starter choice,
  Tokyo City route test, Airfield Trail, Wind Farm Cross Country, Shirakawa
  Circuit and Hokubu Time Attack in that order; ends when the 2020 BMW M2
  Competition Horizon Invitational completes and the first Yellow Wristband
  plus its three reward cars are retained.
- Included: four authored prologue vehicle changes; direct road, snow, dirt,
  cross-country, circuit and Time Attack driving; character appearance only as
  a non-signature setup parameter; assist and difficulty configuration; starter
  selection and garage switching; open-world map, waypoint and ambient traffic;
  the borrowed Tokyo race; six exposed Qualifier choices but the fixed
  four-event trace above; car-class gating; Drivatar races; checkpoint/lap/time
  validation; Rewind; Festival Points; event settlement; Invitational and first
  Wristband unlocks.
- Excluded: Discover Japan Stamp pursuit beyond incidental opening records;
  Festival Playlist and Wheelspins after qualification; live Series 4 rewards;
  multiplayer, co-op, Convoys and Horizon Play; Race Customizer replays;
  AutoDrive; Car Meets, Touge, Street Races, Treasure Cars and Barn Finds;
  garages, Estate and EventLab/CoLab building; tuning, livery creation and
  commerce; later Wristbands, Legend Island and Gold status; Premium add-ons,
  Car Pass and future Drift Attack.
- Potential scoped modules: one Gold-Wristband campaign; Discover Japan Stamp
  progression; one Time Attack or Touge ruleset; Race Customizer/EventLab;
  Horizon Play multiplayer; Estate construction.
- Direct-play status: not conducted. The official starting guide and campaign
  pages define the bounded progression; official release/accessibility pages
  define the current platform and options; a recorded qualifier walkthrough
  reproduces the selected event order, and contemporary review footage
  corroborates checkpoint, Drivatar and Rewind behaviour.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `FH6-001` | PC Standard Edition released on 19 May 2026 and Series 4 was current on the review date | Confirmed | Direct | High | P1, P6 |
| `FH6-002` | A clean campaign starts as a tourist with a four-car prologue, character setup, three owned starter cars and one active choice | Confirmed | Direct | High | P2 |
| `FH6-003` | The Tokyo introduction uses a borrowed Silvia, then exposes the world map, six Qualifier events and a visible Festival Point meter | Confirmed | Direct | High | P2 |
| `FH6-004` | The fixed trace completes four available events before the first Horizon Invitational | Observation | Corroborated | High | P2, S2 |
| `FH6-005` | Festival events use curated car themes/classes and opening events are C-class until the first Wristband | Confirmed | Direct | High | P2, P3, P4 |
| `FH6-006` | Solo races combine direct car control, live vehicle physics, course progress and difficulty-scaled Drivatar opponents | Observation | Corroborated | High | P3, P5, S1 |
| `FH6-007` | Ordered course gates, laps or timed targets determine a valid event result; Rewind can restore recent active-race state | Observation | Corroborated | High | P3, S1, S2 |
| `FH6-008` | Eligible event completion adds Festival Points until the Invitational becomes available | Confirmed | Direct | High | P2, P3, P4 |
| `FH6-009` | Completing the Invitational, not merely crossing the point threshold, grants the first Wristband and three cars | Confirmed | Direct | High | P2, P4 |
| `FH6-010` | Difficulty, driving assists, Offline Game Speed, navigation waypoint and Proximity Radar are configurable | Confirmed | Direct | High | P2, P5 |
| `FH6-011` | Later campaign, Discover Japan, live, multiplayer and building systems are separable from the first-Wristband route | Confirmed | Direct | High | P1, P3, P4, P6 |

## Basic data

- Release / origin: `2026`, Playground Games / Xbox Game Studios, Japan-set
  open-world driving campaign.
- Platform or physical form: Windows PC Standard Edition via Xbox app or Steam;
  Xbox Series X|S and cloud versions exist but are not the asserted platform.
- Puzzle family: real-time vehicle control, course optimisation, adversarial
  race routing and threshold-gated campaign progression.
- Primary sources:
  - `P1` — [official Xbox Store page](https://www.xbox.com/en-US/games/store/forza-horizon-6/9nr1r1xwlcnb),
    for release platform, Standard Edition and tourist-to-Festival campaign.
  - `P2` — [official First Drive starting guide](https://forza.net/news/forza-horizon-6-first-drive),
    for the prologue cars, starter choice, Tokyo race, six Qualifiers, visible
    point meter, Invitational, first Wristband and reward cars.
  - `P3` — [official campaign deep dive](https://forza.net/news/forza-horizon-6-campaign),
    for curated car themes/classes, Drivatars, event configuration, Festival
    Points and Wristband gates.
  - `P4` — [official progression guide](https://forza.net/news/forza-horizon-6-progression),
    for Wristband, Stamp and Horizon Play separation and first-Wristband rules.
  - `P5` — [official accessibility and controls feature](https://forza.net/news/forza-horizon-6-radio),
    for difficulty, driving assists, Offline Game Speed, waypoint AutoDrive and
    Proximity Radar; AutoDrive remains disabled in this scope.
  - `P6` — [official Series 4 update](https://forza.net/news/forza-horizon-6-series-4),
    for the current `2026-08-27` content state and separation of live content.
- Secondary sources:
  - `S1` — [GameSpot review](https://www.gamespot.com/reviews/forza-horizon-6-review-dopamine-highway/1900-6418489/),
    for direct PC driving, route checkpoints, rewind and varied race surfaces.
  - `S2` — [recorded complete Horizon Qualifiers trace](https://www.youtube.com/watch?v=mSmR-ixKEog),
    for Airfield Trail, Wind Farm Cross Country, Shirakawa Circuit, Hokubu Time
    Attack and the following Invitational in one reproducible sequence.
- Claim IDs: `FH6-001`–`FH6-011`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-044`, restore a recent active driving state and resume a
  revised line; `ACT-227`, set a personal destination so GPS guidance appears.
- New genes: `ACT-290`, directly steer the currently assigned car; `ACT-291`,
  select an eligible owned car; `ACT-292`, configure assists and Drivatar
  difficulty; `ACT-293`, commit one unlocked mapped driving event.
- Parameters: input device, starter, active vehicle, assists, difficulty,
  waypoint, selected event and Rewind horizon.
- Claim IDs: `FH6-002`, `FH6-003`, `FH6-006`, `FH6-007`, `FH6-010`.

### System Behaviour Genes

- Existing genes: `SYS-320`, integrate occupied vehicle motion, collision and
  cosmetic damage under the scoped profile; `SYS-365`, route ambient road
  traffic through the live world between events.
- New genes: `SYS-515`, run the difficulty-scaled Drivatar field; `SYS-516`,
  validate checkpoints/laps/time and finish result; `SYS-517`, convert eligible
  event results into Festival Points; `SYS-518`, retain ordered tourist,
  Qualifier, Invitational and first-Wristband unlocks; `SYS-519`, settle event
  results into persistent rewards and garage state.
- Resolution order: accept car and event; instantiate route and eligible field;
  integrate direct inputs, assists, car physics and rival motion; accept ordered
  progress; classify finish; add points and rewards; test the next gate; retain
  unlock state.
- Parameters: vehicle performance, surface, field size, difficulty, checkpoints,
  laps, time, finish order, event points and rewards.
- Claim IDs: `FH6-003`–`FH6-010`.

### Constraint Genes

- New genes: `CON-437`, car theme/class gates Festival entry; `CON-438`, ordered
  checkpoint/lap completion gates a valid finish; `CON-439`, campaign state
  gates event availability; `CON-440`, Qualifier points gate the Invitational;
  `CON-441`, Invitational completion gates the first Wristband.
- Scarce strategic resources: course time and speed retained through each turn;
  track position relative to rivals; remaining route correction before a
  checkpoint; event progress toward the Invitational threshold.
- Claim IDs: `FH6-003`–`FH6-009`.

### Information Genes

- Existing gene: `INF-125`, expose the explored map, opening markers and
  authored campaign gates before route choice.
- New genes: `INF-204`, driving HUD speed/gear/route guidance; `INF-205`, race
  position, course progress and rival proximity; `INF-206`, map/event terms;
  `INF-207`, Festival Point threshold and invitation state; `INF-208`, final
  performance and retained reward settlement.
- Claim IDs: `FH6-003`, `FH6-005`–`FH6-010`.

### Objective Genes

- New gene: `OBJ-098`, qualify for the Horizon Festival and earn the first
  Wristband through the fixed four-event route and Horizon Invitational.
- Success, evaluation and failure: success is the retained first Wristband and
  its three cars; a missed checkpoint or incomplete course prevents a valid
  event result; Rewind can revise recent local failure, while abandoning an
  event leaves its first-completion progress unsettled.
- Claim IDs: `FH6-004`, `FH6-007`–`FH6-009`.

### Time Genes

- Existing gene: `TIM-003`, vehicle, opponent, traffic, physics and event clocks
  advance in real time while driving inputs are accepted; pause and Rewind are
  bounded control parameters rather than a discrete-turn model.
- Claim IDs: `FH6-006`, `FH6-007`, `FH6-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Clean campaign has not begun | Complete the four assigned prologue drives | Each authored vehicle and region segment advances to character and tourist setup | fixed prologue vehicle sequence | `FH6-002` |
| Mei offers three starter cars | Select the 1989 Nissan Silvia K's | All three cars enter the garage and the Silvia becomes active | owned collection versus active vehicle | `FH6-002` |
| Tokyo follow route reaches the test event | Enter and complete the borrowed-Silvia race | The first race settles; multiplayer and then the Qualifier map become available | authored onboarding unlock | `FH6-003` |
| Six Qualifier markers and a point meter are visible | Set a waypoint and enter Airfield Trail | Its car restriction and course instantiate; a valid result adds retained progress | mapped event contract | `FH6-003`, `FH6-005`, `FH6-008` |
| Vehicle approaches the next gate off line | Brake, steer or rewind to an earlier approach | Physics and opponent motion resume from the retained state; only a valid gate crossing advances course progress | reversible live route correction | `FH6-006`, `FH6-007` |
| Fixed Trail, Cross Country, Circuit and Time Attack results are retained | Cross the required Festival Point threshold | Horizon Invitational changes from locked to available | alternative progress to mandatory event | `FH6-004`, `FH6-008` |
| First Invitational is available | Enter the BMW M2 Competition event and complete its course | Result settles, first Yellow Wristband and three reward cars are retained, and Festival features open | terminal qualification gate | `FH6-009` |

## Strategic and experiential structure

- Local decision: choose braking point, turn-in, throttle and recovery while
  reading guidance, surface, checkpoint width and nearby rivals.
- Medium-term planning: preserve speed through a checkpoint sequence, decide
  when a mistake merits Rewind and select the next Qualifier that contributes
  to the point threshold.
- Long-term structure: convert several independently selectable event results
  into one mandatory Invitational and first-Wristband state transition.
- Common heuristics: brake before the sharpest steering input; prioritise valid
  gate passage over a shorter invalid line; use Rewind after a costly miss;
  avoid excess contact that loses exit speed; complete high-value events until
  the Invitational opens.
- Failure attribution: line choice and input timing are direct, while collision
  with Drivatars and assist behaviour make some lost position jointly caused.
- Player-trust factors: explicit driving line, checkpoint gates, position/time,
  proximity cues, point meter and result panel expose why progress did or did
  not settle.
- Claim IDs: `FH6-005`–`FH6-010`.

## Replay and variation

- What changes between sessions: starter/active car, assist profile, Drivatar
  difficulty, Qualifier choice/order, racing line, contacts, Rewind decisions
  and final performance.
- Randomness or procedural generation: ambient traffic and local opponent
  interactions vary; the scoped event routes and campaign gates are authored.
- Multiple viable strategies: conservative assisted lines, later braking,
  contact avoidance or selective Rewind can all produce valid event finishes.
- Typical replay motive: improve position/time, increase difficulty, reduce
  assists or revisit a completed event through Race Customizer, which is outside
  the first-play signature.
- Claim IDs: `FH6-006`, `FH6-007`, `FH6-010`.

## Adjacent systems and history

- Direct predecessors: earlier Forza Horizon games supply the open-world
  festival lineage, but their campaign progression is not imported as evidence.
- Variants: later Wristband bands, Discover Japan, Horizon Play and custom
  events are possible future bounded scopes.
- Similar games: Euro Truck Simulator 2 shares direct vehicle physics, ambient
  traffic, personal waypoint routing and live time; Grand Theft Auto V shares
  those systems plus a mission map; EA SPORTS FC 26 provides a contrasting live
  human-versus-AI spatial contest and regulation result.
- Important differences: the scoped Forza route has no employer cargo, road-law
  or fatigue simulation, no on-foot combat or wanted state and no team ball
  possession; it centres race-course validity, rivals, reversible line choice
  and points-gated Festival entry.
- Claim IDs: `FH6-005`–`FH6-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-044`, `ACT-227`, `ACT-290`–`ACT-293` | starter, active car, assists, event order, Rewind horizon |
| System Behaviour | `SYS-320`, `SYS-365`, `SYS-515`–`SYS-519` | vehicle model, surface, Drivatar field, finish, points, reward |
| Constraint | `CON-437`–`CON-441` | car class, course sequence, unlock, point and Invitational gates |
| Information | `INF-125`, `INF-204`–`INF-208` | map, route, HUD, proximity, Festival meter and results |
| Objective | `OBJ-098` | first Yellow Wristband and three reward cars |
| Time | `TIM-003` | real-time driving, pause and Rewind parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `170` (`GAME-0001`–`GAME-0170`).
- Exact genome matches: none.
- Tied near matches: `GAME-0169` — Euro Truck Simulator 2 (`4 / 48 = 0.083333`).
- Supported combination subsets: `COMB-0169`.
- Scan date: 2026-08-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Euro Truck Simulator 2 (`GAME-0169`) | `ACT-227`, `SYS-320`, `SYS-365`, `TIM-003` | Both directly resolve a waypoint-guided road vehicle amid ambient traffic in live time. Forza replaces employer cargo, law, fatigue, deadline, articulated trailer and delivery pay with dedicated race input, Drivatar fields, ordered course validation, Rewind and Festival points that gate an Invitational. | Near, `0.083333` |

## Taxonomy impact

- Registry changes: twenty Active definitions and links in the six canonical
  registries.
- Taxonomy-change record: none; no prior boundary or signature changes.
- Candidate terms affected: dedicated driving control, race event, Drivatar
  field, race progress, Festival Points, Wristband gate and race-result HUD.

## Negative results

- `ACT-201` is rejected because the scoped car is assigned directly and exposes
  no embodied enter/seat/exit loop.
- `CON-288` is rejected because fuel, seat access and unsafe moving exit do not
  gate the assigned racing car.
- `INF-199` is rejected because the race HUD has no truck/cargo damage, Rest
  State or Mandatory Break clock.
- Festival Playlist, Wheelspins and Discover Japan are excluded even though the
  first Wristband unlocks them; availability after the exit is not causal to
  the completed route.
- AutoDrive is excluded by the fixed profile, so direct waypoint routing remains
  informational rather than autonomous travel.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] A fresh tourist completes a prologue, four fixed
  Qualifiers and the Horizon Invitational before the first Wristband
  (`FH6-002`–`FH6-009`).
- [Confirmed | Direct | High] Car-class, Festival Point and Invitational gates
  keep campaign access separate from open-world freedom (`FH6-005`, `FH6-008`,
  `FH6-009`).

## Нові гени

- [Observation | Corroborated | High] Twenty genes isolate dedicated race
  control, rival/course resolution, event gates, Festival progress and the
  first-Wristband terminal.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0169` captures reversible
  course-valid race control feeding a points-gated Invitational.

## Зміни таксономії

- [Observation | Direct | High] Змін таксономії немає; додано лише нові
  boundaries without revising prior signatures.

## Нові питання

- Which independently analysed racing game will falsify or reuse the new
  dedicated race-course, rival-field and event-progression boundaries?

## Наступна рекомендована гра

- [Confirmed | Direct | High] Нової гри не вибрано: `GAME-0171` завершує
  дозволений дев'ятиігровий Goal `GAME-0163`–`GAME-0171`.
- Optimisation criterion: stop at the authorised boundary and review the active
  singleton-share and latest-nine new-gene advisories before any new horizon.
- Expected information gain: a separately authorised batch-boundary taxonomy
  review can test the twenty new race boundaries without silently selecting a
  tenth game.
- Backlog impact: no new game is reserved.

## Чому саме вона

- [Confirmed | Direct | High] The demand-led queue is exhausted; selecting
  another title would exceed the active Goal and bypass its stop boundary.

## Next research step

- Await explicit maintainer authorisation for a batch-boundary taxonomy-health
  review or another recorded game horizon. Do not start either implicitly.

## Design lessons

- Open-world freedom and a structured campaign can coexist when event entry,
  class and point gates are represented separately from direct travel.
- Rewind changes a racing line from irreversible execution into a local
  branchable simulation without removing real-time vehicle pressure.
- A point threshold and its mandatory terminal event are distinct mechanics;
  reaching the threshold does not itself grant the Wristband.

## Changelog

- 2026-08-27 — Added the reviewed PC Series 4 fresh-save Solo opening through
  the first Yellow Wristband, with twenty new genes and `COMB-0169`.
