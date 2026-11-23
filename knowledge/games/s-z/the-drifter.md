---
game_id: GAME-0613
slug: the-drifter
game_title: "The Drifter"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-087
    - ACT-089
    - ACT-341
    - ACT-814
  system:
    - SYS-112
    - SYS-1807
  constraint:
    - CON-136
  information:
    - INF-179
    - INF-372
  objective:
    - OBJ-026
  time:
    - TIM-002
---

# Game: The Drifter

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The railcar, old tarp, rebar, door and hatch are the observed instances.

## Analysis scope

- Version / ruleset: fully released English Windows Steam base game.
  Steam app 1170570 and Powerhoof date the commercial release to
  17 July 2025. The two PC captures date from launch week. Their
  exact installed build and operating system version are unreported.
- Primary decision loop: inspect the currently accessible actor or
  fixture for its action cue, acquire the old tarp, apply it to stop
  the passenger's use of the rebar, collect the released rebar and
  apply it to the heavy door. After the doorway event, cross the
  interior and take the hatch into the next scene.
- Entry: fresh opening in the freight car, at the first addressable
  interior interactions before changing the door.
- Exit: take the high hatch after reaching the far side of the
  interior. The game shows Mick on the embankment under its
  Chapter 1 — Welcoming Party title, then presents the underpass
  scene. Stop before answering the phone or solving Chapter 1.
- Included: hotspot examination and changing action cues, tarp use,
  rebar release and separate pickup, door opening, the authored
  attack sequence, opposite-side crossing and actual hatch exit.
- Excluded: the rest of Chapter 1, the later reservoir return mechanic,
  topic dialogue choices and subsequent object combinations, demo,
  GOG and other operating system or console distributions. No exact
  door-force, real-time failure, input-device parity or save-reload
  claim is made.
- Suggested later scope: follow the separate Chapter 1 phone-power
  and call route through its actual response.

## Direct-play status

No direct play was performed. The Steam listing confirms the Windows
release and Powerhoof's dated announcement distinguishes it from the
earlier demo. Indie James identifies a PC full playthrough and links
the Steam release. RinKa Plays identifies PC and demonstrates the
same opening with a pointer and in-game action-icon tutorial.
The PC footage is evidence for the shown route. It does not expose its
installed executable hash, each storefront licence or patch parity.
The release-day written walkthrough corroborates the items, crossing
and finish. Only writing and sampled static frames were inspected.
No audio was played.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| TD-001 | The target is the English commercial Windows Steam release, scoped to the opening railcar exit. Both PC captures continue beyond the publicly available demo's chapter. | Confirmed | Corroborated | High | P1, P2, W1, W2. The distribution is established by P1/P2; W1 links the Steam release and W2 labels PC. |
| TD-002 | Addressing an object exposes its current operation. When a hotspot changes state, its icon can change and it may accept another interaction. The untouched heavy door resists ordinary opening. | Observation | Direct | High | W2 1:20, 2:00 and 2:50 show the inventory cue, refusal and action-icon lesson; W1 1:40–2:10 shows alternate object prompts and the picked-up tarp. |
| TD-003 | The old tarp is collectable. Re-engaging the now accessible passenger can rouse him and prompt a swing with the rebar. His grip remains intact before the correct item is applied. | Observation | Corroborated | High | W1 1:50–2:40; W2 3:10 and 3:40; S1. Exact rejected commands and compulsory inspection count are not exhaustive. |
| TD-004 | Applying the acquired tarp to the agitated passenger interrupts his use of the rebar. The rebar is acquired separately from the floor. | Observation | Corroborated | High | S1, S2; W1 2:40–3:10 and W2 3:40–4:20. Compare the still-gripped tool, covered passenger and selected bar at the door. |
| TD-005 | The carried rebar operates the heavy door. Opening it starts a scripted encounter at the opening, and leaves the centre open after that encounter. | Observation | Direct | High | W1 3:00–4:00; W2 4:20–5:10; S1. The allowed passage along the inside of the car is distinct from exiting directly through the exposed broad side opening. |
| TD-006 | Select the crossing arrow, reach the far interior side and use the upper hatch. Both records show the exterior and Chapter 1 — Welcoming Party. The scene is not finished by opening the heavy door alone. | Observation | Corroborated | High | S1, S2; W1 4:10–4:50; W2 5:20–6:10. Hovering/examining the lit opening is documented in S1; the precise prompt trigger was not separately negated. |
| TD-007 | The confrontation gives the impression of urgency, but its unresolved player decisions wait for the next choice. Scripted motion between those decisions does not impose a player deadline. | Confirmed | Corroborated | High | P3 directly distinguishes waiting action decisions from animated action. W1 3:30–3:50 and W2 4:40–5:00 show authored motion between interaction states; the traces were not a maximal idle-duration test. |

## Basic data

- Origin: Powerhoof, developed with Dave Lloyd as credited on Steam.
- Analysis target: `PLAT-WINDOWS-PC`, Steam commercial base game,
  English opening through Chapter 1 entry.
- Mechanical family: `FAM-013`, inventory and fixture dependencies.
  The usable rod comes from a scene interaction and has a distinct
  accepted fixture. Machinarium also separates an acquired tool and the
  compatible fixture that exposes the next local route state.
- Sources checked 21 November 2026.
- P1: [Commercial Steam app 1170570](https://store.steampowered.com/app/1170570/The_Drifter/).
  Release date, Windows support, credits and PC distribution.
- P2: [Powerhoof commercial launch announcement](https://www.powerhoof.com/tag/the-drifter/).
  The dated release entry distinguishes the full launch from the demo.
- P3: [Powerhoof's pinned interaction and pacing explanation](https://steamcommunity.com/app/1170570/discussions/0/591776982251977889/).
  The author describes the action scenes waiting at player decision points.
- W1: [Indie James PC full route](https://www.youtube.com/watch?v=AX-ESNnvQrk),
  21 July 2025. Original recording, linked commercial listing and nine
  chapters. At 2:20 the passenger swings. At 3:10 the rod is shown for
  use at the door. At 4:20 Mick has crossed, and 4:40 shows Chapter 1.
- W2: [RinKa Plays PC Chapter 1 and 2 route](https://www.youtube.com/watch?v=Lcufih70hOE).
  19 July 2025. Independent observation with a pointer, the 2:50 action-icon tutorial,
  the rod still held at 3:40, tarp applied at 3:50, rod at the door at
  4:20 and Chapter 1 title visible at 6:00. The trace does not identify
  its exact binary. Timestamp values are video time.
- S1: [Into Indie Games release-day Prologue walkthrough](https://intoindiegames.com/walkthroughs/the-drifter-walkthrough-prologue/).
  Corroborates the tarp, rebar on the floor, the door, arrow and hatch.
- S2: [GameSpew release-day walkthrough](https://www.gamespew.com/2025/07/the-drifter-walkthrough/).
  Confirms the same exit sequence, with the left hatch after the crossing.

## Mechanical decomposition

### Action Genes

- ACT-087: select the acquired rebar and apply it to the compatible
  heavy sliding door. The accepted use is on a specific fixture.
- ACT-089: acquire the tarp and later separately collect the released bar.
- ACT-341: address the passenger to advance his local state, then address
  the far-side hatch to initiate the exit.
- ACT-814: apply the held cover to interrupt the addressed holder's use
  of the required object. The accepting object here is the passenger,
  and he is not offering a voluntary hand-in.
- Claim IDs: TD-002–TD-006.

### System Behaviour Genes

- SYS-112: the rebar use opens the persistent heavy-door state. The
  authored event must run before the next ordinary interior move.
- SYS-1807: using the tarp changes the grip and exposes the rebar as a
  distinct collectable object. It still needs explicit acquisition.
- Claim IDs: TD-004–TD-006.

### Constraint Genes

- CON-136: the supported route passes through the exposed passenger,
  tarp use, released rod, door opening and cross-car access before the
  upper hatch can close the scene. The exact number of optional looks
  on the way is not a prerequisite claim.
- Claim IDs: TD-002–TD-006.

### Information Genes

- INF-179: the current cutaway shows Mick, the passenger, the reachable
  bed area, the door and its open state, and the auxiliary hatch.
- INF-372: the addressable icon distinguishes what the player can do now.
  The tutorial explicitly invites re-interaction when it changes. The
  player still has to choose how to use a collected object.
- Claim IDs: TD-002, TD-003, TD-005, TD-006.

### Objective Genes

- OBJ-026: make the relevant side traversably connected, reach the
  designated upper hatch and actually arrive at the exterior underpass.
  Acquisition, door opening and reaching the hatch are interim results.
- Claim IDs: TD-005, TD-006.

### Time Genes

- TIM-002: consider the next interaction without a deadline between
  decisions. The animation and scene event replay are separate.
- Claim IDs: TD-007.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Untouched heavy door with no usable tool | Try the ordinary door interaction | It stays shut | A visible interaction is not automatically successful | TD-002 |
| Tarp beside the inert passenger | Expose the passenger as needed and collect the tarp | Tarp becomes an inventory choice, and the actor can be readdressed | Scene inspection and item ownership are distinct | TD-002, TD-003 |
| The roused passenger still holds the bar | Target the passenger with the held tarp | His attack stops and the bar becomes accessible on the floor | Countering the holder does not itself give the item to Mick | TD-003, TD-004 |
| Rebar exposed in the local scene | Collect the rebar and apply it to the heavy door | Opening event plays, and the side door remains open afterward | The destination is a fixture with a specific item-driven transition | TD-004, TD-005 |
| Open broad side and no forward progress yet | Cross the interior toward the opposite side | Mick reaches the side from which the top hatch can be used | Crossing the exposed interior is separate from making the door open | TD-006 |
| Opposite interior side reached | Select the high hatch | Exterior embankment and Chapter 1 appear | The observed success is departure through the hatch | TD-006 |

## Strategic and experiential structure

The player distinguishes looking, collecting and item-directed action
on the same small stage. The door gives the immediate problem. The
passenger's state prevents simply selecting the needed tool. The tarp
changes that state and leaves a new pickup rather than solving the door
by itself. Once the large door opens, the route continues across the
interior to the smaller high hatch. The bright scene event gives a
short-term reason to move, and the author states that a decision waits
for input. Claim IDs: TD-002–TD-007.

## Replay and variation

The two commercial PC traces differ in pacing and optional inspections
but show the same material sequence and chapter arrival. They do not
establish that every possible inspection order, any alternate item, or
a direct leap through the broad door supports the same exit. No score,
random item outcome, measurable rebar duration or reload test is
reported. Claim IDs: TD-002–TD-007.

## Adjacent systems and history

The public prerelease Chapter 1 demo and later ports do not establish
the English Windows commercial ruleset. The distinct reservoir sequence
and the consequences of the protagonist's return after death are
chapter mechanics outside this railcar study. The short scene's two
inventory objects are separately used on their targets. No inventory
combination is evidenced within the prologue.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-087, ACT-089, ACT-341, ACT-814 | Apply tool, collect, address a target and cover its holder |
| System Behaviour | SYS-112, SYS-1807 | Reveal the fixture state and separately expose the held tool |
| Constraint | CON-136 | Earlier resolved world states gate the later route |
| Information | INF-179, INF-372 | Current interior and changing legal operation |
| Objective | OBJ-026 | Take the hatch to the exterior |
| Time | TIM-002 | Decisions await the player |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `612` (`GAME-0001`–`GAME-0612`).
- Exact genome matches: none.
- Tied near matches: `GAME-0086` — Machinarium (`5 / 19 = 0.263158`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Machinarium (GAME-0086)](../m-r/machinarium.md) | ACT-087, ACT-089, CON-136, SYS-112, TIM-002 | Both collect an object, apply the compatible tool at a fixture and wait for the next choice. Machinarium also requires articulation, exchange and assembly before a missing component can be recovered. The Drifter changes the passenger’s grip with a carried cover, collects the same released tool, and reaches the far hatch after the ensuing doorway event. | Near, `0.263158` |

## Novelty assessment

| Mechanic or candidate | Closest prior boundary | Decision |
| --- | --- | --- |
| Targeted inventory cover applied to an active character | ACT-087 and ACT-091 | Use ACT-814 for the cover interaction. The rod's later application is a separate ACT-087 fixture use. |
| Interrupted holder's object becomes a separate pickup | SYS-113 and SYS-1483 | Use SYS-1807 for authored release into the scene. The target does not perform a requested hand-in and no finite arena weapon gauge is involved. |
| Current hotspot changes its operation cue | INF-372 | Reuse the changed contextual action icon; it exposes the current operation before activation. |
| Exit after using the prepared route | OBJ-026 | Reuse actual spatial completion. Chapter title supplies the visible successor evidence rather than a new score condition. |
| Separate tarp and rebar items | ACT-090 | Excluded. The route shows sequential uses against distinct compatible targets. |

## Combination candidates

- [Observation | Direct | High] The verified inventory/fixture combinations
  are tested by complete subset membership. A shared action or tool precondition
  does not independently establish a combination.
- [Hypothesis | Limited | Medium] A repeatable inventory-cover-to-release chain
  needs another independently analysed game before any proposal for promotion.

## Taxonomy impact

- [TAXONOMY_CHANGE_359](../../../research/taxonomy-changes/TAXONOMY_CHANGE_359.md)
  records the cover interaction and its separate collectable release.
  The existing acquisition, fixture, information and objective
  meanings remain stable.

## Negative results

- The passenger does not request the tarp or hand over the rebar.
  A held-item delivery gene cannot supply the interruption boundary.
- Both elements are live scene items collected at separate times.
  The evidence shows no held-item combination or authored recipe
  before using the rod.
- The attack sequence animates within the opened door state.
  The archival footage and author explanation give no basis for a
  time limit over the decision to cross.
- The exit across the inside of the freight car goes through the
  elevated hatch. The large opened panel is not the actual end.

## Delta summary

## New facts

- [Observation | Corroborated | High] The passenger's release and subsequent
  rebar acquisition are separate events. TD-003, TD-004.
- [Observation | Direct | High] The heavy door becomes open several steps
  before the route settles at the exterior chapter entrance. TD-005, TD-006.
- [Confirmed | Corroborated | High] The author identifies the urgency of
  animated action as compatible with waiting between choices. TD-007.

## New genes

- [Observation | Corroborated | Medium] ACT-814 and SYS-1807.

## New combinations

- [Observation | Direct | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_359.

## New questions

- Does the lit-opening examination gate the arrow independently of the
  end of the authored encounter?
- Which pre-tarp looks and repeated interactions are mechanically required
  if the contextual state is advanced in a different order?
- What is the precise skip and resume behaviour on an identified Windows
  build through the opening and first controllable exterior scene?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0614`, Mole Mania, original
  North American Game Boy cartridge. Follow one complete early room through
  digging, object movement and an observed exit.

## Why this game

- [Hypothesis | Limited | Medium] The next boundary compares an adventure
  scene where an inventory operation enables access with a spatial puzzle
  where movement between two layers makes an object route reachable.
