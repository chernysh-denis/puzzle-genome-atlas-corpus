---
game_id: GAME-0295
slug: dark-souls-remastered
game_title: DARK SOULS™: REMASTERED
analysis_status: reviewed
reviewed: 2026-09-13
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-199
    - ACT-200
    - ACT-224
    - ACT-249
    - ACT-436
    - ACT-437
    - ACT-438
  system:
    - SYS-215
    - SYS-364
    - SYS-399
    - SYS-412
    - SYS-578
    - SYS-798
  constraint:
    - CON-282
    - CON-286
    - CON-352
    - CON-354
    - CON-359
    - CON-604
  information:
    - INF-119
    - INF-128
    - INF-317
    - INF-318
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: DARK SOULS™: REMASTERED

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Names, quantities
and exact timings parameterise the genes but do not enter their labels.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam application
  `570940`, one-app consumer package `262430`, default public branch Build ID
  `10943698`, branch record updated 2023-05-10; checked 2026-09-13. No reliable
  official semantic client number was found for that build, so none is inferred.
- Product boundary: the 2018 Remastered Windows release by QLOC and
  FromSoftware, published by FromSoftware and Bandai Namco. Its bundled
  `Artorias of the Abyss` content is part of the product but outside this route.
  The original Prepare to Die Edition, consoles, online play and mods are
  excluded.
- Platform, input and setup: English Windows client, keyboard and mouse,
  offline New Game, Knight class, no starting gift. Character creation is a
  fixed predecessor. Entry is first ordinary control in the Northern Undead
  Asylum cell.
- Primary decision loop: leave the cell, read placed instructions, activate and
  rest at the first bonfire, enter the Asylum Demon chamber and escape through
  the open side gate; collect and equip the Knight's shield and broadsword,
  receive five Estus charges and the East Key from Oscar, open the return route,
  compare the default equipment load with a sufficiently lighter temporary
  load, then restore the full declared Knight equipment; spend one shared
  stamina reserve on strikes, sprint, rolls and held shield guard; lock onto
  eligible enemies; drink Estus only in a safe uninterrupted window; deliberately
  die once with incidental souls, return from the last rested bonfire and
  reclaim the one bloodstain before another death replaces it; re-enter the boss
  from above, use the plunging opening if safely aligned, defeat the Asylum
  Demon, take the Big Pilgrim's Key, open the great door and ride the crow to
  Firelink Shrine.
- Positive terminal: rest at the Firelink Shrine bonfire with the restored
  default Knight equipment, the boss-awarded Humanity, remaining Estus and
  carried souls. Quit through the system menu and load the same save; the same
  bonfire, inventory, equipment and counters are the intended retained state.
  No local application or save existed, so this reload was not performed and
  no returned values are claimed as observed.
- Failure and asymmetry: zero health returns the character to the last rested
  bonfire, changes a living character to Hollow and leaves all carried Humanity
  and souls in one bloodstain; a character already Hollow remains Hollow. A
  second death before recovery replaces the mark and destroys the earlier
  stock. This fresh Knight begins Hollow; the route never reverses Hollowing or
  kindles a bonfire, so those Humanity branches remain adjacent rather than
  required transitions.
- Included: authored traversal and gates; light and strong melee; lock-on;
  stamina-priced sprint, roll and held guard; health and Estus; equipment
  transfer and one controlled load comparison; bonfire recovery, save and enemy
  respawn; one death-mark recovery; boss health disclosure; Asylum Demon defeat;
  Firelink arrival, rest and intended same-save reload.
- Excluded: online messages, phantoms, summons, invasions and covenants;
  Humanity spending, Reverse Hollowing and Kindling; levelling, merchants,
  upgrades, magic and attunement; Master Key and every other class or gift;
  optional asylum returns, sequence breaks, later bosses and regions, DLC area,
  New Game Plus, mods, controllers and consoles; screenshots, official artwork,
  third-party images, video and audio.
- Reproducible parameterisation: install app `570940` from package `262430` and
  confirm public Build ID `10943698`; choose offline New Game, Knight and no
  gift; follow the asylum route through the first bonfire, side-gate escape,
  equipment and Oscar supplies. Before the boss, record the default load band,
  remove enough armour to cross one stated equipment-load boundary, compare the
  roll, and restore the entire default set. Create and recover one bloodstain
  before defeating the boss. Defeat the Asylum Demon, reach and rest at Firelink,
  quit and load the same save. Exact damage, stamina, souls, enemy attacks,
  death position, Estus remainder and timings are parameters.
- Direct-play status: not conducted. No application bundle, Steam manifest,
  install directory, save directory, matching userdata or Spotlight result was
  found locally. Valve establishes the exact product and package; the official
  Remastered manual establishes controls, stamina, equipment load, bonfires,
  Estus, Humanity, death, bloodstain replacement, autosave and quit/load rules.
  Two independent static written routes and focused textual references
  corroborate the selected asylum order and boss reward. This is an
  evidence-backed rules reconstruction, not a claimed playthrough, entitlement
  or reload. No audiovisual evidence was used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `DSR-001` | App `570940` and package `262430` identify the current Windows Remastered product, including the bundled DLC but excluding other editions | Confirmed | Direct | High | P1, P2 |
| `DSR-002` | The public branch projects Build ID `10943698`, updated 2023-05-10, without a safely mapped semantic client version | Confirmed | Corroborated | High | S1 |
| `DSR-003` | New Game, Continue and Load use one autosaved progress record and the system menu supplies the intended safe quit boundary | Confirmed | Direct | High | P3, P9 |
| `DSR-004` | Attacks, sprint, roll and guard draw on stamina, while equipment weight and unmet requirements restrict combat performance | Confirmed | Direct | High | P4–P7 |
| `DSR-005` | Bonfire rest restores health and Estus, saves progress, establishes return and respawns ordinary enemies | Confirmed | Direct | High | P5, P8 |
| `DSR-006` | Death leaves carried souls and Humanity in one bloodstain; another death before recovery replaces it | Confirmed | Direct | High | P5 |
| `DSR-007` | Becoming Hollow on death is asymmetric, and Humanity can reverse Hollowing or kindle only on branches excluded here | Confirmed | Direct | High | P5, P8 |
| `DSR-008` | The selected asylum route supplies the Knight's shield, weapon, five Estus and East Key before the later boss entry | Observation | Corroborated | High | S2, S5 |
| `DSR-009` | Re-entering from above permits a plunging opening; defeating the 813-health Asylum Demon awards 2,000 souls, Humanity and the Big Pilgrim's Key | Observation | Corroborated | High | S2, S3, S5 |
| `DSR-010` | The key opens the great door and the crow carries the character to Firelink Shrine, whose Fire Keeper bonfire restores ten Estus | Observation | Corroborated | High | S2, S4, S5 |
| `DSR-011` | No local executable or save existed, so the intended terminal reload remains unexecuted | Confirmed | Direct | High | R1 |

## Basic data

- Release / origin: QLOC and FromSoftware; published by FromSoftware and Bandai
  Namco Entertainment; Windows release 2018-05-23.
- Platform or physical form: lawfully offered Windows Steam application
  `570940`, package `262430`; fresh offline Knight route from the Northern
  Undead Asylum to the first Firelink Shrine rest.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  ordered dependency sequencing.
- Primary and official sources, accessed 2026-09-13:
  - **[P1]** [Valve application data](https://store.steampowered.com/api/appdetails?appids=570940&cc=ua&l=english),
    for exact title, Windows platform, developers, publishers, release and the
    bundled `Artorias of the Abyss` boundary.
  - **[P2]** [Valve package data](https://store.steampowered.com/api/packagedetails?packageids=262430&cc=ua&l=english),
    for the one-app consumer package and current Ukraine offer.
  - **[P3]** [official Remastered start manual](https://www.fromsoftware.jp/manual/darksoulsremastered/win/start.html),
    for New Game, Continue, Load, autosave and menu-safe exit.
  - **[P4]** [official screen manual](https://www.fromsoftware.jp/manual/darksoulsremastered/win/screen.html),
    for health, stamina, Humanity, souls and equipment surfaces.
  - **[P5]** [official basic-rules manual](https://www.fromsoftware.jp/manual/darksoulsremastered/win/basic.html),
    for combat, souls, bonfire reset, death, Hollowing, bloodstain recovery and
    second-death replacement.
  - **[P6]** [official control manual](https://www.fromsoftware.jp/manual/darksoulsremastered/win/operation.html)
    and **[P7]** [official action manual](https://www.fromsoftware.jp/manual/darksoulsremastered/win/action1.html),
    for sprint, roll, lock-on, guard, attacks, item use and two-hand control.
  - **[P8]** [official bonfire manual](https://www.fromsoftware.jp/manual/darksoulsremastered/win/bonfire.html),
    for lighting, rest, recovery, levelling, Hollow reversal and Kindling.
  - **[P9]** [official menu manuals](https://www.fromsoftware.jp/manual/darksoulsremastered/win/menu1.html),
    [equipment section](https://www.fromsoftware.jp/manual/darksoulsremastered/win/menu2.html),
    for equipment, status, system quit, weight and attribute restrictions.
- Corroborating textual sources, accessed 2026-09-13:
  - **[S1]** [SteamCMD public-branch projection](https://api.steamcmd.net/v1/info/570940),
    for Build ID `10943698`, timestamp and executable name.
  - **[S2]** [Undead Asylum route](https://darksouls.wikidot.com/undead-asylum),
    for the ordered cell, bonfire, escape, equipment, Oscar, boss and crow route.
  - **[S3]** [Asylum Demon reference](https://darksouls.wikidot.com/printer--friendly//asylum-demon),
    for New Game health, opening plunge, reward and key.
  - **[S4]** [Estus reference](https://darksouls.wikidot.com/estus-flask), for the
    Firelink Fire Keeper bonfire's ten-charge refill.
  - **[S5]** [independent written route](https://gamefaqs.gamespot.com/pc/230460-dark-souls-remastered/faqs/79510/undead-asylum),
    for the same mandatory sequence and supplies.
- Reproducible control: **[V1]** repository-side transition trace across
  `P1`–`P9`, `S1`–`S5` and `R1`; written-evidence reasoning, not direct play.
- Research record: **[R1]** local preflight on 2026-09-13 found no application,
  manifest, install, save or matching userdata.
- Claim IDs: `DSR-001`–`DSR-011`. No audiovisual evidence was used.

## Mechanical decomposition

### Action Genes

- Existing `ACT-008`, `ACT-161`, `ACT-199`, `ACT-200`, `ACT-224`, `ACT-249`,
  `ACT-436`, `ACT-437` and `ACT-438` own authored traversal, melee strikes,
  pickup/equipment transfer, interruptible Estus use, bonfire rest, bloodstain
  recovery, stamina-priced roll, held shield guard and reversible lock-on.

### System Behaviour Genes

- Existing `SYS-215`, `SYS-364`, `SYS-399`, `SYS-578` and `SYS-798` own live
  combat, bonfire restoration plus enemy repopulation, checkpoint death with one
  recoverable currency mark, continuous health and the shared recovering
  stamina reserve. Existing `SYS-412` owns equipment attributes and load changing
  combat performance. The Asylum Demon has no in-fight transformation, so
  `SYS-799` and `COMB-0260` are rejected.

### Constraint Genes

- Existing `CON-282`, `CON-286`, `CON-352`, `CON-354`, `CON-359` and `CON-604`
  own the guardian gate, uninterrupted restorative, one-mark limit, attack
  stamina/recovery gate, equipment/load legality and the shared reserve needed
  for evasion, sprint and guard.

### Information, Objective and Time Genes

- Existing `INF-119`, `INF-128`, `INF-317` and `INF-318` expose personal
  resources, found items, fixed placed instructions and the boss health bar.
  `OBJ-080` owns defeat of the mandatory guardian and crossing to the next
  declared checkpoint. `TIM-003` owns uninterrupted real-time resolution.

## Reproducible transitions

| Before | Action | Bounded resolution | Claim |
|---|---|---|---|
| Fresh Hollow Knight in the asylum cell | Leave, read instructions and rest at the first bonfire | The authored route and return point become active | `DSR-003`, `DSR-005`, `DSR-008` |
| First boss entry | Escape through the open side gate | The premature encounter ends without defeating the guardian | `DSR-008` |
| Shield, broadsword and Oscar are reachable | Equip the items and accept Estus plus East Key | The declared combat kit and return route become available | `DSR-008` |
| Default Knight equipment is worn | Remove enough armour to cross a load band, roll, then restore it | Equipment load changes movement performance without changing the terminal loadout | `DSR-004` |
| Stamina is available | Strike, sprint, roll, guard and allow recovery | Offence and defence compete for one replenishing reserve | `DSR-004` |
| Incidental souls are carried | Die once, return and touch the bloodstain | The same souls return; a second death beforehand would replace them | `DSR-006`, `DSR-007` |
| Upper boss entry is open | Plunge if aligned and finish the Asylum Demon | Boss health reaches zero and souls, Humanity and key are awarded | `DSR-009` |
| Big Pilgrim's Key is held | Open the great door and approach the ledge | The crow transition delivers the character to Firelink Shrine | `DSR-010` |
| Firelink bonfire is reachable | Rest, quit and load the same save | The declared equipment and counters are intended to return unchanged; local verification remains unperformed | `DSR-003`, `DSR-010`, `DSR-011` |

## Strategic and experiential structure

- Planning horizon: visible health, stamina, Estus, souls, Humanity, equipment
  and any bloodstain support the next risk decision; the authored route supplies
  the immediate dependency rather than an omniscient map.
- Local tactics: preserve stamina for a roll or guard, release the shield to
  recover faster, drink only after an enemy recovery, and use the high-entry
  plunge without assuming it completes the fight.
- Medium-term structure: resting replenishes health and Estus but repopulates
  ordinary enemies. A bloodstain detour risks replacing the sole stored stock.
- Irreversibility: ordinary positioning and lock-on are quickly reversible;
  Estus lasts until rest; a second death permanently erases the prior mark;
  the boss defeat and Firelink arrival settle route progress.

## Replay and variation

- Route geometry, supplies, gate order and boss identity are authored. Enemy
  attack selection and exact damage, stamina, souls and timing vary.
- The packet allows different mixes of roll, guard and spacing, but requires one
  controlled load comparison and one recovered death mark for transfer clarity.

## Adjacent systems and history

- DARK SOULS III shares 25 of these 27 genes but adds a guardian phase change;
  this packet instead makes equipment-load comparison causal in the opening.
- Lies of P shares the checkpoint, stamina and death-mark skeleton but adds
  Guard Regain, blade condition, Perfect Guard and a stagger-finisher chain.
- Humanity, living/Hollow state and Kindling are documented adjacent systems;
  the selected fresh route exposes the counter and asymmetric death rule but
  deliberately never spends Humanity.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-199`, `ACT-200`, `ACT-224`, `ACT-249`, `ACT-436`, `ACT-437`, `ACT-438` | route, weapon, shield and item names |
| System Behaviour | `SYS-215`, `SYS-364`, `SYS-399`, `SYS-412`, `SYS-578`, `SYS-798` | values, load thresholds and recovery rates |
| Constraint | `CON-282`, `CON-286`, `CON-352`, `CON-354`, `CON-359`, `CON-604` | costs, timing and gate order |
| Information | `INF-119`, `INF-128`, `INF-317`, `INF-318` | wording and interface layout |
| Objective | `OBJ-080` | guardian and terminal checkpoint |
| Time | `TIM-003` | animation and recovery timing |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `294` (`GAME-0001`–`GAME-0294`).
- Exact genome matches: none.
- Tied near matches: `GAME-0262` — DARK SOULS™ III (`25 / 28 = 0.892857`).
- Supported combination subsets: none.
- Scan date: 2026-09-13.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0262` — DARK SOULS™ III | `ACT-008`, `ACT-161`, `ACT-199`, `ACT-200`, `ACT-224`, `ACT-249`, `ACT-436`, `ACT-437`, `ACT-438`, `SYS-215`, `SYS-364`, `SYS-399`, `SYS-578`, `SYS-798`, `CON-282`, `CON-286`, `CON-352`, `CON-354`, `CON-604`, `INF-119`, `INF-128`, `INF-317`, `INF-318`, `OBJ-080`, `TIM-003` | Both routes share stamina-priced attack, sprint, roll and guard, checkpoint recovery with ordinary-enemy return, vulnerable healing, reversible lock-on, one replaceable death mark and a guardian-opened next checkpoint. DARK SOULS III adds a health-threshold boss transformation. This Remastered packet instead deliberately crosses an equipment-load boundary and restores the default Knight loadout before settlement. | Near, `0.892857` |

## Taxonomy impact

- New genes, combinations or wording changes: none. All 27 genes are reused.
- Taxonomy-change record: none.
- Candidate terms affected: bonfire, Estus, Humanity, Hollow, bloodstain,
  equipment-load bands, Asylum Demon and Big Pilgrim's Key remain parameters.

## Negative results

- Equipment load is admitted only because the reproducible control deliberately
  crosses a load boundary and restores the declared default equipment.
- Reverse Hollowing and Kindling are not admitted: the route documents but does
  not execute them. A product-specific Humanity gene is therefore unnecessary.
- No audiovisual evidence was opened, played, heard, analysed or used.

## Delta summary

## New facts

- [Confirmed/Observation | Direct/Corroborated | High] `DSR-001`–`DSR-011`:
  one bounded asylum route links shared-stamina melee, equipment-load control,
  bonfire reset and single-mark recovery to the first Firelink rest.

## New genes

- [Observation | Direct | High] No new genes; all 27 active owners are reused.

## New combinations

- [Observation | Direct | High] No new combinations; no verified combination
  is a strict proper subset of this genome.

## Taxonomy changes

- [Observation | Direct | High] No taxonomy changes; no existing definition,
  lifecycle or earlier signature changes.

## Inferences

- [Strong Pattern | Corroborated | High] The 27-gene signature is a reuse-only
  variant of the DARK SOULS III opening: load replaces boss transformation as
  the scoped differentiator.

## Open questions

- Direct same-save reload and exact returned counters await lawful local access.

## Contradictions

- None within the declared product, build and route boundary.

## New questions

- Which exact Estus, Humanity, souls and equipment values return after a
  performed current-build Firelink reload?

## Next recommended game

- [Hypothesis | Limited | High] Noita.
- Optimisation criterion: replace authored checkpoint melee with a simulated
  pixel-material descent and wand-spell composition.
- Expected information gain: test whether destructive material interaction and
  spell ordering produce a distant signature without inventing substance names.
- Backlog impact: keep MONSTER HUNTER RISE after Noita in selection-018 order.

## Why this game

- [Hypothesis | Limited | High] Noita sharply changes the action, simulation
  and information surfaces while retaining real-time risk and a bounded early
  terminal.

## Confidence and unresolved questions

- Confidence: High for product, manual rules and ordered asylum route; Medium
  for unperformed current-build terminal values.
- Resolution path: perform the declared offline route, record text-only state
  before quit and after load, and compare the counters and default equipment.
- Consequence: the reload remains an intended verification boundary rather than
  an observation.
