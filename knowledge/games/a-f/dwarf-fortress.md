---
game_id: GAME-0126
slug: dwarf-fortress
game_title: Dwarf Fortress
analysis_status: reviewed
reviewed: 2026-08-18
combination_ids:
  - COMB-0124
gene_ids:
  action:
    - ACT-006
    - ACT-120
    - ACT-142
    - ACT-144
    - ACT-145
    - ACT-148
    - ACT-150
    - ACT-151
    - ACT-152
    - ACT-153
    - ACT-154
  system:
    - SYS-004
    - SYS-045
    - SYS-051
    - SYS-156
    - SYS-158
    - SYS-161
    - SYS-186
    - SYS-192
    - SYS-195
    - SYS-196
    - SYS-197
    - SYS-198
    - SYS-199
    - SYS-200
    - SYS-201
    - SYS-202
  constraint:
    - CON-062
    - CON-172
    - CON-185
    - CON-193
    - CON-195
    - CON-198
    - CON-199
    - CON-200
    - CON-201
  information:
    - INF-001
    - INF-002
    - INF-003
    - INF-071
    - INF-072
  objective:
    - OBJ-061
  time:
    - TIM-003
---

# Game: Dwarf Fortress

## Analysis scope

- Version / ruleset: Premium/Steam `v53.15`, released 2026-06-25; ordinary
  Fortress Mode from world generation, site and seven-dwarf embark through
  capital eligibility and arrival of the civilization's monarch.
- Included: embark budget; excavation, construction, workshops, work details,
  priorities, stockpiles and manager orders; rooms, offices, needs, thoughts,
  stress and strange moods; caravans, nobles, squads and world-connected sieges.
- Excluded: Adventure, Legends and Arena modes; Classic-interface differences;
  mods and DFHack; custom challenges and megaprojects; off-site mission
  optimisation; the post-arrival seven-symbol Mountainhome quest.
- Direct-play status: not conducted. The official product and release pages
  establish the current ruleset; the maintained version-53.15 reference
  corroborates the scoped transitions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DF-001` | A seed creates a persistent historical world and concealed multi-level site | Confirmed | Corroborated | High | P1, P2, P3 |
| `DF-002` | Site, seven residents, skills, goods and animals share one embark budget | Confirmed | Corroborated | High | P4 |
| `DF-003` | Designations and priorities create jobs claimed by eligible reachable residents | Confirmed | Corroborated | High | P5, P6, P7 |
| `DF-004` | Filtered stockpiles and links route autonomous hauling and workshop supply | Confirmed | Corroborated | High | P8, P9 |
| `DF-005` | Manager conditions can repeat production according to visible stocks | Confirmed | Corroborated | High | P10 |
| `DF-006` | Individual needs, experience, memory and personality alter focus and stress | Confirmed | Corroborated | High | P11, P12 |
| `DF-007` | Strange moods claim a workshop and requested materials for artifact production | Confirmed | Corroborated | High | P13 |
| `DF-008` | Seasonal caravans reach a depot and exchange value through a trader | Confirmed | Corroborated | High | P14, P15, P16 |
| `DF-009` | Squads execute persistent equipment, schedule and active-order policies | Confirmed | Corroborated | High | P17, P18 |
| `DF-010` | Population and wealth promote settlement rank toward monarch arrival | Confirmed | Corroborated | High | P19, P20 |
| `DF-011` | Current hostile forces may path, destroy, dig or build toward targets | Confirmed | Corroborated | High | P2, P21 |

## Basic data

- Release / origin: Bay 12 Games; Premium edition published by Kitfox Games,
  released in 2022 and updated to version 53.15 on 2026-06-25.
- Platform or physical form: real-time desktop colony and world simulation.
- Puzzle family: automation and spatial programming; real-time system pressure;
  agent routing and coordination; ordered dependency sequencing.
- Primary sources: **[P1]** [official Steam page](https://store.steampowered.com/app/975370/Dwarf_Fortress/);
  **[P2]** [official Bay 12 release page](https://bay12games.com/dwarves/);
  **[P3]** [current version-53.15 reference](https://dwarffortresswiki.org/);
  **[P4]** [Embark](https://dwarffortresswiki.org/index.php/Embark);
  **[P5]** [Fortress Mode](https://dwarffortresswiki.org/index.php/Fortress_mode);
  **[P6]** [Designations](https://dwarffortresswiki.org/index.php/Designations);
  **[P7]** [Work details](https://dwarffortresswiki.org/index.php/Work_detail);
  **[P8]** [Stockpiles](https://dwarffortresswiki.org/index.php/Stockpiles);
  **[P9]** [Hauling](https://dwarffortresswiki.org/index.php/Haul);
  **[P10]** [Work orders](https://dwarffortresswiki.org/index.php/Work_orders);
  **[P11]** [Thoughts and preferences](https://dwarffortresswiki.org/index.php/Thoughts_and_Preferences);
  **[P12]** [Stress](https://dwarffortresswiki.org/index.php/Stress);
  **[P13]** [Strange mood](https://dwarffortresswiki.org/index.php/Strange_mood);
  **[P14]** [Trading](https://dwarffortresswiki.org/index.php/Trading);
  **[P15]** [Trade depot](https://dwarffortresswiki.org/index.php/Depot);
  **[P16]** [Broker](https://dwarffortresswiki.org/index.php/Broker);
  **[P17]** [Squads](https://dwarffortresswiki.org/index.php/Squads);
  **[P18]** [Schedules](https://dwarffortresswiki.org/index.php/Schedule);
  **[P19]** [Settlement ranks](https://dwarffortresswiki.org/index.php/Population);
  **[P20]** [Monarch](https://dwarffortresswiki.org/index.php/Monarch);
  **[P21]** [Siege](https://dwarffortresswiki.org/index.php/Siege).
- Claim IDs: `DF-001`–`DF-011`.

## Mechanical decomposition

### Action Genes

- Reused: `ACT-006`, `ACT-120`, `ACT-142`, `ACT-144`, `ACT-145` and
  `ACT-148` cover speed, configuration, embark, designations, priority and plans.
- New: `ACT-150`–`ACT-154` cover conditional orders, linked stockpiles,
  institutional zones, military policy and appointed offices.
- Claim IDs: `DF-002`–`DF-005`, `DF-008`–`DF-010`.

### System Behaviour Genes

- Reused: autonomous locomotion and job brokerage, production, power,
  extraction, trigger networks, combat and seeded outcomes.
- New: `SYS-195`–`SYS-202` cover historical sites, filtered hauling,
  quality, personal stress, migration and rank, moods, caravans and sieges.
- Resolution order: accept policy; broker eligible jobs; path agents and items;
  execute work, needs and mechanisms; resolve world arrivals and conflict;
  update wealth, population, stress, rank and terminal eligibility.
- Claim IDs: `DF-001`, `DF-003`–`DF-011`.

### Constraint Genes

- Reused: compatible footprints and recipes, finite staffing, supplied
  construction and agent survival.
- New: `CON-198`–`CON-201` bind embark spending, job eligibility, stockpile
  acceptance and institutional requirements.
- Scarce strategic resources: resident time, food, drink, beds, tools,
  materials, containers, safe paths, workshop capacity and defensive readiness.
- Claim IDs: `DF-002`–`DF-010`.

### Information Genes

- `INF-001`–`INF-003` separate revealed current state, unknown future arrivals
  and concealed terrain; `INF-071` exposes colony reports; `INF-072` explains
  one resident's work, needs, thoughts and relationships.
- Claim IDs: `DF-001`, `DF-003`–`DF-011`.

### Objective Genes

- `OBJ-061` retains open-ended survival while bounding this record at capital
  eligibility and monarch arrival, before the newer Mountainhome quest.
- Claim IDs: `DF-010`.

### Time Genes

- `TIM-003`: jobs, residents, fluids, mechanisms, caravans and enemies advance
  in real time with pause and speed controls.
- Claim IDs: `DF-003`–`DF-011`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| One preparation pool is unspent | Add a mining skill and pickaxe | both costs reduce the same remaining embark points | starting capability competes with supplies | `DF-002` |
| A rock wall is reachable by an enabled miner | Mark it for mining | a mining job enters the pool; the dwarf claims it and leaves stone | spatial orders broker autonomous work | `DF-003` |
| A food stockpile accepts prepared meals | Paint it near the dining room | haulers move matching meals into free accepted tiles | storage filters reshape labour and distance | `DF-004` |
| Drinks are below ten and a still has inputs | Enable a conditional brew order | the manager permits jobs until the checked stock condition is satisfied | visible reserves can control repeated production | `DF-005` |
| A skilled craftsdwarf completes a metal item | Let the workshop job finish | material and skill determine time, quality and item value | agents and matter jointly shape output | `DF-005` |
| A resident repeatedly lacks sleep and social contact | Continue ordinary time | unmet needs and memories reduce focus and can raise stress | labourers retain personal causal histories | `DF-006` |
| A moody dwarf has claimed a craft workshop | Supply every demanded material | the dwarf consumes them, creates an artifact and gains mastery | a random event becomes a material dependency puzzle | `DF-007` |
| A caravan reaches an accessible depot | Move selected lots and approve trade | accepted values exchange and the caravan retains the agreed goods | world relations enter through spatial logistics | `DF-008` |
| A trained equipped squad has an active station order | Unpause the simulation | scheduled members equip and path toward the declared station | military control is authored policy, not direct movement | `DF-009` |
| Population, wealth, rank and rooms satisfy capital rules | Continue until the monarch travels | the monarch arrives and the fortress becomes the civilization's capital | the open simulation has a reproducible horizon | `DF-010` |

## Strategic and experiential structure

- Local decision: choose which job, shortage, route or resident deserves scarce
  attention while autonomous work and needs continue elsewhere.
- Medium-term planning: shorten material routes, condition production on stock,
  qualify rooms and offices, and train a force without collapsing civilian work.
- Long-term structure: transform a seven-person expedition into a resilient
  capital embedded in the generated civilization and its trade and wars.
- Common heuristics: keep drink and food loops redundant; inspect job
  cancellations; place specialised stores near consumers; limit simultaneous
  designations; read resident profiles before treating stress as random.
- Failure attribution: jobs, announcements, stocks and citizen panels expose
  proximate causes, though long remembered experiences and world events can
  make the initiating cause historically distant.
- Claim IDs: `DF-001`–`DF-011`.

## Replay and variation

- What changes: world history, civilizations, geology, aquifers, resources,
  residents, moods, migrants, caravans, artifacts, enemies and emergent stories.
- Randomness: generated state changes the problem, while filters, eligibility,
  recipes, room requirements and visible causal reports remain inspectable.
- Multiple viable strategies: yes; layouts, industries, welfare, trade,
  defence, water engineering and institutional growth admit different solutions.
- Typical replay motive: discover how the same policy tools interact with a new
  historical world, site, population and sequence of crises.
- Claim IDs: `DF-001`, `DF-006`–`DF-011`.

## Adjacent systems and history

- Direct predecessors: settlement simulations, roguelike world generation,
  economic production games and autonomous-agent management.
- Similar games: Oxygen Not Included, RimWorld, Factorio and Against the Storm.
- Important difference: Dwarf Fortress connects resident-scale needs and jobs
  to a persistent generated world whose civilizations, histories and attacks
  remain mechanically active.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-006`, `ACT-120`, `ACT-142`, `ACT-144`, `ACT-145`, `ACT-148`, `ACT-150`–`ACT-154` | job, room, link and policy parameters |
| System Behaviour | `SYS-004`, `SYS-045`, `SYS-051`, `SYS-156`, `SYS-158`, `SYS-161`, `SYS-186`, `SYS-192`, `SYS-195`–`SYS-202` | history, labour, need and world-event parameters |
| Constraint | `CON-062`, `CON-172`, `CON-185`, `CON-193`, `CON-195`, `CON-198`–`CON-201` | eligibility, stock and institution thresholds |
| Information | `INF-001`–`INF-003`, `INF-071`, `INF-072` | report and profile granularity |
| Objective | `OBJ-061` | capital and monarch threshold |
| Time | `TIM-003` | live simulation with pause and speed |

## Corpus comparison

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`: `ACT-006,ACT-120,ACT-142,ACT-144,ACT-145,ACT-148,ACT-150,ACT-151,ACT-152,ACT-153,ACT-154; SYS-004,SYS-045,SYS-051,SYS-156,SYS-158,SYS-161,SYS-186,SYS-192,SYS-195,SYS-196,SYS-197,SYS-198,SYS-199,SYS-200,SYS-201,SYS-202; CON-062,CON-172,CON-185,CON-193,CON-195,CON-198,CON-199,CON-200,CON-201; INF-001,INF-002,INF-003,INF-071,INF-072; OBJ-061; TIM-003`.
- Indexed games scanned: 126, including this record.
- Indexed combinations scanned: 124.
- Exact genome matches: none.
- Near matches and similarity scores: `GAME-0125` Oxygen Not Included is the
  unique nearest game at `21 / 64 = 0.328125`; Against the Storm follows at
  `14 / 76 = 0.184211`, and Factorio at `10 / 56 = 0.178571`. ONI shares
  autonomous labour, construction, survival and live infrastructure, while
  Dwarf Fortress adds persistent history, offices, trade, moods and war and
  does not share ONI's conserved material-cell atmosphere.
- Supported combination subsets: `COMB-0124`.
- Scan date: 2026-08-18.

### Full prior-game Jaccard scan

- `GAME-0001`: `3 / 54 = 0.055556`; `GAME-0002`: `1 / 49 = 0.020408`; `GAME-0003`: `1 / 51 = 0.019608`; `GAME-0004`: `4 / 54 = 0.074074`.
- `GAME-0005`: `1 / 49 = 0.020408`; `GAME-0006`: `1 / 51 = 0.019608`; `GAME-0007`: `1 / 50 = 0.020000`; `GAME-0008`: `1 / 49 = 0.020408`.
- `GAME-0009`: `3 / 56 = 0.053571`; `GAME-0010`: `1 / 51 = 0.019608`; `GAME-0011`: `1 / 55 = 0.018182`; `GAME-0012`: `1 / 51 = 0.019608`.
- `GAME-0013`: `1 / 55 = 0.018182`; `GAME-0014`: `1 / 57 = 0.017544`; `GAME-0015`: `2 / 55 = 0.036364`; `GAME-0016`: `4 / 54 = 0.074074`.
- `GAME-0017`: `1 / 55 = 0.018182`; `GAME-0018`: `5 / 57 = 0.087719`; `GAME-0019`: `1 / 52 = 0.019231`; `GAME-0020`: `2 / 55 = 0.036364`.
- `GAME-0021`: `2 / 50 = 0.040000`; `GAME-0022`: `2 / 53 = 0.037736`; `GAME-0023`: `0 / 53 = 0.000000`; `GAME-0024`: `1 / 54 = 0.018519`.
- `GAME-0025`: `3 / 51 = 0.058824`; `GAME-0026`: `2 / 53 = 0.037736`; `GAME-0027`: `4 / 51 = 0.078431`; `GAME-0028`: `6 / 54 = 0.111111`.
- `GAME-0029`: `4 / 51 = 0.078431`; `GAME-0030`: `4 / 53 = 0.075472`; `GAME-0031`: `2 / 52 = 0.038462`; `GAME-0032`: `1 / 53 = 0.018868`.
- `GAME-0033`: `2 / 54 = 0.037037`; `GAME-0034`: `3 / 54 = 0.055556`; `GAME-0035`: `3 / 58 = 0.051724`; `GAME-0036`: `1 / 54 = 0.018519`.
- `GAME-0037`: `1 / 51 = 0.019608`; `GAME-0038`: `2 / 57 = 0.035088`; `GAME-0039`: `1 / 51 = 0.019608`; `GAME-0040`: `1 / 50 = 0.020000`.
- `GAME-0041`: `2 / 52 = 0.038462`; `GAME-0042`: `2 / 50 = 0.040000`; `GAME-0043`: `1 / 56 = 0.017857`; `GAME-0044`: `1 / 52 = 0.019231`.
- `GAME-0045`: `1 / 56 = 0.017857`; `GAME-0046`: `1 / 52 = 0.019231`; `GAME-0047`: `2 / 55 = 0.036364`; `GAME-0048`: `1 / 56 = 0.017857`.
- `GAME-0049`: `1 / 51 = 0.019608`; `GAME-0050`: `1 / 57 = 0.017544`; `GAME-0051`: `5 / 54 = 0.092593`; `GAME-0052`: `1 / 52 = 0.019231`.
- `GAME-0053`: `1 / 51 = 0.019608`; `GAME-0054`: `1 / 53 = 0.018868`; `GAME-0055`: `1 / 52 = 0.019231`; `GAME-0056`: `1 / 50 = 0.020000`.
- `GAME-0057`: `1 / 50 = 0.020000`; `GAME-0058`: `1 / 51 = 0.019608`; `GAME-0059`: `1 / 49 = 0.020408`; `GAME-0060`: `1 / 49 = 0.020408`.
- `GAME-0061`: `1 / 52 = 0.019231`; `GAME-0062`: `1 / 50 = 0.020000`; `GAME-0063`: `1 / 49 = 0.020408`; `GAME-0064`: `1 / 47 = 0.021277`.
- `GAME-0065`: `1 / 49 = 0.020408`; `GAME-0066`: `1 / 52 = 0.019231`; `GAME-0067`: `2 / 49 = 0.040816`; `GAME-0068`: `1 / 50 = 0.020000`.
- `GAME-0069`: `1 / 50 = 0.020000`; `GAME-0070`: `1 / 50 = 0.020000`; `GAME-0071`: `1 / 49 = 0.020408`; `GAME-0072`: `1 / 50 = 0.020000`.
- `GAME-0073`: `1 / 49 = 0.020408`; `GAME-0074`: `1 / 51 = 0.019608`; `GAME-0075`: `1 / 51 = 0.019608`; `GAME-0076`: `1 / 49 = 0.020408`.
- `GAME-0077`: `1 / 49 = 0.020408`; `GAME-0078`: `1 / 49 = 0.020408`; `GAME-0079`: `1 / 49 = 0.020408`; `GAME-0080`: `1 / 49 = 0.020408`.
- `GAME-0081`: `1 / 50 = 0.020000`; `GAME-0082`: `1 / 50 = 0.020000`; `GAME-0083`: `1 / 50 = 0.020000`; `GAME-0084`: `1 / 52 = 0.019231`.
- `GAME-0085`: `1 / 53 = 0.018868`; `GAME-0086`: `1 / 55 = 0.018182`; `GAME-0087`: `2 / 51 = 0.039216`; `GAME-0088`: `1 / 51 = 0.019608`.
- `GAME-0089`: `1 / 51 = 0.019608`; `GAME-0090`: `1 / 57 = 0.017544`; `GAME-0091`: `2 / 50 = 0.040000`; `GAME-0092`: `4 / 49 = 0.081633`.
- `GAME-0093`: `1 / 51 = 0.019608`; `GAME-0094`: `2 / 51 = 0.039216`; `GAME-0095`: `2 / 53 = 0.037736`; `GAME-0096`: `2 / 51 = 0.039216`.
- `GAME-0097`: `2 / 49 = 0.040816`; `GAME-0098`: `2 / 48 = 0.041667`; `GAME-0099`: `1 / 50 = 0.020000`; `GAME-0100`: `1 / 53 = 0.018868`.
- `GAME-0101`: `0 / 53 = 0.000000`; `GAME-0102`: `0 / 50 = 0.000000`; `GAME-0103`: `1 / 51 = 0.019608`; `GAME-0104`: `1 / 51 = 0.019608`.
- `GAME-0105`: `1 / 52 = 0.019231`; `GAME-0106`: `0 / 50 = 0.000000`; `GAME-0107`: `1 / 50 = 0.020000`; `GAME-0108`: `1 / 52 = 0.019231`.
- `GAME-0109`: `3 / 56 = 0.053571`; `GAME-0110`: `2 / 49 = 0.040816`; `GAME-0111`: `1 / 49 = 0.020408`; `GAME-0112`: `2 / 49 = 0.040816`.
- `GAME-0113`: `2 / 55 = 0.036364`; `GAME-0114`: `2 / 48 = 0.041667`; `GAME-0115`: `1 / 48 = 0.020833`; `GAME-0116`: `2 / 47 = 0.042553`.
- `GAME-0117`: `1 / 50 = 0.020000`; `GAME-0118`: `2 / 57 = 0.035088`; `GAME-0119`: `10 / 56 = 0.178571`; `GAME-0120`: `3 / 69 = 0.043478`.
- `GAME-0121`: `2 / 64 = 0.031250`; `GAME-0122`: `4 / 54 = 0.074074`; `GAME-0123`: `3 / 78 = 0.038462`; `GAME-0124`: `14 / 76 = 0.184211`.
- `GAME-0125`: `21 / 64 = 0.328125`.

## Evidence and unknowns

- The official product and release pages are authoritative for the current
  edition and world-colony premise; current 53.15 wiki pages provide maintained
  community evidence for exact mechanics.
- Numeric thresholds and probabilities remain parameters rather than genes.
- Direct play would improve observations of ordering, current labels and rare events.

## Verification status

- Structure: reviewed.
- Evidence coverage: corroborated for all active claims.
- Novelty: new boundaries remain candidates until independent recurrence.
- Web presentation and localisation: reviewed in this game unit.

## Next useful test

Run the nine-game batch audit, then compare RimWorld against the newly observed
autonomous-colony boundary without assuming either game is a clone.

## Taxonomy impact

- Added five Action, eight System Behaviour, four Constraint, one Information
  and one Objective gene where no active boundary covered the mechanic.
- Reused autonomous errand, production, survival and information genes only
  where their operational definitions fit Dwarf Fortress.
- `COMB-0124` tests recurrence of authored spatial work through autonomous agents.

## Negative results

- `COMB-0123` is not a subset: Dwarf Fortress does not simulate Oxygen Not
  Included's conserved gas-cell atmosphere, morale debt or conduit context.
- `SYS-187` and `SYS-188` were rejected: DF fluids and temperature do not share
  ONI's complete conserved cell-mass and phase-transition boundary.
- `ACT-146` was rejected: DF skills chiefly grow through work rather than a
  player-spent prerequisite point with morale expectation.

## Delta summary

## Нові факти

- Просторові позначення, фільтри й політики створюють роботу, яку автономно
  розбирають мешканці з власними навичками, потребами та пам’яттю.
- Фортеця є частиною згенерованого історичного світу, а не ізольованою мапою.
- Прибуття монарха дає перевірювану межу аналізу перед новим квестом Mountainhome.

## Нові гени

- `ACT-150`–`ACT-154`; `SYS-195`–`SYS-202`; `CON-198`–`CON-201`; `INF-072`; `OBJ-061`.

## Нові комбінації

- `COMB-0124` — автономна робота фортеці через просторові позначення,
  фільтроване постачання й умовне виробництво.

## Зміни таксономії

- Нових родин не створено. Гра включена до `FAM-008`, `FAM-010`, `FAM-015`
  і `FAM-017`.
