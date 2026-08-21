---
game_id: GAME-0140
slug: pubg-battlegrounds
game_title: "PUBG: BATTLEGROUNDS"
analysis_status: reviewed
reviewed: 2026-08-21
combination_ids:
  - COMB-0138
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-184
    - ACT-186
    - ACT-198
    - ACT-199
    - ACT-200
    - ACT-201
    - ACT-202
    - ACT-203
  system:
    - SYS-208
    - SYS-215
    - SYS-292
    - SYS-316
    - SYS-317
    - SYS-318
    - SYS-319
    - SYS-320
    - SYS-321
    - SYS-322
    - SYS-323
    - SYS-324
    - SYS-325
  constraint:
    - CON-262
    - CON-283
    - CON-284
    - CON-285
    - CON-286
    - CON-287
    - CON-288
    - CON-289
    - CON-290
    - CON-291
  information:
    - INF-073
    - INF-075
    - INF-115
    - INF-127
    - INF-128
    - INF-129
  objective:
    - OBJ-074
  time:
    - TIM-003
---

# Game: PUBG: BATTLEGROUNDS

## Analysis scope

- Version / ruleset: public PC Update 42.3, reviewed 2026-08-21; one ordinary
  Normal Match in Solo TPP on Erangel, from the starting aircraft through
  elimination or `Winner Winner Chicken Dinner`.
- Included: up-to-100-player or bot-filled matchmaking; variable aircraft path,
  jump and parachute; random world loot, equipment and attachments; firearm,
  melee and throwable combat; posture, local sight and sound; health, armour,
  healing and boost; land vehicles; care packages and Red Zones; Update 42.1
  Blue Zone pacing and time-exposure damage; Update 41.1 destructible Erangel
  terrain; permanent Solo defeat and last-survivor victory.
- Excluded: Duo, Squad, Recall and DBNO; Ranked, Casual, Arcade, Intense Battle
  Royale, Custom, Training and event modes; other maps and map-exclusive rules;
  progression, achievements, Survivor Pass, cosmetics, Workshop, esports,
  anti-cheat and post-match rating.
- Direct-play status: no complete direct match was played. Current official
  overview, Update 42.3 notes, map service and Blue Zone documentation establish
  the live boundary; official catalogue pages and maintained mechanical
  references corroborate inventory, consumables, attachments and vehicles.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PUBG-001` | Update 42.3 Normal Solo TPP on Erangel is a current selectable PC battle-royale route with up to 100 participants and occasional bot substitution | Confirmed | Corroborated | High | P1, P2, P4, P8 |
| `PUBG-002` | A variable aircraft exit and controlled parachute descent determine the player's initial position before any world loot is owned | Confirmed | Corroborated | High | P1, S1 |
| `PUBG-003` | Random ground loot, typed equipment slots, backpack capacity, ammunition and compatible attachments create a replaceable match-local loadout | Observation | Corroborated | High | P1, P6, S1, S2 |
| `PUBG-004` | Direct fire resolves cover, range, body region and degrading armour while stance, lean, reload and throwable timing alter exposure | Observation | Corroborated | High | P2, P6, S2 |
| `PUBG-005` | Timed medical items and boost trade temporary vulnerability and inventory capacity for immediate or gradual health recovery | Observation | Corroborated | High | S2, S3 |
| `PUBG-006` | Vehicles exchange fuel, noise and collision or exit risk for rapid rotation and mobile cover | Confirmed | Corroborated | High | P1, P2, P7, S4 |
| `PUBG-007` | Normal Match reveals successive safe areas, contracts the Blue Zone and now increases damage with continuous exposure rather than distance | Confirmed | Direct | High | P3 |
| `PUBG-008` | Care-package smoke and warned Red Zones create visible optional reward and hazard loci outside the core player encounter schedule | Observation | Corroborated | High | P1, S5 |
| `PUBG-009` | Erangel terrain can be excavated by declared tools and explosions into temporary tactical cover within fixed depth and surface limits | Confirmed | Direct | High | P9 |
| `PUBG-010` | In Solo, lethal defeat is terminal for that match; the last living participant receives the match victory | Confirmed | Corroborated | High | P1, P10 |

## Basic data

- Release / origin: PUBG Studios / KRAFTON; Windows 1.0 release, 2017; current
  free-to-play live service reviewed at PC Update 42.3.
- Platform or physical form: networked Windows PC client; Steam and Epic Games
  participants share the PC matchmaking environment.
- Puzzle family: stochastic one-life spatial survival under a contracting area.
- Primary sources:
  - **[P1]** [official gameplay overview](https://www.pubg.com/en-asia/game-info/overview),
    for 100-player framing, aircraft, parachute, loot, care package, vehicles,
    Blue Zone, Solo mode and last-survivor victory.
  - **[P2]** [official Update 42.3 notes](https://pubg.com/en/news/10885), for
    the current PC build, weapon state and firing from vehicles.
  - **[P3]** [official Blue Zone revamp](https://www.pubg.com/en/news/10280),
    for Normal Match phase pacing and exposure-duration damage.
  - **[P4]** [official Update 42.3 map service](https://pubg.com/en/news/10854),
    for fixed Erangel availability in EU and other selection regions.
  - **[P5]** [official Erangel page](https://www.pubg.com/en-asia/game-info/maps/erangel),
    for the scoped 8×8 terrain and current map identity.
  - **[P6]** [official weapon catalogue](https://www.pubg.com/en-asia/game-info/weapons/ar),
    for weapon classes and current carried firearm vocabulary.
  - **[P7]** [official vehicle catalogue](https://www.pubg.com/en-asia/game-info/vehicles/land),
    for the available land-vehicle system.
  - **[P8]** [official Steam product page](https://store.steampowered.com/app/578080/PUBG_BATTLEGROUNDS/),
    for release, publisher, platform and land-loot-survive framing.
  - **[P9]** [official Update 41.1 notes](https://pubg.com/en/news/9926), for
    Erangel destructible terrain, eligible tools and bounded exceptions.
  - **[P10]** [official PUBG support mode guide](https://support.pubg.com/hc/en-us/articles/115004198834-How-to-play-PUBG),
    for Solo last-person-standing rules and TPP/FPP distinction.
- Secondary sources:
  - **[S1]** [maintained gameplay overview](https://en.wikipedia.org/wiki/PUBG:_Battlegrounds),
    for variable flight path, empty start and procedural item distribution.
  - **[S2]** [maintained attachments reference](https://pubg.wiki.gg/wiki/Attachments),
    for compatibility and auto-equip transfer behaviour.
  - **[S3]** [maintained consumables reference](https://pubg.wiki.gg/wiki/Consumables),
    for timed, interruptible consumption and inventory removal.
  - **[S4]** [maintained vehicle reference](https://pubg.wiki.gg/wiki/Vehicles),
    for movement value, damage, collision and unsafe exit.
  - **[S5]** [maintained Normal rules reference](https://pubg.wiki.gg/wiki/Game_Modes/Custom/Guides/Normal_Mode),
    for explicit Blue/Red Zone and care-package parameters.
- Claim IDs: `PUBG-001`–`PUBG-010`.

## Mechanical decomposition

### Action Genes

- Existing gene IDs: `ACT-008`, direct avatar navigation; `ACT-161`, aimed
  melee or firearm attack; `ACT-164`, select active carried weapon or throwable;
  `ACT-183`, timed magazine reload; `ACT-184`, prime and throw grenade;
  `ACT-186`, drop carried match item.
- New genes: `ACT-198`, choose aircraft exit and steer descent; `ACT-199`,
  transfer and equip compatible world loot; `ACT-200`, use an interruptible
  restorative consumable; `ACT-201`, enter, operate, change seat or exit a
  vehicle; `ACT-202`, change combat posture or lean; `ACT-203`, excavate
  eligible terrain for cover.
- Parameters: input device, perspective, jump time, descent vector, item and
  slot, weapon, fire mode, reload time, stance, lean side, consumable cast,
  vehicle seat and terrain tool.
- Claim IDs: `PUBG-002`–`PUBG-006`, `PUBG-009`.

### System Behaviour Genes

- Existing gene IDs: `SYS-208`, resolve ranged attack through cover, armour and
  body hit; `SYS-215`, resolve direct live hostile combat; `SYS-292`, resolve
  tactical grenade trajectory and field effect.
- New genes: `SYS-316`, initialise the match's aircraft, participants, loot and
  vehicles; `SYS-317`, resolve freefall and parachute landing; `SYS-318`, apply
  compatible attachments and degrading regional armour; `SYS-319`, resolve
  cast healing and boost-over-time; `SYS-320`, simulate occupied vehicle motion,
  fuel, collision and damage; `SYS-321`, reveal and contract phased safe areas
  while applying Blue Zone exposure damage; `SYS-322`, fly and signal a care
  package; `SYS-323`, warn and bombard a random Red Zone; `SYS-324`, deform
  eligible terrain; `SYS-325`, convert lethal defeat into a death crate,
  survivor-count update and terminal winner.
- Resolution order: initialise aircraft and distributed match state; resolve
  exit/descent/landing; accept concurrent navigation, looting and combat while
  zones, vehicles and hazards advance; on lethal damage remove that participant
  and expose eligible carried loot; terminate when one participant remains.
- Parameters: participant fill, bot ratio, flight line, spawn tables, ballistics,
  armour, healing, vehicle physics, phase schedule, random circle centres,
  exposure duration, package and Red Zone schedules, terrain limits and winner.
- Claim IDs: `PUBG-001`–`PUBG-010`.

### Constraint Genes

- Existing gene IDs: `CON-262`, typed weapon, throwable and ammunition capacity.
- New genes: `CON-283`, insertion is bounded by aircraft route and descent
  reach; `CON-284`, backpack capacity and equipment slots bound the loadout;
  `CON-285`, weapon operation requires compatible ammunition, attachment and
  action state; `CON-286`, restorative use requires a legal health state and
  uninterrupted cast; `CON-287`, armour protects only its covered body region
  while durability remains; `CON-288`, vehicle operation requires a seat, fuel
  and traversable geometry and makes a moving exit hazardous; `CON-289`, phased
  safe areas impose escalating live deadlines; `CON-290`, Solo defeat permits
  no recall, revival or same-match respawn; `CON-291`, terrain deformation is
  limited by map, surface, tool, range and depth.
- Scarce strategic resources: landing time, safe-area travel time, concealed
  position, ammunition, magazine readiness, armour durability, backpack
  capacity, healing supplies, vehicle fuel and health, and participant life.
- Claim IDs: `PUBG-002`–`PUBG-010`.

### Information Genes

- Existing gene IDs: `INF-073`, carried equipment and active weapon are visible;
  `INF-075`, health and armour condition are visible; `INF-115`, local sight,
  sound and effects expose only partial opponent state.
- New genes: `INF-127`, the map and HUD expose current aircraft, safe-area,
  Blue/Red Zone and phase timing; `INF-128`, ground loot and inventory expose
  item identity, compatibility and remaining capacity; `INF-129`, alive count,
  kill feed and terminal result expose population loss without omniscient
  opponent positions.
- Claim IDs: `PUBG-002`–`PUBG-010`.

### Objective Genes

- New gene: `OBJ-074`, remain the last living Solo participant.
- Success, evaluation and failure: the sole remaining participant wins;
  ordinary kills, loot or placement do not independently satisfy the objective;
  lethal defeat ends the player's run.
- Claim IDs: `PUBG-010`.

### Time Genes

- Existing gene: `TIM-003`, real-time input during forced progression.
- Parameters: live combat, vehicle and hazard clocks; phase warnings and
  contraction durations; healing casts; no player pause.
- Claim IDs: `PUBG-003`–`PUBG-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Unarmed participant rides the current transport-aircraft line | Exit, choose fall vector and steer parachute | Gravity, drag and canopy control map exit timing into one reachable landing region | Aircraft route and descent are coupled positional commitments | `PUBG-002` |
| Compatible rifle, ammunition and attachment lie within interaction reach | Transfer the items and equip the rifle | Capacity accepts legal quantities; compatible attachment changes rifle state and rejected excess remains outside | Loot is a bounded, replaceable match loadout | `PUBG-003` |
| Rifle magazine is partly empty and compatible reserve ammunition remains | Commit reload | Fire readiness is surrendered until the timed transfer completes or is cancelled | Magazine readiness is an exposed live opportunity cost | `PUBG-003` |
| Opponent is partially visible beyond cover | Change posture or lean, aim and fire | Ballistics, cover, body region and armour resolve a miss or wound and reduce eligible armour durability | Exposure control and regional protection shape firefights | `PUBG-004` |
| Avatar is injured and owns a legal medical item | Begin use, then either preserve or break its channel | Completion consumes the item and restores the declared health state; cancelling action prevents the effect | Healing exchanges time, mobility and supply for survival | `PUBG-005` |
| Fuelled vehicle has an empty controllable seat | Enter and drive toward the shown safe area | Steering, terrain, speed, collision, fuel and vehicle damage update continuously; unsafe exit may injure the avatar | Rotation speed has physical and informational costs | `PUBG-006` |
| New safe circle is revealed while the avatar remains outside it | Rotate late or continue looting | Blue boundary contracts on schedule and exposure-duration damage escalates until entry, healing or death | The zone converts spatial uncertainty into a live deadline | `PUBG-007` |
| Eligible Erangel soil is exposed and the player has a valid tool or explosive | Strike or detonate the surface | Terrain is removed only inside supported depth, range and material limits, creating traversable cover | Current Erangel permits bounded player-authored terrain geometry | `PUBG-009` |
| Two Solo participants remain | One receives lethal legal damage | Defeated inventory becomes a death crate, alive count falls to one and the survivor receives victory | Elimination and last-survivor objective share one terminal transition | `PUBG-010` |

## Strategic and experiential structure

- Local decision: whether to expose, fire, reload, heal, loot, dig, enter a
  vehicle or preserve concealment given incomplete enemy state.
- Medium-term planning: choose a landing density, assemble a compatible
  loadout and secure a route or vehicle before the next revealed circle closes.
- Long-term structure: trade centre position against edge information and loot,
  preserve finite armour, healing and mobility, and repeatedly rotate until the
  terminal one-on-one or last uncontested survival state.
- Common heuristics: observe nearby parachutes, prioritise weapon/ammunition and
  protection, avoid silhouette exposure, rotate before terrain and Blue Zone
  eliminate route options, and treat red smoke or vehicle noise as shared
  information rather than free reward.
- Failure attribution: most deaths trace to landing density, exposure, aim,
  resource timing or rotation, but future circles, loot distribution and unseen
  opponents preserve material uncertainty.
- Player-trust factors: exact future loot, participant behaviour and circle
  centres remain hidden, while current zone, health, equipment, alive count and
  strong audiovisual events are exposed.
- Claim IDs: `PUBG-002`–`PUBG-010`.

## Replay and variation

- What changes between sessions: participants or bots, aircraft line, landing
  choices, world loot, vehicle locations, care packages, Red Zones, safe-area
  centres and combat encounters.
- Randomness or procedural generation: bounded stochastic match initialisation
  and live hazard or reward schedules over a persistent authored Erangel map.
- Multiple viable strategies: hot or remote drop, centre or edge play, foot or
  vehicle rotation, long- or short-range loadout, package contest or avoidance.
- Typical replay motive: variable spatial-information problems and opponent
  interactions under one-life stakes.
- Claim IDs: `PUBG-001`–`PUBG-010`.

## Adjacent systems and history

- Direct predecessors: Brendan Greene's earlier Battle Royale mods and H1Z1
  establish the last-person-standing lineage; this analysis does not assign
  their unreviewed mechanics to the corpus.
- Variants: Duo/Squad add team state, DBNO, revival and Recall; Ranked changes
  matchmaking and zone/economy assumptions; other maps add distinct features.
- Similar games: Counter-Strike 2 shares direct gunplay, inventory slots,
  reloading, grenades, one-life equipment loss and partial local information.
- Important differences: PUBG starts empty, commits a variable aerial landing,
  builds a random found loadout across an 8×8 map, contracts playable space and
  ends one continuous Solo life rather than resetting team rounds with economy.
- Claim IDs: `PUBG-001`–`PUBG-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-186`, `ACT-198`–`ACT-203` | exact controls and item mappings are parameters |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-292`, `SYS-316`–`SYS-325` | spawn probabilities and numeric physics are parameters |
| Constraint | `CON-262`, `CON-283`–`CON-291` | capacities, timers and damage values are parameters |
| Information | `INF-073`, `INF-075`, `INF-115`, `INF-127`–`INF-129` | HUD styling and audiovisual assets are presentation |
| Objective | `OBJ-074` | participant count is a parameter |
| Time | `TIM-003` | phase and cast durations are parameters |

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`: `ACT-008,ACT-161,ACT-164,ACT-183,ACT-184,ACT-186,ACT-198,ACT-199,ACT-200,ACT-201,ACT-202,ACT-203; SYS-208,SYS-215,SYS-292,SYS-316,SYS-317,SYS-318,SYS-319,SYS-320,SYS-321,SYS-322,SYS-323,SYS-324,SYS-325; CON-262,CON-283,CON-284,CON-285,CON-286,CON-287,CON-288,CON-289,CON-290,CON-291; INF-073,INF-075,INF-115,INF-127,INF-128,INF-129; OBJ-074; TIM-003`.
- Indexed games scanned: all 139 earlier canonical games.
- Indexed combinations scanned: all 137 earlier verified combinations.
- Exact genome matches: none.
- Near matches and similarity scores: Counter-Strike 2 (`GAME-0137`),
  `13 / 60 = 0.216667`.
- Supported combination subsets: none among the 137 earlier combinations;
  new `COMB-0138` is a strict 27-gene subset of this genome.
- Scan date: 2026-08-21.

Exhaustive prior-game ledger:

- GAME-0001: 0 / 57 = 0.000000; GAME-0002: 0 / 50 = 0.000000; GAME-0003: 0 / 52 = 0.000000; GAME-0004: 1 / 57 = 0.017544.
- GAME-0005: 0 / 50 = 0.000000; GAME-0006: 1 / 51 = 0.019608; GAME-0007: 0 / 51 = 0.000000; GAME-0008: 0 / 50 = 0.000000.
- GAME-0009: 0 / 59 = 0.000000; GAME-0010: 0 / 52 = 0.000000; GAME-0011: 0 / 56 = 0.000000; GAME-0012: 0 / 52 = 0.000000.
- GAME-0013: 0 / 56 = 0.000000; GAME-0014: 0 / 58 = 0.000000; GAME-0015: 0 / 57 = 0.000000; GAME-0016: 1 / 57 = 0.017544.
- GAME-0017: 0 / 56 = 0.000000; GAME-0018: 1 / 61 = 0.016393; GAME-0019: 0 / 53 = 0.000000; GAME-0020: 0 / 57 = 0.000000.
- GAME-0021: 1 / 51 = 0.019608; GAME-0022: 0 / 55 = 0.000000; GAME-0023: 0 / 53 = 0.000000; GAME-0024: 1 / 54 = 0.018519.
- GAME-0025: 1 / 53 = 0.018868; GAME-0026: 1 / 54 = 0.018519; GAME-0027: 1 / 54 = 0.018519; GAME-0028: 1 / 59 = 0.016949.
- GAME-0029: 2 / 53 = 0.037736; GAME-0030: 1 / 56 = 0.017857; GAME-0031: 0 / 54 = 0.000000; GAME-0032: 0 / 54 = 0.000000.
- GAME-0033: 2 / 54 = 0.037037; GAME-0034: 2 / 55 = 0.036364; GAME-0035: 2 / 59 = 0.033898; GAME-0036: 1 / 54 = 0.018519.
- GAME-0037: 0 / 52 = 0.000000; GAME-0038: 2 / 57 = 0.035088; GAME-0039: 0 / 52 = 0.000000; GAME-0040: 1 / 50 = 0.020000.
- GAME-0041: 2 / 52 = 0.038462; GAME-0042: 0 / 52 = 0.000000; GAME-0043: 1 / 56 = 0.017857; GAME-0044: 1 / 52 = 0.019231.
- GAME-0045: 1 / 56 = 0.017857; GAME-0046: 0 / 53 = 0.000000; GAME-0047: 0 / 57 = 0.000000; GAME-0048: 0 / 57 = 0.000000.
- GAME-0049: 0 / 52 = 0.000000; GAME-0050: 1 / 57 = 0.017544; GAME-0051: 1 / 58 = 0.017241; GAME-0052: 0 / 53 = 0.000000.
- GAME-0053: 1 / 51 = 0.019608; GAME-0054: 1 / 53 = 0.018868; GAME-0055: 1 / 52 = 0.019231; GAME-0056: 0 / 51 = 0.000000.
- GAME-0057: 0 / 51 = 0.000000; GAME-0058: 0 / 52 = 0.000000; GAME-0059: 0 / 50 = 0.000000; GAME-0060: 0 / 50 = 0.000000.
- GAME-0061: 0 / 53 = 0.000000; GAME-0062: 0 / 51 = 0.000000; GAME-0063: 0 / 50 = 0.000000; GAME-0064: 0 / 48 = 0.000000.
- GAME-0065: 0 / 50 = 0.000000; GAME-0066: 0 / 53 = 0.000000; GAME-0067: 0 / 51 = 0.000000; GAME-0068: 0 / 51 = 0.000000.
- GAME-0069: 0 / 51 = 0.000000; GAME-0070: 0 / 51 = 0.000000; GAME-0071: 0 / 50 = 0.000000; GAME-0072: 0 / 51 = 0.000000.
- GAME-0073: 0 / 50 = 0.000000; GAME-0074: 0 / 52 = 0.000000; GAME-0075: 0 / 52 = 0.000000; GAME-0076: 0 / 50 = 0.000000.
- GAME-0077: 0 / 50 = 0.000000; GAME-0078: 0 / 50 = 0.000000; GAME-0079: 0 / 50 = 0.000000; GAME-0080: 0 / 50 = 0.000000.
- GAME-0081: 0 / 51 = 0.000000; GAME-0082: 0 / 51 = 0.000000; GAME-0083: 0 / 51 = 0.000000; GAME-0084: 0 / 53 = 0.000000.
- GAME-0085: 0 / 54 = 0.000000; GAME-0086: 0 / 56 = 0.000000; GAME-0087: 1 / 52 = 0.019231; GAME-0088: 0 / 52 = 0.000000.
- GAME-0089: 0 / 52 = 0.000000; GAME-0090: 1 / 57 = 0.017544; GAME-0091: 2 / 50 = 0.040000; GAME-0092: 1 / 52 = 0.019231.
- GAME-0093: 0 / 52 = 0.000000; GAME-0094: 2 / 51 = 0.039216; GAME-0095: 2 / 53 = 0.037736; GAME-0096: 2 / 51 = 0.039216.
- GAME-0097: 2 / 49 = 0.040816; GAME-0098: 2 / 48 = 0.041667; GAME-0099: 1 / 50 = 0.020000; GAME-0100: 1 / 53 = 0.018868.
- GAME-0101: 0 / 53 = 0.000000; GAME-0102: 0 / 50 = 0.000000; GAME-0103: 0 / 52 = 0.000000; GAME-0104: 1 / 51 = 0.019608.
- GAME-0105: 2 / 51 = 0.039216; GAME-0106: 0 / 50 = 0.000000; GAME-0107: 1 / 50 = 0.020000; GAME-0108: 1 / 52 = 0.019231.
- GAME-0109: 0 / 59 = 0.000000; GAME-0110: 1 / 50 = 0.020000; GAME-0111: 1 / 49 = 0.020408; GAME-0112: 2 / 49 = 0.040816.
- GAME-0113: 2 / 55 = 0.036364; GAME-0114: 1 / 49 = 0.020408; GAME-0115: 0 / 49 = 0.000000; GAME-0116: 2 / 47 = 0.042553.
- GAME-0117: 1 / 50 = 0.020000; GAME-0118: 1 / 58 = 0.017241; GAME-0119: 1 / 65 = 0.015385; GAME-0120: 0 / 72 = 0.000000.
- GAME-0121: 1 / 65 = 0.015385; GAME-0122: 1 / 57 = 0.017544; GAME-0123: 0 / 81 = 0.000000; GAME-0124: 1 / 89 = 0.011236.
- GAME-0125: 1 / 84 = 0.011905; GAME-0126: 1 / 85 = 0.011765; GAME-0127: 2 / 89 = 0.022472; GAME-0128: 1 / 58 = 0.017241.
- GAME-0129: 7 / 71 = 0.098592; GAME-0130: 1 / 95 = 0.010526; GAME-0131: 4 / 85 = 0.047059; GAME-0132: 1 / 93 = 0.010753.
- GAME-0133: 1 / 87 = 0.011494; GAME-0134: 1 / 93 = 0.010753; GAME-0135: 1 / 90 = 0.011111; GAME-0136: 1 / 102 = 0.009804.
- GAME-0137: 13 / 60 = 0.216667; GAME-0138: 2 / 76 = 0.026316; GAME-0139: 7 / 90 = 0.077778.

Near matches are selected by the canonical formula. Detailed comparison is
limited to those records; ties are retained.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Counter-Strike 2 (`GAME-0137`) | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-186`, `SYS-208`, `SYS-215`, `SYS-292`, `CON-262`, `INF-073`, `INF-115`, `TIM-003` | one stochastic continuous life across landing, loot, vehicles and shrinking terrain versus fixed-team repeated bomb rounds with purchases, economy and role swap | nearest at `13 / 60 = 0.216667` |

- New genes: `ACT-198`–`ACT-203`, `SYS-316`–`SYS-325`, `CON-283`–`CON-291`,
  `INF-127`–`INF-129` and `OBJ-074` (29 total).
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: existing direct-combat genes preserve genuine reuse,
  while aerial commitment, random match loadout, drive/zone coupling, permanent
  Solo elimination and terrain excavation have distinct operational boundaries.

## Taxonomy impact

- Registry changes: add 29 bounded active genes and `COMB-0138`; reuse existing
  firearm, grenade, equipment-information and live-time records without changing
  their classifications.
- Taxonomy-change record: none.
- Candidate terms affected: battle royale, hot drop, rotation, circle luck and
  chicken dinner remain genre, strategy, parameter or presentation vocabulary.

## Negative results

- none.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] `PUBG-001`–`PUBG-010`: PC Update 42.3
  Normal Solo TPP on Erangel links variable aerial insertion and random loadout
  to phased zone pressure, permanent defeat and last-survivor victory.

## Нові гени

- [Observation | Corroborated | High] Added `ACT-198`–`ACT-203`,
  `SYS-316`–`SYS-325`, `CON-283`–`CON-291`, `INF-127`–`INF-129` and `OBJ-074`.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0138` — one-life aerial insertion,
  stochastic loadout and contracting-area survival.

## Зміни таксономії

- [Observation | Direct | High] Змін таксономії немає.

## Нові питання

- How much battle-royale recurrence will `GAME-0143` ARC Raiders expose once its
  extraction, persistence and team boundaries receive the same decomposition?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] `GAME-0141` — Rust.
- Optimisation criterion: preserve the authorised search-demand sequence.
- Expected information gain: contrast one-match stochastic survival with a
  persistent multiplayer world, construction, upkeep, raiding and offline risk.
- Backlog impact: advances the current 17-game Goal by one independent unit.

## Чому саме вона

- [Hypothesis | Limited | High] Rust should reuse embodied survival, direct
  combat and inventory genes while testing whether persistent ownership,
  upkeep and asynchronous player threat require bounded new records.
