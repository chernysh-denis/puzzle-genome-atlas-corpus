---
game_id: GAME-0296
slug: noita
game_title: Noita
analysis_status: reviewed
reviewed: 2026-09-13
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-199
    - ACT-446
  system:
    - SYS-004
    - SYS-187
    - SYS-213
    - SYS-215
    - SYS-222
    - SYS-578
    - SYS-840
    - SYS-858
    - SYS-859
    - SYS-860
    - SYS-861
    - SYS-862
    - SYS-863
  constraint:
    - CON-175
    - CON-210
    - CON-632
    - CON-633
  information:
    - INF-119
    - INF-128
    - INF-235
    - INF-337
    - INF-338
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Noita

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `881100`, one-app base package `279818`, default public branch Build ID
  `17130612`, manifest `1707227655636660075`, built 2025-01-25 and projected
  updated the same day; checked 2026-09-13. The matching official
  2025-01-25 release notes carry hash
  `8d7016a611ceb7c6530534c83dc6c74c20ba52c6` and change only the maximum
  `EntityTags` count for modding, so no unsupported semantic client number is
  inferred. Beta and archived update branches are excluded.
- Product boundary: the released Nolla Games Windows base game. The soundtrack
  application, mods, Daily Run, Daily Practice, Nightmare, seed-changing tools,
  parallel worlds, later biomes, hidden quests and full victory are excluded.
- Platform, input and setup: English Windows client, keyboard and mouse,
  unmodded `New Game` from a clean profile. The product displays the build and
  world seed when the run starts; both must be transcribed before moving. Entry
  is first ordinary control outside the mountain with the two generated
  starting wands and starter flask. Because no local install existed, no seed,
  generated item or exact carried terminal value is claimed as observed.
- Primary decision loop: inspect both starting wands and their ordered or
  shuffled spell contents, select between wand and flask slots, walk and spend
  replenishing levitation to descend through the generated Mines, fire a wand
  at enemies or mutable terrain, collect reachable gold and optionally replace
  a carried wand or flask within the bounded slots, read local materials and
  stains, and use water when available to wash a harmful or burning stain and
  to convert contacted toxic sludge. Flowing liquids, granular terrain, fire,
  spell timing and hostile movement keep changing in real time while the
  player seeks any first-biome portal.
- Positive terminal: the first settled state immediately after a bottom-of-
  Mines portal transfers the character into the first Holy Mountain, with
  current health, gold, four wand slots and four item slots recorded. The route
  stops before collecting the full-health or spell-refresh pickups, buying,
  choosing a perk, editing a wand or entering the next biome.
- Failure and asymmetry: reaching zero health settles the death screen and
  removes the run's resumable attempt state. Generated terrain, carried wands,
  flasks, gold and the same route cannot be restored; starting another New Game
  generates a new attempt. Profile statistics may remain independently.
- Included: direct walking and levitation; the one personal levitation reserve;
  quick-slot selection; generated starting and found wand compositions; wand
  mana, cast delay and recharge; aimed projectile or explosive use; direct
  hostile combat; health; contact pickup of gold; explicit wand/flask pickup
  and replacement; four wand plus four item slots; one seed-determined mutable
  Mines topology; liquids and granular material moving under gravity; water
  converting toxic sludge; liquid stains and washing; ordinary fire spread and
  extinguishing; effect-driven terrain removal; portal arrival; one-life death.
- Excluded: Holy Mountain pickups, shop, perk choice and wand editing because
  the positive terminal precedes them; guaranteed wand, enemy, gold, flask or
  terrain outcomes; lava-lake detours and temperature phase changes; electricity,
  polymorph, teleportation, alchemical recipes beyond water and toxic sludge;
  bosses, later biomes, parallel worlds, secret areas, quest systems, victory,
  Daily variants, Nightmare, mods, consoles, screenshots, official artwork,
  third-party images, video and audio.
- Reproducible parameterisation: install app `881100` from package `279818` on
  public Build ID `17130612`; start one unmodded New Game and record the on-screen
  build and world seed. Before descent, record both starting wand panels and
  the flask contents. Use each starting wand once against an eligible enemy or
  mutable material, cross one unsupported gap while observing levitation drain
  and supported recovery, then descend by any traversable generated route. If
  toxic sludge or fire contacts the character while water remains, spray water
  to wash the stain; deliberately put water in contact with one reachable toxic-
  sludge edge without entering it. Record any pickup or replacement. End on the
  first Holy Mountain entry or settled death screen. Seed, topology, opponents,
  drops, wand statistics, spell order, damage, gold and terminal inventory are
  run parameters, not predetermined results.
- Direct-play status: not conducted. No Steam manifest, installation directory,
  save directory, matching userdata or local executable was found. Valve fixes
  the product and package; the official site and release notes establish the
  material simulation, wand construction, procedural generation, permanent
  death and build/seed disclosure. The community-maintained official wiki is
  one secondary source family for controls, the Mines/Holy Mountain boundary,
  wand statistics, water, toxic sludge, stains, fire and save details. This is
  an evidence-backed rules reconstruction, not a claimed playthrough, seed,
  entitlement or captured terminal. No audiovisual evidence was used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `NOI-001` | App `881100` and package `279818` identify the released Windows base game and exclude the soundtrack application | Confirmed | Direct | High | P1, P2 |
| `NOI-002` | The public branch projects Build ID `17130612` and manifest `1707227655636660075`, built 2025-01-25 | Confirmed | Corroborated | High | P3, S1 |
| `NOI-003` | New Game displays build and world seed before the generated run begins | Confirmed | Direct | High | P4 |
| `NOI-004` | The world simulates moving materials, chemical reactions, fire, electricity and thermodynamics at pixel scale | Confirmed | Direct | High | P5 |
| `NOI-005` | Wands execute spell contents under order or shuffle, spells-per-cast, mana, cast-delay and recharge statistics | Observation | Corroborated | High | P5, S3, S4 |
| `NOI-006` | Walking and bounded levitation provide direct movement through the generated Mines | Observation | Corroborated | High | S2, S5 |
| `NOI-007` | Water flows, extinguishes fire, washes stains and converts contacted toxic sludge into water | Observation | Corroborated | High | S2, S6, S7 |
| `NOI-008` | Material contact can stain the actor and retain Wet, toxic or On Fire effects until washing, replacement or decay | Observation | Corroborated | High | S6, S7, S8 |
| `NOI-009` | Most defeated enemies drop expiring gold nuggets that collect on contact | Observation | Limited | Medium | S9 |
| `NOI-010` | Bottom-of-Mines portals converge on the first Holy Mountain, whose services begin only after entry | Observation | Corroborated | High | S2, S5, S10 |
| `NOI-011` | Death permanently ends the current generated run rather than restoring a checkpoint | Confirmed | Corroborated | High | P5, S11 |
| `NOI-012` | No local app or save existed, so build, seed and terminal values were not directly captured | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: developed and published by Nolla Games; Windows release
  2020-10-15.
- Platform or physical form: lawfully offered Windows Steam application
  `881100`, base package `279818`; one fresh unmodded generated New Game from the
  mountain entrance to first Holy Mountain entry or settled death.
- Puzzle family: physics and object manipulation; real-time system pressure;
  world topology and perspective.
- Primary and official sources, accessed 2026-09-13:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=881100&cc=ua&l=english),
    for title, Windows platform, developer, publisher, release and application
    boundary.
  - **[P2]** [Valve package data](https://store.steampowered.com/api/packagedetails?packageids=279818&cc=ua&l=english),
    for the one-app base package and current Ukraine offer.
  - **[P3]** [official 2025-01-25 release notes](https://noitagame.com/release_notes/20250125/),
    for the current public update's dated developer hash and limited change.
  - **[P4]** [official 2020-10-22 release notes](https://noitagame.com/release_notes/20201022/),
    for build and world seed always displayed at New Game start.
  - **[P5]** [official Noita site](https://noitagame.com/), for pixel-material
    simulation, liquids, gases, rigid bodies, chemical reactions, electricity,
    thermodynamics, spell construction, procedural generation and permanent
    death.
- Corroborating textual sources, accessed 2026-09-13:
  - **[S1]** [SteamCMD public-branch projection](https://api.steamcmd.net/v1/info/881100),
    for Build ID, manifest, executable and save-root metadata.
  - **[S2]** [Noita controls and play overview](https://noita.wiki.gg/wiki/Controls),
    for movement, levitation, wand fire, flask spray, pickup, kick and the
    first-Holy-Mountain transition.
  - **[S3]** [wand reference](https://noita.wiki.gg/wiki/Wands) and **[S4]**
    [wand-mechanics guide](https://noita.wiki.gg/wiki/Guide:_Wand_Mechanics),
    for starting wands, slots, spell sequencing, shuffle, mana and timing.
  - **[S5]** [Mines reference](https://noita.wiki.gg/wiki/Mines), for the first
    generated biome and its downward route.
  - **[S6]** [water reference](https://noita.wiki.gg/wiki/Water), **[S7]**
    [toxic-sludge reference](https://noita.wiki.gg/wiki/Toxic_Sludge) and
    **[S8]** [fire reference](https://noita.wiki.gg/wiki/Fire), for flow,
    reaction, stains, damage, ignition and extinguishing.
  - **[S9]** [gold-nugget reference](https://noita.wiki.gg/wiki/Gold_Nuggets),
    for hostile drops, expiry and contact collection.
  - **[S10]** [Holy Mountain reference](https://noita.wiki.gg/wiki/Holy_Mountain),
    for first-biome portals and post-entry services.
  - **[S11]** [save reference](https://noita.wiki.gg/wiki/Save), for resumable
    attempt state and its loss at death.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P5`, `S1`–`S11` and `R1`; written-evidence reasoning, not direct play.
- Research record: **[R1]** local preflight on 2026-09-13 found no application,
  manifest, install, save, matching userdata or executable.
- Claim IDs: `NOI-001`–`NOI-012`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`, `ACT-161`, `ACT-164`, `ACT-199` and `ACT-446` own direct
  walking/levitation, aimed wand use against hostiles or mutable terrain,
  quick-slot selection, explicit wand/flask transfer and continuous flask spray.
  No wand-edit command is admitted before the terminal.

### System Behaviour Genes

- Existing `SYS-004`, `SYS-187`, `SYS-213`, `SYS-215`, `SYS-222`, `SYS-578`
  and `SYS-840` own generated selections, fluid/granular redistribution, seeded
  mutable topology, live combat, contact gold pickup, continuous health and
  one-life save deletion. New `SYS-858`–`SYS-863` separate levitation reserve,
  wand execution, material reaction, actor stains, spreading fire and
  effect-driven material-cell removal.

### Constraint Genes

- Existing `CON-175` and `CON-210` own terminal health and the four-wand/four-
  item carrying bounds. New `CON-632` and `CON-633` keep wand readiness/mana
  and positive levitation reserve as distinct legality predicates.

### Information, Objective and Time Genes

- Existing `INF-119`, `INF-128` and `INF-235` expose personal reserves, carried
  capacity and the local threats/pickups/effects. New `INF-337` exposes the
  executable wand specification and `INF-338` joins local material identity to
  the current stain state. `OBJ-026` owns reaching any first portal and
  `TIM-003` owns uninterrupted live resolution.

## Reproducible transitions

| Before | Action | Bounded resolution | Claim |
|---|---|---|---|
| Fresh New Game has displayed its identifiers | Transcribe build and world seed before moving | One exact generated attempt becomes reproducible without fixing its outcomes | `NOI-002`, `NOI-003` |
| Two starting wands and flask are carried | Inspect each wand, select it and fire once at an eligible target | Spell order or shuffle, mana, cast delay and recharge govern the shot | `NOI-005` |
| An unsupported gap interrupts the descent | Hold levitation, steer, then land and release | The reserve drains in flight and replenishes on support; exhaustion would force descent | `NOI-006` |
| Water and toxic sludge are reachable | Spray water onto the sludge edge without entering it | Contact converts affected toxic sludge into water and the liquid continues flowing | `NOI-004`, `NOI-007` |
| A harmful or burning stain occurs while water remains | Spray or enter water | The coating is washed or replaced and its ongoing effect ends as the stain clears | `NOI-007`, `NOI-008` |
| Mutable terrain blocks a local line | Fire an eligible starting-wand effect into it | Affected cells are removed or displaced and collision plus liquid paths update | `NOI-004`, `NOI-005` |
| A defeated enemy leaves reachable gold | Contact the nugget before expiry | Gold transfers automatically to the run counter | `NOI-009` |
| A bottom portal is reached | Enter it | The run transfers to the first Holy Mountain and stops before its services | `NOI-010` |
| Health reaches zero first | Let death settlement complete | The generated attempt becomes non-resumable and the death screen is terminal | `NOI-011` |

## Strategic and experiential structure

- Planning horizon: the visible local material field, health, levitation,
  flask amount, wand statistics and carried slots constrain the next few
  seconds; the seed fixes but does not disclose the route ahead.
- Local tactics: preserve lift for the far lip of a gap, wait for wand readiness,
  avoid putting a volatile material chain beside the avatar, and spend water on
  a harmful stain or toxic route rather than treating it as decoration.
- Medium-term structure: descending gains gold and possible wand choices but
  makes retreat through changed terrain harder. A new wand can improve output
  while consuming one of four slots and changing the executable spell program.
- Irreversibility: terrain removal, material reaction, consumed flask contents,
  missed expiring gold, replacements and damage persist for this run; death
  erases the entire resumable attempt.

## Replay and variation

- The recorded seed and generator build determine Mines topology and generated
  placements. Wands, spells, flask contents, hostiles and drops vary within
  that generated attempt; movement, material and combat outcomes then diverge
  through simulation.
- The packet permits fighting, bypassing and optional replacement, but requires
  inspection of both starters, one use of each, one levitation drain/recovery
  control and the water/toxic-sludge reaction when water is available.

## Adjacent systems and history

- Terraria shares direct traversal, generated mutable terrain, carried slots,
  combat and health but breaks addressed tiles into drops; Noita instead runs
  cell materials, reactions, stains and effect-driven destruction continuously.
- Dead Cells shares a generated first-biome real-time run and terminal health,
  but its authored chunks, equipment loop and retained meta-unlocks do not
  execute a wand program or conserve a reacting material field.
- Baba Is You changes noun-level rules on a discrete board. Noita's material
  rules remain fixed while their simulated cells and reaction fronts move.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-199`, `ACT-446` | route, wand, slot, flask and targets |
| System Behaviour | `SYS-004`, `SYS-187`, `SYS-213`, `SYS-215`, `SYS-222`, `SYS-578`, `SYS-840`, `SYS-858`, `SYS-859`, `SYS-860`, `SYS-861`, `SYS-862`, `SYS-863` | seed, materials, rates, spells, timings and outcomes |
| Constraint | `CON-175`, `CON-210`, `CON-632`, `CON-633` | terminal threshold, slots, mana and lift reserve |
| Information | `INF-119`, `INF-128`, `INF-235`, `INF-337`, `INF-338` | HUD, material labels and inspection layout |
| Objective | `OBJ-026` | first Holy Mountain portal |
| Time | `TIM-003` | simulation and input cadence |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `295` (`GAME-0001`–`GAME-0295`).
- Exact genome matches: none.
- Tied near matches: `GAME-0258` — Prey (2017) (`11 / 44 = 0.250000`); `GAME-0272` — Serious Sam 4 (`9 / 36 = 0.250000`).
- Supported combination subsets: none.
- Scan date: 2026-09-13.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0258` — Prey (2017) | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-199`, `SYS-215`, `SYS-578`, `CON-210`, `INF-119`, `INF-128`, `OBJ-026`, `TIM-003` | Both packets join direct exploration, quick-slot tools, aimed combat, bounded inventory, visible personal state and a live route exit. Prey uses authored station geometry, fixed weapons and checkpoint recovery. Noita instead executes generated wand programs inside a reacting mutable material field, spends levitation and deletes the one-life attempt on death. | Near, `0.250000` |
| `GAME-0272` — Serious Sam 4 | `ACT-008`, `ACT-161`, `ACT-164`, `SYS-215`, `SYS-222`, `SYS-578`, `INF-119`, `OBJ-026`, `TIM-003` | Both packets expose direct real-time movement, selected ranged attacks, hostile drops, continuous health and an onward route. Serious Sam 4 is an authored finite-group ammunition corridor with checkpoint continuation. Noita's route is seed-determined, materially transformable and permanently lost at death. | Near, `0.250000` |

## Taxonomy impact

- New genes: `SYS-858`–`SYS-863`, `CON-632`, `CON-633`, `INF-337` and
  `INF-338`.
- Existing wording or lifecycle changes: none.
- Taxonomy-change record: none; no earlier definition or signature changes.
- Candidate terms affected: Noita, Mines, Holy Mountain, wand, spell, shuffle,
  levitation, water, toxic sludge, stain, Wet, On Fire, gold nugget, build and
  world seed remain product, route, interface, evidence or game parameters.

## Negative results

- `SYS-188` is rejected because the bounded control never requires a
  temperature-threshold phase change. Lava and freezing remain outside scope.
- `SYS-212`, `SYS-324` and `SYS-755` do not own Noita terrain removal: it is
  neither harvest-to-drop, bounded match deformation nor one discrete durable
  object.
- Holy Mountain wand editing, shopping, perk choice and recovery are not
  admitted because the terminal is the first entry state before those actions.
- No exact build, seed, item, topology or terminal inventory is represented as
  observed, and no audiovisual evidence was opened or used.

## Delta summary

## New facts

- [Confirmed/Observation | Direct/Corroborated | High] `NOI-001`–`NOI-012`:
  one generated first-biome run binds executable wand composition, finite
  levitation and interacting simulated materials to portal entry or permanent
  attempt loss.

## New genes

- [Observation | Corroborated | High] `SYS-858`–`SYS-863`, `CON-632`,
  `CON-633`, `INF-337` and `INF-338` isolate ten portable boundaries not owned
  by lower-ID genes.

## New combinations

- [Observation | Direct | High] None proposed; deterministic subset validation
  decides whether any existing verified combination is supported.

## Taxonomy changes

- [Observation | Direct | High] None; no existing definition, lifecycle or
  earlier game signature changes.

## Inferences

- [Strong Pattern | Corroborated | High] Noita's puzzle structure comes from
  forecasting interactions among persistent material cells and executable wand
  contents under one-life pressure, not from a separate authored puzzle mode.

## Open questions

- Exact current-build build/seed text, starting wand rolls, flask contents and
  terminal state await lawful local access and a performed reproduction.

## Contradictions

- None within the declared build, mode and first-biome boundary.

## New questions

- Which first-Mines seeds make the water/toxic-sludge control reachable without
  relying on a generated starter flask after clean-profile state changes?

## Next recommended game

- [Hypothesis | Limited | High] MONSTER HUNTER RISE.
- Optimisation criterion: replace one-life material simulation with a retained
  quest whose movement and recovery are shaped by Wirebug and Palamute systems.
- Expected information gain: compare the first large-monster settlement against
  both existing Monster Hunter genomes without importing Sunbreak systems.
- Backlog impact: close the reserved nine-game selection-018 horizon.

## Why this game

- [Hypothesis | Limited | High] Rise is the last reserved contrast unit and can
  test which Wirebug-era rules transfer beyond World and Wilds.

## Confidence and unresolved questions

- Confidence: High for product, official simulation premise, build/seed
  disclosure and permanent death; Medium for exact unperformed first-biome
  values and community-sourced UI details.
- Resolution path: run the declared public build, capture only text-state build,
  seed, wand panels and terminal counters, and compare them with this packet.
- Consequence: generated quantities remain parameters rather than observations.
