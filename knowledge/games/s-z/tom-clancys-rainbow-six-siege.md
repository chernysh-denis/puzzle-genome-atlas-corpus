---
game_id: GAME-0174
slug: tom-clancys-rainbow-six-siege
game_title: Tom Clancy’s Rainbow Six Siege
analysis_status: reviewed
reviewed: 2026-08-28
combination_ids:
  - COMB-0172
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-184
    - ACT-185
    - ACT-186
    - ACT-187
    - ACT-188
    - ACT-190
    - ACT-202
    - ACT-212
    - ACT-215
    - ACT-241
    - ACT-301
    - ACT-302
    - ACT-303
  system:
    - SYS-208
    - SYS-215
    - SYS-292
    - SYS-293
    - SYS-294
    - SYS-296
    - SYS-380
    - SYS-386
    - SYS-527
    - SYS-528
    - SYS-529
    - SYS-530
  constraint:
    - CON-262
    - CON-263
    - CON-264
    - CON-265
    - CON-266
    - CON-267
    - CON-268
    - CON-269
    - CON-449
    - CON-450
    - CON-451
  information:
    - INF-073
    - INF-075
    - INF-115
    - INF-116
    - INF-150
    - INF-214
    - INF-215
  objective:
    - OBJ-071
  time:
    - TIM-003
---

# Game: Tom Clancy’s Rainbow Six Siege

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: PC public build `24657867`, Year 11 Season 2.3 / Operation
  System Override, observed `2026-08-28`; one private/local 5v5 Bomb match on
  Clubhouse using the 2026 Pro League preset, finite three-round overtime.
- Primary decision loop: ban and select role-legal operators; attackers scout
  with drones while defenders identify sites, reinforce surfaces and deploy
  gadgets; then move, observe, communicate, breach, shoot, use gadgets and
  contest the defuser until one team wins the round; rebuild the site and swap
  roles at the declared match boundaries.
- Entry and exit: begins at the operator-ban phase before round one and ends
  when one fixed team wins the map in regulation or finite overtime.
- Included: 5v5 attacker/defender roles; scheduled operator bans and unique
  picks; operator weapon/gadget loadouts; preparation/action phases; drones,
  cameras, pings and team cues; barricades, reinforcements and destructible
  surfaces; firearms, grenades and typed gadgets; health, injury, ally revival
  and final elimination; two bomb sites, carried defuser, plant, disable,
  timeout and score; regulation, role swap and three-round overtime.
- Excluded: matchmaking and rank; reputation, account, Battle Pass, shop and
  cosmetic progression; Quick Match, Standard, Dual Front and non-Bomb modes;
  maps other than Clubhouse; best-of series, coaches, tactical timeouts and
  tournament administration; future Year 11 Season 3 announced for
  `2026-09-01`.
- Potential scoped modules: ranked map veto; other objective modes; Dual Front;
  one operator-specific gadget interaction; infinite-overtime competition.
- Direct-play status: not conducted. Current Ubisoft guides establish the
  preparation/action loop, drones, fortification, destructibility, gadgets and
  observation tools; the official 2026 BLAST R6 rulebook fixes the bounded Bomb
  settings and ban schedule; Steam app-info pins the reviewed public build.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `R6S-001` | Steam build `24657867` is the current public PC package in Year 11 Season 2.3; Season 3 is outside this scope | Observation | Corroborated | High | P1, P2, S1 |
| `R6S-002` | The Pro League Bomb preset uses fixed 5v5 teams, twelve regulation rounds, a role swap after six and finite three-round overtime with a two-round margin | Confirmed | Direct | High | P8 |
| `R6S-003` | Attackers use drones to scout during preparation while defenders locate the sites, reinforce eligible surfaces and deploy defensive gadgets | Confirmed | Direct | High | P3, P4 |
| `R6S-004` | Each round uses role-bounded, non-duplicate operator picks under a scheduled operator-ban pool | Confirmed | Direct | High | P7, P8 |
| `R6S-005` | Soft destruction, reinforcement and hard breach alter traversable openings, sightlines, cover and sound paths | Observation | Corroborated | High | P3, P4, P6 |
| `R6S-006` | Local sight and sound are incomplete, while live drones, cameras, scans, pings and team cues expose device-bounded shared intelligence | Confirmed | Corroborated | High | P3, P5 |
| `R6S-007` | Firearms, explosives and gadgets can injure, revive or finally eliminate a player for the current round | Observation | Corroborated | High | P3, P6, P8 |
| `R6S-008` | Attackers may plant the defuser near either bomb; defenders may disable it, while elimination, timeout and the planted-device clock resolve the round in ordered precedence | Confirmed | Direct | High | P3, P8 |
| `R6S-009` | Every round rebuilds its local siege state; score persists, roles swap after six regulation rounds and ban state changes on the rulebook schedule | Confirmed | Direct | High | P8 |
| `R6S-010` | Fixed-team communication turns partial observation, breaching and gadget interaction into strategic counterplay rather than kill-score maximisation | Observation | Corroborated | High | P3, P5, P8 |

## Basic data

- Release / origin: `2015`, Ubisoft Montreal / Ubisoft; current Year 11 PC
  state observed `2026-08-28`.
- Platform or physical form: Windows PC client; private/local multiplayer match.
- Puzzle family: asymmetric team tactical counterplay, destructible-space
  planning, device-bounded information and staged bomb defence.
- Primary sources:
  - `P1` — [official Y11S2.3 patch notes](https://www.ubisoft.com/en-us/game/rainbow-six/siege/news-updates/2EIn06EmkAIG7su2fpITue/y11s23-patch-notes),
    for the current live patch boundary.
  - `P2` — [official Operation System Override page](https://www.ubisoft.com/en-us/game/rainbow-six/siege/news-updates/seasons/systemoverride),
    for the Year 11 Season 2 identity and current feature context.
  - `P3` — [official launch game guide, part 1](https://www.ubisoft.com/en-us/game/rainbow-six/siege/news-updates/2YagcXYDLVw3niBT2z5ZG7/launch-game-guide-part-1),
    for attacker drones, defender preparation, destructible environments and
    Bomb's two-site defuser objective.
  - `P4` — [official Tools of Attack guide](https://www.ubisoft.com/en-us/game/rainbow-six/siege/news-updates/1qBe9DIHhdmclzHegvNZi2/behind-the-wall-series-tools-of-attack),
    for fortification, breach and role-specific preparation.
  - `P5` — [official Observation Tool design note](https://www.ubisoft.com/en-us/game/rainbow-six/siege/news-updates/6KlY4IEhecnajBCIzPc89l/dev-blog-observation-tool-changes-and-bulletproof-camera),
    for device feeds, camera rotation, scanning and destruction.
  - `P6` — [official Y10S4 designer's notes](https://www.ubisoft.com/en-us/game/rainbow-six/siege/news-updates/1XzWbYPWo59u7NgZVDjaIm/y10s4-designers-notes),
    for current reinforcement and surface interaction.
  - `P7` — [official Year 11 roadmap](https://www.ubisoft.com/en-us/game/rainbow-six/siege/news-updates/roadmap),
    for the current Pick & Ban schedule and the future Season 3 boundary.
  - `P8` — [official 2026 BLAST R6 rulebook](https://staticctf.ubisoft.com/p0f8o8d25gmk/4vLmovz8mJb3XUEdtHZBJA/1227a0d321ed95d3564499afb713c9d5/Global_Rulebook_BLASTR6_Season_2026_Kickoff_Update_v2.pdf),
    for Pro League Bomb settings, timers, round count, role swap, overtime and
    scheduled operator bans.
- Secondary source:
  - `S1` — [Steam app-info mirror](https://api.steamcmd.net/v1/info/359550),
    observed `2026-08-28`, for public build `24657867`; Ubisoft's patch page
    independently establishes the live season and patch.
- Reproducibility: archived source hashes are recorded in the research log;
  `P8` SHA-256 is
  `d4738365b1d20bafef7d56c8b2e4bdf28f5ba42be4a1291aaf24f8bf8dd8bb4c`.
- Claim IDs: `R6S-001`–`R6S-010`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, direct first-person traversal; `ACT-161`, aimed
  weapon or gadget attack; `ACT-164`, select active carried equipment;
  `ACT-183`, reload; `ACT-184`, prime and throw a grenade; `ACT-185`, hold a
  plant/disable channel; `ACT-186`, drop the defuser; `ACT-187`, communicate a
  team cue; `ACT-188`, commit an operator; `ACT-190`, use a selected ability;
  `ACT-202`, change stance; `ACT-212`, place/remove barricade or reinforcement;
  `ACT-215`, configure an operator loadout; `ACT-241`, revive an injured ally.
- New genes: `ACT-301`, ban one eligible opposing-role operator; `ACT-302`,
  direct one live observation device or feed; `ACT-303`, breach one eligible
  constructed surface.
- Parameters: role, operator, weapon, secondary gadget, stance, surface,
  breach tool, observation device, site, timing and communication channel.
- Claim IDs: `R6S-003`–`R6S-008`.

### System Behaviour Genes

- Existing genes: `SYS-208`, resolve ranged attacks through material and body;
  `SYS-215`, direct simultaneous combat; `SYS-292`, resolve thrown utility;
  `SYS-293`, remove final eliminations for the round; `SYS-294`, adjudicate the
  asymmetric bomb round; `SYS-296`, swap roles under retained score;
  `SYS-380`, resolve typed gadgets; `SYS-386`, destroy eligible geometry.
- New genes: `SYS-527`, resolve observation-device movement, feed, scan and
  loss; `SYS-528`, apply defensive fortification layers; `SYS-529`, resolve
  injury, ally revival and final elimination; `SYS-530`, rebuild and rotate
  round-local siege state.
- Resolution order: accept concurrent movement, observation and equipment
  input; resolve legal gadget/surface interaction and combat; update injury,
  device and objective state; award the round; rebuild local state and apply
  the next role/ban boundary while preserving score.
- Claim IDs: `R6S-002`–`R6S-009`.

### Constraint Genes

- Existing genes: `CON-262`, bounded round equipment; `CON-263`, final
  elimination suspends control; `CON-264`, planted-device interaction gates;
  `CON-265`, asymmetric pre/post-plant deadlines; `CON-266`, fixed role
  authority; `CON-267`, bounded regulation/overtime; `CON-268`, unique
  operator commitments; `CON-269`, gadget target/readiness gates.
- New genes: `CON-449`, preparation and action phases gate role-specific
  control; `CON-450`, fortification and gadget deployment require eligible
  surface and stock; `CON-451`, observation requires a live device and leaves
  the operator body exposed.
- Scarce strategic resources: living operators, information devices,
  reinforcements, barricades, gadget charges, ammunition, destructible cover,
  action time and planted-defuser time.
- Claim IDs: `R6S-002`–`R6S-009`.

### Information Genes

- Existing genes: `INF-073`, active loadout and ammunition; `INF-075`, health
  and injury; `INF-115`, local sight and sound; `INF-116`, team, score, clock
  and objective HUD; `INF-150`, operator roster, kits and current bans.
- New genes: `INF-214`, observation-network device-bounded team intelligence;
  `INF-215`, local surface material, fortification and breach state.
- Claim IDs: `R6S-003`–`R6S-010`.

### Objective Genes

- Existing gene: `OBJ-071`, win the bounded bomb-defusal match by round score
  under the declared regulation and overtime policy.
- Claim IDs: `R6S-002`, `R6S-008`, `R6S-009`.

### Time Genes

- Existing gene: `TIM-003`, movement, observation, attacks, gadgets and
  objective channels advance in real time during each phase.
- Parameters: `45`-second preparation, `180`-second action, `7`-second plant,
  `45`-second planted fuse and `7`-second disable timers.
- Claim IDs: `R6S-002`, `R6S-008`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Round one ban phase is open | Each team bans two eligible opposing-role operators | Four operators become unavailable under the declared role schedule | shared roster denial | `R6S-004` |
| Preparation begins with hidden defender site | Attacker drives a live drone while defenders reinforce and deploy gadgets | The drone may reveal bounded site/operator information; legal surfaces gain defensive layers | opposed preparation | `R6S-003`, `R6S-006` |
| Reinforced wall separates attacker from a bomb room | Use a compatible hard-breach charge | Valid placement and completion open traversable/visible geometry; denial can interrupt it | constructed-space counterplay | `R6S-005` |
| A live drone or camera is available | Enter its feed and rotate, move or scan where supported | Only that device's current field exposes information; destruction removes the feed while the body remains locally vulnerable | device-bounded intelligence | `R6S-006` |
| Operator takes injury-threshold damage and a teammate can reach them | Hold the legal revive interaction | Completion returns the ally with configured health; further or disqualifying damage finalises elimination | recoverable injury | `R6S-007` |
| Attacker holds the defuser near bomb A or B | Hold plant for seven uninterrupted seconds | A live planted-defuser state replaces the original action deadline with its own timer | staged objective clock | `R6S-008` |
| Defender reaches the planted defuser | Hold disable for seven uninterrupted seconds | Completion awards defenders; interruption or timer expiry leaves attacker victory possible | objective channel precedence | `R6S-008` |
| Six regulation rounds are complete | Cross the round boundary | Teams exchange attacker/defender roles while map score persists and round-local geometry/devices rebuild | role rotation and reset | `R6S-002`, `R6S-009` |
| Regulation or finite overtime margin is reached | Award the decisive round | The map ends for the team satisfying the configured score policy | bounded match terminal | `R6S-002`, `R6S-009` |

## Strategic and experiential structure

- Local decision: choose exposure, stance, crosshair, observation feed, surface,
  gadget and timing while opponents can act simultaneously.
- Medium-term planning: convert drones and cameras into a coordinated breach,
  preserve flank observation, deny a plant route and trade or revive teammates.
- Long-term structure: adapt operator bans, site defence and attack plans across
  repeated rebuilt rounds and the attacker/defender role swap.
- Common heuristics: keep drones alive after locating the site; create more than
  one entry threat; reinforce surfaces that protect a plan rather than every
  wall; leave one teammate able to trade an observer or planter; reserve enough
  action time for the seven-second plant.
- Failure attribution: HUD, kill feed, device loss and changed surfaces expose
  immediate causes, while hidden opponents and team communication preserve
  uncertainty about the best counterfactual plan.
- Player-trust factors: fixed timers and visible score are auditable; dense
  gadget interactions require consistent surface and feedback rules.
- Claim IDs: `R6S-003`–`R6S-010`.

## Replay and variation

- What changes between matches: bans, operator compositions, bomb-site choice,
  fortification, gadget placement, breach route, observation survival and
  human timing.
- Randomness or procedural generation: the scoped map and rules are fixed;
  variation is generated chiefly by simultaneous hidden human choices.
- Multiple viable strategies: direct execute, roam clear, vertical pressure,
  split breach, plant denial and retake exchange time, information and gadgets.
- Typical replay motive: learn material and sightline interactions, improve
  operator coordination and adapt site plans after the role swap.
- Claim IDs: `R6S-004`–`R6S-010`.

## Adjacent systems and history

- Direct predecessors: earlier Rainbow Six games establish the tactical series
  lineage but do not supply evidence for this live ruleset.
- Variants: Ranked, Standard, Quick Match, Dual Front and non-Bomb modes change
  map, participant, phase or objective contracts and remain separate scopes.
- Similar games: Counter-Strike 2 shares fixed-team real-time bomb rounds,
  partial opponent information and side-swapped scoring; Battlefield 6 shares
  live firearms, gadgets, revival and destructible cover.
- Important differences: Siege makes observation devices, operator identity,
  defensive construction and material breach central round resources, rebuilds
  those local layers each round and permits recoverable injury before final
  one-life elimination.
- Claim IDs: `R6S-002`–`R6S-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`–`ACT-188`, `ACT-190`, `ACT-202`, `ACT-212`, `ACT-215`, `ACT-241`, `ACT-301`–`ACT-303` | lean, rappel and exact operator controls are parameters |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-292`–`SYS-294`, `SYS-296`, `SYS-380`, `SYS-386`, `SYS-527`–`SYS-530` | recoil and exact destruction meshes are parameters |
| Constraint | `CON-262`–`CON-269`, `CON-449`–`CON-451` | map geometry and exact charge counts are parameters |
| Information | `INF-073`, `INF-075`, `INF-115`, `INF-116`, `INF-150`, `INF-214`, `INF-215` | marker colour and sound range are parameters |
| Objective | `OBJ-071` | regulation/overtime thresholds are parameters |
| Time | `TIM-003` | phase and interaction durations are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `173` (`GAME-0001`–`GAME-0173`).
- Exact genome matches: none.
- Tied near matches: `GAME-0137` — Counter-Strike 2 (`25 / 54 = 0.462963`).
- Supported combination subsets: `COMB-0172`.
- Scan date: 2026-08-28.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Counter-Strike 2 (`GAME-0137`) | direct movement/fire, carried equipment, grenade and plant channels, round removal, bomb adjudication, side roles, local information, score HUD and real time | Siege replaces purchase economy with unique operator kits, drones/cameras, fortification, material breach, recoverable injury and full round-local map rebuilding | Near, `0.462963` |

### Preserved research notes

- New genes: `ACT-301`–`ACT-303`, `SYS-527`–`SYS-530`, `CON-449`–`CON-451`,
  `INF-214`–`INF-215`.
- Classification result: `New gene`, boundary-preserving support expansion and
  a new combination of known/new genes.
- Evidence and reasoning: weapon statistics, lean/rappel bindings and each
  operator gadget remain parameters; new boundaries isolate player-visible
  decisions not already represented by generic combat or ability use.

## Taxonomy impact

- Registry changes after normalisation: twelve bounded active genes plus
  Rainbow Six Siege support added to twenty-seven existing records.
- Taxonomy-change record: none. Existing definitions are broadened only where
  the same operational boundary now has a second evidenced parameterisation.
- Candidate terms affected: wallbang, spawn peek, roam, execute and retake are
  strategies or parameters inside admitted genes, not separate genes.

## Negative results

- Direct-play evidence was unavailable, so exact recoil, spread, operator
  balance values and map-specific lineups were not admitted as claims.
- The announced Year 11 Season 3 state was rejected as future evidence.

## Delta summary

## Нові факти

- [Observation/Confirmed | Direct/Corroborated | High] Зафіксовано актуальну
  версію Y11S2.3 та правила Bomb: 5v5, дванадцять раундів основного часу,
  зміна ролей після шести й скінченний овертайм (`R6S-001`, `R6S-002`).

## Нові гени

- [Observation/Confirmed | Direct/Corroborated | High] Дванадцять нових генів
  ізолюють бан операторів, мережу спостереження, фортифікацію, пролом,
  поранення та раундове відновлення мапи (`R6S-003`–`R6S-009`).

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0172` поєднує рольово-унікальний
  вибір, спостереження, укріплення і пролом із поетапною Bomb-ціллю
  (`R6S-003`–`R6S-009`).

## Нові зв'язки

- [Observation | Corroborated | High] Виявлено близькість до Counter-Strike 2
  через командні Bomb-раунди, але Siege додає перебудову простору,
  device-bounded інформацію та відновлюване поранення (`R6S-005`–`R6S-010`).

## Зміни таксономії

- [Observation | Corroborated | High] Межі наявних генів planted device,
  role swap, operator selection, destructible geometry та team HUD розширено
  другим підтвердженим параметричним прикладом без зміни сигнатур
  (`R6S-002`–`R6S-009`).

## Джерела

- [Confirmed | Direct | High] Офіційні матеріали Ubisoft і BLAST R6 задають
  механічні переходи та match preset; Steam app-info лише фіксує public build
  (`R6S-001`–`R6S-010`).

## Що перевірено востаннє

- [Observation | Corroborated | High] На `2026-08-28` build `24657867` та
  Y11S2.3 були останнім знайденим публічним PC-станом; анонсований Y11S3
  виключено (`R6S-001`).

## Ризики

- [Inference | Corroborated | Medium] Live-service patches можуть змінити
  операторів, gadget-и й точні таймери; запис тому прив'язаний до Y11S2.3 і
  Pro League preset, а точні balance values не підняті до генів.
