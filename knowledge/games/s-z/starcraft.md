---
game_id: GAME-0469
slug: starcraft
game_title: StarCraft
analysis_status: reviewed
reviewed: 2026-10-01
combination_ids: []
gene_ids:
  action:
    - ACT-139
    - ACT-189
    - ACT-316
    - ACT-318
  system:
    - SYS-215
    - SYS-297
    - SYS-305
    - SYS-549
    - SYS-550
    - SYS-551
    - SYS-553
  constraint:
    - CON-273
    - CON-292
    - CON-467
    - CON-469
  information:
    - INF-224
    - INF-225
  objective:
    - OBJ-266
  time:
    - TIM-003
---

# Game: StarCraft — first Terran Wasteland mission

Use the canonical [vocabulary and comparison rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Unit costs, the ten-Marine threshold, SCV builder count and map positions are parameters, not additional genes.

## Analysis scope

- Version / ruleset: original English 1998 Windows base *StarCraft*, first Terran campaign mission **Wasteland**, after the optional Boot Camp. Not *Brood War*, *StarCraft II*, *Remastered* or the whole campaign. The exact original executable revision was not inspected.
- Structured analysis target: `PLAT-WINDOWS-PC` in [platform coverage](../../platforms/games.json).
- Entry: first player control on the mission map with the starting Marines. Finding Jim Raynor is an objective; his survival after joining remains a condition. The exact initial SCV count and original-patch unit positions are not asserted.
- Primary decision loop: reveal reachable terrain with controlled Marines, order movement and attacks to reach Raynor and the Terran base, assign SCVs to mineral extraction and Command Center return, place and complete a Barracks with an SCV, then queue Marines while preserving mineral stock and available supply. Live time and hostile combat continue between commands.
- Positive terminal: Raynor has been found and survives, the Barracks has been completed and at least ten living ordinary Marines are simultaneously under the player's control. Surviving starting Marines count toward ten; Marines lost on the route must be replaced. Do not count Raynor as an ordinary Marine without separate evidence.
- Negative / interrupted state: Raynor's death fails his survival condition; losses reduce the live Marine count and may force further production. The exact failure-screen timing, save state and possibility of resource softlock for a particular original build were not measured.
- Included: local scouting and fog, selected-unit move and attack commands, SCV mineral harvest and deposit, one-SCV construction and repair, legal building footprint, Barracks and Marine production, mineral/production/supply gates, local real-time engagements, strategic selection/HUD state and the three-part mission terminal.
- Excluded: vespene extraction, later technologies and unit classes, control of the other races, multiplayer, later missions, map editor, expansion and remaster rules. These exclusions do not assert that the complete game lacks those systems.
- Reproducibility parameters: original Windows build and speed setting, mission start save, unit positions and health, Raynor-found and survival flags, mineral-node reserves, SCV routes and return trips, Command Center and Barracks status, queue, mineral stock, supply and living controlled Marine roster at each timed order. No executable input trace was available.
- Potential scoped modules: later Terran missions, the other playable races, multiplayer economy, expansion missions and original-versus-remaster equivalence.
- Direct-play status: no disc, executable, replay, screenshot, gameplay video or audio was inspected. This is a documentary reconstruction from Blizzard's original Terran references and written Wasteland routes. The new illustration is interpretive, not a captured frame.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `SC-001` | A selected SCV is ordered to mine minerals and deliver its carried load to a Command Center for shared spending. | Observation | Corroborated | High | P1, P2, P3 |
| `SC-002` | One SCV constructs a Terran Barracks on a legal site; a completed Barracks can train Marines using minerals and supply headroom. | Observation | Corroborated | High | P1, P2, P4, S1 |
| `SC-003` | Wasteland asks the player to find Raynor, build a Barracks and achieve a ten-Marine force while keeping Raynor alive. | Observation | Corroborated | Medium | S1, S2, S3 |
| `SC-004` | The ten-Marine terminal tests living controlled ordinary Marines, so surviving starting Marines contribute and casualties need replacement. | Strong Pattern | Corroborated | Medium | S1, S2, S3 |
| `SC-005` | Visibility and real-time enemy responses constrain movement, command and production decisions during the route. | Observation | Corroborated | High | P1, P4, S1 |
| `SC-006` | Exact original-patch positions, the initial SCV count, resource rates and failure/restart details are not established by the inspected evidence. | Observation | Limited | High | P1–P4, S1–S3 |

## Basic data

- Release / origin: original 1998 Windows base *StarCraft* by Blizzard Entertainment. The analysis does not claim an installed build or patch hash.
- Puzzle families: `FAM-010` real-time system pressure, `FAM-015` agent routing and coordination, `FAM-017` ordered dependency sequencing. The objective depends on reaching the ally, mineral economy, construction and a live roster, not on eliminating every hostile.
- **[P1]** [Blizzard's original Terran basics](https://classic.battle.net/scc/terran/basic.shtml): original Terran buildings, supply, SCV, Marine and campaign basics; accessed 2026-10-01.
- **[P2]** [Blizzard's SCV reference](https://classic.battle.net/scc/Terran/uscv.shtml): SCV mining, construction and repair; accessed 2026-10-01.
- **[P3]** [Blizzard's Command Center reference](https://classic.battle.net/scc/popup/cc.htm): mineral return and SCV production at Command Center; accessed 2026-10-01.
- **[P4]** [Blizzard's original Marine reference](https://classic.battle.net/scc/terran/um.shtml): Barracks-trained infantry and resource/supply cost; accessed 2026-10-01.
- **[S1]** [StrategyWiki's original StarCraft Wasteland route](https://strategywiki.org/wiki/StarCraft/Wasteland): written mission objective and ten-living-Marines terminal; accessed through indexed page text 2026-10-01, not an executed original build.
- **[S2]** [Altered Gamer's original StarCraft first-mission guide](https://www.alteredgamer.com/starcraft/21122-walkthrough-terran-missions-1-5/): Raynor survival, construction and Marine training in the original game; accessed 2026-10-01.
- **[S3]** [Gamepressure's Remastered Wasteland guide](https://www.gamepressure.com/starcraft-remastered/mission-1-wasteland/z6a023): corroborates the first-mission objective and notes the live controlled count rather than ten new training events. The remaster guide is not evidence for original-patch constants; accessed 2026-10-01.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-189` for contextual movement or attack orders to selected Marines and Raynor, not direct avatar steering.
- Reuse `ACT-318` for selecting an SCV and assigning it to minerals, construction or repair. This is the selected-economic-worker boundary, not an Age-of-Empires-only villager role.
- Reuse `ACT-139` for placing a Terran Barracks or Supply Depot on a legal footprint; placing is separate from the SCV's timed construction work.
- Reuse `ACT-316` for queuing a Marine at a completed Barracks or an SCV at Command Center.

### System Behaviour Genes

- Reuse `SYS-297` for route finding and attack acquisition under unit orders, `SYS-305` for vision propagation and fog, and `SYS-215` for live hostile combat. None implies a turn queue.
- Reuse `SYS-549` for repeated SCV mineral extraction, carried return and shared-stock credit. `SYS-550` advances assigned SCV construction or repair, with one construction SCV in this ruleset; `SYS-551` advances Barracks or Command Center unit queues.
- Reuse `SYS-553` for completed supply providers and the live unit cap. The exact available headroom on the first mission map is a state parameter, not a new gene.

### Constraint Genes

- Reuse `CON-273` for fog-dependent targetability and `CON-292` for a clear legal building footprint.
- Reuse `CON-469` for reachable minerals and a compatible Command Center return point; `CON-467` requires an eligible completed site, minerals and supply for unit orders.

### Information Genes

- Reuse `INF-224` for stockpile, selection, unit condition, production and capacity state in the strategic interface. Reuse `INF-225` for explored terrain remaining distinct from current sight under fog.

### Objective Genes

- New `OBJ-266` isolates the Wasteland sequence and terminal: find and preserve Raynor, finish a Barracks and control ten *living* ordinary Marines. The word “train” on the mission objective is not taken to demand ten **additional** production events.

### Time Genes

- Reuse `TIM-003`: unit movement, harvesting, construction, training and combat proceed while the player decides.

## Reproducible transitions

| Before | Input or event | Source-derived resolution | Boundary | Claim |
|---|---|---|---|---|
| Starting Marines face partially unseen terrain | Select and order a reachable route toward Raynor | Units path through legal terrain; sight reveals the local route and may expose opposition | Discovery is not omniscient map access | `SC-003`, `SC-005` |
| Raynor is found | Keep him alive while moving to the Terran base | The ally objective is met, but mission completion still depends on Barracks and Marine roster | Raynor is not counted as an ordinary Marine | `SC-003` |
| An SCV can reach a mineral patch | Command mining | It gathers a carried amount and returns to the Command Center, increasing shared minerals | Mineral contact without delivery is not stockpile credit | `SC-001` |
| A legal clear build footprint and enough minerals exist | Place Barracks and assign SCV | The SCV works until Barracks construction completes | One construction SCV, not autonomous instant placement | `SC-002` |
| Barracks complete, minerals and supply headroom available | Queue a Marine | A timed production order yields one living Marine if completion remains legal | A queued but unfinished unit does not satisfy the roster | `SC-002`, `SC-004` |
| Ten Marines have been produced over time but some died | Inspect the living controlled roster | Mission remains short of the threshold until replacements exist simultaneously | Cumulative training is not the terminal | `SC-004` |
| Raynor lives, Barracks complete and ten ordinary Marines live under control | Game evaluates mission conditions | Wasteland's bounded success condition is met | No requirement to eliminate every Zerg hostile | `SC-003`, `SC-004` |

These cases reconstruct documented rules; they are not results of local gameplay execution.

## Strategic and experiential structure

- The opening is not a generic build-order skirmish. Scouting finds a named ally; preserving that ally and the starting Marines reduces the amount of replacement production needed.
- Resource workers create a spatial loop: extraction and Command Center return fund a legal Barracks and further Marines. Construction is a timed job tied to an SCV, unlike a globally finished structure that appears instantly.
- Supply and stockpile distinguish an available production button from a satisfiable order. Enemy contact can lower the live Marine count even after the total trained over time reached ten.

## Replay and variation

- The exact path to Raynor, fighting choices, SCV assignments, building footprint and loss rate may vary while preserving the same mission terminal. The inspected sources do not establish an exact original-build trace or deterministic casualty count.

## Adjacent systems and history

- *StarCraft II*'s already analysed bounded mission shares contextual orders, sight and real-time combat but lacks this original mission's SCV mineral economy and Barracks-to-ten-Marines terminal. We do not import that sequel's later-production details.
- *Age of Empires II* shares selected-worker extraction, construction and site production, but its villagers and age technologies are not imported into the Terran packet. The selected-worker gene labels generalise without changing earlier genomes.

## Normalised genome

| Type | Active gene IDs | Boundary |
|---|---|---|
| Action | `ACT-139`, `ACT-189`, `ACT-316`, `ACT-318` | footprint, commands, unit queue and SCV task |
| System Behaviour | `SYS-215`, `SYS-297`, `SYS-305`, `SYS-549`, `SYS-550`, `SYS-551`, `SYS-553` | combat, path, fog, mining, work, queue and supply |
| Constraint | `CON-273`, `CON-292`, `CON-467`, `CON-469` | visibility, footprint, order and return gates |
| Information | `INF-224`, `INF-225` | strategic state and explored terrain |
| Objective | `OBJ-266` | found ally, completed Barracks and living roster |
| Time | `TIM-003` | continuous RTS time |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `468` (`GAME-0001`–`GAME-0468`).
- Exact genome matches: none.
- Tied near matches: `GAME-0179` — Age of Empires II: Definitive Edition (`17 / 31 = 0.548387`).
- Supported combination subsets: none.
- Scan date: 2026-10-01.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0179` — Age of Empires II: Definitive Edition | `ACT-139`, `ACT-189`, `ACT-316`, `ACT-318`, `CON-273`, `CON-467`, `CON-469`, `INF-224`, `INF-225`, `SYS-215`, `SYS-297`, `SYS-305`, `SYS-549`, `SYS-550`, `SYS-551`, `SYS-553`, `TIM-003` | Both combine selected-unit command, worker-carried resource return, worker construction, site-bound unit production, supply/production legality, strategic state and live fog. Wasteland is a fixed original Terran opener requiring Raynor, a Barracks and ten living ordinary Marines; Age of Empires II uses its scoped generated civilisation match, broader resource/Age progression and Conquest terminal. Shared economy and command do not make their mission conditions equivalent. | Near, `17 / 31 = 0.548387` |

### Preserved research notes

- New genes: `OBJ-266`.
- Generalised gene labels without changing prior signatures: `ACT-318`, `SYS-550`, `CON-469`.
- Reused genes: 18 earlier Active definitions.
- Classification result: one new mission objective and worker-role boundary clarification.
- Evidence and reasoning: ordinary RTS commands, extraction, building and production transfer unchanged; the first-mission live-roster objective does not.

## Taxonomy impact

- One new Active Objective definition and three boundary-preserving selected-worker generalisations; no prior game signature or verified combination changes.
- Taxonomy-change record: [`TAXONOMY_CHANGE_206`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_206.md).

## Negative results

- No original Windows executable or direct play. Exact first-map positions, start SCV count, resource throughput, failure timing and restart state remain unresolved.
- A later Remastered written guide corroborates the live-Marine count but cannot establish original patch-specific unit statistics or placement.
- The original artwork depicts a plausible early Terran base while Marines and SCVs coexist. It is an interpretation, not source evidence or an official game asset.

## Delta summary

## New facts

- [Observation | Corroborated | Medium] The first Terran mission closes on a found, living ally, a completed Barracks and ten controlled living Marines (`SC-003`, `SC-004`).

## New genes

- [Observation | Corroborated | Medium] `OBJ-266` isolates that terminal; prior selected-worker definitions are made role-neutral without changing their causal boundaries.

## New combinations

- [Observation | Direct | High] None claimed until the verified-subset scan is computed.

## Taxonomy changes

- [Observation | Corroborated | Medium] One new objective and three worker-label generalisations; no earlier signatures changed.

## Open questions

- Direct execution of an original Windows build could establish initial unit counts, map placements, exact death/restart state and supply edge cases.

## Next research candidate

- `GAME-0470` *Burnout 3: Takedown*, original PlayStation 2, after full acceptance and the Goal stop window.
