---
game_id: GAME-0305
slug: sons-of-the-forest
game_title: Sons Of The Forest
analysis_status: reviewed
reviewed: 2026-09-18
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-036
    - ACT-093
    - ACT-148
    - ACT-245
    - ACT-341
  system:
    - SYS-312
    - SYS-313
    - SYS-327
    - SYS-407
    - SYS-887
  constraint:
    - CON-210
    - CON-292
    - CON-621
  information:
    - INF-073
    - INF-075
    - INF-128
    - INF-131
    - INF-132
  objective:
    - OBJ-171
  time:
    - TIM-003
    - TIM-007
---

# Game: Sons Of The Forest

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Product labels,
resource quantities, crash location and companion identity are parameters,
not gene names.

## Analysis scope

- Version / ruleset: unmodified English Windows Steam base application
  `1326470`, public branch Build ID `20228174` reported by the SteamCMD
  projection and checked 2026-09-18. This is a remotely projected build, not
  an observed local installation or publisher semantic version. The
  post-early-access 1.0 release was 2024-02-22.
- Structured analysis target: Windows base game, fresh offline single-player
  `Normal`, keyboard and mouse; see `GAME-0305` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Entry: the first ordinary control after a new-game helicopter crash, with
  Kelvin injured nearby, before the player has built a shelter. Choose a
  reachable local site with trees, loose sticks and rocks; crash placement and
  source coordinates are not fixed by this analysis.
- Primary decision loop: help Kelvin at the crash and use his notepad to assign
  `Get > Logs > Drop Here` near the planned site; while he independently
  brings logs, collect reachable sticks and rocks, open the Guide Book's
  Hunting Shelter plan, place its visible outline on clear ground, and commit
  the required compatible materials to its remaining counts. When the five
  logs, six sticks and seven rocks have been accepted, use the completed
  Hunting Shelter's separate save interaction and accept a save slot.
- Positive terminal: one intact Hunting Shelter has been completed and its
  manual save command has accepted the current world as a continuation state.
  The selected source hypothesis asked for a reload-verified exact inventory,
  Kelvin, GPS, world and elapsed-time snapshot. No installed application or
  save was available, so that stronger terminal is **not observed** and is
  not claimed. A later direct-play reload test remains a separate verification
  module, not an invented result of this source-backed packet.
- Included: local first-person traversal; Kelvin's post-crash recovery and
  notepad role assignment; autonomous log gathering and world-point delivery;
  loose stick and rock pickup; finite carried stacks; visible survival state;
  Guide Book plan, footprint feedback and typed requirements; incremental
  material contribution and completed fixture; separate manual save; live
  world time and retained save-history capability. The GPS may display the
  survivor and Kelvin, but this short local route does not require a GPS
  waypoint or prove a specific Hunting Shelter marker.
- Excluded: multiplayer, Peaceful, Hard, Custom and Creative differences;
  free-form log construction, structural cutting, Kelvin's `Finish Structure`
  and other orders; tree felling by the player, advanced bases, caves, story
  progression, later companions, combat, sleeping, consoles, mods and endings.
  Those are not silently encoded in this prefab-shelter packet.
- Reproducible parameterisation: verify the public branch and choose fresh
  single-player Normal. At the crash, help Kelvin, select `Get > Logs > Drop
  Here` at a legal nearby clearing with reachable trees, and wait for enough
  delivered logs; collect six sticks and seven rocks, using multiple trips if
  carried capacity requires them. Select Hunting Shelter in the Guide Book,
  move the outline off obstructed terrain, commit it, and supply five logs,
  six sticks and seven rocks according to the visible counters. At the intact
  shelter, choose save rather than sleep and accept a slot. The selected
  terrain, exact Kelvin path, local resources, inventory overage, weather,
  survival meters and elapsed time remain instance parameters. If Kelvin is
  blocked or a resource is absent, relocate or restart the packet; this record
  does not misreport a guaranteed fixed crash seed.
- Potential scoped modules: performed save/quit/reload comparison of inventory,
  Kelvin, GPS, structures, source changes and time; free-form structural
  cutting; Kelvin's `Finish Structure`; shelter sleep; combat; multiplayer
  persistence; and later story each need their own causal scope and evidence.
- Direct-play status: not conducted. No Windows game installation, app
  manifest, entitlement, save or local play trace was available. Valve and
  Endnight establish product, release, survival construction, companion and
  save interfaces; independent written references corroborate the exact
  Hunting Shelter packet and Kelvin command. This is a source-bounded
  reconstruction, not a claimed played or reload-verified route. No video or
  audio was opened, played or analysed.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SOTF-001` | Steam app `1326470` is Endnight's released Windows base product, published by Newnight, with single-player support | Confirmed | Direct | High | P1 |
| `SOTF-002` | The remotely projected public branch reports Build ID `20228174`; the installed local build was not observed | Observation | Corroborated | Medium | S1, R1 |
| `SOTF-003` | A fresh run follows a helicopter crash, with Kelvin present as an injured companion who receives notepad orders | Observation | Corroborated | Medium | P2, S2, S3 |
| `SOTF-004` | `Get > Logs > Drop Here` directs Kelvin to gather logs and deposit them at a chosen world location without continuous steering | Observation | Corroborated | Medium | P3, S2, S3 |
| `SOTF-005` | The Guide Book's Hunting Shelter outline takes five logs, six sticks and seven rocks supplied as discrete requirements | Observation | Corroborated | High | S4, S5 |
| `SOTF-006` | Rocks and sticks can be taken from reachable local sources, while completed material counts convert the outline into a usable fixture | Observation | Corroborated | Medium | S4, S5 |
| `SOTF-007` | The completed Hunting Shelter offers separate save and sleep interactions; saving does not require sleeping | Observation | Corroborated | Medium | P3, S4, S6 |
| `SOTF-008` | Survival and world time remain live while the player collects and builds; a save slot is intended to retain that state | Observation | Corroborated | Medium | P1, P2, S6 |
| `SOTF-009` | The 1.0 release changed building and GPS interfaces and recommends a fresh save; old early-access controls are not assumed unchanged | Confirmed | Direct | High | P2 |
| `SOTF-010` | No local game or save/reload trace was available, so exact post-load inventory, Kelvin, GPS and world retention are unverified | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: Endnight Games Ltd / Newnight; 1.0 released 2024-02-22.
  Public Build ID `20228174` was remotely projected on 2026-09-18.
- Platform or physical form: Windows Steam base application `1326470`, fresh
  offline single-player `Normal`.
- Puzzle family: inventory and fixture dependencies; real-time system
  pressure; ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-18:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=1326470&cc=ua&l=english),
    for the app, developer, publisher, release, Windows support and
    single-player classification.
  - **[P2]** [Endnight's official 1.0 release announcement](https://steamcommunity.com/games/1326470/announcements/detail/4192358592270167293),
    for fresh-save guidance, construction changes, GPS changes and companion
    behaviour in the released ruleset.
  - **[P3]** [Endnight's official update notes](https://store.steampowered.com/news/posts/?enddate=1682022314&feed=steam_community_announcements),
    for Kelvin's log carrying and save-related patch history; historical
    patch facts are cross-checked against current secondary references.
- Corroborating textual sources, accessed 2026-09-18:
  - **[S1]** [SteamCMD branch projection](https://api.steamcmd.net/v1/info/1326470),
    secondary Build ID data, not an observed installed version.
  - **[S2]** [Kelvin reference](https://sonsoftheforest.wiki.gg/wiki/Kelvin),
    for crash injury, notepad command menu, log gathering and delivery.
  - **[S3]** [independent Kelvin written route](https://www.pcgamer.com/sons-of-the-forest-tips-how-to-survive-your-first-hours-on-the-terrifying-island/),
    for the notepad and `Get logs > Drop here` instruction.
  - **[S4]** [Hunting Shelter written route](https://www.gamerguides.com/sons-of-the-forest/guide/crafting/shelter/how-to-make-the-hunting-shelter-in-sons-of-the-forest),
    for plan placement, resource collection, discrete filling, completion and
    separate save/sleep prompts; its early-access key bindings are not adopted.
  - **[S5]** [Hunting Shelter reference](https://sonsoftheforest.wiki.gg/wiki/Prefab_Buildings/Hunting_Shelter),
    for the five-log, six-stick, seven-rock bill and usable fixture.
  - **[S6]** [save and sleep reference](https://sonsoftheforest.wiki.gg/wiki/Sleeping),
    for shelter interaction and its separation from the save action.
- Research record: **[R1]** local 2026-09-18 preflight found no matching
  Windows installation or save; no direct play or reload was performed.
- Claim IDs: `SOTF-001`–`SOTF-010`.

## Mechanical decomposition

### Action Genes

- `ACT-008` owns local traversal; `ACT-036` the one notepad task assignment
  to Kelvin; `ACT-245` loose stick and rock collection; `ACT-148` selecting
  and placing the Hunting Shelter plan; `ACT-093` each compatible contribution
  to its counters; and `ACT-341` the finished fixture's manual save command.
  Helping Kelvin is an ordinary contextual interaction, not a new revival
  combat gene. Claims: `SOTF-003`–`SOTF-008`.

### System Behaviour Genes

- `SYS-313` owns the persistent open survival world, `SYS-327` live personal
  condition, `SYS-407` Kelvin's persistent companion follow/support presence,
  `SYS-887` his assigned source-to-world-point log delivery, and `SYS-312`
  the remaining-plan-count settlement into a complete shelter.
- Resolution order: aid Kelvin; issue one legal notepad order; he selects
  reachable logs and drops them near the chosen point; the player collects
  sticks and rocks and places a legal outline; each compatible contribution
  consumes available material and decrements a visible requirement; completing
  all three typed requirements creates the finished shelter; save accepts a
  slot without executing sleep. Claims: `SOTF-003`–`SOTF-008`.

### Constraint Genes

- `CON-210` owns finite typed carrying; `CON-292` a legal clear shelter
  footprint; `CON-621` the completed shelter as the designated save fixture.
  The exact material bill, Kelvin's reachable sources and any delivery
  interruption are parameters of these and `SYS-887`, not unsupported new
  constraint IDs. Claims: `SOTF-004`–`SOTF-008`.

### Information Genes

- `INF-073` owns visible carried stacks, `INF-075` survivor condition,
  `INF-128` reachable material and inventory fit, `INF-131` the outline,
  remaining counts and finished fixture prompts, and `INF-132` the known
  Guide Book material dependencies. GPS direction and marker detail are not
  required to navigate this local packet. Claims: `SOTF-005`–`SOTF-009`.

### Objective Genes

- `OBJ-171` owns the bounded material-to-completed-shelter-to-accepted-save
  chain. An outline or unconfirmed reload is not a terminal. Claims:
  `SOTF-005`–`SOTF-010`.

### Time Genes

- `TIM-003` owns live time during resource delivery, gathering and building;
  `TIM-007` owns the documented branchable save-history capability. No exact
  retained values after reload are asserted. Claims: `SOTF-007`–`SOTF-010`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Kelvin is injured by the fresh crash | Help and open his notepad | He becomes available for a selected written task | companion recovery precedes assignment | `SOTF-003` |
| Kelvin is available near reachable trees | Choose `Get > Logs > Drop Here` | He autonomously gathers eligible logs and deposits them at the selected place, subject to pathing and interruption | assignment differs from directly controlled harvesting and from a shared stockpile | `SOTF-004` |
| Loose stick or rock is reachable with capacity | Pick it up | The matching carried stack increases | typed local collection remains player-controlled | `SOTF-006` |
| Hunting Shelter is selected in the Guide Book | Move the outline to clear ground and commit | A material-backed plan with three visible remaining counts exists | placement is not instantaneous completion | `SOTF-005` |
| Compatible carried or delivered material is available | Add it to the unfinished plan | One requirement falls and the material is consumed | multiple independent trips can fill the same plan | `SOTF-005`, `SOTF-006` |
| Five logs, six sticks and seven rocks have been accepted | Supply the last missing item | The unfinished outline becomes an intact usable Hunting Shelter | completion precedes saving | `SOTF-005`, `SOTF-006` |
| Completed shelter and free/selected save slot | Choose save, not sleep | The save command accepts the current state as a continuation | source-supported terminal, not an observed reload | `SOTF-007`, `SOTF-010` |
| Save exists, but no local game/save is available | Do not assert post-load equality | Inventory, Kelvin, GPS and world snapshot comparison remains unperformed | prevents a false reload-verification claim | `SOTF-010` |

## Strategic and experiential structure

- Local decision: position the delivery point near a legal footprint and
  collect sticks and rocks without losing track of Kelvin's delivered logs.
- Medium-term planning: parallelise companion log gathering with the player's
  smaller-material collection, then fill the plan across any capacity-limited
  trips before relying on it as a save fixture.
- Long-term structure: one constructed world object closes the scoped chain;
  optional base architecture and island story do not enter it.
- Common heuristics: choose clear ground close to resources; observe the
  remaining material counts; if Kelvin cannot reach logs, adjust the order or
  site rather than assuming completion; distinguish save from sleep.
- Failure attribution: blocked footprint, missing or full carried stack,
  inaccessible log source, interrupted companion, incomplete plan and wrong
  fixture state are distinct reasons a command may not advance the packet.
- Player-trust factors: visible notepad order, on-ground deliveries, Guide
  Book material bill, outline counters and the completed shelter prompt
  expose the transition without a hidden automatic objective.
- Claim IDs: `SOTF-003`–`SOTF-010`.

## Replay and variation

- What changes between sessions: crash site, local resource layout, weather,
  Kelvin's path and interruption, carried overage, survival meters, shelter
  position and chosen save slot.
- Randomness or procedural generation: the island is persistent while fresh
  crash placement and encountered local state vary; the packet does not
  invent a fixed seed or exact time.
- Multiple viable strategies: the player can gather smaller materials while
  Kelvin brings logs, in either order, and choose any legal nearby footprint.
- Typical replay motive: wider construction, exploration, combat and story;
  each exceeds the selected shelter-save packet.
- Claim IDs: `SOTF-003`–`SOTF-010`.

## Adjacent systems and history

- Direct predecessor: The Forest uses a material-backed Temporary Shelter
  and fixture-bound save, but its scoped route requires the player to harvest
  every material and its optional sleep destroys the one-use shelter.
- Variants: different difficulty, multiplayer ownership, alternate crash
  sites, free-form building and later Kelvin orders may change eligibility
  and persistence; none is silently merged into this packet.
- Similar games: Valheim shares a placed material-backed shelter and live
  world pressure; Monster Hunter Wilds has a persistent autonomous companion
  but not Kelvin's source-to-player-chosen-world-point delivery.
- Important differences: the notepad splits an explicit player task choice
  from Kelvin's autonomous log acquisition, while the player still chooses
  where to build and contributes materials to the prefab plan.
- Claim IDs: `SOTF-003`–`SOTF-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-036`, `ACT-093`, `ACT-148`, `ACT-245`, `ACT-341` | traversal, order, pickup, outline, contribution, save |
| System Behaviour | `SYS-312`, `SYS-313`, `SYS-327`, `SYS-407`, `SYS-887` | world, survival, companion delivery, completion |
| Constraint | `CON-210`, `CON-292`, `CON-621` | capacity, footprint, save fixture |
| Information | `INF-073`, `INF-075`, `INF-128`, `INF-131`, `INF-132` | stacks, meters, sources, plan and costs |
| Objective | `OBJ-171` | intact shelter and accepted save |
| Time | `TIM-003`, `TIM-007` | live world and branchable save |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `304` (`GAME-0001`–`GAME-0304`).
- Exact genome matches: none.
- Tied near matches: `GAME-0292` — The Forest (`19 / 29 = 0.655172`).
- Supported combination subsets: none.
- Scan date: 2026-09-18.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0292` — The Forest | `ACT-008`, `ACT-093`, `ACT-148`, `ACT-245`, `ACT-341`, `SYS-312`, `SYS-313`, `SYS-327`, `CON-210`, `CON-292`, `CON-621`, `INF-073`, `INF-075`, `INF-128`, `INF-131`, `INF-132`, `OBJ-171`, `TIM-003`, `TIM-007` | Both packets gather local material, place and fill a shelter outline, then save at the finished fixture in a live survival world. The Forest's scoped Temporary Shelter requires direct vegetation harvesting and has a one-use sleep branch; the sequel delegates log gathering to Kelvin's chosen world drop point while the player obtains sticks and rocks, and this packet excludes sleep. Neither study observed a reload. | Tied near, `19 / 29 = 0.655172` |

### Preserved research notes

- New genes: `SYS-887`.
- Classification result: `New gene`.
- Evidence and reasoning: `ACT-036` reuses the general assignment boundary.
  `SYS-046` covers execution of an assigned role but not a persistent
  companion's repeated gathering into a player-selected *world* drop point;
  `SYS-549` routes a worker into a compatible building and shared stockpile,
  not loose material where the player intends to build. The new settlement
  boundary is therefore a specifically evidenced delivery process, not a
  renaming of Kelvin or of ordinary resource pickup.

## Taxonomy impact

- Registry changes: one new Active System Behaviour `SYS-887`; no earlier
  signature or gene definition changes.
- Taxonomy-change record: none; no existing boundary is rewritten.
- Candidate terms affected: Kelvin, notepad, `Get > Logs > Drop Here`,
  Guide Book, Hunting Shelter, GPS and app/build identifiers remain instance
  parameters, not gene names.

## Negative results

- The selected reload-verified terminal is not established without a local
  game/save trace. This is a direct-play evidence limit, not a claim that save
  does not retain state.
- `SYS-549` is rejected for Kelvin's delivery because no compatible shared
  stockpile building is required. Free-form building and structural cutting
  are rejected as outside the prefab Hunting Shelter route, not treated as
  unsupported new genes. `ACT-214` and sleep-specific resolution are absent
  because the positive route chooses save without sleeping.

## Delta summary

## New facts

- [Observation | Corroborated | Medium] One written Kelvin log-delivery order
  lets the companion bring material to a chosen world point while the player
  collects other shelter resources (`SOTF-003`, `SOTF-004`).
- [Observation | Corroborated | High] The scoped Hunting Shelter requires
  five logs, six sticks and seven rocks, then offers a separate save action
  (`SOTF-005`–`SOTF-007`).
- [Confirmed | Direct | High] No exact reload comparison was performed
  (`SOTF-010`).

## New genes

- [Observation | Corroborated | Medium] `SYS-887` distinguishes autonomous
  companion gathering into a player-chosen world drop point from direct
  collection and worker-to-stockpile economy.

## New combinations

- [Observation | Corroborated | Medium] No new verified combination; the
  subset scan is recorded above.

## Taxonomy changes

- [Confirmed | Direct | High] No earlier gene boundary or signature changed.

## New questions

- Does the current installed public build retain every exact inventory,
  Kelvin, GPS and world value after save/quit/reload? This requires an
  authorised Windows run and side-by-side capture.
- How does Kelvin's delivery behave when the source or selected drop point
  becomes unreachable? The current packet records interruption as a boundary,
  not an observed trace.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0306` METAL GEAR SOLID V: THE PHANTOM
  PAIN, Xbox One base game.
- Optimisation criterion: contrast companion-assisted survival construction
  against authored stealth infiltration, detection and extraction.
- Expected information gain: test whether a scoped mission's tactical
  observation, alert and Fulton progression add independent boundaries.
- Backlog impact: final subject of the selected nine-game horizon; no later
  unit starts without the next Goal turn or explicit continuation.

## Why this game

- [Hypothesis | Limited | Medium] The preceding The Forest shelter route
  makes Kelvin's delegated delivery and a reusable shelter an informative
  same-series contrast, while avoiding a false claim about reload or
  free-form construction in an unplayed build.
