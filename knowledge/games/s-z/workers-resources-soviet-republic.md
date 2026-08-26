---
game_id: GAME-0134
slug: workers-resources-soviet-republic
game_title: "Workers & Resources: Soviet Republic"
analysis_status: reviewed
reviewed: 2026-08-21
combination_ids:
  - COMB-0132
gene_ids:
  action:
    - ACT-006
    - ACT-023
    - ACT-068
    - ACT-117
    - ACT-120
    - ACT-139
    - ACT-145
    - ACT-148
    - ACT-149
    - ACT-177
    - ACT-178
  system:
    - SYS-156
    - SYS-157
    - SYS-194
    - SYS-264
    - SYS-265
    - SYS-266
    - SYS-267
    - SYS-268
    - SYS-269
    - SYS-270
    - SYS-271
    - SYS-273
    - SYS-274
  constraint:
    - CON-062
    - CON-172
    - CON-173
    - CON-184
    - CON-185
    - CON-236
    - CON-237
    - CON-238
    - CON-239
    - CON-240
    - CON-241
    - CON-242
    - CON-243
    - CON-244
  information:
    - INF-001
    - INF-058
    - INF-059
    - INF-060
    - INF-086
    - INF-098
    - INF-099
    - INF-100
    - INF-101
    - INF-102
    - INF-103
  objective:
    - OBJ-069
  time:
    - TIM-003
---

# Game: Workers & Resources: Soviet Republic

## Analysis scope

- Version / ruleset: released PC base game `1.1.1.7` (16 June 2026), no
  paid DLC; fresh profile, completing `A New Republic is Born` and then every
  mandatory branch of the unlocked `Soviet Revolution` campaign.
- Included: placed settlements and networks; citizens, education, jobs, needs
  and public transport; road and rail freight; staffed recipes; construction
  and distribution offices; customs, rubles, dollars and market response;
  power, heating, water, sewage, pollution, seasons, fire, waste and wear where
  enabled by the campaigns; university research; nuclear fuel, generation and
  waste; campaign objective scripts.
- Excluded: sandbox after campaign completion; custom difficulty or maps;
  Early Start, Biomes, World Maps and other DLC; mods; exhaustive aircraft,
  tourism, personal-car, ship and every optional industry route.
- Direct-play status: not conducted. Current official release notes establish
  the version; official publisher wiki mechanics and campaign documentation
  establish the bounded route and operational gates.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `WRSR-001` | `1.1.1.7` is the current documented base version and released 16 June 2026 | Confirmed | Direct | High | P1–P2 |
| `WRSR-002` | The two released campaigns are sequential and progress through branching measured objectives | Confirmed | Direct | High | P3–P5 |
| `WRSR-003` | Citizens seek jobs and services by walking or enabled transit, with one-hour waiting and four-hour in-vehicle limits | Confirmed | Corroborated | High | P6 |
| `WRSR-004` | Scheduled vehicles carry people or physical goods through compatible road and rail networks | Confirmed | Corroborated | High | P6–P7 |
| `WRSR-005` | Construction offices dispatch materials, mechanisms and labour from assigned sources by phase and priority | Confirmed | Corroborated | High | P8–P9 |
| `WRSR-006` | Distribution offices dispatch suitable vehicles from configured supply, demand and storage thresholds | Confirmed | Corroborated | High | P9–P10 |
| `WRSR-007` | Customs physically settle trade in rubles or dollars and traded volume changes later market prices | Confirmed | Corroborated | High | P11–P13 |
| `WRSR-008` | Electricity, heat, water and sewage depend on connected network capacity and live operating state | Confirmed | Corroborated | High | P14–P16 |
| `WRSR-009` | Staffed universities accumulate workdays through prerequisite research trees | Confirmed | Corroborated | High | P17 |
| `WRSR-010` | Nuclear production couples uranium processing, fuel fabrication, qualified staff, cooling, power, waste and radiation | Confirmed | Corroborated | High | P18–P20 |
| `WRSR-011` | Campaign 2 includes a fuel-independence / nuclear-fuel export route | Confirmed | Corroborated | High | P4, P21 |
| `WRSR-012` | Completing Campaign 2 after Campaign 1 is a bounded endpoint that exercises the republic's linked economy | Observation | Corroborated | High | P3–P5, P21 |

## Basic data

- Release / origin: 3Division; Early Access 15 March 2019; full PC release
  20 June 2024; published by Hooded Horse.
- Form: pausable real-time city-building, logistics and command-economy simulation.
- Puzzle family: network construction; resource and logistics optimisation;
  agent routing; ordered dependencies; real-time system pressure.
- Primary and official sources:
  - **[P1]** [official game page](https://wiki.hoodedhorse.com/Workers_Resources_Soviet_Republic/Workers_%26_Resources%3A_Soviet_Republic), release, developer and current version list.
  - **[P2]** [official Update 1.1.1.7 notes](https://wiki.hoodedhorse.com/Workers_Resources_Soviet_Republic/Update_1.1.1.7), version date and current changes.
  - **[P3]** [official campaign report](https://wiki.hoodedhorse.com/Workers_Resources_Soviet_Republic/Report_for_the_community_80), sequential campaigns, branches and measured objectives.
  - **[P4]** [official maps reference](https://wiki.hoodedhorse.com/Workers_Resources_Soviet_Republic/Maps), campaign maps and starting populations.
  - **[P5]** [official game settings](https://wiki.hoodedhorse.com/Workers_Resources_Soviet_Republic/Game_settings), campaign and realistic-rule boundaries.
- Current mechanics references:
  - **[P6]** [Citizens](https://wiki.hoodedhorse.com/Workers_Resources_Soviet_Republic/How_to_treat_your_citizens%3F), work, education and travel limits.
  - **[P7]** [Resources](https://wiki.hoodedhorse.com/Workers_Resources_Soviet_Republic/Resources), physical goods, storages and transport classes.
  - **[P8]** [Construction office](https://wiki.hoodedhorse.com/Workers_Resources_Soviet_Republic/Construction_office), sources, vehicles, phases and priority.
  - **[P9]** [Questions and answers](https://wiki.hoodedhorse.com/Workers_Resources_Soviet_Republic/Questions_and_answers), construction and distribution workflows.
  - **[P10]** [Research](https://wiki.hoodedhorse.com/Workers_Resources_Soviet_Republic/Research), distribution-office and other workday unlocks.
  - **[P11]** [Trade](https://wiki.hoodedhorse.com/Workers_Resources_Soviet_Republic/Trade), customs, blocs and currencies.
  - **[P12]** [Economy](https://wiki.hoodedhorse.com/Workers_Resources_Soviet_Republic/Economy), line-driven manual trade.
  - **[P13]** [official market report](https://wiki.hoodedhorse.com/Workers_Resources_Soviet_Republic/Report_for_the_community_56), volume-responsive prices.
  - **[P14]** [Electricity](https://wiki.hoodedhorse.com/Workers_Resources_Soviet_Republic/Voltage_wires), imports, generation and grid distribution.
  - **[P15]** [Heating](https://wiki.hoodedhorse.com/Workers_Resources_Soviet_Republic/Heating), temperature, pipe loss and health.
  - **[P16]** [roadmap](https://wiki.hoodedhorse.com/Workers_Resources_Soviet_Republic/Roadmap_building_a_republic), city, utilities, work and production dependencies.
  - **[P17]** [Researches](https://wiki.hoodedhorse.com/Workers_Resources_Soviet_Republic/Researches), faculty, prerequisite and workday costs.
  - **[P18]** [Nuclear fuel](https://wiki.hoodedhorse.com/Workers_Resources_Soviet_Republic/Nuclear_fuel), material and fabrication chain.
  - **[P19]** [Nuclear power plant](https://wiki.hoodedhorse.com/Workers_Resources_Soviet_Republic/Nuclear_power_plant), staff, fuel, cooling and waste gates.
  - **[P20]** [Energy management](https://wiki.hoodedhorse.com/Workers_Resources_Soviet_Republic/Energy_management), supply and outage effects.
  - **[P21]** [Update 1.0.0.7](https://wiki.hoodedhorse.com/Workers_Resources_Soviet_Republic/Update_1.0.0.7), Campaign 2 nuclear-fuel objective fixes.
- Claim IDs: `WRSR-001`–`WRSR-012`.

## Mechanical decomposition

### Action Genes

- Reused: `ACT-006` changes simulation speed; `ACT-023` edits ordered lines;
  `ACT-068` edits roads; `ACT-117` places utilities; `ACT-120` configures local
  recipes, vehicle stops and filters; `ACT-139` places settlement buildings;
  `ACT-145` changes priorities; `ACT-148` places material-backed plans;
  `ACT-149` selects staffed research.
- New: `ACT-177` configures an office's automatic remit; `ACT-178` commits
  foreign purchases or border power rules.

### System Behaviour Genes

- Reused: `SYS-156` runs production recipes; `SYS-157` transports physical
  cargo through live logistics; `SYS-194` converts staffed research work into
  a technology unlock.
- New: `SYS-264`–`SYS-271`, `SYS-273` and `SYS-274` cover citizens, transit, vehicle lines, construction
  and distribution dispatch, responsive trade, utilities, environmental wear,
  research, nuclear operation and campaign scripts.
- Resolution order: accept edits; update time and environment; route citizens
  and vehicles; dispatch offices; run utilities and recipes; settle trade;
  advance research, nuclear state and objective counters.

### Constraint Genes

- Reused: `CON-062` footprint; `CON-172` recipe flow; `CON-173` extraction
  locus; `CON-184` available design and materials; `CON-185` finite staff slots.
- New: `CON-236`–`CON-244` separate phased construction, vehicle compatibility,
  citizen travel eligibility, office remit, utilities, customs, research,
  nuclear safety and sequential campaign gates.

### Information Genes

- Reused: `INF-001` exposes the map; `INF-058` the economy ledger; `INF-059`
  recipes and research dependencies; `INF-060` live production diagnostics;
  `INF-086` citizen well-being and workforce state.
- New: `INF-098`–`INF-103` expose transport, construction, trade,
  utilities and environment, nuclear research and campaign progress.

### Objective and Time Genes

- `OBJ-069` ends after both released base campaigns; `TIM-003` advances the
  pausable republic simulation.

## Reproducible transitions

| Before | Action | Bounded resolution | Establishes | Claims |
|---|---|---|---|---|
| Fresh profile | Finish Campaign 1 | Its measured branches complete and unlock Campaign 2 | sequential endpoint | `WRSR-002` |
| Housing, jobs, stop and line | Assign bus and advance | workers walk, wait, ride and fill eligible jobs or time out | physical labour commute | `WRSR-003`–`004` |
| Planned structure and configured office | Assign sources, fleet and priority | vehicles deliver each phase's inputs and work advances | realistic construction | `WRSR-005` |
| Supply and demand storages | Set resource and percentage rules | suitable truck dispatches only across triggered thresholds | demand dispatch differs from lines | `WRSR-006` |
| Factory output and customs route | Run export line over several periods | physical cargo yields bloc currency; sustained volume changes price | responsive dual market | `WRSR-007` |
| Generator and connected consumers | Advance under changing load | capacity and network loss determine supplied operation | utilities are live networks | `WRSR-008` |
| Staffed university and reachable project | Select research and advance | qualified workdays accumulate, then unlock capability | research consumes labour-time | `WRSR-009` |
| Fuel plant and reactor chain | Supply chemicals, uranium, staff and cooling | fuel becomes power and waste; blocked waste stops operation | nuclear dependency | `WRSR-010` |
| Campaign 2 fuel objective active | Produce and export required fuel | objective counter records physical delivery and completes branch | simulation feeds script | `WRSR-011` |
| Every mandatory Campaign 2 branch done | Advance objective state | completion presentation fires; sandbox may continue | bounded corpus endpoint | `WRSR-012` |

## Strategic and experiential structure

- Local: place one building or network edge, revise one line, recipe, office,
  priority, import or research target.
- Medium term: synchronise housing, travel, staffing, utilities, construction
  fleets, storages, factories and cash flow without teleporting dependencies.
- Long term: replace imports, research the nuclear chain and satisfy all
  Campaign 2 branches through physically produced exports.
- Failure attribution: citizen, line, site, utility, economy, research and
  objective panels expose current bottlenecks; future prices and incidents vary.

## Replay and variation

- What changes: settlement and industrial placement, route topology, vehicle
  mix, construction order, import substitution and power strategy.
- Randomness: campaign maps and required branches are authored; fires, market
  context and operating delays vary within the simulation rules.
- Multiple viable strategies: yes; mandatory measured objectives admit
  different networks and production balances.

## Adjacent systems and history

- Similar games: Cities: Skylines, Factorio, Anno 1800, Oxygen Not Included,
  Frostpunk and Timberborn.
- Historical position: the 2024 full release consolidated a long Early Access
  simulation into base-game campaigns that teach its physical economy.

## Adjacent comparison

- Cities: Skylines shares roads and utilities but abstracts goods, construction
  and much citizen travel; Factorio shares recipes and scheduled cargo but not
  finite educated citizens or dual border markets; Anno 1800 shares production
  and trade but ships do not instantiate this office-dispatch/construction stack.

## Taxonomy impact

- Existing line, road, recipe, staffing and diagnostic genes keep their limits.
  New genes isolate office remits, physical phased construction, citizen transit,
  responsive bloc trade, staffed workday research and the nuclear/campaign chain.

## Negative results

- Rejected: `SYS-155` abstracts generated urban trips too broadly; `SYS-186`
  claims individual errands rather than citizens finding shifts; `SYS-239`
  dispatches station drones/vessels rather than threshold-configured office fleets;
  `SYS-154` is tax/upkeep settlement, not physical command-economy trade.

## Delta summary

## Нові факти

- Зафіксовано `1.1.1.7`, дві послідовні base-game campaigns, physical customs,
  office dispatch, staffed research та nuclear-fuel campaign route.

## Нові гени

- Додано `ACT-177`–`ACT-178`, `SYS-264`–`SYS-271`, `SYS-273`, `SYS-274`,
  `CON-236`–`CON-244`, `INF-098`–`INF-103` та `OBJ-069`.

## Нові комбінації

- `COMB-0132` фіксує шлях від physical planned economy через staffed logistics
  та research до campaign-completing nuclear-fuel export.

## Зміни таксономії

- Межі наявних генів не змінено; taxonomy-change record не потрібен.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | `ACT-006`, `ACT-023`, `ACT-068`, `ACT-117`, `ACT-120`, `ACT-139`, `ACT-145`, `ACT-148`, `ACT-149`, `ACT-177`, `ACT-178` | lines, offices, construction, trade, research |
| System Behaviour | `SYS-156`, `SYS-157`, `SYS-264`–`SYS-274` | citizens, logistics, economy, utilities, nuclear, campaign |
| Constraint | `CON-062`, `CON-172`, `CON-173`, `CON-184`, `CON-185`, `CON-236`–`CON-244` | access, deliveries, capacity and progression gates |
| Information | `INF-001`, `INF-058`, `INF-059`, `INF-060`, `INF-086`–`INF-103` | live republic and campaign disclosure |
| Objective | `OBJ-069` | finish Campaign 2 after Campaign 1 |
| Time | `TIM-003` | pausable real-time simulation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `133` (`GAME-0001`–`GAME-0133`).
- Exact genome matches: none.
- Tied near matches: `GAME-0133` — Timberborn (`16 / 80 = 0.200000`).
- Supported combination subsets: `COMB-0132`.
- Scan date: 2026-08-21.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0133`.
