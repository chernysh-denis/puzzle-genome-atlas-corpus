---
game_id: GAME-0141
slug: rust
game_title: Rust
analysis_status: reviewed
reviewed: 2026-08-21
combination_ids:
  - COMB-0139
gene_ids:
  action:
    - ACT-008
    - ACT-122
    - ACT-123
    - ACT-161
    - ACT-164
    - ACT-165
    - ACT-199
    - ACT-204
    - ACT-205
    - ACT-206
    - ACT-207
    - ACT-208
    - ACT-209
  system:
    - SYS-208
    - SYS-215
    - SYS-216
    - SYS-223
    - SYS-326
    - SYS-327
    - SYS-328
    - SYS-329
    - SYS-330
    - SYS-331
    - SYS-332
    - SYS-333
    - SYS-334
    - SYS-335
    - SYS-336
  constraint:
    - CON-210
    - CON-281
    - CON-292
    - CON-293
    - CON-294
    - CON-295
    - CON-296
    - CON-297
    - CON-298
    - CON-299
    - CON-300
    - CON-301
    - CON-302
  information:
    - INF-073
    - INF-075
    - INF-115
    - INF-128
    - INF-130
    - INF-131
    - INF-132
  objective:
    - OBJ-075
  time:
    - TIM-003
    - TIM-017
---

# Game: Rust

## Analysis scope

- Version / ruleset: public PC `Power Trip` build released 2026-08-06; one
  default vanilla procedural monthly-wipe server, solo, from a new beach spawn
  with no assumed non-default blueprints until the next scheduled wipe.
- Included: resource harvesting and loot; inventory, food and exposure;
  hand-crafting, Furnace and Recycler; blueprint research; current Workbench
  tier and fragment progression; connected building blocks, stability, locks,
  Tool Cupboard privilege and upkeep; Sleeping Bag respawn; direct combat,
  death drop and recovery; sleeping-body/offline persistence; explosive
  structural raiding; scheduled world wipe.
- Reproducible progression trace: establish a locked TC-protected base, craft
  Workbench tiers through Level 3, learn and craft one Timed Explosive Charge,
  breach one unauthorised player structure and return at least one stolen
  stored stack to locked TC-protected storage. This is an analytical trace, not
  a game-authored victory; the survival objective remains open until wipe.
- Excluded: teams or clans; Softcore, Creative, custom and modded servers;
  Tutorial Island; DLC, cosmetics and account economy; vehicles, electricity,
  industrial automation, farming and ocean systems; exhaustive monuments,
  events and endgame-event scoring; administrator tools.
- Direct-play status: no complete wipe-cycle playthrough was performed. Official
  Facepunch product, update and wiki material establishes the live scope and
  reproducible transition boundaries.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `RUST-001` | The only authored high-level aim is survival; no kill, raid or crafted item is a terminal victory | Confirmed | Direct | High | P1 |
| `RUST-002` | A default server may initialise a procedural island with biomes, monuments, protected areas and sampled resources or loot | Confirmed | Corroborated | High | P2, P3, P4 |
| `RUST-003` | Personal survival couples gathering, bounded inventory, crafting, metabolism, equipment and direct combat | Observation | Corroborated | High | P1, P2, P5 |
| `RUST-004` | Connected building placement, grade, stability and repair alter persistent traversable geometry | Observation | Corroborated | High | P6, P7, P8 |
| `RUST-005` | A Tool Cupboard projects building privilege and consumes connected grade-specific upkeep; shortage decays affected material from exposed layers | Confirmed | Direct | High | P9 |
| `RUST-006` | Locks and TC authorisation separate physical reach from permission until credentials or structure are defeated | Confirmed | Direct | High | P9, P10 |
| `RUST-007` | Blueprints are learned through scrap research or ordered Workbench tech trees, and current Workbench recipes require predecessor tiers and blueprint fragments | Confirmed | Direct | High | P11, P12, P13 |
| `RUST-008` | Sleeping Bags provide assigned cooldown-bound respawn while ordinary death exposes carried inventory in the continuing world | Observation | Corroborated | High | P14, P15 |
| `RUST-009` | Timed Explosive Charge is a Workbench-3 craft intended to breach bases, so a legal raid couples research, production and material-specific structural damage | Confirmed | Direct | High | P16 |
| `RUST-010` | Server time and hostile interaction continue across player absence, leaving sleepers, storage and bases vulnerable | Confirmed | Corroborated | High | P1, P17 |
| `RUST-011` | The default monthly wipe timer reaches its boundary on the first Thursday at 19:00 London time and replaces the persistent world cycle | Confirmed | Direct | High | P18 |

## Basic data

- Release / origin: Facepunch Studios; Steam Early Access 2013, 1.0 release 2018;
  current PC live service reviewed at `Power Trip`.
- Platform or physical form: networked Windows, macOS and Linux PC client;
  scoped to public PC vanilla rules.
- Puzzle family: adversarial persistent-world survival through claimed
  construction, upkeep and recoverable loss.
- Primary sources:
  - **[P1]** [official Rust overview](https://rust.facepunch.com/), for survival,
    building, other survivors and persistent threat.
  - **[P2]** [official Steam page](https://store.steampowered.com/app/252490/Rust/),
    for survival, crafting, bases, stored loot and territory.
  - **[P3]** [official current Power Trip update](https://rust.facepunch.com/news/power-trip),
    for the reviewed 2026-08-06 public version boundary.
  - **[P4]** [official map guide](https://wiki.facepunch.com/rust/map), for
    procedural maps, biomes, monuments, build-protected regions and safe zones.
  - **[P5]** [official Tutorial Island guide](https://wiki.facepunch.com/rust/tutorial_island),
    used only to corroborate the core movement, gathering, combat, crafting,
    Furnace, Workbench, building and respawn vocabulary excluded from the route.
  - **[P6]** [official Building Plan item](https://wiki.facepunch.com/rust/item/building.planner),
    for direct block selection and placement.
  - **[P7]** [official Hammer item](https://wiki.facepunch.com/rust/item/hammer),
    for building material upgrades, repair and eligible pickup.
  - **[P8]** [official building terminology](https://wiki.facepunch.com/rust/Building-terminology),
    for mechanically possible airlocks and layered bases.
  - **[P9]** [official Tool Cupboard, decay and privilege guide](https://wiki.facepunch.com/rust/the_tool_cupboard),
    for authorisation, projected privilege, connected upkeep, grade-specific
    decay, outer-layer order and destruction protection.
  - **[P10]** [official Code Lock item](https://wiki.facepunch.com/rust/item/lock.code),
    for credentialled access.
  - **[P11]** [official Blueprint item](https://wiki.facepunch.com/rust/item/blueprintbase),
    for Research Table and tech-tree learning.
  - **[P12]** [official Workbench Level 2 item](https://wiki.facepunch.com/rust/item/workbench2),
    for the current predecessor/material/basic-fragment recipe.
  - **[P13]** [official Workbench Level 3 item](https://wiki.facepunch.com/rust/item/workbench3),
    for the current predecessor/material/advanced-fragment recipe.
  - **[P14]** [official Sleeping Bag item](https://wiki.facepunch.com/rust/item/sleepingbag),
    for assigned respawn and cooldown.
  - **[P15]** [official server commands reference](https://wiki.facepunch.com/rust/useful_commands),
    for authoritative death, corpse, respawn and sleeper parameters.
  - **[P16]** [official Timed Explosive Charge item](https://wiki.facepunch.com/rust/item/explosive.timed),
    for base breach purpose, Workbench-3 recipe and research paths.
  - **[P17]** [official Rust+ description](https://rust.facepunch.com/companion),
    for remote alerts and raids while away.
  - **[P18]** [official server wipe timer](https://wiki.facepunch.com/rust/server-wipe-timer),
    for the default monthly schedule and explicit wipe horizon.
- Secondary sources: none admitted.
- Claim IDs: `RUST-001`–`RUST-011`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, navigation; `ACT-122`, extract or dismantle a
  world entity; `ACT-123`, hand-craft a queued recipe; `ACT-161`, direct
  hostile attack; `ACT-164`, quick-slot selection; `ACT-165`, consume food;
  `ACT-199`, transfer compatible world or container loot.
- New genes: `ACT-204`, place/upgrade/repair a building block; `ACT-205`,
  configure authority; `ACT-206`, operate a processing fixture; `ACT-207`,
  learn one recipe; `ACT-208`, assign respawn; `ACT-209`, attach C4.
- Claim IDs: `RUST-003`–`RUST-009`.

### System Behaviour Genes

- Existing genes: `SYS-208`, projectile/cover/armour resolution; `SYS-215`,
  live hostile combat; `SYS-216`, death drop and same-world respawn;
  `SYS-223`, tool durability.
- New genes: `SYS-326`–`SYS-336`, covering procedural world initialisation,
  metabolism, crafting and processing, connected buildings, privilege, upkeep,
  offline persistence, raiding, blueprints and wipe.
- Resolution order: initialise one shared island; advance survival, gathering,
  crafting, construction and conflict concurrently; persist state and sleepers
  across connections; charge upkeep and accept hostile damage under server time;
  replace the cycle at the configured wipe boundary.
- Claim IDs: `RUST-002`–`RUST-011`.

### Constraint Genes

- Existing genes: `CON-210`, typed stack-and-slot inventory; `CON-281`,
  climate-compatible embodied survival.
- New genes: `CON-292`–`CON-302`, covering placement, grade material,
  privilege, upkeep, locks, crafting, Workbench order, respawn, breach,
  disconnected vulnerability and wipe horizon.
- Scarce strategic resources: safe time, calories and water; tools and
  durability; inventory slots; wood, stone, metal, sulfur, scrap and blueprint
  fragments; protected storage; upkeep duration; base layers and sleeping bags.
- Claim IDs: `RUST-003`–`RUST-011`.

### Information Genes

- Existing genes: `INF-073`, active equipment; `INF-075`, health, hunger,
  armour and durability; `INF-115`, partial local opponent information;
  `INF-128`, visible loot identity and inventory compatibility.
- New genes: `INF-130`, map and wipe horizon; `INF-131`, placement,
  privilege and upkeep status; `INF-132`, blueprint and crafting dependencies.
- Claim IDs: `RUST-002`–`RUST-011`.

### Objective Genes

- New gene: `OBJ-075`, preserve or rebuild a recoverable secured foothold
  until the scheduled world wipe.
- Evaluation: ordinary death, one base loss, a kill, Workbench 3 or the scoped
  raid milestone is non-terminal; the bounded review ends only at wipe.
- Claim IDs: `RUST-001`, `RUST-008`–`RUST-011`.

### Time Genes

- Existing gene: `TIM-003`, forced real-time progression while connected.
- New gene: `TIM-017`, authoritative time while the player is absent.
- Parameters: craft and processor cycles, respawn cooldown, upkeep and decay,
  explosive fuse, disconnect interval and scheduled wipe.
- Claim IDs: `RUST-003`–`RUST-011`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| New survivor owns harvested wood and cloth | Craft a Building Plan, TC, lock and Sleeping Bag; place a legal connected shell | Ingredients become fixtures and blocks; TC authorises the placer; lock gates access; bag records a respawn | One material foothold links geometry, ownership and recovery | `RUST-004`–`RUST-008` |
| Connected stone and metal blocks are protected by a TC | Put the exact charged materials in TC, then remove one required grade | Protection time rises; after that grade's material expires, exposed blocks of only that grade begin decay | Upkeep is typed ongoing cost, not abstract ownership | `RUST-005` |
| Furnace holds compatible ore and wood | Light it and preserve output capacity through a cycle | Fuel and ore become metal, sulfur or high-quality products plus by-products | Material progression is live fixture processing | `RUST-003` |
| Player owns scrap and an eligible found item or reachable tech-tree node | Research the recipe | Scrap and any required research item are consumed and personal blueprint knowledge gains the recipe | Loot can become persistent production knowledge | `RUST-007` |
| Workbench 1 and current Basic fragments/materials exist | Craft Workbench 2, then repeat with its Advanced-fragment recipe | Each predecessor is consumed into the next tier; tier three becomes physically placeable | Current high-tier production is an ordered material chain | `RUST-007` |
| C4 blueprint, Workbench 3 and exact ingredients are available | Queue one Timed Explosive Charge | Ingredients are consumed and one charge appears after its craft duration | The raid tool is downstream of research and production | `RUST-009` |
| Locked unauthorised route separates raider from stored stacks | Attach enough legal timed charges to one material layer | Fuses resolve blast damage; destroyed layers lose collision and expose reachable contents | Physical damage can defeat credentialled access | `RUST-006`, `RUST-009` |
| Avatar dies while an assigned off-cooldown bag survives | Choose that bag for respawn and revisit the corpse | Avatar returns at the bag while recoverable carried stacks remain in shared state subject to other players | Death is costly but not necessarily terminal | `RUST-008` |
| Owner disconnects with a locked supplied base | Another participant raids or upkeep expires before reconnect | Server-authoritative damage, loot and decay alter the returning owner's state | Absence is a strategic time commitment | `RUST-010` |
| Default monthly timer reaches zero | Execute scheduled wipe | Current island, buildings and world inventories are replaced under reset policy | Persistence has an explicit outer horizon | `RUST-011` |

## Strategic and experiential structure

- Local decision: harvest, conceal, fight, retreat, craft, upgrade, repair,
  research, spend upkeep or expose a raid path under incomplete hostile state.
- Medium-term planning: choose a defensible site, secure TC and respawn,
  balance base footprint against upkeep, and route scrap/fragments through
  ordered Workbench and C4 dependencies.
- Long-term structure: preserve multiple recovery options and enough secured
  productive state that death, offline loss or one breach remains recoverable
  before the fixed wipe horizon.
- Common heuristics: airlock external doors, lock the TC, avoid oversized early
  grades, keep upkeep ahead of absence, distribute respawn and storage, and
  calculate the weakest physical raid path rather than attacking every layer.
- Failure attribution: starvation, exposure and combat are locally legible;
  unseen participants, stochastic loot and offline actions preserve uncertainty.
- Claim IDs: `RUST-001`–`RUST-011`.

## Replay and variation

- What changes: map seed, terrain/monuments, resource and loot placements,
  participants, neighbours, conflicts, deaths, bases and raid history.
- Randomness or procedural generation: seeded island plus sampled resource and
  loot states; player behaviour dominates the persistent strategic history.
- Multiple viable strategies: remote or contested site, compact or distributed
  base, research-table finds or tech-tree path, avoidance or offensive raiding.
- Typical replay motive: emergent adversarial histories under recoverable loss
  and a shared scheduled reset.
- Claim IDs: `RUST-002`–`RUST-011`.

## Adjacent systems and history

- Minecraft is nearest because both combine direct gathering, hand-crafting,
  durable tools, construction, survival, inventory loss and same-world respawn.
- Palworld shares broader embodied survival and persistent base state, but its
  scoped base is operated by autonomous Pals rather than hostile ownership,
  typed upkeep and offline raiding.
- PUBG shares direct combat, partial information and found loadouts but deletes
  the continuous world after one irreversible match life.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-122`, `ACT-123`, `ACT-161`, `ACT-164`, `ACT-165`, `ACT-199`, `ACT-204`–`ACT-209` | recipes, controls and building shapes are parameters |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-216`, `SYS-223`, `SYS-326`–`SYS-336` | rates, seeds and damage values are parameters |
| Constraint | `CON-210`, `CON-281`, `CON-292`–`CON-302` | costs, radii, grades and cooldowns are parameters |
| Information | `INF-073`, `INF-075`, `INF-115`, `INF-128`, `INF-130`–`INF-132` | HUD style is presentation |
| Objective | `OBJ-075` | the raid trace is a milestone, not terminal success |
| Time | `TIM-003`, `TIM-017` | live/offline durations and wipe schedule are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `140` (`GAME-0001`–`GAME-0140`).
- Exact genome matches: none.
- Tied near matches: `GAME-0139` — Palworld (`14 / 91 = 0.153846`).
- Supported combination subsets: `COMB-0139`.
- Scan date: 2026-08-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Palworld (`GAME-0139`) | direct survival, crafting, navigation, combat, inventory and live time | captured autonomous workers and story finale versus manually built claimed base, typed upkeep and offline raid risk | Near, `0.153846` |

### Preserved research notes

- New genes: `ACT-204`–`ACT-209`, `SYS-326`–`SYS-336`,
  `CON-292`–`CON-302`, `INF-130`–`INF-132`, `OBJ-075` and
  `TIM-017` (33 total).
- Classification: `New gene` and `New combination of known and new genes`.

## Taxonomy impact

- Registry changes: add 33 bounded active genes and `COMB-0139`; preserve the
  existing gathering, crafting, combat, inventory and respawn boundaries.
- Taxonomy-change record: none.
- Candidate terms: wipe, offline raid, honeycomb and airlock remain parameters,
  strategy vocabulary or combinations rather than atomic genes.

## Negative results

- No earlier combination is a proper subset of the scoped genome.
- No authored terminal win state was found; the explicit survival aim is
  bounded analytically by the server wipe rather than reclassified as victory.
