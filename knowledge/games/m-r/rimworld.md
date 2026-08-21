---
game_id: GAME-0127
slug: rimworld
game_title: RimWorld
analysis_status: reviewed
reviewed: 2026-08-18
combination_ids:
  - COMB-0125
gene_ids:
  action:
    - ACT-006
    - ACT-120
    - ACT-144
    - ACT-145
    - ACT-147
    - ACT-148
    - ACT-149
    - ACT-150
    - ACT-151
    - ACT-152
    - ACT-155
    - ACT-156
    - ACT-157
    - ACT-158
  system:
    - SYS-004
    - SYS-045
    - SYS-051
    - SYS-156
    - SYS-158
    - SYS-161
    - SYS-186
    - SYS-194
    - SYS-196
    - SYS-197
    - SYS-198
    - SYS-203
    - SYS-204
    - SYS-205
    - SYS-206
    - SYS-208
    - SYS-209
  constraint:
    - CON-062
    - CON-172
    - CON-192
    - CON-193
    - CON-199
    - CON-200
    - CON-202
    - CON-203
    - CON-204
    - CON-205
  information:
    - INF-001
    - INF-002
    - INF-059
    - INF-071
    - INF-072
  objective:
    - OBJ-062
  time:
    - TIM-003
---

# Game: RimWorld

## Analysis scope

- Version / ruleset: PC base game `1.6`, ordinary Crashlanded scenario with
  Cassandra Classic on Strive to Survive, from three survivors to launching a
  player-built ship.
- Included: seeded planet and landing map; work priorities, designations,
  schedules, zones, stockpiles, bills and research; needs, mood, health,
  relationships and prisoners; drafted combat; storyteller incidents, wealth,
  caravans and the constructed-ship ending.
- Excluded: Royalty, Ideology, Biotech, Anomaly and Odyssey; mods, dev mode,
  custom scenarios and difficulty settings; the journey-offer ship; post-launch play.
- Direct-play status: not conducted. The official product description and
  maintained base-game 1.6 reference agree on the scoped causal transitions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `RW-001` | A seed creates a planet and selected colony map for three generated survivors | Confirmed | Corroborated | High | P1, P2 |
| `RW-002` | Designations, priorities, schedules and areas create bounded autonomous work | Confirmed | Corroborated | High | P2, P3, P4 |
| `RW-003` | Bills and filtered stockpiles maintain material production through pawn hauling | Confirmed | Corroborated | High | P2, P5, P6 |
| `RW-004` | Needs, thoughts and relationships update mood and may remove a pawn from control | Confirmed | Corroborated | High | P1, P7, P8, P9 |
| `RW-005` | Local body conditions alter capacities, work, treatment and survival | Confirmed | Corroborated | High | P1, P10, P11 |
| `RW-006` | Drafting switches an eligible pawn from work autonomy to exact tactical orders | Confirmed | Corroborated | High | P12 |
| `RW-007` | Storyteller incidents depend on colony state, difficulty and recent outcomes | Confirmed | Corroborated | High | P1, P13, P14 |
| `RW-008` | Captives can be assigned a repeated resistance-and-recruitment policy | Confirmed | Corroborated | High | P1, P15 |
| `RW-009` | A selected research project receives staffed bench work and unlocks technology | Confirmed | Corroborated | High | P2, P16 |
| `RW-010` | Loaded caravans form locally, then path and act across the persistent world | Confirmed | Corroborated | High | P1, P17 |
| `RW-011` | A connected ship launches only after a surviving fifteen-day reactor startup | Confirmed | Corroborated | High | P18, P19, P20 |

## Basic data

- Release / origin: Ludeon Studios; commercial 1.0 release on 2018-10-17;
  scoped to the current base-game 1.6 rules line.
- Platform or physical form: pausable real-time PC colony and tactical simulation.
- Puzzle family: automation and spatial programming; real-time system pressure;
  agent routing and coordination; ordered dependency sequencing.
- Primary sources: **[P1]** [official product page](https://store.steampowered.com/app/294100/RimWorld/);
  **[P2]** [base-game Crashlanded guide](https://rimworldwiki.com/wiki/Basics);
  **[P3]** [work system](https://rimworldwiki.com/wiki/Work);
  **[P4]** [allowed areas](https://rimworldwiki.com/wiki/Allowed_area);
  **[P5]** [bills](https://rimworldwiki.com/wiki/Bill);
  **[P6]** [stockpiles](https://rimworldwiki.com/wiki/Stockpile_zone);
  **[P7]** [needs](https://rimworldwiki.com/wiki/Needs);
  **[P8]** [mental breaks](https://rimworldwiki.com/wiki/Mental_break);
  **[P9]** [social relations](https://rimworldwiki.com/wiki/Social);
  **[P10]** [health](https://rimworldwiki.com/wiki/Health);
  **[P11]** [capacities](https://rimworldwiki.com/wiki/Capacity);
  **[P12]** [drafting](https://rimworldwiki.com/wiki/Drafting);
  **[P13]** [AI storytellers](https://rimworldwiki.com/wiki/AI_Storytellers);
  **[P14]** [wealth](https://rimworldwiki.com/wiki/Wealth);
  **[P15]** [prisoners](https://rimworldwiki.com/wiki/Prisoner);
  **[P16]** [research](https://rimworldwiki.com/wiki/Research);
  **[P17]** [caravans](https://rimworldwiki.com/wiki/Caravan);
  **[P18]** [ship](https://rimworldwiki.com/wiki/Ship);
  **[P19]** [ship reactor](https://rimworldwiki.com/wiki/Ship_reactor);
  **[P20]** [endings](https://rimworldwiki.com/wiki/Endings).
- Claim IDs: `RW-001`–`RW-011`.

## Mechanical decomposition

### Action Genes

- Reused: `ACT-006`, `ACT-120`, `ACT-144`, `ACT-145`, `ACT-147`–`ACT-152`
  cover time controls, work, plans, schedules, bills, stores, rooms and research.
- New: `ACT-155`–`ACT-158` cover resident policies, direct tactical draft,
  world caravans and prisoner handling.
- Claim IDs: `RW-002`, `RW-003`, `RW-006`, `RW-008`–`RW-010`.

### System Behaviour Genes

- Reused: autonomous movement, combat, production, power, extraction, errand
  routing, hauling, quality, personal need-memory outcomes and staffed research.
- New: `SYS-203`–`SYS-206`, `SYS-208` and `SYS-209` cover storyteller pressure,
  body capacities, relationships, recruitment, cover-sensitive wounds and map
  generation.
- Resolution order: accept policies and plans; broker work; path, haul and
  produce; update bodies, needs, mood and relations; schedule incidents;
  resolve drafted combat and world travel; test ship completion.
- Claim IDs: `RW-001`–`RW-011`.

### Constraint Genes

- Reused: recipe supply, network power, work eligibility, material-backed
  construction, survival, job inputs and stockpile acceptance.
- New: `CON-202`–`CON-205` bind autonomous interaction to policies, suspend
  control during breaks, require viable caravans and gate ship launch.
- Scarce strategic resources: pawn time and health, food, medicine, power,
  components, growing space, storage, carrying capacity and defensible wealth.
- Claim IDs: `RW-002`–`RW-011`.

### Information Genes

- `INF-001` and `INF-002` separate inspectable current state from the next
  unpreviewed incident; `INF-059`, `INF-071` and `INF-072` expose dependencies,
  colony reports and individual causal state.
- Claim IDs: `RW-002`–`RW-011`.

### Objective Genes

- `OBJ-062` bounds the open colony at research, construction, reactor defence
  and launch of the player-built ship.
- Claim IDs: `RW-011`.

### Time Genes

- `TIM-003`: work, needs, weather, incidents, combat and reactor startup advance
  in live time while pause, speed and commands remain available.
- Claim IDs: `RW-002`–`RW-011`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A reachable wall is unmined | designate it for mining | an eligible pawn ranks, claims and performs the generated job | spatial orders create autonomous work | `RW-002` |
| Meals are below a chosen stock target | set a stove bill to make until X | cooks repeat the recipe while ingredients, job eligibility and target permit | production is conditional policy | `RW-003` |
| A high-priority freezer accepts food | paint and filter its stockpile | haulers move eligible food toward free accepted cells | storage geometry changes labour | `RW-003` |
| A pawn accumulates hunger, pain and hostile thoughts | let time advance below a break threshold | a sampled mental break suspends ordinary control and work | welfare can disable labour | `RW-004` |
| A leg is wounded and bleeding | assign treatment and provide medicine | tending changes the condition while the damaged part reduces movement | health is local and capacity-bearing | `RW-005` |
| A raid enters weapon range | draft two colonists and order cover positions | pawns move exactly, then aimed shots resolve cover, armour and body hits | crisis control is direct | `RW-006` |
| Colony wealth and population have grown | continue Cassandra's schedule | a state-scaled incident is selected after the storyteller interval | prosperity raises pressure | `RW-007` |
| A prisoner has positive resistance | assign Recruit interaction | wardens repeatedly reduce resistance and attempt conversion | population growth can be authored policy | `RW-008` |
| Ship technology is still locked | select its prerequisite and staff a suitable bench | research points accumulate and unlock the project at its cost | technology is staffed dependency work | `RW-009` |
| Selected travellers and food are on the colony map | commit caravan formation and route | members gather cargo, exit together and path across terrain | local logistics becomes world travel | `RW-010` |
| A complete connected ship has an occupied casket | activate and defend the reactor for fifteen days | surviving startup enables launch and credits | the open colony has a reproducible end horizon | `RW-011` |

## Strategic and experiential structure

- Local decision: decide whether a pawn should work, rest, receive treatment or
  be drafted while other needs and jobs keep changing.
- Medium-term planning: shorten hauling, maintain food and power, manage wealth,
  train specialists and build layered defence without collapsing mood.
- Long-term structure: turn three incompatible survivors into a self-sustaining
  colony capable of researching, building and defending an escape ship.
- Common heuristics: specialise work carefully; keep meals and medicine buffered;
  separate clean production from dirty storage; draft only for crises; spend wealth on readiness.
- Failure attribution: work tabs, alerts, health, needs, mood and combat logs
  expose proximate causes, although storyteller randomness can obscure timing.
- Player-trust factors: incidents are unpreviewed but difficulty, wealth,
  adaptation, pawn state and most local causal panels are inspectable.
- Claim IDs: `RW-002`–`RW-011`.

## Replay and variation

- What changes: planet, biome, map resources, pawn traits and skills, factions,
  incidents, recruits, relationships, wounds, quests and attack composition.
- Randomness: the seed and storyteller change circumstances while job,
  production, health, mood and launch rules remain reproducible.
- Multiple viable strategies: yes; colony layout, economy, recruiting,
  research order, defensive geometry and caravan use admit distinct paths.
- Typical replay motive: observe how the same policy tools produce a different
  survival story from a new roster, site and incident sequence.
- Claim IDs: `RW-001`, `RW-004`–`RW-011`.

## Adjacent systems and history

- Direct predecessors: Dwarf Fortress, settlement simulations, tactical
  squad games and autonomous-worker management.
- Variants: DLC add royalty, ideology, reproduction, anomalies and gravships;
  all are outside this record.
- Similar games: Dwarf Fortress, Oxygen Not Included and Against the Storm.
- Important differences: RimWorld alternates indirect colony policy with exact
  draft control, and scales authored storyteller incidents against colony state.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-006`, `ACT-120`, `ACT-144`, `ACT-145`, `ACT-147`–`ACT-152`, `ACT-155`–`ACT-158` | policy, draft, bill and caravan parameters |
| System Behaviour | `SYS-004`, `SYS-045`, `SYS-051`, `SYS-156`, `SYS-158`, `SYS-161`, `SYS-186`, `SYS-196`–`SYS-198`, `SYS-203`–`SYS-209` | incident, health, relation and combat parameters |
| Constraint | `CON-062`, `CON-172`, `CON-192`, `CON-193`, `CON-199`, `CON-200`, `CON-202`–`CON-205` | policy, caravan and ship gates |
| Information | `INF-001`, `INF-002`, `INF-059`, `INF-071`, `INF-072` | panel and alert granularity |
| Objective | `OBJ-062` | constructed-ship ending |
| Time | `TIM-003` | live simulation with pause and speed |

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`: `ACT-006,ACT-120,ACT-144,ACT-145,ACT-147,ACT-148,ACT-149,ACT-150,ACT-151,ACT-152,ACT-155,ACT-156,ACT-157,ACT-158; SYS-004,SYS-045,SYS-051,SYS-156,SYS-158,SYS-161,SYS-186,SYS-196,SYS-197,SYS-198,SYS-203,SYS-204,SYS-205,SYS-206,SYS-194,SYS-208,SYS-209; CON-062,CON-172,CON-192,CON-193,CON-199,CON-200,CON-202,CON-203,CON-204,CON-205; INF-001,INF-002,INF-059,INF-071,INF-072; OBJ-062; TIM-003`.
- Indexed games scanned: 127, including this record.
- Indexed combinations scanned: 125.
- Exact genome matches: none.
- Near matches and similarity scores: `GAME-0126` Dwarf Fortress is the unique
  nearest game at `28 / 63 = 0.444444`; Oxygen Not Included follows at
  `22 / 68 = 0.323529`. Shared work, hauling, needs and live-colony genes expose
  the intended relationship, while RimWorld adds temporary direct draft control,
  storyteller pressure, local body capacities, caravans and a ship ending.
- Supported combination subsets: `COMB-0125`.
- Scan date: 2026-08-18.

### Full prior-game Jaccard scan

- `GAME-0001`: `3 / 59 = 0.050847`; `GAME-0002`: `1 / 54 = 0.018519`; `GAME-0003`: `0 / 57 = 0.000000`; `GAME-0004`: `4 / 59 = 0.067797`.
- `GAME-0005`: `1 / 54 = 0.018519`; `GAME-0006`: `1 / 56 = 0.017857`; `GAME-0007`: `1 / 55 = 0.018182`; `GAME-0008`: `1 / 54 = 0.018519`.
- `GAME-0009`: `3 / 61 = 0.049180`; `GAME-0010`: `1 / 56 = 0.017857`; `GAME-0011`: `1 / 60 = 0.016667`; `GAME-0012`: `1 / 56 = 0.017857`.
- `GAME-0013`: `1 / 60 = 0.016667`; `GAME-0014`: `1 / 62 = 0.016129`; `GAME-0015`: `2 / 60 = 0.033333`; `GAME-0016`: `4 / 59 = 0.067797`.
- `GAME-0017`: `0 / 61 = 0.000000`; `GAME-0018`: `5 / 62 = 0.080645`; `GAME-0019`: `1 / 57 = 0.017544`; `GAME-0020`: `2 / 60 = 0.033333`.
- `GAME-0021`: `2 / 55 = 0.036364`; `GAME-0022`: `2 / 58 = 0.034483`; `GAME-0023`: `0 / 58 = 0.000000`; `GAME-0024`: `1 / 59 = 0.016949`.
- `GAME-0025`: `3 / 56 = 0.053571`; `GAME-0026`: `2 / 58 = 0.034483`; `GAME-0027`: `4 / 56 = 0.071429`; `GAME-0028`: `6 / 59 = 0.101695`.
- `GAME-0029`: `4 / 56 = 0.071429`; `GAME-0030`: `4 / 58 = 0.068966`; `GAME-0031`: `2 / 57 = 0.035088`; `GAME-0032`: `1 / 58 = 0.017241`.
- `GAME-0033`: `2 / 59 = 0.033898`; `GAME-0034`: `3 / 59 = 0.050847`; `GAME-0035`: `3 / 63 = 0.047619`; `GAME-0036`: `1 / 59 = 0.016949`.
- `GAME-0037`: `1 / 56 = 0.017857`; `GAME-0038`: `2 / 62 = 0.032258`; `GAME-0039`: `1 / 56 = 0.017857`; `GAME-0040`: `1 / 55 = 0.018182`.
- `GAME-0041`: `2 / 57 = 0.035088`; `GAME-0042`: `2 / 55 = 0.036364`; `GAME-0043`: `1 / 61 = 0.016393`; `GAME-0044`: `1 / 57 = 0.017544`.
- `GAME-0045`: `1 / 61 = 0.016393`; `GAME-0046`: `1 / 57 = 0.017544`; `GAME-0047`: `1 / 61 = 0.016393`; `GAME-0048`: `1 / 61 = 0.016393`.
- `GAME-0049`: `0 / 57 = 0.000000`; `GAME-0050`: `1 / 62 = 0.016129`; `GAME-0051`: `5 / 59 = 0.084746`; `GAME-0052`: `1 / 57 = 0.017544`.
- `GAME-0053`: `1 / 56 = 0.017857`; `GAME-0054`: `1 / 58 = 0.017241`; `GAME-0055`: `1 / 57 = 0.017544`; `GAME-0056`: `1 / 55 = 0.018182`.
- `GAME-0057`: `1 / 55 = 0.018182`; `GAME-0058`: `1 / 56 = 0.017857`; `GAME-0059`: `1 / 54 = 0.018519`; `GAME-0060`: `1 / 54 = 0.018519`.
- `GAME-0061`: `1 / 57 = 0.017544`; `GAME-0062`: `1 / 55 = 0.018182`; `GAME-0063`: `1 / 54 = 0.018519`; `GAME-0064`: `1 / 52 = 0.019231`.
- `GAME-0065`: `0 / 55 = 0.000000`; `GAME-0066`: `0 / 58 = 0.000000`; `GAME-0067`: `2 / 54 = 0.037037`; `GAME-0068`: `0 / 56 = 0.000000`.
- `GAME-0069`: `1 / 55 = 0.018182`; `GAME-0070`: `1 / 55 = 0.018182`; `GAME-0071`: `1 / 54 = 0.018519`; `GAME-0072`: `1 / 55 = 0.018182`.
- `GAME-0073`: `1 / 54 = 0.018519`; `GAME-0074`: `1 / 56 = 0.017857`; `GAME-0075`: `1 / 56 = 0.017857`; `GAME-0076`: `1 / 54 = 0.018519`.
- `GAME-0077`: `1 / 54 = 0.018519`; `GAME-0078`: `1 / 54 = 0.018519`; `GAME-0079`: `1 / 54 = 0.018519`; `GAME-0080`: `1 / 54 = 0.018519`.
- `GAME-0081`: `1 / 55 = 0.018182`; `GAME-0082`: `1 / 55 = 0.018182`; `GAME-0083`: `1 / 55 = 0.018182`; `GAME-0084`: `1 / 57 = 0.017544`.
- `GAME-0085`: `0 / 59 = 0.000000`; `GAME-0086`: `1 / 60 = 0.016667`; `GAME-0087`: `2 / 56 = 0.035714`; `GAME-0088`: `1 / 56 = 0.017857`.
- `GAME-0089`: `1 / 56 = 0.017857`; `GAME-0090`: `1 / 62 = 0.016129`; `GAME-0091`: `2 / 55 = 0.036364`; `GAME-0092`: `4 / 54 = 0.074074`.
- `GAME-0093`: `1 / 56 = 0.017857`; `GAME-0094`: `2 / 56 = 0.035714`; `GAME-0095`: `2 / 58 = 0.034483`; `GAME-0096`: `2 / 56 = 0.035714`.
- `GAME-0097`: `2 / 54 = 0.037037`; `GAME-0098`: `2 / 53 = 0.037736`; `GAME-0099`: `1 / 55 = 0.018182`; `GAME-0100`: `1 / 58 = 0.017241`.
- `GAME-0101`: `0 / 58 = 0.000000`; `GAME-0102`: `0 / 55 = 0.000000`; `GAME-0103`: `1 / 56 = 0.017857`; `GAME-0104`: `1 / 56 = 0.017857`.
- `GAME-0105`: `1 / 57 = 0.017544`; `GAME-0106`: `0 / 55 = 0.000000`; `GAME-0107`: `1 / 55 = 0.018182`; `GAME-0108`: `1 / 57 = 0.017544`.
- `GAME-0109`: `3 / 61 = 0.049180`; `GAME-0110`: `2 / 54 = 0.037037`; `GAME-0111`: `1 / 54 = 0.018519`; `GAME-0112`: `2 / 54 = 0.037037`.
- `GAME-0113`: `2 / 60 = 0.033333`; `GAME-0114`: `2 / 53 = 0.037736`; `GAME-0115`: `1 / 53 = 0.018868`; `GAME-0116`: `2 / 52 = 0.038462`.
- `GAME-0117`: `1 / 55 = 0.018182`; `GAME-0118`: `2 / 62 = 0.032258`; `GAME-0119`: `11 / 60 = 0.183333`; `GAME-0120`: `2 / 75 = 0.026667`.
- `GAME-0121`: `2 / 69 = 0.028986`; `GAME-0122`: `4 / 59 = 0.067797`; `GAME-0123`: `2 / 84 = 0.023810`; `GAME-0124`: `12 / 83 = 0.144578`.
- `GAME-0125`: `22 / 68 = 0.323529`; `GAME-0126`: `28 / 63 = 0.444444`.

### Registry normalisation 006 score corrections

These recomputed values supersede the pre-normalisation fractions above:

- `GAME-0125`: `23 / 67 = 0.343284`
- Current prior-corpus near match after normalisation 006: `GAME-0126`.

## Evidence and unknowns

- The official product page establishes the base-game premise and major systems;
  the maintained 1.6 reference supplies reproducible operational detail.
- Exact storyteller, hit and recruitment probabilities are parameters, not genes.
- Direct play would improve confidence in current UI labels and rare ordering edges.

## Verification status

- Structure: reviewed.
- Evidence coverage: corroborated for all active claims.
- Novelty: new boundaries remain unassessed outside this corpus comparison.
- Web presentation and localisation: reviewed in this game unit.

## Next useful test

Compare Satisfactory against the expanded production and colony graph without
assuming that direct-avatar factory building shares autonomous-pawn work.

## Taxonomy impact

- Added four Action, six System Behaviour, four Constraint and one Objective
  gene where no active boundary covered RimWorld's exact mechanic.
- Reused Dwarf Fortress and Oxygen Not Included genes only where their
  operational definitions fit without broadening.
- `COMB-0124` is not a subset because RimWorld has no finite staffed job-slot
  assignment equivalent to `CON-185`; `COMB-0125` records the direct-crisis variant.

## Negative results

- `COMB-0124` did not recur exactly: RimWorld work permissions and ranked jobs
  do not assign a finite population to bounded staffed slots.
- `SYS-195` was rejected because RimWorld generates a planet and site without
  Dwarf Fortress's simulated persistent civilization history.
- `ACT-153` was rejected because drafting exact pawns is not persistent squad policy.

## Delta summary

## Нові факти

- RimWorld поєднує непрямі робочі політики з точним draft-керуванням під час криз.
- Storyteller перетворює багатство, населення й недавні втрати на змінний тиск подій.
- Локальні травми, думки й стосунки можуть змінити працездатність або забрати контроль.

## Нові гени

- `ACT-155`–`ACT-158`; `SYS-203`–`SYS-206`, `SYS-208`, `SYS-209`;
  `CON-202`–`CON-205`; `OBJ-062`.

## Нові комбінації

- `COMB-0125` — автономна праця колонії з прямим тактичним перехопленням під час криз.

## Зміни таксономії

- Нових родин не створено. Гра включена до `FAM-008`, `FAM-010`, `FAM-015`
  і `FAM-017`.

## Нові питання

- Чи повторить Satisfactory виробничі залежності без автономної праці мешканців?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] Satisfactory.
- Optimisation criterion: continue approved Batch 02 while testing direct-avatar
  construction against the established automation graph.
- Expected information gain: separate live production recurrence from autonomous-agent labour.
- Backlog impact: preserves Frostpunk as the following colony-pressure test.

## Чому саме вона

- [Hypothesis | Limited | High] Satisfactory should reuse factory-network genes
  while sharply contrasting RimWorld's pawn needs, storyteller and draft control.
