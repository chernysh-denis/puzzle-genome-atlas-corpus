---
game_id: GAME-0170
slug: stalker-2-heart-of-chornobyl
game_title: "S.T.A.L.K.E.R. 2: Heart of Chornobyl"
analysis_status: reviewed
reviewed: 2026-08-27
combination_ids:
  - COMB-0168
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-199
    - ACT-200
    - ACT-221
    - ACT-232
    - ACT-288
    - ACT-289
  system:
    - SYS-215
    - SYS-223
    - SYS-251
    - SYS-369
    - SYS-373
    - SYS-379
    - SYS-511
    - SYS-512
    - SYS-513
    - SYS-514
  constraint:
    - CON-210
    - CON-284
    - CON-285
    - CON-286
    - CON-321
    - CON-336
    - CON-433
    - CON-434
    - CON-435
    - CON-436
  information:
    - INF-073
    - INF-075
    - INF-115
    - INF-125
    - INF-128
    - INF-148
    - INF-202
    - INF-203
  objective:
    - OBJ-097
  time:
    - TIM-003
---

# Game: S.T.A.L.K.E.R. 2: Heart of Chornobyl

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: official PC base game at Patch `2.0.2`, one fresh unmodded
  single-player New Game on `Stalker` difficulty, with the free Update 2.0
  rules inherited by that patch.
- Primary decision loop: navigate by PDA, compass and local evidence; inspect
  sound, anomaly cues, status, ammunition, equipment condition and carried
  weight; probe a hazard with a bolt or route around it; fight, heal, loot or
  withdraw; use the Echo Detector to manifest an artifact; prepare at Zalissya;
  then commit dialogue and item-hand-in choices that update the investigation.
- Entry and exit: begins when the fresh campaign confirms `Stalker` difficulty;
  succeeds when Skif has completed `There and Back Again`, reached Zalissya,
  obtained the Ward Sensors from Squint by exchanging the Mold artifact during
  `Piece of Cake`, and handed the sensors to Richter to close `A Needle in a
  Haystack` on the declared branch.
- Included: first-person movement, stance, aiming, firearm and melee combat;
  weapon selection, magazines, ammunition and reloads; local hostile sight and
  sound; health, stamina, bleeding, radiation, hunger and overload; medical and
  anti-radiation quick use; reachable loot, inventory slots and weight; weapon
  condition and one eligible Zalissya technician repair; PDA map, compass,
  markers, mission log and dialogue; bolts, anomalies, Echo Detector searches,
  artifact manifestation and optional armour-slot effects; the prologue,
  Zalissya, Richter's investigation route, `Piece of Cake`, the Mold exchange
  and the final Richter hand-in.
- Reproducible parameterisation: use default controls and the equipment supplied
  by the fresh route. In the prologue, retrieve the required artifact with the
  Echo Detector. After reaching Zalissya, follow Gaffer and Richter's route to
  Squint rather than Captain Zotov's Ward warehouse route. Calm Squint, accept
  `Piece of Cake`, traverse the acid field with bolts and the Echo Detector,
  return the Mold artifact for the Ward Sensors, then give the sensors to
  Richter. Record one inventory-overload threshold, one condition change and
  repair if current coupons permit it; exact loot and ambient encounters remain
  sampled parameters.
- Excluded: `Cost of Hope` and all paid expansion content; `Stories Untold`,
  `Sealed Truth` and other optional post-launch quest packets; pre-order or
  edition bonuses; mods, console commands, alternate difficulty modes and
  multiplayer; Captain Zotov as the terminal sensor recipient; killing Squint
  or retaining Mold; later regions and main missions; exhaustive A-Life,
  faction war, reputation, emissions, upgrades, trading, world stashes, coded
  safes and their clue trails, artifacts, weapons, armour, mutants, endings and
  the full Zone.
- Potential scoped modules: Zotov's mutually exclusive early branch; one
  emission-and-shelter packet; one later faction-territory response; a complete
  equipment upgrade/economy loop; one reproducible coded-safe route with its
  locally acquired numeric clues and stash transfer; or one expansion route
  after separate review.
- Direct-play status: no fresh paid-account run was conducted. GSC Game World's
  current patch archive and official support articles directly establish the
  maintained survival, anomaly, artifact, HUD, inventory, hub and interaction
  systems. Two maintained route references independently corroborate Squint,
  `Piece of Cake`, Mold, Ward Sensors and the mutually exclusive hand-in.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `ST2-001` | Patch 2.0.2 is the current reviewed PC ruleset, and free Update 2.0 is distinct from the excluded Cost of Hope expansion | Confirmed | Direct | High | P1, P2, P3 |
| `ST2-002` | The opening reaches Zalissya as the first hub, where trade, treatment, repair, stash and authored jobs prepare the next route | Confirmed | Direct | High | P4, P10 |
| `ST2-003` | Nearby anomalies advertise danger and bolts can trigger some of them into a short discharged interval | Confirmed | Direct | High | P5 |
| `ST2-004` | Artifacts remain invisible until a compatible detector brings Skif into critical range, then can be collected and equipped for effects plus radiation | Confirmed | Direct | High | P6 |
| `ST2-005` | Health, stamina, bleeding, hunger, radiation and overload modify live survival and movement while quick slots expose immediate treatment access | Confirmed | Direct | High | P7, P8 |
| `ST2-006` | Inventory weight and equipment compatibility bound carried loot, while weapon condition can justify a technician repair | Confirmed | Direct | High | P4, P7, P9 |
| `ST2-007` | Firearm combat consumes compatible ammunition and unfolds through local cover, enemy perception, health and recovery | Confirmed | Direct | High | P4, P8 |
| `ST2-008` | Dialogue, jobs and reputation-sensitive services can retain choices that alter relationships, access and later world response | Confirmed | Direct | High | P9, P11 |
| `ST2-009` | The PDA and HUD expose explored map, markers, current mission state, notifications, weapon state and survival effects without revealing the whole Zone | Confirmed | Direct | High | P8, P12 |
| `ST2-010` | Calming Squint and completing Piece of Cake yields the Ward Sensors in exchange for Mold; giving them to Richter closes the selected early investigation branch | Observation | Corroborated | High | S1, S2 |
| `ST2-011` | Death returns play through save restoration rather than permanently ending the campaign identity | Confirmed | Direct | High | P4 |

## Basic data

- Release / origin: GSC Game World; released 2024; reviewed on 2026-08-27 at
  PC Patch `2.0.2`, following free Update 2.0.
- Platform or physical form: authored single-player first-person open-world
  survival shooter; unmodded PC base game.
- Puzzle family: real-time system pressure; inventory and fixture dependencies;
  knowledge and evidence progression; tactical forecast and counterplay.
- Primary sources:
  - `P1` — [official Patch 2.0.2 notes](https://store.steampowered.com/news/app/1643320/view/677381523352061228),
    current PC patch, checked 2026-08-27.
  - `P2` — [official patch archive](https://www.stalker2.com/patch-notes?id=stories-untold),
    2.0.2, 2.0.1 and Update 2.0 ordering, checked 2026-08-27.
  - `P3` — [official Update 2.0 and Cost of Hope boundary](https://www.stalker2.com/news/cost-of-hope-update-2-0-everything-to-know),
    free update, paid expansion and save/mod notes, checked 2026-08-27.
  - `P4` — [official beginner guide](https://support.stalker2.com/hc/en-us/articles/27929320406929-Beginner-s-Guide-FAQs),
    Zalissya, preparation, open world, combat and save restoration, checked
    2026-08-27.
  - `P5` — [official anomaly guide](https://support.stalker2.com/hc/en-us/articles/27929296711185-Anomalies),
    danger cues, bolt triggering and artifact fields, checked 2026-08-27.
  - `P6` — [official artifact and detector guide](https://support.stalker2.com/hc/en-us/articles/29871997411473-Artifacts-and-finding-them-with-detectors),
    detector signals, manifestation, effects, radiation and armour slots,
    checked 2026-08-27.
  - `P7` — [official inventory guide](https://support.stalker2.com/hc/uk/articles/29871864417041-%D0%86%D0%BD%D0%B2%D0%B5%D0%BD%D1%82%D0%B0%D1%80-%D1%82%D0%B0-%D1%81%D1%85%D0%BE%D0%B2%D0%BE%D0%BA-%D0%B3%D1%80%D0%B0%D0%B2%D1%86%D1%8F),
    item weight, overload, equipment, disposal and shared stash, checked
    2026-08-27.
  - `P8` — [official HUD guide](https://support.stalker2.com/hc/en-us/articles/27929379798033-HUD),
    health, stamina, effects, radiation, quick slots, ammunition, markers and
    notifications, checked 2026-08-27.
  - `P9` — [official NPC interaction guide](https://support.stalker2.com/hc/en-us/articles/27929396562065-NPC-Interactions),
    dialogue, trade, missions, technicians, relationships and reputation gates,
    checked 2026-08-27.
  - `P10` — [official hub guide](https://support.stalker2.com/hc/en-us/articles/27929313982609-Hubs),
    treatment, trade, repair, jobs, stash and shelter services, checked
    2026-08-27.
  - `P11` — [official faction and reputation guide](https://support.stalker2.com/hc/en-us/articles/27929297919889-Factions-and-reputation),
    decisions, balance, access, traders and safe movement, checked 2026-08-27.
  - `P12` — [official PDA guide](https://support.stalker2.com/hc/en-us/articles/27929373572113-PDA),
    map, mission log, markers and notes, checked 2026-08-27.
- Secondary sources:
  - `S1` — [Neoseeker A Needle in a Haystack walkthrough](https://www.neoseeker.com/stalker-2-heart-of-chornobyl/walkthrough/A_Needle_in_a_Haystack),
    Squint, `Piece of Cake`, Mold, detector route and sensor branch, checked
    2026-08-27.
  - `S2` — [Gamer Guides Piece of Cake walkthrough](https://www.gamerguides.com/stalker-2-heart-of-chornobyl/guide/side-missions/lesser-zone/piece-of-cake-mission-walkthrough),
    independent Mold-for-Ward-Sensors route corroboration, checked 2026-08-27.
- Claim IDs: `ST2-001`–`ST2-011`.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate Skif through the locally visible Zone.
- `ACT-161` — aim and attack a reachable hostile; melee and firearm are parameters.
- `ACT-164` — switch the active carried weapon or quick-use selection.
- `ACT-183` — reload the active magazine from compatible reserve ammunition.
- `ACT-199` — transfer and equip compatible reachable loot.
- `ACT-200` — use an interruptible medical or anti-radiation consumable.
- `ACT-221` — pay an eligible hub technician to repair retained weapon condition.
- `ACT-232` — commit one authored dialogue or quest response.
- `ACT-288` — throw a bolt to test an anomaly and its discharge window.
- `ACT-289` — sweep with the Echo Detector and collect the manifested artifact.
- Claim IDs: `ST2-003`–`ST2-010`.

### System Behaviour Genes

- `SYS-215` — resolve directly commanded hostile combat in real time.
- `SYS-223` — reduce weapon condition through eligible use.
- `SYS-251` — advance the authored opening and Lesser Zone quest sequence.
- `SYS-369` — restore an authored mission save after lethal state.
- `SYS-373` — escalate local suspicion and perception into combat.
- `SYS-379` — advance authored quest state from retained choices.
- `SYS-511` — cycle an anomaly through trigger, discharge and recovery.
- `SYS-512` — manifest an artifact when detector proximity becomes critical.
- `SYS-513` — integrate survival statuses and load into live capacity.
- `SYS-514` — compose equipped artifact benefits and radiation.
- Resolution order: current body, inventory, equipment and quest state expose
  legal actions; local movement, anomalies and actors advance in live time;
  combat and hazards update statuses and condition; detector range manifests an
  artifact; hub actions change retained equipment; dialogue and hand-ins update
  the investigation; lethal state may restore a prior save.
- Claim IDs: `ST2-002`–`ST2-011`.

### Constraint Genes

- `CON-210` — typed stacks and carried slots bound inventory transfer.
- `CON-284` — inventory and equipment slots plus weight bound the live loadout.
- `CON-285` — weapon operation requires compatible live weapon and ammunition.
- `CON-286` — restorative use requires a legal uninterrupted carried state.
- `CON-321` — weapon repair requires the retained item and declared coupons.
- `CON-336` — retained quest state gates later branch availability.
- `CON-433` — anomaly traversal requires a safe phase or accepted exposure.
- `CON-434` — artifact pickup requires detector range and physical reach.
- `CON-435` — survival thresholds restrict movement and continued action.
- `CON-436` — artifact effects require armour slots and radiation tolerance.
- Scarce strategic resources: safe distance and local cover; health, stamina and
  time before bleed or radiation damage; ammunition, weapon condition, healing
  items and coupons; carry-weight headroom; artifact slots; and the one retained
  sensor-recipient branch.
- Claim IDs: `ST2-003`–`ST2-011`.

### Information Genes

- `INF-073` — active firearm, magazine, reserve and carried weapon slots are visible.
- `INF-075` — health, hunger and equipment durability are inspectable.
- `INF-115` — local sight and sound only partially expose nearby hostile state.
- `INF-125` — explored map, markers and authored mission gates are visible.
- `INF-128` — reachable loot, compatibility and remaining carrying state are visible.
- `INF-148` — dialogue exposes available responses without every consequence.
- `INF-202` — HUD exposes survival pressure, radiation and quick-use state.
- `INF-203` — detector cadence exposes changing artifact proximity.
- Claim IDs: `ST2-003`–`ST2-010`.

### Objective Genes

- `OBJ-097` — resolve the first Ward Sensors investigation for Richter.
- Success, evaluation and failure: handing the sensors to Richter after the Mold
  exchange closes the declared route; death restores a save and remains
  non-terminal to the campaign; killing Squint, keeping Mold or handing the
  sensors to Zotov leaves the selected parameterisation and is not an alternate
  success for this unit.
- Claim ID: `ST2-010`, `ST2-011`.

### Time Genes

- `TIM-003` — movement, actors, attacks, statuses, anomaly recovery and detector
  search advance continuously outside explicit menu, dialogue and load boundaries.
- Claim IDs: `ST2-003`–`ST2-011`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh `Stalker` campaign reaches the prologue anomalous field | Equip the Echo Detector and move by its signal | Signal cadence increases; critical proximity manifests the required artifact for pickup | Hidden artifact localisation is an action-system chain | `ST2-004` |
| Active anomaly blocks a locally visible route after the prologue | Throw a bolt across the intended line and cross during discharge | The bolt triggers the typed effect; a bounded recovery interval follows | Environmental timing is probed rather than fully disclosed | `ST2-003` |
| Hostile actor detects Skif at firearm range | Aim, fire, reload or move behind cover | Live perception, ammunition, hit state, bleeding, stamina and weapon condition update | Combat shares resources with traversal and survival | `ST2-005`–`ST2-007` |
| Inventory approaches overload after reachable loot is revealed | Transfer, equip, drop or retain one item | Slots, compatibility and weight update; crossing a load threshold restricts movement | Loot value competes with immediate mobility | `ST2-005`, `ST2-006` |
| Worn weapon and eligible technician are available in Zalissya | Pay for one repair | Coupons are spent and retained weapon condition rises | Condition survives combat and creates a hub decision | `ST2-002`, `ST2-006` |
| Squint is reached alive during `A Needle in a Haystack` | Calm him and accept `Piece of Cake` | The cave and Mold-artifact objective become the active branch | Dialogue writes mission state | `ST2-008`, `ST2-010` |
| Echo Detector is active in the cave acid field | Probe hazards, follow the signal and collect Mold | Anomalies cycle; detector range manifests Mold; pickup enters carried inventory | Anomaly and artifact systems combine in one route | `ST2-003`, `ST2-004`, `ST2-010` |
| Mold is carried and Squint awaits the exchange | Hand Mold to Squint | Mold leaves inventory and Ward Sensors become the quest item | Mutually dependent hand-in changes possession and route state | `ST2-010` |
| Ward Sensors are carried and both early recipients are conceptually possible | Return to Richter and hand over the sensors | Richter receives the unique quest item, rewards settle and the Zotov hand-in is no longer available | One retained authored branch closes the scope | `ST2-008`, `ST2-010` |

## Strategic and experiential structure

- Local decision: spend ammunition or concealment, accept exposure or probe an
  anomaly, heal now or preserve a quick item, and carry valuable mass without
  losing the stamina needed for escape.
- Medium-term planning: reach Zalissya with viable weapons and room for quest
  loot; decide whether condition warrants paid repair; preserve detector, bolts
  and medical resources for the Mold cave; retain the declared Richter branch.
- Long-term structure: the scoped unit stops at one early investigation. Its
  item hand-in and relationship direction can affect later access and response,
  but no later faction arc or campaign ending is inferred.
- Common heuristics: listen before entering; test unseen hazard space with a
  bolt; keep weight below overload before combat; reload from cover; treat
  bleeding and radiation before ordinary health loss compounds; distinguish
  carrying an artifact from safely equipping its radiating effect.
- Failure attribution: HUD statuses, radiation meter, ammunition, condition,
  inventory weight, detector cadence, markers and dialogue options explain most
  controllable errors; sampled loot, actor movement and concealed choice effects
  retain uncertainty.
- Claim IDs: `ST2-003`–`ST2-011`.

## Replay and variation

- What changes: incidental loot, combat, damage, ammunition, current weapon
  condition, repair affordability, actor encounters and exact artifact position.
- Randomness or procedural generation: the authored opening route contains
  sampled local encounters and loot under the maintained A-Life world; their
  exact seed is not a new player action.
- Multiple viable strategies: stealth, direct combat, detours and different
  equipment can all reach Squint, but the declared route fixes the peaceful Mold
  exchange and Richter hand-in so comparison remains reproducible.
- Typical replay motive: choose Zotov, keep Mold, test another difficulty or
  carry a different survival loadout; each changes parameters or leaves scope.
- Claim IDs: `ST2-006`–`ST2-010`.

## Adjacent systems and history

- Direct predecessors: earlier S.T.A.L.K.E.R. games and survival shooters; this
  is a mechanical adjacency statement, not a title-ancestry proof.
- Variants: later patches and free content can alter A-Life, balance and optional
  routes; `Cost of Hope` is a separately excluded paid expansion.
- Similar games: Cyberpunk 2077 shares first-person combat, inventory, authored
  dialogue and retained quest branches; Project Zomboid shares embodied survival,
  load and condition pressure; Elden Ring shares live resource combat, equipment
  preparation and save/checkpoint recovery.
- Important differences: this scope binds detector-mediated invisible artifacts,
  probe-cycled anomalies, radiation-bearing equipment and a unique quest-item
  recipient to one survival-FPS investigation.
- Claim IDs: `ST2-001`–`ST2-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-199`, `ACT-200`, `ACT-221`, `ACT-232`, `ACT-288`, `ACT-289` | stance, weapon and exact route are parameters |
| System Behaviour | `SYS-215`, `SYS-223`, `SYS-251`, `SYS-369`, `SYS-373`, `SYS-379`, `SYS-511`–`SYS-514` | loot and actor samples are parameters |
| Constraint | `CON-210`, `CON-284`–`CON-286`, `CON-321`, `CON-336`, `CON-433`–`CON-436` | thresholds and prices are parameters |
| Information | `INF-073`, `INF-075`, `INF-115`, `INF-125`, `INF-128`, `INF-148`, `INF-202`, `INF-203` | interface placement is a parameter |
| Objective | `OBJ-097` | Richter is the fixed recipient parameter |
| Time | `TIM-003` | menus and loads bound live progression |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `169` (`GAME-0001`–`GAME-0169`).
- Exact genome matches: none.
- Tied near matches: `GAME-0146` — Cyberpunk 2077 (`19 / 73 = 0.260274`).
- Supported combination subsets: `COMB-0168`.
- Scan date: 2026-08-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0146` — Cyberpunk 2077 | first-person movement and combat, reloading, loot, HUD/map, dialogue choice and retained quest state | S.T.A.L.K.E.R. 2 adds survival-load thresholds, degrading weapons, probe-cycled anomalies, detector-manifested artifacts and radiating armour-slot effects; Cyberpunk adds build, cyberware and quickhack systems | Near, `0.260274` |

### Preserved research notes

- New genes: `ACT-288`, `ACT-289`, `SYS-511`–`SYS-514`, `CON-433`–`CON-436`,
  `INF-202`, `INF-203` and `OBJ-097`.
- Classification result: bounded new genes plus reuse and one new combination.
- Evidence and reasoning: the corpus already owns live combat, reloads, loot,
  repair, map, local perception, dialogue and quest retention. New boundaries
  isolate bolt-cycled anomalies, detector manifestation, joined radiation/load
  survival pressure, radiating artifact equipment and the early sensor hand-in.

## Taxonomy impact

- Registry changes: thirteen Active genes and `COMB-0168`.
- Taxonomy-change record: none; no existing definition is deprecated, merged or split.
- Candidate terms affected: none.

## Negative results

- A-Life is not promoted as a new scoped gene: the fixed opening observes local
  actor response but does not reproduce the whole persistent world simulation.
- General faction reputation is not a new meter gene: the route records one
  authored recipient and retained response while later faction systems remain out.
- Trading, stash, equipment upgrades and fast travel are not admitted merely
  because Zalissya exposes them; only one condition repair is reproduced.
- Anomalies are not ordinary enemies, traps or damage fields: a bolt can expose
  their local phase, while detector range governs the separate hidden artifact.
- Claim IDs: `ST2-002`–`ST2-010`.

## Open questions

- Exact balance values, incidental A-Life encounters, sampled loot and the Mold
  manifestation point remain parameters of Patch 2.0.2.
- A separate packet is required before claiming a later faction-territory loop,
  emission shelter route, upgrade economy or expansion-specific mechanic.
- Future patches must be re-reviewed before replacing the `2.0.2` boundary.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Поточний base-game маршрут Patch 2.0.2 поєднує
  живий survival-FPS, вагу й стан спорядження, аномалії, bolts, detector-hidden
  artifacts та ранній взаємовиключний quest hand-in (`ST2-001`–`ST2-011`).

## Нові гени

- [Observation | Corroborated | High] Тринадцять нових меж ізолюють probe-cycled
  anomalies, detector-driven artifact manifestation, radiation/load survival
  pressure, artifact risk-benefit slots і Ward Sensors investigation terminal.

## Нові комбінації

- [Observation | Corroborated | High] `COMB-0168` — пройти timed anomaly phase,
  проявити прихований artifact detector proximity, обміняти його на унікальний
  quest item і закрити один retained recipient branch.

## Зміни таксономії

- [Confirmed | Direct | High] Змін таксономії немає.

## Family classification

- `FAM-010` — Real-time system pressure: combat, anomalies, bleeding, radiation,
  hunger, stamina and load continue while Skif moves and decides.
- `FAM-013` — Inventory and fixture dependencies: ammunition, weapon condition,
  medical items, carried weight, detector and armour artifact slots gate action.
- `FAM-012` — Knowledge and evidence progression: detector cadence, PDA state,
  dialogue and Ward Sensors turn partial information into a retained branch.
- `FAM-009` — Tactical forecast and counterplay: local sight, sound, cover and
  anomaly timing make each approach a risk forecast.
- No new family is created from one game.

## Plain-language interpretation

The opening makes danger legible without making it harmless. A bolt can reveal
when an anomaly fires and briefly recovers, but the player still chooses the
line and timing. An Echo Detector does not simply mark treasure on the map: its
signal strengthens until an invisible artifact can appear and be picked up.
That artifact can then become money, quest evidence or a wearable benefit whose
radiation creates a second cost.

The same journey is limited by ammunition, weapon condition, bleeding,
radiation, hunger, stamina and carried weight. Zalissya provides preparation,
but the declared unit stays finite: find Squint through Richter's investigation,
retrieve Mold, exchange it for the Ward Sensors and give those sensors to
Richter. The final hand-in records a choice without pretending to model every
later faction consequence in the Zone.

## New questions

- Which later bounded route can directly reproduce A-Life territory and faction
  response without conflating it with this authored early investigation?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0171` — Forza Horizon 6.
- Optimisation criterion: finish the authorised four-game Goal in its recorded
  demand-led order after one bounded survival-FPS investigation.
- Expected gene pressure: festival entry, direct vehicle handling, event rules,
  route checkpoints, difficulty/assist parameters and race settlement.
- Anti-bias note: do not import anomaly, detector, survival or faction mechanics
  into an open-world racing scope.

## Next research step

- Integrate `GAME-0171` — Forza Horizon 6 after the required thirty-second stop window.

## Design lessons

- A hidden collectible becomes a mechanical search when proximity changes both
  information quality and the object's visible existence.
- One quest-item recipient can bound authored world response without requiring
  a claim about the complete faction simulation.

## Changelog

- 2026-08-27 — Added the reviewed Patch 2.0.2 base-game opening through the
  Richter Ward Sensors hand-in, with official-system evidence, route
  corroboration, thirteen new genes and `COMB-0168`.
