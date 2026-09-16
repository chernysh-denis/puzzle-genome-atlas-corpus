---
game_id: GAME-0294
slug: v-rising
game_title: V Rising
analysis_status: reviewed
reviewed: 2026-09-13
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-087
    - ACT-123
    - ACT-161
    - ACT-164
    - ACT-199
    - ACT-204
    - ACT-223
    - ACT-341
    - ACT-454
  system:
    - SYS-215
    - SYS-216
    - SYS-222
    - SYS-327
    - SYS-328
    - SYS-330
    - SYS-332
    - SYS-578
    - SYS-591
    - SYS-736
    - SYS-856
    - SYS-857
  constraint:
    - CON-136
    - CON-210
    - CON-281
    - CON-292
    - CON-295
    - CON-297
    - CON-630
    - CON-631
  information:
    - INF-067
    - INF-073
    - INF-075
    - INF-119
    - INF-125
    - INF-128
    - INF-131
    - INF-132
    - INF-142
  objective:
    - OBJ-173
  time:
    - TIM-003
    - TIM-007
---

# Game: V Rising

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Product names,
Journal labels, resource quantities, territory identity, day phase and save
identity parameterise the genes but do not enter their labels.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `1604030`, one-app consumer base package `568520`, default public branch Build
  ID `23521359`, updated 2026-06-02; checked 2026-09-13. Stunlock's latest
  client-affecting notice is `V Rising 1.1 Hot Fix 11`; the later `Hot Fix 12`
  adds only a server-side multiplayer ownership-permission check and therefore
  does not replace the observed client build for this offline packet.
- Product boundary: V Rising base game by Stunlock Studios, not the commercial-
  licence package `943863`, PlayStation edition, cosmetic or Castlevania DLC,
  soundtrack, modification or historical branch.
- Platform, input and world: English Windows client, keyboard and mouse, fresh
  private solo PvE world in LAN/offline mode, `StandardPvE` and
  `Difficulty_Normal`, with no advanced-setting changes. Public servers, PvP,
  co-op, clans, admin commands and custom multipliers are excluded.
- Entry: first ordinary control of the new vampire in the opening crypt before
  `Collecting the Remains` has settled.
- Primary decision loop: follow the one-at-a-time Journal stages; move and use
  early melee, Shadowbolt, Blood Rite and Veil actions against living hostiles;
  collect Bones, Wood, Stone, Plant Fibre and Blood Essence; hand-craft and equip
  the required Bone and Boneguard loadout; weaken a living blood-bearing target
  below the feeding threshold, complete Feed or Bite and accept replacement of
  the current blood pool, type, quality and passive profile; gather the declared
  `Gathering` totals; inspect the map for an eligible unclaimed Build Location;
  place and interact with a Castle Heart there; supply Blood Essence to power
  it; extend connected Rough Floor, Palisade Wall, Entrance and Gate pieces into
  a closed perimeter; place the Wooden Coffin, Small Chest and Mist Brazier;
  fuel and activate the brazier with Bones; close the gate and remain inside the
  claimed, powered, mist-protected early shelter.
- Positive terminal: after the `Shelter` Journal stage has exposed its early
  fixtures, one Castle Heart legally claims the selected Build Location and has
  positive Blood Essence; a continuous Rough Floor footprint supports a fully
  closed Palisade perimeter with a shut Gate; one Wooden Coffin, one Small Chest
  and one bone-fuelled active Mist Brazier are inside. Let an autosave occur,
  exit and reload the same private world; the same claimed shelter is the
  intended retained successor. No local application or save existed, so the
  autosave/reload was not performed and no returned object or meter value is
  claimed as observed.
- Important enclosure boundary: this is an unroofed early palisade enclosure,
  not a later stone room. The active Mist Brazier supplies the lawful early sun
  protection. Full Castle Walls, Castle Flooring, automatic roof creation,
  Castle Heart level 2 and every later production room are excluded.
- Negative states: Feed is unavailable while the target is dead, non-living or
  above its required low-health threshold, and movement or interruption can
  abort the channel. Castle Heart placement fails outside a valid unclaimed
  Build Location or without its materials. A Heart without Blood Essence loses
  power and eventually its anti-decay protection; an open gate or exhausted
  brazier does not satisfy the closed protected-shelter terminal.
- Included: the current opening Journal sequence through `Shelter`; movement,
  basic attacks, Shadowbolt, Blood Rite and Veil; health, ability cooldowns,
  blood reserve/type/quality, target telegraphs and sunlight warning; gathering
  and drops; bounded carried stacks; personal timed crafting and equipping;
  weakened-target feeding; Build Location discovery; Castle Heart placement,
  claim, Blood Essence power and decay pressure; connected early floors,
  palisades, entrance and gate; coffin, chest and Mist Brazier placement and
  operation; day/night exposure; ordinary death/respawn; local autosaves and
  same-world continuation.
- Excluded: roofed stone construction, refinement and production stations;
  Castle Heart upgrades; V Blood tracking or defeat; Wolf Form, servants,
  prisons, horses, waygates, gardens, multiple territories and castle relocation;
  public-server persistence, sieges, raids, PvP, clans and ownership transfer;
  later regions, campaign bosses and ending; altered rules, mods, DLC cosmetics,
  achievements, screenshots, official artwork, third-party images, video and
  audio.
- Reproducible parameterisation: install app `1604030` from package `568520`,
  confirm public Build ID `23521359`, create a fresh English private solo LAN
  world with the `StandardPvE` and `Difficulty_Normal` presets and do not edit
  advanced settings. Complete the Journal stages from `Collecting the Remains`
  through `Shelter`. Preserve enough Wood, Stone, Plant Fibre, Bones and Blood
  Essence for a legal Heart, an expanded connected floor, a closed palisade
  perimeter, coffin, chest and active brazier. Choose any available Build
  Location, claim it with the Heart, power the Heart, close the constructed Gate
  and activate the brazier. Wait for an autosave, exit and continue that same
  world. Spawn, target identities, exact route, incidental drops, blood profile,
  damage, extra materials, footprint and autosave slot remain parameters.
- Potential scoped modules: direct save/reload observation; level-2 stone room
  and automatic roof; one refinement chain; first V Blood hunt; ordinary
  death-and-coffin recovery; servant conversion; or multiplayer castle authority
  each requires its own entry, loop, terminal and evidence review.
- Direct-play status: not conducted. No V Rising application bundle, Steam
  manifest, install directory, Stunlock save directory or matching userdata was
  found locally. Valve and Stunlock establish the product, current build window,
  offline private-world option, default-preset vocabulary, sunlight, Mist
  Brazier and save boundaries. The current player-maintained V Rising Wiki
  supplies the clause-level opening Journal order, Feed threshold and early
  construction costs. This is an evidence-backed rules reconstruction, not a
  claimed playthrough, entitlement, autosave or reload. No audiovisual source
  was opened, played, heard, analysed or used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `VRS-001` | Steam app `1604030` and one-app consumer package `568520` identify the released Windows base product by Stunlock Studios | Confirmed | Direct | High | P1, P2 |
| `VRS-002` | The public branch projects Build ID `23521359` from 2026-06-02; Hot Fix 11 is the matching client notice and Hot Fix 12 is server-side only | Confirmed | Corroborated | High | P3, P4, S1 |
| `VRS-003` | A fresh private game can run solo offline in LAN mode, while the current server schema names `StandardPvE` and `Difficulty_Normal` as preset boundaries | Confirmed | Direct | High | P5, P6, P7 |
| `VRS-004` | The opening Journal advances one taught predicate at a time from bone equipment and combat actions through `Gathering`, Castle Heart construction, `Fortify` and `Shelter` | Observation | Corroborated | High | S2–S6 |
| `VRS-005` | Feed requires a living blood-bearing target below one quarter health; accepted feeding kills the target, refills the blood pool and replaces its type, quality and passive profile | Observation | Corroborated | High | S7–S9 |
| `VRS-006` | Blood and sunlight are independent live survival pressures: blood drains and powers recovery, while direct daylight produces warnings and then rapid damage unless shade or mist protects the vampire | Confirmed | Corroborated | High | P8, P9, S8, S10 |
| `VRS-007` | `Gathering` requires 300 Wood, 300 Stone and 50 Blood Essence before the Castle Heart recipe becomes available | Observation | Limited | Medium | S3 |
| `VRS-008` | A level-1 Castle Heart costs 240 Stone and 30 Blood Essence, must occupy a valid unclaimed territory and claims that whole Build Location | Observation | Corroborated | High | S4, S11, S12 |
| `VRS-009` | Blood Essence placed in the Heart powers castle functions; exhausting it removes protection and permits castle decay | Confirmed | Corroborated | High | P10, S11 |
| `VRS-010` | `Lord of Shadows` unlocks Rough Floor, Palisade Wall, Entrance, Gate and Pillar after Heart interaction; `Fortify` requires three Floors and three Palisades | Observation | Corroborated | High | S4, S5 |
| `VRS-011` | `Shelter` asks for a Wooden Coffin, Small Chest and Mist Brazier; the brazier costs 120 Stone and consumes Bones to create sun-blocking mist | Confirmed | Corroborated | High | P9, S6, S13–S15 |
| `VRS-012` | Full walls and flooring create permanent roof protection only after later castle upgrades, so the scoped early enclosure remains unroofed and uses mist | Confirmed | Corroborated | High | P9, S12 |
| `VRS-013` | Local/private sessions retain versioned autosaves and can be continued through Load Game; official transfer guidance names castles, map exploration and world structures as saved state | Confirmed | Direct | High | P6, P11 |
| `VRS-014` | No local executable, manifest or save existed, so the intended autosave/reload is an unexecuted verification boundary | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: developed and published by Stunlock Studios; Windows 1.0
  release 2024-05-08.
- Platform or physical form: lawfully offered English Windows Steam app
  `1604030`, consumer base package `568520`; fresh private offline solo PvE
  world on normal presets.
- Puzzle family: real-time system pressure; inventory and fixture dependencies;
  world topology and perspective; ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-13:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=1604030&cc=ua&l=english),
    for title, app, developer, publisher, release, Windows, single-player, Save
    Anytime and Steam Cloud categories and available packages.
  - **[P2]** [Valve package data](https://store.steampowered.com/api/packagedetails?packageids=568520&cc=ua&l=english),
    for the one-app consumer base package and current Ukraine offer.
  - **[P3]** [official Hot Fix 11 announcement](https://store.steampowered.com/news/app/1604030/view/1833968530900688),
    for the latest client localization correction in the observed build window.
  - **[P4]** [official Hot Fix 12 announcement](https://store.steampowered.com/news/app/1604030/view/1843481262694634),
    used only to bound its later server-side multiplayer ownership check.
  - **[P5]** [official V Rising overview](https://playvrising.com/), for solo or
    online survival, blood feeding, sunlight danger, castle building and
    persistent open-world scope.
  - **[P6]** [official PC 1.1 server instructions](https://github.com/StunlockStudios/vrising-dedicated-server-instructions/blob/master/1.1.x-pc/INSTRUCTIONS.md),
    for current persistence version, autosaves, local-session paths, presets and
    save loading.
  - **[P7]** [official private-game offline guide](https://guides.playvrising.com/hc/en-us/articles/5549283940125-Private-Game-Offline-Mode),
    for solo LAN/offline play.
  - **[P8]** [official advanced-setting guide](https://guides.playvrising.com/hc/en-us/articles/5549267131677-Advanced-Game-Settings),
    for configurable blood drain and sun pressure, which remain unchanged here.
  - **[P9]** [official sunlight guide](https://guides.playvrising.com/hc/en-us/articles/28675169915805-How-to-Manage-Sunlight-Exposure-and-Avoid-Fighting-During-the-Day),
    for live warning and damage, shifting shade, 120-Stone Mist Brazier, Bone
    fuel and later full-roof protection.
  - **[P10]** [Stunlock Castle Heart development reference](https://blog.stunlock.com/v-rising-update-12-dark-domains/),
    for Blood Essence power and decay when the Heart runs dry.
  - **[P11]** [official private-save transfer guide](https://guides.playvrising.com/hc/en-us/articles/28560453725725-How-to-Transfer-Save-Files-to-a-New-Host-in-V-Rising-Private-Server),
    for local and cloud autosaves, Load Game and retained castles, structures
    and map exploration.
- Corroborating textual sources, accessed 2026-09-13:
  - **[S1]** [SteamCMD public-branch projection](https://api.steamcmd.net/v1/info/1604030),
    for Build ID `23521359` and its timestamp; secondary distribution data.
  - **[S2]** [Journal reference](https://vrising.fandom.com/wiki/Journal), for
    the complete current opening-stage order through `Shelter`.
  - **[S3]** [`Gathering`](https://vrising.fandom.com/wiki/Gathering),
    **[S4]** [`Lord of Shadows`](https://vrising.fandom.com/wiki/Lord_of_Shadows),
    **[S5]** [`Fortify`](https://vrising.fandom.com/wiki/Fortify) and **[S6]**
    [`Shelter`](https://vrising.fandom.com/wiki/Shelter), for clause-level
    requirements and unlocked early structures.
  - **[S7]** [abilities reference](https://vrising.fandom.com/wiki/Abilities),
    **[S8]** [blood reference](https://vrising.fandom.com/wiki/Blood) and
    **[S9]** [Blood Mend reference](https://vrising.fandom.com/wiki/Blood_Mend),
    for Feed eligibility, blood-profile replacement, drain and recovery.
  - **[S10]** [sun-exposure reference](https://vrising.fandom.com/wiki/Sun_Exposure),
    for exposure accumulation, shade recovery and mist operation.
  - **[S11]** [Castle Heart reference](https://vrising.fandom.com/wiki/Castle_Heart)
    and **[S12]** [castle-building reference](https://vrising.fandom.com/wiki/Castle_Building),
    for Heart cost, territorial claim, connected construction and early-versus-
    roofed boundaries.
  - **[S13]** [Small Chest reference](https://vrising.fandom.com/wiki/Small_Chest),
    **[S14]** [Wood reference](https://vrising.fandom.com/wiki/Wood) and
    **[S15]** [Basic Flooring reference](https://vrising.fandom.com/wiki/Basic_Flooring),
    for scoped fixture and floor costs.
- Source-class limitation: the exact Journal predicates, feeding threshold and
  early construction costs remain player-maintained. Official Stunlock material
  independently establishes the private-world, blood, sun, Heart-power,
  brazier, roof and persistence invariants. Exact counts are kept only where the
  current wiki makes the selected route reproducible; they are not promoted to
  universal taxonomy labels.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P11`, `S1`–`S15` and `R1`; written-evidence reasoning, not direct play.
- Research record: **[R1]** local preflight on 2026-09-13 found no application,
  Steam manifest, install, save directory or matching userdata.
- Claim IDs: `VRS-001`–`VRS-014`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008` owns direct movement and shade-seeking; `ACT-123` personal
  crafting; `ACT-161` early weapon and Shadowbolt attacks against living targets
  or resource objects; `ACT-164` quick-slot selection; `ACT-199` inventory
  transfer and equipping; `ACT-204` connected floor, wall, entrance and gate
  placement; `ACT-223` timed Blood Rite or Veil response; `ACT-341` the Journal,
  Heart, gate, coffin, chest and brazier interactions; and `ACT-087` the
  irreversible transfer of Blood Essence or Bones into a compatible fixture.
- New `ACT-454` owns the distinct channelled Feed/Bite command on a weakened
  living blood-bearing target. It is not an ordinary strike or item use.
  Claims: `VRS-004`–`VRS-011`.

### System Behaviour Genes

- Existing `SYS-215` owns live combat; `SYS-216` ordinary death and return;
  `SYS-222` world-drop pickup; `SYS-328` timed personal crafting; `SYS-330`
  connected building health and collision; `SYS-578` damage and recovery;
  `SYS-591` resource return; and `SYS-736` the one-stage-at-a-time Journal.
- Existing `SYS-327`, generalised by `TAXONOMY_CHANGE_071`, owns blood-reserve
  and sunlight-exposure updates alongside health. Existing `SYS-332`, likewise
  generalised, owns Blood Essence consumption by the Heart and loss of power or
  decay protection when its reserve is absent.
- New `SYS-856` settles a completed Feed by killing the source, refilling the
  pool and replacing blood type, quality and passive profile. New `SYS-857`
  turns an accepted Castle Heart placement into persistent ownership of one
  predefined Build Location and authorises connected construction there.
- Resolution order: Journal predicates unlock the next recipes; attacks and
  gathering produce eligible resources and a weakened feed target; Feed replaces
  the blood state; crafting emits equipment; legal Heart placement claims the
  territory; supplied Blood Essence powers it; connected blocks and fixtures
  form the closed shelter; sunlight and blood continue updating throughout; the
  autosave retains the resulting world. Claims: `VRS-004`–`VRS-013`.

### Constraint Genes

- Existing `CON-136` owns ordered persistent Journal gates; `CON-210` carried
  stack and slot capacity; `CON-292` clear supported building footprints;
  `CON-297` known-recipe ingredients and output capacity. Generalised `CON-281`
  owns blood, health, sunlight protection and recovery as viability bounds;
  generalised `CON-295` requires sufficient reserve in the connected ownership
  core for power and decay protection.
- New `CON-630` requires a living blood-bearing target below the Feed threshold
  and an uninterrupted reachable channel. New `CON-631` requires the Heart's
  materials and a valid unclaimed Build Location before its territorial claim
  can settle.
- Scarce or gated state is the active Journal stage, health, blood reserve and
  profile, daylight/shade state, carried slots, Wood, Stone, Plant Fibre, Bones,
  Blood Essence, free territory, Heart reserve, connected footprint and brazier
  fuel. Claims: `VRS-004`–`VRS-012`.

### Information Genes

- Existing `INF-067` owns current Journal requirements and unlocks; `INF-073`
  the hotbar and equipment; `INF-075` health, blood and wear state; `INF-119`
  ability resources and cooldowns; `INF-125` map position and Build Locations;
  `INF-128` loot and inventory fit; `INF-131` placement legality, Heart power,
  remaining protection and fixture state; `INF-132` recipe dependencies; and
  `INF-142` hostile telegraphs and sunlight warnings before response.
- No omniscient map, hidden future blood profile or exact future damage is
  claimed. Claims: `VRS-004`–`VRS-012`.

### Objective Genes

- New `OBJ-173` owns the complete opening dependency chain to one powered,
  claimed, closed and mist-protected early shelter retained by the private-world
  save. A placed but unpowered Heart, open perimeter, unfuelled brazier, roof
  assumption or unsaved transient state is not the positive terminal. Claims:
  `VRS-004`, `VRS-007`–`VRS-014`.

### Time Genes

- Existing `TIM-003` owns combat, blood drain, sunlight, moving shade, crafting,
  Heart reserve and brazier fuel while ordinary input remains live. Existing
  `TIM-007` owns the retained private-world autosave history that can be loaded
  for another continuation; the selected reload remains unexecuted. Claims:
  `VRS-006`, `VRS-009`, `VRS-011`, `VRS-013`, `VRS-014`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Current Journal predicate is incomplete | Perform its required action or reach its state | The stage records completion and exposes the next instruction and unlock | staged opening dependency | `VRS-004` |
| Living blood-bearing target is below the threshold | Hold Feed; optionally finish with Bite | Completion kills the target, fills the pool and replaces type, quality and passives; interruption cancels | distinct blood acquisition | `VRS-005` |
| Vampire enters direct daylight | Move toward current shade or mist | Warning accumulates before rapid health damage; protection clears exposure | live environmental pressure | `VRS-006` |
| `Gathering` totals are satisfied | Accept stage settlement | Castle Heart construction becomes available | resource-to-unlock gate | `VRS-007` |
| Valid unclaimed Build Location and Heart materials exist | Place and interact with Castle Heart | The territory becomes claimed and connected construction is authorised | territorial ownership core | `VRS-008`, `VRS-010` |
| Heart reserve is empty or positive | Transfer Blood Essence, then allow time to advance | Positive reserve powers protection; exhaustion removes it and permits decay | upkeep boundary | `VRS-009` |
| Legal sockets and materials exist in claimed territory | Place floors, palisades, entrance and gate | Connected health-bearing collision forms the chosen closed perimeter | early enclosure | `VRS-010` |
| `Shelter` fixtures are unlocked | Place coffin, chest and Mist Brazier inside | Each fixture becomes locally operable | terminal fixture set | `VRS-011` |
| Brazier is empty and Bones are carried | Transfer Bones and activate it | Fuel is consumed over time while protective mist covers its radius | early sun protection | `VRS-011`, `VRS-012` |
| Powered claimed enclosure is complete and closed | Wait for autosave, exit and load the same world | Intended check returns the retained shelter; not executed locally | positive persistence boundary | `VRS-013`, `VRS-014` |

## Strategic and experiential structure

- Local decision: fight in shade, create a safe Feed window, preserve the right
  materials and place each piece where it closes rather than fragments the
  perimeter.
- Medium-term planning: satisfy Journal predicates in order while reserving
  Heart power and enough Stone/Bones for a sun-safe work area.
- Long-term structure: a vulnerable mobile vampire converts gathered resources
  into a persistent owned territory whose power core, enclosure and local mist
  create the first stable continuation base.
- Common heuristics: travel at night or through moving shade; Feed before the
  pool becomes critical; inspect unclaimed Build Locations early; power the
  Heart before expansion; put the brazier where its finite radius covers the
  unroofed interior; close the gate before the terminal check.
- Failure attribution: distinguish target health/type, interrupted Feed,
  missing Journal prerequisite, full inventory, invalid or claimed territory,
  blocked socket, missing material, empty Heart, open gate and empty brazier.
- Player-trust factors: Journal counters, target health and blood information,
  inventory and recipe panels, placement preview, Heart reserve, clock,
  sunlight warning and visible mist disclose the important transitions.
- Claim IDs: `VRS-004`–`VRS-013`.

## Replay and variation

- What changes: chosen Build Location, travel and gathering route, target blood
  type/quality, incidental combat, drops, material overage, day phase, footprint,
  brazier position and autosave identity.
- Randomness or procedural generation: Vardoran and its Build Locations are
  authored, while ordinary target populations, loot and available territory can
  vary; no exact seed or coordinate is required.
- Multiple viable strategies: resources and feed targets can come from several
  nearby sources, the early perimeter may use any legal connected geometry and
  the three required fixtures may occupy any protected interior positions.
- Typical replay motive: alternative settings, blood profiles, castle designs,
  co-op/PvP servers and later progression; all lie outside the packet.
- Claim IDs: `VRS-003`–`VRS-013`.

## Adjacent systems and history

- Direct predecessors: the current 1.1 PC branch and its server schema are the
  sole admitted rules; Early Access free-placement and historical castle rules
  are context only.
- Variants: PvP, public servers, co-op, advanced settings, DLC cosmetics and
  later castle tiers change authority, timing, costs or capability and are
  excluded.
- Similar games: Valheim shares live survival, gathering, crafting, connected
  construction and an early shelter; Rust shares an ownership core, reserve-
  backed structural protection and persistent claimed building; The Forest
  shares gathered-material shelter completion but not territorial claim or
  ongoing Heart power.
- Important differences: V Rising makes target blood both a replenished reserve
  and replaceable passive profile, makes sunlight a moving lethal exposure, and
  turns one Heart into a predefined territory claim whose early unroofed base
  needs finite mist protection.
- Claim IDs: `VRS-002`–`VRS-013`.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `293` (`GAME-0001`–`GAME-0293`).
- Exact genome matches: none.
- Tied near matches: `GAME-0197` — Valheim (`24 / 60 = 0.400000`).
- Supported combination subsets: none.
- Scan date: 2026-09-13.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0197` — Valheim | `ACT-008`, `ACT-087`, `ACT-123`, `ACT-161`, `ACT-164`, `ACT-199`, `ACT-204`, `ACT-223`, `SYS-215`, `SYS-216`, `SYS-222`, `SYS-330`, `SYS-591`, `CON-136`, `CON-210`, `CON-292`, `CON-297`, `INF-073`, `INF-075`, `INF-128`, `INF-131`, `INF-132`, `INF-142`, `TIM-003` | Both traverse a live survival world, gather resources, manage inventory, craft and equip an early loadout, construct connected shelter blocks, use fixture-bound item transfers, fight with timed defence, expose the relevant dependencies and permit death/return. Valheim adds a seeded procedural world, active-food set, comfort/rest, station cover and repair, skill progression, Forsaken summon and trophy-mounted power. V Rising instead replaces a typed blood profile through weakened-target feeding, survives moving sunlight, follows staged Journal unlocks, claims a predefined territory with a Heart, pays its ongoing Blood Essence reserve and ends at a closed mist-protected early shelter retained by autosave. | Near, `24 / 60 = 0.400000` |

- New genes: `ACT-454`, `SYS-856`, `SYS-857`, `CON-630`, `CON-631` and
  `OBJ-173`.
- Classification result: `New genes`.
- Evidence and reasoning: the shared survival-construction backbone transfers
  to Valheim and other earlier owners, while feeding's typed profile
  replacement, an authored whole-territory Heart claim and the powered closed
  early-shelter terminal do not.

### Preserved research notes

- New genes: `ACT-454`, `SYS-856`, `SYS-857`, `CON-630`, `CON-631` and
  `OBJ-173`.
- Classification result: `New genes`.
- Evidence and reasoning: the shared survival-construction backbone transfers
  to Valheim and other earlier owners, while feeding's typed profile
  replacement, an authored whole-territory Heart claim and the powered closed
  early-shelter terminal do not.
- Generalised genes: `SYS-327`, `SYS-332`, `CON-281` and `CON-295` under
  [`TAXONOMY_CHANGE_071`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_071.md).
- Classification: `FAM-010`, `FAM-013`, `FAM-014`, `FAM-017`.
- Evidence and reasoning: no later roof, V Blood, server authority or station
  chain is imported merely because the base product supports it.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-087`, `ACT-123`, `ACT-161`, `ACT-164`, `ACT-199`, `ACT-204`, `ACT-223`, `ACT-341`, `ACT-454` | route, fixture transfer, craft, strike, equipment, building, response and Feed channel |
| System Behaviour | `SYS-215`, `SYS-216`, `SYS-222`, `SYS-327`, `SYS-328`, `SYS-330`, `SYS-332`, `SYS-578`, `SYS-591`, `SYS-736`, `SYS-856`, `SYS-857` | combat, survival, crafting, construction, upkeep, Journal, blood and claim state |
| Constraint | `CON-136`, `CON-210`, `CON-281`, `CON-292`, `CON-295`, `CON-297`, `CON-630`, `CON-631` | prerequisites, capacity, survival, placement, reserve, crafting, Feed and territory legality |
| Information | `INF-067`, `INF-073`, `INF-075`, `INF-119`, `INF-125`, `INF-128`, `INF-131`, `INF-132`, `INF-142` | Journal, equipment, blood, abilities, map, loot, castle, recipe and warning display |
| Objective | `OBJ-173` | powered claimed closed early shelter retained in the private world |
| Time | `TIM-003`, `TIM-007` | live pressure and retained autosave history |

## Taxonomy impact

- Registry changes: six new Active owners; product-neutral wording and V Rising
  support for four existing survival and ownership-core owners; no earlier
  signature or lifecycle change.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_071`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_071.md).
- Candidate terms affected: Feed, Bite, Blood Essence, Journal, Gathering,
  Build Location, Castle Heart, Rough Floor, Palisade Wall, Entrance, Gate,
  Wooden Coffin, Small Chest, Mist Brazier, StandardPvE and Difficulty_Normal
  remain parameters rather than canonical IDs.

## Negative results

- `SYS-331` and `CON-294` are rejected because the scoped private solo world
  does not configure identity authorisation, locks or hostile building
  privilege. `SYS-333` is rejected because the local LAN world pauses when the
  host exits rather than continuing hostile simulation while absent.
- `SYS-632` is rejected because target blood replaces a typed passive profile
  and reserve; it is not a simultaneous multi-food set. `SYS-698` is rejected
  because no coupled bleeding, shock, unconsciousness and waking pipeline is
  present. `CON-626` is rejected because an authored Build Location is claimed
  by a placed Heart, not surveyed and purchased by a mobile stellar constructor.
- Later automatic roof creation, station processing, servants, V Blood tracking,
  multiple territories, raids and clan authority are excluded rather than
  inferred from the base-game feature envelope.

## Delta summary

## New facts

- [Observation | Corroborated | High] The opening Journal reaches a first
  territory claim and closed mist-protected shelter only after blood, gathering,
  crafting and staged construction predicates (`VRS-004`–`VRS-012`).
- [Confirmed | Direct | High] App `1604030`, package `568520`, public Build ID
  `23521359`, private LAN mode, current preset vocabulary and versioned local
  autosaves freeze the Windows packet; no local play or reload is claimed
  (`VRS-001`–`VRS-003`, `VRS-013`, `VRS-014`).

## New genes

- [Observation | Corroborated | High] `ACT-454` and `CON-630` isolate the
  player-held Feed command and its weakened-living-target legality; `SYS-856`
  isolates the resulting refill plus typed-profile replacement.
- [Observation | Corroborated | High] `CON-631` and `SYS-857` isolate legal
  ownership-core placement and the resulting whole-Build-Location claim.
- [Observation | Corroborated | High] `OBJ-173` isolates the retained powered,
  claimed, closed and mist-protected early-shelter terminal.

## New combinations

- [Observation | Direct | High] No new combination; no verified combination is
  asserted as a strict proper subset of the forty-two-gene genome.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_071` generalises
  `SYS-327`, `CON-281`, `SYS-332` and `CON-295` to portable personal-reserve /
  environmental-exposure and ownership-core-reserve boundaries. All earlier
  signatures remain unchanged.

## New questions

- In a performed current-build run, which exact Heart, fixture, inventory,
  blood-profile and Journal fields return after the first post-shelter autosave?
- Does the first available Build Location ever force additional construction
  beyond the declared closed palisade when resource and spawn variation are
  held at normal presets?
- What smallest level-2 packet makes automatic roof creation causally necessary
  without importing a complete production-room progression?

## Next recommended game

- [Hypothesis | Limited | High] DARK SOULS™: REMASTERED.
- Optimisation criterion: replace a configurable persistent survival territory
  with an authored action-RPG route centred on stamina, checkpoints, recoverable
  currency and one early boss gate.
- Expected information gain: test the shared soulslike backbone against Lies of
  P while separating V Rising's blood, sunlight, construction and ownership.
- Backlog impact: keep Noita and MONSTER HUNTER RISE in selection-018 order.

## Why this game

- [Hypothesis | Limited | High] V Rising tests whether a player target can be
  both a combat opponent and the source of a replaceable survival profile, and
  whether a placed core can independently claim, power and protect an authored
  build territory before later castle tiers appear.

## Confidence and unresolved questions

- Confidence: High for product, mode, build window, sun, Heart power, mist and
  persistence; Medium for the player-maintained opening counts and exact Feed
  predicate.
- Unresolved: direct client confirmation of the complete current English Journal
  text, exact default timer values and the post-reload object values.
- Resolution path: run the declared current Windows build, capture text-only
  state transitions and compare one pre-exit autosave with the returned world.
- Consequence: unresolved values remain parameters; no absent local run is
  promoted to observation.

## Multilingual notes

- The canonical record stays English. Ukrainian presentation translates the
  mechanical meaning and retains official product, Journal, structure, preset,
  platform and version names where translation would reduce reproducibility.
- Technical identifiers, resource counts and source labels remain unchanged.

## Completeness checklist

- Scope, ruleset, entry, terminal, exclusions and potential modules are explicit.
- Every gene is supported by the claim ledger and a bounded transition.
- Six new owners pass lower-ID transfer review; four existing owners are
  generalised without changing earlier signatures.
- The source families, local preflight and no-audiovisual boundary are explicit.
- Ukrainian game, gene, presentation, salience and card layers are required.
- Original artwork must show the powered Heart, closed palisade, early fixtures,
  mist and sunlight contrast without copied UI, logos or character designs.
