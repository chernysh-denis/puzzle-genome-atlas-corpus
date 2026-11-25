---
game_id: GAME-0702
slug: escaping-wonderland
game_title: "Escaping Wonderland"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-072
    - ACT-787
  system:
    - SYS-112
    - SYS-1980
  constraint:
    - CON-893
  information:
    - INF-640
  objective:
    - OBJ-026
  time: []
---

# Game: Escaping Wonderland

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Bring Molly to the broken steam panel and change from guiding her
through the diorama to repairing pipe connections by hand. Return
to her and take the newly available passage.

## Analysis scope

- Version / ruleset: the native English commercial Meta Quest base
  product 6146292702126753, Cortopia Studios and Beyond Frames
  Entertainment, released September 26, 2024. The platform target
  is Quest 3. One capture is labelled Quest 3 and was posted
  shortly before launch. An independent launch-week full-game
  capture corroborates the route. Exact application binaries and
  the second capture's device model were not authenticated.
- Structured analysis target: PLAT-META-QUEST in
  [platform coverage](../../platforms/games.json).
- Entry: Chapter 1 after Mr Mole's request. Begin with Molly in the
  diorama before the first stationary steam-pipe repair, at the
  panel next to the passage that lacks steam.
- Primary decision loop: address the panel, use the close-up
  hand view, identify matching marked permanent terminals and
  grip and orient supplied straight or elbow sections. Inspect
  each gauge as its route is repaired and finish the outstanding
  connections. Resume Molly's exploration when the view returns.
- Positive terminal: pass the steam-dependent door and reach the
  floor at the foot of the next room's ladder. Stop before
  operating the next puzzle controls.
- Included: local panel interaction, change of control perspective,
  tracked manipulation, spatial and typed connection compatibility,
  local pressure indicators, return to Molly and passage to the
  tank-and-ladder room.
- Excluded: prior dialogue and glasses task, root-grip camera
  manipulation outside the route, optional hints and collectibles,
  exact fit tolerance, supply order or a claimed global piece limit,
  button telemetry, later puzzles, ports and differences across
  headset models and patch levels.
- Potential scoped module: the next ladder-and-tank room after
  observing the state change from its own controls.
- Direct-play status: no personal Meta Quest 3 session, native
  pose trace or runtime inspection. The product and publisher
  establish the release. Two independent Quest-attributed records
  were inspected as short silent frame sequences. The pre-release
  written demonstrations supplement only shared observed rules.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| EW-001 | Cortopia's commercial English Meta Quest version supports Quest 3. Meta identifies product 6146292702126753 and September 26, 2024 as the release date. | Confirmed | Direct | High | P1, P2, P3 |
| EW-002 | At the steam panel Molly is separately visible and navigable. Addressing the panel opens a stationary first-person manipulation view at the mechanism. | Observation | Corroborated | High | P2; W1 9:30–9:35; W2 8:06–8:13; S1, S2 |
| EW-003 | Straight and elbow sections are grasped and oriented into end-to-end joins. Matching permanent pipes are distinguished by their visible colors or bands, and the solution bridges the corresponding terminals in three dimensions. | Observation | Corroborated | High | W1 9:41–10:20 and 13:19–13:25; W2 11:21–11:54; S1, S2 |
| EW-004 | Gauges next to the connected routes provide local feedback. A needle can reach the green sector before every other route has been completed. | Observation | Corroborated | High | W1 9:35 and 13:00–13:05; W2 8:10 and 11:48 |
| EW-005 | The completed panel is followed by a return to the diorama with Molly at the same site. No separate answer screen appears between the last visible joins and the restored view. The exact last button signal is unavailable. | Observation | Corroborated | High | W1 13:24.5–13:27; W2 11:53–11:57 |
| EW-006 | After the panel settles, Molly can move through the nearby right-hand passage and reach the next tank-and-ladder room. The player then operates Molly rather than the close-up pipes. | Observation | Corroborated | High | W1 9:30 and 13:29–13:37; W2 8:13 and 12:12–12:40 |

## Basic data

- Release / origin: Cortopia Studios and Beyond Frames Entertainment,
  native Meta Quest commercial release, September 2024.
- Mechanical family: FAM-005. Build continuous routes between
  matching terminals to restore local connectivity in the apparatus
  and unlock the separate route for Molly.
- P1: [Meta Quest commercial product](https://www.meta.com/experiences/escaping-wonderland/6146292702126753/).
  Lists its Quest 3 support, English and September 26 release.
- P2: [Beyond Frames' release-day statement](https://www.prnewswire.com/news-releases/off-with-their-headsets-escaping-wonderland-takes-players-down-the-rabbit-hole-on-meta-quest-and-pico-302260286.html).
  Identifies third-person movement through connected dioramas and
  stationary first-person puzzle interactions as distinct modes.
- P3: [Cortopia's product page](https://www.cortopia.com/project/escaping-wonderland/).
  Identifies the game and project independently of its predecessor.
- W1: [TruGamer4Realz Quest 3 recording](https://www.youtube.com/watch?v=IVtx8PQseUw&t=570s).
  September 24, launch-window footage with English interface.
  Shows stationary manipulation, the diagnostic needle and the
  next room. Device attribution comes from the recording author.
- W2: [The Laughing Veteran full-game recording](https://www.youtube.com/watch?v=oLgL7tLqzXA&t=488s).
  September 27, with the Meta product link and Quest 3 tag. The
  runtime is not independently identified. Supports the same
  sequence with different timings and hand positions.
- S1: [UploadVR Quest 3 demo account](https://www.uploadvr.com/escaping-wonderland-vr-impressions/).
  Confirms stick-controlled Molly, the first-person pipe fixture
  and supplied shapes. Its demo alone does not prove retail behavior.
- S2: [MIXED's preview and developer interview](https://mixed-news.com/en/escaping-wonderland-preview/).
  Describes repairing missing sections between matching colored
  pipes in three-dimensional space.
- Claim IDs: EW-001–EW-006.

### Reproducible fixture evidence

1. Bring Molly to the panel in the orange machine chamber. In
   W1 at 9:30 a nearby hint identifies the inactive steam door.
   W2 shows the third-person position at 8:08 and a close view of
   the unconnected panel at 8:10. W2 briefly looks toward the
   neighboring shut door at 8:13 before resuming the pipe task.
2. Inspect the unjoined terminals and the low gauge positions.
   Take a supplied gray pipe section, orient it and fit the
   open end to a compatible port. W2 11:21–11:54 shows loose
   parts in the foreground, successive orientations, and retained
   joints along the yellow and banded connections. Use compatible
   straight lengths or elbows until a matching pair is linked.
3. Read each pressure gauge as a separate signal. W1 9:35
   shows a red-sector needle on an incomplete route. By 13:05
   the round blue-route gauge shows green while the close-up is
   still active and later connections are still being made.
   Continue until the panel sequence resolves, rather than using
   a single green gauge as proof of total completion.
4. At 13:24.5–13:26.5 in W1 the close-up gives way to the
   diorama and Molly is at the repaired panel. W2 reproduces
   the change at 11:54–11:57. The frames contain no separate
   answer menu. They do not identify an invisible final input.
5. Move Molly right to the passage. W1 shows her reaching it
   near 13:31 and the tank-and-ladder room by 13:35. W2 shows
   the corresponding passage and floor at 12:12–12:40. Stop on
   the floor before using the next ladder controls.

## Mechanical decomposition

### Action Genes

- ACT-008: steer Molly in the diorama up to the panel and
  through the reopened passage to the successor room.
- ACT-072: invoke the local steam-panel interaction.
- ACT-787: grasp, orient and release the available physical
  sections at their addressed connections using the tracked hand.

### System Behaviour Genes

- SYS-112: the accepted repair changes the steam-dependent
  passage and leaves it available for Molly's return traversal.
- SYS-1980: the addressed panel changes command of Molly to
  stationary hand manipulation, then restores avatar control
  at the repaired fixture once the challenge resolves.

### Constraint Genes

- CON-893: the accepted repair uses continuous compatible
  ports between matching fixed terminals in spatial alignment.

### Information Genes

- INF-640: the visible pipe color and banding identify which
  terminals belong together. A localized gauge indicates the
  accepted state of its own route while the rest remains live.

### Objective Genes

- OBJ-026: reach the next room through the restored passage.
  Making a single valid connection is an intermediate result.

### Time Genes

No timer or continuously advancing failure threshold is
established for this scoped repair.

### Parameters

Fixed terminal markers, open port locations and directions,
supplied geometries, selected part pose, gauge sector, triggering
fixture, return location and the passage destination are parameters.

## Reproducible transitions

| Entry state | Input | Expected next state | Evidence |
| --- | --- | --- | --- |
| Molly can reach the broken panel | Address the panel | Stationary first-person hand task appears | EW-002 |
| A matched pair is still open | Fit supplied straight sections and elbows end to end | A physically connected route and changed local gauge | EW-003–EW-004 |
| One gauge has reached green and others remain open | Complete the outstanding routes | The panel settles and control returns to Molly | EW-004–EW-005 |
| Molly is beside the repaired mechanism | Walk through the steam-dependent passage | The next tank-and-ladder room is traversable | EW-006 |

## Strategic and experiential structure

The wall labels expose which ends are meant to meet without
providing the sequence of turns and lengths. A local success
indicator lets the player distinguish a completed connection from
the full repair. After the control handoff, Molly still has to
take the passage herself.

## Replay and variation

In the two records different attempts and orientations lead to
the same returned view and successor. The amount of allowed
overlap, alternate routing limits, piece replacement policy and
any exact numerical gauge thresholds remain unmeasured.

## Adjacent systems and history

Root grabbing adjusts the broader diorama view elsewhere. The
later tank-and-ladder puzzle asks for a different interaction.
The separate PC VR and Pico releases are not used to infer native
Quest build equivalence.

## Normalised genome

- Action: ACT-008, ACT-072, ACT-787.
- System Behaviour: SYS-112, SYS-1980.
- Constraint: CON-893.
- Information: INF-640.
- Objective: OBJ-026.
- Time: none.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `701` (`GAME-0001`–`GAME-0701`).
- Exact genome matches: none.
- Tied near matches: `GAME-0699` — Dungeon Master (`4 / 13 = 0.307692`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Dungeon Master (GAME-0699)](dungeon-master.md) | ACT-008, ACT-072, OBJ-026, SYS-112 | Both connect interaction with a fixture to reaching the next world location. The Hall of Champions enrolls selected champions before a threshold and gated descent. The steam panel shifts from avatar navigation to spatial pipe assembly, shows local route feedback and then restores control beside the door. | Near, `0.307692`. |

## Taxonomy impact

Reuse navigation, addressing fixtures, tracked hand release, linked
mechanism opening and reaching a designated world position. Admit
the matched terminal geometry, paired local state display and
avatar-to-manipulation-to-avatar challenge transition.

## Negative results

- An isolated correct connection and its green gauge do not
  complete the full steam panel.
- The observed solved state restores exploration, but does not
  automatically carry Molly through the neighboring passage.
- The exact retail binary and the last button gesture were not
  recovered from either record.

## Delta summary

Eight genes cover the change in control, a multi-route physical
repair and one observed traversal made possible by its settlement.

## New facts

- A local diorama fixture moves control into a stationary hand task.
- Pipe gestures operate at exposed endpoints whose markings identify
  the required partners.
- A completed route has its own cue before the larger state change.
- The accepted panel returns control to Molly before she crosses.

## Principles and design implications

Use a local change of scale to make spatial placement readable.
Report each branch independently, then show the final connection
through the avatar's newly reachable route.

## Puzzle or game generation potential

Attach a short first-person repair to an addressed diorama node.
Require compatible endpoint joins for typed pairs. Give each pair a
local completion indicator. Restore the avatar beside the repaired
fixture and test that the passage is traversable as a separate step.

## New genes

- CON-893
- INF-640
- SYS-1980

## New combinations

None. None of the 274 verified combinations is a proper subset.

## Taxonomy changes

[Taxonomy Change 448](../../../research/taxonomy-changes/TAXONOMY_CHANGE_448.md).

## New questions

- How many distinct accepted layouts reach the same terminal pairs?
- Which functions of the neighboring tank are separate from steam access?

## Next recommended game

This unit closes Selection 060. Continue from the next approved
mixed-platform selection in the research plan.

## Why this game

The room clearly separates building an object at hand scale from
guiding an avatar through the resulting access change.
