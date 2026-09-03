---
game_id: GAME-0229
slug: no-mans-sky
game_title: "No Man’s Sky"
analysis_status: reviewed
reviewed: 2026-09-02
combination_ids:
  - COMB-0227
gene_ids:
  action:
    - ACT-008
    - ACT-122
    - ACT-123
    - ACT-201
    - ACT-206
    - ACT-338
    - ACT-399
    - ACT-400
  system:
    - SYS-161
    - SYS-320
    - SYS-326
    - SYS-327
    - SYS-329
    - SYS-734
    - SYS-735
    - SYS-736
  constraint:
    - CON-281
    - CON-297
    - CON-499
    - CON-569
    - CON-570
  information:
    - INF-075
    - INF-125
    - INF-132
    - INF-268
    - INF-279
  objective:
    - OBJ-143
  time:
    - TIM-003
---

# Game: No Man's Sky

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam release, app
  `275850`, official patch `6.45.1`, public Build ID `24039799`, built and
  published 2026-07-03, checked 2026-09-02; one new empty-slot single-player
  `Normal` preset with network multiplayer disabled and no post-start difficulty
  changes.
- Entry: select an empty save slot and unchanged `Normal`, then retain the first
  controllable moment of `Awakenings` on its procedurally generated hazardous
  starting planet with Exosuit, Multi-Tool and starter-starship systems in their
  authored damaged state.
- Primary decision loop: read the current tutorial instruction, hazard and life
  support, damaged technology requirements and local markers; move among
  shelter, resources, the crashed starship and the chart-directed shelter; mine
  finite yields; craft components; recharge survival technology; repair and
  pulse the Scanner; use the Analysis Visor; deploy, fuel and unload one
  Portable Refiner; install repair components; restore and fuel the Pulse Engine
  and Launch Thruster; launch, complete early flight prompts and follow the
  mysterious-signal marker.
- Positive retained terminal: land at the first `Awakenings` abandoned-building
  destination revealed after launch, exit the ship, interact with its required
  terminal, return to the starter ship, enter and exit once more, wait for the
  save indicator to clear, return cleanly to mode selection and reload. Success
  requires the same site, repaired ship and mission progress beyond the
  accepted terminal to be retained. Arrival, first ship exit or terminal
  interaction without the verified reload is intermediate.
- Negative evaluation terminal: death before that retained terminal rejects
  the fresh-save packet. Selecting respawn continues from altered initial state
  and is outside this unit; failure to create or reload the declared
  post-terminal ship-exit save also rejects the run.
- Included: one generated start planet and its sampled resource layout;
  first-person movement; hazard protection and life support; shelter and
  resource recharge; Mining Beam, Scanner and Analysis Visor; finite Ferrite
  Dust, Carbon, Di-hydrogen and Sodium collection; personal crafting; one
  Portable Refiner and required Pure Ferrite conversion; diagnosis and repair
  of scoped Multi-Tool, Exosuit and starter-starship technologies; Planetary
  Chart, tutorial messages and markers; Hermetic Seal route; launch fuel;
  direct starter-starship flight; first mysterious-signal building interaction;
  silent autosave, guaranteed ship-exit full save and one verification reload.
- Reproducible parameterisation: use Steam public patch `6.45.1` / Build
  `24039799`; create a genuinely empty slot; choose `Normal` without opening
  Custom; disable network multiplayer before control; redeem no expedition,
  account, Twitch or previous-save reward; follow the current `Awakenings`
  chain and stop after the verified save made by the post-terminal ship exit.
  Planet name, biome, weather, resource poses, ship model and route may vary.
- Excluded: `Relaxed`, `Survival`, `Permadeath`, `Creative`, Custom and
  Expedition; multiplayer, cross-save imports, mods, save editing and reward
  claims; arbitrary exploration; base building, Base Computer, Space Anomaly,
  hyperdrive, first warp, Artemis or Atlas progression; trading, combat,
  discovery completion, freighters, settlements, vehicles, pets, farming and
  the full galaxy or story.
- Potential scoped modules: first base construction, first hyperdrive and warp,
  one Space Anomaly visit, one named expedition milestone set or one fixed
  combat/trade loop each requires its own version, entry and retained terminal.
- Direct-play status: no client session was played. Current Hello Games release,
  mode, repair, scanning, inventory and save documentation plus the official
  Steam product establish the product and rules boundary; current written
  walkthroughs corroborate the early `Awakenings` order and building terminal.
  The trace is evidence-based rules reasoning. No video or audio was opened,
  played, heard or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `NMS-001` | Patch `6.45.1` and Steam public Build `24039799` form the current reviewed Windows release | Confirmed | Corroborated | High | P1, P2, S1 |
| `NMS-002` | An empty slot admits unchanged Normal, while Custom can alter or remove survival, resource, fuel, recipe and tutorial rules | Confirmed | Direct | High | P3, P5 |
| `NMS-003` | Expedition is a separate start without the ordinary tutorial and is not interchangeable with this Normal packet | Confirmed | Direct | High | P6 |
| `NMS-004` | Fresh Awakenings places the traveller on a variable hazardous planet with damaged equipment and a crashed starter ship | Observation | Corroborated | High | P2, S2, S3, S4 |
| `NMS-005` | Hazard protection and life support deplete during exposure and recover through shelter or compatible resources | Confirmed | Corroborated | High | P3, P4, S2 |
| `NMS-006` | Mining, personal crafting and a fuelled Portable Refiner produce the early repair components taught by the tutorial | Observation | Corroborated | High | P3, P4, P7, S2, S3 |
| `NMS-007` | A functional rechargeable Scanner pulse reveals nearby resources whose identity and distance can be read with the Analysis Visor | Confirmed | Direct | High | P3, P5 |
| `NMS-008` | Damaged technology exposes component requirements and regains function when compatible inputs fill its repair slots | Confirmed | Direct | High | P4, P7 |
| `NMS-009` | Awakenings orders Scanner repair, ship discovery, Pulse Engine and Launch Thruster repair, launch and signal pursuit | Observation | Corroborated | High | S2, S3, S4, S5 |
| `NMS-010` | The first post-launch signal leads to an abandoned building whose terminal advances the opening mission | Observation | Corroborated | High | S3, S4, S5 |
| `NMS-011` | The current game silently autosaves and still makes a full save whenever the player exits a ship | Confirmed | Direct | High | P3, P5 |
| `NMS-012` | Exiting the starter ship after the first required building terminal provides a reproducible retained early terminal | Observation | Corroborated | High | P3, P5, S3, S4, S5 |

## Basic data

- Release / origin: Hello Games developed and published No Man's Sky; the
  original Windows release was 2016-08-12 and the reviewed live release is
  official patch `6.45.1`.
- Platform or physical form: single-player first-person science-fiction
  exploration and survival on Windows/Steam; one Normal tutorial packet.
- Puzzle family: real-time system pressure; resource transformation and
  production; inventory and fixture dependencies; world topology and
  perspective; ordered dependency sequencing.
- Primary and official sources:
  - **[P1]** [official The Swarm patch 6.45.1](https://www.nomanssky.com/2026/06/the-swarm-6-45-1/),
    for the current Steam patch boundary and 2026-06-22 release record.
  - **[P2]** [official Steam product page](https://store.steampowered.com/app/275850/No_Mans_Sky/),
    for app identity, Windows availability, creator, release date and generated
    survival/exploration premise.
  - **[P3]** [official Waypoint Update](https://www.nomanssky.com/waypoint-update/?cli_action=1665248610.192),
    for presets, mutable-difficulty exclusions, hazard/life-support, mining,
    scanner, fuel, crafting and tutorial settings, continual autosave and
    guaranteed full saves on ship exit.
  - **[P4]** [official NEXT Update](https://www.nomanssky.com/en/next-update/),
    for incremental damaged-slot repair, required components, hazard and
    life-support displays, mining, Analysis Visor and marker semantics.
  - **[P5]** [official Atlas Rises patch 1.38](https://www.nomanssky.com/2017/10/atlas-rises-patch-1-38/),
    for empty-slot mode selection, ship-exit saves and Analysis Visor distance
    for Scanner-discovered resources.
  - **[P6]** [official Expeditions Update](https://www.nomanssky.com/expeditions-update/),
    for the separate no-tutorial Expedition start excluded here.
  - **[P7]** [official Synthesis Update](https://www.nomanssky.com/synthesis-update/),
    for compatible items applied to damaged technology and hazard recharge.
- Secondary and reproducible sources:
  - **[S1]** [SteamDB depots](https://steamdb.info/app/275850/depots/), for
    Windows depot `275851`, public Build `24039799` and its 2026-07-03 timestamp.
  - **[S2]** [current Awakenings walkthrough](https://nmsguide.com/guides/nms-awakenings-mission-walkthrough),
    updated 2026-07-30, for the variable start, survival, Scanner, Visor,
    mining, crafting, Portable Refiner and ship-repair order.
  - **[S3]** [Gamer Guides Awakenings](https://www.gamerguides.com/no-mans-sky/guide/missions/primary-missions/awakenings),
    for first-mission launch and the scan leading to an abandoned building.
  - **[S4]** [No Man's Sky Resources: Awakenings](https://www.nomansskyresources.com/story-missions/awakenings),
    for repair, launch, signal tracking and terminal interaction.
  - **[S5]** [community wiki: Awakenings](https://nomanssky.fandom.com/wiki/Awakenings),
    for the Planetary Chart, Hermetic Seal, thruster ingredients, flight tutorial
    and first signal sequence.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P7` and `S1`–`S5` under the fixed version, preset, network and terminal
  contract; no audiovisual playback or direct-play claim.
- Claim IDs: `NMS-001`–`NMS-012`.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`: traverse the start planet; `ACT-122`: hold the Mining
  Beam on reachable finite resource objects; `ACT-123`: commit known personal
  recipes; `ACT-201`: enter, pilot, land and exit the starter ship; `ACT-206`:
  load the Portable Refiner and collect Pure Ferrite; `ACT-338`: place the
  crafted refiner on compatible ground.
- New `ACT-399`: supply a compatible material or component to one addressed
  damaged or chargeable technology slot; new `ACT-400`: trigger one local
  Scanner pulse after repair and recharge readiness.
- Parameters: generated position, resource, tool fuel, recipe, ingredient,
  fixture pose, refiner slots, technology slot, component, charge, cooldown,
  ship input and landing site.
- Claim IDs: `NMS-005`–`NMS-010`.

### System Behaviour Genes

- Existing `SYS-161`: mined yields reduce each local finite source; `SYS-320`:
  integrate piloted starship motion, landing and collision; `SYS-326`: generate
  and populate the sampled hazardous start planet; `SYS-327`: advance exposure
  and survival; `SYS-329`: turn refiner fuel and input into typed output.
- New `SYS-734`: consume accepted repair or recharge inputs and restore
  technology function or reserve; new `SYS-735`: turn a valid survey pulse into
  temporarily revealed nearby resource bearings; new `SYS-736`: advance the
  tutorial only when the current taught action or state predicate is satisfied.
- Resolution order: accept movement, mining, inventory, repair, scan, refiner
  or vehicle input; update exposure and charge; validate and consume resources;
  resolve crafting, processing, repair or survey; advance the tutorial; update
  the marker; integrate flight and landing; accept the building terminal; then
  create and verify the post-terminal save.
- Claim IDs: `NMS-004`–`NMS-012`.

### Constraint Genes

- Existing `CON-281`: exposure remains viable only while hazard and life
  support are recoverable; `CON-297`: personal crafting requires known recipes
  and ingredients; `CON-499`: Portable Refiner placement requires clear terrain.
- New `CON-569`: technology requires completed damaged slots and usable charge;
  new `CON-570`: a survey pulse requires a functional, recharged Scanner.
- Scarce strategic resources: hazard protection, life support, Mining Beam and
  technology charge; Ferrite Dust, Carbon, Di-hydrogen, Sodium and derivatives;
  refiner fuel; shelter distance; scanner readiness and launch fuel.
- Claim IDs: `NMS-005`–`NMS-009`.

### Information Genes

- Existing `INF-075`: expose survival and equipment charge; `INF-125`: expose
  the current mission marker; `INF-132`: expose recipes and component
  dependencies; `INF-268`: state the current tutorial instruction and next step.
- New `INF-279`: expose identity, bearing and approximate distance of locally
  surveyed resources through Scanner and Analysis Visor feedback.
- Hidden geography, later mission stages and the next silent autosave moment do
  not enter the information set.
- Claim IDs: `NMS-005`–`NMS-012`.

### Objective Genes

- New `OBJ-143`: restore disabled transport through taught survival and
  production dependencies, reach the first guided destination, accept its
  required interaction and retain that progress through explicit save/reload.
- Launch, arrival or terminal interaction without verified retention is
  intermediate. Death before retention or a missing save is non-positive; base
  building and later story are outside the objective.
- Claim IDs: `NMS-009`–`NMS-012`.

### Time Genes

- Existing `TIM-003`: exposure, survival drain, refiner processing, scanner
  recharge and vehicle motion advance in real time while the player acts.
- Claim IDs: `NMS-005`–`NMS-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Traveller is exposed with falling hazard protection | Enter shelter or supply a compatible recharge resource | Environmental drain pauses or charge rises enough to continue | live survival budget precedes open traversal | `NMS-005` |
| Scanner is damaged and declares a component | Mine and craft the input, then apply it | The damaged slot clears and Scanner function becomes available | diagnosed repair, not possession alone | `NMS-006`, `NMS-008` |
| Functional Scanner is ready | Trigger a pulse and inspect a revealed target with the Analysis Visor | Nearby eligible resources gain identity, bearing and distance feedback | gated action produces local information | `NMS-007` |
| A recipe is known and ingredients are carried | Commit the recipe | Inputs become the declared repair component | personal crafting closes a taught dependency | `NMS-006` |
| Portable Refiner has a valid pose | Place it, load fuel and input, let it run and collect output | Fuel and input become Pure Ferrite over time | processing differs from hand crafting | `NMS-006` |
| Ship systems expose incomplete repair slots | Supply the components and compatible launch fuel | Pulse Engine and Launch Thruster become operable | exact repairs gate direct flight | `NMS-008`, `NMS-009` |
| Ship is launch-capable | Enter, launch and complete early flight/scan prompts | Direct flight begins and the signal marker becomes authoritative | transport changes traversal scale | `NMS-009` |
| Signal building is marked | Fly, land, exit and interact with its terminal | The destination terminal advances Awakenings | arrival alone is not completion | `NMS-010` |
| Building terminal has advanced the mission | Enter and exit the ship, wait for saving, return to menu and reload | Site, repaired ship and post-terminal mission state persist; otherwise reject | explicit positive retained terminal | `NMS-011`, `NMS-012` |
| Traveller dies before retention | Do not continue the respawned state for this packet | The fresh-save attempt is rejected | negative evaluation boundary | `NMS-005`, `NMS-012` |

## Strategic and experiential structure

- Local decision: compare charge and shelter distance before mining; distinguish
  raw, crafted and refined requirements; repair only current dependencies.
- Medium-term planning: reserve Carbon for Mining Beam and refiner operation,
  Sodium for exposure and the exact Ferrite/Di-hydrogen chain for ship repair.
- Long-term structure: tutorial predicates turn survival, information, crafting
  and processing into a repaired vehicle; flight then turns the first remote
  terminal into retained mission progress.
- Common heuristics: shelter while reading inventory; scan before walking; pin
  the current dependency; place the refiner beside ship or cover.
- Failure attribution: meters, repair slots, grey recipes, cooldown, refiner
  slots, mission text, marker and save indicator distinguish failure causes.
- Player trust: generated positions vary, but instruction order, repair
  predicates, marker relation and explicit reload test remain inspectable.

## Replay and variation

- What changes: planet, biome, weather, names, terrain, resource positions,
  route, incidental hazards, starter-ship appearance and flight approach.
- Randomness or procedural generation: a new save generates the surrounding
  world and required tutorial opportunities; generation is not completion.
- Multiple viable strategies: shelter and collection order vary, but repair,
  launch, building interaction and verified save remain mandatory.
- Typical replay motive: compare another generated start or a safer resource
  route. Continuing the open universe is outside this packet.

## Adjacent systems and history

- Direct predecessors: earlier No Man's Sky releases established generated
  exploration; Waypoint changed saves and difficulty without merging Normal
  and Expedition.
- Similar games: Subnautica joins live survival, gathered inputs, crafting,
  deployed production and direct vehicle use; Valheim and Don't Starve Together
  join generated survival terrain, production and clear-ground fixtures.
- Important differences: this packet begins with damaged technology, produces
  temporary resource bearings through a rechargeable pulse, gates dependencies
  through staged teaching and ends after repaired flight, a remote terminal and
  verified ship-exit save. It excludes Subnautica's breath-limited dives,
  fragments, habitat integrity and fabricated Seamoth.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-122`, `ACT-123`, `ACT-201`, `ACT-206`, `ACT-338`, `ACT-399`, `ACT-400` | traverse, mine, craft, process, repair, scan and pilot |
| System Behaviour | `SYS-161`, `SYS-320`, `SYS-326`, `SYS-327`, `SYS-329`, `SYS-734`, `SYS-735`, `SYS-736` | finite sources, generated start, exposure, processing, repair, survey and tutorial advance |
| Constraint | `CON-281`, `CON-297`, `CON-499`, `CON-569`, `CON-570` | survival, recipes, placement, repair and scanner readiness |
| Information | `INF-075`, `INF-125`, `INF-132`, `INF-268`, `INF-279` | survival, mission, dependency, tutorial and survey state |
| Objective | `OBJ-143` | repair transport and retain first guided destination |
| Time | `TIM-003` | continuous exposure, processing, recharge and motion |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `228` (`GAME-0001`–`GAME-0228`).
- Exact genome matches: none.
- Tied near matches: `GAME-0186` — Don’t Starve Together (`12 / 58 = 0.206897`).
- Supported combination subsets: `COMB-0227`.
- Scan date: 2026-09-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0186` — Don’t Starve Together | `ACT-008`, `ACT-122`, `ACT-123`, `ACT-338`, `SYS-326`, `SYS-327`, `SYS-329`, `CON-281`, `CON-499`, `INF-075`, `INF-132`, `TIM-003` | Both begin in generated survival terrain, couple live personal pressure to local extraction, personal recipes and one placed material processor, and expose recipe and survival state. Don't Starve Together instead requires two humans, seasonal hunger/sanity/thermal coordination, science prototyping, ghost revival and a Fuelweaver checkpoint. No Man's Sky uses a solo staged tutorial, slot-addressed technology repair, a rechargeable resource-survey pulse, repaired starship flight, a building terminal and verified ship-exit retention. | Near, `0.206897` |

### Preserved research notes

- New genes: `ACT-399`, `ACT-400`, `SYS-734`, `SYS-735`, `SYS-736`,
  `CON-569`, `CON-570`, `INF-279`, `OBJ-143`.
- Reused genes: `ACT-008`, `ACT-122`, `ACT-123`, `ACT-201`, `ACT-206`,
  `ACT-338`, `SYS-161`, `SYS-320`, `SYS-326`, `SYS-327`, `SYS-329`,
  `CON-281`, `CON-297`, `CON-499`, `INF-075`, `INF-125`, `INF-132`,
  `INF-268` and `TIM-003`.
- Classification result: `New gene` and new verified interaction combination.
- Evidence and reasoning: generic traversal, extraction, crafting, portable
  processing, generation, survival, vehicle operation and instruction displays
  retain existing boundaries. New records isolate technology restoration,
  gated survey, local disclosure, taught-predicate progression and the retained
  repair-to-destination objective.

## Taxonomy impact

- Registry changes: `ACT-399`, `ACT-400`, `SYS-734`, `SYS-735`, `SYS-736`,
  `CON-569`, `CON-570`, `INF-279`, `OBJ-143`; no earlier signature changes.
- Taxonomy-change record: none.
- Candidate terms affected: technology repair slot, chargeable technology,
  survey pulse, scanner recharge, local resource bearing, tutorial predicate
  and retained guided destination.

## Negative results

- `SYS-216` is rejected: Normal respawn exists, but death rejects this packet.
- `ACT-313`, `SYS-544` and `CON-461` are rejected: the early Scanner emits a
  pulse; it does not require a held target scan or fragment threshold.
- `SYS-545` and `CON-462` are rejected: the Portable Refiner is a loaded,
  fuelled processing fixture, not a powered fabricator boundary.
- Bases, discovery completion, combat, economy, later vehicles, multiplayer and
  the complete Artemis/Atlas story are excluded rather than unioned.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Поточний `Normal` зберігає керування захистом,
  ресурсами, паливом, рецептами та навчанням, які Custom може змінити або
  вимкнути (`NMS-002`, `NMS-005`–`NMS-008`).
- [Observation | Corroborated | High] Ранній `Awakenings` з'єднує виживання,
  ремонт Scanner і корабля, перероблення, політ, перший термінал і перевірене
  завантаження (`NMS-004`–`NMS-012`).

## Нові гени

- [Observation | Corroborated | High] `ACT-399`, `ACT-400`, `SYS-734`,
  `SYS-735`, `SYS-736`, `CON-569`, `CON-570`, `INF-279`, `OBJ-143`.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0227`.

## Зміни таксономії

- [Observation | Corroborated | High] Змін життєвого циклу чи сигнатур раніше
  перевірених ігор немає.

## Нові питання

- Чи має окремий bounded packet першої бази самостійний просторовий виробничий
  цикл, відмінний від цієї навчальної послідовності?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0230` — STAR WARS Battlefront II (2017).
- Optimisation criterion: перейти від процедурного survival tutorial до однієї
  стабільної заданої першої сюжетної місії.
- Expected information gain: перевірити наземний бій, здібності, керовані етапи
  та збережений сюжетний terminal без об'єднання Arcade й мережі.
- Backlog impact: продовжити активний Goal, не починаючи `GAME-0230` у цьому
  unit.

## Чому саме вона

- [Hypothesis | Limited | High] Це наступна записана гра Batch 011 і контрольна
  зміна від процедурної ресурсної залежності до заданої бойової місії.
