---
game_id: GAME-0211
slug: world-of-tanks
game_title: World of Tanks
analysis_status: reviewed
reviewed: 2026-09-01
combination_ids:
  - COMB-0209
gene_ids:
  action:
    - ACT-161
    - ACT-290
  system:
    - SYS-320
    - SYS-701
    - SYS-702
    - SYS-703
    - SYS-704
  constraint:
    - CON-262
    - CON-488
    - CON-555
  information:
    - INF-115
    - INF-116
    - INF-270
  objective:
    - OBJ-131
  time:
    - TIM-003
---

# Game: World of Tanks

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current official English Windows PC Americas client,
  Update `2.4: Overdrive`, reviewed 2026-09-01; one solo, non-platoon ordinary
  Random Battle admitted only when the assigned type is `Standard Battle`,
  using the free U.S.S.R. Tier I light tank MS-1 with its starting modules,
  crew and standard armour-piercing ammunition. Steam public bootstrap manifest
  `25041956` is retained only as secondary package metadata, not as the complete
  rules build.
- Primary decision loop: directly steer the MS-1 through cover and terrain;
  read the minimap, base state and local or allied spotting; choose Arcade or
  Sniper aim, let the movement-sensitive aiming circle settle and fire a loaded
  finite shell; resolve impact against range, angle and armour into vehicle hit
  points, modules and crew; preserve one's single tank while helping destroy
  the opposing team or accumulate enemy-base capture; after destruction,
  observe the remaining team until the shared result settles.
- Entry and exit: queue `Random Battle` from an otherwise eligible regular
  account and retain the first assigned Standard Battle. Entry is the first
  controllable MS-1 frame after the battle countdown on the sampled legal map.
  Positive exit is the post-battle victory result after complete enemy-vehicle
  destruction or enemy-base capture; failure is the post-battle defeat after
  the opposing team completes either terminal; expiry of the fifteen-minute
  limit without either terminal is a draw. The player's own tank destruction
  removes direct control but is not the packet exit while allies remain.
- Included: one MS-1; direct tracked driving, hull and turret orientation;
  Arcade and Sniper aiming; aiming-circle dispersion and settling; finite
  standard AP ammunition and automatic reload; shell travel, impact angle,
  effective armour, penetration and ricochet; aggregate hit points; module and
  crew impairment; destruction; view range, proximity spotting, concealment,
  foliage and firing/movement penalties; radio-shared allied sightings;
  minimap, roster, timer and two bases; damage-interruptible base capture;
  single-tank non-return, postmortem/spectator state and victory/defeat/draw.
- Excluded: novice matchmaking and bots; platoons; Encounter, Assault, Grand
  Battle, Frontline, Onslaught, clan, tournament, event and training modes;
  World of Tanks Blitz, Modern Armor and consoles; other nations, tiers and
  tanks; premium or alternate ammunition; consumables, equipment, directives,
  optional Armor Flashlight and modifications; research, blueprints, crew
  training and perks, missions, currencies, service costs, Battle Pass,
  achievements, account progression, replays and the whole live-service
  history.
- Sampled parameters: legal Standard Battle map, spawn side, team and enemy
  roster, player movement, spotted targets, armour angles, dispersion results,
  shot outcomes, capture contributors and final result. A rejected non-Standard
  queue result does not enter the analytical packet.
- Potential scoped modules: a current higher-tier light-tank role packet;
  Encounter; Assault; a platoon; novice matchmaking with AI participants; or
  the garage research and equipment economy.
- Direct-play status: not conducted. Current official update, newcomer,
  control, survival, ammunition, crew, postmortem and Random Battle documents
  establish the declared rules and terminal. The trace below is evidence-based
  rules reconstruction, not a claimed captured match. No video or audio was
  opened, played, heard or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `WOT-001` | Update 2.4 is the current official PC client boundary; Steam manifest 25041956 describes only the public bootstrap package | Confirmed | Corroborated | High | P1, S1 |
| `WOT-002` | New players can enter Random Battles and the free Tier I MS-1 is a legal starting vehicle | Confirmed | Direct | High | P2, P3 |
| `WOT-003` | Standard Battle assigns two teams and bases and settles by destroying all opponents, capturing the enemy base or reaching the fifteen-minute draw limit | Confirmed | Corroborated | High | P4, P5 |
| `WOT-004` | The player directly drives the tank, aims its gun and fires only after a compatible shell is loaded | Confirmed | Direct | High | P6, P7 |
| `WOT-005` | Movement and turret traverse enlarge the aiming circle; waiting narrows the uncertain impact area | Confirmed | Direct | High | P6 |
| `WOT-006` | AP impact tests distance, angle and effective armour, then can reduce vehicle hit points and separately damage crew or modules | Confirmed | Corroborated | High | P7, P8 |
| `WOT-007` | Enemy visibility depends on proximity, view range and concealment, and eligible allied observations are relayed through radio range | Confirmed | Direct | High | P8 |
| `WOT-008` | Base capture is accumulated by eligible attackers and damage to a capturing tank removes eligible capture contribution | Confirmed | Direct | High | P4 |
| `WOT-009` | Destruction ends control of the single tank and permits postmortem or spectator viewing while the team result remains unresolved | Confirmed | Direct | High | P9 |
| `WOT-010` | The bounded loop couples uncertain armoured shots, shared detection, one personal tank life and two alternative team terminals | Observation | Corroborated | High | P2–P9, V1 |

## Basic data

- Release / origin: developed and published for the scoped region by
  Wargaming; the current official product title is **World of Tanks**.
- Platform or physical form: networked real-time armoured-vehicle game; only
  the current official Windows PC Americas rules declared above are admitted.
- Puzzle family: physics and object manipulation; tactical forecast and
  counterplay; real-time system pressure; agent routing and coordination.
- Primary and official sources:
  - **[P1]** [official Update 2.4: Overdrive notes](https://worldoftanks.com/en/news/updates/wot-2-4/),
    for the current named update boundary and PC live-service context.
  - **[P2]** [official Getting Started guide](https://worldoftanks.com/en/content/guide/newcomers-guide/getting_started/),
    for Random Battle entry, the map/roster/objective loading context and Tier I
    starting vehicles.
  - **[P3]** [official MS-1 Tankopedia entry](https://worldoftanks.com/en/tankopedia/3329-R11_MS-1/),
    for the free U.S.S.R. Tier I light-tank identity.
  - **[P4]** [official battle-mode breakdown](https://worldoftanks.com/en/news/general-news/breakdown-game-modes/),
    for Standard Battle teams, bases, capture, destruction and time boundary.
  - **[P5]** [official current FAQ](https://worldoftanks.com/en/content/guide/general/frequently_asked_questions/),
    for the fifteen-minute Standard Battle duration and draw condition.
  - **[P6]** [official controls and shooting guide](https://worldoftanks.com/en/content/guide/newcomers-guide/game_controls/),
    for direct driving, turret/gun control, Arcade/Sniper views, reload state,
    ammunition count and movement-sensitive aiming-circle dispersion.
  - **[P7]** [official upgrading and ammunition guide](https://worldoftanks.com/en/content/guide/newcomers-guide/upgrading_vehicles/),
    for starting Tier I AP ammunition, penetration, distance and ricochet.
  - **[P8]** [official survival and mechanics guide](https://worldoftanks.com/en/content/guide/newcomers-guide/how_to_survive/),
    for effective armour, crew/modules, proximity and range spotting,
    concealment, foliage, radio sharing and detection limits.
  - **[P9]** [official postmortem and battle-result guide](https://worldoftanks.com/en/content/guide/game-mechanics-and-achievements/postmortem-mode-and-battle-rating/),
    for destruction, postmortem/spectator access and post-battle settlement.
- Secondary build metadata:
  - **[S1]** [SteamDB depots for app 1407200](https://steamdb.info/app/1407200/depots/),
    used only to retain public bootstrap Build ID `25041956`, updated
    2026-08-31; it is not treated as rules authority or a full client build.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P9` under the declared tank, match and exclusions; rules reasoning,
  not a direct-play claim.
- Claim IDs: `WOT-001`–`WOT-010`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-290`: directly steer, accelerate, reverse, brake and orient the
  assigned tracked vehicle without an embodied enter/exit loop.
- Existing `ACT-161`: aim the loaded tank gun at a reachable hostile armour
  point and commit a shot; dispersion, penetration and damage remain systemic.
- Parameters: tank, throttle, steering, hull, turret, elevation, view mode,
  target point and fire input.
- Claim IDs: `WOT-004`–`WOT-006`, `WOT-010`.

### System Behaviour Genes

- Existing `SYS-320`: integrate the MS-1's direct tracked motion, terrain
  contact, collision and broad vehicle-damage envelope.
- New `SYS-701`: resolve AP impact through range, angle and armour into both
  aggregate vehicle hit points and separate module or crew impairment.
- New `SYS-702`: compare view range and concealment, guarantee proximity
  detection where applicable and relay eligible spotted markers through radio.
- New `SYS-703`: accumulate capture from eligible surviving attackers and
  remove affected contribution after departure, destruction or eligible damage.
- New `SYS-704`: settle the shared result by complete opposing destruction,
  enemy-base capture or an unresolved fifteen-minute draw.
- Resolution order: integrate hull/turret motion and spotting; narrow or widen
  the aim envelope; accept a legal loaded shot; resolve travel, armour and
  damage; update spotted and functional state; update base capture and living
  rosters; then settle or continue the match.
- Claim IDs: `WOT-003`, `WOT-005`–`WOT-010`.

### Constraint Genes

- Existing `CON-262`: the MS-1 has finite compatible standard AP ammunition.
- Existing `CON-488`: firing requires ammunition, completed automatic reload
  and a legal gun traverse, elevation and line; the reticle cannot guarantee
  the later shell result.
- New `CON-555`: destruction permanently removes the one assigned tank from
  this battle and leaves only observation until the shared terminal.
- Scarce strategic resources: tank hit points, functioning crew/modules,
  shells, loaded state, settled aim, concealment, safe lines, capture progress,
  living allies and remaining battle time.
- Claim IDs: `WOT-004`–`WOT-010`.

### Information Genes

- Existing `INF-115`: local sight, spatial effects and impacts expose only the
  currently perceived opponent state; unspotted vehicles remain hidden.
- Existing `INF-116`: the live interface exposes allied state, roster, minimap,
  clock, base capture and eligible shared spotted markers.
- New `INF-270`: the tank HUD exposes ammunition/reload, an uncertain aiming
  circle, hit points and known crew/module impairment.
- Claim IDs: `WOT-003`–`WOT-010`.

### Objective Genes

- New `OBJ-131`: win the Standard Battle by completing enemy-base capture or
  destroying every opposing vehicle before the inverse terminal and timer.
- Personal survival, damage, kills, experience and credits are not substitute
  objectives; the allied team can still win after the scoped MS-1 is destroyed.
- Claim IDs: `WOT-003`, `WOT-008`–`WOT-010`.

### Time Genes

- Existing `TIM-003`: vehicles, aiming, reload, spotting, capture and battle
  time advance continuously while participants act; spectating does not turn
  the remaining match into discrete turns.
- Claim IDs: `WOT-003`–`WOT-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| An eligible regular account has the free MS-1 selected | Queue Random Battle and retain the first Standard Battle | The server assigns a legal map, side, roster and two-base objective | exact entry while variable matchmaking remains a parameter | `WOT-002`, `WOT-003` |
| Countdown ends with the MS-1 alive | Hold forward and steer | Tracks translate hull input through terrain while turret orientation can remain distinct | one dedicated directly controlled vehicle | `WOT-004` |
| Turret or hull has just moved | Stop motion while keeping the same aim point | The aiming circle contracts over time but still describes a possible impact area | waiting trades exposure for accuracy | `WOT-005` |
| AP is loaded and a visible opponent lies inside legal gun geometry | Fire once | One shell leaves inventory, reload begins and impact later tests distance, angle and armour | legal release and physical resolution remain separate | `WOT-004`–`WOT-006` |
| A shell penetrates eligible armour | Give no further input during resolution | Vehicle hit points decrease and a contacted module or crew role may become impaired | durability and internal function coexist | `WOT-006` |
| An enemy is beyond current detection after occlusion/concealment tests | Move an allied observer into a legal spotting relation | The enemy becomes marked for the observer and eligible radio-linked allies | team knowledge is bounded and relayed | `WOT-007` |
| The MS-1 enters the enemy base while alive | Remain in the capture circle | Its capture contribution rises; leaving, destruction or eligible received damage removes affected progress | capture is persistent attacker-owned progress, not mere occupancy | `WOT-008` |
| The MS-1 reaches zero hit points | Attempt no further tank input | Direct control ends permanently for this battle and postmortem/spectator view remains | one personal life is distinct from the team terminal | `WOT-006`, `WOT-009` |
| All opposing vehicles are destroyed first | Give no further action | Standard Battle records allied victory and opens the result screen | elimination is one positive terminal | `WOT-003`, `WOT-010` |
| Enemy-base capture completes first | Give no further action | Standard Battle records allied victory even if opponents remain alive | base capture is the alternate positive terminal | `WOT-003`, `WOT-008` |
| Neither team completes capture or destruction before fifteen minutes | Let regulation expire | Standard Battle records a draw and opens the result screen | bounded terminal without a winner | `WOT-003` |

## Strategic and experiential structure

- Local decision: move and enlarge dispersion or wait exposed for a tighter
  shot; show stronger frontal armour or seek a thinner angle; fire now, change
  line, use foliage, reset a capturer or preserve a damaged module.
- Medium-term planning: use radio-shared markers to choose a covered firing
  lane; protect the single tank while allies still need spotting; decide
  whether enemy-base progress is safer than searching for the last vehicle.
- Long-term structure: preserve enough allied observation, fire authority and
  surviving vehicles to complete either team terminal before the opposing base
  capture, elimination or regulation clock does so.
- Common heuristics: stop briefly before a difficult shot; avoid firing from
  concealment unless the value outweighs disclosure; angle rather than expose
  flat armour; damage a capturer to reset progress; do not treat one's own
  destruction as permission to ignore the unresolved result.
- Failure attribution: the aim circle, penetration/impact feedback, damage
  indicators, minimap, roster, base progress and timer explain much of the
  chain; hidden opponents, dispersion and simultaneous team action preserve
  uncertainty.
- Player-trust factors: visible uncertainty avoids promising exact impact,
  separate module warnings explain degraded control and the result names the
  shared destruction/capture/time terminal.
- Claim IDs: `WOT-004`–`WOT-010`.

## Replay and variation

- What changes between sessions: sampled Standard Battle map, spawn side,
  rosters, routes, foliage use, detections, armour angles, dispersion, module
  hits, capture contribution and shared result.
- Randomness or procedural generation: battle maps and vehicle rules are
  authored; matchmaking and human simultaneous decisions create most
  variation, while shell dispersion and damage rolls add bounded uncertainty.
- Multiple viable strategies: concealed spotting, covered overwatch, armoured
  advance, coordinated focus, defensive reset and committed base capture can
  all advance the same two-path team objective.
- Typical replay motive: improve map lanes, concealment discipline, aim timing,
  armour targeting, capture resets and judgment about elimination versus base.
- Claim IDs: `WOT-003`–`WOT-010`.

## Adjacent systems and history

- Direct predecessors: historical versions are not imported; Update 2.4 is the
  current declared client boundary.
- Variants: novice matches may add AI participants; Encounter and Assault alter
  base topology and team roles; higher tiers add vehicle roles, equipment,
  crew builds and broader ammunition choices.
- Similar games: War Thunder shares direct tracked control, finite ammunition,
  armoured shots, spotting and team objectives; Battlefield 6 shares vehicles,
  partial team information and live territorial pressure.
- Important differences: this packet has one aggregate-HP tank life, separate
  component impairment, radio-relayed concealment tests, damage-reset capture
  and a symmetric destroy-all/base-capture result with a timed draw.
- Claim IDs: `WOT-001`–`WOT-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-161`, `ACT-290` | drive, aim and fire |
| System Behaviour | `SYS-320`, `SYS-701`–`SYS-704` | motion, damage, spotting, capture and settlement |
| Constraint | `CON-262`, `CON-488`, `CON-555` | ammunition, shot legality and one tank life |
| Information | `INF-115`, `INF-116`, `INF-270` | local cues, team state and tank HUD |
| Objective | `OBJ-131` | destroy all or capture before loss or draw |
| Time | `TIM-003` | continuous battle and fifteen-minute limit |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `210` (`GAME-0001`–`GAME-0210`).
- Exact genome matches: none.
- Tied near matches: `GAME-0184` — War Thunder (`8 / 26 = 0.307692`).
- Supported combination subsets: `COMB-0209`.
- Scan date: 2026-09-01.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0184` — War Thunder | `ACT-161`, `ACT-290`, `SYS-320`, `CON-262`, `CON-488`, `INF-115`, `INF-116`, `TIM-003` | Both join directly driven armoured fire, finite ammunition, partial detection, team state and real-time pressure. World of Tanks replaces War Thunder's three-vehicle lineup, purely spatial internal damage, three contested points and tickets with one aggregate-HP tank, distinct component impairment, range/concealment radio spotting, damage-reset enemy-base capture and a destroy-all/capture/time result | Near, `0.307692` |

### Preserved research notes

- New genes: `SYS-701`–`SYS-704`, `CON-555`, `INF-270` and `OBJ-131`.
- Classification result: `New gene` and new verified interaction combination.
- Evidence and reasoning: eight generic direct-control, ammunition,
  perception, team-state and live-time records fit unchanged; seven new records
  isolate aggregate-plus-component damage, radio spotting, base progress,
  single-tank removal and the exact Standard Battle terminal.

## Combination status

- `COMB-0209` is a verified strict thirteen-gene subset of the fifteen-gene
  genome, joining direct tank control, uncertain armoured fire, shared spotting,
  one non-returning vehicle, damage-reset capture and team settlement. Generic
  local sight and the broad vehicle-motion envelope remain outside the subset.
- Every earlier verified combination is tested deterministically after
  registration; none is an exact substitute for this chain.

## Taxonomy impact

- Registry changes: seven new Active genes, evidence links on reused
  `CON-488`, one new combination and four existing family memberships.
- Taxonomy-change record: none; no prior lifecycle or reviewed game signature
  changes.
- Candidate terms affected: hybrid tank damage, radio spotting,
  damage-interruptible capture, Standard Battle settlement, single-tank
  non-return and combined dispersion/durability HUD.

## Negative results

- `SYS-580` and `SYS-581` are not reused because their War Thunder boundary
  explicitly replaces aggregate hit points with a continuing internal
  projectile path and Arcade partial-function loss; World of Tanks retains a
  shared tank hit-point pool beside component and crew effects.
- `SYS-395` and `CON-348` are not reused because Standard Battle base capture
  does not stop merely from opposing occupancy; eligible damage removes an
  individual capturer's contribution.
- `SYS-582`, `CON-489` and `OBJ-108` are not reused because the MS-1 has no
  second lineup spawn, team tickets or no-spawnable-player terminal.
- `CON-263` is not reused because the destroyed tank does not return at a later
  round boundary inside this single battle.
- Optional penetration-colour assistance, alternative ammunition, repair
  consumables and novice bots are excluded rather than silently made universal.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Current Update 2.4 Standard Battle joins
  one Tier I MS-1 life, finite AP fire, aggregate and component damage, shared
  range/concealment spotting, two bases and a fifteen-minute team terminal
  (`WOT-001`–`WOT-010`).

## Нові гени

- [Observation | Corroborated | High] Added seven genes for hybrid tank damage,
  radio-relayed spotting, damage-reset base capture, match settlement,
  single-tank non-return, tank HUD and the two-path team objective.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0209` isolates the one-tank chain
  from uncertain shot and shared detection to capture/elimination/time result.

## Зміни таксономії

- [Observation | Direct | High] No lifecycle migration and no earlier reviewed
  signature change.

## Family classification

- `FAM-007` — Physics and object manipulation: tracked motion, shell path,
  impact geometry and armour angle make position causal.
- `FAM-009` — Tactical forecast and counterplay: spotting, concealment, aim
  settling, armour, capture resets and enemy response shape every exposure.
- `FAM-010` — Real-time system pressure: all vehicles, reloads, spotting,
  capture and the regulation clock advance together.
- `FAM-015` — Agent routing and coordination: radio-shared detections and two
  bases make the sampled team distribution mechanically relevant even solo.
- No one-game family is created.

## Plain-language interpretation

In this packet, World of Tanks is one ordinary team battle, not a garage or a
history of hundreds of tanks. You get one basic MS-1. Driving or turning the
gun makes the aiming circle wider; waiting makes it smaller, but never promises
the exact impact. A shell still has to meet the target at a useful angle and
penetrate armour. A successful hit can reduce the tank's main durability and
also impair a separate crew role or module.

Enemies are not permanently visible. Your tank or an ally must detect them
through distance, view range and concealment, and the radio network determines
which allies receive that marker. The team wins by destroying every opposing
tank or completing capture of the enemy base. Damaging a capturing tank can
remove its progress. If your MS-1 is destroyed you may watch, but cannot return;
the packet ends only when the whole team receives victory, defeat or a timed
draw.

## Нові питання

- Would a bounded higher-tier light-tank packet reuse radio spotting while
  adding role-specific assistance scoring without changing Standard Battle?
- Does a later armoured game reuse aggregate-plus-component damage but remove
  shared detection or base capture?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0212` — Half-Life 2.
- Optimisation criterion: continue Batch 009 in its recorded immutable order.
- Expected information gain: replace a sampled online team tank battle with an
  authored single-player physics-combat route and explicit chapter boundary.
- Backlog impact: fifth of nine authorised game units.

## Чому саме вона

- [Confirmed | Direct | High] Half-Life 2 is the next subject in
  `SEARCH_DEMAND_GAME_SELECTION_009`.

## Localisation status

- Ukrainian game, new-gene and combination entries are reviewed in this unit.
- The canonical product title remains `World of Tanks`; explanatory Ukrainian
  prose uses natural tank terminology and preserves exact official mode, tank,
  update and platform labels only where evidence requires them.

## Open questions

- Re-check the current update, client manifest, starting MS-1 availability and
  Standard Battle capture/reset wording on future review-on-touch.
