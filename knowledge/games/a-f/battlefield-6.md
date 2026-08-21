---
game_id: GAME-0149
slug: battlefield-6
game_title: Battlefield 6
analysis_status: reviewed
reviewed: 2026-08-21
combination_ids:
  - COMB-0147
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-184
    - ACT-187
    - ACT-190
    - ACT-201
    - ACT-215
    - ACT-240
    - ACT-241
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
  constraint:
    - CON-262
    - CON-269
    - CON-272
    - CON-288
    - CON-346
    - CON-347
    - CON-348
  information:
    - INF-073
    - INF-115
    - INF-116
    - INF-119
    - INF-155
  objective:
    - OBJ-079
  time:
    - TIM-003
---

# Game: Battlefield 6

## Analysis scope

- Version / ruleset: PC Game Update `1.4.2.0`, live from 2026-08-18 and
  reviewed 2026-08-21; one standard official Open Weapons Conquest match on
  Liberation Peak, with default 1,000 reinforcement tickets per team.
- Included: four-person squads; Assault, Engineer, Support and Recon class
  loadouts; direct infantry and vehicle movement; firearms, reloads and
  grenades; class gadgets and Training Paths; pings, voice and text; partial
  sight and sound; downing, dragging, revival, bleedout and timed redeployment;
  headquarters, held objectives, squadmates, beacons and vehicles as spawn
  sources; point capture and contest; vehicle damage and repair; tactical
  destruction; ticket loss from unrevived deaths and held objectives; the
  first team reaching zero tickets.
- Excluded: Campaign, REDSEC and Battle Royale; Portal, custom and Casual
  experiences; Initiation bots; Rush, Breakthrough, Escalation, Obliteration,
  tactical modes and limited-time events; Closed Weapons; other maps and
  map-specific naval rules; Career, Hardware and Battle Pass progression;
  assignments, cosmetics, store, anti-cheat, matchmaking and post-match rewards.
- Direct-play status: no authenticated live match was played. Current official
  update, mode, class, loadout, squad, vehicle and destruction documentation was
  inspected and combined into a repository-side deterministic transition trace.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `BF6-001` | Update 1.4.2.0 is the current live PC boundary and standard Conquest starts each team with 1,000 reinforcements | Confirmed | Corroborated | High | P1, P2 |
| `BF6-002` | Conquest captures a point through eligible friendly presence, halts progress while both teams contest it and transfers ownership after the required hold | Confirmed | Direct | High | P2, P3 |
| `BF6-003` | An unrevived death removes one team reinforcement while every held point repeatedly drains one reinforcement from the opposing team | Confirmed | Direct | High | P2, P3 |
| `BF6-004` | A downed squadmate may be dragged and revived by any class; Support can revive any teammate and has faster or instant options | Confirmed | Corroborated | High | P4, P5, P6 |
| `BF6-005` | Four classes bind distinct gadgets, signature traits and Training Paths to a configurable weapon, gadget and grenade loadout | Confirmed | Corroborated | High | P4, P7 |
| `BF6-006` | Redeployment can use eligible team objectives, squad sources, Spawn Beacons or available vehicle seats, subject to timing and combat state | Observation | Corroborated | High | P5, P8, P9 |
| `BF6-007` | Directly operated vehicles combine seats, movement, weapon fire, damage and Engineer repair with infantry objective capture | Confirmed | Corroborated | High | P3, P6, P9 |
| `BF6-008` | Eligible structures and cover can be destroyed to open routes or sightlines while the authored combat zone and objective anchors remain usable | Confirmed | Corroborated | High | P10, P11 |
| `BF6-009` | The repository trace reproduces loadout, deployment, capture, contest, downing, revival, ticket drain, vehicle repair, destruction and both zero-ticket outcomes | Observation | Direct | High | V1 |

## Basic data

- Release / origin: Battlefield Studios and Electronic Arts; released
  2025-10-10 and maintained as a live service.
- Platform or physical form: networked PC and console first-person shooter;
  this scope uses the current PC official multiplayer rules.
- Puzzle family: squad-based combined-arms territory control under partial
  information and shared finite reinforcements.
- Primary sources:
  - **[P1]** [official Game Update 1.4.2.0 notes](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-4-2-0),
    for the current 2026-08-18 live boundary.
  - **[P2]** [official mode guide](https://www.ea.com/games/battlefield/battlefield-6/news/modes),
    for default tickets, capture, contest, point drain, revival and terminal state.
  - **[P3]** [official Open Beta and Conquest guide](https://www.ea.com/games/battlefield/battlefield-6/news/everything-you-need-to-know-for-the-open-beta),
    for Liberation Peak, Conquest control, combined arms and ticket effects.
  - **[P4]** [official class overview](https://www.ea.com/games/battlefield/battlefield-6/features/classes),
    for the four roles and their distinct equipment boundaries.
  - **[P5]** [official new-player guide](https://www.ea.com/games/battlefield/battlefield-6/news/new-player-guide-to-battlefield-6),
    for squad revival, Support authority, dragging and reduced-health return.
  - **[P6]** [official initiation guide](https://www.ea.com/games/battlefield/battlefield-6/news/how-to-complete-initiation-challenges),
    for objective capture from vehicles, beacons, vehicle deployment, repair,
    resupply, spotting and revival.
  - **[P7]** [official Season 4 loadout guide](https://www.ea.com/games/battlefield/battlefield-6/news/loadout-creation-and-weapon-classes),
    for class-bound Training Paths, gadgets, grenades, weapons and attachments.
  - **[P8]** [official Assault guide](https://www.ea.com/games/battlefield/battlefield-6/news/assault-class),
    for Deploy Beacon, objective capture, squad spawn and combat-state gating.
  - **[P9]** [official EA vehicle guide](https://help.ea.com/en/articles/battlefield/battlefield-6/vehicles-guide/),
    for seats, deployment, direct operation, weapons, damage and repair.
  - **[P10]** [official Battlefield 6 feature overview](https://www.ea.com/games/battlefield/battlefield-6/features),
    for tactical destruction as a current core system.
  - **[P11]** [official Frostbite destruction retrospective](https://www.ea.com/news/how-battlefield-6-redefined-destruction),
    for tactical cover, route and combat-flow changes from authored destruction.
- Secondary sources: none admitted.
- Reproducible control:
  - **[V1]** repository-side state trace derived from `P1`–`P11`; it is rules
    reasoning rather than a claim of direct play.
- Claim IDs: `BF6-001`–`BF6-009`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, direct soldier movement; `ACT-161`, aimed firearm,
  melee or launcher attack; `ACT-164`, switch carried weapon or gadget;
  `ACT-183`, reload; `ACT-184`, throw a tactical grenade; `ACT-187`, send a
  live squad/team cue; `ACT-190`, activate a targeted or untargeted gadget;
  `ACT-201`, enter, drive, fly, fire from and leave a vehicle; `ACT-215`,
  configure a bounded compatible combat loadout.
- New genes: `ACT-240`, select a legal deployment source and redeploy;
  `ACT-241`, drag
  and revive one eligible downed ally.
- Parameters: class, Training Path, weapon, attachments, gadget, grenade,
  spawn source, seat, revive duration, movement stance and communication channel.
- Claim IDs: `BF6-004`–`BF6-007`.

### System Behaviour Genes

- Existing genes: `SYS-208`, resolve aimed fire through range, cover, armour
  and body hit; `SYS-215`, live hostile combat; `SYS-292`, grenade trajectory
  and typed field; `SYS-320`, occupied vehicle motion and damage; `SYS-382`,
  timed return after knockout; `SYS-386`, tactical destruction of eligible
  geometry; `SYS-380`, resolve a typed live ability or gadget effect.
- New genes: `SYS-394`, resolve downing,
  revival, bleedout and the resulting ticketed death; `SYS-395`, convert point
  occupancy into neutralisation, contest and ownership; `SYS-396`, aggregate
  unrevived deaths and held-point drain into team tickets and terminal result.
- Resolution order: live damage may down a soldier; a completed revive restores
  control without ticket loss, while bleedout or give-up commits death and one
  ticket; redeployment waits for a legal source; simultaneous point occupancy
  updates capture or contest; owned points drain the opponent until one ticket
  pool reaches zero.
- Parameters: damage, gadget, repair rate, downed window, capture rate, point
  ownership, drain cadence, ticket value and terminal tie handling.
- Claim IDs: `BF6-002`–`BF6-009`.

### Constraint Genes

- Existing genes: `CON-262`, weapon, gadget, grenade and ammunition capacity;
  `CON-269`, gadget target, charge and cooldown legality; `CON-272`, no direct
  control while dead and waiting to redeploy; `CON-288`, vehicle seat,
  operating state and geometry legality.
- New genes: `CON-346`, loadout components must fit the selected class and
  unlocked Open Weapons rules; `CON-347`, redeployment requires an elapsed
  timer and a currently legal headquarters, objective, squad, beacon or vehicle
  source; `CON-348`, point progress requires eligible friendly presence and
  stops under opposing contest.
- Scarce strategic resources: team tickets, living squad members, legal spawn
  sources, point ownership, vehicle availability and health, ammunition,
  gadget charges, grenades, cover and safe revive time.
- Claim IDs: `BF6-001`–`BF6-007`.

### Information Genes

- Existing genes: `INF-073`, carried weapon, gadget and ammunition state;
  `INF-115`, partial opponents through local sight and sound; `INF-116`, allied
  radar, score and objective state; `INF-119`, personal health, class, status
  and gadget readiness.
- New gene: `INF-155`, the deployment map exposes current objectives, squad
  sources, beacons, vehicles and source legality before redeployment.
- Claim IDs: `BF6-002`, `BF6-004`–`BF6-007`.

### Objective Genes

- New gene: `OBJ-079`, deplete the opposing Conquest reinforcement pool before
  the allied pool reaches zero.
- Success, evaluation and failure: the shared team result is awarded when one
  ticket pool reaches zero; personal kills or captures matter only through
  their effect on the team state.
- Claim IDs: `BF6-001`–`BF6-003`.

### Time Genes

- Existing gene: `TIM-003`, movement, combat, revival, capture, vehicle state
  and ticket drain continue in real time while players act.
- Parameters: simulation tick, revive channel, respawn timer, capture duration
  and ticket-drain cadence.
- Claim IDs: `BF6-002`–`BF6-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Assault class is selected before deployment | Configure an Open Weapons loadout with one Training Path, primary, secondary, two gadgets and grenade | Compatible equipment becomes the next soldier life's active kit | class remains a causal equipment boundary even with open primary weapons | `BF6-005` |
| Redeployment timer has ended and one held objective is safe | Select that objective on the deployment map | Soldier enters at the objective with the configured class loadout | owned territory is also a reinforcement source | `BF6-006` |
| Equivalent timer state but a squadmate is in combat | Select that squadmate | Deployment remains unavailable until the combat-state gate clears | squad proximity is not an unconditional teleport | `BF6-006` |
| Ally is downed inside the revival window | Drag behind cover and complete revive | Ally returns with reduced health and no team ticket is removed | revival preserves the shared finite resource | `BF6-003`, `BF6-004` |
| Downed window expires or the player gives up | Do not complete a revive | Death is committed, one allied ticket is removed and redeployment begins | downing and ticket loss are distinct transitions | `BF6-003`, `BF6-004` |
| Neutral or enemy point contains only eligible allied soldiers | Remain inside its capture area | Progress neutralises enemy ownership and then establishes allied ownership | physical presence converts into strategic territory | `BF6-002` |
| Both teams occupy that capture area | Continue contesting | Capture progress halts until opposing presence clears | eliminations matter through occupancy, not as an alternate point claim | `BF6-002` |
| Allied team owns more objectives | Maintain control | Each held point repeatedly removes tickets from the opposing pool | territory applies continuous shared-resource pressure | `BF6-003` |
| Damaged friendly tank is reachable by an Engineer | Hold the Repair Tool on the vehicle | Vehicle health is restored while the channel and target remain legal | class equipment preserves a finite combined-arms asset | `BF6-005`, `BF6-007` |
| Destructible wall protects an occupied firing angle | Apply sufficient explosive or vehicle impact | Wall fractures or collapses and changes cover/path state | destruction is tactical state mutation, not presentation | `BF6-008` |
| Opposing ticket pool reaches zero | No further action is required | Match resolves as allied victory; the inverse state is defeat | Conquest has one finite team terminal predicate | `BF6-001`, `BF6-003` |

## Strategic and experiential structure

- Local decision: expose for a shot, cross open ground, spend a grenade or
  gadget, revive under fire, repair a vehicle, remain in capture radius or
  redeploy into another tactical angle.
- Medium-term planning: compose complementary squad roles, maintain a viable
  forward spawn, preserve vehicles, rotate between points and choose whether a
  risky revive saves more tickets than it is likely to cost.
- Long-term structure: convert map control into sustained ticket advantage,
  deny enemy reinforcement routes and avoid trading unrevived deaths faster
  than held objectives drain the opponent.
- Common heuristics: keep one Support near the push, give vehicles Engineer
  coverage, contest before a point finishes flipping, spawn on safe squad
  sources and destroy cover only when the new angle benefits the team.
- Failure attribution: ticket and point states are visible and deaths/revives
  are locally traceable; hidden opponents, simultaneous squads and long-range
  vehicle threats make individual causal attribution incomplete.
- Player-trust factors: explicit point/ticket feedback and deterministic revive
  preservation are strong; matchmaking and network quality are outside scope.
- Claim IDs: `BF6-002`–`BF6-008`.

## Replay and variation

- What changes between sessions: team and squad composition, chosen classes,
  loadouts, vehicle use, point routes, local destruction, spawn network and the
  temporal balance between death loss and objective drain.
- Randomness or procedural generation: Liberation Peak geometry and Conquest
  points are authored; human simultaneous choice, weapon dispersion and live
  destruction create the meaningful variation.
- Multiple viable strategies: infantry swarms, vehicle-supported pushes,
  dispersed back-captures, defended point clusters, aerial pressure and
  squad-beacon flanks trade mobility, sustain and ticket efficiency.
- Typical replay motive: improve combined-arms execution and discover a better
  class, vehicle, spawn and objective response to changing team state.
- Claim IDs: `BF6-002`–`BF6-008`.

## Adjacent systems and history

- Direct predecessors: Battlefield 1942 through Battlefield 2042 establish the
  series' Conquest lineage of control points, tickets, squads and vehicles.
- Variants: Closed Weapons narrows primary selection; Breakthrough and Rush
  create asymmetric sectors or M-COMs; Portal permits authored rule changes.
- Similar games: Counter-Strike 2, PUBG: BATTLEGROUNDS, Marvel Rivals, Delta
  Force and other objective or combined-arms shooters.
- Important differences: the scoped match does not use one-life rounds,
  last-survivor elimination or capture-to-escort. It repeatedly converts
  squad deployment, revival, vehicle preservation and simultaneous territory
  ownership into one shared ticket resource.
- Claim IDs: `BF6-001`–`BF6-008`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-187`, `ACT-190`, `ACT-201`, `ACT-215`–`ACT-241` | exact bindings, weapon identities and callout vocabulary are parameters |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-292`, `SYS-320`, `SYS-382`, `SYS-386`, `SYS-380`–`SYS-396` | numeric damage, repair, capture and drain values are parameters |
| Constraint | `CON-262`, `CON-269`, `CON-272`, `CON-288`, `CON-346`–`CON-348` | point geometry, ticket count and timers are parameters |
| Information | `INF-073`, `INF-115`, `INF-116`, `INF-119`, `INF-155` | HUD placement and audiovisual presentation are excluded |
| Objective | `OBJ-079` | team side and initial ticket value are parameters |
| Time | `TIM-003` | all admitted match transitions remain live |

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`: `ACT-008,ACT-161,ACT-164,ACT-183,ACT-184,ACT-187,ACT-190,ACT-201,ACT-215,ACT-240,ACT-241; SYS-208,SYS-215,SYS-292,SYS-320,SYS-382,SYS-386,SYS-380,SYS-394,SYS-395,SYS-396; CON-262,CON-269,CON-272,CON-288,CON-346,CON-347,CON-348; INF-073,INF-115,INF-116,INF-119,INF-155; OBJ-079; TIM-003`.
- Indexed games scanned: all 148 earlier canonical games.
- Indexed combinations scanned: all 146 earlier verified combinations.
- Exact genome matches: none.
- Near match: Counter-Strike 2 (`GAME-0137`) at
  `14 / 51 = 0.274510`.
- Supported prior combination subsets: none; new
  `COMB-0147` is a strict subset of this 35-gene genome.
- Scan date: 2026-08-21.

Exhaustive prior-game ledger:

- GAME-0001: 0 / 49 = 0.000000; GAME-0002: 0 / 42 = 0.000000; GAME-0003: 0 / 44 = 0.000000; GAME-0004: 1 / 49 = 0.020408.
- GAME-0005: 0 / 42 = 0.000000; GAME-0006: 1 / 43 = 0.023256; GAME-0007: 0 / 43 = 0.000000; GAME-0008: 0 / 42 = 0.000000.
- GAME-0009: 0 / 51 = 0.000000; GAME-0010: 0 / 44 = 0.000000; GAME-0011: 0 / 48 = 0.000000; GAME-0012: 0 / 44 = 0.000000.
- GAME-0013: 0 / 48 = 0.000000; GAME-0014: 0 / 50 = 0.000000; GAME-0015: 0 / 49 = 0.000000; GAME-0016: 1 / 49 = 0.020408.
- GAME-0017: 0 / 48 = 0.000000; GAME-0018: 1 / 53 = 0.018868; GAME-0019: 0 / 45 = 0.000000; GAME-0020: 0 / 49 = 0.000000.
- GAME-0021: 1 / 43 = 0.023256; GAME-0022: 0 / 47 = 0.000000; GAME-0023: 0 / 45 = 0.000000; GAME-0024: 1 / 46 = 0.021739.
- GAME-0025: 1 / 45 = 0.022222; GAME-0026: 1 / 46 = 0.021739; GAME-0027: 1 / 46 = 0.021739; GAME-0028: 1 / 51 = 0.019608.
- GAME-0029: 2 / 45 = 0.044444; GAME-0030: 1 / 48 = 0.020833; GAME-0031: 0 / 46 = 0.000000; GAME-0032: 0 / 46 = 0.000000.
- GAME-0033: 2 / 46 = 0.043478; GAME-0034: 2 / 47 = 0.042553; GAME-0035: 2 / 51 = 0.039216; GAME-0036: 1 / 46 = 0.021739.
- GAME-0037: 0 / 44 = 0.000000; GAME-0038: 2 / 49 = 0.040816; GAME-0039: 0 / 44 = 0.000000; GAME-0040: 1 / 42 = 0.023810.
- GAME-0041: 2 / 44 = 0.045455; GAME-0042: 0 / 44 = 0.000000; GAME-0043: 1 / 48 = 0.020833; GAME-0044: 1 / 44 = 0.022727.
- GAME-0045: 1 / 48 = 0.020833; GAME-0046: 0 / 45 = 0.000000; GAME-0047: 0 / 49 = 0.000000; GAME-0048: 0 / 49 = 0.000000.
- GAME-0049: 0 / 44 = 0.000000; GAME-0050: 1 / 49 = 0.020408; GAME-0051: 1 / 50 = 0.020000; GAME-0052: 0 / 45 = 0.000000.
- GAME-0053: 1 / 43 = 0.023256; GAME-0054: 1 / 45 = 0.022222; GAME-0055: 1 / 44 = 0.022727; GAME-0056: 0 / 43 = 0.000000.
- GAME-0057: 0 / 43 = 0.000000; GAME-0058: 0 / 44 = 0.000000; GAME-0059: 0 / 42 = 0.000000; GAME-0060: 0 / 42 = 0.000000.
- GAME-0061: 0 / 45 = 0.000000; GAME-0062: 0 / 43 = 0.000000; GAME-0063: 0 / 42 = 0.000000; GAME-0064: 0 / 40 = 0.000000.
- GAME-0065: 0 / 42 = 0.000000; GAME-0066: 0 / 45 = 0.000000; GAME-0067: 0 / 43 = 0.000000; GAME-0068: 0 / 43 = 0.000000.
- GAME-0069: 0 / 43 = 0.000000; GAME-0070: 0 / 43 = 0.000000; GAME-0071: 0 / 42 = 0.000000; GAME-0072: 0 / 43 = 0.000000.
- GAME-0073: 0 / 42 = 0.000000; GAME-0074: 0 / 44 = 0.000000; GAME-0075: 0 / 44 = 0.000000; GAME-0076: 0 / 42 = 0.000000.
- GAME-0077: 0 / 42 = 0.000000; GAME-0078: 0 / 42 = 0.000000; GAME-0079: 0 / 42 = 0.000000; GAME-0080: 0 / 42 = 0.000000.
- GAME-0081: 0 / 43 = 0.000000; GAME-0082: 0 / 43 = 0.000000; GAME-0083: 0 / 43 = 0.000000; GAME-0084: 0 / 45 = 0.000000.
- GAME-0085: 0 / 46 = 0.000000; GAME-0086: 0 / 48 = 0.000000; GAME-0087: 1 / 44 = 0.022727; GAME-0088: 0 / 44 = 0.000000.
- GAME-0089: 0 / 44 = 0.000000; GAME-0090: 1 / 49 = 0.020408; GAME-0091: 2 / 42 = 0.047619; GAME-0092: 1 / 44 = 0.022727.
- GAME-0093: 0 / 44 = 0.000000; GAME-0094: 2 / 43 = 0.046512; GAME-0095: 2 / 45 = 0.044444; GAME-0096: 2 / 43 = 0.046512.
- GAME-0097: 2 / 41 = 0.048780; GAME-0098: 2 / 40 = 0.050000; GAME-0099: 1 / 42 = 0.023810; GAME-0100: 1 / 45 = 0.022222.
- GAME-0101: 0 / 45 = 0.000000; GAME-0102: 0 / 42 = 0.000000; GAME-0103: 0 / 44 = 0.000000; GAME-0104: 1 / 43 = 0.023256.
- GAME-0105: 2 / 43 = 0.046512; GAME-0106: 0 / 42 = 0.000000; GAME-0107: 1 / 42 = 0.023810; GAME-0108: 1 / 44 = 0.022727.
- GAME-0109: 0 / 51 = 0.000000; GAME-0110: 1 / 42 = 0.023810; GAME-0111: 1 / 41 = 0.024390; GAME-0112: 2 / 41 = 0.048780.
- GAME-0113: 2 / 47 = 0.042553; GAME-0114: 1 / 41 = 0.024390; GAME-0115: 0 / 41 = 0.000000; GAME-0116: 2 / 39 = 0.051282.
- GAME-0117: 1 / 42 = 0.023810; GAME-0118: 1 / 50 = 0.020000; GAME-0119: 1 / 57 = 0.017544; GAME-0120: 0 / 64 = 0.000000.
- GAME-0121: 1 / 57 = 0.017544; GAME-0122: 1 / 49 = 0.020408; GAME-0123: 0 / 73 = 0.000000; GAME-0124: 1 / 81 = 0.012346.
- GAME-0125: 1 / 76 = 0.013158; GAME-0126: 1 / 77 = 0.012987; GAME-0127: 2 / 81 = 0.024691; GAME-0128: 1 / 50 = 0.020000.
- GAME-0129: 6 / 64 = 0.093750; GAME-0130: 1 / 87 = 0.011494; GAME-0131: 4 / 77 = 0.051948; GAME-0132: 1 / 85 = 0.011765.
- GAME-0133: 1 / 79 = 0.012658; GAME-0134: 1 / 85 = 0.011765; GAME-0135: 1 / 82 = 0.012195; GAME-0136: 1 / 94 = 0.010638.
- GAME-0137: 14 / 51 = 0.274510; GAME-0138: 7 / 63 = 0.111111; GAME-0139: 6 / 83 = 0.072289; GAME-0140: 15 / 63 = 0.238095.
- GAME-0141: 8 / 78 = 0.102564; GAME-0142: 8 / 78 = 0.102564; GAME-0143: 6 / 78 = 0.076923; GAME-0144: 5 / 65 = 0.076923.
- GAME-0145: 16 / 67 = 0.238806; GAME-0146: 15 / 84 = 0.178571; GAME-0147: 12 / 48 = 0.250000; GAME-0148: 7 / 71 = 0.098592.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Counter-Strike 2 (`GAME-0137`) | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-187`, `SYS-208`, `SYS-215`, `SYS-292`, `CON-262`, `INF-073`, `INF-115`, `INF-116`, `TIM-003` | one-life economy rounds and an asymmetric bomb deadline versus repeated class/squad redeployment, revival, vehicles and simultaneous point-to-ticket pressure | nearest, not exact; `14 / 51 = 0.274510` |

- New genes: `ACT-240`, `ACT-241`, `SYS-394`–`SYS-396`, `CON-346`–`CON-348`,
  `INF-155`, `OBJ-079`.
- Classification result: `New gene` and new combination of known and new genes.
- Evidence and reasoning: the distinctive boundary is the repeated conversion
  of class/squad deployment, reversible downing and simultaneous point control
  into one finite shared ticket pool, not firearm statistics or theme.

### Registry normalisation 006 score corrections

These recomputed values supersede the pre-normalisation fractions above:

- `GAME-0132`: `2 / 84 = 0.023810`
- `GAME-0138`: `8 / 62 = 0.129032`
- `GAME-0143`: `7 / 77 = 0.090909`
- `GAME-0147`: `14 / 46 = 0.304348`
- Current prior-corpus near match after normalisation 006: `GAME-0147`.

## Taxonomy impact

- Registry changes after normalisation: add ten bounded genes and `COMB-0147`;
  extend evidence for the twenty-five reused records.
- Taxonomy-change record: `TAXONOMY_CHANGE_012` and `TAXONOMY_CHANGE_013`.
- Candidate terms affected: suppression, attachment points, 1,000 tickets,
  four-player squad and exact point geometry remain parameters.

## Negative results

- No separate negative-result record. No prior claim, candidate or gene
  distinction was rejected.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Unrevived deaths and held points debit the same
  finite reinforcement pool, while completed revives prevent the death debit
  (`BF6-002`–`BF6-004`).
- [Confirmed | Corroborated | High] Class gadgets, squad spawn sources,
  vehicles and destructible cover jointly alter control-point access and
  sustain (`BF6-005`–`BF6-008`).

## Нові гени

- [Observation | Corroborated | High] Ten bounded genes cover deployment
  choice, drag-revive, downed
  settlement, point control, ticket aggregation and deployment information.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0147` — Squad combined arms convert
  contested territory and reversible deaths into reinforcement attrition.

## Зміни таксономії

- [Observation | Direct | High] Змін таксономії немає.

## Нові питання

- Will another analysed large-team shooter reuse the same revive-preserved
  ticket pool and point-ownership drain without Battlefield's vehicle layer?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] `GAME-0150` — Hollow Knight: Silksong.
- Optimisation criterion: continue the recorded demand-led tranche while
  moving from live large-team control to authored solo traversal progression.
- Expected information gain: crest/tool configuration, traversal gates,
  currency recovery, benches and boss-state progression.
- Backlog impact: advances the active 17-game Goal without skipping a unit.

## Чому саме вона

- [Hypothesis | Limited | High] Silksong should be mechanically distant from
  Conquest while testing reuse among action-platforming, recovery and
  metroidvania dependency records already present in the corpus.
