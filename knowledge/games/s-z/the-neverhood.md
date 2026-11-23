---
game_id: GAME-0528
slug: the-neverhood
game_title: The Neverhood
analysis_status: reviewed
reviewed: 2026-11-17
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-049
    - ACT-089
    - ACT-341
    - ACT-721
  system:
    - SYS-065
    - SYS-1431
    - SYS-1515
    - SYS-1516
    - SYS-1517
    - SYS-1518
    - SYS-1519
  constraint:
    - CON-001
    - CON-810
  information:
    - INF-001
    - INF-513
  objective:
    - OBJ-026
  time:
    - TIM-002
    - TIM-003
---

# Game: The Neverhood

Use the canonical [vocabulary and genome rules](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Room names, slot counts, sound pitches and switch colours parameterise the rules.

## Analysis scope

- Version / ruleset: original English Windows 95 retail CD, The Neverhood,
  Inc. and DreamWorks Interactive, 1996, ordinary new game. The packet
  reconstructs the CD rules from its manual, authored route evidence and
  the matching ScummVM engine. No exact installed disc was identified.
- Structured analysis target: PLAT-WINDOWS-PC, English full release;
  no demo, PlayStation localisation or ScummVM-specific convenience option.
- Primary decision loop: inspect clickable fixtures, acquire and position
  prerequisites, then test the local arrangement or supply. Carry its effects
  to separate rooms, check which controls at the cave have become enabled
  and release the corresponding local bolts.
- Entry: Klaymen wakes in the first room, before pulling the wall handle.
  Exit: after enabling the three cave controls and releasing the door's
  three local bolts, take the first crossing onto the bridge. Stop before
  the symbols, cannon or lake controls.
- Included: nursery handle and plant, the dummy panel and creature
  barrier, the H slider, the Hall of Records beaker, shared spikes and lift,
  water source and five pipes, the spiral car switch, attic activation and
  bolt door. Narrative recordings and exhaustive optional exploration are
  not prerequisites.
- Excluded: completion of the story-disc collection, auxiliary nursery
  radio power, exact initial H-board shuffle distribution, lake draining,
  telescope, radio tuning, reduction in size, teleporter, later puzzles,
  marked drain death and ending. Exact original animation timings and
  equivalence with ports are untested.
- Direct-play status: no game binary, CD, emulator, audio or video ran.
  The ScummVM source is a reimplementation, not the original executable.
  Contemporary written play and separate walkthroughs corroborate the
  route. Pipe sounds were verified by code and text, not by listening.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| NH-001 | The full English retail CD targets Windows. Mouse interactions indicate walk and view actions, collect addressed items and automatically use a compatible held item at its puzzle. | Confirmed | Direct | High | P1 pp. 2–5, P2 detector |
| NH-002 | Three wall-handle pulls open the first passage. Push the plant under the fourth ring from the left, then pull the ring so the plant takes it and holds the exit open. Pulling unaided does not sustain the same access. | Observation | Corroborated | High | P2 Scene1002, S1, S2 |
| NH-003 | Each position in the dummy panel exchanges the contents of its prescribed pair. The arrangement puts the six fused parts at their target positions and lowers the dummy. The creature encounter supplies a match separately and the prepared dummy clears the obstruction. | Observation | Corroborated | High | P2 Scenes1201–1202, S1, S2 |
| NH-004 | The 3 × 3 H panel has eight cubes and one vacancy. Each cubical move is to an orthogonally adjacent empty position. The reimplementation shuffles once and tests seven marked positions; the leftover cube and vacancy may exchange the two centre edge slots. | Observation | Corroborated | High | P2 Scene2202 and initCubeSymbolsPuzzle, S1, S2 |
| NH-005 | The Hall of Records provides a carried beaker and a separate spike switch. Its spike state affects whether the pipe house's attic is climbable. The Hall basement is reached by lift and has its own remote cave control. | Observation | Corroborated | High | P2 Scenes2205/2207/2404, S1, S2, S3 |
| NH-006 | Enable the supply at the separate source first. The pipe house pedal then starts a brief flow. A valid collection during flow also requires the beaker. A missed window can be reopened. | Observation | Corroborated | High | P2 Scene2401, S1, S2 |
| NH-007 | Match the five target tones by stepping the corresponding pipe levels. The button plays target, then current tones, and checks every indexed level. The matched vector is 3, 1, 2, 0, 4. Wrong submission flushes populated pipes. The qualified door can close and be opened again. | Observation | Corroborated | High | P2 initWaterPipesPuzzle, Scene2401 and AsScene2401Door, S1, S2 |
| NH-008 | The spiral car stop, the Hall of Records basement and the pipe house attic each enable a separate cave bolt control. Pressing all three remote switches does not itself retract the local bolts. An enabled local control must be operated and all three bolts must release. | Observation | Corroborated | High | P2 Scene3010 and SsScene3010DeadBoltButton, S1, S2, S3 |
| NH-009 | Enter the cave passage after its bolt door settles, then navigate to the bridge. No cannon shot or lake drain is required to reach this endpoint. | Observation | Corroborated | High | P2 Scene3010, S1, S2 |

## Basic data

- Release / origin: The Neverhood, Inc., DreamWorks Interactive, 1996.
- Families: state transformation, inventory and fixture dependencies,
  and ordered dependency sequencing.
- Sources accessed 2026-11-17:
  - **P1** — [Original DreamWorks Interactive manual](https://smetisteher.cz/manualy/neverhood_manual.pdf), English cover, requirements and How to Play. The reproduction identifies the original Windows 95 CD and explains the Klay Arrow and automatic item use.
  - **P2** — ScummVM v2.9.1 reimplementation. The [detector](https://github.com/scummvm/scummvm/blob/v2.9.1/engines/neverhood/detection.cpp) distinguishes English full resources from demos. The [initialisers](https://github.com/scummvm/scummvm/blob/v2.9.1/engines/neverhood/gamemodule.cpp), [nursery](https://github.com/scummvm/scummvm/blob/v2.9.1/engines/neverhood/modules/module1000.cpp), [dummy](https://github.com/scummvm/scummvm/blob/v2.9.1/engines/neverhood/modules/module1200.cpp), [H panel and Hall](https://github.com/scummvm/scummvm/blob/v2.9.1/engines/neverhood/modules/module2200.cpp), [pipes and attic](https://github.com/scummvm/scummvm/blob/v2.9.1/engines/neverhood/modules/module2400.cpp), [pipe door](https://github.com/scummvm/scummvm/blob/v2.9.1/engines/neverhood/modules/module2400_sprites.cpp) and [deadbolts](https://github.com/scummvm/scummvm/blob/v2.9.1/engines/neverhood/modules/module3000.cpp) were read as source. Code-level details are not frame measurements of the original executable.
  - **S1** — [Len Green's original game walkthrough](https://www.justadventure.com/walkthrough/the-neverhood/), first room through the tunnel and bridge, including the optical puzzle, water and distinct buttons.
  - **S2** — [The Walkthrough King's PC route](https://www.walkthroughking.com/text/neverhood.aspx), opening and entry to Lake Bottom. The route gives one H arrangement; the reimplementation's predicate permits either compatible arrangement.
  - **S3** — [Contemporary 1996 player discussion](https://groups.google.com/g/comp.sys.ibm.pc.games.adventure/c/GXxODriTCjk), separate early bolt controls, supplied water and the path through the creature area.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: direct Klaymen to the reachable part of the current
  scene or through a walkable exit with the cursor.
- Reuse `ACT-049`: operate persistent world switches at their accessible
  locations, including the shared spikes and the source.
- Reuse `ACT-089`: pick up the Hall beaker and the exposed match into
  Klaymen's stored items.
- Reuse `ACT-341`: act on the handle, plant, ring, dummy, pipe controls
  and local latches as their current state allows.
- New `ACT-721`: select one face tile orthogonally beside the vacancy
  to slide into it. The starting vacancy and carved cube positions vary.
- Claim IDs: NH-001–NH-009.

### System Behaviour Genes

- Reuse `SYS-065`: the Hall elevator carries Klaymen along its fixed
  shaft when commanded, granting access to the basement control. The
  spiral track car is a separate connection.
- Reuse `SYS-1431`: opening the room handle and other permitted local
  door actions change traversable access.
- New `SYS-1515`: place a movable helper under a spring-return control
  so it catches and holds the control when the player's pull would end.
- New `SYS-1516`: change the dummy's bounded arrangement through
  designated local exchanges. Completing the fused destination positions
  settles an assembled figure for subsequent scene use.
- New `SYS-1517`: separate remote switch flags enable the corresponding
  controls at a common door. The door opens after all enabled local
  actions settle, rather than immediately when the last remote flag changes.
- New `SYS-1518`: adjust indexed pipe levels and submit them as a
  complete ordered vector. Exact equality opens the door. A nonempty
  mismatch flushes the setting to a recoverable initial state.
- New `SYS-1519`: toggle one distributed fixture state to change
  climbable geometry at a different location.
- Claim IDs: NH-002–NH-009.

### Constraint Genes

- Reuse `CON-001`: the H board has fixed single occupancy plus its
  one vacancy, and the dummy exchange preserves its fixed size.
- New `CON-810`: the needed intake requires both a compatible carried
  vessel and a currently active short flow from a separately fed fixture.
- Claim IDs: NH-003, NH-004, NH-006.

### Information Genes

- Reuse `INF-001`: the H board's current marked tiles and vacancy are
  visible in the local panel before choosing a move.
- New `INF-513`: the same playback action presents reference tones,
  then plays the current keyed instrument states in the same order.
- Claim IDs: NH-004, NH-007.

### Objective Genes

- Reuse `OBJ-026`: connect the initial land to the bridge by making the
  cave door passable, then enter the bridge.
- Claim IDs: NH-008, NH-009.

### Time Genes

- Reuse `TIM-002`: the exploration and panel arrangements are editable
  step by step without a stage deadline.
- Reuse `TIM-003`: the triggered water intake and open pipe doorway
  have windows that can close before the action is taken.
- Claim IDs: NH-003, NH-004, NH-006, NH-007.

## Reproducible transitions

| Before | Action | Bounded resolution | What it establishes | Claim ID |
|---|---|---|---|---|
| Klaymen wakes, first passage closed | Pull the handle three times | The first passage opens | One repeated fixture input crosses the local gate | NH-002 |
| Plant under the fourth ring, exit closed | Pull that ring and let the plant take it | The plant sustains the held control and exit | The same pull without spatial preparation is temporary | NH-002 |
| Dummy has duds in fused target positions | Click a selected position | Its content is exchanged with the prescribed other position in that group | This is an exchange, not unrestricted creation of a new piece | NH-003 |
| Fused pieces all in target positions, creature route unresolved | Settle panel, trigger encounter, use collected fixture item on dummy | The figure lowers after assembly; the later scene action clears the obstacle | Assembly alone does not clear the route | NH-003 |
| H panel has an empty neighbour | Click the neighbouring tile | Tile occupies the former blank and leaves its own slot vacant | Moving into a vacancy is distinct from exchanging two occupied positions | NH-004 |
| Seven H positions correct | Let the board settle | Access to the Hall opens even if blank and filler occupy the alternate permitted edge centres | Seven positions are checked, not a full nine-slot password | NH-004 |
| Hall accessible, water task not ready | Take beaker, set spikes, visit lift basement | Carry equipment, expose later climb route and enable one remote bolt | A single building provides separate prerequisites | NH-005 |
| Pedal not supplied, or water active without the beaker | Attempt to collect | No valid supply reaches the current puzzle | The pedal and inventory are distinct requirements | NH-006 |
| Supply active, vessel held, flow expired | Reopen the pedal window and collect promptly | The intake is available for setting the pipes | Timeout is local and recoverable | NH-006 |
| At least one pipe differs after filling | Submit using the test button | Reference and current pitches play, and populated levels flush | A wrong combination is reversible | NH-007 |
| Five pipe levels match | Submit and enter while the door opens | Local access lets the player climb to the attic when the remote spikes permit it | Tone matching and rung availability are separate | NH-005, NH-007 |
| Three remote controls enabled, door still has local bolts | Actuate each permitted local control, then enter | After all three releases the corridor grants access to the bridge | Distributed enablement precedes local commitment | NH-008, NH-009 |

## Strategic and experiential structure

The opening teaches the difference between briefly operating a fixture and
making it stay useful while moving elsewhere. The beaker, water supply,
shared spikes and basement button encourage retaining the consequences of
past interactions. Pressing a red button beside the wrong pipe vector is a
safe trial, but it costs the time of rebuilding that local setting.

## Replay and variation

- Early room order permits revisiting the Hall, pipe house and spiral
  control when the required local prerequisites are ready. The cave
  observes separate flags rather than a single sequence of button colours.
- Compare an unaided ring pull with the positioned plant. Compare a
  partial pipe match with a fully matched five-position vector.
- Claim IDs: NH-002, NH-005–NH-009.

## Adjacent systems and history

- The game combines local compact arrangement puzzles with linked
  fixtures across navigable rooms. Later collection, radio and lake
  puzzles form their own scopes.
- Original assets and the reimplementation's detailed state conditions
  are kept distinct from native runtime measurements.
- Claim IDs: NH-001, NH-004–NH-009.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | `ACT-008`, `ACT-049`, `ACT-089`, `ACT-341`, `ACT-721` | local destination, switches, items, fixtures, vacancy slide |
| System Behaviour | `SYS-065`, `SYS-1431`, `SYS-1515`, `SYS-1516`, `SYS-1517`, `SYS-1518`, `SYS-1519` | lift, open passage, held ring, arrangement, flags, pipe comparison, spikes |
| Constraint | `CON-001`, `CON-810` | one vacancy, compatible held vessel, flowing water |
| Information | `INF-001`, `INF-513` | current tile layout, indexed reference and response tones |
| Objective | `OBJ-026` | bridge access and first crossing |
| Time | `TIM-002`, `TIM-003` | ordinary self-pacing and activated local windows |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `527` (`GAME-0001`–`GAME-0527`).
- Exact genome matches: none.
- Tied near matches: `GAME-0302` — Captain Toad: Treasure Tracker (`5 / 20 = 0.250000`).
- Supported combination subsets: none.
- Scan date: 2026-11-17.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
|---|---|---|---|
| `GAME-0302` — Captain Toad: Treasure Tracker | `ACT-008`, `ACT-049`, `INF-001`, `SYS-065`, `TIM-003` | Both examine placed geometry, guide an avatar through authored space and use a switch for a linked moving route. Captain Toad's first course is a small continuously simulated route inspected by turning the camera. The Neverhood builds access across rooms, a carried beaker and multiple discrete panels before acquiring the three permissions that enable the local bridge door. | Tied near (`0.250000`) |

### Preserved research notes

- New genes: `ACT-721`, `SYS-1515`–`SYS-1519`, `CON-810`, `INF-513`.
- Classification result: `New gene`.
- Evidence and reasoning: retained fixture effects bridge rooms, while
  the situated arrangements retain separate validation rules.

## Taxonomy impact

- Registry changes: eight Active additions and eleven transfers.
- Taxonomy-change record: [TAXONOMY_CHANGE_275](../../../research/taxonomy-changes/TAXONOMY_CHANGE_275.md).

## Negative results

- No earlier verified combination is a proper subset.
- No direct evidence establishes exact original animation countdowns or
  the equivalence of the separate PlayStation rules.

## Delta summary

## New facts

- [Observation | Corroborated | High] A remote cave flag makes a latch
  operable, while the player must still release each latch at the door.
  Water supply, carry state and the short intake window are also distinct.

## New genes

- [Observation | Corroborated | High] Eight definitions in
  `TAXONOMY_CHANGE_275`.

## New combinations

- [Observation | Corroborated | High] No new combination proposed.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_275`.

## New questions

- Which room interaction timings differ if native animation is skipped
  with the optional keyboard shortcut?

## Next recommended game

- [Hypothesis | Limited | Medium] Original PlayStation 4 *Tetris Effect*.
- Optimisation criterion: contrast self-paced fixture changes and positional
  validation with live line settlement under a finite timing intervention.
- Backlog impact: advance Selection 041 to its seventh candidate.

## Why this game

- [Hypothesis | Limited | Medium] The bounded bridge route makes a chained
  dependency and its observable local outcomes inspectable without relying
  on the campaign ending.
