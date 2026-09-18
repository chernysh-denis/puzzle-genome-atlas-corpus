---
game_id: GAME-0301
slug: divinity-original-sin-2-definitive-edition
game_title: "Divinity: Original Sin 2 - Definitive Edition"
analysis_status: reviewed
reviewed: 2026-09-18
combination_ids: []
gene_ids:
  action:
    - ACT-019
    - ACT-048
    - ACT-089
    - ACT-096
    - ACT-199
    - ACT-232
    - ACT-341
  system:
    - SYS-061
    - SYS-356
    - SYS-379
    - SYS-875
    - SYS-876
  constraint:
    - CON-269
    - CON-638
  information:
    - INF-073
    - INF-128
    - INF-343
  objective:
    - OBJ-113
  time:
    - TIM-001
---

# Game: Divinity: Original Sin 2 - Definitive Edition

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Enemy health,
Action Point costs and loot are parameters, not separate genes.

## Analysis scope

- Version / ruleset: the Windows Steam base product `435150`, Definitive
  Edition rules, fresh single-player Classic campaign, with every Gift Bag
  feature disabled. The publisher dates Definitive Edition to 2018-08-31;
  the installed Windows build was not observed. Sir Lora and Divine
  Ascension extras are outside this packet.
- Structured analysis target: the Windows base-product entry in
  `knowledge/platforms/games.json`; no inference about other platforms.
- Primary decision loop: move the one selected origin character through the
  Merryweather tutorial; place two crates on paired tutorial pressure
  plates, collect and equip a weapon, follow the authored ship dialogue and
  disaster, then take turns against the two main-deck Voidlings. On each
  combat turn compare visible order and Action Points, spend AP on reachable
  movement or a legal attack, and use the upper-deck water-barrel/fire lesson before
  committing the lifeboat escape to the Fort Joy beach.
- Entry and exit: confirm Ifan ben-Mezd as the one origin character with the
  unchanged Wayfarer preset and enter the new Classic campaign. Exit after
  the immediate lifeboat branch reaches first controllable Fort Joy beach
  state, before any beach encounter or recruitment. The selection packet
  proposed a beach autosave and reload check; no installed game or save was
  available, so neither autosave firing nor retained post-reload fields are
  claimed as observed. This narrows the verified terminal, not the recorded
  future direct-play question.
- Included: the Definitive Edition's additional tutorial deck, paired
  pressure-plate object lesson, the first inventory/equipment step, Siwan/Payde and
  Windego's opening quest sequence, one environmental fire/water lesson,
  the mandatory two-Voidling main-deck fight, AP-limited initiative turns,
  and the immediate lifeboat branch. The other origin characters are present
  but cannot join the party aboard the ship.
- Excluded: a lower-deck rescue return, optional murder investigation,
  Persuasion gate, extra fights, Fort Joy beach fights or recruitment, later
  quests and acts, co-op, Arena, Game Master, Gift Bags, Workshop mods and
  extras. Physical and magic armour, armour-gated status, multi-member party
  positioning and advanced elemental combinations are not admitted: the
  scoped two Voidlings are reported without armour, and no such interaction
  is necessary before the beach terminal.
- Potential scoped modules: verify the exact current Windows build, first
  beach autosave and reload, fixed-preset inventory after transition, and
  optional armour/status and party interactions through direct play before
  any signature expansion.
- Direct-play status: not conducted. No licensed Windows install, fresh save,
  capture or reload was available. Publisher material supports product and
  general tactical/solo rules; two written route references support the
  Definitive Edition deck and ship sequence. The route is source-bounded
  reconstruction, not an observed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `C-301-001` | Definitive Edition is the Windows base game's 2018 revision and supports a solo origin-character campaign. | Confirmed | Direct | High | Larian product/history; Steam product |
| `C-301-002` | Definitive Edition adds a separate tutorial deck with object, paired pressure-plate and item lessons before the established ship route. | Pattern | Corroborated | Medium | Guides4Gamers Hold map; Definitive Edition written walkthrough |
| `C-301-003` | The opening quest advances through Siwan/Payde, Windego's disaster, the middle deck and a main-deck fight against two Viscous Voidlings before an immediate lifeboat branch. | Pattern | Corroborated | Medium | Guides4Gamers quest/map; Definitive Edition written walkthrough |
| `C-301-004` | Combat participants act in visible initiative order and spend a refreshed per-character AP budget on movement and attacks; unspent AP may carry subject to the cap. | Pattern | Corroborated | Medium | PC Definitive Edition action-point guide; community mechanics reference |
| `C-301-005` | The upper deck permits water from a barrel to extinguish a local fire surface; this is a state change, not a spell or armour interaction. | Pattern | Limited | Medium | Definitive Edition written walkthrough; Guides4Gamers generic tutorial-surface note |
| `C-301-006` | The ship's two first main-deck Voidlings have no physical or magic armour in the cited Classic encounter; armour-status rules are not demonstrated by this fight. | Pattern | Limited | Medium | Definitive Edition written walkthrough; community creature reference |
| `C-301-007` | The other origins on the ship are future recruits, not controllable party members in this opening packet. | Pattern | Corroborated | Medium | Guides4Gamers Hold map |
| `C-301-008` | A first beach autosave retaining all requested fields after reload is unverified here. | Hypothesis | Limited | Low | Selection packet; no direct play |

## Basic data

- Release / origin: Larian Studios; Definitive Edition dated 2018-08-31 by
  the publisher, while the underlying game's original release was 2017.
- Platform or physical form: Windows Steam base product, app `435150`.
- Puzzle family: tactical forecast and counterplay; inventory and fixture
  dependencies; ordered dependency sequencing.
- Primary sources: [Larian product](https://divinity.com/original-sin-ii),
  [Larian history](https://divinity.com/original-sin-ii/history),
  [official Steam product](https://store.steampowered.com/app/435150/Divinity_Original_Sin_2_Definitive_Edition/),
  [Steam-hosted game manual](https://shared.fastly.steamstatic.com/store_item_assets/steam/apps/435150/manuals/DOS2_Game_Manual.pdf?t=1725653917)
  and [Larian Gift Bag explanation](https://forums.larian.com/ubbthreads.php?Number=656607&page=all&ubb=showflat).
- Secondary sources: [the Hold map](https://guides4gamers.com/divinity-original-sin-2/maps/the-hold/),
  [Troubled Waters quest](https://guides4gamers.com/divinity-original-sin-2/quests/troubled-waters/),
  [Definitive Edition Merryweather walkthrough](https://gamefaqs.gamespot.com/ps4/236378-divinity-original-sin-ii-definitive-edition/faqs/81674/chapter-1-the-merryweather),
  [PC Definitive Edition AP guide](https://gamefaqs.gamespot.com/pc/243225-divinity-original-sin-ii-definitive-edition/faqs/75293/action-points)
  and [Voidling creature reference](https://divinity.fandom.com/wiki/Viscous_Voidling).
- Claim IDs: `C-301-001`–`C-301-008`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-096`, select a reachable world destination rather than
  steer each footstep; `ACT-048`, move a portable crate or barrel; `ACT-089`,
  collect the tutorial weapon; `ACT-199`, equip it; `ACT-232`, commit a quest
  response; `ACT-341`, operate a door, stair or lifeboat; `ACT-019`, choose a
  combat ability and legal target. The two Voidlings do not require a second
  player-controlled unit.
- Candidate genes: none. A basic attack is represented by the selected unit
  ability/target commitment, not a real-time aimed strike.
- Parameters: Ifan, object, equipment slot, destination, response, target,
  range and AP cost.
- Claim IDs: `C-301-002`–`C-301-004`.

### System Behaviour Genes

- Existing genes: `SYS-061`, occupying each of two pressure plates sustains
  its required gate input;
  `SYS-356`, advance a visible initiative queue; `SYS-379`, retain the opening
  quest stage and lifeboat branch.
- New genes: `SYS-875`, refresh and carry a capped combatant AP balance at
  turn boundaries; `SYS-876`, turn upper-deck barrel-released water into a
  water surface and extinguish overlapping local fire.
- Resolution order: quest and deck state gate the next passage; combat
  initiative selects an actor; AP and range legality filter commands; attack
  and surface effects settle before the next decision; the lifeboat response
  advances the quest to beach control.
- Claim IDs: `C-301-002`–`C-301-005`.

### Constraint Genes

- Existing gene: `CON-269`, a targeted skill requires legal target, range,
  resources and readiness.
- New gene: `CON-638`, a combat turn cannot spend more AP than the acting
  character currently holds; movement distance and attack choice compete
  for that same budget. This is not Baldur's Gate 3's separate Action, Bonus
  Action and movement economy (`CON-343`).
- Scarce resources: turn AP, health, reachable deck positions and consumable
  or equipment availability; physical/magic armour is not active in this
  scoped encounter.
- Claim IDs: `C-301-004`, `C-301-006`.

### Information Genes

- Existing genes: `INF-073`, selected weapon and hotbar; `INF-128`, nearby
  loot and inventory compatibility.
- New gene: `INF-343`, ship-combat HUD shows acting character, visible
  initiative sequence, available AP and target health before committing a
  move or attack; it does not assert a Break gauge (`INF-141`).
- Claim IDs: `C-301-002`–`C-301-004`, `C-301-006`.

### Objective Genes

- Existing gene: `OBJ-113`, escape an authored captivity/disaster tutorial
  into first exterior-world control. The terminal is the Fort Joy beach,
  not victory over the later island campaign. The word retained denotes
  continuing campaign state, not an independently tested reload here.
- Claim IDs: `C-301-003`, `C-301-008`.

### Time Genes

- Existing gene: `TIM-001`, commit one combat command and let its movement,
  attack and environmental consequences settle before the next command.
  Exploration outside combat is not claimed to impose a live deadline.
- Claim IDs: `C-301-004`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Two tutorial crates and paired plates are available | Put a crate on each plate | Both occupied plates hold the required gate inputs; removing either body can close the passage | Objects can hold a gate state, not only become loot | `C-301-002` |
| A reachable weapon can be collected | Collect and equip it | Inventory and active weapon state change before the required fight | Loot and equipment are separate commitments | `C-301-002` |
| Siwan and Payde are present | Follow the offered opening responses | Registration leads to Windego's blast and the escape quest advances | Dialogue and world event gate later decks | `C-301-003` |
| An actor begins a main-deck combat turn | Move to a reachable point, then select an in-range attack | Each commitment spends its listed AP; unused AP is bounded at the later turn refresh | One common AP pool constrains movement and attack | `C-301-004` |
| Fire blocks part of the upper deck and a water barrel is available | Break or move the barrel so water reaches the fire | Water occupies the affected surface and the overlapping fire is extinguished | Environmental state can alter traversal | `C-301-005` |
| Two first main-deck Voidlings are active | Resolve the fight in initiative order | Both hostiles lose health and are removed; no armour break is necessary | The admitted fight does not demonstrate physical/magic armour | `C-301-003`, `C-301-006` |
| Main deck is clear and lifeboat is offered | Choose immediate departure | The authored ship disaster resolves to first Fort Joy beach control | Bounded opening escape reaches exterior state | `C-301-003`, `C-301-008` |

## Strategic and experiential structure

- Local decision: choose reachable deck position and combat target while
  preserving enough AP for the next useful command.
- Medium-term planning: use a movable object to hold a gate; equip a found
  weapon; use water/fire surface state before committing the lifeboat branch.
- Long-term structure: complete the Merryweather escape and stop at first
  Fort Joy beach control. No later origin quest or four-member party is in
  this signature.
- Failure attribution: a blocked pressure plate closes its linked gate; an
  illegal range or AP deficit rejects an attack; losing all health requires
  recovery outside the observed route.
- Player trust: an unplayed Windows build and untested autosave/reload are
  disclosed rather than presented as measured results.
- Claim IDs: `C-301-002`–`C-301-008`.

## Replay and variation

- Fixed for this packet: Ifan, unchanged preset, Classic, disabled Gift Bags,
  immediate lifeboat branch and terminal before beach exploration.
- Variable parameters: attack sequence, movement path, loot choice and AP
  left at turn end. The source record does not prove a random seed.
- Excluded variants: rescuing the other origins below deck and recruiting
  them later; the map notes that they cannot join aboard the ship.
- Claim IDs: `C-301-003`, `C-301-004`, `C-301-007`.

## Adjacent systems and history

- Baldur's Gate 3 also combines authored dialogue and turn-based tactics,
  but its distinct Action/Bonus Action/movement economy and concentration
  are not Divinity's shared AP pool.
- XCOM 2 schedules squad actions by mission turns; this one-character ship
  encounter has no controllable squad or cover-flanking claim.
- The Definitive Edition tutorial deck is not interchangeable with the
  original 2017 release's opening; later Gift Bag toggles are explicitly off.
- Claim IDs: `C-301-001`–`C-301-004`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-019`, `ACT-048`, `ACT-089`, `ACT-096`, `ACT-199`, `ACT-232`, `ACT-341` | Target, crate, loot, path and response |
| System Behaviour | `SYS-061`, `SYS-356`, `SYS-379`, `SYS-875`, `SYS-876` | Plate, turn refresh, water/fire and quest state |
| Constraint | `CON-269`, `CON-638` | Range, readiness and pooled AP |
| Information | `INF-073`, `INF-128`, `INF-343` | Hotbar, loot and combat HUD |
| Objective | `OBJ-113` | First beach control after escape |
| Time | `TIM-001` | Command then settled consequences |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `300` (`GAME-0001`–`GAME-0300`).
- Exact genome matches: none.
- Tied near matches: `GAME-0221` — World of Warcraft (`6 / 38 = 0.157895`); `GAME-0240` — Kingdom Come: Deliverance II (`6 / 38 = 0.157895`).
- Supported combination subsets: none.
- Scan date: 2026-09-18.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0221` — World of Warcraft | `ACT-199`, `ACT-341`, `SYS-379`, `CON-269`, `INF-073`, `INF-128` | Both equip found gear, interact with authored objects and advance a quest, but World of Warcraft's Exile's Reach Warrior develops through live combat, ability acquisition and a follower-filled dungeon; this ship packet uses one actor's pooled AP and a short turn-based escape. | Near, `0.157895` |
| `GAME-0240` — Kingdom Come: Deliverance II | `ACT-048`, `ACT-199`, `ACT-232`, `ACT-341`, `SYS-379`, `INF-073` | Both move an object, equip gear, choose dialogue and advance an opening route; Kingdom Come's embodied timed recipe/recovery work does not have initiative, a shared turn AP pool or water/fire tutorial transformation. | Near, `0.157895` |

## Taxonomy impact

- Registry changes: four new bounded Active definitions; existing definitions
  and earlier signatures remain unchanged.
- Taxonomy-change record: none; prospective game addition.
- Candidate terms: ship AP refresh/carry, AP legality, local water/fire
  transformation and battle resource display.

## Negative results

- `CON-343` is BG3's separate Action/Bonus Action/movement budget, not
  Divinity's pooled AP. `INF-141` requires a Break gauge absent here.
  `SYS-389` bundles concentration and spell-slot effects not exercised on
  this route. The two armour types and party switching are deliberately
  excluded rather than inferred from the later game.

## Delta summary

## New facts

- [Pattern | Corroborated | Medium] The Definitive Edition tutorial deck and
  Merryweather escape form a bounded first exterior-control route.

## New genes

- [Pattern | Corroborated | Medium] Four boundaries distinguish pooled AP,
  environmental water/fire change and their decision-visible state.

## New combinations

- [Pattern | Limited | Medium] The deterministic subset scan finds no
  verified combination fully contained in this ship-opening signature.

## Taxonomy changes

- [Pattern | Corroborated | Medium] No earlier definition or game signature
  changes.

## New questions

- Does a clean current Windows Classic run create a beach autosave that
  retains Ifan's equipment, quest, dialogue and tutorial state after reload?
- Is the selected tutorial pressure-plate and water-barrel route identical on
  the current Windows build with all Gift Bags disabled?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0302` Captain Toad: Treasure Tracker,
  original Wii U edition, as recorded in the platform-amended selection.
- Optimisation criterion: move from turn/AP tactics to compact spatial
  routing without expanding this game's later-act scope.
- Backlog impact: no later subject reordered.

## Why this game

- [Hypothesis | Limited | Medium] The source-bounded ship opening tests the
  portability of turn order, pooled AP and object/surface dependencies while
  leaving armour and full-party systems for evidence that actually exercises
  them.
