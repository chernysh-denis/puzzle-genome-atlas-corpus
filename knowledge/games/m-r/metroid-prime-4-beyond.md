---
game_id: GAME-0678
slug: metroid-prime-4-beyond
game_title: "Metroid Prime 4: Beyond"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-313
    - ACT-903
  system:
    - SYS-112
    - SYS-398
    - SYS-982
  constraint:
    - CON-889
  information:
    - INF-368
  objective:
    - OBJ-357
  time: []
---

# Game: Metroid Prime 4: Beyond

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The named rooms, source statues, controller glyphs and socket counts
are parameters of the observed route and fixtures.

## Analysis scope

- Version / ruleset: English commercial base game, Nintendo Switch 2
  Edition, released December 4, 2025. Normal solo Fury Green, from
  the Arboreal Chapel side entry to the first opening of Cliffside
  Gate. The reference recording identifies the edition and difficulty.
  Exact executable version and hardware are unverified.
- Structured analysis target: PLAT-NINTENDO-SWITCH-2 in
  [platform coverage](../../platforms/games.json).
- Entry: after the low approach tunnel, stand at the chapel's side
  doorway with the yellow analyser target above it. The Psychic Visor
  is available and the Psychic Glove has yet to be acquired.
- Primary decision loop: switch to the visor and complete the
  eligible scan to open the side entrance. Acquire the Psychic Glove.
  Use the visor to identify the local energy mote and its matching
  receptacle. Grasp, aim and release the mote to open the chapel exit.
  Return through the connecting path to Cliffside Gate. Transfer
  one mote at a time into its two currently empty sockets. Move
  through the newly opened gap when the second placement settles.
- Exit: Cliffside Gate withdraws and Samus crosses into the adjoining
  recessed space. The Psychic Container is visible there. Stop
  before operating it or continuing the Fury Green route.
- Included: local movement, analysis mode, held scannable fixture
  response, acquired persistent capability, directed mote transfer,
  separately occupied compatible sockets and the resulting open gate.
- Excluded: acquisition of the visor and Morph Ball, the entry tunnel
  before this scope, surrounding combat and ordinary door details,
  container opening and its Energy Tank, Control Beam, later powers,
  cross-platform parity, exact grab and release ranges and reset
  behaviour after saving or missing a throw.
- Potential scoped module: trace the container's guided ring
  operation separately from the loose-mote transfer.
- Direct-play status: no personal Switch 2 execution or binary
  inspection. Nintendo establishes product and affordance. BeardBear's
  Normal Nintendo Switch 2 Edition trace and ProsafiaGaming's Hard
  Switch 2 trace both show the power and local placement outcomes.
  The Hard run corroborates those outcomes only. Exact patches,
  capture hardware and failed throws are unverified. Frames were
  inspected in the background with audio excluded.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| MPB-001 | Nintendo Switch 2 Edition was released on December 4, 2025. Nintendo distinguishes the Psychic Glove, which manipulates energy and mechanisms, from the later Control Beam projectile ability. | Observation | Direct | High | P1, P2 |
| MPB-002 | The player uses the Psychic Visor to target and complete a scan on the yellow chapel entry sensor. The door opens and the player can approach the glove room. The sensor's scan is the enabling interaction before acquisition, separate from seating a mote. | Observation | Corroborated | High | W2 21:13–21:21, R1 |
| MPB-003 | The room gives the Psychic Glove as a retained ability. Its tutorial shows that the Psychic Visor and a held grasp input are used to manipulate eligible targets. Later use at the gate verifies the ability stays available after leaving the acquisition room. | Observation | Corroborated | High | P2, W1 33:10–33:24 and 34:06–34:17, W2 21:24–21:37 and 22:32–22:42 |
| MPB-004 | The chapel exit accepts a single energy mote. The visor identifies the socket and the statue source. The player grasps the loose mote, aims at the socket and releases the mote, after which the door opens. | Observation | Corroborated | High | W1 33:30–33:46, W2 22:00–22:13, R1 |
| MPB-005 | Cliffside Gate has two addressable sockets, and the exterior statues supply two motes. One installed mote leaves the gate shut while a second can be grasped. The panels open only after the second socket also receives a mote. No specific source-to-slot identity or mandatory order is asserted. | Observation | Corroborated | High | W1 34:06–34:20, W2 22:32–22:46, R1 |
| MPB-006 | Traversal becomes possible after the visible gate opening. Samus moves inside, with a distinct Psychic Container visible beyond the panels. Operating the container is outside the accepted terminal. | Observation | Corroborated | High | W1 34:18–34:22, W2 22:43–22:49 |

## Basic data

- Release / origin: Nintendo, developed by Retro Studios. Official
  December 4, 2025 Nintendo Switch 2 Edition product. The bounded trace
  is the commercial solo game and does not depend on optional mouse input.
- Puzzle families: FAM-013 for typed sockets and local keys that open
  traversable fixtures; FAM-017 for the ordered acquisition, chapel
  exit and deployment of the retained ability at the earlier gate.
- P1: [Nintendo Switch 2 Edition product page](https://www.nintendo.com/en-gb/Games/Nintendo-Switch-2-Edition/Metroid-Prime-4-Beyond-Nintendo-Switch-2-Edition-2790001.html).
  Edition, date and intended psychic exploration.
- P2: [Nintendo's release explanation](https://www.nintendo.com/en-ca/whatsnew/available-now-explore-and-battle-across-an-unknown-planet-in-metroid-prime-4-beyond/).
  The glove manipulates energy and mechanisms. The Control Beam
  separately changes the trajectory of projectiles.
- W1: [BeardBear, Normal Switch 2 Edition recording](https://www.youtube.com/watch?v=3q0jQZ9ga7o&t=1985s).
  Use the visual receipts rather than the broad chapter label.
  The glove is visibly awarded at about 33:13, the one-mote exit
  opens around 33:44–33:46 and the paired gate opens at about
  34:18–34:20.
- W2: [ProsafiaGaming and Bepples, Hard Switch 2 recording](https://www.youtube.com/watch?v=z8ReMPB9C4w&t=1273s).
  Shows entry sensor, acquisition, one-mote exit and two-mote gate
  at approximately 21:13–22:49.
- R1: [Switch 2 Edition guide, chapter 2](https://gamefaqs.gamespot.com/switch-2/524791-metroid-prime-4-beyond-nintendo-switch-2-edition/faqs/82310/chapter-2-into-the-wilds-fury-green).
  Identifies the Arboreal Chapel side route and the single and paired
  placements. It also names the container beyond the gate as a
  separate interaction.
- Claim IDs: MPB-001–MPB-006.

### Reproducible fixture evidence

1. At the yellow target above the chapel door, activate the
   Psychic Visor and hold the matching scan. Around 21:14–21:19 in
   W2 the target is marked, shows scan progress and the doorway
   opens. Enter and approach the glove pickup.
2. Finish acquisition and read the Psychic Glove prompt. The
   recordings show switching to the Psychic Visor and holding
   ZL to grasp the target. The visibly selected energy source
   changes to a held glowing mote. Aim at the one socket above
   the exit and release. At about 33:34–33:46 in W1 the mote is
   held, the socket responds and the exit rises.
3. Return to the gate outside. Look toward each statue and grasp
   a single mote. Aim at a vacant socket and release to seat it.
   At about 34:08 in W1 one socket is occupied, the other remains
   unfilled and the gate stays closed. Grasp the remaining mote
   and release toward the second socket.
4. At approximately 34:14–34:20, both receptacles register energy,
   the centre glows and the panels separate. W2 shows the same
   states around 22:39–22:46. Move through and stop with the
   container visible, before grasping any part of that container.

## Mechanical decomposition

### Action Genes

- ACT-008: walk to the pickup, along the return route and through
  the opened gate. MPB-002, MPB-006.
- ACT-313: hold the active analyser on the eligible sensor or
  receptor to finish the scan. MPB-002, MPB-004.
- ACT-903: grasp one available energy mote through the visor and
  glove, then aim and release it toward a receptacle. MPB-003–MPB-005.

### System Behaviour Genes

- SYS-112: an accepted fixture placement opens the assigned
  downstream passage once its required slots are filled. MPB-004–MPB-006.
- SYS-398: acquire and retain the world-interaction ability through
  its use at multiple fixtures. The glove is not consumed by those
  placements. MPB-003–MPB-005.
- SYS-982: resolve the held yellow sensor scan into its authored
  doorway response and present distinct information for the socket
  scan. MPB-002, MPB-004.

### Constraint Genes

- CON-889: all required distinct sockets must receive separate
  eligible motes before the linked barrier opens. The single
  chapel receiver and the paired gate are two instances. MPB-004,
  MPB-005.

### Information Genes

- INF-368: expose eligible scan targets, progress and the specific
  completed result in the Psychic Visor. MPB-002, MPB-004.

### Objective Genes

- OBJ-357: acquire the reusable remote transfer ability, demonstrate
  it on the chapel exit and reopen the earlier gated route before
  using the adjacent container. MPB-003–MPB-006.

### Time Genes

None admitted. The filmed sequence does not establish a timed
acceptance window at either set of receptors.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| Side entrance closed, visor available | Hold analysis on the yellow sensor | Enter the glove room | MPB-002 |
| Reach the named glove acquisition | Complete its pickup and tutorial | Remote grasp and release become available | MPB-003 |
| Single chapel socket empty | Grasp, aim and release the resident mote | Chapel exit opens | MPB-004 |
| Paired gate closed, two sockets empty | Seat one mote | One occupied socket, second transfer still needed | MPB-005 |
| One occupied socket, another still empty | Seat the other available mote | Both receivers activate and the gate opens | MPB-005 |
| Gate visibly open | Move through the new opening | Traversable inner space with untouched container | MPB-006 |

## Strategic and experiential structure

The first fixture lets the player practise one transfer close
to the pickup. The later gate repeats the interaction without
granting passage on the first placement. Remaining sources and
unfilled sockets are separate parts of the route decision.

## Replay and variation

The independent Normal and Hard captures show the same local
one- and two-socket requirements. They are positive examples.
They do not establish the outcome of a missed throw, full
reset or choosing a different source-to-socket assignment.

## Adjacent systems and history

The Psychic Container beyond the gate is a separate fixture.
The later Control Beam, Psychic Lasso and other equipment
are different interactions outside this sequence.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-313, ACT-903 | Walk, hold the scanner and transfer a reachable mote |
| System Behaviour | SYS-112, SYS-398, SYS-982 | Open the qualified fixture, retain the glove and resolve scans |
| Constraint | CON-889 | Fill each distinct required socket |
| Information | INF-368 | Read scan eligibility, progress and typed response |
| Objective | OBJ-357 | Prove the retained ability on the exit and earlier barrier |
| Time | none | No separate deadline established |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `677` (`GAME-0001`–`GAME-0677`).
- Exact genome matches: none.
- Tied near matches: `GAME-0355` — Metroid Prime (`4 / 25 = 0.160000`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Metroid Prime (GAME-0355)](metroid-prime.md) | ACT-008, ACT-313, INF-368, SYS-982 | Both move around authored rooms, hold analysis on eligible targets and distinguish information from fixture responses. The original prologue uses lock-relative combat, evacuation and authored capability loss. Beyond's bounded chapel-to-gate route adds a retained grasp ability and requires independently filled sockets before the passage opens. | Near, `0.160000` |

## Taxonomy impact

Three admissions distinguish grasp and directed release, independent
mote occupancy and the acquisition-to-gate objective. Six existing
genes cover traversal, visor scanning, typed scan consequences,
retained ability and accepted fixture activation.

## Negative results

- The observed partially filled gate remains closed.
- The glove stays usable after the first successful placement.
- The separate container and Control Beam are outside the success
  predicate. The opening proves access, not an Energy Tank receipt.

## Delta summary

Nine genes, three new and six reused. The record follows the
Psychic Glove acquisition through the one-socket lesson and
the first two-socket gate.

## New facts

- A held sensor scan and a later mote placement can open different
  barriers. Both involve the visor, but they have different inputs.
- Each of the two motes supplies an independently seated part of
  the gate condition.

## Principles and design implications

Teach a reusable transfer with a single socket, then test whether
the player recognises the same role in a two-source fixture. Leave
remaining sources visible while one placement remains committed.

## Puzzle or game generation potential

Design a new mechanism with a remote activation tool and two
independent receivers. Verify the incomplete and complete states
separately and use readable feedback to guide each placement.

## New genes

- ACT-903
- CON-889
- OBJ-357

## New combinations

None. All 274 verified combinations were checked as proper subsets.

## Taxonomy changes

[Taxonomy Change 424](../../../research/taxonomy-changes/TAXONOMY_CHANGE_424.md).

## New questions

- Where does a missed mote return and which visible states persist?
- Does every reachable source satisfy either vacant receptor?
- How does the separately documented container guide a carried node?

## Next recommended game

Continue Selection 058 with `GAME-0679`, Jeanne d'Arc on PSP.
Follow one tactical battle through a transformation or team-attack
interaction and the observed terminal result.

## Why this game

A single retained interaction tool changes two nearby passage
conditions, clearly separating analysis, transfer and traversal.
