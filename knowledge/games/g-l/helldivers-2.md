---
game_id: GAME-0159
slug: helldivers-2
game_title: Helldivers 2
analysis_status: reviewed
reviewed: 2026-08-27
combination_ids:
  - COMB-0157
gene_ids:
  action:
    - ACT-008
    - ACT-106
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-184
    - ACT-187
    - ACT-190
    - ACT-215
    - ACT-218
    - ACT-253
  system:
    - SYS-208
    - SYS-215
    - SYS-292
    - SYS-380
    - SYS-434
    - SYS-435
    - SYS-436
    - SYS-437
  constraint:
    - CON-262
    - CON-269
    - CON-272
    - CON-381
    - CON-382
    - CON-383
  information:
    - INF-073
    - INF-115
    - INF-116
    - INF-119
    - INF-137
    - INF-169
  objective:
    - OBJ-087
  time:
    - TIM-003
---

# Game: Helldivers 2

## Analysis scope

- Version / ruleset: PC and console rules at official patch `7.0.2`, `Devoid
  of Liberty`, released 25 August 2026; one private four-player Easy
  (difficulty 2) operation whose single mission is `Terminate Illegal
  Broadcast`, against the first currently available non-Void faction front.
- Primary decision loop: inspect the map, main objective, squad, reinforcement
  stock, ammunition, health and stratagem readiness; traverse and fight or
  enter a stratagem code and throw its beacon; react to patrol detection,
  hostile reinforcements and friendly fire; complete the broadcast objective,
  then call extraction and preserve surviving sample carriers until departure.
- Reproducible entry: a host selects an active eligible planet, Easy difficulty
  and an offered `Terminate Illegal Broadcast` operation; four players retain
  legal base-game equipment and four selected non-premium stratagems each,
  accept the standard twenty-Reinforce squad budget, choose a drop zone and
  enter their steerable Hellpods.
- Reproducible exit: destroy or manually disable the illegal broadcast, call
  the extraction terminal, and stop at the mission debrief after Pelican
  departure or the post-objective squad's final deaths. Record mission success
  independently from extracted Helldivers and recovered samples; because Easy
  contains one mission, its result also settles the operation contribution.
- Included: loadout and drop-zone choice; third-person traversal and aimed
  combat; finite weapons, ammunition and grenades; stratagem codes, thrown
  targeting, charges and cooldowns; patrol detection and enemy reinforcement;
  universal friendly fire; shared Reinforce budget and Hellpod return; the
  required broadcast objective; extraction, survivor/sample retention and
  operation-to-Galactic-War contribution.
- Excluded: tutorial; public matchmaking or drop-in; other difficulties,
  objectives, factions and operations; optional objectives, outposts and
  point-of-interest grinding; premium or crossover Warbonds; ship upgrades,
  purchases and long-term unlock optimisation; Major Order or campaign
  completion; Void-only modules and unbounded Galactic War play.
- Direct-play status: not conducted. Arrowhead and PlayStation material fixes
  the current build and core squad, mission, friendly-fire and stratagem rules;
  current community documentation supplies reproducible Easy-operation,
  Reinforce, extraction and settlement edge cases.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `HD2-001` | Patch `7.0.2` is the current 25 August 2026 ruleset | Confirmed | Direct | High | P1, S1 |
| `HD2-002` | Up to four Helldivers select equipment and stratagems, deploy by Hellpod and fight under universal friendly fire | Confirmed | Direct | High | P2, P3, P4 |
| `HD2-003` | A stratagem requires its exact directional code, a thrown beacon and then its typed arrival, charge or cooldown rule | Observation | Corroborated | High | P2, P3, S2 |
| `HD2-004` | Easy contains one mission per operation, and `Terminate Illegal Broadcast` is an Easy-compatible main objective | Observation | Corroborated | High | S3, S4 |
| `HD2-005` | Patrol detection can raise an alarm and introduce faction reinforcement into live combat | Observation | Corroborated | High | P2, P3, S5 |
| `HD2-006` | Four players share twenty initial Reinforce uses; a live player calls a dead teammate back in a steerable Hellpod | Observation | Corroborated | High | P4, S6 |
| `HD2-007` | Completing the main objective determines mission success; extraction separately retains surviving Helldivers and carried samples | Observation | Corroborated | High | S7, S8 |
| `HD2-008` | The mission horizon disables ordinary chosen stratagem support and forces the final extraction sequence | Observation | Corroborated | High | S6, S8 |
| `HD2-009` | Successful mission and operation settlement contributes shared impact to the selected Galactic War planet | Confirmed | Corroborated | High | P5, S9 |

## Basic data

- Release / origin: Arrowhead Game Studios; Sony Interactive Entertainment,
  8 February 2024.
- Platform or physical form: online cooperative third-person shooter on PC and
  console; this packet uses a private four-player squad.
- Puzzle family: real-time cooperative tactical execution under shared
  reinforcements, partial information and separable mission/extraction results.
- Primary sources: **[P1]** [official patch 7.0.2 announcement](https://steamcommunity.com/games/553850/announcements/detail/671752023818896713),
  **[P2]** [official PlayStation beginner guide](https://www.playstation.com/en-us/editorial/a-beginner-s-guide-to-helldivers-2/),
  **[P3]** [official hands-on report](https://blog.playstation.com/2024/02/02/helldivers-2-hands-on-report-chaotic-co-op-and-empowering-stratagems/),
  **[P4]** [official cooperative gameplay details](https://blog.playstation.com/?p=382074&sf267758520=1),
  **[P5]** [official Steam product page](https://store.steampowered.com/app/553850/HELLDIVERS_2?l=english).
- Secondary sources: **[S1]** [SteamDB patch record](https://steamdb.info/patchnotes/24826606/),
  **[S2]** [Stratagem rules](https://helldivers.wiki.gg/wiki/Stratagems),
  **[S3]** [difficulty rules](https://helldivers.wiki.gg/wiki/Difficulty),
  **[S4]** [Terminate Illegal Broadcast](https://helldivers.wiki.gg/wiki/Terminate_Illegal_Broadcast),
  **[S5]** [patrol and alert rules](https://helldivers.wiki.gg/wiki/Patrols),
  **[S6]** [Reinforce rules](https://helldivers.wiki.gg/wiki/Reinforce),
  **[S7]** [mission success rules](https://helldivers.wiki.gg/wiki/Missions),
  **[S8]** [extraction rules](https://helldivers.wiki.gg/wiki/Extraction),
  **[S9]** [Galactic War mechanics](https://helldivers.wiki.gg/wiki/Second_Galactic_War_Mechanics).
- Claim IDs: `HD2-001`–`HD2-009`.

## Mechanical decomposition

### Action Genes

- `ACT-215` configures the finite deployment loadout. `ACT-008`, `ACT-161`,
  `ACT-164`, `ACT-183` and `ACT-184` cover direct movement, shooting, equipment
  switching, reload and grenade use; `ACT-187` communicates a team cue.
- `ACT-106` enters a stratagem's ordered directional code and `ACT-190`
  commits its target beacon. `ACT-253` lets a survivor call a dead teammate
  back; `ACT-218` calls and enters the final extraction endpoint.
- Candidate genes: none.
- Claim IDs: `HD2-002`–`HD2-008`.

### System Behaviour Genes

- `SYS-208`, `SYS-215` and `SYS-292` resolve aimed weapons, continuous hostile
  combat and grenade fields. `SYS-380` resolves a coded stratagem's typed
  orbital, aerial, weapon, emplacement or supply effect.
- `SYS-434` converts patrol detection into an alarm and faction reinforcement;
  `SYS-435` spends the shared Reinforce pool and returns the teammate in a
  steerable Hellpod.
- `SYS-436` settles objective success separately from extraction and sample
  retention. `SYS-437` converts the successful one-mission operation into
  shared Galactic War impact.
- Resolution order: local perception and input; weapon or code validation;
  live effect and alert response; main-objective state; Reinforce or extraction
  state; mission, operation and war settlement.
- Claim IDs: `HD2-002`–`HD2-009`.

### Constraint Genes

- `CON-262` bounds carried weapons, grenades and ammunition; `CON-269` gates
  stratagem targets, charges and cooldowns. `CON-272` suspends control after
  death until a valid return.
- `CON-381` keeps allies damageable by the same weapons, stratagems and
  Hellpods. `CON-382` requires a live caller and shared stock for ordinary
  Reinforce, with the depleted-pool recharge as a parameter. `CON-383` makes
  the forty-minute Super Destroyer horizon disable support and force bounded
  emergency extraction.
- Scarce strategic resources: live squad bodies, shared Reinforce stock,
  ammunition, grenades, stratagem charges/readiness, time and carried samples.
- Claim IDs: `HD2-002`, `HD2-003`, `HD2-006`–`HD2-008`.

### Information Genes

- `INF-073` exposes current weapons, grenades and ammunition; `INF-119` exposes
  health and stratagem readiness. `INF-115` leaves enemies locally revealed
  through sight, sound and effects while `INF-116` exposes the squad, timer,
  Reinforce stock and shared objective state.
- `INF-137` exposes the mission map, main objective and extraction site.
  `INF-169` exposes the debrief's separate success, extraction, sample and
  operation/Galactic-War consequences.
- Candidate genes: none.
- Claim IDs: `HD2-003`–`HD2-009`.

### Objective Genes

- `OBJ-087` requires main-objective completion before the destroyer horizon,
  then treats extraction of survivors and sample carriers as a separable result
  rather than a prerequisite for mission success.
- Success, evaluation and failure: destruction or manual shutdown completes
  the objective; a total wipe before that point fails, while deaths after it
  preserve mission success but can lose bodies and samples.
- Claim IDs: `HD2-004`, `HD2-007`, `HD2-008`.

### Time Genes

- `TIM-003` advances patrols, combat, stratagem readiness, Reinforce and the
  mission/extraction clocks continuously without a tactical pause.
- Candidate genes: none.
- Claim IDs: `HD2-003`, `HD2-005`, `HD2-006`, `HD2-008`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A selected ready stratagem has a unique code | Enter its ordered arrows correctly and throw the resulting beacon | A wrong symbol resets the code; a valid beacon schedules the typed effect at its legal target under charge/cooldown rules | symbolic command plus spatial deployment | `HD2-003` |
| A patrol has not detected the squad | Remain visible/noisy inside its detection conditions | The alerted patrol requests faction reinforcement and the combat state escalates | perception-triggered escalation | `HD2-005` |
| One Helldiver is dead, another is alive and shared stock remains | Enter and throw the Reinforce code | One shared use is consumed and the teammate returns through a steerable Hellpod | survivor-mediated return | `HD2-006` |
| The illegal broadcast still owns mission success | Destroy its tower or complete its terminal sequence | The main objective becomes complete and extraction becomes the remaining bounded route, even if nobody later survives | separate objective success | `HD2-004`, `HD2-007` |
| The main objective is complete | Call extraction and enter the Pelican before departure | Boarded Helldivers survive and their carried samples are retained; absent or dead carriers do not | separable extraction/sample result | `HD2-007`, `HD2-008` |
| The Easy mission reaches successful debrief | Accept the one-mission operation settlement | Mission contribution and operation bonus are applied to the selected planet's shared war state | local result to shared campaign | `HD2-009` |

## Strategic and experiential structure

- Local decision: balance aimed fire, movement, reload, grenade and a coded
  stratagem against current friendly positions and emerging patrol pressure.
- Medium-term planning: avoid unnecessary alarms, preserve shared Reinforce
  stock, clear a route to the broadcast and keep enough support ready for the
  extraction defence.
- Long-term structure: turn one successful objective and the surviving sample
  carriers into a completed Easy operation and a small shared war contribution.
- Common heuristics: spread around large-area stratagem targets; call Reinforce
  into cover; recover dropped samples; disengage from nonessential patrols;
  finish the objective before searching, then converge at extraction.
- Failure attribution: ally indicators, Reinforce count, objective state,
  stratagem readiness, timer and debrief separate friendly-fire loss, stock
  depletion, missed objective, failed extraction and sample loss.
- Player-trust factors: all damage must obey the advertised friendly-fire rule,
  code errors and cooldowns need immediate feedback, and success must remain
  visibly distinct from extraction quality.
- Claim IDs: `HD2-002`–`HD2-009`.

## Replay and variation

- What changes between sessions: planet terrain, faction, patrol routes,
  encounter timing, selected loadouts, casualties, dropped samples and final
  war-state contribution.
- Randomness or procedural generation: mission layout and encounters vary;
  the main-objective, Reinforce, extraction and settlement contracts persist.
- Multiple viable strategies: the tower can be demolished at range or disabled
  through its terminal, and many weapon/stratagem combinations can protect the
  final route.
- Typical replay motive: improve extraction and sample yield, test another
  squad loadout or contribute to a different active front.
- Claim IDs: `HD2-003`–`HD2-009`.

## Adjacent systems and history

- Direct predecessor: Helldivers uses the same cooperative satire, directional
  stratagem inputs, friendly fire and Galactic Campaign from an overhead view.
- Variants: solo or smaller squads, other factions and higher difficulties
  alter reinforcement pressure, operation length and objective composition.
- Similar games: Battlefield 6 shares squad firefights and gadgets; Apex
  Legends shares survivor-mediated teammate return; ARC Raiders shares a
  called extraction endpoint, but none combines them with symbolic orbital
  commands and separate community-war settlement.
- Important differences: samples require extraction but mission success does
  not; the shared war receives an aggregate result after the bounded operation.
- Claim IDs: `HD2-002`–`HD2-009`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-106`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-187`, `ACT-190`, `ACT-215`, `ACT-218`, `ACT-253` | movement, firearm, grenade, stratagem, Reinforce, extraction |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-292`, `SYS-380`, `SYS-434`, `SYS-435`, `SYS-436`, `SYS-437` | combat, alert, return, settlement and war impact |
| Constraint | `CON-262`, `CON-269`, `CON-272`, `CON-381`, `CON-382`, `CON-383` | capacity, readiness, friendly fire, stock and horizon |
| Information | `INF-073`, `INF-115`, `INF-116`, `INF-119`, `INF-137`, `INF-169` | HUD, local hostiles, map and debrief |
| Objective | `OBJ-087` | required broadcast; separable extraction quality |
| Time | `TIM-003` | continuous combat, cooldown and deadline time |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `158` (`GAME-0001`–`GAME-0158`).
- Exact genome matches: none.
- Tied near matches: `GAME-0149` — Battlefield 6 (`20 / 48 = 0.416667`).
- Supported combination subsets: `COMB-0157`.
- Scan date: 2026-08-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0149` — Battlefield 6 | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-184`, `ACT-187`, `ACT-190`, `ACT-215`, `SYS-208`, `SYS-215`, `SYS-292`, `SYS-380`, `CON-262`, `CON-269`, `CON-272`, `INF-073`, `INF-115`, `INF-116`, `INF-119`, `TIM-003` | Both coordinate equipped squads through direct real-time gun, grenade and gadget combat under finite resources and partial information; Battlefield 6 converts capture control, revives, deployment sources and deaths into opposing reinforcement attrition, while Helldivers 2 adds symbolic orbital calls, universal friendly fire, a shared teammate-return pool, an authored main objective and separate extraction/war settlement | Near, `0.416667` |

### Preserved research notes

- New genes: `SYS-434`, `SYS-435`, `SYS-436`, `SYS-437`, `CON-381`,
  `CON-382`, `CON-383`, `INF-169` and `OBJ-087`.
- Reused genes: `ACT-008`, `ACT-106`, `ACT-161`, `ACT-164`, `ACT-183`,
  `ACT-184`, `ACT-187`, `ACT-190`, `ACT-215`, `ACT-218`, `ACT-253`,
  `SYS-208`, `SYS-215`, `SYS-292`, `SYS-380`, `CON-262`, `CON-269`,
  `CON-272`, `INF-073`, `INF-115`, `INF-116`, `INF-119`, `INF-137` and
  `TIM-003`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: the scoped genome admits only the systems required
  for one Easy objective-to-debrief loop; optional sites, purchases and the
  broader evolving war do not cause its declared exit.

## Taxonomy impact

- Registry changes: nine new active genes; existing records gain Helldivers 2
  evidence only.
- Taxonomy-change record: none.
- Candidate terms affected: patrol-alarm escalation, shared Reinforce return,
  friendly-fire validity, split success/extraction settlement and local-to-war
  contribution.

## Negative results

- Samples are not an inventory-retention gene here: their causal distinction
  is the post-objective extraction settlement. Optional outposts, ship modules,
  Warbond purchases, Major Orders and full-campaign control are excluded
  modules rather than hidden members of the one-operation signature.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] One Easy Helldivers 2 operation couples
  symbolic stratagem deployment, squad-wide friendly fire and shared returns
  to a mission result whose extraction and war effects settle separately
  (`HD2-001`–`HD2-009`).

## Нові гени

- [Observation | Corroborated | High] `SYS-434`–`SYS-437`, `CON-381`–`CON-383`,
  `INF-169`, `OBJ-087`.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0157`.

## Зміни таксономії

- [Observation | Corroborated | High] Змін таксономії немає.

## Нові питання

- Does a higher-difficulty multi-mission operation add a reusable intermission
  attrition state, or only parameters around this mission/operation boundary?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] Pokémon Legends: Z-A.
- Optimisation criterion: contrast continuous four-player squad pressure with
  a bounded solo creature-command and urban progression loop.
- Expected information gain: test real-time trainer positioning, move command,
  capture and day/night tournament progression against the combat corpus.
- Backlog impact: continue the authorised demand-led Goal.

## Чому саме вона

- [Hypothesis | Limited | High] It is the next recorded `GAME-0160` unit and
  changes both control ownership and reward horizon after a shared-war shooter.
