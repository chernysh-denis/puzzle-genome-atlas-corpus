---
game_id: GAME-0348
slug: resident-evil-directors-cut
game_title: "Resident Evil: Director’s Cut"
analysis_status: reviewed
reviewed: 2026-09-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-199
    - ACT-341
  system:
    - SYS-057
    - SYS-215
    - SYS-369
    - SYS-578
  constraint:
    - CON-210
    - CON-282
    - CON-285
    - CON-296
    - CON-621
  information:
    - INF-073
    - INF-075
    - INF-115
    - INF-125
    - INF-128
  objective:
    - OBJ-026
  time:
    - TIM-003
    - TIM-007
---

# Game: Resident Evil: Director's Cut

Use the canonical [vocabulary, genome signature and comparison
rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Chris Redfield,
Jill Valentine, Rebecca Chambers, Spencer Mansion, Dining Room, Main Hall,
west save room, Sword Key, Ink Ribbon, typewriter, PlayStation and
`SLUS-00551` are carrier parameters, not gene names.

## Analysis scope

- Version / ruleset: the first North American English PlayStation release of
  *Resident Evil: Director's Cut*, game-disc serial `SLUS-00551`, published
  1997-09-30 with the separate *Resident Evil 2* demo disc `SLUS-90009`.
  Select the menu's exact `STANDARD (original version)` rules, Chris Redfield
  and fresh save data. The later Dual Shock Version `SLUS-00747`, `TRAINING`,
  `ADVANCED`, Jill, other regions, ports, downloadable wrappers, remakes,
  randomisers, cheats and modifications are separate products or packets.
- Structured analysis target: the original booklet's controls, status,
  inventory, map and save rules joined to the written original-PlayStation
  route from first Chris control through the Sword Key's three opening uses
  and a reload-verified typewriter save; see `GAME-0348` in
  [`knowledge/platforms/games.json`](../../platforms/games.json).
- Scenario and entry: start a new `STANDARD (original version)` game as Chris.
  The opening presentation and Wesker's Dining Room order have ended; the
  packet begins at first ordinary Chris control with an empty six-slot
  inventory and no prior file, key, opened lock or route flag.
- Fixed reproducible route: inspect the first zombie corridor and return to the
  Main Hall; receive or collect the opening handgun and Ink Ribbon; reach the
  west mansion save room, meet Rebecca and take the Sword Key; use that one
  retained key on the Keeper's Bedroom door, the Piano Bar door and the Art
  Room exit to the L Passage in an order legal for the original layout; accept
  the prompt to discard it only after its final compatible lock; step through
  the newly connected L Passage; return to the west save room; insert one Ink
  Ribbon at the typewriter, write a fresh memory-card file, quit, reload and
  verify that the opened route remains available while the exhausted Sword Key
  remains absent.
- Primary decision loop: read the fixed-camera room and sounds, turn Chris
  relative to his own facing, walk or run toward a visible door, item or
  hostile, ready and fire the equipped handgun or evade, preserve one of six
  carried slots for the key and Ink Ribbon, apply the matching key to each
  lock, and decide when to spend the finite ribbon on a retained branch.
- Positive terminal: after crossing the final Sword-Key passage at least once,
  a fresh typewriter file is loaded and ordinary control resumes in the west
  save room with all three admitted doors still opened and no Sword Key in the
  six-slot inventory. The reload is a retention check for the reached spatial
  objective; no action after confirmation is admitted.
- Failure and recovery: hostile attacks reduce Chris's one condition pool; zero
  health ends the attempt. Loading the chosen file restores its recorded room,
  condition, inventory and route flags rather than the failed transient state.
  A death before the first write must restart the packet because no scoped file
  exists yet.
- Included: tank-relative turning and forward/backward movement, running only
  forward, fixed-camera room transitions, the opening handgun, readied fire,
  automatic reload when an empty handgun has another compatible clip,
  perception-driven zombie approach, real-time damage and death, Chris's six
  inventory slots, pickup and equip state, the Sword Key and its three
  compatible locks, final-use discard prompt, explored-room map, condition and
  inventory displays, Ink Ribbon, typewriter, memory-card file and reload.
- Reproducible parameterisation: default controls; no existing memory-card
  file; Chris; `STANDARD (original version)`; keep the opening Ink Ribbon and
  reserve one free slot for the Sword Key. Exact ammunition, hits, evasion
  path, enemy positions at a room transition, remaining condition and save-file
  number may vary. The six-slot limit, three keyed locks, final discard
  eligibility, one-ribbon save cost and retained route state do not.
- Excluded: the bundled demo; `TRAINING`, `ADVANCED` and Jill; item-box
  transfers; herbs and other healing; examining or combining puzzle items;
  shotgun, armour, crests, chemical, piano performance and emblem exchange;
  Hunters, Yawn, Plant 42, Tyrant, later mansion/laboratory routes, partners,
  endings and rankings; exact damage, enemy-health or random-drop values;
  audio-visual criticism and every other edition or platform.
- Direct-play status: not conducted. No disc, console, controller, memory card,
  emulator, ROM, save, screenshot, video or audio was used. The packet is a
  source-bounded reconstruction from the exact English manual, verified disc
  identity and three written Chris routes, not a claimed playthrough.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| `REDC-001` | The selected product is the first North American `SLUS-00551` Director's Cut game disc released 1997-09-30, not the bundled `SLUS-90009` demo or later `SLUS-00747` Dual Shock Version | Confirmed | Corroborated | High | P1, P2, S1 |
| `REDC-002` | Its exact original-rules menu label is `STANDARD (original version)` beside `TRAINING` and `ADVANCED` | Confirmed | Direct | High | P1 |
| `REDC-003` | Chris uses character-relative forward/backward motion and turning; running combines Square with forward and does not apply backward | Confirmed | Direct | High | P1 |
| `REDC-004` | R1 readies a weapon, direction aims and X attacks; the handgun carries fifteen bullets and automatically reloads from another clip when empty | Confirmed | Direct | High | P1 |
| `REDC-005` | Chris carries at most six inventory items; status exposes carried/equipped state and condition, while the map records visited rooms | Confirmed | Direct | High | P1 |
| `REDC-006` | A manual save requires inserting and consuming one Ink Ribbon at a typewriter; one memory-card block holds one file and up to five files are supported | Confirmed | Direct | High | P1 |
| `REDC-007` | The opening Chris route supplies a handgun and Ink Ribbon, reaches Rebecca and the Sword Key, and exposes the west save-room typewriter | Observation | Corroborated | High | S2, S3, S4 |
| `REDC-008` | In `STANDARD`, the Sword Key opens the Keeper's Bedroom, Piano Bar and Art Room-to-L-Passage doors; it stays carried between uses and becomes discardable only after the last compatible lock | Observation | Corroborated | High | S2, S3, S4 |
| `REDC-009` | Zombies act in real time, can pursue Chris through locally connected room space and reduce one visible condition pool to death | Observation | Corroborated | Medium | P1, S2, S3, S4 |
| `REDC-010` | The bounded terminal is the newly traversable L Passage retained by a fresh typewriter save and reload, without importing later mansion puzzles | Strong Pattern | Corroborated | High | `REDC-001`–`REDC-009`, V1 |

## Basic data

- Release / origin: Capcom; first North American English PlayStation
  *Director's Cut* release, 1997-09-30.
- Platform or physical form: licensed North American PlayStation CD-ROM game
  disc `SLUS-00551`; a separate bundled demo disc is outside the packet.
- Puzzle family: tactical forecast and counterplay; inventory and fixture
  dependencies; ordered dependency sequencing; real-time system pressure.
- Primary sources, accessed 2026-09-21:
  - **[P1]** [Capcom's original North American PlayStation instruction
    booklet](https://www.videogamemanual.com/ps1/Resident%20Evil%20-%20Director%27s%20Cut%20%28USA%29.pdf),
    cover and pp. 6–23, for serial, exact mode labels, Chris/Jill selection,
    controls, handgun capacity and automatic reload, status, condition, map,
    six/eight-slot inventories, typewriter, Ink Ribbon and memory-card rules.
  - **[P2]** [TASVideos' verified Redump-derived disc
    entry](https://tasvideos.org/Games/805/Versions/View/1351), for
    `SLUS-00551`, SHA-1 `d926cec7ac6a1665cc00039ab92dee6a6bebe824`
    and MD5 `50d96c24761ebf5926719c7090f8bf22`.
- Corroborating textual sources, accessed 2026-09-21:
  - **[S1]** [Lost Releases' first-edition product
    record](https://crimson-ceremony.net/lostreleases/item.php?id=regame_re1dc-ps1-usa4),
    separating game disc `SLUS-00551`, demo disc `SLUS-90009`, release date
    and the later Dual Shock product.
  - **[S2]** [GameFAQs Chris guide by
    Rombie](https://gamefaqs.gamespot.com/ps/198462-resident-evil-directors-cut/faqs/16828),
    for the opening handgun, Rebecca, Sword Key, keyed rooms and save route.
  - **[S3]** [GameFAQs updated Chris
    walkthrough](https://gamefaqs.gamespot.com/ps/198462-resident-evil-directors-cut/faqs/76571/chris-redfield-walkthrough),
    for the same route and final Sword-Key disposition.
  - **[S4]** [GameFAQs original Chris route by
    CRatman](https://gamefaqs.gamespot.com/ps/198462-resident-evil-directors-cut/faqs/2200),
    for an independent original-PlayStation ordering check.
- Validation source: **[V1]** repository-side executable state reconstruction
  derived from P1–P2 and S1–S4; it does not execute or inspect the commercial
  program.
- Claim IDs: `REDC-001`–`REDC-010`.

## Mechanical decomposition

### Action Genes

- `ACT-008`: turn Chris and move him forward or backward relative to his own
  facing, or run forward, through fixed-camera mansion rooms.
- `ACT-161`: ready, aim and fire the equipped handgun at one reachable zombie.
- `ACT-199`: take the handgun, ammunition, Ink Ribbon and Sword Key into a
  compatible carried slot and equip the handgun through the status screen.
- `ACT-341`: open ordinary doors, apply the Sword Key to matching locks,
  accept its final discard and commit the typewriter interaction.
- Rejected `ACT-183`: the selected rules automatically reload an empty handgun
  when another clip exists; the player does not issue a live reload action.
  Rejected `ACT-164`: paused equipment selection is a transfer/equip operation,
  not a quick-slot weapon swap.
- Claims: `REDC-003`–`REDC-008`.

### System Behaviour Genes

- `SYS-057`: a zombie that perceives Chris leaves its local idle position and
  approaches him, with room geometry and door transitions parameterised.
- `SYS-215`: movement, readying, shots, hostile contact, damage and defeat
  resolve while the room continues in real time.
- `SYS-578`: zombie attacks reduce one condition pool whose zero state ends the
  attempt; scoped healing is deliberately excluded.
- `SYS-369`: after a scoped save exists, loading it following death replaces
  the failed room, condition, inventory and route state with the recorded file.
- Rejected `SYS-063`: the Sword Key is not consumed by every door. It remains
  one carried authority until its last compatible lock, then the player may
  discard it. That is a parameter of `ACT-341` plus `CON-296`, not per-fixture
  key consumption.
- Resolution order: accept movement, aim, fire, pickup, key, discard or save
  input; validate weapon, slot, authority, fixture and ribbon predicates;
  resolve pursuit and combat; update condition; write or restore retained state.
- Claims: `REDC-004`, `REDC-006`, `REDC-008`, `REDC-009`.

### Constraint Genes

- `CON-210`: Chris may carry only six items; a pickup needs a free compatible
  slot or stack, so the route reserves room for the Sword Key and Ink Ribbon.
- `CON-282`: the admitted route requires the authored opening, handgun/ribbon,
  Rebecca/Sword Key, compatible locks, final passage and later save in a legal
  dependency order.
- `CON-285`: firing requires the handgun to be equipped and loaded; automatic
  reload requires another compatible clip.
- `CON-296`: each admitted locked door exposes its opening interaction only
  while the one matching Sword Key is carried.
- `CON-621`: the manual write is legal at a typewriter only while an Ink Ribbon
  is carried; accepting it consumes one ribbon and writes a chosen eligible
  memory-card file. The existing boundary already declares an optional
  per-save consumable, so no ribbon-specific gene is added.
- Scarce strategic resources: six carried slots, handgun ammunition,
  condition, the retained Sword Key, Ink Ribbons and memory-card files.
- Claims: `REDC-004`–`REDC-008`.

### Information Genes

- `INF-073`: status exposes the equipped weapon and carried ammunition state
  before the next room action.
- `INF-075`: the condition monitor exposes Chris's current survival state.
- `INF-115`: fixed camera, local line of sight, hostile movement and spatial
  sound disclose only nearby danger rather than an omniscient enemy map.
- `INF-125`: the map records visited rooms and Chris's current mansion route.
- `INF-128`: pickup prompts and the status inventory expose item identity,
  quantity, equip state and remaining slot capacity.
- Claims: `REDC-003`–`REDC-009`.

### Objective Genes

- `OBJ-026`: carry the Sword Key through all three compatible fixtures so the
  Art Room exit becomes traversably connected, cross into the L Passage, then
  verify that reached route by save and reload.
- Rejected `OBJ-155`: this is not a named chapter or mission completion with a
  settlement screen and successor handoff. The save is a separately chosen
  retention check.
- Success, evaluation and failure: success is the newly reached passage whose
  opened state and exhausted key survive reload; death or a missing ribbon is
  failure/recovery, not completion.
- Claims: `REDC-006`, `REDC-008`, `REDC-010`.

### Time Genes

- `TIM-003`: movement, pursuit, aim, shots and damage advance in real time;
  status, map and save selection pause that live room state.
- `TIM-007`: the written memory-card file can be restored and continued with a
  different route or resource choice, replacing the previously observed future.
- Claims: `REDC-004`, `REDC-006`, `REDC-009`, `REDC-010`.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Fresh title state | choose `NEW GAME` → `STANDARD (original version)` → Chris | first ordinary Dining Room control begins under the original rules with Chris's six-slot capacity | exact entry | `REDC-001`–`REDC-003` |
| Chris faces away from a connected doorway | press left/right, then forward; optionally hold Square with forward | Chris turns around his own axis and moves in the facing direction; fixed camera does not redefine forward | tank-relative navigation | `REDC-003` |
| Handgun is equipped with loaded bullets and a zombie is reachable | hold R1, aim and press X | one shot resolves while the zombie and room remain live; if the handgun empties and another clip exists, the game reloads automatically | readied firearm state without manual reload | `REDC-004`, `REDC-009` |
| A required item is reachable and one of six slots is free | use the action interaction | the item enters the inventory; without capacity the transfer cannot complete | finite carried state | `REDC-005`, `REDC-007` |
| First or second matching door is locked and the Sword Key is carried | interact and use the Sword Key | the door opens while the same key remains carried for later compatible locks | reusable authority | `REDC-008` |
| Third matching door is locked and the Sword Key is carried | use the key, then accept the no-longer-needed discard prompt | the L Passage becomes traversable and the exhausted authority leaves inventory | final authority exhaustion | `REDC-008`, `REDC-010` |
| West typewriter is reachable, one Ink Ribbon and a usable memory-card file exist | interact, insert the ribbon and choose the fresh file | one ribbon is consumed and current condition, inventory and opened-route state are written | consumable fixture save | `REDC-006` |
| The fresh file exists | quit and load that file | Chris, his recorded state, opened doors and absent exhausted Sword Key return | retained spatial terminal and branchability | `REDC-006`, `REDC-010` |
| After the save, hostile damage reaches zero | load the chosen file | failed transient positions, condition and combat state are replaced by the written state | failure recovery | `REDC-009` |

## Strategic and experiential structure

- Local decisions: reorient before committing to a fixed-camera exit, preserve
  distance before readying the handgun, evade or spend ammunition, and keep a
  free slot for the next route object.
- Medium-term planning: carry one authority through several locks instead of
  treating each door as a new key expense, then deliberately free its slot only
  after the final compatible lock.
- Long-term structure: the route turns limited inventory and local visibility
  into a dependency chain whose reached state is made branchable by spending a
  separate finite save resource.
- Common heuristics: backtrack to the known typewriter only after the last key
  use; do not spend or store the scoped Ink Ribbon; avoid unnecessary shots.
- Failure attribution: the condition monitor, ammunition/equip state, six-slot
  inventory, door refusal, final key prompt and typewriter refusal separate
  combat, capacity, authority and save-resource mistakes.
- Player-trust factors: the same key must remain after early locks, become
  discardable only after the last, the ribbon must decrease on save and the
  reloaded file must preserve the opened route.
- Claims: `REDC-003`–`REDC-010`.

## Replay and variation

- What changes between attempts: exact room order among legal key doors,
  ammunition spent, hits taken, evasions, enemy pose at transitions, condition
  at the save and chosen file number.
- Randomness or procedural generation: mansion topology, key locations, door
  compatibility and typewriter are authored; hostile timing and combat contact
  create bounded local variation.
- Multiple viable strategies: the first zombie and later local threats may be
  fought, stunned or evaded while the same key-and-save terminal remains.
- Typical replay motive: conserve ammunition and condition, improve route
  order or compare Chris with excluded modes/characters in separate packets.
- Claims: `REDC-003`–`REDC-010`.

## Adjacent systems and history

- Direct product corridor: the selected first Director's Cut reissues the
  original scenario with `STANDARD`, adds `TRAINING` and `ADVANCED`, and ships
  beside a separate demo. The later Dual Shock Version is a different serial
  and remains excluded.
- Resident Evil 2 (2019 remake) shares direct traversal, readied handgun fire,
  finite inventory, one condition pool, perception pressure, a carried key,
  visited map, typewriter persistence and branchable reload. Its opening has a
  manually reloaded magazine, one-use gas-station key, autosaves, no ribbon on
  Standard and a hostile-proximity save predicate. This packet instead uses
  tank-relative fixed cameras, automatic empty reload, one authority across
  three locks and a consumed Ink Ribbon.
- Silent Hill 2 (2024 remake) shares local survival information, carried key
  gates and a mapped location route but not the six-slot inventory, retained
  multi-door key or ribbon-spending typewriter.
- Important difference: no new gene is needed. `CON-621` already parameterises
  an optional per-save consumable, and `ACT-341` plus `CON-296` already admit a
  key retained across compatible interactions until its final disposition.
- Claims: `REDC-001`–`REDC-010`.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-161`, `ACT-199`, `ACT-341` | tank-relative movement, handgun, key, doors and typewriter are parameters |
| System Behaviour | `SYS-057`, `SYS-215`, `SYS-369`, `SYS-578` | zombie perception, damage and load disposition are parameters |
| Constraint | `CON-210`, `CON-282`, `CON-285`, `CON-296`, `CON-621` | six slots, three locks, automatic reload, one ribbon and file are parameters |
| Information | `INF-073`, `INF-075`, `INF-115`, `INF-125`, `INF-128` | camera, sounds, condition display and inventory presentation are parameters |
| Objective | `OBJ-026` | L Passage and reload verification are parameters |
| Time | `TIM-003`, `TIM-007` | live room cadence and memory-card branch are parameters |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `347` (`GAME-0001`–`GAME-0347`).
- Exact genome matches: none.
- Tied near matches: `GAME-0280` — Resident Evil 2 (2019 remake) (`21 / 27 = 0.777778`).
- Supported combination subsets: none.
- Scan date: 2026-09-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0280` — Resident Evil 2 (2019 remake) | `ACT-008`, `ACT-161`, `ACT-199`, `ACT-341`, `SYS-057`, `SYS-215`, `SYS-369`, `SYS-578`, `CON-210`, `CON-282`, `CON-285`, `CON-296`, `CON-621`, `INF-073`, `INF-075`, `INF-115`, `INF-125`, `INF-128`, `OBJ-026`, `TIM-003`, `TIM-007` | Both packets traverse authored survival-horror rooms, ready and fire a handgun, manage finite carried slots, apply a matching key, read local danger, condition and a visited map, and retain a reached route through fixture saving and branchable reload. Resident Evil 2 adds direct manual reload, body-region shot response, focused-reticle power, a restorative branch and hostile-proximity typewriter legality. Director's Cut instead uses tank-relative fixed cameras, automatic empty reload, one key retained across three locks and an Ink Ribbon consumed by the save. | Tied near, `21 / 27 = 0.777778` |

### Preserved research notes

- New genes: none.
- Reused genes: `ACT-008`, `ACT-161`, `ACT-199`, `ACT-341`, `SYS-057`,
  `SYS-215`, `SYS-369`, `SYS-578`, `CON-210`, `CON-282`, `CON-285`,
  `CON-296`, `CON-621`, `INF-073`, `INF-075`, `INF-115`, `INF-125`,
  `INF-128`, `OBJ-026`, `TIM-003` and `TIM-007`.
- Classification result: `New combination of known genes`.
- Evidence and reasoning: every operational boundary transfers from reviewed
  lower-ID carriers. The exact old-game combination of a multi-door retained
  authority, six-slot survival inventory and consumable fixture save is new,
  but it does not warrant a new atomic gene or corpus combination.

## Taxonomy impact

- Registry changes: reused Active boundaries gain explicit carrier evidence;
  no lifecycle, wording, ID, earlier signature, combination or family boundary
  changes.
- Taxonomy-change record:
  [`TAXONOMY_CHANGE_090`](../../../research/taxonomy-changes/TAXONOMY_CHANGE_090.md).
- Candidate terms affected: Chris Redfield, Jill Valentine, Rebecca Chambers,
  Spencer Mansion, Dining Room, Main Hall, Sword Key, Ink Ribbon, typewriter,
  `STANDARD (original version)`, PlayStation, `SLUS-00551`, `SLUS-90009` and
  `SLUS-00747` remain product, actor, place, item, interface, mode, platform or
  serial parameters.

## Negative results

- No direct-play, disc, console, controller, memory-card, ROM, emulator,
  screenshot, video or audio claim.
- The selection phrase `Original mode` is corrected to the exact
  `STANDARD (original version)` label from the selected booklet.
- The provisional claim that a key is consumed per door is rejected: the one
  Sword Key remains through early compatible locks and becomes discardable
  only after the final use. `SYS-063` and a new key-consumption boundary are
  therefore excluded.
- `ACT-183`, `ACT-164`, `OBJ-155`, item-box transfer, healing, puzzles and every
  later mansion/laboratory mechanic remain outside this packet.

## Delta summary

## New facts

- [Confirmed | Direct | High] The selected serial's exact original-rules label
  is `STANDARD (original version)`, not `Original mode` (`REDC-001`,
  `REDC-002`).
- [Observation | Corroborated | High] One Sword Key opens three admitted locks,
  remains carried between them and becomes discardable only after the last
  compatible use (`REDC-008`).
- [Confirmed | Direct | High] Each accepted typewriter save consumes one Ink
  Ribbon and writes a chosen memory-card file (`REDC-006`).

## New genes

- [Observation | Corroborated | High] No new genes; all twenty-one boundaries
  transfer without generalisation.

## New combinations

- [Observation | Corroborated | High] No new registered combination; the
  twenty-one-gene game signature is unique but lacks a recurring independently
  evidenced shared-core candidate.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_090` records a reuse-only
  carrier extension and explicit rejection of per-door key consumption.

## New questions

- Does a later mansion packet justify separating item-box storage, combined
  puzzle-object inspection or poison treatment without bloating this opening?

## Next recommended game

- [Hypothesis | Corroborated | High] `GAME-0349` — Tom Clancy's Splinter Cell.
- Optimisation criterion: test light visibility, sound and alarm constraints
  against the local-perception and stealth vocabulary.
- Expected information gain: distinguish deliberate concealment feedback from
  survival-horror occlusion and direct pursuit.
- Backlog impact: sixth of nine selected games completed; three units remain.

## Why this game

- [Hypothesis | Corroborated | High] Splinter Cell should reuse embodied
  traversal and partial opponent information while stressing light-dependent
  visibility, nonlethal interaction and alarm-state boundaries absent here.
