---
game_id: GAME-0612
slug: pipistrello-and-the-cursed-yoyo
game_title: "Pipistrello and the Cursed Yoyo"
analysis_status: reviewed
reviewed: 2026-11-21
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-813
  system:
    - SYS-037
    - SYS-398
    - SYS-1735
    - SYS-1805
    - SYS-1806
  constraint:
    - CON-349
    - CON-854
  information:
    - INF-179
  objective:
    - OBJ-080
  time:
    - TIM-003
---

# Game: Pipistrello and the Cursed Yoyo

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The lever, bridge, panels and trapdoor are authored instances of the
scoped traversal rules.

## Analysis scope

- Version / ruleset: original Nintendo Switch commercial eShop game,
  released 28 May 2025. English regular story progression through
  Abandoned Tunnels, bounded to the first exit into the Safe House.
  W1 identifies version 1.1 in docked original-Switch mode; W2 is
  period Switch corroboration with its exact build unreported.
- Primary decision loop: take dry ledges and use the ordinary tethered
  yo-yo against nearby obstructions or foes. At the first wide pool,
  demonstrate and gain Offstring Throw. Hit distant linked switches
  to make or redirect walkable crossings, then clear the sealed
  encounter and enter the Safe House.
- Entry: regain control after Pippit falls into the Abandoned Tunnels
  and speaks to his aunt in the yo-yo. The manor before the fall is
  context for the initial tool and controls.
- Exit: the final orange barriers lift, Pippit reaches the marked
  red trapdoor and appears inside the Safe House. Stop at the first
  Safe House handoff before South Plaza.
- Included: navigation, short jumps to supported ledges, ordinary
  tethered attacks, the first demonstrated detached throw and its
  ability notice, later player-operated throws to bridge switches,
  the sealed hammer-foe encounter and actual trapdoor entry.
- Excluded: Walk-the-Dog and later abilities, city exploration, badges,
  contracts, charge or damage coefficients, assist setting parity,
  menu remapping, full game-over and resume testing, sequence breaks,
  demo progression, Switch 2 edition, other platforms and later patches.
- Suggested later scope: follow one mall crossing after the taught
  Walk-the-Dog ability with its own reward or exit.

## Direct-play status

No direct play was performed. Nintendo and the publisher identify the
original commercial Switch release. The first-party game director
explains why knowledge of different yo-yo moves changes the city’s
routes. Handheld Players identifies a publisher-provided review
key, docked original Switch and version 1.1; the recorded route
includes the release game’s tunnel exit and later city access.
The independent 8-Bit Walkthru Switch capture supports the route
and identifies ZR and Y as the input pair. Both are consulted through
static frames and written descriptions. The build of the second
capture, exact timing, assist values throughout each run and actual
save persistence were not independently tested.

## Claim ledger

| ID | Claim | Claim status | Evidence quality | Confidence | Evidence |
| --- | --- | --- | --- | --- | --- |
| PY-001 | The target is the original Nintendo Switch commercial release from 28 May 2025. The bounded route enters Abandoned Tunnels and exits into the Safe House. | Confirmed | Corroborated | High | P1–P3, W1 9:57 and 19:09, W2 14:00 and 26:40. W1 describes original Switch v1.1; this is evidence for an identified capture, not a survey of later builds. |
| PY-002 | Pippit moves along dry floors and jumps among separated ledges. The ordinary yo-yo remains visibly tethered during nearby attacks. The initial broad water gap leaves the far lever out of that ordinary reach. | Observation | Corroborated | High | W1 11:40–14:20, W2 18:40–19:50 and 22:40, P3. No exact jump range or water damage requirement is measured. |
| PY-003 | At the broad pool Pippit demonstrates a detached throw. The now-reached lever changes state and a bridge spans the water. The shot and the avatar’s subsequent crossing are separate actions. | Observation | Direct | High | W1 14:10–14:40 and W2 19:40–20:20 show the far lever before, the deployed pink bridge after and Pippit standing on it while the disk remains by the fixture. |
| PY-004 | The first demonstration precedes the named Offstring Throw unlock. It becomes an ordinary available action for later rooms. The conventional Switch input is ZR with Y. | Observation | Corroborated | High | W1 14:50 and W2 20:30 show the named grant. W2’s route description identifies the input; later independent W1 and W2 throws show reuse. Alternate and remapped commands were not verified. |
| PY-005 | The detached yo-yo can trigger remote tunnel switches during free play. Later bridge panels present different crossing layouts, letting the player connect successive dry ledges without walking on the water. | Observation | Direct | High | W1 15:50–16:20 and 17:40–17:50; W2 21:50–22:40. At 22:10 the disk crosses a gap, and the views at 22:20 and 22:30 distinguish narrower and extended pink bridge panels. |
| PY-006 | The final mandatory encounter shuts both passages. Successive enemies, including hammer carriers, must fall before the barriers release. Health and hazards are visible while moving and attacking. | Observation | Corroborated | High | W1 18:00–18:50, W2 25:00–26:20 show the active barriers, successive enemies and exit reopening. A single successful hit is insufficient. No fixed damage or enemy-spawn timing is asserted. |
| PY-007 | After the encounter the red trapdoor is reachable in the crate corridor. It leads to the Safe House, and both recordings show arrival there. | Observation | Direct | High | W1 18:50–19:10; W2 26:20–26:40 shows the entrance cue and Safe House, with a saving indication. A reload or future position is not inferred from that indication. |

## Basic data

- Release / origin: developed by Pocket Trap and published by PM Studios.
- Platform: `PLAT-NINTENDO-SWITCH`, original Nintendo Switch commercial
  eShop release. W1 reports a commercial v1.1 review copy on that system.
- Puzzle families: inventory and fixture dependencies (FAM-013), for a
  retained tool reaching its linked switch, and world topology and
  perspective (FAM-014), for authored edges joining previously separate
  walkable islands.
- P1: [Nintendo’s original Switch eShop listing](https://www.nintendo.com/us/store/products/pipistrello-and-the-cursed-yoyo-switch/).
  Confirms the full product, target platform and release date.
- P2: [PM Studios and Pocket Trap’s release announcement](https://www.gamespress.com/ja-JP/The-Worlds-First-Yoyovania-is-Here---Pipistrello-and-the-Cursed-Yoyo-i).
  Confirms commercial availability and distinguishes the original launch
  from the earlier Switch demo.
- P3: [Henrique Lorenzi’s developer interview](https://www.nintendolife.com/features/the-yoyo-was-special-finding-the-gba-magic-in-pipistrello-and-the-cursed-yoyo).
  Discusses bounded reach, diagonal geometry and route progression
  through known yo-yo tricks. This contextual material is not
  evidence for exact hit angles or motion timing.
- W1: [Handheld Players’ original Switch v1.1 capture](https://www.youtube.com/watch?v=mtTtt5f94Ds&t=597s),
  published 28 May 2025. Tunnels from 9:57, first bridge 14:10–14:40,
  named move grant 14:50, later bridge use, sealed fight 18:00–18:50,
  and Safe House at 19:09.
- W2: [8-Bit Walkthru’s Switch Abandoned Tunnels route](https://www.youtube.com/watch?v=aSupUPJaWwA&t=1180s),
  published 13 June 2025. Wide-pool lesson 19:40–20:30, later bridge
  panels 21:50–22:40, combat 25:00–26:20 and Safe House by 26:40.
  Its written description identifies the Switch buttons.
- R1: [Hey Poor Player’s firsthand commercial Switch review](https://www.heypoorplayer.com/2025/05/28/pipistrello-and-the-cursed-yoyo-review-switch/).
  Corroborates learned yo-yo techniques, differences between tools
  that open routes directly and later liquid travel, and the Switch
  launch year. It is not the source for the tunnel timecodes.

### Reproducible route evidence

1. From the first controllable tunnel room, follow the dry approach
   and jump between close solid ledges. Use the ordinary yo-yo
   against nearby threats or breakable obstructions. W1 12:20–12:40
   shows the hammer enemy and the route continuing after the fight.
   Stop before the wide pool rather than attempting water travel.
2. Approach the wider pool with the lever on the far dry bank.
   At W1 14:10 and W2 19:40 the water interrupts the dry route.
   The demonstration sends the yo-yo without its string. The
   lever changes and the pink bridge spans the gap. At W1 14:40
   or W2 20:20 Pippit stands on the bridge with the disk visible
   at the far end. The named ability notice follows at W1 14:50
   or W2 20:30.
3. Continue into the later water rooms. Hold ZR and press Y with
   a reachable switch aligned across the water. Observe the new
   bridge position before moving. In the two-ledge room W2 at
   22:10 has the released disk travelling horizontally while
   Pippit stands separately on his ledge. At 22:20 and 22:30
   the bridge configurations differ, and the player reaches a
   dry ledge on the opposite side.
4. Cross the last shown pink span into the orange-barrier room
   (W1 17:50–18:00). Defeat the required enemies. W2 at 25:40
   shows two hammer carriers while the room is still sealed; by
   26:10 the last such threat is gone and the exit is releasing.
5. Continue past the crates to the red trapdoor. W2's dialogue
   at 26:20 identifies that entrance, and 26:40 shows Pippit
   inside the Safe House. W1 records the same handoff at 19:09.
   End at that arrival.

These are recording timecodes, not time limits or recommended speeds.
Claim IDs: PY-001–PY-007.

## Mechanical decomposition

### Action Genes

- ACT-008: walk and jump through local dry geometry.
- ACT-161: aim and strike a reachable hostile or breakable object
  with the ordinary yo-yo.
- ACT-813: combine the ordinary throw and learned modifier for
  independent tool travel beyond normal tether reach.
- Claim IDs: PY-002–PY-006.

### System Behaviour Genes

- SYS-037: incidental coin or useful contact pickups are removed
  as the attempt continues.
- SYS-398: retain the named Offstring Throw after the authored
  demonstration so it can be used in later compatible rooms.
- SYS-1735: later strike-triggered bridge panels change the
  traversable layout between authored states.
- SYS-1805: a strike to the linked distant fixture deploys a
  crossing the player uses independently of the released disk.
- SYS-1806: a sealed encounter blocks both paths until the last
  required enemy is removed.
- Claim IDs: PY-002–PY-007.

### Constraint Genes

- CON-349: the live remote interaction needs the learned throw
  at the aligned switch. Merely approaching the water is insufficient.
- CON-854: ordinary movement and jumps need supporting dry feet
  at the intended destination; the wide pool needs a bridge.
- Claim IDs: PY-002–PY-005.

### Information Genes

- INF-179: the room view shows dry ledges, water, switches,
  changed bridge states and the enemies closing off the path.
- Claim IDs: PY-002–PY-007.

### Objective Genes

- OBJ-080: satisfy the route gates, clear the sealed fight and
  actually enter the Safe House by the trapdoor.
- Claim IDs: PY-003, PY-005–PY-007.

### Time Genes

- TIM-003: choose movement, attack and jumps during live hazards.
  Authored dialogue and instruction interrupts are separate moments.
- Claim IDs: PY-002, PY-005, PY-006.

## Reproducible transitions

| Before | Action | Resolution | What it establishes | Claim ID |
| --- | --- | --- | --- | --- |
| Close dry ledges with water between | Jump to the reachable supported tile | Land while retaining the ordinary tool | Not every water gap requires the new move | PY-002 |
| A wide pool cuts the route and the lever is beyond the tether | Complete the scripted detached throw demonstration | The hit changes the lever and extended panels form a bridge | The tool can cross the gap before the player | PY-003 |
| The first span is available | Walk across and continue the instruction | Retain the Offstring Throw shown by the reward notice | One demonstration becomes an ordinary capability | PY-003, PY-004 |
| A new bridge room has unreachable switch hardware | Align from a dry ledge and use the learned throw | The bridge changes layout and exposes a new legal foot path | A reusable switch action changes connectivity | PY-005 |
| The orange barriers are active during the fight | Keep moving and defeat the required occupants | The barrier stays until the encounter clears | One defeated enemy does not imply an exit | PY-006 |
| The barrier is released and the red trapdoor is accessible | Continue through the crate corridor and enter the marked trapdoor | Pippit appears inside the Safe House | The transition is settled at actual arrival | PY-007 |

## Strategic and experiential structure

A close dry ledge or nearby threat can be reached with existing
movement or the tethered tool. The first wider pool forces a
different operation. After the lesson, learn the current shape of
a switch room, stand on stable footing and send the detached disk
before choosing a walkable route. An open bridge does not clear
the later enemies. The last short arena requires timely movement
and attacks before the separate exit transition can happen.
Claim IDs: PY-002–PY-007.

## Replay and variation

The original Switch traces show the same authored gates at different
paces and with different movement and combat choices. The observed
health and collection values are not route requirements. The lesson
and Safe House arrival are the positive evidence at both boundaries.
No exact jump timing or tool maximum distance is derived from the
static samples.

## Adjacent systems and history

Walk-the-Dog provides a different liquid-traversal rule later in
the commercial campaign. The first Safe House also introduces
later city progression. Neither system is needed for the claimed
tunnel exit. Replays on Switch 2, other platforms and any demo
do not establish the exact original-release ruleset.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-161, ACT-813 | Navigate, strike nearby, or detach the tool for range |
| System Behaviour | SYS-037, SYS-398, SYS-1735, SYS-1805, SYS-1806 | Pickups, retained move, bridge layouts, linked fixture and encounter |
| Constraint | CON-349, CON-854 | Capability access and solid landing support |
| Information | INF-179 | Current threats, switches, routes and exit state |
| Objective | OBJ-080 | Open and traverse the route into the Safe House |
| Time | TIM-003 | Move and attack during live hazards |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `611` (`GAME-0001`–`GAME-0611`).
- Exact genome matches: none.
- Tied near matches: `GAME-0394` — LittleBigPlanet 2 (`6 / 20 = 0.300000`).
- Supported combination subsets: none.
- Scan date: 2026-11-21.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [LittleBigPlanet 2 (GAME-0394)](../g-l/littlebigplanet-2.md) | ACT-008, CON-349, INF-179, SYS-037, SYS-398, TIM-003 | Both move and jump across supported surfaces under continuous timing, with visible obstacles and linked level geometry. The Abandoned Tunnels use a newly detached disk to reach the switch through a water gap, then settle a mandatory fight before the trapdoor exit. LittleBigPlanet 2 trains traversal and object manipulation through its own authored platforming route. | Near, `0.300000` |

### Preserved research notes

- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_358](../../../research/taxonomy-changes/TAXONOMY_CHANGE_358.md)
  separates the learned detached throw, impact-opened crossing
  and mandatory room-clear seal.

## Negative results

- ACT-385 addresses throwing and actively recalling the same
  deployed implement. The evidence here distinguishes a modifier
  switching the ordinary tethered throw to a detached branch.
  Exact recall timing and any independent command are unmeasured.
- SYS-1743 pulls a target through an attached tether. This switch
  reacts to an impact by a released disk.
- SYS-934 materialises individually countable breakable crates.
  The encountered support is an authored bridge span.
- SYS-799 changes attack phase within a continuous sealed fight.
  The relevant final transition here is releasing the passage.
- Walk-the-Dog grants later liquid travel. No such travel explains
  the observed first bridge.

## Delta summary

## New facts

- [Observation | Direct | High] The first detached shot reaches
  the remote lever before Pippit crosses the water. PY-003.
- [Observation | Corroborated | High] The named grant follows the
  demonstration and the learned throw changes later bridge routes. PY-004, PY-005.
- [Observation | Direct | High] Clearing the mandatory encounter
  exposes a trapdoor whose actual exit is the Safe House. PY-006, PY-007.

## New genes

- [Observation | Corroborated | Medium] ACT-813, SYS-1805,
  SYS-1806 and CON-854.

## New combinations

- [Observation | Direct | High] No new combinations.

## Taxonomy changes

- [Observation | Corroborated | High] TAXONOMY_CHANGE_358.

## New questions

- How is the free disk’s allowed travel and return defined in
  a room with multiple eligible rebound surfaces?
- How does Walk-the-Dog handle entry and exit on exactly the
  same local gap from a later completed campaign state?
- How does the tunnel encounter recover after zero health on
  a specifically documented original Switch preset?

## Next recommended game

- [Hypothesis | Limited | Medium] `GAME-0613`, The Drifter,
  commercial Windows Steam release. Establish a complete opening
  escape with evidenced object use and a settled exit.

## Why this game

- [Hypothesis | Limited | Medium] Pipistrello opens a spatial
  path by learning a tool action. The next route can test the
  corresponding access boundary using object combination and
  authored adventure state.
