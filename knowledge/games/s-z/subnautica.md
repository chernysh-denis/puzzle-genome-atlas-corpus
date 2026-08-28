---
game_id: GAME-0178
slug: subnautica
game_title: Subnautica
analysis_status: reviewed
reviewed: 2026-08-28
combination_ids:
  - COMB-0176
gene_ids:
  action:
    - ACT-008
    - ACT-123
    - ACT-164
    - ACT-165
    - ACT-201
    - ACT-245
    - ACT-311
    - ACT-312
    - ACT-313
    - ACT-314
    - ACT-315
  system:
    - SYS-216
    - SYS-320
    - SYS-327
    - SYS-543
    - SYS-544
    - SYS-545
    - SYS-546
    - SYS-547
    - SYS-548
  constraint:
    - CON-394
    - CON-460
    - CON-461
    - CON-462
    - CON-463
    - CON-464
    - CON-465
  information:
    - INF-073
    - INF-075
    - INF-132
    - INF-223
  objective:
    - OBJ-102
  time:
    - TIM-003
---

# Game: Subnautica

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: original Subnautica on PC/Steam after the official 2025
  Patch released 2025-08-12; vanilla single-player Survival mode, fresh save,
  no console commands or mods.
- Primary decision loop: leave Lifepod 5, watch oxygen and depth while swimming,
  collect minerals and small fauna, return to breathable space, fabricate
  sustenance, tools and components, scan fragments into blueprints, construct a
  positive-integrity solar-powered habitat, fabricate a Mobile Vehicle Bay and
  the first unmodified Seamoth, then pilot it back within safe depth.
- Entry and exit: begins after the opening crash in Lifepod 5 with Survival
  health, food and water active; ends after the first player-built Seamoth is
  parked outside the scoped powered habitat and the survivor exits it, enters
  the dry habitat and restores oxygen without a hull breach.
- Included: swimming and surface breathing; oxygen, health, food and water;
  catching edible small fauna and collecting finite material yields; carried
  inventory and quick slots; the Lifepod Fabricator; known recipes and
  ingredient conversion; Scanner battery, range, held progress and fragment
  thresholds; Habitat Builder placement and deconstruction; one I Compartment,
  Hatch and Solar Panel; base hull integrity, flooding, power and oxygen; a
  deployable Mobile Vehicle Bay; first Seamoth fabrication, entry, piloting,
  energy, collision damage and the unmodified 200 m crush-depth boundary;
  ordinary Survival death, secured inventory and respawn.
- Excluded: radio-message or Aurora-story progression; infection, radiation and
  the Aurora explosion; islands, Degasi bases, alien facilities and campaign
  escape; Scanner Room, Moonpool, Vehicle Upgrade Console and every vehicle
  upgrade; Cyclops, Prawn Suit and Neptune rocket; caves or dives requiring more
  than the unmodified Seamoth's 200 m crush depth; Freedom, Hardcore and Creative
  modes; multiplayer, VR-specific input, mods, Below Zero and Subnautica 2.
- Potential scoped modules: Aurora repair and radiation route; Moonpool and
  depth-module progression; Cyclops/Prawn production; complete cure-and-escape
  campaign.
- Direct-play status: not conducted. The current official patch and Steam
  product page establish the reviewed PC boundary and core oxygen, collecting,
  crafting, habitat, hull and submersible loop. Stable numeric thresholds and
  transition details are corroborated by the original-game community wiki.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SUB-001` | The reviewed PC boundary is the original single-player game after the official 2025 Patch | Confirmed | Direct | High | P1, P2 |
| `SUB-002` | Survival continuously couples oxygen, health, food and water to real-time exploration and death | Observation | Corroborated | High | P2, S1–S3 |
| `SUB-003` | Surface air, Lifepod 5, a powered habitat and a powered vehicle replenish the survivor's oxygen | Observation | Corroborated | High | S1, S4 |
| `SUB-004` | Collected resources and fauna enter a rectangular carried inventory and legal Fabricator recipes consume ingredients into outputs | Observation | Corroborated | High | P2, S5, S6 |
| `SUB-005` | A held powered Scanner records interruptible target progress and unlocks a blueprint only after its required fragments | Confirmed | Corroborated | High | S7, S8 |
| `SUB-006` | The Mobile Vehicle Bay and Seamoth each require three scanned fragments before their recipes are available | Confirmed | Corroborated | High | S6, S8, S9 |
| `SUB-007` | Habitat Builder placement consumes materials, joins modules and changes hull integrity; non-positive integrity causes breaches and flooding | Observation | Corroborated | High | P2, S10, S11 |
| `SUB-008` | A solar-powered habitat provides oxygen and power to connected functions; an unpowered habitat does not | Confirmed | Corroborated | High | S4, S10, S12 |
| `SUB-009` | The Mobile Vehicle Bay is deployed into the world and fabricates a legal unlocked vehicle from supplied materials | Observation | Corroborated | High | S9 |
| `SUB-010` | The first unmodified Seamoth is a powered one-person vehicle with independent oxygen and a 200 m crush depth | Confirmed | Corroborated | High | S13 |
| `SUB-011` | Ordinary Survival death respawns the survivor at the last secured habitat and applies a scoped carried-item loss while preserving the world | Observation | Corroborated | High | S2, S3 |

## Basic data

- Release / origin: Unknown Worlds Entertainment; released 2018; reviewed PC
  rules include the 2025 Patch released 2025-08-12.
- Platform or physical form: first-person single-player underwater survival on
  PC/Steam.
- Puzzle family: real-time system pressure; knowledge and evidence progression;
  inventory and fixture dependencies; world topology and perspective; ordered
  dependency sequencing.
- Primary sources:
  - **[P1]** [official Subnautica 2025 Patch](https://www.unknownworlds.com/en/news/subnautica-2025-patch),
    for the current reviewed PC patch boundary and continued Seamoth, Seabase,
    oxygen and hunger semantics.
  - **[P2]** [official Steam product page](https://store.steampowered.com/app/264710/Subnautica/),
    for original-game single-player scope and the oxygen, resource, crafting,
    submersible, habitat, hull-integrity and base-oxygen loop.
- Secondary sources:
  - **[S1]** [Oxygen](https://subnautica.fandom.com/wiki/Oxygen), for depletion,
    surface refill and powered interior sources.
  - **[S2]** [Game Modes](https://subnautica.fandom.com/wiki/Game_Modes), for
    Survival meters, secured inventory and ordinary death.
  - **[S3]** [Getting Started](https://subnautica.fandom.com/wiki/Getting_Started),
    for the Lifepod 5 entry, early equipment loop and respawn boundary.
  - **[S4]** [Seabases](https://subnautica.fandom.com/wiki/Seabases_%28Subnautica%29),
    for power sources, oxygen and connected appliance demand.
  - **[S5]** [Food & Water](https://subnautica.fandom.com/wiki/Food_%26_Water),
    for Survival depletion and consumable restoration.
  - **[S6]** [Fabricator](https://subnautica.fandom.com/wiki/Fabricator_%28Subnautica%29),
    for recipe legality, output handling and energy use.
  - **[S7]** [Scanner](https://subnautica.fandom.com/wiki/Scanner_%28Subnautica%29),
    for range, battery, interruptible scan progress and blueprint acquisition.
  - **[S8]** [Blueprints](https://subnautica.fandom.com/wiki/Blueprints_%28Subnautica%29),
    for persistent fragment-threshold unlocks and reusable recipes.
  - **[S9]** [Mobile Vehicle Bay](https://subnautica.fandom.com/wiki/Mobile_Vehicle_Bay_%28Subnautica%29),
    for three-fragment acquisition, deployment and vehicle fabrication.
  - **[S10]** [Habitat Builder](https://subnautica.fandom.com/wiki/Habitat_Builder_%28Subnautica%29),
    for the I Compartment, Hatch and Solar Panel quick-start contract.
  - **[S11]** [Hull Integrity](https://subnautica.fandom.com/wiki/Hull_Integrity),
    for the base value, module changes, breaches and flooding.
  - **[S12]** [Solar Panel](https://subnautica.fandom.com/wiki/Solar_Panel_%28Subnautica%29),
    for shallow-light generation and base power storage.
  - **[S13]** [Seamoth](https://subnautica.fandom.com/wiki/Seamoth), for the
    one-person Power Cell, oxygen, damage and unmodified 200 m crush depth.
- Reproducible control: **[V1]** repository-side transition trace across P1–P2
  and S1–S13; rules reasoning, not a claim of direct play.
- Claim IDs: `SUB-001`–`SUB-011`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, swim and move through traversable space;
  `ACT-123`, commit a known recipe; `ACT-164`, select a carried tool;
  `ACT-165`, consume food; `ACT-201`, enter and pilot the Seamoth; `ACT-245`,
  gather a finite material yield.
- New genes: `ACT-311`, consume a carried drink; `ACT-312`, catch one reachable
  free-swimming small organism; `ACT-313`, hold a Scanner on a target;
  `ACT-314`, build or deconstruct one habitat module; `ACT-315`, deploy or pack
  the Mobile Vehicle Bay.
- Parameters: swimming direction, depth, target, reach, tool, battery, scan
  progress, recipe, ingredients, module pose, construction progress, carried
  footprint, vehicle seat and exit state.
- Claim IDs: `SUB-002`–`SUB-010`.

### System Behaviour Genes

- Existing genes: `SYS-216`, apply Survival loss and respawn in the same world;
  `SYS-320`, integrate an occupied vehicle's motion and damage; `SYS-327`,
  advance health, calories and hydration from activity and consumption.
- New genes: `SYS-543`, deplete and replenish the survivor's oxygen reserve;
  `SYS-544`, accumulate scan progress and unlock fragment-gated blueprints;
  `SYS-545`, resolve one powered Fabricator recipe; `SYS-546`, join habitat
  modules and resolve integrity, breach and flooding; `SYS-547`, generate and
  distribute base power and oxygen; `SYS-548`, consume Seamoth energy and apply
  collision or over-depth damage.
- Resolution order: accept movement, gathering, scanning, building or vehicle
  input; update oxygen and Survival meters; resolve reachable collection and
  inventory fit; advance scanning or fabrication; commit construction and
  integrity; generate and spend habitat or vehicle energy; apply damage and,
  at lethal state, secured-inventory loss and respawn.
- Claim IDs: `SUB-002`–`SUB-011`.

### Constraint Genes

- Existing gene: `CON-394`, carried items require compatible rectangular
  inventory cells or equipment slots.
- New genes: `CON-460`, underwater action is bounded by remaining oxygen and a
  reachable air source; `CON-461`, each fragment blueprint requires its own
  scan count; `CON-462`, crafting requires known recipe, ingredients, capacity
  and the correct available fabricator; `CON-463`, habitat construction requires
  legal placement, material and positive recoverable hull integrity; `CON-464`,
  habitat oxygen and powered functions require connected generation and stored
  energy; `CON-465`, Seamoth motion requires energy and remains safe only within
  the current crush depth.
- Scarce strategic resources: oxygen, daylight and surface distance; carried
  cells; food and water; battery and Power Cell charge; raw materials;
  unscanned fragments; habitat power and integrity; Seamoth safe depth.
- Claim IDs: `SUB-002`–`SUB-010`.

### Information Genes

- Existing genes: `INF-073`, expose quick slots and selected tool; `INF-075`,
  expose immediate Survival meters; `INF-132`, expose blueprint, fragment and
  recipe dependencies.
- New gene: `INF-223`, expose scan progress, depth, habitat power/integrity and
  Seamoth energy, health and crush-depth state at the relevant interfaces.
- Claim IDs: `SUB-002`–`SUB-010`.

### Objective Genes

- New gene: `OBJ-102`, fabricate the first Seamoth and finish safely inside a
  dry powered player-built habitat.
- Success, evaluation and failure: success requires a player-built, operable,
  unmodified Seamoth, a controlled trip within 200 m and re-entry into a powered
  positive-integrity habitat; drowning, lethal Survival depletion, destructive
  vehicle loss or a breached unpowered habitat fails the current attempt but
  not the persistent-world save.
- Claim IDs: `SUB-002`, `SUB-007`–`SUB-011`.

### Time Genes

- Existing gene: `TIM-003`, oxygen, food, water, fauna, construction, power and
  vehicle motion advance in real time while the player acts.
- Claim IDs: `SUB-002`–`SUB-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Survivor is inside Lifepod 5 with active Survival meters | Exit through the hatch and swim downward | Oxygen begins decreasing while depth and surface distance change | Exploration consumes a live breathing budget | `SUB-002`, `SUB-003` |
| Oxygen is low below the surface | Reach the surface or enter a powered interior | Oxygen automatically refills toward capacity | Air access, not inventory alone, closes each early dive | `SUB-003` |
| A reachable outcrop, loose resource or small fish is in view | Gather the yield or catch the organism | The item enters compatible free inventory cells; otherwise collection is blocked | Spatial collection is coupled to carried capacity | `SUB-004` |
| Lifepod Fabricator shows a known recipe with all ingredients | Select one output | Ingredients are consumed, fabrication runs and the output becomes collectable | Recipe knowledge and material conversion are separate states | `SUB-004` |
| Scanner has charge and an unscanned MVB fragment is within range | Hold scan until completion | Target progress completes and the blueprint counter advances by one | World observation becomes persistent fabrication knowledge | `SUB-005`, `SUB-006` |
| Three MVB and three Seamoth fragments have been scanned | Inspect the PDA blueprint list | Both recipes are unlocked for repeated legal fabrication | Separate fragment thresholds gate station and vehicle | `SUB-006` |
| Builder has materials at a legal shallow pose | Build I Compartment, Hatch and Solar Panel | Modules join one habitat, consume materials, change integrity and begin solar charging | Geometry, hull and energy are co-produced | `SUB-007`, `SUB-008` |
| Habitat has positive integrity and stored solar energy | Enter through the Hatch | Interior is dry and automatically replenishes oxygen | A powered base is a new breathable return node | `SUB-007`, `SUB-008` |
| Crafted MVB is carried near open water | Deploy it and board the platform | Bay unfolds at the surface and exposes unlocked affordable vehicle recipes | A carried deployable becomes a world fabrication fixture | `SUB-009` |
| Seamoth blueprint and required materials are available at the MVB | Select Seamoth fabrication | Drones consume ingredients and create the first powered vehicle | Production changes the reachable dive envelope | `SUB-009`, `SUB-010` |
| Unmodified Seamoth has charge above 200 m | Enter, pilot to the habitat, stop, exit and enter the Hatch | Vehicle spends energy, supplies oxygen while occupied and remains safe; habitat restores survivor oxygen | Explicit route terminal joins vehicle, depth and base safety | `SUB-003`, `SUB-010` |
| Survivor dies after collecting unsecured items | Allow lethal state to resolve | Survivor returns at the last secured habitat with the scoped carried-item penalty; built world state persists | Failure is recoverable but materially costly | `SUB-011` |

## Strategic and experiential structure

- Local decision: continue a dive or surface, collect a reachable yield, catch
  food, scan a fragment, use a Fabricator, place a module, or turn the Seamoth
  before oxygen, energy or depth becomes unsafe.
- Medium-term planning: batch shallow resource trips; reserve inventory cells
  for bulky crafted items; search Kelp Forest and Grassy Plateaus for the two
  three-fragment unlocks; place the first habitat where sunlight, materials and
  the 200 m vehicle envelope overlap.
- Long-term structure: convert repeated breath-limited swimming sorties into
  persistent knowledge, powered refuge and finally a mobile oxygen-bearing
  vehicle that expands safe exploration.
- Common heuristics: turn back before the last oxygen warning; fabricate water
  before food becomes urgent; carry charged Scanner and Builder batteries;
  build shallow for better solar generation; keep hull integrity positive;
  approach the MVB and habitat within the unmodified Seamoth's safe depth.
- Failure attribution: HUD meters, scanner ring, recipe greying, placement
  preview, integrity notice, base power and Seamoth depth/energy make most
  failures legible; fauna motion and sampled fragment locations retain local
  uncertainty.
- Player-trust factors: consistent surface oxygen, persistent scan progress,
  explicit recipe costs, reversible deconstruction, readable hull warnings and
  a declared crush-depth alarm.
- Claim IDs: `SUB-002`–`SUB-011`.

## Replay and variation

- What changes between sessions: Lifepod position within the starting region,
  sampled resource and fragment placement, fauna paths, chosen habitat site,
  recipe order and trip routing.
- Randomness or procedural generation: the authored world topology and biome
  relationships remain stable while some resources, fragments and the starting
  Lifepod placement vary within bounded regions.
- Multiple viable strategies: the player may prioritise oxygen equipment,
  sustenance, Scanner, habitat or vehicle materials differently and may build
  the first base at many shallow legal sites.
- Typical replay motive: safer route planning, fewer surface returns, earlier
  vehicle fabrication, a different base location or progression into excluded
  campaign modules.
- Claim IDs: `SUB-002`–`SUB-010`.

## Adjacent systems and history

- Direct predecessors: underwater exploration and survival-crafting lineages
  provide context; no predecessor rules are imported into this record.
- Variants: Freedom removes food and water; Hardcore makes death terminal;
  Creative removes ordinary survival and material gates.
- Similar games: Minecraft and Rust share survival, gathering, inventory,
  crafting, building and persistent-world death; Terraria shares exploration,
  recipe dependencies and mutable refuge; Grand Theft Auto V shares direct
  water-vehicle operation.
- Important differences: Subnautica makes oxygen and vertical distance the
  primary excursion clock, turns scanned world fragments into fabrication
  knowledge, couples underwater rooms to hull integrity and power-generated
  oxygen, and gives the first vehicle its own air, energy and crush-depth limit.
- Claim IDs: `SUB-002`–`SUB-011`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-123`, `ACT-164`, `ACT-165`, `ACT-201`, `ACT-245`, `ACT-311`–`ACT-315` | dive route, collection, scan, fabrication, building and vehicle input |
| System Behaviour | `SYS-216`, `SYS-320`, `SYS-327`, `SYS-543`–`SYS-548` | oxygen, blueprint progress, conversion, hull, power and crush damage |
| Constraint | `CON-394`, `CON-460`–`CON-465` | carried cells, air, fragments, recipe, placement, power and depth |
| Information | `INF-073`, `INF-075`, `INF-132`, `INF-223` | HUD, PDA, scan, base and vehicle state |
| Objective | `OBJ-102` | first Seamoth and safe powered-habitat return |
| Time | `TIM-003` | real-time Survival and exploration |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `177` (`GAME-0001`–`GAME-0177`).
- Exact genome matches: none.
- Tied near matches: `GAME-0141` — Rust (`10 / 74 = 0.135135`).
- Supported combination subsets: `COMB-0176`.
- Scan date: 2026-08-28.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0141` — Rust | `ACT-008`, `ACT-123`, `ACT-164`, `ACT-165`, `SYS-216`, `SYS-327`, `INF-073`, `INF-075`, `INF-132`, `TIM-003` | Both couple embodied real-time survival, carried tools, food, crafting knowledge and persistent-world respawn. Subnautica replaces a procedural shared island, combat raiding, building privilege, upkeep, Workbench research and scheduled wipes with oxygen-limited vertical sorties, counted fragment scanning, pressure-hull flooding, power-generated interior air and a crush-limited submersible | Near, `0.135135` |

### Preserved research notes

- New genes: `ACT-311`–`ACT-315`, `SYS-543`–`SYS-548`, `CON-460`–`CON-465`,
  `INF-223` and `OBJ-102`.
- Classification result: `New gene` and new verified interaction combination.
- Evidence and reasoning: fourteen established boundaries fit without change;
  nineteen new records isolate hydration, fauna capture, fragment analysis,
  underwater construction, oxygen, powered fabrication, pressure integrity,
  life-support power, crush depth and the safe-return terminal.

## Combination status

- `COMB-0176` is a verified strict 26-gene subset coupling breath-limited
  gathering and scanning to powered habitat and submersible production.
- Earlier verified combinations are tested deterministically after registration.

## Taxonomy impact

- Registry changes: nineteen new Active genes, links on fourteen reused genes,
  `COMB-0176` and five existing family memberships.
- Taxonomy-change record: none; no prior lifecycle, definition or signature
  changes.
- Candidate terms affected: hydration consumption, moving-fauna capture,
  fragment scan, habitat construction, floating vehicle bay, oxygen reserve,
  blueprint count, powered fabrication, pressure hull, life support and crush
  depth.

## Negative results

- `ACT-204`, `SYS-330` and `CON-292` are not reused because their Rust boundary
  requires socketed grade, repair, stability, privilege or monument exclusion;
  Subnautica construction instead uses held progress, reversible material and a
  connected pressure-hull value.
- `SYS-328` is not reused because it owns a persistent multi-request personal
  crafting queue, while the scoped Fabricator resolves one station-owned output.
- `SYS-335` is not reused because it learns recipes through paid Rust research
  and Workbench tier, not counted physical fragment scans.
- `INF-199` is not reused because it joins truck, trailer, cargo and mandatory
  rest state; Seamoth exposes charge, health and pressure depth instead.

## Delta summary

## Нові факти

- [Confirmed | Corroborated | High] Original Subnautica after the official 2025
  Patch supports a reproducible fresh-Survival chain from Lifepod 5 through
  counted MVB/Seamoth scans and a powered shallow habitat to the first
  unmodified 200 m Seamoth return (`SUB-001`–`SUB-011`).

## Нові гени

- [Observation | Corroborated | High] Added nineteen genes for hydration,
  moving-fauna capture, fragment scanning, underwater module work, floating
  vehicle fabrication, oxygen, pressure integrity, base life support, Seamoth
  depth and the explicit route terminal.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0176` isolates the oxygen-to-scan-
  to-refuge-to-submersible production chain as a strict 26-gene subset.

## Зміни таксономії

- [Observation | Corroborated | High] No taxonomy migration; fourteen generic
  genes and five existing multi-game families are reused unchanged.

## Нові питання

- Which later underwater survival game reuses spatial oxygen and powered refuge
  while replacing counted fragment blueprints or pressure-hull construction?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0179` — Age of Empires II: Definitive Edition.
- Optimisation criterion: continue the recorded demand-led Goal in exact order.
- Expected information gain: contrast embodied survival production with
  multi-agent economic growth, technology ages and real-time territorial war.
- Backlog impact: eighth of nine authorised game units.

## Чому саме вона

- [Confirmed | Direct | High] It is the next immutable subject in
  `SEARCH_DEMAND_GAME_SELECTION_005` after the reviewed Subnautica unit.

## Confidence and open questions

- High confidence: current PC patch boundary; oxygen sources; Survival meters;
  fragment scanning; three-fragment MVB acquisition; habitat power and hull
  integrity; Seamoth power and 200 m base crush depth.
- Medium confidence: exact sampled placement of every required fragment and
  material on an arbitrary fresh save; the route therefore names stable biomes
  and thresholds rather than a fixed coordinate walkthrough.
- Open questions: none blocking this bounded first-Seamoth analysis. Exact
  hidden spawn weights and low-level simulation constants remain outside scope.

## Reproducibility notes

1. Start original Subnautica on PC/Steam after the official 2025 Patch, choose
   a fresh vanilla Survival save and do not use console commands.
2. Treat Lifepod 5 as the entry and preserve food, water, health and oxygen
   pressure; gather only enough shallow resources and fauna for tools,
   sustenance, the scoped habitat, MVB and Seamoth.
3. Craft and charge a Scanner, then complete three MVB and three Seamoth
   fragment scans; record interruptible progress and final blueprint unlocks.
4. Use the Habitat Builder to place one shallow I Compartment, Hatch and Solar
   Panel; verify positive integrity, stored power and oxygen on entry.
5. Fabricate, deploy and board the MVB; fabricate the first unmodified Seamoth.
6. Pilot above its 200 m crush boundary to the habitat, stop outside, exit and
   enter the powered dry compartment. This is the terminal, not Moonpool docking.

## Review record

- Research status: `reviewed`.
- Reviewed: 2026-08-28.
- Scope changes during review: narrowed from an open-ended campaign reading to
  one fresh-Survival production route ending at first safe Seamoth return;
  removed radio, Aurora, Moonpool, upgrades and full-story claims.
- Evidence changes during review: current patch and broad loop are primary-
  source anchored; stable numeric and UI transitions are explicitly secondary.
- Gene changes during review: reused fourteen established embodied survival,
  crafting, vehicle, inventory, HUD and time genes; added nineteen boundaries
  specific to hydration, fauna capture, scanning, habitat, oxygen, fabrication,
  power, pressure, vehicle depth and the route terminal.

## Localisation status

- Ukrainian game, all new-gene and combination entries are reviewed in this unit.
- Canonical product and item names remain `Subnautica`, `Seamoth`, `Lifepod 5`
  and `Mobile Vehicle Bay`; explanatory Ukrainian is not replaced by raw English.

## Source notes

- Official pages were checked on 2026-08-28. The 2025 Patch owns the reviewed PC
  boundary; later Switch 2 work is excluded from this PC scope.
- Community wiki pages are used only for stable numeric and UI transitions and
  are explicitly separated from the primary official product claims.

## Next recommended action

- Integrate `GAME-0179` — Age of Empires II: Definitive Edition after the
  required thirty-second stop window.
