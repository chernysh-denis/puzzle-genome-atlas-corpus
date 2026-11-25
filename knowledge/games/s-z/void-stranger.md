---
game_id: GAME-0693
slug: void-stranger
game_title: "Void Stranger"
analysis_status: reviewed
reviewed: 2026-11-24
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-162
    - ACT-912
  system:
    - SYS-1967
  constraint:
    - CON-001
    - CON-208
  information:
    - INF-001
  objective:
    - OBJ-164
  time:
    - TIM-002
---

# Game: Void Stranger

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The first rod room makes every placed square a trade for support
taken somewhere else.

## Analysis scope

- Version / ruleset: System Erasure's commercial English Windows
  Steam base game, app 2121980, originally released September 1,
  2023. Use the ordinary Gray route with the base Void Rod.
  The primary recorded menu shows version 1.1.0. Its exact Steam
  depot, executable and install provenance were not inspected.
  The second trace predates the 1.1.0 announcement.
- Structured analysis target: PLAT-WINDOWS-PC in
  [platform coverage](../../platforms/games.json).
- Entry: the initial, unvoided B002 room with Gray on the
  right bank and the rod still in the authored chest. The
  stairs on the left bank are separated by one empty column.
- Primary decision loop: open the chest, identify a spare
  reachable floor tile, lift it into the empty rod, walk
  along retained support and place it into the adjacent gap.
  Use the installed support to reach the stairs.
- Positive terminal: step onto the B002 stairs. Stop at the
  first controllable B003 state with the rod still present.
- Failure and restart: a step into unsupported space can
  cause a fall. The supplementary trace shows HP07 dropping
  to HP00 and a failure prompt without reaching B003.
  It later returns via a second route opening. No recovery
  stock threshold or automatic same-floor reset is inferred.
- Included: four-neighbour movement, fixed cells, visible
  ordinary tiles and holes, chest acquisition of the base rod,
  facing-directed removal and placement, the single held tile,
  the changed support and the early stair transition.
- Excluded: the previous mural, hidden brands, later chest and
  pickup economy, floor replay and reset internals, upgraded
  tools, alternate characters, alternate routes, editable HUD,
  special tiles and the rest of B003.
- Potential scoped module: compare the outcome of carrying a
  tile across different ordinary stair transitions on the same
  retail version, including which held values are retained.
- Direct-play status: no personal Windows session or binary
  inspection. W1 exposes the version and a successful route.
  W2 supplies a distinct successful choice and an earlier
  fall. Both were sampled as game frames in the background
  without audio. Input telemetry was unavailable.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- |
| VST-001 | System Erasure lists September 1, 2023 for the Windows Steam release. W1 shows version 1.1.0 in its settings, then enters B002 on the normal Gray route. | Confirmed | Corroborated | High | P1, P2, P3, W1 4:32–4:41 and 5:05–5:10 |
| VST-002 | On B002 the chest yields the base rod while the stair and one-column gap are visible. The tool icon appears after acquisition. | Observation | Corroborated | High | W1 5:07–5:35, W2 7:25–7:52, H1 |
| VST-003 | Gray uses the rod on a faced ordinary tile. The selected support disappears and the icon displays a held tile while the character moves away. The two recordings choose different donor positions. | Observation | Corroborated | High | W1 6:02–6:04, W2 15:04–15:08, H1, H2 |
| VST-004 | A held tile placed in the middle gap is traversable. The held marker clears, and the donor hole stays open. W1 moves M6 to E6; W2 moves F7 to E6. | Observation | Corroborated | High | W1 6:02–6:05, W2 15:04–15:12, H1 |
| VST-005 | The player crosses on the placed tile and takes the left stairs to B003 with the base rod still shown. W2 later experiments with other placements before departing through that stair. | Observation | Corroborated | High | W1 6:04–6:08, W2 15:09–15:12 and 15:25–15:31 |
| VST-006 | In W2's earlier attempt, walking off the upper footing while the rod is empty leads to HP00 and the fall prompt, without a staircase transition. | Observation | Direct | High | W2 7:57–8:07 |

## Basic data

- Release / origin: System Erasure, Windows Steam app 2121980,
  release September 1, 2023. English in both captures.
- Mechanical families: FAM-003 for bounded local state
  transformation; FAM-014 for the changed route connectivity.
- P1: [Windows Steam release](https://store.steampowered.com/app/2121980/Void_Stranger/).
  Identifies developer, publisher, platform, app and release.
- P2: [System Erasure press kit](https://se-made.com/press/sheet.php?p=void_stranger).
  Creator description and commercial availability.
- P3: [System Erasure version 1.1.0 announcement](https://store.steampowered.com/news/app/2121980/view/4167591962351328636).
  Identifies the released patch named by the W1 settings.
- W1: [DocFirebird's Normal-mode recording](https://www.youtube.com/watch?v=R7bHmSEIByc&t=307s).
  Settings near 4:32–4:41 display 1.1.0. Witness the B002 chest,
  right-edge donor and solved exit at 5:07–6:08. Earlier
  practice transfers inside B002 are separate from the exit.
- W2: [clockworksaint's unedited first-play recording](https://www.youtube.com/watch?v=75qPMRx39_o&t=904s).
  For acquisition and the failed first attempt see 7:25–8:07.
  The later attempt demonstrates the lower-left donor and
  passage at 15:04–15:12. Use 15:25–15:31 for the settled exit.
  The video predates the 1.1.0 release and does not identify
  its exact build.
- H1: [lunacent's PC floor account, B002](https://gamefaqs.gamespot.com/pc/401863-void-stranger/faqs/81299).
  Locates the chest, stairs and gap. Its coordinates label
  the three playable rows 5–7, with gap column E. Coordinates
  are a reference overlay for this record.
- H2: [Independent player account of the base rod](https://lunarcrawler.nekoweb.org/blogposts/games/2026-03-22-VOID-STRANGER.html).
  Describes holding one ordinary floor tile at a time. It
  supports the capacity interpretation alongside the observed HUD.
- Claim IDs: VST-001–VST-006.

### Reproducible fixture evidence

1. Begin on B002, approach the chest and interact from its
   immediate floor approach. Confirm the rod and the same
   uncovered gap. W1 5:07–5:35, W2 7:25–7:52.
2. Approach the right-edge donor M6 from its neighbouring
   support. Face M6 and use the empty rod. Around 6:02–6:03
   in W1, M6 becomes a hole and the held marker appears.
   W2 instead faces and lifts F7 around 15:04–15:07.
3. Move to solid F6, face west and use the held tile on E6.
   Around 6:04 in W1 and 15:07–15:09 in W2, E6 becomes
   solid, the slot clears and the donor remains empty.
4. Cross on E6, continue to the left bank and descend C7.
   W1 shows the supported crossing and B003 by 6:08.
   W2 tests further reversible placements, then takes the
   same stairs and reaches B003 around 15:29–15:31.
5. For the failure boundary, compare W2 7:57–8:07: a step
   into an empty top-edge cell ends movement on B002 without
   entering its ordinary successor.

## Mechanical decomposition

### Action Genes

- ACT-008: walk one cardinal cell at a time through the accessible
  area and navigate onto the newly placed tile. VST-002–VST-005.
- ACT-162: place the already held tile in the faced reachable
  empty position. VST-004.
- ACT-912: use the empty rod to lift a selected adjacent ordinary
  tile for later placement. VST-003.

### System Behaviour Genes

- SYS-1967: removal and placement conserve one ordinary floor
  unit through the rod and change which cells provide footing.
  VST-003–VST-005.

### Constraint Genes

- CON-001: cell addresses stay fixed while their floor state
  changes between ordinary tile and uncovered void. VST-002–VST-004.
- CON-208: the placement must address a reachable, compatible
  empty position. W1 and W2 populate the faced gap from its edge.
  VST-003–VST-004.

### Information Genes

- INF-001: the bounded room shows the walkable cells, holes,
  stairs and tool status required for the crossing. The
  initial rod chest is the authored entry action. VST-002–VST-005.

### Objective Genes

- OBJ-164: enter the prescribed stairs and arrive at the next
  floor with the rod retained. VST-005.

### Time Genes

- TIM-002: choose movement and tool actions in sequence at
  the player's pace. B002 has no pressure clock or autonomous
  hostile acting while the player waits. VST-002–VST-005.

## Reproducible transitions

| From | Input or event | To | Evidence |
| --- | --- | --- | --- |
| B002 right bank, tool absent | Interact with the rod chest | Base rod is available; the gap stays empty | VST-002 |
| Empty rod and faced M6 in W1, or F7 in W2 | Lift the ordinary tile | Donor becomes a hole, tool hold becomes full | VST-003 |
| Facing E6 from supported F6 with one tile held | Place the tile | E6 is traversable, hold is empty and donor stays open | VST-004 |
| Newly connected banks | Walk across E6 and onto stair C7 | B003 starts with the same base rod | VST-005 |
| Supported at an unfilled edge | Step off ordinary footing | Fall and failed B002 attempt in W2 | VST-006 |

## Strategic and experiential structure

The gap itself can be filled with several donors. Taking
a square needed for the approach would subtract support from
the route to the recipient. Choosing a spare tile preserves
the path to the gap and the path across it.

## Replay and variation

The two runs demonstrate different donor locations for E6.
The first witness uses a more distant right-edge tile and
the second takes one near the lower edge of the gap. Both
use the same active stairs.

## Adjacent systems and history

The game later introduces more tile states, different moves
and alternate routes. This first floor uses a base rod and
one ordinary bridge tile. None of the deeper mechanics is
needed to settle the fixture.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-162, ACT-912 | Navigate, place held support and lift one native tile |
| System Behaviour | SYS-1967 | Transfer one unit between support states through the hold |
| Constraint | CON-001, CON-208 | Fixed cells and local valid placement |
| Information | INF-001 | Visible room geometry and tool state |
| Objective | OBJ-164 | Descend the stair into the next floor |
| Time | TIM-002 | Advance at the player's pace |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `692` (`GAME-0001`–`GAME-0692`).
- Exact genome matches: none.
- Tied near matches: `GAME-0006` — Sokoban (`4 / 14 = 0.285714`).
- Supported combination subsets: none.
- Scan date: 2026-11-24.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Sokoban (GAME-0006)](sokoban.md) | ACT-008, CON-001, INF-001, TIM-002 | Both give the player a fixed, legible grid and time to plan a route. Sokoban pushes crates on existing floor to designated goals. Void Stranger removes a unit of support, seats it elsewhere and walks on it to reach a stair. | Near, `0.285714` |

## Taxonomy impact

Retain existing held-tile placement. Isolate the pickup of
authored floor support and the conserved one-tile transfer
from old footing to the hole the player intends to cross.

## Negative results

- Receiving the rod does not itself fill the gap or reach the stair.
- The donor remains empty after the recipient becomes walkable.
- The first floor does not require an enemy, a specific donor
  tile, a collectible quota or a separate exit interaction.
- The comparison stops on entry to B003.

## Delta summary

Nine genes, with new boundaries for lifting native support
and obtaining renewed support from the same carried unit.

## New facts

- The empty and loaded rod states display different marks.
- M6 and F7 can independently supply the same crossing at E6.
- The ordinary stair advances the floor and preserves the rod.

## Principles and design implications

A limited relocation tool makes the origin as important as the
destination. One compatible destination can have several safe
donors, even within a small authored room.

## Puzzle or game generation potential

Design an original board with two banks, limited stepping
stones and a one-slot tool. Test which donors leave the
actor connected to the receiving gap and the exit.

## New genes

- ACT-912
- SYS-1967

## New combinations

None of the 274 verified combinations is a proper subset.

## Taxonomy changes

[Taxonomy Change 439](../../../research/taxonomy-changes/TAXONOMY_CHANGE_439.md).

## New questions

- Which ordinary falls return to the same floor when recovery
  stock is present on this release?
- When does an ordinary stair retain or clear a tile in the rod?

## Next recommended game

The ninth scoped unit closes Selection 059. The next horizon
requires its own recorded mixed-platform selection.

## Why this game

The rod makes a small crossing depend on preserving access
while moving a finite unit of the level itself.
