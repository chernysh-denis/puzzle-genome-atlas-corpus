---
game_id: GAME-0585
slug: into-the-radius
game_title: Into the Radius
analysis_status: reviewed
reviewed: 2026-11-20
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-161
    - ACT-341
    - ACT-787
    - ACT-788
  system:
    - SYS-045
    - SYS-210
    - SYS-215
    - SYS-578
    - SYS-1725
    - SYS-1726
    - SYS-1727
  constraint:
    - CON-136
  information:
    - INF-119
    - INF-130
    - INF-179
  objective:
    - OBJ-014
  time:
    - TIM-003
---

# Game: Into the Radius

Use the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
Use a hand-held map and loose supplies to reach the first contract object.
Carry it home to Vanno and submit it at the receiving terminal.

## Analysis scope

- Version / ruleset: English standalone Meta Quest 2 commercial base
  release of September 8, 2022, Meta product 5817243991680545.
  Use the Normal, tutorial-on solo rules for a fresh first expedition.
  This is a reproduction configuration. The launch recording does not
  independently identify the executable revision or all difficulty toggles.
- Structured analysis target: PLAT-META-QUEST, with Meta Quest 2 as the
  native headset. See [platform coverage](../../platforms/games.json).
- Entry: in Vanno after initial training and admission. At the mission
  terminal take the first Top Priority retrieval contract, called The
  First Expedition in the release recording. Carry ordinary starting
  gear and use the route from Vanno into Pervomay Route.
- Primary decision loop: arrange tools, loose supplies and space to
  carry the mission item. Read the map for the marked objective and
  return route. While moving around hostile bodies and anomalies, keep
  hands available for tools or combat. Pick up the Explorer Bracelet,
  a separate wristwatch-shaped prop in the blockhouse, and stow it.
  Return along the rope-marked path alive and bring the object to
  Vanno's mission receiver.
- Positive exit: place the watch in the mission tray and confirm
  completion at the terminal. The accepted hand-in grants a reward and
  the first security level. Acquiring the watch or crossing into Vanno
  alone does not complete the mission. Stop before follow-on training or
  accepting another contract.
- Negative exit: death aborts the current live outing. Returning
  without the target leaves the retrieval requirement open. Manual and
  automatic save options are documented for the release, but the
  exact dropped-item, reload and retry states were not verified.
- Included: base preparation for this contract, tracked item handling
  and magazine readiness, loose spatial backpack storage, traversing
  Pervomay with the map and wrist status display, optional response to
  the early ordinary Fragment, the physical watch, the return boundary
  and the distinct terminal hand-in.
- Excluded: PCVR including the earlier ruleset, Quest beta, modified
  runs, other headsets, later missions, later equipment, the capture's
  optional rift and artifact detour, trading, workshops, a complete
  Tide reset, exact light or damage values, and behavior across death or
  saves beyond ending the present outing.
- Potential scoped modules: Total Recall through film hand-in, or a
  controlled pre-/post-Tide artifact outing.
- Direct-play status: not conducted. CM Games and Meta identify the
  commercial carrier. Launch-day native Quest-labelled stills anchor
  the journey: field entry, the bracelet section, the dark return, tray
  and result. Written play observations confirm item and mission state.
  No executable, video playback or audio was used.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| IR-001 | The full English native Quest 2 base release was sold from September 8, 2022. | Confirmed | Direct | High | P1, P2, P3 |
| IR-002 | In the released Quest version, hands deal with separate items. An open backpack retains loose items by placement, and held magazine objects support manual readiness. Fixed body attachments are distinct from the loose pack. | Observation | Corroborated | High | W1, R1, R2, R3 |
| IR-003 | After accepting the first contract in Vanno, following the marked route out changes the active area to Pervomay Route. The held map exposes the objective area and return path, while its Tide display describes the next reset rather than a mission completion deadline. | Observation | Corroborated | High | W1, W2, R1, R3 |
| IR-004 | Moving, threats and the field clock advance together. The wrist device exposes condition separately from the item to be recovered. Attacks can harm the Explorer, and carried healing restores missing health. | Observation | Corroborated | Medium | P2, W1, R1, R3, R5 |
| IR-005 | An eligible dark Fragment can collapse into a distinct exposed core. An intact core can restore the hostile, while destroying it prevents that local recovery. Fighting every threat is unnecessary for the hand-in. | Observation | Corroborated | Medium | W1, W2, R3, R4 |
| IR-006 | The first contract requests a distinct watch-shaped mission prop at the marked blockhouse site. It can be grasped and kept in the pack without satisfying the mission yet. | Observation | Corroborated | High | W1, W2, R3 |
| IR-007 | Travelling back to Vanno with the watch preserves the carried prop and the active mission. The boundary itself gives no turn-in credit. | Observation | Corroborated | High | W1, W2, R3 |
| IR-008 | Place the requested watch in the mission terminal's delivery tray and confirm the completion. The payout and first security-level award follow acceptance. The ordinary sale receiver is separate. | Observation | Corroborated | High | W1, W2, R3 |

## Basic data

- CM Games, Meta Quest 2. The carrier is a native commercial Quest
  download. The scoped objective uses one fixed receiver. FAM-013
  covers the portable mission item, physical tray and terminal chain.
  FAM-009 captures the decision to spend combat time or preserve
  an escape path around moving threats.
- P1: [Meta product 5817243991680545](https://www.meta.com/experiences/into-the-radius/5817243991680545/).
  Official base-game listing with Quest 2 and September 8, 2022.
- P2: [CM Games' dated release announcement](https://www.gamespress.com/en-US/Into-the-Radius-is-officially-launching-on-Meta-Quest-2-today-Septembe).
  Separates commercial Quest release from its closed beta and the
  previous PC history, and documents the day and night cycle.
- P3: [CM Games producer's native-port retrospective](https://www.uploadvr.com/guest-post-how-cm-games-ported-into-the-radius-to-quest/).
  Confirms the September 2022 Quest build lineage. It does not bind
  individual mechanics to a binary hash.
- W1: [Substatica's September 8 Quest route](https://www.youtube.com/watch?v=lNlGE7rqvs8).
  The author labels this standalone, distinct from the linked beta
  playlist. Static frames at 1:20–2:40 show the hands, pack and
  tools. At 7:10–9:40 they show map use, base departure and area
  transition. At 10:30–13:10 they show Fragments, the blockhouse
  approach and the lit search. The author marks the Explorer
  Bracelet at 12:50. At 33:40–35:20 the route reaches Vanno and
  the first receiver. The watch sits in its tray at 35:00. The
  intervening artifact-area detour is beyond the scoped route.
- W2: [Orbb's first-story-mission capture](https://www.youtube.com/watch?v=R-6yw71v-88).
  June 2022, separately treated as other-carrier corroboration.
  Its chapter timestamps distinguish acceptance at 0:26, field
  entry at 1:00, the building at 1:50 and delivery at 2:36.
  These support the common route independently of the Quest
  capture. They do not establish native launch parity by themselves.
- R1: [Road to VR's September 2022 Quest 2 review](https://roadtovr.com/into-the-radius-quest-2-review/).
  First-hand release report on loose backpack placement, hand
  interactions, field threats and the Tide reset.
- R2: [UploadVR's September 2022 Quest hands-on review](https://www.uploadvr.com/into-the-radius-quest-2-review/).
  Distinguishes VR-held ammunition carriers, backpack organisation and
  manually taking tools from body-relative points.
- R3: [Reality Remake's Normal first-mission route](https://www.realityremake.com/articles/into-the-radius-walkthrough-and-guide-the-first-mission-equipment-retrieval).
  Its later English UI uses Equipment Retrieval. It shows the
  M1 map marker, watch location, optional fighting, return trail,
  separate delivery tray and resulting first security level. Its
  difficulty prescription does not establish native patch parity.
- R4: [Reality Remake's direct enemy observations](https://www.realityremake.com/articles/all-into-the-radius-vr-enemies-and-how-to-kill-them).
  The Fragment section distinguishes an exposed core from final
  removal and differentiates variants. Exact regeneration time is
  outside the verified native claim.
- R5: [The VR Grid's launch-era Quest 2 review](https://www.thevrgrid.com/into-the-radius/).
  Distinguishes interruption by death, manual saves and automatic
  saves. It does not settle a post-death inventory rule.
- Sources accessed 2026-11-20.

## Mechanical decomposition

### Action Genes

- ACT-008 steers the Explorer along the base-to-blockhouse route.
  ACT-341 addresses the base terminal to take and then settle the
  contract. ACT-787 manipulates portable items with tracked hands,
  including the mission watch, pack and tray transfers (IR-002,
  IR-003, IR-006–IR-008).
- ACT-788 readies a held tool using a separate handled magazine
  object. ACT-161 commits actual ranged or melee strikes during
  optional hostile encounters (IR-002, IR-005).

### System Behaviour Genes

- SYS-045 advances nearby autonomous hostiles, and SYS-215 resolves
  live combat. SYS-578 updates injury and compatible healing.
  SYS-1726 can restore a collapsed hostile from its surviving core
  (IR-004, IR-005).
- SYS-1725 retains loose items at their chosen locations in the pack.
  SYS-1727 carries the active load and pending mission across the
  base-field boundary. SYS-210 settles the selected turn-in into
  reward and security-level progression (IR-002, IR-006–IR-008).

### Constraint Genes

- CON-136 binds terminal completion to the accepted retrieval and
  the required object at the proper receiver (IR-006–IR-008).

### Information Genes

- INF-119 gives the Explorer's condition via the wrist instrument.
  INF-130 exposes region bearings and the next field reset on the
  map. INF-179 makes current geometry, visible threats and nearby
  fixtures inspectable without exposing all contents (IR-003,
  IR-004, IR-006).

### Objective Genes

- OBJ-014 requires a specific physical payload at Vanno's
  mission receiver and completion of its hand-in (IR-006–IR-008).

### Time Genes

- TIM-003 permits actions in a running world with mobile hostiles
  and changing light over the route (IR-003–IR-005).

## Reproducible transitions

| Initial state | Intervention | Discriminating result | Evidence |
| --- | --- | --- | --- |
| First mission available in Vanno | Accept it, prepare equipment and follow the rope-marked trail into the fog | Pervomay Route loads with current loadout. The map gives the active objective marker. | IR-002, IR-003 |
| Open loose backpack and reachable supplies | Move a prop into the pack, close it, travel and open it | It retains a chosen local place and can be taken out. A hand-ready magazine is a separable carried object. | IR-002 |
| Dark Fragment advances near the approach | Compare disengaging with continuing the fight after a core becomes visible | Leaving the core intact can let it restore the body. Destruction prevents that local recovery. Either outcome is independent of the terminal objective. | IR-004, IR-005 |
| Explorer reaches the blockhouse with a free hand | Grasp the watch-shaped bracelet and release it inside the backpack | Player custody changes. The first retrieval still awaits the receiver. | IR-006 |
| Watch in the pack while approaching the return trail | Cross back to Vanno and reopen the backpack | The item still exists in inventory and the contract has not settled. | IR-007 |
| Correct object carried while the terminal tray is open | Put it into the delivery tray and confirm at the terminal | The first retrieval settles with its reward and first security level. Returning alone or handing in irrelevant loot cannot produce this result. | IR-008 |

## Strategic and experiential structure

Taking extra gear makes hands and pack access more important under
pressure. The target is a small, physically retained possession.
Combat can buy time on a route, but committing to a second hit on a
Fragment core competes with the choice to keep moving. Once the watch
is acquired the central decision changes from searching to preserving
custody and getting home. Back at base there is still a separate
object-specific submission.

## Replay and variation

More optional searching changes the amount of carried clutter and
the return-light conditions. Short runs can avoid the capture's rift
and detector detour. The Tide is a visible world-reset horizon. A
reset, subsequent anomaly hunting or save/load comparison needs its
own controlled evidence.

## Adjacent systems and history

Quest 2 was a released native port of an established PC game. Later
store compatibility, PC or beta rules and the sequel do not identify
the exact executable from the release-day recording. Scope here ends
before the next training or contract, and leaves exact damage and
drop tables open.

## Normalised genome

| Type | Active gene IDs | Carrier parameters |
| --- | --- | --- |
| Action | ACT-008, ACT-161, ACT-341, ACT-787, ACT-788 | movement, attack, terminal choices, tracked grip and separate magazine |
| System Behaviour | SYS-045, SYS-210, SYS-215, SYS-578, SYS-1725, SYS-1726, SYS-1727 | live threats and health, recovery core, spatial pack, retained crossing and progression |
| Constraint | CON-136 | accepted mission and designated receiver with the correct object |
| Information | INF-119, INF-130, INF-179 | wrist status, map and field view |
| Objective | OBJ-014 | hand in the designated watch at Vanno |
| Time | TIM-003 | running threats and light alongside decisions |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `584` (`GAME-0001`–`GAME-0584`).
- Exact genome matches: none.
- Tied near matches: `GAME-0459` — Daxter (`9 / 27 = 0.333333`).
- Supported combination subsets: none.
- Scan date: 2026-11-20.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| Daxter (`GAME-0459`) | ACT-008, ACT-161, ACT-341, INF-119, INF-179, SYS-045, SYS-215, SYS-578, TIM-003 | Both assign a local job with live traversal, threats, readable health and a separate report. The hotel uses swatter combat and a local gem quota. The Quest outing requires keeping the unique spatial prop through the return and handing it to a physical receiver. | `9 / 27 = 0.333333` |

### Preserved research notes

- New genes: ACT-787, ACT-788, SYS-1725, SYS-1726 and SYS-1727.
- Classification result: New gene.

## Taxonomy impact

- [TAXONOMY_CHANGE_331](../../../research/taxonomy-changes/TAXONOMY_CHANGE_331.md)
  separates embodied manipulation, equipment readiness, portable
  placement, enemy recovery and travel before settlement.

## Negative results

- Reject SYS-222 for the ordinary mission pickup. The watch is grasped
  and placed rather than absorbed on avatar contact.
- Reject CON-210 as a whole-pack replacement rule. The operative
  spatial pack has no mandatory grid slots. Body attachments are
  a different interface.
- Reject SYS-349 and SYS-503 for the return walk. Neither the geometric
  crossing nor possession grants the mission reward.
- Reject CON-068 for the displayed Tide horizon. This unit ends with
  mission submission before any reset, and does not measure a
  mandatory terminal deadline.
- The named target watch is not the equipped condition display or a
  detector-revealed artifact. No exact health and drop coefficients,
  reload timings, task XP thresholds or guaranteed enemy count claimed.

## Delta summary

## New facts

- [Observation | Corroborated | High] The player keeps a specific loose
  item through area travel and physically submits it at a separate
  receiver. Field exit and mission settlement are distinguishable.

## New genes

- [Observation | Corroborated | Medium] Five additions in TAXONOMY_CHANGE_331.

## New combinations

- [Observation | Corroborated | High] No new verified combination
  proposed. Existing subsets are listed in the comparison.

## Taxonomy changes

- [Observation | Corroborated | Medium] Earlier definitions and
  signatures are retained.

## New questions

- Verify an aborted no-watch run followed by re-entry, death-state
  possessions and the pre-/post-Tide boundary directly on Quest 2.

## Next recommended game

- [Hypothesis | Limited | Medium] Selection 047 ends with this
  accepted unit. Choose a separate research horizon with the
  maintainer before recording another game.
- Optimisation criterion: finish parity across all nine native
  release targets before opening a new horizon.

## Why this game

- [Hypothesis | Limited | Medium] A complete early excursion
  distinguishes embodied possession, settlement and hazardous
  route choices without relying on a long campaign.
