---
game_id: GAME-0147
slug: marvel-rivals
game_title: Marvel Rivals
analysis_status: reviewed
reviewed: 2026-08-21
combination_ids:
  - COMB-0145
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-187
    - ACT-190
    - ACT-237
  system:
    - SYS-215
    - SYS-380
    - SYS-381
    - SYS-382
    - SYS-383
    - SYS-384
    - SYS-385
    - SYS-386
  constraint:
    - CON-269
    - CON-272
    - CON-338
    - CON-339
    - CON-340
    - CON-341
  information:
    - INF-115
    - INF-119
    - INF-150
    - INF-151
  objective:
    - OBJ-078
  time:
    - TIM-003
---

# Game: Marvel Rivals

## Analysis scope

- Version / ruleset: public PC `Version 20260820`, Season 9.5, observed
  2026-08-21; one completed 6v6 Quick Match Convergence attack-side result on
  Shin-Shibuya, retaining at least one Luna Snow life from spawn selection to
  knockout or objective completion.
- Included: third-person hero movement and aim, primary attacks, damage and
  healing, cooldown abilities, ultimate energy, Vanguard/Duelist/Strategist
  roles, Season 9 Team-Up loadout selection, allied partner enhancement,
  health and Regenerative Shields, knockout, timed respawn and hero swap,
  team cues, opening capture, mission-vehicle escort and reversal, checkpoints,
  contest, overtime, destructible geometry and terminal win/loss.
- Excluded: Competitive ranks, draft bans and multi-round side swaps; Convoy,
  Domination, Arcade, Practice, AI, Custom and event modes; exhaustive heroes,
  maps and Team-Ups; Battle Pass, store, cosmetics, achievements, account
  progression, tournaments and post-match rewards.
- Direct-play status: no authenticated live match was played. Current official
  product, patch, hero, role, Team-Up and environment material was inspected;
  maintained mode documentation and the current official competition rules
  corroborate the bounded Convergence trace.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MRV-001` | Quick Match places two six-player teams into objective play; each player selects an available hero from one of three functional roles and may change hero in spawn | Observation | Corroborated | High | P1, P6, S1 |
| `MRV-002` | Season 9 lets a hero select one of two Team-Up partner loadouts; its base effect remains available and the enhanced effect requires that selected partner on the allied team | Observation | Corroborated | High | P3, P4, S2 |
| `MRV-003` | Luna Snow directly aims attacks that damage enemies or heal allies and uses cooldown-gated control, healing and movement abilities | Observation | Corroborated | High | P6, P7 |
| `MRV-004` | Damage and healing fill role-scaled ultimate energy; knockout blocks control until timed spawn-room return, where hero and Team-Up selection can change | Observation | Corroborated | High | P4, P6, S1 |
| `MRV-005` | Convergence orders an attacker capture phase before a proximity-driven escort whose vehicle stops under contest, accelerates with attackers, locks checkpoints and can reverse under defenders | Observation | Corroborated | High | P8, S1 |
| `MRV-006` | Active objective pressure can extend an expired clock into overtime; terminal route completion awards attack and cleared pressure after expiry awards defence | Observation | Corroborated | High | P8, S1 |
| `MRV-007` | Eligible arena structures can be destroyed to change cover and routes while essential geometry remains protected | Confirmed | Corroborated | High | P2, P5 |
| `MRV-008` | The repository control reproduces hero/loadout selection, base and enhanced Team-Up state, ability/ultimate gating, knockout/respawn, capture, escort, checkpoint, reversal, overtime and both terminal results | Observation | Direct | High | V1 |

## Basic data

- Release / origin: NetEase Games with Marvel Games; public release 2024,
  continuously updated.
- Platform or physical form: free-to-play networked PC and console client; this
  scope uses the PC Quick Match ruleset.
- Puzzle family: simultaneous team objective combat under partial local information.
- Primary sources:
  - **[P1]** [official game introduction](https://www.marvelrivals.com/news/official/20240320/40185_1144288.html),
    for 6v6 hero combat, Team-Up abilities and destructible environments.
  - **[P2]** [official environmental-destruction talk](https://www.marvelrivals.com/news/official/20240510/40185_1154481.html),
    for destructible versus essential geometry, changed cover and routes, state
    synchronisation and themed reconstruction.
  - **[P3]** [official Season 9 patch](https://www.marvelrivals.com/20260708/41525_1306959.html),
    for the ground-up Team-Up revamp and current season boundary.
  - **[P4]** [official Season 9 balance post](https://www.marvelrivals.com/20260706/41525_1306647.html),
    for role-specific ultimate-energy conversion, Team-Up partner effects and
    Regenerative Shields.
  - **[P5]** [official current patch notes](https://www.marvelrivals.com/20260819/41525_1311622.html),
    for the `Version 20260820` boundary observed on 2026-08-21.
  - **[P6]** [official Luna Snow hero page](https://www.marvelrivals.com/heroes/?id=1077f07b-2178-49d3-80be-d915de78d17c),
    for current Strategist role, health, movement, primary attack, cooldown kit,
    ultimate and Team-Up options.
  - **[P7]** [official hero-design talk](https://www.marvelrivals.com/devtalk/20240814/40954_1153281.html),
    for Vanguard, Duelist and Strategist combat-role boundaries.
  - **[P8]** [official Ignite 2026 Stage 1 rules](https://www.marvelrivals.com/Marvel_Rivals_Ignite_2026_Rules_Stage1_2026.5.9_V2.0.pdf),
    for the current Convergence, Convoy and Domination mode and map roster.
- Secondary and reproducible sources:
  - **[S1]** [maintained Convergence rules reference](https://marvelrivals.fandom.com/wiki/Convergence),
    for capture, escort, attacker-speed cap, defender reversal, checkpoints,
    contest and overtime edge conditions.
  - **[S2]** [maintained Season 9 Team-Up explanation](https://mobalytics.gg/marvel-rivals/guides/season-9-team-ups-explained),
    for the two loadout options, spawn-room changes and base-versus-enhanced effect.
  - **[V1]** repository-side transition trace derived from `P3`–`P8` and checked
    against `S1`–`S2`; it is executable rules reasoning, not direct-play evidence.
- Claim IDs: `MRV-001`–`MRV-008`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, directly navigate the selected hero; `ACT-161`,
  aim and commit a primary strike; `ACT-187`, transmit a team cue; `ACT-190`,
  cast one cooldown or ultimate ability.
- New gene: `ACT-237`, select or swap one available hero and Team-Up loadout in spawn.
- Parameters: hero, role, movement kit, attack form, ability target, cooldown,
  ultimate readiness, communication channel and Team-Up partner.
- Claim IDs: `MRV-001`–`MRV-004`.

### System Behaviour Genes

- Existing gene: `SYS-215`, resolve direct simultaneous hostile combat.
- New genes: `SYS-380`, resolve typed hero ability effects; `SYS-381`, convert
  live contribution into ultimate readiness and spend it; `SYS-382`, resolve
  knockout and timed spawn-room return; `SYS-383`, convert opening capture into
  escort; `SYS-384`, move or reverse the mission vehicle from team proximity;
  `SYS-385`, resolve overtime and the terminal Convergence result; `SYS-386`,
  destroy eligible arena geometry while preserving essential anchors.
- Resolution order: movement, attacks and abilities update live team state;
  lethal damage starts respawn; uncontested objective presence updates capture
  or vehicle position; checkpoints retain route progress and add time; expiry
  enters overtime only under legal pressure; completion or cleared pressure
  awards the match.
- Claim IDs: `MRV-003`–`MRV-007`.

### Constraint Genes

- Existing genes: `CON-269`, an ability requires legal target, range, resource
  and readiness; `CON-272`, knockout blocks hero control until respawn.
- New genes: `CON-338`, hero and Team-Up changes require legal spawn state and
  team uniqueness; `CON-339`, Team-Up enhancement requires the selected allied
  partner; `CON-340`, capture and escort obey ordered presence/contest gates;
  `CON-341`, overtime requires continuing legal objective pressure.
- Scarce strategic resources: health, Regenerative Shield, cooldowns, ultimate
  energy, living teammates, objective presence, line of sight, cover and match time.
- Claim IDs: `MRV-001`–`MRV-006`.

### Information Genes

- Existing genes: `INF-115`, local sight and sound expose partial opponent
  state; `INF-119`, the personal hero HUD exposes health, status, abilities and
  ultimate readiness.
- New genes: `INF-150`, the hero roster exposes roles, kits and Team-Up
  alternatives; `INF-151`, the match HUD exposes team, phase, clock, progress,
  checkpoint, contest, overtime and respawn state.
- Claim IDs: `MRV-001`–`MRV-006`.

### Objective Genes

- New gene: `OBJ-078`, win one Convergence match by completing the ordered
  capture-and-escort route or denying its completion through final overtime.
- Success, evaluation and failure: the attacking team wins on terminal vehicle
  arrival; defenders win when valid time ends without required capture or route
  completion. Eliminations and healing are means, not terminal scores.
- Claim IDs: `MRV-005`, `MRV-006`.

### Time Genes

- Existing gene: `TIM-003`, player input, combat, cooldowns, respawn, objective
  clocks and overtime progress in continuous real time.
- Parameters: attack cadence, cooldown, ultimate gain, respawn timer, capture
  rate, checkpoint award, vehicle speed, phase clock and overtime decay.
- Claim IDs: `MRV-003`–`MRV-006`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Spawn selection is open and Luna Snow is not occupied by an ally | Select Luna Snow and one offered Team-Up partner | The slot gains Luna's Strategist kit and the selected Team-Up base effect before leaving spawn | reversible match identity | `MRV-001`, `MRV-002`, `MRV-008` |
| Selected Team-Up base effect is active without its partner | Ally selects the designated partner | The enhanced effect becomes active while the partner remains on the allied team; losing the partner removes that enhancement | composition-gated loadout | `MRV-002`, `MRV-008` |
| Luna has a visible injured ally or reachable enemy | Fire Light & Dark Ice | The aimed projectile heals the eligible ally or damages the enemy according to target identity | one input has typed ally/enemy resolution | `MRV-003`, `MRV-008` |
| Ultimate energy is below its declared cost | Damage enemies or heal allies | Role-scaled contribution increases the meter; at cost, activation spends readiness and applies Fate of Both Worlds | earned ultimate cycle | `MRV-004`, `MRV-008` |
| Luna's health reaches zero | Accept ordinary knockout | Direct control ends, the respawn timer runs and the active spawn room returns hero-selection authority | reversible live defeat | `MRV-004`, `MRV-008` |
| Attackers occupy the opening mission area without a defender contest | Maintain area control | Capture advances; completion locks the phase, adds time and activates the mission vehicle | ordered phase transition | `MRV-005`, `MRV-008` |
| Active vehicle has one to three nearby attackers and no defender contest | Accompany the vehicle | It advances at the corresponding capped speed; a reached checkpoint locks minimum route progress and adds time | proximity-driven escort | `MRV-005`, `MRV-008` |
| No attacker accompanies the vehicle and defenders control its vicinity beyond a checkpoint | Hold defensive control | The vehicle reverses toward, but not through, the latest secured checkpoint | asymmetric route recovery | `MRV-005`, `MRV-008` |
| Objective clock reaches zero while attackers retain legal pressure | Continue contest | Overtime keeps the phase live; clearing that pressure awards defence, while terminal arrival awards attack | objective-conditioned horizon | `MRV-006`, `MRV-008` |
| A wall marked destructible separates a firing angle | Apply enough eligible impact | The wall fractures or disappears and changes local cover/path state while essential route anchors remain | mutable tactical geometry | `MRV-007`, `MRV-008` |

## Strategic and experiential structure

- Local decision: aim one projectile as damage or healing, manage cooldown and
  ultimate readiness, use cover, decide whether to contest or survive for regroup.
- Medium-term planning: maintain a workable role mix without a hard role queue,
  select a Team-Up partner that the allied roster can enhance, coordinate
  staggered respawns and decide when destructible geometry should open a route.
- Long-term structure: attackers convert area control into sequential escort
  checkpoints; defenders trade space and knockouts for clock until objective
  pressure can be cleared at expiry.
- Common heuristics: regroup rather than feed isolated knockouts, preserve
  support sightlines, contest only when the remaining clock makes it valuable,
  and stand near the vehicle only up to its useful attacker-speed cap.
- Failure attribution: health, cooldown, ultimate, team frames, objective
  progress and clock are visible; hidden opponent positions and simultaneous
  allied choices keep tactical causality partly inferred.
- Player-trust factors: objective progress and respawn are explicit, while
  network latency, matchmaking and anti-cheat are outside this mechanical scope.
- Claim IDs: `MRV-002`–`MRV-007`.

## Replay and variation

- What changes between sessions: the twelve players' hero selections, selected Team-Ups,
  player skill, team composition, path use, geometry destruction and fight timing.
- Randomness or procedural generation: the map and objective route are fixed;
  human simultaneous choice and matchmaking dominate variation.
- Multiple viable strategies: dive, ranged pressure, brawl, sustain and hybrid
  compositions exchange mobility, protection, burst, healing and objective uptime.
- Typical replay motive: master distinct hero kits and adapt composition and
  geometry use to changing allied and opposing selections.
- Claim IDs: `MRV-001`–`MRV-007`.

## Adjacent systems and history

- Direct predecessors: class-based arena shooters and attack/defend payload modes.
- Variants: Convoy omits the opening capture; Domination uses control progress;
  Competitive adds side, rank and format rules excluded here.
- Similar games: Overwatch 2, Paladins and other hero shooters; Dota 2 shares
  role-differentiated real-time hero abilities but uses command pathing, economy,
  levelling, item builds, lanes and an Ancient objective.
- Important differences: the scoped mode couples reversible spawn-room hero and
  Team-Up selection to a capture-then-escort objective and destructible arena geometry.
- Claim IDs: `MRV-001`–`MRV-007`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-187`, `ACT-190`, `ACT-237` | hero-specific attacks and abilities are parameters |
| System Behaviour | `SYS-215`, `SYS-380`–`SYS-386` | exact kit effects, route and geometry are parameters |
| Constraint | `CON-269`, `CON-272`, `CON-338`–`CON-341` | team composition, ranges and timers are parameters |
| Information | `INF-115`, `INF-119`, `INF-150`, `INF-151` | HUD placement and cosmetic effects are excluded |
| Objective | `OBJ-078` | attacker or defender side is a parameter |
| Time | `TIM-003` | all admitted transitions remain live |

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`: `ACT-008,ACT-161,ACT-187,ACT-190,ACT-237; SYS-215,SYS-380,SYS-381,SYS-382,SYS-383,SYS-384,SYS-385,SYS-386; CON-269,CON-272,CON-338,CON-339,CON-340,CON-341; INF-115,INF-119,INF-150,INF-151; OBJ-078; TIM-003`.
- Indexed games scanned: 146 (`GAME-0001`–`GAME-0146`).
- Indexed combinations scanned: 144 (`COMB-0001`–`COMB-0144`).
- Exact genome matches: none.
- Near match: Dota 2 (`GAME-0138`) at `7 / 53 = 0.132075`, sharing live
  hero abilities, team communication, ability gating and real-time progression.
- Supported prior combination subsets: none.
- Scan date: 2026-08-21.

Exhaustive prior-game ledger:

- GAME-0001: 0 / 39 = 0.000000; GAME-0002: 0 / 32 = 0.000000; GAME-0003: 0 / 34 = 0.000000; GAME-0004: 1 / 39 = 0.025641.
- GAME-0005: 0 / 32 = 0.000000; GAME-0006: 1 / 33 = 0.030303; GAME-0007: 0 / 33 = 0.000000; GAME-0008: 0 / 32 = 0.000000.
- GAME-0009: 0 / 41 = 0.000000; GAME-0010: 0 / 34 = 0.000000; GAME-0011: 0 / 38 = 0.000000; GAME-0012: 0 / 34 = 0.000000.
- GAME-0013: 0 / 38 = 0.000000; GAME-0014: 0 / 40 = 0.000000; GAME-0015: 0 / 39 = 0.000000; GAME-0016: 1 / 39 = 0.025641.
- GAME-0017: 0 / 38 = 0.000000; GAME-0018: 1 / 43 = 0.023256; GAME-0019: 0 / 35 = 0.000000; GAME-0020: 0 / 39 = 0.000000.
- GAME-0021: 1 / 33 = 0.030303; GAME-0022: 0 / 37 = 0.000000; GAME-0023: 0 / 35 = 0.000000; GAME-0024: 1 / 36 = 0.027778.
- GAME-0025: 1 / 35 = 0.028571; GAME-0026: 1 / 36 = 0.027778; GAME-0027: 1 / 36 = 0.027778; GAME-0028: 1 / 41 = 0.024390.
- GAME-0029: 2 / 35 = 0.057143; GAME-0030: 1 / 38 = 0.026316; GAME-0031: 0 / 36 = 0.000000; GAME-0032: 0 / 36 = 0.000000.
- GAME-0033: 2 / 36 = 0.055556; GAME-0034: 2 / 37 = 0.054054; GAME-0035: 2 / 41 = 0.048780; GAME-0036: 1 / 36 = 0.027778.
- GAME-0037: 0 / 34 = 0.000000; GAME-0038: 2 / 39 = 0.051282; GAME-0039: 0 / 34 = 0.000000; GAME-0040: 1 / 32 = 0.031250.
- GAME-0041: 2 / 34 = 0.058824; GAME-0042: 0 / 34 = 0.000000; GAME-0043: 1 / 38 = 0.026316; GAME-0044: 1 / 34 = 0.029412.
- GAME-0045: 1 / 38 = 0.026316; GAME-0046: 0 / 35 = 0.000000; GAME-0047: 0 / 39 = 0.000000; GAME-0048: 0 / 39 = 0.000000.
- GAME-0049: 0 / 34 = 0.000000; GAME-0050: 1 / 39 = 0.025641; GAME-0051: 1 / 40 = 0.025000; GAME-0052: 0 / 35 = 0.000000.
- GAME-0053: 1 / 33 = 0.030303; GAME-0054: 1 / 35 = 0.028571; GAME-0055: 1 / 34 = 0.029412; GAME-0056: 0 / 33 = 0.000000.
- GAME-0057: 0 / 33 = 0.000000; GAME-0058: 0 / 34 = 0.000000; GAME-0059: 0 / 32 = 0.000000; GAME-0060: 0 / 32 = 0.000000.
- GAME-0061: 0 / 35 = 0.000000; GAME-0062: 0 / 33 = 0.000000; GAME-0063: 0 / 32 = 0.000000; GAME-0064: 0 / 30 = 0.000000.
- GAME-0065: 0 / 32 = 0.000000; GAME-0066: 0 / 35 = 0.000000; GAME-0067: 0 / 33 = 0.000000; GAME-0068: 0 / 33 = 0.000000.
- GAME-0069: 0 / 33 = 0.000000; GAME-0070: 0 / 33 = 0.000000; GAME-0071: 0 / 32 = 0.000000; GAME-0072: 0 / 33 = 0.000000.
- GAME-0073: 0 / 32 = 0.000000; GAME-0074: 0 / 34 = 0.000000; GAME-0075: 0 / 34 = 0.000000; GAME-0076: 0 / 32 = 0.000000.
- GAME-0077: 0 / 32 = 0.000000; GAME-0078: 0 / 32 = 0.000000; GAME-0079: 0 / 32 = 0.000000; GAME-0080: 0 / 32 = 0.000000.
- GAME-0081: 0 / 33 = 0.000000; GAME-0082: 0 / 33 = 0.000000; GAME-0083: 0 / 33 = 0.000000; GAME-0084: 0 / 35 = 0.000000.
- GAME-0085: 0 / 36 = 0.000000; GAME-0086: 0 / 38 = 0.000000; GAME-0087: 1 / 34 = 0.029412; GAME-0088: 0 / 34 = 0.000000.
- GAME-0089: 0 / 34 = 0.000000; GAME-0090: 1 / 39 = 0.025641; GAME-0091: 2 / 32 = 0.062500; GAME-0092: 1 / 34 = 0.029412.
- GAME-0093: 0 / 34 = 0.000000; GAME-0094: 2 / 33 = 0.060606; GAME-0095: 2 / 35 = 0.057143; GAME-0096: 2 / 33 = 0.060606.
- GAME-0097: 2 / 31 = 0.064516; GAME-0098: 2 / 30 = 0.066667; GAME-0099: 1 / 32 = 0.031250; GAME-0100: 1 / 35 = 0.028571.
- GAME-0101: 0 / 35 = 0.000000; GAME-0102: 0 / 32 = 0.000000; GAME-0103: 0 / 34 = 0.000000; GAME-0104: 1 / 33 = 0.030303.
- GAME-0105: 2 / 33 = 0.060606; GAME-0106: 0 / 32 = 0.000000; GAME-0107: 1 / 32 = 0.031250; GAME-0108: 1 / 34 = 0.029412.
- GAME-0109: 0 / 41 = 0.000000; GAME-0110: 1 / 32 = 0.031250; GAME-0111: 1 / 31 = 0.032258; GAME-0112: 2 / 31 = 0.064516.
- GAME-0113: 2 / 37 = 0.054054; GAME-0114: 1 / 31 = 0.032258; GAME-0115: 0 / 31 = 0.000000; GAME-0116: 2 / 29 = 0.068966.
- GAME-0117: 1 / 32 = 0.031250; GAME-0118: 1 / 40 = 0.025000; GAME-0119: 1 / 47 = 0.021277; GAME-0120: 0 / 54 = 0.000000.
- GAME-0121: 1 / 47 = 0.021277; GAME-0122: 1 / 39 = 0.025641; GAME-0123: 0 / 63 = 0.000000; GAME-0124: 1 / 71 = 0.014085.
- GAME-0125: 1 / 66 = 0.015152; GAME-0126: 1 / 67 = 0.014925; GAME-0127: 1 / 72 = 0.013889; GAME-0128: 1 / 40 = 0.025000.
- GAME-0129: 4 / 56 = 0.071429; GAME-0130: 1 / 77 = 0.012987; GAME-0131: 4 / 67 = 0.059701; GAME-0132: 1 / 75 = 0.013333.
- GAME-0133: 1 / 69 = 0.014493; GAME-0134: 1 / 75 = 0.013333; GAME-0135: 1 / 72 = 0.013889; GAME-0136: 1 / 84 = 0.011905.
- GAME-0137: 6 / 49 = 0.122449; GAME-0138: 7 / 53 = 0.132075; GAME-0139: 4 / 75 = 0.053333; GAME-0140: 5 / 63 = 0.079365.
- GAME-0141: 5 / 71 = 0.070423; GAME-0142: 5 / 71 = 0.070423; GAME-0143: 5 / 69 = 0.072464; GAME-0144: 5 / 55 = 0.090909.
- GAME-0145: 7 / 66 = 0.106061; GAME-0146: 7 / 82 = 0.085366.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0138` — Dota 2 | `ACT-187`, `ACT-190`, `SYS-215`, `CON-269`, `CON-272`, `INF-119`, `TIM-003` | direct avatar aim, reversible spawn hero/Team-Up selection, no match economy or lanes, capture-to-escort route, overtime and destructible geometry | near match only; no prior combination recurs |

- New genes: `ACT-237`, `SYS-380`–`SYS-386`, `CON-338`–`CON-341`,
  `INF-150`, `INF-151`, `OBJ-078`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: the exhaustive prior-game scan found only five shared
  genes with Dota 2. No prior record combines spawn-reversible hero/Team-Up
  selection, typed healing/damage abilities, capture-before-escort control,
  vehicle reversal, contested overtime and mutable arena geometry.

## Taxonomy impact

- Registry changes: add fifteen stable records and extend seven existing
  definitions/evidence links; register `COMB-0145`.
- Taxonomy-change record: none; boundaries are additive and preserve prior uses.
- Candidate terms affected: none.

## Negative results

- No prior combination is a proper subset of the complete admitted genome.
- `ACT-188` is absent because Marvel Rivals permits hero changes in spawn rather
  than permanently committing a draft identity.
- `SYS-208` is absent because body-region and material-penetration resolution is
  not established as a defining complete-roster rule in this bounded scope.
- `INF-116` and `INF-121` are absent because their canonical radar/bomb and
  structure/economy boundaries do not fit the Convergence HUD.

## Delta summary

## Нові факти

- [Observation | Corroborated | High] Season 9.5 couples reversible spawn hero
  selection with a two-option, ally-enhanced Team-Up loadout (`MRV-001`, `MRV-002`).
- [Observation | Corroborated | High] Convergence orders mission-area capture
  before proximity-driven escort, checkpoint locking, reversal and overtime
  (`MRV-005`, `MRV-006`).
- [Confirmed | Corroborated | High] Destructible non-essential arena geometry
  changes tactical routes and cover (`MRV-007`).

## Нові гени

- [Observation | Corroborated | High] Fifteen bounded genes cover spawn
  selection, typed hero effects, ultimate, respawn, Convergence, destruction,
  Team-Up gates, HUD state and terminal objective.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0145` couples reversible hero/Team-Up
  configuration to live combat and ordered capture-to-escort control.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає.

## Нові питання

- Does another analysed hero shooter recur with the same partner-gated loadout
  and destructible capture-to-escort combination?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] `GAME-0148` — Baldur's Gate 3.
- Optimisation criterion: continue the recorded demand-led queue while moving
  from simultaneous team objective combat to persistent turn-based party choice.
- Expected information gain: party dialogue, dice checks, environmental turn
  combat, persistent quests and branching campaign outcomes.
- Backlog impact: advances the active 17-game Goal without skipping a unit.

## Чому саме вона

- [Hypothesis | Limited | High] Baldur's Gate 3 should strongly contrast the
  current live team-objective genome while testing recurrence with authored
  dialogue, tactical turns and persistent-build records already in the corpus.
