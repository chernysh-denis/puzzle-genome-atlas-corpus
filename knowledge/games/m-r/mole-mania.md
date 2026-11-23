---
game_id: GAME-0614
slug: mole-mania
game_title: "Mole Mania"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-009
    - ACT-815
    - ACT-816
  system:
    - SYS-1808
    - SYS-1809
  constraint:
    - CON-855
  information:
    - INF-179
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: Mole Mania

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Two aligned room layers, one black ball and one destructible exit wall
are fixed instances in this packet.

## Analysis scope

- Version / ruleset: North American Nintendo Game Boy cartridge
  DMG-AMOE-USA, printed Nintendo instruction booklet and English
  one-player Quest Mode, commercial release of February 1997.
  The recordings show the original English game with presentation
  palettes. Their cartridge checksums and capture hardware are unreported.
- Primary decision loop: inspect the current surface and underground
  room, choose legal burrow and emergence positions to change the
  side from which the black ball can be handled, guide the ball past
  surface obstacles, then hit the exit wall and cross the opened edge.
- Entry: take the east passage from Grandpa's paved fountain room
  into the first Level 1 ball-and-cabbage room, labeled D3 by
  Koldstare. The west entrance, grass, black ball, moving occupants
  and blocked east edge identify the room independently of that label.
- Exit: cross the east edge after the black ball breaks the wall.
  The first rendered successor is the Level 1 tree-lane room D4.
  Stop on arrival before taking actions there.
- Included: legal layer changes, local movement, black ball and cabbage
  positioning, grab-and-hold throw, holes, the visible live opponents,
  the black-ball wall strike, and the separate actual eastward exit.
  The level-map pickup is a documented detour, separate from wall clearance.
- Excluded: Level 1 boss and other rooms as gameplay targets, full level
  scoring, cabbage-count and heart maximization, the later locator,
  recovery purchases, Vs. Mode, colorization patches, Japanese cartridge
  and 3DS Virtual Console release. No exact charge duration, object
  collision coefficient or save-reload claim is made.
- Suggested later scope: test Level 1's boss separately from the puzzle
  rooms, including his environmental loss condition and the result.

## Direct-play status

No cartridge or ROM was run by the analyst. Nintendo's North American
booklet identifies the original moves, side effects and objective;
a photographed US cartridge, box and booklet tie the code to the
commercial product. Two independent English recordings corroborate the
local room shape, separate layer use or surface positions, open east
edge and arrival in the next room. They do not establish that the
capture used the exact North American cartridge copy or an unmodified
console. The room index and solution cross-check use an independent
written walkthrough. Only written material and static frames were
inspected, with no video or audio playback.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| MM-001 | The target is the released English Game Boy Quest Mode. D3 is the room east of Grandpa's fountain, and this packet stops upon reaching D4. | Confirmed | Corroborated | High | P1, P2, P3, S1; W1 6:10–6:20 and 7:20; W2 5:50–6:30 and 7:20. The room labels are from S1. |
| MM-002 | A switches between surface and underground through eligible terrain or holes. Hard terrain refuses a new hole; underground rock changes the set of paths and emergence points. | Confirmed | Corroborated | High | P1 pp. 4–5 and 12–13; W1 2:10 shows the hard-ground sign, and 6:40 the D3 underground route. Emergence timing was not measured. |
| MM-003 | Muddy uses an available tunnel to change sides independently of the black ball. The black ball cannot be carried underground. A hole encountered by the ball returns it to its starting position. | Confirmed | Corroborated | High | P1 pp. 6–7 and 12–13; W1 6:30, 6:40 and 6:50 show the ball above, Muddy below and both back on the surface; S1 gives the side-changing route. The ball-hole sign is shown at W2 3:00; P1 gives the reset outcome. |
| MM-004 | With movement, nearby props can be pushed or pulled. Holding B on a prop while still reaches a ready glow; a direction then issues the throw. | Confirmed | Corroborated | High | P1 pp. 4–5 and 12–13; W2 3:00 and 4:00 show the black-ball and throw tutorials, S1 D3 records the throw across Muddy's contact side. No ready timing is inferred. |
| MM-005 | The surface view shows independent moving opponents, obstacles, ball and gate state. Surface opponents move independently while the player controls Muddy. | Observation | Direct | High | W1 6:20 and 6:30 show different opponent positions at the same fixed scenery; W2 6:10–6:30 and S1 corroborate the local behavior. The gate's published condition is ball impact. The footage does not measure an idle interval or a relation between kill count and final score. |
| MM-006 | The ball strikes the east exit wall. The edge is open afterward, but the route completes with Muddy's actual eastward movement into the next room. | Confirmed | Corroborated | High | P1 pp. 6–7; W1 6:50 shows black ball at the east barrier, with D4 visible at 7:20. W2 6:30–7:10 shows the broken east edge while still in D3 and 7:20 shows D4. S1 confirms throw, detour and eastward departure. |
| MM-007 | A cabbage entering a hole is deposited rather than returning to its starting position as the black ball does. The optional level-map detour follows the opened gate in the recorded route. | Observation | Corroborated | High | P1 pp. 6–9; S1 D3; W2 6:10 and 6:40–7:10 show the cabbage instruction, removal sequence and map notice. W1 7:00–7:10 samples the separate underground detour. Do not infer that opening the wall requires the map. |

## Basic data

- Origin: Nintendo's commercial Game Boy puzzle adventure. The US
  box and booklet carry DMG-AMOE-USA and copyright 1996, distinct
  from the February 1997 North American retail date.
- Analysis target: `PLAT-GAME-BOY`, North American English Quest
  cartridge, Level 1 D3 room only.
- Mechanical families: `FAM-007` for moving and releasing manipulable
  props to change the spatial state, and `FAM-014` for planning
  around altered layer adjacency. Bionic Bay independently supports
  the first family, and FEZ supports the second.
- Sources checked 21 November 2026.
- P1: [Nintendo of America instruction booklet DMG-AMOE-USA](https://www.gamesdatabase.org/Media/SYSTEM/Nintendo_Game_Boy/manual/Formated/Mole_Mania_-_1997_-_Nintendo.pdf).
  Printed pp. 4–9 and 12–13 give the inputs, ball's hole response,
  goal and movement. The booklet identifies North American use.
- P2: [Photographed US box, booklet and cartridge](https://www.game-boy-database.com/game-AMOE-1286-USA.html).
  The 961202 marking is a production code, not the retail release date.
- P3: [Nintendo Game Boy release catalogue, historical mirror](https://www.digitpress.com/lists/nintendo_oldgames.pdf).
  The Mole Mania entry states February 1997.
- P4: [Nintendo's title description](https://www.nintendo.com/en-gb/Games/Game-Boy/Mole-Mania-641354.html).
  Official title and broad dig-to-find-paths description. Its
  2012 date belongs to the associated reissue context, not P3.
- W1: [Johnny Game Over, English original room trace](https://www.youtube.com/watch?v=_VhVd6xaRpA&t=370s).
  The early Level 1 samples show Grandpa at 6:10, ball manipulation
  at 6:20 and 6:30, underground travel at 6:40, the ball at the east
  exit at 6:50, and the next tree-lane room at 7:20.
- W2: [BackGroundGaming Longplays, English Mole Mania](https://www.youtube.com/watch?v=WKY3Mc8R-sc&t=350s).
  Grandpa at 5:50, cabbage sign at 6:10, missing wall at the east
  edge at 6:30, map notice at 6:50 and 7:00, and D4 at 7:20.
- S1: [Koldstare's Level 1 route and D3 reference](https://gamefaqs.gamespot.com/gameboy/585807-mole-mania/faqs/32710).
  Cross-check of the room's connections, throw, repositioning,
  cabbage disposal, east wall and successor boundary.

## Mechanical decomposition

### Action Genes

- ACT-008: walk the current legal surface or subterranean route.
- ACT-009: reposition one adjacent surface prop by pushing.
- ACT-815: dig or enter a hole, then surface at an eligible coordinate.
- ACT-816: grab an adjacent prop, wait for the ready cue, then send
  it in the intended direction. This is distinct from ordinary
  pushing or pulling while moving.
- Claim IDs: MM-002–MM-004, MM-006.

### System Behaviour Genes

- SYS-1808: compatible ball contact removes the authored exit wall,
  exposing the route for a separate movement by the player.
- SYS-1809: the same hole treats the two eligible prop types
  differently. The ball resets to its origin. A deposited cabbage
  leaves the board and is credited as a cabbage.
- Claim IDs: MM-003, MM-006, MM-007.

### Constraint Genes

- CON-855: distinct terrain governs the two aligned layers. Only
  eligible positions connect them, and the black ball stays
  within its surface layer or resets to its surface origin.
- Claim IDs: MM-002, MM-003.

### Information Genes

- INF-179: view the body, moving opponents, current terrain, ball,
  hole markers and visible exit state. While underground the
  exposed surface layout is replaced by the local lower map.
- Claim IDs: MM-002, MM-005, MM-006.

### Objective Genes

- OBJ-026: use the now-open east edge and actually enter D4.
  Neither breaking the exit wall nor collecting the map completes
  the scoped room by itself.
- Claim IDs: MM-006, MM-007.

### Time Genes

- TIM-003: surface opponents move while actions can be supplied.
  Their positions matter when walking or routing the ball. No
  whole-room countdown or exact input window is claimed.
- Claim IDs: MM-004, MM-005.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Surface approach blocked by the prop or local terrain | Use A on an eligible location, travel below ground and use A at a valid emergence | Muddy reaches a different side; the ball still needs a separate surface operation | Layers separate body approach from prop travel | MM-002, MM-003 |
| An adjacent prop is in reach | Push to reposition, or hold B in place for the ready cue before choosing a direction | The first action changes a neighboring position; the prepared throw advances the prop away | Side access and launch direction determine the lane | MM-004 |
| An inconvenient cabbage is next to a hole | Send the cabbage into the opening | It leaves the surface and is a deposited cabbage | A hole can clear a lane | MM-007 |
| The required black ball is directed into a hole | Allow contact to settle | P1 specifies return to initial position, with no lower-layer possession | The same opening is a liability for routing the ball | MM-003 |
| The ball can now reach the east exit wall | Send the black ball into the wall | The east barrier breaks while Muddy remains in the current room | Opening and crossing are distinct | MM-006 |
| East edge is open | Walk across the edge after any optional detour | The next room renders with its own tree lanes and actors | Cleared exit gives actual room-to-room continuation | MM-006, MM-007 |

## Strategic and experiential structure

The surface must leave a viable ball lane while the lower layer
provides access to different contact sides. A useful burrow can
be a trap for the very object needed at the exit. Placing an
opening to remove an obstructing cabbage is useful only if the
ball can still reach the wall. Surface opponents add situational
pressure. The authored wall is a target for the ball and the open
edge is subsequently a destination for the avatar. MM-002–MM-007.

## Replay and variation

The independent traces use the same authored D3 terrain but take
different amounts of time, make different dirt openings and reach
the next room. The instructional rule for a ball falling in a hole
describes a prop reset, not an automatic return of the entire room.
No fixed route timing, charge duration or exact recovery state on
power cycle is claimed. MM-003–MM-007.

## Adjacent systems and history

The lower layer is local to this room, unlike Pitfall!'s faster
multi-scene underground ring. The level-map detour explains why the
two traces continue in D3 briefly after a broken wall is visible.
Level completion, the boss and alternate modes are separate scopes.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-009, ACT-815, ACT-816 | Move, push, change layers and throw |
| System Behaviour | SYS-1808, SYS-1809 | Break the wall and settle prop-dependent holes |
| Constraint | CON-855 | Gate movement and layer transitions by terrain |
| Information | INF-179 | Read current terrain, threats, props and exit |
| Objective | OBJ-026 | Reach the adjoining eastern room |
| Time | TIM-003 | Choose during live surface motion |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `613` (`GAME-0001`–`GAME-0613`).
- Exact genome matches: none.
- Tied near matches: `GAME-0599` — Sword of the Sea (`4 / 16 = 0.250000`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Sword of the Sea (GAME-0599)](../s-z/sword-of-the-sea.md) | ACT-008, INF-179, OBJ-026, TIM-003 | Both require moving the avatar through a visible evolving route and reaching the actual destination after the path opens. Sword of the Sea uses Hoversword momentum, a prepared high jump and water restoration. Mole Mania changes the angle of access by burrowing between two layers, moves the black ball along the surface and breaks one exit wall before crossing. | Near, `0.250000` |

## Taxonomy impact

- [TAXONOMY_CHANGE_360](../../../research/taxonomy-changes/TAXONOMY_CHANGE_360.md)
  records controlled layer transition, held throw, compatible impact,
  per-prop hole handling and terrain eligibility.

## Negative results

- ACT-772 opens adjacent lower bricks in Lode Runner. Mole Mania
  switches the player between two aligned room states at the
  addressed coordinate.
- SYS-1244 crosses unequal scene strides on a circular route, not a
  two-layer path inside one room.
- ACT-630 describes pulling a block that becomes a usable climb step.
  Here pulling is a control for freely repositioning the surface
  prop. No additional climb-support effect is present.
- ACT-078 omits the grab and ready phase. No ball direction is
  selected freely from anywhere in the field.
- SYS-1754 needs a separate explosive hazard at contact. The D3
  route uses the black ball itself to break the authored wall.
- Defeating all enemies, collecting the map, filling the cabbage
  total and solving the boss are not the documented east exit rule.

## Delta summary

## New facts

- [Confirmed | Corroborated | High] A local digging route gets Muddy
  to the correct contact side while the black ball remains a
  surface prop. MM-002, MM-003.
- [Observation | Corroborated | High] Cabbages can leave the surface
  through holes that would reset the required ball. MM-003, MM-007.
- [Confirmed | Corroborated | High] The compatible ball clears the
  barrier; the player's later eastward crossing settles the exit.
  MM-006.

## New genes

- [Observation | Corroborated | Medium] ACT-815, ACT-816, CON-855,
  SYS-1808 and SYS-1809.

## New combinations

- [Observation | Direct | High] No new combination admitted.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_360.

## New questions

- How is the original room restored if a blocking hole is dug
  then Muddy leaves and later revisits?
- Does a thrown ball skip a hole it would enter under a push on
  exactly the same horizontal line?
- How does collision with the east wall interact with a missed
  optional item on a verified power-cycle save?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0615`, Skate Story, the
  commercial PlayStation 5 release. Trace one complete early trial
  whose input and settled result can be seen on that edition.

## Why this game

- [Hypothesis | Limited | Medium] Mole Mania separates a player
  path from a directional object path. The next title offers a
  different kind of movement boundary through committed skate
  inputs and a trial's judged or authored result.
