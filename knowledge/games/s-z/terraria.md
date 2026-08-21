---
game_id: GAME-0153
slug: terraria
game_title: Terraria
analysis_status: reviewed
reviewed: 2026-08-21
combination_ids:
  - COMB-0151
gene_ids:
  action:
    - ACT-008
    - ACT-040
    - ACT-123
    - ACT-130
    - ACT-131
    - ACT-159
    - ACT-161
    - ACT-162
    - ACT-164
  system:
    - SYS-004
    - SYS-212
    - SYS-213
    - SYS-215
    - SYS-216
    - SYS-217
    - SYS-222
    - SYS-353
    - SYS-416
    - SYS-417
    - SYS-418
    - SYS-419
    - SYS-420
  constraint:
    - CON-206
    - CON-208
    - CON-210
    - CON-366
    - CON-367
    - CON-368
    - CON-369
    - CON-370
  information:
    - INF-073
    - INF-119
    - INF-128
    - INF-132
    - INF-163
    - INF-164
    - INF-165
  objective:
    - OBJ-083
  time:
    - TIM-003
---

# Game: Terraria

## Analysis scope

- Version / ruleset: Desktop `1.4.5.6`, single-player, one new Classic
  character in one new small Classic world with random Corruption/Crimson and
  no special world seeds. The route starts at character/world creation and ends
  after the first Eye of Cthulhu defeat and the eligible Dryad's arrival in a
  prepared vacant valid house.
- Included: seeded finite world generation; movement; hotbar and equipment;
  reachable mining and tile/wall/furniture placement; item drops, pickup,
  storage and stack limits; 1.4.5 immediate crafting and nearby-station/chest
  context; town housing and milestone-gated NPC arrival; purchases; Life
  Crystals; healing and Potion Sickness; real-time combat; Classic coin loss and
  respawn; explored minimap; day/night ecology; manual or natural Eye entry,
  two-phase combat, dawn escape and post-boss Dryad eligibility.
- Excluded: Journey, Expert, Master, Mediumcore and Hardcore; multiplayer;
  secret or combined seeds; cross-world character transfer; King Slime and all
  later bosses, biomes and progression; Hardmode; fishing, wiring, pylons,
  invasions, exhaustive recipes, equipment, NPC happiness and bestiary completion.
- Direct-play status: not conducted. The official Terraria Wiki's current
  versioned rules, source-derived mechanics and reproducible guides establish
  the scoped transitions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `TRR-001` | Desktop 1.4.5.6 is the scoped current version and a seed determines a finite Classic world's terrain, layers, biomes, ores and structures | Confirmed | Corroborated | High | P1, P2, P3 |
| `TRR-002` | The character directly moves, selects a hotbar item, mines reachable mutable tiles with compatible tools and places carried blocks, walls or furniture into legal supported cells | Confirmed | Corroborated | High | P4, P5, P6 |
| `TRR-003` | The 1.4.5 crafting window exposes recipes supported by eligible inventories and nearby stations; commitment consumes inputs and immediately emits output rather than scheduling a timed queue | Confirmed | Corroborated | High | P7, P8 |
| `TRR-004` | Inventory slots and stacks bound pickup; armour/accessory placement changes the active build; Classic death drops half the carried coins and respawns the character while the world persists | Confirmed | Corroborated | High | P9, P10, P11 |
| `TRR-005` | A valid town house requires an accepted enclosed safe-walled area, furniture and a home tile; eligible NPCs need vacant valid housing and their own persistent milestone | Confirmed | Corroborated | High | P12, P13, P14 |
| `TRR-006` | Life Crystals permanently increase maximum health by 20 up to 400, while healing-item use creates Potion Sickness that temporarily blocks another healing item | Confirmed | Direct | High | P15, P16, P17 |
| `TRR-007` | The real-time day/night cycle changes local surface populations, and nocturnal enemies leave at dawn | Confirmed | Corroborated | High | P18, P19 |
| `TRR-008` | The Eye can be manually summoned only at night or naturally enter after its predicates; it changes behaviour below its health threshold and escapes at dawn if not defeated | Confirmed | Corroborated | High | P18, P20 |
| `TRR-009` | First defeat of an eligible boss sets Dryad admission eligibility, but her actual arrival still needs vacant valid housing | Confirmed | Corroborated | High | P13, P21 |
| `TRR-010` | The character-bound minimap retains explored lit terrain, visible mutations and spawn, NPC, boss and latest-death icons | Confirmed | Corroborated | High | P22 |

## Basic data

- Release / origin: Re-Logic; Terraria first released in 2011 and Desktop
  `1.4.5.6` shipped on 9 March 2026 as the current reviewed hotfix.
- Platform or physical form: side-view real-time mutable-tile exploration,
  construction, crafting and combat sandbox.
- Puzzle family: real-time system pressure; world topology and perspective;
  inventory and fixture dependencies; ordered dependency sequencing.
- Primary and reproducible sources:
  - **[P1]** [Desktop version history](https://terraria.wiki.gg/wiki/Desktop),
    for the 1.4.5.6 release boundary.
  - **[P2]** [world creation](https://terraria.wiki.gg/wiki/World), for size,
    Classic difficulty, evil selection and persistent world structure.
  - **[P3]** [world generation](https://terraria.wiki.gg/wiki/World_generation),
    for seed-resolved terrain, layers, ores, biomes and structures.
  - **[P4]** [getting started](https://terraria.wiki.gg/wiki/Guide:Getting_started),
    for the first shelter, Work Bench and embodied opening route.
  - **[P5]** [pickaxes](https://terraria.wiki.gg/wiki/Pickaxes), for tool power,
    mining speed and block-to-item conversion.
  - **[P6]** [placement](https://terraria.wiki.gg/wiki/Placement), for range,
    occupancy, support, layers, furniture and station effects.
  - **[P7]** [recipes](https://terraria.wiki.gg/wiki/Recipes), for the 1.4.5
    crafting window and craft-from-nearby-chests rules.
  - **[P8]** [crafting stations](https://terraria.wiki.gg/wiki/Crafting_station),
    for station reach and station-filtered recipe availability.
  - **[P9]** [inventory](https://terraria.wiki.gg/wiki/Inventory), for hotbar,
    stack/storage, coin, ammunition, armour and accessory slots.
  - **[P10]** [difficulty](https://terraria.wiki.gg/wiki/Difficulty), for
    Classic character and world parameters and death coin fraction.
  - **[P11]** [spawn](https://terraria.wiki.gg/wiki/Spawn), for persistent-world
    return at the world or valid bed spawn point.
  - **[P12]** [house rules](https://terraria.wiki.gg/wiki/House), for enclosure,
    safe walls, area, furniture, home tile and evil-score validity.
  - **[P13]** [housing menu](https://terraria.wiki.gg/wiki/Housing_menu), for
    query feedback, NPC assignment and vacant-room checks.
  - **[P14]** [NPC rules](https://terraria.wiki.gg/wiki/NPC), for milestone-
    gated town arrivals, housing dependence and respawn.
  - **[P15]** [Life Crystal](https://terraria.wiki.gg/wiki/Life_Crystal), for
    the permanent health increment and cap.
  - **[P16]** [health](https://terraria.wiki.gg/wiki/Health), for damage,
    invulnerability, regeneration and death threshold.
  - **[P17]** [Potion Sickness](https://terraria.wiki.gg/wiki/Potion_Sickness),
    for healing-item lockout.
  - **[P18]** [day and night](https://terraria.wiki.gg/wiki/Day_and_night_cycle),
    for phase times, nocturnal populations and boss dawn rules.
  - **[P19]** [NPC spawning](https://terraria.wiki.gg/wiki/NPC_spawning), for
    offscreen, biome/layer, cap and town-suppression spawn state.
  - **[P20]** [Eye of Cthulhu](https://terraria.wiki.gg/wiki/Eye_of_Cthulhu),
    for entry predicates, two phases, servant and charge cycles and defeat.
  - **[P21]** [Dryad](https://terraria.wiki.gg/wiki/Dryad), for first-boss
    eligibility and current 1.4.5 behaviour.
  - **[P22]** [minimap](https://terraria.wiki.gg/wiki/Minimap), for retained
    exploration and world-state icons.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P22`; rules reasoning, not a claim of direct play.
- Claim IDs: `TRR-001`–`TRR-010`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, navigate the character; `ACT-040`, equip compatible
  armour or accessories; `ACT-130`, purchase an offered NPC item; `ACT-131`,
  consume a potion or permanent booster; `ACT-159`, target a reachable terrain
  cell to break; `ACT-161`, aim and strike; `ACT-162`, place a carried tile;
  `ACT-164`, select the active hotbar item; `ACT-123`, select a known personal
  crafting recipe and quantity.
- Parameters: direction, jump, hotbar slot, item, target tile, tool, placement
  layer, support, recipe, quantity, station, equipment slot and shop price.
- Claim IDs: `TRR-002`–`TRR-006`, `TRR-008`.

### System Behaviour Genes

- Existing genes: `SYS-004`, select unresolved random results; `SYS-212`,
  resolve the targeted terrain break and item drop; `SYS-213`, generate the
  seed-determined mutable tile world; `SYS-215`, resolve direct real-time
  hostile combat; `SYS-217`, resolve tile placement and neighbour updates;
  `SYS-222`, contact-pick up an eligible item; `SYS-216`, apply Classic death
  loss and respawn while preserving the world; `SYS-353`, consume recipe inputs
  and emit the known crafted output.
- New genes: `SYS-416`,
  advance day/night ecology and local spawns; `SYS-417`, apply permanent
  character-capacity boosters; `SYS-418`, validate town housing; `SYS-419`,
  admit eligible NPCs; `SYS-420`, resolve the night-bound two-phase Eye.
- Resolution order: running time and local ecology advance; one valid direct
  command resolves its break, placement, craft, pickup, equipment, item or
  combat consequences; lethal damage settles coin loss and respawn; housing
  and NPC admission evaluate persistent world and vacancy state; Eye defeat
  persists its boss flag and drops before Dryad eligibility can admit her.
- Parameters: seed, random outcome, clock, biome, layer, spawn cap, damage,
  defence, knockback, death fraction, recipe output, health cap, room validity,
  NPC milestone, Eye phase and dawn.
- Claim IDs: `TRR-001`–`TRR-010`.

### Constraint Genes

- Existing genes: `CON-206`, terrain breaking needs reach, mutability and a
  compatible tool; `CON-208`, placement needs compatible reachable space and
  support; `CON-210`, stacks and slots bound inventory transfer.
- New genes: `CON-366`, crafting needs all inputs and station context;
  `CON-367`, town housing needs a safe furnished room and home tile;
  `CON-368`, NPC arrival needs its milestone and vacant valid housing;
  `CON-369`, Eye entry and completion need a legal night state; `CON-370`,
  healing-item use needs missing health and no Potion Sickness.
- Scarce strategic resources: early ore and bars, ammunition, coins, healing
  items and cooldown opportunities, inventory slots, night duration, vacant
  houses and boss-preparation time.
- Claim IDs: `TRR-002`–`TRR-009`.

### Information Genes

- Existing genes: `INF-073`, hotbar and active equipment are visible;
  `INF-119`, character health, mana, defence and build are visible; `INF-128`,
  world items, inventory compatibility and capacity are visible; `INF-132`,
  crafting dependencies and output are visible.
- New genes: `INF-163`, explored minimap retains lit terrain and icons;
  `INF-164`, housing query exposes room validity and assignment; `INF-165`,
  world and boss cues expose night risk and Eye state.
- Parameters: hotbar, inventory, equipment, health, mana, defence, recipe,
  station, map brightness, icon, housing message, day phase, warning and boss bar.
- Claim IDs: `TRR-002`–`TRR-010`.

### Objective Genes

- New gene: `OBJ-083`, defeat the world's first Eye of Cthulhu and keep a
  vacant valid house until the eligible Dryad arrives.
- Claim IDs: `TRR-008`, `TRR-009`.

### Time Genes

- Existing gene: `TIM-003`, world time, ecology, combat, boss behaviour and NPC
  arrival advance in real time while the player moves, builds and fights;
  inventory Autopause remains a scoped setting parameter.
- Claim IDs: `TRR-003`, `TRR-007`, `TRR-008`.

## Reproducible transitions

1. Create a new Classic character and small Classic random world without a
   special seed; enter at central surface spawn with the Guide and starter tools.
2. Select the axe or pickaxe, harvest reachable wood or ore tiles and verify
   persistent removal, eligible item drops and contact pickup into bounded stacks.
3. Place blocks, safe background walls, a light, Work Bench, chair and entrance;
   use the housing query to distinguish an invalid room from valid vacant housing.
4. Open inventory near the Work Bench, compare exposed recipes, craft an early
   weapon or furniture piece and verify immediate ingredient consumption/output;
   repeat with an opened or toggled nearby chest under 1.4.5 rules.
5. Equip compatible armour or an accessory, retain ammunition and healing in
   bounded slots, and purchase an offered item after an eligible NPC arrives.
6. Explore lit underground terrain, collect and consume Life Crystals, then
   verify permanent maximum-health increments and retained minimap geometry.
7. Take lethal damage with coins on a Classic character; verify the rounded
   half-coin drop, respawn into the unchanged world and latest-death map icon.
8. Observe day turn to night and surface spawn composition change; shelter,
   fight or prepare while running time continues.
9. At night consume a Suspicious Looking Eye, or satisfy and observe the
   natural-entry warning; verify that a duplicate boss cannot enter and dawn
   ends an unfinished encounter.
10. Fight through the Eye's servant/charge first phase and transformed faster
    second phase; use one healing item, observe Potion Sickness blocking another,
    and defeat the Eye before dawn.
11. Preserve at least one vacant valid house, wait under legal arrival
    conditions and verify that the now-eligible Dryad is assigned and appears;
    the scoped objective completes.

## Strategic and experiential structure

- Local decision: choose which reachable tile, item, recipe, placement, target
  or healing window to commit while enemies and time remain live.
- Medium-term planning: turn finite early materials into tools, shelter,
  stations, armour, ammunition, health and valid NPC rooms before another night.
- Long-term structure: persistent world mutations, character upgrades, NPC
  milestones and boss flags form an open dependency graph rather than one
  authored linear mission list.
- Common heuristics: secure one valid house and Work Bench, light underground
  routes, upgrade health and defence, build a simple arena and preserve enough
  night for the Eye's second phase.
- Failure attribution: ordinary death exposes the combat or traversal mistake
  but preserves world work and equipment; lost coins and an escaped dawn-bound
  Eye make timing and preparation costs legible without deleting the save.
- Player-trust factors: recipes, item tooltips, housing diagnostics, health,
  boss bar and minimap expose current legality; exact future drops and natural
  spawn rolls remain hidden.
- Claim IDs: `TRR-002`–`TRR-010`.

## Replay and variation

- What changes between sessions: world seed, evil biome, ore alternatives,
  terrain, cave and chest layout, drops, item modifiers, NPC timing and route.
- Randomness or procedural generation: seed fixes world geography; live random
  processes select eligible loot, modifiers, spawns and natural Eye entry.
- Multiple viable strategies: melee, ranged or mixed equipment; manual versus
  natural Eye entry; surface construction versus deeper exploration; early NPC
  order and arena geometry.
- Typical replay motive: a different world and build route, difficulty or seed;
  only Classic non-special single-player is admitted here.
- Claim IDs: `TRR-001`, `TRR-003`, `TRR-005`, `TRR-007`, `TRR-008`.

## Adjacent systems and history

- Direct predecessor comparison: Minecraft shares embodied seeded terrain
  mutation, hotbar selection, placement, pickup and live combat.
- Important differences: Terraria generates a finite layered side-view world,
  crafts by selecting currently offered station recipes rather than arranging a
  grid, drops only Classic coins on death, ties residents to validated furnished
  rooms and makes the first boss explicitly night-bound.
- Variants excluded: Journey research/duplication, Expert/Master encounter
  changes, Mediumcore inventory loss, Hardcore permanent death and special seeds.
- Claim IDs: `TRR-001`–`TRR-010`.

## Normalised genome

The genome contains 39 genes: 26 reused and 13 new. It treats dimensionality,
world size, item counts, room dimensions, health thresholds and night duration
as parameters while separating direct commands, automatic resolution, legality,
disclosure, the composed first-boss objective and real-time scheduling.

## Edge cases

- The starting Guide does not need a prior vacant-house admission check, but he
  needs valid housing to remain assigned and to respawn after death.
- A room can shelter the player yet fail town housing because its background
  walls, area, furniture, home tile, occupancy or nearby evil is invalid.
- A bed room and NPC house overlap in many builds but their predicates are not
  identical; bed assignment is not mandatory in this scope.
- Crafting proximity exposes recipes without consuming or operating the station;
  the craft command owns commitment, and crafting is immediate rather than timed.
- Classic death retains carried items and equipment while dropping half the
  carried coins; it is not Minecraft's complete inventory drop.
- Life Crystal use is permanently character-bound and can be carried across
  worlds in the wider game, but cross-world transfer is excluded here.
- A manually summoned Eye needs night but not the natural spawn's health,
  defence, town-count or random-roll predicates.
- The Eye can be damaged before its transformation and may be defeated without
  a specific armour set, arena, NPC shop, natural spawn or healing item.
- Boss defeat makes the Dryad eligible; objective completion waits for a vacant
  valid house and legal arrival state rather than ending at the loot drop.

## Corpus comparison

Similarity uses exact unweighted Jaccard over complete typed gene sets; no
family, salience, presentation or parameter changes the score.

- Indexed games scanned: all 152 earlier canonical games.
- Indexed combinations scanned: all 150 earlier verified combinations.
- Exact genome matches: none.
- Near match: Minecraft (\`GAME-0129\`) at \`15 / 59 = 0.254237\`.
- Supported prior combination subsets: none; new \`COMB-0151\` is a strict
  subset of this 39-gene genome.
- Scan date: 2026-08-21.

Exhaustive prior-game ledger:

- `GAME-0001`: `1 / 52 = 0.019231`.
- `GAME-0002`: `0 / 46 = 0.000000`.
- `GAME-0003`: `0 / 48 = 0.000000`.
- `GAME-0004`: `2 / 52 = 0.038462`.
- `GAME-0005`: `0 / 46 = 0.000000`.
- `GAME-0006`: `1 / 47 = 0.021277`.
- `GAME-0007`: `0 / 47 = 0.000000`.
- `GAME-0008`: `0 / 46 = 0.000000`.
- `GAME-0009`: `1 / 54 = 0.018519`.
- `GAME-0010`: `0 / 48 = 0.000000`.
- `GAME-0011`: `0 / 52 = 0.000000`.
- `GAME-0012`: `0 / 48 = 0.000000`.
- `GAME-0013`: `0 / 52 = 0.000000`.
- `GAME-0014`: `0 / 54 = 0.000000`.
- `GAME-0015`: `1 / 52 = 0.019231`.
- `GAME-0016`: `2 / 52 = 0.038462`.
- `GAME-0017`: `0 / 52 = 0.000000`.
- `GAME-0018`: `2 / 56 = 0.035714`.
- `GAME-0019`: `0 / 49 = 0.000000`.
- `GAME-0020`: `1 / 52 = 0.019231`.
- `GAME-0021`: `1 / 47 = 0.021277`.
- `GAME-0022`: `0 / 51 = 0.000000`.
- `GAME-0023`: `0 / 49 = 0.000000`.
- `GAME-0024`: `1 / 50 = 0.020000`.
- `GAME-0025`: `1 / 49 = 0.020408`.
- `GAME-0026`: `1 / 50 = 0.020000`.
- `GAME-0027`: `1 / 50 = 0.020000`.
- `GAME-0028`: `3 / 53 = 0.056604`.
- `GAME-0029`: `2 / 49 = 0.040816`.
- `GAME-0030`: `1 / 52 = 0.019231`.
- `GAME-0031`: `0 / 50 = 0.000000`.
- `GAME-0032`: `0 / 50 = 0.000000`.
- `GAME-0033`: `2 / 50 = 0.040000`.
- `GAME-0034`: `2 / 51 = 0.039216`.
- `GAME-0035`: `2 / 55 = 0.036364`.
- `GAME-0036`: `1 / 50 = 0.020000`.
- `GAME-0037`: `0 / 48 = 0.000000`.
- `GAME-0038`: `2 / 53 = 0.037736`.
- `GAME-0039`: `0 / 48 = 0.000000`.
- `GAME-0040`: `1 / 46 = 0.021739`.
- `GAME-0041`: `2 / 48 = 0.041667`.
- `GAME-0042`: `0 / 48 = 0.000000`.
- `GAME-0043`: `1 / 52 = 0.019231`.
- `GAME-0044`: `1 / 48 = 0.020833`.
- `GAME-0045`: `1 / 52 = 0.019231`.
- `GAME-0046`: `0 / 49 = 0.000000`.
- `GAME-0047`: `0 / 53 = 0.000000`.
- `GAME-0048`: `0 / 53 = 0.000000`.
- `GAME-0049`: `0 / 48 = 0.000000`.
- `GAME-0050`: `1 / 53 = 0.018868`.
- `GAME-0051`: `2 / 53 = 0.037736`.
- `GAME-0052`: `0 / 49 = 0.000000`.
- `GAME-0053`: `1 / 47 = 0.021277`.
- `GAME-0054`: `1 / 49 = 0.020408`.
- `GAME-0055`: `1 / 48 = 0.020833`.
- `GAME-0056`: `0 / 47 = 0.000000`.
- `GAME-0057`: `0 / 47 = 0.000000`.
- `GAME-0058`: `0 / 48 = 0.000000`.
- `GAME-0059`: `0 / 46 = 0.000000`.
- `GAME-0060`: `0 / 46 = 0.000000`.
- `GAME-0061`: `0 / 49 = 0.000000`.
- `GAME-0062`: `0 / 47 = 0.000000`.
- `GAME-0063`: `0 / 46 = 0.000000`.
- `GAME-0064`: `0 / 44 = 0.000000`.
- `GAME-0065`: `0 / 46 = 0.000000`.
- `GAME-0066`: `0 / 49 = 0.000000`.
- `GAME-0067`: `1 / 46 = 0.021739`.
- `GAME-0068`: `0 / 47 = 0.000000`.
- `GAME-0069`: `0 / 47 = 0.000000`.
- `GAME-0070`: `0 / 47 = 0.000000`.
- `GAME-0071`: `0 / 46 = 0.000000`.
- `GAME-0072`: `0 / 47 = 0.000000`.
- `GAME-0073`: `0 / 46 = 0.000000`.
- `GAME-0074`: `0 / 48 = 0.000000`.
- `GAME-0075`: `0 / 48 = 0.000000`.
- `GAME-0076`: `0 / 46 = 0.000000`.
- `GAME-0077`: `0 / 46 = 0.000000`.
- `GAME-0078`: `0 / 46 = 0.000000`.
- `GAME-0079`: `0 / 46 = 0.000000`.
- `GAME-0080`: `0 / 46 = 0.000000`.
- `GAME-0081`: `0 / 47 = 0.000000`.
- `GAME-0082`: `0 / 47 = 0.000000`.
- `GAME-0083`: `0 / 47 = 0.000000`.
- `GAME-0084`: `0 / 49 = 0.000000`.
- `GAME-0085`: `0 / 50 = 0.000000`.
- `GAME-0086`: `0 / 52 = 0.000000`.
- `GAME-0087`: `1 / 48 = 0.020833`.
- `GAME-0088`: `0 / 48 = 0.000000`.
- `GAME-0089`: `0 / 48 = 0.000000`.
- `GAME-0090`: `1 / 53 = 0.018868`.
- `GAME-0091`: `2 / 46 = 0.043478`.
- `GAME-0092`: `1 / 48 = 0.020833`.
- `GAME-0093`: `0 / 48 = 0.000000`.
- `GAME-0094`: `2 / 47 = 0.042553`.
- `GAME-0095`: `2 / 49 = 0.040816`.
- `GAME-0096`: `2 / 47 = 0.042553`.
- `GAME-0097`: `2 / 45 = 0.044444`.
- `GAME-0098`: `2 / 44 = 0.045455`.
- `GAME-0099`: `1 / 46 = 0.021739`.
- `GAME-0100`: `1 / 49 = 0.020408`.
- `GAME-0101`: `0 / 49 = 0.000000`.
- `GAME-0102`: `0 / 46 = 0.000000`.
- `GAME-0103`: `0 / 48 = 0.000000`.
- `GAME-0104`: `1 / 47 = 0.021277`.
- `GAME-0105`: `2 / 47 = 0.042553`.
- `GAME-0106`: `0 / 46 = 0.000000`.
- `GAME-0107`: `1 / 46 = 0.021739`.
- `GAME-0108`: `1 / 48 = 0.020833`.
- `GAME-0109`: `1 / 54 = 0.018519`.
- `GAME-0110`: `1 / 46 = 0.021739`.
- `GAME-0111`: `1 / 45 = 0.022222`.
- `GAME-0112`: `2 / 45 = 0.044444`.
- `GAME-0113`: `2 / 51 = 0.039216`.
- `GAME-0114`: `1 / 45 = 0.022222`.
- `GAME-0115`: `0 / 45 = 0.000000`.
- `GAME-0116`: `2 / 43 = 0.046512`.
- `GAME-0117`: `1 / 46 = 0.021739`.
- `GAME-0118`: `1 / 54 = 0.018519`.
- `GAME-0119`: `1 / 61 = 0.016393`.
- `GAME-0120`: `3 / 65 = 0.046154`.
- `GAME-0121`: `1 / 61 = 0.016393`.
- `GAME-0122`: `1 / 53 = 0.018868`.
- `GAME-0123`: `3 / 74 = 0.040541`.
- `GAME-0124`: `3 / 83 = 0.036145`.
- `GAME-0125`: `2 / 79 = 0.025316`.
- `GAME-0126`: `2 / 80 = 0.025000`.
- `GAME-0127`: `2 / 85 = 0.023529`.
- `GAME-0128`: `1 / 54 = 0.018519`.
- `GAME-0129`: `15 / 59 = 0.254237`.
- `GAME-0130`: `2 / 90 = 0.022222`.
- `GAME-0131`: `4 / 81 = 0.049383`.
- `GAME-0132`: `1 / 89 = 0.011236`.
- `GAME-0133`: `1 / 83 = 0.012048`.
- `GAME-0134`: `1 / 89 = 0.011236`.
- `GAME-0135`: `1 / 86 = 0.011628`.
- `GAME-0136`: `2 / 97 = 0.020619`.
- `GAME-0137`: `7 / 62 = 0.112903`.
- `GAME-0138`: `4 / 70 = 0.057143`.
- `GAME-0139`: `10 / 83 = 0.120482`.
- `GAME-0140`: `7 / 75 = 0.093333`.
- `GAME-0141`: `9 / 81 = 0.111111`.
- `GAME-0142`: `8 / 82 = 0.097561`.
- `GAME-0143`: `8 / 80 = 0.100000`.
- `GAME-0144`: `6 / 68 = 0.088235`.
- `GAME-0145`: `9 / 78 = 0.115385`.
- `GAME-0146`: `10 / 93 = 0.107527`.
- `GAME-0147`: `5 / 59 = 0.084746`.
- `GAME-0148`: `9 / 73 = 0.123288`.
- `GAME-0149`: `7 / 67 = 0.104478`.
- `GAME-0150`: `7 / 54 = 0.129630`.
- `GAME-0151`: `8 / 67 = 0.119403`.
- `GAME-0152`: `10 / 74 = 0.135135`.

Minecraft is uniquely nearest at \`15 / 59 = 0.254237\`, sharing \`ACT-008\`,
\`ACT-159\`, \`ACT-161\`, \`ACT-162\`, \`ACT-164\`, \`SYS-212\`, \`SYS-213\`,
\`SYS-215\`, \`SYS-217\`, \`SYS-222\`, \`CON-206\`, \`CON-208\`, \`CON-210\`,
\`INF-073\` and \`TIM-003\`. No earlier registered combination is a complete
strict subset of Terraria's genome.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Minecraft (\`GAME-0129\`) | \`ACT-008\`, \`ACT-159\`, \`ACT-161\`, \`ACT-162\`, \`ACT-164\`, \`SYS-212\`, \`SYS-213\`, \`SYS-215\`, \`SYS-217\`, \`SYS-222\`, \`CON-206\`, \`CON-208\`, \`CON-210\`, \`INF-073\`, \`TIM-003\` | Minecraft uses 3D chunked terrain, spatial-grid crafting, hunger/durability, complete inventory death drops and End progression; Terraria uses finite layered terrain, offered station recipes, coin-only Classic loss, validated NPC housing, day/night ecology and the Eye-to-Dryad gate | nearest, not exact; \`15 / 59 = 0.254237\` |

### Registry normalisation 006 score corrections

These recomputed values supersede the pre-normalisation fractions above:

- `GAME-0119`: `2 / 60 = 0.033333`
- `GAME-0128`: `2 / 53 = 0.037736`
- `GAME-0129`: `16 / 58 = 0.275862`
- `GAME-0131`: `5 / 80 = 0.062500`
- `GAME-0132`: `2 / 88 = 0.022727`
- `GAME-0137`: `8 / 61 = 0.131148`
- `GAME-0139`: `11 / 82 = 0.134146`
- `GAME-0141`: `11 / 79 = 0.139241`
- `GAME-0143`: `10 / 78 = 0.128205`
- `GAME-0146`: `11 / 92 = 0.119565`
- `GAME-0151`: `9 / 66 = 0.136364`
- `GAME-0152`: `11 / 73 = 0.150685`
- Current prior-corpus near match after normalisation 006: `GAME-0129`.

## Combination assessment

`COMB-0151` is a 35-gene strict subset that retains mutable terrain,
station-crafting, build preparation, housing/NPC gates, day-night ecology,
Classic death recovery and the complete Eye-to-Dryad causal chain while omitting
generic purchases, unresolved random selection, contact pickup and broad ground-
loot comparison.

## Taxonomy impact

`TAXONOMY_CHANGE_010` generalises seven Minecraft-derived mutable-world genes
from implementation-specific voxel wording to embodied tile-world cells. It
does not change Minecraft's signature or create dimension-specific duplicates.
The unit adds sixteen bounded records for immediate station crafting, day/night
ecology, permanent resource boosters, validated NPC housing/admission, first-Eye
resolution, housing/map/boss disclosure and the composed objective.

## Negative results

No existing crafting Action represents an immediate offered-recipe commitment:
Minecraft's `ACT-160` requires a spatial grid and `ACT-123` queues timed work.
Palworld's generic defeat/respawn system transfers, but Minecraft's complete
inventory-drop record does not. Existing settlement housing genes describe
population capacity or supplied survival rather than validating one furnished
room and admitting milestone-gated named NPCs. Two-dimensional terrain did not
justify parallel break/place genes and instead triggered accepted taxonomy
generalisation 010.

## Delta summary

## Нові факти

- Desktop 1.4.5 crafting is an immediate recipe selection whose current source
  context can include nearby chests.
- Classic death preserves equipment and items but drops half the carried coins.
- Valid town housing is a system-evaluated constructed predicate, not shelter alone.
- The first Eye is both progression-gated and night-bounded; Dryad arrival adds
  a second housing condition after victory.

## Нові гени

- Adds `SYS-416`–`SYS-420`, `CON-366`–`CON-370`, `INF-163`–`INF-165`
  and `OBJ-083`.

## Нові комбінації

- `COMB-0151` records the 35-gene mutable-world preparation, housing and
  night-bound first-boss-to-Dryad chain.

## Зміни таксономії

- Accepted `TAXONOMY_CHANGE_010`; seven existing mutable-world records gain
  dimension-neutral definitions and Terraria evidence.

## Family classification

- `FAM-010` Real-time system pressure.
- `FAM-013` Inventory and fixture dependencies.
- `FAM-014` World topology and perspective.
- `FAM-017` Ordered dependency sequencing.

## Plain-language interpretation

Terraria's opening asks the player to turn one unknown mutable world into a
safe and capable foothold before the night closes. The same gathered materials
become terrain, stations, rooms, weapons and health preparation. Valid housing
converts world milestones into useful residents; the Eye converts an open
sandbox route into one bounded night fight; the Dryad's arrival proves both the
boss flag and the built-room dependency.

## New questions

- Which later Terraria boss-to-world-state transitions recur outside mutable
  construction sandboxes?
- Does housing-query disclosure recur as a reusable validation-interface pattern
  in games with authored residents rather than aggregate population capacity?

## Наступна рекомендована гра

- [Confirmed | Direct | High] No next game is authorised in this Goal.

## Чому саме вона

- `GAME-0153` completes the recorded 17-game demand-led Goal and brings the
  corpus to exactly seventeen nine-game catalogue groups. The next selection
  requires a new maintainer decision after local review.
