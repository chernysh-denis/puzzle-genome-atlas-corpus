---
game_id: GAME-0722
slug: quackshot-starring-donald-duck
game_title: "QuackShot Starring Donald Duck"
analysis_status: reviewed
reviewed: 2026-11-25
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-096
    - ACT-202
    - ACT-295
    - ACT-341
  system:
    - SYS-398
    - SYS-2018
    - SYS-2019
    - SYS-2020
  constraint:
    - CON-296
    - CON-902
  information:
    - INF-192
    - INF-425
    - INF-653
  objective:
    - OBJ-026
  time:
    - TIM-003
---

# Game: QuackShot Starring Donald Duck — Duckburg and Mexico return route

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Plunger colours, the Hero Key and the named regions are instances of rule boundaries.

## Analysis scope

- Version / ruleset: North American English Sega Genesis commercial
  cartridge, 1991. Reproduce with the manual's default controls.
  W1 is NTSC Genesis-labelled and W2 is Genesis-labelled. Exact
  ROM revision, physical hardware and recorded input traces are unavailable.
- Structured analysis target: `PLAT-SEGA-GENESIS`. Begin on the
  opening map with the yellow plunger. Reach the first Duckburg
  flag, fly to Mexico and reach the closed ruins. Return for the
  Hero Key, use it at the ruins, reach Goofy and take the red
  plunger. Return to the first Duckburg flag and reach the top
  of its formerly blocked wall. Stop at the first rooftop
  transition, before the wire route and Gyro's reward.
- Primary decision loop: read near obstacles, stun foes long
  enough to pass, then use checkpoint calls and the map to follow
  the clues between regions. Use the key at its matching door.
  After the upgrade, shoot the wall at useful heights and jump
  onto the attached plungers.
- Included: direct movement, reduced-height slides through low
  passages, aimed plunger shots, brief hostile interruption, the
  first flag cue and aircraft transfers, the linked key, the
  plunger upgrade and the red-plunger ascent.
- Excluded: the optional Transylvania detour visible in W1,
  force or frame arithmetic, full ammo and health economies,
  exact attachment limit and expiry, the note's later riddle,
  green plungers, bubblegum, bosses, death/continue settlement,
  and save persistence in collections or emulators.
- Direct-play status: no personal console or emulator run.
  The Sega of America printed booklet and two independently
  attributed Genesis play recordings support the scope. The
  recordings were checked through background silent frames.
  No executable or input telemetry was inspected.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| QS-001 | Sega of America issued the English Genesis commercial cartridge in 1991. The printed default maps A to Dash, B to Shoot and C to Jump. | Observation | Corroborated | High | P1 PDF pp. 5, 7, 24; S1 |
| QS-002 | The unlimited yellow plunger temporarily stops eligible enemies. Aiming is directional, including up. The route can proceed past the stopped enemy while other hazards continue. | Observation | Corroborated | High | P1 PDF pp. 9, 11; W1 02:15–02:53; W2 04:15–04:45; S3 |
| QS-003 | At the first Duckburg checkpoint, the high wall blocks continuation. A local hint names the need to climb high walls but omits the required tool. Nearby, the HUD Flag Signal discloses the available aircraft call. | Observation | Corroborated | High | P1 PDF pp. 11, 14; W1 03:05–03:22; W2 04:47–05:02 |
| QS-004 | Stand by the reached flag, call the airplane from the item menu and choose an offered map destination. First arrival is at the regional start. On subsequent trips the avatar arrives beside the recorded flag with carried state. | Observation | Corroborated | High | P1 PDF pp. 8, 13–14; W1 03:19–03:32, 07:11–07:42; W2 04:57–05:12, 07:07–07:40 |
| QS-005 | The first visit to the Mexico ruins identifies the Hero Key in Duckburg. An NPC there grants it after the clue is known. With that key, use the menu at the Mexico entrance to open the door and enter. | Observation | Corroborated | High | S2, S3; W1 05:37–05:45, 07:15–07:47; W2 06:53–07:26 and 07:38–07:49 |
| QS-006 | In the ruins, a low slide changes the envelope and passes beneath low ceilings. Ladders and jumps connect higher ledges. | Observation | Corroborated | High | P1 PDF p. 9; S2; W1 08:30–09:44; W2 07:49–09:46 |
| QS-007 | Goofy gives Donald the red plunger and a note. The acquired plunger mode is carried across the return flight and remains available beside the earlier wall. | Observation | Corroborated | High | P1 PDF p. 12; S2, S3; W1 09:45–10:06 and 11:36–11:44; W2 09:50–10:17 and 11:47–11:52 |
| QS-008 | Red shots attach to the Duckburg wall and act as local supports. Jumping between impacts reaches the upper boundary. W2 shows multiple attached plungers and then enters the rooftop scene. | Observation | Corroborated | High | P1 PDF p. 12; S2, S3; W1 11:39–11:49; W2 11:47–11:54 |

## Basic data

- Release / origin: Sega developed the game and Sega of America
  published the North American cartridge. The retail booklet carries
  Sega and Disney 1991 copyright. Year-level catalog agreement
  supports 1991; no exact North American day is used.
- Platform or physical form: single-player North American Genesis
  cartridge. Later compilations and non-North-American timing
  differences are outside this fixture.
- Mechanical families: `FAM-013` for the key, matching entrance
  and acquired wall tool, and `FAM-017` for the sequence of
  earlier incompleted routes, tool acquisition and return.
- Primary source accessed 2026-11-25:
  - **P1:** [Sega of America Genesis instruction booklet](https://www.retrogames.cz/manualy/Genesis/QuackShot_-_Genesis_-_Manual.pdf),
    digitised retail booklet, PDF pp. 5, 7–9, 11–14 and 24.
    Control bindings, regional choice, weapon rules, contextual
    item-usage, the Flag Signal and destination resolution.
- Secondary and recorded play evidence:
  - **S1:** [MobyGames regional release catalogue](https://www.mobygames.com/game/7960/quackshot-starring-donald-duck/releases/)
    for the commercial United States issue.
  - **S2:** [Raph136's Genesis walkthrough](https://gamefaqs.gamespot.com/genesis/586403-quackshot-starring-donald-duck/faqs/37739)
    for the Duckburg/Mexico key dependency, low passages and
    the wall transition. Solo regional route may include or omit
    later detours.
  - **S3:** [Independent Genesis replay and stills](https://superadventuresingaming.blogspot.com/2013/01/quackshot-genesismega-drive-replay.html)
    corroborate temporary interruption, the ineffective initial
    plunger at the tall wall, and later temporary footholds.
  - **W1:** [Retro Game Spacko, NTSC Genesis run](https://www.youtube.com/watch?v=mCGTDMxX_Oo&t=128s).
    Note the optional Transylvania stop after Mexico A. Its later
    return to Duckburg shows the key handover, then Mexico B and
    the red-plunger climb.
  - **W2:** [BitsAndGlory, Genesis run](https://www.youtube.com/watch?v=IS-zpHhrCmk&t=230s).
    First Duckburg and Mexico flags, key at 07:24, item-menu
    entrance around 07:44, red upgrade around 10:14, and first
    wall climb at 11:47–11:54.
- Claim IDs: `QS-001`–`QS-008`. To reproduce, compare firing
  across the wall with the initial and the upgraded shot.
  Record the popped-out flag, reached region, landing coordinate
  and carried key or plunger state on each departure and arrival.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: walk, jump, dash and climb ladders where
  support permits movement (`QS-001`, `QS-006`, `QS-008`).
- Reuse `ACT-096`: choose one offered region on the map and
  delegate the flight to the game (`QS-004`).
- Reuse `ACT-202`: use the slide to adopt a lower posture and
  cross strips beneath the ordinary walking envelope (`QS-006`).
- Reuse `ACT-295`: choose a position and fire the plunger.
  The active shot and targeted surface or enemy determine its
  effect (`QS-002`, `QS-007`, `QS-008`).
- Reuse `ACT-341`: address the actor or fixture to receive a
  key or upgrade, use the key at its entrance or call a plane
  from the flag context (`QS-003`–`QS-007`).

### System Behaviour Genes

- Reuse `SYS-398`: acquiring the upgraded plunger adds the
  retained traversal ability to the continuing character
  (`QS-007`, `QS-008`).
- New `SYS-2018`: a susceptible foe temporarily stops after
  a plunger hit, leaving a passage interval (`QS-002`).
- New `SYS-2019`: wall impacts of the eligible shot create
  local surfaces at the impact height (`QS-007`, `QS-008`).
- New `SYS-2020`: regional landing resolves to the start on a
  new visit or at the last reached flag on return. Possessions
  travel with the character (`QS-004`–`QS-008`).

### Constraint Genes

- Reuse `CON-296`: the secured entrance admits the specific
  Hero Key at its location (`QS-005`).
- New `CON-902`: the ordinary plane call requires being
  close to the reached travel marker (`QS-003`, `QS-004`).

### Information Genes

- Reuse `INF-192`: the side view discloses local enemies,
  low passages, surfaces and a reachable wall approach
  (`QS-002`, `QS-006`, `QS-008`).
- Reuse `INF-425`: the first Duckburg contact describes the
  need to climb a high wall. The actual tool is not identified
  by this particular cue (`QS-003`).
- New `INF-653`: the Flag Signal discloses transport availability
  from the current position (`QS-003`, `QS-004`).

### Objective Genes

- Reuse `OBJ-026`: reach the high route beyond the earlier
  Duckburg wall after adding compatible supports
  (`QS-003`, `QS-007`, `QS-008`).

### Time Genes

- Reuse `TIM-003`: the platform route, attacks and enemies
  progress in live time, including the available passage
  interval after a stun (`QS-002`, `QS-006`, `QS-008`).

## Formal state and transitions

The state tracks the active region, player position and posture,
last reached travel flag per region, the carried key, active
plunger capability, local hostile interruption and attached
supports. Plane-call legality depends on the current reached
flag and position. Arrival resolves using the selected region's
stored flag state. A shot resolves against the actual contacted
target or face. The ascent preserves the solid wall and adds
a sequence of landing supports.

## Reproducible transitions

| Before | Action or event | Bounded resolution | Claim ID |
| --- | --- | --- | --- |
| Initial Duckburg route contains an eligible moving foe | Hit with the yellow plunger and advance | The foe stops for a short passage interval | QS-002 |
| First Duckburg flag marks the approach to a high wall | Read the hint and call the plane from beside the flag | The map offers Mexico as a destination; first arrival starts its route | QS-003, QS-004 |
| The Mexico ruins entrance is closed | Read the clue and fly to Duckburg | The original Duckburg checkpoint is the landing; talking there grants the Hero Key | QS-004, QS-005 |
| The Hero Key is carried on the return to Mexico | Use it by the closed ruins entrance | The door opens and the avatar enters | QS-004, QS-005 |
| A low corridor interrupts the ruins route | Slide below the ceiling and reach Goofy | Taking the offered upgrade changes the plunger capability | QS-006, QS-007 |
| Donald climbs out and calls the plane by the Mexico flag | Return to Duckburg | The wall is reached from the recorded flag with the red plunger | QS-004, QS-007 |
| The original tall wall remains solid | Shoot the face at successive reachable heights and jump onto the supports | The player reaches the top and enters the first rooftop scene | QS-008 |

## Strategic and experiential structure

A shot can create an opening in enemy timing or a new spatial
support. Decide which effect the immediate situation needs.
Checkpoint travel shortens the return to the obstacle and
preserves the tool gained elsewhere. Investigating the Mexico
door before revisiting Duckburg determines which item to seek.

## Replay and variation

The witnesses differ in route order. W1 also visits Transylvania
before collecting the key. W2 demonstrates key retrieval and
the wall ascent without that detour. Both reach the same route
outcome and show the local control interaction.

## Adjacent systems and history

The complete game later grants bubblegum ammo, the green
plunger and a use for Goofy's note. These systems are outside the
present route. The paper note is visible evidence of the encounter
but its contents are not resolved by a later puzzle here.

## Normalised genome

- Action: ACT-008, ACT-096, ACT-202, ACT-295, ACT-341.
- System Behaviour: SYS-398, SYS-2018, SYS-2019, SYS-2020.
- Constraint: CON-296, CON-902.
- Information: INF-192, INF-425, INF-653.
- Objective: OBJ-026.
- Time: TIM-003.

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `721` (`GAME-0001`–`GAME-0721`).
- Exact genome matches: none.
- Tied near matches: `GAME-0615` — Skate Story (`5 / 20 = 0.250000`).
- Supported combination subsets: none.
- Scan date: 2026-11-25.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Skate Story (GAME-0615)](../s-z/skate-story.md) | ACT-008, ACT-341, OBJ-026, SYS-398, TIM-003 | Both move in live time, interact with an authored source of a retained capability and use it to reach a previously blocked route. Skate Story learns the Ollie from the obelisk and lands qualified jumps at four crests to open a portal. QuackShot carries a matching key between regions, takes the new projectile and places footholds at its wall impact heights. | Near, `0.250000`. |

## Taxonomy impact

Retain the direct movement, tool action, door credential and
context-dependent interaction vocabulary. Distinguish temporary
enemy interruption, shot-built footholds, flag-dependent travel
access, resolved destination anchoring and the visible local cue.
An automatic retry from death is a different transition.

## Negative results

- The initial yellow shot does not provide the red shot's support
  on the tall wall.
- Seeing the Mexico entrance does not open it. Holding the Hero Key
  must be followed by using it at the door.
- Returning to the reached flag does not restore the earlier
  inventory. The newly acquired capability travels with the avatar.
- The documented route does not establish exact stun or support
  duration, a maximum number of wall attachments or native ROM identity.

## Delta summary

Record a route blocked by height, one by a key, and the
transport mechanism that makes revisiting both practical.
The same player uses the gained shot to supply small climbable
surfaces while the original wall remains in place.

## New facts

- The initial and upgraded plunger uses differ at eligible walls.
- Revisited regions use the latest reached travel flag rather
  than their original entry when a flag has been recorded.
- The key interaction and the wall climb are separate types of
  route admission.

## Principles and design implications

Put a clear unresolved barrier beside a useful travel anchor.
A later capability can change how the same space is traversed
without removing the obstacle. Leave enough local feedback to
tell a created support from a briefly interrupted foe.

## Puzzle or game generation potential

Provide two bounded regions with confirmed return markers and
different gates. Let the key open one entrance and the wall
tool create incremental supports at specific impact heights.
Verify that returning preserves capabilities and that the
original weapon cannot produce the wall steps.

## New genes

- CON-902
- INF-653
- SYS-2018
- SYS-2019
- SYS-2020

## New combinations

None.

## Taxonomy changes

[Taxonomy Change 468](../../../research/taxonomy-changes/TAXONOMY_CHANGE_468.md).

## Next recommended game

holedown on Android is the next Selection 063 unit.

## Why this game

Its visible route links a temporary shot effect, one exact item
gate, retained world travel and player-placed climbing supports.

## Review status

Reviewed 2026-11-25 for the North American commercial Genesis
cartridge, through the first Duckburg wall after the Mexico upgrade.
