---
game_id: GAME-0145
slug: grand-theft-auto-v
game_title: Grand Theft Auto V
analysis_status: reviewed
reviewed: 2026-08-21
combination_ids:
  - COMB-0143
gene_ids:
  action:
    - ACT-008
    - ACT-130
    - ACT-140
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-184
    - ACT-201
    - ACT-226
    - ACT-227
    - ACT-228
    - ACT-229
    - ACT-230
  system:
    - SYS-208
    - SYS-215
    - SYS-222
    - SYS-292
    - SYS-320
    - SYS-342
    - SYS-365
    - SYS-366
    - SYS-367
    - SYS-368
    - SYS-369
    - SYS-370
    - SYS-371
  constraint:
    - CON-136
    - CON-188
    - CON-269
    - CON-282
    - CON-285
    - CON-288
    - CON-326
    - CON-327
    - CON-328
    - CON-329
    - CON-330
    - CON-331
  information:
    - INF-073
    - INF-115
    - INF-117
    - INF-119
    - INF-125
    - INF-144
    - INF-145
    - INF-146
  objective:
    - OBJ-077
  time:
    - TIM-003
---

# Game: Grand Theft Auto V

## Analysis scope

- Version / ruleset: PC Enhanced at public Title Update `1.73`, reviewed
  2026-08-21; one fresh Story Mode save from Prologue through the first
  completion of `The Third Way` after `The Big Score`.
- Included: authored critical-path missions and setup gates; third-person and
  first-person movement; aiming, firearms, explosives and contextual cover;
  vehicle entry and direct road, water and air control; ambient traffic and
  civilians; crime reporting, one-to-five-star wanted pursuit and evasion;
  map waypoints and GPS; Michael, Franklin and Trevor control switching;
  character-specific special abilities and activity-developed statistics;
  Story Mode money, weapon, ammunition and armour purchases; mission failure
  and checkpoint retry; major-heist approach and specialist selection,
  execution, loss, improvement, cut and payout; terminal option C.
- Reproducible checkpoint: from a clean save complete the required mission graph
  to unlock all three protagonists; place and follow a personal waypoint, enter
  and damage a road vehicle, trigger and then clear an ordinary wanted level by
  leaving police sight, switch to every currently available protagonist and use
  each special ability in its compatible context. For one major heist, record
  the planning board before and after approach and complete-role selection,
  finish its setup and execution, and compare the displayed take with crew cuts.
  Separately violate one declared mission condition, retry its latest checkpoint,
  finish The Big Score and commit option C through The Third Way.
- Excluded: GTA Online and its economy, progression, businesses, heists,
  anti-cheat and updates; Director Mode and Rockstar Editor; mods, cheats and
  speedrun skips; optional Strangers and Freaks, random events, properties,
  stock-market optimisation, sports, hobbies, collectibles and 100% completion;
  post-story free roam, alternate endings as the first persistent branch,
  mission replay medals, achievements, cosmetics and exhaustive vehicles,
  weapons, radio, dialogue or scripted set pieces.
- Direct-play status: no complete fresh paid-account campaign was conducted.
  Rockstar's current 1.73 notes, Enhanced product material, official gameplay
  and PC-control guidance establish the version and control boundary; creator
  previews plus maintained mission, wanted and heist references corroborate the
  full scoped route. Exact balance and mission-script values remain parameters.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `GTA-001` | Title Update 1.73 is the current reviewed PC Enhanced baseline, and Story Mode remains a distinct migratable single-player save | Confirmed | Corroborated | High | P1, P2, P3 |
| `GTA-002` | The critical path combines direct on-foot combat, contextual cover and player-operated land, water and air vehicles inside one continuous authored world | Confirmed | Corroborated | High | P3, P4, P5, S1 |
| `GTA-003` | Witnessed or reported crime escalates wanted stars into matching police pressure; leaving police sight enters a timed search whose reacquisition resumes pursuit | Observation | Corroborated | High | P6, S2, S6 |
| `GTA-004` | Michael, Franklin and Trevor retain separate location, money, statistics and special abilities, and legal switching transfers control into the selected character's current activity | Confirmed | Corroborated | High | P4, P5, S1 |
| `GTA-005` | Each protagonist spends and restores a distinct temporary special meter, while matching performed activities improve persistent personal statistics | Observation | Corroborated | High | P4, P6, S1 |
| `GTA-006` | Required missions and setups form authored prerequisite gates; death, arrest or loss of a declared critical actor, asset or area fails the current attempt and permits checkpoint retry | Observation | Corroborated | High | S3, S5, S7 |
| `GTA-007` | Major heists bind one approach to required specialist roles; crew skill and cut affect mistakes, retained haul, survival, later improvement and protagonist payout | Confirmed | Corroborated | High | P5, S4, S8 |
| `GTA-008` | The Big Score exposes three mutually exclusive terminal options whose completed branch persists protagonist survival and Story Mode completion; this scope selects The Third Way | Confirmed | Corroborated | High | P3, S3, S5 |
| `GTA-009` | Map, minimap, HUD, character wheel and heist board disclose route, wanted state, character readiness and plan trade-offs without revealing exact future traffic, pursuit or crew mistakes | Observation | Corroborated | High | P4, P6, S2, S4 |

## Basic data

- Release / origin: Rockstar North, published by Rockstar Games; original
  release 2013, PC release 2015, PC Enhanced release 2025; reviewed at Title
  Update 1.73 on 2026-08-21.
- Platform or physical form: authored single-player open-world action game;
  PC Enhanced Story Mode is scoped.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  agent routing and coordination; ordered dependency sequencing.
- Primary sources:
  - **[P1]** [Rockstar Title Update 1.73 notes](https://support.rockstargames.com/articles/4vRqEDvjUs9h7nqRUgc8YO/gtav-title-update-1-73-notes-ps5-ps4-xbox-series-x-or-s-xbox-one-pc-enhanced-legacy),
    for the current PC Enhanced/Legacy title-update boundary.
  - **[P2]** [Rockstar PC Enhanced release](https://www.rockstargames.com/intl/newswire/article/7551a7k917554a/free-upgrade-for-grand-theft-auto-v-on-pc-now-available),
    for the 2025 Enhanced release and distinct Story Mode migration.
  - **[P3]** [official Grand Theft Auto V page](https://www.rockstargames.com/gta-v),
    for the three protagonists, dangerous heists and current Story Mode product.
  - **[P4]** [official gameplay video](https://www.rockstargames.com/newswire/article/k49a58878oo552/grand-theft-auto-v-official-gameplay-video.html),
    for open-world traversal, combat, driving, character switching, statistics,
    special abilities and mission structure.
  - **[P5]** [Rockstar worldwide preview digest](https://www.rockstargames.com/newswire/article/o349k552514927/worldwide-grand-theft-auto-v-previews.html),
    for continuous character switching and skill/cut-sensitive heist crews.
  - **[P6]** [Rockstar PC controls and settings tips](https://www.rockstargames.com/newswire/article/51974aa3a724o2/rockstar-game-tips-tailoring-your-settings-and-controls-in),
    for map waypoints, vehicle controls, character skills and special input.
- Secondary sources:
  - **[S1]** [Grand Theft Auto V overview](https://en.wikipedia.org/wiki/Grand_Theft_Auto_V),
    for first/third-person control, critical-path shooting/driving, individual
    character skills and surviving crew improvement.
  - **[S2]** [GTA Wiki wanted-level mechanics](https://gta.fandom.com/wiki/Wanted_Level_in_GTA_V),
    for civilian reports, search cones, perception loss and severity timing.
  - **[S3]** [current Story Mode mission list](https://gtaintel.com/news/gta-5-all-story-missions-in-order),
    for critical-path and heist-setup ordering through the final choice.
  - **[S4]** [current Story Mode heist crew guide](https://gtaintel.com/news/gta-5-heists-complete-crew-guide),
    for approach, specialist, skill, cut, mistake, survival and improvement.
  - **[S5]** [The Third Way record](https://gta.fandom.com/wiki/The_Third_Way),
    for option C, its prerequisites, failure conditions and Story Complete state.
  - **[S6]** [Rockstar Race Creator guide](https://media.rockstargames.com/rockstargames/img/global/news/upload/GTAO_Race_Creator_Guide.pdf),
    for engine-level traffic and wanted-pursuit toggles shared with the base world.
  - **[S7]** [Grand Theft Wiki mission record](https://www.grandtheftwiki.com/The_Third_Way),
    for the bounded final mission and three-option branch.
  - **[S8]** [Story Mode heist guide](https://www.gtaboom.com/gta-5-heists-guide-story-mode-8cd4/),
    for the five heists and plan-to-payout consequences.
- Claim IDs: `GTA-001`–`GTA-009`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, navigate the controlled protagonist; `ACT-130`,
  purchase offered Story Mode equipment; `ACT-140`, commit terminal option C;
  `ACT-161`, aim and attack; `ACT-164`, choose an active weapon; `ACT-183`,
  reload; `ACT-184`, throw a carried explosive; `ACT-201`, enter, steal and
  directly operate a world vehicle.
- New genes: `ACT-226`, attach to contextual cover; `ACT-227`, set a personal
  waypoint; `ACT-228`, switch direct control among available protagonists;
  `ACT-229`, activate the current protagonist's special ability; `ACT-230`,
  configure a heist approach and specialist roster.
- Parameters: control binding, camera perspective, weapon/vehicle model,
  waypoint position, protagonist, special duration, approach and crew identity.
- Claim IDs: `GTA-002`–`GTA-009`.

### System Behaviour Genes

- Existing genes: `SYS-208`, resolve aimed fire through cover and body region;
  `SYS-215`, resolve live hostile combat; `SYS-222`, collect eligible world
  pickup on contact; `SYS-292`, resolve thrown explosives; `SYS-320`, simulate
  directly operated vehicle motion and damage; `SYS-342`, improve statistics
  through matching activity.
- New genes: `SYS-365`, simulate ambient traffic and reactive civilians;
  `SYS-366`, escalate and clear wanted pursuit; `SYS-367`, preserve concurrent
  protagonists through control transfer; `SYS-368`, drain and restore the
  character-specific special meter; `SYS-369`, restore a mission checkpoint
  after failure; `SYS-370`, resolve heist plan and crew proficiency into take;
  `SYS-371`, resolve the terminal branch into persistent roster state.
- Resolution order: the shared world advances traffic, civilians and threats;
  direct movement, combat or vehicle input resolves; eligible crime changes the
  wanted state; protagonist control may transfer without resetting the world;
  mission scripts test objectives and failure; major-heist plans determine
  setups, execution and payout; the completed final option fixes Story Mode's
  terminal roster and completion state.
- Claim IDs: `GTA-002`–`GTA-008`.

### Constraint Genes

- Existing genes: `CON-136`, persistent prerequisites gate mechanisms and
  missions; `CON-188`, the final offer permits one persistent option;
  `CON-269`, special use requires compatible context, meter and readiness;
  `CON-282`, main missions obey ordered authored gates; `CON-285`, weapon use
  requires compatible live ammunition state; `CON-288`, vehicle control
  requires a viable seat, operating state and geometry.
- New genes: `CON-326`, cover requires reachable protective geometry;
  `CON-327`, character switching requires current authored availability;
  `CON-328`, wanted clearance requires an uninterrupted unseen search interval;
  `CON-329`, heist plans require a legal approach and complete specialist roles;
  `CON-330`, mission-critical actors, assets and area must remain viable;
  `CON-331`, weapon classes and ammunition have fixed carried capacity.
- Scarce strategic resources: health, armour and ammunition; usable vehicles
  and safe cover; wanted-search time and concealment; special meter; mission
  checkpoint progress; specialist competence against percentage cut; retained
  heist take and terminal protagonist availability.
- Claim IDs: `GTA-002`–`GTA-009`.

### Information Genes

- Existing genes: `INF-073`, active weapon and ammunition are visible;
  `INF-115`, local sight and sound expose only partial hostile state; `INF-117`,
  personal money, prices and purchase state are visible; `INF-119`, health,
  armour, special meter and statistics are visible; `INF-125`, the explored map
  and current authored mission gates are visible.
- New genes: `INF-144`, map and minimap expose GPS and wanted-search state;
  `INF-145`, the character wheel exposes protagonist availability and context;
  `INF-146`, the heist board exposes approaches, roles, crew skill and cuts.
- Claim IDs: `GTA-003`–`GTA-009`.

### Objective Genes

- New gene: `OBJ-077`, complete every required critical-path mission through
  The Big Score, commit option C and finish The Third Way so the save records
  Story Complete.
- Success, evaluation and failure: local mission objectives and constraints
  gate each checkpoint; failure retries the current mission rather than ending
  the save; only completed terminal option C satisfies the scoped objective.
- Claim IDs: `GTA-006`, `GTA-008`.

### Time Genes

- Existing gene: `TIM-003`, traffic, civilians, enemies, vehicles, wanted
  pursuit and mission timers advance in real time while player input continues;
  pausing single-player play is a rate-control parameter.
- Claim IDs: `GTA-002`–`GTA-006`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Known destination has no personal route | Set its map waypoint | GPS draws and recalculates a road path while direct driving remains with the player | Navigation advice is information, not autonomous travel | `GTA-002`, `GTA-009` |
| Available vehicle has a reachable seat | Enter and accelerate through traffic | Driver authority transfers; handling, collision and damage resolve continuously | Vehicles are direct world tools inside the same simulation | `GTA-002` |
| Eligible crime is observed with no current wanted stars | Commit it, then break police sight | Stars summon pursuit; unseen evasion changes stars to search and clears them after its interval | Wanted pressure is perception- and time-dependent | `GTA-003` |
| Two protagonists are unlocked and switching is legal | Select the other character | World time advances through the transition and control arrives in that character's retained activity | The trio is concurrent authored state, not three save slots | `GTA-004` |
| Franklin has special meter while driving | Activate driving focus, then exhaust it | Meter drains while handling and time are modified, then ordinary driving resumes and recharge can begin | Special identity is a bounded spendable resource | `GTA-005` |
| Current mission protects an ally or vehicle | Let the protected state fail and choose checkpoint retry | Attempt ends; authored checkpoint actors, assets and objective state are restored | Mission failure rewinds bounded script state | `GTA-006` |
| Heist board exposes at least two legal approaches and role candidates | Commit one approach and fill every role | Setup branch and execution roster lock; skill and cuts later change mistakes and net take | Planning decisions propagate into action and economy | `GTA-007` |
| The Big Score is complete and all final options are offered | Commit option C and complete The Third Way | Its authored mission runs; all three protagonists survive and Story Complete persists | One exclusive choice fixes the terminal roster state | `GTA-008` |

## Strategic and experiential structure

- Local decision: choose on-foot or vehicle route, cover edge, weapon and shot;
  read nearby traffic, civilians and police; decide whether to fight, flee,
  switch characters or spend a special meter.
- Medium-term planning: preserve ammunition and armour, improve matching
  character statistics, sequence mission prerequisites and setups, and choose
  heist approach and specialists by competence-versus-cut trade-off.
- Long-term structure: the authored mission graph unlocks protagonists,
  locations, equipment and heists; successful crew may improve for later work;
  final option C converts the accumulated trio into the scoped surviving roster.
- Common heuristics: set a waypoint but deviate when traffic or police block it;
  leave sight before hiding; use cover in firearm encounters; use each special
  in its matching context; pay more for reliable specialists when lost take
  exceeds saved cut; keep all protagonists available by choosing option C.
- Failure attribution: HUD, wanted stars, search cones, mission prompts, explicit
  failure reasons, checkpoint boundary and heist-board trade-offs explain most
  immediate loss; concealed traffic, police approach and crew mistakes preserve
  bounded uncertainty.
- Player-trust factors: checkpoints reduce repetition, but authored mission-area
  restrictions and undisclosed future crew errors can narrow apparent freedom.
- Claim IDs: `GTA-002`–`GTA-009`.

## Replay and variation

- What changes between sessions: route and vehicle choice, traffic and civilian
  encounters, pursuit path, combat execution, character statistics, purchases,
  heist approaches and specialists, net take and final branch.
- Randomness or procedural generation: Los Santos, Blaine County and critical
  mission graph are authored; ambient agents, traffic, some pickups and combat
  resolution vary without generating a new campaign map.
- Multiple viable strategies: direct assault or safer cover use, road or
  off-road escape, character-specific special timing, lower-cut developing crew
  or expensive reliable crew and authored heist approaches.
- Typical replay motive: test alternate heist plans, improve mission execution,
  compare payouts and experience the two excluded terminal branches through
  replay or another save.
- Claim IDs: `GTA-002`–`GTA-009`.

## Adjacent systems and history

- Counter-Strike 2 is the mathematical near match because both share aimed
  firearm combat, cover/body-hit resolution, weapon selection, reloads,
  explosives, ammunition gates, personal purchase information, partial hostile
  perception and live timing. GTA V replaces one-life team rounds and bomb
  economy with a continuous authored world, vehicles, wanted pursuit, three
  protagonists, checkpoints and campaign heists.
- PUBG: BATTLEGROUNDS shares direct traversal, combat, world pickups, vehicles,
  equipment state and one continuous real-time space, but its stochastic
  insertion and shrinking one-life arena remove persistent protagonists,
  authored mission gates and specialist-planned heists.
- Palworld shares an explored mission-gated world and persistent controlled
  character state, but its capture and autonomous companion/base labour differ
  from GTA V's authored trio, law response and role-planned criminal operations.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-130`, `ACT-140`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-201`, `ACT-226`–`ACT-230` | bindings, camera and content identities are parameters |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-222`, `SYS-292`, `SYS-320`, `SYS-342`, `SYS-365`–`SYS-371` | balance, traffic density and script values are parameters |
| Constraint | `CON-136`, `CON-188`, `CON-269`, `CON-282`, `CON-285`, `CON-288`, `CON-326`–`CON-331` | exact caps, gates and search duration are parameters |
| Information | `INF-073`, `INF-115`, `INF-117`, `INF-119`, `INF-125`, `INF-144`–`INF-146` | camera and HUD styling are presentation |
| Objective | `OBJ-077` | option C is the scoped terminal parameter |
| Time | `TIM-003` | pause and mission-specific clocks are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `144` (`GAME-0001`–`GAME-0144`).
- Exact genome matches: none.
- Tied near matches: `GAME-0137` — Counter-Strike 2 (`14 / 64 = 0.218750`).
- Supported combination subsets: `COMB-0143`.
- Scan date: 2026-08-21.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0137`.

### Preserved research notes

- New genes: `ACT-226`–`ACT-230`, `SYS-365`–`SYS-371`,
  `CON-326`–`CON-331`, `INF-144`–`INF-146`, `OBJ-077`.
- Classification result: new verified combination of reused and new genes.
- Evidence and reasoning: the distinctive boundary is the coupling of direct
  open-world action and police evasion to three persistent authored
  protagonists, then converting specialist planning into a multi-role heist and
  the terminal branch into retained roster state.

## Taxonomy impact

- Registry changes: 22 new bounded genes and `COMB-0143`; `ACT-130`, `ACT-140`,
  `ACT-201`, `SYS-320`, `SYS-342`, `CON-188`, `CON-282`, `CON-288`, `INF-117`,
  `INF-119` and `INF-125` gain a campaign example. `SYS-320`, `SYS-342`,
  `CON-282` and `CON-288` are broadened only across previously listed
  parameters; their type, lifecycle and causal boundary do not change.
- Taxonomy-change record: none.
- Candidate terms affected: none.

## Negative results

- No separate negative-result record. The exhaustive scan found no exact
  genome and no earlier registered combination that is a proper subset.
