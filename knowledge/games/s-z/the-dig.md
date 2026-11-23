---
game_id: GAME-0636
slug: the-dig
game_title: "The Dig"
analysis_status: reviewed
reviewed: 2026-11-22
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-087
    - ACT-089
    - ACT-847
  system:
    - SYS-112
    - SYS-1839
  constraint:
    - CON-136
  information:
    - INF-590
  objective:
    - OBJ-343
  time:
    - TIM-002
---

# Game: The Dig

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: original English North American LucasArts IBM PC
  CD-ROM of 1995, running under MS-DOS. The printed company-store
  product is 01-031. Two sources identify DOS execution in emulation.
  The exact disc pressing and binary revision of each capture are
  unverified.
- Primary decision loop: recover the kit from its container, locate
  the two assigned sites from the asteroid overview, match each
  inventory command to the prepared scene target, report both ready
  states via the crew communicator and check the reopened route.
- Entry: the first controllable asteroid exterior after the crew
  departs the shuttle and the Flying Pig is available as a container.
- Exit: the completed exterior assignment is reported to Borden,
  the authored sequence reveals the new fissure and the team visibly
  descends into the lit first interior scene.
- Included: the supply container, local navigation by labelled
  hotspots, accepted inventory operations, the two independent
  readiness states, the PenUltimate report and the observed
  expedition transition.
- Excluded: shuttle setup before arrival, the PenUltimate mini-game,
  later interior mechanisms, subsequent worlds, other OS releases
  and reissues, saved-game behaviour and exact binary parity. All
  item names and interactions below refer to the game interface.
- Suggested later scope: the independent interior plate sequence and
  its first completed mechanical outcome.

## Direct-play status

No direct play was performed. The LucasArts catalogue and archived
documentation identify the commercial PC disc, DOS launch and
ordinary inventory/communication interface. W1 labels its run PC
DOS on DOSBox Pure. W2 identifies DOSBox. These video tracks were
inspected as silent static frames. The 1995 first-hand walkthrough
corroborates the operation and its successor. No physical pressing
checksum, author input trace, audio or later port equivalence was tested.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| DIG-001 | LucasArts offered the original 1995 IBM PC CD-ROM as 01-031. Its contemporary documentation supplies a DOS launch and names Attila and the crew assignment. | Confirmed | Direct | High | P1 p. 26, P2 DOS start and P3 opening pages. P4 archives one English carrier. W1 and W2 identify emulated DOS execution. |
| DIG-002 | The exterior container supplies separately selected objects. An addressed target's label is visible, and selecting an inventory item places it on the cursor and previews the proposed Use command with the target. | Observation | Corroborated | High | P3 inventory interface. W1 9:06–9:26, 9:52–10:00 and 10:24–10:29. W2 about 8:58–9:19 and 17:35–17:40. |
| DIG-003 | The overview opens Quadrant 2. A compatible inventory operation changes its surface to the labelled Dirt target. Alpha is installed at that prepared site, with Brink assisting in the resulting scene. A separate item-to-object operation produces a visible ready indication. | Observation | Corroborated | High | W1 9:28–11:22, including the changed label near 10:17, the issued Alpha command near 10:28 and the independent readiness indication near 11:17. W2 17:33–17:40 and W3 opening walkthrough. |
| DIG-004 | The separately addressable Quadrant 3 has a blocking boulder. A different tool clears the site. Beta is placed at the exposed surface and reaches its ready state through the retained key already used on Alpha. | Observation | Corroborated | High | W1 11:36–14:43, including the changed scene around 12:54 and the second repeated key use near 14:35. W3 corroborates the pair of distinct sites. No interchangeable-site or ordering claim beyond the shown route. |
| DIG-005 | Back at the shuttle, Low opens the PenUltimate, selects Borden and submits the equipment status topic. Borden acknowledges both placed and ready objects, and the scene advances after the report. | Observation | Corroborated | High | P3 communicator and topic controls. W1 16:58–17:49, with selection and report at 17:20–17:34. W3 corroborates Borden and the topic. |
| DIG-006 | The authored sequence leaves a visible fissure in Attila. The crew arrives at the opening and then descends into the first lit interior. | Observation | Corroborated | High | W1 17:48–19:24 and 19:54–20:45. A labelled interior hotspot is visible around 21:20. W3 distinguishes the subsequent interior as a new section. Later plate and tunnel interactions are outside this packet. |

## Basic data

- Analysis target: `PLAT-DOS`.
- Developer and publisher: LucasArts Entertainment Company.
- Mechanical family: `FAM-013`, inventory and fixture dependencies.
- Checked: 2026-11-22.
- P1: [LucasArts Company Store catalogue, The Adventurer 11](https://www.mocagh.org/lucasfilm/adventurer11-alt.pdf), p. 26.
- P2: [LucasArts The Dig Reference Guide](https://mocagh.org/lucasfilm/digwl-refcard.pdf), DOS installation and package contents.
- P3: [LucasArts The Dig manual](https://www.mocagh.org/lucasfilm/dig-alt-manual.pdf), crew, inventory and PenUltimate.
- P4: [RetroTech Archive commercial CD-ROM and packaging](https://retrotecharchive.omeka.net/items/show/4).
- W1: [CRT Gems, PC DOS capture in DOSBox Pure](https://www.youtube.com/watch?v=TgjlQGi3EW8&t=543s).
- W2: [Squakenet, DOS PC capture in DOSBox](https://www.youtube.com/watch?v=gERUjzcFYmI&t=525s).
- W3: [Paul Greunke's November 1995 PC walkthrough](https://gamefaqs.gamespot.com/pc/9487-the-dig/faqs/2025), exterior and first interior headings.

## Mechanical decomposition

### Action Genes

- ACT-008: navigate Low via points in the scene and from the asteroid
  overview to the named quadrants and shuttle.
- ACT-087: select an inventory object and commit it to the matching
  world target in the appropriate state.
- ACT-089: take the individually addressed items from the Flying Pig
  into the inventory.
- ACT-847: select Borden's roster entry and the status icon within
  the PenUltimate conversation.

### System Behaviour Genes

- SYS-112: accepted item use changes the sites persistently so
  their dependent operations can address the exposed targets.
- SYS-1839: the report after both local preparations leads through
  the authored sequence into the newly accessible expedition scene.

### Constraint Genes

- CON-136: the local tool operations precede the matching placements,
  and the separate deployed states precede the shared report.

### Information Genes

- INF-590: read the pointer's current target label and the pending
  item-to-object command before clicking.

### Objective Genes

- OBJ-343: finish both distinct preparations, report the result and
  see the crew reach the newly accessible passage and enter it.

### Time Genes

- TIM-002: choose the next item, site and report at the player's pace.
  Local animations play when actions are committed.

## Reproducible transitions

| State | Input or event | Result | Evidence |
| --- | --- | --- | --- |
| The expedition is on Attila's exterior | Open the Flying Pig and select individual objects | The container empties and the objects become separately selectable in inventory | DIG-002 |
| The overview shows Quadrant 2 | Select the area and use the matching carried tool at its site | The subsequent addressed target is labelled Dirt, and Alpha can be placed there | DIG-003 |
| The Quadrant 3 site is obstructed | Resolve the compatible boulder operation, place Beta and use the retained key | The second world site reaches its local ready state | DIG-004 |
| Both sites are ready and the shuttle is addressed | Select Borden in PenUltimate and submit the relevant status topic | The acknowledged report leads into the authored scene transition | DIG-005 |
| The exterior sequence ends | The crew returns to the changed asteroid | The fissure is visible and the team descends into the first lit interior | DIG-006 |

## Strategic and experiential structure

The inventory cursor identifies a specific operand, and the visible
hotspot supplies a separate target. The operation changes the target
available for the next action. The two locations must be prepared
separately. A shared reporting step closes the exterior assignment
and the visible successor confirms progression beyond the inventory
or readiness display.

## Replay and variation

The two DOS records spend different lengths of time on the opening
conversations. Both show the collect, address and use interface for
the exterior kit. The accepted route does not measure every rejected
pair, a different order of visiting sites or replay across a save.

## Adjacent systems and history

The archived documentation describes the built-in handheld mini-game
and the separate PC and Macintosh offers. Those are outside the
mechanical packet, as are all interactions inside the first passage.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-087, ACT-089, ACT-847 | Navigate, use typed objects, collect the kit and address a report |
| System Behaviour | SYS-112, SYS-1839 | Expose the dependent sites and open the successor after reporting |
| Constraint | CON-136 | Require the prerequisite world states |
| Information | INF-590 | Read the hotspot and pending item-to-target command |
| Objective | OBJ-343 | Finish both local actions and reach the successor |
| Time | TIM-002 | Choose actions at the player's pace |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `635` (`GAME-0001`–`GAME-0635`).
- Exact genome matches: none.
- Tied near matches: `GAME-0613` — The Drifter (`5 / 16 = 0.312500`).
- Supported combination subsets: none.
- Scan date: 2026-11-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [The Drifter (GAME-0613)](the-drifter.md) | ACT-087, ACT-089, CON-136, SYS-112, TIM-002 | Both use player-paced pickups and compatible item applications to expose later interactions. The Drifter follows an ordered freight-car tool dependency and a hatch exit. The Dig prepares two separately addressed sites and resolves their common status through a remote contact before the next expedition scene. | Near, `0.312500` |

## Taxonomy impact

Four definitions cover the remote contact and topic operation, the
pending command display, the joint objective and the reported
transition. Existing navigation, acquisition, fixture use, persistent
preconditions, fixture activation and timing apply as written.

## Negative results

- Selecting an item or merely pointing at the target does not
  establish that the pending operation has been accepted.
- One site's ready state and a completed joint report are separate
  points in the observed route.
- The bounded packet ends with the verified first interior
  transition. It contains no claim about how to solve that area.

## Delta summary

Ten genes capture the first exterior packet. Four are new and
six are reused. Earlier definitions and game signatures are unchanged.

## New facts

- The site labels and item-to-target command expose both operands
  before an ordinary inventory interaction.
- Two different local changes precede the accepted common report.
- The subsequent scene shows actual access to the new fissure
  and the crew's transition to the interior.

## Principles and design implications

- Keep a pending command distinguishable from its accepted result.
- Give separate local tasks readable states before settling their
  combined outcome.
- Show the next explorable space after the common report.

## Puzzle or game generation potential

Prototype two work sites with disjoint preparation tools and one
shared reporting interface. The report should settle only after
both local states are ready and leave an explorable scene as proof.

## New genes

ACT-847, INF-590, OBJ-343 and SYS-1839.

## New combinations

None. No verified combination has every required member in this signature.

## Taxonomy changes

[TAXONOMY_CHANGE_382](../../../research/taxonomy-changes/TAXONOMY_CHANGE_382.md).

## New questions

Are the exterior sites interchangeable in visit order? Can any
independent completion fragment be reported before the joint state?

## Next recommended game

Analyse the Windows Steam commercial Tiny Glade wall-and-path
interaction through the observed arch creation and response to removal.

## Why this game

The exterior separates acquiring equipment, matching it to a
changing world state, and reporting the finished assignment.
