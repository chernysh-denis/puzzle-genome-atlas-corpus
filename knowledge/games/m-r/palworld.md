---
game_id: GAME-0139
slug: palworld
game_title: Palworld
analysis_status: reviewed
reviewed: 2026-08-21
combination_ids:
  - COMB-0137
gene_ids:
  action:
    - ACT-008
    - ACT-087
    - ACT-122
    - ACT-123
    - ACT-134
    - ACT-145
    - ACT-148
    - ACT-161
    - ACT-164
    - ACT-165
    - ACT-194
    - ACT-195
    - ACT-196
    - ACT-197
  system:
    - SYS-004
    - SYS-045
    - SYS-051
    - SYS-186
    - SYS-196
    - SYS-197
    - SYS-215
    - SYS-216
    - SYS-222
    - SYS-223
    - SYS-299
    - SYS-307
    - SYS-308
    - SYS-310
    - SYS-311
    - SYS-312
    - SYS-313
    - SYS-315
  constraint:
    - CON-062
    - CON-192
    - CON-193
    - CON-200
    - CON-210
    - CON-276
    - CON-277
    - CON-278
    - CON-279
    - CON-280
    - CON-281
    - CON-282
  information:
    - INF-059
    - INF-073
    - INF-075
    - INF-122
    - INF-123
    - INF-124
    - INF-125
    - INF-126
  objective:
    - OBJ-073
  time:
    - TIM-003
---

# Game: Palworld

## Analysis scope

- Version / ruleset: public Windows `v1.0.3`, reviewed 2026-08-21; one fresh
  single-player Normal world with default settings, from character spawn
  through the first completion of the World Tree main-story finale.
- Included: direct exploration and combat; gathering, inventory, crafting,
  construction, hunger, climate and ordinary defeat; probabilistic Pal capture;
  party deployment, Partner Skills and persistent levelling; Palbox storage,
  base assignment, work suitability, hauling, food, SAN and illness; technology
  unlocks; main missions, tower bosses, Sunreach, Echoing Flute, Panthalus and
  the terminal Sealed Calamity encounter.
- Excluded: multiplayer, Guild authority, PvP and Arena; custom world settings,
  dedicated servers and mods; cosmetics and paid add-ons; exhaustive breeding,
  mutation, Awakening and collection; optional hard-mode tower rematches,
  challenge raids and post-story optimisation.
- Direct-play status: no complete fresh story run was conducted. Pocketpair's
  current product and 1.0/1.0.3 release material establish the scope; the
  maintained official wiki and current 1.0 route references corroborate the
  bounded mechanics and ending trace.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PAL-001` | A new persistent world supports direct gathering, crafting, construction, survival and combat | Confirmed | Corroborated | High | P1, P2, S1, S2 |
| `PAL-002` | A Sphere hit on an eligible wild Pal resolves a displayed health-, target- and device-sensitive capture chance into owned storage | Confirmed | Corroborated | High | P2, S3 |
| `PAL-003` | Captured Pals move among storage, a five-member party and bounded base slots; one deployed party Pal follows and fights autonomously | Confirmed | Corroborated | High | P1, S4, S5 |
| `PAL-004` | Base Pals claim reachable jobs only through matching work suitability, fixed assignment and priority, while food, SAN and health qualify their work | Confirmed | Corroborated | High | P2, S4, S6 |
| `PAL-005` | Capture and combat experience raise persistent player and Pal levels; level and point gates constrain technology purchases | Confirmed | Corroborated | High | P2, S7 |
| `PAL-006` | The reworked main mission orders tower and world gates through Sunreach, Echoing Flute, Panthalus and the World Tree finale | Confirmed | Corroborated | High | P2, S8, S9 |
| `PAL-007` | Default Normal defeat preserves the world and respawns the avatar under the current configured drop rule | Confirmed | Corroborated | High | P2, S10 |

## Basic data

- Release / origin: Pocketpair; Early Access began 19 January 2024 and full
  version 1.0 released 10 July 2026.
- Platform or physical form: third-person open-world survival, creature capture,
  combat, crafting and base-management game.
- Puzzle family: real-time system pressure; agent routing and coordination;
  automation and spatial programming; ordered dependency sequencing.
- Primary sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/1623730/Palworld/),
    for Pocketpair authorship and the fight, capture, building, farming and
    factory-work premise.
  - **[P2]** [official Palworld v1.0 release changelog](https://store.steampowered.com/news/app/1623730/view/686383649529010623),
    for the released rules boundary, reworked main mission, World Tree,
    combat/capture/base/technology changes and default Normal death setting.
  - **[P3]** [official Palworld v1.0.3 update](https://store.steampowered.com/news/app/1623730/view/695395286786244641),
    for the current public patch boundary and post-release fixes.
- Secondary and reproducible sources:
  - **[S1]** [official wiki: Palworld](https://palworld.wiki.gg/wiki/Palworld),
    for the persistent open-world survival loop.
  - **[S2]** [official wiki: Crafting](https://palworld.wiki.gg/wiki/Crafting),
    for material recipes, workbenches and player/Pal workload.
  - **[S3]** [official wiki: Capturing Pals](https://palworld.wiki.gg/wiki/Capturing_Pals),
    for Sphere eligibility, displayed chance and capture resolution.
  - **[S4]** [official wiki: Palbox](https://palworld.wiki.gg/wiki/Palbox),
    for storage, party/base assignment and base capacity.
  - **[S5]** [official wiki: Party](https://palworld.wiki.gg/wiki/Party),
    for five active slots, deployment and companion field behaviour.
  - **[S6]** [official wiki: Work Suitability](https://palworld.wiki.gg/wiki/Work_Suitability),
    for typed jobs, fixed assignments, priorities and work state.
  - **[S7]** [official wiki: Technology](https://palworld.wiki.gg/wiki/Technology),
    for level tiers, prerequisites and technology-point spending.
  - **[S8]** [VGC World Tree route](https://www.videogameschronicle.com/guide/palworld-10-enter-world-tree/),
    for Sunreach, defence modules, Echoing Flute, Panthalus and the World Tree gate.
  - **[S9]** [current World Tree finale guide](https://www.palguides.com/guides/palworld-zenara-astralym-guide/),
    for the terminal 1.0 story encounter and first-clear boundary.
  - **[S10]** [official wiki: Death](https://palworld.wiki.gg/wiki/Death),
    for world persistence, respawn and world-setting-dependent loss.
- Claim IDs: `PAL-001`–`PAL-007`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, navigate the avatar; `ACT-087`, apply a held key
  item to a compatible fixture; `ACT-122`, extract or dismantle a world entity;
  `ACT-123`, hand-craft a selected recipe; `ACT-134`, purchase a persistent
  technology node; `ACT-145`, configure worker/task priority; `ACT-148`, place
  a material-backed construction plan; `ACT-161`, directly attack a hostile;
  `ACT-164`, select active carried equipment; `ACT-165`, consume food.
- New genes: `ACT-194`, throw a capture device; `ACT-195`, deploy or recall a
  party Pal; `ACT-196`, transfer a Pal among storage, party and base;
  `ACT-197`, activate one Partner Skill.
- Parameters: world target, tool, recipe, structure, technology, Pal, roster,
  base, priority, capture device, Partner Skill and mount state.
- Claim IDs: `PAL-001`–`PAL-005`.

### System Behaviour Genes

- Existing genes: `SYS-004`, random outcome selection; `SYS-045`, autonomous
  locomotion; `SYS-051`, autonomous combat engagement; `SYS-186`, ranked
  errand choice; `SYS-196`, filtered hauling; `SYS-197`, skill-conditioned work
  duration; `SYS-215`, direct real-time combat; `SYS-222`, contact pickup;
  `SYS-223`, equipment durability loss; `SYS-299`, experience levels and build
  points; `SYS-216`, configured defeat loss and same-world respawn.
- New genes: `SYS-307`, probabilistic capture into storage; `SYS-308`, deployed
  companion follow/combat; `SYS-310`, work-suitability base dispatch;
  `SYS-311`, Pal hunger/SAN/condition;
  `SYS-312`, material-backed crafting/construction workload; `SYS-313`,
  persistent generated survival world;
  `SYS-315`, mission progression through tower and raid gates.
- Resolution order: live movement, work and combat update health, hunger and
  durability; a capture consumes its device before the random checks; successful
  ownership enables party/base transfer; work turns supplied materials into
  items and structures; experience and technology unlock later traversal,
  equipment and story gates; the terminal mission completion ends the scope.
- Claim IDs: `PAL-001`–`PAL-007`.

### Constraint Genes

- Existing genes: `CON-062`, compatible structure footprint; `CON-192`, worker
  permission/skill/reach; `CON-193`, construction material and cells;
  `CON-200`, filtered storage capacity; `CON-210`, typed inventory slots/stacks.
- New genes: `CON-276`, capture target/device gate; `CON-277`, distinct Pal
  roster capacities; `CON-278`, technology level/prerequisite/point gate;
  `CON-279`, base task suitability/facility gate; `CON-280`, Pal food/rest/
  condition dependency; `CON-281`, avatar climate and survival dependency;
  `CON-282`, ordered main-story encounter gates.
- Scarce resources: player and Pal health, hunger, stamina and SAN; Sphere and
  ammunition counts; inventory, party, storage and base slots; food, materials,
  technology points, equipment durability, work time and boss time limits.
- Claim IDs: `PAL-001`–`PAL-007`.

### Information Genes

- Existing genes: `INF-059`, visible recipe/technology dependencies;
  `INF-073`, carried equipment and active slot; `INF-075`, health, hunger,
  armour and durability.
- New genes: `INF-122`, capture probability; `INF-123`, Pal combat/work profile;
  `INF-124`, avatar and party survival state; `INF-125`, explored map and mission
  gates; `INF-126`, base assignments, resources and worker condition.
- Claim IDs: `PAL-001`–`PAL-007`.

### Objective Genes

- New gene: `OBJ-073`, complete the World Tree main-story finale.
- Success, evaluation and failure: the first completed terminal Sealed Calamity
  encounter after the ordered main-mission gates completes the scoped story;
  avatar defeat is recoverable and collection percentage is not the objective.
- Claim IDs: `PAL-006`, `PAL-007`.

### Time Genes

- Existing gene: `TIM-003`, exploration, combat, work, hunger, cooldowns and
  mission encounters resolve in real time.
- Parameters: work duration, day/night, hunger decay, respawn, ability cooldown,
  capture sequence and tower timer.
- Claim IDs: `PAL-001`–`PAL-007`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| A wild capturable Pal is weakened and a Sphere is carried | Throw the Sphere at the target | The device is consumed, the displayed chance resolves and success moves the Pal to owned storage | probabilistic capture | `PAL-002` |
| An owned Pal is in storage and party/base capacity is open | Transfer it through the Palbox | The chosen destination roster gains the Pal and the source slot is freed | persistent roster partition | `PAL-003` |
| A party Pal is selected and no other companion is deployed | Throw it to a reachable position | It materialises, follows the avatar and autonomously attacks eligible hostiles until recall/incapacitation | companion field AI | `PAL-003` |
| A base Pal has Mining suitability and a reachable mine has work | Assign or prioritise the task | The Pal routes to the facility and accumulates work while food, SAN and health permit | suitability-gated labour | `PAL-004` |
| A known structure has valid support and enough shared material | Place its construction plan | Material and player/Pal workload complete the persistent structure | work-backed building | `PAL-001`, `PAL-004` |
| The player reaches a level-gated technology with enough points | Purchase the node | Points are deducted and its recipe, structure or equipment becomes available | persistent technology progression | `PAL-005` |
| Sunreach defence modules and its tower boss are complete | Follow the marked researcher route and assemble the Echoing Flute | The raid stone accepts the key item and exposes the Panthalus encounter | authored dependency gate | `PAL-006` |
| Panthalus is defeated, captured and in the active party | Interact at the World Tree altar | The barrier sequence opens the World Tree and advances the final missions | companion-as-story-key | `PAL-006` |
| Every final mission condition is complete | Defeat the terminal Sealed Calamity encounter | The game records the first main-story completion while the world remains available | scoped ending | `PAL-006` |

## Strategic and experiential structure

- Local decision: weaken rather than kill a desired Pal; choose Sphere tier;
  swap player weapon and active companion; manage dodge, stamina, hunger and
  temperature; match one worker to one urgent compatible task.
- Medium-term planning: turn captures into party elemental coverage and a
  balanced base workforce, secure food and materials, spend technology points
  on the next equipment/saddle/production dependency and build in reachable space.
- Long-term structure: climb player and Pal levels, replace manual gathering
  with supported base labour, clear the ordered tower and quest chain, prepare
  the required key item and Pal, then enter and complete the World Tree finale.
- Common heuristics: lower target health before a costly Sphere; carry climate
  protection and food; keep party roles diverse; reserve healthy workers for
  their highest suitability; prevent food/SAN collapse before expanding output.
- Failure attribution: capture chance, Pal suitability, recipe requirements,
  survival bars, mission gates and base condition are visible; random capture
  results and autonomous path/task choice retain bounded uncertainty.
- Claim IDs: `PAL-001`–`PAL-007`.

## Replay and variation

- What changes: world seed, encountered Pals and traits, capture outcomes,
  party composition, base sites/layouts, technology order and combat preparation.
- Randomness or procedural generation: the persistent world and creature/resource
  distribution vary; capture checks and Pal traits add local uncertainty.
- Multiple viable strategies: direct player firepower, mounted Partner Skills,
  companion elemental counters, capture-heavy levelling and differently
  specialised bases can reach the same story gates.
- Typical replay motive: build a different Pal roster/base economy, explore
  another seed and solve the progression chain with different companions.
- Claim IDs: `PAL-001`–`PAL-006`.

## Adjacent systems and history

- Direct predecessors: creature-collection RPGs, open-world survival crafting
  and colony/base automation.
- Variants: multiplayer adds Guild ownership and shared bases; custom settings
  alter rates, difficulty and death loss; hard tower/raid content extends combat.
- Similar games: Ark: Survival Evolved, Pokémon Legends: Arceus, Craftopia,
  Minecraft and survival games with recruitable automation workers.
- Important differences: one captured roster serves three mechanically distinct
  roles—probabilistic collection, active combat/traversal and suitability-gated
  autonomous base labour—inside the same persistent survival progression.
- Claim IDs: `PAL-001`–`PAL-006`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-087`, `ACT-122`, `ACT-123`, `ACT-134`, `ACT-145`, `ACT-148`, `ACT-161`, `ACT-164`, `ACT-165`, `ACT-194`–`ACT-197` | exact tools, Pals and recipes are parameters |
| System Behaviour | `SYS-004`, `SYS-045`, `SYS-051`, `SYS-186`, `SYS-196`, `SYS-197`, `SYS-215`, `SYS-222`, `SYS-223`, `SYS-307`–`SYS-315` | world seed, rates and rosters are parameters |
| Constraint | `CON-062`, `CON-192`, `CON-193`, `CON-200`, `CON-210`, `CON-276`–`CON-282` | exact costs, capacities and timers are parameters |
| Information | `INF-059`, `INF-073`, `INF-075`, `INF-122`–`INF-126` | UI layout is a parameter |
| Objective | `OBJ-073` | optional endgame goals are excluded |
| Time | `TIM-003` | live durations are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `138` (`GAME-0001`–`GAME-0138`).
- Exact genome matches: none.
- Tied near matches: `GAME-0129` — Minecraft (`13 / 76 = 0.171053`).
- Supported combination subsets: `COMB-0137`.
- Scan date: 2026-08-21.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0129`.

### Preserved research notes

- New genes: `ACT-194`–`ACT-197`, `SYS-307`, `SYS-308`, `SYS-310`–`SYS-313`,
  `SYS-315`, `CON-276`–`CON-282`,
  `INF-122`–`INF-126`, `OBJ-073`.
- Classification result: `New combination of known and new genes`.
- Evidence and reasoning: capture, party and base share one persistent Pal
  identity but apply different actions, capacities and autonomous resolution;
  no existing gene boundary represented that three-way transfer or probabilistic
  capture. Existing colony, survival and direct-combat genes were reused only
  where their causal definitions remained intact.

## Taxonomy impact

- Registry changes after normalisation: 24 new stable genes and `COMB-0137`;
  `SYS-216` and `SYS-299` are reused; memberships in existing
  families `FAM-008`, `FAM-010`, `FAM-015` and `FAM-017`.
- Taxonomy-change record: `TAXONOMY_CHANGE_013`.
- Candidate terms affected: none.

## Negative results

- No exact full-genome match and no prior verified combination subset.
- `SYS-213` is not reused: Palworld's persistent generated open world is not a
  mutable block-addressable voxel world.
- `SYS-216` is reused with Palworld's current Normal loss mode as its configured
  carried-state-loss parameter; it does not imply Minecraft's full-inventory drop.
- `ACT-189` is not reused: direct avatar locomotion plus limited Pal target
  direction does not become Dota's general destination/attack-move command model.
