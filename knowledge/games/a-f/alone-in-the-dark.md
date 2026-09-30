---
game_id: GAME-0456
slug: alone-in-the-dark
game_title: Alone in the Dark
analysis_status: reviewed
reviewed: 2026-09-30
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-009
    - ACT-089
    - ACT-161
    - ACT-199
    - ACT-216
    - ACT-295
    - ACT-341
    - ACT-453
    - ACT-606
    - ACT-607
  system:
    - SYS-215
    - SYS-1201
    - SYS-1202
    - SYS-1203
  constraint:
    - CON-175
    - CON-210
    - CON-285
    - CON-734
    - CON-735
  information:
    - INF-003
    - INF-075
    - INF-115
    - INF-438
  objective:
    - OBJ-026
  time:
    - TIM-003
    - TIM-007
---

# Game: Alone in the Dark

Use the canonical [vocabulary and signature](../../../docs/ARCHITECTURE.md#canonical-vocabulary). A haunted mansion, costume, oil volume, exact mass, monster appearance and controller binding are parameters, not theme genes.

## Analysis scope

- Version / ruleset: Original 1992 Alone in the Dark, documentary target English DOS CD-ROM edition described by Infogrames’ 1993 manual; Edward Carnby from first attic control through the adjoining storeroom’s exit to the corridor, before crossing the corridor. Both furniture-block and unblocked-entry combat branches, search/take/leave, letter and book reading, body attacks, rifle, empty bow, held-item verbs, drop/throw/recovery, oil-to-lamp refill with retained empty can, count and mass limits, local fixed cameras, health, live schedules, explicit P pause and save/load are included. Choose Actions or a carried item through I/Return Options, then a permitted verb; sustain Space and compatible directions to execute it. DOS running uses released then quickly repeated Up, not Macintosh Shift-Up. The original game date is 1992, not a claim of CD/floppy control or engine parity. Exact executable, region, entry seconds, damage, item-state table and save-timer identity were not measured. Source-reported internal weights, 700 mass limit and effective 28 collectible slots remain limited to the written CD mechanics testimony, not an inspected interface. Exclude later corridor floor collapse, deeper mansion, matchbox-lit lamp and dark-maze fuel drain, keys, healing food outside these rooms, boss, ending, speedrun glitches, cheats, later ports, sequels and remakes. Exit at the outward storeroom doorway alive, death or deliberate abandonment; optional documents and all item collection are not compulsory.
- Primary decision loop: read local geometry and active verb, approach a furniture contact side and block an entry before its schedule resolves; search, accept or leave contents, select and perform an eligible body/item operation, manage ammunition and carried mass, recover released items if useful, and continue through the adjoining storeroom alive. An unblocked hostile branch remains admitted rather than treating the furniture solution as the only possible play.
- Entry and exit: first Edward Carnby control in the attic through the outward doorway of its adjoining storeroom, before corridor travel; death and abandonment are alternate terminals. Documentary edition is the DOS CD release of the 1992 original, not a new 1993 game or a claim of all floppy builds.
- Included: the complete affordances and alternative branches in the two-room route above. Selecting Emily instead, keys/healing in later rooms, final boss and dark-maze lamp consumption are separate future packets. Optional searches and documents are not selected mandatory milestones.
- Excluded: later-room traversal, key chains, food, matches and illumination drain; exhaustive mansion route, speedrun clipping/lag/debug cheats, ports, sequels and remakes. No whole-game uniqueness claim.
- Direct-play status: Not conducted. No DOS executable, CD, floppy image, save file, input trace, gameplay video or audio was opened or played. Printed original DOS CD manual pages 8–12 were inspected visually. Public written player routes and first-hand CD mechanics reports were read; their experiments are not our execution, and exact CD/floppy or Carnby/Emily parity is not asserted. The Macintosh manual was rejected for DOS bindings. Artwork is an original illustration, not a screenshot.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| AITD-001 | Original DOS CD manual distinguishes selected action from its later held Space/direction execution; run is double-tapped Up | Observation | Direct | High | P1 printed pp. 8–12 |
| AITD-002 | Search reveals concealed authored contents; Take/Leave and available item-specific operations are separate | Observation | Direct | High | P1 pp. 10–11 |
| AITD-003 | Timely wardrobe/window and chest/trapdoor placement prevents the respective hostile entry; failure admits a live combat branch | Observation | Limited | Medium | S1 attic route; S2 contemporary PC route; S3 pushing and room scripts |
| AITD-004 | Optional attic cover, rifle, lamp, letter and book precede storeroom bow and oil; the latter refills the lamp and leaves a can | Observation | Limited | Medium | S1; S2; S3 items/refill |
| AITD-005 | Finite carried object count and total mass are independent; reported 700 mass and effective 28 collectible slots are unexecuted CD testimony | Observation | Direct | Medium | S3 inventory/items |
| AITD-006 | Compatible body attacks and equipped weapon commands operate in live control; rifle is not a gravity projectile | Observation | Direct | High | P1 pp. 11–12; S3 firing |
| AITD-007 | A released collectible retains world identity for recovery; Drop placement can fail if no eligible free space | Observation | Direct | Medium | P1 item functions; S3 dropping/items |
| AITD-008 | Oil transfer retains the can; direct Use and lamp Reload differ in the reported can-weight update | Observation | Direct | Medium | S3 items |
| AITD-009 | P pauses and save/load restore a stored branch, but not every timer or animation identically; arbitrary menus are not universal timer stops | Observation | Direct | Medium | P1 pp. 10–11; S3 pausing and saving/loading |
| AITD-010 | Original cameras are authored local views; ordinary view or room change is not collectible destruction | Observation | Direct | Medium | S3 camera views, items and save state |
| AITD-011 | Every prior signature and verified combination is scanned without changing earlier boundaries | Observation | Direct | High | deterministic canonical recomputation |

## Basic data

- Release / origin: original Infogrames Alone in the Dark, 1992; documentary edition is original DOS CD-ROM documented in 1993, not later remakes. No original executable is available to this analysis.
- Platform or physical form: DOS PC, keyboard and original CD-ROM; structured target PLAT-DOS, release coverage audit not started. Existing DOS registry reused.
- Puzzle family: FAM-007 physics and object manipulation, FAM-010 real-time system pressure. Furniture position changes admission while a schedule continues. Inventory alone does not justify a route-wide dependency family.
- Primary source checked 2026-09-30: **P1**, [Infogrames original English DOS CD manual](https://mocagh.org/miscgame/aitdtrilogy-alt-aitd1-manual.pdf), printed pp. 8–12 visually inspected. Printed 1993 documentation explicitly identifies CD; the game is the 1992 original.
- **S1**, [The Walkthrough King's written Alone in the Dark route](https://www.walkthroughking.com/text/aloneinthedark.aspx), attic and storeroom only; edition unspecified, not exclusive CD authority. **S2**, [1994 archived PC adventure discussion reproducing the contemporary PC Format route](https://groups.google.com/g/comp.sys.ibm.pc.games.adventure/c/HWUdOlV_DQ4), attic/book/oil clauses; reprint warns of errors. Its debug cheats and later-room guesses are rejected, and it is not independent execution by this analyst.
- **S3**, [SDA first-hand written mechanics and reverse-engineering report](https://kb.speeddemosarchive.com/Alone_in_the_Dark_%281-3%29/Game_Mechanics_and_Glitches), predominantly original-game GOG CD with Emily. Only stated generic command, item, pushing, firing, camera and saved-object rules transfer here, at Medium confidence for unexecuted internal values and Carnby parity. No experiment is claimed as ours.
- Rejected control authority: the Macintosh trilogy manual uses a different run binding. No Macintosh control fills a DOS gap. Restricted GameFAQs pages were not bypassed or used for inaccessible detailed rules.

## Mechanical decomposition

### Action Genes

`ACT-008` — Move the controlled body relative to its facing rather than the current camera. Changing the fixed view does not turn the up arrow into screen-up movement.

`ACT-009` — Select Push, sustain Space and a direction at the contact side to displace the wardrobe or chest. The wardrobe must reach the window; merely selecting Push does not block it.

`ACT-089` — Accept the visible-item or searched-item collection prompt. Leave the old cover outside if you do not want its carried weight.

`ACT-161` — Use the equipped weapon and directional action keys to aim and fire at an admitted monster. The bow found next door has no arrows supplied within this packet.

`ACT-199` — Select an already held compatible item through inventory rather than a quick-slot bar. Choose the rifle rather than assuming it fires while a letter is active.

`ACT-216` — Hold the search command near an eligible object to reveal its existing contents. Searching the chest reveals the rifle; searching is not automatic taking.

`ACT-295` — Fight mode maps held Space and arrows to body attacks, separate from an equipped gun. If a monster entered, a punch does not require rifle ammunition.

`ACT-341` — Perform the authored nearby door or document operation after choosing its appropriate verb. Read the collected letter or open the exit toward the storeroom.

`ACT-453` — Choose an available refill operation with carried oil and lamp. The command is separate from whether the empty can remains afterward.

`ACT-606` — Keep a chosen body or item verb active until you select another eligible operation. Space used for Push must not be assumed to search or fight at the same time.

`ACT-607` — Drop or throw the retained item into reachable world space instead of destroying it. Drop the emptied oil can after refilling the lamp.

### System Genes

`SYS-215` — An admitted hostile can attack during movement; compatible attacks and contact change health. Moving furniture after entry does not automatically erase the monster.

`SYS-1201` — The scheduled attic entry checks whether its window or trapdoor is already obstructed. A blocked window does not also block the separate floor trapdoor.

`SYS-1202` — Oil transfers into the lamp but the emptied can remains a collectible. Reported Use and Reload paths differ in the can-weight update; no direct measurement is claimed.

`SYS-1203` — Legal release keeps an item in the world for later eligible collection. The discarded letter is not inherently consumed just because its carried entry disappeared.

### Constraint Genes

`CON-175` — Health lost to admitted monsters carries through this route; zero ends the attempt. Entering the storeroom does not promise a fresh full life bar.

`CON-210` — Collection obeys a finite object-slot limit independently of carrying mass. A free object entry does not by itself make a heavy object collectable.

`CON-285` — Firing requires the compatible equipped weapon and usable ammunition. Picking up an empty bow does not supply arrows from nowhere.

`CON-734` — The finite total mass limit is separate from the number of inventory objects. An emptied can still occupies a slot and can retain weight.

`CON-735` — Available operations depend on that item and its current state. Do not assume an emptied can can refill again merely because it is still carried.

### Information Genes

`INF-003` — A closed container or concealed letter hides existing authored contents, not a future random draw. The rifle is in the chest before the search reveals it.

`INF-075` — Options exposes the protagonist’s current condition without a promise of automatic recovery. After a hit, inspect life before risking another close attack.

`INF-115` — Authored camera views show nearby space but do not reveal the whole mansion or all hidden contents. A view change alters the visible angle, not the protagonist’s facing.

`INF-438` — Options separates held identities, selected quantities and available versus chosen operations. Check that Push is selected before pressing the shared action key against the wardrobe.

### Objective Genes

`OBJ-026` — Traverse the attic and neighbouring storeroom to its outward doorway without exhausting life. Reading every optional document is not a mandatory exit predicate.

### Time Genes

`TIM-003` — World movement and scheduled entry run in real time outside explicit pause. Do not promise that visiting every menu freezes every timer.

`TIM-007` — Save and load retain world-object, inventory and health state for a revised continuation. A restored chest position is not a claim of bit-identical animation and timer restoration.

## Reproducible transitions

These are bounded source-derived cases, not locally executed engine tests. A future run must record a licensed original DOS CD executable and protagonist, initial inventory, object positions, selected verb and save.

| Before | Action | Source-described resolution | Boundary | Claim |
|---|---|---|---|---|
| First attic control, window entry pending | Select Push and move wardrobe at its contact side before entry | Window entry is obstructed; trapdoor remains a separate threat | obstacle placement is not mere selection | AITD-001/003 |
| Trapdoor entry pending | Push chest completely over its opening | That entry is suppressed; no claim of deleting a monster already inside | independent aperture test | AITD-003 |
| Opening remains unblocked when its schedule resolves | Fight with body or usable rifle | Admitted monster can attack; health loss is live | alternative branch retained | AITD-003/006 |
| Contents remain concealed | Search chest, then choose Take or Leave | Rifle becomes available; revealing alone does not add it | search and transfer separate | AITD-002/004 |
| Selected Push versus selected Open/Search | Hold the same Space with the appropriate target and direction | Different verb resolves; a menu choice alone does not execute either | persistent input mode | AITD-001 |
| Letter or book is held | Read, retain, drop or throw | Reading is optional; released object is not inherently consumed | optional document and recovery | AITD-002/007 |
| An item has a state-specific menu | Select a permitted verb, then change its state | Eligible operations follow that item state, not a universal list | possession is insufficient | AITD-002/005 |
| Lamp and oil can are held in storeroom | Direct can Use versus lamp Reload | Fuel transfers, can stays; reported direct path lowers can weight while Reload does not | retained container, no measured amount | AITD-004/008 |
| Empty can still carried | Drop into legal free world space | Frees its entry and carried weight; object can be collected later | stock consumption is not object deletion | AITD-005/007 |
| Item-count space remains but mass limit would be exceeded | Attempt collection | Mass gate can reject independently | two capacity predicates | AITD-005 |
| Bow collected in storeroom without arrows in this packet | Attempt to fire | Possession does not create ammunition | ready weapon constraint | AITD-004/006 |
| Change authored camera or enter adjoining room | Continue body-relative navigation | View changes, not the tank-control meaning or retained inventory | local information | AITD-001/010 |
| World threat advancing | Explicit P pause and compatible resume | Pause interrupts play; CD Space resume can also execute the selected action | edition-specific caution | AITD-009 |
| Saved chest/inventory/life state precedes a mistaken continuation | Load save | Restores earlier object/health branch, not bit-identical timer and animation state | save boundary | AITD-009/010 |
| Zero health versus alive at storeroom exit | Continue route | Zero terminates; alive reaches the declared route endpoint | bounded objective | AITD-006 |

## Strategic and experiential structure

The first decision spends live movement on preventing entry or preserves a fight branch at health and ammunition cost. Selected action, body facing and camera angle are different states. Search is information acquisition before a weighted transfer; optional documents can be read and left without imposing a made-up all-items objective. Oil is finite contents rather than the container identity, and the two reported refill paths matter to the separate mass gate. These are source-grounded interpretations, not player-performance measurements.

## Replay and variation

Keep the original DOS CD target and Carnby fixed. Timing, furniture placement, admitted monsters, search/take decisions, selected verb, body/weapon attack, optional reading, release, refill path and saved continuation can vary. No exact entry deadline, random seed, best route, collision exploit or hidden value was measured.

## Adjacent systems and history

Later keys, food, matches, dark-maze illumination and final boss do not become attic genes merely because the game eventually contains them. CD/floppy differences in controls, pause and scripts prevent blanket edition parity. The Macintosh manual and later remakes are separate implementations.

## Normalised genome

| Type | Active gene IDs | Role |
|---|---|---|
| action | `ACT-008`, `ACT-009`, `ACT-089`, `ACT-161`, `ACT-199`, `ACT-216`, `ACT-295`, `ACT-341`, `ACT-453`, `ACT-606`, `ACT-607` | bounded action decisions |
| system | `SYS-215`, `SYS-1201`, `SYS-1202`, `SYS-1203` | bounded system decisions |
| constraint | `CON-175`, `CON-210`, `CON-285`, `CON-734`, `CON-735` | bounded constraint decisions |
| information | `INF-003`, `INF-075`, `INF-115`, `INF-438` | bounded information decisions |
| objective | `OBJ-026` | bounded objective decisions |
| time | `TIM-003`, `TIM-007` | bounded time decisions |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `455` (`GAME-0001`–`GAME-0455`).
- Exact genome matches: none.
- Tied near matches: `GAME-0348` — Resident Evil: Director’s Cut (`12 / 36 = 0.333333`).
- Supported combination subsets: none.
- Scan date: 2026-09-30.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0348` — Resident Evil: Director’s Cut | ACT-008, ACT-161, ACT-199, ACT-341, SYS-215, CON-210, CON-285, INF-075, INF-115, OBJ-026, TIM-003, TIM-007 | The original-PlayStation Chris route shares body-relative navigation, equipped fire, carried slots, local views, life and retained continuation. It does not supply scheduled furniture-blocked entry, a persistent shared-key verb, weighted released objects or a refill that retains its empty can. Its keyed route, consumable ribbon/typewriter save, map and perception signature do not transfer into this DOS intro. | Near, `0.333333` |

## Taxonomy impact

Eight Active boundaries enter through [TAXONOMY_CHANGE_193](../../../research/taxonomy-changes/TAXONOMY_CHANGE_193.md). Nineteen existing uses transfer unchanged. ACT-009's adjacency and displacement-distance parameters admit body-contact movement, not independent furniture dragging. ACT-453's finite replacement unit is the can contents, not a new battery action; SYS-791 remains explicitly battery-stock settlement. All 27 uses receive named salience and reviewed bilingual plain-language cards.

## Negative results

- No full-information INF-001 or quick-slot INF-073/ACT-164: local views conceal contents, and Options is not a quick-slot bar.
- No traversal-triggered SYS-749: its trigger omits scheduled aperture entry and obstructing furniture. No SYS-057 perception behaviour is inferred merely from monster appearance.
- No gravity-projectile SYS-146 for hitscan rifle. No lamp-drain SYS-754, toggle ACT-409 or lit-match predicate before the declared rooms provide matches. No keys, food/heal, later corridor collapse or boss from a full-game walkthrough.
- No ACT-186 team-round equipment release, nor SYS-791 battery deletion for an empty retained can. No pure-slot or equipment-category rule substituted for mass.
- Internal capacities, refill-path mass and retained-object data remain source-reported CD facts, not our inspected executable. Exact Carnby/Emily internal parity and timer restoration are unverified.

## Delta summary

## New facts

- [Observation | Direct | High] DOS selected verb and subsequent world execution are separate.
- [Observation | Direct | Medium] The written CD report distinguishes mass, object count, retained empty container and saved world state.

## New genes

- [Observation | Direct | Medium] Eight separately bounded mode, release, scheduled obstruction, refill, persistence, mass, item eligibility and information records; no external novelty claim.

## New combinations

- [Observation | Direct | High] All 274 verified combinations checked; none is a proper subset of this signature. No invented combination.

## Taxonomy changes

- [Observation | Direct | High] TAXONOMY_CHANGE_193; no earlier definition migration.

## New questions

- Which licensed original DOS CD executable reproduces these intro transitions with Carnby, and what exact entry timing, capacity rejection and refill mass does recorded input demonstrate?

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0457 Sega Rally Championship, original arcade, next approved unit only after full acceptance and the 30-second stop window.
- Optimisation criterion: preserve the approved cross-platform order, one complete unit and one local commit; no push, publication or deployment.

## Why this game

- [Hypothesis | Limited | Medium] The approved DOS anchor tests timed spatial prevention and item-state management against the existing corpus rather than assigning genes to horror imagery.
