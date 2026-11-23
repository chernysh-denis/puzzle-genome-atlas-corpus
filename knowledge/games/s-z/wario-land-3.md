---
game_id: GAME-0645
slug: wario-land-3
game_title: Wario Land 3
analysis_status: reviewed
reviewed: 2026-11-22
combination_ids: []
gene_ids:
  action:
    - ACT-008
    - ACT-295
  system:
    - SYS-1863
    - SYS-1864
  constraint: []

  information:
    - INF-192
    - INF-599
  objective:
    - OBJ-347
  time:
    - TIM-003
---

# Game: Wario Land 3

This analysis uses the [canonical vocabulary](../../../docs/ARCHITECTURE.md#canonical-vocabulary).

## Analysis scope

- Version / ruleset: original North American Game Boy Color retail cartridge
  CGB-AW8A-USA, shared English/Japanese program CGB-AW8A-0, English selected.
  The cartridge and its label are documented separately from the play traces.
- Entry: a fresh Normal Game after the Temple introduction, with N1 Out of
  the Woods as the only available level on the North map.
- Primary decision loop: move through the forest and choose where to jump
  or attack. Collect the Gray Key on the raised route, take it into the
  next room and approach the Gray Chest from the ladder.
- Exit: open the chest, clear the visit with the Axe, see the removed tree
  and the new map choices N2 The Peaceful Village and N3 The Vast Plain,
  observe the automatic save and enter N2. The videos corroborate actual
  entry to each new node, with the N3 entry occurring after an N2 clear.
- Included: the first daylight forest route, local support and hazards,
  color-matched key and chest, clear result and both separate map unlocks.
- Excluded: later keys, chests and routes, other treasures, the day/night
  schedule and switch rules, forms and upgrades, golf and Time Attack,
  re-entry rules, cold reload tests, Nintendo 3DS and Switch reissues.
- Suggested later scope: from a fresh Axe clear, take N3 before N2, then
  reload the cartridge to check the map and the used chest independently.

## Direct-play status

No direct play was performed. A North American cartridge inspection documents
the label and program markings. Nintendo of America's original booklet shows
the matching key and chest, the clear, the Axe event and the save flow.
An English Game Boy Player capture and a second capture labelled NTSC
by its author show the complete route. The first author identifies
physical capture hardware. Neither footage provides the cartridge label
or a ROM checksum. The edition is established by the cartridge and official
booklet, with the behavior corroborated across both attributed captures.
Sampled frames were inspected in the background without audio. No physical
inputs, power cycle or original save file were inspected.

## Claim ledger

| ID | Claim | Status | Evidence | Confidence | Sources |
| --- | --- | --- | --- | --- | --- |
| WL-001 | The original North American Game Boy Color cartridge is CGB-AW8A-USA with documented CGB-AW8A-0 program markings. This packet uses the English opening. | Confirmed | Direct | High | P1 shows Nintendo's English North American booklet, P2 documents the physical label and ROM marking, P3 confirms Nintendo's Game Boy Color product. |
| WL-002 | At first the North map exposes N1 Out of the Woods as the only enterable level. The daylight N1 forest scrolls around the directly controlled character, with raised platforms, attackable blocks and live enemies. | Observation | Corroborated | High | P1 pp. 4–7 and 11. W1 3:10–3:45 and W2 2:50–3:37. |
| WL-003 | The Gray Key is collected by reaching its elevated forest ledge. The route drops back down, heads right through a doorway and climbs a ladder to the Gray Chest. The matching key authorizes opening by touching the chest. | Observation | Corroborated | High | P1 pp. 7–8 shows this specific key and chest, with the general match rule. W1 3:45–4:29 and W2 3:43–4:39 show the route and touch. Wrong-color and no-key runs were not sampled. |
| WL-004 | Opening the Gray Chest reveals the Axe and ends the visit. The clear screen shows the treasure and separately lists ordinary coins. The following musical-coin screen reads 1/8 in both traces. | Observation | Corroborated | High | P1 p. 8. W1 4:27–4:39 shows 26 ordinary coins and W2 4:38–4:51 shows 13. The coin readings describe these runs, not a required quota. |
| WL-005 | After the result, the Axe scene removes a tree from the North map. The reveal marks and names N2 The Peaceful Village and N3 The Vast Plain before the player chooses the next level. | Observation | Corroborated | High | P1 pp. 8–9 distinguishes the found treasure, event, changed map and autosave. W1 4:39–4:58 and W2 4:51–5:08 show the event and map markers. |
| WL-006 | The automatic save completes after the map reveal. The game resumes map selection and both recordings enter N2. Each later enters N3 after N2's result. | Observation | Corroborated | High | P1 pp. 7, 9 and 14. W1 4:56–5:08 and 6:45–7:03. W2 5:08–5:20 and 6:58–7:10. The footage does not isolate N3-first travel or power-off persistence. |

## Basic data

- Analysis target: `PLAT-GAME-BOY-COLOR`, original CGB-AW8A-USA cartridge.
- Publisher: Nintendo.
- Mechanical family: `FAM-013`, inventory and fixture dependencies.
- Checked: 2026-11-22.
- P1: [Nintendo of America original Wario Land 3 instruction booklet](https://www.videogamemanual.com/gbc/Wario%20Land%203%20%28USA%29.pdf),
  2000, printed pp. 4–9, 11 and 14. It illustrates the exact gray route
  alongside its general controls and progression.
- P2: [Comrade Claire's physical North American cartridge and PCB inventory](https://gbhwdb.gekkio.fi/cartridges/CGB-AW8A-0/comrade-claire-1.html),
  case stamp 22 and program chip CGB-AW8A-0.
- P3: [Nintendo's Wario Land 3 original-platform product entry](https://www.nintendo.com/en-gb/Games/Game-Boy-Color/Wario-Land-3-688167.html).
  The page also lists the later UK 3DS download and its date.
- W1: [WatchmeplayNintendo, Game Boy Player capture, Part 1](https://www.youtube.com/watch?v=xGLGeSqcIyw&t=220s).
  The creator describes direct GameCube Game Boy Player capture.
- W2: [LongplayArchive, English NTSC-labelled playthrough](https://www.youtube.com/watch?v=WPzqU2LGxJc&t=182s).
  The channel identifies the Game Boy Color NTSC release.

## Mechanical decomposition

### Action Genes

- ACT-008: move directly through the forest, jump between the ledges and
  climb the ladder into reach of the chest.
- ACT-295: commit Wario's attack while moving through the forest. An
  ordinary attack can break the eligible blocks on the stepped path.

### System Behaviour Genes

- SYS-1863: register the collected color key and open the matching
  chest on contact. Award the chest's treasure and end the current visit.
- SYS-1864: run the earned Axe event after the clear, remove the tree
  and make two new nodes selectable. The automatic save follows.

### Information Genes

- INF-192: the scrolling view exposes the current ledges, hazards,
  room exits and local geometry as the player moves.
- INF-599: the changed map highlights and names each newly available
  destination before normal node selection returns.

### Objective Genes

- OBJ-347: take the matching key to the chosen chest and settle
  its treasure. The first Gray Key is insufficient on its own.

### Time Genes

- TIM-003: move and attack as enemy positions and local hazards
  change in real time.

## Reproducible transitions

| State | Action or event | Result | Evidence |
| --- | --- | --- | --- |
| Fresh North map with N1 available | Move to N1 and confirm | Daylight Out of the Woods begins | WL-002 |
| Forest floor under staggered ledges | Jump upward, then touch the Gray Key | Key disappears from the ledge and unlock eligibility follows the player | WL-003 |
| Key registered, chest still unopened | Descend, travel right through the doorway, climb the next room's ladder and touch the Gray Chest | The chest opens and displays the Axe | WL-003, WL-004 |
| Axe revealed in the opened chest | Let the clear and musical-coin screens settle | The clear registers the Axe separately from the two coin counts | WL-004 |
| Axe settled after clear | Proceed through the event sequence | The map tree is removed and the two named level nodes are highlighted | WL-005 |
| Map changes shown and auto-save finishes | Select and enter N2 | Live movement in The Peaceful Village starts. Both captures later enter N3 too | WL-006 |

## Strategic and experiential structure

There are two local destinations. The first is the key on a high ledge,
while the visit ends at a separated chest across a room boundary.
Bending the platforming route around the key and then the ladder
determines which reward can be settled. The reward's overworld effect
then opens two distinct destinations.

## Replay and variation

The opening forest routes differ around enemies and the ordinary
coin total, settling 26 in W1 and 13 in W2. Both open the same chest,
receive the Axe and expose the same map choices. The coin total
varies independently of the successful result. No no-key replay,
wrong-color interaction or power cycle was attempted in scope.

## Adjacent systems and history

The original booklet describes further colored chests, changes to
previously visited levels, multi-treasure events and later control
of time of day. The opening Axe is a single-treasure event. The
two newly exposed nodes delimit the first progression step.

## Normalised genome

| Type | Stable genes | Role |
| --- | --- | --- |
| Action | ACT-008, ACT-295 | Traverse the forest and attack while within reach |
| System Behaviour | SYS-1863, SYS-1864 | Open a matched chest and apply its earned map event |
| Information | INF-192, INF-599 | Show local geometry and disclose both newly available nodes |
| Objective | OBJ-347 | Settle a selected color-matched treasure |
| Time | TIM-003 | Act while enemies and hazards remain live |

## Corpus comparison

- Comparison algorithm: `genome-jaccard-v1`.
- Prior game signatures scanned: `644` (`GAME-0001`–`GAME-0644`).
- Exact genome matches: none.
- Tied near matches: `GAME-0640` — Pizza Tower (`4 / 16 = 0.250000`).
- Supported combination subsets: none.
- Scan date: 2026-11-22.

### Selected-neighbour interpretation

| Neighbour | Shared genes | Decision-relevant differences | Match result |
| --- | --- | --- | --- |
| [Pizza Tower (GAME-0640)](../m-r/pizza-tower.md) | ACT-008, ACT-295, INF-192, TIM-003 | Both use directly controlled platform travel, a character attack and a scrolling live route. Pizza Tower changes the way back and starts an escape countdown at Pillar John. Wario Land 3 takes a matching key to a chest and expands the map after clear without a timed escape. | Near, `0.250000` |

## Taxonomy impact

Four additions distinguish the key-controlled local clear, the
reward-controlled map change, the explicit reveal of new nodes and the
treasure objective. Four reused definitions cover travel, character
attacks, local viewport and real-time play. SYS-063 covers a passage
barrier opened by a carried key. The Gray Chest ends the current visit
and awards its treasure instead. OBJ-120 ends at a retained new actor
capability, whereas the Axe changes the map. SYS-905 converts attempt
measures and starts a designated successor; the map still requires a choice.

## Negative results

- Merely reaching the Gray Key leaves the chest and visit unfinished.
- Ordinary coin totals differ across the two valid clears.
- No further Axe activation or equip action appears before the map event.
- The first chest leads back to map selection. N2 entry is separately
  chosen. N3 access is disclosed at the same reveal and entered later.
- No reload, N3-first route or other colored chest was tested in scope.

## Delta summary

Eight scoped genes, four new and four reused. The packet admits one
matching chest clear, its immediate map effect and live successor entry.

## New facts

- The same color links an independently placed key and reward chest.
- The Axe visibly settles before the map expands.
- Both new locations are named before normal map selection resumes.

## Principles and design implications

Place the key and the reward fixture on different legs of a local route.
Let the successful reward change reachable destinations and make those
destinations visible before asking for the next choice.

## Puzzle or game generation potential

Build a forest loop with a high key and a separated chest above a ladder.
On the first clear, use the earned item to clear one overworld obstruction,
then disclose two playable destinations.

## New genes

- SYS-1863
- SYS-1864
- INF-599
- OBJ-347

## New combinations

None. No verified combination has every required member in this signature.

## Taxonomy changes

[TAXONOMY_CHANGE_391](../../../research/taxonomy-changes/TAXONOMY_CHANGE_391.md).

## New questions

Can the player choose N3 first immediately after the Axe event, and
which map and chest states survive a verified cartridge reload?

## Next recommended game

Analyse the native PS5 commercial release of Cairn through the first
authored climbing objective and its observed result.

## Why this game

One short key route links player-controlled platforming to an observed
change in available destinations on the map.
