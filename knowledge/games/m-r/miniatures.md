---
game_id: GAME-0727
slug: miniatures
game_title: "Miniatures"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-048
    - ACT-341
    - ACT-945
  system:
    - SYS-1439
  constraint:
    - CON-282
    - CON-903
  information:
    - INF-658
  objective:
    - OBJ-052
  time:
    - TIM-002
---

# Game: Miniatures — Familiar from screwdriver to story end

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Screwdriver, jars, fasteners, panels and cabinet are scoped instances.

## Analysis scope

- Version / ruleset: English commercial macOS Steam base game,
  app `2428840`, released 14 November 2024 by Other Tales Interactive.
  Scope the full release and its object-select route. The original
  standalone Familiar demo and its executable are outside the scope.
- Structured target: `PLAT-MACOS`. Start with the open memory box,
  select the screwdriver to enter Familiar, then follow that story
  through its final cabinet scene and fade back to the box. The
  solo player operates individual tasks among depicted family hands.
- Primary decision loop: recognise the currently possible placement
  or tool action, move or apply the visible piece, then follow the
  resulting change to the next authored work scene.
- Included: the object entry, staged sorting, plate screws, panels
  and later attempts to close the cabinet. Excluded: the other three
  stories, optimum speed, global chapter order, achievement mechanics,
  other platforms’ input mapping and claims about alternative endings
  or untouched task variants.
- Direct-play status: no personal installation, ownership or direct
  macOS play was verified. Store and developer material establish the
  commercial Mac target. The two recorded full-game sequences
  corroborate the visual rules without exposing their host OS or
  installed revisions. Frames were inspected in the background
  with sound disabled; no auditory cue is used as evidence.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| MT-001 | The Steam base game and developer press kit identify the commercial macOS release on 14 November 2024. The screwdriver chooses Familiar from the open memory box. The full-game recordings also contain the other tales. | Observation | Corroborated | High | P1, P2, W1 21:33–21:50, W2 00:16–00:40 |
| MT-002 | Three open jars stand over several hardware types. Holding and transferring the pieces sorts the loose set. A pointing hand supplies a local destination cue; an unsuccessful attempt at a jar leaves the sort incomplete. The sorting scene cuts away when the loose set is cleared. | Observation | Corroborated | High | W1 22:07–22:36, W2 00:55–01:26 |
| MT-003 | Place loose screws in the two connector holes. The raised heads remain until a separately wielded screwdriver drives them down; the visible staged cut follows the seating. Exact gesture increments and any minimum press duration are unmeasured. | Observation | Corroborated | High | P1, W1 22:37–23:05, W2 01:27–01:57 |
| MT-004 | After a separate parts-handling scene, place short pegs on the panel’s mounting points. Walls meet the panel and the sequence shows an open rectangular subassembly. | Observation | Corroborated | High | W1 23:23–23:58, W2 02:28–02:53 |
| MT-005 | Successors include the tugged handle, seam fit and adhesive scene, another screw placement, tape and pressure on the open faces. The assembly scenes remain ordered in both records. The footage does not establish exact gesture thresholds or every available alternative. | Observation | Corroborated | High | W1 24:04–26:24, W2 03:00–06:08 |
| MT-006 | The closing work exposes dark material and brings the family to a final view of the uneven cabinet. The cut returns to the memory box. W2 returns while other stories remain available. W1, which saved Familiar for last, returns before the collection credits. | Observation | Corroborated | High | P2, W1 26:10–27:19, W2 05:48–06:59 |
| MT-007 | The gestures in the local assembly scenes are taken at the player’s pace. Pauses between one placement and the next do not end the stage in either observed recording. No test here establishes an unlimited-idle rule for every scene. | Observation | Corroborated | High | W1 22:18–22:32 and 26:00–26:12, W2 01:28–01:57 and 03:06–03:35 |

## Basic data

- Release / origin: Other Tales Interactive, Steam commercial game
  app `2428840`, 14 November 2024. The developer distributes a
  distinct Familiar demo, excluded here. Its independent Itch
  macOS package corroborates availability of a native port but
  is not the chosen Steam edition.
- Platform or physical form: macOS native version, single-player
  rendered scenes with pointer-driven interaction. The witnesses
  disclose a pointer, not whether it is a mouse or trackpad.
- Mechanical family: `FAM-017`, because the small parts tasks,
  placements and closures must be advanced in an authored order.
- Primary sources checked 2026-11-25:
  - **P1:** [Other Tales Interactive's Steam listing](https://store.steampowered.com/app/2428840/Miniatures/).
    English support, macOS requirements, release, solo scope,
    commercial game and separately labelled demo, and screwdriver story.
  - **P2:** [Other Tales Interactive’s press kit](https://www.othertales.com/miniatures).
    Date, Mac launch, four distinct solo stories and short object-led structure.
  - **P3:** [Developer’s separately distributed download](https://othertales.itch.io/miniatures).
    Confirms the native macOS distribution and choice of story order.
- Independent recorded sources:
  - **W1:** [Adventure Vault full-game English walkthrough](https://www.youtube.com/watch?v=uuDvZV180gc).
    Familiar starts from the box around 21:36. Sorting, screws,
    pegs, subsequent hand work, cabinet and return are visible.
    Other tales precede it, establishing that Familiar is selectable.
  - **W2:** [msBean's release-day recording](https://www.youtube.com/watch?v=2DG-rO43wEw).
    Familiar is selected first. The sorting, repeated fastening,
    panel closures and the return to the open box corroborate W1.
    Used as a visual cross-check without assuming language or binary parity.
- Claim IDs: MT-001–MT-007. The reproducible stopping point is the
  first return to the box after this one tale, before a new object
  selection or whole-collection completion.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-048`: take one loose part, move it with the controlled
  hand and release it at a receiver (MT-002–MT-004).
- Reuse `ACT-341`: select the screwdriver in the memory box; later
  address a currently usable scene element (MT-001, MT-005).
- New `ACT-945`: seat a threaded fastener further with the
  separately wielded hand driver (MT-003, MT-005).

### System Behaviour Genes

- Reuse `SYS-1439`: progressing through the ordinary last cabinet work
  reaches the authored adverse display. Correct gesture completion
  advances the story even where the scene shows gaps and distortion
  (MT-005, MT-006).

### Constraint Genes

- Reuse `CON-282`: the local tasks lead into further authored work
  in order, rather than coming from a free room editor (MT-003–MT-006).
- New `CON-903`: the sorting step pairs different loose hardware
  classes with compatible jars and does not settle on an unsuccessful
  placement (MT-002).

### Information Genes

- New `INF-658`: a depicted hand indicates the relevant item or
  receiver while the work remains under player control (MT-002, MT-005).

### Objective Genes

- Reuse `OBJ-052`: reach the conclusion of the selected tale and
  the return to its replay or selection boundary (MT-001, MT-006).

### Time Genes

- Reuse `TIM-002`: pause between the observed placement inputs
  without an expiring attempt or score countdown (MT-007).

## Formal state and transitions

Track selected story, current work scene, loose and held parts,
accepted placements, per-fastener seating, visible cues and the
pending successor. Each scene has its own reachable objects.
The return to the box terminates the scoped tale. It does not
represent a numeric assembly score or successful furniture inspection.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Claim ID |
| --- | --- | --- | --- |
| The memory box is open | Select the screwdriver | The application starts Familiar | MT-001 |
| Several classes of parts lie below three jars | Place one part in a compatible jar | The accepted part leaves the loose set | MT-002 |
| A screw head stands proud of the connector | Apply the screwdriver to its head | The screw seats deeper; both flush heads precede the cut | MT-003 |
| The construction panel has vacant mounting points | Place pegs and bring the sides to the panel | The open rectangular subassembly appears | MT-004 |
| The cabinet faces remain unsettled | Continue the authored closing work | The final cabinet is shown and the game returns to the box | MT-005, MT-006 |

## Strategic and experiential structure

Read the gestures and the placements available at the current
table setup. Finish each small task before trying to use an object
from the next scene. The final result makes literal assembly and
story progression distinct outcomes.

## Replay and variation

The larger collection allows a choice of starting tale. Both
witnesses complete the same observed core assembly sequence
despite different tale order and work pace. No alternative
Familiar ending or persistence after restarting was tested.

## Adjacent systems and history

The remaining objects lead to different interaction systems.
Keep the demonstration package, global progress and ending
conditions of the collection outside the selected tale.

## Normalised genome

- Action: ACT-048, ACT-341, ACT-945.
- System Behaviour: SYS-1439.
- Constraint: CON-282, CON-903.
- Information: INF-658.
- Objective: OBJ-052.
- Time: TIM-002.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `726` (`GAME-0001`–`GAME-0726`).
- Exact genome matches: none.
- Tied near matches: `GAME-0115` — Unpacking (`2 / 13 = 0.153846`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Unpacking (GAME-0115)](../s-z/unpacking.md) | ACT-048, TIM-002 | Both let the player move individual objects at their own pace. Unpacking validates a room of household objects against their support contexts. Familiar sorts hardware by receptacle and applies the separate driver to seated screws to advance a sequence of authored scenes. | Near, `0.153846`. |

## Taxonomy impact

Generic part pickup, contextual interaction and story progression
are reused. A fastener placed in a hole is not yet driven into it.
The sorting receptacle restricts admission by class, and a hand can
indicate the local next step without completing that step for the player.

## Negative results

- The observed family hands are scene actors in one solo game.
- The initial screw insertion alone leaves a raised head.
- The illustrated cabinet state is the outcome of the observed
  route, without evidence for a conventional grade or failure screen.
- Neither walkthrough identifies its hardware or installed build.
- Nothing observed ties the opening order of the four tales
  to a different Familiar solution.

## Delta summary

Record a complete screwdriver-led microstory in which sorted
parts, installation and separately applied tools advance the work.
The visual ending resolves the tale without an assembly grade.

## New facts

- The screwdriver serves as the selectable story object.
- The hardware sort and two-hole connector demonstrate
  acceptance and secure fastening as separate states.
- The cabinet scene resolves back to the memory box.

## Principles and design implications

Make a compatible drop identifiable from the current task view.
Show a visible distinction between placing and securing a
part, and use the later scene to make the consequence readable.

## Puzzle or game generation potential

Provide a finite hardware assortment with typed receivers, a
plate with two compatible holes and one hand tool. Test the
unseated and seated states before using them to gate a separate
scene. Make any terminal story outcome explicit.

## New genes

- ACT-945
- CON-903
- INF-658

## New combinations

None matched after checking all 274 verified combinations.

## Taxonomy changes

[Taxonomy Change 473](../../../research/taxonomy-changes/TAXONOMY_CHANGE_473.md).

## Next recommended game

Metal Warriors on Super Nintendo is the next Selection 063 unit.

## Why this game

The authored cabinet sequence separates sorting, fitting and
tool use and shows how those tasks lead to one local story ending.

## Review status

Reviewed 2026-11-25 for the English macOS commercial Steam
base game. The analysis is bounded to one completed Familiar tale.
