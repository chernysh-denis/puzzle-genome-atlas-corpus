---
game_id: GAME-0186
slug: dont-starve-together
game_title: "Don’t Starve Together"
analysis_status: reviewed
reviewed: 2026-08-29
combination_ids:
  - COMB-0184
gene_ids:
  action:
    - ACT-008
    - ACT-087
    - ACT-122
    - ACT-123
    - ACT-161
    - ACT-164
    - ACT-165
    - ACT-199
    - ACT-338
    - ACT-339
  system:
    - SYS-215
    - SYS-223
    - SYS-326
    - SYS-327
    - SYS-329
    - SYS-353
    - SYS-416
    - SYS-591
    - SYS-592
    - SYS-593
    - SYS-594
    - SYS-595
    - SYS-596
    - SYS-597
  constraint:
    - CON-210
    - CON-281
    - CON-366
    - CON-496
    - CON-497
    - CON-498
    - CON-499
    - CON-500
    - CON-501
  information:
    - INF-073
    - INF-075
    - INF-128
    - INF-132
    - INF-136
    - INF-240
    - INF-241
  objective:
    - OBJ-110
  time:
    - TIM-003
---

# Game: Don't Starve Together

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current Windows PC stable build `747465`, reviewed
  2026-08-29; one private two-player Survival server on a newly generated
  Forest world. Survival is the default standard mode. Both participants select
  base Wilson; ordinary Forest settings remain default except Starting Season
  is explicitly Autumn and Events is explicitly none. PvP is off.
- Primary decision loop: split exploration and gathering; return or transfer
  materials; craft and place tools, fires, storage, cooking and science
  fixtures; prototype retained recipes; manage food freshness, hunger, sanity,
  darkness and temperature; fight ordinary threats; restore a ghost partner if
  death interrupts the plan; consolidate a warm shared base and repeat through
  the first Winter.
- Entry and exit: begins when both fresh Wilson survivors become controllable at
  the Florid Postern on day 1 of the new Autumn Forest. It succeeds at the first
  visible calendar transition out of Winter after day 35 into Spring while both
  survivors are alive and controllable beside a lit Fire Pit at one shared base
  containing an Alchemy Engine, Crock Pot and Chest, with each survivor carrying
  a Thermal Stone or wearing an ordinary insulating item. All-player death that
  reaches the Survival reset is failure. The Spring transition is an explicit
  analytical checkpoint, not a game-authored victory claim: it closes one full
  gather-build-prototype-preserve-recover climate loop in an otherwise open
  world.
- Included: seeded procedural Forest generation; personal explored maps;
  walking, harvesting and ordinary tool durability; finite stacks, inventory,
  equipment and item transfer; known recipes, ingredient checks and fixture
  placement; Science Machine and Alchemy Engine proximity/prototyping; Campfire
  and Fire Pit fuel, light and heat; health, hunger, sanity and temperature;
  raw/cooked food, Crock Pot conversion and spoilage; day, dusk and night;
  default 20-day Autumn, 15-day Winter and the first Spring boundary; ordinary
  local hostile combat; inventory drop, ghost state, Telltale Heart revival and
  the 120-second all-dead Survival reset.
- Excluded: Caves and Ruins, which require a separate server shard; oceans,
  Lunar Island, Moon Quay, moon-storm, Ancient Fuelweaver, Celestial Champion,
  Alter and shadow-alignment quest arcs; seasonal bosses as objectives;
  post-Spring survival, Summer and exhaustive multi-year ecology; farms,
  domestication, boats, magic and every recipe or creature not required by the
  transition trace; character skill trees and character-specific kits; public
  servers, PvP, Endless, Wilderness, Relaxed and Lights Out; mods, console,
  admin commands, rollback and custom resource/damage multipliers; time-limited
  events, skins, account inventory and platform economy.
- Potential scoped modules: one default Caves shard; one named character's
  current skill tree; one ocean expedition; one seasonal-boss preparation loop;
  or a later bounded Spring-to-Summer survival packet.
- Direct-play status: not conducted. Current first-party build and product
  records, maintained official-wiki rules and the bounded transition trace
  establish the packet without claiming unpublished generation probabilities
  or a game-authored ending.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DST-001` | `747465` is the current official Windows PC stable build boundary on the review date | Confirmed | Direct | High | P1, P2 |
| `DST-002` | The product is a cooperative procedurally generated survival world built around gathering, crafting, structures and exploration | Confirmed | Direct | High | P3, P4 |
| `DST-003` | Survival is the default standard mode; all-player death starts a 120-second world-reset timer | Confirmed | Direct | High | P5 |
| `DST-004` | Forest defaults support Autumn entry, ordinary seasons and omission of the separate Caves shard and events | Confirmed | Direct | High | P6 |
| `DST-005` | Default Autumn lasts 20 days, first Winter occupies days 21–35 and the next boundary enters Spring | Confirmed | Direct | High | P7 |
| `DST-006` | Hunger, temperature, darkness and sanity advance during live day-night and seasonal play | Confirmed | Direct | High | P7–P10 |
| `DST-007` | Gathering, known recipes, station proximity and personal prototyping connect raw materials to retained science access | Observation | Corroborated | High | P3, P8, P11, P12 |
| `DST-008` | Fires consume fuel and create local light and heat; complete darkness suppresses ordinary action and permits Charlie attacks | Confirmed | Direct | High | P9, P13 |
| `DST-009` | Food can be consumed, cooked or combined in a Crock Pot and ages toward spoilage over live time | Observation | Corroborated | High | P3, P12, P14 |
| `DST-010` | Death creates a ghost and drops inventory; a living partner can give a crafted Telltale Heart to revive the ghost with penalties | Confirmed | Direct | High | P5, P15 |
| `DST-011` | The interface exposes survival meters and warnings while explored map state remains partial and personal | Observation | Corroborated | High | P5, P8–P10, P16 |
| `DST-012` | The bounded puzzle is cooperative division of labour that converts a partial procedural map into a recoverable warm base before the first Winter closes | Observation | Corroborated | High | P1–P16, V1 |

## Basic data

- Release / origin: developed and published by Klei Entertainment; the official
  maintained product title is **Don't Starve Together**.
- Platform or physical form: networked survival game for PC and consoles; this
  record admits only the declared Windows PC stable build.
- Puzzle family: real-time system pressure; inventory and fixture dependencies;
  agent routing and coordination; ordered dependency sequencing.
- Primary and official sources:
  - **[P1]** [official Klei update `747465`](https://forums.kleientertainment.com/game-updates/dst/747465-r2783/),
    published 2026-08-13, for the current PC build boundary.
  - **[P2]** [official Don't Starve Together updates feed](https://kleiforums.com/rss/6-dont-starve-together-updates.xml/),
    for ordering the current PC build against later platform-specific updates.
  - **[P3]** [official Klei product page](https://www.klei.com/games/dont-starve-together),
    for cooperation, procedural biomes, gathering, crafting, structures,
    farming, combat and exploration.
  - **[P4]** [official Steam product record](https://store.steampowered.com/api/appdetails?appids=322330&l=english&cc=us),
    for the maintained title, developer, Windows form and first-party product
    description.
  - **[P5]** [official wiki game overview](https://dontstarve.wiki.gg/wiki/Don%27t_Starve_Together),
    for Survival's default status, hosted play, ghost state, revival and the
    all-dead reset.
  - **[P6]** [official wiki world customisation](https://dontstarve.wiki.gg/wiki/World_Customization_Don%27t_Starve_Together),
    for Forest defaults, explicit Autumn entry, disabled events and Caves as a
    separate optional shard.
  - **[P7]** [official wiki seasons reference](https://dontstarve.wiki.gg/wiki/Seasons),
    for default season lengths, first-Winter days, temperature, resources,
    daylight and the Spring boundary.
  - **[P8]** [official wiki Science Machine reference](https://dontstarve.wiki.gg/wiki/Science_Machine),
    for station proximity, tier-one prototyping and retained recipe knowledge.
  - **[P9]** [official wiki day-night cycle](https://dontstarve.wiki.gg/wiki/Day-Night_Cycle),
    for eight-minute days, segmented phases, darkness interaction and seasonal
    day-length changes.
  - **[P10]** [official wiki sanity reference](https://dontstarve.wiki.gg/wiki/Sanity),
    for visible sanity state, gains and losses, perception changes and hostile
    shadow thresholds.
  - **[P11]** [official wiki gathering reference](https://dontstarve.wiki.gg/wiki/Gathering),
    for hand and tool extraction of renewable Forest materials.
  - **[P12]** [official wiki crafting reference](https://dontstarve.wiki.gg/wiki/Crafting/Don%27t_Starve_Together),
    for recipe filters, ingredients, science tiers and personal outputs.
  - **[P13]** [official wiki freezing reference](https://dontstarve.wiki.gg/wiki/Freezing),
    for below-zero damage, warnings, fires, Thermal Stones and insulation.
  - **[P14]** [official wiki food reference](https://dontstarve.wiki.gg/wiki/Food),
    for eating, cooking, Crock Pot outputs and perishability.
  - **[P15]** [official wiki Telltale Heart reference](https://dontstarve.wiki.gg/wiki/Telltale_Heart),
    for recipe, 40-health cost, living-giver requirement and revival penalty.
  - **[P16]** [official wiki map reference](https://dontstarve.wiki.gg/wiki/Map),
    for personally explored terrain and mapped structures.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P16` under the declared server settings and exclusions; evidence-based
  rules reconstruction, not a direct-play claim.
- Claim IDs: `DST-001`–`DST-012`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: directly move one survivor through traversable Forest
  geometry.
- Existing `ACT-087`: feed compatible carried fuel to an existing fire.
- Existing `ACT-122`: gather, pick, chop, mine or dig a reachable world source.
- Existing `ACT-123`: craft one currently known legal personal recipe.
- Existing `ACT-161`: aim and strike one reachable hostile with the equipped
  ordinary weapon or tool.
- Existing `ACT-164`: select a carried tool, food or fuel stack as the active
  hand.
- Existing `ACT-165`: consume eligible food to restore hunger and apply its
  other declared effects.
- Existing `ACT-199`: pick up, transfer, store or equip compatible items.
- New `ACT-338`: position and place one crafted persistent survival fixture.
- New `ACT-339`: give a carried Telltale Heart to the partner's ghost.
- Parameters: survivor, partner, position, reach, source, tool, item, stack,
  recipe, fixture, fuel, food, hostile, ghost and recovery item.
- Claim IDs: `DST-002`, `DST-006`–`DST-012`.

### System Behaviour Genes

- Existing `SYS-215`: resolve directly commanded real-time combat against
  ordinary Forest hostiles.
- Existing `SYS-223`: reduce eligible tool durability and remove a broken tool.
- Existing `SYS-326`: generate and populate the shared seeded procedural Forest.
- Existing `SYS-327`: advance health, hunger and temperature exposure from
  environment, activity, food and equipment.
- Existing `SYS-329`: convert selected Crock Pot inputs through its live cycle.
- Existing `SYS-353`: consume ingredients and resolve eligible personal
  station-gated crafting.
- Existing `SYS-416`: advance day-night ecology and eligible local spawns.
- New `SYS-591`: yield materials and update or schedule resource-source return.
- New `SYS-592`: advance sanity and threshold-dependent shadow manifestation.
- New `SYS-593`: consume fire fuel into a local light/heat field and enforce
  complete-darkness danger.
- New `SYS-594`: expose station science tiers and persist first prototypes per
  survivor.
- New `SYS-595`: advance seasonal climate, resources and ecology.
- New `SYS-596`: convert death into ghost/drop state and settle revival or the
  all-dead reset.
- New `SYS-597`: age perishable food toward stale and spoiled states.
- Resolution order: generate the Forest and admit both survivors; advance the
  shared clock continuously; resolve movement, harvest, craft, placement,
  transfer and combat against current legality; debit survival meters, fuel,
  durability and food freshness; update light, heat, sanity, day/night,
  resource, creature and seasonal state; resolve individual death as a ghost
  that can be revived, or begin the all-dead reset; repeat until the declared
  Spring checkpoint or failure.
- Claim IDs: `DST-002`–`DST-012`.

### Constraint Genes

- Existing `CON-210`: item transfer is bounded by compatible stack and slot
  capacity.
- Existing `CON-281`: survival requires recoverable hunger, temperature, health,
  protection and durable equipment state.
- Existing `CON-366`: each craft requires all ingredients and any reachable
  station context.
- New `CON-496`: harvesting requires compatible source, reach, action and tool
  state.
- New `CON-497`: complete darkness requires a live local light source.
- New `CON-498`: science-tier recipes require nearby station authority until
  personally prototyped.
- New `CON-499`: fixture placement requires compatible unobstructed ground.
- New `CON-500`: Telltale Heart revival requires a living giver, paid recipe and
  a reachable other-player ghost.
- New `CON-501`: personal sanity thresholds gate shadow physicality and
  aggression.
- Scarce strategic resources: daylight, food freshness, grass, twigs, logs,
  rocks, flint, gold, fuel, fire radius, science access, inventory slots, tool
  durability, health, hunger, sanity, warmth, travel time and each partner's
  recoverable embodied state.
- Claim IDs: `DST-003`–`DST-012`.

### Information Genes

- Existing `INF-073`: hotbar, carried stacks and active equipment are visible.
- Existing `INF-075`: health, hunger and ordinary equipment condition are
  visible.
- Existing `INF-128`: nearby loot identity and storage/equipment compatibility
  are inspectable.
- Existing `INF-132`: recipe ingredients, science tier and prototype status are
  inspectable.
- Existing `INF-136`: calendar, weather cues, food freshness, reserves and base
  fixtures are inspectable.
- New `INF-240`: sanity, thermal/light warning and partner or ghost danger are
  exposed.
- New `INF-241`: each survivor retains only personally explored map geography.
- Claim IDs: `DST-004`–`DST-012`.

### Objective Genes

- New `OBJ-110`: keep both survivors alive and controllable through the first
  Winter and enter Spring together beside the declared viable shared base.
- Success, evaluation and failure: the transition is successful only when both
  survivors satisfy the life, location, warmth and infrastructure predicates at
  the first post-day-35 Spring boundary. A recoverable individual ghost is an
  interruption; all-player death that completes the Survival reset is failure.
  No victory screen or indefinite-survival claim is inferred.
- Claim IDs: `DST-003`–`DST-006`, `DST-012`.

### Time Genes

- Existing `TIM-003`: both players act in real time while clock, metabolism,
  fuel, food, ecology, combat and seasons continue to advance.
- Claim IDs: `DST-005`–`DST-012`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Private Survival server has default Forest settings, Autumn entry, no events and no Caves shard | Both players select Wilson and launch the new world | A seeded shared Forest is generated and both fresh survivors become controllable at the Florid Postern on day 1 | exact bounded entry | `DST-002`–`DST-004` |
| Nearby grass and saplings are unharvested | Split routes and pick compatible sources | Grass and Twigs enter the acting inventories and the local sources enter their harvested states | manual spatial input economy | `DST-007` |
| One survivor holds a usable Axe beside a tree | Chop until the source completes | Tool durability falls, Logs are yielded and the tree becomes a stump | target, tool and return state are coupled | `DST-007` |
| Recipe panel shows a known item with all ingredients | Craft the item | Ingredients are consumed and its output enters carried inventory or deployment state | known-recipe conversion | `DST-007` |
| Crafted Fire Pit deployment is selected near the shared camp | Position it on clear compatible ground and confirm | A persistent Fire Pit occupies that footprint and becomes addressable | craft and placement are distinct | `DST-007`, `DST-008` |
| The lit Fire Pit has a declining fuel reserve | Add compatible held fuel | Fuel reserve and light/heat duration rise; continued live time consumes them again | local protection is depleting | `DST-008` |
| Night is complete darkness and no live light covers a survivor | Remain outside illumination | Ordinary interaction is curtailed, sanity falls and Charlie can attack; reaching live light restores the protection relation | darkness is mechanical, not cosmetic | `DST-006`, `DST-008` |
| A Science Machine is placed and a personally unknown tier-one recipe is visible nearby | Craft its first copy in range | Inputs are consumed, the output is created, sanity is awarded and that survivor retains the prototype for remote later crafting | personal knowledge crosses a spatial gate | `DST-007` |
| Raw compatible foods occupy a Crock Pot | Start cooking and wait through its cycle | Inputs are replaced by the matched prepared dish, whose freshness then continues to age | food conversion and spoilage are separate | `DST-009` |
| Darkness, rain or monsters have lowered one survivor's sanity below the hostile threshold | Remain in that state near a shadow creature | Perception intensifies and the shadow creature becomes corporeal and aggressive for that survivor | internal threshold changes legal combat | `DST-006`, `DST-011` |
| One survivor's health reaches zero while the partner remains alive | Allow death to resolve | Eligible inventory drops and the dead player remains as a ghost that affects nearby sanity | individual death preserves cooperative presence | `DST-010` |
| Living survivor has paid 3 Cut Grass, 1 Spider Gland and 40 health to carry a Telltale Heart | Give it to the partner ghost | The heart is consumed and the partner returns alive with the declared health and maximum-health penalty | asymmetric cooperative recovery | `DST-010` |
| Both survivors are ghosts in Survival | Do not revive before 120 seconds elapse | The server resets the world and the bounded attempt fails | reproducible failure terminal | `DST-003`, `DST-010` |
| Autumn ends after day 20 | Continue live survival into day 21 | Winter begins; temperature, daylight, weather, resources and eligible ecology change | first climate challenge begins | `DST-005`, `DST-006` |
| Winter day 35 closes with both survivors alive at the declared warm base | Maintain light, warmth and embodied state through the clock boundary | The season indicator enters Spring and the analytical success predicate is satisfied | reproducible completion checkpoint | `DST-005`, `DST-012` |

## Strategic and experiential structure

- Local decision: gather one more distant source or turn back before dusk; spend
  fuel now or preserve it for colder night; eat, cook or store food before it
  spoils; prototype one recipe or reserve gold and logs; fight, flee or draw a
  hostile away from the shared work area.
- Medium-term planning: divide discovery and hauling, exchange map knowledge by
  rendezvous, establish fire and food before science, grow Science Machine into
  Alchemy Engine access, stockpile winter fuel and warmth and retain enough
  health/material slack to craft a Telltale Heart after one death.
- Long-term structure: convert two partial explorations into one shared resource
  and fixture network whose food, warmth, light, tools and recovery capacity
  remain viable as the calendar transforms Autumn abundance into Winter risk.
- Common heuristics: travel in daylight, carry emergency light and food, place
  central fixtures close enough to share heat and storage, prototype before
  leaving the station, cook perishables in useful batches, avoid both survivors
  taking the same lethal risk and preserve Spider Gland plus Cut Grass for
  revival.
- Failure attribution: visible meters, clock, recipes, inventory and local
  warnings explain immediate pressure, but undiscovered geography, sampled
  resources, weather and spawns keep exact plans uncertain; separately explored
  maps make communication and rendezvous part of the puzzle.
- Player-trust factors: the interface signals legal crafting, placement,
  temperature, sanity and darkness, but a first-Winter checkpoint must remain
  labelled as the Atlas's bounded analytical terminal rather than a claimed
  authored victory.
- Claim IDs: `DST-005`–`DST-012`.

## Replay and variation

- What changes between sessions: world seed, biome/resource layout, explored
  routes, weather, spawns, loot, damage, food state, task division, base site,
  prototype order, deaths, recoveries and material slack at the Spring boundary.
- Randomness or procedural generation: the Forest is generated from a seed and
  population/weather/encounter systems sample eligible outcomes; exact
  proprietary probabilities are not inferred.
- Multiple viable strategies: yes; players may specialise in scouting and base
  work, travel together for safety, centralise one camp or stage supplies, rely
  on clothing or Thermal Stones and favour traps, kiting or avoidance.
- Typical replay motive: improve early route sharing, base placement, science
  order, food/fuel reserve and cooperative recovery under a different Forest.
- Claim IDs: `DST-002`, `DST-005`–`DST-012`.

## Adjacent systems and history

- Direct predecessor: Don't Starve supplies the solitary survival kernel;
  Together makes generation, resource contention, labour and death recovery a
  concurrent shared-state problem.
- Variants: Relaxed, Endless, Wilderness and Lights Out alter death, reset,
  light or survival pressure; Caves add a second shard; characters, events and
  custom settings change the admitted mechanics and remain separate modules.
- Similar games: Minecraft, Terraria, Rust, Project Zomboid and Palworld.
- Important differences: unlike Minecraft, darkness itself can trigger a
  direct attacker and sanity changes entity hostility. Unlike Terraria, science
  proximity creates per-survivor retained prototype knowledge rather than only
  live station context. Unlike Rust, the bounded private packet centres
  cooperative seasonal preparation and ghost revival rather than persistent
  player-versus-player territory. Unlike Project Zomboid, a dead participant
  remains an active ghost whom the living partner can restore.
- Claim IDs: `DST-002`–`DST-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-087`, `ACT-122`, `ACT-123`, `ACT-161`, `ACT-164`, `ACT-165`, `ACT-199`, `ACT-338`, `ACT-339` | move, fuel, harvest, craft, fight, select, eat, transfer, place and revive parameters |
| System Behaviour | `SYS-215`, `SYS-223`, `SYS-326`, `SYS-327`, `SYS-329`, `SYS-353`, `SYS-416`, `SYS-591`–`SYS-597` | combat, wear, world, survival, cooking, craft, clock, resources, sanity, light, science, season, death and perishability |
| Constraint | `CON-210`, `CON-281`, `CON-366`, `CON-496`–`CON-501` | slots, survival, recipes, harvest, darkness, science, placement, revival and sanity parameters |
| Information | `INF-073`, `INF-075`, `INF-128`, `INF-132`, `INF-136`, `INF-240`, `INF-241` | inventory, meters, loot, recipe, calendar, danger and map observations |
| Objective | `OBJ-110` | two living survivors, warm shared base and Spring transition |
| Time | `TIM-003` | concurrent players and continuously advancing survival world |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `185` (`GAME-0001`–`GAME-0185`).
- Exact genome matches: none.
- Tied near matches: `GAME-0141` — Rust (`19 / 74 = 0.256757`).
- Supported combination subsets: `COMB-0184`.
- Scan date: 2026-08-29.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0141` — Rust | `ACT-008`, `ACT-122`, `ACT-123`, `ACT-161`, `ACT-164`, `ACT-165`, `ACT-199`, `SYS-215`, `SYS-223`, `SYS-326`, `SYS-327`, `SYS-329`, `CON-210`, `CON-281`, `INF-073`, `INF-075`, `INF-128`, `INF-132`, `TIM-003` | both generate a real-time survival world whose embodied player gathers, crafts, fights and maintains metabolism through finite inventory and durable tools, but DST adds cooperative personal science, sanity-made threats, depleting local darkness protection, perishable food, a fixed seasonal checkpoint and living-to-ghost recovery instead of Rust's ordinary respawn, workbench queue, building territory and PvP persistence | Near, `0.256757` |

### Preserved research notes

- New genes: `ACT-338`–`ACT-339`, `SYS-591`–`SYS-597`, `CON-496`–`CON-501`,
  `INF-240`–`INF-241` and `OBJ-110`.
- Classification result: `New gene` and new verified interaction combination.
- Evidence and reasoning: embodied movement, inventory, gathering, crafting,
  combat, procedural generation and real-time survival reuse safely; sanity
  manifestation, depleting local darkness protection, retained personal
  science, coupled seasons and cooperative ghost recovery require new genes.

## Combination status

- `COMB-0184` is a verified strict thirty-gene subset of the forty-two-gene
  genome, coupling shared resource acquisition, science, fixtures, food, light,
  sanity, season and revival to the first-Winter cooperative terminal.
- Every earlier verified combination is tested deterministically after
  registration.

## Taxonomy impact

- Registry changes: eighteen new Active genes, links on twenty-four reused
  genes, `COMB-0184` and four existing family memberships.
- Taxonomy-change record: none; no prior lifecycle, definition or reviewed game
  signature changes.
- Candidate terms affected: survival fixture placement, ghost-item recovery,
  renewable harvesting, sanity manifestation, fuelled darkness protection,
  personal science prototypes, seasonal ecology, ghost/reset state, food
  perishability, target/tool harvesting, light requirement, placement ground,
  revival roles, shadow threshold, survival danger HUD, personal explored map
  and bounded first-Winter terminal.

## Negative results

- `SYS-216` is not reused: it respawns an ordinary avatar into the same world,
  while Survival mode first retains a ghost and can reset the entire world if
  every participant remains dead.
- `SYS-224` and `SYS-225` are not reused: Frostpunk consumes city-wide coal and
  computes building heat, while this packet uses embodied local fire fields and
  survivor temperature.
- `SYS-328` is not reused: ordinary scoped crafting resolves immediately rather
  than through Rust's timed cancellable personal queue.
- `INF-133` is not reused: Project Zomboid moodles aggregate graded conditions,
  while the present packet exposes distinct health, hunger, sanity, thermal and
  darkness state with a sanity-gated entity consequence.
- Caves, bosses, quests, boats, farms, magic, special character kits, events and
  later seasons are not admitted simply because the open-ended live client
  contains them.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Current PC build `747465` supports a default
  two-player Survival Forest whose first Winter follows a 20-day Autumn and
  whose death rules preserve ghosts before a timed all-dead reset
  (`DST-001`–`DST-012`).

## Нові гени

- [Observation | Corroborated | High] Added eighteen genes for fixture placement,
  partner revival, renewable harvesting, sanity, fuelled light/heat, persistent
  prototyping, seasons, ghost/reset state, food spoilage, associated gates and
  the explicit first-Winter cooperative terminal.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0184` isolates cooperative resource,
  science, base, food, light, sanity and revival preparation through the first
  Winter-to-Spring transition.

## Зміни таксономії

- [Observation | Corroborated | High] No lifecycle migration or reviewed-game
  signature change; twenty-four established generic genes remain unchanged.

## Нові питання

- Which later cooperative survival game retains asymmetric partner recovery
  while replacing sanity-gated entities or a fixed seasonal preparation cycle?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0187` — Team Fortress 2.
- Optimisation criterion: continue the recorded demand-led Goal in exact order.
- Expected information gain: replace open procedural cooperation with a bounded
  authored two-team class shooter and objective-mode terminal.
- Backlog impact: seventh of nine authorised game units.

## Чому саме вона

- [Confirmed | Direct | High] It is the next immutable subject in
  `SEARCH_DEMAND_GAME_SELECTION_006`.

## Localisation status

- Ukrainian game, new-gene and combination entries are reviewed in this unit.
- The canonical brand title remains `Don't Starve Together`; the explanatory
  Ukrainian title is presentation-only.

## Open questions

- Recheck the current PC build, default world settings, event toggle and
  first-Winter day boundary before later review-on-touch; keep the Spring
  checkpoint labelled as an analytical terminal rather than authored victory.
