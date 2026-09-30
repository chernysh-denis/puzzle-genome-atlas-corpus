---
game_id: GAME-0458
slug: the-legend-of-zelda-links-awakening
game_title: The Legend of Zelda: Link's Awakening
analysis_status: reviewed
reviewed: 2026-09-30
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-009
    - ACT-161
    - ACT-199
    - ACT-223
    - ACT-341
    - ACT-437
  system:
    - SYS-037
    - SYS-045
    - SYS-063
    - SYS-215
    - SYS-398
    - SYS-417
    - SYS-578
    - SYS-605
    - SYS-910
    - SYS-931
    - SYS-1206
    - SYS-1207
    - SYS-1208
    - SYS-1209
  constraint:
    - CON-175
    - CON-349
    - CON-402
    - CON-737
  information:
    - INF-073
    - INF-179
    - INF-180
    - INF-317
    - INF-356
    - INF-440
  objective:
    - OBJ-018
  time:
    - TIM-003
---

# Game: The Legend of Zelda: Link's Awakening

Use the canonical [vocabulary and signature](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Link, Tail Cave, suit, tool identity and heart counts are parameters, not theme genes.

## Analysis scope

- Version / ruleset: Original English 1993 monochrome Game Boy Link’s Awakening, DMG-ZL-USA-1 documentary rules; one first Tail Cave attempt from initial dungeon entry after the Tail Key unlock through credit of Full Moon Cello, or zero-health Game Over. Start with the ordinary sword, shield, three hearts and the retained powder from the forest, no optional purchased shovel, bombs, extra heart pieces or upgraded sword. Include eight-direction movement, side-view ladders and Goombas, sword swings and held-charge spin, A/B inventory assignment and its planning pause, active shield rejection and beetle overturn, enemy knockback into pits, keys and Nightmare Key, pressure switches, pushed-block doors, finite clearances, chests, Roc’s Feather acquisition and assigned jumps, Three-of-a-Kinds matching and Stone Slab Fragment hint, map and compass outline/markers/tone, live health, ordinary drops and temporary defensive/offensive pickups, method-dependent Goomba rewards, Rolling Bones, Moldorm’s tail vulnerability and arena-fall reset, optional boss Heart Container and required cello collection. Stop before death-menu recovery or the next overworld mission; pit recovery inside a surviving attempt is included. Magic Powder is carried entry context; its optional tool-specific transformations, optional bomb-wall shell room, miniboss shortcut portal use, shops, trading chain, other dungeons, full eight-instrument finale, DX Stone Beak/owl statues/Color Dungeon, Switch remake, glitches and emulator save states are separate excluded modules. No exact timing, boss-hit count, drop RNG or cartridge revision beyond the documented edition is claimed.
- Structured analysis target: PLAT-GAME-BOY, original DMG target in [platform coverage](../../platforms/games.json).
- Primary decision loop: inspect the current room and acquired map/compass; assign two carried tools, move, strike or defend while threats continue; satisfy enemy, block, switch, key and matching gates; acquire and assign the feather to cross the next required gaps; preserve health and position through Rolling Bones and Moldorm; take the first required instrument.
- Entry and exit: first ordinary Tail Cave entry after the overworld Tail Key unlock, three hearts, ordinary sword/shield, retained forest powder and no optional purchased route tools. Complete at first Full Moon Cello credit, not boss defeat alone; fail at zero-health Game Over. Do not continue the later eight-instrument sequence or death recovery.
- Included: all causally necessary authored first-dungeon progression, active tool selection, movement, live combat, information, health, room-puzzle and instrument-credit rules named above.
- Excluded: powder-specific optional transformations, optional bomb-wall shell detour, miniboss portal use, death/save recovery, other dungeons, external trading/shopping, DX, remake and exact unmeasured runtime constants. These exclusions do not claim the features are absent from the product.
- Potential scoped modules: forest powder route, optional tools and shell detour, portal/retry/save persistence, each later dungeon, DX and remake differences, exact legal cartridge observation.
- Direct-play status: Not conducted. No cartridge, ROM, emulator, input trace, save, gameplay video or audio was opened or played. The original Nintendo DMG-ZL-USA-1 instruction manual was visually inspected, including printed pp. 5–6, 9–14 and 19–26; the original Nintendo Player’s Guide Tail Cave map and printed pp. 27–29 were visually inspected and pp. 10–16 and 26 cross-checked textually. Its source screenshots distinguish Stone Fragment from DX’s owl system. Exact runtime frames, restoration after saving, drop generator and revision parity are unmeasured. The colour artwork is an original interpretive illustration, not a game capture.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| LA-001 | Original English monochrome 1993 Game Boy rules are documented by DMG-ZL-USA-1 and Nintendo’s original Player’s Guide; no exact software revision is inspected. | Observation | Direct | High | P1 cover, P2 pp. 2–3 |
| LA-002 | Any selected tool, including sword/shield/feather, is assigned to A or B; Start opens inventory; movement has eight directions; a held sword charge produces Whirling Blade on release. | Observation | Direct | High | P1 pp. 5–6, 9–14; P2 pp. 12–15 |
| LA-003 | Raised shield rejects eligible frontal attacks and flips Spiked Beetles; sword contact pushes Helmet Beetles into holes; ordinary foes and attacks resolve live. | Observation | Direct | High | P1 p. 14; P2 pp. 28–29, enemy roster |
| LA-004 | Small keys, Nightmare Key, enemy clears, a pressure switch, pushed block, chests and feather-dependent gaps gate the authored route. | Observation | Direct | High | P1 pp. 11, 20–22; P2 pp. 16, 26–29 |
| LA-005 | Three-of-a-Kinds cycle suits, sword hits stop them and a matching set exposes Stone Fragment; the original slab then supplies its hint, not a DX owl statue. | Observation | Direct | High | P1 p. 21; P2 p. 28 |
| LA-006 | Acquired map and compass reveal outline, Nightmare/chests and a local key/chest entry tone; unvisited exact contents remain undisclosed. | Observation | Direct | High | P1 pp. 20–22; P2 pp. 14, 28 |
| LA-007 | Side-view Goombas give rupees after sword defeat and hearts after a stomp; hearts/fairies heal, ordinary hostile damage persists, capacity and temporary bonuses are distinct. | Observation | Direct | High | P1 pp. 23–25; P2 pp. 10–11, 28–29 |
| LA-008 | Roc’s Feather is retained and must be assigned to jump small gaps; Rolling Bones’ roller can be jumped before striking him. | Observation | Direct | High | P1 p. 17; P2 p. 29 |
| LA-009 | Ordinary bottomless falls return locally; some pits lead below. Falling from Moldorm’s arena restores the guardian’s damage; only its tail is vulnerable. | Observation | Direct | High | P1 p. 23; P2 p. 29 |
| LA-010 | Defeating the first Nightmare exposes an optional Heart Container and the required Full Moon Cello; instrument credit, not boss defeat alone, closes this first collection stage. | Observation | Direct | High | P1 pp. 10, 24; P2 pp. 26–29 |
| LA-011 | No cartridge, ROM, emulator, play, save/reload or audiovisual recording was used; exact drop, frame and persistence details outside this attempt are not measured. | Observation | Limited | High | Documentary method |

## Basic data

- Release / origin: Nintendo’s original 1993 Game Boy game, not the later Game Boy Color DX edition or Switch remake.
- Platform or physical form: English monochrome original Game Boy cartridge target, documentary revision identity; no release parity asserted.
- Mechanical families: FAM-004 for live suit matching; FAM-007 for block pushing and sword displacement into pits; FAM-009 for positioning against live hostile responses; FAM-010 for continuing room threats; FAM-013 for owned tools and key/fixture dependencies; FAM-017 for the authored dependency route. Test the other eleven boundaries and reject them: no constructed route, changed topology, autonomous programme, partial-evidence investigation or full logical assignment.
- Primary sources accessed 2026-09-30:
  - P1: [original Nintendo DMG-ZL-USA-1 manual](https://www.retrogames.cz/manualy/GameBoy/The_Legend_of_Zelda-Links_Awakening_-_GameBoy_-_Manual.pdf), cover and all seventeen PDF leaves visually inspected; printed pp. 5–6, 9–14 and 19–26 supply controls, assignment, active shield, items, map, slab, keys, pits, hearts and recovery boundaries. The archival host is not a game download.
  - P2: [original Nintendo Player’s Guide](https://archive.org/details/Nintendo_Players_Guide_GB_Legend_of_Zelda_The_Links_Awakening), Nintendo of America/Tokuma 1993: printed pp. 27–29 including the Tail Cave map visually inspected; printed pp. 10–16, 26, 98 and 102–103 textually checked for tools, gates, local tone, Goomba method drops and guardian. Its original screenshots are evidence, not incorporated web assets.
- Secondary sources: none needed for admitted core rules. Modern DX/Switch walkthroughs are not accepted as original-edition parity evidence.
- Claim IDs: LA-001–LA-011.

## Mechanical decomposition

### Action Genes

`ACT-008` — Direct movement positions Link in the current room or side-view passage. After acquiring and assigning the feather, jump a narrow floor gap.

`ACT-009` — Facing a movable block and pressing toward it moves it from its contact side. Move the authored block that opens the onward door.

`ACT-161` — An assigned sword makes a normal strike or a held-charge Whirling Blade attack. Release the charged blade when a reachable hostile approaches.

`ACT-199` — The inventory transfers a carried tool into an action-button slot, replacing its prior assignment. Replace the shield with the feather while retaining a sword on the other button.

`ACT-223` — A feather-enabled jump can be timed against the miniboss’s live rolling attack. Jump Rolling Bones’ roller and land before the next sword attack.

`ACT-341` — A reachable fixture accepts its currently legal contextual interaction. Open the revealed feather chest; use the Stone Fragment to read the slab.

`ACT-437` — Holding the assigned shield button requests eligible frontal protection. Raise it before a Spiked Beetle makes contact.

- Parameters and claim IDs: LA-001–LA-011; tools, buttons, room identity, suit and exact damage values do not create additional genes.

### System Genes

`SYS-037` — Compatible loose collectibles are credited when Link reaches them. Reach the heart left by a stomped Goomba when health is missing.

`SYS-045` — Hostile locomotion continues on the live clock while Link acts. A Mini Moldorm keeps moving as Link changes position.

`SYS-063` — A carried small key is consumed when its compatible locked barrier opens. Obtain the entrance-area key before opening a small-key door.

`SYS-215` — Reach, facing and enemy hit conditions determine sword and contact results in real time. Strike Moldorm’s vulnerable tail rather than its armoured body.

`SYS-398` — An authored acquisition retains a non-consumed traversal tool for compatible later route edges. The feather remains owned after crossing the first gap.

`SYS-417` — An admitted permanent capacity pickup raises Link’s maximum health. The defeated Nightmare exposes an optional Heart Container.

`SYS-578` — Hits remove health and compatible hearts or a fairy restore missing capacity. The fairy after Rolling Bones can heal prior damage.

`SYS-605` — Authored flags reveal or open the next dungeon segment. Defeat the required Spiked Beetles to reveal the stairs toward the feather.

`SYS-910` — A typed contact pickup temporarily changes the declared combat or defence state. A Guardian Acorn is temporary defence, not permanent heart capacity.

`SYS-931` — Dungeon map and compass acquisition expand retained navigation information. The acquired compass identifies the Nightmare’s room.

`SYS-1206` — Sword strikes stop the cycling card targets and matching suits clear their set. Stop all Three-of-a-Kinds on hearts to reveal their chest.

`SYS-1207` — Eligible contact with a raised frontal shield changes the hostile into an attackable state. Shield contact overturns a Spiked Beetle; follow with the sword.

`SYS-1208` — A dungeon fall returns Link locally, while a fall from Moldorm’s arena restores the guardian. After falling below the boss platform, return to a healed Moldorm.

`SYS-1209` — The admitted Goomba defeat method changes its collectible reward class. Stomp with the feather when a heart is more useful than a rupee.

- Parameters and claim IDs: LA-001–LA-011; tools, buttons, room identity, suit and exact damage values do not create additional genes.

### Constraint Genes

`CON-175` — Unhealed room damage persists and zero health ends this scoped attempt. Do not assume the next doorway restores the health meter.

`CON-349` — A capability-gated edge is usable only after retaining its required tool and supplying compatible input. Possessing and assigning Roc’s Feather enables the required narrow-gap jump.

`CON-402` — A declared enemy-clearance shutter remains unavailable until its finite set is defeated. A small key does not replace the hostile-clearance condition.

`CON-737` — Sword, shield and feather remain owned, but only two are assigned for active use at once. With sword and feather assigned, reassign before raising the shield.

- Parameters and claim IDs: LA-001–LA-011; tools, buttons, room identity, suit and exact damage values do not create additional genes.

### Information Genes

`INF-073` — The inventory and HUD expose the selected tools and relevant finite carried state. Check that the feather is assigned, not merely owned.

`INF-179` — The local view exposes Link, visible threats, holes, chests and door states. Moldorm’s body and the edge are visible; future motion is not promised.

`INF-180` — Visited room cells remain distinguished from undisclosed room contents. An acquired outline is not the exact contents of an unentered room.

`INF-317` — An authored slab supplies its fixed local instruction after the fragment enables reading. Read the Stone Slab, not a DX owl statue.

`INF-356` — The dungeon display combines local position with earned navigation layers and resource state. Use the acquired map and compass without assuming hidden drops are revealed.

`INF-440` — The acquired compass cues a room containing a key or chest without explaining how to obtain it. The tone can alert you before a hidden reward has appeared.

- Parameters and claim IDs: LA-001–LA-011; tools, buttons, room identity, suit and exact damage values do not create additional genes.

### Objective Genes

`OBJ-018` — The bounded first collection stage ends only after the Full Moon Cello is credited. Moldorm’s defeat alone does not collect the cello.

- Parameters and claim IDs: LA-001–LA-011; tools, buttons, room identity, suit and exact damage values do not create additional genes.

### Time Genes

`TIM-003` — Room combat and symbol cycling continue live outside the paused inventory. Time a strike at the card suit you want, rather than treating it as a turn.

- Parameters and claim IDs: LA-001–LA-011; tools, buttons, room identity, suit and exact damage values do not create additional genes.

## Reproducible transitions

| Before | Action | Deterministic or bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Sword and shield assigned, feather newly owned | Assign feather to one A/B slot | That slot replaces its previous tool; no third simultaneous verb | Possession differs from active assignment | LA-002, LA-008 |
| Assigned sword held until flashing | Release its button | Charged Whirling Blade attack replaces the normal release result | Charge is a parameter of a direct strike | LA-002 |
| Spiked Beetle approaches a raised shield | Maintain eligible facing contact, then strike | Enemy flips before an accepted sword hit | Not passive armour or universal guard | LA-003 |
| Helmet Beetle near a hole | Strike repeatedly from a useful side | Stun and displacement can put it into the pit | Damage is not the only useful hit result | LA-003 |
| Map-room hostile set remains | Defeat its required members | Authored chest appears with the map | Clearance rewards differ from key locks | LA-004 |
| Key-bearing chest unavailable | Step on its authored floor switch | Chest appears; opening it grants carried key state | A switch flag precedes consumption | LA-004 |
| Two required Spiked Beetles active | Flip and defeat both | Stairs appear toward side-view passage and feather chest | Complete the dependency, not unrelated kills | LA-003, LA-004 |
| Feather owned but not assigned | Try its button as a different assigned tool | Feather jump is not available through that input | Tool choice gates traversal | LA-002, LA-008 |
| Three cards cycle their suits | Strike each on the same suit | Matching set disappears and Stone Fragment chest appears | Live matching, not a static tile swap | LA-005 |
| Broken original slab, fragment unowned | Obtain fragment and read slab | The authored local instruction becomes available | Not DX Stone Beak/owl logic | LA-005 |
| Compass acquired, eligible room entered | Enter normally | Sound signals key/chest presence, not exact hidden solution | Documentary sound cue, no played recording | LA-006 |
| Underground Goomba reachable | Sword-defeat it or feather-stomp it | Rupee class versus heart class | Attack method changes reward opportunity | LA-007 |
| Rolling Bones sends its roller | Jump it and land near legal sword reach | Avoid the roller and attack during the live encounter | Retained feather enables timed response | LA-008 |
| Moldorm already damaged | Fall from the arena and return | Guardian damage is restored | Surviving pit fall is not save rollback | LA-009 |
| Moldorm alive, body reachable | Strike body versus tail | Only eligible tail strikes damage the guardian | Weak-point condition within combat | LA-009 |
| First guardian defeated, instrument not credited | Reach and collect Full Moon Cello | First declared collection token is retained | Boss victory alone is not the terminal | LA-010 |

## Strategic and experiential structure

The two assigned buttons turn retained equipment into an immediate choice: sword/feather allows attack and jump but no active shield until reassignment. Inventory planning does not make the resumed combat turn-based. Door, key, switch and feather flags set a dependency route; Three-of-a-Kinds add live timing to explicit matching. The compass reduces local uncertainty without giving the solution. Goomba method rewards couple health needs to attack choice. Moldorm position matters independently of dealt damage because a surviving arena fall erases that encounter’s damage. None of these facts establishes exact hit counts, an optimal route or a played timing experiment. Claims LA-002–LA-011.

## Replay and variation

Hold original edition, starter equipment and first-dungeon boundary fixed; room order where legal, tool assignments, attacks, damage and optional map/fragment/heart acquisition can vary. Record the complete required route even when an optional clue or capacity item is skipped. Do not infer a drop generator, exact boss acceleration curve, pixel collision frame or later-dungeon parity. Claims LA-004–LA-011.

## Adjacent systems and history

The forest powder sequence supplies entry context but has its own transformation loop. The guide recommends buying a shovel then bombs; those purchases and the optional shell wall do not gate the feather, Nightmare Key or first instrument and are not silently made mandatory. Optional miniboss portal use and death/save recovery need separate persistence evidence. The original Stone Fragment/slab and A/B-selected sword/shield must not inherit DX owl objects, Color Dungeon or dedicated remake controls. The complete eight-instrument finale is outside a one-stage collection token set. Claims LA-001–LA-011.

## Normalised genome

| Type | Active gene IDs | Parameters |
|---|---|---|
| action | `ACT-008`, `ACT-009`, `ACT-161`, `ACT-199`, `ACT-223`, `ACT-341`, `ACT-437` | scoped documentary action rules |
| system | `SYS-037`, `SYS-045`, `SYS-063`, `SYS-215`, `SYS-398`, `SYS-417`, `SYS-578`, `SYS-605`, `SYS-910`, `SYS-931`, `SYS-1206`, `SYS-1207`, `SYS-1208`, `SYS-1209` | scoped documentary system rules |
| constraint | `CON-175`, `CON-349`, `CON-402`, `CON-737` | scoped documentary constraint rules |
| information | `INF-073`, `INF-179`, `INF-180`, `INF-317`, `INF-356`, `INF-440` | scoped documentary information rules |
| objective | `OBJ-018` | scoped documentary objective rules |
| time | `TIM-003` | scoped documentary time rules |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `457` (`GAME-0001`–`GAME-0457`).
- Exact genome matches: none.
- Tied near matches: `GAME-0325` — The Legend of Zelda (`16 / 36 = 0.444444`).
- Supported combination subsets: none.
- Scan date: 2026-09-30.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0325` — The Legend of Zelda | Direct movement, aimed attacks, live hostiles, carried keys, continuous health, dungeon flags, map/compass navigation and real-time scheduling | Original Game Boy adds two reassigned active buttons, retained feather-gated jumps, active shield overturn, timed suit matching, method-dependent drops and a pit that restores Moldorm; the NES packet uses passive shield and fixed sword/selected B item before a Triforce fragment | Near match, `16 / 36 = 0.444444`; shared dungeon-action structure with different active-tool, room-puzzle and terminal-token decisions |

## Taxonomy impact

Six new boundaries in [TAXONOMY_CHANGE_195](../../../research/taxonomy-changes/TAXONOMY_CHANGE_195.md), 27 unchanged uses. Named GAME-0458 salience review partitions all 33 uses and pairs every explanation. No carrier-specific sword, feather or cello gene replaces the reusable command, capability or finite staged collection boundaries.

## Negative results

- No passive shield SYS-932, fixed NES A-button assumption or DX Stone Beak/owl/Color Dungeon imports. Active facing guard uses ACT-437, not separately aimed weapon-direction ACT-349 or guard-meter ACT-383.
- No CON-210 inventory storage cap: two assigned verbs are not the total carried item count. No new charge action duplicating ACT-161 or ordinary jump duplicating ACT-008.
- No SYS-770 execution-only recovery conversion: Goomba sword rupees versus stomp hearts has two reward classes. No SYS-369 full checkpoint rollback for a nonlethal pit with retained tools.
- No OBJ-191 Triforce fragment or OBJ-250 recorded melody: the first-stage token is a physically collected instrument; reuse OBJ-018 with the declared one-stage finite set instead of claiming all eight instruments.
- No omniscient future-room content, exact hit/drop/expiry constants, directly heard audio, direct-play novelty, firmware parity or full-product genome. No earlier game, gene boundary or published mapping changes.

## Delta summary

## New facts

- [Observation | Direct | High] Original Nintendo sources separate A/B-selected tools and Stone Fragment/slab from later editions; compass tone and Goomba method drops affect local decisions. LA-002, LA-005–LA-007.

## New genes

- [Observation | Direct | High] Six bounded symbol-stop, active shield result, pit/guardian reset, defeat-method reward, two-button legality and acoustic information records; no external novelty claim.

## New combinations

- [Observation | Direct | High] Complete proper-subset scan reviewed; no new combination or earlier combination edit.

## Taxonomy changes

- [Observation | Direct | High] TAXONOMY_CHANGE_195; earlier definitions and signatures unchanged.

## New questions

- Which lawful original-cartridge observation resolves exact symbol mismatch resets, optional portal state, drop expiry, boss frames and save/reload persistence without importing DX?

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0459 Daxter, original PSP, after full acceptance and the stop window.
- Optimisation criterion: approved platform order, one complete unit/one local commit; no push or public release.

## Why this game

- [Hypothesis | Limited | Medium] Two assigned item buttons and capability-gated room dependencies test the approved historical target beyond a generic real-time sword-game resemblance.
