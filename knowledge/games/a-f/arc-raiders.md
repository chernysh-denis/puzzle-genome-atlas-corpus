---
game_id: GAME-0143
slug: arc-raiders
game_title: ARC Raiders
analysis_status: reviewed
reviewed: 2026-08-21
combination_ids:
  - COMB-0141
gene_ids:
  action:
    - ACT-008
    - ACT-123
    - ACT-161
    - ACT-164
    - ACT-191
    - ACT-199
    - ACT-200
    - ACT-215
    - ACT-216
    - ACT-217
    - ACT-218
    - ACT-219
    - ACT-221
  system:
    - SYS-215
    - SYS-223
    - SYS-299
    - SYS-319
    - SYS-328
    - SYS-346
    - SYS-347
    - SYS-348
    - SYS-349
    - SYS-350
    - SYS-352
    - SYS-353
    - SYS-354
  constraint:
    - CON-210
    - CON-284
    - CON-285
    - CON-286
    - CON-290
    - CON-315
    - CON-316
    - CON-317
    - CON-318
    - CON-319
    - CON-320
    - CON-321
    - CON-322
  information:
    - INF-075
    - INF-115
    - INF-128
    - INF-132
    - INF-137
    - INF-138
    - INF-139
    - INF-140
  objective:
    - OBJ-021
  time:
    - TIM-003
---

# Game: ARC Raiders

## Analysis scope

- Version / ruleset: PC Standard Edition at public `Live Update 1.42.0`,
  released 2026-08-18; solo matchmaking into a standard Dam Battlegrounds raid
  with no special Map Condition, using the offered Free Loadout.
- Included: pre-raid loadout state; one bounded shared Topside session; direct
  movement, weapons, health, shield and restorative use; ARC and human threats;
  sight, sound and machine telegraphs; searching, looting, Safe Pocket, field
  recycling and crafting; ordinary extraction or knockout; retained stash,
  sale, Workshop craft, weapon maintenance, XP, level and skill allocation.
- Reproducible checkpoint: enter Dam Battlegrounds solo with Free Loadout;
  search at least one ordinary container; transfer one eligible valuable item
  to the Safe Pocket; collect or produce one unsecured item; then trace both
  terminal branches from equivalent legal states. Successful extraction banks
  the unsecured loadout and loot, while knockout forfeits it but retains the
  pocketed item. In Speranza, use retained state for one legal sale or recycle,
  one available craft or repair and the first available skill-point purchase.
- Excluded: duo and trio parties, Practice Range, special Map Conditions,
  named seasonal events, quests beyond incidental progress, Trials, Feats,
  Raider Decks, Projects, Expedition departure and reset, Nomadic Envoy vault,
  paid cosmetics and exhaustive maps, ARC types, weapons or recipes.
- Direct-play status: no live paid-account raid was conducted. Current official
  Help Center rules, product material and versioned patch notes directly
  establish the scoped state transitions; exact numeric balance remains a
  parameter and is not promoted into the genome.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `ARC-001` | The reviewed public ruleset is PC Live Update 1.42.0 and supports separately tracked solo matchmaking | Confirmed | Corroborated | High | P1, P2, P3 |
| `ARC-002` | A Free Loadout stakes no retained gear but supplies a smaller randomized kit for one Topside raid | Confirmed | Direct | High | P4 |
| `ARC-003` | Higher-danger locations and changing conditions alter available loot while search and carry capacity bound acquisition | Observation | Corroborated | High | P2, P4, P5 |
| `ARC-004` | ARC machines and human Raiders create simultaneous PvE and PvP pressure through local visual and acoustic information | Observation | Corroborated | High | P2, P5, P6 |
| `ARC-005` | Compatible weapons, ammunition, mods, augments, shields and utilities determine live combat capability and attrition | Observation | Corroborated | High | P2, P7, P8 |
| `ARC-006` | Search, medical use and extraction are interruptible proximity- or duration-bound interactions in the live session | Observation | Corroborated | High | P6, P8 |
| `ARC-007` | Successful extraction banks ordinary carried state, while knockout forfeits all unsecured entered and scavenged items | Confirmed | Corroborated | High | P2, P4, P9 |
| `ARC-008` | Eligible Safe Pocket contents survive the same knockout settlement that removes ordinary carried inventory | Confirmed | Corroborated | High | P4, P9 |
| `ARC-009` | Retained loot feeds sales, recycling, station-gated Workshop craft, repair and later loadouts | Confirmed | Corroborated | High | P2, P5, P7, P8 |
| `ARC-010` | Raid activity awards persistent XP, levels and skill points spent across Conditioning, Mobility and Survival | Confirmed | Direct | High | P2, P5 |

## Basic data

- Release / origin: Embark Studios; released 2025-10-30; reviewed at Live
  Update 1.42.0 on 2026-08-21.
- Platform or physical form: online third-person PvPvE extraction adventure on
  PC and current consoles; PC Standard Edition is the analytical platform.
- Puzzle family: tactical forecast and counterplay; real-time system pressure;
  inventory and fixture dependencies; ordered dependency sequencing.
- Primary sources:
  - **[P1]** [official Live Update 1.42.0](https://arcraiders.com/de/news/live-update-1-42-0),
    for the current version boundary, regional Map Conditions, ARC behaviour,
    combat fixes and live-service state.
  - **[P2]** [official Steam product page](https://store.steampowered.com/app/1808500/ARC_Raiders/),
    for release, solo or three-player scope, surface-to-Speranza loop, maps,
    risk, ARC, crafting, recipes, quests, skills, weapons, augments and tools.
  - **[P3]** [official Live Update 1.36.0](https://arcraiders.com/news/live-update-1-36-0),
    for separately tracked solo, duo and trio matchmaking state.
  - **[P4]** [official first-raid guide](https://id.embark.games/arc-raiders/support/faq/135-your-first-raid-1759328782),
    for scavenging, danger-weighted loot, knockout loss, Safe Pocket and Free
    Loadout trade-offs.
  - **[P5]** [official launch systems overview](https://arcraiders.com/fr/news/everything-you-need-to-know),
    for Topside conditions, XP, skills, Workshop, Traders and risk settlement.
  - **[P6]** [official Shrouded Sky 1.17.0 notes](https://arcraiders.com/news/shrouded-sky-patch-notes-1-17-0),
    for proximity searches, cancellation, downed state, hatch extraction,
    field craft, deployables and readable machine attacks.
  - **[P7]** [official gearing guide](https://id.embark.games/arc-raiders/support/faq/140-gearing-up),
    for loadout classes, ammunition, mods, gadgets, augments, durability and
    resource-paid weapon repair.
  - **[P8]** [official game-progression guide](https://id.embark.games/arc-raiders/support/faq/139-game-progression-1759329960),
    for persistent levels, skill branches, recipes and specialised stations.
  - **[P9]** [official 1.18.0 notes](https://id.embark.games/arc-raiders/support/faq/236-patch-notes-1-18-0),
    for protected-pocket item eligibility and risk-conditioned blueprint loot.
  - **[P10]** [official Field Crafting guide](https://id.embark.games/arc-raiders/support/faq/141-field-crafting-1759329975),
    for carried-material recipes and immediate Field Recycling.
- Secondary sources: none admitted.
- Claim IDs: `ARC-001`–`ARC-010`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, navigate; `ACT-123`, hand-craft a selected field
  recipe; `ACT-161`, aim and strike; `ACT-164`, select a carried quick item;
  `ACT-191`, spend a persistent build point; `ACT-199`, transfer or equip loot;
  `ACT-200`, use an interruptible restorative.
- New genes: `ACT-215`, assemble a retained or Free Loadout; `ACT-216`, search
  a container or disabled machine; `ACT-217`, move an item through Safe Pocket
  protection; `ACT-218`, activate and enter extraction; `ACT-219`, sell or
  recycle; `ACT-221`, repair or upgrade
  a retained weapon.
- Claim IDs: `ARC-002`–`ARC-010`.

### System Behaviour Genes

- Existing genes: `SYS-215`, direct real-time hostile combat; `SYS-223`, weapon
  durability loss; `SYS-319`, restorative cast resolution; `SYS-328`, personal
  Field Crafting queue; `SYS-299`, convert persistent experience into levels
  and build points.
- New genes: `SYS-346`–`SYS-350` and `SYS-352`–`SYS-354`, covering conditioned raid instantiation, ARC
  perception and typed attacks, shield-health-DBNO state, raid settlement,
  Safe Pocket retention, persistent XP, cross-raid stash and recipes,
  station-gated Workshop output and danger-conditioned loot.
- Resolution order: initialise the condition-bound shared raid; accept live
  movement, search, loot and combat; resolve extraction or knockout; partition
  carried state; award XP; persist returned inventory and hub progression.
- Claim IDs: `ARC-001`–`ARC-010`.

### Constraint Genes

- Existing genes: `CON-210`, typed stack capacity; `CON-284`, backpack and
  equipment slots; `CON-285`, compatible live weapon state; `CON-286`, legal
  uninterrupted restorative cast; `CON-290`, terminal Solo defeat for one match.
- New genes: `CON-315`–`CON-322`, covering augment-shaped loadout legality,
  Safe Pocket eligibility, live extraction, unsecured knockout loss,
  interruptible search, Workshop prerequisites, weapon-maintenance costs and
  skill-tree purchase gates.
- Scarce strategic resources: session time, concealment and sound discipline;
  ammunition, shield charge and health; loadout, backpack and protected slots;
  extraction access; weapon durability; retained ingredients and skill points.
- Claim IDs: `ARC-002`–`ARC-010`.

### Information Genes

- Existing genes: `INF-075`, health, protection and durability; `INF-115`,
  partial local hostile sight and sound; `INF-128`, loot and inventory
  compatibility; `INF-132`, crafting dependencies.
- New genes: `INF-137`, current map, condition, extraction and time; `INF-138`,
  value, compatibility and defeat protection; `INF-139`, ARC attention,
  telegraphs and components; `INF-140`, retained/lost items and rewards.
- Claim IDs: `ARC-003`–`ARC-010`.

### Objective Genes

- Existing gene: `OBJ-021`, secure accumulated expedition resources.
- Evaluation: extraction is a successful banking decision rather than a fixed
  loot quota; knockout is a failed unsecured settlement but can still return
  a deliberately protected item and persistent XP.
- Claim IDs: `ARC-003`, `ARC-007`, `ARC-008`.

### Time Genes

- Existing gene: `TIM-003`, real-time input during forced progression.
- Parameters: matchmaking boundary, live raid clock, search and medical
  durations, ARC telegraphs, extraction arrival and closure, DBNO and knockout.
- Claim IDs: `ARC-003`–`ARC-008`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Solo queue is selected and no retained gear is staked | Accept Free Loadout and ready | A smaller randomized compatible kit becomes the raid inventory | Entry risk and capacity are chosen before matchmaking | `ARC-002` |
| Closed ordinary container is reachable | Hold search without moving or changing equipment | Completion reveals sampled contents; interruption leaves them unrevealed | Discovery and transfer are separate timed decisions | `ARC-003`, `ARC-006` |
| Valuable eligible loot is in the backpack and one pocket slot is free | Move it into the Safe Pocket | The item keeps its identity but changes its defeat-retention partition | Protection is positional and capacity-bounded | `ARC-008` |
| ARC has no current target and the Raider emits a visible or audible cue | Move, fire or cross its perception | The machine may acquire and route toward the Raider, then telegraph its typed attack | PvE pressure follows local information | `ARC-004` |
| Weapon, ammunition and target are legal | Aim and fire at armour or a vulnerable component | Live combat applies weapon state and hit location while durability declines | Weak-point choice trades ammunition, exposure and salvage | `ARC-005` |
| Carried materials match a known Field recipe | Queue one item or recycle an owned object | Ingredients become the declared field output, or the item becomes components | Loot can be converted before settlement | `ARC-009` |
| An enabled extraction is reachable before closure | Call or unlock it and enter its departure zone | Session closes successfully and ordinary carried state returns to Speranza | Extraction converts temporary possession into persistent ownership | `ARC-006`, `ARC-007` |
| Equivalent inventory exists but the Raider reaches knockout first | Allow health and DBNO recovery to fail | Ordinary loadout and scavenged items are forfeited; valid pocket contents return | Loss and Safe Pocket retention form one partition | `ARC-007`, `ARC-008` |
| Extracted ingredients and a known station recipe exist | Craft, sell, recycle, repair or upgrade one legal item | Persistent inventory, coins, durability or equipment state changes | Raid yield feeds the next loadout rather than ending at a score | `ARC-009` |
| Awarded XP crosses a level threshold | Spend the resulting point on an eligible tree node | The chosen persistent modifier applies to later raids | Activity becomes player-directed metaprogression | `ARC-010` |

## Strategic and experiential structure

- Local decision: move quietly or quickly; search under exposure; shoot armour
  or a weak point; fight, signal neutrality or disengage from another Raider;
  pocket one item; heal, field-craft or route toward extraction.
- Medium-term planning: value every slot against likely sale, recipe and quest
  use; preserve ammunition, shield and durability; approach a live extraction
  with enough time and alternate cover; decide when expected upside no longer
  justifies the unsecured stake.
- Long-term structure: repeated extraction turns volatile Topside possession
  into stash, recipes, stations, repaired gear and skills that reshape later
  risk budgets without removing knockout loss.
- Common heuristics: stake Free Loadout while poor, protect the smallest
  high-leverage item, search from cover, treat gunfire as information broadcast,
  leave before every slot is perfect and spend extracted materials on a
  reproducible next kit rather than hoarding unusable value.
- Failure attribution: visible loadout, inventory protection, local audio,
  machine telegraphs and result settlement explain most losses; hidden loot,
  other Raiders and sampled session state preserve consequential uncertainty.
- Claim IDs: `ARC-002`–`ARC-010`.

## Replay and variation

- What changes: Free Loadout, insertion, participant behaviour, ARC placement,
  containers, loot and durability, extraction route, combat, secured item,
  extracted value and chosen persistent upgrade.
- Randomness or procedural generation: authored maps receive sampled session
  population, loot and ARC state under the currently scheduled condition.
- Multiple viable strategies: stealth scavenging, selective ARC hunting,
  opportunistic PvP, cooperative signalling, early low-risk extraction or
  deeper high-value routing.
- Typical replay motive: convert a different risk profile into useful retained
  state and test how workshop and skill choices alter the next raid.
- Claim IDs: `ARC-001`–`ARC-010`.

## Adjacent systems and history

- PUBG: BATTLEGROUNDS is nearest because both combine direct firearm combat,
  partial local information, sampled loot, constrained loadouts, live healing
  and terminal Solo defeat. ARC Raiders replaces last-survivor victory and a
  contracting safe zone with discretionary extraction, Safe Pocket loss
  partition and persistent Workshop progression.
- Rust shares retained crafting, durability, looting and adversarial real-time
  risk, but its persistent shared world, building authority and scheduled wipe
  replace ARC Raiders' bounded session and explicit extraction settlement.
- Project Zomboid shares vulnerable looting, crafting, body pressure and local
  sound, but one irreversible character life replaces repeatable raids that
  deliberately transfer selected state into a safe persistent hub.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-123`, `ACT-161`, `ACT-164`, `ACT-199`, `ACT-200`, `ACT-215`–`ACT-221` | bindings, item identities and Free Loadout contents are parameters |
| System Behaviour | `SYS-215`, `SYS-223`, `SYS-319`, `SYS-328`, `SYS-346`–`SYS-354` | numeric balance and session seed are parameters |
| Constraint | `CON-210`, `CON-284`–`CON-286`, `CON-290`, `CON-315`–`CON-322` | slot counts, costs and timings are parameters |
| Information | `INF-075`, `INF-115`, `INF-128`, `INF-132`, `INF-137`–`INF-140` | HUD placement is presentation |
| Objective | `OBJ-021` | acceptable extracted value is strategic, not a fixed quota |
| Time | `TIM-003` | exact durations are versioned parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `142` (`GAME-0001`–`GAME-0142`).
- Exact genome matches: none.
- Tied near matches: `GAME-0140` — PUBG: BATTLEGROUNDS (`15 / 77 = 0.194805`).
- Supported combination subsets: `COMB-0141`.
- Scan date: 2026-08-21.

### Selected-neighbour interpretation

No pre-migration reviewed selected-neighbour table row exists for: `GAME-0140`.

### Preserved research notes

- New genes: `ACT-215`–`ACT-219`, `ACT-221`, `SYS-346`–`SYS-350`,
  `SYS-352`–`SYS-354`,
  `CON-315`–`CON-322`, `INF-137`–`INF-140`.
- Classification result: new verified combination of reused and new genes.
- Evidence and reasoning: the distinctive boundary is not shooting or looting
  alone. It is the explicit terminal partition that converts one live shared
  raid into persistent extracted state, forfeited unsecured state and protected
  pocket state, then feeds the retained branch into workshop and skill choices.

## Taxonomy impact

- Registry changes after normalisation: 26 new bounded genes and `COMB-0141`;
  `ACT-191` and `SYS-299` are reused.
- Taxonomy-change record: `TAXONOMY_CHANGE_012` and `TAXONOMY_CHANGE_013`.
- Candidate terms affected: none.

## Negative results

- No separate negative-result record. The exhaustive scan found no exact
  genome and no earlier registered combination that is a proper subset.
