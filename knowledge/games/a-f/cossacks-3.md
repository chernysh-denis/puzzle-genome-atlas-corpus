---
game_id: GAME-0209
slug: cossacks-3
game_title: Cossacks 3
analysis_status: reviewed
reviewed: 2026-09-01
combination_ids:
  - COMB-0207
gene_ids:
  action:
    - ACT-121
    - ACT-139
    - ACT-189
    - ACT-316
    - ACT-317
    - ACT-318
    - ACT-380
  system:
    - SYS-051
    - SYS-161
    - SYS-215
    - SYS-297
    - SYS-549
    - SYS-550
    - SYS-551
    - SYS-552
    - SYS-553
    - SYS-554
    - SYS-692
    - SYS-693
    - SYS-694
    - SYS-695
    - SYS-696
  constraint:
    - CON-466
    - CON-467
    - CON-469
    - CON-470
    - CON-551
    - CON-552
  information:
    - INF-224
    - INF-268
  objective:
    - OBJ-130
  time:
    - TIM-003
---

# Game: Cossacks 3

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam Standard/base
  game, public build `3154226`, reviewed 2026-09-01; single-player Tutorial
  campaign `War Ruse`, mission `Peace`, Normal difficulty.
- Primary decision loop: read the current adviser instruction and RTS HUD;
  select peasants and allocate food, wood, stone, coal, iron and gold; place,
  construct and repair buildings; train peasants, pikemen, officers, drummers
  and mercenary bowmen; research the instructed upgrades; form and command the
  regiment; build and operate one ferry; guard capturable economic assets;
  then burn the enemy barracks and complete the Academy/Town Hall instruction.
- Entry and exit: from the main menu choose `Tutorial`, `Peace`, `Normal` and
  `Start Mission`; the first retained controllable frame contains the Swedish
  king and escort before the settlement. The positive terminal follows the
  final Town Hall selection, adviser completion dialogue, mission-complete
  settlement and return to the campaign screen. Abort, restart, fatal force
  loss or unrecovered economic collapse does not satisfy completion; a
  distinct scripted loss screen was not directly verified.
- Included: the authored Peace objective chain; basic selection and movement;
  mill, field, storehouse, mine, houses, barracks, shipyard, Diplomatic Center,
  Academy and Town Hall; finite resource work and food consumption; building
  and unit queues; 36-pikeman regiment with officer and drummer; formation and
  guard orders; scripted blacksmith fire and repair; one ferry crossing with
  peasants and soldiers; founding the second settlement; capture risk for
  unguarded peasants, mills and mines; mercenary hiring, escalating purchase
  price, gold wages and mutiny at zero gold; bowmen igniting and destroying the
  hostile barracks; nearby explosion danger; the final tutorial terminal.
- Excluded: the `War` tutorial; five historical campaigns and every other
  mission; Random Map, multiplayer, ranked play, spectator mode, editor,
  Workshop, mods and cheats; every DLC nation or campaign; exhaustive national
  balance; market trade; walls, towers and naval warfare; artillery, because
  this mission explicitly says time and funds are insufficient and directs
  the player to mercenary bowmen; unrestricted eighteenth-century development;
  achievements and the whole product history.
- Potential scoped modules: `War` as a combat-only tutorial; one historical
  scenario; a seeded Random Map economy; artillery and ammunition; naval
  combat beyond ferry transport; market exchange; multiplayer capture and
  diplomacy; one independently versioned DLC nation.
- Direct-play status: not conducted. Current depot metadata, official product
  text and developer patch notes establish the live build, Tutorial entry,
  mission return behaviour, formation, transport, capture, famine and
  mercenary rules. A maintained textual transcription of the English tutorial
  supplies the exact Peace objective order and adviser terminal. The
  transition trace is rules reasoning, not a claim of authenticated play. No
  video or audio evidence was opened or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `COS3-001` | Steam public build 3154226 is the reviewed current Windows base-game boundary | Confirmed | Direct | High | P1, P2 |
| `COS3-002` | The official Tutorial button opens the tutorial campaign, which contains Peace and War missions | Confirmed | Corroborated | High | P3, S1 |
| `COS3-003` | Peace on Normal begins with movement instruction and advances through an authored settlement objective sequence | Observation | Corroborated | High | S1, S2 |
| `COS3-004` | Peasants gather six resources, construct and repair buildings, while food supports population and starvation can kill units | Observation | Corroborated | High | P1, P4, S1 |
| `COS3-005` | Building-local training and research, housing capacity and a 36-pikeman officer/drummer regiment are mandatory Peace steps | Observation | Corroborated | High | P4, S1 |
| `COS3-006` | The mission requires ferry construction, embarkation, crossing, disembarkation and a second Town Hall | Observation | Corroborated | High | P5, S1 |
| `COS3-007` | Unguarded peasants, mines and mills can be captured, while guards defend them | Observation | Corroborated | High | P4, S1 |
| `COS3-008` | Mercenary bowmen have escalating hire price, consume gold wages and mutiny when gold is exhausted | Observation | Corroborated | High | P4, S1 |
| `COS3-009` | Bowmen replace unavailable artillery, ignite the enemy barracks and expose nearby units to its destruction blast | Observation | Corroborated | High | S1 |
| `COS3-010` | The final Academy/Town Hall instruction produces adviser completion and mission settlement, then campaign return | Observation | Corroborated | High | P6, S1 |

## Basic data

- Release / origin: developed and published by Ukrainian studio GSC Game
  World; released for Windows on 2016-09-20.
- Platform or physical form: Windows real-time strategy; one fixed authored
  single-player tutorial mission is scoped.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  agent routing and coordination; ordered dependency sequencing.
- Primary and reproducible sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/333420/Cossacks_3/),
    for product, developer, release, single-player, resources, cities,
    technologies, armies, nations, buildings, units and Ukrainian support.
  - **[P2]** [current public depot record](https://steamdb.info/app/333420/depots/)
    and [build 3154226 record](https://steamdb.info/patchnotes/3154226/), for
    the current Windows public branch and build date.
  - **[P3]** [official patch 2.0.2.87.5828](https://steamcommunity.com/app/333420/discussions/0/2595630410192992259/),
    for the main-menu Tutorial button and tutorial campaign entry.
  - **[P4]** [official 2.1.5.91.5955 announcement](https://steamcommunity.com/ogg/333420/announcements/detail/1694922348760819247),
    for worker/resource distribution, mine assignment, stand-ground,
    formation-related state, famine, mercenary rebellion and building capture.
  - **[P5]** [official 1.5.6.74.5273 announcement](https://steamcommunity.com/ogg/333420/announcements/detail/1262543810911169694),
    for transport capacity and shipyard/transport behaviour.
  - **[P6]** [official patch 1.2.5.60.4425](https://steamcommunity.com/app/333420/discussions/0/144513248281117502/),
    for story-mission return to the campaign screen, group formations and
    building-local unit queues.
- Secondary sources:
  - **[S1]** [maintained textual English tutorial transcription](https://wikiwiki.jp/cossacks3-j/%E3%83%81%E3%83%A5%E3%83%BC%E3%83%88%E3%83%AA%E3%82%A2%E3%83%AB),
    for every ordered Peace adviser instruction, economic warning, ferry,
    capture, mercenary, fire and final Town Hall line.
  - **[S2]** [Cossacks Portal tutorial index](https://cossacksportal.ru/index.php?game=cossacks-3&mission=tutorial),
    for the two-mission `War Ruse` structure and the Peace/War distinction.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P6`, `S1` and `S2` under the declared build, language, difficulty and
  mission; no audiovisual playback or direct-play claim.
- Claim IDs: `COS3-001`–`COS3-010`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-121`, queue one instructed research upgrade; `ACT-139`,
  place or demolish a settlement building; `ACT-189`, issue a destination,
  attack or guard command; `ACT-316`, queue a unit at its building; `ACT-317`,
  choose formation and stance; `ACT-318`, assign peasants to a resource,
  foundation or repair target.
- New gene: `ACT-380`, load selected peasants or soldiers into the ferry and
  unload them at an eligible opposite shore.
- Parameters: selection, target, map point, building, footprint, worker task,
  queue entry, upgrade, formation, guard target, ferry, shore and passenger set.
- Claim IDs: `COS3-003`–`COS3-009`.

### System Behaviour Genes

- Existing genes: `SYS-051`, let guards acquire nearby attackers; `SYS-161`,
  deplete finite spatial sources; `SYS-215`, resolve commanded real-time
  combat; `SYS-297`, execute pathing and target acquisition; `SYS-549`, gather,
  carry and deposit resources; `SYS-550`, advance construction and repair;
  `SYS-551`, advance building-local unit queues; `SYS-552`, complete
  building-bound research; `SYS-553`, apply completed housing capacity;
  `SYS-554`, resolve formation movement and stance.
- New genes: `SYS-692`, retain passengers inside a ferry through crossing and
  release them at a legal shore; `SYS-693`, transfer control of exposed
  economic targets and let guards prevent that capture; `SYS-694`, debit
  mercenary wages and trigger rebellion at exhausted gold; `SYS-695`, advance
  ignition, fire damage, repair and destruction for a targeted building;
  `SYS-696`, debit the shared food stockpile for population and apply
  starvation deaths after exhaustion.
- Resolution order: accept selection, worker, building, queue, formation,
  transport and combat orders; advance gathering, food and mercenary upkeep;
  advance construction, repair, training and research; update population and
  formations; move ferry and ground groups; resolve capture, guard engagement,
  ordinary combat and building fire; then advance the authored tutorial step
  or settle the final Town Hall completion.
- Claim IDs: `COS3-003`–`COS3-010`.

### Constraint Genes

- Existing genes: `CON-466`, foundations need a legal footprint, resources and
  reachable peasants; `CON-467`, unit and research orders need the right
  completed building, unlock, stockpile and capacity; `CON-469`, resource work
  needs a reachable source and compatible delivery relation; `CON-470`, group
  orders obey terrain, formation space, range and target reachability.
- New genes: `CON-551`, ferry embarkation and disembarkation require an
  eligible shore/ramp, capacity and reachable passenger relation; `CON-552`,
  the instructed infantry regiment requires the declared same-type unit count
  and nearby officer/drummer support before formation.
- Scarce strategic resources: peasant time, six stockpiles, food upkeep, gold
  wages, population capacity, queue time, guard coverage, formation members,
  ferry capacity, shore access, repair time and distance to the barracks.
- Claim IDs: `COS3-004`–`COS3-009`.

### Information Genes

- Existing gene: `INF-224`, expose resources, population, selection, health,
  commands and active queues in the RTS command view.
- New gene: `INF-268`, expose the current Peace adviser instruction, its legal
  action explanation and completion transition without revealing every later
  objective in advance.
- Claim IDs: `COS3-003`–`COS3-010`.

### Objective Genes

- New gene: `OBJ-130`, complete the ordered `War Ruse — Peace` teaching route
  and return to the campaign screen.
- Success, evaluation and failure: an economy, regiment, ferry crossing or
  burning barracks is only an intermediate state. Success requires the final
  Town Hall interaction and settled mission completion. Abort, restart, fatal
  force loss or unrecovered famine/economic collapse is non-positive and does
  not satisfy the route; no separate scripted loss-screen claim is made.
- Claim IDs: `COS3-003`–`COS3-010`.

### Time Genes

- Existing gene: `TIM-003`, workers, stockpile consumption, wages, queues,
  fires, movement and combat progress while the player continues issuing RTS
  orders.
- Claim IDs: `COS3-004`–`COS3-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Public build 3154226 is at the main menu | Choose Tutorial, Peace, Normal and Start Mission | `War Ruse — Peace` loads at the Swedish king and movement instruction | Version, mode, difficulty and authored entry are bounded | `COS3-001`–`COS3-003` |
| The settlement can feed and employ peasants | Assign workers, place the mill/field, storehouse and mine | Peasants travel and gather into six stockpiles while the objective advances after required work | Economy is selected spatial labour, not passive income | `COS3-004` |
| Food is consumed while new workers and soldiers are trained | Let the food stockpile reach zero | Famine advances and units die until food production recovers | Population creates continuing upkeep pressure | `COS3-004` |
| A barracks, resources, housing and queue room are available | Queue 36 pikemen plus an officer and drummer | Each building queue advances and population capacity admits completed units | Stockpile, site and housing jointly gate army production | `COS3-005` |
| Required infantry and leaders stand together | Select them and create the instructed regiment/formation | The group gains ordered slots and formation movement/stance | Formation is a composition-dependent commitment | `COS3-005` |
| The scripted blacksmith catches fire | Assign peasants to repair it | Worker time restores the building while fire damage continues | Repair competes with economic work under live damage | `COS3-004`, `COS3-009` |
| A ferry and passengers reach the first shore | Load soldiers and peasants, cross and unload | Units leave ground control, travel inside the vessel and reappear at a legal opposite shore | Transport changes containment and topology | `COS3-006` |
| The transported peasants can reach the instructed site | Place and construct the second Town Hall | A new settlement anchor completes and the hostile/capture lesson begins | Building is an authored dependency, not the terminal | `COS3-006`, `COS3-007` |
| A mill, mine or peasant is left without soldiers nearby | Allow an enemy unit to reach it, then assign guards | Exposed eligible ownership can transfer; guards automatically engage future captors | Guard placement protects economic control | `COS3-007` |
| A Diplomatic Center and gold are available | Hire mercenary bowmen and continue paying them | Hire price rises, wages drain gold and zero gold can turn the mercenaries hostile | Mercenary force strength creates a recurring loyalty liability | `COS3-008` |
| Bowmen are in range of the enemy barracks | Order the attack while keeping friendlies clear | Fire damages the structure until destruction; its blast threatens nearby units | Building destruction has delayed spatial risk | `COS3-009` |
| Academy and final instructed settlement state are complete | Select the required Town Hall | Adviser completion dialogue runs, success settles and control returns to the campaign screen | The reproducible terminal is later than the barracks destruction | `COS3-010` |

## Strategic and experiential structure

- Local decision: move the next peasant to a needed stockpile, place a building
  near work, maintain housing, choose a queue, repair the fire, assemble the
  regiment, position guards, fit ferry passengers or keep troops outside the
  barracks blast.
- Medium-term planning: preserve food while creating 36 pikemen and leaders;
  reserve wood and stone for the ferry and second settlement; maintain enough
  gold to keep hired bowmen loyal; replace economic labour diverted to repair,
  construction, transport and guard duty.
- Long-term structure: turn the escorted king into a functioning economy,
  formal regiment and transported colony, then defend ownership, purchase one
  ranged breach force and satisfy every authored teaching dependency before
  the Town Hall terminal.
- Common heuristics: keep food positive; construct houses before the queue
  blocks; avoid long worker routes; form exactly the taught regiment; unload
  peasants with an escort; guard capturable assets; do not overhire mercenaries;
  attack the barracks from range and clear the destruction radius.
- Failure attribution: adviser text, resource and population totals, disabled
  command buttons, queue progress, formation availability, capture ownership,
  gold drain, burning buildings and the final dialogue make most failures
  legible; exact pathing and hostile timing retain live uncertainty.
- Player-trust factors: ordered explicit instructions, visible stockpiles,
  stable building costs and requirements, inspectable queues, visible fire and
  ownership, and a separate completion transition.
- Claim IDs: `COS3-003`–`COS3-010`.

## Replay and variation

- What changes between sessions: peasant allocation, building positions,
  queue timing, formation route, ferry manifest, guard coverage, hostile
  contact and the amount of gold left when mercenaries are hired.
- Randomness or procedural generation: the mission's authored objective order
  is fixed; path selection and live combat timing can diverge after different
  player orders. No seeded-map claim is made.
- Multiple viable strategies: labour and build timing can vary inside each
  objective; different guards and crossing groups can protect the settlement;
  bowmen can approach the barracks from different safe ranges, but the authored
  teaching order and terminal remain fixed.
- Typical replay motive: complete instructions with less idle time, avoid
  famine and capture, preserve mercenary gold, reduce ferry trips and keep the
  regiment outside the barracks explosion.
- Claim IDs: `COS3-003`–`COS3-010`.

## Adjacent systems and history

- Direct predecessors: Cossacks: European Wars and Back to War establish the
  series economy and mass-army lineage; their historical values are not
  imported into this current Cossacks 3 build.
- Variants: `War` removes the economy lesson; campaigns replace tutorial steps
  with historical objectives; Random Map exposes configurable nations and
  starts; multiplayer adds human diplomacy and capture pressure; DLC adds
  separately versioned nations and missions.
- Similar games: Age of Empires II: Definitive Edition shares selected
  villagers, finite resources, construction, housing, local queues, research,
  formations and live combat. Hearts of Iron IV shares concurrent economy and
  military dependencies but operates through national production and fronts.
- Important differences: the bounded Peace tutorial demands a composition-
  checked 36-pikeman regiment, one ferry-borne colony, capturable economic
  ownership, mercenary wage rebellion, repairable fire, deliberate building
  ignition and an authored teaching terminal instead of open Conquest.
- Claim IDs: `COS3-003`–`COS3-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-121`, `ACT-139`, `ACT-189`, `ACT-316`–`ACT-318`, `ACT-380` | worker, queue, formation, guard and ferry orders |
| System Behaviour | `SYS-051`, `SYS-161`, `SYS-215`, `SYS-297`, `SYS-549`–`SYS-554`, `SYS-692`–`SYS-696` | economy, queues, transport, capture, wages, fire and famine |
| Constraint | `CON-466`, `CON-467`, `CON-469`, `CON-470`, `CON-551`, `CON-552` | foundation, queue, resource, group, shore and regiment legality |
| Information | `INF-224`, `INF-268` | RTS HUD and current tutorial instruction |
| Objective | `OBJ-130` | complete Peace and return to campaign |
| Time | `TIM-003` | continuously advancing settlement and conflict |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `208` (`GAME-0001`–`GAME-0208`).
- Exact genome matches: none.
- Tied near matches: `GAME-0179` — Age of Empires II: Definitive Edition (`21 / 40 = 0.525000`).
- Supported combination subsets: `COMB-0207`.
- Scan date: 2026-09-01.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0179` — Age of Empires II: Definitive Edition | `ACT-121`, `ACT-139`, `ACT-189`, `ACT-316`–`ACT-318`, `SYS-161`, `SYS-215`, `SYS-297`, `SYS-549`–`SYS-554`, `CON-466`, `CON-467`, `CON-469`, `CON-470`, `INF-224`, `TIM-003` | Both bind selected villagers, finite resources, buildings, population, local queues, research, formations and combat to one live economy. Cossacks 3 replaces a seeded four-Age Conquest match, fog and civilization-wide elimination with an authored tutorial sequence, food famine, ferry containment, economic capture, mercenary wage rebellion, burning-building resolution and a final Town Hall teaching terminal | Near, `0.525000` |

### Preserved research notes

- New genes: `ACT-380`, `SYS-692`–`SYS-696`, `CON-551`, `CON-552`,
  `INF-268` and `OBJ-130`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: the reusable RTS economy and command vocabulary is
  retained, while ferry containment, guardable capture, mercenary rebellion,
  building fire, global famine and the objective-driven terminal require
  narrower boundaries than the open Conquest neighbour.

## Combination assessment

- `COMB-0207` is a strict twenty-one-gene subset joining worker assignment,
  construction, production, formation, ferry transport, economic capture,
  mercenary wages, burning-building resolution, current tutorial instructions
  and the final Peace completion.
- Existing verified combinations are scanned for exact and proper-subset
  relationships by repository validation; no earlier subset is supported.

## Taxonomy impact

- Registry changes: ten new Active genes, evidence-preserving Cossacks 3
  examples on twenty-two reused genes, `COMB-0207` and memberships in
  `FAM-009`, `FAM-010`, `FAM-015` and `FAM-017`.
- Taxonomy-change record: none; no existing lifecycle, causal boundary or
  reviewed game signature changes.
- Candidate terms affected: exact cost, rate, unit count beyond the taught
  36-pikeman packet, formation geometry, ferry capacity, capture radius,
  mercenary price curve, wage interval, fire rate and adviser wording remain
  parameters. Artillery remains an excluded future module.

## Negative results

- No separate negative-result record. The review rejected the `War` tutorial
  because it omits the selected settlement loop, rejected Random Map because it
  lacks the fixed authored terminal, rejected artillery because Peace explicitly
  withholds it, and rejected barracks destruction as the final terminal because
  the Academy/Town Hall instruction and mission settlement still remain.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Current public build `3154226` retains the
  official Tutorial entry and mission-return boundary (`COS3-001`, `COS3-002`,
  `COS3-010`).
- [Observation | Corroborated | High] Peace joins a settlement economy,
  regiment, ferry colony, capture lesson, mercenary liability, building fire
  and final Town Hall completion in one authored route (`COS3-003`–`COS3-010`).

## Нові гени

- [Observation | Corroborated | High] Ten new records isolate ferry loading,
  transported containment, economic capture, mercenary rebellion, building
  fire, global famine, ferry shore legality, composition-checked formation,
  current tutorial instruction and the retained Peace terminal.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0207` joins the settlement-to-
  ferry-to-mercenary-breach teaching chain.

## Зміни таксономії

- [Observation | Direct | High] Змін таксономії немає.

## Family classification

- `FAM-009` — Tactical forecast and counterplay: formation, guard coverage,
  ferry landing and barracks-blast distance trade immediate progress against
  hostile responses.
- `FAM-010` — Real-time system pressure: workers, queues, food, wages, fire,
  movement and combat advance together.
- `FAM-015` — Agent routing and coordination: selected peasants, regiment,
  guards and ferry passengers require spatial task assignment.
- `FAM-017` — Ordered dependency sequencing: every teaching objective exposes
  the next legal economy, regiment, transport, capture and breach dependency.
- No new family is created from one game.

## Plain-language interpretation

`War Ruse — Peace` is not a free skirmish. The adviser reveals one practical
task at a time: feed the settlement, place storage and mines, train exactly the
required pikemen and leaders, organise them as a regiment, create housing and
repair a fire. Workers are always doing something in the live economy, so a
builder or repairer is temporarily not gathering while food and other
stockpiles continue changing.

The second half teaches three risks absent from a simple build order. A ferry
must carry peasants and troops across the river before a new Town Hall can be
founded. Economic assets without guards can change owner. Mercenary bowmen
solve the ranged breach after artillery is explicitly refused, but they keep
draining gold and may rebel at zero. Burning the barracks is still not the
terminal: the final Academy/Town Hall instruction must settle before the game
returns to the campaign screen.

## Нові питання

- Would a separately bounded current Random Map reproduce capture, famine and
  mercenary rebellion without the tutorial's authored ordering?
- Does a current direct-play trace expose a distinct scripted defeat screen for
  Peace, or only abort/restart and emergent unrecoverable failure?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] `GAME-0210` DayZ.
- Optimisation criterion: contrast authored RTS instruction and retained
  mission completion with an official-server fresh-spawn survival lifecycle
  whose irreversible death is the negative terminal.
- Expected information gain: persistent online world, embodied needs, social
  uncertainty, inventory exposure and character death.
- Backlog impact: proceeds to the third game in the recorded Batch 009 order;
  reserve use still requires the selection's high-risk evidence gate.

## Чому саме вона

- [Hypothesis | Limited | High] DayZ should share live pressure and spatial
  resource decisions while replacing selected-agent settlement construction
  with one vulnerable avatar in a persistent multiplayer world.
