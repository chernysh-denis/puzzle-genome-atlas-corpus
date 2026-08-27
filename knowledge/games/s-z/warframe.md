---
game_id: GAME-0168
slug: warframe
game_title: Warframe
analysis_status: reviewed
reviewed: 2026-08-27
combination_ids:
  - COMB-0166
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-164
    - ACT-183
    - ACT-190
    - ACT-215
    - ACT-218
    - ACT-283
    - ACT-284
  system:
    - SYS-215
    - SYS-222
    - SYS-251
    - SYS-348
    - SYS-380
    - SYS-500
    - SYS-501
    - SYS-502
    - SYS-503
    - SYS-504
  constraint:
    - CON-262
    - CON-269
    - CON-425
    - CON-426
    - CON-427
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-195
    - INF-196
    - INF-197
  objective:
    - OBJ-095
  time:
    - TIM-003
---

# Game: Warframe

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Parameters describe
gene instances but do not enter the signature.

## Analysis scope

- Version / ruleset: official PC build `43.5.4`, fresh account, Solo
  matchmaking, default controls and difficulty, deterministic starter route
  using Excalibur, Skana, Lato and Braton.
- Primary decision loop: read the local generated corridor, waypoint and enemy
  pressure; parkour or move to a firing/melee position; aim, attack, reload or
  cast within current Energy/readiness; collect reachable drops; complete the
  mission objective; follow the extraction marker; settle rewards and Affinity
  on the Orbiter; then configure the restored function for the next quest step.
- Entry and exit: begins at the first Warframe choice in Awakening; succeeds
  when every mandatory Awakening and Vor's Prize step is complete, the required
  Orbiter functions are restored and Captain Vor is defeated.
- Included: starter selection; double jump, slide, bullet jump, aim glide and
  wall traversal as direct navigation parameters; primary, secondary, melee and
  ability combat; ammunition, Shields, Health, Energy, downed state and finite
  self-revives; Grineer terminal hacking; generated tile-set routes, objective
  markers and extraction; contact pickups; Arsenal loadout and Mod placement;
  equipment Affinity/ranks; mission settlement; the mandatory opening quest.
- Excluded: every later quest, Junction and planet; open worlds; exhaustive
  Star Chart clearing; alternate starters as separate signatures; companions,
  clans, trading, Market/Platinum, Foundry catalogue breadth, Mastery tests,
  multiplayer coordination, PvP, events, Steel Path, endgame and monetisation.
- Potential scoped modules: one Junction route; one later quest; one open-world
  bounty loop; cooperative matchmaking and revive authority; or a Foundry build
  packet with real-time completion.
- Direct-play status: no fresh full PC run was conducted. Digital Extremes'
  current patch notes establish build `43.5.4`; its official New Player, Quick
  Start, Vor's Prize, Mods and multiplayer guides directly establish the
  controls, interfaces, Solo boundary, hub restoration and quest terminal. The
  official community wiki corroborates tile-set assembly only.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `WF-001` | The scoped current PC build is `43.5.4`, while the opening guides remain the official onboarding route | Confirmed | Direct | High | P1, P2 |
| `WF-002` | Awakening supplies one starter Warframe and primary, secondary and melee choices before the player restores the Orbiter | Confirmed | Direct | High | P2, P3, P4 |
| `WF-003` | Direct movement includes slide, bullet jump, aim glide, wall traversal and ordinary locomotion while combat remains live | Confirmed | Direct | High | P4 |
| `WF-004` | A live loadout exposes primary, secondary, melee, abilities, ammunition, Shields, Health and Energy | Confirmed | Direct | High | P4 |
| `WF-005` | Zero Health enters a downed/bleedout state; self-revival consumes one of four mission revives restored aboard the ship | Confirmed | Direct | High | P4 |
| `WF-006` | Grineer hacking rotates timed terminal nodes into a connected solution and may be retried | Confirmed | Direct | High | P4 |
| `WF-007` | Mission routes connect reusable tiles from entry through objective to extraction, with partial branches | Observation | Corroborated | High | P4, S1 |
| `WF-008` | The minimap and white/yellow markers disclose the current objective or extraction direction but not every future room | Confirmed | Direct | High | P3, P4 |
| `WF-009` | Arsenal configuration and Mods change equipment under compatibility, capacity, rank and polarity rules | Confirmed | Direct | High | P3, P4, P5 |
| `WF-010` | Affinity advances the separately ranked Warframe and weapons and raises Mod capacity | Confirmed | Direct | High | P4, P5 |
| `WF-011` | Valid extraction settles eligible pickups, rewards and equipment progress before returning to the Orbiter | Confirmed | Direct | High | P2, P3, P4 |
| `WF-012` | Vor's Prize restores Arsenal, Foundry, Mod Station and Navigation functions across mandatory missions and ends after defeating Vor | Confirmed | Direct | High | P3, P7 |
| `WF-013` | Solo is an explicit valid matchmaking mode and removes matchmaking rather than changing the quest route | Confirmed | Direct | High | P6 |

## Basic data

- Release / origin: Digital Extremes; public release 2013; scoped PC hotfix
  `43.5.4` in August 2026.
- Platform or physical form: PC online software played in explicit Solo mode.
- Puzzle family: generated-route real-time action mission with persistent
  equipment preparation and extraction settlement.
- Primary sources:
  - `P1` — [official Warframe patch notes](https://www.warframe.com/en/patch-notes),
    current PC hotfix `43.5.4`, checked 2026-08-27.
  - `P2` — [official New Player Guide](https://www.warframe.com/en/news/new-player-guide),
    checked 2026-08-27.
  - `P3` — [official Vor's Prize quest guide](https://www.warframe.com/en/guides/quests/vors-prize),
    checked 2026-08-27.
  - `P4` — [official Quick Start Guide](https://www.warframe.com/en/game/quickstart),
    checked 2026-08-27.
  - `P5` — [official Mods Guide](https://www.warframe.com/en/news/mods-guide),
    checked 2026-08-27.
  - `P6` — [official Multiplayer Guide](https://www.warframe.com/en/news/multiplayer-guide),
    checked 2026-08-27.
  - `P7` — [official Quest Tips](https://support.warframe.com/hc/en-us/articles/218290327-Quest-Tips-Up-to-Second-Dream-Minimal-Spoilers),
    checked 2026-08-27.
- Secondary sources:
  - `S1` — [Warframe Wiki: Tile Sets](https://wiki.warframe.com/w/Tile_Sets),
    entry-objective-exit assembly and branch structure, checked 2026-08-27.
- Claim IDs: `WF-001`–`WF-013`.

## Mechanical decomposition

### Action Genes

- `ACT-008` — navigate the Warframe through the locally visible 3D route;
  parkour forms are movement parameters, not separate goals.
- `ACT-161` — aim and attack a reachable hostile with the active firearm or melee.
- `ACT-164` — switch among the carried primary, secondary and melee slots.
- `ACT-183` — reload the active magazine-fed weapon.
- `ACT-190` — cast one selected Warframe ability.
- `ACT-215` — configure the bounded Warframe/primary/secondary/melee loadout.
- `ACT-218` — enter the activated extraction region after the objective.
- `ACT-283` — install or remove one compatible Mod in the Arsenal.
- `ACT-284` — rotate a timed terminal network into its accepted cipher.
- Parameters: input device, starter choice, parkour timing, aim, active weapon,
  Mod inventory, equipment rank and current quest step.
- Claim IDs: `WF-002`–`WF-006`, `WF-009`.

### System Behaviour Genes

- `SYS-215` — resolve directly commanded hostile combat in real time.
- `SYS-222` — collect eligible ammunition, resources and Mods on contact.
- `SYS-251` — advance the authored mandatory quest sequence.
- `SYS-348` — resolve regenerating Shields, Health and the downed state.
- `SYS-380` — resolve each selected ability into its typed live effect.
- `SYS-500` — assemble an entry-objective-extraction route from authored tiles.
- `SYS-501` — apply installed Mods through capacity and polarity.
- `SYS-502` — distribute Affinity into separate equipment ranks.
- `SYS-503` — settle valid extraction into retained rewards and progress.
- `SYS-504` — restore Orbiter segments across the opening quest chain.
- Resolution order: create mission route; resolve navigation, combat, pickups
  and hacking continuously; complete the objective; activate extraction; settle
  rewards/Affinity; restore the quest-bound segment; expose the next mission.
- Claim IDs: `WF-003`–`WF-012`.

### Constraint Genes

- `CON-262` — the live loadout and its magazine/reserve ammunition are bounded.
- `CON-269` — an ability requires sufficient Energy, readiness, range and target.
- `CON-425` — Mods obey compatibility, capacity and polarity-adjusted drain.
- `CON-426` — objective completion gates extraction settlement.
- `CON-427` — self-revival consumes finite per-mission stock.
- Claim IDs: `WF-004`, `WF-005`, `WF-009`, `WF-011`.

### Information Genes

- `INF-073` — active weapon, carried weapon slots and ammunition are visible.
- `INF-115` — local sight and sound expose only nearby hostile state.
- `INF-119` — Shields, Health, Energy, rank/Affinity and ability state are visible.
- `INF-125` — Navigation and the quest guide expose unlocked nodes and next gates.
- `INF-195` — minimap and markers expose the partial live route and endpoint.
- `INF-196` — Arsenal exposes ranks, Mod slots, capacity, polarity and statistics.
- `INF-197` — mission summary exposes retained rewards, rank and quest changes.
- Claim IDs: `WF-004`, `WF-008`–`WF-012`.

### Objective Genes

- `OBJ-095` — complete Awakening and Vor's Prize, restore the Orbiter and defeat
  Captain Vor.
- Success, evaluation and failure: final quest completion is success; each
  extracted mission is intermediate evaluation; exhausting revival/mission
  recovery fails the current mission but does not erase retained prior progress.
- Claim IDs: `WF-002`, `WF-011`, `WF-012`.

### Time Genes

- `TIM-003` — mission movement, enemies, attacks, projectiles and timers advance
  while input remains available.
- Claim IDs: `WF-003`–`WF-006`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh account reaches starter selection | Choose Excalibur and the fixed starter weapon sequence | The selected Warframe and three weapon classes become the initial live loadout | Bounded reproducible parameterisation | `WF-002` |
| Objective marker lies beyond a mixed-height corridor | Slide, bullet-jump and aim-glide toward it | Current motion and collision advance while the route remains locally revealed | Direct parkour through generated tiles | `WF-003`, `WF-007`, `WF-008` |
| Grineer blocks the next route | Aim, attack, switch or reload; optionally cast | Damage, ammunition, Energy, Shields and enemy behaviour resolve in real time | Layered live combat loop | `WF-004`, `WF-005` |
| A locked Grineer terminal is active | Rotate nodes before the timer expires | Accepted connectivity unlocks the gated continuation; failure permits another attempt | Timed terminal cipher | `WF-006` |
| Mandatory objective reaches completion | Follow the extraction marker and enter its region | Mission closes and eligible rewards/Affinity become persistent | Objective-gated extraction | `WF-008`, `WF-011` |
| Restored Arsenal contains an owned compatible Mod | Install it in a legal slot | Polarity-adjusted drain consumes capacity and previewed statistics change | Persistent preparation loop | `WF-009`, `WF-010` |
| Final mandatory Vor's Prize mission reaches Captain Vor | Defeat Vor and settle the mission | Quest records completion with restored Orbiter functions and retained equipment progress | Scoped terminal | `WF-012` |

## Strategic and experiential structure

- Local decision: balance speed, cover/spacing, target priority, ammunition and
  ability Energy while following only the revealed route.
- Medium-term planning: extract with useful drops, inspect rank/capacity gains,
  install compatible Mods and choose a stronger configuration for the next
  mandatory mission.
- Long-term structure: each successful mission restores one part of the Orbiter
  and narrows the remaining quest chain toward Vor.
- Common heuristics: keep moving to preserve spacing; use bullet jumps to cross
  vertical rooms; reload before committing to an objective chamber; match Mod
  polarity when capacity is scarce; follow the updated marker after objectives.
- Failure attribution: visible resources, damage layers, objective state,
  markers and Mod validation distinguish combat, route and preparation errors.
- Claim IDs: `WF-003`–`WF-012`.

## Replay and variation

- What changes between sessions: assembled mission rooms, drops, combat spawns,
  accumulated Affinity and chosen Mod configuration.
- Randomness or procedural generation: mission layouts reuse authored tiles in
  varying valid arrangements; this scope does not treat their seed as a choice.
- Multiple viable strategies: gun, melee and ability emphasis can all complete
  ordinary opening encounters; fixed starter choices keep this record reproducible.
- Typical replay motive: retry a failed mission, improve equipment ranks and
  refine Mods; farming beyond the mandatory route is excluded.
- Claim IDs: `WF-007`, `WF-009`–`WF-011`.

## Adjacent systems and history

- Direct predecessors: third-person action missions with persistent equipment
  preparation and hub return; this is a mechanical adjacency claim, not title
  ancestry.
- Variants: later Warframe quests add cinematic state, Junction prerequisites,
  companions, open worlds and specialised mission economies.
- Similar games: Helldivers 2 shares live objectives and extraction, while ARC
  Raiders shares hub preparation and retained results.
- Important differences: this scope makes extraction mandatory for ordinary
  mission settlement, preserves owned equipment, ranks it through Affinity and
  restores an authored hub function after each tutorial step.
- Claim IDs: `WF-007`–`WF-013`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-164`, `ACT-183`, `ACT-190`, `ACT-215`, `ACT-218`, `ACT-283`, `ACT-284` | exact starter and parkour form are parameters |
| System Behaviour | `SYS-215`, `SYS-222`, `SYS-251`, `SYS-348`, `SYS-380`, `SYS-500`–`SYS-504` | enemy/spawn values and tile seed are parameters |
| Constraint | `CON-262`, `CON-269`, `CON-425`–`CON-427` | capacities, drains and revive count are parameters |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-195`–`INF-197` | HUD scale and marker distance are parameters |
| Objective | `OBJ-095` | alternate starter choices do not change the terminal |
| Time | `TIM-003` | network latency is excluded in Solo scope |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `167` (`GAME-0001`–`GAME-0167`).
- Exact genome matches: none.
- Tied near matches: `GAME-0159` — Helldivers 2 (`15 / 51 = 0.294118`).
- Supported combination subsets: `COMB-0166`.
- Scan date: 2026-08-27.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0159` — Helldivers 2 | direct navigation, weapon switching, aiming, reloading, abilities, loadout preparation, extraction, live hostile combat, typed ability effects, ammunition and ability constraints, active-equipment/local-threat/resource HUD and real-time input | Warframe's Solo opening assembles tile routes, solves terminal ciphers, equips capacity-and-polarity Mods, ranks several equipment items through Affinity, makes extraction the ordinary reward settlement and restores Orbiter functions through a finite quest; Helldivers uses four-player stratagem codes, friendly fire, patrol escalation, shared Reinforce and separates mission success from optional extraction and Galactic War settlement | Near, `0.294118` |

### Preserved research notes

- New genes: `ACT-283`, `ACT-284`, `SYS-500`–`SYS-504`, `CON-425`–`CON-427`,
  `INF-195`–`INF-197` and `OBJ-095`.
- Classification result: bounded new genes plus reuse and one new combination.
- Evidence and reasoning: the existing corpus already owns direct navigation,
  weapons, abilities, loadout selection, layered combat, authored quests and
  real-time input. New boundaries isolate Mod socket economics, tile-set mission
  assembly, equipment-specific Affinity, extraction settlement, Orbiter
  restoration, timed hacking and the exact opening terminal.

## Taxonomy impact

- Registry changes: fourteen Active genes and `COMB-0166`.
- Taxonomy-change record: none; no existing definition is deprecated, merged or split.
- Candidate terms affected: none.

## Negative results

- Mastery Rank is excluded: the bounded opening terminal does not require an
  account test or a general account-level progression model.
- Foundry crafting duration is excluded: the quest restores the function, but
  the scoped terminal does not require analysing its wider recipe/time economy.
- Multiplayer revive, trading and clans are excluded by explicit Solo scope.
- Later quest, Junction, open-world and monetisation state cannot silently enter
  the signature merely because the same account could access them later.

## Delta summary

## Нові факти

- [Confirmed | Direct | High] Поточний solo-маршрут Awakening і Vor's Prize
  пов'язує рух, бій, злам терміналів, цілі місій, евакуацію, Моди, ранги
  спорядження та поступове відновлення Орбітера (`WF-001`–`WF-013`).

## Нові гени

- [Observation | Corroborated | High] Чотирнадцять нових меж ізолюють
  установлення Модів, термінальний шифр, складання маршруту з тайлів, місткість
  і полярність, Affinity спорядження, збереження результатів евакуації,
  відновлення Орбітера, маркери маршруту та фінал вступного квесту.

## Нові комбінації

- [Confirmed | Direct | High] `COMB-0166` — solo-ланцюг місій від підготовки
  спорядження через локальну ціль до евакуації та стійкого поступу.

## Зміни таксономії

- [Confirmed | Direct | High] Змін таксономії немає.

## Family classification

- `FAM-010` — Real-time system pressure: movement, enemies, resources and
  objective execution continue while the player acts.
- `FAM-013` — Inventory and fixture dependencies: persistent equipment, Mods,
  restored Orbiter stations and mission rewards constrain the next mission.
- `FAM-017` — Ordered dependency sequencing: mandatory quest settlement restores
  functions and unlocks the next step in a fixed opening dependency chain.
- No new family is created from one game.

## Plain-language interpretation

The opening does more than teach shooting. Each mission is a short generated
route with a visible immediate marker: move through it, survive the objective
and reach extraction. What returns to the Orbiter matters. Resources, Mods and
equipment Affinity persist, while temporary ammunition and the room layout do
not. The player then turns those gains into a legal Mod configuration under a
small capacity budget.

Vor's Prize links those loops into an ordered tutorial. Successful missions
restore the Arsenal, Foundry, Mod Station and Navigation, so the hub itself
becomes the record of progress. Defeating Captain Vor closes a finite opening
route without pretending that twelve years of later quests, frames, economies
and multiplayer systems belong to the same analysis.

## New questions

- Which extraction game reuses objective-gated mission settlement while
  replacing persistent owned equipment with carried gear at risk?

## Наступна рекомендована гра

- [Confirmed | Direct | High] `GAME-0169` — Euro Truck Simulator 2.
- Optimisation criterion: continue the recorded four-game Goal in immutable
  demand-led order after Warframe's generated action-extraction loop.
- Expected gene pressure: road-rule navigation, vehicle physics, fatigue/fuel,
  cargo-contract deadlines, delivery evaluation and persistent company economy.
- Anti-bias note: do not import Warframe's combat, generated tile route or
  extraction settlement into a road-haul scope.

## Next research step

- Integrate `GAME-0169` — Euro Truck Simulator 2 after the required thirty-second stop window.

## Design lessons

- A tutorial can be a complete systemic unit when it restores a persistent hub
  and terminates at a named boss rather than merely ending after controls.
- Extraction is not one universal boundary: here it commits rewards and gear
  growth, unlike games that risk or forfeit the carried loadout.

## Open questions

- Should a later multiplayer scope reuse the same extraction genome when squad
  revival and shared Affinity introduce additional authority and information?
