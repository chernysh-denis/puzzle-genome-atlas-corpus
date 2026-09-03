---
game_id: GAME-0210
slug: dayz
game_title: DayZ
analysis_status: reviewed
reviewed: 2026-09-01
combination_ids:
  - COMB-0208
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-165
    - ACT-183
    - ACT-199
    - ACT-200
    - ACT-311
    - ACT-381
    - ACT-382
  system:
    - SYS-208
    - SYS-215
    - SYS-223
    - SYS-327
    - SYS-339
    - SYS-345
    - SYS-416
    - SYS-697
    - SYS-698
    - SYS-699
    - SYS-700
  constraint:
    - CON-210
    - CON-281
    - CON-284
    - CON-285
    - CON-286
    - CON-304
    - CON-305
    - CON-306
    - CON-313
    - CON-553
    - CON-554
  information:
    - INF-073
    - INF-075
    - INF-115
    - INF-128
    - INF-269
  objective:
    - OBJ-076
  time:
    - TIM-003
---

# Game: DayZ

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam base game,
  PC Steam Stable `1.29.163709`, public branch build `24689949`, reviewed
  2026-09-01; one solo fresh-spawn life on vanilla official Chernarus+ server
  `3776 | EUROPE - DE | 1st Person Only`. The server identity, version, map,
  60-slot cap and no-mod state were observed through a current textual server
  query; population, exact coast spawn, daylight, weather, loot and encounters
  are declared sampled parameters rather than stable rules.
- Primary decision loop: read the survivor's body, metabolism, clothing,
  carried space and nearby threat state; move and scavenge an authored shared
  landscape; choose what to wear, carry, combine, eat, drink or use for
  treatment; preserve stamina, warmth, hydration, energy, blood and health;
  avoid, distract or fight infected; identify nearby human survivors through
  incomplete sight, sound and proximity communication; and repeat while the
  Central Economy, weather, day cycle, item condition, illness and other
  participants continue changing the server world.
- Entry and exit: from the official-server browser choose the declared server
  and enter as a newly generated default `Survivor`; entry is the first
  retained controllable frame at the sampled Chernarus coast spawn with the
  server-default starting gear. There is no positive victory or duration
  threshold. The reproducible negative evaluation terminal is the explicit
  death state after this survivor reaches lethal bodily condition and loses
  control. Selecting respawn creates a different survivor and is outside the
  analysed life.
- Included: one connected first-person life; direct walking, sprinting,
  crouching and vaulting; visible local navigation without an external route;
  reachable world and corpse loot; clothing, nested storage, equipment and
  quick slots; item stacks, bulk, compatibility, carried weight and stamina;
  contextual item combination, splitting and simple hand crafting; eating,
  drinking and item condition; metabolism, wetness and temperature; health,
  blood, shock, bleeding, unconsciousness and recovery; treatable ordinary
  diseases and wound contamination; basic melee and firearm operation;
  infected sight/sound pursuit; nearby human uncertainty, proximity voice and
  gestures; current weather and day/night state; Central Economy spawning,
  lifetime, cleanup and persistence; permanent death of the current identity.
- Excluded: Frostline/Sakhal, Livonia, Badlands/Nasdara, Deluxe and Cool
  editions, future update 1.30, Experimental, console builds, community
  servers, private shards, Workshop and mods; third-person servers; groups or
  authenticated friends; reconnect/offline survival; bases, tents and buried
  stashes across sessions; construction, agriculture, horticulture, hunting,
  fishing, fireplaces, cooking and long-term food preservation; vehicles and
  boats; contaminated-zone progression, bunker routes and dynamic convoy or
  seasonal events; blood transfusion and advanced medical cooperation;
  account achievements, cosmetics, monetisation and the whole live-service
  history. These exclusions prevent optional persistent modules from being
  mistaken for requirements of one fresh-spawn life.
- Potential scoped modules: one declared reconnecting official-server life;
  base and stash persistence; fireplace and cooked-food survival; hunting or
  agriculture; one vehicle repair-and-travel route; one contaminated-zone
  expedition; a fixed two-person cooperative life; Frostline, Livonia or
  Badlands under its own current version and terminal.
- Direct-play status: not conducted. Current official product and patch text,
  Bohemia's server/mission documentation and the maintained public DayZ script
  source establish the live build boundary, shared economy, body variables,
  action gates, illness, unconsciousness and death. A current textual server
  observation establishes the sampled official Chernarus context. The
  transition trace is rules reasoning, not a claim of authenticated play. No
  video or audio was opened, played or used as evidence.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DAYZ-001` | PC Steam Stable 1.29.163709 and public build 24689949 are the reviewed current Windows boundary | Confirmed | Direct | High | P1, P2, S1 |
| `DAYZ-002` | The sampled server is an unmodded official first-person Chernarus+ server on the reviewed version | Observation | Corroborated | High | P2, S2 |
| `DAYZ-003` | A new multiplayer survivor is generated at one sampled spawn with configurable starting gear and a persistent server world | Confirmed | Direct | High | P3, P4 |
| `DAYZ-004` | Central Economy maintains loot, infected, animals, persistence and cleanup independently of any one player | Confirmed | Direct | High | P3, P4 |
| `DAYZ-005` | Water, energy, heat comfort, wetness, stamina, carried weight and environment jointly alter survival and action capacity | Confirmed | Direct | High | P5, P6 |
| `DAYZ-006` | Health, blood, shock and bleeding can produce recoverable unconsciousness before lethal death | Confirmed | Direct | High | P5, P6 |
| `DAYZ-007` | Contaminated food, water, hands or wounds can add agents whose modifiers cause symptoms and admit condition-specific treatment | Confirmed | Direct | High | P6 |
| `DAYZ-008` | Infected react to local visual/acoustic cues while nearby human survivors remain only partially observable and may communicate locally | Observation | Corroborated | High | P1, P6 |
| `DAYZ-009` | Compatible held-item operations consume, split, repair or transform inventory items under action-state and capacity gates | Confirmed | Direct | High | P6 |
| `DAYZ-010` | Death permanently ends this survivor identity; respawn begins another analytical life, so no positive win is invented | Confirmed | Direct | High | P1, P5, P6 |

## Basic data

- Release / origin: developed and published by Bohemia Interactive; Windows
  1.0 released on 2018-12-13 after the earlier public-development period.
- Platform or physical form: online Windows first-person open-world survival;
  one official persistent-server life is scoped.
- Puzzle family: real-time system pressure; tactical forecast and counterplay;
  resource transformation and production; hidden-state deduction.
- Primary and reproducible sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/221100/DayZ/),
    for the current product title, Windows platform, official open-world
    survival premise, limited resources, infected, strangers and absence of a
    conventional authored victory.
  - **[P2]** [official 1.29 stable announcement](https://store.steampowered.com/news/app/221100/view/511861552615262777)
    and [official PC Stable Update 2 notes](https://forums.dayz.com/forum/137-pc-stable-updates/),
    for the stable 1.29 line, current Road to Badlands update, Chernarus rules
    and version `1.29.163709`.
  - **[P3]** [Bohemia Central Economy setup](https://community.bistudio.com/wiki/DayZ:Central_Economy_setup_for_custom_terrains),
    for Chernarus+ mission files, playable-character creation, spawn points,
    loot, infected, animals, dynamic events and persistent storage.
  - **[P4]** [Bohemia Central Economy configuration](https://community.bistudio.com/wiki/DayZ:Central_Economy_Configuration),
    for spawn limits, item and corpse cleanup, persistence segments and backup
    processing.
  - **[P5]** [Bohemia Gameplay Settings](https://community.bistudio.com/wiki/DayZ:Gameplay_Settings),
    for stamina, shock recovery, unconscious respawn controls, wetness weight,
    drowning, environment temperature and damage parameters.
  - **[P6]** [Bohemia DayZ-Script-Diff](https://github.com/BohemiaInteractive/DayZ-Script-Diff),
    especially `PlayerBase`, `ShockHandler`, bleeding managers, player stats,
    environment, inventory actions and disease/agent modifiers, for current
    action and body-state transitions.
- Secondary sources:
  - **[S1]** [SteamDB DayZ depots](https://steamdb.info/app/221100/depots/),
    for public build `24689949` and its 2026-08-12 timestamp.
  - **[S2]** [current textual server observation](https://moddingcommunity.com/dayz/s/5.62.99.23%3A11100),
    for server `3776`, official-style 1PP identity, Chernarus+, no-mod context,
    version and sampled capacity. It corroborates context but does not define
    the canonical rules.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P6`, `S1` and `S2` under the declared build, server, perspective and
  fresh-spawn identity; no audiovisual playback or direct-play claim.
- Claim IDs: `DAYZ-001`–`DAYZ-010`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, directly navigate the survivor; `ACT-161`, aim
  or strike a reachable threat; `ACT-164`, change the active quick-slot item;
  `ACT-165`, consume food; `ACT-183`, reload a magazine-fed firearm;
  `ACT-199`, transfer and equip compatible loot; `ACT-200`, use an
  interruptible treatment; `ACT-311`, drink from a carried source.
- New genes: `ACT-381`, combine, split or apply one compatible held inventory
  item to another through the contextual inventory action; `ACT-382`, address
  nearby survivors through proximity voice or a visible gesture without a
  guaranteed alliance or response.
- Parameters: spawn, destination, stance, target, held item, quick slot,
  container, recipe pair, portion, weapon, magazine, treatment, voice range,
  gesture and interruption.
- Claim IDs: `DAYZ-003`, `DAYZ-005`–`DAYZ-009`.

### System Behaviour Genes

- Existing genes: `SYS-208`, resolve ranged hits through geometry and body
  zones; `SYS-215`, resolve direct live combat; `SYS-223`, wear or ruin used
  items; `SYS-327`, advance metabolism and environmental exposure; `SYS-339`,
  route infected from local sight and emitted sound; `SYS-345`, end the current
  identity at permanent death; `SYS-416`, advance day/night, weather and local
  ecology.
- New genes: `SYS-697`, maintain the server's Central Economy by spawning,
  aging, persisting and cleaning eligible loot, corpses, infected and animals;
  `SYS-698`, couple health, blood, shock and bleeding into injury,
  unconsciousness, recovery or death; `SYS-699`, transmit and advance
  condition-specific pathogens through agents, immunity, symptoms and
  treatment; `SYS-700`, resolve contextual held-item combination, splitting,
  consumption, repair or crafting into the declared inventory result.
- Resolution order: accept movement, inventory, item-use, communication and
  combat inputs; validate reach, capacity, compatibility, condition and body
  state; advance timed actions and item transformations; resolve perception,
  attacks, bleeding and shock; advance agents, metabolism, temperature,
  weather, ecology and Central Economy; then retain control, enter
  unconsciousness, recover or settle death.
- Claim IDs: `DAYZ-004`–`DAYZ-010`.

### Constraint Genes

- Existing genes: `CON-210`, stacks and carried slots are finite; `CON-281`,
  survival depends on climate-compatible equipment and resources; `CON-284`,
  bulk and equipment slots bound the carried load; `CON-285`, firearm use
  requires compatible ammunition, magazine, attachment and action state;
  `CON-286`, restorative use needs a legal uninterrupted channel; `CON-304`,
  current body and load state constrain movement and work; `CON-305`, infected
  pursuit needs a perceived cue and reachable route; `CON-306`, weapon use
  needs viable body, reach and equipment; `CON-313`, this survivor cannot
  respawn after death.
- New genes: `CON-553`, consumption or treatment requires a compatible item
  whose condition, contamination, target state and dose permit the intended
  effect; `CON-554`, an unconscious survivor cannot issue ordinary actions,
  remains exposed to the shared world and regains control only after legal
  shock recovery before death.
- Scarce strategic resources: daylight and distance, hydration, energy,
  warmth, dry insulation, health, blood, shock, stamina, clean food and water,
  disinfected treatment, item condition, ammunition, storage space, carried
  weight, local concealment and reliable information about strangers.
- Claim IDs: `DAYZ-005`–`DAYZ-010`.

### Information Genes

- Existing genes: `INF-073`, expose quick slots and the active hand;
  `INF-075`, expose survival capacity and equipment wear; `INF-115`, reveal
  only locally visible or audible opponents; `INF-128`, expose reachable loot,
  inventory state and compatibility.
- New gene: `INF-269`, show categorical health, blood, temperature, energy,
  hydration, bleeding and sickness icons with directional trends while
  withholding exact internal values, agent identity and future outcome.
- Claim IDs: `DAYZ-004`–`DAYZ-009`.

### Objective Genes

- Existing gene: `OBJ-076`, extend one controllable survivor life until
  irreversible death. Food, equipment, a weapon, inland travel, a kill or a
  survival duration is only an intermediate state. No positive DayZ victory is
  fabricated for a ruleset that provides none.
- Success, evaluation and failure: the run is evaluated by how long and under
  what retained condition this identity remains controllable. Unconsciousness
  is non-terminal if shock recovery restores control. The explicit death state
  is the negative terminal; menu exit and disconnect are excluded rather than
  counted as death.
- Claim IDs: `DAYZ-006`, `DAYZ-010`.

### Time Genes

- Existing gene: `TIM-003`, the shared server, needs, bleeding, illness,
  weather, infected and other survivors continue in real time while decisions
  and interruptible actions are made.
- Claim IDs: `DAYZ-004`–`DAYZ-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Stable 1.29.163709 is at the official-server browser | Join server 3776 as a new default Survivor | The server selects a legal Chernarus spawn and supplies its current default gear in a persistent shared world | Build, server, perspective, identity and sampled entry are bounded | `DAYZ-001`–`DAYZ-003` |
| A reachable item occupies the world or an exposed corpse | Transfer it to clothing, hands or equipment | The item moves only if its stack, bulk and compatible slot fit; carried weight can reduce available stamina | Loot is a capacity and mobility decision, not abstract collection | `DAYZ-004`, `DAYZ-005`, `DAYZ-009` |
| Two held items expose a compatible contextual operation | Combine, split, load, repair or craft them | The action consumes or changes declared quantities and conditions and emits the corresponding inventory state | DayZ crafting is embodied item compatibility rather than a detached production queue | `DAYZ-009` |
| Water, energy or warmth is falling | Select a known safe carried resource and consume it | Stomach transfer raises water or energy over time; unsafe contamination can instead add an illness agent | Resource identity and safety matter beyond meter refill | `DAYZ-005`, `DAYZ-007` |
| The survivor is wet, cold, loaded or exhausted | Change clothing/load and move or rest | Environment and carried weight recompute heat comfort and stamina capacity; body state changes legal movement and combat performance | Equipment, weather and metabolism jointly bound action | `DAYZ-005` |
| Movement, a voice, impact or gunshot reaches an infected | Break line of sight, change route or fight | A locally cued infected investigates or pursues a reachable remembered position and resolves contact attacks if it closes | Infected do not need omniscient global tracking | `DAYZ-008` |
| Another survivor is locally seen or heard | Speak through proximity voice or perform a gesture | Only recipients within the current local channel can receive the cue; alliance, truth and response remain uncontrolled | Social information is spatial and strategically unreliable | `DAYZ-008` |
| Damage creates one or more bleeding sources | Apply a compatible bandage or disinfected rag without interruption | Successful treatment closes eligible bleeding while blood, shock and health continue from their current values | Wound control consumes time and condition-compatible supply | `DAYZ-006`, `DAYZ-009` |
| Shock crosses the unconscious threshold before lethal health loss | Issue no ordinary action and allow live recovery or further damage | Control is suspended; shock may refill and return control, while bleeding, infected or players can still kill the body | Unconsciousness is recoverable exposure, not the terminal itself | `DAYZ-006`, `DAYZ-010` |
| A compatible pathogen was acquired from consumption, hands, contact or a wound | Preserve warmth/resources and use a matching treatment when available | Agent count, immunity and modifiers advance symptoms and may recover, persist or worsen according to the condition | Illness is concealed causal state, not a generic health subtraction | `DAYZ-007` |
| Health reaches lethal bodily state | Observe the explicit death state | Direct control of this identity ends; its body and items can remain in the server world, and respawn would create another Survivor | Death is the only admitted evaluation terminal | `DAYZ-004`, `DAYZ-010` |

## Strategic and experiential structure

- Local decision: enter a building or avoid its sightline; take warmer clothing
  or leave capacity free; risk an unknown food/water source; combine supplies;
  sprint at the cost of stamina; treat bleeding now; speak, hide, fight or flee
  when another body is detected.
- Medium-term planning: stabilise hydration, calories, warmth and basic medical
  capacity; move away from the sampled coast without becoming overloaded;
  retain compatible ammunition and a reliable tool; manage visible symptoms
  before they compound with cold, blood loss or hostile contact.
- Long-term structure: there is no authored win state. The same survivor keeps
  converting uncertain local information and finite shared resources into more
  controllable life until one causal chain reaches permanent death.
- Common heuristics: drink from known safe sources; keep hands and wound-care
  materials clean; replace wet clothing; avoid carrying every find; break an
  infected's perception before fighting several; treat bleeding before travel;
  assume an armed stranger's intention is unknown even after communication.
- Failure attribution: visible directional status trends, blood/health state,
  bleeding count, sickness symbol, item condition and local cues expose many
  immediate causes, but exact agent load, remote loot, other players' intent
  and the future Central Economy state remain deliberately incomplete.
- Player-trust factors: consistent contextual action labels, visible inventory
  compatibility, stable local cause/effect, recoverable unconsciousness and an
  explicit death state; stochastic shared loot and human deception create
  uncertainty without changing the declared rules.
- Claim IDs: `DAYZ-004`–`DAYZ-010`.

## Replay and variation

- What changes between lives: legal coast spawn, initial local weather and
  daylight, nearby loot, item condition, infected/wildlife presence, server
  population, human encounters, acquired disease and the chain that causes
  death.
- Randomness or procedural generation: Chernarus+ geometry is authored, not a
  newly generated map. Central Economy and player-spawn configuration sample
  dynamic world entities and a legal start inside the persistent server state.
- Multiple viable strategies: stealth, scavenging route, carried load,
  clothing, treatment timing, interpersonal communication and willingness to
  fight can vary widely; none becomes a positive terminal.
- Typical replay motive: survive longer, stabilise sooner, reach a different
  region, learn safer resource patterns, interpret strangers better or avoid a
  previously legible death chain.
- Claim IDs: `DAYZ-003`–`DAYZ-010`.

## Adjacent systems and history

- Direct predecessors: the DayZ mod and the standalone's earlier public builds
  establish historical lineage but do not supply current 1.29 parameters.
- Variants: Livonia, Frostline/Sakhal and future Badlands/Nasdara change maps,
  climate, resources and authored facilities; community servers can alter
  Central Economy, starting gear, perspective, persistence and rules.
- Similar games: Project Zomboid shares metabolism, local zombie perception,
  embodied condition and one identity ending at permanent death. Rust shares
  persistent online survival, scavenged inventory, climate and human threat.
  PUBG shares live firearms, capacity-bound loot and one-life risk but has a
  bounded match and positive last-survivor terminal.
- Important differences: DayZ keeps an authored server landscape and shared
  Central Economy running without a match win, makes blood/shock-based
  unconsciousness, treatable pathogens, contextual held-item operations and
  proximity negotiation causal, and treats respawn as a new identity rather
  than continuation of the scoped life.
- Claim IDs: `DAYZ-001`–`DAYZ-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-165`, `ACT-183`, `ACT-199`, `ACT-200`, `ACT-311`, `ACT-381`, `ACT-382` | navigation, combat, carried items, treatment and local communication |
| System Behaviour | `SYS-208`, `SYS-215`, `SYS-223`, `SYS-327`, `SYS-339`, `SYS-345`, `SYS-416`, `SYS-697`–`SYS-700` | combat, needs, ecology, economy, trauma, agents and item resolution |
| Constraint | `CON-210`, `CON-281`, `CON-284`–`CON-286`, `CON-304`–`CON-306`, `CON-313`, `CON-553`, `CON-554` | capacity, climate, equipment, body, treatment, pursuit and one-life gates |
| Information | `INF-073`, `INF-075`, `INF-115`, `INF-128`, `INF-269` | local equipment, status, loot and partial-threat evidence |
| Objective | `OBJ-076` | extend one identity's controllable life until death |
| Time | `TIM-003` | continuously advancing shared survival world |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `209` (`GAME-0001`–`GAME-0209`).
- Exact genome matches: none.
- Tied near matches: `GAME-0142` — Project Zomboid (`22 / 68 = 0.323529`).
- Supported combination subsets: `COMB-0208`.
- Scan date: 2026-09-01.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0142` — Project Zomboid | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-165`, `ACT-199`, `SYS-208`, `SYS-215`, `SYS-223`, `SYS-339`, `SYS-345`, `CON-210`, `CON-281`, `CON-304`, `CON-305`, `CON-306`, `CON-313`, `INF-073`, `INF-075`, `INF-115`, `INF-128`, `OBJ-076`, `TIM-003` | Both make local zombie perception, body and climate pressure, finite carried supplies, direct combat and permanent identity death part of one unbounded survival life. Project Zomboid uses a retained local Apocalypse save, selected body-region care, graded moodles, accelerated timed actions, shelter construction, calendar attrition and incurable Knox Infection; DayZ uses a live shared Central Economy, item-pair operations, blood/shock unconsciousness, ordinary treatable agents and proximity negotiation with uncontrolled human survivors | Near, `0.323529` |

### Preserved research notes

- New genes: `ACT-381`, `ACT-382`, `SYS-697`–`SYS-700`, `CON-553`,
  `CON-554` and `INF-269`.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: reusable survival, combat, inventory and one-life
  boundaries are retained. Shared Central Economy, blood/shock trauma,
  treatable agents, contextual held-item transformation, proximity negotiation,
  compatible consumption/treatment and vulnerable unconsciousness require
  narrower boundaries than the existing Project Zomboid, Rust and PUBG records.

## Combination assessment

- `COMB-0208` is a strict eighteen-gene subset of the thirty-nine-gene genome,
  joining dynamic shared loot,
  embodied metabolism, infected perception, blood/shock unconsciousness,
  treatable pathogens, contextual held-item operations, local social
  uncertainty and permanent identity death.
- Existing verified combinations are scanned for exact and proper-subset
  relationships by repository validation; deterministic migration will record
  any earlier supported subset before completion.

## Taxonomy impact

- Registry changes: nine new Active genes, evidence-preserving DayZ examples
  on reused genes, `COMB-0208` and memberships in `FAM-004`, `FAM-009` and
  `FAM-010`.
- Taxonomy-change record: none; no existing lifecycle, causal boundary or
  reviewed game signature changes.
- Candidate terms affected: exact server population, spawn coordinate, loot
  quantity, weather, status thresholds, item values, voice distance, agent
  rates, damage and elapsed survival remain parameters. Optional persistent
  construction, vehicles, cooking and alternative maps remain future scopes.

## Negative results

- No separate negative-result record. The review rejected a fabricated
  positive victory, rejected elapsed-time or inland-equipment checkpoints as
  terminals, excluded reconnecting persistence and optional base/vehicle/map
  modules, and rejected the reserve because current stable rules, primary
  evidence and a reproducible permanent-death terminal are available.
