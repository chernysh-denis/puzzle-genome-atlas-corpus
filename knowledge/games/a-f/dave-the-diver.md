---
game_id: GAME-0278
slug: dave-the-diver
game_title: DAVE THE DIVER
analysis_status: reviewed
reviewed: 2026-09-08
combination_ids:
  - COMB-0270
gene_ids:
  action:
    - ACT-008
    - ACT-091
    - ACT-245
    - ACT-447
    - ACT-448
  system:
    - SYS-030
    - SYS-543
    - SYS-822
    - SYS-823
  constraint:
    - CON-460
    - CON-620
  information:
    - INF-075
    - INF-117
    - INF-299
    - INF-330
  objective:
    - OBJ-167
  time:
    - TIM-002
    - TIM-003
---

# Game: DAVE THE DIVER

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `1868140`, package `672152`, publisher-labelled version `v1.0.6.2087` from the
  `8/10 Hotfix`, observed against sole public-branch build `24651119`; both the
  announcement and branch record are dated 2026-08-10. Checked 2026-09-08.
- Product boundary: the base application on Windows. The five separately listed
  DLC apps, including collaboration and content packs, are outside this packet.
- Platform, input and difficulty: English interface, Windows, keyboard or
  controller, single player from a fresh story save. No selectable difficulty
  is varied.
- Setup-only predecessors: the opening cutscenes, the first control tutorial,
  the knife and three-fish harpoon exercises, the first return to the boat, the
  earthquake at the restaurant and the request to catch seven further fish.
  They establish the route but are not replayed as part of its decision set.
- Entry: accept ordinary control on the boat for the required second dive under
  `Prepare Sushi Ingredients`, before entering the water and before any of its
  seven fish are caught.
- Primary decision loop: enter the water; read oxygen and choose a reachable
  small fish; navigate into harpoon range and take it into carried stock; repeat
  until exactly the seven required fish are retained, then surface before
  oxygen exhaustion. In the evening, inspect recipes, supported serving counts
  and prices; commit a bounded menu from that stock; complete the required drink
  pour and prepared-dish delivery tutorial; open the service; read current dish
  or drink requests, kitchen readiness and individual wait pressure; move the
  matching prepared item to the most urgent requester; then accept the closing
  sales report and grade before continuing into the next play day.
- Positive terminal: the first restaurant service closes, its sales categories
  and aggregate grade are visible, and the game advances to `Sunday 10/02` with
  the earned balance and next-day state retained. The longer `Repair Bancho
  Sushi` mission is not required and is not falsely claimed complete.
- Negative terminal: during the required second dive, allow oxygen to reach
  zero and accept the forced return to the surface with most of that excursion's
  catch lost. A missed restaurant customer is an evaluated local loss, not
  terminal failure of the whole service.
- Included: direct movement in the dive and restaurant; exactly seven ordinary
  starting-area fish taken with the harpoon; the depleting oxygen reserve and
  forced-return loss; recipe, serving and price inspection; menu allocation;
  the mandatory early drink-pour and dish-delivery tutorials; system-arriving
  requests, visible individual wait pressure, prepared-dish readiness, service
  revenue, closing report, grade and transition to the next day.
- Excluded: optional catches beyond seven and the resulting encumbrance or later
  pickup cutoff; weapon crates, hostile-fish combat and equipment upgrades; the
  uncompleted 100-Gold repair mission; the next day's specimen and weaponsmith
  routes; staff, farming, research, branch management, later restaurant tools
  and all later story days; DLC, collaboration packs, achievements and account
  progression; screenshots, official artwork, third-party media, video and
  audio evidence.
- Reproducible parameterisation: start a fresh English Windows save in
  `v1.0.6.2087`; complete the first tutorial dive and earthquake setup; begin
  the required second dive, catch seven small starting-area fish with the
  harpoon and surface immediately; use those ingredients to complete the menu,
  drink and delivery tutorials; open and finish the first real service; read the
  sales report and grade; continue until `Sunday 10/02` is shown. Species,
  prices, serving allocations, customer order sequence and exact grade remain
  parameters.
- Potential scoped modules: an overcapacity dive that actually crosses both
  weight thresholds; the completed 100-Gold prologue; staff automation; farming;
  weapon and equipment economies; later restaurant ranks and branch operation.
- Direct-play status: not conducted. Valve application data and the Steam store
  establish lawful availability, exact product identity, Windows support,
  package and DLC boundaries. The publisher's official announcement establishes
  the exact current Windows version, and the public SteamCMD projection supplies
  the matching branch build observation. Two complete independent written
  prologue guides establish and corroborate the bounded route, oxygen loss,
  overcapacity slowdown, menu rules, individual wait failure, closing report
  and transitions. No video or audio was opened, played, heard, analysed or
  used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DTD-001` | Steam app `1868140` is the lawfully offered Windows base game in package `672152`, with five separate DLC apps | Confirmed | Direct | High | P1 |
| `DTD-002` | The current Windows build is publisher-labelled `v1.0.6.2087`, and the dated hotfix matches public build `24651119` | Confirmed | Corroborated | High | P2, S1 |
| `DTD-003` | After the first tutorial dive and earthquake, `Prepare Sushi Ingredients` requires a second dive and seven further fish | Observation | Corroborated | High | S2, S3 |
| `DTD-004` | Oxygen falls underwater; exhaustion forces return and loses most current catch, while safe surfacing retains it | Observation | Corroborated | High | P1, S3 |
| `DTD-005` | The displayed normal carry threshold first slows movement; it does not itself end the corrected seven-fish route | Observation | Corroborated | High | S3, S4 |
| `DTD-006` | Available ingredients determine recipes and supported serving counts, and the player configures the service menu from them | Observation | Corroborated | High | S2, S3 |
| `DTD-007` | The required opening service teaches a release-timed drink pour and delivery of a prepared dish to its matching requester | Observation | Corroborated | High | S2, S3 |
| `DTD-008` | Customers arrive during live service, disclose requests and individual wait pressure, and may leave before fulfilment | Observation | Corroborated | High | S2, S3 |
| `DTD-009` | Closing service exposes sales categories and an aggregate performance grade before the next play day begins | Observation | Corroborated | High | S2, S3 |
| `DTD-010` | The first service does not necessarily complete the longer 100-Gold repair mission | Observation | Corroborated | High | S2, S3 |
| `DTD-011` | The packet's portable identity is one retained stock crossing from a quota-bounded excursion into a separately timed and graded service activity | Strong Pattern | Corroborated | High | `DTD-003`–`DTD-010` |

## Basic data

- Release / origin: MINTROCKET; released 2023-06-28.
- Platform or physical form: lawfully offered English Windows Steam application
  `1868140`; one fresh-save transition from required second dive through the
  first restaurant report and into the next play day.
- Puzzle family: inventory and fixture dependencies; real-time system pressure;
  ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-08:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=1868140&cc=ua&l=english),
    for exact title, app, package, Windows support, release date, single-player
    category, five DLC apps, lawful offer, and the official day-dive / night-
    restaurant description including oxygen-exhaustion loss.
  - **[P2]** [publisher announcement surface](https://steamcommunity.com/app/1868140),
    for the `8/10 Hotfix`, Windows version `v1.0.6.2087` and Mac version
    `v1.0.6.740` as distinct platform observations.
- Corroborating textual sources, accessed 2026-09-08:
  - **[S1]** [public SteamCMD info projection](https://api.steamcmd.net/v1/info/1868140),
    for public branch build `24651119` and its 2026-08-10 update timestamp.
  - **[S2]** [Rectify Gaming prologue walkthrough](https://www.rectifygaming.com/dave-the-diver-prologue-a-sushi-bar-by-the-blue-hole-walkthrough/),
    read completely, for the two-dive opening, seven-fish requirement, menu,
    supported serving counts, drink pour, delivery, first customer set, sales
    report, grade and `Sunday 10/02` boundary.
  - **[S3]** [Sirus Gaming prologue walkthrough](https://sirusgaming.com/dave-the-diver-walkthrough-a-sushi-bar-by-the-blue-hole-prologue/),
    read completely, for oxygen loss, overcapacity slowdown, menu allocation,
    drink evaluation, requested-dish delivery, individual customer waits,
    closing sales summary and next-day transition.
  - **[S4]** [Steam Community weight discussion](https://steamcommunity.com/app/1868140/discussions/0/3801651941330462133/),
    used only to corroborate that the displayed normal weight threshold imposes
    slowdown before a separate upper pickup cutoff; it is not used to define a
    gene in this route.
- Source-class limitation: exact product and version claims are primary. The
  route's control-level mechanics are established by complete independent
  written secondary sources rather than direct play and therefore remain
  observations rather than confirmations.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P2` and `S1`–`S4` under the declared app, version, build, fresh save,
  exact seven-fish route, exclusions and terminals; rules reasoning, not direct
  play.
- Claim IDs: `DTD-001`–`DTD-011`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: direct movement navigates both the underwater route and
  the restaurant floor.
- Existing `ACT-091`, generalised by `TAXONOMY_CHANGE_038`: pick up the prepared
  dish and commit it to the customer whose current request accepts it.
- Existing `ACT-245`: address one reachable eligible fish with the harpoon and
  extract its finite yield into carried stock.
- New `ACT-447`: select an available recipe and commit its supported serving
  stock to the bounded service menu.
- New `ACT-448`: hold the drink dispenser and release it against the visible
  target level, accepting the resulting evaluation.
- `ACT-341` is removed from the candidate: entering a surface or opening the bar
  is transition plumbing, while the decision-bearing interactions have exact
  lower-ID or new portable boundaries. Claims: `DTD-003`, `DTD-006`, `DTD-007`.

### System Behaviour Genes

- Existing `SYS-030`, generalised by `TAXONOMY_CHANGE_038`: simulation time
  introduces visible service requests that wait for compatible fulfilment.
- Existing `SYS-543`: oxygen depletes underwater, warns near exhaustion and is
  restored at breathable surface state.
- Existing `SYS-822`, generalised by `TAXONOMY_CHANGE_038`: service closure
  evaluates how the bounded activity was performed and records a grade.
- New `SYS-823`, corrected from the candidate: the previous dive's fish stock
  determines selectable menu capacity; prepared and accepted deliveries consume
  that capacity and settle as revenue at service close.
- Resolution order: the second dive produces stock under oxygen pressure;
  surfacing retains and converts the catch into ingredient capacity; menu setup
  exposes selected servings; service time introduces requests, kitchen
  preparation makes matching dishes ready, accepted deliveries consume servings
  and pay revenue; closing computes the grade and advances to the next day.
  Claims: `DTD-004`, `DTD-006`–`DTD-009`, `DTD-011`.

### Constraint Genes

- Existing `CON-460`: the underwater route remains viable only while oxygen or
  reachable air can cover the return.
- New `CON-620`: each service request is legal only until its individual wait
  allowance expires; one expiry loses that customer without ending the session.
- Candidate `CON-618` is deprecated by `TAXONOMY_CHANGE_038`: the displayed
  normal carry threshold causes slowdown rather than ending the excursion, and
  this fixed route deliberately stops at seven small fish without testing the
  later pickup cutoff.
- Scarce resources: oxygen, seven retained catch slots as an objective quota,
  supported menu servings and each current request's remaining wait allowance.
  Claims: `DTD-003`–`DTD-005`, `DTD-008`.

### Information Genes

- Existing `INF-075`: the live personal surface exposes oxygen sufficiently to
  judge the safe return.
- Existing `INF-117`, generalised by `TAXONOMY_CHANGE_038`: recipe prices,
  supported servings, retained balance and offer availability are inspectable
  before menu allocation.
- Existing `INF-299`: the closing report exposes sales categories and aggregate
  performance grade.
- New `INF-330`: the live service surface identifies current requests,
  preparation readiness and individual wait pressure for prioritisation.
- `INF-036` is rejected because it covers one static requester/item disclosure,
  not a concurrent live queue with preparation and expiry state. Claims:
  `DTD-004`, `DTD-006`, `DTD-008`, `DTD-009`.

### Objective Genes

- New `OBJ-167`, corrected from the candidate: complete the required second
  excursion quota, carry that stock through the first service's own settlement,
  accept the report and reach the next play day. It does not require completion
  of the longer repair mission.
- `OBJ-163` ends by selling a voyage's catch directly to a buyer before night;
  this packet instead consumes the catch through another playable activity.
  `OBJ-021` only secures expedition resources and lacks the service terminal.
  Claims: `DTD-003`, `DTD-006`, `DTD-009`–`DTD-011`.

### Time Genes

- Existing `TIM-002`: menu inspection and allocation are self-paced before the
  player opens live service.
- Existing `TIM-003`: oxygen, drink filling, kitchen preparation, customer waits
  and movement progress while player input remains accepted.
- Candidate `TIM-013` is removed: the route crosses an ordinary next-day
  boundary, but no completed progression predicate schedules a new world
  capability overnight inside this packet. Claims: `DTD-004`, `DTD-006`–`DTD-009`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| The required second dive is available with zero of seven fish retained | Enter the water and navigate to one small reachable fish | Oxygen begins falling while movement remains live | oxygen-priced excursion entry | `DTD-003`, `DTD-004` |
| One eligible small fish is within harpoon range | Commit the harpoon catch | One finite catch enters carried stock and quota progress rises by one | gathered stock and quota | `DTD-003` |
| Exactly seven required fish are retained with oxygen remaining | Surface immediately | The catch is kept, the dive ends and evening menu setup becomes available | retained activity handoff | `DTD-003`, `DTD-006` |
| The menu is empty and ingredient stock is present | Select an available recipe and commit supported servings | The recipe becomes offerable and its serving capacity is exposed to the coming service | menu allocation | `DTD-006` |
| The drink tutorial shows an empty vessel and target line | Hold, then release the dispenser | The achieved fill level is evaluated and changes customer payment | continuous quantity commitment | `DTD-007` |
| A prepared dish and its matching requester are both visible | Carry the dish to that requester and deliver it | The request is fulfilled, serving stock is consumed and payment may be earned | addressed delivery | `DTD-007` |
| Several requests are live with unlike wait states | Prioritise one compatible ready delivery | Fulfilment removes that request; an ignored request whose wait expires leaves unpaid while service continues | local expiry pressure | `DTD-008` |
| The first customer set is exhausted and the bar closes | Accept the result surface | Sales categories and aggregate grade settle, then the calendar advances to `Sunday 10/02` | finite positive terminal | `DTD-009`, `DTD-010` |
| Oxygen reaches zero during the required second dive | Accept forced surfacing | The excursion ends and most current catch is lost | reproducible negative terminal | `DTD-004` |

## Strategic and experiential structure

- Planning horizon: the seven-fish quota is small, but its species and value
  determine which recipes and how many servings the first service can offer.
- Local tactics: underwater, return distance competes with oxygen; in service,
  requester urgency competes with kitchen readiness and travel distance.
- Medium-term structure: menu allocation converts the retained catch into a
  commitment under demand uncertainty, including risk to unused prepared stock.
- Reversible versus irreversible: navigation is revisable, but surfacing fixes
  the dive stock; menu allocation exposes servings to the session; a delivered,
  expired or closed-out request cannot be replayed inside that service.
- Failure attribution: oxygen loss is legible on the live reserve, while missed
  payment is traceable to an expired visible request or an inaccurate pour.
- Player trust: the route exposes oxygen, supported serving counts, prices,
  current requests, wait pressure, kitchen readiness and the final categories
  before or at the decisions they explain.

## Replay and variation

- What changes: generated shallow layout, species chosen for the fixed quota,
  resulting menu choices, request order, drink accuracy and final grade.
- Randomness or procedural generation: the Blue Hole may choose among layouts;
  no claim depends on one exact geometry or species distribution.
- Multiple viable strategies: any seven eligible small fish complete the dive
  quota, and different menus and service priorities can still reach closure.
- Typical replay motive: improve revenue and grade by bringing a better mix and
  serving the most urgent compatible requests more accurately.

## Adjacent systems and history

- Direct predecessors: none for this product in the corpus.
- Variants: later daily cycles, staff automation, farming, branch operation and
  DLC are potential modules, not merged into this first-service packet.
- Similar games: `GAME-0269` DREDGE for an excursion whose catch enters an
  economy; `GAME-0277` Cuphead for a live bounded activity whose performance is
  graded and explained in a terminal report.
- Important differences: DREDGE packs catch in a spatial grid, advances its
  clock through travel and sells the retained cargo directly before night. This
  packet stops before optional overcapacity, uses oxygen as the dive pressure,
  configures a menu from the retained catch and requires a second live activity
  in which requests may expire. Cuphead grades a combat win from health, time
  and technique use; this packet grades service after independently arriving
  demand and item delivery. Claims: `DTD-005`–`DTD-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-091`, `ACT-245`, `ACT-447`, `ACT-448` | fish, recipes, servings and target fill line are parameters |
| System Behaviour | `SYS-030`, `SYS-543`, `SYS-822`, `SYS-823` | arrival order, oxygen values, grade scale and settlement values are parameters |
| Constraint | `CON-460`, `CON-620` | air sources and individual wait durations are parameters |
| Information | `INF-075`, `INF-117`, `INF-299`, `INF-330` | interface styling and report category names are presentation |
| Objective | `OBJ-167` | quota, activities and retained settlement values are parameters |
| Time | `TIM-002`, `TIM-003` | menu pacing and live rates are implementation parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `277` (`GAME-0001`–`GAME-0277`).
- Exact genome matches: none.
- Tied near matches: `GAME-0269` — DREDGE (`5 / 28 = 0.178571`).
- Supported combination subsets: `COMB-0270`.
- Scan date: 2026-09-08.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0269` — DREDGE | `ACT-008`, `ACT-245`, `INF-117`, `TIM-002`, `TIM-003` | Both navigate an excursion, gather catch, inspect transaction value and alternate self-paced preparation with live action. DREDGE advances its day only through travel and chosen actions, packs catch and hardware in one spatial grid, lets catch decay and ends by selling it directly before night. This packet spends oxygen during the dive, stops at a fixed seven-fish quota, configures a menu from the retained stock and then runs a second live activity with arriving requests, individual expiry, manual delivery and a graded report. The shared theme still resolves to only five portable genes. | Near, `0.178571` |

- New genes: `ACT-447`, `ACT-448`, `SYS-823`, `CON-620`, `INF-330`, `OBJ-167`.
- Classification result: `New gene`.
- Evidence and reasoning: the corrected packet adds portable boundaries for
  menu allocation, release-timed dispensing, cross-activity service conversion,
  individual request expiry, live service disclosure and the two-activity
  terminal. It reuses twelve lower-ID boundaries instead of treating restaurant
  operations as generic authored-object interaction.

### Preserved research notes

- New genes: `ACT-447`, `ACT-448`, `SYS-823`, `CON-620`, `INF-330`, `OBJ-167`.
- Classification result: `New gene`.
- Evidence and reasoning: the corrected packet adds portable boundaries for
  menu allocation, release-timed dispensing, cross-activity service conversion,
  individual request expiry, live service disclosure and the two-activity
  terminal. It reuses twelve lower-ID boundaries instead of treating restaurant
  operations as generic authored-object interaction.

## Taxonomy impact

- Registry changes: add `ACT-447`, `ACT-448`, `CON-620` and `INF-330`; retain
  the corrected new `SYS-823` and `OBJ-167`; add independent evidence to twelve
  reused genes.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_038`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_038.md)
  generalises `ACT-091`, `SYS-030`, `SYS-822` and `INF-117`, adds an independent
  service carrier to unchanged information boundary `INF-299`, and deprecates
  `CON-618`. No earlier reviewed signature changes.
- Candidate terms affected: `DAVE THE DIVER`, MINTROCKET, Blue Hole, Bancho
  Sushi, named missions, dishes, characters, drinks, calendar labels, Gold,
  version, app, package and build identifiers remain game-scoped parameters or
  official labels.

## Negative results

- No video or audio evidence was opened or used. Search results that exposed
  video links were not entered, played, heard or analysed.
- Reject the candidate's “first dive” packet: the opening first dive is only a
  knife/harpoon tutorial, while the seven fish that supply the service belong to
  a required second dive after the earthquake.
- Reject the candidate's semantic-version gap: the current publisher hotfix
  explicitly labels Windows version `v1.0.6.2087`.
- Reject the historical `CON-618`, deprecated by `TAXONOMY_CHANGE_038`: the
  displayed normal weight threshold slows the swimmer; it does not force
  surfacing. The later upper pickup cutoff is optional and is not tested by the
  exact seven-small-fish route.
- Reject `ACT-341` as a substitute for menu allocation, pouring and delivery;
  each is a different portable action with a different commitment boundary.
- Reject `INF-036` because one static requested-item depiction lacks a live
  concurrent queue, preparation readiness and individual expiry pressure.
- Reject `CON-052`: one impatient customer leaves, but the whole service does
  not terminate at that wait limit.
- Reject `CON-297`, `ACT-123`, `SYS-156` and `SYS-551`: menu allocation is not
  personal crafting or an autonomous production queue, and the scoped kitchen
  preparation is part of the service conversion rather than a player-authored
  factory.
- Reject `OBJ-163` and `OBJ-021` for the objective; direct sale or secure return
  does not include the second playable activity and its evaluated report.
- Reject `TIM-013`: ordinary next-day continuation is not an overnight scheduled
  capability unlock. Exclude the repair mission because the first service need
  not earn its full target.

## Delta summary

## New facts

- [Confirmed | Corroborated | High] `DTD-001`–`DTD-002`: current Windows
  `v1.0.6.2087`, public build `24651119`, package and DLC boundary.
- [Observation | Corroborated | High] `DTD-003`–`DTD-011`: the corrected second-
  dive-to-first-service route, its negative terminal and its next-day positive
  terminal.

## New genes

- [Observation | Corroborated | High] `ACT-447`, `ACT-448`, `SYS-823`,
  `CON-620`, `INF-330`, `OBJ-167`.

## New combinations

- [Pattern | Corroborated | High] `COMB-0270` — graded bounded activity with an
  explanatory terminal report, supported independently by Cuphead and this
  packet.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_038` — generalise four
  reused boundaries, expand `INF-299` with an independent service carrier and
  deprecate the false `CON-618` candidate.

## New questions

- Does a later independently scoped product support the menu-allocation,
  individual-expiry or release-timed dispenser genes strongly enough for a new
  cross-product combination?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0279` — PowerWash Simulator.
- Optimisation criterion: end the batch with a bounded coverage task whose only
  objective is measured completeness.
- Expected information gain: separate a completion percentage from a score.
- Backlog impact: completes the recorded 271-to-279 horizon.

## Why this game

- [Hypothesis | Limited | Medium] The selection asked which decisions causally
  bridge dive inventory to service resolution. The corrected answer is an
  explicit chain from quota catch through menu allocation, live expiring demand
  and a graded report, not the candidate's hard-capacity shortcut.
