---
game_id: GAME-0179
slug: age-of-empires-ii-definitive-edition
game_title: Age of Empires II: Definitive Edition
analysis_status: reviewed
reviewed: 2026-08-28
combination_ids:
  - COMB-0177
gene_ids:
  action:
    - ACT-121
    - ACT-139
    - ACT-189
    - ACT-316
    - ACT-317
    - ACT-318
  system:
    - SYS-004
    - SYS-161
    - SYS-215
    - SYS-297
    - SYS-305
    - SYS-549
    - SYS-550
    - SYS-551
    - SYS-552
    - SYS-553
    - SYS-554
    - SYS-555
  constraint:
    - CON-273
    - CON-466
    - CON-467
    - CON-468
    - CON-469
    - CON-470
  information:
    - INF-059
    - INF-224
    - INF-225
  objective:
    - OBJ-103
  time:
    - TIM-003
---

# Game: Age of Empires II: Definitive Edition

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: official PC build `177723`, the current live build found
  on 2026-08-28; vanilla single-player Skirmish, `Random Map`, Tiny `Arabia`,
  fixed seed `20260828179`, player Britons (Blue) against one Standard AI Franks
  opponent (Red), Dark Age start, Standard resources, population limit 200,
  Normal speed, Normal map reveal and Conquest as the only victory condition.
- Primary decision loop: read the map, economy, population, Age, selection and
  queues; assign villagers to food, wood, gold, stone, construction or repair;
  place buildings; queue villagers, military and research; scout through fog;
  command and form armies; then adapt while every worker, queue, opponent and
  battle continues resolving in real time.
- Entry and exit: begins at the first controllable Dark Age frame with one Town
  Center, three villagers and one Scout Cavalry; succeeds when the Franks resign
  or lose the civilization-wide unit and production-building set required by
  Conquest, and fails this route if the Britons suffer the symmetric terminal
  first.
- Included: seeded generated terrain and finite food, wood, gold and stone;
  villager carrying and drop-off; construction and repair; Town Center and
  military-building queues; Houses and the 200-population cap; Feudal, Castle
  and Imperial Age research with building prerequisites; Briton archery-range
  units and Longbowmen, ordinary infantry, cavalry and siege support; formation,
  stance, pathing, range and minimum range; explored terrain, live fog and the
  minimap; one Imperial Age trebuchet siege against the final Frank economy and
  production base; defeat, resignation and Conquest settlement.
- Excluded: campaigns, scenarios, co-op, multiplayer, ranked ladder, spectator
  mode and lobby diplomacy; every DLC civilization or DLC-only mechanic; treaty,
  Regicide, Empire Wars, Death Match, Battle Royale and other starts/modes;
  Wonder, Relic, Score and time-limit victory; cheats, turbo, full-tech-tree,
  mods, custom data sets, map editor, save editing and exhaustive civilization
  balance comparison.
- Potential scoped modules: a ranked team match; naval maps and transport;
  trade and allied markets; monk conversion and relic victory; Castle siege
  without Imperial Age; one campaign scenario; one independently versioned DLC.
- Direct-play status: not conducted. Official current-build, game-mode,
  Random Map, starting, economy, Age, military and Conquest documentation
  establishes the bounded transition model; the seed is a reproducibility
  control for a future execution, not a claim that the exact generated map was
  captured in direct play.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `AOE2-001` | Build 177723 is the reviewed live PC rules boundary | Confirmed | Direct | High | P1, P2 |
| `AOE2-002` | A solo Random Map Skirmish can bind civilizations, map, size, AI difficulty, resources, population, speed, reveal and victory settings | Confirmed | Direct | High | P3, P4 |
| `AOE2-003` | A declared Random Map seed can recreate the generated map under the same settings and build | Confirmed | Direct | High | P3 |
| `AOE2-004` | Villagers gather four finite resources, carry them to compatible drop-offs and construct the economy in real time | Confirmed | Direct | High | P5, P6 |
| `AOE2-005` | Completed buildings own paid unit and research queues, while constructed housing gates live unit release | Confirmed | Direct | High | P5–P7 |
| `AOE2-006` | Feudal, Castle and Imperial advancement consumes resources and requires the declared current-Age buildings | Confirmed | Direct | High | P7 |
| `AOE2-007` | Allied units and buildings reveal current space while explored terrain persists beneath ordinary fog of war | Confirmed | Direct | High | P4, P6 |
| `AOE2-008` | Selected military groups path, arrange by formation and stance, acquire legal targets and exchange range-, cadence- and armour-dependent attacks in real time | Observation | Corroborated | High | P4, P8 |
| `AOE2-009` | Unit types counter one another and siege units provide specialised building attack, including the scoped trebuchet | Confirmed | Direct | High | P8 |
| `AOE2-010` | Conquest ends when opposing civilizations resign or lose their recoverable civilization-wide military/economic production set | Confirmed | Direct | High | P4, P9 |
| `AOE2-011` | The scoped route can progress from the initial Dark Age economy through all four Ages to Briton ranged pressure and Imperial siege | Observation | Corroborated | High | P4–P9, V1 |

## Basic data

- Release / origin: developed by Forgotten Empires, Tantalus Media and Wicked
  Witch, published by Xbox Game Studios; Definitive Edition released 2019.
- Platform or physical form: real-time strategy on PC; one fixed solo Skirmish
  is scoped.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  agent routing and coordination; ordered dependency sequencing.
- Primary and reproducible sources:
  - **[P1]** [official Update 177723](https://www.ageofempires.com/news/age-of-empires-ii-definitive-edition-update-177723/),
    for the reviewed live build and its verification string.
  - **[P2]** [official Steam product page](https://store.steampowered.com/app/813780/Age_of_Empires_II_Definitive_Edition/),
    for the PC product and single-player boundary.
  - **[P3]** [official Random Map generation guide](https://support.ageofempires.com/hc/en-us/articles/11393047456020-Using-Random-Map-Generation),
    for deterministic seed entry and map reproduction.
  - **[P4]** [official civilizations and game-modes guide](https://www.ageofempires.com/learn-to-play/civilizations-game-modes-aoe2/),
    for solo Skirmish, Random Map, civilization, map and difficulty selection.
  - **[P5]** [official control and resources guide](https://www.ageofempires.com/learn-to-play/control-resources-aoe2/),
    for four resources, villagers, collection, drop-off and the live HUD.
  - **[P6]** [official expanding guide](https://www.ageofempires.com/learn-to-play/expanding-your-empire-aoe2/),
    for scouting, fog, houses, buildings, villagers and the opening loop.
  - **[P7]** [official advancing guide](https://www.ageofempires.com/learn-to-play/advancing-aoe2/),
    for four Ages, research costs and current-Age building prerequisites.
  - **[P8]** [official military and economy guide](https://www.ageofempires.com/learn-to-play/military-and-economy-aoe2/),
    for production buildings, counters, range, minimum range and siege.
  - **[P9]** [official ending-a-match guide](https://www.ageofempires.com/learn-to-play/ending-a-match-aoe2/),
    for Conquest defeat and resignation.
  - **[P10]** [official multiplayer setup reference](https://support.ageofempires.com/hc/en-us/articles/360047306372-How-do-I-create-a-multiplayer-match-in-Age-of-Empires-II-Definitive-Edition),
    used only to confirm exposed match settings also fixed in this solo scope.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P10` under the declared build, setup and seed; rules reasoning, not a
  claim of direct play.
- Claim IDs: `AOE2-001`–`AOE2-011`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-121`, queue a reachable technology or Age research;
  `ACT-139`, place or demolish an ordinary building; `ACT-189`, issue a move,
  attack, attack-move, stop or hold-position command.
- New genes: `ACT-316`, append a unit to an eligible building-local queue;
  `ACT-317`, set formation and stance for a selected group; `ACT-318`, task
  selected villagers to a resource, foundation or repair target.
- Parameters: selection, target, map point, building, footprint, unit, research,
  queue position, villager task, formation, stance and command modifier.
- Claim IDs: `AOE2-004`–`AOE2-009`.

### System Behaviour Genes

- Existing genes: `SYS-004`, sample the seeded Random Map; `SYS-161`, deplete a
  finite spatial source; `SYS-215`, resolve directly commanded real-time combat;
  `SYS-297`, execute ordered pathing and target acquisition; `SYS-305`, update
  current allied vision and fog.
- New genes: `SYS-549`, loop villager extraction, carrying and deposit;
  `SYS-550`, advance villager construction and repair; `SYS-551`, advance each
  building-local unit queue; `SYS-552`, complete building-bound technology and
  Age research; `SYS-553`, apply built housing capacity; `SYS-554`, resolve
  formation movement and stance; `SYS-555`, settle Conquest or resignation.
- Resolution order: accept economic, building, queue and military commands;
  advance worker travel and gathering; advance construction, training and
  research timers; update population and unlocks; execute group movement and
  combat; update current vision; then settle a Conquest terminal if either
  civilization can no longer recover or resigns.
- Claim IDs: `AOE2-003`–`AOE2-011`.

### Constraint Genes

- Existing gene: `CON-273`, current hostile position and direct targeting are
  gated by allied vision under fog.
- New genes: `CON-466`, building work needs legal placement, resources and a
  reachable assigned villager; `CON-467`, unit and research orders need the
  right completed building, unlocks, stockpile and capacity; `CON-468`, the next
  Age needs resources and current-Age buildings; `CON-469`, gathering needs a
  reachable source and compatible drop-off; `CON-470`, group orders obey
  terrain, formation space, vision, range and minimum range.
- Scarce strategic resources: villager time, food, wood, gold, stone, housing,
  production-building time, map vision, army position, reinforcement distance
  and the opponent's continuing capacity to raid or rebuild.
- Claim IDs: `AOE2-004`–`AOE2-010`.

### Information Genes

- Existing gene: `INF-059`, expose reachable unit, building, technology and Age
  dependencies before commitment.
- New genes: `INF-224`, expose resources, population, Age, selections, health,
  commands and queues in the RTS HUD; `INF-225`, preserve explored terrain while
  hiding current hostile occupancy outside allied vision.
- Claim IDs: `AOE2-004`–`AOE2-009`.

### Objective Genes

- New gene: `OBJ-103`, defeat the sole opposing civilization under Conquest.
- Success, evaluation and failure: a won battle is insufficient while the Frank
  economy and production network can recover; the route succeeds only at the
  Conquest result and fails if Briton civilization-wide capacity is eliminated
  or the player resigns first.
- Claim IDs: `AOE2-010`, `AOE2-011`.

### Time Genes

- Existing gene: `TIM-003`, workers, queues, scouting, the opponent, movement
  and combat progress in real time while the player continues issuing orders.
- Claim IDs: `AOE2-004`–`AOE2-011`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Declared build and seeded Tiny Arabia settings are loaded | Start the Skirmish | The seed generates the same map input under the same build and setup | Map variation is bounded before play | `AOE2-001`–`AOE2-003` |
| Dark Age Town Center, three villagers and Scout are controllable | Assign villagers to sheep/wood and queue a Villager | Workers path, gather and return yields while the Town Center advances its paid queue | Economy and unit production are concurrent live processes | `AOE2-004`, `AOE2-005` |
| A villager reaches a legal House footprint and Wood is available | Place the House and assign construction | Resources are committed, work advances and completion raises population capacity | Spatial building work unlocks later production | `AOE2-005` |
| Scout crosses unrevealed Arabia terrain | Issue a destination command | Traversed terrain becomes explored; only current allied vision discloses mobile hostile state | Remembered map and live fog are distinct | `AOE2-007` |
| Food threshold and two completed Dark Age buildings are available | Queue Feudal Age at the Town Center | Paid building-local research advances, then persistently changes Age and unlocks | Economy plus spatial prerequisites gate era order | `AOE2-006` |
| Feudal Age and an Archery Range are complete | Queue archers and economic/military technologies | Each eligible building advances its own finite paid queue while housing and stockpile remain legal | Concurrent sites share economy and capacity | `AOE2-005`, `AOE2-006` |
| Castle Age, a Castle and sufficient resources are available | Queue Longbowmen and set the ranged group to line/stand-ground | Units train into population headroom; the selected group preserves declared topology and acquisition policy | Composition and formation are explicit decisions | `AOE2-005`, `AOE2-008` |
| A visible Frank force enters range | Attack-move the formed Briton group with support | Pathing, formation, counters, range, cadence, armour and defeat resolve continuously | Tactical contact couples geometry to composition | `AOE2-008`, `AOE2-009` |
| Imperial Age and a Castle are available | Train a trebuchet, deploy it in protected range and attack production buildings | Siege damage removes structures while escort units respond to hostile counterplay | Specialised siege converts map control into base removal | `AOE2-009` |
| Frank villagers, military and Conquest-relevant production are no longer recoverable, or AI resigns | Continue legal attacks until terminal evaluation | The match reports Briton victory; symmetric Briton elimination reports defeat | The route ends at civilization-wide Conquest, not one kill | `AOE2-010`, `AOE2-011` |

## Strategic and experiential structure

- Local decision: assign the next villager, add a House before a population
  block, choose a queue, scout through fog, place production safely, form an
  army, focus a counter unit or reposition vulnerable siege.
- Medium-term planning: balance food for villagers/Ages, wood for farms and
  buildings, gold for ranged units and research, and stone for a Castle; keep
  several queues productive without consuming the stockpile required for the
  next Age.
- Long-term structure: convert a tiny Dark Age labour base into a four-resource
  economy, unlock each Age through constructed prerequisites, establish ranged
  map control and add protected Imperial siege before the opponent rebuilds.
- Common heuristics: avoid Town Center idle time; build housing ahead of demand;
  scout resource and enemy positions early; preserve ranged distance; screen
  siege; raid exposed workers; replace exhausted sources and forward drop-offs;
  attack production and villagers rather than treating one won fight as victory.
- Failure attribution: grey queue items, resource and population totals,
  foundation preview, Age requirements, formation icons, range feedback, fog,
  health bars and the final result make most failures legible; AI choices and
  unseen army movement preserve adversarial uncertainty.
- Player-trust factors: disclosed costs and prerequisites, stable seeded terrain,
  persistent explored geography, deterministic unit statistics, visible queue
  progress and symmetric Conquest evaluation.
- Claim IDs: `AOE2-002`–`AOE2-011`.

## Replay and variation

- What changes between sessions: seed and generated resource positions, chosen
  civilizations, AI behaviour, scouting information, build order, army mix,
  formation, attack timing and the opponent's resignation point.
- Randomness or procedural generation: the declared seed controls the Random Map
  input; combat and AI decisions still create divergent live trajectories after
  player choices differ.
- Multiple viable strategies: Britons may prioritise Feudal archers, Castle Age
  Longbowmen, economy, defensive Castles, raiding or a later Imperial siege;
  Franks can be pressured economically or defeated through army and production
  attrition.
- Typical replay motive: improve build timing and villager distribution, scout
  faster, reduce idle queues, counter a different army, test another seed or
  compare a separately scoped civilization.
- Claim IDs: `AOE2-002`–`AOE2-011`.

## Adjacent systems and history

- Direct predecessors: Age of Empires II and its HD edition establish lineage;
  no historical balance values are imported into this current-build record.
- Variants: campaigns author scripted objectives; multiplayer replaces Standard
  AI with human adversarial inference; naval maps add water control and transport;
  alternative victories change the terminal predicate.
- Similar games: Sid Meier's Civilization VI shares seeded maps, research,
  construction, fog, tactical counters and era progression; Dota 2 shares
  commanded real-time pathing, formation-adjacent group movement, combat and
  vision; Against the Storm shares workers, buildings and production chains.
- Important differences: AoE II makes selected villagers physically gather and
  build, gives each world building its own live queue, constructs population
  capacity, resolves all economies and armies simultaneously, and evaluates
  Conquest across a recoverable civilization rather than one avatar or city.
- Claim IDs: `AOE2-004`–`AOE2-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-121`, `ACT-139`, `ACT-189`, `ACT-316`–`ACT-318` | research, building, unit queue, worker and group orders |
| System Behaviour | `SYS-004`, `SYS-161`, `SYS-215`, `SYS-297`, `SYS-305`, `SYS-549`–`SYS-555` | seeded map, economy, queues, Ages, housing, formations, combat and Conquest |
| Constraint | `CON-273`, `CON-466`–`CON-470` | fog, foundation, queue, Age, drop-off and group legality |
| Information | `INF-059`, `INF-224`, `INF-225` | dependencies, RTS HUD and remembered terrain |
| Objective | `OBJ-103` | Conquest over the sole opponent |
| Time | `TIM-003` | continuously advancing economy and war |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `178` (`GAME-0001`–`GAME-0178`).
- Exact genome matches: none.
- Tied near matches: `GAME-0138` — Dota 2 (`6 / 58 = 0.103448`).
- Supported combination subsets: `COMB-0177`.
- Scan date: 2026-08-28.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0138` — Dota 2 | `ACT-189`, `SYS-215`, `SYS-297`, `SYS-305`, `CON-273`, `TIM-003` | Both accept live destination/attack orders, execute unit pathing and attacks, and gate current hostile state through allied vision. AoE II replaces one persistent hero, item/ability progression, lanes and Ancient destruction with selected villagers, spatial resource deposits, constructed housing, many independent production/research queues, four ordered Ages, explicit group formation and civilization-wide Conquest | Near, `0.103448` |

### Preserved research notes

- New genes: `ACT-316`–`ACT-318`, `SYS-549`–`SYS-555`, `CON-466`–`CON-470`,
  `INF-224`, `INF-225` and `OBJ-103`.
- Classification result: `New gene` and new verified interaction combination.
- Evidence and reasoning: eleven established seeded-map, research, placement,
  command, combat, depletion, pathing, vision, fog, dependency and real-time
  boundaries fit unchanged; eighteen new records isolate live RTS labour,
  queues, housing, Ages, formation and civilization-wide Conquest.

## Combination status

- `COMB-0177` is a verified strict 25-gene subset coupling spatial worker
  economy and constructed production capacity to four-Age ranged and siege
  Conquest.
- Earlier verified combinations are tested deterministically after registration.

## Taxonomy impact

- Registry changes: eighteen new Active genes, links on eleven reused genes,
  `COMB-0177` and four existing family memberships.
- Taxonomy-change record: none; no prior lifecycle, definition or signature
  changes.
- Candidate terms affected: selected RTS labour, worker deposit loop,
  building-local queue, constructed housing, building-gated Age, group formation,
  remembered fog terrain and recoverable-civilization Conquest.

## Negative results

- Civilization VI city production and era systems are not reused for live AoE II
  building queues: one turn-settled city target is not a finite queue attached
  to each constructed production building.
- Factorio automation genes are not reused for villager gathering: the selected
  mobile worker carries finite yields to an eligible world drop-off instead of
  feeding a persistent logistics network.
- Football Manager 26 formation and role genes are not reused: those configure
  an abstract team plan before simulated phases, while AoE II applies formation
  topology to a directly selected moving combat group.
- Dota 2 objective genes are not reused: destroying one Ancient is a fixed-target
  terminal, whereas Conquest tests a civilization's surviving ability to recover.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Build 177723 supports a bounded seeded solo
  Random Map route from the initial Dark Age economy through Feudal, Castle and
  Imperial production to civilization-wide Conquest (`AOE2-001`–`AOE2-011`).

## Нові гени

- [Observation | Corroborated | High] Added eighteen genes for selected live RTS
  labour, finite worker deposit, villager construction, building-local queues,
  constructed housing, Age gates, formation movement, RTS state display,
  remembered fog terrain and Conquest settlement.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0177` isolates the worker-economy-
  to-four-Age-siege chain as a strict 25-gene subset.

## Зміни таксономії

- [Observation | Corroborated | High] No taxonomy migration; eleven generic
  genes and four existing families are reused unchanged.

## Нові питання

- Which later real-time strategy reuses constructed capacity and building-local
  queues while replacing villager return trips or Age prerequisites?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0180` — Microsoft Flight Simulator 2024.
- Optimisation criterion: finish the recorded demand-led Goal in exact order.
- Expected information gain: contrast many-agent territorial production with a
  single high-fidelity aircraft, procedural world, checklists and live systems.
- Backlog impact: ninth and final authorised game unit.

## Чому саме вона

- [Confirmed | Direct | High] It is the next immutable subject in
  `SEARCH_DEMAND_GAME_SELECTION_005` after the reviewed AoE II unit.

## Confidence and open questions

- High confidence: current build, seed support, setup dimensions, four resources,
  building and Age loop, fog, counters, siege and Conquest boundary.
- Medium confidence: exact Standard AI response and resignation timing for the
  declared seed; those are deliberately treated as live variation rather than a
  fixed walkthrough.
- Open questions: none blocking this bounded rules analysis. Exact hidden AI
  utility weights and complete balance tables remain outside scope.

## Reproducibility notes

1. Verify that the title screen reports build `177723`; use the unmodded base
   PC product and disable cheats, turbo and full-tech-tree.
2. Create a solo Skirmish Random Map with Tiny Arabia, seed `20260828179`,
   Britons/Blue against Standard AI Franks/Red, Dark Age, Standard resources,
   population 200, Normal speed/reveal and Conquest only.
3. From the first Dark Age frame, record villager tasks, resource deposits,
   House capacity and independent building queues; scout under normal fog.
4. Satisfy the declared building/resource gates for Feudal, Castle and Imperial
   Ages; field a Briton ranged group, set its formation/stance and preserve it
   through at least one counter interaction.
5. Train and deploy an Imperial trebuchet with an escort, remove the remaining
   Frank recovery network and stop only at the Conquest victory/result screen.

## Review record

- Research status: `reviewed`.
- Reviewed: 2026-08-28.
- Scope changes during review: narrowed from the full evolving product to one
  fixed-build, seeded solo Arabia Conquest route using base-content civilizations.
- Evidence changes during review: current build, settings and core loop are
  official-source anchored; group formation detail and the future exact seeded
  trace remain explicitly corroborated rather than direct-play evidence.
- Gene changes during review: reused eleven established generic boundaries and
  added eighteen for selected labour, queues, housing, Age progression,
  formations, RTS information and Conquest.

## Localisation status

- Ukrainian game, all new-gene and combination entries are reviewed in this unit.
- Canonical names remain `Age of Empires II: Definitive Edition`, `Britons`,
  `Franks`, `Random Map`, `Conquest` and `Longbowman`; surrounding explanation
  is reviewed Ukrainian rather than raw English.

## Source notes

- Official pages were checked on 2026-08-28. Update 177723 owns the current
  build boundary; the setup support page is not used to imply multiplayer scope.
- The declared seed improves repeatability but does not freeze AI decisions or
  import an unobserved direct-play trace.

## Next recommended action

- Integrate `GAME-0180` — Microsoft Flight Simulator 2024 after the required
  thirty-second stop window.
