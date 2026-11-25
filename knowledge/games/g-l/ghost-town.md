---
game_id: GAME-0680
slug: ghost-town
game_title: "Ghost Town"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-072
    - ACT-085
    - ACT-087
    - ACT-787
  system:
    - SYS-112
    - SYS-1952
  constraint:
    - CON-136
  information:
    - INF-003
    - INF-626
  objective:
    - OBJ-358
  time:
    - TIM-002
---

# Game: Ghost Town

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The lighthouse, component appearance and three named rows parameterise the accepted fixture.

## Analysis scope

- Version / ruleset: Fireproof Games' English commercial Meta
  Quest base game, released April 24, 2025, Meta store product
  9531494193591052. Single player, Tanner's Rock lighthouse,
  after the severance ritual. The recording published on
  launch day links the Quest product. Its capture build and headset revision
  are unverified.
- Structured analysis target: PLAT-META-QUEST in
  [platform coverage](../../platforms/games.json).
- Entry: resume in the lantern machinery room after the ritual,
  before servicing the lamp. Approach the housing controls with
  the beacon dark and the damaged bulb still in its housing.
  W1 starts the fixture with the earlier room-power work complete.
- Primary decision loop: inspect the housing and three readiness
  rows. Use the nearby mechanism controls to gain service access.
  Lower the housing, remove the damaged bulb, find the intact spare
  behind a movable cabinet shelf and seat it in the exposed receiver.
  Set the rotation to engaged and raise the housing again. Verify
  the three readiness lights and operate Light Power. Confirm that
  the beacon visibly lights.
- Exit: the powered lighthouse illuminates the lantern chamber.
  Stop at the first visible running light, before leaving the room
  or communicating with Angela.
- Included: direct movement of captive controls and cabinet shelves,
  tracked handling of loose bulbs, compatible socket seating,
  reversible housing travel with the same installed part, separate
  readiness indicators and the explicit light command.
- Excluded: earlier power and floor puzzles, the ritual and its
  offerings, the route to the island, later scanner and archives,
  unrelated cabinet contents, optional hints and exact input binds,
  other platforms, controller reach tolerances, reset and save
  behaviour, and attempted power at every invalid indicator state.
- Potential scoped module: analyse the earlier reconfigurable
  electrical puzzle separately from the lamp-service fixture.
- Direct-play status: no personal headset execution or binary
  inspection. Fireproof and Meta identify the commercial Quest
  game. MissChiefVR's launch-day recording supplies the main trace.
  Al Martin Gaming independently shows the service, reassembly
  and lit result. W2 confirms those transitions without establishing
  cross-platform parity. Both recordings were inspected as frames
  in the background, with audio excluded.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| GHT-001 | Fireproof's single-player VR adventure shipped commercially on Meta Quest in April 2025. The April 30 developer update places the launch on the immediately preceding Thursday, April 24. The developer documents physical interaction with tracked controllers. | Observation | Direct | High | P1–P3 |
| GHT-002 | The dark lighthouse has a local panel with separate Rotation Engaged, Bulb Housing Raised and Bulb Check rows above the Light Power control. Rotation and housing can be marked ready together while the bulb row is red. | Observation | Corroborated | High | W1 43:04, 43:20 and 44:20; W2 38:04–38:07 |
| GHT-003 | A nearby drawing shows the lamp assembly. The hand-operated octagonal control and its adjacent housing lever change access to the lower assembly. At service height the physically damaged bulb can be grasped and taken out. The housed part and cabinet controls have different local motions. | Observation | Corroborated | High | W1 42:45–43:28; W2 38:10–38:35 |
| GHT-004 | Individual cabinet shelves can be pulled. One exposes an intact amber crystal-like bulb. The player takes that spare from the shelf, carries it to the lowered housing and seats it in the empty receiver. It remains in place after the hand releases it. | Observation | Corroborated | High | W1 43:38–43:58; W2 38:40–38:58 |
| GHT-005 | The replacement can be installed while the housing is still down. The rotation control and housing lift remain separate operations after installation. The indicators eventually show all three checks green while the beacon is still dark and the power control has yet to be moved. | Observation | Corroborated | High | W1 43:58–44:20; W2 38:55–39:21 |
| GHT-006 | After the ready state, the player operates Light Power. The lens and room visibly illuminate. The result differs from the ready state before the final input. | Observation | Corroborated | High | W1 44:19–44:24; W2 39:19–39:29 |

## Basic data

- Release / origin: Fireproof Games. April 2025 standalone Meta Quest
  digital release. The game is played from Edith's first-person view.
- Puzzle families: FAM-013 for the typed spare and its fixture,
  and FAM-017 for exposing, replacing, raising and commissioning
  the same assembly in a mechanically valid sequence.
- P1: [Fireproof Games product page](https://www.fireproofgames.com/games/ghost-town).
  Identifies direct VR manipulation and the product across releases.
- P2: [Meta Quest store product](https://www.meta.com/experiences/ghost-town/9531494193591052/).
  The official Quest product identifier and supported platform.
- P3: [Fireproof Games launch update, dated April 30](https://steamcommunity.com/app/2496180/allnews/).
  The Quest launch precedes the later Steam release and is dated to
  the preceding Thursday in the studio update.
- W1: [MissChiefVR's launch-day recording](https://www.youtube.com/watch?v=dPZNGpAZIy8&t=2560s).
  The Lighthouse Lightbulb Puzzle chapter starts at 42:40. Follow
  the housing to the installed bulb and the separate power switch.
- W2: [Al Martin Gaming, Restarting the Light](https://www.youtube.com/watch?v=X00gN-TS8tA&t=2264s).
  Shows the original damaged bulb at service height, the cabinet
  replacement and the lit result. Exact build and headset are unstated.
- Claim IDs: GHT-001–GHT-006.

### Reproducible fixture evidence

1. At the dark beacon, read the housing legend and the nearby
   three-row panel. Before the assembly is fully prepared, the
   rows can disagree. W2 at 38:04 has the first two checks green
   and the bulb check red.
2. At the lower control stand, set the linked rotary mechanism
   and use the housing lever to bring the assembly down. Confirm
   that the receiver is reachable at the lower opening. In W2
   around 38:31–38:35, the red broken bulb is visible there and
   then in the player's hand.
3. At the tall cabinet, pull shelves until the intact replacement
   is visible. Take it using the tracked hand and carry it to the
   vacant socket. At 43:52–43:58 in W1 and 38:53–38:58 in W2 the
   amber bulb is moved into the lower housing and remains seated.
4. Restore rotation and use the raise position on the housing
   lever. Verify the actual housing movement and all three green
   rows. W1 at 44:20 and W2 around 39:20 still show a dark light
   assembly after the readiness states have settled.
5. Turn the separate Light Power control. At around 44:21–44:24
   in W1 the upper lens chamber becomes bright. W2 confirms the
   same effect near 39:22–39:29. Stop before following the next lead.

## Mechanical decomposition

### Action Genes

- ACT-072: operate the addressed Light Power control to start
  the ready beacon. GHT-006.
- ACT-085: turn the linked mechanism and drag its lever or the
  cabinet shelf through its available travel. GHT-003–GHT-005.
- ACT-087: commit the acquired intact bulb into the matching
  local socket at service height. GHT-004.
- ACT-787: grasp the portable damaged or spare bulb with a
  tracked hand, carry it and release it at the intended site.
  GHT-003, GHT-004.

### System Behaviour Genes

- SYS-112: the accepted housing control exposes the reachable
  lamp assembly for downstream service. GHT-003.
- SYS-1952: move the same housing along its captive guide between
  service and operating positions while retaining the seated
  replacement on the way up. GHT-003–GHT-005.

### Constraint Genes

- CON-136: expose the socket, exchange the bulb and return
  the assembly to its ready state for the final command.
  The two traces establish working configurations. They do not
  exhaust the response to every invalid attempt. GHT-002–GHT-006.

### Information Genes

- INF-003: the fixed spare is out of view until the relevant
  cabinet shelf is pulled. GHT-004.
- INF-626: expose the current state of each named machine check,
  separately from the final light output. GHT-002, GHT-005.

### Objective Genes

- OBJ-358: change the failed lighthouse into a visibly lit
  beacon through replacement, ready position and intentional
  startup. GHT-002–GHT-006.

### Time Genes

- TIM-002: intermediate decisions can be made at the player's pace.
  The trace pauses for inspection without a countdown. The
  housing animation follows its authored command. GHT-002–GHT-006.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Dark beacon, damaged bulb in the housing | Inspect panel and housing drawing | Named checks and service affordance identified | GHT-002, GHT-003 |
| Receiver above its service height | Reorient local control and lower housing | Broken bulb accessible for extraction | GHT-003 |
| Damaged bulb in reachable receiver | Grasp and remove it | Vacant receiver | GHT-003 |
| Cabinet shelf shut | Pull the shelf, grasp the intact spare | Portable bulb in hand | GHT-004 |
| Empty accessible receiver | Seat the compatible spare and release | Intact bulb retained in lowered fixture | GHT-004, GHT-005 |
| Replacement seated, lower position | Restore rotation and raise the housing | Three green checks, light still off | GHT-005 |
| Prepared dark beacon | Operate Light Power | Lens lights and chamber brightens | GHT-006 |

## Strategic and experiential structure

The panel points to a particular readiness condition instead of
collapsing all problems into one failure light. Service access
is itself temporary. It makes the receiver reachable, then must
be changed again to ready the beacon. The green panel therefore
gives a useful intermediate result before the task is complete.

## Replay and variation

W2 shows the first two rows ready before the repair, then lowers
the housing to remove the broken part. Both traces finish with the
same visible checks and a separate power command. Neither tests
a full set of wrong bulbs, every order of individual settings
or loading a save during the exchange.

## Adjacent systems and history

The earlier generator, floor and ritual are part of the route to
this fixture. The later scanner and archive investigation begin
after its terminal. Their rules are outside the lamp-service genome.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-072, ACT-085, ACT-087, ACT-787 | Command power, move captive controls and handle and place the bulb |
| System Behaviour | SYS-112, SYS-1952 | Expose service access and translate the same assembly back to operation |
| Constraint | CON-136 | Satisfy the service and setup dependencies |
| Information | INF-003, INF-626 | Expose the hidden spare and read each named readiness state |
| Objective | OBJ-358 | Restore and intentionally start the local beacon |
| Time | TIM-002 | Deliberate untimed manipulations and visual inspections |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `679` (`GAME-0001`–`GAME-0679`).
- Exact genome matches: none.
- Tied near matches: `GAME-0085` — The Room (`7 / 15 = 0.466667`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [The Room (GAME-0085)](../s-z/the-room.md) | ACT-072, ACT-085, ACT-087, CON-136, INF-003, SYS-112, TIM-002 | Both expose and operate authored physical fixtures step by step. The Room reshapes a key, uses a lens to reveal alignment and opens an enclosure. Ghost Town transfers a loose replacement with a tracked hand, raises that same installed part, checks named readiness lights and deliberately switches on the beacon. | Near, `0.466667` |

## Taxonomy impact

Three new definitions separate ready-state feedback, reversible
service access and the intentionally powered endpoint. Existing
physical input, item delivery and dependency definitions cover
the other transitions.

## Negative results

- A housing-ready row can be green while the bulb check is red.
- The installed bulb in the lowered housing is an intermediate
  repair state.
- Three green lights precede the actual light output. The
  state before the explicit power command is visibly dark.
- Neither recording establishes that every conceivable order,
  invalid activation or mis-seated bulb was tested.

## Delta summary

Eleven genes, three new and eight reused. A complete local
mechanism puzzle goes from dark and damaged to an observed lit
beacon by way of a still-dark ready state.

## New facts

- Access and readiness are different positions of the same
  housing and the installed bulb stays with it.
- The named checks identify what to solve before the separate
  start command.

## Principles and design implications

Distinguish where a part is accessible, when it satisfies the
machine's setup conditions and when the player commands operation.
Give the player feedback for each condition before the final effect.

## Puzzle or game generation potential

Design an original repair station with a captive, serviceable
assembly and individually visible diagnostics. Verify the power
state separately from a successful replacement.

## New genes

- INF-626
- SYS-1952
- OBJ-358

## New combinations

None admitted. All 274 verified combinations were checked as proper subsets.

## Taxonomy changes

[Taxonomy Change 426](../../../research/taxonomy-changes/TAXONOMY_CHANGE_426.md).

## New questions

- What does each row show if the housing is lowered again after
  starting the light?
- Can the intact bulb be seated from multiple orientations?
- Which partial configurations persist across a checkpoint?

## Next recommended game

Continue Selection 058 with `GAME-0681`, the original English
North American Dreamcast release of Power Stone 2. Follow one
four-fighter stage through object use, a stage or power change
and the recorded result.

## Why this game

Its physical repair makes preparedness distinguishable from
actual operation through two separate visible results.
