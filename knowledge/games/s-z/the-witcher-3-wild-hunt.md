---
game_id: GAME-0205
slug: the-witcher-3-wild-hunt
game_title: "The Witcher 3: Wild Hunt"
analysis_status: reviewed
reviewed: 2026-08-31
combination_ids:
  - COMB-0203
gene_ids:
  action:
    - ACT-008
    - ACT-107
    - ACT-123
    - ACT-131
    - ACT-161
    - ACT-190
    - ACT-199
    - ACT-223
    - ACT-232
    - ACT-245
    - ACT-370
  system:
    - SYS-215
    - SYS-379
    - SYS-405
    - SYS-680
  constraint:
    - CON-269
    - CON-282
    - CON-284
    - CON-357
    - CON-358
  information:
    - INF-073
    - INF-115
    - INF-119
    - INF-125
    - INF-128
    - INF-148
    - INF-265
  objective:
    - OBJ-127
  time:
    - TIM-003
---

# Game: The Witcher 3: Wild Hunt

## Analysis scope

- Version / ruleset: unmodified Windows Steam public Patch `4.04`, build
  `14504303` dated 2024-06-06, reviewed 2026-08-31; English base-game single
  player, fresh `New Game`, `Story and Sword!` difficulty, tutorials on,
  default gameplay options, simulated The Witcher 2 save off, no mods, no
  New Game+, and expansion/free-DLC content not entered.
- Primary decision loop: read the tracked objective, map and dialogue options;
  navigate to an informant or search area; hold Witcher Senses, follow a trail
  and inspect highlighted evidence; gather the required Buckthorn, prepare and
  equip the taught potion and crossbow, choose a sword/Sign/dodge response for
  the griffin, loot its trophy, then report the kill and choose the declared
  reward response.
- Entry and exit: entry is the first retained controllable Kaer Morhen tutorial
  frame after the fresh-game choice commits an empty-history save. Positive
  exit is retained controllable White Orchard state after `The Beast of White
  Orchard` is marked complete, the griffin trophy has been handed in, the
  declared `Take the coin` response has settled and `Lilac and Gooseberries`
  resumes as the tracked main quest. Stop before the White Orchard tavern
  incident or departure for Vizima. Death followed by abandoning the route is
  failure; merely killing the griffin before the captain's settlement is not a
  terminal.
- Included: the required opening tutorial and road combat; White Orchard
  inquiry needed to reach the Nilfgaardian captain; the captain, Mislav and
  Tomira conversations; the attacked camp, tracks, griffin nest and corpse
  clues; Witcher Senses; Buckthorn gathering; the taught Thunderbolt brew and
  one equipped/consumed dose; the received crossbow; silver-sword, Sign,
  crossbow and dodge choices in the royal-griffin fight; trophy looting;
  quest/map/inventory/bestiary/HUD information; the final captain dialogue and
  ordinary coin reward.
- Excluded: Gwent, notice-board tasks, optional treasure, Places of Power,
  unrelated side quests and contracts; wandering or levelling beyond what the
  fixed route incidentally causes; equipment crafting/upgrading outside the
  taught potion; merchants, alchemy experimentation and monster farming;
  post-terminal tavern combat, Vizima and the search for Ciri; Hearts of Stone,
  Blood and Wine, all free-DLC quests/items, New Game+, My Rewards,
  cross-progression, Photo Mode, mods, REDkit, Workshop content, console
  commands, achievements, multiplayer, the announced 2026 Remastered release
  and 2027 Songs of the Past expansion.
- Potential scoped modules: another named contract, one Gwent match, one
  alchemy/equipment progression packet, one major choice branch, either
  expansion or the future Remastered edition each requires a separately fixed
  version, entry and terminal.
- Direct-play status: no authenticated current Windows play was performed.
  Official patch, build, manual and product evidence establish the executable,
  controls and base systems; five current or stable walkthrough traces
  corroborate the ordered quest boundary. The transition table is repository
  rules reasoning, not a direct-play claim.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `W3-001` | Patch `4.04` / public build `14504303` is the reviewed current Windows Steam boundary | Confirmed | Corroborated | High | P1, P2, S1 |
| `W3-002` | The official base rules expose two swords, Signs, potions/oils, crossbow, Witcher Senses, dodge/roll, stamina, toxicity and tracked quest information | Confirmed | Direct | High | P3, P4 |
| `W3-003` | The Beast of White Orchard is a base-game main quest whose ordered captain, Mislav, Tomira and Vesemir steps precede the griffin fight | Observation | Corroborated | High | S2, S3, S4, S5 |
| `W3-004` | Witcher Senses highlight local clues and tracks whose inspection advances the authored investigation | Observation | Corroborated | High | P3, S2, S3 |
| `W3-005` | Buckthorn and the trophy are reachable finite yields required at different quest gates | Observation | Corroborated | High | S2, S4, S5 |
| `W3-006` | The preparation route teaches Thunderbolt and equips the newly supplied crossbow before the griffin fight | Observation | Corroborated | High | S2, S3 |
| `W3-007` | Real-time griffin combat couples weapon, Sign, crossbow, dodge, vitality and stamina/toxicity information | Confirmed | Corroborated | High | P3, P4, S2 |
| `W3-008` | Looting the Griffin Trophy and reporting to the captain are required after the kill | Observation | Corroborated | High | S2, S3, S4, S5 |
| `W3-009` | Choosing the declared coin response completes The Beast of White Orchard and resumes Lilac and Gooseberries with retained control | Observation | Corroborated | High | S2, S3, S5 |
| `W3-010` | The announced Remastered edition and Songs of the Past are future products outside build `14504303` | Confirmed | Direct | High | P5, P6 |

## Basic data

- Release / origin: CD PROJEKT RED; Windows PC release 2015, reviewed at
  Patch `4.04` / build `14504303` in 2026.
- Platform or physical form: third-person real-time open-world action role-
  playing game on Windows; one base-game White Orchard main-quest packet is
  scoped.
- Puzzle family: environmental observation and clue chaining; ordered
  dependency sequencing; resource preparation; tactical forecast and
  counterplay; real-time system pressure.
- Primary and official sources:
  - **[P1]** [official Patch 4.04 announcement](https://www.thewitcher.com/ch/it/news/48553/la-patch-4-04-e-disponibile-per-tutte-le-piattaforme-inclusa-nintendo-switch),
    for the current named patch lineage and a White Orchard quest checkpoint
    fix.
  - **[P2]** [official June 2024 hotfix notes](https://steamcommunity.com/ogg/292030/announcements/detail/4187860062629159882),
    for the later PC hotfix associated with the reviewed public build.
  - **[P3]** [official Windows PC manual](https://cdn-l-thewitcher.cdprojektred.com/media/TW3/Pdf/Manuals/PC/The_Witcher_3_Wild_Hunt_Game_Manual_PC_EN.pdf),
    for controls, Witcher Senses, Signs, swords, crossbow, consumables, HUD,
    stamina, toxicity, objectives and tracked-quest information.
  - **[P4]** [official product page](https://www.thewitcher.com/us/en/witcher3),
    for monster hunting, preparation with elixirs/oils and consequence-bearing
    choices in the current base title.
  - **[P5]** [official Remastered announcement](https://www.thewitcher.com/pl/en/news/52017/announcing-the-witcher-3-wild-hunt-remastered),
    for the future 2026-09-29 release boundary.
  - **[P6]** [official Songs of the Past announcement](https://www.thewitcher.com/us/en/news/52016/a-look-at-the-witcher-3-wild-hunt-songs-of-the-past),
    for the separate future 2027 expansion boundary.
- Reproducible mechanics sources:
  - **[S1]** [SteamDB public build record](https://steamdb.info/patchnotes/14504303/),
    for build `14504303`, dated 2024-06-06.
  - **[S2]** [Game8 current quest trace](https://game8.co/games/Witcher3/archives/275498),
    for camp clues, tracks, nest, Buckthorn, Vesemir, crossbow, trophy, captain
    report and coin-choice completion.
  - **[S3]** [GameBanshee quest trace](https://www.gamebanshee.com/thewitcher3/walkthrough/thebeastofwhiteorchard.php),
    for the ordered investigation, preparation, fight and settlement.
  - **[S4]** [GamePressure quest trace](https://www.gamepressure.com/thewitcher3/the-beast-of-white-orchard/z577cd),
    for the Mislav/Tomira branches, required objects and quest conclusion.
  - **[S5]** [Guides4Gamers quest trace](https://guides4gamers.com/witcher-3-wild-hunt/quests/the-beast-of-white-orchard/),
    for the retained quest-state sequence and final report.
- Claim IDs: `W3-001`–`W3-010`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, navigate the controlled witcher; `ACT-107`, ask
  an authored character for an operational fact; `ACT-123`, brew the known
  Thunderbolt recipe; `ACT-131`, consume one equipped dose; `ACT-161`, strike
  the reachable griffin; `ACT-190`, cast a selected Sign; `ACT-199`, equip
  compatible inventory gear; `ACT-223`, choose a timed dodge or parry response;
  `ACT-232`, commit the captain's final reward response; `ACT-245`, gather
  Buckthorn or loot the eligible trophy yield.
- New gene: `ACT-370`, focus Witcher Senses and inspect one highlighted clue or
  follow its exposed trail.
- Parameters: route, character, dialogue option, clue, trail, recipe, material,
  potion, toxicity, equipment slot, sword, crossbow, Sign, stamina, target,
  dodge timing, trophy and reward response.
- Claim IDs: `W3-002`–`W3-009`.

### System Behaviour Genes

- Existing genes: `SYS-215`, resolve directly commanded real-time hostile
  combat; `SYS-379`, advance authored quest state from completed objectives and
  dialogue choices; `SYS-405`, settle the completed hunt into reward and
  retained quest completion.
- New gene: `SYS-680`, convert the ordered examination of highlighted clues
  into retained investigation facts, new search areas, bestiary knowledge and
  the next authored objective.
- Resolution order: start the fixed fresh-game tutorial state; advance the
  required road and White Orchard objectives; retain dialogue facts; expose
  and settle each clue; gather Buckthorn; brew/equip the taught preparation;
  instantiate the griffin fight; exchange attacks, Signs, shots and evasions in
  real time; mark defeat; yield the trophy; validate its hand-in and final
  response; settle reward, quest completion and resumed retained control.
- Parameters: quest stage, dialogue flag, search area, clue order, track,
  bestiary entry, inventory, recipe, equipment, target health, stamina,
  toxicity, hit, defence, defeat, trophy, reward and completion flag.
- Claim IDs: `W3-002`–`W3-009`.

### Constraint Genes

- Existing genes: `CON-269`, Signs require sufficient stamina and legal
  readiness/target state; `CON-282`, authored quest steps require their ordered
  prior dialogue, discovery, item and location gates; `CON-284`, carry weight
  and typed equipment slots bound inventory use; `CON-357`, brewing requires a
  known recipe and ingredients; `CON-358`, Buckthorn and trophy extraction
  require reachable eligible finite sources.
- Scarce strategic resources: vitality, stamina, toxicity capacity, potion
  dose, inventory weight, equipped quick slots, crossbow bolts, preparation
  materials, combat space and timing.
- Claim IDs: `W3-002`–`W3-009`.

### Information Genes

- Existing genes: `INF-073`, show quick-slot and active equipment state;
  `INF-115`, expose the griffin through local sight, sound and effects;
  `INF-119`, show vitality, stamina, toxicity, experience and active status;
  `INF-125`, show explored map, tracked quest and authored objective markers;
  `INF-128`, show loot identity and inventory/equipment compatibility;
  `INF-148`, show available contextual dialogue responses.
- New gene: `INF-265`, Witcher Senses and the journal/bestiary expose
  highlighted local evidence, a followable trace and learned monster
  preparation information without revealing unexamined future clues.
- Claim IDs: `W3-002`–`W3-009`.

### Objective Genes

- New gene: `OBJ-127`, complete The Beast of White Orchard by satisfying its
  investigation and preparation gates, defeating the royal griffin, looting
  and handing in its trophy and settling the declared coin response.
- Success, evaluation and failure: success requires the quest-complete flag and
  retained control with Lilac and Gooseberries resumed. Death may restore an
  earlier checkpoint, but abandonment before the hand-in fails the bounded
  attempt. A kill, trophy or reward choice alone is insufficient.
- Claim IDs: `W3-003`–`W3-009`.

### Time Genes

- Existing gene: `TIM-003`, navigation, hazards, preparation use and hostile
  combat continue in real time; menu pauses and checkpoint restoration are
  presentation/attempt handling rather than a second admitted time model.
- Claim IDs: `W3-002`, `W3-006`, `W3-007`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Patch `4.04` / build `14504303` has no prior save history | Start the declared fresh `Story and Sword!` game | The opening reaches retained Kaer Morhen tutorial control | current bounded entry | `W3-001`, `W3-002` |
| White Orchard inquiry reaches the Nilfgaardian captain | Accept the griffin condition | The Beast of White Orchard tracks the hunter and herbalist leads | the named quest, not the whole prologue, owns the packet | `W3-003` |
| Mislav leads Geralt to the attacked camp | Hold Witcher Senses, inspect the clues and follow the footprints | Examined evidence advances the search to the nest and corpse conclusion | clue examination authors the target route | `W3-004` |
| Tomira names the required lure material | Enter the marked water and gather Buckthorn | The finite plant yield satisfies the preparation gate | navigation and material extraction are causally required | `W3-005` |
| Both investigation branches have settled | Return to Vesemir, brew/equip Thunderbolt and equip the supplied crossbow | The ambush/fight stage becomes available with the declared tools | evidence becomes monster-specific preparation | `W3-006` |
| The royal griffin is active at the lure site | Use the silver sword, crossbow, Signs and timed evasions while managing vitality, stamina and toxicity | Real-time exchanges reduce the target to defeat or Geralt to death/checkpoint restoration | preparation and combat meet in one live state | `W3-007` |
| The griffin is defeated | Loot the Griffin Trophy | The trophy enters carried quest state and the captain-report objective opens | the kill is necessary but not yet terminal | `W3-008` |
| The trophy is carried and the captain is reachable | Report the kill and choose `Take the coin` | Reward and quest-complete state settle; Lilac and Gooseberries resumes with retained control | system-authored positive terminal | `W3-009` |

## Strategic and experiential structure

- Local decision: choose a marked lead, align the sensory highlight with a
  reachable clue, equip one preparation, then time a strike, Sign, shot or
  evasion against the griffin's current approach.
- Medium-term planning: finish both clue/material branches and arrive with the
  taught potion, crossbow and usable combat resources rather than treating the
  boss as an isolated damage check.
- Long-term structure: turn conversation into a search region, physical clues
  into monster knowledge, knowledge into lure/preparation, and defeat into a
  trophy-backed contract settlement.
- Common heuristics: keep the quest tracked; sweep search areas slowly under
  Witcher Senses; inspect every highlighted mandatory clue; gather Buckthorn
  before returning to Vesemir; equip Thunderbolt and crossbow; preserve stamina
  for a defensive Sign; dodge lateral aerial attacks; do not stop at the kill.
- Failure attribution: objective markers identify the missing authored gate;
  sensory highlights identify unexamined evidence; inventory and journal expose
  preparation; vitality/stamina/toxicity and enemy health expose combat state;
  the trophy and captain dialogue expose settlement readiness.
- Player-trust factors: named objectives, bounded search areas, visible clue
  highlighting, explicit recipes and equipment slots, readable resource bars
  and a quest-complete transition make the packet auditable.
- Claim IDs: `W3-003`–`W3-009`.

## Replay and variation

- What changes between attempts: exploration line, exact clue-facing, gathered
  incidental herbs, equipped sword/Sign, potion timing, griffin attack order,
  damage taken, checkpoint reloads and combat duration.
- Randomness or procedural generation: authored quest people, places and gates
  remain fixed; combat sequencing and incidental open-world encounters vary.
- Multiple viable strategies: aggressive sword pressure, defensive Quen use,
  crossbow grounding and other legal Sign/evasion mixes can reach the same
  trophy and hand-in state.
- Typical replay motive: find the mandatory clues faster, prepare before the
  ambush, take less damage and settle the same quest with fewer reloads.
- Claim IDs: `W3-004`–`W3-009`.

## Adjacent systems and history

- Direct predecessors: the first two Witcher games share monster research,
  alchemy and consequence-bearing quests; their exact rules are not imported.
- Variants: another contract changes clues, target and settlement; difficulty,
  alternative final response, expansions and Remastered require separate
  ruleset qualification.
- Similar games: Monster Hunter Wilds shares target preparation, real-time
  combat and hunt settlement; Cyberpunk 2077 shares tracked open-world quests,
  equipment and authored dialogue; S.T.A.L.K.E.R. 2 shares a focused field-
  sensing action but detects anomalies/artifacts rather than interpreting an
  ordered authored crime scene.
- Important differences: the fixed Witcher packet makes authored forensic
  evidence and two informant branches prerequisites for a prepared boss fight,
  then requires a physical trophy hand-in before its retained terminal.
- Claim IDs: `W3-003`–`W3-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-107`, `ACT-123`, `ACT-131`, `ACT-161`, `ACT-190`, `ACT-199`, `ACT-223`, `ACT-232`, `ACT-245`, `ACT-370` | named characters, tools and response are parameters |
| System Behaviour | `SYS-215`, `SYS-379`, `SYS-405`, `SYS-680` | exact damage, reward and checkpoint values are parameters |
| Constraint | `CON-269`, `CON-282`, `CON-284`, `CON-357`, `CON-358` | resource amounts and search radii are parameters |
| Information | `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `INF-148`, `INF-265` | iconography and HUD placement are presentation |
| Objective | `OBJ-127` | named griffin, trophy and reward response are parameters |
| Time | `TIM-003` | exact cadence is a parameter |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `204` (`GAME-0001`–`GAME-0204`).
- Exact genome matches: none.
- Tied near matches: `GAME-0190` — The Elder Scrolls V: Skyrim Special Edition (`15 / 41 = 0.365854`).
- Supported combination subsets: `COMB-0203`.
- Scan date: 2026-08-31.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0190` — The Elder Scrolls V: Skyrim Special Edition | `ACT-008`, `ACT-131`, `ACT-161`, `ACT-190`, `ACT-199`, `SYS-215`, `SYS-379`, `CON-269`, `CON-282`, `INF-073`, `INF-115`, `INF-119`, `INF-125`, `INF-128`, `TIM-003` | Both are fresh-save open-world action-RPG routes with tracked authored gates, equipment, consumables, melee, magic and live combat. Skyrim's Helgen escape uses ancestry confirmation, one exclusive companion, physics fixtures, lock risk, stealth and a cave-exit terminal; this Witcher packet uses informants, sensory forensic clues, monster-specific preparation and a trophy hand-in before quest completion | Near, `15 / 41 = 0.365854` |

### Preserved research notes

- New genes: `ACT-370`, `SYS-680`, `INF-265` and `OBJ-127`.
- Reused genes: twenty-five lower IDs; no earlier reviewed signature changed.
- Classification result: `New gene` and `New combination of known and new genes`.
- Evidence and reasoning: generic traversal, dialogue, crafting, equipment,
  combat, quest-state and hunt-settlement boundaries remain reusable; focused
  clue interpretation and the exact White Orchard terminal remain new.

## Taxonomy impact

- Registry changes: four bounded Active genes and `COMB-0203`; no earlier
  reviewed game signature changes.
- Taxonomy-change record: none.
- Candidate terms affected: Witcher Senses, highlighted clue, authored trail,
  bestiary preparation, trophy hand-in and retained quest completion.

## Negative results

- The explicit quest-complete flag after the captain hand-in is used instead of
  inventing a White Orchard departure, Ciri search or character-level terminal;
  no selection amendment is needed.
- Steam's current Complete Edition storefront label does not import expansion
  content into this base-story packet.
- Remastered and Songs of the Past are announced future releases and are not
  evidence for build `14504303` mechanics.
- Horse travel, Gwent, shops, unrelated encounters and optional clues remain
  incidental parameters or exclusions because the fixed quest does not require
  their full systems.
- No prior combination is accepted from genre resemblance; strict subset
  support remains validator-owned.
