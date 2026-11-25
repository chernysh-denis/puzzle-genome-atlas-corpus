---
game_id: GAME-0733
slug: solomons-key
game_title: "Solomon's Key"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-948
  system:
    - SYS-036
    - SYS-085
    - SYS-1029
    - SYS-2042
  constraint:
    - CON-068
  information:
    - INF-179
  objective:
    - OBJ-164
  time:
    - TIM-003
---

# Game: Solomon's Key — Aries Room 1 on the North American NES cartridge

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Dana, the brown stones, the key and the door are instances of the
scoped traversal and room-clear rules.

## Analysis scope

- Version / ruleset: Tecmo's English North American 1987 commercial
  Nintendo Entertainment System cartridge, documented as NES-KE-USA.
  The first recording shows the English title and a 1987 Tecmo
  copyright. The recording hardware and ROM revision are unverified.
- Entry: start from the title screen and wait for first control in
  ordinary Aries Room 1. The key is visible on the right and the
  lower door is closed. Stop at the Room 2 introduction after the
  first room's score conversion, before acting in Room 2.
- Primary decision loop: move or jump to address a tile, make a
  brown stone to add footing or remove one to open space, then
  reach the key and carry the room state to the opened lower door.
  The active LIFE clock limits how long those steps can take.
- Included: direct running and jumping, stance and facing in block
  placement, fixed and mutable terrain, keyed release, door entry,
  countdown and score settlement. Excluded: optional fireball stock,
  goblin combat, fairies and score items, exact collision windows,
  seal glitches, secret rooms, later fixtures and other ports.
- Direct-play status: no personal cartridge or emulator session.
  The original booklet, period review and two recorded NES routes
  establish the scoped rules. Only silent background frames were
  inspected.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| SK-001 | Tecmo published the North American cartridge in July 1987. The start sequence leads to ordinary Aries Room 1 with a visible key, fixed white masonry, mutable brown stones and a closed lower exit. | Observation | Corroborated | High | P1 cover, P2 p. 11, W1 08:01–08:08, W2 10:10–10:17, S1 |
| SK-002 | Dana runs, crouches and jumps through the side view. Gravity returns him to a support surface or takes him through an unobstructed fall. | Observation | Corroborated | High | P1 pp. 4–5, W1 08:07–08:16 and 08:27–08:33, W2 10:21–10:33 |
| SK-003 | The A input addresses a local tile relative to body position, stance and facing. Standing casts reach ahead. Crouching sends the cast lower, and airborne casting changes the available target through position. | Observation | Corroborated | High | P1 p. 6 and its three diagrams, W1 08:11–08:17, W2 10:25–10:33 |
| SK-004 | In eligible space the same stone magic adds one solid brown stone to an empty tile or removes a brown stone already there. Fixed white blocks are immune. W2 creates an extra left-side foothold. Both routes remove brown terrain on the key approach. | Observation | Corroborated | High | P1 p. 6, W1 08:23–08:28, W2 10:25–10:33 and 10:57–11:01, S1 |
| SK-005 | Reaching the room's key automatically replaces the closed-door image with an open arch. The player remains in control and must reach and enter the arch separately. | Observation | Corroborated | High | P1 p. 8, W1 08:29–08:39, W2 11:00–11:16, S2 |
| SK-006 | LIFE decreases during live movement and editing. Running it out loses the current attempt. The exact initial reserve and decrement cadence are not assumed from the opening title alone. | Observation | Corroborated | High | P1 p. 9, W1 08:07–08:38, W2 10:16–11:15, S2 Room 1, S3 Timer |
| SK-007 | Entry into the unlocked door triggers room settlement. W1 visibly transfers the remaining 37,600 LIFE into score, from 500 to 38,100, then shows the Room 2 introduction and a renewed LIFE count. | Observation | Corroborated | High | W1 08:38–08:44, W2 11:14–11:22, S3 Timer |

## Basic data

- Release / origin: Tecmo, North American Nintendo Entertainment
  System commercial cartridge, July 1987. Target platform
  `PLAT-NINTENDO-ENTERTAINMENT-SYSTEM`, catalogue ID NES-KE-USA.
- Mechanical families: `FAM-005` for adding or removing route
  supports, and `FAM-010` for movement and editing under a clock.
- Primary evidence checked 2026-11-25:
  - **P1:** [Tecmo's North American instruction booklet](https://www.gamingalexandria.com/highquality/NES/Solomon%27s%20Key/Solomon%27s%20Key%20-%20Manual.pdf).
    Printed pp. 4–6 specify posture, movement and block magic.
    Printed pp. 8–9 distinguish key pickup, entry and LIFE.
  - **P2:** [Nintendo of America's licensed NES release list](https://manuals.plus/m/85a9f766719c1047cdc259909dd061316c12c63383d5b0a46424e73de23dc084.pdf),
    mirrored PDF p. 11. The list records Tecmo and July 1987.
- Recorded and independent evidence:
  - **W1:** [Jason Smith's NES Room 1 recording](https://www.youtube.com/watch?v=OUkyExEZu1M&t=481s).
    Shows the title, key approach, open door, settled LIFE
    credit and the Room 2 introduction. Read the displayed
    values rather than measuring video playback time.
  - **W2:** [Video Games 101's NES opening](https://www.youtube.com/watch?v=4yI6Z1Is-Po&t=610s).
    Shows repeated movement and casting on the left, the later
    key pickup and the same independent exit event.
  - **S1:** [Computer Entertainer, August 1987](https://www.ataricompendium.com/archives/newsletters/video_game_update/computer_entertainer_aug87.pdf),
    the NES review and availability listing. The review independently
    describes the Aries opening and stepping-stone placement and removal.
  - **S2:** [TVotava's NES walkthrough](https://gamefaqs.gamespot.com/nes/570522-solomons-key/faqs/10324),
    Room 1. Verifies which initial visible item is the room key and
    distinguishes the time limit and optional local activities.
  - **S3:** [Speed Demos Archive's NES mechanics notes](https://kb.speeddemosarchive.com/Solomon%27s_Key_%28NES%29/Game_Mechanics),
    Timer. Describes the live drain and separate post-room countdown.
- Claim IDs: SK-001–SK-007. Read positions and state changes
  in the recorded room. Exact cartridge chips, timing and
  display capture configurations remain unverified.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: run, crouch and steer jumps locally through the room (SK-002).
- New `ACT-948`: cast at the local tile selected by facing, stance and current body position (SK-003).

### System Behaviour Genes

- Reuse `SYS-036`: resolved support and collisions govern jumps and falling after terrain edits (SK-002, SK-004).
- Reuse `SYS-1029`: reaching the opened terminal converts remaining room time to score (SK-007).
- New `SYS-2042`: toggle occupancy at the addressed mutable cell. A new stone provides support or an obstacle. Removing it frees the same cell (SK-004).
- Reuse `SYS-085`: collecting the sole required token makes the fixed exit eligible. The room settles only after entering that exit (SK-005).

### Constraint Genes

- Reuse `CON-068`: finish before the active LIFE reserve reaches zero (SK-006). The block edit restrictions belong to the edit resolution.

### Information Genes

- Reuse `INF-179`: the room view shows Dana, wall classes, key location and the door's closed or open state (SK-001, SK-004, SK-005).

### Objective Genes

- Reuse `OBJ-164`: enter the keyed door, settle the room and carry the accumulated score into Room 2 (SK-005, SK-007).

### Time Genes

- Reuse `TIM-003`: route edits and movement take place while the room clock and body dynamics continue (SK-002, SK-006).

## Formal state and transitions

Track Dana's position, facing, stance, velocity and support, the
room's fixed and mutable tiles, the key credit, door state, LIFE
and accumulated score. The cast first selects a local tile from
the actor state. The result depends on that tile's occupancy
and eligibility. A subsequent jump or fall uses the new geometry.
Key contact releases the gate. Entering it triggers a separate
score transfer before the successor room.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Claim ID |
| --- | --- | --- | --- |
| Below a higher traversable ledge, beside a reachable empty tile | Cast toward the tile | Add one solid brown block that can serve as footing | SK-002–SK-004 |
| A brown block occupies the addressed space | Use the same magic on it | Remove the block and open that tile | SK-004 |
| Fixed white masonry is the target | Try the stone magic | The fixed tile remains | SK-004 |
| Key remains visible and door is closed | Reach and collect the key | Key is credited and the door opens while the room remains live | SK-005 |
| Door is open and LIFE is positive | Reach and enter the door | The attempt settles, remaining LIFE credits score and Room 2 is announced | SK-006, SK-007 |

## Strategic and experiential structure

A created block can shorten a climb or block a future passage.
Casting posture matters when the useful cell is below the
current target line. Opening the door gives a destination but
leaves the descent and approach to the player. Optional detours
spend live clock reserve and can change the score before the exit.

## Replay and variation

The first recording visits optional items before leaving.
The second takes longer on the left to demonstrate stepping stones.
Both show the same right-side key and independent lower exit.
The observed allocations and scores belong to their individual routes.

## Adjacent systems and history

The original booklet describes stone-prohibited marks, headbutt
breakage, fireball stock and other enemies. They are outside this
key route's admitted rule set. Later NES rooms, the arcade edition
and ports are outside the version and entry boundary.

## Normalised genome

- Action: ACT-008, ACT-948.
- System Behaviour: SYS-036, SYS-085, SYS-1029, SYS-2042.
- Constraint: CON-068.
- Information: INF-179.
- Objective: OBJ-164.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `732` (`GAME-0001`–`GAME-0732`).
- Exact genome matches: none.
- Tied near matches: `GAME-0706` — Kula World (`5 / 14 = 0.357143`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Kula World (GAME-0706)](../g-l/kula-world.md) | ACT-008, CON-068, OBJ-164, SYS-085, TIM-003 | Both navigate under a live deadline, take the required key and then reach the activated exit. Kula World reorients the ball's support frame while rolling across existing faces. Solomon's Key changes the route itself by adding or erasing a block, then uses the changed support for jumps and falls. | Near, `0.357143`. |

## Taxonomy impact

Separate cast addressing from occupancy resolution. A standing cast
and a lower crouched cast are parameters of the same action. The
added stone changes subsequent collision geometry, while the key
changes the exit's eligibility without changing the supporting stones.

## Negative results

- White masonry is immutable under the brown-stone rule.
- The closed door and the separate key prevent bare destination contact
  from completing the initial room.
- Key contact alone leaves the clock and room play active.

## Delta summary

Capture the opening room's local geometry edits, keyed access and
remaining-clock credit as distinct transitions.

## New facts

- A cast's target moves with Dana's facing, posture and position.
- The same magic forms an eligible block or removes one.
- The key opens the door without ending the attempt.

## Principles and design implications

Allow a small reversible edit to change route reachability. Use
the visible key and door states to keep the collection and escape
goals legible while the floor is changing.

## Puzzle or game generation potential

Build a room with permanent walls and a single editable step,
a visible key and a separate keyed exit. Require both a positive
support change and an erasure in the route fixture. Record clock
and score at the door rather than awarding the clear at key contact.

## New genes

- ACT-948
- SYS-2042

## New combinations

None. No verified combination is a proper subset of the signature.

## Taxonomy changes

[Taxonomy Change 479](../../../research/taxonomy-changes/TAXONOMY_CHANGE_479.md).

## Next recommended game

Nex Machina on the English Windows Steam release is the next Selection 064 unit.

## Why this game

The room's platforms are a player-controlled variable during
a running attempt. After the key changes the door's state,
the player still has to navigate the altered room to escape.

## Review status

Reviewed 2026-11-25 for the first ordinary room of the North American
NES cartridge and the introduction to Room 2.
