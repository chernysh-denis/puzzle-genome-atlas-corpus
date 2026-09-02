---
game_id: GAME-0220
slug: battlefield-v
game_title: Battlefield V
analysis_status: reviewed
reviewed: 2026-09-01
combination_ids:
  - COMB-0147
  - COMB-0218
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-184
    - ACT-187
    - ACT-190
    - ACT-199
    - ACT-200
    - ACT-201
    - ACT-215
    - ACT-240
    - ACT-241
    - ACT-388
    - ACT-389
  system:
    - SYS-208
    - SYS-215
    - SYS-292
    - SYS-320
    - SYS-380
    - SYS-382
    - SYS-386
    - SYS-394
    - SYS-395
    - SYS-396
    - SYS-713
    - SYS-714
    - SYS-715
  constraint:
    - CON-262
    - CON-269
    - CON-272
    - CON-286
    - CON-288
    - CON-346
    - CON-347
    - CON-348
    - CON-560
    - CON-561
  information:
    - INF-073
    - INF-115
    - INF-116
    - INF-119
    - INF-155
    - INF-274
    - INF-275
  objective:
    - OBJ-079
  time:
    - TIM-003
---

# Game: Battlefield V

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current official Windows Steam public client, app
  `1238810`, public build `15984572`, checked 2026-09-01. The gameplay boundary
  retains DICE Update `7.3` and uses EA anticheat, introduced for Battlefield V
  on PC in April 2024. One ordinary official 64-player-cap Conquest round on
  Arras is admitted; Community Games and every custom modifier are excluded.
- Reproducible match parameters: Windows/Steam; Arras; Conquest; British Allied
  side; base Field Medic Combat Role for every controlled infantry life; one
  currently legal unmodified Medic SMG and the standard Medical Pouch and Smoke
  Grenade Launcher. If matchmaking assigns the German side, another ordinary
  Arras Conquest round is joined before the bounded attempt begins. Human team,
  squad and vehicle availability are sampled rather than fixed.
- Primary decision loop: inspect tickets, six flags, squad, deployment sources,
  health, ammunition and nearby fortification outlines; deploy; move, aim,
  fire, reload, throw smoke or explosives and communicate; heal or revive an
  eligible ally; replenish scarce health and ammunition; build an eligible
  trench, sandbag, barrier or supply station; enter an available vehicle when
  useful; capture, contest, defend or rotate among A–F; when squad-leader
  authority and points permit, call one legal reinforcement; after death,
  select a safe legal source and redeploy.
- Entry and terminal: begins at the first deployment surface of a fresh
  ordinary Arras Conquest round with the British side and Field Medic fixed.
  The round succeeds when the opposing reinforcement-ticket pool reaches zero
  first and fails when the British pool reaches zero first. A server-declared
  ordinary round result is authoritative if a built-in round-time guard settles
  the match; leaving, a personal score, a weapon unlock or one captured flag is
  not terminal.
- Included: four-person squad play; British and German teams as opponent sides;
  the six Arras capture points; infantry movement and weapon handling; Medic
  gadgets, smoke, health and ammunition scarcity; self-bandage, team healing,
  squad and Medic revival; downing, bleedout, death and redeployment; point
  ownership, contest and ticket drain; authored Fortifications; destructible
  cover; available tanks, aircraft and seats; squad-point accumulation and one
  legal leader-called reinforcement; live partial information.
- Excluded: Firestorm, Grand Operations, Breakthrough, Frontlines, Domination,
  Team Deathmatch, Squad Conquest, Final Stand, Combined Arms, Practice Range
  and War Stories; Community Games, private servers and altered tickets, round
  time, damage, spawn timing, classes, vehicles, weapons, gadgets, HUD or
  friendly fire; maps other than Arras; other controlled classes and Combat
  Medic; Company, Specializations, assignments, Tides of War, cosmetics,
  account rewards, store and complete service history.
- Potential scoped modules: another map, class, faction, vehicle start,
  Community Game, Grand Operation day or Firestorm match requires a separate
  version, entry, rules packet and terminal.
- Direct-play status: no authenticated live match was played. Current official
  product, anti-cheat, class, Conquest, Arras, Fortification, attrition and
  squad-reinforcement documentation was combined with the public Steam build
  record into a repository-side transition trace. No video or audio was opened,
  played, heard or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BFV-001` | The current Windows/Steam boundary is app 1238810, public build 15984572, Update 7.3 gameplay plus the April 2024 EA-anticheat client | Confirmed | Corroborated | High | P1, P2, P3, P4 |
| `BFV-002` | Ordinary Conquest supports up to 64 players and turns majority flag control plus committed deaths into opposing ticket depletion | Confirmed | Direct | High | P5, P6 |
| `BFV-003` | Arras Conquest has six named points A–F and admits infantry, tanks, aircraft, destructible routes and Fortifications | Confirmed | Direct | High | P5 |
| `BFV-004` | Field Medic uses an SMG, Medical Pouch and Smoke Grenade Launcher and revives any teammate faster and to full health | Confirmed | Direct | High | P7 |
| `BFV-005` | A squadmate may revive a squadmate, while Medic has broader and stronger revive authority; an unrevived death enters the ticket and redeployment loop | Confirmed | Corroborated | High | P6, P7, P8 |
| `BFV-006` | Battlefield V limits carried health and ammunition, permits partial health regeneration and replenishes through compatible players, stations or enemy ammunition | Confirmed | Direct | High | P8, P9 |
| `BFV-007` | Every class can build authored Fortifications, while the resulting trenches, barriers and supply positions change cover, routes and sustain | Confirmed | Direct | High | P5, P8 |
| `BFV-008` | Squad cooperation earns shared points that the squad leader can spend on typed Reinforcements such as supply, smoke or a strike | Confirmed | Direct | High | P8 |
| `BFV-009` | Community Games can alter ticket, round, damage, spawn, class, vehicle, equipment and HUD rules and is therefore not interchangeable with this packet | Confirmed | Direct | High | P10 |
| `BFV-010` | The repository trace reproduces deployment, combat, scarcity, fortification, revival, capture, reinforcement and both team-ticket outcomes | Observation | Direct | High | V1 |

## Basic data

- Release / origin: DICE and Electronic Arts; released in 2018 and still
  distributed as Battlefield V Definitive Edition.
- Platform or physical form: networked Windows first-person shooter through
  Steam and the EA app; one current official multiplayer round.
- Puzzle family: real-time system pressure; spatial control and routing;
  cooperative role dependencies; resource transformation.
- Primary sources:
  - **[P1]** [official Steam page](https://store.steampowered.com/app/1238810/Battlefield_V/),
    for current title, Windows delivery, developer/publisher and Definitive
    Edition surface.
  - **[P2]** [official Update 7.3 notes](https://forums.ea.com/discussions/battlefield-v-en/battlefield-v---update-7-3/6703660),
    for the retained final gameplay-update boundary.
  - **[P3]** [official EA-anticheat notice](https://www.ea.com/games/battlefield/news/eaac-and-battlefield),
    for the April 2024 PC client transition.
  - **[P4]** [SteamDB app and public depot record](https://steamdb.info/app/1238810/depots/?branch=eacc),
    checked 2026-09-01 only for public build `15984572` because EA exposes no
    separate current executable build number.
  - **[P5]** [official Arras guide](https://www.ea.com/games/battlefield/news/battlefield-5-arras-map),
    for the six points, 64-player-cap Conquest, combined arms, destructible
    routes and map-specific Fortifications.
  - **[P6]** [official Conquest explanation](https://www.ea.com/games/battlefield/news/chapter-2-lightning-strikes-faq-all-you-need-to-know),
    for majority point control, kills, ticket drain and zero-ticket loss.
  - **[P7]** [official Medic guide](https://www.ea.com/games/battlefield/news/battlefield-5-medic-class-and-combat-roles),
    for Field Medic, SMG, Medical Pouch, Smoke Grenade Launcher and revive authority.
  - **[P8]** [official gameplay deep dive](https://www.ea.com/games/battlefield/news/battlefield-5-deep-dive-gameplay-changes-and-additions),
    for squad assignment, revival, Fortifications, attrition and squad Reinforcements.
  - **[P9]** [official attrition tips](https://www.ea.com/games/battlefield/news/tides-of-war-chapter-1-overture-week-1-tips),
    for one carried bandage, finite resupply and Fortification sustain.
  - **[P10]** [official Community Games rules](https://www.ea.com/en-gb/games/battlefield/news/fall-update),
    for the configurable values explicitly excluded here.
- Reproducible control:
  - **[V1]** repository-side state trace derived from `P1`–`P10`; rules
    reasoning rather than a claim of direct play.
- Claim IDs: `BFV-001`–`BFV-010`.

## Mechanical decomposition

### Action Genes

- Existing: `ACT-008`, move and change stance; `ACT-161`, aim and attack;
  `ACT-164`, switch weapon or gadget; `ACT-183`, reload; `ACT-184`, throw a
  grenade; `ACT-187`, communicate or ping; `ACT-190`, use the Medical Pouch or
  Smoke Grenade Launcher; `ACT-199`, recover compatible ammunition; `ACT-200`,
  apply the carried bandage; `ACT-201`, enter and operate a vehicle; `ACT-215`,
  keep a compatible Field Medic loadout; `ACT-240`, choose a legal deployment
  source; `ACT-241`, revive one eligible downed ally.
- New `ACT-388`: use the toolbox at one authored outline to build or repair a
  legal Fortification or supply station.
- New `ACT-389`: as eligible squad leader, select and call one affordable
  typed squad Reinforcement.
- Parameters: map, faction, role, weapon, gadget, bandage, deployment source,
  fortification outline, vehicle seat, reinforcement and communication channel.
- Claim IDs: `BFV-003`–`BFV-010`.

### System Behaviour Genes

- Existing: `SYS-208`, resolve aimed fire; `SYS-215`, live hostile combat;
  `SYS-292`, grenade trajectory/effect; `SYS-320`, vehicle motion and damage;
  `SYS-380`, typed Medic-gadget effect; `SYS-382`, timed return after death;
  `SYS-386`, destructible cover; `SYS-394`, downing, revival and ticketed
  death; `SYS-395`, occupancy, contest and point ownership; `SYS-396`, combine
  deaths and point control into ticket attrition and result.
- New `SYS-713`: progress an authored Fortification build into a persistent
  trench, barrier, emplacement or supply state that changes route, cover or
  replenishment until damaged or destroyed.
- New `SYS-714`: resolve bounded ammunition, one-bandage and partial-health
  attrition, then replenish only the compatible resource from a Medic, Support,
  station or eligible field source.
- New `SYS-715`: accumulate squad points from cooperative actions and spend
  them on the leader-selected Reinforcement's typed delivery and effect.
- Resolution order: live action changes health, ammunition, geometry,
  downed state and point occupancy; revive can prevent a committed death;
  fortification can change the next route or sustain source; squad actions add
  points and a legal call spends them; owned points and unrevived deaths drain
  tickets; zero tickets or the ordinary server result closes the round.
- Claim IDs: `BFV-002`–`BFV-010`.

### Constraint Genes

- Existing: `CON-262`, ammunition, magazine, gadget and grenade capacity;
  `CON-269`, gadget target and readiness; `CON-272`, no live body control while
  dead; `CON-286`, bandage use needs a legal damaged state and completed use;
  `CON-288`, vehicle seat and operating legality; `CON-346`, role-compatible
  equipment; `CON-347`, deployment needs elapsed time and a safe legal source;
  `CON-348`, capture requires friendly occupancy and halts under contest.
- New `CON-560`: Fortification work requires a visible authored outline,
  compatible toolbox interaction, reach and uninterrupted build progress.
- New `CON-561`: a squad Reinforcement requires squad-leader authority,
  sufficient shared points, an available typed option and a legal target.
- Scarce resources: team tickets, living allies, revive time, ammunition,
  bandage and gadget stock, safe supply, cover, vehicle availability, squad
  points, legal deployment sources and point ownership.
- Claim IDs: `BFV-002`–`BFV-010`.

### Information Genes

- Existing: `INF-073`, weapon/ammunition/gadget state; `INF-115`, partial
  opponents through local sight and sound; `INF-116`, squad, team, tickets,
  clock and point state; `INF-119`, personal health, role and readiness;
  `INF-155`, deployment map and legal sources.
- New `INF-274`: local outlines and material feedback expose available,
  building, completed, damaged and destroyed Fortification states.
- New `INF-275`: the squad interface exposes current shared points, leader
  authority, available Reinforcements, cost, target and delivery state.
- Claim IDs: `BFV-002`–`BFV-010`.

### Objective Genes

- Existing `OBJ-079`: deplete the opposing Conquest reinforcement pool before
  the allied pool reaches zero. A server-declared ordinary time settlement is
  a terminal parameter, not a second personal objective.
- Claim IDs: `BFV-002`, `BFV-010`.

### Time Genes

- Existing `TIM-003`: combat, capture, bleedout, revival, redeployment, build,
  replenishment, vehicle motion, reinforcement delivery and ticket drain
  advance while participants act.
- Claim IDs: `BFV-002`–`BFV-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh Arras Conquest deployment surface | Select British Field Medic and an eligible headquarters source | Soldier enters with the compatible Medic kit; sampled team/squad state remains live | exact entry and role boundary | `BFV-002`–`BFV-004` |
| Magazine is partly empty and reserve remains | Reload | Fire readiness pauses, then compatible reserve fills the magazine | ammunition is operational state | `BFV-006` |
| Health is below its recoverable cap and one bandage remains | Complete self-bandage | The carried bandage is spent and declared health is restored; later use needs resupply | one-life health sustain is bounded | `BFV-006` |
| Eligible teammate is downed and reachable | Complete Field Medic revive | Teammate returns at full health without committing the corresponding ticket loss | role authority preserves team tickets | `BFV-004`, `BFV-005` |
| Downed state expires without revival | Allow bleedout and redeploy | Death commits, ticket state updates and a legal source is required for return | downing and death are separate | `BFV-002`, `BFV-005` |
| Authored trench or sandbag outline is visible | Hold the toolbox build interaction | Build progress completes and the new geometry changes cover or route access | fortification is causal map state | `BFV-003`, `BFV-007` |
| Authored supply-station outline is completed | Interact with the compatible station | Health or ammunition stock replenishes according to station type | construction can create sustain | `BFV-006`, `BFV-007` |
| Point contains only eligible British presence | Remain in its capture area | Ownership advances through neutralisation to British control | presence changes strategic state | `BFV-002`, `BFV-003` |
| Both teams occupy the same point | Continue contesting | Capture progress stops until opposing presence clears | kills matter through occupancy | `BFV-002` |
| Squad has earned enough points and the player is leader | Select one legal supply, smoke or strike Reinforcement and target | Shared points are spent; delivery resolves its typed battlefield effect | cooperation becomes a spendable tactical call | `BFV-008` |
| British side owns the point majority | Maintain control while avoiding unrevived deaths | German tickets repeatedly drain while British committed deaths still cost tickets | local control and survival share one pool | `BFV-002` |
| German ticket pool reaches zero first | No further input required | Server declares British victory; inverse state is defeat | bounded team terminal | `BFV-002`, `BFV-010` |

## Strategic and experiential structure

- Local: choose cover, shot, smoke, revive, bandage, supply source, build
  outline, vehicle seat or capture radius while ammunition and nearby threats
  remain only partly known.
- Medium-term: fortify vulnerable approaches, keep Medic sustain near a push,
  preserve forward deployment sources, accumulate squad points and spend a
  Reinforcement where it can change point ownership rather than personal score.
- Long-term: maintain enough of Arras's six-point network that flag pressure
  drains German tickets faster than British unrevived deaths drain the allied
  pool.
- Heuristics: smoke before an exposed revive; finish useful supply stations;
  resupply before crossing fields; contest before a flag flips; call expensive
  Reinforcements at clustered objective pressure; redeploy away from unsafe
  squadmates.
- Failure attribution: tickets, points, build outlines, health, ammunition,
  squad points and delivery cues are visible; hidden opponents, simultaneous
  squads and sampled vehicles keep exact individual causation partial.
- Player trust: explicit scarcity and build feedback link choices to outcomes;
  team imbalance and network quality are outside the mechanics packet.

## Replay and variation

- Team and squad composition, hostile plans, vehicle availability, local
  destruction, fortification choices, reinforcement calls and point routes vary.
- Arras and its six points are authored; live human decisions, weapon handling,
  destructible cover and rebuild choices create the main variation.
- Infantry-focused defence, mobile back-capture, vehicle-supported pushes,
  supply-fortified holds and squad-call timing are all viable under one terminal.
- Replays improve map rotation, scarce-resource discipline, fortification
  placement, revive judgement and team-ticket efficiency.

## Adjacent systems and history

- Battlefield 6 is the closest direct corridor: both use squads, classes,
  vehicles, destructible cover, deployment sources, reversible downing, points
  and symmetric ticket attrition.
- Battlefield V differs mechanically through one carried bandage, partial
  health recovery, authored player-built Fortifications/supply stations and a
  squad-point economy spent by the leader on Reinforcements.
- War Thunder and World of Tanks share team vehicles and spatial control but
  not infantry revival, buildable sustain or a squad-call economy. Delta Force
  shares downing and objective tickets but uses asymmetric sector progression.
- Firestorm, Grand Operations and Community Games are variants outside the
  fixed ordinary Conquest packet, not historical context folded into it.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-187`, `ACT-190`, `ACT-199`–`ACT-201`, `ACT-215`, `ACT-240`, `ACT-241`, `ACT-388`, `ACT-389` | exact weapon, gadget, outline, vehicle and call are parameters |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-292`, `SYS-320`, `SYS-380`, `SYS-382`, `SYS-386`, `SYS-394`–`SYS-396`, `SYS-713`–`SYS-715` | numeric damage, build, resupply, point and ticket values are parameters |
| Constraint | `CON-262`, `CON-269`, `CON-272`, `CON-286`, `CON-288`, `CON-346`–`CON-348`, `CON-560`, `CON-561` | surface, leader, cost, target, seat and source legality |
| Information | `INF-073`, `INF-115`, `INF-116`, `INF-119`, `INF-155`, `INF-274`, `INF-275` | HUD position and audiovisual style are excluded |
| Objective | `OBJ-079` | British/German side and ordinary server time settlement are parameters |
| Time | `TIM-003` | all admitted match transitions remain live |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `219` (`GAME-0001`–`GAME-0219`).
- Exact genome matches: none.
- Tied near matches: `GAME-0149` — Battlefield 6 (`35 / 47 = 0.744681`).
- Supported combination subsets: `COMB-0147`, `COMB-0218`.
- Scan date: 2026-09-01.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0149` — Battlefield 6 | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-187`, `ACT-190`, `ACT-201`, `ACT-215`, `ACT-240`, `ACT-241`, `SYS-208`, `SYS-215`, `SYS-292`, `SYS-320`, `SYS-380`, `SYS-382`, `SYS-386`, `SYS-394`, `SYS-395`, `SYS-396`, `CON-262`, `CON-269`, `CON-272`, `CON-288`, `CON-346`, `CON-347`, `CON-348`, `INF-073`, `INF-115`, `INF-116`, `INF-119`, `INF-155`, `OBJ-079`, `TIM-003` | both convert class/squad combined arms, reversible deaths and simultaneous point control into symmetric ticket attrition; Battlefield V additionally makes one-bandage health and ammunition scarcity, authored Fortifications/supply stations and leader-spent squad Reinforcements part of the ordinary loop, while Battlefield 6's reviewed packet instead foregrounds Training Paths, Spawn Beacons, drag-to-cover and Engineer repair | Near, `35 / 47 = 0.744681` |

## Taxonomy impact

- Added `ACT-388`, `ACT-389`, `SYS-713`–`SYS-715`, `CON-560`, `CON-561`,
  `INF-274`, `INF-275` and one verified combination.
- Reused generic combat, vehicle, deployment, revival, point and ticket genes;
  no previously reviewed signature or lifecycle changed.
- The new boundaries isolate only construction, scarcity/resupply and
  leader-authorised shared-resource decisions missing from prior Conquest data.

## Negative results

- `SYS-528` and `CON-450` encode Siege's stock-limited defensive layers on
  soft surfaces, not toolbox construction at authored battlefield outlines.
- `SYS-600` is a continuous attacker-only Payload-cart field, not stationary
  class/station resupply under symmetric Conquest.
- The unshipped pre-release teammate-drag promise is not admitted; `ACT-241`
  is used only for its active revive boundary.
- Combat Medic, exact weapon Specializations, assignments, account unlocks and
  every Community Game modifier remain outside the fixed Field Medic packet.

## Delta summary

## Нові факти

- Arras Conquest поєднує шість прапорів, піхоту, техніку, руйнування та
  відбудовувані укріплення в одному симетричному бою за квитки підкріплень.
- Field Medic працює в умовах обмеженого здоров’я й боєзапасу, а взаємодія
  загону перетворюється на очки для виклику підкріплень командиром.

## Нові гени

- Дев’ять нових меж описують будівництво укріплень, виснаження й поповнення
  ресурсів, спільні очки загону, виклик підкріплень та їхні видимі умови.

## Нові комбінації

- `COMB-0218` — дефіцит, укріплення й командні підкріплення підтримують
  відновлюваний наступ на прапори, який виснажує спільні квитки супротивника.

## Зміни таксономії

- Додано дев’ять Active-меж без зміни наявних генів або сигнатур.

## Нові питання

- Чи повторить інша командна гра спільну економіку загону, де право витрати
  належить одній ролі, але ресурс заробляють усі учасники?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0221` World of Warcraft.
- Optimisation criterion: return from one fixed team round to a bounded
  persistent MMORPG route while preserving Batch 010 order.
- Expected information gain: class-fixed quest progression without a later
  class-transfer terminal.
- Backlog impact: Unit 5 of the active nine-game Goal.

## Чому саме вона

- It is the next authorised subject in `SEARCH_DEMAND_GAME_SELECTION_010` and
  separates the two requested MMORPG representatives by a combined-arms unit.

## Family classification

- `FAM-005` — Route and network construction.
- `FAM-007` — Physics and object manipulation.
- `FAM-009` — Tactical forecast and counterplay.
- `FAM-010` — Real-time system pressure.
- `FAM-014` — World topology and perspective.
- `FAM-015` — Agent routing and coordination.
