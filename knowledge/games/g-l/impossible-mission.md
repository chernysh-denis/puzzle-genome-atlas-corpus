---
game_id: GAME-0484
slug: impossible-mission
game_title: Impossible Mission
analysis_status: reviewed
reviewed: 2026-10-02
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-216
    - ACT-341
    - ACT-644
    - ACT-645
    - ACT-646
    - ACT-647
    - ACT-648
  system:
    - SYS-004
    - SYS-045
    - SYS-057
    - SYS-1273
    - SYS-1274
    - SYS-1275
    - SYS-1276
    - SYS-1277
    - SYS-1278
  constraint:
    - CON-068
    - CON-296
    - CON-749
    - CON-750
  information:
    - INF-003
    - INF-179
    - INF-460
  objective:
    - OBJ-002
    - OBJ-273
  time:
    - TIM-003
---

# Game: Impossible Mission — original Commodore 64 timed password mission

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary). Furniture, note pitches, punch-card colours, nine letters and clock penalties are carrier parameters, not genes per object or number.

## Analysis scope

- Version / ruleset: original English 1984 Epyx Commodore 64 rules, reconstructed from the licensed publisher's reproduction of the original instructions and independent written original-C64 play. Exact disk/tape revision and native PAL/NTSC variant were not inspected. No cross-standard timing or wall-shot bug is asserted. This is not Impossible Mission II, the Oric remake, Atari 7800 or Master System port, or THEC64's launcher restart/save facilities.
- Structured analysis target: original English Commodore 64 base game; existing `PLAT-COMMODORE-64`. Other releases remain unaudited.
- Primary decision loop: observe each room's guards and platform routes; reach furniture and hold its search, interrupting or returning later when necessary. Acquire password fragments and scarce utility codes, spend a code to disable room robots temporarily or reset its lifts, or earn another through pitch sorting. In a corridor or elevator, reflect, recolour and superimpose acquired fragments into recognised punch cards, optionally reverse a mistaken join or pay mission time for help. Complete the password and return to its door before the shared clock expires.
- Entry and exit: start one new original mission at the initial elevator with its 12:00 mission clock and fresh generated layout/puzzles. End at the first completed-password control-room entry, terminal 6:00 expiry, or abandonment. Search, guarded traversal, optional code rooms, pocket-computer manipulation, paid help, ordinary pause, death penalties and final scoring all belong to the same packet; it is not a first-room micro-scope. Record lawful native edition, display standard, new-game state, visited rooms, held search intervals, code expenditures, puzzle edits/help and terminal state for reproduction.
- Included: direct walking/somersault and occupant-directed vertical lifts; floor-bound robot locomotion and eligible sensory pursuit; lethal robot/orb/fall events with continued control and mission-time debit, not finite stock lives; searched-content concealment; held progress retained inside a room but reset on leaving while incomplete; typed consumable terminal effects; ascending-pitch code challenges with length growth; an explored room/tunnel map; corridor-only puzzle workspace with copy/drag, horizontal/vertical reflection, recolour, display removal without deleting memory, recent-delete/join undo, same-colour non-overlap joins, oriented four-fragment recognition and nine-letter progress; time-priced orientation/inventory help; password-gated door, mission deadline and independent terminal score.
- Excluded: sequel towers, bombs/mines and saves; later-port controls and bugs; THEC64's added menu restart, emulator snapshots, downloading a ROM, exact random generator/distribution, robot-program catalogue, collision boxes, jump arc, note/freeze durations, frame rate, score optimisation and a measured winning input trace. A remembered password is not accepted as a substitute for assembling the cards. No guessed universal robot hearing/sight or geometric immunity is asserted.
- Potential scoped modules: a lawful native executable trace could establish death-return placement, retained state, token decrement, exact clock rate and pause/terminal scheduling; independently scoped ports need their own rules evidence rather than inferred parity.
- Direct-play status: no original C64 program, emulator, saved state, gameplay image/video/audio or input trace was executed or inspected. The complete licensed HTML instruction reproduction was read, including search, terminals, code rooms, pocket computer, phone, scoring and author hints. A first-hand written original-C64 account and an independent room-guide introduction were read; the creator interview's indexed puzzle/password answers were inspected, not its unavailable full HTML. Native revision, precise death restoration and timing remain unmeasured. Artwork is an original possible scene, not a captured original room.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
|---|---|---|---|---|---|
| IM-001 | Direct walking, somersault and standing-on-platform vertical movement negotiate rooms linked by elevators and corridors. | Observation | Direct | High | P1 Controls/Playing |
| IM-002 | Robots remain on floors and have different sensory/movement/fire programs; an orb, lethal zap or bottom fall costs mission time rather than a fixed life stock. | Observation | Corroborated | Medium | P1 Robots/Scoring/Hints; S1 written play |
| IM-003 | Held furniture search has a remaining bar, resumes after interruption in the same room, resets if the room is left incomplete, and reveals nothing, a utility code or an automatically retained fragment. | Observation | Direct | High | P1 Searching for codes |
| IM-004 | A matching held utility code enables a terminal's temporary robot disable or room-lift reset; the tokens are one-use. | Observation | Corroborated | Medium | P1 Security terminals; S1 one-time-use tokens; S2 scarcity |
| IM-005 | Code-room response sorts presented note squares from low to high, not presentation order; success awards a utility code and lengthens the next sequence. | Observation | Corroborated | High | P1 Code Rooms; S1 pitch-sorting account |
| IM-006 | Only elevators/corridors permit the pocket computer; its glove edits retained fragments using reflections, colours, copying, superposition and display removal. Recent deletion or joining can be undone. | Observation | Direct | High | P1 Pocket Computer/Using the glove |
| IM-007 | Same colour and no overlapping occupied parts permit a join, but do not prove the fragments belong together. Four correctly oriented fragments form one recognised card/letter; all nine letters enable the control-room door. | Observation | Corroborated | High | P1 Solving/Hints; S1 completed mission; P2 indexed creator answer |
| IM-008 | Optional phone help costs two game minutes and either correctly orients the two memory-window pieces or answers whether the upper piece's three partners have been found. Ordinary Paws pause is separately available. | Observation | Corroborated | High | P1 Phone/Pocket Computer; S1 help account |
| IM-009 | The shared clock runs from 12:00 to terminal 6:00; each documented death event charges ten game minutes. Remaining time, found fragments/codes, solved cards and mission completion contribute to final score. | Observation | Corroborated | High | P1 Scoring; S1 clock/deaths |
| IM-010 | New original games rearrange rooms/robot programs and generate different puzzles; exploration retains a visited map, while unsearched contents remain concealed. | Observation | Corroborated | Medium | P1 Playing/New game; S1 generated maze; S2 introduction |

## Basic data

- Release / origin: Dennis Caswell's original Epyx Commodore 64 game, 1984. Exact release day is not required for this packet.
- Platform or physical form: original English C64 base edition; no claim that every port is reviewed.
- Mechanical families: `FAM-004` matching and combination, `FAM-006` spatial assembly, `FAM-010` live system pressure and `FAM-013` inventory/fixture dependencies. Pitch/fragment compatibility, geometric card assembly, guarded search under a deadline and utility/password-gated fixtures each have a causal boundary.
- Primary sources accessed 2026-10-02:
  - **P1:** [Licensed Retro Games C64 instructions](https://retrogames.biz/games/c64/impossible-mission/), full English manual reproduction read. Original rules are separated from the explicitly modern THEC64 menu instruction; humorous fictional robot specifications are not measured physics.
  - **P2:** [Dennis Caswell interview](https://www.mayhem64.co.uk/interview/caswell.htm), indexed creator answers about nine-letter passwords and mental reflection/superposition were read. Full-page retrieval failed; no claim to have read the complete interview or inspected his source listing.
- Independent written sources:
  - **S1:** [Data Driven Gamer's original-C64 first-hand account](https://datadrivengamer.blogspot.com/2022/08/game-333-impossible-mission.html), 26 August 2022, complete main article read. Corroborates expendable tokens, live penalties, pitch sorting, paid help and completed-card gate. Its subjective collision judgements and exact alternation claims are not imported as measured binary facts.
  - **S2:** [The Commodore Zone room-guide introduction](https://www.the-commodore-zone.com/articlelive/articles/25/2/Impossible-Mission/Page2.html), 2006, main introduction read. Supports route context, code scarcity, corridor computer and password assembly; its 31-room figure differs from the booklet's 32-room description and is not used as an independent exact total. Its emulator snapshots are explicitly excluded.
- Claim IDs: `IM-001`–`IM-010`. Original binary behaviour, native standard and timing remain separate research questions.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008` for direct walking/jumping, `ACT-216` for the reachable held search command, and `ACT-341` for contextual terminal and completed-password door activation.
- `ACT-644` manipulates a retained fragment/composite workspace, not a world-map tile or capacity-packed inventory; `ACT-645` reverses only the latest eligible delete/join; `ACT-646` chooses mission-time-priced orientation or inventory help; `ACT-647` submits pitch-sorted squares rather than repeating a cue sequence; `ACT-648` directly moves a lift while occupying it. `IM-001`, `IM-003`–`IM-008`.

### System Behaviour Genes

- Reuse `SYS-004` for new-game selection/rearrangement without claiming its distribution, `SYS-045` for autonomous guard/orb locomotion, and `SYS-057` for eligible perception-triggered pursuit. No uniform omniscience, combat resource or health gauge is inferred.
- `SYS-1273` settles held search, room-local partial retention/reset and revealed typed acquisition; `SYS-1274` spends a matching token to apply local temporary disabling or lift reinitialisation; `SYS-1275` joins eligible fragment copies and recognises an oriented four-piece card into a letter; `SYS-1276` awards a code and lengthens a successful pitch challenge; `SYS-1277` charges a fixed mission-time penalty on a lethal return rather than consuming a finite life; `SYS-1278` aggregates the terminal clock/finding/card/completion score. Help charges are parameters of `ACT-646`, not a second death system. `IM-002`–`IM-010`.

### Constraint Genes

- Reuse `CON-068` for terminal deadline expiry and `CON-296` for token/password authority at a protected fixture.
- `CON-749` restricts puzzle-computer activation to elevators/corridors; `CON-750` distinguishes permissive same-colour non-overlap joins from an oriented complete-card solution. `CON-319` is Raider-specific uninterrupted search and does not capture room-local resumed progress. Lethal contact is recoverable until the mission deadline, so `CON-006` does not transfer. `IM-003`, `IM-006`–`IM-009`.

### Information Genes

- Reuse `INF-003` for fixed but concealed furniture contents and `INF-179` for visible local geometry, guards and fixtures. No exact hostile-program preview is provided.
- `INF-460` discloses context-dependent visited map, search bar/results, code counts, fragment workspace, letter progress, mission clock and paid orientation/partner feedback. Ordinary map availability is different from a globally revealed room inventory. `IM-002`, `IM-003`, `IM-006`–`IM-010`.

### Objective Genes

- `OBJ-273` completes the fragmented password then uses its room door before mission expiry. Guessing a known word or merely collecting all fragments is insufficient.
- Reuse `OBJ-002` for improving terminal numerical score independently of mission completion. Exact manual weights are parameters: remaining seconds, found pieces/codes, solved cards and success contribute separately. `IM-007`, `IM-009`.

### Time Genes

- Reuse `TIM-003` for running movement, guards, held searches and the mission clock while input remains available. Paws is an ordinary explicit pause, not permission to issue frozen tactical orders or an unlimited untimed solve. Exact freeze/restart/terminal menu scheduling is unmeasured; no port timing is borrowed. `IM-001`–`IM-009`.

## Reproducible transitions

| Before | Action | Deterministic resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Agent stands on a striped room lift | Hold vertical direction | Lift carries its occupant along its permitted vertical travel | Direct occupant control, not a remote switch trajectory | IM-001 |
| Reachable furniture, search incomplete | Hold up; interrupt; resume without leaving | Remaining progress resumes and completion reveals its result | Not an instant loot click or mandatory all-or-nothing hold | IM-003 |
| Partially searched furniture | Leave and re-enter its room | That unfinished search starts again | Partial retention is room-local, not mission-persistent | IM-003 |
| Search reaches completion | Finish held channel | Nothing, code or fragment is revealed; eligible discovery is retained | Concealed result and automatic transfer, not visible contact loot | IM-003 |
| Terminal reached with matching code | Select room disable or lift reset | One-use token enables its typed local effect | Temporary freeze is not robot destruction; lift reset is not world rewind | IM-004 |
| Presented code-room note squares | Select low-to-high pitch order | Correct response grants utility code; next challenge grows | Not Simon's presented-order replay | IM-005 |
| Agent in a room versus corridor | Request pocket computer | Room fire jumps; corridor/elevator activates editing workspace | Same input has location-dependent affordance | IM-006 |
| Two different-colour or overlapping fragments | Attempt superposition | Ineligible join is rejected | Geometry and colour matter separately | IM-007 |
| Same-colour non-overlapping fragments from wrong card | Join | Partial combination is permitted but may not complete a valid card | Legal local join does not prove global solution | IM-007 |
| Four matching fragments, reversed complete card | Reflect into required orientation | Recognised solution contributes one password letter | Complete silhouette alone is insufficient | IM-007 |
| Displayed piece removed or pair just joined | Use recent undo | Eligible last deletion/join is reversed | Display deletion did not delete the retained memory; not simulation rewind | IM-006 |
| Two window pieces or incomplete upper card | Call chosen Agency help | Charge two game minutes; orient pieces or disclose partner availability | Time pays for information/correction, not a hint coin | IM-008 |
| Bottom fall, orb collision or lethal robot zap | Continue after failure | Charge ten game minutes and resume while budget permits | No fixed finite-life counter; exact return location unmeasured | IM-002, IM-009 |
| All nine recognised letters and time remains | Reach and activate control-room door | Mission completes and terminal score is settled | Collection or remembered word alone is insufficient | IM-007, IM-009 |
| Clock reaches 6:00 without completion | No completed entry | Attempt ends and terminal score reflects achieved progress | A lower score is not successful mission completion | IM-009 |

## Strategic and experiential structure

Observe guard behaviour before committing a long furniture search. A utility token can buy safer search time, but earning replacements costs time and increasingly demanding pitch sorting. Room departure sacrifices incomplete search; completing a difficult object before moving can preserve work. Puzzle edits themselves permit locally plausible wrong joins, so reflection, undo and paid orientation/partner information trade mental effort against the same mission budget that funds lethal retries. These are source-supported decisions, not an optimal route or quantitative success prediction. `IM-002`–`IM-009`.

## Replay and variation

New original missions change room placement, robot configuration and puzzle fragments. A completed run can seek a better score by preserving time, finding resources and solving cards; no seed distribution or universally solvable generated layout was tested. The manual documents native new-game input, whereas THEC64's separate restart and emulator snapshots are not original reversible time. `IM-009`, `IM-010`.

## Adjacent systems and history

Caswell's indexed answer directly contrasts mental reflection/superposition with robot avoidance. This supports the mixed loop, not an inferred lineage from numerical corpus neighbours. Sequel towers and later-port controls do not enter the original packet. The original manual's room total and the guide's room catalogue differ, so the latter does not establish an exact independently corroborated count. `IM-001`, `IM-007`, `IM-010`.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
|---|---|---|
| Action | `ACT-008`, `ACT-216`, `ACT-341`, `ACT-644`–`ACT-648` | direct movement, search, fixtures, fragment editing, undo, help, pitch order, occupied lifts |
| System Behaviour | `SYS-004`, `SYS-045`, `SYS-057`, `SYS-1273`–`SYS-1278` | new-game variation, guards, search retention, local token effects, card recognition, code reward, death-time debit, score |
| Constraint | `CON-068`, `CON-296`, `CON-749`, `CON-750` | mission expiry, authority, computer location, join/solution compatibility |
| Information | `INF-003`, `INF-179`, `INF-460` | hidden contents, visible room, contextual computer/search feedback |
| Objective | `OBJ-002`, `OBJ-273` | independent score and completed-password room entry |
| Time | `TIM-003` | live search/guards/mission clock with ordinary explicit pause |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `483` (`GAME-0001`–`GAME-0483`).
- Exact genome matches: none.
- Tied near matches: `GAME-0430` — Silent Hill (`6 / 43 = 0.139535`).
- Supported combination subsets: none.
- Scan date: 2026-10-02.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0430` Silent Hill | `ACT-008`, `ACT-341`, `SYS-045`, `SYS-057`, `CON-296`, `TIM-003`: live direct traversal, contextual fixtures, autonomous/perceiving hostiles and authorised gates. | The original PlayStation early school route uses fog, map/notes, radio/flashlight information and health/combat resources. The C64 mission instead couples room-local held search, consumable robot/lift codes, reflected/recoloured card assembly and paid help with one deadline that also funds lethal retries. Generic shared traversal does not transfer a health gauge, finite ammunition or punch-card recognition between them. | Near; `6 / 43 = 0.139535`. Shared rule boundaries do not imply historical lineage or experiential equivalence. |

## Taxonomy impact

`TAXONOMY_CHANGE_221` admits fifteen bounded additions and twelve unchanged reuses. A named causal-role review partitions all twenty-seven uses. No earlier definition, signature, verified combination or platform identity changes.

## Negative results

- Reject Simon's presented-order replay for pitch sorting; a packed attaché case or world-map fragment for editable punch-card overlays; free simulation rewind for last-delete/join undo; and a currency coin for mission-time-priced help.
- Reject a life-stock game over, permanent robot removal for temporary disabling, instant search, mission-persistent incomplete search, and guessing a known word instead of recognising nine cards.
- Reject importing THEC64 menu restart, emulator snapshots, sequel saves or a native-standard bug from uninspected executable variants. Robot speeds, penalties, card/letter counts and score weights remain parameters.

## Delta summary

## New facts

- [Observation | Direct | High] Original documented search keeps unfinished progress only inside its room; puzzle joins can be locally legal yet globally wrong. `IM-003`, `IM-007`.
- [Observation | Corroborated | High] Pitch sorting, guarded searching and card recognition share one mission budget with paid help and lethal retry penalties. `IM-005`–`IM-009`.

## New genes

- [Observation | Direct | Medium] Fifteen boundaries preserve the original search/overlay/clock loop without new names for individual furniture, pitches or numerical parameters.

## New combinations

- [Observation | Limited | Medium] No new verified combination; existing proper subsets are recomputed from the complete admitted signature.

## Taxonomy changes

- [Observation | Direct | Medium] `TAXONOMY_CHANGE_221`; no prior definition or signature mutation.

## New questions

- Execute a lawful native edition to measure clock/pause scheduling, exact death restoration, token decrement, collision/guard programs and fragment-recognition representation. Do not retrofit those unmeasured details into this source-based packet.

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0485` *Shenmue*, original Dreamcast, follows complete acceptance and the Goal stop window.
- Optimisation criterion: change platform and decision structure from timed guarded search/geometric assembly to situated investigation.

## Why this game

- [Hypothesis | Limited | Medium] The approved cross-platform batch tests a classic C64 mixed search-and-assembly loop rather than adding another Nintendo platformer.
