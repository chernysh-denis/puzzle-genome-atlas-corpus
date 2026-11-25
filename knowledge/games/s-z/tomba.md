---
game_id: GAME-0668
slug: tomba
game_title: "Tomba!"
analysis_status: reviewed
reviewed: 2026-11-23
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-341
    - ACT-889
    - ACT-890
  system:
    - SYS-1917
  constraint:
    - CON-883
  information:
    - INF-425
    - INF-614
  objective:
    - OBJ-026
  time: []
---

<!-- markdownlint-disable-next-line MD026 -->
# Game: Tomba!

This record uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).
The item, village, ledge, fog and numbered credit values are parameters.

## Analysis scope

- Version / ruleset: original English North American PlayStation retail
  disc, SCUS-94236 (1998), ordinary single-player New Game. No Special
  Edition, PSOne Classics wrapper, regional localisation, demo, rewind
  or externally modified rules.
- Structured analysis target: PLAT-PLAYSTATION in
  `knowledge/platforms/games.json`. W1 displays the English PlayStation
  release. W2 identifies its version as the July 16, 1998 NTSC release.
  The captures do not independently authenticate the disc medium,
  executable hash, hardware or controller inputs.
- Entry: regain movement at the village start beside the first
  building and the visiting adventurer. The fog route is still closed
  and the Furious Tornado has not been acquired.
- Primary decision loop: use the local clue and scenery to locate the
  mailbox, reach it by moving and jumping through the available
  depth transfer, then activate it. Carry the acquired Furious Tornado
  to the rooftop approach and release it through Use Item where the
  event item is eligible. Verify the clear and steer through the
  reopened route.
- Exit: Clear the Fog settles and the avatar can traverse into the
  Forest of All Beginnings. Stop after the first visible free movement
  inside the newly accessible forest, before another task settlement.
- Included: directed traversal and the background approach, opening
  clue and mailbox, event identification and resolution feedback,
  inventory release conditional on place, and ordinary movement
  through the reopened route.
- Excluded: optional pig and flower interactions visible in the traces,
  unrelated AP sources, weapon and damage rules, Save and Continue,
  subsequent quests, other fog sites, circuitous edge approaches and
  possible speedrun bypasses. AP spending and save persistence were
  not examined.
- Potential scoped modules: the Kokka chick recovery event, or Dwarf
  Language and its later dialogue access.

## Direct-play status

No personal installation, physical disc validation or play. The original
SCEA manual describes this exact event and separates finding the item
from using it at the fog. Two attributed retail play traces show the
required transitions. Their static video frames were inspected in the
background without audio. The exact activation volume and connected
controller input are unverified.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| TOM-001 | The scoped retail version is the English North American PlayStation Tomba!, SCUS-94236, released in 1998. | Observation | Corroborated | High | P1 front matter and regional notice, R1, W2 attribution |
| TOM-002 | The opening village has directed jumps and depth changes at eligible approaches. Opening the mailbox supplies the Furious Tornado as an event item. | Observation | Corroborated | High | P1 pp. 12–15, 22–23 and 25, W1 3:14–3:36, W2 4:55–5:05 |
| TOM-003 | The adventurer supplies a clue about removing the fog without naming the Furious Tornado. The event has a distinct discovery state. The traces display its discovery for 500 AP after the mailbox, and the manual illustrates the fog-first ordering. | Observation | Corroborated | High | P1 pp. 19, 22–23, W1 3:29–3:36 and 4:40–4:55, W2 4:21–4:44 and 4:58–5:05, R2 |
| TOM-004 | Use Item requires an authored eligible location to select an event item. At the fog ledge, confirm Furious Tornado from inventory to trigger its release without aiming at a separate fixture. | Observation | Corroborated | High | P1 pp. 18, 22–23, W2 5:31–5:38 |
| TOM-005 | The ordinary roof continuation is blocked by the fog before use. The released tornado removes the fog, making the forest route traversable. | Observation | Corroborated | High | P1 pp. 22–23, W1 5:18–6:12, W2 5:24–5:31 and 5:37–6:10 |
| TOM-006 | After the effect the game shows the named clear and 1,000 AP, returns normal movement and lets the player enter and move within the forest. | Observation | Corroborated | High | W1 5:55–6:05, W2 6:00–6:11, P1 p. 19, R2 |

## Basic data

- Release / origin: Whoopee Camp and Sony Computer Entertainment America,
  1998. North American PlayStation retail disc, SCUS-94236. One player.
- Family: FAM-013, a carried object from one authored scene changes route
  access where its separate destination rule admits use.
- P1: [North American SCEA instruction booklet](https://www.videogamemanual.com/ps1/Tomba%21%20%28USA%29.pdf).
  Use the printed page numbers. Pages 12–15 describe jump and depth
  control, pages 18–19 describe item use and event status, and
  pages 22–23 use this event to illustrate the clue, obstacle,
  mailbox, correct item use and completion.
- W1: [VICIOGAME PlayStation retail trace](https://www.youtube.com/watch?v=b1piEA5IEgs&t=159s).
  The creator identifies the 1998 PlayStation release. The capture
  shows English and obtains the item before the rooftop approach.
- W2: [LongplayArchive PlayStation NTSC trace](https://www.youtube.com/watch?v=Bc3vs73HfMo&t=156s).
  The attribution identifies the North American release date. This
  route visits the blocked roof before returning to the mailbox.
- R1: [Product release listing and disc identifier](https://gamefaqs.gamespot.com/ps/199051-tomba/data).
  It distinguishes SCUS-94236 from the 2012 digital distribution and
  the later Special Edition.
- R2: [Retail event table](https://tomba.club/wiki/Event_list).
  Lists the alternate discovery contacts, the eligible use area and
  the two Adventure Point awards. No demo-only rule was admitted.
- Claim IDs: TOM-001–TOM-006.

### Reproducible route evidence

1. Start with the first adventurer conversation and ordinary control
   in the Village of All Beginnings. The North American manual's
   solution first reaches the fog and then returns toward the mailbox.
   In W2, the adventurer explains the blocked way from 4:21, and the
   avatar approaches the opaque edge near 4:40.
2. Return left to the beginning. At the authored approach, hold Up and press Cross to
   jump toward the background hut or mailbox track. Open the
   mailbox and receive the Furious Tornado. W2 shows impact around
   4:57, then event cubes and 500 around 4:59. Around 3:30 W1 has
   already discovered the event before approaching the far roof.
   The traces show the ordering without showing every physical input.
3. Cross the village and climb the roof to the position abutting the
   fog. Even with the item, the fog remains an obstacle on arrival.
   The manual documents Use Item, selection of an eligible event item
   and confirmation with the Cross button. W2 shows the release
   acknowledgement around 5:37 at the roof edge.
4. Wait through the visible whirlwind. The forest emerges from the
   fog in W2 around 5:52–5:58. The event name returns near 6:01,
   followed by CLEAR and 1,000 near 6:04. Move right along the
   open route. Stop when ordinary movement is visible in the forest
   around 6:10. W1 independently shows the result and forest entry
   around 5:57–6:05.

## Mechanical decomposition

### Action Genes

- ACT-008: steer the persistent avatar left or right along the active
  track, approach the roof and move through the reopened way.
  TOM-002, TOM-005, TOM-006.
- ACT-341: use the reachable mailbox as a world interaction to
  obtain its authored contents. The manual and trace support mailbox
  activation by direct contact from a jump. TOM-002.
- ACT-889: use a directed jump to change traversal depth near the
  starting buildings and approach the mailbox. TOM-002.
- ACT-890: explicitly select and release the acquired event item
  from Use Item at the rooftop edge. TOM-004.

### System Behaviour Genes

- SYS-1917: the accepted use triggers a whirlwind that removes
  the ordinary traversal obstruction and opens the forest route.
  TOM-004–TOM-006.

### Constraint Genes

- CON-883: the item can be owned before the relevant location makes
  it selectable for use. Use eligibility depends on the current
  position. TOM-004.

### Information Genes

- INF-425: the adventurer or named event clue discloses the need to
  blow away the fog. The clue itself leaves the remedy unnamed. TOM-003.
- INF-614: discovery and completion are separately shown for the
  same named event. The manual describes the retained Events-screen
  entries, and the traces show the distinct awards. TOM-003, TOM-006.

### Objective Genes

- OBJ-026: reach ordinary traversal in the forest after connecting
  it to the avatar's current route by clearing the fog. TOM-005, TOM-006.

### Time Genes

No independent timing rule is required. The use gate is spatial.

## Reproducible transitions

| Starting condition | Decision | Observable transition | Evidence |
| --- | --- | --- | --- |
| The fog still blocks the roof | Investigate the obstacle before the mailbox | Clue and impassable roof are visible, with the remedy still elsewhere | P1, W2 4:21–4:44 |
| The mailbox on the other depth track is reached | Open the mailbox | Furious Tornado becomes available for the route and the discovery can credit 500 AP | P1, W1 3:14–3:36, W2 4:55–5:05 |
| Furious Tornado is held and the roof position is eligible | Confirm the event item in Use Item | Released whirlwind disperses fog | P1, W2 5:31–5:58 |
| The fog is gone | Observe the clear and move right | Named clear credits 1,000 AP and ordinary movement reaches the forest | W1 5:55–6:05, W2 6:00–6:11 |

## Strategic and experiential structure

The adventurer's hint gives the player a problem to solve and a place
to return. Wind-blown leaves around the mailbox suggest the remote
clue without making ordinary forward motion sufficient. Reaching the
separate depth track is part of acquiring the item. The site gate
creates a second decision: take the remedy back to the obstruction
before trying to select it for use. Separate event receipts prevent
the acquisition from looking like the successful clear.

## Replay and variation

The two traces approach the blocker and item in different order.
The manual supplies the excluded-location restriction for Use Item.
The traces show successful use, not a systematic sweep of its
positional boundary.

## Adjacent systems and history

The separate Event and Item screens preserve both a named lead and a
candidate tool. Optional discoveries can appear during the same village
traversal. They are independent of the route into the Forest of All
Beginnings and excluded from this genome.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-341, ACT-889, ACT-890 | Direct movement, mailbox interaction, depth transfer and item release |
| System Behaviour | SYS-1917 | Resolve the event item into an opened route |
| Constraint | CON-883 | Allow item selection at the authored use location |
| Information | INF-425, INF-614 | Clue and separate discovery/clear status |
| Objective | OBJ-026 | Reach ordinary movement through the reopened way |
| Time | None | No separate timing predicate admitted |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `667` (`GAME-0001`–`GAME-0667`).
- Exact genome matches: none.
- Tied near matches: `GAME-0440` — Scribblenauts (`3 / 15 = 0.200000`); `GAME-0615` — Skate Story (`3 / 15 = 0.200000`).
- Supported combination subsets: none.
- Scan date: 2026-11-23.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Scribblenauts (GAME-0440)](scribblenauts.md) | ACT-008, ACT-341, INF-425 | Both give a need without naming the remedy and let the avatar interact with the world. Scribblenauts composes a compatible noun, applies the spawned object to the addressed person and retrieves the revealed token. Tomba! obtains an authored item at one depth track and releases it from an eligible position to clear a route. | Near, `0.200000` |
| [Skate Story (GAME-0615)](skate-story.md) | ACT-008, ACT-341, OBJ-026 | Both use directed traversal and world interactions before crossing a newly accessible threshold. Skate Story settles four crests using timed supported Ollies to open its portal. Tomba! takes a specific event item to the fog and can select it there to open the route. | Near, `0.200000` |

## Taxonomy impact

Five boundaries isolate transfer by a depth jump, menu-based event
item release, location-gated item selection, discovery versus clear
feedback, and the rule that removes an obstruction after eligible use.
Four existing genes cover direct movement, mailbox interaction, an
unnamed-object clue and reaching a designated newly accessible area.

## Negative results

- Possession alone does not dispatch the tornado or reopen the route.
- The obstacle has a traversal consequence in the ordinary route.
  Fog colour and rendered thickness do not establish an independent
  visibility threshold or field of view rule.
- Point credits identify event transitions here. They are not input
  costs or currency requirements for release.
- No exact coordinates, alternate successful hit inputs, time limit,
  executable identity or across-save persistence were measured.

## Delta summary

Nine admitted genes, including four reuses and five additions.

## New facts

- A brief clue states the need independently of finding the remedy.
- Discovery and clear credit visibly distinct states of the same event.
- Eligibility to select the item for use depends on where the avatar stands.

## Principles and design implications

A visible obstruction and an unnamed remedy support a short search
with a readable return objective. Separate feedback for making progress
and completing the objective helps a player distinguish supply from use.

## Puzzle or game generation potential

Design one path with a visible obstruction, an independently
accessible source and an eligible application position. Allow the
source and obstruction to be found in either order while preserving
the need to reach the application position and traverse the result.

## New genes

- ACT-889
- ACT-890
- SYS-1917
- CON-883
- INF-614

## New combinations

None. All 274 verified combinations were checked as proper subsets.

## Taxonomy changes

[TAXONOMY_CHANGE_414](../../../research/taxonomy-changes/TAXONOMY_CHANGE_414.md).

## New questions

Which footprint and height make the Use Item entry selectable? Do other
authored event items present the same clue and settlement arrangement?
What aspects of the clear survive each save and reload boundary?

## Next recommended game

Wilmot Works It Out on macOS. Trace one picture through assembly and
its accepted completion.

## Why this game

This section exposes a complete authored route through clue, local
tool acquisition, spatially conditional use and a verifiable opening.
