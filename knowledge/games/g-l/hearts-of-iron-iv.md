---
game_id: GAME-0182
slug: hearts-of-iron-iv
game_title: Hearts of Iron IV
analysis_status: reviewed
reviewed: 2026-08-29
combination_ids:
  - COMB-0180
gene_ids:
  action:
    - ACT-006
    - ACT-121
    - ACT-189
    - ACT-324
    - ACT-325
    - ACT-326
    - ACT-327
    - ACT-328
    - ACT-329
  system:
    - SYS-297
    - SYS-305
    - SYS-563
    - SYS-564
    - SYS-565
    - SYS-566
    - SYS-567
    - SYS-568
    - SYS-569
    - SYS-570
    - SYS-571
  constraint:
    - CON-273
    - CON-477
    - CON-478
    - CON-479
    - CON-480
    - CON-481
    - CON-482
    - CON-483
    - CON-484
  information:
    - INF-059
    - INF-229
    - INF-230
    - INF-231
    - INF-232
    - INF-233
    - INF-234
  objective:
    - OBJ-106
  time:
    - TIM-003
---

# Game: Hearts of Iron IV

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: Windows PC stable public patch `1.19.2`, Steam public build
  `23969257`, reviewed 2026-08-29; English single-player official Tutorial as
  Italy from 1 January 1936, Regular tutorial settings, Ironman off, no mods and
  every separately selectable DLC disabled. The concurrently offered public
  open beta is not this ruleset.
- Primary decision loop: inspect national, map, industry, logistics, army and
  air state; choose a National Focus and research; allocate civilian factories
  to construction and military factories to equipment; organise divisions
  under commanders; draw and execute fronts; assign air support; advance or
  pause time; then revise production, supply and orders as the Ethiopian war
  changes.
- Entry and exit: begins at the first paused controllable tutorial frame with
  Italy already at war with Ethiopia. It ends when Ethiopia capitulates and the
  war's terminal settlement is resolved; the broader save may continue, but
  post-war play is outside this packet.
- Included: the tutorial's existing Italian and Ethiopian positions; national
  focus and research slots; civilian construction; military production lines,
  resources, efficiency, stockpiles, manpower and reinforcement; division
  assignment, commanders, front lines, offensive lines, execution and manual
  orders; terrain, weather, organisation, strength and combat; rail, supply
  hubs, motorisation and local delivery; scoped fighters and close air support;
  province and victory-point control, surrender progress, capitulation and the
  immediate war settlement; pause and speed controls.
- Excluded: any campaign after the Ethiopian war; world-conquest or Second
  World War coverage; other nations and starts; navy, diplomacy, factions,
  justifications, occupation and resistance after settlement; exhaustive laws,
  agencies, designers and intelligence; DLC-specific focus branches or systems;
  the public open beta, multiplayer, achievements, Ironman, mods, console
  commands and historical balance comparison.
- Potential scoped modules: one separate naval war; one diplomatic/faction
  route; an independently versioned DLC focus path; logistics in a larger
  theatre; multiplayer; or one post-capitulation occupation packet.
- Direct-play status: no fresh end-to-end authenticated tutorial run was
  conducted. Current official build evidence and official tutorial, planning,
  production and supply material establish a reproducible transition model;
  exact AI choices and battle duration remain live variation rather than a
  claimed captured play trace.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `HOI4-001` | Patch 1.19.2 / build 23969257 is the reviewed stable public PC rules boundary, distinct from the public open beta | Confirmed | Direct | High | P1, P2 |
| `HOI4-002` | The official tutorial starts Italy in the ongoing Ethiopian war and deliberately permits the save to continue after its teaching sequence | Confirmed | Direct | High | P3 |
| `HOI4-003` | National Focus and research choices advance time-bound prerequisite systems and apply persistent national effects | Confirmed | Corroborated | High | P2, P8 |
| `HOI4-004` | Civilian factories advance ordered state construction while military factories convert resources and efficiency into equipment | Confirmed | Direct | High | P2, P7, P8 |
| `HOI4-005` | Produced equipment and available manpower replenish divisions rather than appearing directly as free combat power | Confirmed | Corroborated | High | P7, P9 |
| `HOI4-006` | Divisions can be grouped under an army, assigned a front and offensive line, then execute or receive manual overrides | Confirmed | Direct | High | P4 |
| `HOI4-007` | Division combat changes strength, organisation, position and control continuously under terrain and current combat conditions | Observation | Corroborated | High | P2, P4 |
| `HOI4-008` | Supply flows from the capital through railway-linked hubs and last-mile delivery; insufficient capacity constrains divisions | Confirmed | Direct | High | P5, P6 |
| `HOI4-009` | Assigned aircraft operate within base, range and mission constraints and can support the scoped land offensive | Observation | Corroborated | Medium | P2, P10 |
| `HOI4-010` | Current allied control reveals map state while fog and intelligence limit actionable hostile information | Observation | Corroborated | High | P2, P4 |
| `HOI4-011` | Province and victory-point losses produce surrender progress; the bounded route stops at Ethiopian capitulation and immediate war settlement | Observation | Corroborated | High | P3, P9 |
| `HOI4-012` | The tutorial route couples focus, research, industry, logistics, front execution and air support without requiring any post-war campaign | Observation | Corroborated | High | P2–P10, V1 |

## Basic data

- Release / origin: developed and published by Paradox Interactive; released
  for PC on 2016-06-06 and maintained as a live strategy product.
- Platform or physical form: pausable real-time grand-strategy simulation on
  Windows PC; one current official tutorial war is scoped.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  agent routing and coordination; ordered dependency sequencing.
- Primary and reproducible sources:
  - **[P1]** [official 1.19.2 announcement](https://steamcommunity.com/ogg/394360/announcements/detail/717908846920599779),
    for the latest default public version and its separation from the beta.
  - **[P2]** [official Steam product page](https://store.steampowered.com/app/394360/Hearts_of_Iron_IV/),
    for the current PC product, nation control, industry, research, division
    design and battle-plan boundary.
  - **[P3]** [official tutorial developer diary](https://store.steampowered.com/news/posts/?appids=394360&enddate=1464622058),
    for Italy, the Ethiopian war and the intentionally non-terminal tutorial.
  - **[P4]** [official battle-plan developer diary](https://store.steampowered.com/news/posts/?appids=394360&enddate=1457093764),
    for armies, front lines, offensive lines, execution and manual overrides.
  - **[P5]** [official supply-system first look](https://store.steampowered.com/news/posts/?appids=394360&enddate=1618239639&feed=steam_community_announcements),
    for hubs, rails, terrain, weather and motorised last-mile reach.
  - **[P6]** [official supply-system follow-up](https://store.steampowered.com/news/posts/?appids=394360&enddate=1626890445&feed=steam_community_announcements),
    for capital-to-hub capacity and multi-hub division supply.
  - **[P7]** [official production and resources diary](https://store.steampowered.com/news/posts/?appids=394360&enddate=1487775050&feed=steam_community_announcements),
    for factory allocation, line efficiency and resource shortage.
  - **[P8]** [official industry and National Focus diary](https://store.steampowered.com/news/posts/?appids=394360&enddate=1455284529),
    for factory slots and focus/technology effects on national capacity.
  - **[P9]** [official Paradox-published game guide mirror](https://manuals.plus/wp-content/sideloads/-hearts-of-iron-iv-game-guide-original.pdf),
    used as secondary corroboration for tutorial sequence, production,
    reinforcement, combat, surrender and peace settlement.
  - **[P10]** [official Hearts of Iron IV air-warfare reference](https://hoi4.paradoxwikis.com/Air_warfare),
    a maintained official-wiki reference for bases, regions, range and missions.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P10` under the declared build and tutorial boundary; rules reasoning,
  not a direct-play claim.
- Claim IDs: `HOI4-001`–`HOI4-012`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-006`, change the running simulation speed; `ACT-121`,
  select or queue reachable research; `ACT-189`, issue a selected division a
  manual destination or attack order.
- New genes: `ACT-324`, select one eligible National Focus; `ACT-325`, place and
  prioritise state construction in the national queue; `ACT-326`, configure an
  equipment production line and its factory allocation; `ACT-327`, assign
  divisions to an army and commander; `ACT-328`, draw a front and offensive
  line and toggle execution; `ACT-329`, assign an air wing to a region and
  mission.
- Parameters: focus, research slot, technology, state, building, queue priority,
  equipment type, factory count, division set, army, commander, front,
  offensive line, execution state, manual order, air wing, region, mission,
  pause and speed.
- Claim IDs: `HOI4-003`–`HOI4-010`.

### System Behaviour Genes

- Existing genes: `SYS-297`, execute selected-unit pathing and attack
  acquisition; `SYS-305`, update allied vision, fog and detection.
- New genes: `SYS-563`, advance the active National Focus and apply its effects;
  `SYS-564`, advance parallel research slots and apply completed technologies;
  `SYS-565`, distribute civilian construction work through the priority queue;
  `SYS-566`, turn military factories, resources and line efficiency into
  equipment; `SYS-567`, distribute manpower and equipment through reinforcement
  and replacement; `SYS-568`, execute army plans and resolve division combat;
  `SYS-569`, propagate supply through capital, rail, hubs and last-mile delivery;
  `SYS-570`, resolve assigned air missions and their land-combat contribution;
  `SYS-571`, convert territorial loss into surrender, capitulation and immediate
  war settlement.
- Resolution order: accept paused national and theatre commands; when time runs,
  advance focus, research, construction and production; distribute equipment,
  manpower and supply; execute movement, plans, air missions and combat; update
  vision and territorial control; then test surrender and settle the war.
- Parameters: daily progress, focus and technology costs, factory allocation,
  resources, efficiency, stockpile, manpower, reinforcement priority, plan,
  planning bonus, organisation, strength, combat width, terrain, weather, rail
  level, hub throughput, motorisation, air coverage, victory points and surrender.
- Claim IDs: `HOI4-003`–`HOI4-012`.

### Constraint Genes

- Existing gene: `CON-273`, fog and current detection gate actionable hostile
  state.
- New genes: `CON-477`, one active focus obeys prerequisites and mutual
  exclusions; `CON-478`, research needs an available slot and reachable
  technology; `CON-479`, construction needs state capacity and assignable
  civilian factories; `CON-480`, production needs an unlocked equipment line,
  allocated factories and resources; `CON-481`, army plans need assigned
  divisions, legal fronts and reachable orders; `CON-482`, supply is bounded by
  rail, hub, transport and local delivery capacity; `CON-483`, air missions need
  aircraft, a viable base, range, fuel and a selected region; `CON-484`,
  capitulation requires sufficient surrender progress and terminal war state.
- Scarce strategic resources: calendar time, research slots, civilian and
  military factories, state slots, strategic resources, line efficiency,
  equipment stockpiles, manpower, organisation, planning time, rail/hub
  throughput, trains, trucks, fuel, aircraft, range and controlled victory points.
- Claim IDs: `HOI4-003`–`HOI4-011`.

### Information Genes

- Existing gene: `INF-059`, expose reachable technology dependencies and
  unlocks.
- New genes: `INF-229`, expose national focus, research and top-level resource
  state; `INF-230`, expose construction, production, resource and equipment
  flow; `INF-231`, show armies, divisions, fronts, plan status and combat on the
  strategic map; `INF-232`, expose supply hubs, rails, reach and deficits;
  `INF-233`, expose air-region coverage, wing and mission state; `INF-234`, show
  territorial control, victory points, surrender progress and war settlement.
- Claim IDs: `HOI4-003`–`HOI4-011`.

### Objective Genes

- New gene: `OBJ-106`, force Ethiopia to capitulate and conclude the tutorial
  war as Italy.
- Success, evaluation and failure: the packet succeeds when territorial and
  victory-point loss crosses Ethiopia's surrender threshold and the immediate
  war settlement completes; it fails if Italy can no longer prosecute the war
  or the bounded route is abandoned before that terminal.
- Claim IDs: `HOI4-002`, `HOI4-011`, `HOI4-012`.

### Time Genes

- Existing gene: `TIM-003`, national systems, armies and war advance in real
  time while the player may pause for unbounded planning or select a faster
  running rate.
- Claim IDs: `HOI4-003`–`HOI4-012`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Stable 1.19.2 is selected and the official Tutorial is loaded | Begin as Italy | The first paused 1936 frame exposes the existing Ethiopian war and tutorial guidance | Entry is current, official and bounded | `HOI4-001`, `HOI4-002` |
| No National Focus is active and a research slot is open | Select one eligible focus and reachable technologies | Daily progress advances each independent target and applies completed effects | Parallel national dependencies consume time | `HOI4-003` |
| Civilian factories and legal state capacity are available | Queue and prioritise one useful construction | Assigned civilian capacity advances the first eligible projects and persists completed infrastructure | Industry is an allocation queue, not a one-click purchase | `HOI4-004` |
| Infantry equipment or support aircraft has an unlocked line | Assign military factories and inspect resource supply | Daily output depends on factory count, resources and retained line efficiency, then enters stockpile | Industrial configuration produces later combat capacity | `HOI4-004` |
| A division lacks equipment or manpower | Keep the relevant stockpile and manpower available | Reinforcement transfers replacements over time, changing strength and readiness | Production and combat bodies are coupled indirectly | `HOI4-005` |
| Italian divisions are available in Eritrea and Somaliland | Assign them to armies and commanders | Each division gains army membership and can receive a shared plan or manual order | Command authority is explicit and many-agent | `HOI4-006` |
| An army faces Ethiopian territory | Draw a front and offensive line, then execute | Divisions distribute along the front, accumulate planning and advance toward the line while combat resolves | A plan is a persistent spatial instruction field | `HOI4-006`, `HOI4-007` |
| One local axis needs correction | Issue a manual move or attack order | The selected division paths and acquires a reachable target, overriding ordinary plan movement where legal | High-level planning retains local intervention | `HOI4-006`, `HOI4-007` |
| A supply map exposes weak reach to a front | Improve or motorise the relevant route and avoid overloading it | Rail/hub/last-mile capacity changes delivered supply and resulting penalties | Logistics constrains feasible front pressure | `HOI4-008` |
| Fighters or close-air-support wings have viable bases and range | Assign their region and mission | Eligible sorties alter air and land-combat contribution while fuel and coverage remain legal | Air support is a bounded parallel theatre system | `HOI4-009` |
| Ethiopian provinces and victory points are contested | Continue legal front and manual pressure | Control changes update surrender progress while equipment, organisation and supply continue resolving | Territorial progress is produced by the whole coupled loop | `HOI4-007`–`HOI4-011` |
| Ethiopia crosses its surrender threshold | Resolve capitulation and the immediate terminal settlement | The Ethiopian war concludes; stop before any post-war national play | The unit has a reproducible ADR-007 terminal | `HOI4-011`, `HOI4-012` |

## Strategic and experiential structure

- Local decision: change speed, repair a production deficit, reprioritise one
  build, move one division, adjust a front or air mission, or pause before a
  deteriorating battle settles.
- Medium-term planning: align focus and research completion with equipment
  output; preserve organisation and supply; coordinate northern and southern
  pressure so victory-point gains cost less manpower and equipment.
- Long-term structure: convert Italy's starting national capacity into a
  supplied two-front offensive, maintain enough land and air pressure to take
  Ethiopian victory points, and stop at capitulation rather than importing the
  rest of the world simulation.
- Common heuristics: plan while paused; keep production lines stable enough to
  retain efficiency; read shortages before adding divisions; do not overstack a
  low-supply front; use manual orders only where they improve the plan; base air
  wings within useful range; prioritise connected victory points.
- Failure attribution: focus/research panels expose dependencies; industry and
  logistics views expose shortages; division tooltips expose organisation and
  strength; plan indicators expose readiness; combat bubbles, air regions and
  surrender progress distinguish tactical, logistical and terminal failures.
- Player-trust factors: inspectable prerequisites and allocations, explicit
  pause/rate control, visible route capacity, persistent drawn plans and a
  declared surrender terminal.
- Claim IDs: `HOI4-003`–`HOI4-012`.

## Replay and variation

- What changes between sessions: research/focus order, factory allocation,
  construction priority, army grouping, front geometry, manual overrides, air
  allocation, AI response, battle duration and equipment losses.
- Randomness or procedural generation: combat and AI decisions can diverge;
  the tutorial start, countries and current stable ruleset are fixed.
- Multiple viable strategies: conservative plan execution, local manual
  encirclement, stronger northern concentration, balanced two-front pressure or
  greater air investment can all reach the same capitulation terminal.
- Typical replay motive: reduce casualties and time, preserve stockpiles,
  improve supply, coordinate fronts or test a different lawful focus/research
  sequence within the same tutorial boundary.
- Claim IDs: `HOI4-002`–`HOI4-012`.

## Adjacent systems and history

- Direct predecessors: earlier Hearts of Iron titles establish lineage, but no
  historical rules or balance values are imported into patch 1.19.2.
- Variants: DLC focus trees and systems, other countries, multiplayer, naval
  theatres and later world war all require independent scopes.
- Similar games: Civilization VI shares national research, construction,
  resources, fog and strategic war; Age of Empires II shares real-time unit
  commands, vision, production dependencies and territorial combat; Factorio
  shares production flow and bottleneck diagnosis.
- Important differences: HOI4 allocates national factories rather than city or
  building-local queues, translates stockpiles through reinforcement, retains
  drawn army plans, routes supply through a theatre network and resolves a
  country surrender threshold instead of one city, unit or fixed structure.
- Claim IDs: `HOI4-003`–`HOI4-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-006`, `ACT-121`, `ACT-189`, `ACT-324`–`ACT-329` | time, focus, research, construction, production, army, front and air orders |
| System Behaviour | `SYS-297`, `SYS-305`, `SYS-563`–`SYS-571` | progress, industry, reinforcement, plans, combat, supply, air and capitulation |
| Constraint | `CON-273`, `CON-477`–`CON-484` | fog, prerequisites, capacity, resources, command, logistics, air and surrender gates |
| Information | `INF-059`, `INF-229`–`INF-234` | dependencies, national, industry, army, supply, air and war state |
| Objective | `OBJ-106` | conclude the Ethiopian war through capitulation |
| Time | `TIM-003` | pausable continuously advancing national war |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `181` (`GAME-0001`–`GAME-0181`).
- Exact genome matches: none.
- Tied near matches: `GAME-0179` — Age of Empires II: Definitive Edition (`7 / 60 = 0.116667`).
- Supported combination subsets: `COMB-0180`.
- Scan date: 2026-08-29.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0179` — Age of Empires II: Definitive Edition | `ACT-121`, `ACT-189`, `SYS-297`, `SYS-305`, `CON-273`, `INF-059`, `TIM-003` | Both select research, issue live unit orders, execute pathing and gate hostile state through vision. AoE II uses mobile villagers, physical drop-offs, constructed housing, building-local queues and four Ages; HOI4 allocates national factories, reinforces divisions from stockpiles, retains drawn fronts, routes theatre supply, assigns regional air missions and aggregates victory points into country capitulation | Near, `0.116667` |

### Preserved research notes

- New genes: `ACT-324`–`ACT-329`, `SYS-563`–`SYS-571`, `CON-477`–`CON-484`,
  `INF-229`–`INF-234` and `OBJ-106`.
- Classification result: thirty new boundaries plus eight established generic
  genes and one verified strict combination.
- Evidence and reasoning: the national focus, factory-allocation,
  reinforcement, battle-plan, supply and surrender chain has no earlier single
  carrier; each reused gene retains its prior intervention-response boundary.

## Combination status

- `COMB-0180` is a verified strict subset coupling national dependencies,
  industry, stockpile reinforcement, drawn fronts, supply, air support and
  surrender into the bounded tutorial-war terminal.
- Earlier verified combinations remain tested after registration.

## Taxonomy impact

- Registry changes: thirty new Active genes, links on eight reused Active
  genes, `COMB-0180` and four existing family memberships.
- Taxonomy-change record: none; no prior lifecycle, definition or reviewed game
  signature changes.
- Candidate terms affected: national focus, national construction allocation,
  production-line efficiency, stockpile reinforcement, battle plan, theatre
  supply, air-region mission and country surrender.

## Negative results

- Civilization VI city production and turn settlement are not reused: HOI4
  distributes national factories continuously across state construction and
  equipment lines.
- Age of Empires II building-local queues and selected villager labour are not
  reused: no constructed site owns the national focus, research or production
  progress in this packet.
- Direct real-time combat `SYS-215` is not reused: divisions execute persistent
  plans and orders at an abstract province scale rather than exposing embodied
  player-controlled attacks.
- The complete world-war, diplomacy, navy, occupation, intelligence and DLC
  systems are excluded instead of being unioned into this tutorial genome.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Stable patch 1.19.2 supports one official
  Italy tutorial route whose bounded terminal is the conclusion of the
  Ethiopian war, even though the save itself may continue (`HOI4-001`–`HOI4-012`).

## Нові гени

- [Observation | Corroborated | High] Thirty new boundaries isolate national
  focus, factory allocation, reinforcement, drawn fronts, theatre supply, air
  support and capitulation from earlier city- and building-scale strategy games.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0180` records the strict national-
  allocation-to-capitulation chain for this tutorial war.

## Зміни таксономії

- [Confirmed | Direct | High] No existing gene or reviewed signature changes.

## Family classification

- `FAM-009` — Tactical forecast and counterplay: front geometry, production and
  support are revised against live hostile responses.
- `FAM-010` — Real-time system pressure: every national and theatre process
  advances while time runs, with pause as a planning control.
- `FAM-015` — Agent routing and coordination: multiple divisions and air wings
  are organised through shared commands and spatial plans.
- `FAM-017` — Ordered dependency sequencing: research, focus, industry,
  equipment, supply and territorial steps gate later war progress.
- No new family is created from one game.

## Plain-language interpretation

The tutorial war is not solved by selecting an army and watching a bar fill.
Italy's front depends on decisions made at several scales: which national work
finishes next, where civilian factories build, which equipment military
factories produce, and whether replacements and supply can reach the divisions
asked to advance.

The map then turns those allocations into a live planning problem. A drawn
front gives many divisions a shared instruction, but the player still pauses,
reads weak axes and changes a local order or air mission. Capturing territory
matters because important victory points raise surrender progress; the unit
ends when that coupled national and spatial system concludes the Ethiopian war,
not when the continuing sandbox runs out of things to do.

## New questions

- Which later grand-strategy game reuses national production and multi-agent
  fronts while replacing continuous supply delivery or surrender thresholds?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0183` — Vampire Survivors, the next ordered
  horizon item in `SEARCH_DEMAND_GAME_SELECTION_006`.
- Optimisation criterion: contrast state-scale planning with one bounded
  auto-attack survival run and its build-draft pressure.
- Expected gene pressure: automatic weapons, experience pickups, timed waves,
  level-up choices, evolution dependencies and a reproducible run terminal.
- Anti-bias note: do not carry HOI4's commanded-agent or national-allocation
  assumptions into an avatar-centred automatic-combat loop.

## Next research step

- Integrate `GAME-0183` Vampire Survivors as one independently reviewed unit;
  do not start it inside this unit's commit.

## Design lessons

- A pausable simulation remains a real-time pressure system because every
  coupled process changes independently whenever time resumes.
- A bounded country surrender can make one tutorial war reproducible without
  pretending to analyse the entire live-service grand-strategy product.

## Open questions

- Exact AI choices, daily battle duration and casualty totals vary and are not
  asserted by this rules-level transition trace.
- A future direct-play verification should confirm the precise current text of
  the final tutorial prompt without expanding the terminal beyond Ethiopia.

## Reproducibility notes

1. Verify stable public patch `1.19.2` / Steam build `23969257`; do not opt into
   the public beta. Use English, no mods, Ironman off and disable every
   separately selectable DLC.
2. Start the official Tutorial as Italy and record the first paused controllable
   frame on 1 January 1936 with the Ethiopian war already active.
3. Record one focus, research, construction and military-production commitment;
   inspect equipment, manpower and reinforcement state before advancing time.
4. Organise the Eritrean and Somaliland divisions, draw legal fronts and
   offensive lines, execute at least one plan and record one justified manual
   correction under normal fog.
5. Inspect supply routes and one scoped air-support assignment; continue only
   until Ethiopian surrender progress triggers capitulation and the immediate
   war settlement, then stop the trace.

## Review record

- Research status: `reviewed`.
- Reviewed: 2026-08-29.
- Scope changes during review: narrowed from the complete current product to
  stable 1.19.2's official Italy tutorial through the Ethiopian war only.
- Evidence changes during review: current patch, tutorial intent, battle plans,
  industry and supply are primary-source anchored; exact AI and final prompt
  wording remain explicitly non-direct-play.
- Gene changes during review: reused eight generic boundaries and added thirty
  for nation-scale allocation, planning, logistics and surrender.

## Localisation status

- Ukrainian game, all new-gene and combination entries are reviewed in this
  unit. Canonical title and interface terms remain `Hearts of Iron IV`,
  `National Focus`, `Italy` and `Ethiopia` where product identity benefits from
  preservation; surrounding explanation is reviewed Ukrainian.

## Source notes

- Official sources were checked on 2026-08-29. The stable public announcement
  owns the version boundary; older official diaries own enduring mechanics, not
  current numerical balance values.
- The official guide mirror is secondary corroboration and does not override
  current 1.19.2 material.

## Next recommended action

- Integrate `GAME-0183` — Vampire Survivors after the required thirty-second
  stop window.
