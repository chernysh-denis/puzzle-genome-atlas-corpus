---
game_id: GAME-0275
slug: command-and-conquer-remastered-collection
game_title: Command & Conquer Remastered Collection
analysis_status: reviewed
reviewed: 2026-09-07
combination_ids: []
gene_ids:
  action:
    - ACT-139
    - ACT-189
    - ACT-315
    - ACT-316
  system:
    - SYS-158
    - SYS-215
    - SYS-297
    - SYS-305
    - SYS-551
    - SYS-821
  constraint:
    - CON-273
    - CON-292
    - CON-467
  information:
    - INF-131
    - INF-224
    - INF-225
  objective:
    - OBJ-166
  time:
    - TIM-003
---

# Game: Command & Conquer Remastered Collection

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `1213210`, single package `419639`, observed against public branch build
  `21590013`, whose branch record was updated 2026-01-28; checked 2026-09-07.
  EA publishes no version-named announcement for this client, so **no semantic
  version is asserted**.
- Product boundary: the application is a collection. This packet analyses only
  **Tiberian Dawn Remastered's opening GDI campaign mission, X16-Y42**. Red
  Alert Remastered, every expansion and later mission, the bonus gallery,
  multiplayer, skirmish, the map editor and Workshop content are outside it.
- Platform, input and difficulty: English interface, Windows, mouse and
  keyboard, unmodified offline single-player campaign at the default difficulty
  from a fresh profile.
- Entry: accept first ordinary control with the opening infantry present,
  before issuing an order.
- Primary decision loop: use the starting infantry until the authored arrival
  supplies the mobile construction vehicle and further combat units; clear a
  legal footprint and deploy that vehicle into a construction site; spend the
  finite opening credit balance through the shared structure channel on a power
  facility and then the unlocked infantry-production building; place each ready
  structure on legal ground; train a small infantry group; read current sight,
  remembered terrain, unit health, credit, power and production state; then
  select groups and commit movement or attack orders until the declared hostile
  set is gone.
- Positive terminal: all mission-declared hostile units and fortifications are
  removed, the mission reports victory and presents its score/debrief, and the
  campaign advances to the next scenario.
- Negative terminal: the mission's player-loss trigger settles first; the
  attempt returns to restart rather than advancing the campaign.
- Included: direct group orders and continuous combat; autonomous pathing and
  attack acquisition; unit-projected sight, fog-gated targeting and remembered
  terrain; the authored friendly arrival; deployment of the mobile construction
  vehicle into the construction site; the single paid structure-production
  channel; legal placement of the completed power and infantry-production
  buildings; the power supply/demand state; one building-local infantry queue;
  the command sidebar's live state; and the eliminate, debrief and successor
  terminal.
- Excluded: resource harvesting, because X16-Y42 starts with enough credits and
  introduces no harvester/refinery loop; any structure or unit beyond the power
  facility, infantry-production building and one ordinary infantry type used in
  the route; selling, repair and packing the construction site back into a
  vehicle; Red Alert Remastered, expansions, later missions, multiplayer,
  skirmish, the editor, Workshop and gallery content; legacy executables;
  achievements, account progression, screenshots, official art, third-party
  assets, video and audio evidence.
- Reproducible parameterisation: install English app `1213210`, confirm the
  public branch build, start a fresh Tiberian Dawn Remastered GDI campaign at
  default difficulty, follow the written mission instruction by deploying the
  arriving mobile construction vehicle, build and place the power facility then
  the unlocked infantry-production building, train at least one ordinary
  infantry unit and eliminate the remaining hostile set. Exact unit counts,
  structure names, costs, map geography and arrival timings are parameters.
- Potential scoped modules: the same mission completed by the force-only
  shortcut; a later economy mission with harvesting; Red Alert Remastered;
  skirmish or multiplayer.
- Direct-play status: not conducted. Valve data and the current Steam offer
  establish lawful availability and product identity. EA's released
  Tiberian Dawn DLL source directly establishes deploy legality, vehicle-to-site
  conversion, build availability, paid timed production, ready placement,
  power accounting, sight, reinforcement actions and campaign settlement.
  Full-page written references establish the exact opening-mission instruction
  and route. No audiovisual source was opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CNC-001` | Steam app `1213210` is the current lawfully offered Windows collection, sold through package `419639`, with single-player, multiplayer, Workshop and editor categories | Confirmed | Direct | High | P1 |
| `CNC-002` | The public branch carries build `21590013`, updated 2026-01-28, while no version-named client announcement is available | Observation | Corroborated | Medium | S1, P1 |
| `CNC-003` | The collection contains two remastered base games, so the packet must bind one included game and mission | Confirmed | Direct | High | P1, P2 |
| `CNC-004` | X16-Y42's authored instruction is to protect and deploy the arriving mobile construction vehicle, begin a base with a power facility, and eliminate the surrounding hostile force | Observation | Corroborated | High | S2, S3 |
| `CNC-005` | Deployment requires a legal full structure footprint and replaces the mobile construction vehicle with an owned construction site while carrying forward its health ratio | Confirmed | Direct | High | P3 |
| `CNC-006` | The construction sidebar exposes price and production state; one paid structure advances over real time, then becomes a player-placed completed object | Confirmed | Direct | High | P4, P5 |
| `CNC-007` | The power facility is available from the opening build level, while the infantry-production building requires it and then provides the infantry production site | Confirmed | Direct | High | P6, P7 |
| `CNC-008` | Owned power output and building demand form a live power fraction whose shortfall changes dependent building behaviour | Confirmed | Direct | High | P6, P8 |
| `CNC-009` | Unit movement, acquisition, combat and current sight resolve continuously under committed orders, while explored terrain persists under fog | Confirmed | Direct | High | P2, P9 |
| `CNC-010` | An authored reinforcement action can add the mission's friendly group without player cost or production; X16-Y42 supplies combat units and the mobile construction vehicle this way | Observation | Corroborated | High | P10, S2 |
| `CNC-011` | A win trigger enters the victory flow, presents mission score, increments the scenario and starts the next scenario | Confirmed | Direct | High | P10, P11 |
| `CNC-012` | The standard bounded route is a complete command, economy and combat packet: authored supply establishes the base, one prerequisite chain converts finite credits and power into infantry, and direct orders close the hostile-set terminal | Strong Pattern | Corroborated | High | `CNC-004`–`CNC-011` |

## Basic data

- Release / origin: developed by Petroglyph Games and Lemon Sky Studios and
  published by Electronic Arts; released 2020-06-05, remastering the two base
  games originally released in 1995 and 1996.
- Platform or physical form: lawfully offered Windows Steam application
  `1213210`; one offline single-player mission is scoped.
- Puzzle family: agent routing and coordination; tactical forecast and
  counterplay; real-time system pressure; ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-07:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=1213210&cc=ua&l=english),
    for exact title, app, Windows support, publisher, release date, package and
    store categories.
  - **[P2]** [EA's official Remastered Collection source repository](https://github.com/electronicarts/CnC_Remastered_Collection),
    for the direct relationship between the released Tiberian Dawn DLL source
    and the commercial collection.
  - **[P3]** [Tiberian Dawn `UNIT.CPP`](https://github.com/electronicarts/CnC_Remastered_Collection/blob/master/TIBERIANDAWN/UNIT.CPP#L1679-L1760),
    for legal deployment, vehicle rotation, construction-site creation, reveal,
    inherited health ratio and deletion of the vehicle.
  - **[P4]** [Tiberian Dawn `SIDEBAR.CPP`](https://github.com/electronicarts/CnC_Remastered_Collection/blob/master/TIBERIANDAWN/SIDEBAR.CPP#L2284-L2410),
    for price disclosure, production start/suspend/cancel, completion and manual
    placement of a ready building.
  - **[P5]** [Tiberian Dawn `FACTORY.CPP`](https://github.com/electronicarts/CnC_Remastered_Collection/blob/master/TIBERIANDAWN/FACTORY.CPP#L255-L300),
    for timed production steps, progressive credit debit, insufficient-credit
    stall and completion.
  - **[P6]** [Tiberian Dawn `BDATA.CPP`](https://github.com/electronicarts/CnC_Remastered_Collection/blob/master/TIBERIANDAWN/BDATA.CPP),
    for construction-site, power-facility and infantry-production-site roles,
    prerequisites, costs, production classes and power values.
  - **[P7]** [Tiberian Dawn `HOUSE.CPP` build legality](https://github.com/electronicarts/CnC_Remastered_Collection/blob/master/TIBERIANDAWN/HOUSE.CPP#L533-L608),
    for buildability, ownership, prerequisite and build-level validation.
  - **[P8]** [Tiberian Dawn `HOUSE.CPP` power fraction](https://github.com/electronicarts/CnC_Remastered_Collection/blob/master/TIBERIANDAWN/HOUSE.CPP#L4655-L4675),
    for the owner-wide power supply/demand ratio.
  - **[P9]** [Tiberian Dawn `MAP.CPP`](https://github.com/electronicarts/CnC_Remastered_Collection/blob/master/TIBERIANDAWN/MAP.CPP#L277-L340),
    for sight updates around moving or deployed units; command and combat rules
    are corroborated throughout the same released DLL source.
  - **[P10]** [Tiberian Dawn `TRIGGER.CPP`](https://github.com/electronicarts/CnC_Remastered_Collection/blob/master/TIBERIANDAWN/TRIGGER.CPP#L850-L900),
    for authored win, loss and reinforcement actions.
  - **[P11]** [Tiberian Dawn `SCENARIO.CPP`](https://github.com/electronicarts/CnC_Remastered_Collection/blob/master/TIBERIANDAWN/SCENARIO.CPP#L355-L542),
    for the victory notice, score presentation, scenario increment and successor
    start.
- Corroborating textual sources, accessed 2026-09-07:
  - **[S1]** [public SteamCMD info projection](https://api.steamcmd.net/v1/info/1213210),
    for public build `21590013` and its branch timestamp; this remains a
    secondary distribution observation.
  - **[S2]** [StrategyWiki's complete X16-Y42 page](https://strategywiki.org/wiki/Command_%26_Conquer/X16-Y42),
    for the written mission briefing, optional force-only shortcut and next
    mission identity.
  - **[S3]** [Gamer Walkthroughs' complete X16-Y42 page](https://gamerwalkthroughs.com/command-conquer/gdi-mission-1/),
    for the standard base, power, infantry-production, training and hostile-set
    route.
- Reproducible control: **[V1]** repository-side transition trace over the
  released code and complete written route under the declared app, build,
  platform, input, difficulty, fresh profile and exclusions; rules reasoning,
  not direct play.
- Claim IDs: `CNC-001`–`CNC-012`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-139`: place the completed power or infantry-production building
  on one legal owned footprint.
- Existing `ACT-189`: select one or more commanded units and commit a movement,
  destination or attack order.
- Existing `ACT-315`: deploy the mobile fabrication vehicle into its fixed
  construction-site state.
- Existing `ACT-316`: commit the next eligible structure or infantry order to
  its production channel.
- Parameters: selected group, destination, target, mobile fixture, structure,
  production site, order, footprint and cancellation state. Claims: `CNC-004`–
  `CNC-007`, `CNC-009`.

### System Behaviour Genes

- Existing `SYS-158`: pool the owner's current power output and demand and apply
  the resulting satisfaction state to dependent buildings.
- Existing `SYS-215`: resolve range-, cadence-, damage-, armour- and
  defeat-dependent combat continuously.
- Existing `SYS-297`: execute the committed navigable path and acquire the
  ordered legal target.
- Existing `SYS-305`: update current allied sight and fog from controlled unit
  positions.
- Existing `SYS-551`: advance the active paid site-bound production order; a
  completed structure waits for placement, while a completed infantry order
  exits its site.
- Existing `SYS-821`: deliver the authored friendly group at the declared
  mission event without player cost or production.
- Resolution order: an arrival makes the mobile fabrication vehicle available;
  its legal deployment creates the construction site; production drains credits
  over time and exposes the completed structure for legal placement; power
  changes the shared supply state; the placed infantry site advances a paid
  unit order; group commands then resolve movement, sight, target acquisition
  and combat until the terminal trigger fires. Claims: `CNC-005`–`CNC-011`.

### Constraint Genes

- Existing `CON-273`: current hostile position and ordinary targeting require
  allied sight.
- Existing `CON-292`: deployment and completed-building placement require a
  compatible clear footprint.
- Existing `CON-467`: each production order requires the eligible owned site,
  current unlock/prerequisite and sufficient credits; the infantry site is not
  available before the power facility.
- Scarce resources: the finite starting force, fixed opening credit balance,
  single structure-production channel, shared power supply, production time and
  unit-projected sight. Claims: `CNC-004`–`CNC-010`.

### Information Genes

- Existing `INF-131`: the deploy cursor and building-placement feedback expose
  whether the current footprint is legal before commitment.
- Existing `INF-224`: the command view exposes credits, power, current
  selection, health, available orders and production progress.
- Existing `INF-225`: explored terrain persists while current mobile hostile
  state remains hidden outside allied sight.
- Claims: `CNC-004`–`CNC-009`.

### Objective Genes

- Existing `OBJ-166`: eliminate the mission-declared hostile set, reach the
  victory/score settlement and retain the campaign successor.
- The objective is not `OBJ-029`: that gene ends at incapacitating one bounded
  encounter set and carries no campaign settlement. It is not `OBJ-103`, whose
  Conquest terminal is a symmetric recoverable-civilization predicate.
- Claims: `CNC-004`, `CNC-011`, `CNC-012`.

### Time Genes

- Existing `TIM-003`: production, power state, movement, combat and trigger
  evaluation progress while commands continue to be accepted.
- Claims: `CNC-006`, `CNC-008`–`CNC-012`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| First infantry are controllable and the mobile construction vehicle is absent | Clear the nearby route and continue | The authored reinforcement action supplies the vehicle and further owned combat units | scripted friendly arrival | `CNC-004`, `CNC-010` |
| The mobile construction vehicle is idle on clear terrain | Commit deployment | Full construction-site footprint legality is checked; the vehicle turns, becomes the owned construction site and preserves its health ratio | mobile-to-fixed fabrication | `CNC-005` |
| The construction site is active and the opening credit balance is visible | Start the power-facility order | The shared structure channel advances over real time and debits credits by production step until ready | paid live construction | `CNC-006` |
| The power facility is ready and the deploy cursor is over a compatible footprint | Commit placement | The completed object joins the owned base, adds power and exposes the next prerequisite-dependent option | spatial placement and power | `CNC-006`–`CNC-008` |
| The power prerequisite and credits are present | Produce and place the infantry-production building | The same shared structure channel completes it; legal placement creates an infantry production site | ordered dependency | `CNC-006`, `CNC-007` |
| The infantry site is active and credits remain | Queue one ordinary infantry unit | Its site-bound paid production advances and releases the completed unit | unit production | `CNC-006`, `CNC-007` |
| A group is selected beside unexplored ground | Commit a destination or attack order | Pathing moves the group, active sight updates, remembered terrain persists and legal targets are acquired inside sight | command, fog and combat | `CNC-009` |
| The final declared hostile object is removed | Continue through settlement | The win flag enters victory handling, presents the mission result, increments the scenario and starts its successor | reproducible terminal | `CNC-011` |

## Strategic and experiential structure

- Planning horizon: one fixed credit balance and one structure channel must
  satisfy a short prerequisite chain before the same economy can add infantry.
- Local tactics: each move simultaneously changes formation geometry, current
  sight, legal targets and exposure to return fire.
- Medium-term structure: protect the arriving mobile construction vehicle,
  convert it into production authority, establish power before infantry
  production, then convert remaining credits and time into enough force to
  close the hostile set.
- Reversible versus irreversible: an order may be replaced, and production may
  be suspended or cancelled; a deployed vehicle, placed structure, spent
  production time and lost unit are not freely undone in the scoped route.
- Failure attribution: current credits, power, production progress, legal
  placement feedback, health, sight and remembered terrain make whether the
  failure came from the dependency chain or the advance legible.
- Player trust: the mission instruction names the chain, the released rules
  expose stable legality and cost relations, and the terminal advances through
  a declared trigger rather than an arbitrary stopping point.

## Replay and variation

- What changes: exact footprint choices, how many infantry are trained, group
  composition, order of advance and which visible hostile is focused first.
- Randomness or procedural generation: the map, arrival and hostile set are
  authored. No procedural-generation claim enters the packet.
- Multiple viable strategies: the standard tutorial chain is declared here;
  completing with only provided forces is a valid but separately excluded
  shortcut because it removes the selection unit's economy question.
- Typical replay motive: reduce losses or production delay while preserving the
  standard dependency chain.

## Adjacent systems and history

- Direct predecessors: the original 1995 Tiberian Dawn mission supplies the
  authored scenario; only the current Remastered Collection client and released
  DLL boundary are asserted here.
- Variants: Red Alert Remastered, later Tiberian Dawn missions, skirmish and
  multiplayer are distinct rulesets outside this packet.
- Similar games: `GAME-0179` Age of Empires II: Definitive Edition shares RTS
  selection, placement, site-bound production, prerequisite legality, command,
  combat, fog and command-view disclosure; `GAME-0138` Dota 2 supplies the
  lower-level order/pathing/sight corridor; `GAME-0178` Subnautica supplies the
  mobile fabrication-fixture deployment boundary.
- Important differences: this mission has no gathering loop, population cap,
  research or Ages. Its tiny economy starts from a fixed credit balance, runs
  one shared structure channel, uses an owner-wide power pool and receives its
  initial production authority through an authored arrival.
- Claims: `CNC-004`–`CNC-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-139`, `ACT-189`, `ACT-315`, `ACT-316` | unit, order, mobile fixture, production target and footprint are parameters |
| System Behaviour | `SYS-158`, `SYS-215`, `SYS-297`, `SYS-305`, `SYS-551`, `SYS-821` | power-domain topology, production output and arrival composition are parameters |
| Constraint | `CON-273`, `CON-292`, `CON-467` | sight, footprint, producer, prerequisite and credit values are parameters |
| Information | `INF-131`, `INF-224`, `INF-225` | cursor form and exact command-panel fields are presentation parameters |
| Objective | `OBJ-166` | hostile-set composition and successor identity are parameters |
| Time | `TIM-003` | tick, production and combat cadence are implementation parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `274` (`GAME-0001`–`GAME-0274`).
- Exact genome matches: none.
- Tied near matches: `GAME-0179` — Age of Empires II: Definitive Edition (`12 / 35 = 0.342857`).
- Supported combination subsets: none.
- Scan date: 2026-09-07.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0179` — Age of Empires II: Definitive Edition | `ACT-139`, `ACT-189`, `ACT-316`, `SYS-215`, `SYS-297`, `SYS-305`, `SYS-551`, `CON-273`, `CON-467`, `INF-224`, `INF-225`, `TIM-003` | Both turn a visible economy and prerequisite graph into placed production capacity, then command units through fog in real time. Age of Empires physically tasks villagers through four gathered stockpiles, builds population capacity, advances Ages and runs many site-local queues toward civilization-wide Conquest. X16-Y42 starts with one finite credit balance, no gathering, one shared structure channel, a short power-to-infantry dependency and an authored reinforcement that delivers the mobile source of construction authority. | Near, `12 / 35 = 0.342857` |

- Reused genes: all eighteen genes; no new ID survives independent review.
- Classification result: `Existing gene` plus eight accepted wording
  generalisations in `TAXONOMY_CHANGE_036`.
- Evidence and reasoning: the candidate's two new genes remain reusable, but
  the supposedly economy-free scope was rejected. The standard route supplies
  new independent evidence for sixteen lower-ID genes and turns product-bound
  wording in eight of them into portable parameters.

### Preserved research notes

- Reused genes: all eighteen genes; no new ID survives independent review.
- Classification result: `Existing gene` plus eight accepted wording
  generalisations in `TAXONOMY_CHANGE_036`.
- Evidence and reasoning: the candidate's two new genes remain reusable, but
  the supposedly economy-free scope was rejected. The standard route supplies
  new independent evidence for sixteen lower-ID genes and turns product-bound
  wording in eight of them into portable parameters.

## Taxonomy impact

- `TAXONOMY_CHANGE_036` generalises `ACT-139`, `ACT-315`, `ACT-316`, `SYS-158`,
  `SYS-551`, `CON-292`, `CON-467` and `INF-224` from one carrier's settlement,
  water, Age, network or unit nouns to the transferable operation.
- `SYS-821` and `OBJ-166` remain Active but gain released-code corroboration;
  their meaning, lifecycle and IDs do not change.
- No earlier reviewed game signature or combination gene set changes. The only
  signature mutation is this draft game's correction from eight to eighteen
  genes.
- All product, faction, mission, unit, structure, numeric cost and map names
  remain game-scoped parameters.

## Negative results

- The candidate's force-only shortcut was rejected as the canonical packet.
  Although it can finish the mission, it deliberately skipped the authored
  deploy/build instruction and contradicted the selection question's required
  command–economy–combat scope.
- `ACT-117` was rejected: it describes municipal service-placement policy,
  whereas the reusable action here is ordinary owned-building placement already
  carried by `ACT-139`; power output belongs to `SYS-158`.
- `SYS-550` and `CON-466` were rejected: no mobile worker supplies or advances
  these structures. `SYS-551` and `CON-467` cover the site-bound paid production
  channel instead.
- `OBJ-029` and `OBJ-103` were rejected: neither carries this mission's
  score/debrief and retained successor boundary.
- No new combination is recorded: every verified combination either requires a
  materially larger economy/progression chain or lacks the complete base-build
  and mission-terminal interaction.
- No video or audio evidence was used.

## Delta summary

## New facts

- [Strong Pattern | Corroborated | High] `CNC-004`–`CNC-012`: the standard
  opening mission is not an economy-free command exercise. An authored arrival
  delivers the mobile construction authority, a paid power-first prerequisite
  chain creates infantry production, and the resulting commanded force closes
  a trigger-settled campaign mission.

## New genes

- [Observation | Direct | High] `No new genes`; all eighteen boundaries reuse
  Active lower-ID genes or the two already staged candidate IDs.

## New combinations

- [Observation | Direct | High] `No new combinations`.

## Taxonomy changes

- [Observation | Direct | High] `TAXONOMY_CHANGE_036` generalises eight Active
  definitions without changing any previous signature, lifecycle or ID.

## New questions

- Does a later bounded Tiberian Dawn mission add harvesting while retaining the
  same shared structure channel, and which workerless resource genes then join
  this packet?
- Does a second carrier show `SYS-821` is the friendly-side parameter of a more
  general authored force-release system, or does control transfer keep it
  distinct from hostile `SYS-749`?

## Next recommended game

- [Hypothesis | Direct | High] `GAME-0276` — Forza Horizon 5.
- Optimisation criterion: return to one controlled vehicle and test an ordinary
  race against already reviewed series and genre neighbours.
- Expected information gain: separate portable race rules from open-world and
  live-service layers.
- Backlog impact: advances the recorded 271-to-279 closure horizon by one unit.

## Why this game

- [Strong Pattern | Corroborated | High] The independently corrected packet now
  answers the selection question it was chosen for: the smallest complete
  command, economy and combat genome of the standard opening route, without
  importing harvesting, later technology or the collection's second game.
