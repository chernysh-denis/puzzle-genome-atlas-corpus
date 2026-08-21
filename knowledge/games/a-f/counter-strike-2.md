---
game_id: GAME-0137
slug: counter-strike-2
game_title: Counter-Strike 2
analysis_status: reviewed
reviewed: 2026-08-21
combination_ids:
  - COMB-0135
gene_ids:
  action:
    - ACT-008
    - ACT-130
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-184
    - ACT-185
    - ACT-186
    - ACT-187
  system:
    - SYS-208
    - SYS-215
    - SYS-222
    - SYS-292
    - SYS-293
    - SYS-294
    - SYS-295
    - SYS-296
  constraint:
    - CON-261
    - CON-262
    - CON-263
    - CON-264
    - CON-265
    - CON-266
    - CON-267
  information:
    - INF-073
    - INF-115
    - INF-116
    - INF-117
  objective:
    - OBJ-071
  time:
    - TIM-003
---

# Game: Counter-Strike 2

## Analysis scope

- Version / ruleset: public Windows Counter-Strike 2 build and Competitive
  configuration observed 2026-08-21; one ordinary 5v5 bomb-defusal map under
  24-round MR12 regulation, with no overtime.
- Included: first-person movement, weapon selection, firearm/knife attacks,
  reloads, grenades, armour and hit groups, one life per round, dropped-item
  pickup, buy time and cross-round economy, team communication, C4 plant,
  defuse and explosion, halftime side swap, thirteen-round clinch and 12–12 draw.
- Excluded: Premier rating and overtime, per-map Competitive Skill Groups,
  Casual, Wingman, Retakes, Deathmatch, Arms Race, hostage maps, community
  servers, workshop maps, tournament series, anti-cheat, cosmetics, inventory
  trading, Armory progression and esports administration.
- Direct-play status: no complete direct match was played for this analysis.
  Valve's live configuration snapshot was inspected as executable rules data;
  official Valve product/update material and a current competitive rulebook
  independently corroborate the bounded transitions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CS2-001` | Current Competitive uses 24 regulation rounds, halftime, $800 starts, a $16,000 cap, 20-second buy time, friendly fire and no same-round respawn | Confirmed | Corroborated | High | P2, S1 |
| `CS2-002` | A defusal round is asymmetric: attackers may plant C4 at a site; defenders win an unplanted timeout or may defuse a plant; an explosion awards attackers | Confirmed | Corroborated | High | P2, S1, S2 |
| `CS2-003` | Kills, objective actions, team result, surviving gear and consecutive losses couple adjacent rounds through economy | Confirmed | Corroborated | High | P2, P4, S1 |
| `CS2-004` | Firearms resolve aim, range/material interaction, armour and hit groups while grenades create typed spatial effects | Confirmed | Corroborated | High | P3, P5, S2 |
| `CS2-005` | Local sight and spatial sound leave opponent state incomplete; radar, HUD and voluntary team cues combine partial team knowledge | Observation | Corroborated | High | P1, P3, S2 |
| `CS2-006` | The bounded control reproduces purchases, a save decision, equipment transfer, elimination, plant, interrupted and successful defuse, explosion, timeout, halftime and match clinch/draw | Observation | Direct | High | V1 |

## Basic data

- Release / origin: Valve; Counter-Strike 2 public release, 2023, replacing
  Counter-Strike: Global Offensive on Steam app `730`.
- Platform or physical form: free-to-play PC client with Valve matchmaking.
- Puzzle family: simultaneous team tactical counterplay under partial information.
- Primary sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/730/CounterStrike_2/),
    for developer, current product and team competitive framing.
  - **[P2]** [current extracted `gamemode_competitive.cfg`](https://github.com/SteamTracking/GameTracking-CS2/blob/master/game/csgo/cfg/gamemode_competitive.cfg),
    for regulation, halftime, money, buy, friendly-fire, drops and respawn values.
  - **[P3]** [official Counter-Strike 2 updates](https://www.counter-strike.net/news/updates),
    observed through the 2026-07-20 update, for current C4, smoke, fire, movement,
    sound and Competitive behaviour changes.
  - **[P4]** [official 2025-07-16 gameplay update](https://www.counter-strike.net/newsentry/529852487375519749),
    for the live CT per-Terrorist team award and weapon/utility changes.
  - **[P5]** [official current Steam announcements](https://steamcommunity.com/app/730/announcements),
    for the 2026 C4 damage preview and explosion interaction with smoke and fire.
- Secondary and reproducible sources:
  - **[S1]** [Valve Developer Community game-mode reference](https://developer.valvesoftware.com/wiki/Counter-Strike%3A_Global_Offensive/Game_Modes),
    for current CS2 mode/config routing and Competitive distinctions.
  - **[S2]** [EWC 2026 Counter-Strike 2 rulebook](https://resources.esportsworldcup.com/en/competitive-ops/rulebooks/cs2),
    for current MR12 bomb-defusal terminology and operational edge cases.
  - **[V1]** repository-side transition control derived from `P2` and checked
    against `P3`–`S2`; it is a rules trace, not a claim of direct play.
- Claim IDs: `CS2-001`–`CS2-006`.

## Mechanical decomposition

### Action Genes

- Existing gene IDs: `ACT-008`, direct first-person traversal; `ACT-161`, aimed
  direct firearm, knife or utility attack; `ACT-164`, select one carried weapon,
  grenade, knife or C4 as the active hand; `ACT-130`, buy one offered asset.
- New genes: `ACT-183`, reload the active
  magazine; `ACT-184`, prime and throw one tactical grenade; `ACT-185`, hold a
  plant/defuse channel; `ACT-186`, drop equipment for redistribution;
  `ACT-187`, communicate a live team cue.
- Parameters: movement speed and stance; weapon, recoil and magazine; grenade
  type and throw; price; plant/defuse duration; communication channel.
- Claim IDs: `CS2-001`, `CS2-002`, `CS2-004`, `CS2-005`.

### System Behaviour Genes

- Existing gene IDs: `SYS-208`, resolve a ranged attack through cover/material,
  armour and hit group; `SYS-215`, direct simultaneous real-time combat;
  `SYS-222`, pick up compatible dropped equipment on contact.
- New genes: `SYS-292`, resolve grenade trajectory and typed field effect;
  `SYS-293`, remove a defeated player for the round and drop equipment;
  `SYS-294`, adjudicate bomb-round objectives; `SYS-295`, award and carry the
  round economy; `SYS-296`, swap sides and reset half economy.
- Resolution order: live movement/fire/utility resolution may eliminate a
  participant; C4 plant changes the operative clock; defuse or explosion may
  override elimination state; round award updates score/economy and saved gear;
  halftime swaps roles while retaining score.
- Parameters: weapon data, material penetration, grenade effect, awards, loss
  count, side, score and half boundary.
- Claim IDs: `CS2-001`–`CS2-004`.

### Constraint Genes

- New genes: `CON-261`, purchases require buy time, spawn zone and funds;
  `CON-262`, weapon/grenade/ammunition capacity; `CON-263`, one life per round;
  `CON-264`, role/item/site/channel objective gate; `CON-265`, asymmetric
  round-to-C4 deadline; `CON-266`, fixed role authority and friendly
  interaction; `CON-267`, finite 12-round halves and 24-round regulation.
- Scarce strategic resources: money, saved weapons, armour, ammunition, grenade
  slots, defuse kit, living players, map time and C4 fuse time.
- Claim IDs: `CS2-001`–`CS2-004`.

### Information Genes

- Existing gene IDs: `INF-073`, carried inventory, active weapon and ammunition
  are visible.
- New genes: `INF-115`, opponent state is exposed locally through sight and
  sound; `INF-116`, HUD/radar expose allied, score, clock and bomb state;
  `INF-117`, personal money and purchase state are visible.
- Claim IDs: `CS2-003`, `CS2-005`.

### Objective Genes

- New gene: `OBJ-071`, win the regulation bomb-defusal match by reaching the
  thirteen-round clinch before the opponent; 12–12 is a bounded draw.
- Success, evaluation and failure: each round awards one side; regulation ends
  at a clinch or after round 24, not from personal kill score.
- Claim IDs: `CS2-001`, `CS2-002`.

### Time Genes

- Existing gene ID: `TIM-003`, players act while movement, attacks, grenades,
  clocks, plant and defuse channels progress in real time.
- Parameters: freeze time, buy time, 1:55 round clock, plant/defuse duration,
  C4 fuse and between-round interval.
- Claim IDs: `CS2-001`, `CS2-002`, `CS2-004`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Living player in buy zone during buy time with sufficient money and capacity | Purchase one offered item | Price leaves personal balance and item enters the compatible round slot | gated cross-round economy | `CS2-001`, `CS2-003`, `CS2-006` |
| Teammate cannot afford a rifle; buyer carries an eligible rifle | Drop rifle | Rifle becomes a world item and compatible contact transfers it to the teammate | team equipment redistribution | `CS2-003`, `CS2-006` |
| Attacker carries C4 inside a bombsite while the original round clock runs | Hold plant through completion | C4 becomes planted and its separate fuse replaces the unplanted deadline | asymmetric two-stage clock | `CS2-002`, `CS2-006` |
| Defender reaches planted C4 without enough uninterrupted time remaining | Start defuse | Interruption or fuse expiry cancels completion; explosion awards attackers | continuous objective gate | `CS2-002`, `CS2-006` |
| Defender reaches planted C4 with sufficient uninterrupted time | Complete defuse | Round immediately awards defenders even if no attackers remain | objective precedence over elimination | `CS2-002`, `CS2-006` |
| C4 remains unplanted when the pre-plant clock reaches zero | No completed plant | Defenders receive the round regardless of surviving attackers | asymmetric timeout | `CS2-002`, `CS2-006` |
| Player takes lethal damage | No revival control exists | Control ends for this round; eligible gear drops; next-round spawn restores participation | one-life round state | `CS2-001`, `CS2-004`, `CS2-006` |
| Twelve regulation rounds have completed | Round boundary | Teams exchange T/CT roles, score persists and starting half economy resets | role reversal under retained score | `CS2-001`, `CS2-006` |
| One team reaches 13 wins before round 24 | Round award | Match clinches immediately; otherwise 12–12 after round 24 is a draw | finite match horizon | `CS2-001`, `CS2-006` |

## Strategic and experiential structure

- Local decision: crosshair placement, exposure, movement noise, recoil control,
  grenade timing, reload safety and whether a plant/defuse channel can finish.
- Medium-term planning: infer rotations from incomplete cues, trade teammate
  deaths, preserve utility, coordinate site entry/retake and decide whether to
  save equipment instead of contesting an implausible round.
- Long-term structure: balance full buys, partial buys and saves across loss
  awards; adapt after the halftime role swap; convert round leads into a clinch.
- Common heuristics: isolate sightlines, avoid solo equipment loss, trade from
  cover, deny a safe plant, preserve enough fuse time for a complete defuse.
- Failure attribution: damage, economy, equipment, clock and round result are
  inspectable, but hidden enemy positions and team coordination keep causal
  attribution partly social and probabilistic.
- Player-trust factors: deterministic objective clocks and visible personal
  economy are strong; matchmaking, anti-cheat and rating quality are excluded
  from this mechanical scope.
- Claim IDs: `CS2-002`–`CS2-005`.

## Replay and variation

- What changes between sessions: map, opponents, teammate plans, spawns within
  fixed team areas, purchased kits, weapon drops and the sequence of round outcomes.
- Randomness or procedural generation: the scoped map and rules are fixed;
  human simultaneous choice, weapon spread and some spawn/details create variation.
- Multiple viable strategies: site executes, defaults, fakes, rushes, saves,
  retakes and force-buy policies exchange information, time and economy.
- Typical replay motive: competitive mastery of aim, utility, positioning,
  communication and cross-round economic adaptation.
- Claim IDs: `CS2-003`–`CS2-005`.

## Adjacent systems and history

- Direct predecessors: Counter-Strike, Counter-Strike: Source and Counter-Strike:
  Global Offensive establish the classic bomb-defusal lineage.
- Variants: Premier adds map veto, rating and overtime; Wingman compresses the
  player/map/round counts; Casual changes economy, equipment and friendly rules.
- Similar games: Valorant, Rainbow Six Siege, tactical round shooters.
- Important differences: this scope centres purchasable carried equipment,
  dropped-item transfer, a two-stage C4 deadline and side-swapped MR12 regulation.
- Claim IDs: `CS2-001`–`CS2-005`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-130`–`ACT-187` | aim, stance, throw strength and communication vocabulary are parameters |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-222`, `SYS-292`–`SYS-296` | recoil/spread remain attack-resolution parameters |
| Constraint | `CON-261`–`CON-267` | map geometry, prices and exact timers are parameters |
| Information | `INF-073`, `INF-115`–`INF-117` | radar scale and sound ranges are parameters |
| Objective | `OBJ-071` | regulation threshold is a parameter |
| Time | `TIM-003` | freeze, round, plant/defuse and fuse durations are parameters |

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`: `ACT-008,ACT-161,ACT-164,ACT-130,ACT-183,ACT-184,ACT-185,ACT-186,ACT-187; SYS-208,SYS-215,SYS-222,SYS-292,SYS-293,SYS-294,SYS-295,SYS-296; CON-261,CON-262,CON-263,CON-264,CON-265,CON-266,CON-267; INF-073,INF-115,INF-116,INF-117; OBJ-071; TIM-003`.
- Indexed games scanned: 136 (`GAME-0001`–`GAME-0136`).
- Indexed combinations scanned: 134 (`COMB-0001`–`COMB-0134`).
- Exact genome matches: none.
- Near matches and similarity scores: Minecraft (`GAME-0129`), provisional
  pre-generation scan `7 / 58 = 0.120690`; regenerated corpus scan must confirm.
- Supported combination subsets: none among `COMB-0001`–`COMB-0134`.
- Scan date: 2026-08-21.

### Exhaustive prior-game similarity scan

- GAME-0001: 0 / 44 = 0.000000; GAME-0002: 0 / 37 = 0.000000; GAME-0003: 0 / 39 = 0.000000; GAME-0004: 1 / 44 = 0.022727.
- GAME-0005: 0 / 37 = 0.000000; GAME-0006: 1 / 38 = 0.026316; GAME-0007: 0 / 38 = 0.000000; GAME-0008: 0 / 37 = 0.000000.
- GAME-0009: 0 / 46 = 0.000000; GAME-0010: 0 / 39 = 0.000000; GAME-0011: 0 / 43 = 0.000000; GAME-0012: 0 / 39 = 0.000000.
- GAME-0013: 0 / 43 = 0.000000; GAME-0014: 0 / 45 = 0.000000; GAME-0015: 0 / 44 = 0.000000; GAME-0016: 1 / 44 = 0.022727.
- GAME-0017: 0 / 43 = 0.000000; GAME-0018: 1 / 48 = 0.020833; GAME-0019: 0 / 40 = 0.000000; GAME-0020: 0 / 44 = 0.000000.
- GAME-0021: 1 / 38 = 0.026316; GAME-0022: 0 / 42 = 0.000000; GAME-0023: 0 / 40 = 0.000000; GAME-0024: 1 / 41 = 0.024390.
- GAME-0025: 1 / 40 = 0.025000; GAME-0026: 1 / 41 = 0.024390; GAME-0027: 1 / 41 = 0.024390; GAME-0028: 1 / 46 = 0.021739.
- GAME-0029: 2 / 40 = 0.050000; GAME-0030: 1 / 43 = 0.023256; GAME-0031: 0 / 41 = 0.000000; GAME-0032: 0 / 41 = 0.000000.
- GAME-0033: 2 / 41 = 0.048780; GAME-0034: 2 / 42 = 0.047619; GAME-0035: 2 / 46 = 0.043478; GAME-0036: 1 / 41 = 0.024390.
- GAME-0037: 0 / 39 = 0.000000; GAME-0038: 2 / 44 = 0.045455; GAME-0039: 0 / 39 = 0.000000; GAME-0040: 1 / 37 = 0.027027.
- GAME-0041: 2 / 39 = 0.051282; GAME-0042: 0 / 39 = 0.000000; GAME-0043: 1 / 43 = 0.023256; GAME-0044: 1 / 39 = 0.025641.
- GAME-0045: 1 / 43 = 0.023256; GAME-0046: 0 / 40 = 0.000000; GAME-0047: 0 / 44 = 0.000000; GAME-0048: 0 / 44 = 0.000000.
- GAME-0049: 0 / 39 = 0.000000; GAME-0050: 1 / 44 = 0.022727; GAME-0051: 1 / 45 = 0.022222; GAME-0052: 0 / 40 = 0.000000.
- GAME-0053: 1 / 38 = 0.026316; GAME-0054: 1 / 40 = 0.025000; GAME-0055: 1 / 39 = 0.025641; GAME-0056: 0 / 38 = 0.000000.
- GAME-0057: 0 / 38 = 0.000000; GAME-0058: 0 / 39 = 0.000000; GAME-0059: 0 / 37 = 0.000000; GAME-0060: 0 / 37 = 0.000000.
- GAME-0061: 0 / 40 = 0.000000; GAME-0062: 0 / 38 = 0.000000; GAME-0063: 0 / 37 = 0.000000; GAME-0064: 0 / 35 = 0.000000.
- GAME-0065: 0 / 37 = 0.000000; GAME-0066: 0 / 40 = 0.000000; GAME-0067: 0 / 38 = 0.000000; GAME-0068: 0 / 38 = 0.000000.
- GAME-0069: 0 / 38 = 0.000000; GAME-0070: 0 / 38 = 0.000000; GAME-0071: 0 / 37 = 0.000000; GAME-0072: 0 / 38 = 0.000000.
- GAME-0073: 0 / 37 = 0.000000; GAME-0074: 0 / 39 = 0.000000; GAME-0075: 0 / 39 = 0.000000; GAME-0076: 0 / 37 = 0.000000.
- GAME-0077: 0 / 37 = 0.000000; GAME-0078: 0 / 37 = 0.000000; GAME-0079: 0 / 37 = 0.000000; GAME-0080: 0 / 37 = 0.000000.
- GAME-0081: 0 / 38 = 0.000000; GAME-0082: 0 / 38 = 0.000000; GAME-0083: 0 / 38 = 0.000000; GAME-0084: 0 / 40 = 0.000000.
- GAME-0085: 0 / 41 = 0.000000; GAME-0086: 0 / 43 = 0.000000; GAME-0087: 1 / 39 = 0.025641; GAME-0088: 0 / 39 = 0.000000.
- GAME-0089: 0 / 39 = 0.000000; GAME-0090: 1 / 44 = 0.022727; GAME-0091: 2 / 37 = 0.054054; GAME-0092: 1 / 39 = 0.025641.
- GAME-0093: 0 / 39 = 0.000000; GAME-0094: 2 / 38 = 0.052632; GAME-0095: 2 / 40 = 0.050000; GAME-0096: 2 / 38 = 0.052632.
- GAME-0097: 2 / 36 = 0.055556; GAME-0098: 2 / 35 = 0.057143; GAME-0099: 1 / 37 = 0.027027; GAME-0100: 1 / 40 = 0.025000.
- GAME-0101: 0 / 40 = 0.000000; GAME-0102: 0 / 37 = 0.000000; GAME-0103: 0 / 39 = 0.000000; GAME-0104: 1 / 38 = 0.026316.
- GAME-0105: 2 / 38 = 0.052632; GAME-0106: 0 / 37 = 0.000000; GAME-0107: 1 / 37 = 0.027027; GAME-0108: 1 / 39 = 0.025641.
- GAME-0109: 0 / 46 = 0.000000; GAME-0110: 1 / 37 = 0.027027; GAME-0111: 1 / 36 = 0.027778; GAME-0112: 2 / 36 = 0.055556.
- GAME-0113: 2 / 42 = 0.047619; GAME-0114: 1 / 36 = 0.027778; GAME-0115: 0 / 36 = 0.000000; GAME-0116: 2 / 34 = 0.058824.
- GAME-0117: 1 / 37 = 0.027027; GAME-0118: 1 / 45 = 0.022222; GAME-0119: 1 / 52 = 0.019231; GAME-0120: 0 / 59 = 0.000000.
- GAME-0121: 1 / 52 = 0.019231; GAME-0122: 1 / 44 = 0.022727; GAME-0123: 0 / 68 = 0.000000; GAME-0124: 1 / 76 = 0.013158.
- GAME-0125: 1 / 71 = 0.014085; GAME-0126: 1 / 72 = 0.013889; GAME-0127: 2 / 76 = 0.026316; GAME-0128: 1 / 45 = 0.022222.
- GAME-0129: 7 / 58 = 0.120690; GAME-0130: 1 / 82 = 0.012195; GAME-0131: 4 / 72 = 0.055556; GAME-0132: 1 / 80 = 0.012500.
- GAME-0133: 1 / 74 = 0.013514; GAME-0134: 1 / 80 = 0.012500; GAME-0135: 1 / 77 = 0.012987; GAME-0136: 1 / 89 = 0.011236.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Minecraft (`GAME-0129`) | `ACT-008`, `ACT-161`, `ACT-164`, `SYS-215`, `SYS-222`, `INF-073`, `TIM-003` | persistent voxel survival/crafting and ordinary respawn versus finite team rounds, economy, partial opponent information and bomb objectives | provisional nearest at `7 / 58 = 0.120690` |

- New genes: `ACT-183`–`ACT-187`, `SYS-292`–`SYS-296`, `CON-261`–`CON-267`,
  `INF-115`–`INF-117`, `OBJ-071`.
- Classification result: `New gene` and new combination of known/new genes.
- Evidence and reasoning: existing combat/navigation/item genes preserve their
  operational boundaries; the new records isolate cross-round economy,
  one-life round participation, asymmetric C4 timing and shared partial team
  information rather than promoting weapon statistics into genes.

### Registry normalisation 006 score corrections

These recomputed values supersede the pre-normalisation fractions above:

- `GAME-0120`: `1 / 58 = 0.017241`
- `GAME-0123`: `1 / 67 = 0.014925`
- `GAME-0124`: `2 / 75 = 0.026667`
- `GAME-0132`: `2 / 79 = 0.025316`
- Current prior-corpus near match after normalisation 006: `GAME-0129`.

## Taxonomy impact

- Registry changes after normalisation: 21 bounded active genes and added CS2
  evidence for eight reused records.
- Taxonomy-change record: `TAXONOMY_CHANGE_012`.
- Candidate terms affected: recoil pattern, counter-strafing, wallbang and save
  are parameters or strategies inside admitted genes, not separate genes.

## Negative results

- Negative results: none. No prior claim, candidate or gene boundary was rejected.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Competitive MR12 поєднує one-life rounds,
  cross-round economy, side swap і asymmetric bomb deadline (`CS2-001`–`CS2-003`).
- [Confirmed | Corroborated | High] Grenade fields and partial audiovisual
  information make space and communication causal without omniscient state (`CS2-004`, `CS2-005`).

## Нові гени

- [Observation | Corroborated | High] Додано 21 gene для reload/utility,
  plant-defuse control, team cues, round death/economy/adjudication, bomb clocks,
  partial team information і match victory.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0135` — round-economy bomb-defusal counterplay.

## Зміни таксономії

- [Observation | Direct | High] Змін таксономії немає.

## Нові питання

- Чи відтворює Dota 2 подібну cross-player information boundary без discrete
  one-life rounds, і які combat/economy genes справді переносяться?

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] `GAME-0138` Dota 2.
- Optimisation criterion: continue the recorded demand-led queue while testing
  whether simultaneous team combat reuses any CS2 genes beyond generic timing.
- Expected information gain: lane economy, fog of war, item builds, respawn,
  team objectives and long-horizon base victory.
- Backlog impact: preserves `GAME-0139` Palworld and all later subjects.

## Чому саме вона

- [Hypothesis | Limited | Medium] Dota 2 keeps current public demand high while
  providing a strong counterexample to round-bounded shooter structure.
