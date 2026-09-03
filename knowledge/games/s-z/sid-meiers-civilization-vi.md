---
game_id: GAME-0166
slug: sid-meiers-civilization-vi
game_title: Sid Meier’s Civilization VI
analysis_status: reviewed
reviewed: 2026-08-27
combination_ids:
  - COMB-0164
gene_ids:
  action:
    - ACT-019
    - ACT-096
    - ACT-121
    - ACT-130
    - ACT-139
    - ACT-275
    - ACT-276
    - ACT-277
    - ACT-278
    - ACT-279
    - ACT-280
    - ACT-281
  system:
    - SYS-004
    - SYS-154
    - SYS-213
    - SYS-305
    - SYS-481
    - SYS-482
    - SYS-483
    - SYS-484
    - SYS-485
    - SYS-486
    - SYS-487
    - SYS-488
    - SYS-489
    - SYS-490
    - SYS-491
    - SYS-492
    - SYS-493
  constraint:
    - CON-062
    - CON-185
    - CON-273
    - CON-410
    - CON-411
    - CON-412
    - CON-413
    - CON-414
    - CON-415
    - CON-416
    - CON-417
    - CON-418
    - CON-419
    - CON-420
    - CON-421
  information:
    - INF-058
    - INF-059
    - INF-086
    - INF-184
    - INF-185
    - INF-186
    - INF-187
    - INF-188
    - INF-189
    - INF-190
    - INF-191
  objective:
    - OBJ-093
  time:
    - TIM-018
---

# Game: Sid Meier's Civilization VI

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: official launch/base-game PC rules represented by the
  English 25th Anniversary manual and current Steam base product; single-player
  `Create Game` with Trajan/Rome, Prince difficulty, Standard speed, Tiny
  Pangaea, three fixed base-game opponents (Pericles/Greece,
  Cleopatra/Egypt and Frederick/Germany), zero city-states, no barbarians, no
  tribal villages, Science Victory as the only enabled victory type, game seed
  `20260827166` and map seed `20260827167`.
- Primary decision loop: inspect the revealed hex map, units, cities, yields,
  current technology/civic, government, diplomacy and Science Victory state;
  issue legal movement, unit, city, research, policy, trade, purchase,
  construction or diplomatic commands; end Rome's turn; then let the three
  rivals resolve their turns and return control with changed world state.
- Entry and exit: begins on Turn 1 before Rome's starting Settler founds the
  first city; succeeds when Rome launches the third required Mars module and
  the base-game Science Victory resolves, or fails for the route if another
  civilization wins first or Rome loses every city.
- Included: seeded Pangaea terrain and resources; exploration and fog of war;
  hex movement, terrain costs, zone of control and one-unit-per-class stacking;
  city founding, territory, citizens, worked tiles, food, Housing and Amenities;
  production, Gold and purchases; builders, improvements and strategic/luxury
  resources; districts, buildings, placement and adjacency; Technology and
  Civic trees, prerequisites and boosts; governments and policy slots; trade
  routes, roads and trading posts; civilization diplomacy, deals, war, peace
  and warmonger state; unit/city combat, promotion and capture; the Spaceport,
  Satellite, Moon Landing and three Mars-module Science Victory chain; Rome
  and Trajan effects only as fixed parameters of this route.
- Excluded: Rise and Fall, Gathering Storm, Leader Pass, New Frontier Pass and
  all DLC civilizations/scenarios; multiplayer, mods and alternate map scripts;
  city-states, envoys and suzerainty; barbarians and tribal villages; Religious,
  Culture, Domination and Score Victory terminals; founding a player religion,
  theological combat, tourism/Great Works, espionage, exhaustive wonders,
  exhaustive Great People and comparisons across every leader ability.
- Potential scoped modules: the base-game Religious or Culture route; a
  city-state and envoy network; espionage; one different leader/civilization;
  one multiplayer match; or one separately versioned expansion ruleset.
- Direct-play status: no fresh full-length paid-account Mars run was conducted.
  The official launch manual supplies reproducible setup, turn, map, city,
  research, government, trade, diplomacy, combat and launch transitions; the
  official product page and Steam record establish the base-game/expansion
  boundary; official Rome material establishes the selected leader parameter.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `CIV6-001` | Advanced Setup can bind map, pace, difficulty, rival count, victory types and seeds into one reproducible solo game | Confirmed | Direct | High | P1, P2 |
| `CIV6-002` | Solo play alternates one multi-command human turn with a turn for every rival until a victory resolves | Confirmed | Direct | High | P1 |
| `CIV6-003` | A seed produces hex terrain, resources and fog states whose revealed information persists | Confirmed | Direct | High | P1 |
| `CIV6-004` | Units spend movement under terrain, passability, stacking and zone-of-control rules | Confirmed | Direct | High | P1 |
| `CIV6-005` | A Settler founds a spaced city whose citizens work territory and whose food, Housing and Amenities affect growth | Confirmed | Direct | High | P1 |
| `CIV6-006` | Each city accumulates one production target while Gold may buy eligible units or buildings | Confirmed | Direct | High | P1 |
| `CIV6-007` | Districts occupy separate legal hexes, use population capacity and derive yields from placement, adjacency and buildings | Confirmed | Direct | High | P1 |
| `CIV6-008` | Science and Culture advance parallel prerequisite trees, with boosts accelerating disclosed targets and unlocks | Confirmed | Direct | High | P1 |
| `CIV6-009` | Governments expose typed policy slots; traders select destinations and create yields, roads and later trading posts | Confirmed | Direct | High | P1 |
| `CIV6-010` | Diplomacy supports contact, relationships, deals, war and peace, while combat can defeat units or capture cities | Confirmed | Direct | High | P1 |
| `CIV6-011` | Base-game Science Victory requires a Spaceport, Satellite, Moon Landing and all three Mars modules in order | Confirmed | Direct | High | P1, P2 |
| `CIV6-012` | Trajan is the selected base-game Roman leader and founded Roman cities begin with the current City Center building entitlement | Confirmed | Corroborated | High | P3, P4 |

## Basic data

- Release / origin: developed by Firaxis Games and published by 2K; PC release
  2016-10-21.
- Platform or physical form: turn-based single-player 4X strategy game; fixed
  launch/base-game PC setup is scoped.
- Puzzle family: route and network construction; tactical forecast and
  counterplay; agent routing and coordination; ordered dependency sequencing.
- Primary and reproducible sources:
  - **[P1]** [official English launch manual](https://downloads.2kgames.com/civilization/vi/manuals/eu/CIV_VI_25TH_ONLINE_MANUAL_ENG.pdf),
    for Advanced Setup, turn order, hex world, units, cities, districts,
    research, government, trade, diplomacy, combat and Science Victory.
  - **[P2]** [official Civilization VI page](https://civilization.2k.com/en-GB/civ-vi/),
    for the base game, twenty historical leaders, five base victory paths and
    the separation of expansion systems.
  - **[P3]** [official Rome First Look](https://www.youtube.com/watch?v=8Deqrw_Is3Y),
    for Trajan, Rome and the route's civilization parameters.
  - **[P4]** [official 2K Trajan/Julius Caesar article](https://store.2k.com/news/add-julius-caesar-and-scout-cat-to-civilization-vi),
    for Trajan as default Roman leader and his founded-city building effect.
  - **[P5]** [Steam product page](https://store.steampowered.com/app/289070/Sid_Meiers_Civilization_VI/),
    for the reviewed PC product, release and base-game/DLC distinction.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P5` under the declared setup and seeds; rules reasoning, not a direct-play claim.
- Claim IDs: `CIV6-001`–`CIV6-012`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-019`, select a unit ability and target, including Found
  City, improve, attack and fortify; `ACT-096`, choose an eligible unit
  destination; `ACT-121`, select a Technology research target; `ACT-130`, buy
  an eligible unit or building; `ACT-139`, place a district or wonder footprint.
- New genes: `ACT-275`, choose one city's production target; `ACT-276`, choose
  the active Civic; `ACT-277`, assign a citizen to a worked tile or specialist
  slot; `ACT-278`, select a government and fill policy slots; `ACT-279`, choose
  an eligible trader destination; `ACT-280`, propose or answer a diplomatic
  deal, relationship, war or peace action; `ACT-281`, end the current
  civilization's multi-command turn.
- Parameters: selected unit/city, hex, target, queue item, technology, civic,
  citizen, government, policy card, route, rival, deal terms and confirmation.
- Claim IDs: `CIV6-002`, `CIV6-004`–`CIV6-010`.

### System Behaviour Genes

- Existing genes: `SYS-004`, sample declared setup randomness from the fixed
  seeds; `SYS-154`, settle recurring empire income and costs; `SYS-213`, retain
  a mutable seed-generated tile world; `SYS-305`, update fog and current vision.
- New genes: `SYS-481`, turn a consumed Settler into a city and initial
  territory; `SYS-482`, aggregate worked-tile and specialist yields; `SYS-483`,
  convert food, Housing and Amenities into growth and yield modifiers;
  `SYS-484`, accumulate city production and complete its current target;
  `SYS-485`, expand city borders through Culture; `SYS-486`, advance parallel
  Technology and Civic targets with Science, Culture and boosts; `SYS-487`,
  compute district placement, adjacency and building yields; `SYS-488`, convert
  builder improvements and connected resources into yields, unit access and
  Amenities; `SYS-489`, apply government and policy effects; `SYS-490`, settle
  trader yields while creating roads and trading posts; `SYS-491`, resolve
  relationships, deals, war, peace and warmonger consequences; `SYS-492`,
  resolve unit/city combat, promotion, defeat and capture; `SYS-493`, advance
  the ordered Spaceport launch chain and settle Science Victory.
- Resolution order: Roman commands mutate provisional unit, city, economy and
  diplomatic state; End Turn settles yields, production, growth, research and
  timed effects; each fixed rival then takes and settles one turn; fog and
  relationships update before Rome receives the next decision interval; the
  first enabled victory predicate terminates the game.
- Parameters: seeds, map, yields, growth thresholds, costs, adjacency values,
  boost fractions, policy effects, trade yields, relationship values, combat
  strength, project costs and rival choices.
- Claim IDs: `CIV6-001`–`CIV6-011`.

### Constraint Genes

- Existing genes: `CON-062`, a placed district footprint must fit its target;
  `CON-185`, citizens are finite reassignable work slots; `CON-273`, actions
  cannot rely on map state still concealed by fog.
- New genes: `CON-410`, units obey per-turn movement/action budgets, terrain,
  rivers, passability and zone of control; `CON-411`, one combat unit and one
  civilian unit at most may share a hex; `CON-412`, city founding obeys terrain
  and minimum inter-city distance; `CON-413`, citizens work only eligible tiles
  or slots assigned to that city; `CON-414`, districts require population
  capacity and district-specific legal terrain; `CON-415`, builders spend
  finite charges only on eligible improvements; `CON-416`, Technology and Civic
  targets require their prerequisite graph; `CON-417`, production and purchase
  targets require unlocks, resources, capacity and affordability; `CON-418`,
  policy cards fit only compatible government slots; `CON-419`, trade routes
  require capacity, an available trader and an eligible reachable destination;
  `CON-420`, diplomacy, war and peace actions obey contact, relationship and
  treaty timing gates; `CON-421`, Spaceport projects require their district,
  technologies and declared launch order.
- Scarce strategic resources: per-turn unit movement/actions, Settlers,
  Builders and charges, citizens, district capacity, Food, Production, Gold,
  Science, Culture, Housing, Amenities, strategic/luxury resources, policy
  slots, trader capacity, military health and turns before rival victory.
- Claim IDs: `CIV6-004`–`CIV6-011`.

### Information Genes

- Existing genes: `INF-058`, show empire income, balances and recurring costs;
  `INF-059`, expose Technology/Civic prerequisites and unlock dependencies;
  `INF-086`, show settlement population, needs and workforce.
- New genes: `INF-184`, retain explored terrain, resources, borders and current
  visibility on the hex map; `INF-185`, expose city yields, production, growth,
  Housing, Amenities and citizen assignments; `INF-186`, show district legal
  hexes and adjacency preview; `INF-187`, show government slots and policy
  effects; `INF-188`, expose rival relationship, deal, war, peace and warmonger
  state; `INF-189`, show trade capacity, destinations and route yields;
  `INF-190`, show unit movement, actions, strength and combat forecast;
  `INF-191`, show Science Victory milestones and rival progress.
- Claim IDs: `CIV6-003`–`CIV6-011`.

### Objective Genes

- New gene: `OBJ-093`, found and develop Rome, build a Spaceport, launch the
  Satellite and Moon Landing, then launch all three Mars modules before any
  fixed rival reaches its enabled terminal.
- Success, evaluation and failure: the third legal Mars-module launch settles
  success; a rival Science Victory or the loss of every Roman city settles
  failure for the selected route.
- Claim IDs: `CIV6-001`, `CIV6-011`.

### Time Genes

- New gene: `TIM-018`, each civilization receives a sequential turn containing
  any number of legal unit, city, economy, research and diplomacy commands,
  then commits it before the next civilization acts.
- Claim IDs: `CIV6-002`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Declared setup and both seeds are entered | Start Game | One Tiny Pangaea map, Rome and the three named rivals are instantiated under Prince/Standard rules | Reproducible entry packet | `CIV6-001`, `CIV6-003` |
| Rome's Settler stands on a legal Turn 1 hex | Use Found City | Settler is consumed; Rome gains a City Center, initial territory and Trajan's current starting-building entitlement | City founding is a state transition | `CIV6-005`, `CIV6-012` |
| A unit has movement remaining beside mixed terrain | Choose a reachable destination | Terrain and river costs spend movement; impassable and stacking-invalid endpoints are rejected | Hex travel is budgeted and constrained | `CIV6-004` |
| A city has an unassigned citizen | Assign one eligible tile | That tile's yields join the next city/empire settlement; the former assignment stops contributing | Citizens select, rather than merely decorate, yield production | `CIV6-005` |
| A Campus placement lens is open near two mountains | Place the Campus on a legal hex | The separate hex is reserved and its disclosed adjacency contributes when completed | District geometry affects later yield | `CIV6-007` |
| A builder has a charge on eligible resource terrain | Order the matching improvement | One charge is spent; yields and eligible connected-resource effects update | Improvements transform finite worker authority into economy | `CIV6-006`, `CIV6-009` |
| A Technology or Civic is active and its boost condition is met | Complete the boost trigger, then End Turn | The declared fraction of progress applies; later Science/Culture completes the target and unlocks dependants | The two trees are parallel dependency races | `CIV6-008` |
| A government has one compatible empty slot | Assign an eligible policy | The card occupies that slot and its declared effects apply until a legal replacement | Government is a typed configuration | `CIV6-009` |
| A trader and capacity are free | Select the second Roman city | Per-turn route yields begin and traversed hexes acquire road/trading-post state as declared | Trade is both income and route construction | `CIV6-009` |
| Rome and a rival have contact | Propose a deal, declare war or later negotiate peace | Terms, relationship and treaty gates determine acceptance and persistent diplomatic consequences | Rival state changes future legal choices | `CIV6-010` |
| A Roman unit attacks a legal rival target | Commit the attack | Strength modifiers settle damage; defeat, promotion or city capture follows if thresholds are crossed | Combat converts positioning into ownership risk | `CIV6-004`, `CIV6-010` |
| Rome owns a Spaceport and the required technologies | Complete Satellite, Moon Landing and the three Mars projects in legal order | Each project advances the disclosed Science track; the third Mars module triggers victory if no rival has already won | Explicit terminal chain | `CIV6-011` |

## Strategic and experiential structure

- Local decision: choose which unit moves or acts, which hex a city works or
  claims, what each city produces and whether immediate military, economic or
  diplomatic pressure is worth delaying the Science route.
- Medium-term planning: connect improved resources, balance Food and Production,
  reserve population and terrain for Campus/Industrial Zone/Spaceport, time
  boosts, policy configurations and trade routes, and deter or exploit rivals.
- Long-term structure: parallel Technology and Civic dependency graphs unlock
  governments, infrastructure and the ordered five-project Spaceport terminal.
- Common heuristics: settle fresh water without blocking later districts;
  assign citizens to the current bottleneck; place Campus and Industrial Zone
  for visible adjacency; trigger reachable boosts; preserve Builder charges;
  use domestic routes to develop a second city; keep enough military to protect
  production; begin the Spaceport chain before a rival closes the race.
- Failure attribution: city panels, placement lenses, tree prerequisites,
  policy slots, route previews, combat forecasts and victory milestones expose
  most causal failures; rival choices and unrevealed territory remain bounded.
- Player-trust factors: explicit yields and forecasts make long plans
  inspectable, but fog, combat ranges and opponent diplomacy keep uncertainty.
- Claim IDs: `CIV6-003`–`CIV6-011`.

## Replay and variation

- What changes between sessions: seeded terrain/resource layout, founding
  position, expansion direction, district geometry, research order, policies,
  routes, diplomacy, wars and rival progress.
- Randomness or procedural generation: the two fixed seeds reproduce map-level
  setup, while rival decisions and outcomes remain state-dependent.
- Multiple viable strategies: taller or wider settlement, adjacency-first or
  conquest-supported production, domestic or international trade and different
  policy/boost sequences can all feed the same Mars terminal.
- Typical replay motive: test another leader, map, victory route or expansion;
  each is a potential new scope rather than evidence for this genome.
- Claim IDs: `CIV6-001`–`CIV6-011`.

## Adjacent systems and history

- Anno 1800 shares population-gated production, settlement needs and trade, but
  runs continuously and lacks hex-unit turns, separate adjacency districts,
  typed policy slots and the Mars launch chain.
- Factorio shares resource transformation, research prerequisites, constructed
  logistics and a rocket objective, but lacks sovereign citizens, diplomacy,
  city territory and alternating civilization turns.
- Humankind shares turn-based hex empires, territories, research, diplomacy and
  war, but does not reproduce Civilization VI's district/policy configuration
  and launch-rule five-project Science terminal.
- Important difference: the scoped game makes map geometry, population
  allocation and two concurrent research currencies converge on one explicitly
  ordered interplanetary project race.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-019`, `ACT-096`, `ACT-121`, `ACT-130`, `ACT-139`, `ACT-275`–`ACT-281` | civilization, city, unit and content identities are parameters |
| System Behaviour | `SYS-004`, `SYS-154`, `SYS-213`, `SYS-305`, `SYS-481`–`SYS-493` | seeds, costs, yields and AI choices are parameters |
| Constraint | `CON-062`, `CON-185`, `CON-273`, `CON-410`–`CON-421` | movement, thresholds, prices and capacities are parameters |
| Information | `INF-058`, `INF-059`, `INF-086`, `INF-184`–`INF-191` | exact UI geometry and icon style are presentation |
| Objective | `OBJ-093` | leader, rivals, seeds and enabled terminal are scoped parameters |
| Time | `TIM-018` | participant order and Standard pace values are parameters |

## Combination pattern

- New `COMB-0164` — found a hex empire and sequence its science economy from
  the first city through the three Mars launches.
- The combination excludes generic setup randomness, ordinary purchases,
  non-defining ledger detail and support forecasts while preserving the city,
  yield, district, research, government, trade, diplomacy, combat and launch
  dependency chain that distinguishes the selected route.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `165` (`GAME-0001`–`GAME-0165`).
- Exact genome matches: none.
- Tied near matches: `GAME-0132` — Anno 1800 (`7 / 101 = 0.069307`).
- Supported combination subsets: `COMB-0164`.
- Scan date: 2026-08-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0132` — Anno 1800 | `ACT-019`, `ACT-096`, `ACT-139`, `SYS-154`, `CON-062`, `INF-058`, `INF-086` | Anno 1800 grows population-gated island production and live cyclic shipping toward an exhibition. Civilization VI instead alternates whole empire turns on a hex map, assigns citizens to individual yields, configures separate adjacency districts and policies, conducts war and completes five ordered Spaceport projects. | Near, `0.069307` |

### Preserved research notes

- New genes: `ACT-275`–`ACT-281`, `SYS-481`–`SYS-493`, `CON-410`–`CON-421`,
  `INF-184`–`INF-191`, `OBJ-093` and `TIM-018`.
- Classification result: `New gene` and new combination of known and new genes.
- Evidence and reasoning: the distinctive boundary is the coupling of separate
  hex districts, finite city citizens, parallel Technology/Civic progress,
  typed policies and trader roads to the ordered five-project launch terminal.

## Taxonomy impact

- Registry changes: add 42 bounded genes and `COMB-0164`; reuse 15 established
  records at their existing causal boundaries.
- Taxonomy-change record: none.
- Candidate terms affected: leader, civilization, rival identity, seeds, map
  size, speed, exact costs/yields/boost values and balance remain parameters.

## Negative results

- No separate negative-result record. The review rejected Civic selection as a
  Technology parameter, government policies as unit equipment, trader routes
  as ordinary cargo steering, districts as City Center buildings, End Turn as
  one unit action and Gathering Storm's terminal as base-game Science Victory.
