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
    - SYS-222
    - SYS-223
    - SYS-307
    - SYS-308
    - SYS-309
    - SYS-310
    - SYS-311
    - SYS-312
    - SYS-313
    - SYS-314
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
  `SYS-223`, equipment durability loss.
- New genes: `SYS-307`, probabilistic capture into storage; `SYS-308`, deployed
  companion follow/combat; `SYS-309`, persistent player/Pal experience levels;
  `SYS-310`, work-suitability base dispatch; `SYS-311`, Pal hunger/SAN/condition;
  `SYS-312`, material-backed crafting/construction workload; `SYS-313`,
  persistent generated survival world; `SYS-314`, defeat/drop/respawn;
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

- Genome signature `(ACT; SYS; CON; INF; OBJ; TIM)`: `ACT-008,ACT-087,ACT-122,ACT-123,ACT-134,ACT-145,ACT-148,ACT-161,ACT-164,ACT-165,ACT-194,ACT-195,ACT-196,ACT-197; SYS-004,SYS-045,SYS-051,SYS-186,SYS-196,SYS-197,SYS-215,SYS-222,SYS-223,SYS-307,SYS-308,SYS-309,SYS-310,SYS-311,SYS-312,SYS-313,SYS-314,SYS-315; CON-062,CON-192,CON-193,CON-200,CON-210,CON-276,CON-277,CON-278,CON-279,CON-280,CON-281,CON-282; INF-059,INF-073,INF-075,INF-122,INF-123,INF-124,INF-125,INF-126; OBJ-073; TIM-003`.
- Indexed games scanned: 138 (`GAME-0001`–`GAME-0138`).
- Indexed combinations scanned: 136 (`COMB-0001`–`COMB-0136`).
- Exact genome matches: none.
- Near match: RimWorld (`GAME-0127`) at `14 / 88 = 0.159091`, sharing
  autonomous worker routing, construction, hauling, work condition and live time.
- Supported prior combination subsets: none.
- Scan date: 2026-08-21.

### Exhaustive prior-game similarity scan

- GAME-0001: 1 / 67 = 0.014925; GAME-0002: 0 / 61 = 0.000000; GAME-0003: 0 / 63 = 0.000000; GAME-0004: 2 / 67 = 0.029851.
- GAME-0005: 0 / 61 = 0.000000; GAME-0006: 1 / 62 = 0.016129; GAME-0007: 0 / 62 = 0.000000; GAME-0008: 0 / 61 = 0.000000.
- GAME-0009: 1 / 69 = 0.014493; GAME-0010: 0 / 63 = 0.000000; GAME-0011: 0 / 67 = 0.000000; GAME-0012: 0 / 63 = 0.000000.
- GAME-0013: 0 / 67 = 0.000000; GAME-0014: 0 / 69 = 0.000000; GAME-0015: 1 / 67 = 0.014925; GAME-0016: 2 / 67 = 0.029851.
- GAME-0017: 0 / 67 = 0.000000; GAME-0018: 2 / 71 = 0.028169; GAME-0019: 0 / 64 = 0.000000; GAME-0020: 1 / 67 = 0.014925.
- GAME-0021: 1 / 62 = 0.016129; GAME-0022: 1 / 65 = 0.015385; GAME-0023: 0 / 64 = 0.000000; GAME-0024: 1 / 65 = 0.015385.
- GAME-0025: 2 / 63 = 0.031746; GAME-0026: 1 / 65 = 0.015385; GAME-0027: 3 / 63 = 0.047619; GAME-0028: 4 / 67 = 0.059701.
- GAME-0029: 3 / 63 = 0.047619; GAME-0030: 2 / 66 = 0.030303; GAME-0031: 1 / 64 = 0.015625; GAME-0032: 0 / 65 = 0.000000.
- GAME-0033: 2 / 65 = 0.030769; GAME-0034: 3 / 65 = 0.046154; GAME-0035: 3 / 69 = 0.043478; GAME-0036: 1 / 65 = 0.015385.
- GAME-0037: 0 / 63 = 0.000000; GAME-0038: 2 / 68 = 0.029412; GAME-0039: 0 / 63 = 0.000000; GAME-0040: 1 / 61 = 0.016393.
- GAME-0041: 2 / 63 = 0.031746; GAME-0042: 1 / 62 = 0.016129; GAME-0043: 1 / 67 = 0.014925; GAME-0044: 1 / 63 = 0.015873.
- GAME-0045: 1 / 67 = 0.014925; GAME-0046: 0 / 64 = 0.000000; GAME-0047: 0 / 68 = 0.000000; GAME-0048: 0 / 68 = 0.000000.
- GAME-0049: 0 / 63 = 0.000000; GAME-0050: 1 / 68 = 0.014706; GAME-0051: 2 / 68 = 0.029412; GAME-0052: 0 / 64 = 0.000000.
- GAME-0053: 1 / 62 = 0.016129; GAME-0054: 1 / 64 = 0.015625; GAME-0055: 1 / 63 = 0.015873; GAME-0056: 0 / 62 = 0.000000.
- GAME-0057: 0 / 62 = 0.000000; GAME-0058: 0 / 63 = 0.000000; GAME-0059: 0 / 61 = 0.000000; GAME-0060: 0 / 61 = 0.000000.
- GAME-0061: 0 / 64 = 0.000000; GAME-0062: 0 / 62 = 0.000000; GAME-0063: 0 / 61 = 0.000000; GAME-0064: 0 / 59 = 0.000000.
- GAME-0065: 0 / 61 = 0.000000; GAME-0066: 0 / 64 = 0.000000; GAME-0067: 1 / 61 = 0.016393; GAME-0068: 0 / 62 = 0.000000.
- GAME-0069: 0 / 62 = 0.000000; GAME-0070: 0 / 62 = 0.000000; GAME-0071: 0 / 61 = 0.000000; GAME-0072: 0 / 62 = 0.000000.
- GAME-0073: 0 / 61 = 0.000000; GAME-0074: 0 / 63 = 0.000000; GAME-0075: 0 / 63 = 0.000000; GAME-0076: 0 / 61 = 0.000000.
- GAME-0077: 0 / 61 = 0.000000; GAME-0078: 0 / 61 = 0.000000; GAME-0079: 0 / 61 = 0.000000; GAME-0080: 0 / 61 = 0.000000.
- GAME-0081: 0 / 62 = 0.000000; GAME-0082: 0 / 62 = 0.000000; GAME-0083: 0 / 62 = 0.000000; GAME-0084: 0 / 64 = 0.000000.
- GAME-0085: 1 / 64 = 0.015625; GAME-0086: 1 / 66 = 0.015152; GAME-0087: 2 / 62 = 0.032258; GAME-0088: 0 / 63 = 0.000000.
- GAME-0089: 0 / 63 = 0.000000; GAME-0090: 1 / 68 = 0.014706; GAME-0091: 2 / 61 = 0.032787; GAME-0092: 2 / 62 = 0.032258.
- GAME-0093: 0 / 63 = 0.000000; GAME-0094: 2 / 62 = 0.032258; GAME-0095: 2 / 64 = 0.031250; GAME-0096: 2 / 62 = 0.032258.
- GAME-0097: 2 / 60 = 0.033333; GAME-0098: 2 / 59 = 0.033898; GAME-0099: 1 / 61 = 0.016393; GAME-0100: 1 / 64 = 0.015625.
- GAME-0101: 0 / 64 = 0.000000; GAME-0102: 0 / 61 = 0.000000; GAME-0103: 0 / 63 = 0.000000; GAME-0104: 1 / 62 = 0.016129.
- GAME-0105: 2 / 62 = 0.032258; GAME-0106: 0 / 61 = 0.000000; GAME-0107: 1 / 61 = 0.016393; GAME-0108: 1 / 63 = 0.015873.
- GAME-0109: 1 / 69 = 0.014493; GAME-0110: 1 / 61 = 0.016393; GAME-0111: 1 / 60 = 0.016667; GAME-0112: 2 / 60 = 0.033333.
- GAME-0113: 2 / 66 = 0.030303; GAME-0114: 1 / 60 = 0.016667; GAME-0115: 0 / 60 = 0.000000; GAME-0116: 2 / 58 = 0.034483.
- GAME-0117: 1 / 61 = 0.016393; GAME-0118: 1 / 69 = 0.014493; GAME-0119: 7 / 70 = 0.100000; GAME-0120: 1 / 82 = 0.012195.
- GAME-0121: 1 / 76 = 0.013158; GAME-0122: 3 / 66 = 0.045455; GAME-0123: 2 / 90 = 0.022222; GAME-0124: 5 / 96 = 0.052083.
- GAME-0125: 10 / 86 = 0.116279; GAME-0126: 12 / 85 = 0.141176; GAME-0127: 14 / 88 = 0.159091; GAME-0128: 5 / 65 = 0.076923.
- GAME-0129: 12 / 77 = 0.155844; GAME-0130: 5 / 102 = 0.049020; GAME-0131: 9 / 91 = 0.098901; GAME-0132: 3 / 102 = 0.029412.
- GAME-0133: 7 / 92 = 0.076087; GAME-0134: 5 / 100 = 0.050000; GAME-0135: 6 / 96 = 0.062500; GAME-0136: 11 / 103 = 0.106796.
- GAME-0137: 7 / 77 = 0.090909; GAME-0138: 4 / 85 = 0.047059.

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| RimWorld (`GAME-0127`) | `ACT-008`, `ACT-145`, `ACT-148`, `SYS-045`, `SYS-051`, `SYS-186`, `SYS-196`, `SYS-197`, `CON-192`, `CON-193`, `CON-200`, `INF-059`, `INF-075`, `TIM-003` | direct capture/party combat and embodied survival versus policy-led human colony simulation and ship construction | nearest at `14 / 88 = 0.159091` |

- New genes: `ACT-194`–`ACT-197`, `SYS-307`–`SYS-315`, `CON-276`–`CON-282`,
  `INF-122`–`INF-126`, `OBJ-073`.
- Classification result: `New combination of known and new genes`.
- Evidence and reasoning: capture, party and base share one persistent Pal
  identity but apply different actions, capacities and autonomous resolution;
  no existing gene boundary represented that three-way transfer or probabilistic
  capture. Existing colony, survival and direct-combat genes were reused only
  where their causal definitions remained intact.

## Taxonomy impact

- Registry changes: new stable genes and `COMB-0137`; memberships in existing
  families `FAM-008`, `FAM-010`, `FAM-015` and `FAM-017`.
- Taxonomy-change record: none; no earlier gene is revised or deprecated.
- Candidate terms affected: none.

## Negative results

- No exact full-genome match and no prior verified combination subset.
- `SYS-213` is not reused: Palworld's persistent generated open world is not a
  mutable block-addressable voxel world.
- `SYS-216` is not reused: Palworld's current default Normal loss boundary is
  world-setting-dependent rather than Minecraft's fixed full-inventory drop.
- `ACT-189` is not reused: direct avatar locomotion plus limited Pal target
  direction does not become Dota's general destination/attack-move command model.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Palworld 1.0.3 couples probabilistic capture,
  persistent party combat and suitability-gated base work through the same Pal roster (`PAL-002`–`PAL-004`).
- [Confirmed | Corroborated | High] The released main story now terminates in
  the ordered World Tree finale (`PAL-006`).

## Нові гени

- [Observation | Corroborated | High] Added 26 bounded capture, companion,
  base-work, survival, mission, information and ending genes.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0137` joins probabilistic capture
  to persistent companion transfer, combat and autonomous base labour.

## Зміни таксономії

- [Observation | Corroborated | High] No taxonomy-change record; four existing
  family memberships are reused.

## Нові питання

- Does a later reviewed creature-work game recur the strict capture-to-labour
  subset without Palworld's story or survival layers?

## Наступна рекомендована гра

- [Hypothesis | Limited | Medium] `GAME-0140` PUBG: BATTLEGROUNDS.
- Optimisation criterion: follow the authorised demand-led queue without skipping.
- Expected information gain: test shrinking-zone last-survivor combat against
  existing live tactical and partial-information genes.
- Backlog impact: advances the active 17-game Goal by one unit.

## Чому саме вона

- [Hypothesis | Limited | Medium] PUBG should reuse embodied shooter and
  incomplete-information boundaries while testing a new spatial contraction,
  loot and last-survivor objective combination.
