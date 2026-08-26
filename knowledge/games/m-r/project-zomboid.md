---
game_id: GAME-0142
slug: project-zomboid
game_title: Project Zomboid
analysis_status: reviewed
reviewed: 2026-08-21
combination_ids:
  - COMB-0140
gene_ids:
  action:
    - ACT-006
    - ACT-008
    - ACT-122
    - ACT-123
    - ACT-161
    - ACT-164
    - ACT-165
    - ACT-199
    - ACT-210
    - ACT-211
    - ACT-212
    - ACT-213
    - ACT-214
  system:
    - SYS-204
    - SYS-208
    - SYS-215
    - SYS-223
    - SYS-328
    - SYS-337
    - SYS-338
    - SYS-339
    - SYS-340
    - SYS-341
    - SYS-342
    - SYS-343
    - SYS-344
    - SYS-345
  constraint:
    - CON-210
    - CON-281
    - CON-303
    - CON-304
    - CON-305
    - CON-306
    - CON-307
    - CON-308
    - CON-309
    - CON-310
    - CON-311
    - CON-312
    - CON-313
    - CON-314
  information:
    - INF-073
    - INF-075
    - INF-115
    - INF-128
    - INF-133
    - INF-134
    - INF-135
    - INF-136
  objective:
    - OBJ-076
  time:
    - TIM-003
---

# Game: Project Zomboid

## Analysis scope

- Version / ruleset: public PC Stable Build `42.20.3`; one fresh unmodded
  single-player `Apocalypse` (`Lore Canon`) life, starting in Muldraugh with a
  legal zero-net-point occupation and trait loadout, from character creation to
  that survivor's irreversible death.
- Included: occupation and traits; direct movement, stealth and combat; local
  sight and emitted noise; looting, inventory, food, crafting and durability;
  body-part wounds, treatment, ordinary wound infection and concealed Knox
  Infection; moodles, sleep and selectable time rate; skill experience;
  barricading and basic shelter construction; utility shutoff, spoilage,
  weather, seasons and one persistent crop.
- Reproducible thirty-day checkpoint: secure one ordinary dwelling, barricade
  every reachable ground-floor opening, establish stored food and water, and
  plant and maintain one season-valid crop through day 30. The same life then
  continues until permanent death; the checkpoint is analytical, not victory.
- Excluded: multiplayer and split-screen co-op; Custom Sandbox, Outbreak,
  Rising, Extinction and Challenges; mods, debug and administrator tools;
  vehicles; animals, hunting, trapping and fishing; exhaustive foraging,
  blacksmithing, masonry and other advanced crafting; Louisville completion,
  collection goals and any later character in the retained save.
- Direct-play status: no complete thirty-day-to-death run was performed.
  Current official release, feature and mode material plus maintained official
  wiki mechanics establish the scoped transitions.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `PZ-001` | Apocalypse has no authored victory; the scoped objective is to extend one life until inevitable irreversible death | Confirmed | Direct | High | P1, P2 |
| `PZ-002` | Build 42 combines authored Knox Country with seed-controlled generated basements, wilderness, zombie distribution and randomized interiors | Confirmed | Direct | High | P3, P4 |
| `PZ-003` | Occupation and balanced traits set starting skills and modifiers, while eligible work later advances personal skills | Observation | Corroborated | High | P3, P5, P6 |
| `PZ-004` | Hunger, thirst, fatigue, exertion, panic, stress, temperature, pain and sickness become graded moodles that constrain live action | Observation | Corroborated | High | P1, P5 |
| `PZ-005` | Zombies react to locally perceived movement and emitted sound rather than receiving omniscient survivor position | Observation | Corroborated | High | P1, P5, P7 |
| `PZ-006` | Combat resolves reach, body state, weapon condition, aim and protection into body-part injury and impaired capacity | Observation | Corroborated | High | P3, P5 |
| `PZ-007` | Body-region treatments can stop bleeding or improve ordinary wound recovery, but established Knox Infection remains concealed, incurable and fatal | Confirmed | Corroborated | High | P1, P5, P8 |
| `PZ-008` | Barricades and basic construction persistently alter access and sight, require compatible tools and material, and can be broken by concentrated attacks | Confirmed | Corroborated | High | P3, P4, P9 |
| `PZ-009` | Calendar time drives weather, seasonal crops, food spoilage and finite inherited water or electrical service | Confirmed | Corroborated | High | P3, P4, P10 |
| `PZ-010` | Lethal state permanently ends the current character while the retained body may reanimate and the world may outlive that life | Confirmed | Direct | High | P1, P5 |
| `PZ-011` | Sleep and accelerated timed actions advance the same vulnerable world and may return control after interruption | Observation | Corroborated | High | P1, P5 |

## Basic data

- Release / origin: The Indie Stone; Early Access since 2013; Build 42 reached
  Stable in July 2026 and the reviewed public header reports `42.20.3`.
- Platform or physical form: isometric real-time PC survival simulation.
- Puzzle family: real-time system pressure; inventory and fixture dependencies;
  world topology and perspective; tactical forecast and counterplay.
- Primary sources:
  - **[P1]** [official game overview](https://projectzomboid.com/blog/the-game/),
    for embodied survival, scavenging, construction, depression, infection and
    inevitable death.
  - **[P2]** [official Steam page](https://store.steampowered.com/app/108600/Project_Zomboid/),
    for the single-survivor premise and current public product boundary.
  - **[P3]** [official Build 42.20 feature overview](https://projectzomboid.com/blog/features-overview-build-42-20/),
    for the current map, seed, seasonal farming, crafting, traits, aiming,
    containers, placement and stable-build header.
  - **[P4]** [official Build 42.20 release](https://projectzomboid.com/blog/news/2026/07/project-zomboid-build-42-20-released/),
    for the public Stable transition.
  - **[P5]** [official status and build history](https://projectzomboid.com/blog/news/2017/02/buildstatus/),
    for sneaking, injury, clothing protection, cutaway vision, temperature,
    health, infection, skills, reanimation, erosion and endurance.
  - **[P6]** [official Build 42 occupation balancing](https://projectzomboid.com/blog/news/2026/03/balancing-time/),
    for current occupation, trait, skill and discomfort boundaries.
  - **[P7]** [official sound-system update](https://projectzomboid.com/blog/news/2021/07/jumps-n-scares/),
    for audible zombies, doors, windows and tactical local sound.
  - **[P8]** [official PZwiki Bandage entry](https://pzwiki.net/wiki/Bandage),
    for body-panel application, bleeding, dirty or sterilized states and
    ordinary wound infection treatment.
  - **[P9]** [official PZwiki Window entry](https://pzwiki.net/wiki/Window), for
    climbing, breakage, glass injury, curtains and material barricades that
    trade protection against visibility.
  - **[P10]** [official Apocalypse mode refresh](https://projectzomboid.com/blog/news/2026/03/some-new-things/),
    for Lore Canon defaults, crop seasons, authentic 1993 resource balance,
    disabled zombie respawn and fences vulnerable to concentrated attacks.
- Secondary sources: none admitted.
- Claim IDs: `PZ-001`–`PZ-011`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-006`, accelerate automatic progression; `ACT-008`,
  navigate; `ACT-122`, dismantle or extract; `ACT-123`, hand-craft;
  `ACT-161`, direct attack; `ACT-164`, quick-slot selection; `ACT-165`, eat;
  `ACT-199`, transfer or equip visible loot.
- New genes: `ACT-210`, configure occupation and traits; `ACT-211`, treat one
  body wound; `ACT-212`, attach or remove a barricade layer; `ACT-213`, plant,
  tend or harvest; `ACT-214`, sleep.
- Claim IDs: `PZ-003`–`PZ-009`, `PZ-011`.

### System Behaviour Genes

- Existing genes: `SYS-204`, body-part condition into capacities; `SYS-208`,
  aimed ranged resolution; `SYS-215`, direct hostile combat; `SYS-223`, tool
  durability; `SYS-328`, personal crafting queue.
- New genes: `SYS-337`–`SYS-345`, covering seeded Knox Country, moodles,
  zombie perception, interruptible timed actions, Knox Infection, personal
  skill growth, persistent defence geometry, calendar ecology and permanent death.
- Resolution order: initialise one seeded Apocalypse world and survivor; advance
  perception, needs and calendar under live time; resolve queued actions and
  combat through body state; persist constructions and crops; terminate the
  scoped identity at lethal bodily state.
- Claim IDs: `PZ-002`–`PZ-011`.

### Constraint Genes

- Existing genes: `CON-210`, typed stack-and-slot inventory; `CON-281`,
  embodied survival requires compatible equipment and resources.
- New genes: `CON-303`–`CON-314`, covering character-point legality, body-state
  performance, perceived zombie pursuit, viable weapons, wound care,
  incurable Knox Infection, barricades, learned production, seasonal crops,
  vulnerable sleep, one-life death and finite long-horizon supplies.
- Scarce strategic resources: quiet time, daylight and safe routes; calories,
  clean water and sleep; carry capacity and weapon condition; bandages, tools,
  fasteners and planks; skill time; viable seed season and protected crop days.
- Claim IDs: `PZ-003`–`PZ-011`.

### Information Genes

- Existing genes: `INF-073`, hotbar/equipment; `INF-075`, survival and
  durability state; `INF-115`, partial local hostile sight and sound;
  `INF-128`, loot identity and inventory compatibility.
- New genes: `INF-133`, graded moodles; `INF-134`, body health panel;
  `INF-135`, local isometric cutaway; `INF-136`, calendar and infrastructure.
- Claim IDs: `PZ-003`–`PZ-009`, `PZ-011`.

### Objective Genes

- New gene: `OBJ-076`, extend one current survivor life until irreversible death.
- Evaluation: a kill, safehouse, planted crop, skill level or day-30 checkpoint
  is non-terminal; death fixes the life duration without declaring a victory.
- Claim IDs: `PZ-001`, `PZ-010`.

### Time Genes

- Existing gene: `TIM-003`, real-time input during forced progression.
- Parameters: ordinary rate, pause, acceleration, sleep, timed-action duration,
  calendar date, utility window and terminal death instant.
- Claim IDs: `PZ-004`–`PZ-011`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Character creator has one occupation and candidate traits | Add or remove traits until balance and compatibility are legal; confirm | Starting skills and persistent modifiers are written to the new survivor | Creation is a constrained build, not cosmetic selection | `PZ-003` |
| Closed room contains unseen zombies or exterior movement | Move quietly, shout, strike an opening or fire | Eligible cues attract only zombies that perceive them; broken barriers may make a route | Noise changes hostile routing without omniscience | `PZ-005` |
| Zombie reaches melee range | Shove, evade or attack; permit one hostile hit for the injury trace | Facing, exertion, weapon and protection resolve damage to a body region | Combat and bodily consequence are distinct | `PZ-006` |
| Health panel shows a bleeding wound and a compatible bandage is carried | Apply the bandage to that region | A timed action consumes or transforms the item, stops active bleeding and records treatment | Care is location- and item-specific | `PZ-007` |
| Eligible window, hammer, nails and planks are reachable | Add successive planks, then remove one | Layers persist, resist entry and progressively change sight; legal removal returns material | Fortification trades access and information | `PZ-008` |
| Known recipe, tools and reachable ingredients are present | Queue craft at normal and accelerated rates | Inputs become output after live duration; danger can interrupt acceleration | Time controls do not make production safe | `PZ-004`, `PZ-011` |
| Viable plot and season-compatible seed exist | Sow, water and inspect across calendar time | Crop advances only under species, season, water and health rules toward yield or failure | Renewable food is a long-horizon state machine | `PZ-009` |
| Default utility window or perishable age boundary is crossed | Continue ordinary survival time | Service may end and food ages despite shelter; stored alternatives become necessary | Starting infrastructure is finite | `PZ-009` |
| Zombie-transmitted wound establishes Knox Infection | Apply ordinary care and continue time | Visible care may manage the wound but cannot clear infection; sickness reaches death and possible reanimation | Medical legibility stops short of a cure | `PZ-007`, `PZ-010` |
| Any lethal body state is reached | No further input for that survivor | Current identity permanently loses control; retained save state does not respawn the same life | Death is the terminal analytical boundary | `PZ-010` |

## Strategic and experiential structure

- Local decision: move quietly or quickly, inspect an opening, choose a target,
  manage distance and exertion, loot under exposure, or spend vulnerable time
  on treatment, sleep, crafting and fortification.
- Medium-term planning: convert a dwelling into layered shelter, maintain clean
  water and food, train prerequisite skills, preserve tools and establish a
  season-valid crop before inherited infrastructure declines.
- Long-term structure: reduce correlated failure by separating supplies,
  escape routes and noise sources while adapting to bodily deterioration and
  a calendar that removes early abundance.
- Common heuristics: clear before looting, break line of sight before resting,
  cover ground-floor openings without erasing every view, carry wound care,
  avoid fighting while exhausted or panicked, and treat every noisy action as
  a route change for nearby zombies.
- Failure attribution: moodles, body panel and local sound explain many causes;
  hidden zombie positions, loot, utility dates and Knox transmission preserve
  consequential uncertainty.
- Claim IDs: `PZ-003`–`PZ-011`.

## Replay and variation

- What changes: seed-generated locations and interiors, loot, zombie
  distribution, character build, weather, utility dates, wounds, infection,
  shelter route, crop timing and eventual cause or date of death.
- Randomness or procedural generation: one seed stabilises generated world
  elements, while loot, encounters, transmission and schedules provide bounded
  uncertainty within the canonical preset.
- Multiple viable strategies: urban scavenging or quieter outskirts; melee
  avoidance or selective combat; compact safehouse or distributed caches;
  fresh-food consumption or early preservation and farming.
- Typical replay motive: a new emergent death history under a different body,
  seed, shelter and long-horizon scarcity trajectory.
- Claim IDs: `PZ-001`–`PZ-011`.

## Adjacent systems and history

- Rust is nearest because both join direct survival, looting, crafting,
  durability, construction and partial hostile information under live time;
  Project Zomboid replaces shared ownership, respawn and wipe with one body's
  moodles, infection and permanent death.
- Palworld shares embodied survival and persistent production, but autonomous
  captured workers and a story finale replace vulnerable solo timed actions.
- PUBG shares found loadouts, direct combat and one-life defeat, but its world
  contracts into a short match rather than aging through utilities and seasons.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-006`, `ACT-008`, `ACT-122`, `ACT-123`, `ACT-161`, `ACT-164`, `ACT-165`, `ACT-199`, `ACT-210`–`ACT-214` | control bindings and item identities are parameters |
| System Behaviour | `SYS-204`, `SYS-208`, `SYS-215`, `SYS-223`, `SYS-328`, `SYS-337`–`SYS-345` | rates, wound chances and seed values are parameters |
| Constraint | `CON-210`, `CON-281`, `CON-303`–`CON-314` | costs, thresholds and dates are parameters |
| Information | `INF-073`, `INF-075`, `INF-115`, `INF-128`, `INF-133`–`INF-136` | exact HUD layout is presentation |
| Objective | `OBJ-076` | day 30 is a checkpoint, not terminal victory |
| Time | `TIM-003` | pause, speed and sleep are ruleset parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `141` (`GAME-0001`–`GAME-0141`).
- Exact genome matches: none.
- Tied near matches: `GAME-0141` — Rust (`18 / 84 = 0.214286`).
- Supported combination subsets: `COMB-0140`.
- Scan date: 2026-08-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| Rust (`GAME-0141`) | direct survival, gathering, crafting, loot, durability, combat, body information, construction pressure and live time | shared-world respawn, ownership, upkeep and wipe versus one vulnerable body's moodles, infection, calendar and permanent death | Near, `0.214286` |

### Preserved research notes

- New genes: `ACT-210`–`ACT-214`, `SYS-337`–`SYS-345`,
  `CON-303`–`CON-314`, `INF-133`–`INF-136` and `OBJ-076` (31 total).
- Classification: `New gene` and `New combination of known and new genes`.

## Taxonomy impact

- Registry changes: add 31 bounded active genes and `COMB-0140`; extend
  `SYS-204` to another body-part capacity system while preserving the boundary
  between ordinary wound state and irreversible Knox Infection.
- Taxonomy-change record: none.
- Candidate terms: safehouse, moodle, helicopter event and day-30 checkpoint
  remain game vocabulary, parameters or scenario structure rather than atoms.

## Negative results

- No earlier verified combination is a proper subset of the scoped genome.
- No authored terminal win or stable post-scarcity state was found; day 30,
  shelter completion and crop establishment remain analytical milestones.
- The later-character option was excluded rather than misclassified as a
  respawn, because character identity and one-life objective do not continue.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] `PZ-001`–`PZ-011`: canonical Apocalypse
  couples partial local perception, bodily needs and wounds, irreversible
  infection, fortification and calendar attrition into one permanent life.

## Нові гени

- [Observation | Corroborated | High] Added `ACT-210`–`ACT-214`,
  `SYS-337`–`SYS-345`, `CON-303`–`CON-314`, `INF-133`–`INF-136` and
  `OBJ-076`.

## Нові комбінації

- [Confirmed | Corroborated | High] `COMB-0140` — locally perceived embodied
  survival through fortification and long-horizon decay to permanent death.

## Зміни таксономії

- [Observation | Direct | High] Змін таксономії немає.

## Нові питання

- Does ARC Raiders preserve the one-life resource and information pressure
  while replacing permanent local death with extraction and recoverable stash?

## Наступна рекомендована гра

- [Hypothesis | Limited | High] `GAME-0143` — ARC Raiders.
- Optimisation criterion: preserve the authorised search-demand sequence.
- Expected information gain: contrast permanent embodied death and shelter
  persistence with extraction, external stash and hostile machine pressure.
- Backlog impact: advances the current 17-game Goal by one independent unit.

## Чому саме вона

- [Hypothesis | Limited | High] ARC Raiders should retain direct looting,
  partial hostile information and one-life field danger while testing whether
  extraction and account-level recovery form a different terminal structure.
