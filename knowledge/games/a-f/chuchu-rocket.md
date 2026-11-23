---
game_id: GAME-0589
slug: chuchu-rocket
game_title: ChuChu Rocket!
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-006
    - ACT-042
  system:
    - SYS-045
    - SYS-048
    - SYS-055
    - SYS-1736
    - SYS-1737
  constraint:
    - CON-001
    - CON-047
  information:
    - INF-001
  objective:
    - OBJ-321
  time:
    - TIM-009
---

# Game: ChuChu Rocket! — Head-on crash

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Place one Up arrow to divert the patrolling cats so the mouse can reach its
rocket. Once the trial begins, the animals follow the board and its commands.

## Analysis scope

- Version / ruleset: English North American Sega Dreamcast retail base game,
  2000, product MK-51049. Single-player Puzzle Mode, Normal, Stage 10,
  “Head-on crash”, under the original controller rules. The video sources
  establish the board and outcomes without authenticating the exact disc
  revision, regional binary or emulator timing.
- Structured analysis target: PLAT-DREAMCAST.
  See [platform coverage](../../platforms/games.json).
- Entry: Puzzle → Normal → Stage 10 with the actors at their initial
  positions, no marker placed, and one Up panel available.
- Primary decision loop: read the animals' positions, headings and walls.
  Predict their paths, place the available oriented command on an eligible
  tile, and start the trial with R. Watch both species take their routes.
  R can accelerate a running test. Cancel with L to retry from the setup.
- Positive exit: the required mouse reaches the rocket without a failed
  delivery. The recorded run shows “Stage 10 CLEARED!” before the next
  board. Stop at the clear screen.
- Negative exit: a mouse eaten or a cat entering the rocket fails the
  puzzle. The booklet also establishes falling into a hole as a Puzzle
  Mode failure, but there are no holes on this board. A live cancel is
  distinct from an automatic failure.
- Included: authored 12-column by 9-row board, finite reusable arrow
  stock, placement and removal, locked trial, autonomous forward and
  barrier movement, contact steering, opposing cat traffic's two-contact
  arrow degradation, mouse delivery, failure, retry and advance.
- Excluded: exact update order or movement speed, controller remapping,
  save and VMU behavior, Action and Battle modes, team or network play,
  Editor, other stages, later releases and all Battle-only rules.
- Potential scoped module: an original multiplayer match with four
  colored rockets and competing live placement.
- Direct-play status: no native game or input execution. The North American
  booklet establishes the general rules and contemporary product records
  establish the release. Two independent guides and sampled Dreamcast
  visual traces support the fixed board, solution placements and positive
  and negative outcomes. Video and audio were not played.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| CCR-001 | The North American retail Dreamcast release is identified by product MK-51049. Puzzle Mode is an original one-player mode with a fixed number and type of panels per board. | Confirmed | Direct | High | P1 pp. 14–15; P2, P3 |
| CCR-002 | Normal Stage 10 offers one Up panel. The fixed rectangular board has 12 columns and nine rows, one visible mouse, four cats and one rocket. No hole is present on this board. | Observation | Corroborated | High | W1 5:00; W2 4:00; R1 §8 |
| CCR-003 | Setup allows placing an oriented panel at the cursor. Replacing the same panel at its position removes it, and L in setup removes the latest panel. Running begins on R and locks new placements. Later R accelerates both types, while L cancels the trial. | Confirmed | Direct | High | P1 pp. 14–15; R1 §4b |
| CCR-004 | Animals continue in their current direction where possible. A wall prompts a preferred right turn. If the right exit is also blocked, the written guide reports a left or reverse fallback. | Observation | Corroborated | High | P1 pp. 8–9; R1 §4b |
| CCR-005 | An animal entering an oriented panel is steered by it. A cat arriving opposite the panel's direction consumes one of its two head-on contacts: the first visibly shrinks it and the second removes it. Normal aligned or side contact is not the specified wear trigger. The movement update on the second contact was not isolated on this board. | Confirmed | Direct | High | P1 pp. 8–9; R1 §4b |
| CCR-006 | Puzzle success requires all mice to reach safety. Mouse loss or forbidden cat entry ends the trial. A failed approach is followed by the original actor positions and another route attempt in the second record. | Observation | Corroborated | High | P1 pp. 14–15; W2 5:40/6:00 |
| CCR-007 | With Up at F8, the active run retains that marker and reaches the clear banner. An independent successful sequence uses C8 and proceeds to Stage 11. Coordinates count columns A–L left-to-right and rows 1–9 top-to-bottom, with the outer frame omitted. | Observation | Corroborated | High | R1 §8; R2 Normal 10; W1 5:00/5:10/5:20; W2 6:50/7:00/7:10 |

## Basic data

- Sonic Team and Sega. FAM-005 applies because one constrained tile assignment
  changes the effective routes through the authored directed board.
- P1: [Sega of America's original Dreamcast instruction booklet](https://dreamcastlive.net/files/manuals/ccr_manual.pdf),
  printed pp. 8–9 and 14–15. Establishes the species' motion, the head-on
  exception, the placement inventory and Puzzle Mode's controls and terminals.
- P2: [Contemporary coverage of Sega's North American launch announcement](https://www.gamespot.com/articles/sega-announces-march-2-chu-chu/1100-2446501/).
  Establishes the market and Dreamcast launch window. No exact retail day is
  used in the record.
- P3: [Scans of the Dreamcast retail covers](https://www.mobygames.com/game/3725/chuchu-rocket/covers/dreamcast/)
  and [the MK-51049 product record](https://thegamesdb.net/game.php?id=3641).
  Establish the North American disc product, distinct from other releases.
- R1: [NTsui's Dreamcast walkthrough](https://gamefaqs.gamespot.com/dreamcast/196919-chuchu-rocket/faqs/8014),
  sections 4b and 8. Documents the fallback movement order, distinction
  between mode controls and C8 Up solution for Normal Stage 10.
- R2: [supersteve1440's Dreamcast solution guide](https://gamefaqs.gamespot.com/dreamcast/196919-chuchu-rocket/faqs/7975),
  Normal puzzle 10. Includes F8 and C8 among several reported placements.
  Only those two are credited here with corroborating visual sequences.
- W1: [Kain's Dreamcast puzzle run](https://www.youtube.com/watch?v=sXazgD2BH80).
  Still images at 5:00, 5:10 and 5:20 show the opening, active F8 panel and
  named clear screen. They constrain the sequence without measuring frames
  or resolving every tile crossing.
- W2: [Just Rooov's independent Flycast run](https://www.youtube.com/watch?v=YQ56a8T4f9Y).
  Frames at 4:00, 5:40, 6:00, 6:50, 7:00 and 7:10 show the initial board,
  a marked bad approach near the rocket and restored positions, C8 Up
  and the following stage. This corroborates rules rather than proving
  a native release version or exact timing.
- Sources accessed 2026-11-20.

## Mechanical decomposition

### Action Genes

- ACT-042 writes one persistent oriented tile command before the trial.
  Removing it returns the available placement unit. ACT-006 hastens
  resolution with a second R during the trial (CCR-003).

### System Behaviour Genes

- SYS-045 advances the mouse and four cats autonomously while the trial is
  running. SYS-1736 resolves blocked forward motion with a preferred right
  turn, subject to available exits (CCR-002, CCR-003, CCR-004).
- SYS-055 resolves entry on an arrow as local direction assignment.
  SYS-1737 consumes its durability specifically on opposed cat contacts.
  These are distinct from each other and from ordinary barrier turns
  (CCR-004, CCR-005).
- SYS-048 removes a rescued mouse from the active walk and credits the
  required delivery. A loss cannot produce that credit (CCR-006, CCR-007).

### Constraint Genes

- CON-001 bounds movement and placement to the authored tile grid, one
  occupant position per tile for the arrow layout. CON-047 gives the board
  a single typed, reclaimable Up panel; placing it consumes what remains
  available for this setup (CCR-002, CCR-003).

### Information Genes

- INF-001 exposes the initial actor positions and directions, walls,
  rocket, marker orientation and unused stock. Reading that state is
  different from being shown the whole future trajectory (CCR-002–CCR-004).

### Objective Genes

- OBJ-321 requires every protected mouse to enter safety and forbids a
  cat from entering the rocket or any loss of protected walkers. This
  board specialises the supplied population to one mouse (CCR-006, CCR-007).

### Time Genes

- TIM-009 separates self-paced spatial preparation from autonomous
  locked traversal. Speed-up and cancel remain available in the running
  phase, but route commands must be edited in setup (CCR-003, CCR-007).

## Reproducible transitions

| Initial state | Intervention | Discriminating result | Evidence |
| --- | --- | --- | --- |
| Puzzle Mode Normal Stage 10 before a trial | Inspect the panel inventory, actors, rocket and walls | The one Up panel can enter a limited board state before the simulation starts. | CCR-002 |
| Setup with a placed Up panel | Select the same panel at that position or use L to undo the latest placement | One placement unit becomes available again. | CCR-003 |
| Fresh board with the Up panel at F8 | Press R and let the actors approach their barriers and the placed marker | The active scene shows relocated actors and an intact F8 marker. New placements are unavailable. | CCR-003–CCR-005, CCR-007 |
| Active F8 attempt | Let the simulation reach its terminal | The required mouse is gone from the board and “Stage 10 CLEARED!” is displayed. | CCR-006, CCR-007 |
| An alternative setup leads the orange cat toward the rocket | Allow the bad route to resolve and retry | The second recorded run marks the bad approach near the rocket and returns to the original actor positions. | CCR-006 |
| Fresh board with the Up panel at C8 | Start the trial and observe the final state and subsequent transition | The route settles and the recording proceeds to Stage 11. The guide independently gives C8 Up. | CCR-007 |
| An opposed cat approaches a full Up panel from its upper edge | Allow a head-on contact and, if encountered, a second such contact | The general rule is full to small to gone. The confirmed F8 solution does not depend on reproducing this full wear sequence. | CCR-005 |

## Strategic and experiential structure

The player influences the dangerous routes with the same command that
can steer a mouse. A locally useful marker may divert a cat onto the rocket's
approach or be consumed by a pair of opposing contacts. The two corroborated
placements show that a valid plan need not occupy a unique tile. Position is
only one part of a trial: orientation and the heading on contact matter.

## Replay and variation

Retry preserves the board challenge and reproduces the initial actors,
letting the player change the route before the next launch. Different
placements can clear the same board. Different playback speeds are
resolution controls, and the evidence does not establish every path or
a universal tick schedule.

## Adjacent systems and history

HUMANITY uses persistent oriented commands and terminal agent accounting.
Its ability to alter the layout during live trials, recurring bodies in
some routes and larger command vocabulary are separate from the fixed
setup and opposing cat exception here. Railbound uses a locked authored
transport layout, but solves carriage order via connected rail and
switch behavior rather than applying local commands to two hostile
populations.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
| --- | --- | --- |
| Action | ACT-006, ACT-042 | oriented placement and fast-forward |
| System Behaviour | SYS-045, SYS-048, SYS-055, SYS-1736, SYS-1737 | autonomous movement, terminal accounting, steering, wall turns and wear |
| Constraint | CON-001, CON-047 | 12×9 board and one reusable Up marker |
| Information | INF-001 | visible board, actors, headings and stock |
| Objective | OBJ-321 | complete mouse rescue and no cat at rocket |
| Time | TIM-009 | untimed planning and locked simulation |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `588` (`GAME-0001`–`GAME-0588`).
- Exact genome matches: none.
- Tied near matches: `GAME-0029` — HUMANITY (`7 / 17 = 0.411765`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| HUMANITY (GAME-0029) | ACT-006, ACT-042, CON-001, INF-001, SYS-045, SYS-048, SYS-055 | Both route autonomous walkers with persistent commands. HUMANITY allows live editing and has different goal accounting. ChuChu Rocket! locks the trial and wears arrows through opposing cat contact. | 7 shared of 17 in union, 0.411765 (41.18%) |

### Preserved research notes

- New genes: SYS-1736, SYS-1737 and OBJ-321.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_335](../../../research/taxonomy-changes/TAXONOMY_CHANGE_335.md)
  isolates preferred right turns, opposed-contact panel wear and protected
  total evacuation with a hostile exit prohibition.

## Negative results

- The fixed Puzzle Mode reserve is not the live placement and eviction
  limit of Battle Mode. There is no one-third evacuation quota or score
  penalty in the selected normal puzzle.
- No hole, rewinding action, randomized stage event or editable route
  during the running trial is asserted for this board.
- A passing cat does not automatically wear a panel through its mere
  presence. An incoming direction opposing the arrow is required under
  the documented rule.
- The failing run is not evidence of a universal ordering for simultaneous
  contacts. The successful F8 trace has an intact arrow after the rescue
  and does not prove that the full wear allowance was used.

## Delta summary

## New facts

- [Observation | Corroborated | High] Two distinct Up placements, F8
  and C8, are supported for the same complete stage. The manual specifies
  role- and direction-dependent panel degradation.

## New genes

- [Observation | Corroborated | Medium] SYS-1736, SYS-1737 and OBJ-321
  are defined in TAXONOMY_CHANGE_335.

## New combinations

- [Observation | Corroborated | High] No new verified combination
  proposed. Existing subsets are reviewed in the corpus comparison.

## Taxonomy changes

- [Observation | Corroborated | Medium] The new boundaries are additive.

## New questions

- Native frame inspection could distinguish the full order of cat
  movement, panel shrinkage and removal at simultaneous contacts.

## Next recommended game

- [Hypothesis | Limited | Medium] GAME-0590, Tokyo Xtreme Racer on
  Windows, full Steam 1.0. Bound a released highway challenge and settle
  its Spirit Points outcome.
- Optimisation criterion: contrast preparing a fixed route for autonomous
  actors with live steering and score pressure on a shared road.

## Why this game

- [Hypothesis | Limited | Medium] A one-panel puzzle with one protected
  walker is a controlled comparison for steering hazards and evacuees
  using the same command vocabulary.
