---
game_id: GAME-0540
slug: afterplace
game_title: Afterplace
analysis_status: reviewed
reviewed: 2026-11-17
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-737
  system:
    - SYS-037
    - SYS-045
    - SYS-386
    - SYS-578
    - SYS-1561
    - SYS-1562
  constraint: []
  information:
    - INF-179
  objective: []
  time:
    - TIM-003
---

# Game: Afterplace

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Yu, the touch thresholds, the colour and site of the slimes and the room
layout are carrier parameters.

## Analysis scope

- Version / ruleset: full English iPhone game, App Store product 1539778232
  and bundle `com.kice.afterplace`, December 2022 retail-release rules,
  normal portrait touchscreen mode. Exact app build and handset model of
  the contemporary reference recording are unverified. Contemporary
  portrait touch controls and later release history bound the rules.
- Entry: start a fresh file at first control after Yu wakes in a small
  glade. Leave north, take the first path past the crow and through the
  shrub corridor, then go past the pale house to the north exit. Reach the
  vending-machine clearing and leave it east for the stream bank.
- Primary decision loop: drag from a convenient point to walk, use taps
  for sword actions or eligible context interactions, compare local paths
  and gaps, strike a nearby slime when in reach, and walk onto a dropped
  coin. Respond to nearby enemy motion without a turn boundary. The
  second-thumb input option is documented at release, and is not required.
- Positive exit: resolve an ordinary slime encounter at the stream,
  credit a coin and return through the west path into the vending-machine
  clearing. Stop on return. This is a route checkpoint for the analysis.
  It does not grant a mission-clear result or require removing all enemies.
  Stop the negative sample at depleted health before any recovery.
- Included: local movement, contextual tapping, sword and shrubs, crow
  feedback, bordering rooms and signs, enemy motion and damage, displayed
  vitality, coin contact and return. Excluded: the house interior and
  fallen-log detour, shop purchase, optional squirrel and other bosses,
  later quests, save restoration, defeat recovery, roll unlock timing,
  landscape, controller mapping and post-launch ports.
- Direct-play status: no iPhone install, save or hardware run was opened.
  Official product data, developer control notes and contemporary iOS
  accounts corroborate the scope. The opening sequence was compared
  through timestamped still frames extracted in the background from the
  December 2022 portrait capture. No audio track was played.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| AFT-001 | Evan Kice's full iPhone app is App Store product 1539778232. Apple's US metadata dates its initial release to 9 December 2022. | Confirmed | Direct | High | P1, P2 |
| AFT-002 | A relative drag can start anywhere in the ordinary play field. A short tap swings or addresses an eligible object or character. With another thumb, movement and attack inputs can operate separately without a permanent on-screen D-pad or button layout. | Observation | Corroborated | High | P1, P2, P3, S1, R1 0:57–1:14 |
| AFT-003 | An opening crow explains the attack near a shrub row. A qualifying slash removes a shrub, prompts initial acknowledgement and can elicit other remarks when repeated. The player may proceed after the initial lesson without exhausting the remarks. | Observation | Corroborated | High | S2, R1 1:08–2:12 |
| AFT-004 | The route proceeds from the glade past the crow and the pale house, leaves the house clearing to the north, then leaves the vending-machine clearing east into the stream clearing. The player can walk back to the same vending clearing through the west edge. Local signs and scenery give bearings; the route has no objective waypoint. | Observation | Corroborated | High | P2, S1, R1 1:28–2:46, 6:50–7:00, 7:35–8:12 |
| AFT-005 | The nearby blue enemies move on the live field. A close sword swing can defeat one, and incoming contact lowers the same visible vitality pips without changing the coin tally. Missing pips recover in the vending clearing before departure; the exact trigger was not isolated. | Observation | Corroborated | High | P3, S1, S2, R1 6:56–7:12, 7:45–8:04 |
| AFT-006 | Walking to dropped coins increments their independent visible tally. The player can leave the stream clearing without clearing every creature. Returning across the boundary retains the currently shown health and tally in this capture. | Observation | Corroborated | High | S1, R1 7:47–8:12 |

## Basic data

- Evan Kice, December 2022, English iPhone App Store launch-era rule set.
  Single-player direct-touch world exploration and close-range encounters.
- Mechanical family: real-time system pressure.
- Sources accessed 2026-11-17:
  - **P1** — [official App Store listing](https://apps.apple.com/us/app/afterplace/id1539778232)
    and [Apple US product metadata](https://itunes.apple.com/lookup?id=1539778232&country=us)
    for identity, launch date, distribution and native input.
  - **P2** — [developer's product and control reference](https://afterplacegame.com/)
    and the [developer's December 2022 release announcement](https://www.reddit.com/r/iosgaming/comments/zi2xzc/afterplace_is_now_available_on_ios_info_in_comments/).
    Distinguish the release's native touch rules from the later website's
    port and landscape availability.
  - **P3** — [creator interview on Apple Developer](https://developer.apple.com/news/?id=3exkgv43),
    on one-thumb input and the way enemies drive observation and timing.
  - **S1** — [Campbell Bird's December 21, 2022 play review](https://www.148apps.com/afterplace/afterplace-review/),
    for portrait mode, dragging, tapping, independent two-thumb operation
    and local exploration. The review discusses swiping to roll at game
    level without establishing the first point of availability.
  - **S2** — [AppUnwrapper's December 16 iOS play notes](https://www.appunwrapper.com/2022/12/16/my-week-unwrapped-december-16-2022/#Afterplace),
    on the opening crow, repeated shrub reactions and tapping enemies.
  - **R1** — [App Unwrapper's December 12, 2022 gameplay capture](https://www.youtube.com/watch?v=wCzj3YH2hiA).
    Its opening portrait view has touchscreen indicators and a home bar
    consistent with iPhone. Still frames were inspected without audio.
    The capture visits additional areas; the on-foot detours and the shop
    purchase prompt are outside this record.
- Claim IDs: AFT-001–AFT-006.

## Mechanical decomposition

### Action Genes

- Reuse `ACT-008`: walk Yu through the current local geometry and
  steer toward the next traversable edge, rather than selecting a destination.
- Reuse `ACT-161`: aim and use the equipped sword on a nearby shrub or
  enemy, resolving one short-range action.
- New `ACT-737`: choose a drag for movement or a contextual tap on the
  same free touch surface. The transient input indicator follows the
  chosen start point and is not a permanent stick.
- Claim IDs: AFT-002–AFT-005.

### System Behaviour Genes

- Reuse `SYS-037`: approaching a dropped coin credits the visible tally
  without requiring another attack or automatically ending the encounter.
- Reuse `SYS-045`: an ordinary nearby hostile continues moving with live
  timing while the player pauses, advances or repositions.
- Reuse `SYS-386`: an eligible shrub disappears under a sword impact and
  the exposed portion of the route remains traversable. The same input
  leaves the surrounding rock and water boundary in place.
- Reuse `SYS-578`: enemy hits reduce the visible vitality pool and the
  same pool can refill during play. Lower health can carry to the next
  clearing. The source does not establish a specific item drop or the post-loss return.
- New `SYS-1561`: using another touch allows attacks independently of
  an active steering contact. A fixed two-stick layout is unnecessary.
- New `SYS-1562`: the nearby crow acknowledges the taught slash and
  comments differently when the player repeats it on other shrubs.
- Claim IDs: AFT-002–AFT-006.

### Constraint Genes

- No distinct formal gating constraint is assigned. Reach and the bank
  geometry condition the actions without adding a verified locked exit.
- Claim IDs: AFT-003–AFT-006.

### Information Genes

- Reuse `INF-179`: nearby creatures, vegetation, signs and traversable
  edge cues remain readable in the current room. Adjacent rooms are
  discovered by crossing their ordinary path thresholds. The vitality
  pips and coin tally are visible without an objective waypoint.
- Claim IDs: AFT-004–AFT-006.

### Objective Genes

- No game-authored clear predicate was found for this ordinary
  run-off from one clearing and back. Defeating a local slime and
  returning is the scope's reproducible stop condition.
- Claim IDs: AFT-004, AFT-006.

### Time Genes

- Reuse `TIM-003`: movement, enemy advances and live contact can change
  the local state while the player chooses a tap or a new approach.
- Claim IDs: AFT-002, AFT-005, AFT-006.

## Reproducible transitions

| Before | Action or event | Bounded resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Yu stands in the glade at first control | Drag from an unoccupied part of the play field and release after moving north | Yu follows the local direction and stops on release | Walking requires no fixed virtual pad or tap-to-destination | AFT-002 |
| The crow explains one sword use near the shrubs | Tap to swing at the nearest shrub, then repeat at other reachable shrubs | Cut vegetation disappears and the tutor produces different remarks | World change and responsive instruction are separate | AFT-002, AFT-003 |
| Yu has reached the vending-machine clearing from the south | Check the sign or take the east edge directly | Crossing the edge discloses the stream and its local threats | The room transition is spatial, and the sign is contextual guidance | AFT-004 |
| A blue slime is moving near the stream bank | Approach to short reach and tap to strike, then step across a dropped coin | The slime can be defeated and the coin tally increments independently | Defeat and credit can be separate local transitions | AFT-005, AFT-006 |
| The route remains open with local encounters available | Return through the western opening before depleting vitality | The vending-machine room reappears with current health and coins | The exit does not require all hostiles to be defeated | AFT-004, AFT-006 |

## Strategic and experiential structure

A visible trail narrows into local vegetation and then opens beyond
the house. Separate regions encourage orientation by landmarks. The
short sword reach asks the player to manage how close a slime is to
Yu before committing a tap. Defeating a slime and touching its drop
are different actions. Use the health and tally displays to observe
the outcome of the visit, and choose the same exit back rather than
pursue the other available routes.

## Replay and variation

- Try two different arbitrary drag start points in the empty glade.
  Use the same movement direction, then release.
- In the shrub row, compare one cut with additional cuts while the
  crow is present. Observe the message and the independent world change.
- In the stream clearing, compare striking one slime with walking
  back before every hostile has been removed. Exact enemy paths,
  contact thresholds and defeat recovery remain outside this packet.

## Adjacent systems and history

- The closest previous signature, Super Mario 64, has local direct
  movement, visible hazards, autonomous bodies, live vitality and
  contact pickups. Its scoped objective is a required summit throw
  sequence, followed by a separate Star collection. Afterplace's
  forest is traversed by relative drag and contextual tapping and
  the local sword encounter can be left without a boss clear.
- Fixed virtual controls would offer independent movement and action
  through assigned areas. Afterplace allows flexible placement and
  changes the allocation when the player supplies a second contact.
- The independent engine objective of a sealed combat room does not
  transfer to the stream clearing.

## Normalised genome

| Type | Active gene IDs | Candidate genes or parameters |
| --- | --- | --- |
| Action | `ACT-008`, `ACT-161`, `ACT-737` | local walking, equipped sword, free touch surface |
| System Behaviour | `SYS-037`, `SYS-045`, `SYS-386`, `SYS-578`, `SYS-1561`, `SYS-1562` | coin credit, enemy motion, breakable vegetation, health, second contact, responsive tutor |
| Constraint | none | reach and traversable route geometry |
| Information | `INF-179` | local field, edge cues, threats and resources |
| Objective | none | analytic return boundary |
| Time | `TIM-003` | encounter proceeds while the player acts |

Canonical signature:

`ACT-008,ACT-161,ACT-737; SYS-037,SYS-045,SYS-386,SYS-578,SYS-1561,SYS-1562; none; INF-179; none; TIM-003`

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `539` (`GAME-0001`–`GAME-0539`).
- Exact genome matches: none.
- Tied near matches: `GAME-0460` — Super Mario 64 (`6 / 17 = 0.352941`).
- Supported combination subsets: none.
- Scan date: 2026-11-17.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| `GAME-0460` — Super Mario 64 | `ACT-008`, `INF-179`, `SYS-037`, `SYS-045`, `SYS-578`, `TIM-003` | Both steer through a visible live field with hazards, pickups and continuing health. Mario uses camera changes, summit throws and a required Power Star. Yu has touch-dependent steering and sword, repeated tutor feedback and an open retreat after a local encounter. | Tied near (`0.352941`) |

### Preserved research notes

- New genes: `ACT-737`, `SYS-1561`, `SYS-1562`.
- Classification result: `New gene`.
- Evidence and reasoning: flexible placement differs from selecting a
  destination. Concurrent roles are a rule for more than one active contact,
  independent of the use of a single contact. The first and repeated
  tutor reactions differ without a new authored objective.

## Taxonomy impact

- Registry changes: eight definitions reused, three Active additions.
- Taxonomy-change record: [TAXONOMY_CHANGE_287](../../../research/taxonomy-changes/TAXONOMY_CHANGE_287.md).

## Negative results

- No combat gate, player waypoint or required coin threshold is inferred
  from this stopping rule.
- The extended controller and later accessibility options in the App Store
  record do not establish identical behavior at launch.
- The stills show missing and restored vitality. The exact restorative
  item or command, timing, drop probability and native save state are
  not classified.

## Delta summary

## New facts

- [Observation | Corroborated | High] Flexible touch controls allow
  direct one-finger movement and contextual taps. A second contact
  supports a separate attack command.

## New genes

- [Observation | Corroborated | High] Three additions in
  `TAXONOMY_CHANGE_287`.

## New combinations

- [Observation | Corroborated | High] No verified combination is a
  proper subset of the scoped genome.

## Taxonomy changes

- [Observation | Corroborated | High] `TAXONOMY_CHANGE_287`.

## New questions

- Which exact trigger restores the vitality observed near the first
  vending machine, and at what event does the first roll become available?

## Next recommended game

- [Observation | Corroborated | High] Selection 042 ends at this
  unit. A future game requires a newly selected subject.
