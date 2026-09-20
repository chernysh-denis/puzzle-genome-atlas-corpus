---
game_id: GAME-0319
slug: sea-of-thieves
game_title: Sea of Thieves
analysis_status: reviewed
reviewed: 2026-09-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-219
    - ACT-341
    - ACT-474
    - ACT-475
  system:
    - SYS-215
    - SYS-578
    - SYS-918
    - SYS-919
    - SYS-920
  constraint:
    - CON-648
  information:
    - INF-115
    - INF-119
    - INF-351
  objective:
    - OBJ-186
  time:
    - TIM-003
---

# Game: Sea of Thieves

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). The Sloop, Sailor's
Chest, selected island, Outpost and exact wind are carrier parameters rather
than separate genes.

## Analysis scope

- Version / ruleset: current English Xbox Series X|S Standard Edition,
  server version `3.9.0`, Season 21, checked 2026-09-20. The packet covers a
  fresh solo closed-crew Sloop on High Seas and the replayable Gold Hoarders
  Tutorial Voyage `An Introduction to the Gold Hoarders`. Season 21's live
  experiment removes `Dive To` from Voyages, so the complete route is sailed.
- Structured analysis target: Xbox Series X|S Standard Edition; see
  `GAME-0319` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Primary decision loop: inspect the pictorial treasure map and ship chart;
  operate the capstan, sail and wheel from their separate deck stations to
  cross the shared world; compare island silhouette and landmarks, disembark
  and dig at a chosen point; carry the exposed Sailor's Chest back aboard;
  sail to an Outpost while watching the horizon; then carry and sell the chest
  to a Gold Hoarders representative.
- Entry: ordinary control aboard a fresh solo Sloop after the Quest Table has
  accepted `An Introduction to the Gold Hoarders` and supplied its single
  X-marks-the-spot map, before the anchor, sail or wheel is operated for this
  voyage.
- Positive terminal: the scoped Sailor's Chest is handed to a Gold Hoarders
  representative, the sale rewards settle and the tutorial voyage records
  completion while ordinary Outpost control remains available.
- Negative terminal: the only scoped chest becomes unrecoverable for this
  crew—most importantly when another High Seas crew takes and sells it—or the
  session is abandoned before hand-in. Pirate death alone is not terminal:
  the Ferry of the Damned returns the pirate while the voyage can still be
  completed. A sunk ship alone is not terminal if the chest remains recoverable.
- Included: direct pirate movement; Quest Table start; one X-map/chart
  correlation; capstan, sail length/angle and wheel operation; wind-driven
  Sloop travel; compass and horizon reading; one shovel search; incremental
  chest exposure; direct carry/drop; the carried-object sprint/hand restriction;
  shared-world visibility and possible hostile interference; pirate health,
  lethal transition and return; return sailing; Gold Hoarders sale, gold and
  reputation settlement; tutorial completion.
- Excluded: the Maiden Voyage; Safer Seas and Custom Seas; open crews and
  additional crew members; `Dive To`; every non-tutorial Voyage; riddles,
  vaults, raids, Tall Tales, Emissaries, Captained ships and Guilds; deliberate
  combat, cannons, repairs, cooking, fishing, trading and ship cosmetics;
  unrelated emergent events; optimisation of gold or reputation; later
  promotions; PlayStation, Windows and Xbox One rules; Premium Edition content.
  Other crews remain an environmental risk because High Seas cannot promise
  their absence, but seeking or winning combat is not part of the positive route.
- Reproducible parameterisation: create a closed solo Sloop High Seas session;
  select the Gold Hoarders Tutorial Voyage at its Quest Table; use `Sail To`;
  identify the depicted small island on the chart and mark it; manually raise
  anchor, set sail and steer there; use the map and island landmarks to dig up
  the single Sailor's Chest; carry it aboard; chart and sail to any Outpost;
  carry the same chest to its Gold Hoarders tent and hand it in. Stop at the
  first post-sale tutorial-complete state. Island, Outpost, weather, route,
  interference, damage and elapsed time remain bounded run parameters.
- Potential scoped modules: one ordinary post-tutorial buried-treasure Voyage,
  Safer Seas, multi-crew sailing, naval combat, ship loss/recovery and one
  complete live-world session each require their own boundary and evidence.
- Direct-play status: not conducted. No Xbox Series console, installed current
  client, account session, input trace, save, screenshot, video or audio was
  opened or analysed. Official product, Pirate Academy, accessibility and live
  release-note pages establish the current identity and invariant rules; the
  community-maintained voyage record supplies the exact tutorial prompts and
  route. This is a source-bounded reconstruction, not a claimed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SOT-001` | The scoped product is the current Xbox Series X and Series S Standard Edition running live version 3.9.0 / Season 21 | Confirmed | Direct | High | P1, P2 |
| `SOT-002` | Season 21 removes `Dive To` from Voyages, so the selected tutorial route must be sailed | Confirmed | Direct | High | P2 |
| `SOT-003` | The Quest Table supplies a replayable Gold Hoarders Tutorial Voyage whose completion is accepted when its chest is handed in | Confirmed | Corroborated | High | P2, P3, S1 |
| `SOT-004` | The tutorial gives one X-map, asks the player to match its island against the ship chart, sail there, dig and return the chest to an Outpost | Observation | Corroborated | High | P3, P4, S1 |
| `SOT-005` | A solo Sloop is steered by moving among separate anchor, sail and wheel controls whose current settings jointly determine travel | Observation | Corroborated | High | P1, P5, S1, S2 |
| `SOT-006` | A valid shovel search at the marked location exposes a buried chest through repeated digging, after which it becomes carryable | Observation | Corroborated | High | P4, S1 |
| `SOT-007` | Carrying treasure occupies the pirate's hands, blocks sprint and leaves the dropped object available in the world | Confirmed | Direct | High | P5 |
| `SOT-008` | High Seas is a live shared world where another crew can see, take and hand in unprotected treasure | Observation | Corroborated | High | P1, P5, S1 |
| `SOT-009` | Damage depletes visible health; lethal damage sends the pirate through the Ferry of the Damned and back rather than itself failing the voyage | Confirmed | Direct | High | P6 |
| `SOT-010` | Handing the tutorial chest to Gold Hoarders settles gold, reputation and the voyage-complete state | Observation | Corroborated | High | P2, P4, S1 |
| `SOT-011` | The bounded identity joins embodied multi-station sailing, map-to-chart inference and exposed shared-world treasure custody in one return-and-sale circuit | Strong Pattern | Corroborated | High | `SOT-002`–`SOT-010` |

## Basic data

- Release / origin: Rare develops the live shared-world adventure and Xbox Game
  Studios publishes it. The Xbox product page lists Xbox Series X|S and solo
  play, while the live site identifies release 3.9.0 on 2026-09-17.
- Platform or physical form: digital Xbox Series X|S Standard Edition, current
  Season 21 High Seas service, English interface, solo closed crew.
- Puzzle family: spatial reasoning and navigation; physics and object
  manipulation; information and deduction; real-time system pressure.
- Primary and official sources, accessed 2026-09-20:
  - **[P1]** [official Xbox product page](https://www.xbox.com/en-US/games/sea-of-thieves),
    for publisher/developer identity, Xbox Series X|S support, solo play and
    the shared-world sailing/treasure-hunting premise.
  - **[P2]** [official release notes
    3.9.0](https://www.seaofthieves.com/de/release-notes/3.9.0), for current
    Season 21 version, removal of `Dive To` for Voyages and the current fix that
    completes the Gold Hoarders Tutorial Voyage on chest hand-in regardless of
    which crew member began it.
  - **[P3]** [official release notes
    2.10.0](https://www.seaofthieves.com/release-notes/2.10.0), for the ship's
    Quest Table, redesigned Voyage access, tutorial-voyage introduction and the
    distinction between voyage completion and maximum-profit treasure hand-in.
  - **[P4]** [official Gold Hoarders Pirate Academy
    guide](https://www.seaofthieves.com/Pirate-Academy/guide/the-gold-hoarders),
    for matching an X-map to an island, digging at the X and returning sealed
    chests to Gold Hoarders.
  - **[P5]** [official Getting Around Pirate Academy
    guide](https://www.seaofthieves.com/Pirate-Academy/guide/getting-around),
    for direct movement, equipment/map access, compass and shovel, treasure
    carry/drop, loss of sprint and world-object custody.
  - **[P6]** [official Life and Death Pirate Academy
    guide](https://www.seaofthieves.com/Pirate-Academy/guide/life-and-death),
    for health, food recovery, lethal transition, Ferry of the Damned and return.
  - **[P7]** [official accessibility
    page](https://www.seaofthieves.com/accessibility), for the shared online
    world and the separately adjusted sails, anchor, wheel and cannon stations.
- Corroborating textual sources, accessed 2026-09-20:
  - **[S1]** [Sea of Thieves Wiki tutorial-voyage
    record](https://seaofthieves.wiki.gg/wiki/An_Introduction_to_the_Gold_Hoarders),
    for the exact title, Quest Table route, one X-map, island/chart prompts,
    anchor/sail/wheel sequence, repeated digging, Sailor's Chest, Outpost return,
    hand-in terminal and warnings about other crews.
  - **[S2]** [official-site community sailing
    guide](https://www.seaofthieves.com/community/forums/topic/28386/sea-of-thieves-tutorial),
    for Sloop station placement and the anchor–wheel–sail navigation sequence.
    It is a user-authored corroborating guide, not publisher-authored rules.
- Research record: **[R1]** local preflight on 2026-09-20 found no installed
  current client, console session, account capture or input trace. No
  audiovisual evidence was used.
- Claim IDs: `SOT-001`–`SOT-011`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly walk, sprint, jump and swim the pirate between
  ship stations, island landmarks, chest and Outpost receiver.
- Existing `ACT-341`: activate the Quest Table and other reachable stateful
  fixtures whose legal interaction advances voyage state.
- New `ACT-474`: physically reach and operate one Sloop station—capstan, sail
  length/angle rope or wheel—changing only that station's current setting.
- New `ACT-475`: commit a shovel strike at one chosen reachable terrain point
  while searching for the map's buried target.
- Existing `ACT-048`: lift the exposed Sailor's Chest, carry it at a controlled
  offset and put it down in the ship or world.
- Existing `ACT-219`: irreversibly hand the carried chest to a Gold Hoarders
  representative for its disclosed reward and completion settlement.
- Controller bindings, exact station positions, island, chest and buyer remain
  parameters. Claims: `SOT-003`–`SOT-007`, `SOT-010`.

### System Behaviour Genes

- New `SYS-918`: continuously integrate wheel deflection, sail length/angle,
  anchor state, wind and water into the Sloop's heading and speed while no
  single remote travel command owns the route.
- New `SYS-919`: accept shovel strikes only within the buried target's bounded
  terrain region and progressively expose the chest until it becomes a free
  carryable object.
- New `SYS-920`: retain treasure as a free shared-world object whose current
  physical holder or placement, not original finder identity, determines who
  can move and hand it in.
- Existing `SYS-578`: damage reduces current pirate health, compatible food can
  restore it, and zero health enters the lethal transition.
- Existing `SYS-215`: optional hostile interference, attacks, contact and
  damage resolve in real time without pausing sailing or world authority.
- Resolution order: station input changes one control; the live simulation
  updates vessel motion; map and local landmarks guide a player-selected dig;
  accepted strikes expose the chest; carry/drop changes its world custody;
  shared-world actions and damage may intervene; Gold Hoarders hand-in converts
  the still-recoverable chest into reward and voyage completion. Claims:
  `SOT-005`–`SOT-010`.

### Constraint Genes

- New `CON-648`: while a bulky treasure object is held, the pirate cannot
  sprint or use ordinary two-handed equipment and must drop or hand off that
  treasure before unrestricted action returns.
- The chosen Voyage, one chest, terrain tolerance, station reach, wind,
  Outpost and other-crew presence are parameters rather than separate genes.
  Claim: `SOT-007`.

### Information Genes

- New `INF-351`: the held X-map reveals an unlabeled island silhouette,
  landmarks and one marked dig point while the ship chart exposes named island
  geometry, the current vessel position and player marks; neither surface
  automatically identifies the correspondence or plots the sailing solution.
- Existing `INF-115`: horizon sight, silhouettes, spatial sound and local
  effects expose only currently perceivable other crews and threats.
- Existing `INF-119`: the HUD exposes current health and compatible damage/
  recovery feedback before the next survival decision.
- Exact future weather, other-crew intent and hidden buried position remain
  undisclosed. Claims: `SOT-004`, `SOT-008`, `SOT-009`.

### Objective Genes

- New `OBJ-186`: begin the named tutorial Voyage, recover its single mapped
  chest, return through the shared world and hand that same recoverable object
  to Gold Hoarders so reward and tutorial completion settle.
- Digging alone does not complete this tutorial; death alone does not fail it;
  losing the only chest beyond recovery or abandoning the session prevents the
  scoped terminal. Claims: `SOT-003`, `SOT-004`, `SOT-008`–`SOT-010`.

### Time Genes

- Existing `TIM-003`: ship motion, wind, waves, sight, hostile interference,
  damage and custody remain live while the player moves among stations, studies
  maps, digs and carries treasure. Claim: `SOT-005`–`SOT-009`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| The tutorial Voyage is available at the Sloop's Quest Table | Select and begin it | one X-marks-the-spot map enters the crew's voyage state and the tutorial route becomes active | named bounded packet, not an arbitrary chest | `SOT-003`, `SOT-004` |
| The anchor is down and sail is raised | Operate capstan, sail and wheel from their separate positions | each station retains its setting; their current values and wind continuously update vessel travel | embodied multi-station sailing | `SOT-005` |
| The X-map is held | Compare its coastline and landmarks with the ship chart | a player-inferred island may be marked, but no automatic route or correctness proof is supplied | cross-surface spatial inference | `SOT-004` |
| The Sloop is moving | Leave the wheel to trim sail or inspect the chart | the prior wheel/sail settings remain active and the ship continues under live wind and water | unattended station state still matters | `SOT-005` |
| The pirate stands near the inferred X | Dig at a chosen terrain point | a miss changes no treasure state; accepted strikes progressively expose the hidden chest | location-tolerant buried-object search | `SOT-006` |
| The chest is exposed | Pick it up and move | it follows the pirate as a held world object; sprint and ordinary two-handed use are unavailable until release | embodied treasure burden | `SOT-007` |
| The chest is dropped aboard or ashore | Move away or another pirate reaches it | it remains a free world object and any eligible pirate may take it | possession without finder lock | `SOT-008` |
| Health reaches zero while the chest remains recoverable | Accept lethal resolution | the pirate goes through the Ferry and can return; chest and voyage remain governed by the shared world | death is interruption, not objective failure | `SOT-009` |
| The same chest is carried to Gold Hoarders | Commit the sale | chest custody ends, gold/reputation settle and version 3.9.0 records the tutorial complete | positive terminal | `SOT-003`, `SOT-010` |
| Another crew takes and sells the only chest first | Attempt to continue the route | the scoped crew no longer has a recoverable accepted object and cannot reach the declared hand-in terminal | shared-world negative terminal | `SOT-008`, `SOT-010` |

## Strategic and experiential structure

- Local decision: leave one retained ship control to reach another, correct
  heading/sail against wind, compare map geometry, choose a dig point, or set
  down the chest to regain unrestricted movement.
- Medium horizon: keep the Sloop on course while periodically checking the
  chart and horizon, then choose an Outpost route that limits custody exposure.
- Long horizon: preserve one physical treasure through the complete
  quest–sail–infer–dig–return–sale circuit rather than stopping at discovery.
- Reversibility: wheel and sail settings can be corrected; wrong dig points can
  be retried. Lost time, damage and another crew's successful sale cannot be
  rewound inside the session.
- Failure attribution: station positions and motion show navigation error;
  shovel feedback distinguishes wrong ground from accepted excavation; health
  and local perception expose immediate danger; custody and the final hand-in
  distinguish found treasure from completed Voyage.
- Player trust: the tutorial supplies one stable map/object/receiver chain,
  while route, wind and other crews remain deliberately uncertain.

## Replay and variation

- Selected small island, nearby Outpost, weather, wind, live-world population
  and interference may change between starts; no complete procedural-world
  generation claim is made.
- The player can choose route, station timing, dig approach and where to place
  the chest, but the tutorial's map–chest–Gold Hoarders dependency is fixed.
- Replay may improve sailing or custody discipline; reputation optimisation and
  non-tutorial treasure loops are outside this packet.

## Adjacent systems and history

- *DREDGE* shares direct boat travel, a return-to-market circuit and a sale,
  but its first-day catch occupies a bounded cargo grid and must finish before
  night. Sea of Thieves uses physically separated Sloop controls, an inferred
  X-map destination and a stealable world object with no scoped day deadline.
- *DEATH STRANDING DIRECTOR'S CUT* shares carried-object burden and route
  reading, but it arranges a multi-package body load and links topographic
  markers. This packet carries one free rigid chest and compares two distinct
  map surfaces before sailing manually.
- *Rust* shares a live hostile world and recoverable physical resources, but
  its scoped identity centres persistent server absence and wipe authority.
  The tutorial Voyage is one online session circuit with an explicit buyer.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-048`, `ACT-219`, `ACT-341`, `ACT-474`, `ACT-475` | bindings, stations, shovel, chest and buyer are parameters |
| System Behaviour | `SYS-215`, `SYS-578`, `SYS-918`–`SYS-920` | wind, waves, damage, buried tolerance and crew identity are parameters |
| Constraint | `CON-648` | held object, sprint and compatible equipment are parameters |
| Information | `INF-115`, `INF-119`, `INF-351` | map art, chart scale, horizon and HUD layout are parameters |
| Objective | `OBJ-186` | voyage, chest, Outpost and reward are parameters |
| Time | `TIM-003` | server cadence and pause behaviour are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `318` (`GAME-0001`–`GAME-0318`).
- Exact genome matches: none.
- Tied near matches: `GAME-0224` — Once Human (`6 / 25 = 0.240000`).
- Supported combination subsets: none.
- Scan date: 2026-09-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0224` — Once Human | `ACT-008`, `ACT-341`, `SYS-215`, `INF-115`, `INF-119`, `TIM-003` | Both directly traverse a live online world, use contextual fixtures and read local threats plus health. Once Human follows a gated authored combat tutorial into scenario-selection authority; Sea of Thieves coordinates persistent vessel stations, infers an island across two maps, exposes one buried object and protects its freely transferable custody through a return-and-sale circuit. | Near, `0.240000` |

### Preserved research notes

- New genes: `ACT-474`, `ACT-475`, `SYS-918`–`SYS-920`, `CON-648`, `INF-351`
  and `OBJ-186`.
- Classification result: `New gene`; no verified combination is expected.
- Evidence and reasoning: no lower-ID boundary models separately reached ship
  stations whose retained settings jointly drive one live vessel, an X-map
  search that exposes one buried object, or physical shared-world treasure
  custody inside a required return-and-sale tutorial circuit.

## Taxonomy impact

- Registry changes: add two Action, three System Behaviour, one Constraint,
  one Information and one Objective boundary; add Sea of Thieves support to
  compatible existing movement, carry, interaction, sale, combat, health,
  perception, HUD and real-time genes.
- Taxonomy-change record: none; no existing definition changes.
- Candidate terms affected: Sloop, capstan, sail, wheel, X-map, Quest Table,
  Sailor's Chest, Outpost, Gold Hoarders, High Seas and exact reward values
  remain product, fixture, object, place or run parameters.

## Negative results

- No Xbox Series console, installed client, account session, direct play,
  input trace, screenshot, video or audio evidence exists for this unit.
- The live product can change after 3.9.0; this record does not project Season
  21's no-dive experiment into later releases.
- Other crews may never appear in one run. Their possibility and treasure
  authority are admitted because High Seas cannot guarantee absence, not
  because combat was observed or required.
- Exact wind values, island selection probabilities, shovel tolerance,
  respawn interval and gold amount are not established and remain parameters.

## Delta summary

## New facts

- [Confirmed | Direct | High] Version 3.9.0 makes the Gold Hoarders Tutorial
  Voyage a sailed, chest-hand-in terminal during Season 21 (`SOT-001`–`SOT-003`).
- [Observation | Corroborated | High] The route joins map correlation,
  multi-station Sloop control, excavation, physical custody and sale
  (`SOT-004`–`SOT-010`).

## New genes

- [Observation | Corroborated | High] `ACT-474`, `ACT-475`, `SYS-918`–`SYS-920`,
  `CON-648`, `INF-351` and `OBJ-186` isolate the eight new portable boundaries.

## New combinations

- [Observation | Corroborated | High] No new verified combination.

## Taxonomy changes

- [Observation | Corroborated | High] No existing gene boundary changes.

## New questions

- How does the same tutorial packet change in Safer Seas when other-crew
  custody risk is structurally removed?
- Which additional station, repair and crew-authority genes become necessary
  for a bounded multi-player naval engagement?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0320` Animal Crossing: New Horizons.
- Optimisation criterion: move from one live, physically contested voyage to a
  peaceful daily island loop with resource transformation and resident time.
- Expected information gain: test real-world calendar authority, island
  construction and social/resource progression without hostile custody.
- Backlog impact: `GAME-0320` remains next; no later unit starts in this commit.

## Why this game

- [Hypothesis | Limited | High] Sea of Thieves is a recognisable Xbox anchor
  whose smallest current tutorial circuit makes sailing, map inference and
  stealable treasure causally inspectable without pretending to cover the
  entire live service.

## Research checklist

- [x] exact current edition, version, mode, crew, entry and terminal declared
- [x] live Season 21 no-dive rule and chest-hand-in fix verified
- [x] unrelated live-service systems and combat excluded
- [x] official sources separated from community route corroboration
- [x] direct-play and audiovisual limitations disclosed
- [x] complete six-type gene scan performed
- [x] deterministic lower-ID comparison and combination scan completed
- [x] reviewed Ukrainian localisation and bilingual presentation completed
- [x] original artwork and responsive browser checks completed
