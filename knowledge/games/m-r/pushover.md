---
game_id: GAME-0715
slug: pushover
game_title: "Pushover"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-048
    - ACT-931
  system:
    - SYS-2003
    - SYS-2004
  constraint:
    - CON-898
    - CON-899
  information:
    - INF-001
  objective:
    - OBJ-374
  time:
    - TIM-003
---

# Game: Pushover

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Repair one gap in an upright domino row, spend one directional push, and
return to the exit after the fixed striped block falls last.

## Analysis scope

- Version / ruleset: original English commercial Commodore Amiga
  floppy release, Red Rat Software and Ocean Software, 1992.
  The commercial listing and the museum's Amiga 600 bundle
  corroborate the product. The training board is shown by two
  Amiga recordings. The precise disk revision is unverified.
- Structured analysis target: PLAT-AMIGA in
  [platform coverage](../../platforms/games.json).
- Entry: start Level 01 from the original option screen. The
  first factory catwalk begins with 30 seconds, ten plain
  yellow blocks and one striped Trigger. There is one vacant
  slot just before the last plain block.
- Primary decision loop: move the ant along the platform.
  Lift the first plain block, carry it into the gap and leave it
  upright. Return to the left edge of the repaired row, enter
  the push position and start the rightward cascade. Walk into
  the opened door while the clock remains positive.
- Positive terminal: the door entry opens the completion panel
  and credits one token. Stop when the Level 02 card appears
  before its platform becomes playable.
- Included: direct navigation, lift and drop, the fixed but
  topplable Trigger, one manual push, local transit of the fall,
  last-block validation, separate door entry and ordinary timed
  credit. The manual's exception for Stoppers and its late and
  failed-attempt token rules delimit the normal success path.
- Excluded: play on later boards, off-platform impacts and falls,
  actively using the special pieces, help and passcode recovery,
  wrapper features, spending a token in the scoped fixture and
  measuring collision, movement or countdown constants.
- Potential scoped module: compare an ordinary retry with a token
  restore of the same pre-push layout and countdown.
- Direct-play status: no personal Amiga or emulator session,
  disk checksum or input telemetry. The manual and the
  contemporary review specify the control and settlement rules.
  Two Amiga recordings show the same first board and finish.
  Neither selected window exercises late completion or token
  spending. Video frames were inspected in the background
  without audio.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| PU-001 | Red Rat Software's Push-Over was an Ocean commercial floppy title for Commodore Amiga in 1992. The frame trace is the English opening factory board. The museum item is an Amiga 600 bundle and corroborates the Amiga release format. | Confirmed | Corroborated | High | P1, R1, R2; W1 0:56–1:01; W2 0:46–0:50 |
| PU-002 | The ant can walk, pick up a reachable movable block, carry it along the level and drop it at another usable placement. In Level 01 the leftmost ordinary block is lifted out, carried right and seated in the only gap near the Trigger. The manual excludes the striped Trigger from relocation. | Observation | Corroborated | High | P1 Controls and Game Play; W1 1:11–1:19; W2 0:52–0:57 |
| PU-003 | From the local push position, a direction plus the push input starts one manual topple. There is one accepted manual push per attempt. Picking up and dropping the earlier ordinary block leaves that push available. | Confirmed | Corroborated | High | P1 Controls and G.I. Ant; R2; W1 1:19–1:22; W2 0:58–1:00 |
| PU-004 | Falling blocks propagate through reachable upright neighbours. In the repaired row the ordinary blocks fall rightward before the fixed, three-striped end block. The manual requires that block to be last, and excludes red Stoppers from the required fallen set. The first board contains no Stopper block. | Observation | Corroborated | High | P1 Game Play and Blocks; R2; W1 1:21–1:25; W2 0:59–1:02 |
| PU-005 | The opened exit is at the left of the catwalk, away from the striped block. The ant remains in the room after the final fall until it returns to the door and enters. The manual also requires a physically clear exit. | Observation | Corroborated | High | P1 Controls and Dos and Don'ts; W1 1:24–1:29; W2 1:01–1:05 |
| PU-006 | Setup, cascade and door entry share one countdown. Timely entry credits one token in both traces. The manual allows spending a token for a solved but late completion or after another failure to restore the pre-push layout and clock. Those two spends were outside the selected windows. | Confirmed | Corroborated | High | P1 Tokens; R2; W1 0:59 and 1:24–1:35; W2 0:47 and 1:02–1:12 |

## Basic data

- Release / origin: Red Rat Software and Ocean Software,
  original commercial Commodore Amiga floppy, 1992.
- Families: FAM-007 for physical propagation between adjacent
  blocks, and FAM-017 for the chain of dependencies from filling
  the gap to the last block and then entering the door.
- P1: [Ocean manual transcribed by Lemon Amiga](https://www.lemonamiga.com/doc/pushover/1302).
  Controls, Game Play, Blocks, Dos and Don'ts and Tokens. The
  archive text was available through its indexed manual copy.
- R1: [Centre for Computing History Amiga floppy catalogue](https://www.computinghistory.org.uk/det/20329/This-Game-Is-No-Push-Over/)
  and [Lemon Amiga commercial release entry](https://www.lemonamiga.com/game/pushover).
  The museum documents an Amiga 600 bundle copy, while the
  commercial entry distinguishes the floppy release and languages.
- R2: [Mark Ramshaw's contemporary Amiga Power review](https://amigaland.com/dataz/press_magazine/AMIGA_Power/PDF_TXT/Amiga_Power_Issue_14_1992_Jun.pdf),
  June 1992, Pushover review spread. Ramshaw's documented
  play corroborates the one-push and last-Trigger rules and
  reports that a token can settle a valid but late completion.
- W1: [The Retro Game Planet, Commodore Amiga opening boards](https://www.youtube.com/watch?v=6tEZ0l0s8AU&t=59s).
- W2: [njenkin, original Amiga opening](https://www.youtube.com/watch?v=Taz_LfyV-qI&t=47s).
  Both videos label the Amiga target. Native disk provenance
  and machine settings were unavailable.

### Reproducible fixture evidence

1. W1 0:59 shows the 30-second display, two red door panels near
   the left side and a single row of blocks. The initial positions
   have one empty slot between the ninth and tenth plain blocks.
   The striped eleventh block starts at the rightmost block position.
2. W1 1:13–1:17 shows the leftmost block changing from standing
   on the floor to carried, then occupying the empty slot. The
   leftmost original slot is now empty beside the exit. In both
   movies the striped block remains where it started.
3. W1 1:21.25 shows the first plain block falling to the right
   while the striped block remains upright. At about 1:23.5
   the last plain block is falling and the striped block is
   beginning to topple. Subsequent frames show all eleven down.
4. The ant is still beside the former push position at 1:25.5,
   when the right-hand red door panel has already opened. It
   moves left and enters the clear doorway. At 1:28 the reward
   panel is visible over the floor and the clock has stopped
   at four seconds. W2 repeats the gap repair, cascade and exit
   around 0:52–1:05, with more time remaining.

## Mechanical decomposition

### Action Genes

- ACT-008: walk the ant along the row and back to the doorway.
- ACT-048: acquire the reachable plain block and carry and
  place it in the vacant slot, preserving the rest of the row.
- ACT-931: take the push posture and commit a directional
  toppling push to a neighbouring upright block.

### System Behaviour Genes

- SYS-2003: process a chain of physical contacts so each falling
  block tips the next reachable upright block in sequence.
- SYS-2004: credit one reusable token on a valid door entry
  while the clock is positive. Manual-documented spending is
  separate from the award observed on this board.

### Constraint Genes

- CON-898: spend at most one initiating manual topple per attempt.
- CON-899: the terminal block is fixed for placement while still
  eligible to fall at the end of the chain.

### Information Genes

- INF-001: the whole catwalk, block positions and visible markings,
  ant, doors and running timer can be read in the same view.

### Objective Genes

- OBJ-374: topple the required blocks before the Trigger, then
  take the door that opens as a separate transition.

### Time Genes

- TIM-003: make arrangement, push and return decisions while
  time elapses and the chain moves. The normal reward window
  closes on expiry, with the documented token branch separate.

### Parameters

Block positions and types, hand occupancy, push stance and side,
remaining manual push, contact reach, last-block order, doorway
access, countdown, and token stock.

## Reproducible transitions

| Entry state | Input or event | Expected next state | Evidence |
| --- | --- | --- | --- |
| Ordinary block at left end, gap near right | Lift the leftmost block and drop it in the gap | Occupied positions form one consecutive row beginning immediately to the right of the doorway | PU-002 |
| Repaired row, usable push | Enter the left push posture and commit a rightward push | First ordinary block topples. The only manual topple is spent | PU-003 |
| Cascade reaches the right-hand end | Let falling blocks make contact | Ordinary blocks go down first, then the fixed striped Trigger | PU-004 |
| All required blocks have fallen and Trigger fell last | Return to the opened doorway and enter | The level settles separately from the last fall | PU-005 |
| Valid layout and timely door entry | Finish the normal attempt | The result credits one token and proceeds to Level 02 | PU-006 |

## Strategic and experiential structure

The first block can repair the distant gap. Taking it from the
left also leaves a useful approach to the door. The single push
tests the entire arrangement all at once, while the door and clock
reserve a short action after the simulated chain.

## Replay and variation

Both openings repeat the same candidate placement and push.
They differ in time spent walking and initiating the chain.
The before-deadline exits show the same result with different
times left.

## Adjacent systems and history

The manual documents Stopper exemptions, other reactive block types,
pausing for a legend, and an overrun hint. Its optional token spend
can restore the arrangement and time at the push point after a
failed layout, or settle a valid late completion. The two selected
first-board runs establish the award and ordinary transition.

## Normalised genome

- Action: ACT-008, ACT-048, ACT-931.
- System Behaviour: SYS-2003, SYS-2004.
- Constraint: CON-898, CON-899.
- Information: INF-001.
- Objective: OBJ-374.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `714` (`GAME-0001`–`GAME-0714`).
- Exact genome matches: none.
- Tied near matches: `GAME-0112` — Human: Fall Flat (`4 / 14 = 0.285714`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Human: Fall Flat (GAME-0112)](../g-l/human-fall-flat.md) | ACT-008, ACT-048, INF-001, TIM-003 | Both move an avatar and reposition a visible physical object with live timing. Pushover spends one directional action on a contact chain with a designated final block. The scoped Human: Fall Flat route uses embodied grasp, load and traversal under continuous physics. | Near, `0.285714`. |

## Taxonomy impact

Reuse avatar movement, rigid-object handling, current board visibility
and live pacing. Isolate directional toppling posture, the single
manual push budget, the fixed terminal piece, sequential contact
propagation, the timed token result and the ordered exit predicate.

## Negative results

- The slots left and right of the repair are on the same catwalk.
  No bridge or multiple-tier mechanism is needed.
- The Trigger stays in its original slot throughout setup.
- Its fall alone leaves the ant outside the exit and the clock active.
- The captures do not establish behaviour on the late or failed branch.
- Ordinary blocks in the chain are plain. The three bands identify
  the single designated terminal member in this fixture.

## Delta summary

Reposition one ordinary block to make a continuous reach path.
Start the cascade with one directional push. Preserve the last-fall
order and still walk through the door before time runs out.

## New facts

- Setup can relocate ordinary dominoes while keeping the marked
  last block fixed in position.
- The automatic topples consume no later manual push.
- The door check and the time-dependent token award occur after
  the final piece falls.

## Principles and design implications

Separate the placement phase from the initiation budget. Make
a required last event legible in advance. Place the exit so a
locally valid cascade still leaves a meaningful return route.

## Puzzle or game generation potential

Generate one row with a single missing contact and an immovable
striped target. Certify at least one legal arrangement with all
required pieces down before the target, then prove a separate
safe exit before the normal reward window closes.

## New genes

- ACT-931
- CON-898
- CON-899
- OBJ-374
- SYS-2003
- SYS-2004

## New combinations

None.

## Taxonomy changes

[Taxonomy Change 461](../../../research/taxonomy-changes/TAXONOMY_CHANGE_461.md).

## New questions

- Does equal-time contact on separate branches count as simultaneous
  with the Trigger or leave its last-block requirement unsatisfied?
- Which objects and time are restored by a token compared with
  restarting the board without spending one?

## Next recommended game

Continue Selection 062 with Terra Nil, the English Windows Steam
commercial base game. Follow the opening restoration sequence from
power and soil preparation to the required vegetation target.

## Why this game

The introductory board makes the chain mechanical and visible,
yet still separates preparation, manual initiation, cascade order
and the actual exit.
