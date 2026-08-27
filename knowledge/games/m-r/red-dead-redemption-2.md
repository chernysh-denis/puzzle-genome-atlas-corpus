---
game_id: GAME-0165
slug: red-dead-redemption-2
game_title: Red Dead Redemption 2
analysis_status: reviewed
reviewed: 2026-08-27
combination_ids:
  - COMB-0163
gene_ids:
  action:
    - ACT-008
    - ACT-130
    - ACT-131
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-201
    - ACT-226
    - ACT-227
    - ACT-245
    - ACT-271
    - ACT-272
    - ACT-273
    - ACT-274
  system:
    - SYS-208
    - SYS-215
    - SYS-222
    - SYS-251
    - SYS-320
    - SYS-366
    - SYS-369
    - SYS-471
    - SYS-472
    - SYS-473
    - SYS-474
    - SYS-475
    - SYS-476
    - SYS-477
    - SYS-478
    - SYS-479
    - SYS-480
  constraint:
    - CON-269
    - CON-282
    - CON-285
    - CON-288
    - CON-328
    - CON-330
    - CON-331
    - CON-405
    - CON-406
    - CON-407
    - CON-408
    - CON-409
  information:
    - INF-073
    - INF-115
    - INF-117
    - INF-119
    - INF-125
    - INF-144
    - INF-181
    - INF-182
    - INF-183
  objective:
    - OBJ-092
  time:
    - TIM-003
---

# Game: Red Dead Redemption 2

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current Steam PC standard-edition **Red Dead Redemption 2:
  Story Mode** content reviewed on 2026-08-27; one clean single-player save and
  the Chapter 2 `Horseshoe Overlook` packet. Special/Ultimate Edition bonuses
  are disabled or ignored.
- Primary decision loop: inspect Arthur, horse, weapon, map, camp and local
  social/legal state; choose an on-foot or mounted route, equipment, combat,
  hunting, maintenance, purchase, donation or contextual interaction; resolve
  the live world and current mission checkpoint; then return resources and
  mission progress to Horseshoe Overlook until the authored chapter gate opens.
- Entry and exit: begins at first free control in Horseshoe Overlook immediately
  after `Eastward Bound`; succeeds when the required Chapter 2 mission graph
  culminates in `A Strange Kindness` and the gang establishes Clemens Point,
  or locally fails whenever Arthur, a protected actor, mission asset or allowed
  area violates the current checkpoint and must be retried.
- Included: required Chapter 2 Story missions and their legal partial order;
  free-roam links needed between those missions; direct on-foot movement,
  contextual cover, aiming, firearms, reloads and Dead Eye tiers available in
  the chapter; wagons required by missions; current saddled horse calling,
  direct riding, cores, bonding, care and saddle cargo; Arthur's paired cores
  and bars; current carried items, ammunition and money; required or ordinary
  hunting, skinning and carcass donation; weapon condition and gun-oil cleaning;
  Horseshoe Overlook donations, three supply categories and ledger upgrades
  after their authored unlock; ambient contextual responses, witnesses,
  reported crime, wanted search, jurisdictional bounty, surrender/payment and
  honour; map waypoints, mission markers, checkpoint retry and camp transition.
- Excluded: Chapters 1 and 3–6 except their entry boundary; both Epilogues;
  Red Dead Online; Special/Ultimate bonuses; optional Stranger chains, bounty
  boards, challenges, collectibles, legendary hunts, exhaustive crafting,
  camp cosmetics, satchel completion, minigames, theatre, photography,
  fishing not required by the selected mission graph, 100% completion,
  mission medals, cheats, mods and post-story free roam.
- Potential scoped modules: one later story chapter, one full campaign branch,
  one legendary-animal hunt, the optional Stranger network, post-game world or
  a separately versioned Red Dead Online role.
- Direct-play status: no fresh paid-account Chapter 2 playthrough was conducted.
  Rockstar product, Story Mode, support and companion-manual material establish
  the official version and systems; the licensed Piggyback guide sample and
  maintained mission/mechanics references supply reproducible transition detail.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `RDR2-001` | The PC product contains distinct Story Mode and Red Dead Online boundaries, and this analysis admits only the standard Story Mode Chapter 2 packet | Confirmed | Direct | High | P1–P3 |
| `RDR2-002` | Horseshoe Overlook is the Chapter 2 camp from `Eastward Bound` until `A Strange Kindness`, whose completion establishes Clemens Point | Confirmed | Corroborated | High | P4, S1, S2 |
| `RDR2-003` | Arthur's directly ridden saddled horse retains separate health, stamina, bond and cargo state; care and shared travel improve bond capabilities | Confirmed | Corroborated | High | P4–P6, S3 |
| `RDR2-004` | Arthur and horse use visible cores that govern recoverable outer meters, while food, rest, tonics, exertion and damage change those paired resources | Confirmed | Corroborated | High | P4, P5, S4 |
| `RDR2-005` | Firearms retain condition, lose performance through firing or exposure and can be restored in the field by consuming gun oil | Confirmed | Corroborated | High | P6, P7, S5 |
| `RDR2-006` | A witnessed offence can be interrupted before report; identification then escalates law response and leaves a regional bounty beyond the immediate search | Confirmed | Corroborated | High | P4, P7, S6 |
| `RDR2-007` | Honour changes independently from wanted state and modifies economic, ambient and authored consequences | Observation | Corroborated | High | P1, S7 |
| `RDR2-008` | Chapter 2 unlocks a shared donation box and ledger whose funds restock camp supply wagons and buy persistent camp services | Confirmed | Corroborated | High | P1, P4, S8 |
| `RDR2-009` | Dead Eye spends its own bar to slow live action and advances from automatic to manual target marking inside the scoped chapter | Confirmed | Corroborated | High | P4, S9 |
| `RDR2-010` | Required missions obey authored prerequisites and checkpoint failure rules; `A Strange Kindness` is the chapter-closing camp transition | Confirmed | Corroborated | High | P7, P8, S1, S2 |

## Basic data

- Release / origin: developed by Rockstar Studios and published by Rockstar
  Games; console release 2018-10-26 and PC release 2019-11-05/12-05 by store.
- Platform or physical form: single-player authored open-world action game;
  current standard PC Story Mode is scoped.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  inventory and fixture dependencies; ordered dependency sequencing.
- Primary and reproducible sources:
  - **[P1]** [official Rockstar game page](https://www.rockstargames.com/games/RedDeadRedemption2),
    for developer, release, Story Mode premise, gang survival and product scope.
  - **[P2]** [official Rockstar store page](https://store.rockstargames.com/game/buy-red-dead-redemption-2),
    for standard Story Mode versus Red Dead Online and edition boundaries.
  - **[P3]** [Steam product page](https://store.steampowered.com/app/1174180/Red_Dead_Redemption_2/),
    for the reviewed PC product, release and standard/Ultimate separation.
  - **[P4]** [official RDR2 Companion listing](https://play.google.com/store/apps/details?id=com.rockstargames.rdr2app),
    for the full Rockstar manual's controls, attributes, combat, hunting,
    horse bonding and Story progress boundary.
  - **[P5]** [licensed Piggyback guide sample](https://www.piggyback.com/en/wp-content/uploads/sites/7/2020/04/RDR2_UE_SAMPLEPAGES_181019_CO.pdf),
    for the five character/horse attributes, cores, meters and campfire unlock.
  - **[P6]** [Rockstar Story Mode feature material](https://www.rockstargames.com/newswire/article/9k1248838o1892/The-Red-Dead-Redemption-2-Special-Edition-Ultimate-Edition-and-Collect),
    for horse stamina, Story Mode core supplies, camp provision and weapon state.
  - **[P7]** [Rockstar Title Update 1.11 notes](https://support.rockstargames.com/articles/6dT8UroC7aKslsqA38oaxj/red-dead-redemption-2-title-update-1-11-notes-ps4-xbox-one),
    for Story Mode weapon-condition persistence, wanted triggers and Chapter 2
    mission-gate behaviour.
  - **[P8]** [Rockstar Title Update 1.04 notes](https://support.rockstargames.com/articles/D59kHtbUOojkr8G0Laz0y/red-dead-redemption-2-title-update-1-04-notes-ps4-xbox-one),
    for Chapter 2 Horseshoe Overlook save state and mission checkpoint scope.
- Secondary reproducible sources:
  - **[S1]** [Chapter 2 mission graph](https://reddead.fandom.com/wiki/Missions_in_Redemption_2),
    for required branches, legal ordering and the final mission.
  - **[S2]** [`A Strange Kindness`](https://reddead.fandom.com/wiki/A_Strange_Kindness),
    for prerequisites, mission transitions and Clemens Point outcome.
  - **[S3]** [horse guide](https://www.rdr2.org/guides/horses-guide/), for
    ownership, bonding, care, health, stamina and saddle state.
  - **[S4]** [GameSpot core guide](https://www.gamespot.com/articles/red-dead-2-core-guide-how-the-health-stamina-and-d/1100-6462802/),
    for core/bar coupling and restoration.
  - **[S5]** [weapon maintenance guide](https://www.rdr2.org/guides/weapon-maintenance-guide/),
    for use/environment degradation, stat loss, gun oil and gunsmith cleaning.
  - **[S6]** [wanted-system transition guide](https://www.rdr2.org/wiki/wanted-system/),
    for witness, identification, report, search, bounty and settlement states.
  - **[S7]** [GameSpot honour guide](https://www.gamespot.com/articles/red-dead-2-guide-to-honor-how-morality-and-the-hon/1100-6462777/),
    for conduct inputs and price, witness and presentation consequences.
  - **[S8]** [Horseshoe Overlook camp record](https://reddead.fandom.com/wiki/Horseshoe_Overlook),
    for donation-box/ledger unlock, supplies and Chapter 2 camp bounds.
  - **[S9]** [Dead Eye targeting record](https://reddead.fandom.com/wiki/Dead_Eye_Targeting),
    for Chapter 2 tier progression and manual marking.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P8` and `S1`–`S9`; rules reasoning, not a direct-play claim.
- Claim IDs: `RDR2-001`–`RDR2-010`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, navigate Arthur directly; `ACT-130`, buy a current
  shop asset, service, camp restock or ledger upgrade; `ACT-131`, consume food,
  tonic or another immediate carried item; `ACT-161`, aim and strike; `ACT-164`,
  select current equipment; `ACT-183`, reload; `ACT-201`, drive a required
  wagon; `ACT-226`, enter contextual cover; `ACT-227`, set a map waypoint;
  `ACT-245`, skin or harvest an eligible animal yield.
- New genes: `ACT-271`, call, mount and directly ride the persistent horse;
  `ACT-272`, clean one firearm with gun oil; `ACT-273`, donate value to the
  shared camp; `ACT-274`, choose a contextual ambient social response.
- Parameters: bindings, gait, horse, weapon, ammunition, item, oil, donation,
  social response, shop offer, waypoint, animal and wagon identity.
- Claim IDs: `RDR2-003`–`RDR2-010`.

### System Behaviour Genes

- Existing genes: `SYS-208`, resolve ranged attacks through cover/body state;
  `SYS-215`, resolve direct live combat; `SYS-222`, pick up eligible world loot;
  `SYS-251`, advance the authored campaign packet; `SYS-320`, simulate required
  wagons; `SYS-366`, escalate a reported crime into wanted pursuit/search;
  `SYS-369`, restore a failed mission checkpoint.
- New genes: `SYS-471`, integrate persistent horse travel, condition and cargo;
  `SYS-472`, turn care/travel into bonding levels; `SYS-473`, couple cores to
  outer meters; `SYS-474`, degrade firearm condition and performance;
  `SYS-475`, resolve the preventable witness-report phase; `SYS-476`, retain and
  settle regional bounty; `SYS-477`, aggregate conduct into honour;
  `SYS-478`, convert shared camp value into supplies/upgrades; `SYS-479`, slow
  live action and resolve Dead Eye marks; `SYS-480`, settle an animal kill into
  a harvestable carcass.
- Resolution order: live travel, people, wildlife and threats advance; current
  input changes Arthur, horse, equipment or social target; witnessed offences
  may produce a report, then law search and bounty; combat, cores, weapon
  condition and Dead Eye resolve continuously; mission scripts test checkpoints;
  donations and ledger purchases persist at camp; required mission completion
  opens successors until the camp transition.
- Parameters: exact mission graph, balance, horse breed, bond thresholds, core
  drain, weapon loss, witness compliance, bounty values, honour changes,
  supply prices, Dead Eye tier and animal yields.
- Claim IDs: `RDR2-002`–`RDR2-010`.

### Constraint Genes

- Existing genes: `CON-269`, Dead Eye requires target, resource and readiness;
  `CON-282`, main missions require authored gates; `CON-285`, weapon use
  requires compatible equipment/ammunition; `CON-288`, wagon operation requires
  viable geometry/state; `CON-328`, active wanted clearance requires an unseen
  interval; `CON-330`, mission-critical actors/assets/area must remain viable;
  `CON-331`, weapon classes and ammunition remain capacity-bounded.
- New genes: `CON-405`, horse authority requires owned reachable saddle state;
  `CON-406`, field weapon access is split between body and saddle;
  `CON-407`, firearm cleaning requires condition and gun oil; `CON-408`, paired
  core/meter state bounds sustained performance; `CON-409`, camp spending
  requires the ledger, prerequisites and shared funds.
- Scarce strategic resources: Arthur and horse outer meters and cores, Dead Eye,
  ammunition, gun oil, current firearm condition, carried items, horse cargo,
  personal money, shared camp funds/supplies, honour, time outside police sight
  and checkpoint progress.
- Claim IDs: `RDR2-003`–`RDR2-010`.

### Information Genes

- Existing genes: `INF-073`, show active equipment and ammunition; `INF-115`,
  expose local agents through sight/sound; `INF-117`, show personal money and
  prices; `INF-119`, show Arthur's resources; `INF-125`, show explored map and
  mission gates; `INF-144`, show route and current wanted search.
- New genes: `INF-181`, expose horse resources, bond and saddle cargo;
  `INF-182`, expose witness/report/bounty/honour state; `INF-183`, expose camp
  contributions, supplies, shared funds and upgrades.
- Claim IDs: `RDR2-003`–`RDR2-010`.

### Objective Genes

- New gene: `OBJ-092`, finish required Horseshoe Overlook missions and establish
  Clemens Point through `A Strange Kindness`.
- Success, evaluation and failure: the camp transition is scoped success;
  mission-local failure restores an eligible checkpoint rather than ending the
  save, while free-roam death/arrest follows Story Mode recovery outside the
  success predicate.
- Claim IDs: `RDR2-002`, `RDR2-010`.

### Time Genes

- Existing gene: `TIM-003`, traversal, combat, witnesses, law, wildlife, horse
  resources and mission events continue in real time while ordinary input is
  open; Dead Eye changes rate through `SYS-479`, not the scheduling gene.
- Claim IDs: `RDR2-003`–`RDR2-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| `Eastward Bound` has settled and Arthur stands at Horseshoe Overlook | Take direct control and inspect the map | Chapter 2 free roam and currently legal yellow mission markers are available | Explicit entry and authored gate state | `RDR2-002`, `RDR2-010` |
| Current saddled horse is alive and in whistle range | Call, mount and ride at a chosen gait | The same horse approaches; steering drains its outer stamina while saddle cargo remains attached | Horse is persistent state, not a vehicle skin | `RDR2-003` |
| Current horse is below the next bond threshold | Feed, groom, calm, lead or ride it | Eligible care adds bond progress; a reached level changes disclosed horse capabilities | Care modifies later traversal choices | `RDR2-003` |
| Arthur's stamina bar is low while its core remains positive | Stop exertion or consume a compatible provision | Outer stamina refills at the core-conditioned rate; food may replenish or fortify the paired states | Core and bar are distinct coupled resources | `RDR2-004` |
| A dirty owned firearm and gun oil are available | Inspect and clean the firearm | One oil is consumed and condition/performance returns toward its legal maximum | Maintenance trades inventory for combat quality | `RDR2-005` |
| An identifiable civilian witnesses an ordinary offence | Pursue and choose threaten or calm | The witness may stop; failure lets the agent report and starts law investigation | Report is a preventable live transition | `RDR2-006` |
| Arthur is identified and lawmen actively search | Leave the marked area and remain unseen | Active wanted search clears, but the regional monetary bounty remains | Immediate evasion and persistent legal debt differ | `RDR2-006` |
| A regional bounty persists without active pursuit | Pay it at an eligible post office or surrender legally | Money or arrest settlement clears the jurisdictional bounty | Bounty is a spendable persistent consequence | `RDR2-006` |
| Dead Eye bar is available during a Chapter 2 firefight | Activate Dead Eye, mark legal targets and commit fire | Live action slows, the meter drains and shots resolve in mark order | Time-rate control is a resource-backed combat action | `RDR2-009` |
| `Money Lending and Other Sins` unlocks the camp ledger | Donate value, then buy an eligible restock or upgrade | Personal value enters shared camp state; spending shared funds changes supplies or service state | Camp economy is shared and prerequisite-gated | `RDR2-008` |
| A hunt produces a compatible rabbit carcass | Skin and harvest it | Carcass state resolves into carried meat/pelt yield that can be cooked, sold or donated | Hunting connects combat precision to camp resources | `RDR2-003`, `RDR2-008` |
| An active mission's protected actor dies or Arthur leaves its allowed area | Accept checkpoint retry | The authored checkpoint restores required actors, assets and objective state | Mission failure rewinds a bounded script state | `RDR2-010` |
| Required Chapter 2 predecessor missions are complete | Start and finish `A Strange Kindness` | Arthur and Charles find the next site, rescue the settlers and the gang moves to Clemens Point | Explicit chapter success boundary | `RDR2-002`, `RDR2-010` |

## Strategic and experiential structure

- Local decision: choose horse or foot approach, pace, cover, weapon, Dead Eye
  timing, maintenance, social response and whether a witnessed action is worth
  the legal and honour consequence.
- Medium-term planning: keep Arthur and horse cores usable, bond the current
  mount, retain ammunition/oil, carry the right long gun from the saddle,
  convert hunts and loot into personal or shared camp value and order currently
  available story missions.
- Long-term structure: the Chapter 2 mission graph introduces stable, hunting,
  ledger and manual Dead Eye capabilities, while escalating gang exposure until
  `A Strange Kindness` replaces Horseshoe Overlook with Clemens Point.
- Common heuristics: ride at a sustainable gait; retrieve long guns before
  leaving the horse; clean a visibly degraded firearm before a major shootout;
  stop a lone witness before creating more; flee sight before hiding; donate
  only after preserving personal supplies; defer optional content before the
  chapter-ending marker.
- Failure attribution: cores, meters, condition bars, horse bond/cargo, witness
  and wanted markers, bounty, honour feedback, mission prompts and checkpoint
  reasons expose most immediate causes; witness compliance, law approach and
  wildlife behaviour retain bounded uncertainty.
- Player-trust factors: contextual prompts and explicit state displays make
  causal trade-offs readable, but mission-area restrictions and partially
  hidden social outcomes can narrow apparent open-world freedom.
- Claim IDs: `RDR2-002`–`RDR2-010`.

## Replay and variation

- What changes between sessions: mission order within legal branches, route,
  horse and bond, weather/traffic/wildlife encounters, combat execution,
  witness outcomes, bounty/honour, purchases, camp donations and upgrades.
- Randomness or procedural generation: terrain, camp sites and mission graph
  are authored; ambient agents, wildlife, local encounters and some yields vary.
- Multiple viable strategies: mounted or on-foot travel, stealth or direct
  combat, free aim or Dead Eye, personal economy or camp investment and several
  legal mission orders reach the same chapter transition.
- Typical replay motive: test another honour tendency, horse, mission order,
  camp investment or combat approach; later chapters and alternate ending
  consequences remain outside this packet.
- Claim IDs: `RDR2-002`–`RDR2-010`.

## Adjacent systems and history

- Grand Theft Auto V shares authored open-world missions, aiming, cover,
  firearms, wagons/vehicles, wanted search, map guidance and checkpoint retry,
  but its wanted state lacks RDR2's preventable witness phase and retained
  regional bounty, and it has no cared-for persistent saddle inventory.
- Monster Hunter Wilds shares live hunting, mounted traversal, harvesting and
  equipment maintenance, but its target-routed Seikret, finite quest faints and
  material forging do not form a social law, honour or shared camp ledger.
- Elden Ring shares direct mounted combat and resource-bound live combat, but
  Torrent is resummonable and does not retain bond, care or saddle cargo.
- Important differences: the scoped RDR2 loop joins authored missions to one
  simulated social/legal chain and makes horse, weapon, body and camp
  maintenance persist across free-roam transitions.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-130`, `ACT-131`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-201`, `ACT-226`, `ACT-227`, `ACT-245`, `ACT-271`–`ACT-274` | bindings and content identities are parameters |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-222`, `SYS-251`, `SYS-320`, `SYS-366`, `SYS-369`, `SYS-471`–`SYS-480` | exact balance, rates, values and mission scripts are parameters |
| Constraint | `CON-269`, `CON-282`, `CON-285`, `CON-288`, `CON-328`, `CON-330`, `CON-331`, `CON-405`–`CON-409` | capacities, thresholds and prices are parameters |
| Information | `INF-073`, `INF-115`, `INF-117`, `INF-119`, `INF-125`, `INF-144`, `INF-181`–`INF-183` | exact HUD geometry and icon style are presentation |
| Objective | `OBJ-092` | required mission identities and final camp are scoped parameters |
| Time | `TIM-003` | world rate and Dead Eye scale are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `164` (`GAME-0001`–`GAME-0164`).
- Exact genome matches: none.
- Tied near matches: `GAME-0145` — Grand Theft Auto V (`28 / 74 = 0.378378`).
- Supported combination subsets: `COMB-0163`.
- Scan date: 2026-08-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0145` — Grand Theft Auto V | `ACT-008`, `ACT-130`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-201`, `ACT-226`, `ACT-227`, `SYS-208`, `SYS-215`, `SYS-222`, `SYS-320`, `SYS-366`, `SYS-369`, `CON-269`, `CON-282`, `CON-285`, `CON-288`, `CON-328`, `CON-330`, `CON-331`, `INF-073`, `INF-115`, `INF-117`, `INF-119`, `INF-125`, `INF-144`, `TIM-003` | GTA V switches among three protagonists and resolves planned heists inside a modern urban wanted system. This unit instead persists one cared-for horse and saddle cargo, two-layer cores and meters, firearm condition, a pre-report witness window, regional bounty and honour, and a shared camp ledger before a required chapter transition. | Near, `0.378378` |

### Preserved research notes

- New genes: `ACT-271`–`ACT-274`, `SYS-471`–`SYS-480`, `CON-405`–`CON-409`,
  `INF-181`–`INF-183` and `OBJ-092`.
- Classification result: `New gene` and new combination of known and new genes.
- Evidence and reasoning: the distinctive boundary is the coupling of one
  persistent cared-for horse and saddle inventory to core maintenance,
  degradable firearms, preventable witness reports, retained regional bounty,
  honour, shared camp investment and authored chapter gates.

## Combination assessment

- `COMB-0163` is a strict subset isolating the mounted maintained outlaw loop
  through the complete Chapter 2 camp transition.
- No earlier registered combination has the same gene set; independent
  recurrence is unassessed.

## Taxonomy impact

- Registry changes: add 23 bounded genes and `COMB-0163`; reuse 31 established
  records at their existing causal boundaries.
- Taxonomy-change record: none.
- Candidate terms affected: horse breed, gait, exact bond level, core rate,
  weapon values, bounty amount, honour delta, ledger price, mission identity
  and Dead Eye duration remain parameters.

## Negative results

- No separate negative-result record. The review rejected horse riding as a
  road vehicle, witness reporting as instant wanted escalation, regional bounty
  as the active search timer, gun cleaning as generic reload and camp donations
  as fixed-slot collection completion.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] The scoped chapter joins one persistent
  horse, paired cores, maintained firearms, witnesses, bounty, honour and camp
  resources to an authored camp-to-camp mission route (`RDR2-002`–`RDR2-010`).

## Нові гени

- [Observation | Corroborated | High] Twenty-three bounded genes isolate horse
  state, cores, firearm condition, witness/bounty/honour transitions, shared
  camp resources, Dead Eye, carcass yield and the Chapter 2 objective.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0163` — mounted maintained outlaw
  chapter through the Horseshoe Overlook-to-Clemens Point transition.

## Зміни таксономії

- [Observation | Direct | High] Змін таксономії немає.

## Family classification

- `FAM-009` — Tactical forecast and counterplay: cover, weapon condition, Dead
  Eye, horse position and local law cues shape committed responses.
- `FAM-010` — Real-time system pressure: people, wildlife, horse resources,
  witnesses, law and combat continue while Arthur acts.
- `FAM-013` — Inventory and fixture dependencies: oil, ammunition, saddle cargo,
  donations and ledger funds gate maintenance and camp services.
- `FAM-017` — Ordered dependency sequencing: authored Chapter 2 predecessors
  unlock its systems and final camp transition.
- No new family is created from one game.

## Plain-language interpretation

Red Dead Redemption 2 makes travel a maintained relationship. Arthur's horse
keeps its own cores, bond and saddle cargo, so feeding, calming and riding it
change later handling and determine which long guns or carcasses are available
away from camp. Arthur's health, stamina and Dead Eye similarly depend on a
slower core beneath the recoverable outer bar. Firearms also remember dirt and
use; cleaning consumes oil to recover performance.

The open world responds before the police arrive. A witness may run to report
an offence, giving Arthur a short contextual choice to calm, threaten or pursue
them. A successful report becomes active wanted search and, after
identification, a regional bounty that survives escape until payment or
surrender. Honour records a different long-term consequence. At Horseshoe
Overlook, personal value can instead become shared supplies and ledger upgrades.
These persistent states travel between required missions until `A Strange
Kindness` moves the gang to Clemens Point.

## New questions

- Which later open-world game reuses both a preventable witness-report phase
  and a persistent cared-for mount without RDR2's authored camp economy?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0166` — Sid Meier's Civilization VI.
- Optimisation criterion: continue the recorded demand-led horizon in exact order.
- Expected information gain: contrast one embodied real-time authored chapter
  with turn-based empire planning, technology/civic trees and multiple victories.
- Backlog impact: fourth of nine authorised game units; it is not started here.

## Чому саме вона

- [Hypothesis | Limited | High] Civilization VI is the next immutable subject
  in `SEARCH_DEMAND_GAME_SELECTION_004` and should maximise structural distance
  from the mounted real-time social/legal loop.

## Localisation status

- Ukrainian game, new-gene and combination entries are reviewed in this unit.
- The canonical title remains `Red Dead Redemption 2`; the Ukrainian interface
  appends the established translation «Червоне мертве спокутування 2».

## Open questions

- A later direct-play review should record one clean Chapter 2 save and verify
  exact optional mission deferrals, witness compliance and simultaneous
  horse/mission-failure edge cases.

## Source notes

- Official product, store, companion, guide and support materials were checked
  on 2026-08-27. Maintained secondary references fill mission-order and
  transition details the public publisher pages do not enumerate.
- Red Dead Online and edition-bonus facts were excluded even when a source
  discusses them alongside Story Mode.

## Next recommended action

- Integrate `GAME-0166` — Sid Meier's Civilization VI after the required
  thirty-second stop window.
