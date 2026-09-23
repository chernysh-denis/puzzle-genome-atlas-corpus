---
game_id: GAME-0362
slug: the-elder-scrolls-iii-morrowind
game_title: "The Elder Scrolls III: Morrowind"
analysis_status: reviewed
reviewed: 2026-09-22
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-107
    - ACT-199
    - ACT-232
    - ACT-238
    - ACT-341
  system:
    - SYS-004
    - SYS-342
    - SYS-379
    - SYS-993
  constraint:
    - CON-282
  information:
    - INF-073
    - INF-119
    - INF-125
    - INF-128
  objective:
    - OBJ-158
  time:
    - TIM-007
---

# Game: The Elder Scrolls III: Morrowind

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Character names,
places, factions, topics, classes, signs and quest identifiers are carrier
parameters rather than gene names.

## Analysis scope

- Version / ruleset: current unmodified English Windows Steam **Game of the
  Year Edition**, app `22320`, public Build ID `1510067`, checked 2026-09-22;
  keyboard/mouse, default difficulty and one fresh base-game route.
- Content boundary: the sold product includes `Morrowind`, `Tribunal` and
  `Bloodmoon`, but this packet loads the ordinary GOTY distribution without
  mods or OpenMW and does not enter, trigger or use either expansion's content.
- Reproducible character and route: create `Atlas`, male Dunmer, authored
  Warrior class and The Warrior birthsign; take the release papers, iron
  dagger and Apprentice's Lockpick; equip the lockpick and retry the declared
  level-1 tutorial chest until it opens or the finite tool is exhausted; take
  the Engraved Ring of Healing; accept Sellus Gravius's package and written
  directions; leave the Census and Excise Office; buy silt-strider travel from
  Seyda Neen to Balmora; ask Bacola Closcius for Caius Cosades's location;
  follow the retained directions; deliver the package; join the Blades; accept
  the level-below-four `200`-gold support; ask for orders and retain
  `Antabolis Informant`; then save and reload.
- Primary decision loop: inspect character, fatigue, inventory, journal, topic
  list and local map; move to a named actor or fixture; equip or transfer the
  needed item; ask a topic or choose a quest response; follow retained textual
  directions; risk a finite lockpick use against a hidden skill-weighted
  chance; advance the authored report chain and verify its retained result.
- Entry and exit: begins at `New Game` before character confirmation. It
  succeeds only after Caius has accepted the package, inducted Atlas as a
  Blades Novice, awarded the eligible `200` gold, exposed and started
  `Antabolis Informant`, returned control and reproduced that state after one
  manual save/reload. Merely reaching Balmora or finding Caius is insufficient.
- Included: name, race, sex, authored class and birthsign; statistics and
  fatigue; inventory/equipment; release papers; one finite Apprentice's
  Lockpick and one level-1 tutorial chest; journal, dialogue topics and written
  directions; the engraved ring; the package; direct walking; paid silt-
  strider travel; Seyda Neen, Balmora, South Wall Cornerclub, Bacola, Caius,
  Blades induction, support gold, first orders and manual save/load.
- Excluded: combat, spellcasting, persuasion, barter optimisation, theft,
  returning Fargoth's ring, side quests, levelling, custom-class construction,
  later Blades work, guilds, crime, disease, enchanting, alchemy, training,
  fast-travel networks beyond the one ride, Tribunal, Bloodmoon, console ports,
  OpenMW, mods, unofficial patches, console commands, exploits and endings.
- Potential scoped modules: one custom-class allocation, a combat-and-skill-
  progression packet, one later Blades investigation, one guild admission or
  one separately versioned expansion route.
- Direct-play status: no entitlement, installed depot, executable, save,
  input trace, screenshot, video or audio was obtained or inspected. Official
  product and manual evidence establish the current distribution and enduring
  rules; three independent written routes establish the scoped transitions.
  The repository control is a source-bounded reconstruction, not direct play.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `MW-001` | Steam app 22320 remains the Windows GOTY product containing Morrowind, Tribunal and Bloodmoon, with public Build ID 1510067 | Confirmed | Corroborated | High | P1, R1 |
| `MW-002` | A new character commits name, race, sex, class and birthsign before leaving the Census and Excise Office | Confirmed | Direct | High | P2 |
| `MW-003` | The Warrior preset fixes a persistent skill/attribute profile, while health, magicka and fatigue expose the character's current operating state | Confirmed | Direct | High | P2 |
| `MW-004` | A lockpick attempt uses Security, attributes, fatigue, pick quality and lock level in a hidden chance and consumes one tool use on every attempt | Confirmed | Direct | High | P2, P3 |
| `MW-005` | Dialogue topics register operational facts in the journal, and Sellus plus Bacola supply retained directions to Caius without an objective waypoint | Observation | Corroborated | High | P2, S1, S2, S3 |
| `MW-006` | The package is a carried quest item whose delivery settles `Report to Caius Cosades`, Blades induction and the eligible support award | Observation | Corroborated | High | S1, S2, S3 |
| `MW-007` | Asking Caius for orders after induction starts `Antabolis Informant`, providing a named retained successor rather than ending at faction membership | Observation | Corroborated | High | S1, S2, S3 |
| `MW-008` | Manual saving and loading restore character, inventory, faction, journal and quest state for a different continuation | Confirmed | Direct | High | P2 |
| `MW-009` | The repository control reproduces creation, finite lock attempts, information acquisition, delivery, induction, successor and reload invariants without executing the game | Observation | Direct | High | V1 |

## Basic data

- Release / origin: Bethesda Game Studios and Bethesda Softworks; original
  Morrowind released in 2002, while the current Steam listing is the Windows
  Game of the Year Edition containing the two expansions.
- Platform or physical form: one licensed English Windows Steam installation;
  the structured authority is `knowledge/platforms/games.json`.
- Puzzle family: knowledge and evidence progression; inventory and fixture
  dependencies; ordered dependency sequencing.
- Primary sources:
  - **[P1]** [official Steam product page](https://store.steampowered.com/app/22320/The_Elder_Scrolls_III_Morrowind_GOTY_Edition/),
    for current title, Windows product, single-player form, developer,
    publisher and included GOTY content.
  - **[P2]** [official PC GOTY manual](https://steamcdn-a.akamaihd.net/steam/apps/22320/manuals/mwgoty_pcmanual.pdf?t=1498138106),
    for character creation, classes, birthsigns, attributes, fatigue, HUD,
    inventory/equipment, dialogue topics, journal, travel, lockpicking and
    save/load semantics.
  - **[P3]** [official Bethesda lockpick support](https://help.bethesda.net/app/answers/detail/a_id/17578/),
    for equipped lockpick use against a highlighted lock.
- Distribution and independent route sources:
  - **[R1]** [SteamDB depots](https://steamdb.info/app/22320/depots/), for
    public Build ID `1510067`, base executable/content and language-depot
    separation; this is distribution observation, not a publisher claim.
  - **[S1]** [StrategyWiki arrival route](https://strategywiki.org/wiki/The_Elder_Scrolls_III%3A_Morrowind/Arriving_at_Morrowind),
    for release papers, tutorial pickups, ring, Sellus package and travel.
  - **[S2]** [Report to Caius Cosades route](https://elderscrolls.fandom.com/wiki/Report_to_Caius_Cosades),
    for Balmora, South Wall directions, package delivery, rank, support and
    the next orders.
  - **[S3]** [GameBanshee Seyda Neen reference](https://www.gamebanshee.com/morrowind/locations/seydaneen.php),
    independently corroborating Sellus, Caius and silt-strider routing.
  - **[V1]** repository-side transition control derived from the declared
    sources; executable rules reasoning, not direct play.
- Claim IDs: `MW-001`–`MW-009`.

## Mechanical decomposition

### Action Genes

- Existing genes: `ACT-008`, directly walk the character; `ACT-107`, acquire
  retained directions and topic facts through authored dialogue; `ACT-199`,
  transfer the ring, package and lockpick and equip the tool; `ACT-232`, accept
  faction induction and first orders; `ACT-238`, commit the race/class/sign
  campaign character; `ACT-341`, address the chest, transport and other
  currently legal world interactions.
- Candidate genes: none. Selecting paid travel remains a contextual dialogue/
  interaction parameter; a lock attempt uses the same addressed-world-object
  input and differs in automatic resolution.
- Parameters: character choices, actor, topic, direction fact, item, target,
  lockpick, chest, transport destination, response and quest flag.
- Claim IDs: `MW-002`, `MW-004`–`MW-009`.

### System Behaviour Genes

- Existing genes: `SYS-004`, choose the hidden success/failure outcome;
  `SYS-342`, successful admitted Security use may advance its retained skill;
  `SYS-379`, convert package delivery, induction and orders into persistent
  authored quest/faction state.
- New gene: `SYS-993`, resolve one equipped consumable lock tool from current
  skill, supporting attributes, fatigue, tool quality and lock level, consume
  one use, then either open the lock or retain failure.
- Resolution order: character confirmation writes the initial profile; Sellus
  transfers package and directions; topic exchange adds facts; travel and
  walking reach Caius; package delivery removes the carried item and advances
  faction/quest flags; induction and first orders expose the named successor;
  save/load reproduces the resulting state.
- Parameters: build, skill, attributes, fatigue, tool quality, lock level,
  random draw, use count, package, faction rank, reward and successor quest.
- Claim IDs: `MW-002`–`MW-009`.

### Constraint Genes

- Existing gene: `CON-282`, creation, release, package acquisition, Balmora
  arrival, location fact, package delivery, induction and orders must occur in
  their authored predecessor order.
- Candidate genes: none. The equipped tool, positive uses and addressed lock
  are parameters of `SYS-993` and the contextual interaction, not a separate
  cross-game legality boundary in this packet.
- Scarce strategic resources: remaining lockpick uses, fatigue during a chance
  check, money for transport and the carried package; only the package and
  authored order are terminal-critical.
- Claim IDs: `MW-004`–`MW-007`, `MW-009`.

### Information Genes

- Existing genes: `INF-073`, expose active equipment; `INF-119`, expose race,
  class, sign, attributes, skills and three personal resources; `INF-125`,
  retain explored local map, journal entries, quest facts and current authored
  gate without importing a modern objective waypoint; `INF-128`, expose item
  identity, quantity, quality, condition/use stock and carried load.
- Candidate genes: none. Topic text and written directions are parameters of
  the existing authored-mission information boundary.
- Claim IDs: `MW-002`–`MW-008`.

### Objective Genes

- Existing gene: `OBJ-158`, settle one conversation/examination/check-gated
  opening episode into retained successor access. The optional tutorial chest
  demonstrates the chance system but is not required to deliver the package.
- Candidate genes: none.
- Success, evaluation and failure: success requires package removal, Blades
  Novice rank, eligible gold award, active `Antabolis Informant`, returned
  control and reload parity. Exhausting the tutorial pick is a recoverable
  demonstration failure; losing the package or abandoning the save fails the
  declared terminal.
- Claim IDs: `MW-006`–`MW-009`.

### Time Genes

- Existing gene: `TIM-007`, restore a manual save and permit a replacement
  continuation from the retained faction/quest boundary.
- Candidate genes: none. Ordinary walking animation and ambient world time do
  not create a forced progressing decision interval in this non-combat packet.
- Claim IDs: `MW-008`, `MW-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Clean main menu | choose `New Game` | character creation begins without prior retained state | exact entry | `MW-001`, `MW-002` |
| Creation is active | commit Atlas, male Dunmer, Warrior and The Warrior | one persistent starting profile is written | race/class/sign affect play, not cosmetics alone | `MW-002`, `MW-003` |
| Release process is incomplete | finish the papers and take admitted tutorial items | direct control, inventory and release sequence advance | authored onboarding precedes open movement | `MW-002`, `MW-005` |
| Level-1 chest is locked and the Apprentice's Lockpick has uses | equip the pick and activate the chest | one hidden skill-weighted draw consumes one use; success opens, failure leaves it locked | probabilistic finite-tool resolution differs from Skyrim's angular probe | `MW-004` |
| Engraved Ring of Healing is in the barrel | take it without completing Fargoth's side quest | the item enters inventory; the excluded side quest remains unresolved | optional pickup does not expand terminal scope | `MW-005` |
| Sellus is available and release prerequisites hold | ask the admitted topics and accept the order | package and written directions enter inventory/journal | facts and carried authority are separate | `MW-005`, `MW-006` |
| Atlas has left the office | buy travel from Seyda Neen to Balmora | money is paid and the character arrives at the offered destination | one transport interaction compresses the geographic route | `MW-005` |
| Caius's exact house is not yet known | ask Bacola at South Wall | the dialogue topic records precise directions | authored conversation changes later navigation knowledge | `MW-005` |
| Atlas carries the package and reaches Caius | report and deliver it | package is removed; report quest, faction offer and support become available | delivery is a quest-state gate | `MW-006` |
| Caius offers induction | join the Blades and accept eligible support | Atlas becomes Blades Novice and receives 200 gold at level 1 | faction membership and resource result persist | `MW-006` |
| Atlas is a Blades Novice | ask Caius for orders | `Antabolis Informant` starts and ordinary control returns | named successor access closes the packet | `MW-007` |
| Positive terminal is present | save manually, reload and inspect state | build, inventory, rank, journal, completed report and successor match | retained result, not a transient conversation | `MW-008`, `MW-009` |

## Strategic and experiential structure

- Local decision: which topic to ask, which direction to follow, whether to
  spend another finite pick use and which carried object to equip or deliver.
- Medium-term planning: preserve the package, money and lockpick stock; turn
  Sellus and Bacola dialogue into a route; verify prerequisites before asking
  Caius for the next state transition.
- Long-term structure: convert a committed identity and textual information
  chain into faction membership and one retained successor assignment.
- Common heuristics: read the journal rather than expect a waypoint; keep
  fatigue high before probabilistic actions; use the intended level-1 chest;
  distinguish package delivery from the later `Orders` topic; save only after
  the successor appears.
- Failure attribution: a missing topic, wrong destination, absent package,
  exhausted pick, low-fatigue attempt, unaccepted induction, missing order or
  premature save is separable from the random draw itself.
- Player-trust factors: visible character sheet, named topics, persistent
  journal text, written directions, explicit item stock, lock success/failure,
  faction rank, quest entries and manual reload parity.
- Claim IDs: `MW-002`–`MW-009`.

## Replay and variation

- What changes between sessions: race, sex, class, sign, optional creation
  method, lock result/use count, incidental pickups, route, dialogue order and
  optional activity. The canonical trace fixes all terminal-relevant choices.
- Randomness or procedural generation: the admitted lock attempt is random
  under current skill/tool/lock/fatigue inputs; route geometry, speakers,
  package, induction and first orders are authored.
- Multiple viable strategies: Caius can be reached on foot or by transport and
  directions can be learned from multiple residents; the canonical route fixes
  the silt strider plus Bacola. The tutorial chest is optional to quest success.
- Typical replay motive: compare builds, alternative travel and later factions
  or continue the open world. None expands this bounded report packet.

## Adjacent systems and history

- Direct predecessor: the original 2002 Morrowind rules underlie the current
  Windows GOTY distribution; this record does not claim every port or wrapper.
- Variants: original discs, Xbox, regional/localised packages, OpenMW, mods,
  console commands and expansion routes require their own scope evidence.
- Similar games: Skyrim Special Edition, Baldur's Gate 3, Disco Elysium - The
  Final Cut, Fallout 4 and Fallout: New Vegas share selected build, dialogue,
  quests, inventory, checks or save-state boundaries.
- Important differences: Skyrim's lock uses continuous angle/torque feedback,
  while Morrowind resolves a single hidden skill-weighted draw and consumes a
  use. Baldur's Gate 3 exposes d20 difficulty and modifiers. Disco Elysium
  visibly rolls two dice and classifies retries. This packet instead links
  text-only route knowledge and a delivered package to first faction orders.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-107`, `ACT-199`, `ACT-232`, `ACT-238`, `ACT-341` | creation, dialogue, travel, package and lock target |
| System Behaviour | `SYS-004`, `SYS-342`, `SYS-379`, `SYS-993` | hidden draw, Security progress, quest state and finite lock resolution |
| Constraint | `CON-282` | ordered release, information, delivery and induction gates |
| Information | `INF-073`, `INF-119`, `INF-125`, `INF-128` | equipment, build, journal/map and inventory state |
| Objective | `OBJ-158` | settle the report into retained first orders |
| Time | `TIM-007` | manual-save branch restoration |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `361` (`GAME-0001`–`GAME-0361`).
- Exact genome matches: none.
- Tied near matches: `GAME-0361` — Fallout: New Vegas (`11 / 33 = 0.333333`).
- Supported combination subsets: none.
- Scan date: 2026-09-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0361` — Fallout: New Vegas | `ACT-008`, `ACT-199`, `ACT-232`, `ACT-341`, `SYS-379`, `CON-282`, `INF-073`, `INF-119`, `INF-125`, `INF-128`, `TIM-007` | Both packets create a persistent character, navigate an authored open world, handle inventory, converse, advance quest flags and verify state through a manual reload. New Vegas allocates S.P.E.C.I.A.L. plus three tagged skills and recruits a live town defence; Morrowind fixes race/class/sign, follows text-retained directions, risks a consumable skill-weighted lock attempt and turns package delivery into first faction orders without scoped combat | Near, `11 / 33 = 0.333333` |

### Preserved research notes

- Classification result: one new System Behaviour plus seventeen reused
  action, random, skill, quest, information, objective and history boundaries.

## Taxonomy impact

- Add `SYS-993` under
  [`TAXONOMY_CHANGE_101`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_101.md).
- Add support references to reused genes without changing their boundaries or
  any earlier reviewed signature.
- Add no combination: no verified recurring proper subset is established by
  this unit.

## Negative results

- No executable, save or audiovisual evidence was available.
- No combat, spell, persuasion, custom class, level, later faction or expansion
  system is imported merely because the GOTY product contains it.
- The tutorial chest is a mechanics probe, not a prerequisite for reporting to
  Caius; the terminal never depends on a favourable random draw.
- `OBJ-113` is rejected: there is no scripted captivity disaster or dungeon
  escape. `OBJ-158` already covers a dialogue/check-gated opening into retained
  successor access.
- No repeated verified combination was found.

## Delta summary

## New facts

- [Confirmed | Corroborated | High] The exact current Steam GOTY boundary and
  package-to-Blades-to-first-orders route are now represented (`MW-001`–`MW-009`).

## New genes

- [Observation | Corroborated | High] `SYS-993` — resolve one equipped finite
  lock tool from skill, attributes, fatigue, quality and lock level.

## New combinations

- [Observation | Direct | High] No new combination.

## Taxonomy changes

- [Observation | Corroborated | High] Add one Active system boundary through
  `TAXONOMY_CHANGE_101`; preserve all lower-ID signatures.

## New questions

- How does a later Morrowind route couple the same hidden skill-weighted checks
  to combat, spell and reputation systems without obscuring causal boundaries?

## Next recommended game

- [Confirmed | Direct | High] `GAME-0363` — The Legend of Zelda: Ocarina of
  Time, the next authorised unit in `SEARCH_DEMAND_GAME_SELECTION_026`.
- Optimisation criterion: continue the fixed Goal order after complete unit
  acceptance.
- Expected information gain: context-sensitive action, target lock, musical
  command sequence, child inventory and first-dungeon terminal.
- Backlog impact: unit 3 of the active nine-game Goal.

## Why this game

- [Confirmed | Direct | High] It is the next recorded selection and tests a
  recognisable embodied adventure packet against Morrowind's text-and-check
  onboarding.

## Reproducibility notes

1. Install Steam app `22320` English on Windows, public Build ID `1510067`;
   use no OpenMW, mods or console commands and do not enter expansion content.
2. Create Atlas as a male Dunmer, Warrior, under The Warrior birthsign.
3. During release, take the iron dagger and Apprentice's Lockpick; attempt the
   level-1 tutorial chest until success or tool exhaustion; take the engraved
   ring but do not complete Fargoth's side quest.
4. Accept Sellus's package and directions, leave the office and take the silt
   strider from Seyda Neen to Balmora.
5. Ask Bacola Closcius for Caius's location and follow the retained directions.
6. Deliver the package, join the Blades, accept the level-1 support and ask for
   orders until `Antabolis Informant` is active.
7. Save manually, reload and verify character, inventory, package removal,
   Blades Novice rank, completed report and active successor.
8. Run `python3 scripts/verify_morrowind_control.py`, then all repository,
   localisation, web, browser and accessibility gates.

## Localisation review

- `verified`: official names, Steam, Bethesda, Morrowind, Tribunal, Bloodmoon,
  OpenMW, Dunmer, Warrior, The Warrior, Blades, Security and named quests/places
  remain product, interface or proper-name identifiers.
- `corrected`: the complete Ukrainian profile, scope, direct-play note,
  presentation, salience note, new-gene definition and all plain-language cards
  were authored in this unit with natural syntax and complete causal detail.
- `retained-with-reason`: Latin-script residue is limited to the official
  identifiers above; no generic English explanatory prose is deferred.
