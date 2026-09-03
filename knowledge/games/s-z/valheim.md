---
game_id: GAME-0197
slug: valheim
game_title: Valheim
analysis_status: reviewed
reviewed: 2026-08-30
combination_ids:
  - COMB-0195
gene_ids:
  action:
    - ACT-008
    - ACT-087
    - ACT-122
    - ACT-123
    - ACT-161
    - ACT-164
    - ACT-199
    - ACT-204
    - ACT-223
    - ACT-353
    - ACT-354
  system:
    - SYS-215
    - SYS-216
    - SYS-222
    - SYS-223
    - SYS-326
    - SYS-330
    - SYS-342
    - SYS-353
    - SYS-416
    - SYS-591
    - SYS-632
    - SYS-633
    - SYS-634
    - SYS-635
    - SYS-636
  constraint:
    - CON-136
    - CON-210
    - CON-292
    - CON-297
    - CON-354
    - CON-517
    - CON-518
  information:
    - INF-073
    - INF-075
    - INF-128
    - INF-131
    - INF-132
    - INF-142
    - INF-241
  objective:
    - OBJ-120
  time:
    - TIM-003
---

# Game: Valheim

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current stable unmodded Windows Steam Early Access
  `0.221.12`, public build `21981559`, checked 2026-08-30; one fresh character
  in one fresh solo world with seed `PGA0197`, preset **Normal** and every world
  modifier at its preset value. The announced 1.0 release on 2026-09-09 and the
  later save-system Public Test build are not current rules.
- Reproducible start packet: create the character and world, retain the default
  map, portals, raids, death penalty and resource/combat settings, then begin at
  first player control after the Valkyrie drop beside the central Sacrificial
  Stones. Interact with the adjacent Eikthyr Vegvisir to mark the nearest legal
  altar. The exact sampled terrain, resource nodes, wildlife, trophy drops and
  altar coordinates are seed-and-build parameters.
- Primary decision loop: explore the marked Meadows; harvest wood, stone,
  flint, food and hides; place a supported roofed shelter, campfire and covered
  Workbench; craft and repair a legal early loadout; keep up to three distinct
  foods active; hunt deer until two Deer Trophies exist; reach the marked altar;
  offer both trophies; read and evade Eikthyr's telegraphed attacks; defeat it;
  collect the guaranteed Eikthyr Trophy; return to the Sacrificial Stones and
  mount that trophy on Eikthyr's stone.
- Entry and exit: the unit begins at retained control by the Sacrificial Stones.
  Boss defeat alone is non-terminal. It succeeds only when the Eikthyr Trophy
  is mounted on its matching sacrificial stone and the Eikthyr Forsaken Power
  becomes selectable/available. Death, an unfinished summon and owning the
  trophy without mounting it are recoverable non-completion states.
- Included: seeded procedural Meadows geography; personal map and Eikthyr
  marker; movement, sprint and jump; contact pickup and bounded stacks/slots;
  manual resource harvesting and tool durability; known-recipe crafting and
  covered Workbench use/repair; supported wood shelter pieces, roof, fire,
  shelter/comfort, Resting and Rested; three distinct active-food slots and
  decaying health/stamina/regeneration bounds; early melee/ranged combat,
  blocking, perfect block, dodge and skill gain; default death skill loss,
  gravestone recovery, No Skill Drain and Corpse Run; day/night ecology; exact
  two-trophy summon; Eikthyr combat, guaranteed trophy drop and trophy mounting.
- Excluded: multiplayer, PvP and servers; altered world modifiers; another
  seed, character, world or cross-world item transfer; mods, devcommands,
  cheats and Public Test; the unreleased 1.0 rules; Black Forest and every later
  biome/Forsaken; mining or pickaxe progression after the hard-antler drop;
  portals, boats, farming, taming, raids, broad base expansion, exhaustive
  recipes/equipment and any post-power survival objective.
- Potential scoped modules: first Black Forest mining/smelting chain; one raid
  defence; portal logistics; sailing; farming/taming; multiplayer authority; or
  a later Forsaken. Each needs a separate entry, state packet and terminal.
- Direct-play status: no authenticated current Steam playthrough was conducted.
  Official product, FAQ, patch and server-modifier evidence establishes the
  live boundary and core loop. Versioned community mechanics references make
  the exact Eikthyr, food, rest and death transitions reproducible. This is an
  evidence-based rules trace, not captured direct play.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `VLH-001` | Windows Steam Early Access 0.221.12 / build 21981559 is the current stable reviewed public ruleset | Confirmed | Corroborated | High | P1, P2, S1 |
| `VLH-002` | A seed and build generate a persistent survival world of biomes, resources and creatures, while Normal preserves the documented default modifier packet | Confirmed | Corroborated | High | P2, P3, P4, S2 |
| `VLH-003` | The spawn Vegvisir marks the nearest Eikthyr altar on the personal map, converting a fixed world interaction into a seed-resolved route | Observation | Corroborated | High | P3, S3, S4 |
| `VLH-004` | Harvesting, pickup, bounded inventory, recipes, crafting and durability form the Meadows production loop | Observation | Corroborated | High | P2, P3, S5, S6 |
| `VLH-005` | A usable Workbench needs roof and sufficient cover; shelter plus fire permits Resting and then a comfort-scaled Rested effect | Confirmed | Corroborated | High | P3, S7–S9 |
| `VLH-006` | Up to three distinct active foods temporarily set and decay maximum health, stamina and regeneration parameters | Confirmed | Corroborated | High | P3, S10 |
| `VLH-007` | Combat continuously resolves stamina-bound attacks, blocks, perfect responses, dodges, damage and activity-specific skill gain | Observation | Corroborated | High | P1, P5, S11, S12 |
| `VLH-008` | Ordinary death respawns the character, leaves carried state in a gravestone, applies the default skill penalty and grants bounded recovery protections | Confirmed | Corroborated | High | P3, S13, S14 |
| `VLH-009` | Eikthyr's matching altar accepts exactly two Deer Trophies and then instantiates the boss encounter | Confirmed | Corroborated | High | S3, S15 |
| `VLH-010` | Eikthyr telegraphs three attack patterns and its defeat guarantees one Eikthyr Trophy plus three Hard Antlers | Confirmed | Corroborated | High | P5, S3, S15 |
| `VLH-011` | Mounting the Eikthyr Trophy on its matching Sacrificial Stone unlocks the selectable Eikthyr Forsaken Power | Confirmed | Corroborated | High | P5, S3, S16 |
| `VLH-012` | Trophy mounting, rather than boss defeat or hard-antler ownership, is the bounded first-biome terminal | Observation | Corroborated | High | P3, P5, S3, S16, V1 |

## Basic data

- Release / origin: developed by Iron Gate Studio and published by Coffee Stain
  Publishing; Steam Early Access began in 2021 and the reviewed stable patch
  shipped on 19 February 2026.
- Platform or physical form: third-person real-time survival, construction and
  boss progression; scoped to one Windows Steam solo world.
- Puzzle family: real-time system pressure; inventory and fixture dependencies;
  world topology and perspective; ordered dependency sequencing.
- Primary and official sources:
  - **[P1]** [official Valheim Steam page](https://store.steampowered.com/app/892970/Valheim/),
    for the procedural survival world, building, crafting and combat envelope.
  - **[P2]** [official patch 0.221.12](https://www.valheimgame.com/news/patch-0-221-12/),
    for the current stable 2026-02-19 version boundary.
  - **[P3]** [official FAQ](https://www.valheimgame.com/faq/), for solo/co-op,
    procedural biomes, gathering, building, crafting, food-dependent
    health/stamina and biome-by-biome Forsaken progression.
  - **[P4]** [official dedicated-server and world-modifier guide](https://www.valheimgame.com/support/a-guide-to-dedicated-servers/),
    for the Normal preset and separately configurable world modifiers; server
    operation itself remains excluded.
  - **[P5]** [official Call to Arms stable update](https://steamcommunity.com/ogg/892970/announcements/detail/529856925490219059),
    for current Forsaken powers, Eikthyr's stamina effect and Perfect Block /
    Perfect Dodge mechanics retained by the reviewed build.
  - **[P6]** [official 1.0 FAQ](https://www.valheimgame.com/support/valheim-1-0-faq/)
    and [release-date announcement](https://www.valheimgame.com/news/valheim-has-a-release-date/),
    used only to exclude the announced 2026-09-09 release from this unit.
- Reproducible mechanics sources:
  - **[S1]** [public Steam app-info metadata](https://api.steamcmd.net/v1/info/892970),
    for public build `21981559` and its timestamp only.
  - **[S2]** [world seeds](https://valheim.fandom.com/wiki/World_seed), for
    version-and-seed world reproducibility.
  - **[S3]** [Eikthyr](https://valheim.gamecore.wiki/en/creatures/eikthyr/), for
    Vegvisir routing, altar cost, attacks, drops and trophy settlement.
  - **[S4]** [runestones and Vegvisir](https://valheim.fandom.com/wiki/Runestone),
    for the spawn-stone Eikthyr wayfinder and nearest-boss marker.
  - **[S5]** [Workbench](https://valheim.gamecore.wiki/en/buildings/workbench/),
    for crafting, free repairs, build radius and roof/cover requirements.
  - **[S6]** [resource harvesting](https://valheim.gamecore.wiki/en/game_mechanics/resource_gathering/),
    for manual gather/drop/pickup transitions.
  - **[S7]** [shelter](https://valheim.fandom.com/wiki/Shelter), **[S8]**
    [Rested](https://valheim.gamecore.wiki/en/game_mechanics/rested/) and
    **[S9]** [comfort](https://valheim.gamecore.wiki/en/game_mechanics/comfort/),
    for the sheltered-fire Resting predicate and timed Rested benefit.
  - **[S10]** [food](https://valheim.fandom.com/wiki/Food), for three distinct
    active foods and decaying health/stamina/regeneration contributions.
  - **[S11]** [blocking](https://valheim.fandom.com/wiki/Blocking) and **[S12]**
    [damage mechanics](https://valheim.fandom.com/wiki/Damage_mechanics), for
    stamina, block/parry, dodge and damage resolution.
  - **[S13]** [death](https://valheim.gamecore.wiki/en/game_mechanics/death/) and
    **[S14]** [Corpse Run](https://valheim.gamecore.wiki/en/game_mechanics/corpse-run/),
    for gravestone, skill loss, No Skill Drain and recovery aid.
  - **[S15]** [trophies](https://valheim.gamecore.wiki/en/items/trophies/), for
    Deer Trophy chance, exact offering and guaranteed Eikthyr Trophy.
  - **[S16]** [Forsaken powers](https://valheim.gamecore.wiki/en/game_mechanics/forsaken-power/),
    for matching-stone trophy mounting, selection and activation.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P6` and `S1`–`S16`; rules reasoning, not a direct-play claim.
- Claim IDs: `VLH-001`–`VLH-012`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`, navigate, sprint and jump; `ACT-087`, apply matching
  trophies to altar/stone fixtures; `ACT-122`, harvest a world resource;
  `ACT-123`, craft a known recipe; `ACT-161`, directly strike or shoot;
  `ACT-164`, select the active quick slot; `ACT-199`, transfer/equip world or
  gravestone loot; `ACT-204`, place or repair connected shelter blocks; and
  `ACT-223`, time a dodge or perfect block/parry response.
- New `ACT-353`: consume one distinct food into an available timed food slot.
- New `ACT-354`: read an addressed Vegvisir to reveal its nearest Forsaken altar.
- Parameters: movement, target, tool, recipe, build piece, support, quick slot,
  food, food slot, attack, block/dodge timing, fixture, trophy and quantity.
- Claim IDs: `VLH-003`–`VLH-011`.

### System Behaviour Genes

- Existing `SYS-215`, direct live combat; `SYS-216`, death loss, respawn and
  recovery; `SYS-222`, contact pickup; `SYS-223`, durability; `SYS-326`, seeded
  procedural survival-world generation; `SYS-330`, connected building support,
  health and stability; `SYS-342`, activity-specific skills; `SYS-353`,
  station-gated crafting; `SYS-416`, day/night ecology; and `SYS-591`, manual
  harvesting and resource return.
- New `SYS-632`: convert the active food set into decaying health, stamina and
  regeneration bounds. New `SYS-633`: evaluate shelter, fire and comfort into
  Resting/Rested state and covered-station availability. New `SYS-634`: map the
  nearest matching Forsaken altar after a Vegvisir interaction. New `SYS-635`:
  consume the legal altar offering, instantiate Eikthyr and settle guaranteed
  defeat drops. New `SYS-636`: mount a matching Forsaken trophy and unlock its
  selectable power.
- Resolution order: generate the seed; reveal Eikthyr's altar; gather, place,
  craft and prepare; continuously update food/rest/skills/ecology; consume two
  Deer Trophies at the altar; resolve live Eikthyr combat; on defeat expose its
  guaranteed drops; mount the matching trophy; persist power availability.
- Parameters: seed, biome, spawn table, resource/drop roll, shelter/cover,
  comfort, food set and decay, stamina, skill, altar, offering, boss state,
  guaranteed drops, sacrificial stone and power.
- Claim IDs: `VLH-002`–`VLH-011`.

### Constraint Genes

- Existing `CON-136`, persistent prerequisite-gated progression; `CON-210`,
  typed stacks/slots; `CON-292`, legal supported building geometry; `CON-297`,
  recipe ingredients, knowledge and station context; and `CON-354`, stamina,
  equipment-maintenance and animation-recovery legality for combat responses.
- New `CON-517`: active food slots accept only distinct foods whose digestion
  state permits replacement or refresh. New `CON-518`: a Forsaken altar or
  Sacrificial Stone accepts only its matching trophy type, required count and
  current progression state.
- Scarce strategic resources: daylight and safe preparation time, stamina,
  three food slots and remaining durations, health, rested duration, inventory
  slots, tool durability, wood/flint/hides, arrows, Deer Trophy drops and
  recoverable skill progress after death.
- Claim IDs: `VLH-003`–`VLH-011`.

### Information Genes

- Existing `INF-073`, active hotbar/equipment; `INF-075`, health, stamina,
  active-food and durability state; `INF-128`, visible loot and capacity;
  `INF-131`, build legality/support/cover and station operation feedback;
  `INF-132`, recipe dependencies; `INF-142`, Eikthyr motion/sound cues for
  response timing; and `INF-241`, retained personal map geography and marker.
- Parameters: health, stamina, foods/durations, Rested state, hotbar, durability,
  pickup, capacity, build preview, shelter/cover, recipe, map, marker, boss bar,
  animation, sound, trophy prompt and power availability.
- Claim IDs: `VLH-003`–`VLH-011`.

### Objective Genes

- New `OBJ-120`: defeat Eikthyr, recover its guaranteed trophy and mount it on
  the matching Sacrificial Stone to unlock the first Forsaken Power.
- Success, evaluation and failure: mounted-trophy power availability is the
  positive terminal. Boss defeat, hard-antler pickup or possession of the
  unmounted trophy remains incomplete. Death is a recoverable penalty state;
  lost/unrecovered equipment, repeated defeat or an unfinished summon does not
  create a second authored ending.
- Claim IDs: `VLH-008`–`VLH-012`.

### Time Genes

- Existing `TIM-003`: movement, harvesting, food decay, Resting, day/night
  ecology, combat, skill gain and boss behaviour advance in continuous time
  while the player can act. Pausing/menu/server-time variants are outside the
  declared solo packet.
- Claim IDs: `VLH-004`–`VLH-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh seed `PGA0197` begins at the Sacrificial Stones | Read the adjacent Eikthyr Vegvisir | The personal map retains the nearest generated Eikthyr altar marker | authored wayfinder bridges seed variation | `VLH-002`, `VLH-003` |
| Reachable Meadows resource is intact | Strike or collect it with a compatible action/tool | The entity yields its sampled or declared drops; eligible contact transfers them subject to stacks/slots and durability | embodied production has world, tool and capacity costs | `VLH-004` |
| Wood and a Hammer are available on legal ground | Place connected floor/wall/roof pieces, fire and Workbench | Supported blocks persist; shelter/fire admit Resting while enough roof/cover makes the Workbench operational | construction changes both space and fixture legality | `VLH-005` |
| Character owns recipe inputs near a covered Workbench | Craft/repair a legal early weapon, armour or bow | Inputs become known output; eligible worn equipment repairs without resource cost | station context transforms preparedness | `VLH-004`, `VLH-005` |
| Fewer than three food slots contain distinct foods | Consume a different Meadows food | Its timed contribution joins the active set and current max health/stamina/regeneration bounds update then decay | food is a temporary build, not a hunger-death meter | `VLH-006` |
| Character is sheltered beside fire | Remain Resting for the required interval | Rested begins with duration derived from comfort and temporarily improves recovery/experience | base geometry converts waiting into combat capacity | `VLH-005` |
| Two Deer Trophies have been recovered and the marked altar is reached | Apply both trophies to Eikthyr's altar | Exactly the legal offering is consumed and Eikthyr is instantiated | stochastic hunting feeds a deterministic boss entry | `VLH-009` |
| Eikthyr telegraphs a melee, lightning or area attack | Block/parry, dodge or reposition, then counterattack | Timing, stamina, defence and damage settle the exchange while skill experience advances | readable live counterplay determines survival | `VLH-007`, `VLH-010` |
| Character dies with carried state | Respawn, revisit the gravestone and recover legal contents | The world/boss state continues; default skill loss applies, carried state remains recoverable and bounded recovery protections activate | death is costly but non-terminal | `VLH-008` |
| Eikthyr reaches zero health | Pick up the resulting loot | One Eikthyr Trophy and three Hard Antlers are guaranteed, subject to inventory transfer | boss defeat creates the terminal key but is not terminal | `VLH-010`, `VLH-012` |
| Eikthyr Trophy is carried at the Sacrificial Stones | Apply it to Eikthyr's matching stone | The mounted trophy persists and Eikthyr's Forsaken Power becomes selectable/available | first-biome progression closes at explicit settlement | `VLH-011`, `VLH-012` |

## Strategic and experiential structure

- Local decision: choose a resource, food, quick slot, attack window, block,
  dodge, retreat, building support or recovery route from visible state.
- Medium-term planning: turn the sampled Meadows into a covered repair/crafting
  base and a sustainable food/rest/loadout packet before spending two trophies
  on an unavoidable live boss.
- Long-term structure: convert exploration into an altar marker, resources into
  preparedness, stochastic deer drops into a deterministic summon, boss defeat
  into a matching trophy and that trophy into retained power availability.
- Common heuristics: mark the altar first; establish a covered Workbench; keep
  three complementary foods and Rested active; repair before departure; use
  open terrain and read antler/lightning cues; retrieve the gravestone before
  rebuilding; return the trophy to spawn instead of stopping at the kill.
- Failure attribution: inventory/recipe/build prompts separate missing inputs,
  cover and support; food/stamina/rest indicators explain capacity; map marker
  explains route; boss cues distinguish mistiming; gravestone and skill states
  explain death cost; matching-stone feedback distinguishes unmounted progress.
- Player-trust factors: one recorded seed and preset pin the world packet;
  exact offerings and guaranteed boss drops separate random preparation from
  deterministic settlement; the final mounted trophy remains visibly inspectable.
- Claim IDs: `VLH-002`–`VLH-012`.

## Replay and variation

- What changes between sessions: terrain/resource/wildlife placement, deer
  trophy rolls, marked altar position, day count, food/loadout choice, route,
  deaths and recovery history.
- Randomness or procedural generation: seed plus version fixes geography;
  runtime spawn/drop rolls remain sampled. The fixed seed does not assert a
  fixed attempt time or gear list.
- Multiple viable strategies: spear, axe, club or bow emphasis; shield/parry or
  dodge-heavy defence; compact or larger shelter; different three-food sets and
  routes can all satisfy the same altar/trophy terminal.
- Typical replay motive: faster preparation, fewer deaths, another seed or a
  different weapon/food plan. Later-biome progression is outside this unit.
- Claim IDs: `VLH-002`–`VLH-012`.

## Adjacent systems and history

- Direct predecessors: prior Valheim patches establish Early Access history,
  but only stable 0.221.12 and current Call to Arms mechanics are canonical here.
- Variants: multiplayer changes authority and recovery; world modifiers change
  combat, death, raids, portals and resources; later Forsaken add production,
  traversal and boss rules. None is merged into this solo Normal packet.
- Similar games: Minecraft shares procedural gathering, crafting, inventory,
  construction, death recovery and a boss-gated survival route. Terraria adds
  mutable tile topology, housing/NPC admission and night-gated Eye combat.
  Don't Starve Together shares food/rest-like preparation, station crafting and
  day/night survival, but its scoped multiplayer Ancient Fuelweaver packet has
  sanity, seasons and cooperative authority. Rust shares procedural production,
  connected construction and death recovery but is bounded by adversarial
  persistent-server survival and wipe rather than a trophy-power settlement.
- Important differences: Valheim's three-food temporary stat build, covered
  Workbench/rest preparation, authored Vegvisir-to-generated-altar mapping,
  exact trophy summon, guaranteed boss trophy and matching-stone power unlock
  make the dependency chain distinct from open-ended survival stopping points.
- Claim IDs: `VLH-002`–`VLH-012`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-087`, `ACT-122`, `ACT-123`, `ACT-161`, `ACT-164`, `ACT-199`, `ACT-204`, `ACT-223`, `ACT-353`, `ACT-354` | targets, tools, foods, fixtures and bindings are parameters |
| System Behaviour | `SYS-215`, `SYS-216`, `SYS-222`, `SYS-223`, `SYS-326`, `SYS-330`, `SYS-342`, `SYS-353`, `SYS-416`, `SYS-591`, `SYS-632`–`SYS-636` | seed, rolls, shelter, boss and power values are parameters |
| Constraint | `CON-136`, `CON-210`, `CON-292`, `CON-297`, `CON-354`, `CON-517`, `CON-518` | support, slots, stamina, food and trophy requirements are parameters |
| Information | `INF-073`, `INF-075`, `INF-128`, `INF-131`, `INF-132`, `INF-142`, `INF-241` | HUD layout, map position and cue presentation are parameters |
| Objective | `OBJ-120` | Eikthyr identity is the scoped first-Forsaken parameter |
| Time | `TIM-003` | continuous solo-world time only |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `196` (`GAME-0001`–`GAME-0196`).
- Exact genome matches: none.
- Tied near matches: `GAME-0186` — Don’t Starve Together (`20 / 64 = 0.312500`).
- Supported combination subsets: `COMB-0195`.
- Scan date: 2026-08-30.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0186` — Don’t Starve Together | navigate, harvest, craft, fight, equip and build in a procedural survival world with bounded inventory, durability, station-gated production, day/night ecology, direct combat, recoverable death and continuously changing personal state | Valheim is a solo Normal seed whose three distinct foods configure health/stamina, shelter and fire yield Rested/covered-Workbench operation, one Vegvisir selects the nearest generated altar, two trophies summon Eikthyr and a guaranteed boss trophy must settle at a separate stone; the scoped DST packet instead coordinates two players through hunger/sanity/temperature, seasons, science prototyping, ghosts and an Ancient Fuelweaver checkpoint | Near, `0.312500` |

### Preserved research notes

- New genes: `ACT-353`, `ACT-354`, `SYS-632`–`SYS-636`, `CON-517`,
  `CON-518` and `OBJ-120`.
- Classification result: bounded new genes plus reuse and one new combination.
- Evidence and reasoning: the corpus already owns navigation, harvesting,
  inventory, crafting, construction, durability, live combat, reactive timing,
  skills, death recovery, day/night ecology and persistent maps. New boundaries
  isolate only the three-food build, cover/rest conversion, authored wayfinder,
  Eikthyr offering/drop lifecycle and trophy-to-power terminal.

## Taxonomy impact

- Registry changes: forty-two Active genes and `COMB-0195`; four existing
  definitions receive evidence-preserving generalisation without signature changes.
- Taxonomy-change record: none; no existing definition is deprecated, merged or split.
- Candidate terms affected: active food set, sheltered Rested conversion,
  Forsaken wayfinder, boss offering/drop settlement and trophy-power unlock.

## Negative results

- `ACT-165` and `SYS-327` are not reused: Valheim food does not prevent a
  hunger/starvation terminal; three timed foods instead configure decaying
  health, stamina and regeneration bounds.
- `SYS-213` and tile placement/break genes are not reused: terrain is not a
  Terraria/Minecraft mutable tile lattice in this packet; connected building
  pieces alter traversability above generated terrain.
- Rust privilege, lock, upkeep, raid, offline-time and wipe genes remain absent:
  one solo local world has no contested authority or scheduled reset terminal.
- Boss defeat alone is rejected as the endpoint because the guaranteed trophy
  still must be returned and mounted before the first Forsaken Power exists.
- Hard Antlers and pickaxe crafting are outputs/possible continuation, not a
  silent Black Forest extension.
